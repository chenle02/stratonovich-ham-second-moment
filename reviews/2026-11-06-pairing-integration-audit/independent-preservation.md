# Independent custody and preservation audit

Result: PASS for the frozen external draft. This is GPT-family AUTHOR mechanical checking, not cross-family review, mathematical acceptance, HIGH confidence, or adoption.

The checker independently walks the actual TeX input graph from the main file, tokenizes balanced environments, and binds proof owners by their final statement reference. It does not import or execute the producer's scripts. Raw body hashes are bytes strictly between begin/end markers, including original whitespace and comments.

- All 69 frozen manifest members match byte lengths and SHA-256; HELD.json binds the recorded manifest and unadopted status.
- The actual source graph has 28 modules in both versions; 27 are byte-identical. Only the main module differs.
- Original/draft counts are 214/215 proof environments and 240/241 formal declarations.
- 209 old proof bodies are byte-identical. The five changed old bodies are P:mixed, L:joint-fixed-order, L:crude-corrected, L:vertex-crude, and P:envelope. Their 133 inline/display/equation/align math spans are byte-identical in source order.
- All 214 original owned statement bodies are byte-identical. Of all 240 old formal bodies, only the existing source-qualification remark R:source-case2-time-shift changes; the other 239 are byte-identical.
- The new owner is L:pairing-product-envelope, an explicit lemma (main-file lemma ordinal 4) and separate proof. It is not hidden inside the remark. Its raw statement/proof hashes independently reproduce the producer's reported c118323d… / 94df56ba… identities.
- The translated covariance Cauchy–Schwarz proof remains byte-identical. Seven labels were added and none removed.
- The paired draft TeX hash is 516d6a650bdac7d3da68672f37836afd084b651c39553b43d5135d0512e39d14; the paired PDF hash is 26f9f4a5ee65b08449cedc41dc34e688d15147f0ab4e3b9d23e4ee3f9a8624f8. pdfinfo reports 267 pages. The research PDF remains 096cb3cd4610c91d7dc8718bd56526e777cdd06ebca41651a8955bc230eb2f35.
- Hashes of the entire held draft tree, the 28 research TeX modules, and research Git status match before/after the audit. No held/source file, Progress.md, Git state, or runtime was written. No model, build, Lean, or cluster job ran.

No preservation defect was found. Byte-identical math spans do not establish semantic equivalence of surrounding prose or correctness of the new application. PDF hash/page identity is not a full visual gate. Existing reviewer confidence and all scientific gates remain unchanged.

Reproduce from any directory:

    python3 reviews/2026-11-06-pairing-integration-audit/check-preservation.py

The complete receipt is result.json. No canonical ownership/index/grade ledger has been changed.
