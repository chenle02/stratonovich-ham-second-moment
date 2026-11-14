#!/usr/bin/env python3
"""Generate ai-statistics-data.tex for the AI-statistics appendix draft.

Every number printed in ai-statistics.tex comes from this file's output.
Inputs (all committed beside this script, or the repository's git history):

  reviews/runs.tsv           one row per review run (count_reviews.py)
  reviews/review-stats.json  run aggregates and follow-ups (count_reviews.py)
  tokens/token-totals.json  token and cost totals (token_totals.py)
  milestones.json            project milestones (tag, dates, commit, label, source)
  no-go/nogo-counts.json     kind and status of each no-go record (the full
                             ledger is held back; see no-go/README.md)
  git log                    commits per day, first and last date; recorded in
                             commits-per-day.json for use where the counted
                             commit id does not exist (the filtered public repo)

Usage (from the repository root):
  python3 scripts/ai-statistics/make_appendix.py
Writes notes/ai-statistics-data.tex (used by the book and the standalone draft).
"""
import collections
import csv
import datetime as dt
import json
import os
import subprocess

HERE = os.path.dirname(os.path.abspath(__file__))
FAMILIES = ["Claude", "DeepSeek", "Kimi", "GPT/Codex"]
FAM_TEX = {"Claude": "Claude (Opus 5.5)", "DeepSeek": "DeepSeek V4 Pro",
           "Kimi": "Kimi K3", "GPT/Codex": "GPT (Codex)"}
FAM_COLOR = {"Claude": "aiClaude", "DeepSeek": "aiDeepSeek",
             "Kimi": "aiKimi", "GPT/Codex": "aiGPT"}


def load():
    runs = list(csv.DictReader(open(os.path.join(HERE, "reviews", "runs.tsv")),
                               delimiter="\t"))
    stats = json.load(open(os.path.join(HERE, "reviews", "review-stats.json")))
    usage = json.load(open(os.path.join(HERE, "tokens", "token-totals.json")))
    nogo = json.load(open(os.path.join(HERE, "no-go", "nogo-counts.json")))
    milestones = json.load(open(os.path.join(HERE, "milestones.json")))["milestones"]
    return runs, stats, usage, nogo, milestones


COMMITS_FILE = os.path.join(HERE, "commits-per-day.json")


def git_commits(until):
    """Commits per UTC day up to the counted commit.

    In the working repository the counted commit exists: count from git and
    record the result in commits-per-day.json. In the public repository the
    history filter has rewritten every commit id (and dropped commits that
    touched only private files), so the recorded counts are used instead.
    """
    env = dict(os.environ, TZ="UTC")  # same day boundary as the review runs
    known = subprocess.run(["git", "cat-file", "-e", until + "^{commit}"],
                           capture_output=True).returncode == 0
    if known:
        out = subprocess.run(["git", "log", "--format=%ad", "--date=format-local:%Y-%m-%d", until],
                             capture_output=True, text=True, check=True, env=env).stdout.split()
        counts = collections.Counter(out)
        with open(COMMITS_FILE, "w") as fh:
            json.dump({"counted_commit": until, "time_zone": "UTC",
                       "total": sum(counts.values()), "per_day": dict(sorted(counts.items()))},
                      fh, indent=2)
            fh.write("\n")
        return counts
    rec = json.load(open(COMMITS_FILE))
    if rec["counted_commit"] != until:
        raise SystemExit(f"commits-per-day.json records {rec['counted_commit'][:7]}, "
                         f"but the review counts were made at {until[:7]}")
    return collections.Counter(rec["per_day"])


def fmt_int(n):
    return f"{n:,}".replace(",", "{,}")


def fmt_m(n, digits=1):
    """Millions, as text."""
    return f"{n / 1e6:.{digits}f}"


def fmt_b(n, digits=2):
    """Billions, as text."""
    return f"{n / 1e9:.{digits}f}"


