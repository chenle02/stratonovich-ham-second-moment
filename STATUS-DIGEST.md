# STATUS DIGEST — read this first, then the tail of Progress.md

Current working edition (November 12): **384-page book and 28-page reader**,
with 12 chapters and 6 appendices. Chapter 12 contains 33 numbered no-gos,
now framed by subtle rounded boxes with a 6% blue background. Motivation,
proofs and scope remain outside the boxes. The Preface, roadmap, previous
chapters, reader and subject index link to these results.

The Gold lexical audit repaired domains/definitions in NG13, NG16, NG18,
NG19 and NG33; fresh DeepSeek V4 Pro and native Kimi K3 reviews both returned
PASS/HIGH with no required repairs. The three external citations have a
primary-source pinpoint audit. All 216 pre-existing book proof bodies remain
byte-identical; there are 249 proof bodies including the 33 no-gos.
The Le-approved strategy and scaling explanations were added concurrently
by another author and are preserved.

Formal Chapter 12 Gold certification is **IN PROGRESS**. Its four-role panel,
final replay sequence and evidence closure are distinct from the completed
scoped development reviews. The prior native-accepted visual review covers
the pre-box epoch; current boxed-page checks remain to be completed. No
whole-book or human-verification gate is cleared. The 99-label map and all
272 reader-to-book links pass; both builds have zero errors, undefined
references/citations and overfull boxes. Exact source/PDF pins and review
telemetry: notes/figures/VALIDATION.json and
reviews/2026-11-12-nogo-integration/.

The future-work section discusses higher even moments as open extensions.

November 10/11 (editorial, no mathematical change): the preface now explains
how the book was made with Amy, Le's AI research system, and cites Proofs and
Prompts posts as [P1]-[P11] outside the bibliography. New Appendix E, "The AI
work in numbers" (pp. 300-302): 498 review runs by model family, token totals,
the timeline, and 42 recorded no-gos; every number is rebuilt by
scripts/ai-statistics/. Details and open items: the 2026-11-10/11 entry at the
end of Progress.md.

