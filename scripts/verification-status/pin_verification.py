#!/usr/bin/env python3
"""Pin the results table of the verification ledger for Appendix G.

Usage: pin_verification.py LEDGER.md

LEDGER.md is the verification ledger (VERIFICATION.md at the root of the
released repository). The script copies its results table, unchanged, into
verification.md beside this script, with two provenance lines: the date of
the last commit that changed the ledger, and the commit of the Lean
companion's coverage file from which the ledger's Lean column was taken.
make_appendix_g.py reads only the pinned copy, so the book does not change
when the ledger changes until the ledger is pinned again.
"""
import os
import re
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "verification.md")
HEADER = "| Label | Group | Kind | Title | File | AI review | Lean | Human |"


def main():
    if len(sys.argv) != 2:
        raise SystemExit(__doc__)
    src = os.path.abspath(sys.argv[1])
    lines = open(src, encoding="utf-8").read().splitlines()
    try:
        i = lines.index(HEADER)
    except ValueError:
        raise SystemExit(f"results table header not found in {src}")
    table = [lines[i], lines[i + 1]]
    for line in lines[i + 2:]:
        if not line.startswith("|"):
            break
        table.append(line)
    m = re.search(r"`coverage\.yaml`.*? at its commit `([0-9a-f]{7,40})`", "\n".join(lines), re.S)
    if not m:
        raise SystemExit("the ledger does not name the coverage commit of its Lean column")
    if subprocess.run(["git", "-C", os.path.dirname(src), "diff", "--quiet", "HEAD", "--", src]).returncode:
        raise SystemExit(f"{src} has uncommitted changes; pin a committed ledger")
    date = subprocess.run(["git", "-C", os.path.dirname(src), "log", "-1", "--format=%cI", "--", src],
                          check=True, capture_output=True, text=True).stdout.strip()
    if not date:
        raise SystemExit(f"{src} is not committed")
    with open(OUT, "w", encoding="utf-8") as f:
        f.write("<!-- Pinned by pin_verification.py from the verification ledger; do not edit by hand. -->\n")
        f.write(f"ledger-date: {date}\n")
        f.write(f"lean-coverage-commit: {m.group(1)}\n\n")
        f.write("\n".join(table) + "\n")
    print(f"pinned {len(table) - 2} rows (ledger {date}, Lean column at {m.group(1)}) -> {OUT}")


if __name__ == "__main__":
    main()
