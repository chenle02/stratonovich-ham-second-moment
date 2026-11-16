#!/usr/bin/env python3
"""Regenerate VERIFICATION.md (the public verification ledger) from the book's TeX and the pinned Lean coverage.

Usage (from the repository root):
    python3 -I scripts/verification/make_verification.py [--read-rev REV] [--tex-rev REV] [--out FILE] [--check]

The ledger has one row per numbered theorem, proposition, lemma, corollary and no-go result, in document
order. Rows are grouped by chapter (config.json). The Lean column comes from the pinned coverage file
(scripts/lean-coverage/coverage.yaml). Human sign-offs already recorded in the current ledger are kept.
Everything except the explanatory prose of the existing file is regenerated, so the output does not depend
on who ran it or where. --check writes nothing and exits 1 if the file would change.
"""
import argparse, json, re, subprocess, sys
from collections import Counter, OrderedDict
from pathlib import Path

try:
    import yaml
except ImportError:
    sys.exit("make_verification.py needs PyYAML (for example: uv run --with pyyaml python -I ...)")

HERE = Path(__file__).resolve().parent
KINDS = {"theorem": "Theorem", "proposition": "Proposition", "lemma": "Lemma", "corollary": "Corollary", "nogo": "No-go"}
PLURAL = {"Theorem": "theorems", "Proposition": "propositions", "Lemma": "lemmas", "Corollary": "corollaries", "No-go": "no-go results"}
WORDS = "zero one two three four five six seven eight nine ten".split()
RESULT_PREFIX = ("T:", "P:", "L:", "C:")


def git(*a):
    return subprocess.run(["git", *a], capture_output=True, text=True, check=True).stdout.strip()


def tex_lines(rel):
    """(file, line, text) of the book in reading order, \\input and \\include expanded, comments stripped."""
    p = rel if rel.endswith(".tex") else rel + ".tex"
    for i, line in enumerate(open(p, encoding="utf-8"), 1):
        line = re.sub(r"(?<!\\)%.*", "", line.rstrip("\n"))
        m = re.search(r"\\(input|include)\{([^}]*)\}", line)
        if m:
            yield from tex_lines(m.group(2))
            continue
        yield p, i, line


def opt_arg(s):
    s = s.lstrip()
    if not s.startswith("["):
        return None
    depth = brace = 0
    for j, c in enumerate(s):
        if c == "{": brace += 1
        elif c == "}": brace -= 1
        elif c == "[" and brace == 0: depth += 1
        elif c == "]" and brace == 0:
            depth -= 1
            if depth == 0:
                return s[1:j]
    return None


def extract(main_tex, groups):
    """Numbered results with label, kind, title, file and group, plus the number of written proofs."""
    stream = list(tex_lines(main_tex))
    group_of = {c: g for g, cs in groups for c in cs}
    chapter, res, proofs = None, [], 0
    i = 0
    while i < len(stream):
        f, ln, l = stream[i]
        m = re.match(r"\s*\\chapter\*?\{[^}]*\}(?:\\label\{([^}]*)\})?", l)
        if m and m.group(1):
            chapter = m.group(1)
        proofs += l.count("\\end{proof}")
        m = re.search(r"\\begin\{(theorem|proposition|lemma|corollary|nogo)\}", l)
        if not m:
            i += 1
            continue
        env, buf, k = m.group(1), l[m.end():], i
        while "\\end{" + env + "}" not in buf:
            k += 1
            buf += "\n" + stream[k][2]
        body = buf.split("\\end{" + env + "}")[0]
        labels = re.findall(r"\\label\{([^}]*)\}", body)
        if not labels:
            sys.exit(f"unlabelled {env} at {f}:{ln}")
        g = group_of.get(chapter)
        if g is None:
            sys.exit(f"no group for chapter {chapter} ({labels[0]}); add it to config.json")
        res.append(dict(kind=KINDS[env], label=labels[0], title=opt_arg(buf), file=f, group=g))
        proofs += sum(stream[j][2].count("\\end{proof}") for j in range(i + 1, k + 1)) if k > i else 0
        i = k + 1
    dup = [k for k, v in Counter(r["label"] for r in res).items() if v > 1]
    if dup:
        sys.exit(f"duplicate labels: {dup}")
    return res, proofs


def clean_title(t):
    if t is None:
        return ""
    t = re.sub(r"\\cite\{([^}]*)\}\*\{([^}]*)\}", r"[\1, \2]", t)
    t = re.sub(r"\\cite\{([^}]*)\}", r"[\1]", t)
    t = t.replace('\\"o', "ö").replace("~", " ").replace("--", "–")
    return re.sub(r"\s+", " ", t).strip().replace("|", "\\|")


