"""Prepare the next prior-blind cold packet; never dispatch a reviewer."""
from pathlib import Path
import difflib
import gzip
import hashlib
import json
import re
import shutil
import subprocess


ROOT = Path(__file__).resolve().parents[2]
REVIEW = Path(__file__).resolve().parent
PACKET = REVIEW / "packet-v1"
PACKET.mkdir(exist_ok=True)
source = ROOT / "notes/notes_stratonovich_ham_second_moment.tex"
original = source.read_text()
text = original
removed = []
start = 0
while True:
    begin = text.find("\\myCmts{", start)
    if begin < 0:
        break
    depth = 0
    end = None
    for index in range(begin + len("\\myCmts"), len(text)):
        preceding = index - 1
        escaped = False
        while preceding >= 0 and text[preceding] == "\\":
            escaped = not escaped
            preceding -= 1
        if escaped:
            continue
        if text[index] == "{":
            depth += 1
        if text[index] == "}":
            depth -= 1
            if depth == 0:
                end = index + 1
                break
    assert end is not None
    block = text[begin:end]
    if re.search("review|confidence|accepted|gate", block, re.I):
        removed.append(block)
        text = text[:begin] + text[end:]
        start = begin
    else:
        start = end

text, title_count = re.subn(
    r"\{\\normalsize Working notes[^\n}]*\}",
    lambda match: "{\\normalsize Working notes}", text,
)
assert title_count == 1
status = (
    "  argument, even when $\\alpha+\\alpha_0<2$. Opus reviewed this section\n"
    "  with PASS\\_WITH\\_NOTES/medium confidence; configured high-confidence\n"
    "  acceptance remains pending."
)
legacy_status_count = text.count(status)
assert legacy_status_count in (0, 1)
text = text.replace(status, "  argument, even when $\\alpha+\\alpha_0<2$.")
text = re.sub(r"\n{4,}", "\n\n\n", text)
original_proofs = re.findall(r"\\begin\{proof\}.*?\\end\{proof\}", original, re.S)
assert len(original_proofs) == 42
assert original_proofs == re.findall(r"\\begin\{proof\}.*?\\end\{proof\}", text, re.S)
for environment in ["lemma", "proposition", "corollary", "theorem", "goal", "hypothesis"]:
    pattern = r"\\begin\{" + environment + r"\}.*?\\end\{" + environment + r"\}"
    assert re.findall(pattern, text, re.S) == re.findall(pattern, original, re.S)

(PACKET / "candidate.tex").write_text(text)
shutil.copyfile(source.with_suffix(".bbl"), PACKET / "candidate.bbl")
prior = ROOT / "reviews/2026-10-28-full-upper-cold/packet-v1"
for name in [
    "chen-current-author.txt", "crouzeix-palencia-v1.txt", "chen-2023.txt",
    "chen-hu-2025.txt", "balan-conus-2016-source.txt",
    "chen-arxiv-v1-source.txt", "cited-sources.txt",
]:
    shutil.copyfile(prior / name, PACKET / name)

diff = "".join(difflib.unified_diff(
    original.splitlines(keepends=True), text.splitlines(keepends=True),
    fromfile="canonical.tex", tofile="candidate.tex",
))
with gzip.open(REVIEW / "blind-copy.diff.gz", "wb") as output:
    output.write(diff.encode())
assert gzip.decompress((REVIEW / "blind-copy.diff.gz").read_bytes()) == diff.encode()
(REVIEW / "blind-transform.json").write_text(json.dumps({
    "canonical_tex_sha256": hashlib.sha256(source.read_bytes()).hexdigest(),
    "canonical_pdf_sha256": hashlib.sha256(source.with_suffix(".pdf").read_bytes()).hexdigest(),
    "baseline_revision": subprocess.check_output(
        ["git", "rev-parse", "HEAD"], cwd=ROOT, text=True
    ).strip(),
    "removed_review_status_boxes": removed,
    "other_removals": "Title workflow qualifier;legacy verdict sentence only if present",
    "removed_legacy_remark_status": legacy_status_count,
    "all_42_proofs_equal": True,
    "all_nonremark_formal_statements_equal": True,
}, indent=2) + "\n")
print("Blind source prepared; format/build/bind/commit and dispatch are separate steps")
