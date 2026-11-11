#!/usr/bin/env python3
"""Pin the Lean companion's coverage file and receipt numbers for Appendix F.

Usage: pin_companion.py COMPANION_REPO VERIFIED_COMMIT [COVERAGE_COMMIT]
VERIFIED_COMMIT is the commit the receipts and the claims ledger are bound
to (the one the book quotes). COVERAGE_COMMIT (default: the same) is where
coverage.yaml is read; it must descend from VERIFIED_COMMIT through commits
that change only files the Lean build does not read (the companion's
docs-only rule in lean-pkg-binding.yaml).
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
repo, commit = sys.argv[1], sys.argv[2]
cov_commit = sys.argv[3] if len(sys.argv) > 3 else commit
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
        raise SystemExit(f"commits after the verified commit change build inputs: {build}")
open(os.path.join(HERE, "coverage.yaml"), "w").write(git("show", f"{cov_full}:coverage.yaml"))
open(os.path.join(HERE, "coverage-commit.txt"), "w").write(f"{full}\n{date}\n{cov_full}\n")

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
    open(os.path.join(HERE, "coverage-scope-tex.yaml"), "w").write(
        git("show", f"{cov_full}:docs/coverage-scope-tex.yaml"))
if lo.get("schema") != "lower-receipt/1" or co.get("schema") != "comparator-receipt/2":
    raise SystemExit("unexpected receipt schema")
for r in (lo, co):
    if r.get("commit") != full:
        raise SystemExit("receipt is bound to a different commit")
ledger = json.loads(subprocess.run(
    ["lean-pkg", "claims", "ledger", "--json", "stratonovich-ham-second-moment-lean"],
    capture_output=True, text=True, check=True).stdout)

if ledger.get("bound_commit") != full or not ledger.get("ok"):
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
    "comparator": {"result": co["result"],
                   "theorems": len(co["configs"][0]["theorem_names"]),
                   "permitted_axioms": sorted(co["configs"][0]["permitted_axioms"]),
                   "lean_pkg_version": co["producer"]["lean_pkg"]},
    "ledger": {"ok": ledger.get("ok"), "verified": ledger["counts"].get("verified"),
               "open": ledger["counts"].get("open"),
               "out_of_scope": ledger["counts"].get("out-of-scope")},
}
json.dump(summary, open(os.path.join(HERE, "lean-receipt-summary.json"), "w"), indent=2)
print(json.dumps(summary, indent=2))
