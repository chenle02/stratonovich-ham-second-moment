#!/usr/bin/env python3
"""Generate lean-coverage-data.tex for Appendix F ("What Lean checks").

Inputs (beside this script, written by pin_companion.py):
  coverage.yaml               pinned copy of the Lean companion's coverage file
  coverage-scope-tex.yaml     LaTeX versions of the narrower-conclusion sentences
  coverage-commit.txt         verified commit, its date, and the coverage commit
  lean-receipt-summary.json   numbers from the receipts and the claims ledger
and the book's .aux file (argument 1, default notes/...aux), used to check that
every label exists. Output: notes/lean-coverage-data.tex (argument 2).

Every row's text is read from coverage.yaml; nothing is retyped. Book labels
inside scope sentences become references; LaTeX special characters are
escaped. Categories and their wording follow the companion's README.
"""
import collections
import json
import datetime as dt
import os
import re
import sys

import yaml

HERE = os.path.dirname(os.path.abspath(__file__))
AUX = sys.argv[1] if len(sys.argv) > 1 else os.path.join(
    os.path.dirname(os.path.abspath(__file__)), "..", "..", "notes", "notes_stratonovich_ham_second_moment.aux")
ROOT = os.path.abspath(os.path.join(HERE, "..", ".."))
OUT = sys.argv[2] if len(sys.argv) > 2 else os.path.join(ROOT, "notes", "lean-coverage-data.tex")

CATEGORIES = [  # (class, conclusion) -> wording from the companion README
    (("same-assumptions", "full"),
     "Formalized with the paper's own hypotheses; nothing supplied."),
    (("same-assumptions", "weaker"),
     "With the paper's hypotheses; Lean proves a narrower conclusion."),
    (("inputs-supplied", "full"),
     "Every conclusion proved; named analytic inputs supplied as hypotheses."),
    (("inputs-supplied", "weaker"),
     "Steps checked, not the result itself; analytic inputs supplied as hypotheses."),
    (("outside", "full"), "Not formalized."),
]
PREFIX_KIND = {"T": "Theorem", "L": "Lemma", "P": "Proposition", "C": "Corollary",
               "R": "Remark", "D": "Definition", "H": "Hypothesis", "E": "Equation",
               "S": "Section", "SS": "Section"}


def tex_escape(s):
    s = re.sub(r'"([^"]*)"', lambda m: "\x01" + m.group(1) + "\x02", s)  # paired quotes
    out = []
    for ch in s:
        out.append({"\\": r"\textbackslash{}", "&": r"\&", "%": r"\%", "$": r"\$",
                    "#": r"\#", "_": r"\_", "{": r"\{", "}": r"\}",
                    "~": r"\textasciitilde{}", "^": r"\textasciicircum{}",
                    ">": r"\textgreater{}", "<": r"\textless{}"}.get(ch, ch))
    return "".join(out).replace("\x01", "``").replace("\x02", "''")


def time_stamp(iso):
    """'2026-11-11T08:41:56-05:00' -> '8:41~a.m.\\ (UTC$-$5)'."""
    t = dt.datetime.fromisoformat(iso)
    h = t.hour % 12 or 12
    off = t.utcoffset().total_seconds() / 3600
    sign = "$-$" if off < 0 else "+"
    off_s = f"{abs(off):g}"
    return f"{h}:{t.minute:02d}~{'a.m.' if t.hour < 12 else 'p.m.'}\\ (UTC{sign}{off_s})"


