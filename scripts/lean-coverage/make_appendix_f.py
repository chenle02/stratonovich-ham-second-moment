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
WORDS = {0: "no", 1: "one", 2: "two", 3: "three", 4: "four", 5: "five"}  # counts in prose
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


COMPLETION_STATUS = [  # COMPLETION.md status -> (coverage key, wording in the book)
    ("formalized, manuscript hypotheses", ("same-assumptions", "full"),
     "Formalized with the paper's own hypotheses"),
    ("formalized, manuscript hypotheses, narrower conclusion", ("same-assumptions", "weaker"),
     "With the paper's hypotheses; narrower conclusion"),
    ("inputs supplied, every conclusion proved", ("inputs-supplied", "full"),
     "Every conclusion proved; inputs supplied"),
    ("inputs supplied, steps/narrower", ("inputs-supplied", "weaker"),
     "Steps checked; inputs supplied"),
    ("outside Lean (main theorem)", ("outside", "full"), "Main theorems outside Lean"),
    ("not formalized", None, "Not formalized"),
]
NUMBERED = ("T:", "P:", "L:", "C:")


def md_table(lines, start):
    """Rows of the first Markdown table after the line starting with `start`."""
    i = next(k for k, l in enumerate(lines) if l.startswith(start))
    rows, seen = [], False
    for l in lines[i + 1:]:
        if l.startswith("|"):
            seen = True
            cells = [c.strip() for c in l.strip().strip("|").split("|")]
            if not set("".join(cells)) <= set("-: "):
                rows.append(cells)
        elif seen:
            break
    return rows[1:]  # drop the header row


