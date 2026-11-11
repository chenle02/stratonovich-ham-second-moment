# Adjudication: narrow re-check of the H:homog rows after the 975feb3 re-anchor

- **Object:** the Lean companion at `d40f394` (re-anchor commits `c308c82`
  docs and `d9e5ce9` comment/summary line shifts, plus `d40f394`, two
  off-by-one citations corrected) against manuscript revision `975feb3`,
  which added the "Zero covariance" paragraph after `H:homog` (main TeX
  209-214) and qualified the strict comparison `E_* < E` in `T:first` as
  asserted only for `Gamma != 0` (426-432). Six checks: the ledger's anchor
  paragraph and `manuscript-anchor.json`; the `HomogHypothesis` section
  (the Lean model admits `Gamma = mu = 0`, as `H:homog` now says it does by
  design); every other ledger row and coverage note citing `H:homog`
  (strict positivity carries `Gamma != 0`, nothing adds an unsupported
  nondegeneracy); the line citations into the model section and
  `integrated_covariance_foundation.tex`; the `T:full-upper` row; no new
  error in the touched Scope, Index and Not-in-Lean sections.
- **Reviewer:** Codex GPT-6.1-Sol, effort high, read-only, `CODEX_HOME`
  workaround; frozen packet (ledger, claims.yaml, coverage.yaml,
  provenance, Lean modules, all 78 TeX inputs at `975feb3` and the main
  file at `3920258`); contract-check (schema), dry run and contract-check
  on the dispatched prompt clean for both attempts.

## Attempt v1 (`attempt-v1/`): INCONCLUSIVE, medium, not accepted

Five checks PASS; HOMOG-CONSUMERS INCONCLUSIVE; no findings. The only
reason: the packet held twelve Lean modules and lacked
`DampedNorms.lean`, whose declaration `damped_norms_finite_paper` is named
by ledger line 819, so the contract's direct-reading requirement could
not be met. Required repair: supply the file (a packet defect, not a
ledger defect). Checked by hand: `DampedNorms.lean:358-370` assumes
`HomogCovariance` and `SpectralHomogeneous mu alpha`, not `Gamma != 0`,
and proves the three integrability statements the row lists; finiteness
holds at `Gamma = 0`, so the row needs no nonzero hypothesis. Disposition:
packet repaired; review rerun as v2.

## Attempt v2 (`attempt-v2/`): PASS, high, accepted

Same contract plus a note on the earlier attempt; the packet holds all 27
modules of `StratonovichHAMSecondMoment/`. 6 checks PASS; 0 fatal, 0
major, 0 minor; no required repairs. The reviewer confirmed: H:homog at
975feb3 lines 190-207 identical to 3920258 lines 169-186; `HomogCovariance`
has no nonzero field; strict positivity rows (ledger 854, 1677, 1678;
coverage.yaml 453-456) match `ClockCopy.lean:722-734`,
`ClockCopyHomog.lean:53-65` and `MaskedSpectralGrowth.lean:501-517`, all
with `Gamma != 0`; homogeneity, finiteness and nonnegativity rows keep zero
covariance; no stale citation into main lines 150-450; `T:full-upper`
correctly outside Lean.

| ID | Sev | Disposition | Verified | Repair (companion) |
|---|---|---|---|---|
| (none) | | | | |

Afterwards: the 975feb3 re-anchor needs no correspondence repair. Article
commits after `975feb3` (to `f4cd8d4`) change only `preface.tex`,
`ai-statistics.tex` and `ai-statistics-data.tex`, none cited by the
companion, so the anchor stands.
