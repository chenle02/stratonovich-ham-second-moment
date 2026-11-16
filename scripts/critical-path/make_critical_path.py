#!/usr/bin/env python3
"""Generate notes/critical-path-data.tex: what the four main theorems rest on.

Usage (repository root, after a build of the book, so that the .aux exists):
    python3 scripts/critical-path/make_critical_path.py [--check]

Inputs:
  notes/notes_stratonovich_ham_second_moment.tex and the files it inputs
  notes/notes_stratonovich_ham_second_moment.aux   (numbers of the results)
  scripts/lean-coverage/coverage.yaml               (Lean class of a result)
  scripts/critical-path/link-corrections.json       (links added or removed
                                                     by hand, each with its
                                                     evidence)

A result R *rests directly on* a result S when the statement or the proof of
R cites S by \\ref, or cites an equation that is labelled inside the statement
or the proof of S, or when the proof of R says "the preceding lemma" (and the
like) and S is the result just before R. Links found by reading and recorded
in link-corrections.json are added; links recorded there as mentions only are
removed. The results a theorem rests on are the closure of this relation.

The list shows which results a proof cites. It does not say that a proof is
correct, and it is not a review.
"""
import collections
import json
import os
import re
import sys

import yaml

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", ".."))
MAIN = "notes/notes_stratonovich_ham_second_moment.tex"
AUX = os.path.join(ROOT, "notes", "notes_stratonovich_ham_second_moment.aux")
OUT = os.path.join(ROOT, "notes", "critical-path-data.tex")
KINDS = "theorem|lemma|proposition|corollary|nogo|conjecture"
KIND_WORD = {"theorem": "Theorem", "lemma": "Lemma", "proposition": "Proposition", "corollary": "Corollary"}
# The four main theorems, in the order of the book.
ROOTS = ["T:full-upper", "T:intrinsic-second-moment", "T:intrinsic-occupation-ceiling", "T:white-moment-bounds"]
LEAN = {("same-assumptions", "full"): "full", ("same-assumptions", "weaker"): "narrower",
        ("inputs-supplied", "full"): "supplied", ("inputs-supplied", "weaker"): "partial",
        ("outside", "full"): "outside"}
WORDS = {0: "no", 1: "one", 2: "two", 3: "three", 4: "four", 5: "five", 6: "six", 7: "seven",
         8: "eight", 9: "nine", 10: "ten"}


def flatten(path, out):
    for n, line in enumerate(open(os.path.join(ROOT, path)).read().split("\n"), 1):
        m = re.match(r"\s*\\input\{(notes/[^}]+)\}\s*$", line)
        if m:
            flatten(m.group(1) + ("" if m.group(1).endswith(".tex") else ".tex"), out)
        else:
            out.append((path, n, line))


def nocomment(s):
    return re.split(r"(?<!\\)%", s, 1)[0]


def read_results():
    lines = []
    flatten(MAIN, lines)
    start = next(i for i, x in enumerate(lines) if x[2].strip() == r"\mainmatter")
    lines = lines[start:]
    results, order, owner, last = {}, [], {}, None
    i = 0
    gap = 0   # first line after the last result, proof or heading: start of a lead-in
    while i < len(lines):
        path, n, raw = lines[i]
        line = nocomment(raw)
        m = re.match(r"\s*\\begin\{(%s)\}" % KINDS, line)
        if m:
            j, body = i, []
            while True:
                body.append(nocomment(lines[j][2]))
                if re.search(r"\\end\{%s\}" % m.group(1), body[-1]):
                    break
                j += 1
            text = "\n".join(body)
            labs = re.findall(r"\\label\{([^}]+)\}", text)
            main = next((l for l in labs if re.match(r"(T|L|P|C|Conj):", l)), None)
            if main:
                t = re.search(r"\\begin\{%s\}\[((?:[^\[\]]|\[[^\]]*\])*)\]" % m.group(1), text)
                leadin = "\n".join(nocomment(x[2]) for x in lines[gap:i])
                results[main] = dict(kind=m.group(1), title=" ".join(t.group(1).split()) if t else "", file=path,
                                     proof_lines=0, cites=set(re.findall(r"\\(?:eq)?ref\{([^}]+)\}", text)),
                                     prev=[], leadin=set(re.findall(r"\\(?:eq)?ref\{([^}]+)\}", leadin)))
                order.append(main)
                for l in labs:
                    owner[l] = main
                last = main
            i = j + 1
            gap = i
            continue
        if re.match(r"\s*\\begin\{proof\}", line):
            j, body, depth = i, [], 0
            while True:
                s = nocomment(lines[j][2])
                body.append(s)
                depth += len(re.findall(r"\\begin\{proof\}", s)) - len(re.findall(r"\\end\{proof\}", s))
                if depth <= 0:
                    break
                j += 1
            text = "\n".join(body)
            named = re.findall(r"This\s+proves\s+(?:Theorem|Lemma|Proposition|Corollary|No-go)s?~\\ref\{([^}]+)\}", text)
            target = named[-1] if named and named[-1] in results else last
            if target:
                r = results[target]
                r["proof_lines"] += j - i + 1
                r["cites"] |= set(re.findall(r"\\(?:eq)?ref\{([^}]+)\}", text))
                for l in re.findall(r"\\label\{([^}]+)\}", text):
                    owner.setdefault(l, target)
                if re.search(r"\b(preceding|previous)\s+(lemma|proposition|corollary|theorem|result)", text, re.I):
                    k = order.index(target)
                    if k > 0:
                        r["prev"].append(order[k - 1])
            i = j + 1
            gap = i
            continue
        if re.match(r"\s*\\(chapter|section|subsection)\*?[\[{]", line):
            gap = i + 1
        i += 1
    return results, order, owner


