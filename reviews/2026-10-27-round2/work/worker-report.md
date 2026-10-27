# Round 2 G1 worker report

## Todo and scope

- [x] Read current workflow authority and completion contract; user continuation reported by root authorizes G1 after G0.
- [x] Derive all white-space order-four spatial reductions and temporal gaps.
- [x] Obtain independent exact static controls from spatial-sector integration.
- [x] Derive Riesz order-two coefficients and an explicit finite order-four representation.
- [x] Check normalization, finite-order static limits, and scope of asymptotic comparison.
- [x] Write complete G1 section and build clean.
- [ ] Independent Opus review and root adjudication.

The existing G0 results are retained. No all-order factorial estimate, G:upper/G:sharp proof, Skorohod result, new Lean package, sibling edit, external communication, or git operation is claimed or performed by the worker.

## Mathematical deliverables

`P:white-four` (Proposition 4.1) supplies all 15 order-four terms: nine distinct rows for splits (0,4),(1,3),(2,2), and chain exchange supplies the three rows each for (4,0),(3,1). It gives each spatial volume and both temporal pair gaps. The four wave factors contribute 1/16; normalized delta contractions leave a two-dimensional area, with no pairing multiplicity omitted.

`L:static-four` (Lemma 4.2) proves the alpha0↓0 limit at each coefficient by dominated convergence and calculates its exact value. At unit time:

| Split | A=(12)(34) | B=(13)(24) | C=(14)(23) | Sum |
|---|---|---|---|---|
| (0,4) | 1/2880 | 1/8640 | 1/5760 | 11/17280 |
| (1,3) | 1/576 | 29/34560 | 1/640 | 143/34560 |
| (2,2) | 1/144 | 1/480 | 31/17280 | 187/17280 |

The total static order-four coefficient is 2*(11/17280)+2*(143/34560)+187/17280=11/540; total order two is 1/3. These are multiplied by t^6 and t^3, respectively. No remainder estimate or large-time expansion is asserted.

`P:riesz-small` (Proposition 4.3) gives closed/one-dimensional order-two formulas for gamma=c_alpha |x|^-alpha, d1,0<alpha<1, and a fully specified unit-domain order-four integral for every split and pairing. In the latter, each Green measure is h_l times a uniform probability law, so product(h_l), not product(h_l)/16, accompanies the expectation. The representation includes explicit linear time and spatial forms and the independent uniform law; it is not claimed to be a closed-form evaluation.

`R:riesz-static` (Remark 4.4) records the static Riesz degree-two coefficient and the normalization c_alpha=(1-alpha)/2. For each fixed alpha0 the two normalized order-two coefficients converge to c0/2 and c0 as alpha↑1, recovering the white values.

`R:G1-scope` (Remark 4.5) records the necessary exponent calibration, Jensen consistency, structural Skorohod comparison only, and why finitely many coefficients cannot determine the missing all-order factorial power.

## Falsification and independent controls

The time-minimum/interval-area reduction was derived first in `derivation.md`. The exact static check uses a different order of integration: integrate all time slacks first to obtain (1-L1)^m_+(1-L2)^n_+/(16m!n!), then integrate the resulting polynomial over six spatial sectors. This produces the exact rational table and catches wave-normalization or time-simplex factorial errors.

- `static_controls.py` with `static-controls.json`: exact rational SymPy integration of every polynomial sector for all nine distinct rows. This is a computational cross-check; the written proof includes lengths, sector substitutions, exact sector-integral table, and the nontrivial split-sector integrals. No Lean certificate is claimed.
- `numerical_controls.py` with `numerical-controls.json`: independently evaluates the time-reduced static formulas using two scrambled Sobol samples of 262144 points each (seeds271,828). Largest relative deviations from exact values are 0.0001488 and 0.0002482. These are floating diagnostics, not rigorous error bars or certified quadrature.
- The same numerical script compares the Riesz order-two integrated formula with a direct transformed two-dimensional triangular integral at alpha=alpha0=1/2,c_alpha=1. Values are 1.7138642178632644 and 1.7138642178647279, difference about1.46e-12. This is floating agreement, not proof.
- Root separately reports IID Monte Carlo of the original four-time/two-space-color contracted integrals. Root owns that independent evidence; it is not attributed to this worker.

No new fractional-time singular Monte Carlo estimate is presented. The explicit formulas, rather than a numerical guess, are the deliverable.

## Source binding

G1 uses the reviewed G0 mixed-diagram formula, its regularization conventions and wave normalization. No arXiv-v1 first-moment theorem is used.

The only newly cited external asymptotic input is the exponent in Chen–Hu (2025), published Theorem1.2,(1.9), journal p2147. The rendered fourth PDF page was inspected from `../SPDEForge/sources/chen_hu-25-hyperbolic/published-24-AOP1758.pdf`; SHA-256 `58b152d78cd0d54d82b991933b3eaece86e1ed2b44fe09882c14eba921e97e22`. Its publication audit gives the published/preprint number crosswalk. The printed white-space corollary constant is not used; the separate source audit records a discrepancy. No source PDF or sibling file was changed.

## Honesty and review focus

[held back: collaborators' unpublished work]

## Validation and freeze

Only the new G1 section was passed through format-tex. The complete notes build has 0 errors, 0 undefined references/citations, and 0 overfull boxes; 17 pages. Representative rendered formula tables were inspected. The existing G0 reviewed material is unchanged apart from abstract/title navigation acknowledging G1.

Final candidate TeX SHA-256: `1d1646e5b45ce8a80a5ccbde83bc944b8a0b1027620fc5ba6429be57c6c75560`.
Final candidate PDF SHA-256: `bfa0b11fb4f85a9c26a7a09fe021766170900eb2dfe5efd1194965aa99e8b0cb`.

STATUS: DONE_WITH_CONCERNS — G1 candidate complete and frozen; independent review pending.