def macro(name, value):
    return f"\\newcommand{{\\{name}}}{{{value}}}\n"



# ---- The publication closeout reviews (public experiment ledger) ----------
# The ledger is the public, bounded record of the closeout reviews (its own
# `coverage` line says what it covers). It is counted as it stands: no figure
# is estimated or recomputed, and a missing value stays missing. The file is
# chosen explicitly (here, or with --ledger), never as "the newest on disk",
# and must be committed and unmodified: the appendix names it with its commit
# and blob (ledger owner, 2026-11-14). The book build stops if it is absent.
ROOT = os.path.abspath(os.path.join(HERE, "..", ".."))
LEDGER_DEFAULT = "experiment/ledger-updates/2026-11-14-c003-provenance/run-ledger-v4.json"
OUTCOMES = ["accepted-at-scope", "not-accepted", "invalid", "refused",
            "recovered", "preflight", "continuation", "timeout"]
PENDING = "running"   # display class: a review still running (no verdict yet)
OUTCOME_TEX = {"accepted-at-scope": "Accepted at the stated scope",
               "not-accepted": "Not accepted", "invalid": "Invalid report",
               "refused": "Recovery refused", "recovered": "Recovered",
               "preflight": "Preflight (no call)",
               "continuation": "Continuation (no new vote)",
               "timeout": "Timed out",
               PENDING: "Still running (no verdict yet)"}
CLOSEOUT_FAMILY = [("deepseek", "DeepSeek"), ("kimi", "Kimi"), ("k3", "Kimi"),
                   ("qwen", "Qwen"), ("claude", "Claude"), ("gpt", "GPT")]


NO_CALL, UNRECORDED = "no model call", "model not recorded"


def closeout_model(row):
    """The actual model as recorded, without a provider prefix ("deepseek/"),
    so one model reached through two routes is one column. A record with no
    actual model is "no model call" when it records zero provider calls, and
    "model not recorded" otherwise (it ran, but the ledger leaves the model
    out); its tokens and costs are still counted in that column."""
    m = row.get("actual_model")
    if m:
        return m.split("/")[-1]
    return NO_CALL if row.get("provider_calls") == 0 else UNRECORDED


def closeout_family(model):
    for key, fam in CLOSEOUT_FAMILY:
        if model and key in model.lower():
            return fam
    return "other"


def tex_tt(s):
    return "\\texttt{" + s.replace("_", "\\_").replace("-", "-{}") + "}"


# Records that are not additional provider usage: their telemetry, if any, is
# not added to the token and cost sums (ledger owner, 2026-11-14). A format
# continuation counts only if the ledger marks its usage as not overlapping
# the original's (USAGE_NONOVERLAP_FIELD true).
NOT_USAGE_KINDS = {"derived_recovery", "parser_refusal", "preflight", "audit_addendum"}
CONTINUATION_KIND = "format_continuation"
USAGE_NONOVERLAP_FIELD = "usage_nonoverlap_verified"


def counts_as_usage(row):
    kind = row.get("record_kind")
    if kind in NOT_USAGE_KINDS or row.get("provider_calls") == 0:
        return False
    if row.get("aggregation_eligible") is not True:   # v3: an original provider
        return False                                   # attempt with reported usage
    if kind == CONTINUATION_KIND:
        return row.get(USAGE_NONOVERLAP_FIELD) is True
    return True


def ledger_source(rel):
    """Commit and blob of a committed, unmodified ledger file."""
    git = lambda *a: subprocess.run(["git", "-C", ROOT, *a], capture_output=True, text=True)
    if not os.path.exists(os.path.join(ROOT, rel)):
        raise SystemExit(f"{rel} is missing: the closeout subsection is generated from it")
    if git("ls-files", "--error-unmatch", rel).returncode or git("diff", "--quiet", "HEAD", "--", rel).returncode:
        raise SystemExit(f"{rel} is not committed or has local changes; use a committed ledger")
    commit = git("log", "-1", "--format=%h", "--", rel).stdout.strip()
    blob = git("rev-parse", "--short", f"HEAD:{rel}").stdout.strip()
    return commit, blob


