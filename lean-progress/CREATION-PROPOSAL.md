# Decision point 4: private companion proposal

Status: PROPOSED, not created or registered (2026-10-27).

## Concrete package

- Name: `stratonovich-ham-second-moment-lean`.
- Namespace: `StratonovichHAMSecondMoment`.
- Checkout: `../stratonovich-ham-second-moment-lean`.
- Private origin: <HUB> bare repository
  `<REMOTES>/stratonovich-ham-second-moment-lean.git` (relative to the
  <HUB> account home). No public GitHub repository or publication.
- Lean: `leanprover/lean4:v4.35.0`.
- Mathlib: `56a005855ea17e0b0958f73ec801ae140b0a1679`, release `v4.35.0`;
  its own lean-toolchain matches. Transitive dependencies will be locked by
  the generated manifest, not guessed here.
- After approval: create through lean-pkg, register privately, claim a lease,
  compile locally, and retain source-bound verify/receipt/gate evidence.
  No Easley use is proposed.

Release provenance: official Lean and Mathlib latest stable release endpoints
were checked on 2026-10-27; both report v4.35.0 (October 12/13 respectively).
Sources: https://github.com/leanprover/lean4/releases/tag/v4.35.0 and
https://github.com/leanprover-community/mathlib4/releases/tag/v4.35.0.

## First statement fence (G0, already informally reviewed)

1. Reuse the exact-compatible Physlib count of actual fixed-point-free
   involutions on Fin(2k), identify its two-element orbits with manuscript
   pair partitions, and derive the factorial-form consumer. Do not rebuild
   the counting library or define a scalar recurrence as a substitute.
2. Deduce k! <= Pk <= 2^k k!, including k=0, and the 2k+1 chain-length splits.
3. For a partition into Q0,Q1,Q2, derive q0+q2/2=k from q0=q1,
   q0+q1+q2=2k and even q2, with exact natural-number division obligations.
4. Prove the parameter algebra: beta=4-alpha-alpha0>2 and
   1<kappa<rho<2, where kappa=beta/(3-alpha), rho=beta/(beta-1), under
   0<alpha0<1, 0<alpha and alpha+alpha0<2.

This verifies finite/algebraic parts of P:envelope and the cross-term count.
The SPDE, generalized stochastic integrals, analytic norm scaling, imported
Chen theorems and asymptotic series comparison remain outside this initial
fence. No new axioms or assumed target conclusions are proposed. Wave L2
may separately formalize the series growth deduction once L1 is accepted.

## Reuse search and disposition

- Registry searches for pairing, perfect matching and double factorial found
  private SWEExactMomentsR2 finite-group matching lemmas. Direct source
  inspection shows that these count permutations/bipartite matchings, not
  all pair partitions with within-chain pairs. They are possible algebraic
  helpers, not a substitute for the actual Stratonovich counting statement.
- GaussianChaos exists privately on <HUB>/GitHub; the local checkout
  was absent. Its source tree was inspected remotely and is a candidate
  foundations dependency only, not a namespace/scope duplicate.
- Mathlib has Nat.doubleFactorial and graph perfect-matching infrastructure;
  prefer its existing definitions and lemmas. Complete the exact-pinned
  source/Loogle search before adding any nontrivial definition.
- No existing package with the proposed name/namespace was found in the
  registry, and the proposed <HUB> remote is absent.
- Search outputs are in `../reviews/2026-10-27-round2/recon/`.
  Searches are explicitly incomplete (some registry checkouts absent and
  sources omitted/capped); this is not a global theorem-absence claim.

## Approval boundary

PROJECT-GOAL.md decision point 4 requires Le's decision before creating the
companion repository. This proposal creates no repository, changes no sibling,
and claims no Lean verification. Mathematics calibration can proceed while
this package decision is pending.

## Parallel source-search update

Exact compatible reuse was found after the initial proposal: Physlib commit
`3bfc7af8dbd43b439d761e09ce365a3759b5c2f5`, theorem
`Physlib.Fin.involutionNoFixed_card_mul_two`, uses the proposed Lean/Mathlib
pins and counts the actual objects including zero order. Its source module
imports only Mathlib. Prefer an exact-pinned dependency/import and retain its
Apache-2.0 attribution; a Mathlib cycle-type specialization is an alternative,
not a second library to build in parallel. No proof/build acceptance follows
from source inspection. See `recon/2026-10-27-reuse.md` for exact statements,
license/source pins and search limitations. The proposed private repository
name, remote and approval boundary are unchanged.

## Reviewed G2 consumer update

The accepted informal upper proof now covers 0<alpha<=1 in d1/2/3.
After creation approval, the finite/algebraic audit should also reach its
actual consumers: descending-label dependence, the fully summed temporal
pairing permutation invariance, the block-order/split factorial cancellation,
AM–GM constant algebra (with alpha=1 separate), and the factorial/power
conversion to kappa. The scalar series bound is a useful later analysis seam.
Do not claim the spectral, stochastic-integral or SPDE steps are formalized
merely from a finite count certificate. Exact source labels are in notes §5;
no new package or code is created by this proposal update.
