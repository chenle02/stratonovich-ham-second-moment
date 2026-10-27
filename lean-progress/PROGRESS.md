# PROGRESS.md — Lean track (lean-dev authority)

> Authority for the **Lean companion** of Article-Stratonovich-HAM-Second-Moment
> (per the `lean-dev` skill). The mathematics authority is `../Progress.md`.
> `.lean-dev-state.json` mirrors this file and changes only together with it.

## Current wave

- **Wave:** L0 (setup) — `PROPOSED`
- **Companion package:** not yet created. Planned name
  `stratonovich-ham-second-moment-lean` (private, registered through
  `lean-pkg register` only after `lean-pkg search` finds no reusable package).
- **Next:** wave L1 opens only after math Round 1 (Gate G0) has a written,
  reviewed statement worth formalizing.

## Planned waves (strategy in ROADMAP.md)

| Wave | Target | Opens when |
|---|---|---|
| L1 | The finite combinatorics of Gate G0: pair-partition counts for the two-chain integrals and the counting argument that decides whether Theorem 3.1 reaches the scale t^κ | G0 verdict written in the notes |
| L2 | Laplace-to-time growth lemma (Mittag-Leffler / Tauberian conversion) with the analytic inputs as explicit hypotheses; reusable | G2 route fixed |
| L3 | Scalar/algebraic deductions of the G:upper and G:sharp proofs (constants, exponents, the factor 2^{1/(3-α)}) | the corresponding paper proofs reviewed |

## Wave log (append-only)

| Wave | State | Date | Evidence |
|---|---|---|---|
| L0 | PROPOSED | 2026-10-26 | Setup by session #4; no Lean code yet |
