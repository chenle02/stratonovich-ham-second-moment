#!/usr/bin/env python3
"""Generate verification-status-data.tex for Appendix G ("How far each result
has been checked").

Inputs:
  verification.md   pinned results table of the verification ledger
                    (written by pin_verification.py)
  ../lean-coverage/coverage.yaml   the Lean coverage file pinned for Appendix F
  the book's .aux file (argument 1, default notes/...aux)
Output: notes/verification-status-data.tex (argument 2).

Nothing is retyped: every count is computed from the pinned table. The script
stops if the table and the book disagree (a label missing or added, a result
in the wrong group) or if the table's Lean column disagrees with the coverage
file that Appendix F uses.
"""
import collections
import datetime as dt
import os
import re
import sys

import yaml

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", ".."))
AUX = sys.argv[1] if len(sys.argv) > 1 else os.path.join(
    ROOT, "notes", "notes_stratonovich_ham_second_moment.aux")
OUT = sys.argv[2] if len(sys.argv) > 2 else os.path.join(ROOT, "notes", "verification-status-data.tex")
LEDGER = os.path.join(HERE, "verification.md")
COVERAGE = os.path.join(ROOT, "scripts", "lean-coverage", "coverage.yaml")

GROUPS = ["I", "II", "III", "IV", "V"]
ENVS = {"theorem", "proposition", "lemma", "corollary", "nogo"}
# Ledger wording of the Lean column -> (coverage class, conclusion), in table order.
LEAN = [
    ("formalized in full", ("same-assumptions", "full")),
    ("formalized, narrower conclusion", ("same-assumptions", "weaker")),
    ("every conclusion, inputs supplied", ("inputs-supplied", "full")),
    ("steps checked", ("inputs-supplied", "weaker")),
    ("outside Lean", ("outside", "full")),
    ("no Lean claim", None),
]
SHOWN = {"steps checked": "Steps checked; inputs supplied or left outside Lean"}  # wording of Appendix F
WORDS = {1: "one", 2: "two", 3: "three", 4: "four"}
MONTHS = ["January", "February", "March", "April", "May", "June", "July",
          "August", "September", "October", "November", "December"]


def group_of(number, env):
    """Proof group of a result from its number in the book."""
    if env == "nogo":
        return "V"
    head = number.split(".")[0]
    if head.isdigit():
        ch = int(head)
        return "I" if ch <= 3 else "II" if ch <= 7 else "III" if ch <= 11 else None
    return "IV" if head in "ABCD" else None


