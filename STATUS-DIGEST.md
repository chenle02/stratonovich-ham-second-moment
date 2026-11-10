# STATUS DIGEST — read this first, then the tail of Progress.md

Current editorial edition (November 10): **301-page book and 28-page reader**.
All eleven chapters and four appendices have motivation, linked prerequisites
and an outline. Section 1.5 states the two existing results as Theorems 1.5.1
and 1.5.2, with links to their unchanged proofs. All 215 proof bodies are
preserved; 81 technical labels and 248 reader links pass. This presentation
update does not clear the independent review gates below. Older page counts
in dated entries describe their historical editions. Exact current pins:
notes/figures/VALIDATION.json.

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
| L | Lean | Private development: 87 accepted local facts / 26 seams. **Companion created (Le's instruction, 2026-11-09), L0 CLOSED:** `chenle02/stratonovich-ham-second-moment-lean`, PRIVATE until the public flip; verified commit `38d16163` (lean-pkg receipt, registry verified-private). Public counts: 23 of 26 seams, 82 theorems, 43 defs, 88 claims = 78 audited theorems + 6 audited defs + 4 helpers; 68 negative controls all rejected; 0 sorry; axioms propext, Classical.choice, Quot.sound only. 3 seams (9 facts) withheld: they depend on the private gaussian-chaos-lean. Re-anchored at companion `4bdffba` to manuscript `669ccc9` (275 pages; `cf979d6` kept as history): all 46 cited labels exist and the 40 cited statements/proofs are mathematically unchanged, so no correspondence changed. Coverage after the split Codex ledger repair (companion `435fdb0`, docs-only descendant of `38d16163`): 4 main theorems outside Lean, 24 labelled results with analytic inputs supplied (new: `E:kappa`, `L:temporal-equilibrium`). **40 of 88 claim rows map to a manuscript label; 48 are development calculations**; claim rows are not a count of formalized proofs, and the verification section cites only the 40 mapped rows. Ledger correspondence: four valid Codex GPT-6.1-Sol reviews have each FAILED with fatal findings, all repaired: (1) `5e0d122`: `DimensionalMatrix` → `P:actual-wave-form`; (2) `c9e28af`: kernel weight, box rows → `P:radius-mean-anchor`; (3) `1a8c419`: `two_frequency_average` → `L:masked-trig-products`; (4) split review of `0eb9403`, both halves HIGH confidence, main file read gaplessly (lines 1–7706): 86 of 88 rows PASS, `kappa_gt_one` → `E:kappa` and `noise_order` → `L:temporal-equilibrium`. Earlier DeepSeek (MEDIUM) and Kimi-K3 (HIGH, invalid receipts) reports and #3's 2026-11-09 triage missed these. A narrow Codex confirmation of the two repaired rows at companion `48ce162` (re-anchored to manuscript `ba01d98`; cited statements and proofs unchanged except two added figure inputs) returned PASS/HIGH, 6/6, receipt accepted (`reviews/2026-11-10-lean-ledger-codex-confirm/ADJUDICATION.md`). **Correspondence gate CLOSED by Le, 2026-11-10,** at companion `48ce162` over manuscript `ba01d98`, as a documented conjunction (the split complete-reading review of the 86 unchanged rows plus the accepted confirmation of the repairs; no single all-row receipt). Scope: AI statement-to-manuscript correspondence of the ledger only (40 labelled / 48 unlabelled). **Not human verification; analytic inputs outside Lean are not verified;** any later ledger or cited-label change needs a successor review. A human statement read (Group A) is still recommended (`lean-progress/PROGRESS.md`, `d7f3701`). **Wave L1 (2026-11-10):** five labelled results are now formalized in full under the manuscript's own hypotheses (`same-assumptions`): `L:gaussian-scalar-powers`, `L:gram-scalar-algebra`, `L:tube-rayleigh-tail` (without its "In particular" application), `E:kappa` and `E:driver-parameters` under H:homog, which is now modelled in full in Lean. Companion `b876362` (lean-pkg verified-private): 117 claims, 69 labelled / 48 unlabelled; coverage 5 same-assumptions, 19 inputs-supplied, 4 outside. Correspondence of the new rows: the last of three Codex reviews ACCEPTED, PASS_WITH_NOTES/HIGH (`reviews/2026-11-10-lean-homog-model-review/ADJUDICATION.md`, Article `6399c46`); no manuscript defect. **Wave L1 gate CLOSED by Le, 2026-11-10** (scope: AI statement-to-manuscript correspondence of the 29 whole-result ledger rows, including the H:homog model; **not human verification**; any change to these rows or cited labels needs a successor review; `lean-progress/PROGRESS.md`, Article `915ee54`). Work packages B1, B2, B7, B10 and B25 are done; B3, B4 and B9 are reserved as community entry points (not formalized internally before release) | `lean-progress/PROGRESS.md` (f4aab9a); companion `docs/statement-ledger.md`, `coverage.yaml` |

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
