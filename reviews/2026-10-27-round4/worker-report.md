# Round 4 manuscript worker report

STATUS: DONE_WITH_CONCERNS — UNREVIEWED author candidate, ready for root to freeze and dispatch to Opus.

## Exact scope and preservation

Inserted one 342-line section, “Higher spatial exponents under a convolution bound,” immediately before Targets in `notes/notes_stratonovich_ham_second_moment.tex`. No previous manuscript bytes changed: deleting exactly this insertion reproduces the saved pre-edit source byte-for-byte. Abstract, accepted scope/status, prior statements and proofs, Targets and Planned route remain unchanged. The new section carries explicit UNREVIEWED status. The spatial insertion marker is retained and now identifies the inserted Riesz lemma.

- `H:spatial-maximum`: all translations, positive covariance Gaussian widths, nonnegative Green Gaussian widths, including separate widths per edge/factor.
- `P:higher-transfer`: conditional coefficient and target-scale second-moment bounds for d=2,3 and 1<alpha<2-alpha0; delta=alpha-1, conjugate r,r', explicit nonsharp K from the elementary Gamma lower bound.
- `L:higher-riesz` and `C:higher-riesz`: exact optimal uniform d3 Riesz spatial constant for 1<alpha<2, explicit nonoptimal d2 constant for 1<alpha<3/2, and moment applications intersected with alpha+alpha0<2.
- `P:higher-obstructions`: d2 Riesz boundary divergence for alpha>=3/2 within alpha<2; function-valued product covariance obstruction for every alpha in (1,2), transferred to d3 by projection. No supplementary delta example.
- `R:higher-calibrations`: first-moment/Jensen consistency, static exponent limit, and Skorohod comparison without identifying constants or solutions.

Only the manuscript source, its root-build artifacts, and this requested report were written inside the repository. No Git commands, messages, sibling edits, Lean work, independent-review dispatch, or status promotion were performed. Root preflight was accepted as supplied. Temporary author baseline and insertion were saved outside the repository for the byte comparison. No further candidate edits will be made without root request.

## Source inputs and hypothesis matching

Read `AGENTS.md`, the workflow state in `Progress.md`, manuscript model/mixed expansion and Section 5, and the requested reconnaissance files:

- `reviews/2026-10-27-round4/recon/holder-calculation.md`
- `reviews/2026-10-27-round4/recon/literature-gate.md`
- `reviews/2026-10-27-round4/recon/holder-checks.json`
- `reviews/2026-10-27-round4/recon/spatial-probe.md` (later authorized scope extension)

Applied canonical `le-chen-writing-style` and `latex-conventions`, with project amsrefs rules overriding generic bibliography conventions. No new bibliography entries or literature research were needed; the existing Chen author-version key was checked in `extra.bib`. The literature gate remains REFRAME and novelty remains unverified.

[held back until the source author has been told]

The new proof does not apply L:d1-spatial or P:low-alpha-upper outside their hypothesis ranges. It restates the dimension-independent descending-label invariant and uses the new spatial hypothesis in its closing step. It reproduces the inherited Green-first/noise-second passage in d3 with bounded smoothed covariances, weak convergence, dominated convergence for joint covariances, L2 convergence and then L1 convergence of products. In d2 only noise removal is required. No simultaneous reversal of this limit order is asserted.

## Author verification

Independently recalculated the joint counting-measure/time-measure Hölder inequality, Dirichlet normalization (including unused terminal gap), Gamma log-convexity step, explicit Gamma lower bound, factorial exponents, pairing count and split count. The time exponent is beta=4-alpha-alpha0 and factorial exponent is q=3-alpha. The initial diagnostic typo preserved in the root checks is not a mathematical input and was not propagated.

A local standard-library check used exact rational arithmetic at the four memo parameter choices, all pairings/splits through k=4 (4,272 parameter/split/pairing checks), and checked positivity and the average of the two Gamma arguments. Exact exponent identities passed. Floating log-Gamma checks at k=1,2,4,16,64 had positive slack; these are diagnostics, not a proof. The manuscript contains the all-order proof.

Read and checked the spatial probe's sphere formula/maximum argument, d2 small-ball constants and layer-cake integral, boundary wedge divergence, product covariance beta integral, positive definiteness via Gaussian mixtures, and sphere projection. Gaussian averaging preserves the successful bounds; Fatou at the singular shifts refutes uniformity in the failure cases. No claim that a divergent spatial maximum disproves the target moment theorem is made.

## Build and frozen identity

Command from repository root:

```text
latexmk -pdf -interaction=nonstopmode -halt-on-error -outdir=notes notes/notes_stratonovich_ham_second_moment.tex
```

Exit 0; final PDF 30 pages. Final log checks: errors=0, undefined references/citations=0, overfull boxes=0; inserted tabs=0. The log also has nonfatal hyperref PDF-string and counter-printing warnings; no blanket warning-free claim. No new overfull repairs were necessary. Every new proof ends with its linked statement reference. No whole-manuscript restyling or visual-review certification is claimed.

- Original TeX SHA-256: `1ca13d491918d96126e70aef6229a80805ce5043a676f0a55c34c0858238e686`
- Candidate TeX SHA-256: `34139160165b61ca770de3ddf90c66459344373ce43930c488365400b91dd27f`
- Inserted section SHA-256: `292838a5f8ffcc108b35b7c8d127be10200245a92b274d0b8d5e205b33d8f336`
- Built PDF SHA-256: `e2a75558f3d0b487065dafb0eba1cc8d04076feea26e4ef8727d07f267ecc40b`

## Honesty concerns and remaining gates

This is GPT-family author work, not an independent review. Root's elementary checks and the worker's diagnostics do not substitute for Opus. Review should scrutinize joint Hölder rather than illegal per-diagram symmetrization; both Dirichlet denominators; regularization uniformity and source-hypothesis matching; d3 limit order; optimality versus mere upper bounds for the spatial constant; and the anisotropic function counterexample's exact scope.

The conditional transfer is not a general high-alpha theorem under homogeneity alone. The Riesz d2 application excludes alpha>=3/2; the product example blocks a universal spatial-hypothesis deduction even below that threshold. Failure of this route does not establish a moment lower bound or failure of the full goal. Constants are deliberately crude; no sharp constant, exact asymptotic limit, originality, full-goal completion, formal verification, or circulation clearance is claimed. Earlier accepted scope text is deliberately preserved, as requested, pending independent adjudication.

STATUS: DONE_WITH_CONCERNS — candidate frozen at the hashes above; independent Opus review pending.