def tex_title(s):
    return s  # titles are LaTeX already (they are the optional arguments of the environments)


def main():
    check = "--check" in sys.argv[1:]
    results, order, owner = read_results()
    aux = open(AUX).read()
    number = dict(re.findall(r"\\newlabel\{([^}]+)\}\{\{([^}]*)\}", aux))
    proved = [k for k in order if results[k]["proof_lines"] > 0 and results[k]["kind"] in KIND_WORD]
    edges = collections.defaultdict(set)
    for r in proved:
        d = results[r]
        for t in d["prev"]:
            if t in proved:
                edges[r].add(t)
        for c in d["cites"]:
            t = c if c in results else owner.get(c)
            if t and t != r and t in proved:
                edges[r].add(t)
    # links added or removed by hand, with their evidence
    corr = json.load(open(os.path.join(HERE, "link-corrections.json")))
    for c in corr["add"]:
        if c["from"] not in proved or c["to"] not in proved:
            raise SystemExit(f"link-corrections.json: unknown result in {c['from']} -> {c['to']}")
        edges[c["from"]].add(c["to"])
    for c in corr["remove"]:
        if c["to"] not in edges.get(c["from"], ()):
            raise SystemExit(f"link-corrections.json: the link {c['from']} -> {c['to']} to remove is not there")
        edges[c["from"]].discard(c["to"])

    def closure(r):
        seen, stack = set(), [r]
        while stack:
            x = stack.pop()
            for y in edges.get(x, ()):
                if y not in seen:
                    seen.add(y)
                    stack.append(y)
        return seen

    for r in ROOTS:
        if r not in proved:
            raise SystemExit(f"main theorem {r} not found among the proved results")
    cl = {r: closure(r) | {r} for r in ROOTS}
    path = set().union(*cl.values())
    users = collections.defaultdict(set)
    for a in path:
        for b in closure(a):
            users[b].add(a)
    cov = yaml.safe_load(open(os.path.join(ROOT, "scripts", "lean-coverage", "coverage.yaml")))["rows"]
    lean = {r["paper"]["label"]: LEAN[(r["class"], r.get("conclusion", "full"))] for r in cov}
    missing = [k for k in path if k not in number]
    if missing:
        raise SystemExit(f"results without a number in the .aux file (build the book first): {missing[:5]}")

    def chapter(k):
        return number[k].split(".")[0]

    def ref(k):
        return f"{KIND_WORD[results[k]['kind']]}~\\ref{{{k}}}"

    def count(xs):
        c = collections.Counter(lean.get(x, "none") for x in xs)
        return c

    out = ["% Generated by scripts/critical-path/make_critical_path.py; do not edit by hand.\n"]
    macro = lambda name, value: out.append(f"\\newcommand{{\\{name}}}{{{value}}}\n")
    macro("cpResults", str(len(path)))
    chapters = sorted({chapter(k) for k in path}, key=int)
    in_chapters = [k for k in proved if chapter(k).isdigit() and int(chapters[0]) <= int(chapter(k)) <= int(chapters[-1])]
    macro("cpProved", str(len(in_chapters)))
    macro("cpFirstChapter", chapters[0])
    macro("cpLastChapter", chapters[-1])
    macro("cpNotReached", str(len(in_chapters) - len(path)))
    c = count(path)
    macro("cpLeanFull", str(c["full"]))
    macro("cpLeanNarrower", str(c["narrower"]))
    macro("cpLeanSupplied", WORDS.get(c["supplied"], str(c["supplied"])))
    macro("cpLeanPartial", str(c["partial"]))
    macro("cpLeanNone", str(c["none"] + c["outside"]))
    macro("cpLinksAdded", str(len(corr["add"])))
    macro("cpLinksRemoved", str(len(corr["remove"])))
    macro("cpReadByHand", str(corr["read_by_hand"]))
    # table 1: the four theorems
    rows = []
    for r in ROOTS:
        c = count(cl[r] - {r})
        rows.append(f"  {ref(r)} & {results[r]['title']} & {len(cl[r]) - 1} & {c['full']} & {c['narrower']} & "
                    f"{c['supplied']} & {c['partial']} & {c['none'] + c['outside']} \\\\\n")
    out.append("\\newcommand{\\cpTheoremRows}{%\n" + "".join(rows) + "}\n")
    # table 2: by chapter
    rows = []
    for ch in chapters:
        xs = [k for k in path if chapter(k) == ch]
        c = count(xs)
        tot = sum(1 for k in in_chapters if chapter(k) == ch)
        rows.append(f"  {ch} & {tot} & {len(xs)} & {c['full']} & {c['narrower']} & {c['supplied']} & {c['partial']} & "
                    f"{c['none'] + c['outside']} \\\\\n")
    c = count(path)
    rows.append("  \\midrule\n" + f"  All & {len(in_chapters)} & {len(path)} & {c['full']} & {c['narrower']} & "
                f"{c['supplied']} & {c['partial']} & {c['none'] + c['outside']} \\\\\n")
    out.append("\\newcommand{\\cpChapterRows}{%\n" + "".join(rows) + "}\n")
    # the long list, in book order
    word = {"full": "full", "narrower": "narrower", "supplied": "supplied", "partial": "partial",
            "outside": "outside", "none": "---"}
    rows = []
    for k in [x for x in order if x in path]:
        deps = sorted(edges.get(k, ()), key=order.index)
        on = ", ".join(f"\\ref{{{d}}}" for d in deps) if deps else "---"
        # Results cited only in the sentences that introduce this result
        # (between the previous result, proof or heading and its statement)
        # are shown in parentheses and are not links: such a sentence often
        # cites a result to contrast with it.
        lead = {c if c in results else owner.get(c) for c in results[k]["leadin"]}
        lead = sorted((x for x in lead if x and x in proved and x != k and x not in edges.get(k, ())), key=order.index)
        if lead:
            on = ("" if on == "---" else on + " ") + "(" + ", ".join(f"\\ref{{{d}}}" for d in lead) + ")"
        rows.append(f"\\cpRow{{{ref(k)}}}{{{tex_title(results[k]['title'])}}}{{{on}}}{{{len(users[k])}}}"
                    f"{{{word[lean.get(k, 'none')]}}}\n")
    out.append("\\newcommand{\\cpRows}{%\n" + "".join(rows) + "}\n")
    # results of the same chapters that are not reached
    nr = [k for k in in_chapters if k not in path]
    out.append("\\newcommand{\\cpNotReachedList}{%\n" + ",\n".join(ref(k) for k in nr) + "%\n}\n")
    text = "".join(out)
    if check:
        if not os.path.exists(OUT) or open(OUT).read() != text:
            raise SystemExit("notes/critical-path-data.tex is stale; regenerate it")
        print("critical-path data are current")
        return
    open(OUT, "w").write(text)
    print(f"{len(path)} results on the path of {len(in_chapters)} proved in Chapters {chapters[0]}-{chapters[-1]}; "
          f"{len(nr)} not reached; links added {len(corr['add'])}, removed {len(corr['remove'])}; "
          + "; ".join(f"{r}: {len(cl[r]) - 1}" for r in ROOTS))


if __name__ == "__main__":
    main()
