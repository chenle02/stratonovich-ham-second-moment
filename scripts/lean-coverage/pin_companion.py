#!/usr/bin/env python3
"""Pin the Lean companion's coverage file and receipt numbers for Appendix F.

Usage: pin_companion.py COMPANION_REPO VERIFIED_COMMIT [COVERAGE_COMMIT]
           [--successor-check SCRIPT]
VERIFIED_COMMIT is the commit the receipts and the claims ledger are bound
to (the one the book quotes). COVERAGE_COMMIT (default: the same) is where
coverage.yaml is read; it must descend from VERIFIED_COMMIT through commits
that change only files the Lean build does not read (the companion's
docs-only rule in lean-pkg-binding.yaml). The one exception is checked, not
skipped: with --successor-check SCRIPT, a coverage commit that is not a
docs-only successor is accepted only if SCRIPT (the companion's own
verifier, called as  SCRIPT REPO VERIFIED COVERAGE --json OUT) exits 0 with
the verdict ALLOWED-SUCCESSOR for exactly these two commits; its JSON record
is written beside coverage-commit.txt as successor-check.json.
Writes beside this script:
  coverage.yaml               the companion's coverage.yaml at COVERAGE_COMMIT
  coverage-commit.txt         VERIFIED_COMMIT (full) and its date, then
                              COVERAGE_COMMIT (full)
  lean-receipt-summary.json   numbers from the receipts bound to COMMIT and
                              from `lean-pkg claims ledger --json`, with no
                              host names or paths
Run it on the machine that holds the companion and its .lean-receipts/.
"""
import json
import os
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
# Every check runs before any file is written: outputs are collected in `out`
# and written together at the end, so a refused pin leaves the pinned files as
# they were.
out = {}


def write_all(files):
    for name, text in files.items():
        with open(os.path.join(HERE, name), "w") as fh:
            fh.write(text)
args = sys.argv[1:]
successor_check = None
if "--successor-check" in args:
    i = args.index("--successor-check")
    successor_check = args[i + 1]
    del args[i:i + 2]
repo, commit = args[0], args[1]
cov_commit = args[2] if len(args) > 2 else commit
git = lambda *a: subprocess.run(["git", "-C", repo, *a], capture_output=True, text=True, check=True).stdout
full = git("rev-parse", commit).strip()
cov_full = git("rev-parse", cov_commit).strip()
date = git("show", "-s", "--format=%cI", full).strip()
if cov_full != full:
    if subprocess.run(["git", "-C", repo, "merge-base", "--is-ancestor", full, cov_full]).returncode:
        raise SystemExit("coverage commit does not descend from the verified commit")
    changed = git("diff", "--name-only", full, cov_full).split()
    build = [f for f in changed if f.endswith(".lean") or f.startswith("lakefile") or f in
             ("lake-manifest.json", "lean-toolchain", "claims.yaml", "lean-pkg-binding.yaml")]
    if build:
        if not successor_check:
            raise SystemExit(f"commits after the verified commit change build inputs: {build}")
        import tempfile
        with tempfile.TemporaryDirectory() as tmp:
            rec_path = os.path.join(tmp, "record.json")
            run = subprocess.run([sys.executable, "-I", successor_check, repo, full, cov_full,
                                  "--json", rec_path], capture_output=True, text=True)
            rec = json.load(open(rec_path)) if os.path.exists(rec_path) else {}
        if (run.returncode != 0 or rec.get("verdict") != "ALLOWED-SUCCESSOR" or rec.get("failures")
                or rec.get("verified") != full or rec.get("coverage") != cov_full):
            raise SystemExit("the coverage commit is not a docs-only successor and the successor check "
                             f"did not allow it: {rec.get('verdict')} {rec.get('failures')}")
        out["successor-check.json"] = json.dumps(rec, indent=1) + "\n"
out["coverage.yaml"] = git("show", f"{cov_full}:coverage.yaml")
# The companion's completion record (milestones and the status of every
# labelled result), if it exists at the coverage commit.
if "COMPLETION.md" in git("ls-tree", "--name-only", cov_full).split():
    # Headings and tables only: the generator reads nothing else, and the prose
    # may name private machines that must not appear in public files.
    kept = [l for l in git("show", f"{cov_full}:COMPLETION.md").splitlines()
            if l.startswith(("#", "|")) or not l.strip()]
    text = "\n".join(kept)
    while "\n\n\n" in text:
        text = text.replace("\n\n\n", "\n\n")
    out["completion.md"] = (
        f"<!-- Headings and tables of the Lean companion's COMPLETION.md at {cov_full[:12]}, "
        "pinned by pin_companion.py; the prose is omitted. -->\n\n" + text.strip() + "\n")
out["coverage-commit.txt"] = f"{full}\n{date}\n{cov_full}\n"