State as of the November 9 literature revision (baseline `3a94ff9` plus
Agent #16's Lean-header correction `037caa6`); Lean row updated from Agent
#22's companion receipt the same day. This is a **derived summary**, not an
authority. If it conflicts with `Progress.md` (workflow authority) or
`PROJECT-GOAL.md` (completion contract), those win; fix this file.
Update it whenever a gate below changes state.

## One-line state

Research **incomplete.** The focused literature revision is complete locally.
The book-style 284-page working draft
claims both goals; **no whole-paper independent acceptance exists yet.**
The blocker is the review gates, not a known mathematical gap.

## What the draft claims (unadopted)

`notes/notes_stratonovich_ham_second_moment.{tex,pdf}`, 284 pp., 215 OWN
proofs / 241 declarations, clean build (0 err / 0 undef / 0 overfull).
- **G:upper:** `T:full-upper` gives the t^κ scale, κ = (4−α−α₀)/(3−α).
- **G:sharp:** an all-model limit in d = 1,2,3, with C₂ = S₂^pos = 2^{(4−α)/(3−α)} S₁^pos.
  The constant is a variational formula over nonnegative smooth compact
  spacetime controls. It is positive for nonzero γ, zero for γ = 0, and has
  explicit bounds via c²/6 for c·δ₀ in d = 1.
- **Not claimed:** S₁^pos is not shown to be the actual first-moment
  constant; there is no identification with Chen's L; Chen's normalization
  is not corrected.
- The 263-page baseline is at `11e009a`. The 24-page reader
  (`notes/README-reader.md`) is paired with the 284-page book.

## Gate board

| # | Gate (PROJECT-GOAL contract) | State | Evidence |
|---|---|---|---|
| 1 | Complete written proofs | Written; not accepted | main TeX |
| 2 | DeepSeek V4 Pro whole MAIN (HIGH) | **MEDIUM — unaccepted.** PASS_WITH_NOTES, 226 PASS / 37 PWN of 263 rows, no fatal/major/required repair | `reviews/2026-11-09-full-main-v5-kernel-medium-unaccepted/` |
| 3 | Kimi-K3 whole review (HIGH) | **Open — Kimi available again** (Le lifted the hold 2026-11-10); whole review not yet run | Progress 2026-11-10 |
| 4 | Visual / rendered PDF | **Historical 230/267 accepted on the old PDF; 37 old pages open. No automatic visual-credit transfer to the current 284-page edition** | `reviews/2026-11-09-final-local-glyph-correspondence/` |
| 5 | Visual MEDIUM policy | **PROPOSED, NOT ADOPTED — Le's decision** | `reviews/2026-11-09-visual-policy-proposal/POLICY-PROPOSED.md` |
| 6 | Calibrations (α₀→0, p=1, Jensen, Skorohod comparison) | Open as a final gate | AGENTS.md §Calibrations |
| 7 | Fresh independent cold read | Not started | — |
| 8 | Clean build + committed PDF | **PASS** for current bytes | `notes/figures/VALIDATION.json` |
| 9 | Delivery: Progress, wiki status, handoff, <HUB> sync | Git synced. **Wiki project page refreshed 2026-11-09** through the six-repo queue (ticket `tk-20261109-220806-claude-stratonovich-status-digest`, receipt `maintained`, lint clean, wiki commits `aefd5403`, `ae0093ae`). It describes the 269-page unadopted edition, MAIN v5 MEDIUM unaccepted, visual 230/267 on the old edition with no transfer, and keeps the 2026-11-03 block as dated history. Refresh again when a gate changes | `../SPDEs-wiki/content/projects/stratonovich-ham-second-moment.md` |
| L | Lean | Private development: 87 accepted local facts / 26 seams. **Companion created (Le's instruction, 2026-11-09), L0 CLOSED:** `chenle02/stratonovich-ham-second-moment-lean`, PRIVATE until the public flip; verified commit `38d16163` (lean-pkg receipt, registry verified-private). Public counts: 23 of 26 seams, 82 theorems, 43 defs, 88 claims = 78 audited theorems + 6 audited defs + 4 helpers; 68 negative controls all rejected; 0 sorry; axioms propext, Classical.choice, Quot.sound only. 3 seams (9 facts) withheld: they depend on the private gaussian-chaos-lean. Re-anchored at companion `4bdffba` to manuscript `669ccc9` (275 pages; `cf979d6` kept as history): all 46 cited labels exist and the 40 cited statements/proofs are mathematically unchanged, so no correspondence changed. Coverage after the split Codex ledger repair (companion `435fdb0`, docs-only descendant of `38d16163`): 4 main theorems outside Lean, 24 labelled results with analytic inputs supplied (new: `E:kappa`, `L:temporal-equilibrium`). **40 of 88 claim rows map to a manuscript label; 48 are development calculations**; claim rows are not a count of formalized proofs, and the verification section cites only the 40 mapped rows. Ledger correspondence: four valid Codex GPT-6.1-Sol reviews have each FAILED with fatal findings, all repaired: (1) `5e0d122`: `DimensionalMatrix` → `P:actual-wave-form`; (2) `c9e28af`: kernel weight, box rows → `P:radius-mean-anchor`; (3) `1a8c419`: `two_frequency_average` → `L:masked-trig-products`; (4) split review of `0eb9403`, both halves HIGH confidence, main file read gaplessly (lines 1–7706): 86 of 88 rows PASS, `kappa_gt_one` → `E:kappa` and `noise_order` → `L:temporal-equilibrium`. Earlier DeepSeek (MEDIUM) and Kimi-K3 (HIGH, invalid receipts) reports and #3's 2026-11-09 triage missed these. A narrow Codex confirmation of the two repaired rows at companion `48ce162` (re-anchored to manuscript `ba01d98`; cited statements and proofs unchanged except two added figure inputs) returned PASS/HIGH, 6/6, receipt accepted (`reviews/2026-11-10-lean-ledger-codex-confirm/ADJUDICATION.md`). **Correspondence gate CLOSED by Le, 2026-11-10,** at companion `48ce162` over manuscript `ba01d98`, as a documented conjunction (the split complete-reading review of the 86 unchanged rows plus the accepted confirmation of the repairs; no single all-row receipt). Scope: AI statement-to-manuscript correspondence of the ledger only (40 labelled / 48 unlabelled). **Not human verification; analytic inputs outside Lean are not verified;** any later ledger or cited-label change needs a successor review. A human statement read (Group A) is still recommended (`lean-progress/PROGRESS.md`, `d7f3701`). **Wave L1 (2026-11-10):** five labelled results are now formalized in full under the manuscript's own hypotheses (`same-assumptions`): `L:gaussian-scalar-powers`, `L:gram-scalar-algebra`, `L:tube-rayleigh-tail` (without its "In particular" application), `E:kappa` and `E:driver-parameters` under H:homog, which is now modelled in full in Lean. Companion `b876362` (lean-pkg verified-private): 117 claims, 69 labelled / 48 unlabelled; coverage 5 same-assumptions, 19 inputs-supplied, 4 outside. Correspondence of the new rows: the last of three Codex reviews ACCEPTED, PASS_WITH_NOTES/HIGH (`reviews/2026-11-10-lean-homog-model-review/ADJUDICATION.md`, Article `6399c46`); no manuscript defect. **Wave L1 gate CLOSED by Le, 2026-11-10** (scope: AI statement-to-manuscript correspondence of the 29 whole-result ledger rows, including the H:homog model; **not human verification**; any change to these rows or cited labels needs a successor review; `lean-progress/PROGRESS.md`, Article `915ee54`). Work packages B1, B2, B7, B10 and B25 are done; B3, B4 and B9 are reserved as community entry points (not formalized internally before release). **Wave L2 gate CLOSED by Le, 2026-11-10,** at companion `79afdde` over manuscript `ba01d98`: three more whole results (`S:temporal-equilibrium` with its two lemmas under the manuscript's hypotheses; `P:radius-mean-anchor` and `L:masked-trig-products` with every conclusion, their named analytic inputs supplied). Coverage 7 same-assumptions / 18 inputs-supplied / 4 outside; packages B23, B24 and C26 done. Scope: AI correspondence of the 106 wave-L2 ledger rows, **not human verification**; the supplied inputs stay outside Lean (`lean-progress/PROGRESS.md`, Article `635671b`). An Easley `leanchecker --fresh` replay of 837778a (the wave-L2 library) passed 35/35 (companion `687e631`). **Wave L3 gate CLOSED by Le, 2026-11-10,** at companion `dfc2fe8` over manuscript `3920258`: `L:variational-control-dilation`, `L:raw-block-indexed-cone`, `P:clock-copy-obstruction` (then with one supplied input) and the finite slice of `S:compact-gaussian`; four Codex reviews (2 fatal, 12 major, 11 minor findings, all documentation, all repaired) and a confirmation review (`reviews/2026-11-10-lean-wave-l3-*`, Article `56c52f1`). **Wave L4 gate CLOSED by Le, 2026-11-11,** at companion `ac6f767` over manuscript `3920258` (the ledger, claims and coverage files are byte-identical at `2f5ee14`, which carries both lean-pkg receipts): `P:masked-spectral-growth`; `P:clock-copy-obstruction` now with exactly the manuscript's hypotheses (spectral homogeneity derived from `H:homog`); `E:masked-time-schur`, `L:masked-temporal-modulation`; `L:masked-trig-products` input narrowed to the temporal completion; `P:frequency-row`, `C:frequency-time`; `L:occupation-kernel-row`, `L:spatial-physical-pair`; four Codex reviews (0 fatal, 4 major, 4 minor, all documentation, all repaired) and a confirmation review (`reviews/2026-11-11-lean-wave-l4-*`, Article `02e8cdb`). Scope of every gate: AI statement-to-manuscript correspondence, **not human verification**; supplied inputs stay outside Lean; later changes need a successor review. Easley `leanchecker --fresh` replays of the wave-L3 and wave-L4 modules passed (64 runs cover all 51 library modules at `2f5ee14`). **Re-anchor to manuscript `975feb3`** (zero-covariance remark after `H:homog`, nonzero qualification in `T:first`): companion `d40f394`, all 150 cited labels exist, statements and proofs unchanged except `T:full-upper` (cross-reference only); a narrow Codex re-check of the `H:homog` rows PASS/high, accepted by Le 2026-11-11 (`reviews/2026-11-11-lean-reanchor-975feb3`). **Wave L5 gate CLOSED by Le, 2026-11-11,** at companion `712c307` over manuscript `975feb3`: `L:masked-time-completion` (H_a built, density of tests proved), with it `L:masked-trig-products` and `L:masked-continuous-wave` with nothing supplied; `P:masked-auxiliary-norm` (real-H clause not formalized); the rest of `L:damped-homogeneous-norms` (N_0 with the Green mass identity supplied, Le's decision: inputs-supplied, full); `L:variational-heat-envelope` and the display of `L:variational-global-mean`; `L:phase-bessel`; six Codex reviews (0 fatal, 6 major, 2 minor, all documentation, all repaired) and a confirmation review PASS/high 16/16 (`reviews/2026-11-11-lean-wave-l5-*`, Article `ac92bf5`, `b0cdf9e`). Scope: AI statement-to-manuscript correspondence of the wave-L5 ledger rows, **not human verification**; the supplied input stays outside Lean; later changes need a successor review. Package now: 972 claims (810 theorems, 162 definitions; 535 labelled, 437 unlabelled); coverage 26 same-assumptions / 16 inputs-supplied / 4 outside; lean-pkg `verified-private` at `712c307` with both tiers (comparator over all 810 theorem claims); `claims ledger` READY, 0 open; docs-only HEAD `a7f90b0`. Easley `--fresh` replay of the wave-L5 modules at `712c307` passed 9/9 (companion `bae18f4`). **Wave L6 gate CLOSED by Le, 2026-11-11,** at companion `bfa2fd0` over manuscript `975feb3`: `L:damped-homogeneous-norms` now with nothing supplied (wave Green measures, d = 1, 2, 3); `P:masked-quotient-obstruction`; the finite Gaussian comparison of `P:masked-noise-completion` (D1 identification supplied); the spectral core of `P:wave-two-variances` (D1/D8 links supplied); `P:variational-unmasked-rate` (Rayleigh-form part) and `P:variational-positive-scores` (boundedness `S1Bdd` supplied); `P:spatial-smooth-ratio` with R_0 < infinity proved deterministically and `L:spatial-static-controls`; `L:positive-series-type`, `P:moment-growth-logconvex`, `C:static-moment-constant-continuity` (inputs supplied); `C:white-relative-width`, `L:white-clock-laplace`. Eight Codex reviews (2 fatal, 1 major, 13 minor, all documentation, all repaired), a confirmation (one minor, repaired) and a narrow re-confirmation PASS/high 4/4 (`reviews/2026-11-11-lean-wave-l6-*`). Scope: AI statement-to-manuscript correspondence, **not human verification**; supplied inputs stay outside Lean. Package now: 1463 claims (1210 theorems, 253 definitions; 737 labelled, 726 unlabelled); coverage 34 same-assumptions / 21 inputs-supplied / 4 outside; lean-pkg `verified-private` at `bfa2fd0` with both tiers (comparator over all 1210 theorem claims); `claims ledger` READY, 0 open; docs-only HEAD `e4c9bd4`. Both manuscript points added by #3 at Article `a284420`. **Wave L7 gate CLOSED by Le, 2026-11-12,** at companion `f3be834` over manuscript `a284420` (with the re-anchor): `L:inventory-product` (full, nothing supplied), `L:uniform-series-tail` (one input from `L:terminal-wick`), `P:spatial-four-linear`, `P:spatial-energy-map`, `P:occupation-physical-class` (with `H^1` density of test functions proved), scalar steps of `C:static-interaction` and `P:interval-coefficients`; six Codex reviews + confirmations, all findings repaired (one fatal: a plain-English scope sentence said lambda is the Rayleigh supremum instead of its square root; it had reached book p. 307, unpublished, corrected via companion `3c158f5`). **Re-anchored to `a284420`** (new `L:spatial-fourier-bound` row; `L:damped-homogeneous-norms` now narrower); narrow re-check and confirmation PASS/high at companion `f3be834` after 46 citation fixes. Package: 1731 claims (1430 theorems); coverage 39 same-assumptions / 24 inputs-supplied / 4 outside; `verified-private` at `f3be834`, both tiers; ledger READY, 0 open; docs-only HEAD `ed3cd68`; Easley L6 replay 16/16 passed. **Wave L8 gate CLOSED by Le, 2026-11-12,** at companion `aff7409` over manuscript `a284420` (tag `L8-gate`): spectral mass identity R_alpha = R_Gamma(1); damped multiplier lower bounds; space-time positivity; finite occupation ceiling (`T:intrinsic-occupation-ceiling` with K_0 R_sp, same-assumptions, narrower: Le's decision); spatial bracket; mask removal; finite and terminal Wick; symplectic free group; static phase Cauchy-Schwarz; `S1Bdd` proved with nothing supplied. Six Codex reviews, two repair rounds, a confirmation and a re-confirmation PASS/high 24/24 (`reviews/2026-11-12-lean-wave-l8-*`, Article `9c0df47`); recorded: chain measures supplied by their mass, and `hK` (global covariance measurability) an added restriction. Package: 2108 claims (1747 theorems); coverage 43 same-assumptions / 25 inputs-supplied / 3 outside. Scope: AI correspondence, **not human verification**. **Wave L9 gate CLOSED by Le, 2026-11-12,** at companion `6eb79c7` over manuscript `a284420` (tag `L9-gate`; docs successor `f8c9da0`): low-alpha convolution (d = 1, 2, 3) and phase contractions (d = 3) with nothing supplied; wave Green Fourier identities; complex phase scalar steps; exact occupation ceiling C_occ (still narrower: C_2 sentence, class O); Gaussian Hermite, Fock layer and Fock form (FockColumn supplied); one-mode finite word cutoff. Eight Codex reviews, ten confirmation rounds, final one-check confirmation PASS/high at `ff40fde` (`reviews/2026-11-12-lean-wave-l9-*`, Article `fdc863cc`); receipts at `6eb79c7` (comparator 2050 theorem claims PASS; lower tier 0 sorry, 2468 claims; ledger READY); Easley replay 103/103; Slurm receipt pilot identical to the local receipt. Package: 2468 claims (2050 theorems); coverage 47 same-assumptions / 30 inputs-supplied / 3 outside. A docs-only correction of the public-definition count (89 vs 91) follows as an approved successor. **Wave L10 gate CLOSED by Le, 2026-11-13,** at companion `b2bf7a9` over manuscript `a284420` (tag `L10-gate`, private dev repository; docs successor `d6a0505`), with the added hypothesis hQ recorded as accepted for now: higher Riesz bound in full for d = 2, 3 (optimal constant in d = 3); alpha-one convolution from H:homog alone; white-noise model and white moment bounds for S_2^pos (spatial energy supplied, B9); fixed split (core and Fock assembly). Eight Codex reviews, a confirmation and a re-confirmation PASS/high at `0904978`; receipts `c622c25` (comparator 2268 theorem claims PASS; lower tier 0 sorry, 2757 claims; ledger READY); Easley 111/111 at `b2bf7a9`; second Slurm receipt identical. Package: 2757 claims (2268 theorems); coverage 82 rows, 49 same-assumptions / 31 inputs-supplied / 2 outside. Waves L11-L14 in progress (Lean freeze after this wave); public release v0.9.0 (L9 state) in preparation | `lean-progress/PROGRESS.md`; companion `docs/statement-ledger.md`, `coverage.yaml` |

