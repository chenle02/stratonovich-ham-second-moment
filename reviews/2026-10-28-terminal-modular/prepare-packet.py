"""Freeze the terminal/modular revision; byte checks are not proof checks."""
from pathlib import Path
import gzip
import hashlib
import json
import re
import shutil
import subprocess

ROOT = Path(__file__).resolve().parents[2]
ROUND = Path(__file__).resolve().parent
OLD = ROOT / "reviews/2026-10-28-cold-core-expansion/packet-v1"
PACKET = ROUND / "packet-v1"


def digest(data):
    return hashlib.sha256(data).hexdigest()


def dump(path, obj):
    path.write_text(json.dumps(obj, indent=2) + "\n")


source = ROOT / "notes/notes_stratonovich_ham_second_moment.tex"
pdf = source.with_suffix(".pdf")
s = source.read_text()
assert s.count(r"\begin{proof}") == s.count(r"\end{proof}") == 45
assert "\t" not in s
log = source.with_suffix(".log").read_text(errors="replace")
assert not re.search(r"(^!|Undefined control|[Uu]ndefined|Overfull)", log, re.M)
assert re.search(r"Output written on .*\(82 pages", log, re.S)
labels = re.findall(r"\\label\{([^}]+)\}", s)
assert len(labels) == len(set(labels))

# All mathematical sections through the full upper theorem are required.
boundaries = [0] + [s.index(x) for x in [
    r"\section{G2 upper bounds for spatial exponents at most one}",
    r"\section{A static phase estimate at first variance order}",
    r"\section{Interval fields and the full upper bound}",
    r"\section{Targets}",
]]
PACKET.mkdir(exist_ok=True)
for name, left, right in zip(
    ["foundation.txt", "calibrations.txt", "operators.txt", "intervals.txt"],
    boundaries, boundaries[1:],
):
    (PACKET / name).write_text(s[left:right].rstrip() + "\n")
for src, dst in [(source, "canonical.tex"), (pdf, "canonical.pdf"),
                 (source.with_suffix(".bbl"), "references.bbl"),
                 (ROOT / "PROJECT-GOAL.md", "project-goal.md")]:
    shutil.copyfile(src, PACKET / dst)
reuse = [
    "source-excerpts.txt", "chen-current-author.pdf", "crouzeix-palencia-v1.pdf",
    "chen-2023.pdf", "chen-hu-2025.pdf", "balan-conus-2016-source.txt",
    "checks.py", "checks.json",
]
images = sorted(OLD.glob("*.png"))
for name in reuse:
    shutil.copyfile(OLD / name, PACKET / name)
for image in images:
    shutil.copyfile(image, PACKET / image.name)
for name in ["terminal-checks.py", "terminal-checks.json"]:
    shutil.copyfile(ROUND / name, PACKET / name)

baseline = "ef5f691b5d89f71d250bcb6271c3d6eee70376b3"
old = subprocess.check_output(["git", "show", baseline + ":" + str(source.relative_to(ROOT))], cwd=ROOT).decode()
def proof_blocks(text):
    blocks = {}
    for m in re.finditer(r"\\begin\{proof\}.*?\\end\{proof\}", text, re.S):
        closing = re.findall(r"\\ref\{([^}]+)\}", m.group())
        assert closing, m.start()
        key = closing[-1]
        assert key not in blocks, key
        blocks[key] = m.group()
    return blocks