# Receipts are read from the coverage commit through git, not the working tree.
sha12 = full[:12]
names = git("ls-tree", "--name-only", cov_full, ".lean-receipts/").split()
lower = [n for n in names if n.startswith(f".lean-receipts/{sha12}-systemd-") and n.endswith(".json")]
comparator = f".lean-receipts/{sha12}-comparator.json"
if len(lower) != 1 or comparator not in names:
    raise SystemExit(f"need exactly one lower receipt and one comparator receipt for {sha12}; "
                     f"found {len(lower)} lower, comparator={comparator in names}")
lo = json.loads(git("show", f"{cov_full}:{lower[0]}"))
co = json.loads(git("show", f"{cov_full}:{comparator}"))
scope_names = git("ls-tree", "--name-only", cov_full, "docs/").split()
if "docs/coverage-scope-tex.yaml" in scope_names:
    out["coverage-scope-tex.yaml"] = git("show", f"{cov_full}:docs/coverage-scope-tex.yaml")
if lo.get("schema") != "lower-receipt/1" or co.get("schema") != "comparator-receipt/2":
    raise SystemExit("unexpected receipt schema")
for r in (lo, co):
    if r.get("commit") != full:
        raise SystemExit("receipt is bound to a different commit")
def comparator_summary(co):
    # A receipt can hold several comparator configurations (the release holds the credited
    # comparator.json and the smoke check comparator-helpers.json). Every one must pass with
    # the same permitted axioms and their theorem lists must be disjoint; the theorems
    # compared are their sum.
    cfgs = co["configs"]
    axs = {tuple(sorted(c["permitted_axioms"])) for c in cfgs}
    if any(c.get("result", co["result"]) != "pass" for c in cfgs) or len(axs) != 1:
        raise SystemExit("comparator receipt: a configuration did not pass, or the permitted axioms differ")
    names = [n for c in cfgs for n in c["theorem_names"]]
    if len(names) != len(set(names)):
        raise SystemExit("comparator receipt: a theorem is compared in more than one configuration")
    return {"result": co["result"],
            "theorems": len(names),
            "configs": [{"path": c.get("path"), "result": c.get("result", co["result"]),
                         "theorems": len(c["theorem_names"]),
                         "permitted_axioms": sorted(c["permitted_axioms"])} for c in cfgs],
            "permitted_axioms": sorted(next(iter(axs))),
            "lean_pkg_version": co["producer"]["lean_pkg"]}


# Computed from the receipt on every path, including the stored-summary path below, so a
# stored summary can never carry a stale comparator block.
comparator = comparator_summary(co)
ledger = json.loads(subprocess.run(
    ["lean-pkg", "claims", "ledger", "--json", "stratonovich-ham-second-moment-lean"],
    capture_output=True, text=True).stdout or "{}")  # non-zero exit = ledger not ready; judged below

if ledger.get("bound_commit") != full or not ledger.get("ok"):
    # lean-pkg evaluates the ledger against the clone's local HEAD. If HEAD has
    # moved on (new work in progress) but the stored summary is already for
    # this verified commit, keep it: the receipts and the ledger it records are
    # bound to the same commit and did not change.
    summ = os.path.join(HERE, "lean-receipt-summary.json")
    stored = json.load(open(summ)) if os.path.exists(summ) else {}
    if stored.get("commit") == full:
        print(f"note: ledger bound to {str(ledger.get('bound_commit'))[:7]}, ok={ledger.get('ok')} "
              f"against the clone's HEAD; kept the stored summary for {full[:7]}, "
              "with its comparator block recomputed from the receipt")
        stored["comparator"] = comparator
        out["lean-receipt-summary.json"] = json.dumps(stored, indent=2) + "\n"
        write_all(out)
        sys.exit(0)
    raise SystemExit(f"claims ledger is bound to {str(ledger.get('bound_commit'))[:7]} "
                     f"(ok={ledger.get('ok')}), not a finished ledger at {full[:7]}")
ca = lo.get("claim_axioms", {})
count = lambda v: len(v) if isinstance(v, list) else v
summary = {
    "commit": full,
    "lean_pkg_version": lo["producer"]["lean_pkg"],
    "lower": {"sorry_count": lo["sorry_count"], "axioms": sorted(lo["axioms"]),
              "claims_checked": count(ca.get("checked")),
              "claims_nonstandard": count(ca.get("nonstandard")),
              "claims_missing": count(ca.get("missing"))},
    "comparator": comparator,
    "ledger": {"ok": ledger.get("ok"), "verified": ledger["counts"].get("verified"),
               "open": ledger["counts"].get("open"),
               "out_of_scope": ledger["counts"].get("out-of-scope")},
}
out["lean-receipt-summary.json"] = json.dumps(summary, indent=2) + "\n"
write_all(out)
print(json.dumps(summary, indent=2))