def tex_path(s):
    """A long literal (format signature, path) that may break at punctuation."""
    return "\\path{" + s + "}"


WHOLE_BOOK = "WHOLE_BOOK_ACCEPTED"   # field name as in the ledger and its schema


def check_no_whole_book(rows):
    """Refuse a ledger in which any row could accept the whole book.

    The appendix says that no record accepts the whole book. The schema makes
    WHOLE_BOOK_ACCEPTED required and constant false, so a row without the field,
    or with any value other than false, is refused. (An earlier version read a
    lower-case key that the ledger does not have, so it could never fire.)
    """
    missing = [r.get("id") for r in rows if WHOLE_BOOK not in r]
    if missing:
        raise SystemExit(f"ledger rows without {WHOLE_BOOK}: {missing[:5]}")
    accepting = [r.get("id") for r in rows if r[WHOLE_BOOK] is not False]
    if accepting:
        raise SystemExit(f"ledger rows with {WHOLE_BOOK} not false: {accepting[:5]}; "
                         "the appendix text says no record accepts the whole book")


def header_note(rows, letter):
    """Sentence on the records whose counts cover only the panel header/final step.

    Their ledger accounting_scope says so; the sentence names how many there are and
    their format letters. Empty when there are none, so the caveat disappears rather
    than leaving a dangling phrase. It starts with a space: the prose puts it straight
    after a full stop.
    """
    hdr = [r for r in rows if "header/final-step" in (r.get("accounting_scope") or "")]
    if not hdr:
        return ""
    ls = sorted({letter[r["token_format_signature"]] for r in hdr})
    fmt = ("format~" + ls[0]) if len(ls) == 1 else \
        ("formats~" + ", ".join(ls[:-1]) + " and~" + ls[-1])
    return (f" For the {len(hdr)} panel records in {fmt} the reported counts cover only"
            " the final step, not the whole session.")


def running_note(rows):
    """Clause for records still running, which the table shows by status.

    Their ledger outcome is provisional, so the table does not count it; the
    clause says how many such records there are and what the ledger records
    for them. Empty when no record is running, so the sentence stays true.
    """
    run = [r for r in rows if r.get("status") == "running"]
    if not run:
        return ""
    words = "zero one two three four five six seven eight nine ten".split()
    n = len(run)
    count = words[n] if n < len(words) else str(n)
    outs = sorted({OUTCOME_TEX[r["outcome"]].lower() for r in run})
    listed = outs[0] if len(outs) == 1 else ", ".join(outs[:-1]) + " and " + outs[-1]
    if n == 1:
        tail = f"one record, whose provisional outcome is {listed}"
    else:
        tail = f"{count} records, whose provisional outcomes are {listed}"
    return ("; a record whose run is still going is counted by that status"
            f" instead ({tail})")


