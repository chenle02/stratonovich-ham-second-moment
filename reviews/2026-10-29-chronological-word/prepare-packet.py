"""Freeze the chronological-word revision; byte checks are not proof checks."""
from pathlib import Path
import argparse
import gzip
import hashlib
import json
import re
import shutil
import subprocess

ROOT = Path(__file__).resolve().parents[2]
ROUND = Path(__file__).resolve().parent
OLD = ROOT / "reviews/2026-10-28-terminal-modular/packet-v1"
PACKET = ROUND / "packet-v1"
parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument("--build-log", required=True, type=Path)
args = parser.parse_args()


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
assert re.search(r"Output written on .*\(86 pages", log, re.S)
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
images = sorted(OLD.glob("*.png")) + sorted(ROUND.glob("chen-hu-*.png"))
for name in reuse:
    shutil.copyfile(OLD / name, PACKET / name)
shutil.copyfile(ROUND / "interval-checks.py", PACKET / "checks.py")
shutil.copyfile(ROUND / "interval-checks.json", PACKET / "checks.json")
for image in images:
    shutil.copyfile(image, PACKET / image.name)
for name in ["terminal-checks.py", "terminal-checks.json"]:
    shutil.copyfile(ROUND / name, PACKET / name)

baseline = "89b79d65b2f681d8a64aadebfa20982a3ea17c37"
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
for env in ["lemma", "proposition", "corollary", "theorem", "remark", "goal", "hypothesis", "conjecture"]:
    pattern = r"\\begin\{" + env + r"\}.*?\\end\{" + env + r"\}"
    assert re.findall(pattern, old, re.S) == re.findall(pattern, s, re.S), env
change = {
    "baseline_revision": baseline,
    "source_tex_sha256": digest(source.read_bytes()),
    "source_pdf_sha256": digest(pdf.read_bytes()),
    "pages": 86, "proofs": len(new_proofs),
    "new_proofs": sorted(set(new_proofs) - set(old_proofs)),
    "changed_existing_proofs": sorted(k for k in old_proofs if new_proofs.get(k) != old_proofs[k]),
    "unchanged_proofs": sorted(k for k in old_proofs if new_proofs.get(k) == old_proofs[k]),
    "same_full_goal": True,
    "all_formal_statement_bodies_including_remarks_byte_equal": True,
    "new_equation_labels": sorted(set(labels) - set(re.findall(r"\\label\{([^}]+)\}", old))),
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
source_map = source_map.split("\nCurrent terminal/modular revision:", 1)[0].rstrip() + "\n"
source_map += "\nChronological revision: the known model identification uses Chen Theorem1.1(1),pp2--3 and Section5part(ii),pp35--37. Only the MOMENT estimate/series-tail passage is independent of source Section5 convergence. Static source-class audit: Chen--Hu standing assumptionsp2145,Theorem1.2p2147,EXPLICIT generalized-covariance convention(2.18)p2152,time scaling(5.1)p2173,coefficient upper rate(5.15)p2180. Additional full pages2151,2153,2165,2175 show product/measure/fixed-order/finiteness interfaces. These are imported known statements,not proofs newly supplied here.\n"
static_text = (ROOT / "reviews/2026-10-28-full-upper-cold-v3/packet-v1/chen-hu-2025.txt").read_text().split("\f")
excerpts = (PACKET / "source-excerpts.txt").read_text()
for pub in [2145,2147,2151,2152,2153,2165,2173,2175,2180]:
    excerpts += "\nCHEN--HU PUBLISHED PAGE " + str(pub) + "\n" + static_text[pub-2144] + "\n"
(PACKET / "source-excerpts.txt").write_text(excerpts.rstrip() + "\n")
for name in ["static-source-class-audit.md", "endpoint-budget-check.py", "endpoint-budget-check.json"]:
    shutil.copyfile(ROUND / name, PACKET / name)
source_map += "\nThe new chronological proof retains all three previous helper statements. Only L:fixed-split is substantively rewritten:common partition,endpoint identities,fresh cross-color subspaces,exact word norm,normalized Cauchy integral and explicit C_split. P:mixed is clarified without a product-rule input. The actual limit trace is stated in T:full-upper. Known mild-model identification is distinct from the fixed-order input used in the independently proved moment-limit passage.\n"
(PACKET / "source-map.txt").write_text(source_map)
(PACKET / "calibration.md").write_text(
    "The full G:upper, spatial class and sharp target are unchanged. "
    "Retained terminal Gaussian checks use a bounded constant potential ONLY as "
    "an auxiliary-lemma diagnostic, not as an H:homog covariance example. "
    "All unequal-chain splits at orders two/four reproduce 1/3 and 1/105. "
    "The older noncommuting interval and inventory checks are also included. "
    "Neither set is proof or formal certification. The finite endpoint-budget "
    "diagnostic also remains only falsification evidence. The substantive "
    "chronological fixed-split rewrite,source-class/unequal-chain clarifications "
    "and explicit limit trace require a fresh independent verdict. First-moment L_star "
    "calibrations retain explicit premises; no source normalization repair "
    "or sharp constant is adopted. Novelty, Lean, human verification and "
    "whole-paper cold clearance remain separate unresolved boundaries.\n"
)
texts = ["project-goal.md", "foundation.txt", "calibrations.txt", "operators.txt",
         "intervals.txt", "references.bbl", "source-excerpts.txt", "source-map.txt",
         "calibration.md", "checks.py", "checks.json", "terminal-checks.py",
         "terminal-checks.json", "proof-change-map.json", "reading-map.json",
         "static-source-class-audit.md", "endpoint-budget-check.py", "endpoint-budget-check.json"]
dump(PACKET / "reading-map.json", {
    "required_mathematics": texts[:5], "source_images": [p.name for p in images],
    "scope": "Full G:upper; substantive chronological fixed-split rewrite,five changed proofs,auxiliary source-class/unequal-chain/limit interfaces and all prerequisites",
    "pages": 86, "proofs": 45,
    "changed_proofs": change["changed_existing_proofs"],
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
(ROUND / "build-driver.txt.gz").write_bytes(gzip.compress(args.build_log.read_bytes(), mtime=0))
print(json.dumps({"pages": 86, "proofs": 45, "required_texts": len(texts),
                  "required_images": len(images), "new_proofs": change["new_proofs"],
                  "changed_existing_proofs": change["changed_existing_proofs"]}, indent=2))