def completion_tex(path, rows, numbers, commit, sm):
    """Completion and milestone tables from the pinned COMPLETION.md, checked
    against coverage.yaml, the book's labels and the receipt summary."""
    lines = open(path).read().splitlines()
    comp = md_table(lines, "## Completion by labelled result")
    by_status = {r[0]: int(r[1]) for r in comp}
    total = by_status.pop("total labelled results (Theorem, Proposition, Lemma, Corollary)")
    # The numbered no-gos of Chapter 12 (aux anchor "nogo.") are counted in
    # Appendix G, not here, although their labels start with "P:".
    nogos = set(re.findall(r"\\newlabel\{([^}]+)\}\{\{[^}]*\}\{[^}]*\}\{.*?\}\{nogo\.", AUXTEXT))
    book = {k for k in numbers if k.startswith(NUMBERED) and k not in nogos}
    listed = {r[0].strip("`") for r in md_table(lines, "## Every labelled result")}
    if total != len(listed) or listed - book:
        raise SystemExit(f"COMPLETION.md lists {len(listed)} labelled results (total {total}); "
                         f"missing from the book: {sorted(listed - book)[:5]}")
    # Results added to the book after the companion's manuscript revision: they
    # are not in the record and cannot be covered, so they count as not formalized.
    added = book - listed
    covered_labels = {r["paper"]["label"] for r in rows}
    if added & covered_labels:
        raise SystemExit(f"labels covered but missing from COMPLETION.md: {sorted(added & covered_labels)[:5]}")
    cov = collections.Counter((r["class"], r.get("conclusion", "full")) for r in rows
                              if r["paper"]["label"].startswith(NUMBERED))
    covered = 0
    for status, key, _ in COMPLETION_STATUS:
        if key is not None:
            if by_status[status] != cov[key]:
                raise SystemExit(f"COMPLETION.md '{status}' = {by_status[status]}, coverage.yaml has {cov[key]}")
            covered += cov[key]
    if by_status["not formalized"] != total - covered:
        raise SystemExit("COMPLETION.md 'not formalized' does not equal the uncovered results")
    by_status["not formalized"] += len(added)
    total = len(book)
    other = [r["paper"]["label"] for r in rows if not r["paper"]["label"].startswith(NUMBERED)]
    same_full_all = sum(1 for r in rows if (r["class"], r.get("conclusion", "full")) == ("same-assumptions", "full"))
    if same_full_all - cov[("same-assumptions", "full")] != sum(
            1 for r in rows if not r["paper"]["label"].startswith(NUMBERED)
            and (r["class"], r.get("conclusion", "full")) == ("same-assumptions", "full")):
        raise SystemExit("display/remark rows are not all same-assumptions full")
    ctab = ["\\begin{tabular}{@{}lrr@{}}\n  \\toprule\n  Status & Results & Share \\\\\n  \\midrule\n"]
    for status, _, wording in COMPLETION_STATUS:
        n = by_status[status]
        ctab.append(f"  {wording} & {n} & {round(100 * n / total)}\\% \\\\\n")
    ctab.append(f"  \\midrule\n  Total & {total} & 100\\% \\\\\n  \\bottomrule\n\\end{{tabular}}\n")

    ms = md_table(lines, "## Milestones")
    last = ms[-1]
    if last[1].strip("`") != commit[:7]:
        raise SystemExit(f"the last milestone is {last[1]}, the verified commit is {commit[:7]}")
    if sm and (int(last[4]) != sm["lower"]["claims_checked"] or int(last[5]) != sm["comparator"]["theorems"]):
        raise SystemExit("the last milestone's claims or theorems differ from the receipts")
    if int(last[6].split(":")[0]) != len(rows):
        raise SystemExit("the last milestone's coverage rows differ from coverage.yaml")
    mtab = ["\\begin{tabular}{@{}llrrr@{}}\n  \\toprule\n  Stage & Date & Claims & Theorems & Results covered \\\\\n  \\midrule\n"]
    for r in ms:
        d = dt.date.fromisoformat(r[2])
        mtab.append(f"  \\texttt{{{tex_escape(r[0].strip('`'))}}} & {d.strftime('%B')}~{d.day} & "
                    f"{r[4]} & {r[5]} & {r[6].split(':')[0]} \\\\\n")
    mtab.append("  \\bottomrule\n\\end{tabular}\n")
    return [
        "\\newcommand{\\lcCompletionTable}{%\n" + "".join(ctab) + "}\n",
        "\\newcommand{\\lcMilestoneTable}{%\n" + "".join(mtab) + "}\n",
        f"\\newcommand{{\\lcNumberedTotal}}{{{total}}}\n",
        f"\\newcommand{{\\lcNotFormalized}}{{{by_status['not formalized']}}}\n",
        f"\\newcommand{{\\lcNotFormalizedShare}}{{{round(100 * by_status['not formalized'] / total)}}}\n",
        f"\\newcommand{{\\lcOutsideNumbered}}{{{WORDS.get(by_status['outside Lean (main theorem)'], by_status['outside Lean (main theorem)'])}}}\n",
        f"\\newcommand{{\\lcSameFullNumbered}}{{{cov[('same-assumptions', 'full')]}}}\n",
        f"\\newcommand{{\\lcSameFullAll}}{{{same_full_all}}}\n",
        f"\\newcommand{{\\lcOtherRows}}{{{len(other)}}}\n",
        f"\\newcommand{{\\lcFirstStageDate}}{{{dt.date.fromisoformat(ms[0][2]).strftime('%B')}~{dt.date.fromisoformat(ms[0][2]).day}}}\n",
        f"\\newcommand{{\\lcRecordTotal}}{{{len(listed)}}}\n",
        f"\\newcommand{{\\lcAddedSinceRecord}}{{{len(added)}}}\n",
        "\\newcommand{\\lcHaveCompletion}{1}\n",
    ]


