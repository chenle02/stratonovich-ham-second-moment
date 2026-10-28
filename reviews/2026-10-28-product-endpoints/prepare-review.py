"""Freeze Section 9 and exact inherited/source inputs; never launches a review."""
from pathlib import Path
import hashlib
import json
import re
import shutil
import subprocess
import tarfile

ROOT = Path(__file__).resolve().parents[2]
BASE = Path(__file__).resolve().parent
PACKET = BASE / "review-packet-v1"
PREVIOUS = ROOT / "reviews/2026-10-28-static-holder"


def sha(data):
    return hashlib.sha256(data).hexdigest()


def dump(path, value):
    path.write_text(json.dumps(value, indent=2) + "\n")


def main():
    assert not PACKET.exists(), "An immutable packet already exists"
    source = ROOT / "notes/notes_stratonovich_ham_second_moment.tex"
    text = source.read_text()
    qualification = json.loads((BASE / "calibration-qualification.json").read_text())
    assert sha(source.read_bytes()) == qualification["final_tex_sha256"]
    PACKET.mkdir()
    blocks = []

    def take(name, start, end):
        assert text.count(start) == 1, (name, start)
        a = text.index(start)
        b = text.index(end, a)
        data = text[a:b].rstrip("\n") + "\n"
        blocks.append({"name": name, "start_line": text[:a].count("\n") + 1,
                       "end_line": text[:a + len(data)].count("\n"),
                       "sha256": sha(data.encode())})
        return data

    section = take("Section 9", "\\section{Three-dimensional bounds from covariance endpoints}",
                   "\\section{Targets}")
    (PACKET / "section9.txt").write_text(section)
    context = [take("macros", "% === Standard macros ===", "\\begin{document}"),
               take("model", "\\section{Model and standing assumptions}", "\\section{What is known}"),
               take("source-dependent moment statements, qualified", "\\subsection{Known moment bounds}",
                    "\\section{Gate G0:")]
    # Include the complete accepted mixed-expansion proof, not only its statement.
    a = text.index("\\section{Gate G0:")
    e = text.index("\\end{proof}", text.index("\\label{P:mixed}")) + len("\\end{proof}")
    mixed = text[a:e] + "\n"
    blocks.append({"name": "G0 definitions and P:mixed proof",
                   "start_line": text[:a].count("\n") + 1,
                   "end_line": text[:e].count("\n") + 1,
                   "sha256": sha(mixed.encode())})
    context.append(mixed)
    context += [take("ordered-increment dependence and coefficient definitions",
                     "\\section{G2 upper bounds for spatial exponents at most one}",
                     "\\begin{proposition}[One-dimensional upper bound]"),
                take("general spectral and Green conventions",
                     "\\subsection{Spectral bounds for", "\\begin{lemma}[Low-$\\alpha$ convolution bound]")]
    a = text.index("\\begin{lemma}[Degree-one convolution bound]")
    e = text.index("\\end{proof}", a) + len("\\end{proof}")
    degree_one = text[a:e] + "\n"
    blocks.append({"name": "L:alpha-one-convolution including proof",
                   "start_line": text[:a].count("\n") + 1,
                   "end_line": text[:e].count("\n") + 1,
                   "sha256": sha(degree_one.encode())})
    context.append(degree_one)
    (PACKET / "context.txt").write_text("\n".join(context))

    for source_name, target in [(source, "canonical.tex"),
                                (source.with_suffix(".pdf"), "canonical.pdf"),
                                (source.with_suffix(".bbl"), "references.bbl")]:
        shutil.copyfile(source_name, PACKET / target)
    # Reuse byte-identical images with actual prior native exact-delivery evidence.
    archive = PREVIOUS / "planar-native-evidence.tar.xz"
    archive_manifest = json.loads((PREVIOUS / "planar-native-evidence-manifest.json").read_text())
    assert sha(archive.read_bytes()) == archive_manifest["sha256"]
    ledger_name = "opus-planar-skeptic/read-ledger.json"
    receipt_name = "opus-planar-skeptic/receipt.json"
    with tarfile.open(archive, "r:xz") as tf:
        ledger_bytes = tf.extractfile(ledger_name).read()
        receipt_bytes = tf.extractfile(receipt_name).read()
    assert sha(ledger_bytes) == archive_manifest["members"][ledger_name]
    assert sha(receipt_bytes) == archive_manifest["members"][receipt_name]
    ledger, receipt = json.loads(ledger_bytes), json.loads(receipt_bytes)
    assert receipt["coverage_verified"] is True
    assert sha(ledger_bytes) == receipt["read_ledger_sha256"]
    assert receipt["cli_version"] == "2.1.304 (Claude Code)"
    image_requirements = []
    for row in ledger["required_images"]:
        assert row["status"] == "delivered"
        old_image = PREVIOUS / "planar-packet-v2" / row["path"]
        assert sha(old_image.read_bytes()) == row["sha256"]
        shutil.copyfile(old_image, PACKET / row["path"])
        image_requirements.append({"path": row["path"], "kind": "image",
                                   "sha256": row["sha256"], "media_type": row["media_type"]})
    for name in ["paper-chen-author.pdf", "paper-chen-hu.pdf", "paper-chen-2023.pdf", "paper-balan-conus.pdf"]:
        shutil.copyfile(PREVIOUS / "planar-packet-v2" / name, PACKET / name)
    shutil.copyfile(PREVIOUS / "planar-packet-v2/source-map.md", PACKET / "source-map.md")
    with (PACKET / "source-map.md").open("a") as f:
        f.write("\nFor this packet all images are exact copies of previously native-delivered PNGs,\n"
                "not fresh resizes. The present session still needs its own full ledger.\n"
                "Current-author first-moment constants are not an upper-proof input; see\n"
                "normalization-boundary.txt. Static M is the separate published square-root\n"
                "functional and is not the current author's E or E_star.\n")
    (PACKET / "normalization-boundary.txt").write_text(
        "The pinned current author PDF's literal first-moment definitions (1.11)--(1.13)\n"
        "have a separately source-bound, cross-family checked normalization discrepancy\n"
        "under the measurable finite-integrated-energy interpretation. No intended\n"
        "correction is adopted. The manuscript keeps the source statement/formulas\n"
        "verbatim with a warning; Section9's Jensen/first-moment calibration is explicitly\n"
        "conditional on the intended lower bound. No current-author first-moment upper\n"
        "constant is used in the new upper proof. Review that dependency boundary; you\n"
        "are not asked to recover the intended correction or certify sharpness.\n"
        "Sections6/7/8 are unadopted candidates and are not Section9 premises.\n"
        "The accepted inherited mixed expansion and degree-one convolution are supplied\n"
        "with their complete proofs. The full source remains available for extra context.\n")
    constraints = subprocess.check_output(
        ["python3", "../SPDEs-wiki/scripts/rl_query.py", "prompt", "stratonovich-ham-second-moment"],
        cwd=ROOT, text=True)
    constraints += ("\nAdditional project-local boundaries from Progress.md (ledger query is incomplete):\n"
                    "Uniform common-theta per-pairing G0 majorant loses the required factorial power;\n"
                    "that route is not a moment no-go. Euclidean radial lowering of arbitrary d3\n"
                    "covariance fails positive definiteness. Product coordinate-power splitting is\n"
                    "a different construction. No Skorohod proof development or coordinate exponent1\n"
                    "extension, no general d3 factorization, no sharpness claim.\n")
    (PACKET / "route-constraints.txt").write_text(constraints)
    aux = source.with_suffix(".aux").read_text()
    labels = {}
    for label in ["L:product-endpoints", "H:three-endpoints", "P:three-transfer",
                  "C:three-product-riesz", "R:three-endpoint-scope"]:
        m = re.search(r"\\newlabel\{" + re.escape(label) + r"\}\{\{([^}]+)\}\{([^}]+)\}", aux)
        assert m, label
        labels[label] = {"number": m[1], "page": m[2]}
    dump(PACKET / "reading-map.json", {
        "canonical_tex_sha256": sha(source.read_bytes()),
        "canonical_pdf_sha256": sha(source.with_suffix(".pdf").read_bytes()),
        "exact_blocks": blocks, "compiled_labels": labels,
        "scope": "Section9 plus actual inherited dependencies; no Sections6/7/8 premises",
        "context_construction": "Exact canonical slices with one blank line between blocks",
    })
    dump(BASE / "carrier-preflight.json", {
        "prior_archive": "../2026-10-28-static-holder/planar-native-evidence.tar.xz",
        "prior_archive_sha256": archive_manifest["sha256"],
        "ledger_member": ledger_name, "ledger_sha256": sha(ledger_bytes),
        "receipt_member": receipt_name, "receipt_sha256": sha(receipt_bytes),
        "effective_cli": receipt["cli_version"], "exact_previously_delivered_images": len(image_requirements),
        "all_image_bytes_unchanged": True,
        "does_not_prove": "New session delivery, attention, science or acceptance; those remain fresh gates",
        "capacity_boundary": "30 images previously delivered in one native session; no media-removal qualification. No universal image budget claimed.",
    })
    required_texts = ["section9.txt", "context.txt", "reading-map.json", "source-map.md",
                      "references.bbl", "normalization-boundary.txt", "route-constraints.txt"]
    dump(BASE / "review-required-v1.json", [{"path": name} for name in required_texts] + image_requirements)
    mapping = {str(p.relative_to(PACKET)): sha(p.read_bytes())
               for p in sorted(PACKET.rglob("*")) if p.is_file()}
    dump(BASE / "review-manifest-v1.json", mapping)
    print(json.dumps({"files": len(mapping), "required_texts": len(required_texts),
                      "required_images": len(image_requirements), "labels": labels}, indent=2))


if __name__ == "__main__":
    main()