## Standing constraints (do not violate)

[held back: collaborators' unpublished work]

## Pending decisions for Le

1. The agreed "focused recovery" direction is **not yet written** into
   PROJECT-GOAL.md / Progress.md. Record it before new research work.
2. Adopt or reject the visual MEDIUM policy proposal (gate 5).
3. Path to a HIGH whole-math verdict without unchanged retries (gate 2),
   and scheduling the Kimi-K3 whole review now that Kimi is available (gate 3).
4. Lean companion: created and verified (decision point 4 settled by Le,
   2026-11-09). Open: the community Lean effort (release design D9).

## Where to look

- Latest state: the last ~10 `## 2026-11-09` entries of `Progress.md`.
- Human narrative and failed routes: `AI-DEV-HISTORY.md`.
- Draft status: `notes/WORKING-DRAFT-STATUS.md`. Next-session rules: `HANDOFF.md`.

## Current literature task

Le requested the source-checked literature/contribution revision, emphasizing
the present result and three ongoing Balan/Chen/Wang Skorohod projects. See
notes/LITERATURE-REVIEW.md and reviews/2026-11-09-literature-review/. The new
269+20-page pair has clean builds,69 matched labels and 209 valid remote links.
All 215 technical proofs and checked statements are unchanged modulo whitespace.
This bounded editorial task does not complete the original research contract
or promote any independent mathematical/visual review.

## Earlier illustration and style revision (669ccc9)

That edition has 275 technical pages with 12 figures and 24 reader pages with
7 figures. All 71 external technical labels and233 PDF links resolve. Prose
was reviewed throughout the main source,27 modules and reader; private jargon
was replaced, source typing checked, and both builds are clean. The 215 technical
proofs retain their mathematics and labels. Illustration review inspected all
19 figure pages, not the entire new PDFs; no scientific confidence is promoted.
The wiki receipt above describes the preceding269-page edition and needs its
next status refresh to mention this edition. The Lean companion's pinned
cf979d6 source remains historical until its owner updates the anchor manifest.

## Book-format checkpoint

The long companion is 284 pages with 11 numbered chapters and 4 appendices; the
reader remains 24 pages. Both keep the 12/7 diagrams. Stable labels are retained,
but the reader map now has 78 labels and 240 valid remote links. Existing
section-number literals were repaired; source-paper pinpoints are unchanged.
All 215 proofs retain their mathematics. This layout change does not clear a
scientific gate. Use notes/BOOK-GUIDE.md, notes/book-numbering-map.json and
notes/figures/VALIDATION.json. Companion anchoring and the wiki's current-edition
status should be refreshed by their owners after this committed checkpoint.