old_proofs, new_proofs = proof_blocks(old), proof_blocks(s)
change = {
    "baseline_revision": baseline,
    "source_tex_sha256": digest(source.read_bytes()),
    "source_pdf_sha256": digest(pdf.read_bytes()),
    "pages": 82, "proofs": len(new_proofs),
    "new_proofs": sorted(set(new_proofs) - set(old_proofs)),
    "changed_existing_proofs": sorted(k for k in old_proofs if new_proofs.get(k) != old_proofs[k]),
    "unchanged_proofs": sorted(k for k in old_proofs if new_proofs.get(k) == old_proofs[k]),
    "same_full_goal": True,
    "gate": {"errors": 0, "undefined": 0, "overfull": 0, "tabs": 0},
    "status": "CANDIDATE;fresh primary and cold review required",
}
assert not (set(old_proofs) - set(new_proofs))
dump(ROUND / "change-binding.json", change)
dump(PACKET / "proof-change-map.json", change)
for label, name in [("L:fixed-split", "fixed-split.txt"),
                    ("L:terminal-wick", "terminal-wick-lemma.txt"),
                    ("L:uniform-series-tail", "uniform-tail.txt")]:
    at = s.index(r"\label{" + label + "}")
    start = s.rfind(r"\begin{lemma}", 0, at)
    end = s.index(r"\end{proof}", at) + len(r"\end{proof}")
    (ROUND / name).write_text(s[start:end] + "\n")
start = s.index(r"\subsection{Finite Gaussian models and their terminal kernels}")
end = s.index(r"\begin{lemma}[Uniform series tails", start)
(ROUND / "terminal-wick.txt").write_text(s[start:end].rstrip() + "\n")

source_map = (OLD / "source-map.txt").read_text()
source_map += (
    "\nCurrent terminal/modular revision: the MAIN full-upper proof imports only "
    "the fixed-order L2 limit Th4.1(4.2)p22 as its analytic construction input. "
    "It proves a uniform scaled finite-model moment bound and the geometric "
    "tail lemma separately; it does not invoke the source Section5 series "
    "convergence or P:mixed/L:crude-corrected in that final passage. Earlier "
    "sections retain their explicitly labelled separate imports.\n"
)
(PACKET / "source-map.txt").write_text(source_map)
(PACKET / "calibration.md").write_text(
    "The full G:upper, spatial class and sharp target are unchanged. "
    "New terminal Gaussian checks use a bounded constant potential ONLY as "
    "an auxiliary-lemma diagnostic, not as an H:homog covariance example. "
    "All unequal-chain splits at orders two/four reproduce 1/3 and 1/105. "
    "The older noncommuting interval and inventory checks are also included. "
    "Neither set is proof or formal certification. The new fixed-split, "
    "terminal Wick and series-tail lemmas, and revised full deduction, "
    "require an independent mathematical verdict. First-moment L_star "
    "calibrations retain explicit premises; no source normalization repair "
    "or sharp constant is adopted. Novelty, Lean, human verification and "
    "whole-paper cold clearance remain separate unresolved boundaries.\n"
)
texts = ["project-goal.md", "foundation.txt", "calibrations.txt", "operators.txt",
         "intervals.txt", "references.bbl", "source-excerpts.txt", "source-map.txt",
         "calibration.md", "checks.py", "checks.json", "terminal-checks.py",
         "terminal-checks.json", "proof-change-map.json", "reading-map.json"]
dump(PACKET / "reading-map.json", {
    "required_mathematics": texts[:5], "source_images": [p.name for p in images],
    "scope": "Full G:upper; new terminal/fixed-split/tail lemmas and all prerequisites/consumers",
    "pages": 82, "proofs": 45,
    "section_extract_normalization": "Trailing blank lines removed at section boundaries only; proof bytes unchanged",
    "new_proofs": change["new_proofs"],
    "no_prior_review_reports_in_packet": True,
})
required = [{"path": p} for p in texts]
required += [{"path": p.name, "kind": "image", "sha256": digest(p.read_bytes()),
              "media_type": "image/png"} for p in images]
dump(ROUND / "required-v1.json", required)
dump(ROUND / "manifest-v1.json", {
    p.relative_to(PACKET).as_posix(): digest(p.read_bytes())
    for p in sorted(PACKET.rglob("*")) if p.is_file()
})
build = Path("<HOME>/.local/state/tmp/stratonovich-terminal-modular-build.txt")
(ROUND / "build-driver.txt.gz").write_bytes(gzip.compress(build.read_bytes(), mtime=0))
print(json.dumps({"pages": 82, "proofs": 45, "required_texts": len(texts),
                  "required_images": len(images), "new_proofs": change["new_proofs"],
                  "changed_existing_proofs": change["changed_existing_proofs"]}, indent=2))