def main():
    cov = yaml.safe_load(open(os.path.join(HERE, "coverage.yaml")))
    commit, date = open(os.path.join(HERE, "coverage-commit.txt")).read().split()[:2]
    head = open(os.path.join(HERE, "coverage.yaml")).read().splitlines()
    m = next((re.match(r"#\s*(\d+) further claims", l) for l in head[:10]
              if re.match(r"#\s*(\d+) further claims", l)), None)
    unlabelled = m.group(1) if m else None
    aux = open(AUX).read()
    numbers = {k: v for k, v in re.findall(r"\\newlabel\{([^}]+)\}\{\{([^}]*)\}", aux)}

    rows = cov["rows"]
    missing = [r["paper"]["label"] for r in rows if r["paper"]["label"] not in numbers]
    if missing:
        raise SystemExit(f"labels missing from the book: {missing}")

    def ref(label):
        kind = PREFIX_KIND.get(label.split(":", 1)[0], "")
        return f"\\lcRef{{{kind}}}{{{label}}}{{{numbers[label]}}}"

    def text_with_refs(s):
        """Escape plain text; turn known book labels into references."""
        parts = re.split(r"\b((?:SS|[TLPCRDHES]):[A-Za-z0-9-]+)\b", s)
        out = []
        for i, p in enumerate(parts):
            if i % 2 == 1 and p in numbers:
                out.append(ref(p))
            else:
                out.append(tex_escape(p))
        return "".join(out)

    def tex_with_refs(s):
        """LaTeX from coverage.yaml: keep $...$ math as written; turn bare book
        labels outside math into references; leave other text unchanged."""
        pieces = re.split(r"(\$[^$]*\$)", s)
        out = []
        for piece in pieces:
            if piece.startswith("$") and piece.endswith("$") and len(piece) > 1:
                out.append(piece)
                continue
            parts = re.split(r"\b((?:SS|[TLPCRDHES]):[A-Za-z0-9-]+)\b", piece)
            for i, q in enumerate(parts):
                if i % 2 == 1:
                    if q not in numbers:
                        raise SystemExit(f"unknown label in conclusion_scope_tex: {q}")
                    out.append(ref(q))
                else:
                    out.append(q)
        return "".join(out)

    scope_tex = {}
    st_path = os.path.join(HERE, "coverage-scope-tex.yaml")
    if os.path.exists(st_path):
        for r in yaml.safe_load(open(st_path))["rows"]:
            row = next(x for x in rows if x["paper"]["label"] == r["label"])
            if r["ascii"] != row.get("conclusion_scope"):
                raise SystemExit(f"coverage-scope-tex.yaml has drifted from coverage.yaml at {r['label']}")
            scope_tex[r["label"]] = r["tex"]

    by_cat = collections.defaultdict(list)
    for r in rows:
        by_cat[(r["class"], r.get("conclusion", "full"))].append(r)
    unknown = set(by_cat) - {k for k, _ in CATEGORIES}
    if unknown:
        raise SystemExit(f"unknown categories in coverage.yaml: {unknown}")

    body = []
    for key, wording in CATEGORIES:
        rs = by_cat.get(key, [])
        if not rs:
            continue
        body.append(f"\\lcCategory{{{tex_escape(wording)}}}{{{len(rs)}}}\n")

        def order(r):  # book order: chapters by number, then appendices A, B, ...
            parts = numbers[r["paper"]["label"]].split(".")
            return [(0, int(x)) if x.isdigit() else (1, x) for x in parts]
        for r in sorted(rs, key=order):
            p = r["paper"]
            line = f"  {ref(p['label'])} & {tex_escape(p['title'])}"
            scope_tex_r = scope_tex.get(p["label"]) or r.get("conclusion_scope_tex")
            scope = r.get("conclusion_scope")
            if key == ("same-assumptions", "weaker") and (scope_tex_r or scope):
                txt = tex_with_refs(scope_tex_r) if scope_tex_r else text_with_refs(scope)
                line += f"\\newline{{\\footnotesize {txt}}}"
            # One small table per row, so that a long group can break across
            # pages between rows (a single tabular cannot break).
            body.append("\\begin{lcTable}\n" + line + "\n\\end{lcTable}\n")
        body.append("\n")

    summ_path = os.path.join(HERE, "lean-receipt-summary.json")
    receipts = []
    if os.path.exists(summ_path):
        sm = json.load(open(summ_path))
        if sm["commit"] != commit:
            raise SystemExit("lean-receipt-summary.json is for a different commit than coverage.yaml")
        lo, co, le = sm["lower"], sm["comparator"], sm["ledger"]
        std = ["Classical.choice", "Quot.sound", "propext"]
        if lo["sorry_count"] != 0 or lo["axioms"] != std or lo["claims_nonstandard"] or lo["claims_missing"]:
            raise SystemExit("receipt shows unproved steps or non-standard axioms: the paragraph would be false")
        if co["result"] != "pass" or co["permitted_axioms"] != std:
            raise SystemExit("comparator receipt did not pass with the standard axioms")
        receipts = [
            f"\\newcommand{{\\lcLeanPkgVersion}}{{{sm['lean_pkg_version']}}}\n",
            f"\\newcommand{{\\lcClaimsChecked}}{{{lo['claims_checked']}}}\n",
            f"\\newcommand{{\\lcComparatorTheorems}}{{{co['theorems']}}}\n",
            f"\\newcommand{{\\lcVerified}}{{{le['verified']}}}\n",
            f"\\newcommand{{\\lcOpen}}{{{le['open']}}}\n",
            "\\newcommand{\\lcHaveReceipts}{1}\n"]
    d = dt.date.fromisoformat(date[:10])
    out = ["% Generated by make_appendix_f.py from coverage.yaml; do not edit by hand.\n",
           f"\\newcommand{{\\lcCommit}}{{{commit[:7]}}}\n",
           f"\\newcommand{{\\lcDate}}{{{d.strftime('%B')}~{d.day}, {d.year}}}\n",
           f"\\newcommand{{\\lcTime}}{{{time_stamp(date)}}}\n",
           f"\\newcommand{{\\lcRows}}{{{len(rows)}}}\n",
           f"\\newcommand{{\\lcSummary}}{{{tex_escape(cov['summary'])}}}\n",
           f"\\newcommand{{\\lcUnlabelled}}{{{unlabelled}}}\n",
           "\\newcommand{\\lcTables}{%\n" + "".join(body) + "}\n"] + receipts
    open(OUT, "w").write("".join(out))
    print(f"{len(rows)} rows; categories {[ (k, len(by_cat.get(k, []))) for k, _ in CATEGORIES ]}; "
          f"unlabelled {unlabelled}; commit {commit[:7]}")


if __name__ == "__main__":
    main()