def main():
    aux = {}
    for m in re.finditer(r"\\newlabel\{([^}]*)\}\{\{([^}]*)\}\{[^}]*\}\{.*?\}\{([a-zA-Z]+)\.[^}]*\}\{\}\}",
                         open(AUX, encoding="utf-8").read()):
        aux[m.group(1)] = (m.group(2), m.group(3))
    book = {k: v for k, v in aux.items() if v[1] in ENVS and k[:2] in ("T:", "P:", "L:", "C:")}

    text = open(LEDGER, encoding="utf-8").read()
    date = re.search(r"^ledger-date: (\S+)$", text, re.M).group(1)
    lean_commit = re.search(r"^lean-coverage-commit: (\S+)$", text, re.M).group(1)
    rows = []
    for line in text.splitlines():
        if line.startswith("| `"):
            c = [x.strip() for x in line.strip().strip("|").split("|")]
            rows.append({"label": c[0].strip("`"), "group": c[1], "ai": c[5], "lean": c[6], "human": c[7]})

    labels = [r["label"] for r in rows]
    if len(set(labels)) != len(labels):
        raise SystemExit("duplicate labels in the ledger")
    if set(labels) != set(book):
        raise SystemExit(f"ledger and book differ: not in book {sorted(set(labels) - set(book))[:5]}, "
                         f"not in ledger {sorted(set(book) - set(labels))[:5]}")
    for r in rows:
        g = group_of(*book[r["label"]])
        if g != r["group"]:
            raise SystemExit(f"{r['label']} is in group {r['group']} in the ledger, {g} in the book")

    cov = {row["paper"]["label"]: row for row in yaml.safe_load(open(COVERAGE))["rows"]}
    counts = collections.Counter()
    for r in rows:
        m = re.fullmatch(r"(.*?)(?: \((\d+) Lean claims?\))?", r["lean"])
        word, n = m.group(1), m.group(2)
        key = dict(LEAN).get(word, "bad")
        if key == "bad":
            raise SystemExit(f"{r['label']}: unknown Lean entry {r['lean']!r}")
        c = cov.get(r["label"])
        got = None if c is None else (c["class"], c.get("conclusion", "full"))
        if got != key:
            raise SystemExit(f"{r['label']}: ledger says {word!r}, Appendix F's coverage file says {got}")
        expected = 0 if c is None or c["class"] == "outside" else len(c.get("claims", []))
        if int(n or 0) != expected:
            raise SystemExit(f"{r['label']}: ledger has {n or 0} Lean claims, coverage file {expected}")
        if r["human"] == "unchecked":
            h = "unchecked"
        elif r["human"].startswith("checked by "):
            h = "checked"
        elif r["human"].startswith("disputed"):
            h = "disputed"
        else:
            raise SystemExit(f"{r['label']}: unknown Human entry {r['human']!r}")
        counts[("lean", word, r["group"])] += 1
        counts[("human", h, r["group"])] += 1
        counts[("all", r["group"])] += 1
        counts[("ai", r["ai"])] += 1
    ai = [k[1] for k in counts if k[0] == "ai"]
    if ai != ["see review record"]:
        raise SystemExit(f"the AI review column now varies ({ai}); the appendix needs a row for it")

    def line(name, key):  # rows unindented: the format-tex hook expects that
        vals = [counts[key + (g,)] for g in GROUPS]
        return name + " & " + " & ".join(map(str, vals)) + f" & {sum(vals)} \\\\"

    t = dt.datetime.fromisoformat(date)
    body = [line("Numbered results", ("all",)), r"\midrule",
            r"\multicolumn{7}{@{}l}{\emph{Lean}} \\"]
    for word, _ in LEAN:
        body.append(line(r"\quad " + SHOWN.get(word, word[0].upper() + word[1:]), ("lean", word)))
    body += [r"\midrule", r"\multicolumn{7}{@{}l}{\emph{Checked by a person}} \\"]
    for h, name in (("checked", "Checked"), ("disputed", "Disputed"), ("unchecked", "Not yet checked")):
        body.append(line(r"\quad " + name, ("human", h)))
    total = lambda *k: sum(counts[k + (g,)] for g in GROUPS)
    out = [
        "% Generated by make_appendix_g.py from verification.md; do not edit by hand.",
        rf"\newcommand{{\vsDate}}{{{MONTHS[t.month - 1]}~{t.day}, {t.year}}}",
        rf"\newcommand{{\vsLeanCommit}}{{{lean_commit}}}",
        rf"\newcommand{{\vsRows}}{{{len(rows)}}}",
        rf"\newcommand{{\vsLeanAny}}{{{len(rows) - total('lean', 'no Lean claim') - total('lean', 'outside Lean')}}}",
        rf"\newcommand{{\vsOutside}}{{{WORDS.get(total('lean', 'outside Lean'), total('lean', 'outside Lean'))}}}",
        rf"\newcommand{{\vsHumanChecked}}{{{total('human', 'checked')}}}",
        rf"\newcommand{{\vsHumanDisputed}}{{{total('human', 'disputed')}}}",
        r"\newcommand{\vsTable}{%",
        *body,
        "}",
    ]
    with open(OUT, "w", encoding="utf-8") as f:
        f.write("\n".join(out) + "\n")
    print(f"{len(rows)} rows -> {OUT}")


if __name__ == "__main__":
    main()