def closeout(out, ledger_rel):
    commit, blob = ledger_source(ledger_rel)
    led = json.load(open(os.path.join(ROOT, ledger_rel)))
    rows = led["rows"]
    bad = [r.get("id") for r in rows if r.get("outcome") not in OUTCOMES]
    if bad:
        raise SystemExit(f"ledger rows without a known outcome: {bad[:5]}")
    check_no_whole_book(rows)
    named = sorted({closeout_model(r) for r in rows} - {NO_CALL, UNRECORDED})
    cols = named + [k for k in (UNRECORDED, NO_CALL) if any(closeout_model(r) == k for r in rows)]
    label = lambda m: (f"{tex_tt(m)} ({closeout_family(m)})" if m in named
                       else m[0].upper() + m[1:])
    # Column heads in two lines (family over model) so the table fits the page.
    stack = {NO_CALL: "No model\\\\call", UNRECORDED: "Model not\\\\recorded"}
    head = " & ".join(f"\\shortstack[r]{{{closeout_family(m)}\\\\{tex_tt(m)}}}" if m in named
                      else f"\\shortstack[r]{{{stack[m]}}}" for m in cols)
    lines = []
    body = []
    # A review whose provider call is still running (status "running") keeps
    # its ledger outcome but is shown as still running: no acceptance yet, and
    # not a negative verdict. A terminal record that is only pending
    # adjudication (pending true, e.g. an invalid report) keeps its outcome
    # (ledger owner, 2026-11-14).
    shown = lambda r: PENDING if r.get("status") == "running" else r["outcome"]
    for o in OUTCOMES + [PENDING]:
        cnt = [sum(1 for r in rows if shown(r) == o and closeout_model(r) == m) for m in cols]
        if sum(cnt):
            body.append(f"{OUTCOME_TEX[o]} & " + " & ".join(str(c) for c in cnt) + f" & {sum(cnt)} \\\\\n")
    tot = [sum(1 for r in rows if closeout_model(r) == m) for m in cols]
    body.append("\\midrule\n")
    body.append("Records & " + " & ".join(str(c) for c in tot) + f" & {len(rows)} \\\\\n")
    # The whole tabular is one macro: a column specification cannot come from
    # a macro (array expands no preamble tokens).
    # Rows inside the tabular are indented two spaces, as format-tex (the
    # commit hook) writes them, so a committed copy equals a fresh run.
    inner = ["\\toprule\n", f"Outcome & {head} & All \\\\\n", "\\midrule\n"] + body + ["\\bottomrule\n"]
    lines.append("\\newcommand{\\aiCloseoutTable}{%\n"
                 f"\\begin{{tabular}}{{@{{}}l{'r' * (len(cols) + 1)}@{{}}}}\n"
                 + "".join("  " + x for x in inner) + "\\end{tabular}}\n")

    # Tokens (ledger v3): the denominator is the original provider attempts
    # (telemetry_denominator_eligible); the sums use only those with reported
    # usage (aggregation_eligible). Lines are per actual model and exact
    # token_format_signature, under the format's own field names; a record
    # without figures is a "no reported value" line, never zero.
    den = [r for r in rows if r.get("telemetry_denominator_eligible") is True]
    usage = [r for r in rows if counts_as_usage(r)]
    if any(r not in den for r in usage):
        raise SystemExit("a summed record is outside the telemetry denominator")
    sigs = []
    for r in den:
        sg = r.get("token_format_signature")
        if sg and sg != "not-recorded" and sg not in sigs:
            sigs.append(sg)
    letter = {sg: chr(ord("A") + i) for i, sg in enumerate(sigs)}
    tok = []
    for m in cols:
        md = [r for r in den if closeout_model(r) == m]
        if not md:
            continue
        for sg in sigs + ["not-recorded"]:
            bucket = [r for r in md if (r.get("token_format_signature") or "not-recorded") == sg]
            if not bucket:
                continue
            if sg == "not-recorded":
                tok.append(f"{label(m)} & no reported value & {len(bucket)} of {len(md)} \\\\\n")
                continue
            scopes = {("header" if "header/final-step" in (r.get("accounting_scope") or "") else "full")
                      for r in bucket}
            if len(scopes) > 1:
                raise SystemExit(f"mixed accounting scopes in one format for {m}")
            rep_rows = [r for r in bucket if r in usage]
            sums = collections.Counter()
            for r in rep_rows:
                t = r.get("token_usage_reported")
                items = t if isinstance(t, list) else [t]
                for c in items:
                    for k, v in c.items():
                        if isinstance(v, dict):
                            for kk, vv in v.items():
                                sums[f"{k}.{kk}"] += vv or 0
                        elif isinstance(v, (int, float)):
                            sums[k] += v
            vals = ", ".join(f"{tex_tt(k)} {fmt_int(sums[k])}" for k in sorted(sums))
            note = " (header/final-step only)" if scopes == {"header"} else ""
            tok.append(f"{label(m)}, format {letter[sg]}{note} & {vals} & {len(rep_rows)} of {len(md)} \\\\\n")
    lines.append(macro("aiCloseoutHeaderNote", header_note(den, letter)))
    lines.append("\\newcommand{\\aiCloseoutTokenRows}{%\n" + "".join(tok) + "}\n")
    # One line per format, the signature exactly as recorded.
    items = "".join(f"\\item[{letter[sg]}:] {tex_path(sg)}\n" for sg in sigs)
    lines.append("\\newcommand{\\aiCloseoutFormatKey}{%\n" + items + "}\n")

    # Cost: per model over the summed records; no currency is recorded, so
    # none is assigned.
    cost = []
    for m in cols:
        mr = [r for r in usage if closeout_model(r) == m and r.get("cost_reported") is not None]
        for cur in sorted({r.get("cost_currency") or "" for r in mr}):
            sel = [r for r in mr if (r.get("cost_currency") or "") == cur]
            amount = f"{sum(r['cost_reported'] for r in sel):.2f}"
            noun = "record" if len(sel) == 1 else "records"
            cost.append(f"{label(m)}: {amount} ({cur or 'currency not recorded'}; {len(sel)} {noun})")
    lines.append(macro("aiCloseoutCost", "; ".join(cost) if cost else "none reported"))
    lines.append(macro("aiCloseoutRunningNote", running_note(rows)))
    lines.append(macro("aiCloseoutRecords", str(len(rows))))
    lines.append(macro("aiCloseoutUsageRecords", str(len(usage))))
    lines.append(macro("aiCloseoutDenominator", str(len(den))))
    lines.append(macro("aiCloseoutSource", tex_path(ledger_rel)))
    lines.append(macro("aiCloseoutSourceCommit", commit))
    lines.append(macro("aiCloseoutSourceBlob", blob))
    if led.get("correction_recorded_utc"):
        lines.append(macro("aiCloseoutCorrection",
                           dt.datetime.fromisoformat(led["correction_recorded_utc"]).strftime("%B~%-d, %Y")))
    lines.append(macro("aiCloseoutMonth",
                       dt.datetime.fromisoformat(led["snapshot_utc"]).strftime("%B %Y")))
    lines.append(macro("aiCloseoutSnapshot",
                       dt.datetime.fromisoformat(led["snapshot_utc"]).strftime("%B~%-d, %Y")))
    out.extend(lines)

