# Progress.md — Article-Stratonovich-HAM-Second-Moment

> **AUTHORITY.** This file is the sole source of truth for the workflow state
> (per `progress-md-authority-paper-dev`). Start every session here. Update it
> at the end of every round, before committing.

## Current state

- **Phase:** Round 0 complete (setup, 2026-10-26). Next: **Round 1 = Gate G0**.
- **Proved in this project:** Proposition P:Jensen only (liminf ≥ 2L_*), in
  the notes, §2.
- **Open targets:** Goal G:upper, Goal G:sharp (see PROJECT-GOAL.md).
- **Blocking human decisions:** none.
- **Worker:** Codex agent #30 (<MACHINE>, `n30-stratonovich-ham-second`), handed over
  2026-10-26; workflow paper-dev + lean-pkg (Lean track: `lean-progress/PROGRESS.md`).

## Round plan

Each round: one bounded question, a frozen claim boundary, a written result
in the notes (or a recorded no-go), a cross-family review for any new proof,
then the round-close protocol (`paper-dev-round-close-protocol`).

| Round | Gate | Question | Exit criterion |
|---|---|---|---|
| 1 | **G0 diagnosis** | (a) Justify 𝔼u² = Σ_{m,n} 𝔼[S_m(g_m)S_n(g_n)] (m+n even) from (2.13), (2.18), (2.21) and Theorem 1.1, and write each term as a two-chain pairing integral in the form of (3.6). (b) Reproduce Remark 5.1's e^{Ct²} from (2.13), (4.4) and locate exactly where the exponent 2 enters instead of κ. (c) Decide whether Theorem 3.1 with Laplace-weighted kernels (Lemma A.1) can give the scale t^κ. | A written section in the notes: the cross-term formula with proof; the diagnosis; a verdict "Theorem 3.1 route viable / not viable" with the counting argument. |
| 2 | **G1 calibration and small cases** | Compute the n = 1, 2 (chaos orders 2 and 4) contributions to 𝔼u² explicitly (d = 1, α = 1 white space first; then Riesz) and compare their growth with t^κ scaling; check the α₀→0 limit against Chen–Hu (2025). | Explicit low-order formulas plus a calibration table in the notes. |
| 3 | **G2 upper bound** | Prove Goal G:upper by the route chosen in G0 (Laplace transform, two-chain bound, scaling, Tauberian/Mittag-Leffler conversion). | Complete proof plus Opus skeptic review, findings adjudicated. |
| 4+ | **G3 sharp constant** | Two-clock analogue of Chen's Theorem 6.1 for two ordered chains, and the matching large deviations (Theorem 7.1 analogue); lower bound beyond Jensen first. | Per sub-goal; record partial results honestly. |

## Decisions log

[held back: collaborators' unpublished work]

## Verified facts (setup reading, 2026-10-26)

- Theorem 1.2 (p. 3) gives two-sided first-moment bounds L_* ≤ liminf ≤
  limsup ≤ L^*, with L(𝓔) as in the notes; 𝓔_* < 𝓔 ((1.11)–(1.13), p. 4).
- Remark 5.1 (p. 37): 𝔼u²(t,x) ≤ e^{Ct²} for large t, "from (2.13) and (4.4)".
- Remark 6.3 (p. 42): single-chain monotone ordering is why the method
  stops at p = 1.
- Theorem 3.1 (p. 15): universal two-chain pairing bound, including
  cross-pairings, over a partition {Q₀,Q₁,Q₂} with #Q₀ = #Q₁, #Q₂ even.
- Theorem 4.1 (4.3) (p. 22): exact two-chain formula for 𝔼[S_n(g_n)]².
- Conjecture (1.22) (p. 6): constant p^{(4−α)/(3−α)} L^* for p = 1, 2, …

## Failed routes / no-gos

(none yet)

## Round log

| Round | Date | Outcome | Commit |
|---|---|---|---|
| 0 | 2026-10-26 | Setup: repo, notes scaffold (5 pp, clean build), source manifest, wiki project page | see git log |
