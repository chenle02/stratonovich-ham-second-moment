"""Bind a built blind copy; does not dispatch or certify mathematics."""
from pathlib import Path
import gzip
import hashlib
import json
import re
import subprocess

ROOT = Path(__file__).resolve().parents[2]
REVIEW = Path(__file__).resolve().parent
PACKET = REVIEW / "packet-v1"
canonical = ROOT / "notes/notes_stratonovich_ham_second_moment.tex"
candidate = PACKET / "candidate.tex"
s, t = canonical.read_text(), candidate.read_text()


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def dump(path, value):
    path.write_text(json.dumps(value, indent=2) + "\n")


proof = r"\\begin\{proof\}.*?\\end\{proof\}"
assert len(re.findall(proof, s, re.S)) == 45
assert re.findall(proof, s, re.S) == re.findall(proof, t, re.S)
for env in ["lemma", "proposition", "corollary", "theorem", "goal", "hypothesis", "remark", "conjecture", "definition"]:
    pat = r"\\begin\{" + env + r"\}.*?\\end\{" + env + r"\}"
    assert re.findall(pat, s, re.S) == re.findall(pat, t, re.S), env
assert "\t" not in t
subprocess.run(["format-tex", str(candidate)], check=True, cwd=ROOT)
assert candidate.read_text() == t, "Rebuild after formatting changes"
log = candidate.with_suffix(".log").read_text(errors="replace")
assert not re.search(r"(^!|Undefined control|[Uu]ndefined|Overfull)", log, re.M)
pages = int(re.search(r"Output written on .*?\((\d+) pages", log, re.S).group(1))
assert candidate.with_suffix(".bbl").read_bytes() == canonical.with_suffix(".bbl").read_bytes()
assert not re.search(r"Opus|DeepSeek|PASS_WITH|skeptic|cold read|high-confidence", t, re.I)

# The scientific prompt is the verbatim canonical free-form request.
command = (ROOT.parent.parent / "Le-AI-Lab/commands/paper-dev.md").read_text()
marker = "**Cold Reader prompt (verbatim, use exactly this — do not add checklists)**:"
after = command.split(marker, 1)[1].lstrip()
assert after.startswith('"You are a peer reviewer')
cold = after[1:].split('"\n\nDispatch the cold reader', 1)[0]
assert cold.endswith("not to re-derive it.")
orientation = (
    "\n\nPaper: The second moment of the hyperbolic Anderson model with time-dependent "
    "noise: Stratonovich regime. Author: Le Chen.\n"
    "Manuscript: candidate.tex (complete contents below). Bibliography: candidate.bbl "
    "(complete contents below). Frozen cited-source texts are available in the supplied "
    "packet; cited-sources.txt identifies their editions and filenames.\n\n"
)
prompt = cold + orientation + "```latex\n" + t + "\n```\n\nBibliography:\n\n```latex\n"
prompt += candidate.with_suffix(".bbl").read_text() + "\n```\n"
(REVIEW / "prompt-v1.txt").write_text(prompt)

dump(REVIEW / "change-binding.json", {
    "canonical_tex_sha256": sha(canonical),
    "canonical_pdf_sha256": sha(canonical.with_suffix(".pdf")),
    "candidate_tex_sha256": sha(candidate),
    "candidate_pdf_sha256": sha(candidate.with_suffix(".pdf")),
    "all_45_proofs_byte_equal": True,
    "all_formal_statement_bodies_including_remarks_byte_equal": True,
    "pages_blind": pages,
    "gate": {"errors": 0, "undefined": 0, "overfull": 0, "tabs": 0},
    "role": "Fresh free-form DeepSeek V4-Pro cold reader;no graded verdict requested",
    "canonical_prompt_verbatim": True,
})

# Preserve generated build evidence outside the scientific packet.
for suffix in [".aux", ".log", ".out", ".toc", ".fls", ".fdb_latexmk", ".blg"]:
    path = candidate.with_suffix(suffix)
    if path.exists():
        compressed = gzip.compress(path.read_bytes(), mtime=0)
        assert gzip.decompress(compressed) == path.read_bytes()
        (REVIEW / (path.name + ".gz")).write_bytes(compressed)
        path.unlink()
files = sorted(p for p in PACKET.iterdir() if p.is_file())
expected = {
    "candidate.tex", "candidate.pdf", "candidate.bbl", "chen-current-author.txt",
    "crouzeix-palencia-v1.txt", "chen-2023.txt", "chen-hu-2025.txt",
    "balan-conus-2016-source.txt", "chen-arxiv-v1-source.txt", "cited-sources.txt",
}
assert {p.name for p in files} == expected
dump(REVIEW / "manifest-v1.json", {p.name: sha(p) for p in files})
dump(REVIEW / "required-inputs-v1.json", [{"path": p.name} for p in files])
print(json.dumps({"pages_blind": pages, "proofs_equal": 45,
                  "all_formal_statements_equal": True,
                  "packet_members": len(files), "dispatched": False}, indent=2))
