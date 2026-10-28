# Round 4 manuscript worker: v2 clarification report

STATUS: DONE_WITH_CONCERNS — v2 frozen; fresh independent Opus review dispatched by root, not by this worker.

## Review context

Read `reviews/2026-10-27-round4/opus-v1/report.json`: all nine checks PASS, no fatal/major findings or mandatory repairs, PASS_WITH_NOTES at medium confidence. Per root, v1 did not meet the acceptance threshold and the root image manifest omitted the required kind. Neither the report nor its confidence is promoted here. This is a substantive author clarification of analytic justifications, not a confidence-only retry. Root supplies the expanded source context and corrected image manifest for the fresh review.

## Actual changes (new section only)

[held back until the source author has been told]

No theorem was weakened. All hypothesis, proposition, lemma and corollary environment bodies in the new section are byte-identical to v1; only proofs and the comparison remark changed. Constants, parameter ranges, optimality claim, counterexamples and conclusions are unchanged. The new section is now 389 lines.

## Source and verification boundaries

The analytic clarifications were checked by the GPT-family author. They are not independent review. The source pointer follows the checked v1 source context. For the added Balan–Conus applicability sentence, root explicitly supplied its rendered-page checks: p.1489 for Riesz alpha<d and H>1/2, p.1490 for the condition alpha<2, p.1492 for Theorem 2.1(b) and its wave exponent. Those images are supplied by root in `reviews/2026-10-27-round4/packet-v2/`; this worker does not claim a separate image-source audit. The bibliography key already exists in `All.bib`; no bibliography file was changed.

The inherited analytic source dependencies and review-sensitive points recorded in `worker-report.md` remain. No new numerical run was needed for these test-function and limit justifications; the unchanged coefficient algebra and constants retain the prior checks. No mathematical scope beyond the authorized higher-alpha section was edited. No Git command, sibling edit, message, Lean work or reviewer dispatch was performed by this worker.

## Build and preservation

Ran from the repository root:

```text
latexmk -pdf -interaction=nonstopmode -halt-on-error -outdir=notes notes/notes_stratonovich_ham_second_moment.tex
```

Exit 0. Final PDF: 31 pages. Final log: zero errors, zero undefined references/citations, zero overfull boxes. Source tabs: 0. Nonfatal hyperref PDF-string and counter-printing warnings remain; no claim that all warnings vanished. No overfull repair was necessary.

Byte comparison confirms the entire prefix before the new section and the entire suffix starting at Targets are identical to v1. This preserves Sections 1–5, all prior proofs, abstract and status text. Every hypothesis/proposition/lemma/corollary statement in the new section was also compared byte-for-byte with v1 and is unchanged. No full-manuscript restyling or visual audit is claimed.

- V1 TeX SHA-256: `34139160165b61ca770de3ddf90c66459344373ce43930c488365400b91dd27f`
- Frozen v2 TeX SHA-256: `86ea2cf65a8eeff0a2bfb79fe045fcf9709d1e10ae7117b4d9472a7e2bd8a1da`
- V2 section SHA-256: `ff7f80ff17ea74bb2cb67d332b1fef8f9182b04e7c375cdc4f3ecabb4d44a13e`
- Built PDF SHA-256: `9c314be635fbc6f93c2b8cdacbc6f77d217e12e59ce96c9e58b27cfdce1a6c09`

Root reports that this exact v2 source was dispatched to fresh Opus with 17 correctly typed images. At root's freeze instruction, only this separate report was written; candidate source and PDF were not changed. No acceptance, independent-review completion, novelty, formal verification, sharp constant or whole-goal completion is asserted.

STATUS: DONE_WITH_CONCERNS — frozen v2, independent review pending; no further source edits without root request.
