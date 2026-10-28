"""Freeze the new energy lemma and its exact consumers, not a full moment review."""
from pathlib import Path
import hashlib
import json
import re
import shutil

ROOT = Path(__file__).resolve().parents[2]
BASE = Path(__file__).resolve().parent
PACKET = BASE / "packet-v1"
PARENT = ROOT / "reviews/2026-10-28-endpoint-integration"


def sha(data):
    return hashlib.sha256(data).hexdigest()


def dump(path, value):
    path.write_text(json.dumps(value, indent=2) + "\n")


def main():
    assert not PACKET.exists(), "A frozen packet already exists"
    source = ROOT / "notes/notes_stratonovich_ham_second_moment.tex"
    text = source.read_text()
    binding = json.loads((BASE / "change-binding.json").read_text())
    assert sha(source.read_bytes()) == binding["tex_sha256"]
    assert sha(source.with_suffix(".pdf").read_bytes()) == binding["pdf_sha256"]
    PACKET.mkdir()
    blocks = []

    def take(name, start, end):
        assert text.count(start) == 1, (name, start)
        a = text.index(start)
        b = text.index(end, a)
        value = text[a:b].rstrip("\n") + "\n"
        blocks.append({"name": name, "start_line": text[:a].count("\n") + 1,
                       "end_line": text[:a + len(value)].count("\n"),
                       "sha256": sha(value.encode())})
        return value

    (PACKET / "energy.txt").write_text(take(
        "New complete energy section",
        "\\section{Physical and spectral energy for measure covariances}",
        "\\section{Targets}"))
    context = [take("macros", "% === Standard macros ===", "\\begin{document}"),
               take("actual endpoint conditions", "We now take $d=3$,",
                    "\\begin{lemma}[Plane-supported endpoints]"),
               take("actual variational definition and conditional theorem statement",
                    "For the low endpoint let", "\\begin{proof}")]
    a = text.index("\\begin{proof}", text.index("\\label{P:three-transfer}"))
    b = text.index("  Fix $k\\ge1$", a)
    value = text[a:b].rstrip("\n") + "\n"
    context.append(value)
    blocks.append({"name": "static input/dyadic Dalang in the existing consumer",
                   "start_line": text[:a].count("\n") + 1,
                   "end_line": text[:a + len(value)].count("\n"),
                   "sha256": sha(value.encode())})
    context.append(take("source-mollified field and exact static approximant",
                        "  We now identify the static inner Green limit",
                        "  In the second and mixed moments of these integrals,"))
    (PACKET / "consumers.txt").write_text("\n".join(context))
    for name in ["normalization-checks.py", "normalization-checks.json"]:
        shutil.copyfile(BASE / name, PACKET / name)
    for src, name in [(source, "canonical.tex"), (source.with_suffix(".pdf"), "canonical.pdf"),
                      (source.with_suffix(".bbl"), "references.bbl")]:
        shutil.copyfile(src, PACKET / name)
    for name in ["paper-chen-2023.pdf", "paper-chen-hu.pdf"]:
        shutil.copyfile(PARENT / "review-packet-v1" / name, PACKET / name)

    receipt_bytes = (PARENT / "skeptic-v1-receipt.json").read_bytes()
    ledger_bytes = (PARENT / "skeptic-v1-read-ledger.json").read_bytes()
    receipt, ledger = json.loads(receipt_bytes), json.loads(ledger_bytes)
    assert sha(ledger_bytes) == receipt["read_ledger_sha256"]
    assert receipt["coverage_verified"] is True
    carriers = {r["path"]: r for r in ledger["required_images"]}
    image_names = ["chen-2023-01.png", "chen-2023-02.png", "chen-hu-2145.png",
                   "chen-hu-2146.png", "chen-hu-2147.png", "chen-hu-2149.png",
                   "chen-hu-2153.png"]
    image_plan = []
    for name in image_names:
        row = carriers[name]
        data = (PARENT / "review-packet-v1" / name).read_bytes()
        assert row["status"] == "delivered" and sha(data) == row["sha256"]
        (PACKET / name).write_bytes(data)
        image_plan.append({"path": name, "kind": "image", "sha256": row["sha256"],
                           "media_type": "image/png"})
    (PACKET / "source-map.txt").write_text(
        "Chen2023 EJP28#119,DOI10.1214/23-EJP985,pinned SHA256"
        "9ed4b0ae633cc79eb1b985ecf00b2ae67db83061fd0d8a73628704b5b664a5da.\n"
        "chen-2023-01.png: exact identity/generalized covariance class. "
        "chen-2023-02.png: Theorem1.1,Dalang(1.3),quartic variation(1.5),"
        "explicit finiteness. The square-root variation(1.4) is not substituted for(1.5).\n"
        "Chen-Hu published AOP53(6),2144-2195(2025),SHA256"
        "58b152d78cd0d54d82b991933b3eaece86e1ed2b44fe09882c14eba921e97e22.\n"
        "chen-hu-2145/2146.png:model/generalized covariances,homogeneity,Dalang. "
        "chen-hu-2147.png: actual M in(1.11),unit gradient cost. "
        "chen-hu-2149.png: isonormal noise and mollification(2.7),(2.8). "
        "chen-hu-2153.png: measure convention and actual S_n,epsilon(3.1).\n"
        "Every PNG is unchanged from a completed exact-delivery native session;"
        " the new session still needs its own ledger. Full PDFs are optional context.\n")
    (PACKET / "scope.txt").write_text(
        "New mathematical target: complete physical/spectral H1 energy identity and bound,"
        "with actual M_st and source-noise consumers. The full moment theorem is NOT"
        "re-reviewed or accepted here;its prior17PASS/medium,HIGH-unmet status is unchanged.\n"
        "The source quartic finiteness is imported only on real Schwartz profiles before"
        "the new density argument. No circular H1 identity may be assumed.\n"
        "Current-author first-moment normalization,sharpness,arbitrary covariance"
        "factorization,novelty,Lean and circulation clearance are outside scope.\n"
        "Controls are exact matrix/rational plus numerical Gaussian normalizations,"
        "not an analytic or independent certificate. The first matrix control"
        "mistakenly used a column instead of inverse row;the nonsymmetric tilt refused"
        "it and root corrected the diagnostic before freeze. No manuscript formula"
        "was changed for that diagnostic error.\n")
    aux = source.with_suffix(".aux").read_text()
    labels = {}
    for label in ["L:physical-spectral-energy", "E:physical-spectral-energy",
                  "E:energy-quartic-bound", "E:three-static-variational", "P:three-transfer"]:
        m = re.search(r"\\newlabel\{" + re.escape(label) + r"\}\{\{([^}]+)\}\{([^}]+)\}", aux)
        assert m, label
        labels[label] = {"number": m[1], "page": m[2]}
    dump(PACKET / "reading-map.json", {"exact_blocks": blocks, "compiled_labels": labels,
        "canonical_tex_sha256": sha(source.read_bytes()),
        "canonical_pdf_sha256": sha(source.with_suffix(".pdf").read_bytes()),
        "construction": "Exact canonical slices with boundary blank lines trimmed,joined by one blank line"})
    required_text = ["energy.txt", "consumers.txt", "reading-map.json", "source-map.txt",
                     "scope.txt", "references.bbl", "normalization-checks.py", "normalization-checks.json"]
    dump(BASE / "required-v1.json", [{"path": n} for n in required_text] + image_plan)
    dump(BASE / "manifest-v1.json", {str(p.relative_to(PACKET)): sha(p.read_bytes())
        for p in sorted(PACKET.rglob("*")) if p.is_file()})
    dump(BASE / "carrier-binding.json", {"prior_receipt_sha256": sha(receipt_bytes),
        "prior_ledger_sha256": sha(ledger_bytes), "effective_cli": receipt["cli_version"],
        "reused_exact_images": image_names, "prior_exact_delivery": True,
        "does_not_prove": "New session delivery,reading depth,scientific correctness or acceptance"})
    print(json.dumps({"files": len(list(PACKET.iterdir())), "images": len(image_plan),
                      "labels": labels}, indent=2))


if __name__ == "__main__":
    main()
