# STATUS DIGEST — read this first, then the tail of Progress.md

State as of the November 9 literature revision (baseline `3a94ff9` plus
Agent #16's Lean-header correction `037caa6`); Lean row updated from Agent
#22's companion receipt the same day. This is a **derived summary**, not an
authority. If it conflicts with `Progress.md` (workflow authority) or
`PROJECT-GOAL.md` (completion contract), those win; fix this file.
Update it whenever a gate below changes state.

## One-line state

Research **incomplete.** The focused literature revision is complete locally.
The illustrated275-page working draft
claims both goals; **no whole-paper independent acceptance exists yet.**
The blocker is the review gates, not a known mathematical gap.

## What the draft claims (unadopted)

`notes/notes_stratonovich_ham_second_moment.{tex,pdf}`, 275 pp., 215 OWN
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
  (`notes/README-reader.md`) is paired with the275-page draft.

## Gate board

| # | Gate (PROJECT-GOAL contract) | State | Evidence |
|---|---|---|---|
| 1 | Complete written proofs | Written; not accepted | main TeX |
| 2 | DeepSeek V4 Pro whole MAIN (HIGH) | **MEDIUM — unaccepted.** PASS_WITH_NOTES, 226 PASS / 37 PWN of 263 rows, no fatal/major/required repair | `reviews/2026-11-09-full-main-v5-kernel-medium-unaccepted/` |
| 3 | Kimi-K3 whole review (HIGH) | **BLOCKED — Le's hold** (weekly 429 quota) | Progress 2026-11-09 |
| 4 | Visual / rendered PDF | **Historical 230/267 accepted on the old PDF; 37 old pages open. No automatic visual-credit transfer to the current275-page edition** | `reviews/2026-11-09-final-local-glyph-correspondence/` |
| 5 | Visual MEDIUM policy | **PROPOSED, NOT ADOPTED — Le's decision** | `reviews/2026-11-09-visual-policy-proposal/POLICY-PROPOSED.md` |
| 6 | Calibrations (α₀→0, p=1, Jensen, Skorohod comparison) | Open as a final gate | AGENTS.md §Calibrations |
| 7 | Fresh independent cold read | Not started | — |
| 8 | Clean build + committed PDF | **PASS** for current bytes | `notes/figures/VALIDATION.json` |
| 9 | Delivery: Progress, wiki status, handoff, <HUB> sync | Git synced. **Wiki project page refreshed 2026-11-09** through the six-repo queue (ticket `tk-20261109-220806-claude-stratonovich-status-digest`, receipt `maintained`, lint clean, wiki commits `aefd5403`, `ae0093ae`). It describes the 269-page unadopted edition, MAIN v5 MEDIUM unaccepted, visual 230/267 on the old edition with no transfer, and keeps the 2026-11-03 block as dated history. Refresh again when a gate changes | `../SPDEs-wiki/content/projects/stratonovich-ham-second-moment.md` |
| L | Lean | Private development: 87 accepted local facts / 26 seams. **Companion created (Le's instruction, 2026-11-09), L0 CLOSED:** `chenle02/stratonovich-ham-second-moment-lean`, PRIVATE until the public flip; verified commit `38d16163` (lean-pkg receipt, registry verified-private). Public counts: 23 of 26 seams, 82 theorems, 43 defs, 88 claims = 78 audited theorems + 6 audited defs + 4 helpers; 68 negative controls all rejected; 0 sorry; axioms propext, Classical.choice, Quot.sound only. 3 seams (9 facts) withheld: they depend on the private gaussian-chaos-lean. Coverage after the ledger review (companion `a78c5d0`, docs-only descendant of `38d16163`): 4 main theorems outside Lean, 20 labelled results with analytic inputs supplied. 33 of 88 claim rows map to a manuscript label; the other 55 are development calculations that make no current-paper claim (#3's ruling, `private/audit/2026-11-09-companion-target-triage.md`), and claim rows are not a count of formalized proofs. The verification section cites only the 33 mapped rows. DeepSeek V4 Pro ledger-correspondence review: PASS_WITH_CONCERNS, MEDIUM, 0 critical / 1 major / 6 minor, all adjudicated, no Lean or manuscript defect; **below the HIGH gate, so correspondence is not yet accepted** (`reviews/2026-11-09-lean-ledger-correspondence/ADJUDICATION.md`) | `lean-progress/PROGRESS.md` (f4aab9a); companion `docs/statement-ledger.md`, `coverage.yaml` |

## Standing constraints (do not violate)

[held back: collaborators' unpublished work]

## Pending decisions for Le

1. The agreed "focused recovery" direction is **not yet written** into
   PROJECT-GOAL.md / Progress.md. Record it before new research work.
2. Adopt or reject the visual MEDIUM policy proposal (gate 5).
3. Path to a HIGH whole-math verdict without unchanged retries (gate 2),
   and when the Kimi hold ends (gate 3).
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

## Current illustration and style revision

The current pair is275 technical pages with 12 figures and24 reader pages with
7 figures. All 71 external technical labels and233 PDF links resolve. Prose
was reviewed throughout the main source,27 modules and reader; private jargon
was replaced, source typing checked, and both builds are clean. The 215 technical
proofs retain their mathematics and labels. Illustration review inspected all
19 figure pages, not the entire new PDFs; no scientific confidence is promoted.
The wiki receipt above describes the preceding269-page edition and needs its
next status refresh to mention this edition. The Lean companion's pinned
cf979d6 source remains historical until its owner updates the anchor manifest.
