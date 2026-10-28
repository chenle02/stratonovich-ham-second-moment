# PROGRESS.md — Lean track (lean-dev authority)

> Authority for the **Lean companion** of Article-Stratonovich-HAM-Second-Moment
> (per the `lean-dev` skill). The mathematics authority is `../Progress.md`.
> `.lean-dev-state.json` mirrors this file and changes only together with it.

## Current wave

- **Wave:** L0 (setup) — `PROPOSED`
- **Companion package:** not yet created. Planned name
  `stratonovich-ham-second-moment-lean` (private, registered through
  `lean-pkg register` only after `lean-pkg search` finds no reusable package).
- **Next execution gate:** explicit approval at PROJECT-GOAL.md decision point 4
  before companion creation. G0 and the alpha<=1 proof now have reviewed
  statements; that mathematical readiness does not authorize creating a repo.
  No L1 wave, lease, code, local build or cluster job has been opened.

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
| L0 | PROPOSED | 2026-10-28 | Readiness/strategy refresh after source and plane-endpoint reviews; creation approval still pending, no package or Lean verification |

## New proof seams retained for later statement fences

See ROADMAP.md for exact proposed roles and analytic exclusions. These are
planning items, not opened Lean claims:

- Section9 product-endpoint interval algebra and affine coefficient exponents
  (the full moment review remains all14PASS/medium, below HIGH).
- The accepted plane-endpoint parameter algebra and finite positive-sum
  comparison, with covariance/Holder inputs explicit.
- The exact rational separation used by the independently checked source
  normalization audit, with its functional bounds as named hypotheses.
- Static p2 factor-two algebra, keeping the imported coefficient rate and
  its time-independent order threshold outside a pure arithmetic claim.

The existing creation proposal and initial G0 statement fence are unchanged.
Before execution, renew registry/Mathlib reuse searches and compatible release
pins, then use a private registered package and lease after approval. This
ledger update is not a workaround for the creation gate.