def main():
    cov = yaml.safe_load(open(os.path.join(HERE, "coverage.yaml")))
    commit, date = open(os.path.join(HERE, "coverage-commit.txt")).read().split()[:2]
    cov_commit = open(os.path.join(HERE, "coverage-commit.txt")).read().split()[2]
    # A coverage commit other than the verified one must be either a
    # docs-only successor (checked by pin_companion.py when it pins) or carry
    # the record of the companion's successor check for exactly this pair.
    sc_path = os.path.join(HERE, "successor-check.json")
    if os.path.exists(sc_path):
        sc = json.load(open(sc_path))
        if (sc.get("verdict") != "ALLOWED-SUCCESSOR" or sc.get("failures")
                or sc.get("verified") != commit or sc.get("coverage") != cov_commit):
            raise SystemExit("successor-check.json does not allow this verified/coverage pair")
    head = open(os.path.join(HERE, "coverage.yaml")).read().splitlines()
    m = next((re.match(r"#\s*(\d+) further claims", l) for l in head[:10]
              if re.match(r"#\s*(\d+) further claims", l)), None)
    unlabelled = m.group(1) if m else None
    global AUXTEXT
    aux = AUXTEXT = open(AUX).read()
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

    # Typeset wording of the scope sentences and of the supplied inputs,
    # written and checked by the companion's maintainer side
    # (coverage-payload-tex.yaml): per label the ASCII of coverage.yaml (so
    # that drift is detected), the sentence in TeX, its two parts ("Lean
    # proves" / "Not yet formalized") and one TeX item per supplied input.
    payload = {}
    pl_path = os.path.join(HERE, "coverage-payload-tex.yaml")
    if os.path.exists(pl_path):
        for r in yaml.safe_load(open(pl_path))["rows"]:
            row = next((x for x in rows if x["paper"]["label"] == r["label"]), None)
            if row is None:
                raise SystemExit(f"coverage-payload-tex.yaml: unknown label {r['label']}")
            if (r.get("ascii") or "") and r["ascii"] != row.get("conclusion_scope"):
                raise SystemExit(f"coverage-payload-tex.yaml has drifted from coverage.yaml at {r['label']} (scope)")
            want = [x for x in (row.get("inputs") or [])]
            got = [i["ascii"] for i in (r.get("inputs_tex") or [])]
            if got != want:
                raise SystemExit(f"coverage-payload-tex.yaml has drifted from coverage.yaml at {r['label']} (inputs)")
            payload[r["label"]] = r

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
            scope_tex_r = scope_tex.get(p["label"]) or r.get("conclusion_scope_tex")
            scope = r.get("conclusion_scope")
            inputs = r.get("inputs") or []
            if key[0] == "inputs-supplied" and not inputs:
                raise SystemExit(f"{p['label']}: inputs supplied, but coverage.yaml names none")
            detailed = key != ("same-assumptions", "full") and (scope_tex_r or scope or inputs)
            if not detailed:
                # A row of the two-column list: reference and title. One
                # small table per row, so that a group can break across pages.
                line = f"  {ref(p['label'])} & {tex_escape(p['title'])}"
                body.append("\\begin{lcTable}\n" + line + "\n\\end{lcTable}\n")
                continue
            # A result that is not formalized in full gets a full-width
            # entry: reference and title on one line, then what Lean proves,
            # what is not formalized, and the supplied inputs one by one.
            # Line numbers of the companion's manuscript copy do not match
            # this book and are never printed; a draft may (LC_DRAFT=1).
            ent = [f"\\lcEntry{{{ref(p['label'])}}}{{{tex_escape(p['title'])}}}\n"]
            pl = payload.get(p["label"])
            if payload and pl is None:
                raise SystemExit(f"{p['label']}: no typeset wording in coverage-payload-tex.yaml")
            if pl:
                parts = [pl.get("proved_tex") or "", pl.get("not_formalized_tex") or "", pl.get("tex") or ""]
                items = [i["tex"] for i in (pl.get("inputs_tex") or [])]
            else:
                parts = ["", "", scope_tex_r or ""]
                items = None
            # Line numbers of the companion's manuscript copy do not match
            # this book and are never printed.
            for x in parts + (items or inputs):
                if re.search(r"\blines? \d|\bl\. ?\d", x):
                    raise SystemExit(f"{p['label']}: text with manuscript line numbers: {x[:80]}")
            if parts[0]:
                ent.append(f"\\lcPart{{Lean proves}}{{{tex_with_refs(parts[0])}}}\n")
                if parts[1]:
                    ent.append(f"\\lcPart{{Not yet formalized}}{{{tex_with_refs(parts[1])}}}\n")
            elif parts[2]:
                ent.append(f"\\lcText{{{tex_with_refs(parts[2])}}}\n")
            elif scope:
                ent.append(f"\\lcText{{{text_with_refs(scope)}}}\n")
            if inputs:
                word = "Input supplied" if len(inputs) == 1 else "Inputs supplied"
                ent.append(f"\\lcInputs{{{word}}}\n")
                for k, x in enumerate(inputs, 1):
                    txt = tex_with_refs(items[k - 1]) if items is not None else text_with_refs(x.strip())
                    ent.append(f"\\lcInput{{{k}}}{{{txt}}}\n")
            ent.append("\\lcEntryEnd\n")
            body.append("".join(ent))
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
            "\\newcommand{\\lcHaveReceipts}{1}\n"]
        # The claims ledger may be unavailable at the pinned commit (null in
        # the summary): then the verified/open sentence is not printed.
        if le:
            receipts += [f"\\newcommand{{\\lcVerified}}{{{le['verified']}}}\n",
                         f"\\newcommand{{\\lcOpen}}{{{le['open']}}}\n",
                         "\\newcommand{\\lcHaveLedger}{1}\n"]
    comp_path = os.path.join(HERE, "completion.md")
    completion = (completion_tex(comp_path, rows, numbers, commit,
                                 json.load(open(summ_path)) if os.path.exists(summ_path) else None)
                  if os.path.exists(comp_path) else [])
    # Key to the registered model choices (M1, M2, ...), when the companion
    # supplies one: \item lines, printed as they are.
    key_path = os.path.join(HERE, "model-key.tex")
    model_key = []
    if os.path.exists(key_path):
        items = [l for l in open(key_path).read().splitlines() if l.startswith("\\item")]
        used = set(re.findall(r"\bM\d\b", "".join(body)))
        have = set(re.findall(r"\\item\[(M\d)\]", "\n".join(items)))
        if used - have:
            raise SystemExit(f"model codes used in the rows without a key: {sorted(used - have)}")
        model_key = ["\\newcommand{\\lcModelKey}{%\n" + "\n".join(items) + "\n}\n"]
    d = dt.date.fromisoformat(date[:10])
    out = ["% Generated by make_appendix_f.py from coverage.yaml; do not edit by hand.\n",
           f"\\newcommand{{\\lcCommit}}{{{commit[:7]}}}\n",
           f"\\newcommand{{\\lcDate}}{{{d.strftime('%B')}~{d.day}, {d.year}}}\n",
           f"\\newcommand{{\\lcTime}}{{{time_stamp(date)}}}\n",
           f"\\newcommand{{\\lcRows}}{{{len(rows)}}}\n",
           f"\\newcommand{{\\lcSummary}}{{{text_with_refs(cov['summary'])}}}\n",  # labels become references
           f"\\newcommand{{\\lcUnlabelled}}{{{unlabelled}}}\n",
           f"\\newcommand{{\\lcGroups}}{{{WORDS[sum(1 for k, _ in CATEGORIES if by_cat.get(k))]}}}\n",
           "\\newcommand{\\lcTables}{%\n" + "".join(body) + "}\n"] + receipts + completion + model_key
    open(OUT, "w").write("".join(out))
    print(f"{len(rows)} rows; categories {[ (k, len(by_cat.get(k, []))) for k, _ in CATEGORIES ]}; "
          f"unlabelled {unlabelled}; commit {commit[:7]}")


if __name__ == "__main__":
    main()