def main():
    import argparse
    ap = argparse.ArgumentParser(description="Generate notes/ai-statistics-data.tex")
    ap.add_argument("--ledger", default=LEDGER_DEFAULT,
                    help="committed experiment ledger, repository-relative (default: %(default)s)")
    args = ap.parse_args()
    runs, stats, usage, nogo, milestones = load()
    counted_commit = stats["generated_from_commit"]
    commits = git_commits(counted_commit)
    out = []
    out.append("% Generated by make_appendix.py; do not edit by hand.\n")
    out.append(f"% Review runs counted at commit {counted_commit}.\n")

    # ---- overall numbers ----
    days = sorted(commits)
    out.append(macro("aiCountedCommit", counted_commit[:7]))
    out.append(macro("aiCommits", fmt_int(sum(commits.values()))))
    out.append(macro("aiFirstDay", dt.date.fromisoformat(days[0]).strftime("%B~%-d")))
    out.append(macro("aiLastDay", dt.date.fromisoformat(days[-1]).strftime("%B~%-d, %Y")))
    out.append(macro("aiDays", str((dt.date.fromisoformat(days[-1])
                                     - dt.date.fromisoformat(days[0])).days + 1)))
    out.append(macro("aiRuns", fmt_int(len(runs))))
    out.append(macro("aiFollowups", fmt_int(len(stats["followups"]))))
    out.append(macro("aiRunsDatedByFolder",
                     str(sum(r["date_source"] == "folder-name" for r in runs))))
    folders = stats["folders"]  # one entry per review folder counted
    out.append(macro("aiReviewFolders", fmt_int(len(folders))))
    out.append(macro("aiFoldersWithRun",
                     fmt_int(len({r["folder"] for r in runs if r.get("folder")}))))

    # ---- review table by family ----
    def fam_rows(f):
        return [r for r in runs if r["family"] == f]

    rows = []
    coverage = []
    timed = {}
    tot = collections.Counter()
    for f in FAMILIES:
        R = fam_rows(f)
        completed = sum(r["outcome"].startswith("completed") for r in R)  # incl. completed-no-public-text
        failed = len(R) - completed
        bar = sum(r["outcome"].startswith("completed") and r["verdict"] in ("PASS", "PASS_WITH_NOTES")
                  and r["confidence"] == "HIGH" for r in R)
        fail = sum(r["verdict"] == "FAIL" for r in R)
        medium = sum(r["confidence"] == "MEDIUM" for r in R)
        secs = [float(r["elapsed_seconds"]) for r in R if r["elapsed_seconds"] not in ("", "None")]
        hours = f"{sum(secs) / 3600:.1f}" if secs else "--"
        cov = f"{len(secs)}/{len(R)}"
        rows.append(f"{FAM_TEX[f]} & {len(R)} & {completed} & {failed} & {bar} & {fail} "
                    f"& {medium} & {hours} \\\\\n")
        coverage.append(f"{FAM_TEX[f]} {len(secs)} of {len(R)}")
        timed[f] = len(secs)
        tot.update(runs=len(R), completed=completed, failed=failed, bar=bar, fail=fail,
                   medium=medium)
    rows.append("\\midrule\n")
    rows.append(f"Total & {tot['runs']} & {tot['completed']} & {tot['failed']} & {tot['bar']} "
                f"& {tot['fail']} & {tot['medium']} & \\\\\n")
    out.append("\\newcommand{\\aiReviewTableRows}{%\n" + "".join(rows) + "}\n")
    out.append(macro("aiHoursCoverage", "; ".join(coverage)))
    # Runs whose time was recorded, for the prose that says which data are missing
    # (Kimi: the worker-machine logs hold no Kimi tokens and few Kimi times).
    out.append(macro("aiRunsKimiTimed", str(timed["Kimi"])))
    out.append(macro("aiRunsMetBar", str(tot["bar"])))
    out.append(macro("aiRunsFail", str(tot["fail"])))
    out.append(macro("aiRunsMedium", str(tot["medium"])))
    out.append(macro("aiRunsNotCompleted", str(tot["failed"])))
    for f in FAMILIES:
        key = {"Claude": "Claude", "DeepSeek": "DeepSeek", "Kimi": "Kimi", "GPT/Codex": "GPT"}[f]
        out.append(macro(f"aiRuns{key}", str(len(fam_rows(f)))))
    out.append(macro("aiFailGPT", str(sum(r["verdict"] == "FAIL" for r in fam_rows("GPT/Codex")))))

    # ---- usage table ----
    cx = usage["codex_worker"]
    cl = usage["claude_code"]
    ds = usage["opencode"]["by_model"].get("deepseek/deepseek-v4-pro", {})
    cx_in = cx["tokens"]["input_tokens"]
    cx_cached = cx["tokens"]["cached_input_tokens"]
    out.append(macro("aiCodexSessions", str(cx["sessions"])))
    out.append(macro("aiCodexInB", fmt_b(cx_in)))
    out.append(macro("aiCodexCachedPct", f"{100 * cx_cached / cx_in:.1f}"))
    out.append(macro("aiCodexOutM", fmt_m(cx["tokens"]["output_tokens"])))
    out.append(macro("aiCodexReasonM", fmt_m(cx["tokens"]["reasoning_output_tokens"])))
    out.append(macro("aiClaudeCalls", fmt_int(cl["api_calls"])))
    out.append(macro("aiClaudeOutM", fmt_m(cl["tokens"]["output_tokens"])))
    out.append(macro("aiClaudeCacheReadB", fmt_b(cl["tokens"]["cache_read_input_tokens"])))
    out.append(macro("aiDeepSeekSessions", str(usage["opencode"]["sessions"])))
    out.append(macro("aiDeepSeekInM", fmt_m(ds.get("input", 0))))
    out.append(macro("aiDeepSeekCacheM", fmt_m(ds.get("cache_read", 0))))
    out.append(macro("aiDeepSeekOutM", fmt_m(ds.get("output", 0), 2)))
    out.append(macro("aiDeepSeekCost", f"{ds.get('cost_usd', 0):.2f}"))
    out.append(macro("aiUsageSnapshot", usage.get("snapshot_utc", "unknown").replace("T", " ")))
    ratio = cx_in / max(1, ds.get("input", 0) + ds.get("cache_read", 0))
    out.append(macro("aiWorkerToDeepSeekRatio", f"{ratio:.0f}"))

    # ---- no-go counts ----
    recs = nogo["records"]
    kinds = collections.Counter(r["kind"] for r in recs)
    math_recs = [r for r in recs if r["kind"] in ("mathematical no-go", "counterexample/erratum")]
    st = collections.Counter(r["status"] for r in math_recs)
    out.append(macro("aiNogoTotal", str(len(recs))))
    out.append(macro("aiNogoMath", str(len(math_recs))))
    out.append(macro("aiNogoRoutes", str(kinds["mathematical no-go"])))
    out.append(macro("aiNogoCounter", str(kinds["counterexample/erratum"])))
    out.append(macro("aiNogoSource", str(kinds["source-fidelity defect"])))
    out.append(macro("aiNogoMethod", str(kinds["method/verification failure"])))
    out.append(macro("aiNogoProcess", str(kinds["process/tooling failure"])))
    out.append(macro("aiNogoInBook", str(st["proved in book"])))
    out.append(macro("aiNogoReviewed", str(st["reviewed and adjudicated"])))
    out.append(macro("aiNogoRecorded", str(st["recorded only"])))

    # ---- timeline figure (plain TikZ) ----
    by_day = collections.defaultdict(collections.Counter)
    for r in runs:
        by_day[r["date"]][r["family"]] += 1
    all_days = sorted(set(commits) | set(by_day))
    d0 = dt.date.fromisoformat(all_days[0])
    d1 = dt.date.fromisoformat(all_days[-1])
    ndays = (d1 - d0).days + 1
    max_runs = max(sum(c.values()) for c in by_day.values())
    max_commits = max(commits.values())
    W, H = 12.0, 4.2          # cm
    bw = W / ndays
    ys = H / max_runs          # runs scale
    yc = H / max_commits       # commits scale
    fig = ["\\newcommand{\\aiTimelineFigure}{%\n\\begin{tikzpicture}[x=1cm,y=1cm]\n"]
    for i in range(ndays):
        day = (d0 + dt.timedelta(days=i)).isoformat()
        y = 0.0
        for f in FAMILIES:
            n = by_day.get(day, {}).get(f, 0)
            if n:
                fig.append(f"  \\fill[{FAM_COLOR[f]}] ({i * bw + 0.08:.3f},{y:.3f}) rectangle "
                           f"({(i + 1) * bw - 0.08:.3f},{y + n * ys:.3f});\n")
                y += n * ys
    pts = " -- ".join(f"({(i + 0.5) * bw:.3f},{commits.get((d0 + dt.timedelta(days=i)).isoformat(), 0) * yc:.3f})"
                      for i in range(ndays))
    fig.append(f"  \\draw[aiCommits,thick] {pts};\n")
    for i in range(ndays):
        day = d0 + dt.timedelta(days=i)
        fig.append(f"  \\fill[aiCommits] ({(i + 0.5) * bw:.3f},{commits.get(day.isoformat(), 0) * yc:.3f}) circle (1.3pt);\n")
        if i % 2 == 0:
            fig.append(f"  \\node[font=\\scriptsize,anchor=north] at ({(i + 0.5) * bw:.3f},0) "
                       f"{{{day.strftime('%b')}~{day.day}}};\n")
    fig.append(f"  \\draw (0,0) -- ({W:.3f},0);\n")
    # left axis: review runs; right axis: commits
    for v in range(0, max_runs + 1, 20):
        fig.append(f"  \\draw (0,{v * ys:.3f}) -- (-0.08,{v * ys:.3f}) "
                   f"node[left,font=\\scriptsize] {{{v}}};\n")
    for v in range(0, max_commits + 1, 50):
        fig.append(f"  \\draw ({W:.3f},{v * yc:.3f}) -- ({W + 0.08:.3f},{v * yc:.3f}) "
                   f"node[right,font=\\scriptsize,aiCommits] {{{v}}};\n")
    fig.append(f"  \\draw (0,0) -- (0,{H:.3f});\n  \\draw ({W:.3f},0) -- ({W:.3f},{H:.3f});\n")
    fig.append(f"  \\node[rotate=90,font=\\scriptsize,anchor=south] at (-0.75,{H / 2:.3f}) {{review runs}};\n")
    fig.append(f"  \\node[rotate=-90,font=\\scriptsize,anchor=south,aiCommits] at ({W + 0.85:.3f},{H / 2:.3f}) {{commits}};\n")
    # Milestones: numbered markers in a band above the plot, on the UTC day of
    # the milestone's commit; markers on the same day stack upwards.
    stack = collections.Counter()
    marks = []
    for k, m in enumerate(milestones, 1):
        day = dt.date.fromisoformat(m["utc"][:10])
        i = (day - d0).days
        marks.append((k, (i + 0.5) * bw, H + 0.45 + 0.42 * stack[i], stack[i] == 0))
        stack[i] += 1
    for k, x, y, first in marks:  # one dotted line per day, drawn below the circles
        if first:
            fig.append(f"  \\draw[densely dotted,aiMilestone] ({x:.3f},0) -- ({x:.3f},{y - 0.17:.3f});\n")
    for k, x, y, first in marks:
        fig.append(f"  \\node[circle,fill=aiMilestone,text=white,inner sep=0pt,minimum size=0.34cm,"
                   f"font=\\tiny\\bfseries] at ({x:.3f},{y:.3f}) {{{k}}};\n")
    lx = 0.0
    for f in FAMILIES:
        fig.append(f"  \\fill[{FAM_COLOR[f]}] ({lx:.2f},-0.95) rectangle ({lx + 0.25:.2f},-0.75);\n")
        fig.append(f"  \\node[right,font=\\scriptsize] at ({lx + 0.25:.2f},-0.85) {{{FAM_TEX[f]}}};\n")
        lx += 3.05
    fig.append("\\end{tikzpicture}}\n")
    out.append("".join(fig))

    # Key to the milestone markers: one line each, recorded (local) dates.
    def month_day(s):
        d = dt.date.fromisoformat(s)
        return f"{d.strftime('%b')}~{d.day}"
    cells = [f"\\textbf{{{k}}}~{month_day(m['date'])}: {m['label']}"
             for k, m in enumerate(milestones, 1)]
    rows = [f"{c} \\\\\n" for c in cells]  # one line each
    out.append("\\newcommand{\\aiMilestoneKey}{%\n" + "".join(rows) + "}\n")
    out.append(macro("aiMilestones", str(len(milestones))))

    closeout(out, args.ledger)

    root = os.path.abspath(os.path.join(HERE, "..", ".."))
    with open(os.path.join(root, "notes", "ai-statistics-data.tex"), "w") as fh:
        fh.write("".join(out))


if __name__ == "__main__":
    main()