def lean_cell(row):
    if row is None:
        return "no Lean claim", "none"
    n = len(row.get("claims") or [])
    nc = f"{n} Lean claim" + ("s" if n != 1 else "")
    k, w = row["class"], row.get("conclusion")
    if k == "outside":
        return "outside Lean", "outside"
    if k == "same-assumptions":
        return (f"formalized, narrower conclusion ({nc})", "same-narrow") if w == "weaker" else (f"formalized in full ({nc})", "same-full")
    if k == "inputs-supplied":
        return (f"inputs supplied ({nc})", "inputs") if w == "weaker" else (f"every conclusion, inputs supplied ({nc})", "inputs-full")
    sys.exit(f"unknown Lean class {k} for {row['paper']['label']}")


def human_cells(text):
    """Human sign-offs already recorded in the current ledger, by label (never regenerated)."""
    out = {}
    for line in text.splitlines():
        m = re.match(r"\| `([^`]+)` \|.*\| ([^|]+) \|$", line)
        if m:
            out[m.group(1)] = m.group(2).strip()
    return out


def build(cfg, read_rev, tex_rev, current):
    res, _ = extract(cfg["main_tex"], cfg["groups"])
    cov_doc = yaml.safe_load(open(cfg["coverage"]))
    cov = OrderedDict((r["paper"]["label"], r) for r in cov_doc["rows"])
    labels = {r["label"] for r in res}
    missing = [l for l in cov if l.startswith(RESULT_PREFIX) and l not in labels]
    if missing:
        sys.exit(f"coverage labels missing from the book: {missing}")
    other = [l for l in cov if not l.startswith(RESULT_PREFIX)]
    anchor = re.search(r"manuscript revision (\w+)", open(cfg["coverage"]).read()).group(1)
    pins = [l.strip() for l in open(cfg["coverage_commit_file"]) if l.strip()]
    verified, coverage_commit = pins[0][:7], pins[-1][:7]
    rec = json.load(open(cfg["receipt_summary"]))
    human = human_cells(current)
    kinds, leanc, gc, first, last, rows = Counter(), Counter(), Counter(), {}, {}, []
    for r in res:
        cell, cls = lean_cell(cov.get(r["label"]))
        kinds[r["kind"]] += 1; leanc[cls] += 1; g = r["group"]; gc[g] += 1
        first.setdefault(g, r["label"]); last[g] = r["label"]
        rows.append(f"| `{r['label']}` | {g} | {r['kind']} | {clean_title(r['title'])} | `{r['file']}` | see review record | {cell} | {human.get(r['label'], 'unchecked')} |")
    outside_main = sum(1 for t in cfg["main_theorems"] if (cov.get(t) or {}).get("class") == "outside")
    doc = current
    legend = f"""## Lean column legend

- `formalized in full`: the result's conclusions are proved in Lean under the manuscript's own hypotheses (sometimes through an exact-hypothesis wrapper of a more general Lean theorem). The setting `H:homog` is modelled in Lean.
- `formalized, narrower conclusion`: as above, but Lean proves only part of the conclusion; the companion's `coverage.yaml` row says which part.
- `every conclusion, inputs supplied`: every conclusion is proved in Lean, with the named analytic inputs entering as explicit hypotheses.
- `inputs supplied`: Lean checks steps, parts or a narrower form of the result, as listed in the companion's statement ledger; analytic and probabilistic facts either enter as explicit hypotheses or stay outside Lean. The result itself is not checked.
- `outside Lean`: recorded in the companion's coverage file but not formalized ({WORDS[outside_main]} of the {WORDS[len(cfg['main_theorems'])]} main theorems; the SPDE, stochastic integrals and analytic asymptotics are outside Lean).
- `no Lean claim`: no Lean declaration is mapped to this label.
- The count in brackets is the number of companion claims mapped to the row. A Lean entry never certifies the analytic inputs, and it is AI-checked correspondence, not human verification.
"""
    doc = re.sub(r"## Lean column legend\n.*?(?=\n## Results)", lambda m: legend, doc, flags=re.S)
    table = "| Label | Group | Kind | Title | File | AI review | Lean | Human |\n|---|---|---|---|---|---|---|---|\n" + "\n".join(rows) + "\n"
    doc = re.sub(r"## Results\n\n\| Label .*?\n(?=\n## Notes)", lambda m: "## Results\n\n" + table, doc, flags=re.S)
    names = [g for g, _ in cfg["groups"]]
    for g in names:
        doc = re.sub(r"(\| " + g + r"\. [^|]*\|[^|]*\|[^|]*\| )\d+( \| )`[^`]*`( \| )`[^`]*`",
                     lambda m: f"{m.group(1)}{gc[g]}{m.group(2)}`{first[g]}`{m.group(3)}`{last[g]}`", doc)
    nwords = WORDS[len(names)]
    doc = re.sub(r"The \w+ groups have \d+ rows in total[ .].*?(?=\n\n## Lean column legend)",
                 lambda m: f"The {nwords} groups have {len(res)} rows in total ({' + '.join(str(gc[g]) for g in names)}). The Group column of the results table gives each row's group. Row counts are those of this ledger; source sizes count the TeX lines of each chapter and its included files {cfg['source_size_clause']}. The introduction theorems `T:intro-upper` and `T:intro-second-moment` restate `T:full-upper` (group I) and `T:intrinsic-second-moment` (group III); they are rows of group I, where they are stated, and checking them means checking that they agree with the theorems they restate.",
                 doc, flags=re.S)
    other_classes = ", ".join(sorted({cov[e]["class"] for e in other}))
    # Where the Lean column comes from. A released companion is described by
    # the standard sentence; a development state that is not yet released is
    # described by the sentence in config.json ("lean_source_unreleased").
    facts = dict(verified=verified, coverage_commit=coverage_commit, theorems=f"{rec['comparator']['theorems']:,}",
                 claims=f"{rec['lower']['claims_checked']:,}", sorry=rec['lower']['sorry_count'], anchor=anchor,
                 nogo=kinds['No-go'], tex_rev=tex_rev, gate_date=cfg['lean_gate_date'])
    if cfg.get("lean_source_unreleased"):
        lean_source = cfg["lean_source_unreleased"].format(**facts)
    else:
        lean_source = f"""The Lean column is taken from the `coverage.yaml` (class, conclusion and claims of each row) of the public Lean companion, release `{cfg['companion_release']}` (DOI {cfg['companion_doi']}), which is byte-identical to the file of the companion's development repository at its commit `{coverage_commit}`, {cfg['coverage_commit_note'].format(verified=verified)}. The companion's `provenance/DEVELOPMENT.md` maps both development commits to the public release. `{verified}` is where wave {cfg['lean_wave']} was confirmed and both lean-pkg receipts were cut ({rec['comparator']['theorems']:,} theorem claims compared, {rec['lower']['claims_checked']:,} claims, {rec['lower']['sorry_count']} `sorry`, standard axioms only); Le closed the wave-{cfg['lean_wave']} gate on {cfg['lean_gate_date']}. Its manuscript anchor is revision `{anchor}`, so the {kinds['No-go']} no-go results of Chapter 12, added later, have no Lean claim. The companion's `docs/statement-ledger.md` at release `{cfg['companion_release']}` gives the declarations behind each claim. Every theorem, proposition, lemma or corollary label in that coverage file exists at `{tex_rev}`."""
    notes = f"""## Notes

- Results: {len(res)} ({', '.join(f"{kinds[k]} {PLURAL[k]}" for k in PLURAL)}).
- Lean: {leanc['same-full']} formalized in full, {leanc['same-narrow']} formalized with a narrower conclusion, {leanc['inputs-full']} with every conclusion and inputs supplied, {leanc['inputs']} with inputs supplied, {leanc['outside']} outside Lean, {leanc['none']} with no Lean claim.
- `T:first` and `T:crude` restate results of the cited source; their titles give the citation key and pinpoint.
- The companion's coverage file also maps {len(other)} labels that are not numbered theorems, propositions, lemmas or corollaries (displayed equations and a remark), class {other_classes}. They have no rows here.
- Manuscript read at origin/master `{read_rev}`; the book's TeX there is as at `{tex_rev}`. {lean_source}
"""
    doc = re.sub(r"## Notes\n.*\Z", lambda m: notes, doc, flags=re.S)
    return doc


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--config", default=str(HERE / "config.json"))
    ap.add_argument("--ledger", default="VERIFICATION.md", help="the current ledger (prose and human sign-offs are kept)")
    ap.add_argument("--out", default=None, help="default: overwrite --ledger")
    ap.add_argument("--read-rev", default=None, help="default: HEAD, abbreviated")
    ap.add_argument("--tex-rev", default=None, help="default: last commit that changed the book's TeX")
    ap.add_argument("--check", action="store_true", help="write nothing; exit 1 if the ledger would change")
    a = ap.parse_args()
    cfg = json.load(open(a.config))
    read_rev = a.read_rev or git("rev-parse", "--short=7", "HEAD")
    tex_rev = a.tex_rev or git("log", "-1", "--format=%h", "--abbrev=7", "HEAD", "--", "notes/*.tex", "notes/**/*.tex")
    current = open(a.ledger, encoding="utf-8").read()
    new = build(cfg, read_rev, tex_rev, current)
    if a.check:
        if new == current:
            print("VERIFICATION.md: up to date")
            return 0
        print("VERIFICATION.md: would change")
        return 1
    open(a.out or a.ledger, "w", encoding="utf-8").write(new)
    print(f"wrote {a.out or a.ledger}: {new.count(chr(10)+'| `')} rows")
    return 0


if __name__ == "__main__":
    sys.exit(main())
