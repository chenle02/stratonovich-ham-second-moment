#!/usr/bin/env python3
"""Token and cost totals for the AI work on this repository, from local logs.

Reads (read-only) three local stores on the worker machine and writes
aggregate totals only (no paths, prompts or message text) to
token-totals.json beside this script:

1. Codex sessions (the GPT-family worker): every rollout JSONL under
   CODEX_SESSIONS whose first recorded working directory is this repository
   (or a subfolder) or one of its review workspaces (see ours()).
   Per session, the last cumulative `total_token_usage` is taken; the model is
   the last model named in the session's turn contexts.
2. Claude Code project logs: JSONL files under ~/.claude/projects/ for this
   repository, its subfolders and its review workspaces (ours_claude_dir()). Assistant messages are deduplicated by
   (message id, request id); usage fields are summed.
3. OpenCode (DeepSeek and other providers): opencode.db, opened read-only;
   sessions whose directory passes ours(); assistant message
   tokens and cost summed per provider/model.

Usage: python3 token_totals.py [REPO_NAME]
Environment: CODEX_SESSIONS (default ~/.codex/sessions; set it if your Codex
home differs),
OPENCODE_DB (default ~/.local/share/opencode/opencode.db).
"""
import collections
import glob
import json
import os
import sqlite3
import re
import sys

REPO = sys.argv[1] if len(sys.argv) > 1 else "Article-Stratonovich-HAM-Second-Moment"
HERE = os.path.dirname(os.path.abspath(__file__))
CODEX = os.path.expanduser(os.environ.get("CODEX_SESSIONS", "~/.codex/sessions"))
OPENCODE = os.path.expanduser(os.environ.get("OPENCODE_DB", "~/.local/share/opencode/opencode.db"))


def ours(path):
    """True for this repository (and its subfolders) or its review workspaces.

    Review workspaces live under ~/.local/state/Le-AI-Lab/stratonovich-* or
    ~/.local/state/tmp/stratonovich-*. The separate Lean-companion and video
    projects are not counted.
    """
    low = path.lower()
    if REPO.lower() in low:
        return True
    return re.search(r"/\.local/state/(le-ai-lab|tmp)/stratonovich-", low) is not None


def ours_claude_dir(name):
    """Same rule for Claude project folder names (slashes become dashes)."""
    low = name.lower()
    if REPO.lower() in low:
        return True
    return re.search(r"-local-state-(le-ai-lab|tmp)-stratonovich-", low) is not None


def codex():
    sessions = []
    for f in glob.glob(os.path.join(CODEX, "**", "*.jsonl"), recursive=True):
        cwd = None
        model = None
        usage = None
        first = last = None
        with open(f, errors="ignore") as fh:
            for line in fh:
                try:
                    d = json.loads(line)
                except ValueError:
                    continue
                ts = d.get("timestamp")
                if ts:
                    first = first or ts
                    last = ts
                p = d.get("payload") if isinstance(d.get("payload"), dict) else {}
                if d.get("type") in ("session_meta", "turn_context") and cwd is None and p.get("cwd"):
                    cwd = p["cwd"]
                if d.get("type") == "turn_context" and p.get("model"):
                    model = p["model"]
                if d.get("type") == "event_msg" and p.get("type") == "token_count":
                    info = p.get("info") or {}
                    if info.get("total_token_usage"):
                        usage = info["total_token_usage"]
        if cwd and ours(cwd) and usage:
            sessions.append((model or "unknown", usage, first, last))
    tot = collections.Counter()
    by_model = collections.Counter()
    for model, u, _, _ in sessions:
        by_model[model] += 1
        for k in ("input_tokens", "cached_input_tokens", "output_tokens",
                  "reasoning_output_tokens", "total_tokens"):
            tot[k] += int(u.get(k) or 0)
    dates = sorted(s[2] for s in sessions if s[2]) + sorted(s[3] for s in sessions if s[3])
    return {"sessions": len(sessions), "sessions_by_last_model": dict(by_model),
            "tokens": dict(tot), "first": min(dates) if dates else None,
            "last": max(dates) if dates else None}


def claude():
    seen = set()
    tot = collections.Counter()
    models = collections.Counter()
    for d in glob.glob(os.path.expanduser("~/.claude/projects/*")):
        if not ours_claude_dir(os.path.basename(d)):
            continue
        for f in glob.glob(os.path.join(d, "**", "*.jsonl"), recursive=True):
            with open(f, errors="ignore") as fh:
                for line in fh:
                    try:
                        e = json.loads(line)
                    except ValueError:
                        continue
                    m = e.get("message") if isinstance(e.get("message"), dict) else None
                    if not m or m.get("role") != "assistant" or not isinstance(m.get("usage"), dict):
                        continue
                    key = (m.get("id"), e.get("requestId"))
                    if key in seen:
                        continue
                    seen.add(key)
                    models[m.get("model", "unknown")] += 1
                    u = m["usage"]
                    for k in ("input_tokens", "output_tokens",
                              "cache_creation_input_tokens", "cache_read_input_tokens"):
                        tot[k] += int(u.get(k) or 0)
    return {"api_calls": len(seen), "calls_by_model": dict(models), "tokens": dict(tot)}


def opencode():
    if not os.path.exists(OPENCODE):
        return None
    c = sqlite3.connect(f"file:{OPENCODE}?mode=ro", uri=True)
    sess = {r[0] for r in c.execute("select id, directory from session") if ours(r[1])}
    out = collections.defaultdict(collections.Counter)
    for (sid, data) in c.execute("select session_id, data from message"):
        if sid not in sess:
            continue
        try:
            d = json.loads(data)
        except ValueError:
            continue
        if d.get("role") != "assistant":
            continue
        key = f"{d.get('providerID', '?')}/{d.get('modelID', '?')}"
        t = d.get("tokens") or {}
        cache = t.get("cache") or {}
        o = out[key]
        o["messages"] += 1
        o["input"] += int(t.get("input") or 0)
        o["output"] += int(t.get("output") or 0)
        o["reasoning"] += int(t.get("reasoning") or 0)
        o["cache_read"] += int(cache.get("read") or 0)
        o["cache_write"] += int(cache.get("write") or 0)
        o["cost_usd_micro"] += int(round(float(d.get("cost") or 0) * 1e6))
    res = {k: dict(v) for k, v in out.items()}
    for v in res.values():
        v["cost_usd"] = round(v.pop("cost_usd_micro") / 1e6, 2)
    return {"sessions": len(sess), "by_model": res}


if __name__ == "__main__":
    snap = {"repository": REPO, "codex_worker": codex(), "claude_code": claude(),
            "opencode": opencode(),
            "note": "Local logs of the worker machine only; subscription use has no dollar cost.",
            "snapshot_utc": __import__("datetime").datetime.now(
                __import__("datetime").timezone.utc).strftime("%Y-%m-%dT%H:%MZ")}
    # TOKEN_TOTALS_OUT names another file beside this script, so that a later
    # snapshot can be recorded without overwriting an earlier one.
    out_name = os.path.basename(os.environ.get("TOKEN_TOTALS_OUT", "token-totals.json"))
    with open(os.path.join(HERE, out_name), "w") as fh:
        json.dump(snap, fh, indent=2, sort_keys=True)
        fh.write("\n")
    print(json.dumps(snap, indent=2, sort_keys=True))
