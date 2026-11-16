#!/usr/bin/env python3
"""Generate ai-statistics-data.tex for the AI-statistics appendix draft.

Every number printed in ai-statistics.tex comes from this file's output.
Inputs (all committed beside this script, or the repository's git history):

  reviews/runs.tsv           one row per review run (count_reviews.py)
  reviews/review-stats.json  run aggregates and follow-ups (count_reviews.py)
  tokens/token-totals.json  token and cost totals (token_totals.py)
  milestones.json            project milestones (tag, dates, commit, label, source)
  infrastructure.json        start dates of the parts of the system that are
                             older than the book, with first-commit evidence
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
    usage = json.load(open(selected("tokens")))
    nogo = json.load(open(selected("no_go")))
    nogo["first"] = json.load(open(selected("no_go_first")))
    milestones = json.load(open(os.path.join(HERE, "milestones.json")))["milestones"]
    return runs, stats, usage, nogo, milestones


def selected(name):
    """Path of a dated input named in selection.json, checked against its hash.

    The generator never falls back to another snapshot: a missing selection
    file, a missing input or a changed input stops it.
    """
    import hashlib
    sel_file = os.path.join(HERE, "selection.json")
    if not os.path.exists(sel_file):
        raise SystemExit("selection.json is missing: it names the dated inputs to use")
    entry = json.load(open(sel_file)).get(name)
    if not entry:
        raise SystemExit(f"selection.json has no entry {name!r}")
    path = os.path.join(HERE, entry["path"])
    if not os.path.exists(path):
        raise SystemExit(f"selected input {entry['path']} is missing")
    digest = hashlib.sha256(open(path, "rb").read()).hexdigest()
    if digest != entry["sha256"]:
        raise SystemExit(f"selected input {entry['path']} differs from the hash in selection.json")
    return path


COMMITS_FILE = os.path.join(HERE, "commits-per-day.json")
# The timeline (commits per day, first and last day, Figure E.1's line) can be
# counted at a later commit than the review census. timeline.json names that
# commit; its counts are recorded beside the census snapshot, which stays as
# it was.
TIMELINE_FILE = os.path.join(HERE, "timeline.json")
TIMELINE_COMMITS_FILE = os.path.join(HERE, "commits-per-day-timeline.json")


def git_commits(until, *, record=True, path=COMMITS_FILE):
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
        if record:
            with open(path, "w") as fh:
                json.dump({"counted_commit": until, "time_zone": "UTC",
                           "total": sum(counts.values()), "per_day": dict(sorted(counts.items()))},
                          fh, indent=2)
                fh.write("\n")
        return counts
    rec = json.load(open(path))
    if rec["counted_commit"] != until:
        raise SystemExit(f"{os.path.basename(path)} records {rec['counted_commit'][:7]}, "
                         f"but the count was asked for at {until[:7]}")
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
LEDGER_DEFAULT = "experiment/ledger-updates/2026-11-15-cold-closeout/run-ledger-v4.json"
OUTCOMES = ["accepted-at-scope", "not-accepted", "invalid", "refused",
            "recovered", "preflight", "continuation", "timeout"]
PENDING = "running"   # display class: a review still running (no verdict yet)
OUTCOME_TEX = {"accepted-at-scope": "Accepted at the stated scope",
               "not-accepted": "Not accepted", "invalid": "Invalid report",
               "refused": "Recovery refused", "recovered": "Recovered",
               "preflight": "Preflight (no call)",
               "continuation": "Continuation (no new vote)",
               "timeout": "Timed out",
               PENDING: "Running at snapshot"}
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


def tex_text(s):
    """Escape ordinary prose while retaining normal interword line breaks."""
    escapes = {"\\": r"\textbackslash{}", "&": r"\&", "%": r"\%",
               "$": r"\$", "#": r"\#", "_": r"\_", "{": r"\{", "}": r"\}",
               "~": r"\textasciitilde{}", "^": r"\textasciicircum{}"}
    return "".join(escapes.get(c, c) for c in s)


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


def header_note(rows, scope_key):
    """Sentence on the records whose counts cover only the panel header/final step.

    Their ledger accounting_scope says so; the sentence names how many there are and
    their accounting scopes. Empty when there are none, so the caveat disappears rather
    than leaving a dangling phrase. It starts with a space: the prose puts it straight
    after a full stop.
    """
    hdr = [r for r in rows if "header/final-step" in (r.get("accounting_scope") or "")]
    if not hdr:
        return ""
    keys = sorted({scope_key[r["accounting_scope"]] for r in hdr})
    scopes = ("scope~" + keys[0]) if len(keys) == 1 else \
        ("scopes~" + ", ".join(keys[:-1]) + " and~" + keys[-1])
    return (f" For the {len(hdr)} records with {scopes} the reported counts cover only"
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
    return ("; historical running records retain their snapshot status"
            f" ({tail})")


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
    # Keep the original token-field signature and accounting scope distinct.
    # These are reported component sums, never actual all-activity totals.
    scopes_all = list(dict.fromkeys(r.get("accounting_scope") or "Accounting scope not recorded"
                                   for r in den))
    scope_key = {scope: f"S{i+1}" for i, scope in enumerate(scopes_all)}
    tok = []
    for m in cols:
        md = [r for r in den if closeout_model(r) == m]
        if not md:
            continue
        for sg in sigs + ["not-recorded"]:
            bucket = [r for r in md if (r.get("token_format_signature") or "not-recorded") == sg]
            for scope in scopes_all:
                scoped = [r for r in bucket if
                          (r.get("accounting_scope") or "Accounting scope not recorded") == scope]
                if not scoped:
                    continue
                if sg == "not-recorded":
                    tok.append(f"{label(m)}, scope~{scope_key[scope]} & no reported value & {len(scoped)} of {len(md)} \\\\\n")
                    continue
                rep_rows = [r for r in scoped if r in usage]
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
                note = " (header/final-step only)" if "header/final-step" in scope else ""
                tok.append(f"{label(m)}, format {letter[sg]}, scope~{scope_key[scope]}{note} & {vals} & {len(rep_rows)} of {len(md)} \\\\\n")
    scope_descriptions = {
        "Original reported object/list; do not infer a broader accounting level":
            "The usage object as the tool reported it; no wider total is implied.",
        "Panel header/final-step usage only; not verified full-session totals":
            "The final step of a panel run only, not the whole session.",
        "One native assistant response; reported token object. No broader session accounting inferred.":
            "One response of the model; no session total is implied.",
        "header/final-step usage only; previous abandoned stream usage unknown; not full invocation totals.":
            "The final step only; the usage of an earlier abandoned attempt is unknown.",
    }
    accounting_items = "".join(f"\\item[{scope_key[scope]}:] {tex_text(scope_descriptions.get(scope, scope))}\n"
                               for scope in scopes_all)
    lines.append("\\newcommand{\\aiCloseoutAccountingKey}{%\n" + accounting_items + "}\n")
    lines.append(macro("aiCloseoutHeaderNote", header_note(den, scope_key)))
    lines.append("\\newcommand{\\aiCloseoutTokenRows}{%\n" + "".join(tok) + "}\n")
    # One line per format, the signature exactly as recorded.
    items = "".join(f"\\item[{letter[sg]}:] {tex_path(sg)}\n" for sg in sigs)
    lines.append("\\newcommand{\\aiCloseoutFormatKey}{%\n" + items + "}\n")

    # Sum cost components only within model/format/currency/accounting scope.
    # A missing abandoned-stream cost remains unknown, not zero.
    cost = []
    for m in cols:
        mr = [r for r in usage if closeout_model(r) == m and r.get("cost_reported") is not None]
        for scope in scopes_all:
            scoped = [r for r in mr if
                      (r.get("accounting_scope") or "Accounting scope not recorded") == scope]
            for sg in sigs + ["not-recorded"]:
                formatted = [r for r in scoped if
                             (r.get("token_format_signature") or "not-recorded") == sg]
                for cur in sorted({r.get("cost_currency") or "" for r in formatted}):
                    sel = [r for r in formatted if (r.get("cost_currency") or "") == cur]
                    amount = f"{sum(r['cost_reported'] for r in sel):.2f}"
                    noun = "record" if len(sel) == 1 else "records"
                    form = letter.get(sg, "not recorded")
                    cost.append(f"{label(m)}, format {form}, scope~{scope_key[scope]}: {amount} ({cur or 'currency not recorded'}; {len(sel)} {noun}; known reported components only)")
    lines.append(macro("aiCloseoutCost", "; ".join(cost) if cost else "none reported"))
    lines.append(macro("aiCloseoutRunningNote", running_note(rows)))
    recent = [r for r in rows if r["id"] in {f"C{i:03}" for i in range(12, 18)}]
    local = [r for r in recent if r["id"] in {f"C{i:03}" for i in range(14, 18)}]
    words = "zero one two three four five six seven eight nine ten".split()
    word = lambda n: words[n] if n < len(words) else str(n)
    lines.append(macro("aiCloseoutHistoricalRecords", str(len(rows) - len(recent))))
    lines.append(macro("aiCloseoutRecentRecords", str(len(recent))))
    lines.append(macro("aiCloseoutRecentWords", word(len(recent)).capitalize()))
    lines.append(macro("aiCloseoutLocalWords", word(len(local)).capitalize()))
    lines.append(macro("aiCloseoutLocalPassWords",
                       word(sum(r.get("reported_verdict") == "PASS" for r in local))))
    lines.append(macro("aiCloseoutLocalNotesWords",
                       word(sum(r.get("reported_verdict") == "PASS_WITH_NOTES" for r in local))))
    lines.append(macro("aiCloseoutLocalAcceptedWords",
                       word(sum(r.get("accepted_at_stated_scope") is True for r in local)).capitalize()))
    lines.append(macro("aiCloseoutLocalPartialWords",
                       word(sum(str(r.get("adjudication_status", "")).startswith("PARTIAL") for r in local))))
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


def validate_review_evidence(updates, inventory, ledger, later):
    """Check an additive chronology; never infer grades or merge usage."""
    def need(condition, message):
        if not condition:
            raise ValueError(message)

    need(updates.get("schema") == "publication-review-evidence/1",
         "unsupported review evidence schema")
    need(inventory.get("schema") == "publication-review-attempt-inventory/1",
         "unsupported attempt inventory schema")
    need(inventory["base_snapshot"] == updates["base_snapshot"]
         and updates["base_snapshot"]["row_count"] == len(ledger["rows"]),
         "addendum base snapshots disagree")
    attempts = inventory["attempts"]
    followups = inventory["followups"]
    counts = inventory["counts"]
    ids = [row["id"] for row in attempts]
    need(len(set(ids)) == len(ids), "duplicate recovered attempt identifiers")
    need(len(attempts) == counts["attempts"] == later["total"],
         "recovered attempt totals disagree")
    days = collections.Counter(row["date_utc"] for row in attempts)
    need(dict(days) == later["per_day"], "recovered UTC-day totals disagree")
    for day in days:
        dt.date.fromisoformat(day)
    base_ids = {r["id"] for r in ledger["rows"]
                if r["record_kind"] == "provider_attempt"}
    linked = [r["base_record_id"] for r in attempts if r["base_record_id"]]
    need(len(linked) == len(set(linked)) and set(linked) == base_ids,
         "recovered inventory does not link each original attempt exactly once")
    need(len(linked) == counts["base_attempts"] == later["in_closeout_ledger"],
         "base-attempt counts disagree")
    need(len(attempts) - len(linked) == counts["extra_attempts"] ==
         later["not_in_closeout_ledger"], "additional-attempt counts disagree")
    need(len(followups) == counts["followups"], "follow-up counts disagree")
    need(len({r["id"] for r in followups}) == len(followups)
         and not (set(ids) & {r["id"] for r in followups}),
         "follow-ups are duplicated or counted as fresh attempts")
    # This catalog deliberately has no completion or scientific-grade projection.
    for row in attempts:
        need(not ({"verdict", "confidence", "accepted", "accepted_effective"} &
                  set(row)), "quality projection entered the timeline inventory")
    observations = updates["observations"]
    missing = {r["id"] for r in ledger["rows"]
               if r["record_kind"] == "provider_attempt"
               and r["started_utc"] is None}
    need({r["record_id"] for r in observations} == missing
         and len(observations) == len(missing),
         "missing-start observations do not match the frozen ledger")
    starts = [r for r in observations if r.get("recorded_start_utc")]
    clients = [r for r in observations if r.get("client_session_created_utc")]
    bounded = [r for r in observations if r not in starts and r not in clients]
    need(not ({r["record_id"] for r in starts} &
              {r["record_id"] for r in clients}),
         "client clock was promoted to a recorded invocation start")
    observed_counts = updates["counts"]
    need(len(observations) == observed_counts["missing_start_observations"]
         and len(starts) == observed_counts["recorded_starts"]
         and len(clients) == observed_counts["client_clocks"]
         and len(bounded) == observed_counts["bounded_records"],
         "clock-evidence counts disagree")
    need({r["record_id"] for r in starts} ==
         {"C001", "C006", "C007", "C009", "C010", "C011"},
         "recorded-start evidence set changed")

    def utc(value):
        parsed = dt.datetime.fromisoformat(value.replace("Z", "+00:00"))
        need(parsed.tzinfo is not None, "clock lacks a timezone")
        return parsed.astimezone(dt.timezone.utc)

    for row in starts:
        need(utc(row["recorded_start_utc"]).date().isoformat() == row["date_utc"],
             "recorded start and UTC day disagree")
    for row in clients:
        need(not row.get("recorded_start_utc"),
             "client-session creation is not a runner/API start")
        utc(row["client_session_created_utc"])
        if row.get("client_session_updated_utc"):
            utc(row["client_session_updated_utc"])
    need(len(bounded) == 1 and bounded[0]["record_id"] == "P2-deepseek",
         "bounded panel evidence set changed")
    p2 = next(row for row in attempts
              if row["base_record_id"] == "P2-deepseek")
    need(p2["actual_model"] is None and p2["actual_family"] is None,
         "requested P2 route was promoted to actual attribution")
    for row in clients + bounded:
        window = row["invocation_day_bounds"]
        lower = utc(window["start_not_before_utc"])
        upper = utc(window["finish_not_after_utc"])
        need(lower <= upper and lower.date().isoformat() == row["date_utc"]
             == upper.date().isoformat(), "panel invocation day is not bounded")
    point_keys = ("started_utc", "finished_utc", "recorded_start_utc",
                  "invocation_started_utc", "invocation_finished_utc",
                  "client_session_created_utc", "client_session_updated_utc")
    need(not any(p2["time_evidence"].get(k) for k in point_keys),
         "bounded P2 evidence gained an invented point clock")
    c11 = next(row for row in observations if row["record_id"] == "C011")
    need(c11["later_native_status_label"] == "invalid-report"
         and c11["later_recovered_status_label"] == "review-complete-recovered"
         and c11["literal_recovered_reported_result"]["verdict"] == "PASS_WITH_NOTES"
         and c11["literal_recovered_reported_result"]["confidence"] == "medium"
         and c11["new_attempt"] is False,
         "C011 terminal/recovered evidence was changed or counted as a new review")
    decision = updates["policy_decision"]
    expected = {"grades_unchanged": True, "new_whole_book_acceptance": False,
                "new_independent_vote": False, "new_review_call": False,
                "is_public_release_execution": False, "is_final_accept_file": False}
    need(decision["option"] == "A" and decision["date"] == "2026-11-15",
         "author policy event changed")
    for key, value in expected.items():
        need(decision.get(key) is value,
             "policy event must not change grades, calls or acceptance")
    return starts, clients, bounded


def review_evidence(out, ledger_rel):
    """Generate only chronology and decision macros from hash-selected evidence."""
    import hashlib
    updates_path = selected("review_evidence")
    inventory_path = selected("review_inventory")
    updates = json.load(open(updates_path))
    inventory = json.load(open(inventory_path))
    ledger_path = os.path.join(ROOT, ledger_rel)
    base = updates["base_snapshot"]
    if (base["ledger_path"] != ledger_rel or
            hashlib.sha256(open(ledger_path, "rb").read()).hexdigest()
            != base["ledger_sha256"]):
        raise SystemExit("review evidence is not bound to the selected frozen ledger")
    catalog = updates["catalog"]
    if (os.path.abspath(os.path.join(ROOT, catalog["path"])) !=
            os.path.abspath(inventory_path) or
            hashlib.sha256(open(inventory_path, "rb").read()).hexdigest()
            != catalog["sha256"]):
        raise SystemExit("review inventory differs from the evidence addendum")
    ledger = json.load(open(ledger_path))
    later = json.load(open(selected("later_attempts")))
    try:
        starts, clients, bounded = validate_review_evidence(
            updates, inventory, ledger, later)
    except (KeyError, TypeError, ValueError) as error:
        raise SystemExit(f"invalid additive review evidence: {error}")
    counts = inventory["counts"]
    for name, key in [("aiEvidenceAttempts", "attempts"),
                      ("aiEvidenceBaseAttempts", "base_attempts"),
                      ("aiEvidenceExtraAttempts", "extra_attempts"),
                      ("aiEvidenceFollowups", "followups")]:
        out.append(macro(name, fmt_int(counts[key])))
    out.append(macro("aiEvidenceRecordedStarts", str(len(starts))))
    out.append(macro("aiEvidenceClientClocks", str(len(clients))))
    start_rows = []
    for row in sorted(starts, key=lambda r: r["record_id"]):
        stamp = dt.datetime.fromisoformat(row["recorded_start_utc"].replace("Z", "+00:00"))
        stamp = stamp.astimezone(dt.timezone.utc).strftime("%Y-%m-%d %H:%M:%S.%f")
        kind = "CLI receipt start" if row["record_id"] == "C011" else "Runner launch"
        start_rows.append(f'{tex_tt(row["record_id"])} & {tex_tt(stamp)} & {kind} '
                          + r"\\" + "\n")
    out.append("\\newcommand{\\aiEvidenceStartRows}{%\n" + "".join(start_rows) + "}\n")
    out.append(macro("aiEvidenceDecisionDate",
                     dt.date.fromisoformat(updates["policy_decision"]["date"])
                     .strftime("%B~%-d, %Y")))
    out.append(macro("aiEvidenceInventoryPath",
                     tex_path(os.path.relpath(inventory_path, ROOT))))
    out.append(macro("aiEvidenceUpdatesPath",
                     tex_path(os.path.relpath(updates_path, ROOT))))

def infrastructure(out):
    """Macros for the paragraph before Figure E.1: when each part began."""
    parts = {p["key"]: p for p in json.load(open(selected("infrastructure")))["parts"]}
    need = ["book", "bibliography", "library", "sources", "wiki", "skills"]
    if sorted(parts) != sorted(need):
        raise SystemExit("infrastructure.json must have exactly the parts " + ", ".join(need))

    def when(key):
        p = parts[key]
        day = dt.date.fromisoformat(p["start"])
        if not p.get("evidence"):
            raise SystemExit(f"infrastructure.json: {key} has no evidence")
        return day, day.strftime("%B~%-d, %Y" if p["precision"] == "day" else "%B %Y")

    days = {k: when(k) for k in need}
    if any(days[k][0] >= days["book"][0] for k in need if k != "book"):
        raise SystemExit("infrastructure.json: a part does not predate the book")
    if days["bibliography"][1] != days["library"][1]:
        raise SystemExit("infrastructure.json: the text names one month for bibliography and library")
    out.append(macro("aiInfraBookStart", days["book"][1]))
    out.append(macro("aiInfraBibStart", days["bibliography"][1]))
    out.append(macro("aiInfraSourcesStart", days["sources"][1]))
    out.append(macro("aiInfraWikiStart", days["wiki"][1]))
    out.append(macro("aiInfraSkillsWhen", "in the same month"
                     if days["skills"][1] == days["wiki"][1] else "in " + days["skills"][1]))


def rereads(out):
    """Macros for the section on the re-reads after the readability pass.

    Every figure is recounted from the rows of the two frozen files and must
    equal the files' own summary; a difference stops the generator.
    """
    cov = json.load(open(selected("reread_coverage")))
    att = json.load(open(selected("reread_attempts")))
    aid = json.load(open(selected("readability_pass")))
    if cov["summary"] != att["summary"]:
        raise SystemExit("re-read files: the two summaries differ")
    sm, rows, attempts = cov["summary"], cov["proof_rows"], att["attempts"]
    by_id = {a["record_id"]: a for a in attempts}
    current = sorted({r["selected_record_id"] for r in rows})
    status = collections.Counter(r["author_math_reconstruction_status"] for r in rows)
    changed = sum(r["proof_environment_sha256"] != r["baseline_proof_environment_sha256"]
                  for r in rows)
    grades = collections.Counter(a["raw_grade"] for a in attempts)
    cur_grades = collections.Counter(by_id[i]["raw_grade"] for i in current)
    restarted = [a for a in attempts if a["observed_generation_starts"] > 1]
    held = [a for a in restarted if a["protocol_pending"]]
    allowed = [a for a in restarted if not a["protocol_pending"]]
    complete = sum(r["reported_flags"]["old_reading"] == "COMPLETE"
                   and r["reported_flags"]["new_reading"] == "COMPLETE" for r in rows)
    tokens = sm["available_finish_token_sums_only"]
    checks = [
        (len(rows), sm["current_proof_pairs"]), (len(cov["files"]), sm["technical_files"]),
        (len(current), sm["selected_source_current_records"]),
        (len(attempts), sm["actual_coordinator_attempts"]),
        (sum(a["report_present"] for a in attempts), sm["nonempty_public_reports"]),
        (sum(a["assigned_proof_pairs"] for a in attempts), sm["attempt_assigned_proof_pairs"]),
        (grades["PASS"], sm["raw_grade_counts"]["PASS"]),
        (grades["PASS_WITH_NOTES"], sm["raw_grade_counts"]["PASS_WITH_NOTES"]),
        (grades[None], sm["raw_grade_counts"]["NO_PUBLIC_REPORT"]),
        (dict(status), sm["local_author_math_counts"]),
        (complete, sm["current_reported_complete_old_new_readings"]),
        (len(restarted), sm["observed_starts_without_finish_usage"]),
        (sorted(a["record_id"] for a in held), sorted(att["protocol_limits"]["old_unapproved_holds"])),
        (sorted(a["record_id"] for a in allowed),
         sorted(att["protocol_limits"]["prospectively_authorized_observed_recovery"])),
        (len(att["prepared_not_launched"]), len(sm["prepared_unlaunched_ids"])),
        (sum(a["raw_global_confidence"] == "high" for a in attempts),
         sum(a["report_present"] for a in attempts)),
        (sm["whole_book_accepted"], False), (sm["whole_invocation_usage_cost_cap"], None),
        (any(by_id[i]["protocol_pending"] for i in current), False),
        (sum(by_id[i]["assigned_proof_pairs"] for i in current), len(rows)),
        (len(sm["literal_comparison_limits"]), 1), (len(sm["clock_obstruction_core_vs_contract"]), 1),
        (status["PARTIAL"], grades["PASS_WITH_NOTES"]),  # the text calls this equality a coincidence
    ]
    for k, (got, want) in enumerate(checks):
        if got != want:
            raise SystemExit(f"re-read files: recount {k} gives {got!r}, the summary says {want!r}")
    m = lambda name, n: out.append(macro(name, fmt_int(n) if isinstance(n, int) else n))
    m("aiRereadFiles", len(cov["files"]))
    m("aiRereadProofs", len(rows))
    m("aiRereadChanged", changed)
    m("aiRereadUnchanged", len(rows) - changed)
    m("aiRereadStatementsChanged", sum(not r["statement_unchanged"] for r in rows))
    m("aiRereadReaderEditionProofs", aid["reader_edition_proofs_not_counted"])
    m("aiRereadCalls", len(attempts))
    m("aiRereadReports", sum(a["report_present"] for a in attempts))
    m("aiRereadNoReport", grades[None])
    m("aiRereadPass", grades["PASS"])
    m("aiRereadPassNotes", grades["PASS_WITH_NOTES"])
    m("aiRereadPairsSent", sum(a["assigned_proof_pairs"] for a in attempts))
    m("aiRereadNeverSent", len(att["prepared_not_launched"]))
    m("aiRereadCurrent", len(current))
    m("aiRereadCurrentPass", cur_grades["PASS"])
    m("aiRereadCurrentPassNotes", cur_grades["PASS_WITH_NOTES"])
    m("aiRereadEarlier", len(attempts) - len(current))
    m("aiRereadComplete", complete)
    m("aiRereadChecked", status["CHECKED"])
    m("aiRereadConditional", status["CHECKED_CONDITIONAL_PARENT"])
    m("aiRereadConditionalGroups", len(cov["conditional_parent_groups"]))
    m("aiRereadPartial", status["PARTIAL"])
    m("aiRereadRestarted", len(restarted))
    m("aiRereadRestartedHeld", len(held))
    m("aiRereadRestartedAllowed", len(allowed))
    m("aiRereadRestartedCurrentProofs",
      sum(by_id[r["selected_record_id"]]["observed_generation_starts"] > 1 for r in rows))
    m("aiRereadTokens", tokens["reported_total"])
    m("aiRereadTokensCached", tokens["cache_read"])
    m("aiRereadCostCounter", f"{float(sm['available_finish_cost_counter_sum_only_not_invoice']):.2f}")
    day = lambda key, f: dt.datetime.fromisoformat(f(a[key] for a in attempts if a[key]))
    first, last = day("actual_started_utc", min), day("actual_finished_utc", max)
    if first.date() != last.date():
        raise SystemExit("re-read files: the text names one day")
    m("aiRereadDay", first.strftime("%B~%-d, %Y"))
    m("aiRereadSource", cov["source_revision"][:8])
    m("aiRereadReaderRuns", aid["reader_runs"]["count"])
    runs = aid["reader_runs"]
    if (len(runs["stop_points_by_run"]) != runs["count"]
            or sum(runs["stop_points_by_run"].values()) != runs["stop_points_listed"]):
        raise SystemExit("readability-pass record: the per-run stop points do not add up")
    m("aiRereadStopPoints", runs["stop_points_listed"])


def main():
    import argparse
    ap = argparse.ArgumentParser(description="Generate notes/ai-statistics-data.tex")
    ap.add_argument("--ledger", default=LEDGER_DEFAULT,
                    help="committed experiment ledger, repository-relative (default: %(default)s)")
    ap.add_argument("--check", action="store_true",
                    help="verify generated Appendix E data without writing any files")
    args = ap.parse_args()
    runs, stats, usage, nogo, milestones = load()
    counted_commit = stats["generated_from_commit"]
    # The timeline commit and its recorded counts are selected inputs: there
    # is no fallback to the census commit. Where the commit exists, the counts
    # from git must equal the recorded ones.
    timeline_commit = json.load(open(selected("timeline")))["counted_commit"]
    recorded = json.load(open(selected("timeline_commits")))
    if recorded["counted_commit"] != timeline_commit:
        raise SystemExit("commits-per-day-timeline.json was not counted at the commit in timeline.json")
    commits = git_commits(timeline_commit, record=False, path=TIMELINE_COMMITS_FILE)
    if dict(commits) != recorded["per_day"]:
        raise SystemExit("commits per day from git differ from commits-per-day-timeline.json")
    out = []
    out.append("% Generated by make_appendix.py; do not edit by hand.\n")
    out.append(f"% Review runs counted at commit {counted_commit}.\n")
    out.append(f"% Commits per day counted at commit {timeline_commit}.\n")

    # ---- overall numbers ----
    days = sorted(commits)
    out.append(macro("aiCountedCommit", counted_commit[:7]))
    out.append(macro("aiTimelineCommit", timeline_commit[:7]))
    out.append(macro("aiCommits", fmt_int(sum(commits.values()))))
    out.append(macro("aiFirstDay", dt.date.fromisoformat(days[0]).strftime("%B~%-d")))
    out.append(macro("aiLastDay", dt.date.fromisoformat(days[-1]).strftime("%B~%-d, %Y")))
    out.append(macro("aiDays", str((dt.date.fromisoformat(days[-1])
                                     - dt.date.fromisoformat(days[0])).days + 1)))
    out.append(macro("aiReviewLastDay", dt.date.fromisoformat(
        max(r["date"] for r in runs)).strftime("%B~%-d")))
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
    # Required usage fields are never defaulted to zero: a missing one stops
    # the generator.
    try:
        ds = usage["opencode"]["by_model"]["deepseek/deepseek-v4-pro"]
        for k in ("input", "cache_read", "output", "cost_usd"):
            ds[k]
        usage["snapshot_utc"]
    except KeyError as e:
        raise SystemExit(f"token snapshot lacks the required field {e}")
    # Claude Code: "api_calls" counts logged usage records. The per-model
    # parts must add up, and synthetic records must carry no tokens, so that
    # the token totals are those of the named models.
    if sum(cl["calls_by_model"].values()) != cl["api_calls"]:
        raise SystemExit("Claude usage records by model do not add up to the total")
    for k, v in cl["tokens"].items():
        if sum(m.get(k, 0) for m in cl["tokens_by_model"].values()) != v:
            raise SystemExit(f"Claude {k} by model does not add up to the total")
    if any(cl["tokens_by_model"].get("<synthetic>", {}).values()):
        raise SystemExit("synthetic Claude records carry tokens: report them separately")
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
    out.append(macro("aiDeepSeekInM", fmt_m(ds["input"])))
    out.append(macro("aiDeepSeekCacheM", fmt_m(ds["cache_read"])))
    out.append(macro("aiDeepSeekOutM", fmt_m(ds["output"], 2)))
    out.append(macro("aiDeepSeekCost", f"{ds['cost_usd']:.2f}"))
    out.append(macro("aiUsageSnapshot", usage["snapshot_utc"].replace("T", " ")))
    ratio = cx_in / max(1, ds["input"] + ds["cache_read"])
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
    first = [r for r in nogo["first"]["records"]
             if r["kind"] in ("mathematical no-go", "counterexample/erratum")]
    st1 = collections.Counter(r["status"] for r in first)
    out.append(macro("aiNogoTotalFirst", str(len(nogo["first"]["records"]))))
    out.append(macro("aiNogoInBookFirst", str(st1["proved in book"])))
    out.append(macro("aiNogoReviewedFirst", str(st1["reviewed and adjudicated"])))
    out.append(macro("aiNogoRecordedFirst", str(st1["recorded only"])))
    out.append(macro("aiNogoSnapshot", dt.date.fromisoformat(nogo["snapshot_date"]).strftime("%B~%-d, %Y")))

    # ---- timeline figure (plain TikZ) ----
    by_day = collections.defaultdict(collections.Counter)
    for r in runs:
        by_day[r["date"]][r["family"]] += 1
    later = json.load(open(selected("later_attempts")))
    later_days = later["per_day"]
    if sum(later_days.values()) != later["total"]:
        raise SystemExit("later-attempts snapshot: per-day counts do not add up to its total")
    out.append(macro("aiLaterAttempts", str(later["total"])))
    out.append(macro("aiLaterInLedger", str(later["in_closeout_ledger"])))
    out.append(macro("aiLaterFirstDay", dt.date.fromisoformat(min(later_days)).strftime("%B~%-d")))
    out.append(macro("aiLaterLastDay", dt.date.fromisoformat(max(later_days)).strftime("%B~%-d")))
    all_days = sorted(set(commits) | set(by_day) | set(later_days))
    d0 = dt.date.fromisoformat(all_days[0])
    d1 = dt.date.fromisoformat(all_days[-1])
    ndays = (d1 - d0).days + 1
    max_runs = max(max(sum(c.values()) for c in by_day.values()), max(later_days.values()))
    max_commits = max(commits.values())
    W, H = 12.0, 4.2          # cm
    bw = W / ndays
    ys = H / max_runs          # runs scale
    yc = H / max_commits       # commits scale
    fig = ["\\newcommand{\\aiTimelineFigure}{%\n\\begin{tikzpicture}[x=1cm,y=1cm]\n"]
    for i in range(ndays):
        day = (d0 + dt.timedelta(days=i)).isoformat()
        y = 0.0
        # A day with both series shows them side by side, never stacked: the
        # later attempts are not to be added to the census runs.
        both = bool(by_day.get(day)) and bool(later_days.get(day))
        x0, x1 = i * bw + 0.08, (i + 1) * bw - 0.08
        xm = x0 + 0.62 * (x1 - x0)
        cx1 = xm - 0.02 if both else x1
        for f in FAMILIES:
            n = by_day.get(day, {}).get(f, 0)
            if n:
                fig.append(f"  \\fill[{FAM_COLOR[f]}] ({x0:.3f},{y:.3f}) rectangle "
                           f"({cx1:.3f},{y + n * ys:.3f});\n")
                y += n * ys
        n = later_days.get(day, 0)
        if n:  # later attempts: grey, not coloured by family, from the baseline
            fig.append(f"  \\draw[aiCommits,fill=aiCommits!15] "
                       f"({(xm + 0.02) if both else x0:.3f},0.000) rectangle "
                       f"({x1:.3f},{n * ys:.3f});\n")
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
        lx += {"Claude": 3.0, "DeepSeek": 2.9, "Kimi": 1.8}.get(f, 2.3)
    fig.append(f"  \\draw[aiCommits,fill=aiCommits!15] "
               f"({lx:.2f},-0.95) rectangle ({lx + 0.25:.2f},-0.75);\n")
    fig.append(f"  \\node[right,font=\\scriptsize] at ({lx + 0.25:.2f},-0.85) {{recovered attempts}};\n")
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

    infrastructure(out)
    rereads(out)
    closeout(out, args.ledger)
    review_evidence(out, args.ledger)

    root = os.path.abspath(os.path.join(HERE, "..", ".."))
    output = os.path.join(root, "notes", "ai-statistics-data.tex")
    rendered = "".join(out)
    if args.check:
        with open(output) as fh:
            if fh.read() != rendered:
                raise SystemExit("Appendix E generated data are stale; regenerate from the selected committed ledger")
        print("Appendix E generated data match the selected committed ledger")
    else:
        with open(output, "w") as fh:
            fh.write(rendered)


if __name__ == "__main__":
    main()
