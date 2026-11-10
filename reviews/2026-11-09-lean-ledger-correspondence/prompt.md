# Independent correspondence review: Lean statement ledger vs manuscript

You are an independent, skeptical reviewer (mathematical rigor). You have NO tools: everything you need is inline below. Do not assume anything not in these files.

## Object under review
`docs/statement-ledger.md` of a Lean 4 companion (commit 38d16163ab8979dadb63766e41e59e9a84339d68). For each of 88 Lean declarations it claims (i) what the Lean statement says, (ii) which manuscript label it supports ("Paper label", or "no direct label"), and (iii) which inputs stay outside Lean. The manuscript is the LaTeX source at revision cf979d698a6ee7769e8c1316f43bc69948fa224b (main file plus every \input module, all included below). Lean sources and claims.yaml at the same Lean commit are included. The Lean code itself compiles with no sorry and standard axioms only; proof correctness is NOT in question. Correspondence is.

## What to check, for EVERY ledger row (all 88)
1. FIDELITY: Does the ledger's "What it states" match the Lean type exactly (hypotheses, quantifiers, strict vs non-strict, parameter ranges, constants)? Also check the claims.yaml summary for the same declaration.
2. LABEL MAPPING: If a label is given: does that labeled statement (or its proof) actually use this exact fact, with compatible hypotheses, parameter ranges and constants? Quote the TeX line(s). Is the Lean fact what the paper needs, or weaker/stronger/different?
3. NO DIRECT LABEL rows: search the TeX for the computation (formulas, constants, polynomials, parameter names). If it IS used under some label, report the label and quote. If genuinely absent, confirm.
4. OUTSIDE INPUTS: Are the inputs the ledger lists as outside Lean really the hypotheses of the Lean statement, and is any hypothesis an unacknowledged substitute for something the paper proves differently?
5. OVERCLAIM: any sentence in the ledger (intro, module paragraphs, "Not in Lean" list) that overstates what Lean checks or misdescribes the manuscript.
Pay special attention to these mappings the author flagged as uncertain: InteractionDriver.box_scale/box_margin (Lean uses 2/p; P:tube-actual-law/P:radius-mean-anchor appear to use d/Q); JointTilt.tilt_exponent and the two wrong_*_error identities vs P:raw-block-gaussian-law; MovingCone.terminal_margin vs L:raw-block-indexed-cone; RawVariational.dilation_factors as the d=1 case of L:variational-control-dilation; InteractionDriver midpoint choice vs the interval in the paper.

## Output format (exactly)
Section A: one line per ledger row, all 88, in ledger order:
`ROW | <full declaration> | FIDELITY: OK/ISSUE | MAPPING: OK/WRONG/WEAK/ABSENT-CONFIRMED/LABEL-FOUND:<label> | note`
Section B: numbered findings, each with: ID (F1, F2, ...), severity (CRITICAL = wrong mapping or misstatement that a reader citing the row would be misled by; MAJOR = material imprecision; MINOR = wording), the declaration(s), exact quotes from Lean and TeX with file names, the problem, and the precise fix to the ledger text.
Section C: overall verdict: PASS / PASS_WITH_CONCERNS / FAIL, counts by severity, and your confidence (LOW/MEDIUM/HIGH) with the reason. If you could not complete all 88 rows, say exactly which were skipped and why; do not claim completeness you did not achieve.

===== BEGIN LEDGER FILE: docs/statement-ledger.md =====
# Statement ledger

This ledger maps labels of the manuscript on the second moment of the
Stratonovich hyperbolic Anderson model with Gaussian noise fractional in time
to the Lean declarations in this package. Labels refer to the manuscript
revision cf979d6 and are written exactly as in its LaTeX source
(for example `P:clock-copy-obstruction`).

## Scope

- The package checks finite, algebraic and scalar steps only: exact
  identities, polynomial and rational certificates, real-power bookkeeping,
  parameter ranges, and a few finite-dimensional inner-product and
  finite-word facts.
- The SPDE itself, stochastic integrals, Gaussian measures, Fourier and
  spectral analysis, operator theory and all limits in time or in a
  regularization are outside Lean. Where a Lean statement needs an analytic
  fact about the model, that fact enters as an explicit hypothesis of the
  theorem (a "supplied hypothesis" below). Lean checks the deduction from
  those hypotheses, not the hypotheses themselves.
- A successful `lake build` is not a verification receipt for the
  manuscript. It shows that the stated Lean theorems are proved from their
  hypotheses; whether a statement matches the manuscript step it is listed
  against is a separate, human judgment recorded in this ledger.
- Three further modules developed alongside these (normalized Gaussian
  coordinates, vector Gaussian projection, and colored vector words) are
  withheld from this package because they depend on a library that is not
  yet public.
- "no direct label" means the declaration checks a computation from the
  development of the manuscript that does not appear as, or inside, a
  labeled statement of the revision cited above. Such rows make no claim
  about the manuscript.

All declarations live in the namespace `StratonovichHAMAudit.<Module>`; the
file is `StratonovichHAMAudit/<Module>.lean`. The four `PositiveGram`
declarations have status `internal` in `claims.yaml`; all others are
`reusable`.

## Index by label

| Paper label | Lean declarations |
|---|---|
| `C:intrinsic-spatial-bracket` | `RawValueCeiling.strict_log_gap` |
| `E:driver-parameters` | `InteractionDriver.temporal_range` |
| `L:driver-holder-limit` | `InteractionDriver.holder_parameters`, `InteractionDriver.dyadic_ratio` |
| `L:driver-interval-limit` | `InteractionDriver.variance_norm` |
| `L:exact-canonical-scaling` | `DirectEvent.kappa_gt_one`, `DirectEvent.physical_scale`, `DirectEvent.noise_scale`, `DirectEvent.vertex_scale` |
| `L:finite-word-cutoff` | `HermiteWord.raw_support`, `HermiteWord.cut_eq_raw` |
| `L:gaussian-scalar-powers` | `FiniteYoung.weighted_natural_powers` |
| `L:gram-scalar-algebra` | `PositiveGram.scalar_sqrt_dual`, `PositiveGram.gram_norm_square` |
| `L:raw-block-indexed-cone` | `MovingCone.residual_budget`, `MovingCone.cone_conversion`, `MovingCone.terminal_margin` |
| `L:raw-block-inputs` | `JointTilt.shifted_amplitude` |
| `L:raw-block-restart` | `ActualEvent.finite_error_accumulation` |
| `L:tube-rayleigh-tail` | `GaussianTail.cutoff_density_split` |
| `L:variational-control-dilation` | `RawVariational.dilation_factors` |
| `L:white-cdf-square` | `WhiteCDF.cdf_square_bound` |
| `P:clock-copy-obstruction` | `ClockFilter.resolvent_partial_fraction`, `ClockFilter.clock_filter_bounds`, `ClockFilter.strict_filter_integral` |
| `P:gram-entrywise-comparison` | `PositiveGram.half_weighted_entrywise_mono` |
| `P:gram-positive-optimizer` | `PositiveGram.active_upper_bound` |
| `P:raw-block-gaussian-law` | `JointTilt.tilt_exponent`, `JointTilt.wrong_sign_error`, `JointTilt.wrong_cost_error` |
| `P:raw-block-original-lower` | `ActualEvent.moderate_penalty` |
| `P:variational-positive-scores` | `RawVariational.label_score`, `RawVariational.positive_score`, `RawVariational.strict_label_factor` |
| `P:white-spatial-energy` | `WhiteCDF.energy_upper` |
| no direct label | all declarations of `AllAlphaMoment`, `DampedLower`, `DimensionalMatrix`, `GlobalOmega`, `LocalFlow`, `MiddleCross`, `OccupationForm`, `PhaseResponse`, `ProjectionResidual`, `TerminalCross`; `DirectEvent.gauge_inverse`, `DirectEvent.gauge_drift`, `DirectEvent.monodromy`; `InteractionDriver.gaussian_prefactor`, `InteractionDriver.gaussian_exponent`, `InteractionDriver.box_margin`, `InteractionDriver.box_scale`; `RawValueCeiling.exact_gap` |

Totals: 88 declarations (82 theorems, 6 definitions); 35 are listed against
a manuscript label and 53 have no direct label.

## ActualEvent

Checks two scalar steps in the lower bound obtained from restarted time
blocks (Section `S:actual-raw-block-lower`). The first is the elementary
error-accumulation estimate for differences of ordered products, used in
the proof of `L:raw-block-restart`; the second is the normalization of the
linear Gaussian penalty in the proof of `P:raw-block-original-lower`.

| Paper label | Lean declaration | What it states | Inputs left outside Lean |
|---|---|---|---|
| `L:raw-block-restart` | `StratonovichHAMAudit.ActualEvent.finite_error_accumulation` | If `1 <= C`, `0 <= e`, `d 0 <= 0` and `d (n+1) <= C d n + C^n e` for all `n`, then `d n <= n C^n e`. | The recurrence itself (operator-norm submultiplicativity for the product factors), extension of finite factor lists by identities, moments of `C` and of the error. |
| `P:raw-block-original-lower` | `StratonovichHAMAudit.ActualEvent.moderate_penalty` | For `delta > 0`, `delta (delta^(-1/4) / sqrt delta) = delta^(1/4)`. | The Gaussian change of law, the event on which the penalty bound holds, and the limit `delta -> 0`. |

## AllAlphaMoment

Checks a scalar lower bound for a second moment from a mean identity and a
quadratic bound, together with an exact rational gap. These belong to a
damped lower-endpoint comparison from the development of the manuscript
and are not stated in the revision cited above.

| Paper label | Lean declaration | What it states | Inputs left outside Lean |
|---|---|---|---|
| no direct label | `StratonovichHAMAudit.AllAlphaMoment.moment_lower` | If `a, D > 0`, `x + y = a` and `x^2 <= D y / 2`, then `2 a^2 / (D + 4a) <= y`. | Both relations are supplied hypotheses (normalization of a positive density, integration by parts, Cauchy-Schwarz for its moments). |
| no direct label | `StratonovichHAMAudit.AllAlphaMoment.rational_gap` | For `a, D > 0`, an exact difference of two rational expressions equals `a^2 / (2 (D+4a)(D+2a)) > 0`. | Any derivative, Gamma-function or integral representation of the compared quantities. |

## ClockFilter

Checks the scalar core of the obstruction to copying the cross-pair time
transform by analytic clocks (Section `S:two-clock-screen`): the partial
fraction identity for the resolvent product, the bound
`0 < 2 theta / (2 theta + ell) < 1`, and the resulting strict integral
inequality `J < K` in `P:clock-copy-obstruction`.

| Paper label | Lean declaration | What it states | Inputs left outside Lean |
|---|---|---|---|
| `P:clock-copy-obstruction` | `StratonovichHAMAudit.ClockFilter.resolvent_partial_fraction` | For `theta, ell > 0` and real `r`, the resolvent product equals the divided difference of `1/(theta^2 + r^2)` and `1/((theta+ell)^2 + r^2)` over `2 theta ell`. | Evaluation of the time integrals, spectral integration and the smoothing limit. |
| `P:clock-copy-obstruction` | `StratonovichHAMAudit.ClockFilter.clock_filter_bounds` | For `theta, ell > 0`, `0 < 2 theta / (2 theta + ell) < 1`. | None beyond the parameter signs. |
| `P:clock-copy-obstruction` | `StratonovichHAMAudit.ClockFilter.strict_filter_integral` | For a nonzero measure carried by `ell > 0` and an integrable a.e. positive `w`, the filtered integral of `w` is finite and strictly smaller than the integral of `w`. | Integrability and a.e. positivity of the weight `w_theta` (supplied hypotheses), and the identification of the two integrals with `J` and `K`. |

## DampedLower

Checks exact numerical inequalities involving `pi^3` that certify a strict
gain at one parameter point of a damped lower-endpoint comparison from the
development of the manuscript. Not stated in the revision cited above.

| Paper label | Lean declaration | What it states | Inputs left outside Lean |
|---|---|---|---|
| no direct label | `StratonovichHAMAudit.DampedLower.exact_margin` | `9 * 2^28 < 157^3 * 5^4` in the naturals. | None. |
| no direct label | `StratonovichHAMAudit.DampedLower.pi_cube_certificate` | `9 * 2^25 / 5^10 < pi^3`. | None (uses Mathlib's `3.14 < pi`). |
| no direct label | `StratonovichHAMAudit.DampedLower.rational_pi_gain` | `157^3 * 5^4 / (9 * 2^28) < pi^3 * 5^10 / (9 * 2^25)`. | The Gamma, Beta and energy computations that produce these numbers. |

## DimensionalMatrix

Defines the backward, coupling and forward 2x2 phase matrices of a single
interaction and computes their product with all four entries retained. This
belongs to a full-phase matrix computation from the development of the
manuscript; not stated in the revision cited above.

| Paper label | Lean declaration | What it states | Inputs left outside Lean |
|---|---|---|---|
| no direct label | `StratonovichHAMAudit.DimensionalMatrix.backward` | Definition: `[[cp, -sp/p], [p sp, cp]]`. | The interpretation of `cp, sp` as cosine and sine of a phase, and the continuous extension at zero frequency. |
| no direct label | `StratonovichHAMAudit.DimensionalMatrix.coupling` | Definition: `[[0, 0], [H, 0]]`. | The meaning of `H` as a covariance coefficient. |
| no direct label | `StratonovichHAMAudit.DimensionalMatrix.forward` | Definition: `[[cq, sq/q], [-q sq, cq]]`. | As for `backward`. |
| no direct label | `StratonovichHAMAudit.DimensionalMatrix.full_interaction` | The product `backward * coupling * forward` equals an explicit matrix, for all real parameters (field division). | Fourier representation and covariance integrals. |

## DirectEvent

The first four declarations check the exponent arithmetic of the exact
scaling `delta = T^(-kappa)`, `r_T = T delta` in `L:exact-canonical-scaling`,
including `kappa > 1` (also used in Section `S:original-point-transfer`).
The last three are 2x2 matrix identities for a scalar calibration from the
development of the manuscript; they are not stated in the revision cited
above.

| Paper label | Lean declaration | What it states | Inputs left outside Lean |
|---|---|---|---|
| `L:exact-canonical-scaling` | `StratonovichHAMAudit.DirectEvent.kappa_gt_one` | If `a < 1` and `alpha < 3`, then `(4 - alpha - a)/(3 - alpha) > 1`. | None. |
| `L:exact-canonical-scaling` | `StratonovichHAMAudit.DirectEvent.physical_scale` | For `T > 0`, `T * T^(-kappa) = T^((a-1)/(3-alpha))`. | None. |
| `L:exact-canonical-scaling` | `StratonovichHAMAudit.DirectEvent.noise_scale` | For `T > 0`, `T^(-a/2) r_T^(2 - alpha/2) = sqrt delta`. | Scaling of the Gaussian noise and its covariance; equality in law of the rescaled solution. |
| `L:exact-canonical-scaling` | `StratonovichHAMAudit.DirectEvent.vertex_scale` | For `T > 0`, `T^(1 - a/2) r_T^(1 - alpha/2) = delta^(-1/2)`. | Scaling of the Green measure; extension to the full series and its second moment. |
| no direct label | `StratonovichHAMAudit.DirectEvent.gauge_inverse` | `gauge(-w) * gauge(w) = 1` for `gauge(w) = [[1,0],[w,1]]`. | None. |
| no direct label | `StratonovichHAMAudit.DirectEvent.gauge_drift` | `gauge(-w) * [[0,1],[1,0]] * gauge(w) = [[w,1],[1 - w^2, -w]]`. | The differential equation and its growth analysis. |
| no direct label | `StratonovichHAMAudit.DirectEvent.monodromy` | Product, determinant `a^2 - 2b^2` and trace `2(a+b)` of two explicit pulse matrices. | Floquet analysis of the periodic calibration. |

## FiniteYoung

Checks the integer-power weighted arithmetic-geometric mean inequality
`E:gaussian-integer-power` stated in `L:gaussian-scalar-powers`.

| Paper label | Lean declaration | What it states | Inputs left outside Lean |
|---|---|---|---|
| `L:gaussian-scalar-powers` | `StratonovichHAMAudit.FiniteYoung.weighted_natural_powers` | For naturals `0 < L`, `q <= L` and reals `x, y`, `|x|^q |y|^(L-q) <= (q/L)|x|^L + ((L-q)/L)|y|^L`. | The trace and Gaussian-moment estimates in which it is applied. |

## GaussianTail

Checks the scalar exponent split in the proof of the Rayleigh tail budget
`L:tube-rayleigh-tail`.

| Paper label | Lean declaration | What it states | Inputs left outside Lean |
|---|---|---|---|
| `L:tube-rayleigh-tail` | `StratonovichHAMAudit.GaussianTail.cutoff_density_split` | If `0 < M <= x`, `C >= 0`, `1 < nu < 2` and `4C <= M^(2-nu)`, then `C x^nu - x^2/2 <= -M^2/8 - x^2/8`. | The Rayleigh integral and the bound `G(r) <= A_0 + C r^nu` on the integrand. |

## GlobalOmega

Defines an explicit degree-15 polynomial, a denominator and a rational
envelope, and proves the envelope is below one on `(0, 1/2]` by two
Bernstein-form certificates. This belongs to a one-dimensional damped
lower-endpoint comparison from the development of the manuscript; not
stated in the revision cited above.

| Paper label | Lean declaration | What it states | Inputs left outside Lean |
|---|---|---|---|
| no direct label | `StratonovichHAMAudit.GlobalOmega.envelopePolynomial` | Definition: explicit integer-coefficient polynomial of degree 15. | Its derivation from Gamma and Beta integrals. |
| no direct label | `StratonovichHAMAudit.GlobalOmega.envelopeDenom` | Definition: `750 (3-x)(2-x)(1-x)(5-2x)(3-2x)(5-3x)(3-4x-2x^2)`. | As above. |
| no direct label | `StratonovichHAMAudit.GlobalOmega.envelopeRational` | Definition: the explicit rational envelope. | Its identification with the analytic ratio. |
| no direct label | `StratonovichHAMAudit.GlobalOmega.left_certificate` | For `0 <= t <= 1`, `1 <= 4^15 Q(t/4)`. | None. |
| no direct label | `StratonovichHAMAudit.GlobalOmega.right_certificate` | For `0 <= t <= 1`, `1 <= 4^15 Q((1+t)/4)`. | None. |
| no direct label | `StratonovichHAMAudit.GlobalOmega.polynomial_pos` | `Q(x) > 0` for `0 <= x <= 1/2`. | None. |
| no direct label | `StratonovichHAMAudit.GlobalOmega.rational_lt_one` | `V(x) < 1` for `0 < x <= 1/2`. | Integral and energy computations defining the compared constants. |

## HermiteWord

Checks the combinatorial core of `L:finite-word-cutoff` (exact cutoffs for
finite Gaussian words), which is applied in `P:static-phase-all-orders` and
`L:fixed-split`: if each step raises a degree bound by one in its color and
the projection fixes every vector within the cutoff, inserting the
projection around each step does not change the word. The statements are
abstract (arbitrary types and maps). The companion file
`HermiteWordConsumer.lean` instantiates them with the scalar Hermite
recurrence `x He_n = He_(n+1) + n He_(n-1)` as private worked examples; it
adds no public declarations.

| Paper label | Lean declaration | What it states | Inputs left outside Lean |
|---|---|---|---|
| `L:finite-word-cutoff` | `StratonovichHAMAudit.HermiteWord.raw_support` | Under degree-raising and preservation hypotheses on `J` and `F`, the uncut word output satisfies the degree bound given by its color counts. | The Hermite/Fock realization of multiplication by Gaussian coordinates, which must supply the degree-raising hypothesis. |
| `L:finite-word-cutoff` | `StratonovichHAMAudit.HermiteWord.cut_eq_raw` | If moreover `P` fixes vectors within the cutoff `N` and the color counts of the word are at most `N`, then the cut and uncut words agree. | That the Hermite-degree projection fixes such vectors; Bochner integrals of words. |

## InteractionDriver

Checks parameter ranges, exponent bookkeeping and margins used in building
the operator-valued driver (Section `S:actual-operator-driver`). The ranges
and the Holder margin correspond to `E:driver-parameters`,
`L:driver-interval-limit` and `L:driver-holder-limit`; the Lean statements
make one explicit choice (the midpoint between `theta` and `H`) of the
exponent the manuscript only requires to lie in an interval. The Gaussian
mixture and box statements belong to a preliminary derivation that is not
stated in the revision cited above.

| Paper label | Lean declaration | What it states | Inputs left outside Lean |
|---|---|---|---|
| `E:driver-parameters` | `StratonovichHAMAudit.InteractionDriver.temporal_range` | For `0 < a < 1`, `1/2 < 1 - a/2 < 1`. | None. |
| `L:driver-interval-limit` | `StratonovichHAMAudit.InteractionDriver.variance_norm` | For `C >= 0`, `h > 0`, `L >= 0`, `sqrt(C h^(2-a) L^2) = sqrt(C) h^(1-a/2) L`. | The variance budget `E:driver-short-variance-budget` and the Schatten estimate it feeds. |
| `L:driver-holder-limit` | `StratonovichHAMAudit.InteractionDriver.holder_parameters` | For `1/2 < theta < H < 1` and `p > 2/(H - theta)`, the midpoint `m` satisfies `theta < m < H`, `m < 1`, `H - m - 1/p > 0`, `p > 2`. | Gaussian moment bounds for increments. |
| `L:driver-holder-limit` | `StratonovichHAMAudit.InteractionDriver.dyadic_ratio` | If `H - m - 1/p > 0` then `0 < 2^(-(H - m - 1/p)) < 1`. | The dyadic chaining argument and the Holder interpolation. |
| no direct label | `StratonovichHAMAudit.InteractionDriver.gaussian_prefactor` | For `P, u, v > 0`, an explicit product of square roots equals `1/(uv)`. | Spatial convolution of Gaussians; in the application `P = pi`. |
| no direct label | `StratonovichHAMAudit.InteractionDriver.gaussian_exponent` | For `u, v > 0`, `z^2/(4 uv/(u+v)) = z^2/(4u) + z^2/(4v)`. | As above. |
| no direct label | `StratonovichHAMAudit.InteractionDriver.box_margin` | If `a < 1`, `p > 0` and `p > 4/(1-a)`, then `(1-a)/2 - 2/p > 0`. | Maximal inequalities over boxes. |
| no direct label | `StratonovichHAMAudit.InteractionDriver.box_scale` | For `delta > 0`, `delta^((1-a)/2) (delta^(-2))^(1/p) = delta^((1-a)/2 - 2/p)`. | As above. |

## JointTilt

Checks the exponent bookkeeping of the Gaussian change of law in
`P:raw-block-gaussian-law` (completing the square), two identities showing
what a sign error or a doubled cost would leave behind, and the amplitude
identity `g_delta delta^(a/2) = sqrt delta` from the proof of
`L:raw-block-inputs`.

| Paper label | Lean declaration | What it states | Inputs left outside Lean |
|---|---|---|---|
| `P:raw-block-gaussian-law` | `StratonovichHAMAudit.JointTilt.tilt_exponent` | `-s^2 v/2 + r s c + (r^2 w - 2 r s c + s^2 v)/2 = r^2 w/2`. | The Gaussian densities, equivalence of measures and measurability on the path space. |
| `P:raw-block-gaussian-law` | `StratonovichHAMAudit.JointTilt.wrong_sign_error` | With the cross-term sign reversed, the exponent is off by `2 r s c`. | As above. |
| `P:raw-block-gaussian-law` | `StratonovichHAMAudit.JointTilt.wrong_cost_error` | With cost `s^2 v` in place of `s^2 v/2`, the exponent is off by `-s^2 v/2`. | As above. |
| `L:raw-block-inputs` | `StratonovichHAMAudit.JointTilt.shifted_amplitude` | For `delta > 0`, `delta^((1-a)/2) delta^(a/2) / sqrt delta = 1`. | The rescaled noise and its mean shift. |

## LocalFlow

Checks parameter ranges and weighted Schur factors for physical masks and a
local causal evolution, together with two elementary obstructions for a
source Sobolev index. These belong to a working derivation from the
development of the manuscript; not stated in the revision cited above.

| Paper label | Lean declaration | What it states | Inputs left outside Lean |
|---|---|---|---|
| no direct label | `StratonovichHAMAudit.LocalFlow.noise_order` | For `0 < alpha <= 1`, `0 <= (1-alpha)/2 < 1/2` and `alpha - 1 = -2 (1-alpha)/2`. | Spatial regularity of the noise. |
| no direct label | `StratonovichHAMAudit.LocalFlow.schur_row` | For `q, k > 0`, `(q^(-b) k^b) k^(-b) = q^(-b)`. | The Schur test and multiplier integrals. |
| no direct label | `StratonovichHAMAudit.LocalFlow.schur_column` | For `q > 0`, `(q^(-b) k^b) q^(-b) = k^b q^(-2b)`. | As above. |
| no direct label | `StratonovichHAMAudit.LocalFlow.schur_rescale` | For `k, R > 0`, `(k/R)^(2b) R^(2b) = k^(2b)`. | As above. |
| no direct label | `StratonovichHAMAudit.LocalFlow.source_overlap` | For `alpha < 1`, `sigma = -(1+alpha)/4` satisfies `-1/2 < sigma` and `2 sigma + alpha < 0`. | The Hilbert-Schmidt criterion for the source. |
| no direct label | `StratonovichHAMAudit.LocalFlow.source_white_obstruction` | If `-s < sigma` and `s - 1 < sigma`, then not `sigma < -1/2`. | As above. |
| no direct label | `StratonovichHAMAudit.LocalFlow.source_tail_obstruction` | If `-s < sigma`, `s - 1 < sigma` and `2 sigma + alpha < 0`, then `alpha < 1`. | As above. |

## MiddleCross

Checks, by an explicit rational parametrization and a positive polynomial
certificate, a strict comparison between an explicit rational value and an
upper expression evaluated at square roots. This belongs to a white-noise
comparison of four-vertex diagrams from the development of the manuscript;
not stated in the revision cited above.

| Paper label | Lean declaration | What it states | Inputs left outside Lean |
|---|---|---|---|
| no direct label | `StratonovichHAMAudit.MiddleCross.certificate_pos` | The explicit certificate is positive for `x >= 0`, `y > 0`. | None. |
| no direct label | `StratonovichHAMAudit.MiddleCross.parameter_identity` | For `z, t > 0`, the parametrized numerator times `32768 t^7 z^9` equals the certificate at `(z-2, t-1)`. | None. |
| no direct label | `StratonovichHAMAudit.MiddleCross.parameter_numerator_pos` | The parametrized numerator is positive for `z >= 2`, `t > 1`. | None. |
| no direct label | `StratonovichHAMAudit.MiddleCross.difference_identity` | For `b, c >= 1`, `d, e > 0`, `actual - upper = numerator / denominator`. | The diagram integrals that the rational functions represent. |
| no direct label | `StratonovichHAMAudit.MiddleCross.resolvent_difference` | For `b, c >= 1`, `d, e > 0`, an exact divided-difference identity for the resolvent expression. | As above. |
| no direct label | `StratonovichHAMAudit.MiddleCross.root_numerator_pos` | For `b >= 1`, `c > 1`, the numerator at `d = sqrt(b^2+c^2-1)`, `e = sqrt(b^2+1)` is positive. | None. |
| no direct label | `StratonovichHAMAudit.MiddleCross.middle_bound` | For `b >= 1`, `c > 1`, `upper < actual` at those square roots. | The reduction of the diagram comparison to this scalar inequality. |

## MovingCone

Checks the residual, cone-conversion and terminal margins in the proof of
`L:raw-block-indexed-cone`, where a cone around a slowly moving dominant
direction is shown to be preserved block by block.

| Paper label | Lean declaration | What it states | Inputs left outside Lean |
|---|---|---|---|
| `L:raw-block-indexed-cone` | `StratonovichHAMAudit.MovingCone.residual_budget` | If `0 <= theta`, `q <= 1/8`, `0 <= d <= theta`, `e <= theta/4`, then `q (theta + d) + e <= theta/2`. | Spectral gap of the block operators, perturbation bounds and continuity of the projections. |
| `L:raw-block-indexed-cone` | `StratonovichHAMAudit.MovingCone.cone_conversion` | If `0 <= theta`, `a > 0`, `rho < 1/2`, `(1-rho) a <= x`, `y <= theta a/2`, then `x > 0` and `y <= theta x`. | As above. |
| `L:raw-block-indexed-cone` | `StratonovichHAMAudit.MovingCone.terminal_margin` | If `j > 0`, `16 K theta <= j`, `e <= j/8`, `3j/4 - 2K theta - e <= y`, then `j/2 <= y` and `y > 0`. | The terminal observable bounds. |

## OccupationForm

Checks two scalar form inequalities (a potential term absorbed by a
gradient term, and the resulting shifted coercivity) from an occupation
control approximation in the development of the manuscript. Not stated in
the revision cited above.

| Paper label | Lean declaration | What it states | Inputs left outside Lean |
|---|---|---|---|
| no direct label | `StratonovichHAMAudit.OccupationForm.potential_budget` | For `eps > 0`, `A D N + A N^2 <= eps D^2 + (A + A^2/(4 eps)) N^2`. | The identification of `D`, `N` with gradient and `L^2` norms, and the potential bound. |
| no direct label | `StratonovichHAMAudit.OccupationForm.shifted_coercivity` | If `P <= D^2/2 + C N^2`, then `(D^2 + N^2)/2 <= D^2 - P + (C+1) N^2`. | As above. |

## PhaseResponse

Checks the choice of a phase index and its strict margins, two
trigonometric identities, and a two-sided frequency window, for a first
Gaussian response computed in a physical phase norm in the development of
the manuscript. Not stated in the revision cited above.

| Paper label | Lean declaration | What it states | Inputs left outside Lean |
|---|---|---|---|
| no direct label | `StratonovichHAMAudit.PhaseResponse.rough_phase_choice` | For `0 < alpha + a < 2`, `s = 1 - (alpha+a)/4` satisfies `1/2 < s < 1` and three strict margins. | Spectral integrability of the response. |
| no direct label | `StratonovichHAMAudit.PhaseResponse.balanced_phase` | For `alpha + a < 2`, the margins hold at `s = 1/2`. | As above. |
| no direct label | `StratonovichHAMAudit.PhaseResponse.energy_boundary` | `2 + alpha + a < 3` iff `alpha + a < 1`. | None. |
| no direct label | `StratonovichHAMAudit.PhaseResponse.four_component_gram` | A sum of four products of sines and cosines equals `cos(r1-r2) cos(k1-k2)`. | The temporal covariance integrals. |
| no direct label | `StratonovichHAMAudit.PhaseResponse.two_frequency_average` | `cos x cos y = (cos(x-y) + cos(x+y))/2`. | None. |
| no direct label | `StratonovichHAMAudit.PhaseResponse.frequency_window` | If `A, t, r > 0`, `B >= 0`, `2B/(At) <= r` and `|J - A t r^(a-1)| <= B r^(a-2)`, then `(At/2) r^(a-1) <= J <= (3At/2) r^(a-1)`. | The error bound on `J` (supplied hypothesis), coming from an asymptotic expansion of the response. |

## PositiveGram

Checks the finite-dimensional deductions of the positive Gram optimization
(Section `S:finite-positive-gram`): the scalar dual inequality and the Gram
expansion of `L:gram-scalar-algebra`, the conditional upper bound used in
the proof of `P:gram-positive-optimizer`, and the half-quadratic entrywise
monotonicity behind `P:gram-entrywise-comparison`. Remark `R:gram-controls`
states which parts of these arguments remain analytic. These four
declarations are marked `internal`.

| Paper label | Lean declaration | What it states | Inputs left outside Lean |
|---|---|---|---|
| `L:gram-scalar-algebra` | `StratonovichHAMAudit.PositiveGram.scalar_sqrt_dual` | For `w > 0`, `t >= 0`, `2 ell sqrt t <= ell^2/w + w t`. | None. |
| `L:gram-scalar-algebra` | `StratonovichHAMAudit.PositiveGram.gram_norm_square` | In a real inner product space, `||sum w_i k_i||^2 = sum_ij w_i <k_i,k_j> w_j`. | None. |
| `P:gram-positive-optimizer` | `StratonovichHAMAudit.PositiveGram.active_upper_bound` | For positive weights and active labels (`<Phi,k_i> - b_i >= 0`), the active score is bounded by the dual objective. | Dual coercivity, existence and uniqueness of the dual minimizer, attainment, and the maximum over active sets. |
| `P:gram-entrywise-comparison` | `StratonovichHAMAudit.PositiveGram.half_weighted_entrywise_mono` | If `C_ij <= D_ij` and `w_i >= 0`, the half quadratic form in `C` is at most that in `D`. | Gram realization (`L:gram-realization`) and the optimization over weights. |

## ProjectionResidual

Checks the numerical inequality behind a counterexample to discarding the
residual after a rank-one projection, at one explicit parameter choice.
This is a fixed-horizon obstruction from the development of the manuscript;
not stated in the revision cited above.

| Paper label | Lean declaration | What it states | Inputs left outside Lean |
|---|---|---|---|
| no direct label | `StratonovichHAMAudit.ProjectionResidual.projection_gap` | `20000/1932951 + 1/96 < 101/(3200 sqrt 2)`. | The computation of both coefficients from the model. |
| no direct label | `StratonovichHAMAudit.ProjectionResidual.tilted_gap` | If `p >= 101/(3200 sqrt 2)`, then `20000/1932951 + (q-1)p + 1/96 < q p`. | The Gaussian projection and its mean and limit inputs. |

## RawValueCeiling

Checks the strict logarithmic gap
`Delta = [q log q + (q-2a) log(q-2a)]/2 - (q-a) log(q-a) > 0` used in the
proof of `C:intrinsic-spatial-bracket`, and one exact integer instance of
such a gap.

| Paper label | Lean declaration | What it states | Inputs left outside Lean |
|---|---|---|---|
| no direct label | `StratonovichHAMAudit.RawValueCeiling.exact_gap` | `2 * 30^60 < 39^39 * 21^21` in the naturals. | None. |
| `C:intrinsic-spatial-bracket` | `StratonovichHAMAudit.RawValueCeiling.strict_log_gap` | For `a > 0` and `q - 2a > 0`, `Delta > 0`. | The occupation scalar map and energy identifications in which `Delta` appears. |

## RawVariational

Checks the real-power bookkeeping of the dilation of controls in
`L:variational-control-dilation` (the exponents in dimension one) and of
the score homogeneity `S_c = c^((4-alpha)/(3-alpha)) S_1` in
`P:variational-positive-scores`, together with positivity of one dilated
score and the strict inequality `2^m > 2`.

| Paper label | Lean declaration | What it states | Inputs left outside Lean |
|---|---|---|---|
| `L:variational-control-dilation` | `StratonovichHAMAudit.RawVariational.dilation_factors` | For `s > 0`, `s^(3-alpha) s^(alpha-1) = s^2` and `s^(3-alpha) s^2 / s = s^(4-alpha)`. | Homogeneity of the covariance measure and the Rayleigh quotient scaling. |
| `P:variational-positive-scores` | `StratonovichHAMAudit.RawVariational.label_score` | For `c > 0`, `alpha < 3`, `c (c^(1/k) I) - (c^(1/k))^(4-alpha) v/2 = c^((4-alpha)/k) (I - v/2)` with `k = 3 - alpha`. | The variational class, its bijection under dilation, and finiteness of the supremum. |
| `P:variational-positive-scores` | `StratonovichHAMAudit.RawVariational.positive_score` | For `I, v > 0`, `alpha < 3` and `r = (I/v)^(1/(3-alpha))`, `r I - r^(4-alpha) v/2 > 0`. | Positivity of `I` and `v` for an actual control. |
| `P:variational-positive-scores` | `StratonovichHAMAudit.RawVariational.strict_label_factor` | For `alpha < 3`, `2 < 2^((4-alpha)/(3-alpha))`. | None. |

## TerminalCross

Checks, by a positive polynomial certificate and convexity of the
exponential, a strict comparison between two explicit expressions in
`b >= 1`, `c > 1`. This belongs to a white-noise comparison of four-vertex
diagrams from the development of the manuscript; not stated in the revision
cited above.

| Paper label | Lean declaration | What it states | Inputs left outside Lean |
|---|---|---|---|
| no direct label | `StratonovichHAMAudit.TerminalCross.polynomial_identity` | The comparison polynomial equals the certificate at `(b-1, c-1)`. | None. |
| no direct label | `StratonovichHAMAudit.TerminalCross.polynomial_pos` | The comparison polynomial is positive for `b >= 1`, `c > 1`. | None. |
| no direct label | `StratonovichHAMAudit.TerminalCross.rate_le` | For `A > 0`, `s >= 1/2`, `A/(2(A+1)) <= s A/(A + 2s)`. | None. |
| no direct label | `StratonovichHAMAudit.TerminalCross.exponential_difference` | If `0 <= D < C` and `(C-D)k = C r - D R`, then `C e^(-rw) - D e^(-Rw) <= (C-D) e^(-kw)`. | None. |
| no direct label | `StratonovichHAMAudit.TerminalCross.terminal_bound` | For `b >= 1`, `c > 1`, an explicit square-root expression is strictly below an explicit rational expression. | The reduction of the diagram integrals to these expressions. |

## WhiteCDF

Checks the scalar deductions in the white-noise spatial evaluation
(Section `S:intrinsic-white-evaluation`): the bound `3A^2 <= b` that
follows from the CDF square identity of `L:white-cdf-square`, and the
energy bound `c A - b/2 <= c^2/6` in the proof of `P:white-spatial-energy`.

| Paper label | Lean declaration | What it states | Inputs left outside Lean |
|---|---|---|---|
| `L:white-cdf-square` | `StratonovichHAMAudit.WhiteCDF.cdf_square_bound` | If `0 <= b - 2zA + z^2/3` for all real `z`, then `3A^2 <= b`. | The CDF square identity itself (supplied hypothesis), with `A = int f^4`, `b = int (f')^2` for unit `f` in `H^1`. |
| `P:white-spatial-energy` | `StratonovichHAMAudit.WhiteCDF.energy_upper` | If `3A^2 <= b`, then `c A - b/2 <= c^2/6`. | The variational energy, its domain and attainment. |

## Not in Lean

The main analytic ingredients of the manuscript are not formalized here.
In particular:

- Existence of the canonical solution and its expansion, including
  self-pairings and fixed-order coefficients (`P:mild-construction`,
  `L:joint-fixed-order`), and the crude bound `T:crude`.
- The upper bound at the scale `t^kappa` (`T:full-upper`) and the Fock-space,
  Hermite and spectral estimates behind it (`L:fock-form`,
  `P:static-phase-all-orders`).
- Equality in law under the exact scaling (`L:exact-canonical-scaling`),
  beyond the exponent arithmetic listed above.
- Construction of the operator-valued driver and the Young-type evolution
  (`P:actual-operator-driver`).
- Gaussian changes of measure, Cameron-Martin means and tube estimates
  (`P:raw-block-gaussian-law`, `P:cameron-full-mean`, `P:tube-actual-law`).
- The variational lower bound and its constant (`T:intrinsic-second-moment`),
  the occupation ceiling (`T:intrinsic-occupation-ceiling`) and the
  white-noise evaluation (`T:white-moment-bounds`).
- Gamma and Beta identities (`L:equilibrium-gamma-beta`), Fourier analysis
  of the covariance, measure-theoretic constructions, and all limits in
  time and in regularization parameters.

===== END LEDGER FILE: docs/statement-ledger.md =====

===== BEGIN CLAIMS FILE: claims.yaml =====
schema: claims/1
package: stratonovich-ham-second-moment-lean
claims:
# ActualEvent
- id: stratonovich-ham-second-moment-lean/actual-event-finite-error-accumulation
  decl: StratonovichHAMAudit.ActualEvent.finite_error_accumulation
  kind: theorem
  summary: "For reals C, e and a real sequence d on the naturals, if 1 <= C, 0 <= e, d 0 <= 0 and d (n+1) <= C * d n + C^n * e for every n, then d n <= n * C^n * e for every natural n; the per-step recurrence is a supplied hypothesis."
  keywords: [error-accumulation, recurrence, products]
  file: StratonovichHAMAudit/ActualEvent.lean
  status: reusable
- id: stratonovich-ham-second-moment-lean/actual-event-moderate-penalty
  decl: StratonovichHAMAudit.ActualEvent.moderate_penalty
  kind: theorem
  summary: "For real delta > 0, delta * (delta^(-1/4) / sqrt(delta)) = delta^(1/4), with real powers and the real square root."
  keywords: [real-power, scaling]
  file: StratonovichHAMAudit/ActualEvent.lean
  status: reusable
# AllAlphaMoment
- id: stratonovich-ham-second-moment-lean/all-alpha-moment-moment-lower
  decl: StratonovichHAMAudit.AllAlphaMoment.moment_lower
  kind: theorem
  summary: "For reals a, D, x, y with a > 0, D > 0, x + y = a and x^2 <= D*y/2, one has 2*a^2/(D + 4*a) <= y; the mean relation x + y = a and the bound x^2 <= D*y/2 are supplied hypotheses."
  keywords: [moment-bound, scalar-inequality]
  file: StratonovichHAMAudit/AllAlphaMoment.lean
  status: reusable
- id: stratonovich-ham-second-moment-lean/all-alpha-moment-rational-gap
  decl: StratonovichHAMAudit.AllAlphaMoment.rational_gap
  kind: theorem
  summary: "For reals a > 0 and D > 0, a^2/(D*(D+4*a)) - a^2/(2*D*(D+2*a)) = a^2/(2*(D+4*a)*(D+2*a)), and this value is strictly positive."
  keywords: [rational-identity, positivity]
  file: StratonovichHAMAudit/AllAlphaMoment.lean
  status: reusable
# ClockFilter
- id: stratonovich-ham-second-moment-lean/clock-filter-resolvent-partial-fraction
  decl: StratonovichHAMAudit.ClockFilter.resolvent_partial_fraction
  kind: theorem
  summary: "For reals theta > 0, ell > 0 and any real r, (2*theta + ell) / (2*theta*(theta^2 + r^2)*((theta + ell)^2 + r^2)) = (1/(theta^2 + r^2) - 1/((theta + ell)^2 + r^2)) / (2*theta*ell)."
  keywords: [partial-fractions, resolvent]
  file: StratonovichHAMAudit/ClockFilter.lean
  status: reusable
- id: stratonovich-ham-second-moment-lean/clock-filter-clock-filter-bounds
  decl: StratonovichHAMAudit.ClockFilter.clock_filter_bounds
  kind: theorem
  summary: "For reals theta > 0 and ell > 0, 0 < 2*theta/(2*theta + ell) < 1."
  keywords: [filter-factor, scalar-inequality]
  file: StratonovichHAMAudit/ClockFilter.lean
  status: reusable
- id: stratonovich-ham-second-moment-lean/clock-filter-strict-filter-integral
  decl: StratonovichHAMAudit.ClockFilter.strict_filter_integral
  kind: theorem
  summary: "For theta > 0, a nonzero measure sigma with ell > 0 sigma-a.e., and w integrable with w > 0 sigma-a.e. (supplied hypotheses), ell -> 2*theta/(2*theta + ell) * w ell is integrable with integral strictly below the integral of w."
  keywords: [strict-integral-inequality, filter-factor, measure]
  file: StratonovichHAMAudit/ClockFilter.lean
  status: reusable
# DampedLower
- id: stratonovich-ham-second-moment-lean/damped-lower-exact-margin
  decl: StratonovichHAMAudit.DampedLower.exact_margin
  kind: theorem
  summary: "In the natural numbers, 9 * 2^28 < 157^3 * 5^4."
  keywords: [numerical-certificate, integer-inequality]
  file: StratonovichHAMAudit/DampedLower.lean
  status: reusable
- id: stratonovich-ham-second-moment-lean/damped-lower-pi-cube-certificate
  decl: StratonovichHAMAudit.DampedLower.pi_cube_certificate
  kind: theorem
  summary: "As real numbers, 9 * 2^25 / 5^10 < pi^3."
  keywords: [numerical-certificate, pi-bound]
  file: StratonovichHAMAudit/DampedLower.lean
  status: reusable
- id: stratonovich-ham-second-moment-lean/damped-lower-rational-pi-gain
  decl: StratonovichHAMAudit.DampedLower.rational_pi_gain
  kind: theorem
  summary: "As real numbers, 157^3 * 5^4 / (9 * 2^28) < pi^3 * 5^10 / (9 * 2^25)."
  keywords: [numerical-certificate, pi-bound]
  file: StratonovichHAMAudit/DampedLower.lean
  status: reusable
# DimensionalMatrix
- id: stratonovich-ham-second-moment-lean/dimensional-matrix-backward
  decl: StratonovichHAMAudit.DimensionalMatrix.backward
  kind: definition
  summary: "For reals cp, sp, p, the real 2x2 matrix [[cp, -sp/p], [p*sp, cp]], with Lean field division (no nonvanishing condition on p)."
  keywords: [matrix, phase-propagator]
  file: StratonovichHAMAudit/DimensionalMatrix.lean
  status: reusable
- id: stratonovich-ham-second-moment-lean/dimensional-matrix-coupling
  decl: StratonovichHAMAudit.DimensionalMatrix.coupling
  kind: definition
  summary: "For real H, the real 2x2 matrix [[0, 0], [H, 0]]."
  keywords: [matrix, coupling]
  file: StratonovichHAMAudit/DimensionalMatrix.lean
  status: reusable
- id: stratonovich-ham-second-moment-lean/dimensional-matrix-forward
  decl: StratonovichHAMAudit.DimensionalMatrix.forward
  kind: definition
  summary: "For reals cq, sq, q, the real 2x2 matrix [[cq, sq/q], [-q*sq, cq]], with Lean field division (no nonvanishing condition on q)."
  keywords: [matrix, phase-propagator]
  file: StratonovichHAMAudit/DimensionalMatrix.lean
  status: reusable
- id: stratonovich-ham-second-moment-lean/dimensional-matrix-full-interaction
  decl: StratonovichHAMAudit.DimensionalMatrix.full_interaction
  kind: theorem
  summary: "For all reals cp, sp, p, H, cq, sq, q, backward cp sp p * coupling H * forward cq sq q = [[-(sp/p)*H*cq, -(sp/p)*H*(sq/q)], [cp*H*cq, cp*H*(sq/q)]]."
  keywords: [matrix-product, phase-propagator]
  file: StratonovichHAMAudit/DimensionalMatrix.lean
  status: reusable
# DirectEvent
- id: stratonovich-ham-second-moment-lean/direct-event-kappa-gt-one
  decl: StratonovichHAMAudit.DirectEvent.kappa_gt_one
  kind: theorem
  summary: "For reals alpha, a with a < 1 and alpha < 3, kappa alpha a = (4 - alpha - a)/(3 - alpha) satisfies 1 < kappa alpha a."
  keywords: [growth-exponent, scaling]
  file: StratonovichHAMAudit/DirectEvent.lean
  status: reusable
- id: stratonovich-ham-second-moment-lean/direct-event-physical-scale
  decl: StratonovichHAMAudit.DirectEvent.physical_scale
  kind: theorem
  summary: "For T > 0 and alpha < 3, radius T alpha a = T * T^(-kappa alpha a) equals T^((a - 1)/(3 - alpha)), with real powers."
  keywords: [scaling, real-power]
  file: StratonovichHAMAudit/DirectEvent.lean
  status: reusable
- id: stratonovich-ham-second-moment-lean/direct-event-noise-scale
  decl: StratonovichHAMAudit.DirectEvent.noise_scale
  kind: theorem
  summary: "For T > 0 and alpha < 3, T^(-a/2) * (radius T alpha a)^(2 - alpha/2) = sqrt(delta T alpha a), where delta T alpha a = T^(-kappa alpha a) and radius = T * delta."
  keywords: [scaling, real-power, noise-amplitude]
  file: StratonovichHAMAudit/DirectEvent.lean
  status: reusable
- id: stratonovich-ham-second-moment-lean/direct-event-vertex-scale
  decl: StratonovichHAMAudit.DirectEvent.vertex_scale
  kind: theorem
  summary: "For T > 0 and alpha < 3, T^(1 - a/2) * (radius T alpha a)^(1 - alpha/2) = (delta T alpha a)^(-1/2), where delta = T^(-kappa alpha a) and radius = T * delta."
  keywords: [scaling, real-power, vertex-factor]
  file: StratonovichHAMAudit/DirectEvent.lean
  status: reusable
- id: stratonovich-ham-second-moment-lean/direct-event-gauge-inverse
  decl: StratonovichHAMAudit.DirectEvent.gauge_inverse
  kind: theorem
  summary: "For real w, gauge (-w) * gauge w = 1, where gauge w is the real 2x2 matrix [[1, 0], [w, 1]]."
  keywords: [matrix, gauge-transform]
  file: StratonovichHAMAudit/DirectEvent.lean
  status: reusable
- id: stratonovich-ham-second-moment-lean/direct-event-gauge-drift
  decl: StratonovichHAMAudit.DirectEvent.gauge_drift
  kind: theorem
  summary: "For real w, gauge (-w) * drift * gauge w = [[w, 1], [1 - w^2, -w]], where gauge w = [[1, 0], [w, 1]] and drift = [[0, 1], [1, 0]]."
  keywords: [matrix, gauge-transform, conjugation]
  file: StratonovichHAMAudit/DirectEvent.lean
  status: reusable
- id: stratonovich-ham-second-moment-lean/direct-event-monodromy
  decl: StratonovichHAMAudit.DirectEvent.monodromy
  kind: theorem
  summary: "For reals a, b, with pulseTwo a b = [[a, b], [2*b, a]] and pulseZero = [[1, 1], [0, 1]], the product pulseTwo a b * pulseZero equals [[a, a + b], [2*b, a + 2*b]], has determinant a^2 - 2*b^2 and has trace 2*(a + b)."
  keywords: [matrix, monodromy, determinant-trace]
  file: StratonovichHAMAudit/DirectEvent.lean
  status: reusable
# FiniteYoung
- id: stratonovich-ham-second-moment-lean/finite-young-weighted-natural-powers
  decl: StratonovichHAMAudit.FiniteYoung.weighted_natural_powers
  kind: theorem
  summary: "For naturals L, q with 0 < L and q <= L and reals x, y, |x|^q * |y|^(L - q) <= (q/L) * |x|^L + ((L - q)/L) * |y|^L, with natural-number powers and real-cast weights (weighted arithmetic-geometric mean)."
  keywords: [young-inequality, am-gm, integer-powers]
  file: StratonovichHAMAudit/FiniteYoung.lean
  status: reusable
# GaussianTail
- id: stratonovich-ham-second-moment-lean/gaussian-tail-cutoff-density-split
  decl: StratonovichHAMAudit.GaussianTail.cutoff_density_split
  kind: theorem
  summary: "For reals M, x, C, nu with M > 0, M <= x, C >= 0, 1 < nu < 2 and 4*C <= M^(2 - nu), one has C*x^nu - x^2/2 <= -M^2/8 - x^2/8, with real powers."
  keywords: [tail-bound, real-power, cutoff]
  file: StratonovichHAMAudit/GaussianTail.lean
  status: reusable
# GlobalOmega
- id: stratonovich-ham-second-moment-lean/global-omega-envelope-polynomial
  decl: StratonovichHAMAudit.GlobalOmega.envelopePolynomial
  kind: definition
  summary: "An explicit real polynomial of degree 15 in x with integer coefficients, from -237888*x^15 down to the constant term 9900, written out in full in the source."
  keywords: [polynomial, envelope]
  file: StratonovichHAMAudit/GlobalOmega.lean
  status: reusable
- id: stratonovich-ham-second-moment-lean/global-omega-envelope-denom
  decl: StratonovichHAMAudit.GlobalOmega.envelopeDenom
  kind: definition
  summary: "The real function x -> 750*(3 - x)*(2 - x)*(1 - x)*(5 - 2*x)*(3 - 2*x)*(5 - 3*x)*(3 - 4*x - 2*x^2)."
  keywords: [polynomial, denominator]
  file: StratonovichHAMAudit/GlobalOmega.lean
  status: reusable
- id: stratonovich-ham-second-moment-lean/global-omega-envelope-rational
  decl: StratonovichHAMAudit.GlobalOmega.envelopeRational
  kind: definition
  summary: "The explicit real rational function x -> 2*(1 - x^2 + x^4/2)*(1 - 4*x^2)/(1 - 3*x/5) * K(x) * (3 - 4*x)/(3 - 4*x - 2*x^2), where K(x) is the bracket of rational terms written in the source (it contains the constant 177/100)."
  keywords: [rational-function, envelope]
  file: StratonovichHAMAudit/GlobalOmega.lean
  status: reusable
- id: stratonovich-ham-second-moment-lean/global-omega-left-certificate
  decl: StratonovichHAMAudit.GlobalOmega.left_certificate
  kind: theorem
  summary: "For real t with 0 <= t <= 1, 1 <= 4^15 * envelopePolynomial (t/4), proved through an explicit Bernstein-form identity with positive coefficients."
  keywords: [bernstein-certificate, polynomial-bound]
  file: StratonovichHAMAudit/GlobalOmega.lean
  status: reusable
- id: stratonovich-ham-second-moment-lean/global-omega-right-certificate
  decl: StratonovichHAMAudit.GlobalOmega.right_certificate
  kind: theorem
  summary: "For real t with 0 <= t <= 1, 1 <= 4^15 * envelopePolynomial ((1 + t)/4), proved through an explicit Bernstein-form identity with positive coefficients."
  keywords: [bernstein-certificate, polynomial-bound]
  file: StratonovichHAMAudit/GlobalOmega.lean
  status: reusable
- id: stratonovich-ham-second-moment-lean/global-omega-polynomial-pos
  decl: StratonovichHAMAudit.GlobalOmega.polynomial_pos
  kind: theorem
  summary: "For real x with 0 <= x <= 1/2, envelopePolynomial x > 0."
  keywords: [polynomial-positivity, envelope]
  file: StratonovichHAMAudit/GlobalOmega.lean
  status: reusable
- id: stratonovich-ham-second-moment-lean/global-omega-rational-lt-one
  decl: StratonovichHAMAudit.GlobalOmega.rational_lt_one
  kind: theorem
  summary: "For real x with 0 < x <= 1/2, envelopeRational x < 1; the proof uses the identity envelopeDenom x * (1 - envelopeRational x) = x * envelopePolynomial x."
  keywords: [rational-bound, envelope]
  file: StratonovichHAMAudit/GlobalOmega.lean
  status: reusable
# HermiteWord
- id: stratonovich-ham-second-moment-lean/hermite-word-raw-support
  decl: StratonovichHAMAudit.HermiteWord.raw_support
  kind: theorem
  summary: "If Good holds for v0 at the zero count, each J i raises the i-th count of a Good vector and each F b preserves Good, then for every word w the vector raw J F v0 w is Good at the occurrence counts of w."
  keywords: [finite-word, degree-bound, induction]
  file: StratonovichHAMAudit/HermiteWord.lean
  status: reusable
- id: stratonovich-ham-second-moment-lean/hermite-word-cut-eq-raw
  decl: StratonovichHAMAudit.HermiteWord.cut_eq_raw
  kind: theorem
  summary: "Under the hypotheses of raw_support, if P fixes every vector Good at a count d <= N, then every word w with color counts at most N satisfies cut P J F v0 w = raw J F v0 w (inserting P around each J changes nothing)."
  keywords: [finite-word, cutoff, projection]
  file: StratonovichHAMAudit/HermiteWord.lean
  status: reusable
# InteractionDriver
- id: stratonovich-ham-second-moment-lean/interaction-driver-temporal-range
  decl: StratonovichHAMAudit.InteractionDriver.temporal_range
  kind: theorem
  summary: "For real a with 0 < a < 1, temporalH a = 1 - a/2 satisfies 1/2 < temporalH a < 1."
  keywords: [parameter-range, holder-exponent]
  file: StratonovichHAMAudit/InteractionDriver.lean
  status: reusable
- id: stratonovich-ham-second-moment-lean/interaction-driver-variance-norm
  decl: StratonovichHAMAudit.InteractionDriver.variance_norm
  kind: theorem
  summary: "For reals C >= 0, h > 0, L >= 0 and any real a, sqrt(C * h^(2 - a) * L^2) = sqrt(C) * h^(1 - a/2) * L, with real powers."
  keywords: [variance-normalization, real-power, square-root]
  file: StratonovichHAMAudit/InteractionDriver.lean
  status: reusable
- id: stratonovich-ham-second-moment-lean/interaction-driver-gaussian-prefactor
  decl: StratonovichHAMAudit.InteractionDriver.gaussian_prefactor
  kind: theorem
  summary: "For reals P > 0, u > 0, v > 0, (1/sqrt(P)) * (1/sqrt(u*v*(u + v))) * sqrt(P / mixC u v) = 1/(u*v), where mixC u v = u*v/(u + v)."
  keywords: [gaussian-mixture, prefactor, square-root]
  file: StratonovichHAMAudit/InteractionDriver.lean
  status: reusable
- id: stratonovich-ham-second-moment-lean/interaction-driver-gaussian-exponent
  decl: StratonovichHAMAudit.InteractionDriver.gaussian_exponent
  kind: theorem
  summary: "For reals u > 0, v > 0 and any real z, z^2/(4 * mixC u v) = z^2/(4*u) + z^2/(4*v), where mixC u v = u*v/(u + v)."
  keywords: [gaussian-mixture, exponent]
  file: StratonovichHAMAudit/InteractionDriver.lean
  status: reusable
- id: stratonovich-ham-second-moment-lean/interaction-driver-holder-parameters
  decl: StratonovichHAMAudit.InteractionDriver.holder_parameters
  kind: theorem
  summary: "For reals H, theta, p with 1/2 < theta < H < 1, 0 < p and 2/(H - theta) < p, the midpoint m = (H + theta)/2 satisfies theta < m, m < H, m < 1, 0 < H - m - 1/p and 2 < p."
  keywords: [holder-exponent, moment-margin, parameter-choice]
  file: StratonovichHAMAudit/InteractionDriver.lean
  status: reusable
- id: stratonovich-ham-second-moment-lean/interaction-driver-dyadic-ratio
  decl: StratonovichHAMAudit.InteractionDriver.dyadic_ratio
  kind: theorem
  summary: "For reals H, theta, p with 0 < H - (H + theta)/2 - 1/p, the factor 2^(-(H - (H + theta)/2 - 1/p)) lies strictly between 0 and 1."
  keywords: [dyadic-sum, geometric-ratio]
  file: StratonovichHAMAudit/InteractionDriver.lean
  status: reusable
- id: stratonovich-ham-second-moment-lean/interaction-driver-box-margin
  decl: StratonovichHAMAudit.InteractionDriver.box_margin
  kind: theorem
  summary: "For reals a, p with a < 1, 0 < p and 4/(1 - a) < p, one has 0 < (1 - a)/2 - 2/p."
  keywords: [moment-margin, parameter-choice]
  file: StratonovichHAMAudit/InteractionDriver.lean
  status: reusable
- id: stratonovich-ham-second-moment-lean/interaction-driver-box-scale
  decl: StratonovichHAMAudit.InteractionDriver.box_scale
  kind: theorem
  summary: "For real delta > 0 and any reals a, p, delta^((1 - a)/2) * (delta^(-2))^(1/p) = delta^((1 - a)/2 - 2/p), with real powers."
  keywords: [real-power, scaling]
  file: StratonovichHAMAudit/InteractionDriver.lean
  status: reusable
# JointTilt
- id: stratonovich-ham-second-moment-lean/joint-tilt-tilt-exponent
  decl: StratonovichHAMAudit.JointTilt.tilt_exponent
  kind: theorem
  summary: "For all reals r, s, c, v, w, -s^2*v/2 + r*s*c + (r^2*w - 2*r*s*c + s^2*v)/2 = r^2*w/2; this is a polynomial identity, not a statement about Gaussian integrals."
  keywords: [gaussian-tilt, exponent-identity]
  file: StratonovichHAMAudit/JointTilt.lean
  status: reusable
- id: stratonovich-ham-second-moment-lean/joint-tilt-wrong-sign-error
  decl: StratonovichHAMAudit.JointTilt.wrong_sign_error
  kind: theorem
  summary: "For all reals r, s, c, v, w, (-s^2*v/2 + r*s*c + (r^2*w + 2*r*s*c + s^2*v)/2) - r^2*w/2 = 2*r*s*c, so the exponent with the cross-term sign reversed leaves the residual 2*r*s*c."
  keywords: [gaussian-tilt, sign-check]
  file: StratonovichHAMAudit/JointTilt.lean
  status: reusable
- id: stratonovich-ham-second-moment-lean/joint-tilt-wrong-cost-error
  decl: StratonovichHAMAudit.JointTilt.wrong_cost_error
  kind: theorem
  summary: "For all reals r, s, c, v, w, (-s^2*v + r*s*c + (r^2*w - 2*r*s*c + s^2*v)/2) - r^2*w/2 = -s^2*v/2, so using the full cost s^2*v instead of s^2*v/2 leaves the residual -s^2*v/2."
  keywords: [gaussian-tilt, cost-check]
  file: StratonovichHAMAudit/JointTilt.lean
  status: reusable
- id: stratonovich-ham-second-moment-lean/joint-tilt-shifted-amplitude
  decl: StratonovichHAMAudit.JointTilt.shifted_amplitude
  kind: theorem
  summary: "For real delta > 0 and any real a, delta^((1 - a)/2) * delta^(a/2) / sqrt(delta) = 1, with real powers."
  keywords: [amplitude, real-power, scaling]
  file: StratonovichHAMAudit/JointTilt.lean
  status: reusable
# LocalFlow
- id: stratonovich-ham-second-moment-lean/local-flow-noise-order
  decl: StratonovichHAMAudit.LocalFlow.noise_order
  kind: theorem
  summary: "For real alpha with 0 < alpha <= 1, noiseOrder alpha = (1 - alpha)/2 satisfies 0 <= noiseOrder alpha < 1/2 and alpha - 1 = -2 * noiseOrder alpha."
  keywords: [regularity-order, parameter-range]
  file: StratonovichHAMAudit/LocalFlow.lean
  status: reusable
- id: stratonovich-ham-second-moment-lean/local-flow-schur-row
  decl: StratonovichHAMAudit.LocalFlow.schur_row
  kind: theorem
  summary: "For reals q > 0, k > 0 and any real b, (q^(-b) * k^b) * k^(-b) = q^(-b), with real powers."
  keywords: [schur-test, weight-factor, real-power]
  file: StratonovichHAMAudit/LocalFlow.lean
  status: reusable
- id: stratonovich-ham-second-moment-lean/local-flow-schur-column
  decl: StratonovichHAMAudit.LocalFlow.schur_column
  kind: theorem
  summary: "For real q > 0 and any reals k, b, (q^(-b) * k^b) * q^(-b) = k^b * q^(-2*b), with real powers."
  keywords: [schur-test, weight-factor, real-power]
  file: StratonovichHAMAudit/LocalFlow.lean
  status: reusable
- id: stratonovich-ham-second-moment-lean/local-flow-schur-rescale
  decl: StratonovichHAMAudit.LocalFlow.schur_rescale
  kind: theorem
  summary: "For reals k > 0, R > 0 and any real b, (k/R)^(2*b) * R^(2*b) = k^(2*b), with real powers."
  keywords: [schur-test, rescaling, real-power]
  file: StratonovichHAMAudit/LocalFlow.lean
  status: reusable
- id: stratonovich-ham-second-moment-lean/local-flow-source-overlap
  decl: StratonovichHAMAudit.LocalFlow.source_overlap
  kind: theorem
  summary: "For real alpha < 1, sourceSigma alpha = -(1 + alpha)/4 satisfies -1/2 < sourceSigma alpha and 2 * sourceSigma alpha + alpha < 0."
  keywords: [sobolev-index, parameter-range]
  file: StratonovichHAMAudit/LocalFlow.lean
  status: reusable
- id: stratonovich-ham-second-moment-lean/local-flow-source-white-obstruction
  decl: StratonovichHAMAudit.LocalFlow.source_white_obstruction
  kind: theorem
  summary: "For reals s, sigma with -s < sigma and s - 1 < sigma, it is not the case that sigma < -1/2."
  keywords: [sobolev-index, obstruction]
  file: StratonovichHAMAudit/LocalFlow.lean
  status: reusable
- id: stratonovich-ham-second-moment-lean/local-flow-source-tail-obstruction
  decl: StratonovichHAMAudit.LocalFlow.source_tail_obstruction
  kind: theorem
  summary: "For reals alpha, s, sigma with -s < sigma, s - 1 < sigma and 2*sigma + alpha < 0, one has alpha < 1."
  keywords: [sobolev-index, obstruction]
  file: StratonovichHAMAudit/LocalFlow.lean
  status: reusable
# MiddleCross
- id: stratonovich-ham-second-moment-lean/middle-cross-certificate-pos
  decl: StratonovichHAMAudit.MiddleCross.certificate_pos
  kind: theorem
  summary: "For reals x >= 0 and y > 0, certificate x y > 0, where certificate is the explicit polynomial in the source: y times a nested Horner form in x and y with positive integer coefficients."
  keywords: [polynomial-certificate, positivity]
  file: StratonovichHAMAudit/MiddleCross.lean
  status: reusable
- id: stratonovich-ham-second-moment-lean/middle-cross-parameter-identity
  decl: StratonovichHAMAudit.MiddleCross.parameter_identity
  kind: theorem
  summary: "For reals z > 0 and t > 0, numerator (paramB z) (paramC z t) (paramD z t) (paramE z) * (32768 * t^7 * z^9) = certificate (z - 2) (t - 1), where paramB z = (z^2 - 1)/(2*z), paramE z = (z^2 + 1)/(2*z), and paramC, paramD are the explicit rational expressions in z, t defined in the module."
  keywords: [rational-parametrization, polynomial-identity]
  file: StratonovichHAMAudit/MiddleCross.lean
  status: reusable
- id: stratonovich-ham-second-moment-lean/middle-cross-parameter-numerator-pos
  decl: StratonovichHAMAudit.MiddleCross.parameter_numerator_pos
  kind: theorem
  summary: "For reals z >= 2 and t > 1, numerator (paramB z) (paramC z t) (paramD z t) (paramE z) > 0."
  keywords: [rational-parametrization, positivity]
  file: StratonovichHAMAudit/MiddleCross.lean
  status: reusable
- id: stratonovich-ham-second-moment-lean/middle-cross-difference-identity
  decl: StratonovichHAMAudit.MiddleCross.difference_identity
  kind: theorem
  summary: "For reals b >= 1, c >= 1, d > 0, e > 0, actual b c - upper b c d e = numerator b c d e / denominator b c d e, for the explicit rational functions actual, upper, numerator and denominator defined in the module."
  keywords: [rational-identity, comparison]
  file: StratonovichHAMAudit/MiddleCross.lean
  status: reusable
- id: stratonovich-ham-second-moment-lean/middle-cross-resolvent-difference
  decl: StratonovichHAMAudit.MiddleCross.resolvent_difference
  kind: theorem
  summary: "For reals b >= 1, c >= 1, d > 0, e > 0, resolvent b c d - resolvent b c e = (e - d) * massK b c * (part1 b d e + part2 b c d e), for the explicit rational functions defined in the module."
  keywords: [divided-difference, rational-identity]
  file: StratonovichHAMAudit/MiddleCross.lean
  status: reusable
- id: stratonovich-ham-second-moment-lean/middle-cross-root-numerator-pos
  decl: StratonovichHAMAudit.MiddleCross.root_numerator_pos
  kind: theorem
  summary: "For reals b >= 1 and c > 1, numerator b c (sqrt(b^2 + c^2 - 1)) (sqrt(b^2 + 1)) > 0."
  keywords: [positivity, square-root]
  file: StratonovichHAMAudit/MiddleCross.lean
  status: reusable
- id: stratonovich-ham-second-moment-lean/middle-cross-middle-bound
  decl: StratonovichHAMAudit.MiddleCross.middle_bound
  kind: theorem
  summary: "For reals b >= 1 and c > 1, upper b c (sqrt(b^2 + c^2 - 1)) (sqrt(b^2 + 1)) < actual b c, for the explicit rational functions upper and actual defined in the module."
  keywords: [strict-comparison, rational-function]
  file: StratonovichHAMAudit/MiddleCross.lean
  status: reusable
# MovingCone
- id: stratonovich-ham-second-moment-lean/moving-cone-residual-budget
  decl: StratonovichHAMAudit.MovingCone.residual_budget
  kind: theorem
  summary: "For reals theta, q, d, e with 0 <= theta, q <= 1/8, 0 <= d <= theta and e <= theta/4, one has q*(theta + d) + e <= theta/2."
  keywords: [cone-invariance, budget-inequality]
  file: StratonovichHAMAudit/MovingCone.lean
  status: reusable
- id: stratonovich-ham-second-moment-lean/moving-cone-cone-conversion
  decl: StratonovichHAMAudit.MovingCone.cone_conversion
  kind: theorem
  summary: "For reals theta, a, x, y, rho with 0 <= theta, 0 < a, rho < 1/2, (1 - rho)*a <= x and y <= theta*a/2, one has 0 < x and y <= theta*x."
  keywords: [cone-invariance, scalar-inequality]
  file: StratonovichHAMAudit/MovingCone.lean
  status: reusable
- id: stratonovich-ham-second-moment-lean/moving-cone-terminal-margin
  decl: StratonovichHAMAudit.MovingCone.terminal_margin
  kind: theorem
  summary: "For reals j, K, theta, e, y with 0 < j, 16*K*theta <= j, e <= j/8 and 3*j/4 - 2*K*theta - e <= y, one has j/2 <= y and 0 < y."
  keywords: [cone-invariance, terminal-margin]
  file: StratonovichHAMAudit/MovingCone.lean
  status: reusable
# OccupationForm
- id: stratonovich-ham-second-moment-lean/occupation-form-potential-budget
  decl: StratonovichHAMAudit.OccupationForm.potential_budget
  kind: theorem
  summary: "For reals A, D, N and eps > 0, A*D*N + A*N^2 <= eps*D^2 + (A + A^2/(4*eps))*N^2."
  keywords: [form-bound, young-inequality]
  file: StratonovichHAMAudit/OccupationForm.lean
  status: reusable
- id: stratonovich-ham-second-moment-lean/occupation-form-shifted-coercivity
  decl: StratonovichHAMAudit.OccupationForm.shifted_coercivity
  kind: theorem
  summary: "For reals D, N, P, C with P <= D^2/2 + C*N^2, one has (D^2 + N^2)/2 <= D^2 - P + (C + 1)*N^2."
  keywords: [coercivity, form-bound]
  file: StratonovichHAMAudit/OccupationForm.lean
  status: reusable
# PhaseResponse
- id: stratonovich-ham-second-moment-lean/phase-response-rough-phase-choice
  decl: StratonovichHAMAudit.PhaseResponse.rough_phase_choice
  kind: theorem
  summary: "For reals alpha, a with 0 < alpha + a < 2, s = phaseIndex alpha a = 1 - (alpha + a)/4 satisfies 1/2 < s < 1, 2*s + alpha + a < 3, 2*s + alpha + a - 4 < -1 and alpha + a - 3 < -1."
  keywords: [phase-index, parameter-range]
  file: StratonovichHAMAudit/PhaseResponse.lean
  status: reusable
- id: stratonovich-ham-second-moment-lean/phase-response-balanced-phase
  decl: StratonovichHAMAudit.PhaseResponse.balanced_phase
  kind: theorem
  summary: "For reals alpha, a with alpha + a < 2, one has 2*(1/2) + alpha + a < 3 and alpha + a - 3 < -1."
  keywords: [phase-index, parameter-range]
  file: StratonovichHAMAudit/PhaseResponse.lean
  status: reusable
- id: stratonovich-ham-second-moment-lean/phase-response-energy-boundary
  decl: StratonovichHAMAudit.PhaseResponse.energy_boundary
  kind: theorem
  summary: "For all reals alpha, a, 2*1 + alpha + a < 3 if and only if alpha + a < 1."
  keywords: [phase-index, critical-boundary]
  file: StratonovichHAMAudit/PhaseResponse.lean
  status: reusable
- id: stratonovich-ham-second-moment-lean/phase-response-four-component-gram
  decl: StratonovichHAMAudit.PhaseResponse.four_component_gram
  kind: theorem
  summary: "For reals r1, r2, k1, k2, sin r1 cos k1 sin r2 cos k2 + sin r1 sin k1 sin r2 sin k2 + cos r1 cos k1 cos r2 cos k2 + cos r1 sin k1 cos r2 sin k2 = cos(r1 - r2) * cos(k1 - k2)."
  keywords: [trigonometric-identity, gram-factorization]
  file: StratonovichHAMAudit/PhaseResponse.lean
  status: reusable
- id: stratonovich-ham-second-moment-lean/phase-response-two-frequency-average
  decl: StratonovichHAMAudit.PhaseResponse.two_frequency_average
  kind: theorem
  summary: "For reals x, y, cos x * cos y = (cos(x - y) + cos(x + y))/2."
  keywords: [trigonometric-identity, product-to-sum]
  file: StratonovichHAMAudit/PhaseResponse.lean
  status: reusable
- id: stratonovich-ham-second-moment-lean/phase-response-frequency-window
  decl: StratonovichHAMAudit.PhaseResponse.frequency_window
  kind: theorem
  summary: "For reals J, A, B, t, r, a with A > 0, B >= 0, t > 0, r > 0, 2*B/(A*t) <= r and |J - A*t*r^(a-1)| <= B*r^(a-2), one has (A*t/2)*r^(a-1) <= J <= (3*A*t/2)*r^(a-1); the error bound on J is a supplied hypothesis."
  keywords: [two-sided-bound, real-power, frequency-window]
  file: StratonovichHAMAudit/PhaseResponse.lean
  status: reusable
# PositiveGram
- id: stratonovich-ham-second-moment-lean/positive-gram-scalar-sqrt-dual
  decl: StratonovichHAMAudit.PositiveGram.scalar_sqrt_dual
  kind: theorem
  summary: "For reals ell, w, t with w > 0 and t >= 0, 2*ell*sqrt(t) <= ell^2/w + w*t."
  keywords: [scalar-duality, square-root]
  file: StratonovichHAMAudit/PositiveGram.lean
  status: internal
- id: stratonovich-ham-second-moment-lean/positive-gram-gram-norm-square
  decl: StratonovichHAMAudit.PositiveGram.gram_norm_square
  kind: theorem
  summary: "For a finite index type, a real inner product space H, vectors k i in H and real weights w i, ||sum_i w i * k i||^2 = sum_i sum_j w i * <k i, k j> * w j."
  keywords: [gram-matrix, inner-product]
  file: StratonovichHAMAudit/PositiveGram.lean
  status: internal
- id: stratonovich-ham-second-moment-lean/positive-gram-active-upper-bound
  decl: StratonovichHAMAudit.PositiveGram.active_upper_bound
  kind: theorem
  summary: "For a finite index type, Phi and k i in a real inner product space, real ell i, b i, weights w i > 0 and <Phi, k i> - b i >= 0 for every i, 2 * sum_i ell i * sqrt(<Phi, k i> - b i) - ||Phi||^2/2 <= sum_i ell i^2/w i - sum_i b i * w i + ||sum_i w i * k i||^2/2."
  keywords: [gram-matrix, dual-bound, inner-product]
  file: StratonovichHAMAudit/PositiveGram.lean
  status: internal
- id: stratonovich-ham-second-moment-lean/positive-gram-half-weighted-entrywise-mono
  decl: StratonovichHAMAudit.PositiveGram.half_weighted_entrywise_mono
  kind: theorem
  summary: "For a finite index type, real matrices C, D with C i j <= D i j for all i, j and weights w i >= 0, (1/2) * sum_i sum_j w i * C i j * w j <= (1/2) * sum_i sum_j w i * D i j * w j."
  keywords: [entrywise-order, quadratic-form]
  file: StratonovichHAMAudit/PositiveGram.lean
  status: internal
# ProjectionResidual
- id: stratonovich-ham-second-moment-lean/projection-residual-projection-gap
  decl: StratonovichHAMAudit.ProjectionResidual.projection_gap
  kind: theorem
  summary: "With actualMeanCoeff = 20000/1932951 and projectedLower = 101/(3200*sqrt(2)), actualMeanCoeff + 1/96 < projectedLower."
  keywords: [numerical-certificate, counterexample]
  file: StratonovichHAMAudit/ProjectionResidual.lean
  status: reusable
- id: stratonovich-ham-second-moment-lean/projection-residual-tilted-gap
  decl: StratonovichHAMAudit.ProjectionResidual.tilted_gap
  kind: theorem
  summary: "For reals p, q with 101/(3200*sqrt(2)) <= p, one has 20000/1932951 + (q - 1)*p + 1/96 < q*p."
  keywords: [numerical-certificate, affine-bound]
  file: StratonovichHAMAudit/ProjectionResidual.lean
  status: reusable
# RawValueCeiling
- id: stratonovich-ham-second-moment-lean/raw-value-ceiling-exact-gap
  decl: StratonovichHAMAudit.RawValueCeiling.exact_gap
  kind: theorem
  summary: "In the natural numbers, 2 * 30^60 < 39^39 * 21^21."
  keywords: [numerical-certificate, integer-inequality]
  file: StratonovichHAMAudit/RawValueCeiling.lean
  status: reusable
- id: stratonovich-ham-second-moment-lean/raw-value-ceiling-strict-log-gap
  decl: StratonovichHAMAudit.RawValueCeiling.strict_log_gap
  kind: theorem
  summary: "For reals q, a with a > 0 and q - 2*a > 0, (q*log q + (q - 2*a)*log(q - 2*a))/2 - (q - a)*log(q - a) > 0 (strict midpoint convexity of x log x)."
  keywords: [strict-convexity, entropy-gap]
  file: StratonovichHAMAudit/RawValueCeiling.lean
  status: reusable
# RawVariational
- id: stratonovich-ham-second-moment-lean/raw-variational-dilation-factors
  decl: StratonovichHAMAudit.RawVariational.dilation_factors
  kind: theorem
  summary: "For real s > 0 and any real alpha, s^(3 - alpha) * s^(alpha - 1) = s^2 and s^(3 - alpha) * s^2 / s = s^(4 - alpha), with real powers."
  keywords: [dilation, real-power]
  file: StratonovichHAMAudit/RawVariational.lean
  status: reusable
- id: stratonovich-ham-second-moment-lean/raw-variational-label-score
  decl: StratonovichHAMAudit.RawVariational.label_score
  kind: theorem
  summary: "For reals c > 0, alpha < 3 and any reals I, v, c * (c^(1/(3 - alpha)) * I) - (c^(1/(3 - alpha)))^(4 - alpha) * v/2 = c^((4 - alpha)/(3 - alpha)) * (I - v/2)."
  keywords: [score-homogeneity, dilation, real-power]
  file: StratonovichHAMAudit/RawVariational.lean
  status: reusable
- id: stratonovich-ham-second-moment-lean/raw-variational-positive-score
  decl: StratonovichHAMAudit.RawVariational.positive_score
  kind: theorem
  summary: "For reals I > 0, v > 0 and alpha < 3, with r = (I/v)^(1/(3 - alpha)), one has r*I - r^(4 - alpha)*v/2 > 0."
  keywords: [positive-score, dilation]
  file: StratonovichHAMAudit/RawVariational.lean
  status: reusable
- id: stratonovich-ham-second-moment-lean/raw-variational-strict-label-factor
  decl: StratonovichHAMAudit.RawVariational.strict_label_factor
  kind: theorem
  summary: "For real alpha < 3, 2 < 2^((4 - alpha)/(3 - alpha))."
  keywords: [label-factor, real-power]
  file: StratonovichHAMAudit/RawVariational.lean
  status: reusable
# TerminalCross
- id: stratonovich-ham-second-moment-lean/terminal-cross-polynomial-identity
  decl: StratonovichHAMAudit.TerminalCross.polynomial_identity
  kind: theorem
  summary: "For all reals b, c, polynomial b c = certificate (b - 1) (c - 1), where polynomial is the explicit two-variable polynomial built from numP c = c^2 + c + 1 and numN b c = b * numP c + c^3 + c + 1, and certificate is an explicit polynomial with positive integer coefficients times its second argument."
  keywords: [polynomial-certificate, shifted-variables]
  file: StratonovichHAMAudit/TerminalCross.lean
  status: reusable
- id: stratonovich-ham-second-moment-lean/terminal-cross-polynomial-pos
  decl: StratonovichHAMAudit.TerminalCross.polynomial_pos
  kind: theorem
  summary: "For reals b >= 1 and c > 1, polynomial b c > 0."
  keywords: [polynomial-positivity, comparison]
  file: StratonovichHAMAudit/TerminalCross.lean
  status: reusable
- id: stratonovich-ham-second-moment-lean/terminal-cross-rate-le
  decl: StratonovichHAMAudit.TerminalCross.rate_le
  kind: theorem
  summary: "For reals A > 0 and s >= 1/2, A/(2*(A + 1)) <= s*A/(A + 2*s)."
  keywords: [rate-bound, scalar-inequality]
  file: StratonovichHAMAudit/TerminalCross.lean
  status: reusable
- id: stratonovich-ham-second-moment-lean/terminal-cross-exponential-difference
  decl: StratonovichHAMAudit.TerminalCross.exponential_difference
  kind: theorem
  summary: "For reals C, D, r, R, k, w with 0 <= D < C and (C - D)*k = C*r - D*R, one has C*exp(-r*w) - D*exp(-R*w) <= (C - D)*exp(-k*w) (convexity of exp)."
  keywords: [convexity, exponential-bound]
  file: StratonovichHAMAudit/TerminalCross.lean
  status: reusable
- id: stratonovich-ham-second-moment-lean/terminal-cross-terminal-bound
  decl: StratonovichHAMAudit.TerminalCross.terminal_bound
  kind: theorem
  summary: "For reals b >= 1 and c > 1, numP c / (16*c^3*(c + 1)*sqrt(b^2 + (c^2 - 1)/(c^2 + 1))) < numN b c / (32*c^3*(b + c - 1)*(b + 1)), with numP c = c^2 + c + 1 and numN b c = b * numP c + c^3 + c + 1."
  keywords: [strict-comparison, square-root]
  file: StratonovichHAMAudit/TerminalCross.lean
  status: reusable
# WhiteCDF
- id: stratonovich-ham-second-moment-lean/white-cdf-cdf-square-bound
  decl: StratonovichHAMAudit.WhiteCDF.cdf_square_bound
  kind: theorem
  summary: "For reals A, b, if 0 <= b - 2*z*A + z^2/3 for every real z, then 3*A^2 <= b; the quadratic lower bound in z is a supplied hypothesis."
  keywords: [quadratic-discriminant, profile-bound]
  file: StratonovichHAMAudit/WhiteCDF.lean
  status: reusable
- id: stratonovich-ham-second-moment-lean/white-cdf-energy-upper
  decl: StratonovichHAMAudit.WhiteCDF.energy_upper
  kind: theorem
  summary: "For reals c, A, b with 3*A^2 <= b, one has c*A - b/2 <= c^2/6."
  keywords: [energy-bound, completing-square]
  file: StratonovichHAMAudit/WhiteCDF.lean
  status: reusable

===== END CLAIMS FILE: claims.yaml =====

===== BEGIN LEAN FILE: StratonovichHAMAudit/ActualEvent.lean =====
module
public import Mathlib.Tactic
public import Mathlib.Analysis.SpecialFunctions.Pow.Real
@[expose] public section
noncomputable section
set_option autoImplicit false
namespace StratonovichHAMAudit.ActualEvent

theorem finite_error_accumulation (C e : ℝ) (d : ℕ → ℝ)
    (hC : 1 ≤ C) (he : 0 ≤ e) (hzero : d 0 ≤ 0)
    (hstep : ∀ n, d (n+1) ≤ C*d n+C^n*e) (n : ℕ) :
    d n ≤ (n:ℝ)*C^n*e := by
  have hC0 : 0 ≤ C := by linarith
  induction n with
  | zero => simpa using hzero
  | succ n ih =>
    have hmul := mul_le_mul_of_nonneg_left ih hC0
    have hp : 0 ≤ C^n*e := mul_nonneg (pow_nonneg hC0 n) he
    have hg := mul_le_mul_of_nonneg_right hC hp
    simp only [one_mul] at hg
    rw [pow_succ]
    push_cast
    nlinarith [hstep n, hmul, hg]

theorem moderate_penalty (delta : ℝ) (hd : 0 < delta) :
    delta*(delta^(-(1:ℝ)/4)/Real.sqrt delta)=delta^((1:ℝ)/4) := by
  calc
    delta*(delta^(-(1:ℝ)/4)/Real.sqrt delta)
      = delta^(1:ℝ)*(delta^(-(1:ℝ)/4)/delta^((1:ℝ)/2)) := by
          rw [Real.rpow_one, Real.sqrt_eq_rpow]
    _ = delta^((1:ℝ)+(-(1:ℝ)/4-(1:ℝ)/2)) := by
          rw [Real.rpow_add hd, Real.rpow_sub hd]
    _ = delta^((1:ℝ)/4) := by congr 1; norm_num

end StratonovichHAMAudit.ActualEvent

===== END LEAN FILE: StratonovichHAMAudit/ActualEvent.lean =====

===== BEGIN LEAN FILE: StratonovichHAMAudit/AllAlphaMoment.lean =====
module
public import Mathlib.Tactic
@[expose] public section
noncomputable section
set_option autoImplicit false
namespace StratonovichHAMAudit.AllAlphaMoment

theorem moment_lower (a D x y : ℝ) (ha : 0 < a) (hD : 0 < D)
    (hmean : x + y = a) (hcs : x^2 ≤ D*y/2) :
    2*a^2/(D+4*a) ≤ y := by
  have hden : 0 < D+4*a := by positivity
  apply (div_le_iff₀ hden).2
  have hx : x = a-y := by linarith
  rw [hx] at hcs
  nlinarith [sq_nonneg y]

theorem rational_gap (a D : ℝ) (ha : 0 < a) (hD : 0 < D) :
    a^2/(D*(D+4*a))-a^2/(2*D*(D+2*a))
      =a^2/(2*(D+4*a)*(D+2*a)) ∧
    0 < a^2/(2*(D+4*a)*(D+2*a)) := by
  constructor
  · have hD0 : D ≠ 0 := ne_of_gt hD
    have hfour : D+4*a ≠ 0 := ne_of_gt (by positivity)
    have htwo : D+2*a ≠ 0 := ne_of_gt (by positivity)
    field_simp [hD0,hfour,htwo]
    ring
  · positivity

end StratonovichHAMAudit.AllAlphaMoment

===== END LEAN FILE: StratonovichHAMAudit/AllAlphaMoment.lean =====

===== BEGIN LEAN FILE: StratonovichHAMAudit/ClockFilter.lean =====
module

public import Mathlib.MeasureTheory.Integral.Bochner.Basic
public import Mathlib.Tactic

@[expose] public section

set_option autoImplicit false

open MeasureTheory Filter

namespace StratonovichHAMAudit.ClockFilter

theorem resolvent_partial_fraction (θ ell r : ℝ) (hθ : 0 < θ) (hell : 0 < ell) :
    (2 * θ + ell) / (2 * θ * (θ ^ 2 + r ^ 2) * ((θ + ell) ^ 2 + r ^ 2)) =
      (1 / (θ ^ 2 + r ^ 2) - 1 / ((θ + ell) ^ 2 + r ^ 2)) / (2 * θ * ell) := by
  have hA : θ ^ 2 + r ^ 2 ≠ 0 := ne_of_gt (by positivity)
  have hB : (θ + ell) ^ 2 + r ^ 2 ≠ 0 := ne_of_gt (by positivity)
  field_simp [hθ.ne', hell.ne', hA, hB]
  ring

theorem clock_filter_bounds (θ ell : ℝ) (hθ : 0 < θ) (hell : 0 < ell) :
    0 < 2 * θ / (2 * θ + ell) ∧ 2 * θ / (2 * θ + ell) < 1 := by
  have hden : 0 < 2 * θ + ell := by linarith
  constructor
  · exact div_pos (by linarith) hden
  · exact (div_lt_one hden).2 (by linarith)

theorem strict_filter_integral (θ : ℝ) (hθ : 0 < θ)
    (σ : Measure ℝ) (hσ : σ ≠ 0)
    (hell : ∀ᵐ ell ∂σ, 0 < ell)
    (w : ℝ → ℝ) (hw : Integrable w σ)
    (hwpos : ∀ᵐ ell ∂σ, 0 < w ell) :
    Integrable (fun ell => 2 * θ / (2 * θ + ell) * w ell) σ ∧
      (∫ ell, 2 * θ / (2 * θ + ell) * w ell ∂σ) < ∫ ell, w ell ∂σ := by
  let f : ℝ → ℝ := fun ell => 2 * θ / (2 * θ + ell) * w ell
  have hmeas : Measurable (fun ell : ℝ => 2 * θ / (2 * θ + ell)) :=
    measurable_const.div (measurable_const.add measurable_id)
  have hfm : AEStronglyMeasurable f σ :=
    hmeas.aestronglyMeasurable.mul hw.aestronglyMeasurable
  have hnonneg : ∀ᵐ ell ∂σ, 0 ≤ f ell := by
    filter_upwards [hell, hwpos] with ell hell0 hw0
    exact (mul_pos (clock_filter_bounds θ ell hθ hell0).1 hw0).le
  have hstrict : ∀ᵐ ell ∂σ, f ell < w ell := by
    filter_upwards [hell, hwpos] with ell hell0 hw0
    calc
      f ell = 2 * θ / (2 * θ + ell) * w ell := rfl
      _ < 1 * w ell := mul_lt_mul_of_pos_right
        (clock_filter_bounds θ ell hθ hell0).2 hw0
      _ = w ell := one_mul _
  have hle : f ≤ᵐ[σ] w := hstrict.mono fun _ h => h.le
  have hfi : Integrable f σ := hw.mono_nonneg hfm hnonneg hle
  have hIntLe : (∫ ell, f ell ∂σ) ≤ ∫ ell, w ell ∂σ :=
    integral_mono_ae hfi hw hle
  have hne : (∫ ell, f ell ∂σ) ≠ ∫ ell, w ell ∂σ := by
    intro heq
    have hae : f =ᵐ[σ] w := (integral_eq_iff_of_ae_le hfi hw hle).1 heq
    let : (ae σ).NeBot := ae_neBot.2 hσ
    obtain ⟨ell, hlt, heqell⟩ := (hstrict.and hae).exists
    exact (ne_of_lt hlt) heqell
  refine ⟨hfi, ?_⟩
  exact lt_of_le_of_ne hIntLe hne

end StratonovichHAMAudit.ClockFilter

===== END LEAN FILE: StratonovichHAMAudit/ClockFilter.lean =====

===== BEGIN LEAN FILE: StratonovichHAMAudit/DampedLower.lean =====
module
public import Mathlib.Tactic
public import Mathlib.Analysis.Real.Pi.Bounds
@[expose] public section
noncomputable section
set_option autoImplicit false
namespace StratonovichHAMAudit.DampedLower

theorem exact_margin : (9:ℕ)*2^28 < 157^3*5^4 := by
  norm_num

theorem pi_cube_certificate : (9:ℝ)*2^25/5^10 < Real.pi^3 := by
  have hp := Real.pi_gt_d2
  have hfrac : (3.14:ℝ) = 157/50 := by norm_num
  rw [hfrac] at hp
  have hpi : 0 < Real.pi := Real.pi_pos
  have hs : 0 < Real.pi^2+(157/50:ℝ)*Real.pi+(157/50:ℝ)^2 := by
    positivity
  have hm := mul_pos (sub_pos.mpr hp) hs
  have hr : (9:ℝ)*2^25/5^10 < (157/50:ℝ)^3 := by norm_num
  nlinarith

theorem rational_pi_gain :
    (157:ℝ)^3*5^4/(9*2^28) < Real.pi^3*5^10/(9*2^25) := by
  have hp := Real.pi_gt_d2
  have hfrac : (3.14:ℝ) = 157/50 := by norm_num
  rw [hfrac] at hp
  have hpi : 0 < Real.pi := Real.pi_pos
  have hs : 0 < Real.pi^2+(157/50:ℝ)*Real.pi+(157/50:ℝ)^2 := by
    positivity
  have hm := mul_pos (sub_pos.mpr hp) hs
  nlinarith

end StratonovichHAMAudit.DampedLower

===== END LEAN FILE: StratonovichHAMAudit/DampedLower.lean =====

===== BEGIN LEAN FILE: StratonovichHAMAudit/DimensionalMatrix.lean =====
module
public import Mathlib.Tactic
public import Mathlib.LinearAlgebra.Matrix.Notation
@[expose] public section
noncomputable section
set_option autoImplicit false
namespace StratonovichHAMAudit.DimensionalMatrix

def backward (cp sp p : ℝ) : Matrix (Fin 2) (Fin 2) ℝ :=
  !![cp,-sp/p;p*sp,cp]
def coupling (H : ℝ) : Matrix (Fin 2) (Fin 2) ℝ := !![0,0;H,0]
def forward (cq sq q : ℝ) : Matrix (Fin 2) (Fin 2) ℝ :=
  !![cq,sq/q;-q*sq,cq]

theorem full_interaction (cp sp p H cq sq q : ℝ) :
    backward cp sp p * coupling H * forward cq sq q =
      !![-(sp/p)*H*cq,-(sp/p)*H*(sq/q);cp*H*cq,cp*H*(sq/q)] := by
  ext i j
  fin_cases i <;> fin_cases j <;>
    simp [backward,coupling,forward,Matrix.mul_apply,Fin.sum_univ_two]
  all_goals ring

end StratonovichHAMAudit.DimensionalMatrix

===== END LEAN FILE: StratonovichHAMAudit/DimensionalMatrix.lean =====

===== BEGIN LEAN FILE: StratonovichHAMAudit/DirectEvent.lean =====
module
public import Mathlib.Tactic
public import Mathlib.Analysis.SpecialFunctions.Pow.Real
public import Mathlib.LinearAlgebra.Matrix.Notation
public import Mathlib.LinearAlgebra.Matrix.Determinant.Basic
public import Mathlib.LinearAlgebra.Matrix.Trace
@[expose] public section
noncomputable section
set_option autoImplicit false
namespace StratonovichHAMAudit.DirectEvent

def kappa (alpha a : ℝ) : ℝ := (4-alpha-a)/(3-alpha)
def delta (T alpha a : ℝ) : ℝ := T ^ (-kappa alpha a)
def radius (T alpha a : ℝ) : ℝ := T * delta T alpha a

theorem kappa_gt_one (alpha a : ℝ) (ha : a < 1) (halpha : alpha < 3) :
    1 < kappa alpha a := by
  unfold kappa
  apply (lt_div_iff₀ (by linarith : (0:ℝ) < 3-alpha)).2
  linarith

theorem physical_scale (T alpha a : ℝ) (hT : 0 < T) (halpha : alpha < 3) :
    radius T alpha a = T ^ ((a-1)/(3-alpha)) := by
  have hd : 3-alpha ≠ 0 := by linarith
  unfold radius delta
  calc
    T * T ^ (-kappa alpha a) = T ^ ((1:ℝ)-kappa alpha a) := by
      rw [sub_eq_add_neg, Real.rpow_add hT]
      norm_num
    _ = _ := by
      congr 1
      unfold kappa
      field_simp [hd]
      ring

theorem noise_scale (T alpha a : ℝ) (hT : 0 < T) (halpha : alpha < 3) :
    T ^ (-a/2) * (radius T alpha a) ^ (2-alpha/2) = Real.sqrt (delta T alpha a) := by
  have hd : 3-alpha ≠ 0 := by linarith
  rw [physical_scale T alpha a hT halpha]
  unfold delta
  rw [Real.sqrt_eq_rpow, ← Real.rpow_mul hT.le, ← Real.rpow_mul hT.le,
    ← Real.rpow_add hT]
  congr 1
  unfold kappa
  field_simp [hd]
  ring

theorem vertex_scale (T alpha a : ℝ) (hT : 0 < T) (halpha : alpha < 3) :
    T ^ (1-a/2) * (radius T alpha a) ^ (1-alpha/2) =
      (delta T alpha a) ^ (-(1:ℝ)/2) := by
  have hd : 3-alpha ≠ 0 := by linarith
  rw [physical_scale T alpha a hT halpha]
  unfold delta
  rw [← Real.rpow_mul hT.le, ← Real.rpow_mul hT.le, ← Real.rpow_add hT]
  congr 1
  unfold kappa
  field_simp [hd]
  ring

def gauge (w : ℝ) : Matrix (Fin 2) (Fin 2) ℝ := !![1,0;w,1]
def drift : Matrix (Fin 2) (Fin 2) ℝ := !![0,1;1,0]

theorem gauge_inverse (w : ℝ) : gauge (-w) * gauge w = 1 := by
  ext i j
  fin_cases i <;> fin_cases j <;>
    simp [gauge, Matrix.mul_apply, Fin.sum_univ_two]

theorem gauge_drift (w : ℝ) :
    gauge (-w) * drift * gauge w = !![w,1;1-w^2,-w] := by
  simp only [gauge, drift, Matrix.mul_fin_two]
  ext i j
  fin_cases i <;> fin_cases j <;> simp
  ring

def pulseZero : Matrix (Fin 2) (Fin 2) ℝ := !![1,1;0,1]
def pulseTwo (a b : ℝ) : Matrix (Fin 2) (Fin 2) ℝ := !![a,b;2*b,a]

theorem monodromy (a b : ℝ) :
    pulseTwo a b * pulseZero = !![a,a+b;2*b,a+2*b] ∧
    Matrix.det (pulseTwo a b * pulseZero) = a^2-2*b^2 ∧
    Matrix.trace (pulseTwo a b * pulseZero) = 2*(a+b) := by
  have h : pulseTwo a b * pulseZero = !![a,a+b;2*b,a+2*b] := by
    simp [pulseTwo, pulseZero, add_comm]
  rw [h]
  constructor
  · rfl
  constructor
  · simp [Matrix.det_fin_two]
    ring
  · simp [Matrix.trace_fin_two]
    ring

end StratonovichHAMAudit.DirectEvent

===== END LEAN FILE: StratonovichHAMAudit/DirectEvent.lean =====

===== BEGIN LEAN FILE: StratonovichHAMAudit/FiniteYoung.lean =====
module
public import Mathlib.Tactic
public import Mathlib.Analysis.MeanInequalities
@[expose] public section
noncomputable section
set_option autoImplicit false
namespace StratonovichHAMAudit.FiniteYoung

theorem weighted_natural_powers (L q : ℕ) (hL : 0 < L) (hq : q ≤ L) (x y : ℝ) :
    |x| ^ q * |y| ^ (L-q) ≤
      (q : ℝ) / (L : ℝ) * |x| ^ L + ((L-q : ℕ) : ℝ) / (L : ℝ) * |y| ^ L := by
  have hLr : 0 < (L : ℝ) := by exact_mod_cast hL
  have hLn : (L : ℝ) ≠ 0 := ne_of_gt hLr
  have hsum : (q : ℝ) / (L : ℝ) + ((L-q : ℕ) : ℝ) / (L : ℝ) = 1 := by
    rw [← add_div, Nat.cast_sub hq]
    have hn : (q : ℝ) + ((L : ℝ) - (q : ℝ)) = (L : ℝ) := by ring
    rw [hn, div_self hLn]
  have hx : (|x| ^ L) ^ ((q : ℝ) / (L : ℝ)) = |x| ^ q := by
    rw [← Real.rpow_natCast, ← Real.rpow_mul (abs_nonneg x)]
    have he : (L : ℝ) * ((q : ℝ) / (L : ℝ)) = (q : ℝ) := by exact mul_div_cancel₀ _ hLn
    rw [he, Real.rpow_natCast]
  have hy : (|y| ^ L) ^ (((L-q : ℕ) : ℝ) / (L : ℝ)) = |y| ^ (L-q) := by
    rw [← Real.rpow_natCast, ← Real.rpow_mul (abs_nonneg y)]
    have he : (L : ℝ) * (((L-q : ℕ) : ℝ) / (L : ℝ)) = ((L-q : ℕ) : ℝ) := by
      exact mul_div_cancel₀ _ hLn
    rw [he, Real.rpow_natCast]
  have h := Real.geom_mean_le_arith_mean2_weighted
    (div_nonneg (Nat.cast_nonneg q) hLr.le)
    (div_nonneg (Nat.cast_nonneg (L-q)) hLr.le)
    (pow_nonneg (abs_nonneg x) L) (pow_nonneg (abs_nonneg y) L) hsum
  rw [hx, hy] at h
  exact h

end StratonovichHAMAudit.FiniteYoung

===== END LEAN FILE: StratonovichHAMAudit/FiniteYoung.lean =====

===== BEGIN LEAN FILE: StratonovichHAMAudit/GaussianTail.lean =====
module
public import Mathlib.Analysis.SpecialFunctions.Pow.Real
public import Mathlib.Tactic
@[expose] public section
noncomputable section
set_option autoImplicit false
namespace StratonovichHAMAudit.GaussianTail

theorem cutoff_density_split (M x C nu : ℝ)
    (hM : 0 < M) (hx : M ≤ x) (hC : 0 ≤ C)
    (hnu : 1 < nu ∧ nu < 2) (hcut : 4 * C ≤ M ^ (2 - nu)) :
    C * x ^ nu - x ^ 2 / 2 ≤ -M ^ 2 / 8 - x ^ 2 / 8 := by
  have hxpos : 0 < x := lt_of_lt_of_le hM hx
  have hmono : M ^ (2 - nu) ≤ x ^ (2 - nu) :=
    Real.rpow_le_rpow hM.le hx (by linarith [hnu.2])
  have hs := mul_le_mul_of_nonneg_right (hcut.trans hmono)
    (Real.rpow_nonneg hxpos.le nu)
  have hr : x ^ (2 - nu) * x ^ nu = x ^ 2 := by
    calc
      _ = x ^ ((2 - nu) + nu) := (Real.rpow_add hxpos _ _).symm
      _ = x ^ (2 : ℝ) := by congr 1; ring
      _ = x ^ (2 : ℕ) := Real.rpow_natCast x 2
  rw [hr] at hs
  have hprod : 0 ≤ (x - M) * (x + M) :=
    mul_nonneg (sub_nonneg.mpr hx) (by linarith)
  have hCx : 0 ≤ C * x ^ nu := mul_nonneg hC (Real.rpow_nonneg hxpos.le nu)
  nlinarith [hs, hprod, hCx]

end StratonovichHAMAudit.GaussianTail

===== END LEAN FILE: StratonovichHAMAudit/GaussianTail.lean =====

===== BEGIN LEAN FILE: StratonovichHAMAudit/GlobalOmega.lean =====
module
public import Mathlib.Tactic
@[expose] public section
noncomputable section
set_option autoImplicit false
namespace StratonovichHAMAudit.GlobalOmega

def envelopePolynomial (x : ℝ) : ℝ :=
  -237888*x^15 + 2567920*x^14 - 10605344*x^13 + 17964536*x^12 + 3700636*x^11 - 59045877*x^10 + 66291248*x^9 + 36266494*x^8 - 125535292*x^7 + 58424029*x^6 + 68792033*x^5 - 94022217*x^4 + 42981706*x^3 - 8102234*x^2 + 516600*x + 9900

def envelopeDenom (x : ℝ) : ℝ :=
  750*(3-x)*(2-x)*(1-x)*(5-2*x)*(3-2*x)*(5-3*x)*(3-4*x-2*x^2)

def envelopeRational (x : ℝ) : ℝ :=
  2*(1-x^2+x^4/2)*(1-4*x^2)/(1-3*x/5)*
    (1/(2*(1-x))+x*(1-x)/(2-x)+x*(x+1)*(1-x)^2/(3*(3-x))-
      2*(1-3*x/5)*(1/(3-2*x)+(2*x+1)*(1-x)/(3*(5-2*x)))*
        x*(177/100)*(1-7*x/5))*(3-4*x)/(3-4*x-2*x^2)

theorem left_certificate (t : ℝ) (ht0 : 0 ≤ t) (ht1 : t ≤ 1) :
    1 ≤ (4:ℝ)^15*envelopePolynomial (t/4) := by
  have h1 : 0 ≤ 1-t := by linarith
  have hid : (4:ℝ)^15*envelopePolynomial (t/4)-1 =
    (10630044057599:ℝ)*t^0*(1-t)^15 +
    (298124417433585:ℝ)*t^1*(1-t)^14 +
    (2513855498420119:ℝ)*t^2*(1-t)^13 +
    (11108582904823353:ℝ)*t^3*(1-t)^12 +
    (30835186027461291:ℝ)*t^4*(1-t)^11 +
    (58554861260633157:ℝ)*t^5*(1-t)^10 +
    (79751967489125491:ℝ)*t^6*(1-t)^9 +
    (80316614660581085:ℝ)*t^7*(1-t)^8 +
    (61414936532707037:ℝ)*t^8*(1-t)^7 +
    (36921141989698675:ℝ)*t^9*(1-t)^6 +
    (18353430194004037:ℝ)*t^10*(1-t)^5 +
    (7893814205477547:ℝ)*t^11*(1-t)^4 +
    (2890010244293689:ℝ)*t^12*(1-t)^3 +
    (811168303884183:ℝ)*t^13*(1-t)^2 +
    (146648694693297:ℝ)*t^14*(1-t)^1 +
    (12356981993087:ℝ)*t^15*(1-t)^0 := by
    unfold envelopePolynomial
    ring
  have hn : 0 ≤
    (10630044057599:ℝ)*t^0*(1-t)^15 +
    (298124417433585:ℝ)*t^1*(1-t)^14 +
    (2513855498420119:ℝ)*t^2*(1-t)^13 +
    (11108582904823353:ℝ)*t^3*(1-t)^12 +
    (30835186027461291:ℝ)*t^4*(1-t)^11 +
    (58554861260633157:ℝ)*t^5*(1-t)^10 +
    (79751967489125491:ℝ)*t^6*(1-t)^9 +
    (80316614660581085:ℝ)*t^7*(1-t)^8 +
    (61414936532707037:ℝ)*t^8*(1-t)^7 +
    (36921141989698675:ℝ)*t^9*(1-t)^6 +
    (18353430194004037:ℝ)*t^10*(1-t)^5 +
    (7893814205477547:ℝ)*t^11*(1-t)^4 +
    (2890010244293689:ℝ)*t^12*(1-t)^3 +
    (811168303884183:ℝ)*t^13*(1-t)^2 +
    (146648694693297:ℝ)*t^14*(1-t)^1 +
    (12356981993087:ℝ)*t^15*(1-t)^0 := by positivity
  linarith

theorem right_certificate (t : ℝ) (ht0 : 0 ≤ t) (ht1 : t ≤ 1) :
    1 ≤ (4:ℝ)^15*envelopePolynomial ((1+t)/4) := by
  have h1 : 0 ≤ 1-t := by linarith
  have hid : (4:ℝ)^15*envelopePolynomial ((1+t)/4)-1 =
    (12356981993087:ℝ)*t^0*(1-t)^15 +
    (224060765099313:ℝ)*t^1*(1-t)^14 +
    (1894937289568407:ℝ)*t^2*(1-t)^13 +
    (9799655243171641:ℝ)*t^3*(1-t)^12 +
    (34453566936433323:ℝ)*t^4*(1-t)^11 +
    (87031904519822405:ℝ)*t^5*(1-t)^10 +
    (163125524987087987:ℝ)*t^6*(1-t)^9 +
    (231150225523443421:ℝ)*t^7*(1-t)^8 +
    (249909141873911517:ℝ)*t^8*(1-t)^7 +
    (206372784329731187:ℝ)*t^9*(1-t)^6 +
    (129237504527758405:ℝ)*t^10*(1-t)^5 +
    (60326501022497451:ℝ)*t^11*(1-t)^4 +
    (20332988225551929:ℝ)*t^12*(1-t)^3 +
    (4674097187389335:ℝ)*t^13*(1-t)^2 +
    (655486353407985:ℝ)*t^14*(1-t)^1 +
    (42278584319999:ℝ)*t^15*(1-t)^0 := by
    unfold envelopePolynomial
    ring
  have hn : 0 ≤
    (12356981993087:ℝ)*t^0*(1-t)^15 +
    (224060765099313:ℝ)*t^1*(1-t)^14 +
    (1894937289568407:ℝ)*t^2*(1-t)^13 +
    (9799655243171641:ℝ)*t^3*(1-t)^12 +
    (34453566936433323:ℝ)*t^4*(1-t)^11 +
    (87031904519822405:ℝ)*t^5*(1-t)^10 +
    (163125524987087987:ℝ)*t^6*(1-t)^9 +
    (231150225523443421:ℝ)*t^7*(1-t)^8 +
    (249909141873911517:ℝ)*t^8*(1-t)^7 +
    (206372784329731187:ℝ)*t^9*(1-t)^6 +
    (129237504527758405:ℝ)*t^10*(1-t)^5 +
    (60326501022497451:ℝ)*t^11*(1-t)^4 +
    (20332988225551929:ℝ)*t^12*(1-t)^3 +
    (4674097187389335:ℝ)*t^13*(1-t)^2 +
    (655486353407985:ℝ)*t^14*(1-t)^1 +
    (42278584319999:ℝ)*t^15*(1-t)^0 := by positivity
  linarith

theorem polynomial_pos (x : ℝ) (hx0 : 0 ≤ x) (hx1 : x ≤ 1/2) :
    0 < envelopePolynomial x := by
  by_cases h : x ≤ 1/4
  · have hb := left_certificate (4*x) (by linarith) (by linarith)
    have he : (4*x)/4=x := by ring
    rw [he] at hb
    nlinarith
  · have hb := right_certificate (4*x-1) (by linarith) (by linarith)
    have he : (1+(4*x-1))/4=x := by ring
    rw [he] at hb
    nlinarith

theorem rational_lt_one (x : ℝ) (hx : 0 < x) (hh : x ≤ 1/2) :
    envelopeRational x < 1 := by
  have h1 : 0 < 1-x := by linarith
  have h2 : 0 < 2-x := by linarith
  have h3 : 0 < 3-x := by linarith
  have h4 : 0 < 3-2*x := by linarith
  have h5 : 0 < 5-2*x := by linarith
  have h6 : 0 < 5-3*x := by linarith
  have hg : 0 < 1-3*x/5 := by linarith
  have h8 : 0 < 3-4*x-2*x^2 := by
    have hm := mul_nonneg hx.le (sub_nonneg.mpr hh)
    nlinarith
  have hd : 0 < envelopeDenom x := by
    unfold envelopeDenom
    positivity
  have n4 : 3-x*2 ≠ 0 := by simpa only [mul_comm] using ne_of_gt h4
  have n5 : 5-x*2 ≠ 0 := by simpa only [mul_comm] using ne_of_gt h5
  have n8 : 3-x*4-x^2*2 ≠ 0 := by simpa only [mul_comm] using ne_of_gt h8
  have hid : envelopeDenom x*(1-envelopeRational x)=x*envelopePolynomial x := by
    unfold envelopeDenom envelopeRational envelopePolynomial
    field_simp [ne_of_gt h1, ne_of_gt h2, ne_of_gt h3, ne_of_gt h4,
      ne_of_gt h5, ne_of_gt h6, ne_of_gt hg, ne_of_gt h8, n4, n5, n8]
    ring
  have hp := mul_pos hx (polynomial_pos x hx.le hh)
  by_contra hnot
  have hv : 1 ≤ envelopeRational x := le_of_not_gt hnot
  have hn := mul_nonpos_of_nonneg_of_nonpos hd.le (sub_nonpos.mpr hv)
  rw [hid] at hn
  linarith

end StratonovichHAMAudit.GlobalOmega

===== END LEAN FILE: StratonovichHAMAudit/GlobalOmega.lean =====

===== BEGIN LEAN FILE: StratonovichHAMAudit/HermiteWord.lean =====
import Std.Tactic

namespace StratonovichHAMAudit.HermiteWord

variable {C B V : Type} [DecidableEq C]

def bump (i : C) (d : C → Nat) : C → Nat :=
  fun c => d c + if c = i then 1 else 0

def counts : List (C × B) → C → Nat
  | [] => fun _ => 0
  | (i, _) :: w => bump i (counts w)

def raw (J : C → V → V) (F : B → V → V) (v₀ : V) : List (C × B) → V
  | [] => v₀
  | (i, b) :: w => F b (J i (raw J F v₀ w))

def cut (P : V → V) (J : C → V → V) (F : B → V → V)
    (v₀ : V) : List (C × B) → V
  | [] => v₀
  | (i, b) :: w => F b (P (J i (P (cut P J F v₀ w))))

theorem raw_support
    (Good : (C → Nat) → V → Prop)
    (J : C → V → V) (F : B → V → V) (v₀ : V)
    (hv₀ : Good (fun _ => 0) v₀)
    (hJ : ∀ d i v, Good d v → Good (bump i d) (J i v))
    (hF : ∀ d b v, Good d v → Good d (F b v))
    (w : List (C × B)) : Good (counts w) (raw J F v₀ w) := by
  induction w with
  | nil => exact hv₀
  | cons a w ih =>
    exact hF _ a.2 _ (hJ _ a.1 _ ih)

theorem cut_eq_raw
    (Good : (C → Nat) → V → Prop)
    (J : C → V → V) (F : B → V → V) (P : V → V)
    (v₀ : V) (N : C → Nat)
    (hv₀ : Good (fun _ => 0) v₀)
    (hJ : ∀ d i v, Good d v → Good (bump i d) (J i v))
    (hF : ∀ d b v, Good d v → Good d (F b v))
    (hP : ∀ d v, (∀ c, d c ≤ N c) → Good d v → P v = v)
    (w : List (C × B)) (hN : ∀ c, counts w c ≤ N c) :
    cut P J F v₀ w = raw J F v₀ w := by
  induction w with
  | nil => rfl
  | cons a w ih =>
    have hs : ∀ c, counts w c ≤ N c := by
      intro c
      have hc := hN c
      simp only [counts, bump] at hc
      omega
    have hw := raw_support Good J F v₀ hv₀ hJ hF w
    have hp₀ := hP (counts w) (raw J F v₀ w) hs hw
    have hp₁ := hP (bump a.1 (counts w)) (J a.1 (raw J F v₀ w))
      hN (hJ _ _ _ hw)
    change F a.2 (P (J a.1 (P (cut P J F v₀ w)))) =
      F a.2 (J a.1 (raw J F v₀ w))
    rw [ih hs, hp₀, hp₁]

end StratonovichHAMAudit.HermiteWord

===== END LEAN FILE: StratonovichHAMAudit/HermiteWord.lean =====

===== BEGIN LEAN FILE: StratonovichHAMAudit/HermiteWordConsumer.lean =====
import StratonovichHAMAudit.HermiteWord

namespace StratonovichHAMAudit.HermiteWordConsumer
open StratonovichHAMAudit.HermiteWord

-- Coefficients in the unnormalized probabilists' Hermite basis:
-- x He_n = He_(n+1) + n He_(n-1). This defines the finite recurrence;
-- no assertion about Gaussian L² or polynomial realization is imported.
private def vacuum (n : Nat) : Nat := if n = 0 then 1 else 0
private def insert (_ : Unit) (p : Nat → Nat) (n : Nat) : Nat :=
  (if n = 0 then 0 else p (n-1)) + (n+1) * p (n+1)
private def frame (_ : Unit) (p : Nat → Nat) := p
private def project (N : Nat) (p : Nat → Nat) (n : Nat) :=
  if n ≤ N then p n else 0
private def Good (d : Unit → Nat) (p : Nat → Nat) : Prop :=
  ∀ n, d () < n → p n = 0

private theorem vacuum_good : Good (fun _ => 0) vacuum := by
  intro n hn
  simp only [vacuum]
  split <;> omega

private theorem insert_good (d : Unit → Nat) (i : Unit) (p : Nat → Nat)
    (hp : Good d p) : Good (bump i d) (insert i p) := by
  intro n hn
  have hi : i = () := by cases i; rfl
  subst i
  simp [bump] at hn
  have h₁ : p (n-1) = 0 := hp _ (by omega)
  have h₂ : p (n+1) = 0 := hp _ (by omega)
  simp [insert, h₁, h₂]

private theorem frame_good (d : Unit → Nat) (b : Unit) (p : Nat → Nat)
    (hp : Good d p) : Good d (frame b p) := hp

private theorem project_fixes (N : Nat) (d : Unit → Nat) (p : Nat → Nat)
    (hd : ∀ c, d c ≤ N) (hp : Good d p) : project N p = p := by
  funext n
  simp only [project]
  split
  · rfl
  · exact (hp n (by have h := hd (); omega)).symm

private theorem count_length (w : List (Unit × Unit)) : counts w () = w.length := by
  induction w with
  | nil => rfl
  | cons a w ih =>
    have ha : a.1 = () := by cases a with | mk i b => cases i; rfl
    simp [counts, bump, ha, ih]

-- Actual recurrence consumer, arbitrary word length and cutoff; not a third
-- public claim and not the analytic Hermite/Hilbert realization theorem.
example (w : List (Unit × Unit)) (N : Nat) (hN : w.length ≤ N) :
    cut (project N) insert frame vacuum w = raw insert frame vacuum w := by
  apply cut_eq_raw Good insert frame (project N) vacuum (fun _ => N)
    vacuum_good insert_good frame_good (project_fixes N) w
  intro c
  cases c
  simpa only [count_length] using hN

-- Four insertions preserve the vacuum self-contraction 3 at cutoff 4.
example : cut (project 4) insert frame vacuum [ ((),()), ((),()), ((),()), ((),()) ] 0 = 3 := by
  decide
-- An insufficient cutoff actually changes the second-order vector.
example : cut (project 1) insert frame vacuum [ ((),()), ((),()) ] 2 = 0 := by decide
example : raw insert frame vacuum [ ((),()), ((),()) ] 2 = 1 := by decide
-- Removing lowering loses the self-contraction, so creation-only is false.
example : raw insert frame vacuum [ ((),()), ((),()) ] 0 = 1 := by decide

end StratonovichHAMAudit.HermiteWordConsumer

===== END LEAN FILE: StratonovichHAMAudit/HermiteWordConsumer.lean =====

===== BEGIN LEAN FILE: StratonovichHAMAudit/InteractionDriver.lean =====
module
public import Mathlib.Tactic
public import Mathlib.Analysis.SpecialFunctions.Pow.Real
public import Mathlib.Analysis.Real.Sqrt
@[expose] public section
noncomputable section
set_option autoImplicit false
namespace StratonovichHAMAudit.InteractionDriver

def temporalH (a : ℝ) : ℝ := 1-a/2
def midpoint (H theta : ℝ) : ℝ := (H+theta)/2
def mixC (u v : ℝ) : ℝ := u*v/(u+v)
def dyadicFactor (H theta p : ℝ) : ℝ :=
  (2:ℝ)^(-(H-midpoint H theta-1/p))

theorem temporal_range (a : ℝ) (ha0 : 0 < a) (ha1 : a < 1) :
    1/2 < temporalH a ∧ temporalH a < 1 := by
  unfold temporalH
  constructor <;> linarith

theorem variance_norm (C h a L : ℝ) (hC : 0 ≤ C) (hh : 0 < h) (hL : 0 ≤ L) :
    Real.sqrt (C*h^(2-a)*L^2) = Real.sqrt C*h^(1-a/2)*L := by
  have hs : Real.sqrt (h^(2-a)) = h^(1-a/2) := by
    rw [Real.sqrt_eq_rpow, ← Real.rpow_mul hh.le]
    congr 1
    ring
  rw [Real.sqrt_mul (mul_nonneg hC (Real.rpow_nonneg hh.le _)),
    Real.sqrt_sq hL, Real.sqrt_mul hC, hs]

theorem gaussian_prefactor (P u v : ℝ) (hP : 0 < P) (hu : 0 < u) (hv : 0 < v) :
    (1/Real.sqrt P)*(1/Real.sqrt (u*v*(u+v)))*
      Real.sqrt (P/mixC u v) = 1/(u*v) := by
  have hc : 0 < mixC u v := by unfold mixC; positivity
  have hpr : 0 < Real.sqrt P := Real.sqrt_pos.2 hP
  have hdr : 0 < Real.sqrt (u*v*(u+v)) := Real.sqrt_pos.2 (by positivity)
  have hcr : 0 < Real.sqrt (mixC u v) := Real.sqrt_pos.2 hc
  have hs : Real.sqrt (u*v*(u+v))*Real.sqrt (mixC u v) = u*v := by
    rw [← Real.sqrt_mul (by positivity : (0:ℝ) ≤ u*v*(u+v))]
    have he : u*v*(u+v)*mixC u v = (u*v)^2 := by
      unfold mixC
      field_simp [(add_pos hu hv).ne']
    rw [he, Real.sqrt_sq (by positivity)]
  rw [Real.sqrt_div hP.le]
  calc
    (1/Real.sqrt P)*(1/Real.sqrt (u*v*(u+v)))*
        (Real.sqrt P/Real.sqrt (mixC u v)) =
        1/(Real.sqrt (u*v*(u+v))*Real.sqrt (mixC u v)) := by
      field_simp [hpr.ne', hdr.ne', hcr.ne']
    _ = 1/(u*v) := by rw [hs]

theorem gaussian_exponent (u v z : ℝ) (hu : 0 < u) (hv : 0 < v) :
    z^2/(4*mixC u v) = z^2/(4*u)+z^2/(4*v) := by
  unfold mixC
  field_simp [hu.ne', hv.ne', (add_pos hu hv).ne']
  ring

theorem holder_parameters (H theta p : ℝ) (htheta : 1/2 < theta)
    (hthetaH : theta < H) (hH1 : H < 1) (hp : 0 < p)
    (hcut : 2/(H-theta) < p) :
    theta < midpoint H theta ∧ midpoint H theta < H ∧
    midpoint H theta < 1 ∧ 0 < H-midpoint H theta-1/p ∧ 2 < p := by
  have hd : 0 < H-theta := by linarith
  have hb : 2 < p*(H-theta) := (div_lt_iff₀ hd).mp hcut
  have hi : (1:ℝ)/p < (H-theta)/2 := by
    apply (div_lt_iff₀ hp).2
    nlinarith
  have hpd : p*(H-theta) < p := by
    have h := mul_pos hp (show 0 < 1-(H-theta) by linarith)
    nlinarith
  unfold midpoint
  constructor
  · linarith
  constructor
  · linarith
  constructor
  · linarith
  constructor <;> linarith

theorem dyadic_ratio (H theta p : ℝ) (hmargin : 0 < H-midpoint H theta-1/p) :
    0 < dyadicFactor H theta p ∧ dyadicFactor H theta p < 1 := by
  unfold dyadicFactor
  constructor
  · exact Real.rpow_pos_of_pos (by norm_num) _
  · exact Real.rpow_lt_one_of_one_lt_of_neg (by norm_num) (by linarith)

theorem box_margin (a p : ℝ) (ha : a < 1) (hp : 0 < p)
    (hcut : 4/(1-a) < p) : 0 < (1-a)/2-2/p := by
  have h : 4 < p*(1-a) := (div_lt_iff₀ (show (0:ℝ) < 1-a by linarith)).mp hcut
  have hi : (2:ℝ)/p < (1-a)/2 := by
    apply (div_lt_iff₀ hp).2
    nlinarith
  linarith

theorem box_scale (delta a p : ℝ) (hd : 0 < delta) :
    delta^((1-a)/2)*(delta^(-(2:ℝ)))^(1/p) = delta^((1-a)/2-2/p) := by
  rw [← Real.rpow_mul hd.le, ← Real.rpow_add hd]
  congr 1
  ring

end StratonovichHAMAudit.InteractionDriver

===== END LEAN FILE: StratonovichHAMAudit/InteractionDriver.lean =====

===== BEGIN LEAN FILE: StratonovichHAMAudit/JointTilt.lean =====
module
public import Mathlib.Tactic
public import Mathlib.Analysis.SpecialFunctions.Pow.Real
@[expose] public section
noncomputable section
set_option autoImplicit false
namespace StratonovichHAMAudit.JointTilt

theorem tilt_exponent (r s c v w : ℝ) :
    -s^2*v/2+r*s*c+(r^2*w-2*r*s*c+s^2*v)/2 = r^2*w/2 := by
  ring

theorem wrong_sign_error (r s c v w : ℝ) :
    (-s^2*v/2+r*s*c+(r^2*w+2*r*s*c+s^2*v)/2)-r^2*w/2 = 2*r*s*c := by
  ring

theorem wrong_cost_error (r s c v w : ℝ) :
    (-s^2*v+r*s*c+(r^2*w-2*r*s*c+s^2*v)/2)-r^2*w/2 = -s^2*v/2 := by
  ring

theorem shifted_amplitude (delta a : ℝ) (hd : 0 < delta) :
    delta^((1-a)/2)*delta^(a/2)/Real.sqrt delta = 1 := by
  rw [← Real.rpow_add hd]
  have hsum : (1-a)/2+a/2 = (1:ℝ)/2 := by ring
  rw [hsum, ← Real.sqrt_eq_rpow]
  exact div_self (Real.sqrt_pos.2 hd).ne'

end StratonovichHAMAudit.JointTilt

===== END LEAN FILE: StratonovichHAMAudit/JointTilt.lean =====

===== BEGIN LEAN FILE: StratonovichHAMAudit/LocalFlow.lean =====
module
public import Mathlib.Tactic
public import Mathlib.Analysis.SpecialFunctions.Pow.Real
@[expose] public section
noncomputable section
set_option autoImplicit false
namespace StratonovichHAMAudit.LocalFlow

def noiseOrder (alpha : ℝ) : ℝ := (1-alpha)/2
def sourceSigma (alpha : ℝ) : ℝ := -(1+alpha)/4

theorem noise_order (alpha : ℝ) (ha0 : 0 < alpha) (ha1 : alpha ≤ 1) :
    0 ≤ noiseOrder alpha ∧ noiseOrder alpha < 1/2 ∧
    alpha-1 = -2*noiseOrder alpha := by
  unfold noiseOrder
  constructor
  · linarith
  constructor <;> linarith

theorem schur_row (q k b : ℝ) (_hq : 0 < q) (hk : 0 < k) :
    (q^(-b)*k^b)*k^(-b) = q^(-b) := by
  calc
    (q^(-b)*k^b)*k^(-b) = q^(-b)*(k^b*k^(-b)) := by ring
    _ = q^(-b) := by rw [← Real.rpow_add hk]; simp

theorem schur_column (q k b : ℝ) (hq : 0 < q) :
    (q^(-b)*k^b)*q^(-b) = k^b*q^(-2*b) := by
  calc
    (q^(-b)*k^b)*q^(-b) = k^b*(q^(-b)*q^(-b)) := by ring
    _ = k^b*q^(-2*b) := by rw [← Real.rpow_add hq]; congr 2; ring

theorem schur_rescale (k R b : ℝ) (hk : 0 < k) (hR : 0 < R) :
    (k/R)^(2*b)*R^(2*b) = k^(2*b) := by
  rw [Real.div_rpow hk.le hR.le]
  exact div_mul_cancel₀ _ (Real.rpow_pos_of_pos hR _).ne'

theorem source_overlap (alpha : ℝ) (ha : alpha < 1) :
    -(1:ℝ)/2 < sourceSigma alpha ∧ 2*sourceSigma alpha+alpha < 0 := by
  unfold sourceSigma
  constructor <;> linarith

theorem source_white_obstruction (s sigma : ℝ) (hleft : -s < sigma)
    (hright : s-1 < sigma) : ¬ sigma < -(1:ℝ)/2 := by
  intro h
  linarith

theorem source_tail_obstruction (alpha s sigma : ℝ) (hleft : -s < sigma)
    (hright : s-1 < sigma) (hHS : 2*sigma+alpha < 0) : alpha < 1 := by
  linarith

end StratonovichHAMAudit.LocalFlow

===== END LEAN FILE: StratonovichHAMAudit/LocalFlow.lean =====

===== BEGIN LEAN FILE: StratonovichHAMAudit/MiddleCross.lean =====
module
public import Mathlib.Tactic
public import Mathlib.Analysis.Real.Sqrt
@[expose] public section
noncomputable section
set_option autoImplicit false
set_option maxRecDepth 4000
namespace StratonovichHAMAudit.MiddleCross

def actual (b c : ℝ) : ℝ :=
  (2*b^2+4*b*c+2*c^2-c+1) /
    (8*b*c*(b+1)*(2*b+1)*(b+c-1)*(2*b+2*c-1))
def massK (b c : ℝ) : ℝ := 1/(4*b*c*(c+1))
def resolvent (b c r : ℝ) : ℝ :=
  (b+c+r+1)/(4*b*c*(c+1)*r*(b+c+r)*(b+r+1))
def part1 (b d e : ℝ) : ℝ :=
  (d+e+b+1)/(d*e*(b+d+1)*(b+e+1))
def part2 (b c d e : ℝ) : ℝ :=
  (d^2+d*e+e^2+(2*b+c+1)*(d+e)+(b+c)*(b+1)) /
    (d*e*(b+c+d)*(b+c+e)*(b+d+1)*(b+e+1))
def upper (b c d e : ℝ) : ℝ :=
  resolvent b c e + massK b c*(part1 b d e+part2 b c d e)/(d+e)
def denominator (b c d e : ℝ) : ℝ :=
  8*b*c*d*e*(b+1)*(2*b+1)*(c+1)*(d+e)*(b+c-1)*
    (b+c+d)*(b+c+e)*(b+d+1)*(b+e+1)*(2*b+2*c-1)
def numerator (b c d e : ℝ) : ℝ :=
  (2*b^2+4*b*c+2*c^2-c+1)*d*e*(c+1)*(d+e)*
    (b+c+d)*(b+c+e)*(b+d+1)*(b+e+1) -
  2*(b+1)*(2*b+1)*(b+c-1)*(2*b+2*c-1)*
    (d*(d+e)*(b+c+d)*(b+d+1)*(b+c+e+1) +
      (b+c+d)*(b+c+e)*(b+d+e+1) +
      (d^2+d*e+e^2+(2*b+c+1)*(d+e)+(b+c)*(b+1)))
def paramB (z : ℝ) : ℝ := (z^2-1)/(2*z)
def paramE (z : ℝ) : ℝ := (z^2+1)/(2*z)
def paramC (z t : ℝ) : ℝ := ((paramB z+1)*t-(paramB z-1)/t)/2

def paramD (z t : ℝ) : ℝ := ((paramB z+1)*t+(paramB z-1)/t)/2
def certificate (x y : ℝ) : ℝ := y * (
    (((((((((((((((((((((((((((((((((1*y + 28)*y + 354)*y + 2684)*y + 13660)*y + 49456)*y + 131576)*y + 261680)*y + 391296)*y + 437824)*y + 360448)*y + 211200)*y + 82944)*y + 19456)*y + 2048)*x +
    ((((((((((((((55*y + 1512)*y + 18784)*y + 140048)*y + 701336)*y + 2499784)*y + 6550296)*y + 12836128)*y + 18921216)*y + 20883712)*y + 16977536)*y + 9840128)*y + 3832832)*y + 894976)*y + 94208))*x +
    ((((((((((((((1417*y + 38240)*y + 466708)*y + 3420740)*y + 16850280)*y + 59105968)*y + 152480312)*y + 294286272)*y + 427406592)*y + 465044672)*y + 373023616)*y + 213625088)*y + 82394624)*y + 19107840)*y + 2004992))*x +
    ((((((((((((((22727*y + 601996)*y + 7216502)*y + 51985016)*y + 251810540)*y + 868957096)*y + 2206157400)*y + 4191612016)*y + 5994832256)*y + 6425997824)*y + 5081501440)*y + 2872175872)*y + 1095265792)*y + 251738112)*y + 26259456))*x +
    ((((((((((((((254372*y + 6612880)*y + 77851036)*y + 551065316)*y + 2624208512)*y + 8906236696)*y + 22245133008)*y + 41589271840)*y + 58542163584)*y + 61779578240)*y + 48119430272)*y + 26812359936)*y + 10093317120)*y + 2294575104)*y + 237334528))*x +
    ((((((((((((((2110780*y + 53855280)*y + 622592788)*y + 4329796972)*y + 20266599344)*y + 67631178328)*y + 166135404880)*y + 305522152480)*y + 423055944576)*y + 439223476096)*y + 336652184448)*y + 184694641408)*y + 68523174400)*y + 15375787008)*y + 1572855808))*x +
    ((((((((((((((13466068*y + 337223936)*y + 3828171644)*y + 26154845564)*y + 120320374608)*y + 394741504856)*y + 953482998160)*y + 1724232000224)*y + 2347593059776)*y + 2396275198080)*y + 1805705641344)*y + 974129734144)*y + 355575074816)*y + 78575386624)*y + 7927072768))*x +
    ((((((((((((((67589612*y + 1661570624)*y + 18523608516)*y + 124336959444)*y + 562165939360)*y + 1813157890264)*y + 4306136458192)*y + 7655958898336)*y + 10246137617600)*y + 10276941230464)*y + 7607029260928)*y + 4030198677504)*y + 1444733525504)*y + 313647800320)*y + 31109001216))*x +
    ((((((((((((((270870398*y + 6538490728)*y + 71598456224)*y + 472239475756)*y + 2098783816600)*y + 6655722050552)*y + 15543381818112)*y + 27170816846400)*y + 35740140455424)*y + 35213950681984)*y + 25587526626176)*y + 13298388480256)*y + 4673623743488)*y + 994293045248)*y + 96623300608))*x +
    ((((((((((((((874459282*y + 20734832000)*y + 223093795876)*y + 1446315012956)*y + 6320424114656)*y + 19714053281128)*y + 45287230089280)*y + 77861330975392)*y + 100688410891776)*y + 97461485555712)*y + 69506069344128)*y + 35413222757632)*y + 12185165672960)*y + 2534613507072)*y + 240487604224))*x +
    ((((((((((((((2283811966*y + 53221790528)*y + 562911296372)*y + 3588686613556)*y + 15428306862240)*y + 47358829585016)*y + 107086380369088)*y + 181209897521568)*y + 230552554699328)*y + 219395649011328)*y + 153651054921600)*y + 76761971877376)*y + 25850098629632)*y + 5250420224000)*y + 485086054400))*x +
    ((((((((((((((4826029538*y + 110603022648)*y + 1150662129008)*y + 7218434488372)*y + 30552070847320)*y + 92373485329128)*y + 205804912147392)*y + 343184440420416)*y + 430182179905600)*y + 403085090851584)*y + 277684936993664)*y + 136256033695744)*y + 44972739813888)*y + 8927197915136)*y + 802957824000))*x +
    ((((((((((((((8218851284*y + 185383193104)*y + 1898507504164)*y + 11729095321804)*y + 48920555288032)*y + 145855525618056)*y + 320644070286512)*y + 527815115807840)*y + 653253048136320)*y + 604300123774336)*y + 410791095094144)*y + 198708431823616)*y + 64552357450752)*y + 12581167542272)*y + 1106990444544))*x +
    ((((((((((((((11183782540*y + 248493175504)*y + 2507313321276)*y + 15270399802372)*y + 62837415675856)*y + 185014573044104)*y + 402062604887600)*y + 654862449522912)*y + 802621407060352)*y + 735766784662400)*y + 495884624297088)*y + 237879461960960)*y + 76630862958080)*y + 14802571648000)*y + 1289321848832))*x +
    ((((((((((((((11984649124*y + 262569628160)*y + 2612972571412)*y + 15706031299412)*y + 63852219358768)*y + 185981808058312)*y + 400409544657904)*y + 647134292910112)*y + 788337113564736)*y + 719544094696576)*y + 483747050599040)*y + 231944520802816)*y + 74848983220224)*y + 14520748802048)*y + 1274197587968))*x +
    ((((((((((((((9885272348*y + 213777126304)*y + 2100556974908)*y + 12477032327676)*y + 50192120075712)*y + 144905056192392)*y + 309848250179248)*y + 498508265259744)*y + 606106158408512)*y + 553753146532736)*y + 373877356875136)*y + 180713736328192)*y + 59050415532544)*y + 11662726320128)*y + 1048996761600))*x +
    ((((((((((((((6052923401*y + 129352117468)*y + 1256452921150)*y + 7385206406312)*y + 29445863593132)*y + 84437195815480)*y + 179798846509960)*y + 288944179278352)*y + 352126943711360)*y + 323726375768896)*y + 220911778516096)*y + 108459689971200)*y + 36202359308288)*y + 7351264885760)*y + 684966758400))*x +
    ((((((((((((((2590042735*y + 54757609368)*y + 526440369196)*y + 3066335922468)*y + 12138468731144)*y + 34646712967664)*y + 73665081916712)*y + 118637765082944)*y + 145491395759616)*y + 135213713734656)*y + 93733029452288)*y + 46991615202560)*y + 16103027874304)*y + 3375705144320)*y + 326571520000))*x +
    ((((((((((((((690952577*y + 14468003424)*y + 137841467624)*y + 796745823160)*y + 3136787863160)*y + 8930460873656)*y + 19006962914184)*y + 30767520242592)*y + 38095203501248)*y + 35912615870400)*y + 25371025696000)*y + 13020278353152)*y + 4585999234560)*y + 991683084288)*y + 99260620800))*x +
    ((((((((((((((86472015*y + 1795323740)*y + 16970868250)*y + 97478919300)*y + 382298120540)*y + 1087721023760)*y + 2322535698280)*y + 3788061992400)*y + 4746895648320)*y + 4548594982400)*y + 3279014122880)*y + 1722640193280)*y + 622624204800)*y + 138380636160)*y + 14247936000)))

theorem certificate_pos (x y : ℝ) (hx : 0 ≤ x) (hy : 0 < y) :
    0 < certificate x y := by
  unfold certificate
  positivity

set_option maxHeartbeats 2000000 in
 theorem parameter_identity (z t : ℝ) (hz : 0 < z) (ht : 0 < t) :
    numerator (paramB z) (paramC z t) (paramD z t) (paramE z) *
      (32768*t^7*z^9) = certificate (z-2) (t-1) := by
  unfold numerator paramC paramD paramE paramB certificate
  field_simp [hz.ne', ht.ne']
  ring

 theorem parameter_numerator_pos (z t : ℝ) (hz : 2 ≤ z) (ht : 1 < t) :
    0 < numerator (paramB z) (paramC z t) (paramD z t) (paramE z) := by
  have hzpos : 0 < z := by linarith
  have htpos : 0 < t := by linarith
  have hs : 0 < (32768:ℝ)*t^7*z^9 := by positivity
  have hp : 0 < numerator (paramB z) (paramC z t) (paramD z t) (paramE z) *
      (32768*t^7*z^9) := by
    rw [parameter_identity z t hzpos htpos]
    exact certificate_pos (z-2) (t-1) (by linarith) (by linarith)
  exact (mul_pos_iff_of_pos_right hs).1 hp

set_option maxHeartbeats 2000000 in
 theorem difference_identity (b c d e : ℝ) (hb : 1 ≤ b) (hc : 1 ≤ c)
    (hd : 0 < d) (he : 0 < e) :
    actual b c - upper b c d e = numerator b c d e / denominator b c d e := by
  have hb0 : 0 < b := by linarith
  have hc0 : 0 < c := by linarith
  have hbc : 0 < b+c-1 := by linarith
  have h2bc : 0 < 2*b+2*c-1 := by linarith
  have hbe : 0 < b+c+e := by positivity
  have hbd : 0 < b+c+d := by positivity
  have hb1d : 0 < b+d+1 := by positivity
  have hb1e : 0 < b+e+1 := by positivity
  have hb1 : 0 < b+1 := by positivity
  have h2b1 : 0 < 2*b+1 := by positivity
  have hc1 : 0 < c+1 := by positivity
  have hde : 0 < d+e := by positivity
  unfold actual upper resolvent massK part1 part2 numerator denominator
  field_simp (disch := first | positivity | linarith)
  ring

set_option maxHeartbeats 2000000 in
 theorem resolvent_difference (b c d e : ℝ) (hb : 1 ≤ b) (hc : 1 ≤ c)
    (hd : 0 < d) (he : 0 < e) :
    resolvent b c d - resolvent b c e =
      (e-d)*massK b c*(part1 b d e+part2 b c d e) := by
  have hb0 : 0 < b := by linarith
  have hc0 : 0 < c := by linarith
  have hbe : 0 < b+c+e := by positivity
  have hbd : 0 < b+c+d := by positivity
  have hb1d : 0 < b+d+1 := by positivity
  have hb1e : 0 < b+e+1 := by positivity
  have hc1 : 0 < c+1 := by positivity
  unfold resolvent massK part1 part2
  field_simp (disch := first | positivity | linarith)
  ring

 theorem root_numerator_pos (b c : ℝ) (hb : 1 ≤ b) (hc : 1 < c) :
    0 < numerator b c (Real.sqrt (b^2+c^2-1)) (Real.sqrt (b^2+1)) := by
  let d := Real.sqrt (b^2+c^2-1)
  let e := Real.sqrt (b^2+1)
  have hb0 : 0 < b := by linarith
  have hc0 : 0 < c := by linarith
  have hcsq : 1 < c^2 := by nlinarith [sq_nonneg (c-1)]
  have hrad : 0 < b^2+c^2-1 := by nlinarith [sq_nonneg b]
  have hd0 : 0 < d := Real.sqrt_pos.2 hrad
  have he0 : 0 < e := Real.sqrt_pos.2 (by positivity)
  have hdsq : d^2 = b^2+c^2-1 := Real.sq_sqrt hrad.le
  have hesq : e^2 = b^2+1 := Real.sq_sqrt (by positivity)
  have hegt : b < e := (sq_lt_sq₀ hb0.le he0.le).1 (by nlinarith)
  have hdge : b ≤ d := (sq_le_sq₀ hb0.le hd0.le).1 (by nlinarith)
  let z := b+e
  let t := (d+c)/(b+1)
  have hz : 2 ≤ z := by dsimp [z]; linarith
  have hz0 : 0 < z := by linarith
  have hb1 : 0 < b+1 := by positivity
  have ht : 1 < t := by
    dsimp [t]
    exact (one_lt_div hb1).2 (by linarith)
  have ht0 : 0 < t := by linarith
  have hB : paramB z = b := by
    unfold paramB
    field_simp [hz0.ne']
    dsimp [z]
    nlinarith [hesq]
  have hE : paramE z = e := by
    unfold paramE
    field_simp [hz0.ne']
    dsimp [z]
    nlinarith [hesq]
  have hmul : (b+1)*t = d+c := by
    dsimp [t]
    field_simp [hb1.ne']
  have hsubmul : (d-c)*t = b-1 := by
    dsimp [t]
    field_simp [hb1.ne']
    nlinarith [hdsq]
  have hdiv : (b-1)/t = d-c := (div_eq_iff ht0.ne').2 hsubmul.symm
  have hC : paramC z t = c := by
    unfold paramC
    rw [hB,hmul,hdiv]
    ring
  have hD : paramD z t = d := by
    unfold paramD
    rw [hB,hmul,hdiv]
    ring
  have hp := parameter_numerator_pos z t hz ht
  rw [hB,hC,hD,hE] at hp
  exact hp

 theorem middle_bound (b c : ℝ) (hb : 1 ≤ b) (hc : 1 < c) :
    upper b c (Real.sqrt (b^2+c^2-1)) (Real.sqrt (b^2+1)) < actual b c := by
  have hb0 : 0 < b := by linarith
  have hc0 : 0 < c := by linarith
  have hcsq : 1 < c^2 := by nlinarith [sq_nonneg (c-1)]
  have hd : 0 < Real.sqrt (b^2+c^2-1) := Real.sqrt_pos.2 (by nlinarith [sq_nonneg b])
  have he : 0 < Real.sqrt (b^2+1) := Real.sqrt_pos.2 (by positivity)
  have hbc : 0 < b+c-1 := by linarith
  have h2bc : 0 < 2*b+2*c-1 := by linarith
  have hden : 0 < denominator b c (Real.sqrt (b^2+c^2-1)) (Real.sqrt (b^2+1)) := by
    unfold denominator
    positivity
  have hp := root_numerator_pos b c hb hc
  have hdiff : 0 < actual b c - upper b c (Real.sqrt (b^2+c^2-1)) (Real.sqrt (b^2+1)) := by
    rw [difference_identity b c _ _ hb hc.le hd he]
    exact div_pos hp hden
  linarith

end StratonovichHAMAudit.MiddleCross
end

===== END LEAN FILE: StratonovichHAMAudit/MiddleCross.lean =====

===== BEGIN LEAN FILE: StratonovichHAMAudit/MovingCone.lean =====
module
public import Mathlib.Tactic
@[expose] public section
noncomputable section
set_option autoImplicit false
namespace StratonovichHAMAudit.MovingCone

theorem residual_budget (theta q d e : ℝ) (htheta : 0 ≤ theta)
    (hq : q ≤ 1/8) (hd0 : 0 ≤ d) (hd : d ≤ theta)
    (he : e ≤ theta/4) : q*(theta+d)+e ≤ theta/2 := by
  have hprod := mul_le_mul_of_nonneg_right hq (add_nonneg htheta hd0)
  nlinarith [hprod]

theorem cone_conversion (theta a x y rho : ℝ) (htheta : 0 ≤ theta)
    (ha : 0 < a) (hrho : rho < 1/2)
    (hx : (1-rho)*a ≤ x) (hy : y ≤ theta*a/2) :
    0 < x ∧ y ≤ theta*x := by
  have hprod : 0 < (1/2-rho)*a := mul_pos (by linarith) ha
  have hhalf : a/2 < x := by nlinarith [hprod]
  constructor
  · linarith
  · have hmul := mul_le_mul_of_nonneg_left hhalf.le htheta
    nlinarith [hmul]

theorem terminal_margin (j K theta e y : ℝ) (hj : 0 < j)
    (hbudget : 16*K*theta ≤ j) (he : e ≤ j/8)
    (hy : 3*j/4-2*K*theta-e ≤ y) : j/2 ≤ y ∧ 0 < y := by
  constructor <;> nlinarith

end StratonovichHAMAudit.MovingCone

===== END LEAN FILE: StratonovichHAMAudit/MovingCone.lean =====

===== BEGIN LEAN FILE: StratonovichHAMAudit/OccupationForm.lean =====
module
public import Mathlib.Tactic
@[expose] public section
noncomputable section
set_option autoImplicit false
namespace StratonovichHAMAudit.OccupationForm

theorem potential_budget (A D N eps : ℝ) (heps : 0 < eps) :
    A*D*N+A*N^2 ≤ eps*D^2+(A+A^2/(4*eps))*N^2 := by
  have hden : 0 < 4*eps := by positivity
  have hid : eps*D^2+(A^2/(4*eps))*N^2-A*D*N
      = (2*eps*D-A*N)^2/(4*eps) := by
    field_simp
    ring
  have hn := div_nonneg (sq_nonneg (2*eps*D-A*N)) hden.le
  nlinarith

theorem shifted_coercivity (D N P C : ℝ)
    (hbound : P ≤ D^2/2+C*N^2) :
    (D^2+N^2)/2 ≤ D^2-P+(C+1)*N^2 := by
  nlinarith [sq_nonneg N]

end StratonovichHAMAudit.OccupationForm

===== END LEAN FILE: StratonovichHAMAudit/OccupationForm.lean =====

===== BEGIN LEAN FILE: StratonovichHAMAudit/PhaseResponse.lean =====
module
public import Mathlib.Tactic
public import Mathlib.Analysis.SpecialFunctions.Pow.Real
public import Mathlib.Analysis.SpecialFunctions.Trigonometric.Basic
@[expose] public section
noncomputable section
set_option autoImplicit false
namespace StratonovichHAMAudit.PhaseResponse

def phaseIndex (alpha a : ℝ) : ℝ := 1-(alpha+a)/4

theorem rough_phase_choice (alpha a : ℝ) (hpos : 0 < alpha+a) (hsub : alpha+a < 2) :
    1/2 < phaseIndex alpha a ∧ phaseIndex alpha a < 1 ∧
    2*phaseIndex alpha a+alpha+a < 3 ∧
    2*phaseIndex alpha a+alpha+a-4 < -1 ∧ alpha+a-3 < -1 := by
  unfold phaseIndex
  constructor
  · linarith
  constructor
  · linarith
  constructor
  · linarith
  constructor <;> linarith

theorem balanced_phase (alpha a : ℝ) (hsub : alpha+a < 2) :
    2*((1:ℝ)/2)+alpha+a < 3 ∧ alpha+a-3 < -1 := by
  constructor <;> linarith

theorem energy_boundary (alpha a : ℝ) :
    2*(1:ℝ)+alpha+a < 3 ↔ alpha+a < 1 := by
  constructor <;> intro h <;> linarith

theorem four_component_gram (r1 r2 k1 k2 : ℝ) :
    (Real.sin r1*Real.cos k1)*(Real.sin r2*Real.cos k2) +
    (Real.sin r1*Real.sin k1)*(Real.sin r2*Real.sin k2) +
    (Real.cos r1*Real.cos k1)*(Real.cos r2*Real.cos k2) +
    (Real.cos r1*Real.sin k1)*(Real.cos r2*Real.sin k2) =
      Real.cos (r1-r2)*Real.cos (k1-k2) := by
  rw [Real.cos_sub, Real.cos_sub]
  ring

theorem two_frequency_average (x y : ℝ) :
    Real.cos x*Real.cos y = (Real.cos (x-y)+Real.cos (x+y))/2 := by
  rw [Real.cos_sub, Real.cos_add]
  ring

theorem frequency_window (J A B t r a : ℝ) (hA : 0 < A) (_hB : 0 ≤ B)
    (ht : 0 < t) (hr : 0 < r) (hcut : 2*B/(A*t) ≤ r)
    (herr : |J-A*t*r^(a-1)| ≤ B*r^(a-2)) :
    (A*t/2)*r^(a-1) ≤ J ∧ J ≤ (3*A*t/2)*r^(a-1) := by
  have hAt : 0 < A*t := mul_pos hA ht
  have hbudget : B ≤ A*t*r/2 := by
    have h := (div_le_iff₀ hAt).mp hcut
    nlinarith
  have hp : 0 < r^(a-1) := Real.rpow_pos_of_pos hr _
  have hexp : r^(a-2) = r^(a-1)/r := by
    have he : a-2 = (a-1)-1 := by ring
    rw [he, Real.rpow_sub_one hr.ne']
  have hscaled := mul_le_mul_of_nonneg_right hbudget hp.le
  have herror : B*r^(a-2) ≤ (A*t/2)*r^(a-1) := by
    rw [hexp, ← mul_div_assoc]
    apply (div_le_iff₀ hr).2
    nlinarith
  rcases abs_le.mp herr with ⟨hl, hu⟩
  constructor <;> nlinarith

end StratonovichHAMAudit.PhaseResponse

===== END LEAN FILE: StratonovichHAMAudit/PhaseResponse.lean =====

===== BEGIN LEAN FILE: StratonovichHAMAudit/PositiveGram.lean =====
module
public import Mathlib.Analysis.InnerProductSpace.Basic
public import Mathlib.Analysis.Real.Sqrt
public import Mathlib.Tactic
@[expose] public section
noncomputable section
set_option autoImplicit false
open scoped BigOperators
universe u v
namespace StratonovichHAMAudit.PositiveGram

theorem scalar_sqrt_dual (ell w t : ℝ) (hw : 0 < w) (ht : 0 ≤ t) :
    2 * ell * Real.sqrt t ≤ ell ^ 2 / w + w * t :=
by
  have hs : (w * Real.sqrt t) ^ 2 = w ^ 2 * t := by
    rw [mul_pow, Real.sq_sqrt ht]
  apply (mul_le_mul_iff_left₀ hw).mp
  rw [add_mul, div_mul_cancel₀ _ (ne_of_gt hw)]
  nlinarith [sq_nonneg (ell - w * Real.sqrt t)]

theorem gram_norm_square {ι : Type u} {H : Type v} [Fintype ι]
    [NormedAddCommGroup H] [InnerProductSpace ℝ H] (k : ι → H) (w : ι → ℝ) :
    ‖∑ i, w i • k i‖ ^ 2 =
      ∑ i, ∑ j, w i * inner ℝ (k i) (k j) * w j :=
by
  classical
  rw [← real_inner_self_eq_norm_sq]
  simp only [sum_inner, inner_sum, inner_smul_left, inner_smul_right]
  simp only [conj_trivial]
  apply Finset.sum_congr rfl
  intro i hi
  rw [Finset.mul_sum]
  apply Finset.sum_congr rfl
  intro j hj
  rw [real_inner_comm (k i) (k j)]
  ring

theorem active_upper_bound {ι : Type u} {H : Type v} [Fintype ι]
    [NormedAddCommGroup H] [InnerProductSpace ℝ H]
    (Phi : H) (k : ι → H) (ell b w : ι → ℝ)
    (hw : ∀ i, 0 < w i) (ht : ∀ i, 0 ≤ inner ℝ Phi (k i) - b i) :
    2 * (∑ i, ell i * Real.sqrt (inner ℝ Phi (k i) - b i)) - ‖Phi‖ ^ 2 / 2 ≤
      (∑ i, ell i ^ 2 / w i) - (∑ i, b i * w i) + ‖∑ i, w i • k i‖ ^ 2 / 2 :=
by
  classical
  let z : H := ∑ i, w i • k i
  have hs : 2 * (∑ i, ell i * Real.sqrt (inner ℝ Phi (k i) - b i)) ≤
      (∑ i, ell i ^ 2 / w i) +
        (∑ i, w i * (inner ℝ Phi (k i) - b i)) := by
    calc
      _ = ∑ i, 2 * ell i * Real.sqrt (inner ℝ Phi (k i) - b i) := by
        rw [Finset.mul_sum]
        congr 1
        funext i
        ring
      _ ≤ ∑ i, (ell i ^ 2 / w i + w i * (inner ℝ Phi (k i) - b i)) :=
        Finset.sum_le_sum (fun i hi => scalar_sqrt_dual _ _ _ (hw i) (ht i))
      _ = _ := Finset.sum_add_distrib
  have hz : (∑ i, w i * (inner ℝ Phi (k i) - b i)) =
      inner ℝ Phi z - ∑ i, b i * w i := by
    simp only [z, inner_sum, inner_smul_right, mul_sub, Finset.sum_sub_distrib]
    congr 1
    apply Finset.sum_congr rfl
    intro i hi
    ring
  have hn := norm_sub_sq_real Phi z
  have hnon := sq_nonneg ‖Phi - z‖
  rw [hz] at hs
  dsimp [z] at hn hnon hs
  nlinarith

theorem half_weighted_entrywise_mono {ι : Type u} [Fintype ι]
    (C D : ι → ι → ℝ) (w : ι → ℝ)
    (hw : ∀ i, 0 ≤ w i) (hCD : ∀ i j, C i j ≤ D i j) :
    (1 / 2 : ℝ) * (∑ i, ∑ j, w i * C i j * w j) ≤
      (1 / 2 : ℝ) * (∑ i, ∑ j, w i * D i j * w j) :=
by
  classical
  apply mul_le_mul_of_nonneg_left _ (by norm_num)
  apply Finset.sum_le_sum
  intro i hi
  apply Finset.sum_le_sum
  intro j hj
  exact mul_le_mul_of_nonneg_right
    (mul_le_mul_of_nonneg_left (hCD i j) (hw i)) (hw j)

end StratonovichHAMAudit.PositiveGram

===== END LEAN FILE: StratonovichHAMAudit/PositiveGram.lean =====

===== BEGIN LEAN FILE: StratonovichHAMAudit/ProjectionResidual.lean =====
module
public import Mathlib.Tactic
public import Mathlib.Analysis.Real.Sqrt
@[expose] public section
noncomputable section
set_option autoImplicit false
namespace StratonovichHAMAudit.ProjectionResidual

def actualMeanCoeff : ℝ := 20000 / 1932951
def projectedLower : ℝ := 101 / (3200 * Real.sqrt 2)

theorem projection_gap : actualMeanCoeff + 1/96 < projectedLower := by
  have hs : 0 < Real.sqrt (2:ℝ) := Real.sqrt_pos.2 (by norm_num)
  have hs2 := Real.sq_sqrt (show (0:ℝ) ≤ 2 by norm_num)
  have hslt : Real.sqrt (2:ℝ) < 3/2 := by nlinarith
  have hp : (1:ℝ)/48 < projectedLower := by
    unfold projectedLower
    apply (lt_div_iff₀ (show (0:ℝ) < 3200 * Real.sqrt 2 by positivity)).2
    nlinarith
  have ha : actualMeanCoeff < (1:ℝ)/96 := by norm_num [actualMeanCoeff]
  linarith

theorem tilted_gap (p q : ℝ) (hp : projectedLower ≤ p) :
    actualMeanCoeff + (q-1)*p + 1/96 < q*p := by
  have h := projection_gap
  nlinarith

end StratonovichHAMAudit.ProjectionResidual

===== END LEAN FILE: StratonovichHAMAudit/ProjectionResidual.lean =====

===== BEGIN LEAN FILE: StratonovichHAMAudit/RawValueCeiling.lean =====
module
public import Mathlib.Tactic
public import Mathlib.Analysis.SpecialFunctions.Log.NegMulLog
@[expose] public section
noncomputable section
set_option autoImplicit false
namespace StratonovichHAMAudit.RawValueCeiling

theorem exact_gap : (2:ℕ)*30^60 < 39^39*21^21 := by
  norm_num

theorem strict_log_gap (q a : ℝ) (ha : 0 < a) (hpos : 0 < q-2*a) :
    0 < (q*Real.log q+(q-2*a)*Real.log (q-2*a))/2
          -(q-a)*Real.log (q-a) := by
  have hq : 0 ≤ q := by linarith
  have hne : q ≠ q-2*a := by linarith
  have hc := Real.strictConvexOn_mul_log.2
  have h := hc hq hpos.le hne
    (show 0 < (1:ℝ)/2 by norm_num)
    (show 0 < (1:ℝ)/2 by norm_num)
    (show (1:ℝ)/2+(1:ℝ)/2=1 by norm_num)
  simp only [smul_eq_mul] at h
  have hm : (1:ℝ)/2*q+(1:ℝ)/2*(q-2*a)=q-a := by ring
  rw [hm] at h
  linarith

end StratonovichHAMAudit.RawValueCeiling

===== END LEAN FILE: StratonovichHAMAudit/RawValueCeiling.lean =====

===== BEGIN LEAN FILE: StratonovichHAMAudit/RawVariational.lean =====
module
public import Mathlib.Tactic
public import Mathlib.Analysis.SpecialFunctions.Pow.Real
@[expose] public section
noncomputable section
set_option autoImplicit false
namespace StratonovichHAMAudit.RawVariational

theorem dilation_factors (s alpha : ℝ) (hs : 0 < s) :
    s^(3-alpha)*s^(alpha-1)=s^2 ∧
    s^(3-alpha)*s^2/s=s^(4-alpha) := by
  constructor
  · have hsum : (3-alpha)+(alpha-1)=(2:ℝ) := by ring
    rw [← Real.rpow_add hs, hsum, Real.rpow_two]
  · calc
      s^(3-alpha)*s^2/s = s^((3-alpha)+(2:ℝ))/s := by
        rw [Real.rpow_add hs, Real.rpow_two]
      _ = s^(((3-alpha)+(2:ℝ))-(1:ℝ)) := by
        rw [Real.rpow_sub hs, Real.rpow_one]
      _ = s^(4-alpha) := by congr 1; ring

theorem label_score (c I v alpha : ℝ) (hc : 0 < c) (ha : alpha < 3) :
    c*(c^(1/(3-alpha))*I)-(c^(1/(3-alpha)))^(4-alpha)*v/2
      =c^((4-alpha)/(3-alpha))*(I-v/2) := by
  have hk : 3-alpha ≠ 0 := ne_of_gt (by linarith)
  have hsum : (1:ℝ)+1/(3-alpha)=(4-alpha)/(3-alpha) := by
    field_simp [hk]
    ring
  have hprod : (1/(3-alpha))*(4-alpha)=(4-alpha)/(3-alpha) := by ring
  have hmul : c*c^(1/(3-alpha))=c^((4-alpha)/(3-alpha)) := by
    calc
      c*c^(1/(3-alpha))=c^(1:ℝ)*c^(1/(3-alpha)) := by rw [Real.rpow_one]
      _ = c^((1:ℝ)+1/(3-alpha)) := (Real.rpow_add hc _ _).symm
      _ = c^((4-alpha)/(3-alpha)) := by rw [hsum]
  have hpow : (c^(1/(3-alpha)))^(4-alpha)=c^((4-alpha)/(3-alpha)) := by
    rw [← Real.rpow_mul hc.le, hprod]
  rw [← mul_assoc, hmul, hpow]
  ring

theorem positive_score (I v alpha : ℝ) (hI : 0 < I) (hv : 0 < v)
    (ha : alpha < 3) :
    0 < (I/v)^(1/(3-alpha))*I-((I/v)^(1/(3-alpha)))^(4-alpha)*v/2 := by
  let c : ℝ := I/v
  have hc : 0 < c := div_pos hI hv
  have hk : 3-alpha ≠ 0 := ne_of_gt (by linarith)
  have hsum : (1/(3-alpha))*(4-alpha)=1/(3-alpha)+(1:ℝ) := by
    field_simp [hk]
    ring
  have hpow : (c^(1/(3-alpha)))^(4-alpha)=c^(1/(3-alpha))*c := by
    rw [← Real.rpow_mul hc.le, hsum, Real.rpow_add hc, Real.rpow_one]
  have hcv : c*v=I := by
    dsimp [c]
    field_simp [ne_of_gt hv]
  have heq : c^(1/(3-alpha))*I-(c^(1/(3-alpha)))^(4-alpha)*v/2
      =c^(1/(3-alpha))*I/2 := by
    calc
      c^(1/(3-alpha))*I-(c^(1/(3-alpha)))^(4-alpha)*v/2
        =c^(1/(3-alpha))*I-c^(1/(3-alpha))*(c*v)/2 := by rw [hpow]; ring
      _ = c^(1/(3-alpha))*I/2 := by rw [hcv]; ring
  change 0 < c^(1/(3-alpha))*I-(c^(1/(3-alpha)))^(4-alpha)*v/2
  rw [heq]
  exact div_pos (mul_pos (Real.rpow_pos_of_pos hc _) hI) (by norm_num)

theorem strict_label_factor (alpha : ℝ) (ha : alpha < 3) :
    (2:ℝ) < (2:ℝ)^((4-alpha)/(3-alpha)) := by
  have hk : 0 < 3-alpha := by linarith
  have hm : (1:ℝ) < (4-alpha)/(3-alpha) := by
    apply (lt_div_iff₀ hk).2
    linarith
  have h := Real.rpow_lt_rpow_of_exponent_lt (x := (2:ℝ)) (by norm_num) hm
  simpa only [Real.rpow_one] using h

end StratonovichHAMAudit.RawVariational

===== END LEAN FILE: StratonovichHAMAudit/RawVariational.lean =====

===== BEGIN LEAN FILE: StratonovichHAMAudit/TerminalCross.lean =====
module

public import Mathlib.Tactic
public import Mathlib.Analysis.Convex.SpecificFunctions.Basic

@[expose] public section

set_option autoImplicit false

namespace StratonovichHAMAudit.TerminalCross

def numP (c : ℝ) : ℝ := c ^ 2 + c + 1
def numN (b c : ℝ) : ℝ := b * numP c + c ^ 3 + c + 1

def polynomial (b c : ℝ) : ℝ :=
  (c + 1) ^ 2 * ((c ^ 2 + 1) * b ^ 2 + c ^ 2 - 1) * numN b c ^ 2 -
    4 * (c ^ 2 + 1) * numP c ^ 2 * (b + c - 1) ^ 2 * (b + 1) ^ 2

def certificate (x y : ℝ) : ℝ := y * (
  x ^ 4 * (y ^ 7 + 12*y ^ 6 + 61*y ^ 5 + 176*y ^ 4 + 315*y ^ 3 +
    354*y ^ 2 + 234*y + 72) +
  x ^ 3 * (2*y ^ 8 + 28*y ^ 7 + 172*y ^ 6 + 612*y ^ 5 + 1394*y ^ 4 +
    2098*y ^ 3 + 2056*y ^ 2 + 1212*y + 336) +
  x ^ 2 * (y ^ 9 + 18*y ^ 8 + 142*y ^ 7 + 640*y ^ 6 + 1841*y ^ 5 +
    3546*y ^ 4 + 4618*y ^ 3 + 3952*y ^ 2 + 2030*y + 480) +
  x * (2*y ^ 9 + 32*y ^ 8 + 220*y ^ 7 + 868*y ^ 6 + 2194*y ^ 5 +
    3712*y ^ 4 + 4224*y ^ 3 + 3116*y ^ 2 + 1336*y + 240) +
  (2*y ^ 9 + 28*y ^ 8 + 166*y ^ 7 + 568*y ^ 6 + 1254*y ^ 5 +
    1868*y ^ 4 + 1890*y ^ 3 + 1264*y ^ 2 + 512*y + 96))

theorem polynomial_identity (b c : ℝ) :
    polynomial b c = certificate (b - 1) (c - 1) := by
  unfold polynomial certificate numN numP
  ring

theorem polynomial_pos (b c : ℝ) (hb : 1 ≤ b) (hc : 1 < c) :
    0 < polynomial b c := by
  rw [polynomial_identity]
  have hx : 0 ≤ b - 1 := by linarith
  have hy : 0 < c - 1 := by linarith
  unfold certificate
  positivity

theorem rate_le (A s : ℝ) (hA : 0 < A) (hs : (1 : ℝ)/2 ≤ s) :
    A / (2 * (A + 1)) ≤ s * A / (A + 2 * s) := by
  have hD : 0 < A + 2*s := by linarith
  apply (div_le_div_iff₀ (by positivity) hD).2
  have h : 0 ≤ A ^ 2 * (2*s - 1) := mul_nonneg (sq_nonneg A) (by linarith)
  nlinarith

theorem exponential_difference (C D r R k w : ℝ) (hD : 0 ≤ D) (hCD : D < C)
    (hmix : (C - D) * k = C * r - D * R) :
    C * Real.exp (-r*w) - D * Real.exp (-R*w) ≤
      (C - D) * Real.exp (-k*w) := by
  have hC : 0 < C := by linarith
  have ha : 0 ≤ (C-D)/C := div_nonneg (by linarith) hC.le
  have hb : 0 ≤ D/C := div_nonneg hD hC.le
  have hab : (C-D)/C + D/C = 1 := by field_simp [hC.ne']; ring
  have hcombo : (C-D)/C * (-k*w) + D/C * (-R*w) = -r*w := by
    field_simp [hC.ne']
    linear_combination -w * hmix
  have hconv := convexOn_exp.2 (Set.mem_univ (-k*w)) (Set.mem_univ (-R*w)) ha hb hab
  simp only [smul_eq_mul, hcombo] at hconv
  have hscaled := mul_le_mul_of_nonneg_left hconv hC.le
  have hnorm : C * ((C-D)/C * Real.exp (-k*w) + D/C * Real.exp (-R*w)) =
      (C-D)*Real.exp (-k*w) + D*Real.exp (-R*w) := by
    field_simp [hC.ne']
  rw [hnorm] at hscaled
  linarith

theorem terminal_bound (b c : ℝ) (hb : 1 ≤ b) (hc : 1 < c) :
    numP c / (16*c ^ 3*(c+1)*Real.sqrt (b ^ 2+(c ^ 2-1)/(c ^ 2+1))) <
      numN b c / (32*c ^ 3*(b+c-1)*(b+1)) := by
  have hbpos : 0 < b := by linarith
  have hcpos : 0 < c := by linarith
  have hc2 : 0 < c ^ 2 + 1 := by positivity
  have hnum : 0 ≤ c ^ 2 - 1 := by nlinarith
  let rad : ℝ := b ^ 2 + (c ^ 2 - 1)/(c ^ 2 + 1)
  have hrad : 0 < rad := by
    dsimp [rad]
    exact add_pos_of_pos_of_nonneg (sq_pos_of_pos hbpos) (div_nonneg hnum hc2.le)
  have hsqrt : 0 < Real.sqrt rad := Real.sqrt_pos.2 hrad
  let U : ℝ := 2 * numP c * (b+c-1) * (b+1)
  let V : ℝ := (c+1) * numN b c
  have hbc : 0 < b+c-1 := by linarith
  have hU : 0 < U := by dsimp [U, numP]; positivity
  have hV : 0 < V := by dsimp [V, numN, numP]; positivity
  have hradid : (c ^ 2+1)*rad = (c ^ 2+1)*b ^ 2+c ^ 2-1 := by
    dsimp [rad]
    field_simp [hc2.ne']
    ring
  have hid : (c ^ 2+1)*((V*Real.sqrt rad) ^ 2-U ^ 2) = polynomial b c := by
    calc
      _ = V ^ 2*((c ^ 2+1)*rad)-(c ^ 2+1)*U ^ 2 := by
        rw [mul_pow, Real.sq_sqrt hrad.le]
        ring
      _ = polynomial b c := by
        rw [hradid]
        dsimp [V, U, polynomial]
        ring
  have hprod : 0 < (c ^ 2+1)*((V*Real.sqrt rad) ^ 2-U ^ 2) := by
    rw [hid]
    exact polynomial_pos b c hb hc
  have hinner : 0 < (V*Real.sqrt rad) ^ 2-U ^ 2 :=
    (mul_pos_iff_of_pos_left hc2).1 hprod
  have hsq : U ^ 2 < (V*Real.sqrt rad) ^ 2 := by linarith
  have huv : U < V*Real.sqrt rad :=
    (sq_lt_sq₀ hU.le (mul_pos hV hsqrt).le).1 hsq
  apply (div_lt_div_iff₀ (by positivity) (by positivity)).2
  have hclear := mul_lt_mul_of_pos_left huv (show 0 < 16*c ^ 3 by positivity)
  convert hclear using 1 <;> dsimp [U, V, rad] <;> ring

end StratonovichHAMAudit.TerminalCross

===== END LEAN FILE: StratonovichHAMAudit/TerminalCross.lean =====

===== BEGIN LEAN FILE: StratonovichHAMAudit/WhiteCDF.lean =====
module
public import Mathlib.Tactic
@[expose] public section
noncomputable section
set_option autoImplicit false
namespace StratonovichHAMAudit.WhiteCDF

theorem cdf_square_bound (A b : ℝ)
    (h : ∀ z : ℝ, 0 ≤ b - 2 * z * A + z ^ 2 / 3) :
    3 * A ^ 2 ≤ b :=
by
  have hz := h (3 * A)
  nlinarith

theorem energy_upper (c A b : ℝ) (h : 3 * A ^ 2 ≤ b) :
    c * A - b / 2 ≤ c ^ 2 / 6 :=
by
  nlinarith [sq_nonneg (c - 3 * A)]

end StratonovichHAMAudit.WhiteCDF

===== END LEAN FILE: StratonovichHAMAudit/WhiteCDF.lean =====

===== BEGIN TEX FILE: notes/notes_stratonovich_ham_second_moment.tex =====
\documentclass[12pt]{article}

% === amsrefs bibliography setup ===
\usepackage{amsrefs}
\BibSpec{article}{%
+{}{\PrintAuthors}                {author}
+{,}{ \textit}                    {title}
+{.}{ }                           {part}
+{:}{ }                           {subtitle}
+{,}{ \PrintContributions}        {contribution}
+{.}{ \PrintPartials}             {partial}
+{,}{ }                           {journal}
+{}{ \textbf}                     {volume}
+{}{ \parenthesize}               {date}
+{,}{ }                           {pages}
+{,}{ }                           {status}
+{,}{ \PrintDOI}                  {doi}
+{.}{ Available at \eprint}       {eprint}
+{}{}                             {transition}
+{;}{ \PrintReviews}              {review}
+{.}{ }                           {note}
}

% === Core packages ===
\usepackage{amsmath, amsfonts, amssymb, amsthm}
\usepackage{enumerate}
\usepackage{mathrsfs}
\usepackage{xcolor}
\usepackage[colorlinks=true]{hyperref}
\usepackage{framed}
\usepackage{url}
\setlength{\emergencystretch}{3em}

% === Page geometry ===
\setlength{\textwidth}{6.2in}
\setlength{\oddsidemargin}{0.1in}
\setlength{\evensidemargin}{0.1in}
\setlength{\textheight}{8.8in}
\setlength{\topmargin}{0in}

% === Equation numbering ===
\numberwithin{equation}{section}

% === Theorem environments (shared counter) ===
\newtheorem{theorem}{Theorem}[section]
\newtheorem{lemma}[theorem]{Lemma}
\newtheorem{proposition}[theorem]{Proposition}
\newtheorem{corollary}[theorem]{Corollary}
\newtheorem{conjecture}[theorem]{Conjecture}
\theoremstyle{definition}
\newtheorem{definition}[theorem]{Definition}
\newtheorem{hypothesis}[theorem]{Hypothesis}
\newtheorem{remark}[theorem]{Remark}
\newtheorem{goal}[theorem]{Goal}

% === Standard macros ===
\newcommand{\R}{\mathbb{R}}
\newcommand{\N}{\mathbb{N}}
\newcommand{\E}{\mathbb{E}}
\newcommand{\W}{\dot W}
\newcommand{\ud}{\,\mathrm{d}}
\newcommand{\cE}{\mathcal{E}}
\newcommand{\myCmts}[1]{\begin{framed}\noindent\textcolor{red}{#1}\end{framed}}

\begin{document}

\title{The second moment of the hyperbolic Anderson model with time-dependent
noise: Stratonovich regime}
\author{Le Chen}
\date{\today}
\maketitle

[held back until the source author has been told]

\tableofcontents

\section{Model and standing assumptions}\label{S:model}

We study the hyperbolic Anderson model
\cite{chen:author2026:time-dependency}*{(1.1)}
\begin{equation}\label{E:HAM}
  \frac{\partial^2 u}{\partial t^2}(t,x)=\Delta u(t,x)+\W(t,x)u(t,x),
  \qquad u(0,x)=1,\quad \frac{\partial u}{\partial t}(0,x)=0,
\end{equation}
for $(t,x)\in\R_+\times\R^d$, $d\in\{1,2,3\}$, interpreted in the
Stratonovich sense (limit of classical wave equations driven by smoothed
noises $\W_{\epsilon,\delta}$). The noise is centered Gaussian with
\begin{equation}\label{E:cov}
  \operatorname{Cov}\big(\W(s,x),\W(t,y)\big)=|s-t|^{-\alpha_0}\gamma(x-y),
  \qquad 0<\alpha_0<1,
\end{equation}
where $\gamma\ge0$ is nonnegative definite with spectral measure $\mu$.

\begin{hypothesis}[Homogeneous covariance]\label{H:homog}
  Let $d\in\{1,2,3\}$ and $0<\alpha_0<1$.
  The spatial covariance is a nonnegative, even, positive-definite
  tempered Radon measure $\Gamma$ on $\R^d$, with positive even
  tempered Radon spectral measure $\mu$ in the convention
  \[
    \Gamma=\int e^{i\xi\cdot x}\mu(\ud\xi)
    \quad\text{in the sense of tempered distributions}.
  \]
  The symbol $\gamma$ in~\eqref{E:cov} denotes this covariance as a
  function when one exists, and as a distribution otherwise.
  For every Borel set $A$ and $c>0$,
  $\Gamma(cA)=c^{d-\alpha}\Gamma(A)$, and
  \begin{equation}\label{E:threshold}
    \alpha_0+\alpha<2,
  \end{equation}
  with $0<\alpha<d$, or $\alpha=d=1$.
  In particular, the last case includes spatial white noise
  $\Gamma=\delta_0$.
\end{hypothesis}

Throughout we write
\begin{equation}\label{E:kappa}
  \kappa:=\frac{4-\alpha-\alpha_0}{3-\alpha}\in(1,2).
\end{equation}

\paragraph{Contribution of the present work.}
We address the second moment of the original Stratonovich solution with
fractional temporal covariance throughout Hypothesis~\ref{H:homog}.
The independent upper bound reaches the scale $t^\kappa$, rather than
only the coarse quadratic exponential scale in the source.
The main identification gives an intrinsic variational expression for
the limiting constant over all nonnegative smooth compact spacetime
controls, without a separability restriction. It retains the covariance
amplitude, kinetic coefficient one and Gaussian half-action, and includes
the zero covariance case. The upper and lower comparisons refer to the
same canonical solution. The occupation and spatial-energy estimates
then give bounds on this constant; evaluating the white spatial energy
is not a numerical evaluation of the full moment supremum.
The earlier results discussed below concern different stochastic
interpretations or temporal covariances and do not supply this
identification by substitution.

\paragraph{Main result and dependencies.}
Theorem~\ref{T:intrinsic-second-moment} identifies the original point-moment
limit for every covariance in Hypothesis~\ref{H:homog}.
Its full variational domain and normalization are displayed in
\eqref{E:intrinsic-positive-formula}.
Theorem~\ref{T:intrinsic-occupation-ceiling} and
Corollary~\ref{C:intrinsic-spatial-bracket} give derived bounds;
Section~\ref{S:intrinsic-white-evaluation} evaluates the white spatial
energy and its resulting moment bounds.
These bounds need not be attained at the moment constant.

The independent earlier Theorem~\ref{T:full-upper} establishes finite
upper growth at scale $t^\kappa$ and precedes its uses proving
variational finiteness. It uses the fixed-order
construction proved in Lemma~\ref{L:joint-fixed-order}, the Gaussian
and complex phase estimates in Sections~\ref{S:static-phase}--\ref{S:static-all-orders},
and the interval coefficient and inventory estimates in
Section~\ref{S:interval-upper}. It does not use the alternative covariance
interpolation arguments in Sections~\ref{S:higher-alpha}--\ref{S:energy-fidelity}
as inputs. Its uniform geometric tail is proved here from scaled finite-model
moments; the older mixed-series and crude estimates in
Section~\ref{S:G0} are not needed for that moment-limit passage.
The separate verification of the mild equation is proved in
Proposition~\ref{P:mild-construction}, using the corrected
vertexwise bound of Lemma~\ref{L:vertex-crude}. The alternative
arguments are retained to record their separate hypotheses
and limitations. Section~\ref{S:d1-upper} also gives explicit constants for
$\alpha\le1$; the full-class theorem asserts a finite uniform constant,
without giving a numerically optimized value.
The later proof constructs the actual operator and its retaining sources
in Sections~\ref{S:actual-operator-driver}--\ref{S:constant-phase-young},
then proves the same-solution lower bound and positive-control scores
in Sections~\ref{S:actual-raw-block-lower}--\ref{S:unmasked-variational}.
The actual Gaussian upper argument culminates in
Sections~\ref{S:original-point-transfer}--\ref{S:original-signed-score-upper}.
Finite Gram optimization and its physical application then match the
upper and lower values in Section~\ref{S:intrinsic-second-moment}.
This dependency order does not use that final identification to prove
its own finiteness.

\paragraph{Notation and source-dependent statements.}
The target spatial degree is $\alpha$, whereas $\chi$ denotes the degree
of an auxiliary static covariance in
Sections~\ref{S:static-holder}--\ref{S:energy-fidelity}.
The coefficient power is $\beta=4-\alpha-\alpha_0$; the factorial power in
Section~\ref{S:interval-upper} is $\nu=3-\alpha$.
The local exponent $b=2-\alpha$ in Section~\ref{S:d1-upper} is different
from coordinate powers $b_j$ in Section~\ref{S:three-endpoints}.
In Section~\ref{S:higher-alpha}, $\delta=\alpha-1$ is an exponent;
when used for temporal noise smoothing, $\delta$ is a cutoff width.
The covariance measure $\Gamma(\ud x)$ and the Euler Gamma function
$\Gamma(q)$ are distinguished by their arguments. The local
$p=2-\alpha_0$ in Section~\ref{S:interval-upper} is an inventory-decay
exponent; it is not the moment order $p$ in Conjecture~\ref{Conj:allp}.
The unconditional first-to-second moment comparison is
Proposition~\ref{P:Jensen}. Any numerical consequence involving the
source's $L_*$ explicitly assumes a valid first-moment lower bound with
that constant. No correction of its printed normalization is adopted.
When a radius is given for topological support, the closed ball is meant
unless a strict open inclusion is specified. In particular the spatial
cutoffs have support in $\overline B_{2R}$ and the wave Green measures
have support in $\overline B_t$, including the sphere measure in dimension
three. Plateau and causal-cone arguments retain their strict margins.

\paragraph{Which source statements are inputs.}
The moment estimate uses the bounded-operator Crouzeix--Palencia
theorem in~\eqref{E:cp-input}. The fixed-order construction is supplied
here by Lemmas~\ref{L:spatial-wick-measures}--\ref{L:joint-fixed-order},
using Lemma~\ref{L:pairing-product-envelope}, which proves the finite
product envelope used here, and the direct norm bounds in Lemma~\ref{L:damped-homogeneous-norms}.
The Case~2 covariance step is proved independently in
Lemma~\ref{L:translated-covariance-CS}; the precise source-display
qualifications and regularized application are in
Remark~\ref{R:source-case2-time-shift}.
Thus neither Theorem~4.1 nor Lemma~4.4 nor Appendix~A.1 of the source is
an analytic construction input. The finite-width Gaussian field and
multiple Stratonovich integral use its definitions and regularization
conventions, with Green smoothing removed before noise smoothing.

Proposition~\ref{P:mild-construction} proves that the resulting series
satisfies its onefold Stratonovich mild equation, using the corrected
vertexwise bound. It does not import the author's Section~5(ii) argument
or (5.3)--(5.4). No uniqueness assertion is made. The uniform tail passage
for the target-scale moment estimate is proved in
Lemma~\ref{L:uniform-series-tail}, independently of the crude bound and
the source's series estimate. The mixed-width and order-limit passages
for the mild equation are supplied here as well.

The first-moment formulas in Theorem~\ref{T:first} are quoted source
statements, with the printed-normalization qualification there; they are
not premises of the full upper theorem. Chen--Hu's static coefficient
estimates and Chen's 2023 variational finiteness theorem are used only in
the explicitly identified auxiliary sections. In particular, our uses of
the latter cite Theorem~1.1, not Corollary~1.2. Thus neither a disputed
first-moment constant nor an auxiliary static coefficient theorem enters
the interval-field upper bound.

\section{What is known}\label{S:known}

Pinpoints to Xia Chen's time-dependent Stratonovich paper refer to the
current author version~\cite{chen:author2026:time-dependency} (64 pages, ``Submitted to the Annals
of Applied Probability'', SHA-256 \texttt{5f7385ca\dots}); see
\path{sources/SOURCE-MANIFEST.md}. arXiv:2510.01412v1
\cite{chen:25:time-dependency} differs in Theorem~1.2 and must not be used as
the authority for it.

\subsection{Earlier moment results and the present setting}\label{S:literature-context}

For the stochastic wave equation driven by space-time white noise,
Chen--Dalang~\cite{chen.dalang:15:moment}*{Theorem~2.3 and Corollary~1.1}
derive moment bounds and explicit second-moment formulas, including
rough initial data. Their random-field construction uses the
It\^o--Walsh integral. Chen--Guo--Song~\cite{chen.guo.ea:24:moments}*{Theorem~1.1}
extend moment analysis to a fractional SPDE family with space-time white
noise. Besides exact second moments and their Lyapunov exponents, their
wave specialization gives matching upper and lower $p^{3/2}$
moment-growth orders~\cite{chen.guo.ea:24:moments}*{Proposition~5.10;
(1.10)--(1.11), pp.~4257--4258}.
The higher-moment constants in that comparison are not optimal; these
bounds do not assert an exact higher-moment leading constant or the
existence of a general higher-moment limit.

With time-independent Gaussian noise, Balan--Le Chen--Xia
Chen~\cite{balan.chen.ea:22:exact}*{Theorem~1.6}
obtain exact large-time and high-moment asymptotics for the Skorohod
wave equation, with a variational constant, for their homogeneous covariances in
dimensions at most three and spatial white noise in dimensions one and two.
This is a close predecessor for sharp hyperbolic moment asymptotics.
Chen--Eisenberg~\cite{chen.eisenberg:23:interpolating}*{Theorems~1.6--1.7}
develop solvability and exact moment asymptotics for fractional equations
with time-independent noise in the Skorohod sense. Fractional time
differentiation in that family is distinct from temporal correlation
of the noise; its fractional time order lies strictly below two.
For fractional temporal noise, the Skorohod moment bounds of
Balan--Conus~\cite{balan.conus:16:intermittency} provide a further
comparison under their respective covariance assumptions.
Hu--Wang~\cite{hu.wang:24:matching}*{Theorem~3.7}
obtain matching moment-growth bounds under their covariance and
Green-kernel hypotheses; matching growth orders do not by themselves
identify a sharp leading constant.

On the Stratonovich side, Balan~\cite{balan:22:stratonovich}
constructs the time-independent-noise solution in dimensions one and two
under a spectral condition stronger than Dalang's condition.
Xia Chen--Hu~\cite{chen.hu:25:hyperbolic} establish homogeneous
moment asymptotics for the static Stratonovich model.
The Strichartz construction of Xia Chen--Deya--Song--Tindel
in dimensions one and two~\cite{chen.deya.ea:23:hyperbolic}
is another Stratonovich well-posedness approach under its own noise
and data hypotheses. Xia Chen's author-version result for fractional
temporal noise~\cite{chen:author2026:time-dependency}*{Theorem~1.2}
gives two-sided first-moment bounds, with an exact limit predicted
rather than proved there. Its Remark~5.1 supplies the coarse
second-moment upper bound. These are the direct context for the present
second-moment problem.

The distinction between interpretations matters to the argument.
The Skorohod chaos expansion is orthogonal across orders, whereas the
Stratonovich moment expansion retains self-pairings and unequal-order
cross terms. The results above are therefore literature comparisons,
not a transfer of their solutions or sharp constants to this problem.
We derive the actual constant from the present model rather than
prescribe a conjectured endpoint or identify an auxiliary label-one
score with an established first-moment limit.

[held back: collaborators' unpublished work]

\subsection{Stratonovich expansion and moments}

The solution is the Stratonovich expansion
\cite{chen:author2026:time-dependency}*{(2.13)--(2.16)}
\begin{equation}\label{E:expansion}
  \begin{split}
    u(t,x)&=\sum_{n=0}^\infty S_n\big(g_n(\cdot,t,x)\big),\\
    g_n(s_1,\dots,s_n,x_1,\dots,x_n,t,x)
    &=\Big(\prod_{l=1}^nG(s_{l+1}-s_l,x_{l+1}-x_l)\Big)
    \mathbf 1_{[0,t]^n_<}(s_1,\dots,s_n),
  \end{split}
\end{equation}
with $s_{n+1}=t$, $x_{n+1}=x$, $G$ the fundamental solution of the wave
equation, and $[0,t]^n_<=\{0<s_1<\dots<s_n<t\}$. Odd expected Stratonovich
integrals vanish and even ones are given by Wick's formula
\cite{chen:author2026:time-dependency}*{(2.19)--(2.21)}, a sum over pair
partitions $\mathcal D\in\Pi_n$ of $\{1,\dots,2n\}$ that includes
self-pairings within one chain. The second moment of one ordered term is
the two-chain pairing integral, stated in
\cite{chen:author2026:time-dependency}*{Theorem~4.1, (4.3)} and proved
here under Hypothesis~\ref{H:homog} in Proposition~\ref{P:mixed}:
\begin{equation}\label{E:Sn2}
  \begin{split}
    \E\big[S_n(g_n(\cdot,t,x))^2\big]
    &=\sum_{\mathcal D\in\Pi_n}\int_{[0,t]^n_<\times[0,t]^n_<}\ud s
    \int_{(\R^d)^n\times(\R^d)^n}\ud x
    \Big(\prod_{\rho=1}^2\prod_{l\in I_\rho}
    G(s_l-s_{p(l)},x_l-x_{p(l)})\Big)\\
    &\qquad\times\prod_{(j,k)\in\mathcal D}|s_j-s_k|^{-\alpha_0}\gamma(x_j-x_k),
  \end{split}
\end{equation}
with $I_1=\{1,\dots,n\}$ and $I_2=\{n+1,\dots,2n\}$.
Here $p(l)$ is the preceding label in its own chain; at the first vertex
of either chain use the common root $(s_{p(l)},x_{p(l)})=(0,0)$.
Thus, the second chain does not continue the first one. This spells out
the source's conventions in Theorem~4.1.

The full mixed-term expansion is justified in Proposition~\ref{P:mixed}.

\subsection{The universal two-chain bound}

\cite{chen:author2026:time-dependency}*{Theorem~3.1, (3.6), p.~15} states
an estimate for such two-chain pairing integrals with nonnegative kernels
$G_l$ by products of the norms $\|G_l\|^{(0)}$, $\|G_l\|^{(1)}_{j,k}$,
$\|G_l\|^{(2)}_{j,k}$ of \cite{chen:author2026:time-dependency}*{(3.3)--(3.5)},
over a partition $\{Q_0,Q_1,Q_2\}$ of $\{1,\dots,2n\}$ with $\#Q_0=\#Q_1$ and
$\#Q_2$ even. As stated, the theorem uses finite spatial spectral measures
$\mu_{j,k}$ with nonnegative covariance functions and temporal kernels
$\Gamma(\alpha_0)^{-1}\int_{A_{j,k}}e^{-\lambda|r|}
\lambda^{\alpha_0-1}\ud\lambda$ for measurable $A_{j,k}\subset\R_+$.
The application to the full covariance therefore requires regularization;
this is carried out in Lemma~\ref{L:crude-corrected}.
The theorem includes cross-pairings between the two chains.
Our finite maximum formulation is proved in
Lemma~\ref{L:pairing-product-envelope}; a maximizing assignment may depend
on the actual kernels. Lemma~\ref{L:translated-covariance-CS} supplies its Case~2 estimate
with the predecessor-time difference retained, as explained in
Remark~\ref{R:source-case2-time-shift}. In the
source it is used only for Stratonovich integrability (Section~4) and, via
Lemma~A.1 with $G_l(t,x)=e^{-\theta t}G(t,x)$, in Laplace variables.

\subsection{Known moment bounds}

The following statement records the source as printed. Its
variational constants require normalization clarification; see
Remark~\ref{R:three-endpoint-scope}. We retain the printed formulas
without adopting a correction. The upper-bound proofs below do not
use the first-moment upper constant.

[held back until the source author has been told]

The source predicts that the limit exists and equals $L^*$
\cite{chen:author2026:time-dependency}*{p.~4}; this is not proved, and
\cite{chen:author2026:time-dependency}*{Remark~8.1} explains why the lower
bound is not sharp (complex-valued intersection local time).

\begin{theorem}[\cite{chen:author2026:time-dependency}*{Remark~5.1, (5.8)}]\label{T:crude}
  $\E u^2(t,x)\le e^{Ct^2}$ for large $t$.
\end{theorem}

\begin{conjecture}[\cite{chen:author2026:time-dependency}*{(1.22)}]\label{Conj:allp}
  For $p=1,2,\dots$,
  \[
    \lim_{t\to\infty}t^{-\kappa}\log\E|u(t,x)|^p
    =p^{\frac{4-\alpha}{3-\alpha}}L^*.
  \]
\end{conjecture}

Since $p^{(4-\alpha)/(3-\alpha)}$ grows faster than $p$, the conjectured
second-moment constant $2^{(4-\alpha)/(3-\alpha)}L^*$ exceeds $2L^*$.
The source explains why its method stops at $p=1$
\cite{chen:author2026:time-dependency}*{Remark~6.3}: the representation of
Theorem~6.1 there uses the monotone order $s_1\le\dots\le s_{2n}$ of a single
chain.

\begin{proposition}[Jensen lower bound]\label{P:Jensen}
  Under Hypothesis~\ref{H:homog}, $\E u(t,x)\ge1$ and
  $\E u^2(t,x)\ge(\E u(t,x))^2$. Consequently, for every real $\ell$,
  \[
    \liminf_{t\to\infty}t^{-\kappa}\log\E u(t,x)\ge\ell
    \quad\Longrightarrow\quad
    \liminf_{t\to\infty}t^{-\kappa}\log\E u^2(t,x)\ge2\ell.
  \]
  The specialization $\ell=L_*$ is conditional on the intended
  first-moment lower bound with that constant. It is not an unconditional
  adoption of the printed normalization in Theorem~\ref{T:first}.
\end{proposition}

\begin{proof}
  For each fixed $t,x$, Lemma~\ref{L:vertex-crude} below gives
  $\sum_n\|X_n(t,x)\|_2<\infty$; its proof does not use the present
  proposition. Thus, $\sum_n\E|X_n(t,x)|<\infty$, and the mean of
  the canonical series is the sum of its means.
  By \eqref{E:expansion} and \cite{chen:author2026:time-dependency}*{(2.20)--(2.21)},
  $\E u(t,x)=\sum_{n\ge0}\E S_{2n}(g_{2n}(\cdot,t,x))\ge1$, since every term is
  a pairing integral of a nonnegative integrand and $S_0=1$. By the
  Cauchy--Schwarz inequality, $\E u^2(t,x)\ge(\E u(t,x))^2$, so
  $t^{-\kappa}\log\E u^2(t,x)\ge2\,t^{-\kappa}\log\E u(t,x)$.
  Taking lower limits proves the implication for every valid $\ell$.
  Substituting $L_*$ requires its stated first-moment premise.
  This proves Proposition~\ref{P:Jensen}.
\end{proof}

\section{Gate G0: cross terms and the loss in the norm bound}\label{S:G0}

This section records a diagnosis of the proposed route, not a proof of
Goal~\ref{G:upper}. Put $X_n(t,x)=S_n(g_n(\cdot,t,x))$, with $X_0=1$, and
\[
  \beta=4-\alpha-\alpha_0>2,\qquad
  P_k=\#\Pi_k=\frac{(2k)!}{2^k k!}.
\]
The count follows by pairing the smallest remaining label with one of
$2k-1$ labels: $P_0=1$ and $P_k=(2k-1)P_{k-1}$, which gives the displayed
formula by induction. All constants below may depend on the fixed covariance and its parameters,
but not on the orders or on $t$.

\subsection{The complete two-chain expansion}

For $m+n=2k$, label the two chains by
$I_1=\{1,\ldots,m\}$ and $I_2=\{m+1,\ldots,m+n\}$.
A self-pairing has both endpoints in one chain; a cross-pairing has one
endpoint in each chain. Both are included in $\Pi_k$.
Let $p(l)$ denote the preceding vertex in its own chain; at each first
vertex set $(s_{p(l)},y_{p(l)})=(0,0)$. Thus, the second chain has its own
root, rather than the last vertex of the first chain. For $D\in\Pi_k$, set
\begin{equation}\label{E:mixed-diagram}
  \begin{split}
    J_{m,n,D}(t)
    ={}&\int_{[0,t]^m_<\times[0,t]^n_<}\ud\mathbf s
    \int_{(\R^d)^{m+n}}\ud\mathbf y\,
    \prod_{\rho=1}^2\prod_{l\in I_\rho}
    G(s_l-s_{p(l)},y_l-y_{p(l)})\\
    &\hspace{20mm}\times
    \prod_{(j,h)\in D}|s_j-s_h|^{-\alpha_0}\gamma(y_j-y_h).
  \end{split}
\end{equation}
An empty chain contributes the factor one. For $d=3$, the spatial Green
kernels are measures; for spatial white noise the covariance is a delta
measure. Integrals in~\eqref{E:mixed-diagram} use the generalized-kernel
and regularization conventions of the source, not pointwise values of
these measures. Lemmas~\ref{L:spatial-wick-measures}--\ref{L:joint-fixed-order}
construct them with the convention of
\cite{chen:author2026:time-dependency}*{Remark~2.3, p.~11,
and the Green regularization on pp.~13--14}.

\begin{proposition}[Mixed terms]\label{P:mixed}
  Under Hypothesis~\ref{H:homog},
  \begin{equation}\label{E:mixed-moment}
    \E[X_m(t,x)X_n(t,x)]
    =\begin{cases}
      \displaystyle\sum_{D\in\Pi_k}J_{m,n,D}(t),&m+n=2k,\\
      0,&m+n\text{ odd},
    \end{cases}
  \end{equation}
  where the case $m=n=0$ equals one. In particular,
  \begin{equation}\label{E:full-second}
    \E u^2(t,x)=\sum_{k=0}^\infty\sum_{m=0}^{2k}
    \sum_{D\in\Pi_k}J_{m,2k-m,D}(t).
  \end{equation}
  This is a convergent series of nonnegative terms.
\end{proposition}

\begin{proof}
  Lemma~\ref{L:joint-fixed-order} below constructs each $X_n$ and each
  individual two-chain diagram at arbitrary vertexwise widths, including
  unequal and empty chains. Its proof uses the positive spatial-measure
  limit and Lemma~\ref{L:pairing-product-envelope}; it uses neither the present
  proposition nor any infinite solution series.

  At positive noise widths Wick's formula gives zero at odd total order
  and the finite pairing sum at even total order. The Green-width limit
  is taken first, as in the construction preceding
  Lemma~\ref{L:spatial-wick-measures}. At fixed $m,n$, joint $L^2$
  convergence of the two factors gives product convergence in $L^1$:
  \[
    \|Y_mY_n-X_mX_n\|_1
    \le\|Y_m-X_m\|_2\|Y_n\|_2
    +\|X_m\|_2\|Y_n-X_n\|_2\longrightarrow0.
  \]
  A zero-order factor stays equal to one. Each individual Wick diagram
  also has the finite nonnegative limit in
  Lemma~\ref{L:joint-fixed-order}.

  To identify its initial-chain form, for terminal variables in the
  first chain set
  \[
    s'_j=t-s_{m+1-j},\qquad y'_j=x-y_{m+1-j},\qquad1\le j\le m,
  \]
  and use the corresponding length-$n$ transformation on the second
  chain. Each transformed chain has initial root $(0,0)$.
  For example, $G(t-s_m,x-y_m)$ becomes $G(s'_1,y'_1)$;
  every other factor becomes the corresponding successive increment.
  The differences in each covariance change sign, absorbed by evenness.
  The vertex involution is
  \[
    \rho(j)=m+1-j\ (1\le j\le m),\qquad
    \rho(m+j)=m+n+1-j\ (1\le j\le n).
  \]
  It induces the pairing bijection
  $D\mapsto\{\{\rho(a),\rho(b)\}:\{a,b\}\in D\}$.
  The same transformation holds before removing noise smoothing.
  Passing to the finitely many diagram limits proves
  \eqref{E:mixed-moment} with precisely~\eqref{E:mixed-diagram}.

  Lemmas~\ref{L:crude-corrected} and~\ref{L:vertex-crude} independently
  prove fixed-$t$ norm summability of the $X_n$, using the fixed-order
  construction just cited and Lemma~\ref{L:pairing-product-envelope}.
  Proposition~\ref{P:mild-construction} identifies their series as a
  Stratonovich mild solution. None of those proofs uses the present
  mixed-term identity. Hence $U_N=\sum_{n=0}^N X_n\to u$ in $L^2$, and
  \[
    |\E U_N^2-\E u^2|
    \le\|U_N-u\|_2(\|U_N\|_2+\|u\|_2)\longrightarrow0.
  \]
  The finite expansions of $\E U_N^2$ increase, since every mixed
  expectation computed above is nonnegative. Their limit is the full
  double sum, independent of its enumeration. Regrouping by total order
  gives~\eqref{E:full-second}. This proves Proposition~\ref{P:mixed}.
\end{proof}

\subsection{A small-order check and a source uniformity issue}

\begin{lemma}[White-space test]\label{L:white-test}
  For $d=\alpha=1$ and $\gamma=\delta_0$, put
  $c_0=((1-\alpha_0)(2-\alpha_0)(3-\alpha_0))^{-1}$. Then
  \begin{equation}\label{E:white-test}
    \E X_1(t,x)^2=c_0t^{3-\alpha_0},\qquad
    \E X_2(t,x)=\tfrac12c_0t^{3-\alpha_0}.
  \end{equation}
  In particular, the total-order-two contribution to~\eqref{E:full-second}
  is $2c_0t^{3-\alpha_0}$.
\end{lemma}

\begin{proof}
  Here $G(s,y)=\frac12\mathbf1_{\{|y|<s\}}$. Therefore,
  $\int_\R G(s,y)G(r,y)\ud y=\min(s,r)/2$. The $(1,1)$ integral is
  \[
    \int_0^t\ud s\int_0^s r(s-r)^{-\alpha_0}\ud r
    =\frac{t^{3-\alpha_0}}
    {(1-\alpha_0)(2-\alpha_0)(3-\alpha_0)}.
  \]
  For the $(0,2)$ integral, the delta covariance sets the two spatial
  vertices equal. Write $0<r<s<t$ for their ordered time variables.
  The first factor $G_r$ has spatial mass $r$, while
  $G_{s-r}(0)=1/2$. Its time integral is half the
  preceding display. The $(2,0)$ term is identical. This proves
  Lemma~\ref{L:white-test}.
\end{proof}

[held back until the source author has been told]

\subsection{Recovering the quadratic-exponential bound}

Write $G_\theta(s,y)=e^{-\theta s}G(s,y)$ and
$\widehat G_s(\xi)=\sin(s|\xi|)/|\xi|$, with value $s$ at $\xi=0$.
We use the norms in the source's (3.3)--(3.5), with the full covariance,
but give their bounds directly. Write $\Gamma_{\mathrm E}$ for Euler's
Gamma function in the following definitions, to distinguish it from the
covariance measure:
\begin{equation}\label{E:damped-norm-definitions}
  \begin{split}
    N_0(\theta)&=\int_0^\infty e^{-\theta s}G_s(\R^d)\ud s,\\
    N_1(\theta)&=\frac1{\Gamma_{\mathrm E}(\alpha_0)}
    \int_0^\infty\lambda^{\alpha_0-1}\ud\lambda
    \int\frac{\mu(\ud\xi)}{(\theta+\lambda)^2+|\xi|^2},\\
    N_2(\theta)^2&=\int_0^\infty\int_0^\infty
    e^{-\theta(s+t)}|s-t|^{-\alpha_0}
    \int\widehat G_s(\xi)\overline{\widehat G_t(\xi)}
    \mu(\ud\xi)\ud s\ud t.
  \end{split}
\end{equation}
The second expression uses the elementary wave Laplace transform
$\int_0^\infty e^{-as}\widehat G_s(\xi)\ud s=(a^2+|\xi|^2)^{-1}$.
The last expression is the space-time covariance quadratic form;
in physical variables it pairs $G_\theta(s,x)$ with $G_\theta(t,y)$.
Thus, the second Green factor in the printed source (3.5) is read with
the independent variable $y$; see
Lemma~\ref{L:translated-covariance-CS} and
Remark~\ref{R:source-case2-time-shift} for the independent justification
and the exact source qualification.

\begin{lemma}[Homogeneous damped norms and temporal tails]
  \label{L:damped-homogeneous-norms}
  Under Hypothesis~\ref{H:homog}, the integrals in
  \eqref{E:damped-norm-definitions} are finite for every $\theta>0$,
  with $N_2(\theta)^2\ge0$, and
  \[
    N_0(\theta)=\theta^{-2},\qquad
    N_1(\theta)=\theta^{\alpha+\alpha_0-2}N_1(1),\qquad
    N_2(\theta)^2=\theta^{-\beta}N_2(1)^2,
    \quad\beta=4-\alpha-\alpha_0.
  \]
  Let
  \[
    K_M(r)=\frac1{\Gamma_{\mathrm E}(\alpha_0)}
    \int_M^\infty e^{-\lambda|r|}\lambda^{\alpha_0-1}\ud\lambda.
  \]
  Denote by $N_1^{(M)}(1)$ the first norm with $\lambda>M$, and by
  $N_2^{(M)}(1)$ the second norm with $K_M(s-t)$ in place of
  $|s-t|^{-\alpha_0}$. Then
  \begin{equation}\label{E:damped-tail-norms}
    N_1^{(M)}(1)\longrightarrow0,\qquad
    N_2^{(M)}(1)\longrightarrow0\quad(M\to\infty).
  \end{equation}
  Spatial Gaussian smoothing, Gaussian smoothing of the Green kernel,
  and restriction of a temporal Laplace domain do not increase these
  corresponding full or tail norm bounds.
\end{lemma}

\begin{proof}
  Scaling the Fourier representation of $\Gamma$ and using Fourier
  uniqueness gives $\mu(cA)=c^\alpha\mu(A)$. Radon finiteness and
  $\alpha>0$ then imply $\mu(\{0\})=0$. In particular,
  $\mu(B_r)=r^\alpha V$, where $V=\mu(B_1)<\infty$.
  Therefore, for $a>0$,
  \[
    \int\frac{\mu(\ud\xi)}{a^2+|\xi|^2}
    =\alpha V a^{\alpha-2}
    \int_0^\infty\frac{u^{\alpha-1}}{1+u^2}\ud u<\infty.
  \]
  The last integral is finite since $0<\alpha<2$.
  Substitution into $N_1$ reduces its finiteness to
  $\int_0^\infty\lambda^{\alpha_0-1}(\theta+\lambda)^{\alpha-2}
  \ud\lambda<\infty$: the conditions at zero and infinity are
  $\alpha_0>0$ and $\alpha+\alpha_0<2$.

  For $N_2$ use
  $|\widehat G_s(\xi)|\le\min(s,|\xi|^{-1})$.
  On $|\xi|\le1$, absolute integration is bounded by
  \[
    V\int_0^\infty\int_0^\infty
    e^{-\theta(s+t)}|s-t|^{-\alpha_0}st\ud s\ud t<\infty.
  \]
  On $|\xi|>1$, use
  $\int_{|\xi|>1}|\xi|^{-2}\mu(\ud\xi)=\alpha V/(2-\alpha)$
  and the same time integral without $st$. Both time integrals are
  finite by splitting into $s\le t$ and $t\le s$, then using
  $u=\min(s,t)$ and $v=|s-t|$; the only singular factor is
  $v^{-\alpha_0}$, with $\alpha_0<1$.
  This proves absolute integrability of the displayed spectral formula.
  For each $\xi$, its time integral is nonnegative because the
  temporal kernel is positive definite. Indeed, it is a positive
  Laplace mixture of the kernels $e^{-\lambda|s-t|}$.
  This proves $N_2(\theta)^2\ge0$.

  The mass identity $G_s(\R^d)=s$ proves the formula for $N_0$.
  In $N_1$ change $\lambda=\theta u$ and $\xi=\theta\eta$.
  In $N_2$ change $s=u/\theta$, $t=v/\theta$ and
  $\xi=\theta\eta$, using
  $\widehat G_{u/\theta}(\theta\eta)=\theta^{-1}\widehat G_u(\eta)$.
  These changes give exactly the stated powers.

  The first tail in~\eqref{E:damped-tail-norms} is a tail of the
  finite nonnegative $N_1(1)$ integral. For the second,
  $0\le K_M(r)\le|r|^{-\alpha_0}$ and $K_M(r)\to0$ for $r\ne0$.
  The absolute majorant just proved permits dominated convergence
  in $(s,t,\xi)$, giving $N_2^{(M)}(1)^2\to0$.
  The tail kernel is positive definite by the same Laplace-mixture
  argument, so its quadratic form is nonnegative.

  Spatial and Green Gaussian smoothing multiply the spectral integrals
  by factors in $[0,1]$. For $N_1$ the integrand is nonnegative.
  For $N_2$, first integrate in time: the quadratic form at each
  $\xi$ is nonnegative, so its Gaussian multiplier can be removed
  in an upper bound. Restricting a temporal Laplace domain likewise
  decreases the first norm and its nonnegative covariance quadratic
  form. This proves all smoothing and truncation assertions, including
  the bounds for temporal tails.
  This proves Lemma~\ref{L:damped-homogeneous-norms}.
\end{proof}

\paragraph{Covariance pairings of translated kernels.}
Fix $d\in\{1,2,3\}$. Let $\mu$ be a finite positive Borel measure on
$\R^d$ such that $\gamma(z)=\int e^{i\xi\cdot z}\mu(\ud\xi)$ is real and
nonnegative for every $z$. Thus, $\gamma$ is bounded, continuous and even,
with $0\le\gamma(z)\le\mu(\R^d)$. Let $\nu$ be a positive Borel measure
on $(0,\infty)$ with $\nu((0,L])<\infty$ for every $L>0$, and put
\[
  \kappa_L(t)=\int_{(0,L]}e^{-\lambda|t|}\nu(\ud\lambda),\qquad
  C_L((t,x),(s,y))=\kappa_L(t-s)\gamma(x-y).
\]
For complex $L^1(\R\times\R^d)$ functions $f,h$, define
\begin{equation}\label{E:translated-covariance-form}
  Q_L(f,h)=\int_{\R^2}\int_{\R^{2d}}
  f(t,x)\overline{h(s,y)}\kappa_L(t-s)\gamma(x-y)
  \ud x\ud y\ud t\ud s.
\end{equation}
This integral is absolutely convergent, with
$|Q_L(f,h)|\le\nu((0,L])\mu(\R^d)\|f\|_1\|h\|_1$.
For nonnegative $f,h$, define $Q(f,h)=\lim_{L\to\infty}Q_L(f,h)$
as an extended nonnegative number. This positive cap limit also defines
the pairing when the full temporal kernel is singular on the diagonal.
The spatial covariance is fixed throughout this definition.
For a nonnegative Borel function $G$ on $(0,\infty)\times\R^d$, let
$G^0$ be its zero extension to nonpositive times and put
\[
  N_0(G)=\int_0^\infty\int_{\R^d}G(t,x)\ud x\ud t,\qquad
  N_C(G)^2=Q(G^0,G^0).
\]
For $(A,a)\in\R\times\R^d$, write
$T_{A,a}f(t,x)=f(t-A,x-a)$. All translated pairings are over the full
time line.

\begin{lemma}[Translated covariance Cauchy--Schwarz]
  \label{L:translated-covariance-CS}
  Under the preceding assumptions on $\mu$ and $\nu$, let $G_1,G_2$ be
  nonnegative Borel functions with $N_0(G_i),N_C(G_i)<\infty$, $i=1,2$.
  For arbitrary origins $(A,a),(B,b)\in\R\times\R^d$,
  \begin{equation}\label{E:translated-covariance-CS}
    0\le Q(T_{A,a}G_1^0,T_{B,b}G_2^0)\le N_C(G_1)N_C(G_2),
  \end{equation}
  and $Q(T_{A,a}G_i^0,T_{A,a}G_i^0)=N_C(G_i)^2$ for $i=1,2$.
  The coefficient one is independent of the origins, dimension, cap and
  covariance masses. Zero norms and zero measures are included.
\end{lemma}

\begin{proof}
  We first prove positivity and Cauchy--Schwarz for the stationary
  kernel $C_L$ at fixed finite $L$. For $\lambda>0$, define
  \[
    h_\lambda(t,r)=\sqrt{2\lambda}\,e^{-\lambda(t-r)}
    \mathbf1_{\{r\le t\}}.
  \]
  Direct integration gives
  \[
    \int_\R h_\lambda(t,r)h_\lambda(s,r)\ud r
    =2\lambda e^{-\lambda(t+s)}
    \int_{-\infty}^{\min(t,s)}e^{2\lambda r}\ud r
    =e^{-\lambda|t-s|}.
  \]
  In particular, $\int h_\lambda(t,r)^2\ud r=1$.
  On the complex Hilbert space
  \[
    \mathcal H_L=L^2((0,L]\times\R^d\times\R,
    \nu(\ud\lambda)\mu(\ud\xi)\ud r),
  \]
  with inner product linear in its first entry, put
  $\Phi_L(t,x)(\lambda,\xi,r)=h_\lambda(t,r)e^{i\xi\cdot x}$.
  Then
  \[
    \|\Phi_L(t,x)\|^2=m_L:=\nu((0,L])\mu(\R^d),\qquad
    \langle\Phi_L(t,x),\Phi_L(s,y)\rangle=C_L((t,x),(s,y)).
  \]
  The scalar integrals are absolutely convergent: Cauchy--Schwarz in
  $r$ bounds $\int|h_\lambda(t,r)h_\lambda(s,r)|\ud r$ by one, and
  both remaining measures are finite on the cap.

  The map $(t,x)\mapsto\Phi_L(t,x)$ is norm-continuous, since its squared
  increment is $2m_L-2\operatorname{Re}C_L((t,x),(s,y))$.
  Continuity of $C_L$ follows by dominated convergence against the finite
  measures. Thus, the map is strongly measurable, has separable range
  and is bounded. For $f\in L^1$, the Bochner integral
  $F_L(f)=\int f(t,x)\Phi_L(t,x)\ud t\ud x$ exists.
  Bochner Fubini, justified by $m_L\|f\|_1\|h\|_1$, gives
  $Q_L(f,h)=\langle F_L(f),F_L(h)\rangle$. Therefore,
  \[
    |Q_L(f,h)|\le Q_L(f,f)^{1/2}Q_L(h,h)^{1/2}.
  \]
  This uses the original stationary covariance, rather than positivity
  of an independently shifted cross kernel. The feature space is
  deterministic and introduces no new Gaussian field.

  Changing both integration variables in~\eqref{E:translated-covariance-form}
  by the same time and spatial translation gives
  \[
    Q_L(T_{A,a}f,T_{A,a}h)=Q_L(f,h).
  \]
  Both differences remain unchanged. The full time line and Lebesgue
  translation invariance justify this equality without an origin factor.
  Apply Cauchy--Schwarz to the two different translates and this equality
  separately to their self pairings. This proves the capped form
  of~\eqref{E:translated-covariance-CS}.

  To make the passage for possibly unbounded nonnegative kernels
  explicit, set
  \[
    G_{i,M}(t,x)=\min(G_i(t,x),M)
    \mathbf1_{\{0<t\le M,\ |x|\le M\}},\qquad M\in\N.
  \]
  These functions increase to $G_i$ almost everywhere. Their zero
  extensions and translates are bounded compactly supported $L^1$
  functions. Since $C_L\ge0$, monotone convergence passes the capped
  inequality and common-translation identity to $G_i$ as $M\to\infty$.
  Equivalently, the finite-cap passage follows from $L^1$ convergence
  and the absolute bound after~\eqref{E:translated-covariance-form}.

  Finally, positivity of $\nu$ and nonnegativity of $\gamma$ give
  \[
    Q_L(G_i^0,G_i^0)\uparrow N_C(G_i)^2,\qquad
    Q_L(T_{A,a}G_1^0,T_{B,b}G_2^0)
    \uparrow Q(T_{A,a}G_1^0,T_{B,b}G_2^0).
  \]
  The finite self norms bound the latter limit by $N_C(G_1)N_C(G_2)$.
  The common-translation identity passes to the limit in the same way.
  No division by a norm is used, so zero norms cause no exception.
  No spatial Gaussian mollifier is removed in this argument.
  This proves Lemma~\ref{L:translated-covariance-CS}.
\end{proof}

\begin{remark}[Source Case 2 and the actual regularized inputs]
  \label{R:source-case2-time-shift}
  \emph{(i)} In Case~2 of the proof of
  \cite{chen:author2026:time-dependency}*{Theorem~3.1, p.~21}, the final
  vertices belong to two nonempty chains of lengths $n_1,n_2$ with
  $n_1+n_2=2n$. Fix their predecessor origins separately:
  \[
    (A,a)=
    \begin{cases}
      (0,0),&n_1=1,\\
      (s_{n_1-1},x_{n_1-1}),&n_1>1,
    \end{cases}
    \qquad
    (B,b)=
    \begin{cases}
      (0,0),&n_2=1,\\
      (s_{2n-1},x_{2n-1}),&n_2>1.
    \end{cases}
  \]
  The second chain's first vertex uses its own root. An empty chain
  has no interchain Case~2 pair. The final-pair integral is, using
  evenness to fix the orientation,
  \[
    \begin{split}
      I&=\int_A^\infty\int_B^\infty\int_{\R^{2d}}
      G_1(t-A,x-a)\kappa(t-s)\gamma(x-y)G_2(s-B,y-b)
      \ud x\ud y\ud s\ud t\\
      &=Q(T_{A,a}G_1^0,T_{B,b}G_2^0),
    \end{split}
  \]
  where the full temporal expression means the positive cap limit.
  Lemma~\ref{L:translated-covariance-CS} gives
  $0\le I\le N_C(G_1)N_C(G_2)$ uniformly in the predecessors, so the
  bound can be inserted into the remaining nonnegative integrals in the
  source's induction. If only $u=t-A$ and $v=s-B$ are substituted, the
  integrand has factors
  \begin{equation}\label{E:translated-covariance-offset}
    G_1(u,x-a)\kappa(u-v+A-B)\gamma(x-y)G_2(v,y-b).
  \end{equation}
  The time difference $A-B$ must remain. The source's first Case~2
  equality on physical p.~21 displays $\kappa(u-v)$ after this change
  of time variables, which is not an identity for general $A\ne B$.
  Its spatial origins remain in the two tests, so $\gamma(x-y)$ is
  correct in those absolute spatial variables. Changing also
  $x=X+a$, $y=Y+b$ gives $\gamma(X-Y+a-b)$.
  We use the original integral and the proved inequality, not the
  offset-free equality or positivity of a shifted cross kernel.

  \emph{(ii)} The norm $N_C(G)$ pairs $G(t,x)$ with $G(s,y)$ in
  \eqref{E:translated-covariance-form}, with independent spatial variables.
  The source's printed (3.5), physical p.~14, repeats $x$ in its second
  Green factor. Our quadratic form states explicitly the convention used
  in~\eqref{E:damped-norm-definitions}; it is not a literal quotation
  of that display.

  [held back until the source author has been told]

  \emph{(iv)} We prove the product estimate needed here in
  Lemma~\ref{L:pairing-product-envelope}, rather than importing the
  remaining displayed induction. On p.~16, the empty-first-chain base
  caption interchanges the mass and first-norm kernel labels; their
  chronological order gives mass on the first kernel. On p.~18, (3.9)
  omits the factor two when a fused kernel occupies a first-norm slot.
  Retaining that factor and using the mass times first-norm convolution
  bound below preserves the half-bound needed in Case~3. The p.~19
  mass-slot partition uses a union of the two excluded labels, not the
  printed intersection; its first-slot edge count excludes the fused
  slot. The p.~21 Case~2 offset is handled by the preceding lemma.
  These are explicit qualifications of the printed formulas, not
  corrections attributed to the source or a claim that its intended
  product bound is false. The finite maximum below is sufficient for
  all our uses; we assert no partition independent of the kernel family.
\end{remark}

\subsection{A finite product bound for two ordered chains}

Fix $d\ge1$, $0<a<1$ and a matching $D$ on $2n$ labels.
For each edge $e\in D$, let $\mu_e$ be finite and positive, with
$\gamma_e(x)=\int e^{i\xi\cdot x}\mu_e(\ud\xi)\ge0$.
For a measurable $A_e\subset(0,\infty)$ put
\[
  \nu_e(\ud\lambda)=\Gamma_{\mathrm E}(a)^{-1}
  \mathbf1_{A_e}(\lambda)\lambda^{a-1}\ud\lambda,
  \qquad \kappa_e(t)=\int e^{-\lambda|t|}\nu_e(\ud\lambda).
\]
For nonnegative $G\in L^1((0,\infty)\times\R^d)$ define
\begin{equation}\label{E:pairing-edge-norms}
  \begin{split}
    N_0(G)&=\int G(t,x)\ud t\ud x,\\
    N_{1,e}(G)&=\int\left|\int e^{-\lambda t+i\xi\cdot x}
    G(t,x)\ud t\ud x\right|\nu_e(\ud\lambda)\mu_e(\ud\xi),\\
    N_{2,e}(G)^2&=\int G(s,x)G(t,y)
    \kappa_e(s-t)\gamma_e(x-y)\ud s\ud x\ud t\ud y.
  \end{split}
\end{equation}
Time integrations in these definitions are positive. Denote the inner
Laplace--Fourier transform by $\mathcal L G(\lambda,\xi)$. The last
integral means its nonnegative temporal cap limit, as in the preceding
covariance pairing. In particular its spatial variables are independent.

Let $I_1=\{1,\ldots,n_1\}$ and
$I_2=\{n_1+1,\ldots,2n\}$, where $n_1+n_2=2n$ and either chain may
be empty. Each chain is ordered in its own time variables. Write $p(l)$
for its predecessor, using $(s_{p(l)},x_{p(l)})=(0,0)$ at the first
vertex of each chain. Set
\begin{equation}\label{E:pairing-diagram-general}
  \begin{split}
    I_D(\boldsymbol G)=\int
    &\prod_{\rho=1}^2\prod_{l\in I_\rho}
    G_l(s_l-s_{p(l)},x_l-x_{p(l)})\\
    &\times\prod_{e=\{j,k\}\in D}
    \kappa_e(s_j-s_k)\gamma_e(x_j-x_k)
    \ud\boldsymbol s\ud\boldsymbol x .
  \end{split}
\end{equation}
The domain is the product of the two positive ordered time simplices
and all spatial variables.

Call $(Q,\iota)$ admissible if $Q_0,Q_1,Q_2$ partition the kernel labels,
$|Q_0|=|Q_1|$, and the map $\iota:Q_1\cup Q_2\to D$ uses each edge
once on $Q_1$ or twice on $Q_2$, never both. There is no incidence
requirement between $l$ and $\iota(l)$. These assignments form a finite
nonempty set $\mathcal A_D$. Put
\begin{equation}\label{E:pairing-product-general}
  \mathcal P_{Q,\iota}(\boldsymbol G)=
  \prod_{l\in Q_0}N_0(G_l)
  \prod_{l\in Q_1}2N_{1,\iota(l)}(G_l)
  \prod_{l\in Q_2}N_{2,\iota(l)}(G_l).
\end{equation}
Thus, $|Q_2|$ is even and $|Q_0|+|Q_2|/2=n$.

\begin{lemma}[Pairing product envelope]\label{L:pairing-product-envelope}
  Suppose every $G_l$ is nonnegative and integrable, and
  $N_{1,e}(G_l),N_{2,e}(G_l)<\infty$ for every $l$ and $e\in D$.
  Then
  \begin{equation}\label{E:pairing-product-envelope}
    I_D(\boldsymbol G)\le
    \max_{(Q,\iota)\in\mathcal A_D}
    \mathcal P_{Q,\iota}(\boldsymbol G).
  \end{equation}
  A maximizing assignment may depend on the actual kernels and edge data.
  No single assignment valid for all kernel families is asserted.
  For $n=0$, both sides are one. Zero kernels, measures and norms are allowed.
\end{lemma}

\begin{proof}
  First cap every temporal domain at $L<\infty$; its measure is finite
  since $a>0$. The stationary covariance pairing in
  Lemma~\ref{L:translated-covariance-CS} has norm $N_{2,e}$.
  Its feature $h_\lambda(t,r)e^{i\xi\cdot x}$ and its proof apply in
  any finite dimension: their only spatial input is the finite measure
  $\mu_e$. Hence, its coefficient-one Cauchy--Schwarz inequality and
  invariance under simultaneous time and space translation apply here.
  All Fourier and Bochner interchanges at this cap are justified by
  the finite covariance mass times the relevant $L^1$ masses.

  For one-sided spacetime convolution $F=G*H$, positivity and the
  Laplace--Fourier product give
  \begin{equation}\label{E:pairing-convolution-norms}
    \begin{split}
      N_0(F)&=N_0(G)N_0(H),\\
      N_{1,e}(F)&\le N_0(G)N_{1,e}(H),\\
      N_{2,e}(F)&\le N_0(G)N_{2,e}(H).
    \end{split}
  \end{equation}
  Indeed, $|\mathcal L G(\lambda,\xi)|\le N_0(G)$ for $\lambda\ge0$
  proves the first-norm estimate. For the second, zero-extend $H$ in
  time. Its translates have the same covariance Hilbert norm.
  Express $G*H$ as their Bochner integral against $G$ and apply
  Minkowski. Thus, every fused kernel satisfies all remaining edge
  hypotheses. No division by a norm is used.

  We use induction on $n$, beginning with the empty product at $n=0$.
  With two vertices on one chain the integral is at most
  $N_0(G_{\rm first})N_{1,e}(G_{\rm last})$; with one on each chain
  it is at most their two second norms by covariance Cauchy--Schwarz.
  These also verify both nonempty-chain orientations at $n=1$.
  Assume the full bound at $n-1$.

  We first prove a half-bound on any region where an endpoint $v$,
  its predecessor $p$ and its partner $a$ satisfy $s_a\le s_p$.
  Require the region indicator to be independent of $(s_v,x_v)$.
  Write $e_0=\{a,v\}$. Since $\kappa_{e_0}$ is decreasing on positive
  arguments, replace $\kappa_{e_0}(s_v-s_a)$ by
  $\kappa_{e_0}(s_v-s_p)$. Integrating the endpoint and taking the
  modulus of its spatial Fourier phase gives the factor
  \[
    \int |\mathcal L G_v(\lambda,\xi)|
    \nu_{e_0}(\ud\lambda)\mu_{e_0}(\ud\xi)=N_{1,e_0}(G_v).
  \]
  Now drop the region indicator by positivity. Remove $v$ and its edge.
  Its partner $a$ is unpaired. If $a$ is terminal in its remaining
  chain, integrate it to $N_0(G_a)$ and apply induction. The result
  is one half of an admissible product, adding $a$ to $Q_0$ and $v$
  to $Q_1$ with edge $e_0$.

  Otherwise, let $b$ be the immediate successor of $a$ on its own chain.
  Integration at $a$ gives exactly $F=G_a*G_b$ at $b$, also when $a$
  was the first vertex. Apply induction to the two reduced chains and
  $D\setminus\{e_0\}$. Mark the slot $i=0,1,2$ occupied by $F$ in a
  maximizing reduced product. Let $R_0,R_1,R_2$ be its other slots and
  $B_{\rm rest}$ their product, retaining every first-slot factor two.
  The new slots can be chosen as follows:
  \[
    \begin{array}{c|ccc}
      i&Q_0&Q_1&Q_2\\ \hline
      0&R_0\cup\{a,b\}&R_1\cup\{v\}&R_2\\
      1&R_0\cup\{a\}&R_1\cup\{b,v\}&R_2\\
      2&R_0\cup\{a\}&R_1\cup\{v\}&R_2\cup\{b\}.
    \end{array}
  \]
  For $i=0$, $|R_0|+1=|R_1|$ and $|R_2|$ is even. Mass
  multiplicativity gives one half of the displayed new product.
  For $i=1$, $|R_0|=|R_1|+1$ and $|R_2|$ is even. If $e_1$ is the
  inherited edge, the actual term and its bound are
  \begin{align*}
    &N_{1,e_0}(G_v)\,[2N_{1,e_1}(F)]B_{\rm rest}\\
    &\qquad\le\tfrac12N_0(G_a)
    [2N_{1,e_1}(G_b)][2N_{1,e_0}(G_v)]B_{\rm rest}.
  \end{align*}
  The inherited edge stays first exactly once; $e_0$ is first once.
  No incidence condition is needed. For $i=2$, $|R_0|=|R_1|$ and
  $|R_2|$ is odd; $e_1$ already occurs once there. The last inequality
  in~\eqref{E:pairing-convolution-norms} puts its other second norm
  on $G_b$, a mass on $G_a$ and $2N_{1,e_0}(G_v)$ on $v$, again with
  a factor one half. Every old edge retains its type and multiplicity.
  The displayed counts give $|Q_0|=|Q_1|$ and even $|Q_2|$ in all
  three cases. This proves the regional half-bound, using only the
  full induction hypothesis, not an assumed stronger induction.

  A domestic endpoint has its partner before its predecessor, so this
  half-bound applies on the entire domain. This also handles an empty
  chain. If both endpoints $u=n_1$ and $v=2n$ are paired to each other,
  condition on their separate predecessors $(A,z),(B,w)$. The endpoint
  integral keeps the temporal argument $r-q+A-B$ in relative times.
  The original stationary covariance Cauchy--Schwarz inequality bounds
  it by $N_{2,e}(G_u)N_{2,e}(G_v)$; translate each self pairing
  separately. Induction and adding $u,v$ to $Q_2$ prove the full bound.
  There is no origin factor or discarded predecessor-time offset.

  It remains that both endpoint pairs are cross and distinct.
  Let $a$ be the partner of $v$, $b$ the partner of $u$, and put
  $p=u-1$, $q=v-1$. Then $a<u$ and $b<v$.
  On $\{s_a\le s_q\}$ remove $v$ by the regional half-bound.
  Its indicator is independent of $s_v,x_v$.
  On the complementary region the chain orders give
  $s_p\ge s_a>s_q\ge s_b$, so remove $u$ instead; that indicator is
  independent of $s_u,x_u$. The removed partner has a successor on
  its own chain in both cases. The two bounds are $P/2$ and $P'/2$
  for possibly different admissible products of the original labels.
  Therefore, their sum is at most $(P+P')/2\le\max(P,P')$.
  This proves~\eqref{E:pairing-product-envelope} at the finite cap.

  Finally, increase $L$ to infinity. The diagram integrands and all
  norm factors increase to their declared values, by positivity and
  monotone convergence. There are only finitely many admissible
  products, so their maximum converges to the maximum of their limits.
  No kernel-independent or measurable maximizing choice is needed.
  Zero norms and measures require no exception; the positive cap
  convention avoids any undefined product on a singular time diagonal.
  This proves Lemma~\ref{L:pairing-product-envelope}.
\end{proof}

Use the joint Gaussian regularizations of the source's (2.11).
Write $a=(\epsilon,\delta)>0$ for one pair of widths and
$\boldsymbol a=(a_1,\ldots,a_n)$ for vertexwise widths.
Let $Y_n^{\boldsymbol a}(t,x)$ be the ordered terminal integral with
kernel $g_n$ in~\eqref{E:expansion} and field
$W_{\epsilon_j,\delta_j}(s_j,y_j)$ at vertex $j$; put $Y_0=1$.
At fixed positive widths these are Gaussian-polynomial Bochner integrals.
Indeed, Wick's formula bounds their product integrands in $L^2$ by
$\sqrt{(2n-1)!!}\,V^{n/2}$, where $V$ is the largest of the finitely
many field variances. The terminal Green measure has mass
$t^{2n}/(2n)!$, by induction using $G_r(\R^d)=r$.
In dimension three these integrals use the actual Green measures:
products and linear pushforwards of $p_\eta*G$ converge against the
bounded continuous covariance products. Mixed moments with two Green
widths and the same mass bound give the $L^2$ limit as $\eta\downarrow0$,
before any noise width is removed.

\subsection{Spatial Wick measures and fixed-order construction}

Put $\gamma_b=p_b*\Gamma$, where $p_b$ is the Brownian heat kernel.
Fix $m+n=2k\ge2$, the two chains $I_1,I_2$ above and $D\in\Pi_k$.
For a gap vector $\boldsymbol r\in(0,\infty)^{2k}$, let $s_l$ be the
sum of the gaps up to vertex $l$ in its own chain. Similarly, for spatial
increments $z_l$, let $x_l$ be their cumulative sum in that chain.
For positive spatial widths $\boldsymbol\epsilon$ define
\[
  J_{\boldsymbol\epsilon,D}(\boldsymbol r)
  =\int\prod_{l=1}^{2k}G_{r_l}(\ud z_l)
  \prod_{\{j,h\}\in D}
  \gamma_{\epsilon_j+\epsilon_h}(x_j-x_h),\qquad
  \rho_{\boldsymbol\epsilon,D}(\ud\boldsymbol r)
  =J_{\boldsymbol\epsilon,D}(\boldsymbol r)\ud\boldsymbol r.
\]
These are nonnegative measures. They are locally finite because the
smoothed covariances are bounded and the Green masses are $r_l$.
Write $\nu_{\boldsymbol\epsilon,D}=e^{-\sum_l r_l}
\rho_{\boldsymbol\epsilon,D}$, and let $\ell_i$ be the sum of the gaps
in chain $i$, with value zero for an empty chain.

\begin{lemma}[Positive spatial Wick-measure limit]\label{L:spatial-wick-measures}
  Under Hypothesis~\ref{H:homog}, the finite measures
  $\nu_{\boldsymbol\epsilon,D}$ converge weakly, as all spatial widths
  tend to zero at arbitrary relative rates, to a finite measure $\nu_D$.
  The locally finite measure $\rho_D=e^{\sum_l r_l}\nu_D$ satisfies
  \[
    \rho_D(cA)=c^{(4-\alpha)k}\rho_D(A),\qquad c>0.
  \]
  It gives zero mass to every face $r_l=0$ and every face
  $\ell_i=T>0$. Consequently, for every bounded continuous $\varphi$
  and $T_1,T_2>0$,
  \begin{equation}\label{E:spatial-wick-limit}
    \int_{\ell_1<T_1,\,\ell_2<T_2}\varphi\ud\rho_{\boldsymbol\epsilon,D}
    \longrightarrow
    \int_{\ell_1<T_1,\,\ell_2<T_2}\varphi\ud\rho_D.
  \end{equation}
\end{lemma}

\begin{proof}
  Orient each pair $e=\{j,h\}$ as $j<h$, and let $\eta_l(\boldsymbol\xi)$
  be the coefficient of $z_l$ in
  $\sum_{e=\{j,h\}}\xi_e\cdot(x_j-x_h)$.
  Finite heat-weighted spectral measures and the finite damped Green
  masses justify Fourier and Laplace Fubini. The wave Laplace transform
  gives, for $\lambda_l\ge0$,
  \begin{equation}\label{E:spatial-positive-laplace}
    \begin{split}
      L_{\boldsymbol\epsilon,D}(\boldsymbol\lambda)
      &:=\int e^{-\sum_l\lambda_l r_l}\ud\nu_{\boldsymbol\epsilon,D}\\
      &=\int\exp\left\{-\frac12\sum_{e=\{j,h\}}
      (\epsilon_j+\epsilon_h)|\xi_e|^2\right\}
      \prod_{l=1}^{2k}\frac1{(1+\lambda_l)^2+|\eta_l(\boldsymbol\xi)|^2}
      \prod_{e\in D}\mu(\ud\xi_e).
    \end{split}
  \end{equation}
  The integrand is nonnegative. Thus the transforms increase when any
  spatial width decreases. This is transform monotonicity, not pointwise
  monotonicity of the physical covariances.

  We prove a uniform bound on their total masses.
  With $V=\mu(B_1)$, Fourier triangle and radial homogeneity give
  \begin{equation}\label{E:construction-heat-bound}
    0\le(p_t*\gamma_b)(x)\le A t^{-\alpha/2},\qquad t,b>0,
    \quad A=\alpha V\int_0^\infty u^{\alpha-1}e^{-u^2/2}\ud u<\infty.
  \end{equation}
  Indeed, its Fourier multiplier is $e^{-(t+b)|\xi|^2/2}$, whose
  integral is $A(t+b)^{-\alpha/2}\le At^{-\alpha/2}$.
  For a Brownian motion $B$ put
  $S_b(T)=\int_0^T\int_0^T\gamma_b(B_s-B_t)\ud s\ud t$.
  For every integer $j\ge1$,
  \begin{equation}\label{E:construction-brownian-moments}
    \E_B S_b(T)^j
    \le\frac{(2j)![A\Gamma_{\mathrm E}(1-\alpha/2)]^j}
    {\Gamma_{\mathrm E}((2-\alpha/2)j+1)}T^{(2-\alpha/2)j}.
  \end{equation}
  To verify this, order the $2j$ time variables in the moment integral.
  Condition on all but the last remaining Brownian vertex. Its pair
  factor has conditional mean at most $A$ times the last remaining
  time gap to the power $-\alpha/2$, by~\eqref{E:construction-heat-bound}.
  Remove this vertex and its partner. The remaining factors do not
  involve either removed vertex, and their marginal law is again the
  Brownian law at the remaining times. Repeat this procedure.
  The $j$ selected right endpoints are distinct; each selected gap is
  at least the original adjacent gap at its right endpoint.
  On each ordered simplex the resulting bound is therefore $A^j$
  times a product of $j$ distinct adjacent gaps to the power
  $-\alpha/2$. Integration over the simplex gives
  $\Gamma_{\mathrm E}(1-\alpha/2)^j
  T^{(2-\alpha/2)j}/\Gamma_{\mathrm E}((2-\alpha/2)j+1)$.
  There are $(2j)!$ possible orders. This proves the bound uniformly
  in $b$; the zeroth moment is one.

  Let $\epsilon_* =\min_l\epsilon_l$. The positive formula
  \eqref{E:spatial-positive-laplace} bounds $L_{\boldsymbol\epsilon,D}(0)$
  by the transform with every vertex width equal to $\epsilon_*$.
  The identity of finite positive measures
  \[
    \int_0^\infty e^{-at}G_t(\ud x)\ud t
    =\frac12\int_0^\infty e^{-a^2u/2}p_u(x)\ud u\ud x
  \]
  follows by their equal Fourier transforms $(a^2+|\xi|^2)^{-1}$.
  Apply it to the $2k$ Green factors at unit damping. This writes the
  common-width transform as $2^{-2k}$ times a two-Brownian-chain
  integral with gap weights $e^{-\sum_l u_l/2}$ and covariance
  $\gamma_{2\epsilon_*}$ on every pair.
  If $\tau_i$ is the last Brownian time in chain $i$, insert
  \[
    1=\frac14\int_{\tau_1}^\infty\int_{\tau_2}^\infty
    e^{-((a-\tau_1)+(b-\tau_2))/2}\ud a\ud b.
  \]
  This also holds for an empty chain with $\tau_i=0$.
  Positivity permits extension of the ordered Brownian time domains to
  their full cubes. At fixed paths the time integrations then factor
  into one occupation integral per pair.
  For independent Brownian paths, spectral Cauchy--Schwarz gives
  \[
    0\le A_{12}:=\int_0^a\int_0^b
    \gamma_{2\epsilon_*}(B_1(s)-B_2(t))\ud s\ud t
    \le\sqrt{S_{2\epsilon_*}^{(1)}(a)S_{2\epsilon_*}^{(2)}(b)}.
  \]
  If the pairing has $v_1,v_2$ self-pairs and $w$ cross-pairs, with
  $v_1+v_2+w=k$, its occupation product is at most
  \[
    S_1^{v_1+w/2}S_2^{v_2+w/2}\le(1+S_1)^k(1+S_2)^k.
  \]
  By~\eqref{E:construction-brownian-moments}, each expected factor
  is bounded by a fixed finite sum $M_k$ of nonnegative powers of
  its horizon, independently
  of $\epsilon_*$. Independence of the two paths now gives
  \[
    \sup_{\boldsymbol\epsilon>0}L_{\boldsymbol\epsilon,D}(0)
    \le2^{-2k-2}\left(\int_0^\infty e^{-a/2}M_k(a)\ud a\right)^2<\infty.
  \]

  Monotone convergence in~\eqref{E:spatial-positive-laplace} yields
  finite limits $L_D(\boldsymbol\lambda)$ for all
  $\boldsymbol\lambda\ge0$. The limiting integrand at zero is integrable,
  so dominated convergence shows continuity at zero.
  Here is the finite-measure Laplace argument, including possible loss
  of mass. Push the measures to $[0,1]^{2k}$ by $y_l=e^{-r_l}$.
  Uniformly bounded masses on this compact cube have weak cluster limits.
  Their integer monomial moments are the prescribed $L_D$ values, so
  polynomial density determines a unique cluster limit. For $c>0$ the
  integral of $\prod_l y_l^c$ is $L_D(c,\ldots,c)$.
  As $c\downarrow0$, continuity at zero and monotone convergence show
  that the cluster limit has no mass on the faces where any $y_l=0$.
  Closed neighborhoods of the $y$-zero faces have limiting mass tending
  to zero; the portmanteau inequality bounds the approximating tail
  masses by these same quantities. Pulling back therefore proves weak
  convergence on $[0,\infty)^{2k}$.
  Bounded continuous test functions are handled by cutting off a
  neighborhood of those zero faces and then using the vanishing tail mass.
  Every sequence of widths tending to zero has this same limit, so
  the convergence is joint and independent of their relative rates.

  Sending just $\lambda_l\to\infty$ in the limiting positive integral
  \eqref{E:spatial-positive-laplace} gives zero by domination by its
  integrable zero-parameter integrand. On the measure side this limit
  is $\nu_D\{r_l=0\}$. Thus every coordinate-zero face has zero mass.

  Heat and wave scaling give, for Borel sets,
  \[
    \rho_{\boldsymbol\epsilon,D}(cA)
    =c^{(4-\alpha)k}\rho_{\boldsymbol\epsilon/c^2,D}(A).
  \]
  This follows from $G_{cr}(c\ud z)=cG_r(\ud z)$,
  $\gamma_b(cx)=c^{-\alpha}\gamma_{b/c^2}(x)$, and the $2k$ time
  Jacobians. Passing to vague limits proves the stated homogeneity
  of $\rho_D$.
  If a compact part $A$ of $\{\ell_i=T\}$, $T>0$, had positive mass,
  its dilates $cA$ at distinct $c\in[1,2]$ would be disjoint, have a
  common positive lower mass bound, and lie in one compact set.
  This contradicts local finiteness. Exhausting the face by compacts
  proves it has zero mass. For an empty chain the positive-level face
  is empty. The finite-horizon region is bounded, and its boundary is
  contained in these horizon faces and the coordinate-zero faces.
  Weak convergence with a compact cutoff, and the bounded continuous
  multiplier $e^{\sum r_l}\varphi$ there, proves
  \eqref{E:spatial-wick-limit}.
  This proves Lemma~\ref{L:spatial-wick-measures}.
\end{proof}

\begin{lemma}[Joint diagram limits and fixed-order construction]
  \label{L:joint-fixed-order}
  Under Hypothesis~\ref{H:homog}, every two-chain diagram with
  $m+n=2k\ge2$ has a finite joint limit as all its positive vertexwise
  spatial and temporal widths tend to zero, at arbitrary relative rates.
  This includes unequal and empty chains. For every $n\ge1,t>0,x$,
  $Y_n^{\boldsymbol a}(t,x)$ has a unique joint $L^2$ limit, denoted
  $X_n(t,x)$; it is the multiple Stratonovich integral of $g_n$.
  Green smoothing in dimension three is removed before noise smoothing.
\end{lemma}

\begin{proof}
  Use the gap variables and spatial measures of
  Lemma~\ref{L:spatial-wick-measures}. With $s_j=s_j(\boldsymbol r)$
  define, on $\ell_1<T_1,\ell_2<T_2$,
  \[
    F_{\boldsymbol\epsilon,\boldsymbol\delta,D}
    =\int\prod_{\{j,h\}\in D}
    \gamma^0_{\delta_j\vee\delta_h}(s_j-s_h)
    \ud\rho_{\boldsymbol\epsilon,D}.
  \]
  At a common temporal width $\eta>0$ the multiplier is bounded and
  continuous. Hence the spatial limit exists at every $T_1,T_2>0$
  by~\eqref{E:spatial-wick-limit}.

  We next bound removal of that temporal cutoff uniformly in all spatial
  widths. Write $F_{\boldsymbol\epsilon,0,D}$ for the integral with
  full factors $|s_j-s_h|^{-\alpha_0}$.
  It is finite at positive spatial widths: bound the spatial covariances
  by their finite suprema and the Green masses by their horizon bounds,
  then integrate the disjoint-pair time factors on the full time cube.
  Each factor $|s-r|^{-\alpha_0}$ is integrable since $\alpha_0<1$.
  The elementary difference-of-products inequality bounds
  $F_{\boldsymbol\epsilon,0,D}-F_{\boldsymbol\epsilon,\eta,D}$ by a sum
  of $k$ nonnegative integrals, each with one marked time covariance
  $K_{1/\eta}$ and all other time covariances full.

  Apply Lemma~\ref{L:pairing-product-envelope} to the damped kernels
  $e^{-s}G_s$. At first smooth the Green kernels in dimension three and
  cap the temporal Laplace domains above.
  Each spatial edge measure is a finite Gaussian-weighted $\mu$ with
  nonnegative physical covariance, and each temporal domain is a
  Laplace interval or its restriction. These are exactly the hypotheses
  of that lemma. The finite-horizon exponential loss is at most
  $e^{T_1+T_2}$. Lemma~\ref{L:damped-homogeneous-norms} bounds all
  unmarked norms independently of the smoothing parameters. The marked
  edge appears once in the first-norm product or twice in the
  second-norm product in every admissible assignment. Consequently,
  \begin{equation}\label{E:joint-temporal-tail}
    0\le F_{\boldsymbol\epsilon,0,D}
    -F_{\boldsymbol\epsilon,\eta,D}
    \le C_{k,T_1,T_2}
    \left(N_1^{(1/\eta)}(1)+N_2^{(1/\eta)}(1)^2\right),
  \end{equation}
  uniformly in all spatial widths. Constants may depend on the fixed
  covariance and $k,T_1,T_2$; no uniformity in these quantities is needed.
  Let the upper temporal caps tend to infinity by positivity, and then
  remove Green smoothing at these fixed spatial widths. For the latter
  passage, the bounded spatial covariance products, weak convergence
  of Green measures and the integrable time-cube majorant just used
  give convergence. The bound survives both passages.
  Its right side tends to zero as $\eta\downarrow0$.

  Denote the fixed-$\eta$ spatial limit by $b_D(\eta)$. These numbers
  increase as $\eta$ decreases, and~\eqref{E:joint-temporal-tail} makes
  them Cauchy with a finite limit $b_D$. If every $\delta_j<\eta$,
  positivity gives
  \[
    F_{\boldsymbol\epsilon,\eta,D}
    \le F_{\boldsymbol\epsilon,\boldsymbol\delta,D}
    \le F_{\boldsymbol\epsilon,0,D}.
  \]
  Fix $\eta$, pass to the spatial limit in the lower term, and use
  the uniform remainder in~\eqref{E:joint-temporal-tail}; then let
  $\eta\downarrow0$. This proves the asserted joint limit $b_D$ with
  arbitrary spatial/temporal rates. If one chain is empty its horizon
  contributes no variables, and the same proof applies.

  At positive widths Wick's formula gives the mixed second moments
  of two copies of $Y_n$ as the finite sum of these diagrams, after
  reversing both terminal chains at their common horizon $t$.
  Evenness of the covariances absorbs the sign changes. Every such
  mixed moment, including either diagonal moment, tends to the same
  finite sum $Q_n=\sum_{D\in\Pi_n}b_D$. Hence
  \[
    \|Y_n^{\boldsymbol a}-Y_n^{\boldsymbol b}\|_2^2
    \longrightarrow Q_n+Q_n-2Q_n=0.
  \]
  Completeness of $L^2$ gives a unique limit independent of all width
  ratios. At fixed positive noise widths the Green-width limit was
  already taken in the terminal construction, so the result has the
  required Green-before-noise convention. Restricting to common noise
  widths gives precisely the multiple Stratonovich definition for $g_n$.
  This proves Lemma~\ref{L:joint-fixed-order}.
\end{proof}

Since $\beta>2$ and $\alpha+\alpha_0<2$,
Lemma~\ref{L:damped-homogeneous-norms} gives constants
$C_0<\infty$ and $\theta_0=1$ such that, for $\theta\ge\theta_0$,
\begin{equation}\label{E:crude-norms}
  N_0(\theta)=\theta^{-2},\qquad
  N_1(\theta)\le C_0,\qquad N_2(\theta)\le C_0\theta^{-1}.
\end{equation}

\begin{lemma}[Corrected crude estimate]\label{L:crude-corrected}
  Under Hypothesis~\ref{H:homog}, for suitable $C<\infty$ and
  $\theta_0>0$,
  \begin{equation}\label{E:crude-corrected}
    \E X_n(t,x)^2\le e^{2\theta_0t}\frac{C^nt^{2n}}{n!}
    \quad(n\ge1,t>0),\qquad
    \E u^2(t,x)\le2e^{2\theta_0t+2Ct^2}.
  \end{equation}
\end{lemma}

\begin{proof}
  On the two finite chains, the product of the exponential weights
  telescopes to $e^{-\theta(s_n+s_{2n})}\ge e^{-2\theta t}$.
  Extend the nonnegative integral to the two infinite time simplices
  and apply Lemma~\ref{L:pairing-product-envelope}. For every admissible
  product, put $q_i=\#Q_i$. Then
  $q_0=q_1$ and $q_0+q_2/2=n$. Hence,~\eqref{E:crude-norms} bounds
  each pairing by $e^{2\theta t}C^n\theta^{-2n}$.
  Summing the $P_n$ pairings gives
  \begin{equation}\label{E:theta-envelope}
    \E X_n(t,x)^2\le P_n e^{2\theta t}C^n\theta^{-2n},
    \qquad\theta\ge\theta_0.
  \end{equation}
  For the finite-spectral-measure hypothesis in
  Lemma~\ref{L:pairing-product-envelope}, first apply it with the spatially
  smoothed covariance and the temporal truncations of (2.24). The smoothed spectral measure is
  finite: the Gaussian multiplier is bounded by a constant times
  $(1+|\xi|^2)^{-(2-\alpha_0)/2}$, whose integral is finite by (1.5).
  This argument requires no radial density for the spectral measure.
  The zero norm is unchanged; the
  first and second norms are bounded by
  Lemma~\ref{L:damped-homogeneous-norms}: their Gaussian multipliers
  can be removed in the upper bounds for the nonnegative transforms
  and covariance quadratic forms. The bound is
  uniform in these regularizations. In $d=3$, first use
  $G_\eta=p_\eta*G$, as defined on pp.~13--14 of the source. Its
  spatial Fourier multiplier is bounded by one and its spatial mass
  equals that of $G$, so the same bounds are uniform in $\eta$ as well.
  For each fixed noise regularization $(\epsilon,\delta)$, first let
  $\eta\downarrow0$ in the source's $L^2$ definition. The squared
  moments converge, so the inequality survives this first limit.
  Then let $(\epsilon,\delta)\to0$ using Lemma~\ref{L:joint-fixed-order}. In $d=1,2$ only
  this latter limit is needed. These limits transfer a uniform inequality;
  no pointwise delta covariance bound is being used.

  Choose $\theta=\theta_0+n/t$ in~\eqref{E:theta-envelope}. Since
  $(2n)!\le(2n)^{2n}$, we have $P_n n^{-2n}\le2^n/n!$.
  Absorb $2^ne^{2n}$ in $C^n$ to obtain the first bound
  in~\eqref{E:crude-corrected}. Its square roots are summable for each
  fixed $t$, by the ratio test. Thus, the norm series converges independently
  of Proposition~\ref{P:mixed}. By Minkowski and Cauchy--Schwarz,
  \[
    \begin{split}
      \|u(t,x)\|_2
      &\le e^{\theta_0t}\sum_{n\ge0}\frac{(\sqrt C t)^n}{\sqrt{n!}},\\
      \left(\sum_{n\ge0}\frac{z^n}{\sqrt{n!}}\right)^2
      &\le\left(\sum_{n\ge0}2^{-n}\right)
      \left(\sum_{n\ge0}\frac{(2z^2)^n}{n!}\right)
      =2e^{2z^2}.
    \end{split}
  \]
  This proves Lemma~\ref{L:crude-corrected}.
\end{proof}

\subsection{The mild equation with the corrected bound}

\begin{lemma}[Uniform vertexwise regularization bound]\label{L:vertex-crude}
  Under Hypothesis~\ref{H:homog}, there are $C<\infty$ and $\theta_0>0$
  such that, for all positive vertexwise widths and $n\ge1$,
  \begin{equation}\label{E:vertex-crude}
    \|Y_n^{\boldsymbol a}(t,x)\|_2\le q_n(t),\qquad
    q_n(t):=e^{\theta_0t}\frac{C^{n/2}t^n}{\sqrt{n!}}.
  \end{equation}
  The bound also holds for $X_n(t,x)$, with $q_0(t)=e^{\theta_0t}\ge1$.
  For each $T<\infty$,
  \begin{equation}\label{E:vertex-summability}
    \sum_{n\ge0}\sqrt{n+1}\,q_n(T)<\infty.
  \end{equation}
\end{lemma}

\begin{proof}
  Wick's formula \cite{chen:author2026:time-dependency}*{(2.19), p.~12},
  with the joint covariance (2.11), gives the square of
  $Y_n^{\boldsymbol a}$, with the widths copied to the second chain. Its edge
  covariances are
  \[
    \gamma^0_{\delta_j\vee\delta_l}(s_j-s_l)
    \gamma_{\epsilon_j+\epsilon_l}(y_j-y_l).
  \]
  On each terminal chain use
  $s'_j=t-s_{n+1-j}$ and $y'_j=x-y_{n+1-j}$.
  This reverses the chain and only permutes its vertex widths;
  covariance differences change sign and the kernels are even.
  For each pairing apply Lemma~\ref{L:pairing-product-envelope} to
  $e^{-\theta r}G_r$, first with Green smoothing if
  $d=3$. The lemma permits a separate finite spectral measure and
  temporal truncation on each edge.
  These hypotheses hold here: the spatial spectral measure on an edge
  is $e^{-(\epsilon_j+\epsilon_l)|\xi|^2/2}\mu(\ud\xi)$, which is
  finite by (1.5), and its temporal Laplace domain is
  $[0,(\delta_j\vee\delta_l)^{-1}]$.

  All edge norms obey~\eqref{E:crude-norms}, uniformly in their widths.
  For the first norm the Laplace--Fourier transform of the damped Green
  kernel is positive, and the spatial Gaussian multiplier and temporal
  truncation can only decrease its nonnegative spectral integral.
  For the second norm first enlarge the temporal covariance to
  $|s-r|^{-\alpha_0}$, using positivity of the Green kernels and the
  smoothed spatial covariance. Its space-time spectral expression is
  an integral of the squared absolute transform against nonnegative
  measures, so removal of the spatial Gaussian multiplier increases it.
  Green smoothing has multiplier at most one and unchanged mass,
  so the same bounds hold before its removal. These assertions follow
  from Lemma~\ref{L:damped-homogeneous-norms}, rather than an imported
  normalization or large-parameter formula in the source's Appendix.
  The constants are independent of all the vertex widths.

  Since $\#Q_0=\#Q_1$ and $\#Q_0+\#Q_2/2=n$ for every admissible
  product, exactly as in~\eqref{E:theta-envelope} we obtain the following
  bound.
  Indeed, put $D=\max\{1,2C_0\}$. The norm constants contribute at
  most $D^{\#Q_1+\#Q_2}\le D^{2n}$, so we may take $C_1=D^2$:
  \[
    \|Y_n^{\boldsymbol a}(t,x)\|_2^2
    \le P_n e^{2\theta t}C_1^n\theta^{-2n},\qquad\theta\ge\theta_0.
  \]
  Let the Green width tend to zero at these fixed positive noise
  widths, and choose $\theta=\theta_0+n/t$.
  The inequality $P_n n^{-2n}\le2^n/n!$ then proves
  \eqref{E:vertex-crude}, after increasing $C$.
  Lemma~\ref{L:joint-fixed-order} gives the joint noise-width limit $X_n$;
  the same bound passes to it. Finally,
  \[
    \frac{\sqrt{n+2}\,q_{n+1}(T)}
    {\sqrt{n+1}\,q_n(T)}
    =\sqrt C\,T\frac{\sqrt{n+2}}{n+1}\longrightarrow0.
  \]
  The ratio test proves~\eqref{E:vertex-summability}.
  This proves Lemma~\ref{L:vertex-crude}.
\end{proof}

\begin{proposition}[Mild construction from the fixed-order limits]
  \label{P:mild-construction}
  Under Hypothesis~\ref{H:homog}, the series
  $u(t,x)=\sum_{n\ge0}X_n(t,x)$ is a mild solution in
  \cite{chen:author2026:time-dependency}*{Definition~2.1 and (2.12),
  pp.~9--10}. More precisely, for each $t>0$ and $x\in\R^d$,
  \begin{equation}\label{E:mild-construction}
    \lim_{\epsilon,\delta\downarrow0}
    \int_0^t\int_{\R^d}G(t-s,x-\ud y)
    u(s,y)W_{\epsilon,\delta}(s,y)\ud s
    =u(t,x)-1\quad\text{in }L^2(\Omega).
  \end{equation}
  The limit allows arbitrary relative rates of the two widths.
  In dimension three the Green-width limit precedes the noise-width
  limit. No uniqueness assertion is made.
\end{proposition}

For $d=3$ we read the source's generalized-integrand definition using its
Green regularization, with the random factor held fixed. The proof below
establishes that limit for the actual product $uW_{\epsilon,\delta}$.

\begin{proof}
  Let $\mathscr P_{\le n}$ be the closed Gaussian polynomial space of
  total degree at most $n$, generated by all the coupled source fields.
  It includes all lower-degree contractions.
  The fixed-width terminal integrals lie in this space, by their
  Bochner construction; their fixed-order $L^2$ limits $X_n$ do too.

  We first record an elementary multiplication bound on these spaces.
  If $H$ is any centered linear Gaussian variable and
  $F\in\mathscr P_{\le n}$, then
  \begin{equation}\label{E:occupied-multiplication}
    \|HF\|_2\le2\sqrt{n+1}\,\|H\|_2\|F\|_2.
  \end{equation}
  If $H=0$ the assertion is immediate. Otherwise take $H/\|H\|_2$
  as the first coordinate of an orthonormal Gaussian basis.
  On normalized Hermite polynomials its creation and annihilation
  operators have norms at most $\sqrt{n+1}$ and $\sqrt n$ on total
  degrees at most $n$: the squared coefficient sums have respective
  weights $a_1+1\le n+1$ and $a_1\le n$.
  Their sum proves the bound for finite-coordinate polynomials.
  Approximation in the degree-closed space proves it for $F$ as well.
  Indeed, the products of an approximating sequence are $L^2$ Cauchy
  by this bound; subsequences converging almost surely identify their
  limit with $HF$. This also proves the closedness of multiplication
  needed below. The argument allows $F$ to depend on $H$.

  Lemma~\ref{L:vertex-crude} proves absolute $L^2$ convergence of the
  defining series for $u$, locally uniformly in time in the displayed
  norm bounds. All fields are strongly measurable as $L^2(\Omega)$
  vectors. At positive widths, rescale the ordered times and Green
  increments to fixed unit-time domains. The Gaussian evaluations are
  jointly measurable, and their bounded moments and the finite Green
  masses give Bochner domination on bounded time intervals. Parameter
  integration therefore gives joint strong measurability in $(s,y)$.
  Pointwise $L^2$ limits along a fixed countable sequence of widths
  give this property for $X_n$, then for the series.
  For later Green limits we also need spatial continuity at each fixed
  time. Positive-width terminal terms are $L^2$-continuous in space,
  by continuity of their bounded smoothed covariance products and
  dominated integration against the finite Green measures.
  Joint spatial stationarity of the coupled regularizations shows that
  \[
    \|Y_n^{\boldsymbol b}(s,y)-X_n(s,y)\|_2
    =\|Y_n^{\boldsymbol b}(s,0)-X_n(s,0)\|_2.
  \]
  Thus their convergence is uniform in $y$ for fixed $s$.
  Consequently $X_n(s,\cdot)$, and by summability $u(s,\cdot)$,
  have continuous $L^2$ representatives.

  Fix an external width $a=(\epsilon,\delta)>0$ and write
  $W_a=W_{\epsilon,\delta}$, with variance
  $V_a=\gamma^0_\delta(0)\gamma_{2\epsilon}(0)<\infty$.
  For $n\ge1$ define the Bochner integral
  \[
    I_{n,a}(t,x)=\int_0^t\int_{\R^d}G(t-s,x-\ud y)
    W_a(s,y)X_{n-1}(s,y)\ud s.
  \]
  It exists because~\eqref{E:occupied-multiplication} gives
  \begin{equation}\label{E:fixed-external-domination}
    \|W_a(s,y)X_{n-1}(s,y)\|_2
    \le2\sqrt n\sqrt{V_a}\,q_{n-1}(T),\qquad0\le s\le T,
  \end{equation}
  and the spatial Green mass is $t-s$.
  At fixed $a$, multiplication of the inner regularizations by $W_a$
  preserves their $L^2$ convergence, by the same bound on degree
  at most $n-1$. Their norms have the uniform domination just used.
  Dominated Bochner integration therefore gives
  \begin{equation}\label{E:partial-vertex-limit}
    I_{n,a}(t,x)=\lim_{\boldsymbol b\downarrow0}
    Y_n^{(\boldsymbol b,a)}(t,x)\quad\text{in }L^2.
  \end{equation}
  Here $a$ is at the last, terminal vertex and $\boldsymbol b$ at the
  preceding $n-1$ vertices. At positive widths this identity before
  passage to the limit is ordinary terminal-kernel Fubini; its moment
  bound was established before Lemma~\ref{L:vertex-crude}.
  For $n=1$ there are no inner widths and the identity is exact.
  In particular,~\eqref{E:vertex-crude} passes to this inner limit:
  \begin{equation}\label{E:mixed-vertex-bound}
    \sup_{a>0}\|I_{n,a}(t,x)\|_2\le q_n(t).
  \end{equation}

  We spell out the dimension-three convention in these steps.
  The product $W_a(s,y)X_{n-1}(s,y)$ is $L^2$-continuous in $y$.
  Apply~\eqref{E:occupied-multiplication} first to
  $W_a(s,y)(X_{n-1}(s,y)-X_{n-1}(s,y'))$ and then to
  $(W_a(s,y)-W_a(s,y'))X_{n-1}(s,y')$.
  The two factors tend to zero in the required norms, by the continuity
  just proved and the smoothed covariance of $W_a$.
  The bound~\eqref{E:fixed-external-domination} is uniform in $y$.
  Therefore convolution against $p_\eta*G_{t-s}$ converges in $L^2$
  to convolution against $G_{t-s}$: on a compact set approximate this
  continuous vector function by a finite continuous partition of unity
  times fixed vector values, use scalar weak convergence, and control
  the complement by tightness
  and the uniform bound. The mass $t-s$ and
  \eqref{E:fixed-external-domination} permit dominated time integration.
  This proves the Green-width limit at fixed external widths.
  The same argument applies before the inner noise limit; all
  $Y_n^{(\boldsymbol b,a)}$ already use their Green limit at positive
  noise widths. Thus,~\eqref{E:partial-vertex-limit} does not interchange
  the source's Green and noise limits.

  For each fixed $n$, the joint fixed-order convergence in
  Lemma~\ref{L:joint-fixed-order} implies
  \begin{equation}\label{E:external-vertex-limit}
    \lim_{a\downarrow0}I_{n,a}(t,x)=X_n(t,x)\quad\text{in }L^2.
  \end{equation}
  To see the role of joint convergence, fix $\zeta>0$ and choose
  $r>0$ so that every vertex width below $r$ gives
  $\|Y_n^{(\boldsymbol b,a)}-X_n\|_2<\zeta$.
  Fix any external pair $a$ below $r$ and let the inner widths tend
  to zero in~\eqref{E:partial-vertex-limit}. Then
  $\|I_{n,a}-X_n\|_2\le\zeta$. This proves the asserted limit with
  arbitrary relative rates; it does not assume a partial-limit theorem.

  It remains to identify the full product integral, rather than only
  its finite-order terms. At fixed $a$,
  \eqref{E:occupied-multiplication} and
  \eqref{E:vertex-summability} imply
  \[
    \sum_{n\ge1}\|W_a(s,y)X_{n-1}(s,y)\|_2
    \le2\sqrt{V_a}\sum_{n\ge1}\sqrt n\,q_{n-1}(T)<\infty,
    \qquad0\le s\le T.
  \]
  Multiplication is closed: partial sums of $u$ converge in $L^2$,
  and their products converge by this estimate, so an almost surely
  convergent subsequence identifies the product limit with $W_a u$.
  Dominated Green integration and norm summability now prove
  \[
    I_a(t,x):=\int_0^t\int_{\R^d}G(t-s,x-\ud y)
    W_a(s,y)u(s,y)\ud s
    =\sum_{n\ge1}I_{n,a}(t,x)\quad\text{in }L^2.
  \]
  The sum of the product integrands is spatially $L^2$-continuous
  by uniform summability, so its Green-width limit is justified in
  exactly the same way. Finally, for every $N$,
  \[
    \|I_a(t,x)-(u(t,x)-1)\|_2
    \le\sum_{n=1}^N\|I_{n,a}(t,x)-X_n(t,x)\|_2
    +2\sum_{n>N}q_n(t).
  \]
  First let $a\downarrow0$ using~\eqref{E:external-vertex-limit}, then
  let $N\to\infty$ using~\eqref{E:vertex-summability}.
  This proves~\eqref{E:mild-construction}, hence the mild equation in
  the stated definition. The source's (5.3)--(5.4) and its Section~5(ii)
  identification proof have not been used.
  This proves Proposition~\ref{P:mild-construction}.
\end{proof}

Thus, the exponent two enters through replacing the paired norm products
by $C\theta^{-2}$, followed by the pairing count and the order summation.
The sum over unequal chain lengths is not responsible for this loss:
the same loss already occurs in the diagonal estimate and Minkowski's
inequality.

\subsection{What homogeneity recovers, and what the bound still loses}

\begin{proposition}[The uniform pairing estimate]\label{P:envelope}
  Under Hypothesis~\ref{H:homog}, there is $K>0$ such that
  \begin{equation}\label{E:homogeneous-envelope}
    \E[X_m(t,x)X_n(t,x)]
    \le P_k K^k e^{2\theta t}\theta^{-\beta k},
    \qquad m+n=2k\ge2,\quad\theta>0.
  \end{equation}
  Define the numerical majorant produced by applying this estimate
  separately at every total order by
  \begin{equation}\label{E:B-envelope}
    B_K(t)=1+\sum_{k\ge1}(2k+1)P_kK^k
    \inf_{\theta>0}\{e^{2\theta t}\theta^{-\beta k}\}.
  \end{equation}
  Then $\E u^2(t,x)\le B_K(t)$ and, for some $c,C>0$ and all large $t$,
  \begin{equation}\label{E:envelope-growth}
    ct^{\rho}\le\log B_K(t)\le Ct^{\rho},\qquad
    \rho=\frac{\beta}{\beta-1}
    =\frac{4-\alpha-\alpha_0}{3-\alpha-\alpha_0}>\kappa.
  \end{equation}
  The lower bound here concerns the numerical majorant $B_K$, not the
  second moment.
\end{proposition}

\begin{proof}
  The wave kernel scales as
  $G(cs,c\ud y)=cG(s,\ud y)$, and the covariance has degree $-\alpha$.
  Changing all time and spatial variables by $\theta^{-1}$ in the norms
  yields
  \begin{equation}\label{E:homogeneous-norms}
    N_0(\theta)=\theta^{-2},\quad
    N_1(\theta)=N_1(1)\theta^{\alpha+\alpha_0-2},\quad
    N_2(\theta)^2=N_2(1)^2\theta^{-\beta}.
  \end{equation}
  All constants and scalings follow directly from
  Lemma~\ref{L:damped-homogeneous-norms}.
  The products $2N_0N_1$ and $N_2^2$ therefore both have degree
  $-\beta$. Choose
  $K\ge\max\{2N_1(1),N_2(1)^2\}$, increasing it to a positive
  constant if needed. Lemma~\ref{L:pairing-product-envelope} and
  $q_0+q_2/2=k$ give $K^k\theta^{-\beta k}$ for every admissible product. The finite
  horizons contribute at most $e^{2\theta t}$. Apply this first to
  regularized moments. In $d=3$, fix $(\epsilon,\delta)$ and let
  $\eta\downarrow0$ in each factor's $L^2$ limit; Cauchy--Schwarz gives
  $L^1$ convergence of their product. Then let
  $(\epsilon,\delta)\to0$ in the same way, using Lemma~\ref{L:joint-fixed-order} for each
  chain. In $d=1,2$ only the noise limit is required. The estimates are
  uniform at both stages, by the multiplier bounds in
  Lemma~\ref{L:crude-corrected}. This proves~\eqref{E:homogeneous-envelope}.
  Empty-chain cases satisfy the same bound (using $e^{2\theta t}$ is
  harmless). Proposition~\ref{P:mixed} now gives the majorant.

  The infimum in~\eqref{E:B-envelope} is attained at
  $\theta=\beta k/(2t)$ and equals
  $e^{\beta k}(2t/(\beta k))^{\beta k}$. Put $q=\beta-1>1$.
  The elementary estimates
  \[
    k!\le P_k\le2^k k!,\qquad
    (k/e)^k\le k!\le k^k,\qquad 2k+1\le3^k
  \]
  show that, for fixed positive $a,b$ depending only on $K,\beta$,
  \[
    \sum_{k\ge0}\frac{(at^\beta)^k}{(k!)^q}
    \le B_K(t)\le
    \sum_{k\ge0}\frac{(bt^\beta)^k}{(k!)^q}.
  \]
  Indeed, the additional factor $k!^\beta/k^{\beta k}$ lies between
  $e^{-\beta k}$ and one and can be absorbed into $a^k,b^k$.
  For $z>0$, the right-hand series is at most
  $(\sum_{k\ge0}z^{k/q}/k!)^q=e^{qz^{1/q}}$, by the elementary
  $\ell^q$ versus $\ell^1$ inequality for nonnegative sequences.
  For a lower bound choose $k=\lfloor z^{1/q}/2\rfloor$ and use
  $k!\le k^k$; its single summand is at least $2^{qk}$.
  These estimates prove~\eqref{E:envelope-growth}. Finally,
  $\beta-1=3-\alpha-\alpha_0<3-\alpha$, so $\rho>\kappa$.
  This proves Proposition~\ref{P:envelope}.
\end{proof}

\begin{remark}[G0 verdict and its scope]\label{R:G0-verdict}
  Since $\beta>2$, we have $1<\rho<2$. Thus,
  Proposition~\ref{P:envelope} improves the crude quadratic time scale
  under homogeneity. It does not itself settle Goal~\ref{G:upper};
  Section~\ref{S:interval-upper} uses a different argument.
  Theorem~3.1 used through its uniform pairing estimate is \emph{not
  viable for Goal~\ref{G:upper}}: even with exact homogeneous norm
  scaling, the resulting majorant has exponent $\rho>\kappa$.
  The order coefficient has factorial denominator $(k!)^{3-\alpha-\alpha_0}$,
  whereas the desired scale requires $(k!)^{3-\alpha}$; the missing
  factor is $(k!)^{\alpha_0}$, up to exponential factors in $k$.
  Counting the $2k+1$ chain-length splits does not cause this loss,
  since it can be absorbed into an exponential factor.
  This conclusion does not rule out a more refined application retaining
  temporal order or grouping pairings before estimating them, and does not
  disprove the conjecture. In the formal boundary limit
  $\alpha_0\downarrow0$, both $\rho$ and $\kappa$ tend to
  $(4-\alpha)/(3-\alpha)$. This necessary time-independent calibration
  does not distinguish them and asserts no endpoint theorem or uniformity
  of constants in $\alpha_0$. At $p=1$ use the empty-chain case with
  $e^{\theta t}$ in place of $e^{2\theta t}$; minimizing at
  $\theta=\beta k/t$ changes only a constant to the power $k$, leaving
  the same factorial denominator $(k!)^{3-\alpha-\alpha_0}$.
  It therefore also loses the factorial power $\alpha_0$ relative to
  $\beta/\kappa=3-\alpha$, the power corresponding to the target
  series scale. This is a comparison of scales, not a coefficient estimate
  asserted by the source's Theorem~1.2. The loss is not specific to the
  second moment. Both the crude and homogeneous upper bounds are
  consistent with the Jensen lower bound, being at larger time scales.
  No identification with the Skorohod second moment is used: its exclusion
  of self-pairings changes the combinatorics, already visible in the
  $(0,2)$ and $(2,0)$ terms of Lemma~\ref{L:white-test}.
\end{remark}

\section{Gate G1: finite-order calibrations in one space dimension}\label{S:G1}

We now compute the total-order-two and total-order-four coefficients in
Proposition~\ref{P:mixed}, first for spatial white noise and then for
$\gamma(x)=c_\alpha|x|^{-\alpha}$ with $0<\alpha<1$ and $c_\alpha>0$.
Here $d=1$ throughout. A total order is the sum of the two Stratonovich
orders; it is not an orthogonal Wiener-chaos order. Write
\[
  A=\{(1,2),(3,4)\},\quad B=\{(1,3),(2,4)\},\quad
  C=\{(1,4),(2,3)\}.
\]
These are the three pairings of four vertices. All finite integrals below
retain the normalization $G(s,y)=\frac12\mathbf1_{\{|y|<s\}}$ and
covariance $|s-r|^{-\alpha_0}\gamma(y-z)$.

\subsection{Spatial white noise: all order-four diagrams}

For $a,b,c\ge0$, define
\begin{equation}\label{E:interval-area}
  F(a,b,c)=4ab-(a+b-c)_+^2+(|a-b|-c)_+^2.
\end{equation}
This is the area of
$\{(x,y):|x|<a,\ |y|<b,\ |x-y|<c\}$. In particular, $F$ is
nonnegative and symmetric in its three arguments. To verify the formula,
subtract from the rectangle the two regions where $|x-y|\ge c$;
when $c\ge|a-b|$ these are two right triangles, and when
$c<|a-b|$ the retained strip has area $4\min(a,b)c$.
The three formulas, including $c\ge a+b$, give~\eqref{E:interval-area}.
Symmetry also follows from swapping $x,y$ and the determinant-one change
$(x,y)\mapsto(x,x-y)$.

In the following table, $V$ is a spatial factor and $q_1,q_2$ are
nonnegative time gaps. The contribution of a row is the integral of
$V(q_1q_2)^{-\alpha_0}$ over its domain, with ordinary Lebesgue measure
in its four listed variables. The domains are
\[
  \begin{array}{ll}
    (0,4):&a,b,c,d>0,\quad a+b+c+d<t,\\
    (1,3):&0<r<t,\quad a,b,c>0,\quad a+b+c<t,\\
    (2,2):&a,b,c,d>0,\quad a+b<t,\quad c+d<t.
  \end{array}
\]
The letters $a,b,c,d$ denote increments within the nonempty chains;
for $(1,3)$, $r$ is the time of the single vertex. Values on zero-gap
sets do not affect these nonnegative integrals.

\begin{proposition}[White-space order four]\label{P:white-four}
  Suppose that $d=\alpha=1$ and $\gamma=\delta_0$. Each
  $J_{m,n,D}(t)$ with $m+n=4$ is given by the following table or by
  exchanging the two chains:
  \begin{equation}\label{E:white-four-table}
    \begin{array}{c|c|c|c|c}
      (m,n)&D&V&q_1&q_2\\ \hline
      (0,4)&A&ac/4&b&d\\
      (0,4)&B&a\min(b,c,d)/4&b+c&c+d\\
      (0,4)&C&a\min(b,d)/4&b+c+d&c\\ \hline
      (1,3)&A&\min(r,a)b/4&|r-a|&c\\
      (1,3)&B&F(r,a,\min(b,c))/16&|r-a-b|&b+c\\
      (1,3)&C&F(r,a,c)/16&|r-a-b-c|&b\\ \hline
      (2,2)&A&ac/4&b&d\\
      (2,2)&B&\min(a,c)\min(b,d)/4&|a-c|&|a+b-c-d|\\
      (2,2)&C&F(a,c,\min(b,d))/16&|a-c-d|&|a+b-c|
    \end{array}
  \end{equation}
  The total-order-four contribution is
  \begin{equation}\label{E:total-four}
    2\sum_{D\in\{A,B,C\}}J_{0,4,D}(t)
    +2\sum_{D\in\{A,B,C\}}J_{1,3,D}(t)
    +\sum_{D\in\{A,B,C\}}J_{2,2,D}(t).
  \end{equation}
  Each entry scales as $t^{6-2\alpha_0}$ times its unit-time value.
\end{proposition}

\begin{proof}
  In each pairing identify its first pair's spatial positions with $x$
  and the other pair's positions with $y$. The two delta covariances
  have unit mass, so spatial integration leaves $1/16$ times the area
  allowed by the four Green indicators. For a single chain the position
  lists for $A,B,C$ are, respectively,
  $(x,x,y,y)$, $(x,y,x,y)$ and $(x,y,y,x)$.
  Their areas are $4ac$, $4a\min(b,c,d)$ and $4a\min(b,d)$.

  For $(1,3)$ take the single position to be $x$. The long chain has
  positions $(x,y,y)$, $(y,x,y)$ or $(y,y,x)$ for $A,B,C$.
  The first area is $4\min(r,a)b$; the other two areas are
  $F(r,a,\min(b,c))$ and $F(r,a,c)$. For $(2,2)$ the position lists
  of the two chains are $(x,x),(y,y)$ for $A$,
  $(x,y),(x,y)$ for $B$, and $(x,y),(y,x)$ for $C$.
  The areas are $4ac$, $4\min(a,c)\min(b,d)$ and
  $F(a,c,\min(b,d))$. In every case reading the paired times gives
  the two gaps in~\eqref{E:white-four-table}. This proves each row,
  with no unlisted pairing or multiplicity. The distributional delta
  integrations can equivalently be obtained by convolution with the
  source's spatial approximate identity: for positive increments the
  remaining bounded interval indicators have only boundary
  discontinuities, and those boundaries have two-dimensional measure
  zero. The resulting areas converge to the displayed areas. They are
  uniformly bounded at unit time: each smoothed delta has mass one,
  so its integral over its paired coordinates in $[-1,1]^2$ is at most
  two. The four Green factors give a spatial bound $2^2/16=1/4$.
  Integrability of the time weights follows from the disjoint-pair
  bound used in Lemma~\ref{L:static-four} below.

  Exchanging chains gives the $(4,0)$ and $(3,1)$ sums without changing
  the covariance factors. This proves~\eqref{E:total-four}. Finally,
  scaling all four time variables by $t$ gives $t^4$ from their measure,
  $t^2$ from the area and $t^{-2\alpha_0}$ from the covariance factors.
  This proves Proposition~\ref{P:white-four}.
\end{proof}

\begin{lemma}[Static finite-order calibration]\label{L:static-four}
  As $\alpha_0\downarrow0$, each unit-time coefficient in
  Proposition~\ref{P:white-four} converges to the entry below:
  \begin{equation}\label{E:static-four-table}
    \begin{array}{c|ccc|c}
      (m,n)&A&B&C&\text{sum}\\ \hline
      (0,4)&1/2880&1/8640&1/5760&11/17280\\
      (1,3)&1/576&29/34560&1/640&143/34560\\
      (2,2)&1/144&1/480&31/17280&187/17280
    \end{array}
  \end{equation}
  Thus, the static total-order-four contribution is $11t^6/540$.
  The static total-order-two contribution is $t^3/3$.
  These are coefficients, not large-time asymptotic constants.
\end{lemma}

\begin{proof}
  On the unit-time domain all original time coordinates belong to
  $[0,1]$. The spatial factor is bounded by $1/4$, since all positions
  lie in $[-1,1]$ and the two free positions have area at most four.
  Fix $0<\bar a<1$. For $0\le\alpha_0\le\bar a$, the temporal
  factors are bounded by the product with exponent $\bar a$.
  On the full time cube its integral is
  \[
    \left(\int_0^1\int_0^1|s-r|^{-\bar a}\ud s\ud r\right)^2
    =\left(\frac{2}{(1-\bar a)(2-\bar a)}\right)^2<\infty,
  \]
  because the two pairs use disjoint labels. Dominated convergence
  permits setting $\alpha_0=0$ in every row.

  We evaluate the resulting integrals by an independent spatial
  calculation. For fixed free positions $x,y$, let $L_1,L_2$ be the
  sums of absolute spatial increments along the two chains, starting
  at zero. Integrating their time increments first gives
  \begin{equation}\label{E:static-sector}
    J_{m,n,D}(1)\big|_{\alpha_0=0}
    =\frac{1}{16m!n!}\int_{\R^2}
    (1-L_1(x,y))_+^m(1-L_2(x,y))_+^n\ud x\ud y.
  \end{equation}
  An empty-chain factor in this formula is defined to be one. Indeed,
  writing each time increment as its required absolute spatial increment
  plus a nonnegative slack leaves a simplex of volume
  $(1-L_\rho)_+^{n_\rho}/n_\rho!$.
  Put $w=|x-y|$. The length pairs are
  \[
    \begin{array}{c|ccc}
      (m,n)&A&B&C\\ \hline
      (0,4)&(0,|x|+w)&(0,|x|+3w)&(0,|x|+2w)\\
      (1,3)&(|x|,|x|+w)&(|x|,|y|+2w)&(|x|,|y|+w)\\
      (2,2)&(|x|,|y|)&(|x|+w,|x|+w)&(|x|+w,|y|+w)
    \end{array}
  \]
  Divide the plane into $0\le x\le y$, $0\le y\le x$, $x\ge0\ge y$
  and their reflected sectors. Use $(x,y)=(u,u+v),(u+v,u),(u,-v)$,
  respectively, where $u,v\ge0$. Each map has determinant of absolute
  value one. In these three sectors the integrals of
  $(1-L_1)_+^m(1-L_2)_+^n$, before multiplication by $2/(16m!n!)$, are
  \begin{equation}\label{E:sector-values}
    \begin{array}{c|c|ccc}
      (m,n)&D&0\le x\le y&0\le y\le x&x\ge0\ge y\\ \hline
      (0,4)&A&1/30&1/60&1/60\\
      (0,4)&B&1/90&1/120&1/360\\
      (0,4)&C&1/60&1/90&1/180\\
      (1,3)&A&1/24&3/160&11/480\\
      (1,3)&B&1/72&3/160&11/1440\\
      (1,3)&C&1/48&1/30&1/48\\
      (2,2)&A&1/18&1/18&1/9\\
      (2,2)&B&1/30&1/60&1/60\\
      (2,2)&C&31/1440&31/1440&31/2160
    \end{array}
  \end{equation}
  All entries follow by integrating polynomials over the two linear
  constraints $L_1\le1$, $L_2\le1$. For example,
  $\int_{u,v\ge0}(1-pu-qv)_+^4\ud u\ud v=1/(30pq)$.
  The last row's first entry and last entry are, explicitly,
  \[
    \begin{split}
      &\int_0^{1/2}\ud v\int_0^{1-2v}
      (1-u-v)^2(1-u-2v)^2\ud u=\frac{31}{1440},\\
      &\int_0^{1/3}\ud u\int_0^{(1-u)/2}
      (1-2u-v)^2(1-u-2v)^2\ud v\\
      &\quad+\int_{1/3}^{1/2}\ud u\int_0^{1-2u}
      (1-2u-v)^2(1-u-2v)^2\ud v=\frac{31}{2160}.
    \end{split}
  \]
  The stated lengths and linear bounds similarly specify every entry
  of~\eqref{E:sector-values}. Summing and multiplying by
  $2/(16m!n!)$ proves~\eqref{E:static-four-table}. Applying the
  multiplicities in~\eqref{E:total-four} gives $11/540$.
  Lemma~\ref{L:white-test} at $\alpha_0=0$ gives the order-two value.
  This proves Lemma~\ref{L:static-four}.
\end{proof}

\subsection{Riesz covariance: order two and an order-four integral}

\begin{proposition}[Riesz finite coefficients]\label{P:riesz-small}
  Suppose $d=1$, $0<\alpha<1$, $0<\alpha_0<1$, and
  $\gamma(y)=c_\alpha|y|^{-\alpha}$ with $c_\alpha>0$.
  With $\beta=4-\alpha-\alpha_0$, the two order-two terms are
  \begin{equation}\label{E:riesz-two}
    \begin{split}
      \E X_2(t,x)
      &=\frac{c_\alpha t^\beta}
      {(1-\alpha)(2-\alpha-\alpha_0)(3-\alpha-\alpha_0)
      (4-\alpha-\alpha_0)},\\
      \E X_1(t,x)^2
      &=\frac{c_\alpha}{(1-\alpha)(2-\alpha)}
      \int_0^t v^{-\alpha_0}
      \left[\frac{(2t-v)^{3-\alpha}-v^{3-\alpha}}{2(3-\alpha)}
      -(t-v)v^{2-\alpha}\right]\ud v.
    \end{split}
  \end{equation}
  Their total is $\E X_1^2+2\E X_2$.

  The following explicit unit-domain integral gives every order-four
  term. For $m+n=4$, let
  \[
    H_m=\{h\in(0,\infty)^4:\ \sum_{l=1}^m h_l<1,
    \ \sum_{l=m+1}^4 h_l<1\},
  \]
  with an empty sum equal to zero. For each index $l$, let $b(l)$ be
  the first index in its own nonempty chain, and define
  \[
    S_l(h)=\sum_{i=b(l)}^l h_i,\qquad
    Y_l(h,U)=\sum_{i=b(l)}^l h_iU_i,
  \]
  where $U_1,\ldots,U_4$ are independent uniform variables on $[-1,1]$.
  Then, for $D=A,B,C$,
  \begin{equation}\label{E:riesz-four}
    \begin{split}
      J_{m,n,D}(t)
      ={}&c_\alpha^2t^{2\beta}
      \int_{H_m}\left(\prod_{l=1}^4h_l\right)
      \prod_{(j,q)\in D}|S_j(h)-S_q(h)|^{-\alpha_0}\\
      &\hspace{8mm}\times
      \E_U\left[\prod_{(j,q)\in D}
      |Y_j(h,U)-Y_q(h,U)|^{-\alpha}\right]\ud h.
    \end{split}
  \end{equation}
  This is a finite nonnegative integral. It specifies all five splits
  and all three pairings without an unspecified kernel. The total
  coefficient uses the multiplicities in~\eqref{E:total-four}.
\end{proposition}

\begin{proof}
  Direct integration on the two intervals gives
  \[
    \int_{\R^2}G(s,y)G(r,z)c_\alpha|y-z|^{-\alpha}\ud y\ud z
    =\frac{c_\alpha\big((s+r)^{2-\alpha}-|s-r|^{2-\alpha}\big)}
    {2(1-\alpha)(2-\alpha)}.
  \]
  Integrate on $s>r$ and double, set $v=s-r$, and integrate $r$ over
  $(0,t-v)$. This proves the second formula
  in~\eqref{E:riesz-two}. In the single-chain term with increments
  $r,v$, the spatial integral is $c_\alpha rv^{1-\alpha}/(1-\alpha)$.
  Thus, the remaining integral is
  $c_\alpha(1-\alpha)^{-1}\int_{r+v<t}rv^{1-\alpha-\alpha_0}\ud r\ud v$,
  which gives its first formula by two elementary integrations.

  For order four set each spatial increment equal to $h_lU_l$.
  The Green factor $\frac12\mathbf1_{[-h_l,h_l]}$ is $h_l$ times
  the law of $h_lU_l$. The map from increments to vertex positions is
  triangular within each chain with determinant one. Consequently,
  the four spatial integrals give exactly the product $\prod_lh_l$
  and the expectation in~\eqref{E:riesz-four}; the factors $1/16$ are
  already incorporated in the four uniform probability laws. The time
  increments give the domain $H_m$ and the differences $S_j-S_q$.
  Scaling time and space by $t$ contributes $t^8$ from the eight
  integrations and $t^{-2\alpha-2\alpha_0}$ from the two covariance
  factors, giving $t^{2\beta}$.

  Finiteness can be checked without a numerical argument. On the
  unit-time domain all vertex positions lie in $[-1,1]$. Enlarge the
  time domain to $[0,1]^4$ and the spatial domain to $[-1,1]^4$, and
  bound the Green indicators by one. The two time covariance factors
  involve disjoint pairs and are integrable since $\alpha_0<1$.
  The same is true of the two spatial factors since $\alpha<1$.
  Tonelli's theorem now gives a finite bound. This proves
  Proposition~\ref{P:riesz-small}.
\end{proof}

\begin{remark}[Normalization and static Riesz check]\label{R:riesz-static}
  The same integrable bound with any fixed exponent
  $\bar a\in(\alpha_0,1)$ permits $\alpha_0\downarrow0$ at these
  fixed orders. From~\eqref{E:riesz-two}, the static total-order-two
  coefficient is
  \[
    \frac{c_\alpha2^{3-\alpha}}
    {(1-\alpha)(2-\alpha)(3-\alpha)(4-\alpha)}.
  \]
  For example, the double integral of
  $(s+r)^{2-\alpha}-|s-r|^{2-\alpha}$ on $[0,1]^2$ is
  $(2^{4-\alpha}-4)/((3-\alpha)(4-\alpha))$, which verifies this value
  after adding twice the single-chain coefficient.
  If one chooses the normalization $c_\alpha=(1-\alpha)/2$, this
  coefficient tends to $1/3$ as $\alpha\uparrow1$, in agreement with
  the white-space value. More generally, at each fixed $\alpha_0\in(0,1)$
  the two normalized coefficients in~\eqref{E:riesz-two} tend to
  $c_0/2$ and $c_0$, respectively. For the second coefficient, the bracket
  at $t=1$ tends to $(1-v)^2$, the prefactor tends to $1/2$, and dominated
  convergence gives
  $\frac12\int_0^1v^{-\alpha_0}(1-v)^2\ud v=c_0$.
  The brackets are uniformly bounded for $\alpha$ near one, so
  $Cv^{-\alpha_0}$ is an integrable dominator. This is a finite-coefficient
  normalization check; unnormalized $|y|^{-\alpha}$ must not be identified
  with $\delta_0$.
\end{remark}

\subsection{Calibration table and limits of the finite-order test}

Let $M_2$ and $M_4$ denote only the total-order-two and total-order-four
contributions. The results above give
\[
  \begin{array}{c|c|c}
    \text{covariance and time regime}&M_2(t)&M_4(t)\\ \hline
    \delta_0,\quad0<\alpha_0<1
    &2c_0t^{3-\alpha_0}&t^{6-2\alpha_0}\,M_4(1)\\
    \delta_0,\quad\alpha_0=0
    &t^3/3&11t^6/540\\
    c_\alpha|y|^{-\alpha},\quad0<\alpha_0<1
    &t^\beta M_2(1)&t^{2\beta}M_4(1)\\
    c_\alpha|y|^{-\alpha},\quad\alpha_0=0
    &\displaystyle\frac{c_\alpha2^{3-\alpha}t^{4-\alpha}}
    {(1-\alpha)(2-\alpha)(3-\alpha)(4-\alpha)}
    &t^{8-2\alpha}M_4(1)
  \end{array}
\]
Here $c_0$ is defined in Lemma~\ref{L:white-test}; the fractional-time
white coefficient $M_4(1)$ is the explicit four-dimensional time integral
in~\eqref{E:white-four-table}, and the Riesz coefficients are specified
by~\eqref{E:riesz-two}--\eqref{E:riesz-four}. No closed form for those
remaining integrals is asserted.

\begin{remark}[What this gate tests]\label{R:G1-scope}
  The static exponent from the published Chen--Hu theorem is
  $(4-\alpha)/(3-\alpha)$; see~\cite{chen.hu:25:hyperbolic}*{Theorem~1.2,
  (1.9), p.~2147}. Both $\kappa$ and the G0 exponent $\rho$ have this
  boundary limit. The finite coefficient limits above are justified
  separately by dominated convergence; they do not exchange
  $t\to\infty$ and $\alpha_0\downarrow0$ and do not verify an
  asymptotic constant. In particular, the disputed printed white-space
  constant in the separate Chen--Hu source audit is not used here.
  The single-chain rows agree with the first-moment expansion, and all
  mixed rows are nonnegative, consistent with the Jensen comparison.
  Relative to the Skorohod expansion, the rows with self-pairings are present
  here and cannot be dropped: already $M_2=\E X_1^2+2\E X_2$.
  This is a structural comparison only, not a Skorohod result.
  Finally, any fixed truncation is a polynomial in $t^\beta$ with
  nonnegative coefficients, so its logarithm divided by $t^\kappa$
  tends to zero. Orders two and four can falsify a normalization or an
  incorrect pairing rule, but cannot determine an all-order factorial
  power or prove either principal goal.
\end{remark}

\section{G2 upper bounds for spatial exponents at most one}\label{S:d1-upper}

The upper bound at scale $t^\kappa$
is proved for $0<\alpha\le1$ in dimensions one, two and three under
the standing assumptions. The separate one-dimensional Riesz
estimates retain their sharper constants and white endpoint.
Degree-one covariance in dimensions two and three does not mean
full spatial white noise. Section~\ref{S:interval-upper} treats the
higher exponents by a separate argument. The intrinsic constant is
identified later in Theorem~\ref{T:intrinsic-second-moment}.

We retain the two-chain expansion of Proposition~\ref{P:mixed}, but
estimate its spatial and temporal factors in a different order. The
spatial estimate keeps a power of the number of pairs. After taking a
common spatial maximum, we sum all temporal pairings before using the
ordered time domains.

Throughout this section $0<\alpha_0<1$. We first work in dimension one
with either of the spatial covariances
\begin{equation}\label{E:d1-covariances}
  \begin{cases}
    \gamma(y)=c_\alpha|y|^{-\alpha},&0<\alpha<1,\quad c_\alpha>0,\\
    \gamma=c_\delta\delta_0,&\alpha=1,\quad c_\delta>0.
  \end{cases}
\end{equation}
Put $b=2-\alpha$, $q=3-\alpha$, $\beta=4-\alpha-\alpha_0$, and
\begin{equation}\label{E:d1-constants}
  Z=\frac{2}{(1-\alpha_0)(2-\alpha_0)},\qquad
  K_{\rm sp}=
  \begin{cases}
    \displaystyle\frac{c_\alpha 2^{2-\alpha}(1-\alpha)^{-\alpha}}
    {(2-\alpha)^{2-\alpha}},&0<\alpha<1,\\[2mm]
    c_\delta,&\alpha=1.
  \end{cases}
\end{equation}
These parameters satisfy Hypothesis~\ref{H:homog}, so the fixed-order
integrability and mixed expansion already established apply.

\subsection{A spatial bound retaining the ordered increments}

For $m+n=2k$, label the two chains in block order as in
\eqref{E:mixed-diagram}. For each vertex $l$ write
$h_l=s_l-s_{p(l)}>0$ and $y_l=x_l-x_{p(l)}$, with a separate root zero
in each chain. Thus, $x_l$ is the sum of increments in its own chain
up to label $l$. The spatial change of variables has determinant one.
In this section $x_l$ denotes a spatial position and $y_l$ its increment; this local
notation differs from the position variables $y_l$
in~\eqref{E:mixed-diagram}. The terminal evaluation point of $u(t,x)$
remains denoted by $x$.
Let $p_\epsilon$ be the centered Brownian Gaussian density of variance
$\epsilon$ and mass one, and set
$\gamma_\epsilon=p_\epsilon*\gamma$. Allow a separate positive
$\epsilon_e$ for every pair $e\in D$ and define
\[
  S_{D,\boldsymbol\epsilon}(h)
  =\int_{\R^{2k}}\prod_{l=1}^{2k}G(h_l,y_l)
  \prod_{(i,j)\in D}\gamma_{\epsilon_{i,j}}(x_j-x_i)\ud y,
  \qquad G(h,y)=\tfrac12\mathbf1_{\{|y|<h\}}.
\]
This is an ordinary nonnegative integral; no pointwise delta value is
used.

\begin{lemma}[Spatial estimate]\label{L:d1-spatial}
  Suppose~\eqref{E:d1-covariances} holds, $k\ge1$, and $D$ is any
  pairing of the two chains. Orient every pair $(i,j)$ by $i<j$ and
  let $O_D$ and $C_D$ be its opening and closing label sets. Then,
  uniformly in $\boldsymbol\epsilon$,
  \begin{equation}\label{E:d1-spatial-product}
    S_{D,\boldsymbol\epsilon}(h)\le
    \begin{cases}
      \displaystyle\left(\frac{c_\alpha}{1-\alpha}\right)^k
      \prod_{i\in O_D}h_i\prod_{j\in C_D}h_j^{1-\alpha},
      &0<\alpha<1,\\[2mm]
      \displaystyle\left(\frac{c_\delta}{2}\right)^k
      \prod_{i\in O_D}h_i,&\alpha=1.
    \end{cases}
  \end{equation}
  In particular, if $\sum_{l=1}^{2k}h_l\le2t$, then
  \begin{equation}\label{E:d1-spatial-max}
    S_{D,\boldsymbol\epsilon}(h)
    \le K_{\rm sp}^{\,k}\frac{t^{bk}}{k^{bk}}.
  \end{equation}
\end{lemma}

\begin{proof}
  We first record the convolution bounds. For $0<\alpha<1$, the
  integral of the even decreasing function $|y|^{-\alpha}$ over an
  interval of fixed length is maximal when the interval is centered
  at zero. Therefore,
  \[
    \sup_z\int_\R G(h,y)c_\alpha|y+z|^{-\alpha}\ud y
    =\frac{c_\alpha h^{1-\alpha}}{1-\alpha}.
  \]
  By Tonelli's theorem, the integral with $\gamma_\epsilon$ equals
  the $p_\epsilon(w)\ud w$ average of the unsmoothed integrals with
  shifts $z-w$. Its nonnegative mass-one average is therefore bounded
  by the same supremum. In the white case,
  $\gamma_\epsilon=c_\delta p_\epsilon$, so
  \[
    \sup_z\int_\R G(h,y)\gamma_\epsilon(y+z)\ud y
    \le\frac{c_\delta}{2}.
  \]
  Both estimates are uniform in $\epsilon>0$.

  Now integrate \emph{all} spatial increments in descending label
  order $2k,2k-1,\ldots,1$. Before processing label $l$, the remaining
  covariance factors are exactly those pairs whose closing labels are
  at most $l$; the bounds from the removed pairs depend only on $h$.
  If $l\in C_D$, its pair is $(i,l)$ with $i<l$ and
  $x_l-x_i=y_l+z$, where $z$ is independent of $y_l$. Every other
  remaining pair has both endpoints smaller than $l$, so its two
  positions are independent of $y_l$: positions involve only earlier
  increments in their own block chain. Thus, the only covariance
  involving $y_l$ is its own pair, and the convolution bound removes it.
  If $l\in O_D$, its partner has a larger label and its covariance
  factor has already been removed. All remaining covariances have
  endpoints smaller than $l$, so integration of $y_l$ gives only
  $\int G(h_l,y_l)\ud y_l=h_l$. This also preserves the stated
  invariant for the next label. Tonelli's theorem and the nonnegativity
  of all factors justify each step. There are $k$ labels of each type,
  proving~\eqref{E:d1-spatial-product} for every split and pairing.

  For Riesz covariance, weighted arithmetic--geometric mean gives
  \[
    \prod_{i\in O_D}h_i\prod_{j\in C_D}h_j^{1-\alpha}
    \le\left(\frac{2t}{bk}\right)^{bk}
    (1-\alpha)^{(1-\alpha)k}.
  \]
  Indeed, the weights are one at the $k$ openings and $1-\alpha$
  at the $k$ closings, with total $bk$, and the sum of the increments
  is at most $2t$. Multiplication by
  $(c_\alpha/(1-\alpha))^k$ gives~\eqref{E:d1-spatial-max} with
  the stated $K_{\rm sp}$. In the white case,
  $\prod_{i\in O_D}h_i\le(2t/k)^k$; multiplying by
  $(c_\delta/2)^k$ gives the same conclusion with $b=1$ and
  $K_{\rm sp}=c_\delta$. This proves Lemma~\ref{L:d1-spatial}.
\end{proof}

\subsection{Summing temporal pairings before using time ordering}

Define the total-order coefficients
\[
  A_k(t)=\sum_{m=0}^{2k}\E[X_m(t,x)X_{2k-m}(t,x)],\qquad A_0(t)=1.
\]
They do not depend on $x$, by spatial stationarity. By
Proposition~\ref{P:mixed}, $\E u^2(t,x)=\sum_{k\ge0}A_k(t)$.

\begin{proposition}[One-dimensional upper bound]\label{P:d1-upper}
  Under~\eqref{E:d1-covariances}, for every $k\ge1$ and $t>0$,
  \begin{equation}\label{E:d1-coefficient}
    A_k(t)\le
    \frac{(2ZK_{\rm sp})^k t^{\beta k}}{k!\,k^{bk}}
    \le\frac{(2ZK_{\rm sp})^k t^{\beta k}}{(k!)^q}.
  \end{equation}
  Consequently,
  \begin{equation}\label{E:d1-upper}
    \E u^2(t,x)\le\exp(C_2t^\kappa),\qquad
    C_2=q(2ZK_{\rm sp})^{1/q},\quad \kappa=\frac{\beta}{q}.
  \end{equation}
\end{proposition}

\begin{proof}
  We first work with the Gaussian spatial smoothing and temporal
  truncation in~\cite{chen:author2026:time-dependency}*{(2.9), (2.11),
  (2.23)--(2.24)}.
  Let $X_n^{\epsilon,\delta}$ be the smoothed Stratonovich term, using
  common parameters in every factor. Wick's formula expresses each
  mixed expectation of total order $2k$ as a sum over $D\in\Pi_k$.
  After the chain reversal in Proposition~\ref{P:mixed}, its spatial
  factor is the one in Lemma~\ref{L:d1-spatial}; its temporal factors
  are nonnegative and bounded by $|s_i-s_j|^{-\alpha_0}$. For times
  in $[0,t]^m_<\times[0,t]^{2k-m}_<$, the increments sum to the two
  terminal times and therefore to at most $2t$.
  Extract~\eqref{E:d1-spatial-max}, which is independent of the
  time vector, the split, the pairing, and the smoothing parameters.
  The remaining temporal sum is
  \[
    F_k(s_1,\ldots,s_{2k})
    =\sum_{D\in\Pi_k}\prod_{(i,j)\in D}|s_i-s_j|^{-\alpha_0}.
  \]
  Every permutation of the $2k$ labels bijects $\Pi_k$, so $F_k$ is
  fully symmetric. Moreover,
  \[
    \int_{[0,t]^2}|s-r|^{-\alpha_0}\ud s\ud r
    =Zt^{2-\alpha_0},\qquad
    \int_{[0,t]^{2k}}F_k(s)\ud s
    =P_k(Zt^{2-\alpha_0})^k<\infty.
  \]
  The second equality uses the disjoint endpoints of every pairing.
  Partitioning the time cube according to the order within each block
  now gives
  \begin{equation}\label{E:d1-time-symmetry}
    \int_{[0,t]^m_<\times[0,t]^{2k-m}_<}F_k(s)\ud s
    =\frac{P_k(Zt^{2-\alpha_0})^k}{m!(2k-m)!}.
  \end{equation}
  Ties have measure zero. Crucially, this symmetry is applied to the
  \emph{sum} of pairings after taking the common spatial bound, not
  to an individual temporally weighted diagram.

  The number of pairings obeys $P_0=1$ and
  $P_k=(2k-1)P_{k-1}$, by choosing the partner of the smallest label.
  Hence, $P_k=(2k)!/(2^kk!)$. The binomial identity gives
  \[
    \sum_{m=0}^{2k}\frac1{m!(2k-m)!}=\frac{2^{2k}}{(2k)!}.
  \]
  Multiplying~\eqref{E:d1-time-symmetry} by the spatial bound and
  summing over $m$ yields
  \[
    \sum_{m=0}^{2k}\E[X_m^{\epsilon,\delta}X_{2k-m}^{\epsilon,\delta}]
    \le K_{\rm sp}^{\,k}\frac{t^{bk}}{k^{bk}}
    \frac{2^{2k}}{(2k)!}
    \frac{(2k)!}{2^kk!}(Zt^{2-\alpha_0})^k
    =\frac{(2ZK_{\rm sp})^kt^{\beta k}}{k!\,k^{bk}}.
  \]
  The same proof covers empty chains, with $X_0^{\epsilon,\delta}=1$.

  By Lemma~\ref{L:joint-fixed-order}, each smoothed factor converges
  in $L^2$.
  Products converge in $L^1$ by Cauchy--Schwarz; for fixed $k$ the sum
  over splits is finite. The bound is uniform in $\epsilon,\delta$,
  so it passes to $A_k(t)$. Since $k!\le k^k$ and $b>0$, we have
  $k!\,k^{bk}\ge(k!)^{b+1}=(k!)^q$, proving both inequalities
  in~\eqref{E:d1-coefficient}.

  Finally, for $z\ge0$ and $q\ge1$,
  \[
    \sum_{k\ge0}\frac{z^k}{(k!)^q}
    =\sum_{k\ge0}\left(\frac{z^{k/q}}{k!}\right)^q
    \le\left(\sum_{k\ge0}\frac{z^{k/q}}{k!}\right)^q
    =\exp(qz^{1/q}).
  \]
  Apply this inequality with $z=2ZK_{\rm sp}t^\beta$, adding the
  separately defined term $A_0=1$. Proposition~\ref{P:mixed} then
  gives~\eqref{E:d1-upper}. This proves Proposition~\ref{P:d1-upper}.
\end{proof}

\subsection{Spectral bounds for $0<\alpha\le1$ in all three dimensions}

We now retain Hypothesis~\ref{H:homog} with $d\in\{1,2,3\}$ and
$0<\alpha\le1$. The covariance is nonnegative and nonnegative definite
as in Section~\ref{S:model}; when it is a distribution, both these
properties and its homogeneity are understood distributionally.
Let $\mu$ be its positive Radon spectral measure in the convention
$\gamma(x)=\int e^{i\xi\cdot x}\mu(\ud\xi)$, and put
$V=\mu(\{\xi:|\xi|\le1\})$. No isotropy or spectral density is assumed.
Write $G_h$ for the positive wave-kernel measure of mass $h$, and
$G_{h,\eta}=p_\eta*G_h$ for $\eta>0$; set $G_{h,0}=G_h$.
The measure notation includes the sphere kernel in dimension three.
The mixed-moment definition of $A_k(t)$ is now applied to the present
$d$-dimensional solution.

\begin{lemma}[Low-$\alpha$ convolution bound]\label{L:low-alpha-convolution}
  Under the preceding assumptions with $0<\alpha<1$, for every $R,h>0$,
  \begin{equation}\label{E:low-alpha-radial}
    \mu(\{\xi:|\xi|\le R\})=VR^\alpha,\qquad
    \int_{\R^d}\min\{h,|\xi|^{-1}\}\mu(\ud\xi)
    =\frac{V}{1-\alpha}h^{1-\alpha}.
  \end{equation}
  For $\epsilon>0$ and $\eta\ge0$,
  \begin{equation}\label{E:low-alpha-convolution}
    0\le\int_{\R^d}G_{h,\eta}(\ud y)\gamma_\epsilon(y+z)
    \le\frac{V}{1-\alpha}h^{1-\alpha},
    \qquad z\in\R^d.
  \end{equation}
  The estimate is uniform in both smoothing parameters and in $z$.
\end{lemma}

\begin{proof}
  The spectral measure of $\gamma(c\,\cdot)$ is the pushforward of
  $\mu$ under $\xi\mapsto c\xi$. Homogeneity and
  uniqueness of the Fourier transform on tempered distributions
  therefore give $\mu(A/c)=c^{-\alpha}\mu(A)$ for every Borel set $A$.
  Equivalently, $\mu(cA)=c^\alpha\mu(A)$. This proves the ball-mass
  formula. Since $\mu$ is Radon, $V<\infty$, and continuity from above
  gives $\mu(\{0\})=\lim_{R\downarrow0}VR^\alpha=0$.
  By the layer-cake identity and Tonelli's theorem,
  \[
    \int_{\R^d}\min\{h,|\xi|^{-1}\}\mu(\ud\xi)
    =\int_0^h\mu(\{\xi:|\xi|\le u^{-1}\})\ud u
    =V\int_0^h u^{-\alpha}\ud u.
  \]
  The endpoint of each indicator has no effect on its $u$ integral.
  Since $\alpha<1$, the last expression is the finite quantity
  in~\eqref{E:low-alpha-radial}. This computation uses ball masses,
  not a radial density for $\mu$.

  Gaussian weighting gives a finite measure, by the polynomial ball
  growth of $\mu$. Thus, Fourier Fubini is justified for $\gamma_\epsilon$
  and the finite measure $G_{h,\eta}$. From the source's wave-kernel
  formulas~\cite{chen:author2026:time-dependency}*{(2.3)--(2.5), p.~7},
  \[
    \widehat G_h(\xi)=\frac{\sin(h|\xi|)}{|\xi|},\qquad
    G_h(\R^d)=h,
  \]
  with value $h$ in the Fourier formula at zero. The Fourier multipliers
  of $p_\epsilon$ and $p_\eta$ have absolute value at most one, with
  the latter multiplier equal to one when $\eta=0$. Consequently,
  \[
    \left|\int G_{h,\eta}(\ud y)\gamma_\epsilon(y+z)\right|
    \le\int_{\R^d}\frac{|\sin(h|\xi|)|}{|\xi|}\mu(\ud\xi)
    \le\int_{\R^d}\min\{h,|\xi|^{-1}\}\mu(\ud\xi).
  \]
  Nonnegativity of $\gamma$ as a distribution implies
  $\gamma_\epsilon\ge0$, since Gaussian translates are nonnegative
  test functions; $G_{h,\eta}$ is also nonnegative. This proves the
  lower bound in~\eqref{E:low-alpha-convolution}. Combining the
  preceding displays proves its upper bound. No positivity of the
  oscillatory Fourier integrand is asserted. This proves
  Lemma~\ref{L:low-alpha-convolution}.
\end{proof}

\begin{lemma}[Degree-one convolution bound]\label{L:alpha-one-convolution}
  Under the preceding covariance assumptions with $\alpha=1$, for
  every $h>0$, $\epsilon>0$, $\eta\ge0$, and $z\in\R^d$,
  \begin{equation}\label{E:alpha-one-convolution}
    0\le\int_{\R^d}G_{h,\eta}(\ud y)\gamma_\epsilon(y+z)
    \le\frac{\pi V}{2}.
  \end{equation}
  No isotropy or angular density is required.
\end{lemma}

\begin{proof}
  Fourier uniqueness, applied to the distributional homogeneity as
  above, gives $\mu(cA)=c\mu(A)$ and $\mu(\{0\})=0$.
  Define a finite measure on the unit sphere by
  \[
    \sigma(E)=\mu\{\xi:0<|\xi|\le1,\ \xi/|\xi|\in E\}.
  \]
  Its total mass is $V$. Homogeneity implies that the corresponding
  sector of radius $R$ has mass $R\sigma(E)$. Subtracting two such
  sectors shows that a polar rectangle $(r_1,r_2]\times E$ has mass
  $(r_2-r_1)\sigma(E)$. Uniqueness of measures on these generating
  rectangles therefore gives the polar decomposition
  $\mu(\ud\xi)=\ud r\,\sigma(\ud\theta)$, $r>0$,
  $\theta\in\mathbb S^{d-1}$. The real stationary covariance is
  even; Fourier uniqueness makes $\mu$, and hence $\sigma$, even.

  Use the Brownian Gaussian convention, so the combined covariance
  and Green smoothing multiplier is $e^{-ar^2}$ with
  $a=(\epsilon+\eta)/2>0$. Gaussian weighting makes the spectral
  measure finite. Fourier Fubini and evenness give
  \begin{equation}\label{E:alpha-one-polar}
    \begin{split}
      \int G_{h,\eta}(\ud y)\gamma_\epsilon(y+z)
      &=\int_{\mathbb S^{d-1}} I_a(h,\theta\cdot z)\sigma(\ud\theta),\\
      I_a(h,v)&=\int_0^\infty e^{-ar^2}
      \frac{\sin(hr)}r\cos(rv)\ud r.
    \end{split}
  \end{equation}
  The radial integral is absolutely convergent: its integrand is
  bounded near zero and Gaussian-decaying at infinity. Passing from
  the complex exponential to cosine introduces no factor two, since
  both antipodal directions are already included in $\sigma$.

  Let $g_h(v)=\tfrac12\mathbf1_{\{|v|<h\}}$ and let
  $p_{2a}^{(1)}(v)=(4\pi a)^{-1/2}e^{-v^2/(4a)}$ be the
  one-dimensional Gaussian density. Their Fourier transforms are
  $\sin(hr)/r$ and $e^{-ar^2}$. The one-dimensional inversion factor
  is $1/(2\pi)$ in the source convention, so
  \[
    (g_h*p_{2a}^{(1)})(v)
    =\frac1{2\pi}\int_\R e^{irv}e^{-ar^2}
    \frac{\sin(hr)}r\ud r
    =\frac1\pi I_a(h,v).
  \]
  The sign in the inversion exponential is immaterial because the
  integrand pairs evenly under $r\mapsto-r$. Since $p_{2a}^{(1)}$
  has mass one and $0\le g_h\le1/2$, we obtain
  $0\le I_a(h,v)\le\pi/2$. Integrating against $\sigma$, whose mass
  is $V$, proves~\eqref{E:alpha-one-convolution}. This retains the
  oscillation until the one-dimensional integral is evaluated; the
  divergent absolute Fourier envelope at $\alpha=1$ is not used.
  This proves Lemma~\ref{L:alpha-one-convolution}.
\end{proof}

\begin{proposition}[Upper bound for $\alpha\le1$]\label{P:low-alpha-upper}
  Suppose that Hypothesis~\ref{H:homog} and the standing covariance
  positivity assumptions hold, $d\in\{1,2,3\}$, $0<\alpha\le1$,
  and $V>0$. Define
  \begin{equation}\label{E:low-alpha-constants}
    \begin{split}
      K_{\rm sp}^{\rm gen}
      &=\begin{cases}
        \displaystyle\frac{V2^{2-\alpha}(1-\alpha)^{-\alpha}}
        {(2-\alpha)^{2-\alpha}},&0<\alpha<1,\\[2mm]
        \pi V,&\alpha=1,
      \end{cases}\\
      C_2^{\rm gen}&=q(2ZK_{\rm sp}^{\rm gen})^{1/q}.
    \end{split}
  \end{equation}
  With the same $A_k$, $b$, $q$, $\beta$, and $Z$ as above, for
  $k\ge1$ and $t>0$,
  \begin{equation}\label{E:low-alpha-coefficient}
    A_k(t)\le\frac{(2ZK_{\rm sp}^{\rm gen})^k t^{\beta k}}
    {k!\,k^{bk}}
    \le\frac{(2ZK_{\rm sp}^{\rm gen})^k t^{\beta k}}{(k!)^q},
    \qquad
    \E u^2(t,x)\le\exp(C_2^{\rm gen}t^\kappa).
  \end{equation}
\end{proposition}

\begin{proof}
  First smooth the noise as in
  \cite{chen:author2026:time-dependency}*{(2.9), (2.11), (2.23)--(2.24)}.
  In dimension three also use $G_{h,\eta}$ with $\eta>0$, as in the
  source's pp.~13--14. The increment change of variables is now a
  triangular map on vectors in $\R^d$, still of determinant one.
  The descending-label proof of Lemma~\ref{L:d1-spatial} depends only
  on which increments enter each position, not on their dimension.
  Its invariant therefore remains valid: at a closing label there
  is exactly one covariance depending on that vector increment, and
  at an opening label its pair has already been removed.
  If $0<\alpha<1$, Lemma~\ref{L:low-alpha-convolution} gives the
  closing bound $Mh_l^{1-\alpha}$ with $M=V/(1-\alpha)$.
  At $\alpha=1$, Lemma~\ref{L:alpha-one-convolution} gives the
  constant closing bound $M=\pi V/2$. Every opening gives mass
  $h_l$, uniformly in $\eta$ and all noise-smoothing parameters.
  For $\alpha<1$, the same weighted arithmetic--geometric mean
  calculation gives
  \[
    M^k\prod_{i\in O_D}h_i\prod_{j\in C_D}h_j^{1-\alpha}
    \le (K_{\rm sp}^{\rm gen})^k\frac{t^{bk}}{k^{bk}}.
  \]
  At $\alpha=1$, ordinary arithmetic--geometric mean on the $k$
  opening increments gives
  $M^k\prod_{i\in O_D}h_i\le(2M)^kt^k/k^k$, which is the same
  bound with $b=1$ and $K_{\rm sp}^{\rm gen}=\pi V$.
  Both cases use $\sum_lh_l\le2t$. For $d=1,2$ one may use the
  Green densities directly; their opening mass and closing
  convolution obey these same bounds.

  Replace the nonnegative truncated temporal factors by
  $|s_i-s_j|^{-\alpha_0}$ before taking their pairing sum. The temporal
  symmetry, cube integral and split count
  in~\eqref{E:d1-time-symmetry} do not involve the spatial dimension.
  Thus, exactly the multiplication of counts in the proof of
  Proposition~\ref{P:d1-upper} gives the first bound
  in~\eqref{E:low-alpha-coefficient} for the regularized moments.

  We spell out the limit in dimension three. Fix every noise-smoothing
  parameter and first let $\eta\downarrow0$. At each time vector,
  the Gaussian moment formula is a finite sum of bounded continuous
  products of the smoothed covariance functions, integrated against
  products of the finite Green measures. These products of measures
  converge weakly as $\eta\downarrow0$, with the same masses
  $\prod_l h_l$. At fixed noise smoothing the Gaussian covariance
  factors are uniformly bounded, so a constant times $\prod_lh_l$
  dominates on each bounded time simplex. Dominated convergence
  applies also to the covariance between two approximations with
  different $\eta$ values. The resulting common joint covariance
  limit proves the $L^2$ Cauchy property of each fixed-order random
  integral. This is the inner limit used in the source's definition
  on pp.~13--14. Products of two factors converge in $L^1$ by
  Cauchy--Schwarz, so the moment inequality survives this limit.
  Next send the noise-smoothing parameters to zero using the
  fixed-order $L^2$ convergence of Lemma~\ref{L:joint-fixed-order}, and again
  pass products in $L^1$. In dimensions one and two only the latter
  limit is required. The bounds at both stages are uniform.

  We have proved the first coefficient bound for $A_k(t)$. The
  factorial inequality and nonnegative-series argument in
  Proposition~\ref{P:d1-upper} apply unchanged, with
  $K_{\rm sp}^{\rm gen}$ in place of $K_{\rm sp}$ and $A_0=1$.
  This proves Proposition~\ref{P:low-alpha-upper}.
\end{proof}

\begin{remark}[Scope of the spectral estimates]\label{R:low-alpha-scope}
  If $V=0$, spectral homogeneity gives $\mu(B_R)=0$ for every $R$,
  hence $\mu=0$ and $u=1$; the noise-free conclusion is immediate.
  Otherwise, all angular and dimensional dependence is allowed in
  $V$. For $0<\alpha<1$, the example
  $\gamma(x)=c|x_1|^{-\alpha}$ in dimensions two or three has its
  spectral measure supported on an axis; a full-dimensional density
  is not required. The absolute Fourier envelope diverges at
  $\alpha=1$, where the separate oscillatory calculation in
  Lemma~\ref{L:alpha-one-convolution} is essential. The endpoint is
  not obtained by taking a limit in $K_{\rm sp}^{\rm gen}$ for
  $\alpha<1$. For $d=1$ and $\gamma=c_\delta\delta_0$, the source
  convention gives $\mu(\ud\xi)=c_\delta\ud\xi/(2\pi)$ and
  $V=c_\delta/\pi$. Hence, the endpoint constant
  $K_{\rm sp}^{\rm gen}=\pi V=c_\delta$ agrees exactly with
  Proposition~\ref{P:d1-upper}, with no extra antipodal factor.
  In dimensions two and three the endpoint covers degree-one
  homogeneous covariance, not full spatial white noise. No result
  for $\alpha>1$ follows from these estimates.
\end{remark}

\subsection{Checks on the scale, constants and scope}

\begin{corollary}[First-moment calibration]\label{C:d1-first-calibration}
  Let $K_*$ be $K_{\rm sp}$ under~\eqref{E:d1-covariances}, or
  $K_{\rm sp}^{\rm gen}$ under the hypotheses of
  Proposition~\ref{P:low-alpha-upper}. Put
  $C_{2,*}=q(2ZK_*)^{1/q}$. Then
  \begin{equation}\label{E:d1-first-calibration}
    \E u(t,x)\le\exp(C_{1,*}t^\kappa),\qquad
    C_{1,*}=q\left(\frac{ZK_*}{2^{3-\alpha}}\right)^{1/q}
    =\frac{C_{2,*}}{2^{(4-\alpha)/(3-\alpha)}}.
  \end{equation}
  In either nonzero case $2C_{1,*}<C_{2,*}$.
  Conditionally on a first-moment lower rate at least $L_*$,
  $2L_*\le2C_{1,*}<C_{2,*}$, consistently with
  Proposition~\ref{P:Jensen}.
\end{corollary}

\begin{proof}
  For one chain of length $2k$, the increments sum to at most $t$.
  The spatial estimate in Lemma~\ref{L:d1-spatial}, or in the proof
  of Proposition~\ref{P:low-alpha-upper}, therefore applies with
  $t/2$ in place of $t$. The temporal pairing sum on one ordered
  simplex is $P_k(Zt^{2-\alpha_0})^k/(2k)!$.
  Using the same regularization and limit order as in the respective
  upper-bound proof gives
  \[
    \E X_{2k}(t,x)
    \le\frac{(ZK_*/2^{b+1})^k t^{\beta k}}{k!\,k^{bk}}
    \le\frac{(ZK_*/2^{3-\alpha})^k t^{\beta k}}{(k!)^q}.
  \]
  Every odd term has zero expectation. The $L^2$ expansion permits
  taking expectations of partial sums, and the resulting nonnegative
  even series is summed by the scalar inequality in the proof of
  Proposition~\ref{P:d1-upper}. This gives~\eqref{E:d1-first-calibration}.
  If the first-moment lower rate is at least $L_*$,
  \eqref{E:d1-first-calibration} implies $L_*\le C_{1,*}$.
  In the stated nonzero cases $K_*>0$, hence
  $C_{1,*}>0$; and $(4-\alpha)/(3-\alpha)>1$ gives
  $2C_{1,*}<C_{2,*}$. This proves
  Corollary~\ref{C:d1-first-calibration}.
\end{proof}

\begin{remark}[Checks and relation to G0]\label{R:d1-upper-checks}
  The argument preserves the factor $k^{-(2-\alpha)k}$ from the
  spatial increment maximum. Replacing the spatial volume merely by
  a constant times $t^{(2-\alpha)k}$ would lose the factorial power
  needed in~\eqref{E:d1-coefficient}. This proof does not use the
  common-Laplace-parameter norm majorant of
  Proposition~\ref{P:envelope}, and it does not assert a stronger
  factorial estimate for every individual diagram. Instead, the
  temporal ordering is exploited after summing pairings in
  \eqref{E:d1-time-symmetry}. Thus, the scoped G0 obstruction remains
  valid. For unit white covariance, the bound on the total-order-two
  coefficient is $2Z$, whereas the exact value from
  Lemma~\ref{L:white-test} is $2c_0$; their ratio is
  $2(3-\alpha_0)>4$. At the static endpoint the exact order-four
  coefficient is $11/540$, while the first bound
  in~\eqref{E:d1-coefficient} gives $1/2$.
  These are checks of normalization, not evidence of sharp constants.
\end{remark}

\begin{remark}[Boundary and literature comparisons]\label{R:d1-comparisons}
  As $\alpha_0\downarrow0$, the time exponent tends to
  $(4-\alpha)/(3-\alpha)$, the Chen--Hu static exponent cited in
  Remark~\ref{R:G1-scope}. This is an exponent calibration, not an
  interchange of the static and large-time limits. With the Riesz
  normalization $c_\alpha=(1-\alpha)/2$, the displayed $K_{\rm sp}$
  tends to one as $\alpha\uparrow1$, matching unit white covariance.
  For comparison only, the Skorohod upper bound of
  Balan--Conus~\cite{balan.conus:16:intermittency}*{Theorem~2.1(b),
  (8), (10), p.~1492} has time exponent $(2H+2-a)/(3-a)$.
  Setting $H=1-\alpha_0/2$ and $a=\alpha$ yields the same $\kappa$.
  Their covariance normalization contains $H(2H-1)$ and they use a
  Skorohod mild solution. No constants or solutions are identified,
  and their theorem is not an input to the present proof. The current
  coverage of this section is $0<\alpha\le1$ in $d=1,2,3$, including
  the one-dimensional white case. It does not address
  $1<\alpha<2-\alpha_0$ in dimensions two and three.
\end{remark}

\section{Higher spatial exponents under a convolution bound}
\label{S:higher-alpha}

The convolution assumption below is additional to homogeneity, and the
concrete applications cover only the stated Riesz ranges.
Section~\ref{S:interval-upper} establishes the full general upper scale
by a separate argument. This alternative route is not an input to
Theorem~\ref{T:intrinsic-second-moment}.

We retain the standing covariance assumptions and take $d\in\{2,3\}$ and
$1<\alpha<2-\alpha_0$. Put $\delta=\alpha-1$, $q=3-\alpha$, and
$\beta=4-\alpha-\alpha_0$. Here $\delta$ is an exponent, not a smoothing
parameter. Write $p_\epsilon$ for the centered Gaussian density with
covariance $\epsilon I$, $\gamma_\epsilon=p_\epsilon*\gamma$, and
$G_{h,\eta}=p_\eta*G_h$, with $G_{h,0}=G_h$.

\begin{hypothesis}[Spatial maximum]\label{H:spatial-maximum}
  There is $M>0$ such that, for every $h>0$, $z\in\R^d$,
  $\epsilon>0$, and $\eta\ge0$,
  \begin{equation}\label{E:higher-convolution}
    0\le\int_{\R^d}G_{h,\eta}(\ud y)\gamma_\epsilon(y+z)
    \le M h^{-\delta}.
  \end{equation}
  The same $M$ works for all translations and both Gaussian widths.
  In particular, each pairing edge may have its own positive covariance
  width and each Green factor its own nonnegative smoothing width.
\end{hypothesis}

\begin{proposition}[Conditional upper bound]\label{P:higher-transfer}
  Suppose that Hypotheses~\ref{H:homog} and~\ref{H:spatial-maximum}
  hold in the range specified above. Choose and fix
  \[
    \frac1{1-\alpha_0}<r<\frac1\delta,\qquad
    r'=\frac r{r-1},\qquad \theta=\alpha_0r',\qquad
    a=1-\frac{\delta r}{2}.
  \]
  Define the explicit, nonsharp constants
  \begin{equation}\label{E:higher-constants}
    Z_\theta=\frac2{(1-\theta)(2-\theta)},\qquad
    D_a=e^2(e/a)^{2a},\qquad
    K=12M[\Gamma(1-\delta r)D_a]^{1/r}Z_\theta^{1/r'}.
  \end{equation}
  For the total-order coefficients $A_k(t)$ of Section~\ref{S:d1-upper},
  \begin{equation}\label{E:higher-bound}
    A_k(t)\le\frac{K^kt^{\beta k}}{(k!)^q}\quad(k\ge1),
    \qquad \E u^2(t,x)\le\exp\{qK^{1/q}t^\kappa\}.
  \end{equation}
  These estimates hold for every $t>0$ and $x\in\R^d$.
\end{proposition}

\begin{proof}
  The interval for $r$ is nonempty because $\delta+\alpha_0<1$.
  Thus, $\delta r<1$, $\theta<1$, and $1/2<a<1$.
  We use the source's noise regularization from
  Chen~\cite{chen:author2026:time-dependency}*{(2.9), (2.11),
  (2.23)--(2.24)}, as in Section~\ref{S:d1-upper}. Its nonnegative
  temporal covariance is bounded by $|s_i-s_j|^{-\alpha_0}$, and its
  spatial covariance on an edge $e$ is
  $\gamma_{\epsilon_e+\epsilon'_e}$, where $\epsilon_e,\epsilon'_e>0$
  are the two endpoint noise widths. Indeed,
  $p_{\epsilon_e}*p_{\epsilon'_e}=p_{\epsilon_e+\epsilon'_e}$;
  equal widths give the source's $\gamma_{2\epsilon}$.
  Every such positive covariance width is covered by
  Hypothesis~\ref{H:spatial-maximum}. In dimension three first smooth
  the Green measures as prescribed on pp.~13--14 of that source.

  Fix $m+n=2k$, $k\ge1$, and put
  $\Omega_{m,n}=[0,t]^m_<\times[0,t]^n_<$.
  Use the two separate roots and increments $h_l=s_l-s_{p(l)}$ of
  Section~\ref{S:d1-upper}. For $D\in\Pi_k$, orient its pairs by
  increasing block label and denote their opening and closing sets by
  $O_D,C_D$. Descending integration of the vector increments gives
  \[
    S_D(h)\le M^k\prod_{i\in O_D}h_i\prod_{j\in C_D}h_j^{-\delta}
    \le M^k(2t/k)^k H_D(h),\qquad
    H_D(h)=\prod_{j\in C_D}h_j^{-\delta}.
  \]
  Indeed, before label $l$ is integrated, the remaining covariances have
  closing labels at most $l$. At a closing label exactly its own pair
  depends on that increment, as $\gamma_\epsilon(y_l+z)$; all other
  endpoints have smaller labels. Hypothesis~\ref{H:spatial-maximum}
  removes this factor. At an opening its pair is already removed and
  the integral is the Green mass $h_l$. This proves the invariant in
  every dimension and for empty chains. Tonelli applies by positivity.
  Finally, the $k$ opening increments sum to at most $2t$, so ordinary
  arithmetic--geometric mean gives the second inequality. We have not
  applied the low-$\alpha$ conclusion of Lemma~\ref{L:d1-spatial}.

  Set $T_D(s)=\prod_{(i,j)\in D}|s_i-s_j|^{-\alpha_0}$.
  H\"older's inequality on counting measure on $\Pi_k$ times Lebesgue
  measure on $\Omega_{m,n}$ gives
  \begin{equation}\label{E:higher-holder}
    \sum_D\int_{\Omega_{m,n}}H_DT_D\ud s
    \le\left(\sum_D\int_{\Omega_{m,n}}H_D^r\ud s\right)^{1/r}
    \left(\sum_D\int_{\Omega_{m,n}}T_D^{r'}\ud s\right)^{1/r'}.
  \end{equation}
  Both integrals are finite by the following computations. If the two
  chains contain $k_1,k_2$ closing labels, then $k_1+k_2=k$ and the
  simplex change to increments has determinant one. The Dirichlet
  integral, including the unused terminal gap with exponent zero, gives
  \[
    \int_{\Omega_{m,n}}H_D^r\ud s
    =\frac{\Gamma(1-\delta r)^k t^{(2-\delta r)k}}
    {\Gamma(1+m-\delta r k_1)\Gamma(1+n-\delta r k_2)}.
  \]
  To see the normalization, in a chain of length $m$ the $k_1$ closing
  increments have Dirichlet parameter $1-\delta r$, the other increments
  have parameter one, and the terminal gap has parameter one. Scaling
  gives $t^{m-\delta r k_1}$. Iterating the beta integral gives the
  displayed Gamma quotient. Empty chains contribute $\Gamma(1)=1$.
  The two denominator arguments are positive and have average $1+ak$.
  Log convexity of $\Gamma$ therefore bounds their product below by
  $\Gamma(1+ak)^2$. An elementary lower bound makes the constant explicit:
  \[
    \Gamma(1+ak)\ge\int_{ak}^{ak+1}x^{ak}e^{-x}\ud x
    \ge e^{-1}(a/e)^{ak}k^{ak}
    \ge e^{-1}(a/e)^{ak}(k!)^a.
  \]
  Since $k\ge1$, its square is at least
  $D_a^{-k}(k!)^{2-\delta r}$. Writing $P_k=|\Pi_k|$, we obtain
  \[
    \sum_D\int_{\Omega_{m,n}}H_D^r\ud s
    \le\frac{P_k[\Gamma(1-\delta r)D_a]^k
    t^{(2-\delta r)k}}{(k!)^{2-\delta r}}.
  \]
  The sum $\sum_DT_D^{r'}$ is symmetric in all $2k$ time labels,
  because a permutation bijects the pairings. On the full cube each
  pairing has integral $(Z_\theta t^{2-\theta})^k$. Therefore,
  \[
    \sum_D\int_{\Omega_{m,n}}T_D^{r'}\ud s
    =\frac{P_k(Z_\theta t^{2-\theta})^k}{m!n!}
    \le\frac{P_k(Z_\theta t^{2-\theta})^k}{(k!)^2}.
  \]
  Here $m!n!\ge(k!)^2$ since $m+n=2k$. Symmetry is used only for
  the pairing sum, not for an individual diagram. Also,
  $P_k=\prod_{j=1}^k(2j-1)\le2^kk!$ and $k^k\ge k!$.
  Combining these bounds with~\eqref{E:higher-holder} and the opening
  estimate proves, uniformly in all regularization parameters,
  \[
    \sum_D\int_{\Omega_{m,n}}S_D T_D\ud s
    \le\frac{\{4M[\Gamma(1-\delta r)D_a]^{1/r}
    Z_\theta^{1/r'}\}^k t^{\beta k}}{(k!)^q}.
  \]
  Indeed, the time power is
  $1+(2-\delta r)/r+(2-\theta)/r'=3-\delta-\alpha_0=\beta$;
  the factorial power is
  $1+(2-\delta r)/r+2/r'-1=2-\delta=q$.
  There are $2k+1\le3^k$ splits, giving the asserted $K$.

  We now pass to the solution using the independent fixed-order
  construction in Lemma~\ref{L:joint-fixed-order}, which applies under
  Hypothesis~\ref{H:homog}. In dimension
  three, fix the noise smoothing first and send the Green smoothing
  to zero. Smoothed spatial covariances are bounded and continuous.
  Products of the finite Green measures converge weakly, with masses
  $\prod_lh_l$. At fixed noise smoothing all covariance factors are
  bounded, so a constant times $\prod_lh_l$ dominates the time
  integrals on bounded simplexes. The same argument for mixed Green
  approximations gives a common joint covariance limit, and hence the
  fixed-order $L^2$ Cauchy property. This is the inner limit of the
  source's pp.~13--14, detailed in Proposition~\ref{P:low-alpha-upper}.
  Next remove the noise smoothing using Lemma~\ref{L:joint-fixed-order}'s
  fixed-order $L^2$ convergence. In dimension two only this latter limit is needed.
  At each stage products converge in $L^1$, since
  \[
    \|YZ-Y'Z'\|_1
    \le\|Y-Y'\|_2\|Z\|_2+\|Y'\|_2\|Z-Z'\|_2.
  \]
  Each split sum is finite and the bound is uniform. Thus, it passes
  to $A_k(t)$; zero chains remain the constant one. These convergence
  inputs use the standing assumptions, not $\alpha\le1$.

  Finally, Proposition~\ref{P:mixed} supplies the nonnegative full
  series under these same hypotheses. Since $q>1$, for $z\ge0$,
  \[
    \sum_{k\ge0}\frac{z^k}{(k!)^q}
    =\sum_{k\ge0}\left(\frac{z^{k/q}}{k!}\right)^q
    \le\left(\sum_{k\ge0}\frac{z^{k/q}}{k!}\right)^q
    =e^{qz^{1/q}}.
  \]
  Take $z=Kt^\beta$ and use $A_0=1$ and $\beta/q=\kappa$.
  This proves Proposition~\ref{P:higher-transfer}.
\end{proof}

% This lemma discharges H:spatial-maximum only for its explicitly stated
% isotropic Riesz ranges.
\begin{lemma}[Riesz spatial maxima]\label{L:higher-riesz}
  Let $\gamma(x)=c|x|^{-\alpha}$, $c>0$. In dimension three, for
  $1<\alpha<2$, Hypothesis~\ref{H:spatial-maximum} holds with the
  optimal uniform constant $M_3=c2^{1-\alpha}/(2-\alpha)$.
  In dimension two, for $1<\alpha<3/2$, it holds with
  \[
    M_2=c\left\{4^\alpha+
    \frac{2\alpha}{3/2-\alpha}4^{\alpha-3/2}\right\}.
  \]
\end{lemma}

\begin{proof}
  From Chen~\cite{chen:author2026:time-dependency}*{(2.5), p.~7},
  the wave measures are
  \[
    G_h^{(2)}(\ud y)=\frac{\mathbf1_{\{|y|<h\}}\ud y}
    {2\pi\sqrt{h^2-|y|^2}},\qquad
    G_h^{(3)}(\ud y)=\frac{\sigma_h(\ud y)}{4\pi h},
  \]
  where $\sigma_h$ is surface measure on the sphere of radius $h$.
  Both have mass $h$ and satisfy $G_h(hA)=hG_1(A)$. Thus, the
  unsmoothed convolution is $ch^{1-\alpha}F_d(z/h)$, where
  $F_d(w)=\int G_1^{(d)}(\ud y)|y+w|^{-\alpha}$.
  In dimension three spherical coordinates give, for $\rho=|w|>0$,
  \[
    F_3(w)=\frac{(1+\rho)^v-|1-\rho|^v}{2v\rho},
    \qquad v=2-\alpha\in(0,1).
  \]
  For $0<\rho<1$ this is the average of the convex function
  $f(s)=(1+s)^{v-1}$ on $[-\rho,\rho]$. Its derivative has numerator
  $\rho[f(\rho)+f(-\rho)]-\int_{-\rho}^\rho f(s)\ud s\ge0$,
  by the endpoint chord bound for a convex function. For $\rho>1$,
  every distance $\sqrt{1+\rho^2+2\rho u}$, $-1\le u\le1$,
  increases with $\rho$, so its negative power decreases.
  The formula is continuous at $\rho=1$ and at zero. Its maximum
  is therefore $F_3(e_1)=2^{1-\alpha}/(2-\alpha)$.

  In dimension two we claim $G_1(B(w,R))\le2R^{3/2}$ for
  $0<R\le1/4$. Rotate $w=(A,0)$, $A\ge0$. If $A<1/2$, the ball
  lies in $|y|<3/4$, where the density is at most $2/(\pi\sqrt7)$;
  its mass is at most $2R^2/\sqrt7$. If $A\ge1/2$, write $y=(x,v)$.
  On the ball $|v|\le R$ and $x\ge1/4$. Put $L=\sqrt{1-v^2}$.
  Inside the disk, $1-|y|^2=(L-x)(L+x)$ with $L+x>1$.
  Each horizontal slice has length at most $2R$, so integrating
  $(L-x)^{-1/2}$ gives at most $2\sqrt{2R}$. The $v$ range has
  length at most $2R$, giving mass at most
  $(2\sqrt2/\pi)R^{3/2}\le2R^{3/2}$, as claimed. Layer cake now gives
  \[
    F_2(w)\le4^\alpha+
    \alpha\int_0^{1/4}R^{-\alpha-1}G_1(B(-w,R))\ud R
    \le M_2/c.
  \]
  This includes centers outside the disk and is uniform in $w$.

  Finally, Tonelli and the Gaussian convolution rule give
  \[
    \int G_{h,\eta}(\ud y)\gamma_\epsilon(y+z)
    =\int p_{\epsilon+\eta}(w)(G_h*\gamma)(z-w)\ud w.
  \]
  Mass-one averaging preserves both supremum bounds, for all widths
  in Hypothesis~\ref{H:spatial-maximum}. We justify the approximate
  identity used for optimality. For $f(x)=|x|^{-\lambda}$ in
  $\R^j$, $0<\lambda<j$, fix $x\ne0$. In the convolution
  $\int p_\epsilon(x-y)f(y)\ud y$, a small neighborhood of $x$
  gives convergence by continuity. On $|y|<|x|/2$ the integral is
  bounded by a constant times
  $\epsilon^{-j/2}e^{-|x|^2/(8\epsilon)}$, since $f$ is integrable
  on that ball. On the remaining region outside the neighborhood of
  $x$, $f$ is bounded and the Gaussian tail tends to zero.
  Thus, $p_\epsilon*f(x)\to f(x)$ for every $x\ne0$.
  In dimension three Fatou's lemma at a maximizing shift as
  $\epsilon\downarrow0$, $\eta=0$, now recovers the unsmoothed
  value; the single singular point has zero sphere measure.
  Hence, no smaller uniform constant is possible. This proves
  Lemma~\ref{L:higher-riesz}.
\end{proof}

\begin{corollary}[Riesz moment bounds]\label{C:higher-riesz}
  For isotropic Riesz covariance $c|x|^{-\alpha}$, the bounds
  in~\eqref{E:higher-bound} hold in dimension three for
  $1<\alpha<2-\alpha_0$, and in dimension two for
  $1<\alpha<\min\{3/2,2-\alpha_0\}$, with $M=M_d$ in
  \eqref{E:higher-constants}.
\end{corollary}

\begin{proof}
  These Riesz functions are nonnegative, homogeneous of degree
  $-\alpha$, locally integrable since $\alpha<d$, and nonnegative
  definite. For the last property, the identity
  \[
    |x|^{-\alpha}=\frac1{\Gamma(\alpha/2)}
    \int_0^\infty s^{\alpha/2-1}e^{-s|x|^2}\ud s
  \]
  represents the covariance as a positive mixture of positive definite
  Gaussians. To justify this distributionally, take a complex Schwartz
  function $\varphi$, put $\widetilde{\varphi}(x)=\overline{\varphi(-x)}$,
  and set $\psi=\varphi*\widetilde{\varphi}$. This is Schwartz and
  $\int |x|^{-\alpha}|\psi(x)|\ud x<\infty$: local integrability
  controls the origin and rapid decay controls infinity. Tonelli
  applied with $|\psi|$ therefore proves absolute integrability of
  the mixture against $\psi$, so Fubini applies. Each Gaussian has
  nonnegative integral against $\psi$, as follows from its positive
  Fourier transform and the factor $|\widehat{\varphi}|^2$.
  The mixture consequently has nonnegative integral against $\psi$.
  This proves nonnegative definiteness as a tempered distribution.
  The stated ranges satisfy
  $\alpha+\alpha_0<2$, and Lemma~\ref{L:higher-riesz} supplies the
  additional spatial hypothesis with all Gaussian uniformities.
  Proposition~\ref{P:higher-transfer} applies. This proves
  Corollary~\ref{C:higher-riesz}.
\end{proof}

\begin{proposition}[Obstructions to the spatial hypothesis]
  \label{P:higher-obstructions}
  In dimension two, Riesz covariance with $3/2\le\alpha<2$ fails
  Hypothesis~\ref{H:spatial-maximum}. For every $1<\alpha<2$ there
  are nonnegative, nonnegative definite homogeneous locally integrable
  covariance functions in both dimensions two and three that fail it.
\end{proposition}

\begin{proof}
  For the first claim set $h=1$, $z=-e_1$, and
  $y=e_1+\rho(\cos\phi,\sin\phi)$. On the wedge
  $0<\rho<1/2$, $2\pi/3\le\phi\le4\pi/3$, we have
  $0<1-|y|^2\le2\rho$. Therefore,
  \[
    \int G_1^{(2)}(\ud y)c|y-e_1|^{-\alpha}
    \ge\frac{c}{3\sqrt2}\int_0^{1/2}\rho^{1/2-\alpha}\ud\rho
    =\infty.
  \]
  This includes logarithmic divergence at $\alpha=3/2$.
  For the second claim choose
  $a_1=(1+\max\{2-\alpha,\alpha-1\})/2$ and $a_2=\alpha-a_1$.
  Then $0<a_1,a_2<1$ and $a_1+a_2/2>1$.
  The function $\gamma(x)=c|x_1|^{-a_1}|x_2|^{-a_2}$, independent
  of $x_3$ in dimension three, is locally integrable, tempered, and
  homogeneous of degree $-\alpha$. The Gaussian mixture identity
  in the preceding proof applied separately to each coordinate shows
  nonnegative definiteness; products of these Gaussians and the
  constant function in the third coordinate are positive definite.
  More explicitly, for the Schwartz autocorrelation $\psi$ used in
  the preceding proof, choose $N>1$ and bound
  $|\psi(x)|\le C_N\prod_{j=1}^d(1+|x_j|)^{-N}$.
  Then $\int\gamma(x)|\psi(x)|\ud x<\infty$, by the product
  of one-dimensional integrals and $a_1,a_2<1$. Tonelli with
  $|\psi|$ and then Fubini justify the two Gaussian-mixture integrals
  against $\psi$. Their integrands are nonnegative quadratic forms,
  proving the assertion also for the covariance independent of $x_3$.
  With $u=1-y_1$ and then $y_2=\sqrt{2u-u^2}\,w$, Tonelli gives
  \[
    \int G_1^{(2)}(\ud y)\gamma(y-e_1)
    =\frac{c B((1-a_2)/2,1/2)}{2\pi}
    \int_0^2u^{-a_1}(2u-u^2)^{-a_2/2}\ud u=\infty.
  \]
  The beta factor is finite and the integral diverges at zero.
  The projection of $G_1^{(3)}$ onto its first two coordinates is
  $G_1^{(2)}$: the two sphere graphs each have surface Jacobian
  $(1-|y|^2)^{-1/2}$, divided by $4\pi$. Hence, the same divergence
  holds in dimension three. For radial Riesz covariance, the
  approximate-identity argument in Lemma~\ref{L:higher-riesz} applies.
  For the product covariance, Gaussian factorization and Tonelli give
  \[
    (p_\epsilon*\gamma)(x)
    =c\prod_{j=1}^2
    (p_\epsilon^{(1)}*|\,\cdot\,|^{-a_j})(x_j).
  \]
  In dimension three the third coordinate integrates to one. Each
  factor converges when $x_j\ne0$ by the same argument with dimension
  one and exponent $a_j<1$. This does not require the product kernel
  to be bounded at infinity; it is unbounded along its singular axes.
  The singular sets have zero shifted Green measure in both dimensions.
  Fatou with $\eta=0$ implies that the smoothed
  convolution tends to infinity in lower limit as $\epsilon\downarrow0$.
  Even if both widths must be positive, take $\eta=\epsilon$ and use
  their sum in the Gaussian identity above. Thus, no uniform $M$ exists.
  This proves Proposition~\ref{P:higher-obstructions}.
\end{proof}

\begin{remark}[Calibrations and scope]\label{R:higher-calibrations}
  The printed first-moment statement and unconditional comparison are
  Theorem~\ref{T:first} and Proposition~\ref{P:Jensen}. Under the
  additional spatial hypothesis, Cauchy--Schwarz and
  Proposition~\ref{P:higher-transfer} give
  $\E u(t,x)\le\exp\{qK^{1/q}t^\kappa/2\}$, and hence
  $2L_*\le qK^{1/q}$ if the intended first-moment lower bound holds.
  No sharp first- or second-moment constant is
  identified. As $\alpha_0\downarrow0$, the exponent tends to
  $(4-\alpha)/(3-\alpha)$, consistently with the Chen--Hu static
  calibration in Remark~\ref{R:d1-comparisons}; no interchange of limits
  is claimed. For the Riesz cases here, the Skorohod comparison of
  Balan--Conus~\cite{balan.conus:16:intermittency}*{Theorem~2.1(b),
  p.~1492; p.~1490} applies with $a=\alpha<d$, $\alpha<2$, and
  $H=1-\alpha_0/2>1/2$. Its exponent
  $(2H+2-a)/(3-a)$ is $\kappa$. This comparison is restricted to
  those Riesz cases, with a different solution concept and covariance
  normalization; it is not an input here, and no equality with the
  Balan--Chen--Wang second-moment asymptotics is inferred. The
  obstructions above concern only the spatial supremum, not existence,
  moment finiteness, or failure of the target time scale. In particular,
  arbitrary homogeneous covariances remain outside this conditional
  argument, even when $\alpha+\alpha_0<2$.
\end{remark}

\section{Riesz bounds by interpolation with static noise}
\label{S:static-holder}

This alternative argument concerns isotropic Riesz covariance in dimensions
two and three. It does not use the preceding conditional proposition,
settle general anisotropic covariance, or identify the sharp constant.
The full upper and intrinsic formula later use separate arguments.

We use the static Stratonovich model of Chen--Hu as one input and the
space-degree-one estimate of Section~\ref{S:d1-upper} as the other.
The static source allows nonnegative generalized covariances, not only
Riesz functions: see its standing assumptions (1.2)--(1.3), p.~2145,
and its explicit generalized-covariance convention (2.18), p.~2152,
in~\cite{chen.hu:25:hyperbolic}. In the latter convention every covariance
factor is heat regularized before its defining limit. A nonnegative,
even, positive-definite tempered Radon measure is such a generalized
covariance. In each application below we separately verify its homogeneity
range and static Dalang condition before using the source's quantitative
coefficient estimates (5.1) and (5.15). Positive definiteness of a weighted
endpoint is proved in Lemma~\ref{L:planar-endpoints}, or is an explicit
assumption in Hypothesis~\ref{H:three-endpoints}; weighting a measure alone
is not being used to assert that property. Chen's variational finiteness
theorem supplies only finiteness of the static constant, not a
coefficient-rate theorem.

For $d \in \{2,3\}$, $c > 0$, and $0 < \lambda < \min\{2,d\}$, write
\[
  \gamma_\lambda(x)=c|x|^{-\lambda},\qquad
  \gamma_{\lambda,\epsilon}=p_\epsilon*\gamma_\lambda.
\]
All these covariances use the same amplitude $c$ and Gaussian convention.
They are nonnegative, locally integrable, and homogeneous. Their nonnegative
definiteness follows from
\[
  \gamma_\lambda(x)=\frac{c}{\Gamma(\lambda/2)}
  \int_0^\infty s^{\lambda/2-1}e^{-s|x|^2}\ud s.
\]
Indeed, each Gaussian is positive definite. For a Schwartz autocorrelation
$\psi$, the integral $\int |x|^{-\lambda}|\psi(x)|\ud x$ is finite by
$\lambda < d$ and rapid decay. Tonelli with $|\psi|$, followed by Fubini,
therefore justifies the positive Gaussian mixture as a tempered distribution.
The source hypotheses for the Riesz covariances below are thus satisfied.

\begin{lemma}[Static coefficient input]\label{L:static-holder-input}
  Let $U_n(t,x)$ be the ordered Stratonovich integrals for static Gaussian
  noise with covariance $\gamma_\chi$, where
  $d \in \{2,3\}$ and $1 < \chi < 2$. Put $U_0=1$ and
  \[
    B_k(t)=\sum_{m=0}^{2k}\E[U_m(t,x)U_{2k-m}(t,x)].
  \]
  Then $B_0=1$, and there is a finite constant
  $C_{\rm st}=C_{\rm st}(\chi,c,d)>0$ such that
  \begin{equation}\label{E:static-holder-input}
    0\le B_k(t)\le
    \frac{C_{\rm st}^{\,k}t^{(4-\chi)k}}{(k!)^{3-\chi}},
    \qquad k\ge1,\quad t>0.
  \end{equation}
\end{lemma}

\begin{proof}
  The static solution has data $(1,0)$ and wave operator $\Delta$, as here.
  The degree satisfies $\chi<\min\{2,d\}$, so the Riesz covariance meets
  the source's Dalang condition. From
  Chen--Hu~\cite{chen.hu:25:hyperbolic}*{Theorem~3.8(i), p.~2165},
  the fixed-order integrals exist in $L^2$. Their product rule and Wick
  expectation formula in that source's (2.17) and (2.19),
  pp.~2151--2152, identify $B_k$ with the complete nonnegative sum over
  the $2k+1$ splits and every pairing of the $2k$ vertices. In particular,
  it includes within-chain pairs; no orthogonality of different orders
  is asserted. Empty chains contribute the factor one.

  From~\cite{chen.hu:25:hyperbolic}*{(5.1), p.~2173, and (5.15), p.~2180},
  specialized to $p=2$, we have
  \[
    B_k(t)=t^{(4-\chi)k}B_k(1),\qquad
    \limsup_{k\to\infty}\frac1k
    \log\left((k!)^{3-\chi}B_k(1)\right)<\infty.
  \]
  Only the finite upper coefficient rate from the latter formula is
  used. Choose $R>0$ larger than this upper limit. For some $k_0\ge1$,
  $(k!)^{3-\chi}B_k(1)\le e^{Rk}$ for all $k\ge k_0$.
  Each of the remaining coefficients is finite by the fixed-order
  $L^2$ property. Increase $e^R$, if necessary, to a finite positive
  $C_{\rm st}$ that also dominates
  $\left((k!)^{3-\chi}B_k(1)\right)^{1/k}$ for $1\le k<k_0$.
  Homogeneity gives~\eqref{E:static-holder-input}. The source results
  are imported inputs; this finite-order enlargement is the only
  deduction about their constant needed here. This proves
  Lemma~\ref{L:static-holder-input}.
\end{proof}

\begin{proposition}[Interpolation bound for Riesz covariance]
  \label{P:static-holder-upper}
  Suppose that $d \in \{2,3\}$, $c > 0$, $0 < \alpha_0 < 1$, and
  $1 < \alpha < 2-\alpha_0$. Let the spatial covariance be
  $\gamma_\alpha(x)=c|x|^{-\alpha}$, and let $A_k(t)$ denote the full
  total-order-$2k$ coefficient of the second moment, as in
  Proposition~\ref{P:mixed}. Choose and fix
  \begin{equation}\label{E:static-holder-parameters}
    \alpha_0<\vartheta<2-\alpha,\qquad
    b_0=\frac{\alpha_0}{\vartheta},\qquad
    \chi=\frac{\alpha-\vartheta}{1-\vartheta}.
  \end{equation}
  Let $V_1$ be the spectral mass of the unit ball for $\gamma_1$, in
  the convention of Lemma~\ref{L:alpha-one-convolution}, and define
  \[
    Z_{b_0}=\frac2{(1-b_0)(2-b_0)},\qquad
    C_{\rm low}=2Z_{b_0}\pi V_1,\qquad
    C=C_{\rm low}^{\,\vartheta}C_{\rm st}^{\,1-\vartheta},
    \qquad q=3-\alpha,
  \]
  where $C_{\rm st}$ is supplied by Lemma~\ref{L:static-holder-input}
  for the displayed $\chi$. Then, for every $k\ge1$, $t>0$, and
  $x\in\R^d$,
  \begin{equation}\label{E:static-holder-upper}
    A_k(t)\le\frac{C^kt^{(4-\alpha-\alpha_0)k}}{(k!)^{3-\alpha}},
    \qquad
    \E u^2(t,x)\le\exp\left(qC^{1/q}t^\kappa\right).
  \end{equation}
  The finite constants may depend on $\alpha,\alpha_0,c,d$ and the fixed
  choice of $\vartheta$, but not on $k,t,x$.
\end{proposition}

\begin{proof}
  The interval for $\vartheta$ is nonempty by $\alpha+\alpha_0<2$.
  Since $\alpha>1$, we have $0<\vartheta<1$, $0<b_0<1$, and
  \[
    \chi-1=\frac{\alpha-1}{1-\vartheta}>0,\qquad
    2-\chi=\frac{2-\alpha-\vartheta}{1-\vartheta}>0.
  \]
  Thus, both endpoint covariances are admissible in dimensions two and
  three. Moreover,
  \begin{equation}\label{E:static-holder-affine}
    \alpha=\vartheta+(1-\vartheta)\chi,
    \qquad \alpha_0=\vartheta b_0.
  \end{equation}

  Fix $k\ge1$ and $t>0$. Use a common spatial noise width
  $\epsilon>0$ and the target's temporal cutoff width $\delta>0$.
  The covariance on each pairing edge has spatial width $2\epsilon$.
  In dimension three first use $G_{h,\eta}=p_\eta*G_h$ with
  $\eta>0$; in dimension two take $\eta=0$. For each split $m+n=2k$
  and pairing $D\in\Pi_k$, use the two separate roots, increments
  $h_l=s_l-s_{p(l)}$, and positions $x_l$ of
  Section~\ref{S:d1-upper}. Define a common positive measure
  $\nu_{k,t,\eta}$ by
  \[
    \int\Phi\ud\nu_{k,t,\eta}
    :=\sum_{m=0}^{2k}\sum_{D\in\Pi_k}
    \int_{[0,t]^m_<\times[0,t]^{2k-m}_<}\ud s
    \int\Phi(m,D,s,y)\prod_{l=1}^{2k}G_{h_l,\eta}(\ud y_l).
  \]
  Here $y_l$ are vector increments and each $x_l$ is their cumulative
  sum within its own chain. Empty blocks have empty products and their
  own root conventions. This measure is finite: the spatial mass at
  fixed times is $\prod_lh_l$, the time domains are bounded, and both
  discrete sums are finite. It is the same measure for all three
  covariance profiles.

  For $\lambda\in\{1,\alpha,\chi\}$ and $b>0$, put
  \[
    H_\lambda=\prod_{(i,j)\in D}
    \gamma_{\lambda,2\epsilon}(x_i-x_j),\qquad
    T_b=\prod_{(i,j)\in D}|s_i-s_j|^{-b}.
  \]
  The pointwise identity
  $\gamma_\alpha=\gamma_1^{\vartheta}\gamma_\chi^{1-\vartheta}$
  retains the amplitude $c$, since $c^\vartheta c^{1-\vartheta}=c$.
  H\"older's inequality on the Gaussian probability measure gives
  \[
    \gamma_{\alpha,2\epsilon}(z)
    \le\gamma_{1,2\epsilon}(z)^\vartheta
    \gamma_{\chi,2\epsilon}(z)^{1-\vartheta},
    \qquad z\in\R^d.
  \]
  These convolutions are finite because the degrees are below $d$.
  Let $Q_\delta$ denote the product of the target's truncated temporal
  covariances. From the regularization in
  Chen~\cite{chen:author2026:time-dependency}*{(2.9), (2.11)},
  \[
    0\le Q_\delta\le T_{\alpha_0}=T_{b_0}^{\,\vartheta}.
  \]
  This uses only domination by the raw temporal power; no interpolation
  property of distinct temporal cutoffs is required.

  Let $A_k^{\epsilon,\delta,\eta}(t)=\int Q_\delta H_\alpha
  \ud\nu_{k,t,\eta}$ be the target regularized coefficient. The
  Gaussian moment formula and the separate chain reversals in
  Proposition~\ref{P:mixed} identify it with the finite sum of
  regularized mixed moments. Also set
  \[
    L_k^{\epsilon,\eta}(t)=\int T_{b_0}H_1\ud\nu_{k,t,\eta},
    \qquad
    B_k^{\epsilon,\eta}(t)=\int H_\chi\ud\nu_{k,t,\eta}.
  \]
  The second expression is the actual regularized static coefficient,
  by the Gaussian moment formula with all pairings and splits. The first
  is a deterministic integral with raw temporal covariance. We do not
  identify it with a stochastic integral having mixed regularizations.
  H\"older's inequality on the full measure, including its two discrete
  variables, yields
  \begin{equation}\label{E:static-holder-regularized}
    A_k^{\epsilon,\delta,\eta}(t)
    \le\left(L_k^{\epsilon,\eta}(t)\right)^\vartheta
    \left(B_k^{\epsilon,\eta}(t)\right)^{1-\vartheta}.
  \end{equation}

  The deterministic estimates in the proof of
  Proposition~\ref{P:low-alpha-upper}, at spatial degree one and
  temporal degree $b_0$, apply to $L_k^{\epsilon,\eta}$.
  In detail, Lemma~\ref{L:alpha-one-convolution} gives the closing
  bound $\pi V_1/2$, uniformly in both smoothing widths. Descending
  integration and the opening arithmetic--geometric mean give the
  common spatial bound $(\pi V_1)^kt^k/k^k$.
  The temporal pairing sum is symmetric on the full time cube. Its
  integral, after summing every split as in~\eqref{E:d1-time-symmetry},
  is $2^k(Z_{b_0}t^{2-b_0})^k/k!$. Hence,
  \begin{equation}\label{E:static-holder-low}
    L_k^{\epsilon,\eta}(t)
    \le\frac{C_{\rm low}^{\,k}t^{(3-b_0)k}}{k!\,k^k}
    \le\frac{C_{\rm low}^{\,k}t^{(3-b_0)k}}{(k!)^2}.
  \end{equation}
  The raw temporal integral is finite since $b_0<1$. The static
  regularized coefficient is finite because its covariance is bounded
  at fixed $\epsilon$. Thus, the H\"older step has finite right side.

  We pass to fixed-order limits before using the static coefficient
  bound. In dimension three fix $\epsilon,\delta$ and let
  $\eta\downarrow0$. The target and static smoothed covariance
  factors are bounded continuous functions of the spatial positions.
  Products of the finite Green measures converge weakly with masses
  $\prod_lh_l$. A constant times this product dominates each time
  integrand at fixed noise smoothing, so dominated convergence applies
  on the bounded time simplexes. The same argument with two Green
  widths gives a common mixed covariance limit, and hence fixed-order
  $L^2$ convergence. This identifies the static limit with
  the measure convention of
  Chen--Hu~\cite{chen.hu:25:hyperbolic}*{(2.22), pp.~2152--2153}.
  The target uses the corresponding inner limit in
  Chen~\cite{chen:author2026:time-dependency}*{pp.~13--14}.
  We need no limit identification for $L_k^{\epsilon,\eta}$:
  its uniform upper bound in~\eqref{E:static-holder-low} suffices.

  Next let the noise-smoothing parameters tend to zero. From
  Chen--Hu~\cite{chen.hu:25:hyperbolic}*{Theorem~3.8(i), p.~2165},
  each fixed static order converges in $L^2$ to $U_n$.
  For the target, the fixed-order $L^2$ convergence follows from
  Lemma~\ref{L:joint-fixed-order}. If $Y,Y',Z,Z'$ are the corresponding
  approximations and limits, then
  \[
    \|YZ-Y'Z'\|_1
    \le\|Y-Y'\|_2\|Z\|_2+\|Y'\|_2\|Z-Z'\|_2.
  \]
  Therefore, every fixed split product converges in $L^1$. The finite
  sums over the $2k+1$ splits converge as well; a zero-order factor
  stays equal to one. This argument applies directly in dimension two,
  where no Green smoothing is needed. Passing to these limits
  in~\eqref{E:static-holder-regularized}, using
  \eqref{E:static-holder-low}, gives
  \[
    A_k(t)\le
    \left(\frac{C_{\rm low}^{\,k}t^{(3-b_0)k}}{(k!)^2}\right)^\vartheta
    B_k(t)^{1-\vartheta}.
  \]
  Only now apply Lemma~\ref{L:static-holder-input}. No monotonicity
  in $\epsilon$ and no uniform static large-time bound in that
  parameter have been assumed.

  The powers combine without a counting loss. Indeed,
  by~\eqref{E:static-holder-affine},
  \[
    \begin{split}
      2\vartheta+(1-\vartheta)(3-\chi)&=3-\alpha,\\
      \vartheta(3-b_0)+(1-\vartheta)(4-\chi)
      &=4-\alpha-\alpha_0.
    \end{split}
  \]
  This proves the coefficient bound in~\eqref{E:static-holder-upper}.
  The constant term is $A_0=1$. Since $q=3-\alpha>1$, the scalar
  inequality $\sum_{k\ge0}z^k/(k!)^q\le e^{qz^{1/q}}$ proved in
  Proposition~\ref{P:d1-upper} applies with
  $z=Ct^{4-\alpha-\alpha_0}$. Proposition~\ref{P:mixed} identifies
  the nonnegative full coefficient series with $\E u^2(t,x)$.
  Here $(4-\alpha-\alpha_0)/q=\kappa$. This proves
  Proposition~\ref{P:static-holder-upper}.
\end{proof}

\begin{remark}[Calibrations and remaining scope]\label{R:static-holder-scope}
  The time exponent in~\eqref{E:static-holder-upper} tends to
  $(4-\alpha)/(3-\alpha)$ as $\alpha_0\downarrow0$, in agreement
  with the Chen--Hu static exponent. This does not interchange the
  static and large-time limits or assert uniformity of the constants.
  Cauchy--Schwarz gives $\E u(t,x)\le
  \exp(qC^{1/q}t^\kappa/2)$. If the first-moment lower rate is at
  least $L_*$, this upper bound implies $2L_*\le qC^{1/q}$.
  Thus, the first-moment and Jensen calibrations are retained, without
  identifying a sharp constant. The Skorohod comparison remains only
  the comparison recorded in Remark~\ref{R:higher-calibrations}; its
  exponent agrees, but its solution concept and covariance normalization
  differ. No Skorohod estimate is used in this proof. The argument covers
  isotropic Riesz covariance throughout the stated higher-degree range
  in dimensions two and three, including the previously uncovered
  two-dimensional interval $3/2\le\alpha<2-\alpha_0$.
  This argument does not cover arbitrary homogeneous covariances:
  anisotropic profiles need not factor into the admissible endpoints.
  The intrinsic second-moment formula is given separately in
  Theorem~\ref{T:intrinsic-second-moment}. No novelty is asserted here.
\end{remark}

\section{General homogeneous covariance in dimension two}
\label{S:planar-holder}

This section gives planar endpoint constructions and a transfer under
its stated hypotheses. It does not use the preceding Riesz interpolation
argument as an input. The later full upper and intrinsic formula use
separate methods.

Throughout this section $d=2$. Write $\Gamma$ for the spatial covariance
as a nonnegative, even, positive-definite tempered Radon measure. For a
locally integrable covariance function, this means
$\Gamma(\ud x)=\gamma(x)\ud x$. The measure interpretation uses the Gaussian
approximation framework of
Chen~\cite{chen:author2026:time-dependency}*{pp.~2--3, 13} and
Chen--Hu~\cite{chen.hu:25:hyperbolic}*{pp.~2145--2147, 2151--2153}.
All products of covariance factors below are taken after Gaussian smoothing;
no product or fractional power of distributions is used. Homogeneity means
\begin{equation}\label{E:planar-measure-scaling}
  \Gamma(rA)=r^{2-\alpha}\Gamma(A),\qquad r>0,
\end{equation}
for Borel sets $A$. This is equivalent to the covariance homogeneity in
Hypothesis~\ref{H:homog}. If $\Gamma=0$, the noise vanishes and $u=1$.
We first treat $\Gamma\ne0$ and $1<\alpha<2$.

\begin{lemma}[Planar endpoint covariances]\label{L:planar-endpoints}
  Suppose that $\Gamma$ satisfies the preceding assumptions, and let
  $\alpha<\chi<2$. Define the finite angular measure
  \[
    \sigma(E)=(2-\alpha)\Gamma
    \{x:0<|x|\le1,\ x/|x|\in E\},\qquad
    S=\sigma(\mathbb{S}^1).
  \]
  On $\R^2\setminus\{0\}$ define the weighted measures
  \begin{equation}\label{E:planar-endpoints}
    \Gamma_{\rm low}(\ud x)=|x|^{\alpha-1}\Gamma(\ud x),\qquad
    \Gamma_{\rm st}(\ud x)=|x|^{\alpha-\chi}\Gamma(\ud x),
  \end{equation}
  with zero mass at the origin. Both are nonnegative, even,
  positive-definite tempered Radon measures. Their measure scaling
  exponents are $1$ and $2-\chi$, respectively. For every $h>0$,
  $\epsilon>0$, $\eta\ge0$, and $z\in\R^2$,
  \begin{equation}\label{E:planar-line-convolution}
    \int G_{h,\eta}(\ud y)(p_\epsilon*\Gamma_{\rm low})(y+z)
    \le\frac S4.
  \end{equation}
  If $\vartheta=(\chi-\alpha)/(\chi-1)$, then $0<\vartheta<1$ and
  \begin{equation}\label{E:planar-gaussian-holder}
    (p_\epsilon*\Gamma)(z)
    \le(p_\epsilon*\Gamma_{\rm low})(z)^\vartheta
    (p_\epsilon*\Gamma_{\rm st})(z)^{1-\vartheta}.
  \end{equation}
  No angular density or isotropy is assumed.
\end{lemma}

\begin{proof}
  Since $2-\alpha>0$, scaling and local finiteness force
  $\Gamma(\{0\})=0$. The unit-ball mass is finite, so $S<\infty$.
  It is positive: otherwise scaling would make every ball have zero
  mass, contradicting $\Gamma\ne0$. Evenness of $\Gamma$ implies
  evenness of $\sigma$. For $0<a<b$ and Borel $E\subset\mathbb{S}^1$,
  \[
    \Gamma\{x:a<|x|\le b,\ x/|x|\in E\}
    =\frac{b^{2-\alpha}-a^{2-\alpha}}{2-\alpha}\sigma(E)
    =\int_a^b r^{1-\alpha}\ud r\,\sigma(E).
  \]
  These polar rectangles form a generating family. Uniqueness of
  measures, first on finite annuli and then on their increasing union,
  identifies the polar pushforward with
  $r^{1-\alpha}\ud r\,\sigma(\ud\omega)$. Hence, for every
  nonnegative Borel function $f$, Tonelli gives
  \begin{equation}\label{E:planar-polar}
    \int f(x)\Gamma(\ud x)
    =\int_{\mathbb{S}^1}\int_0^\infty
    f(r\omega)r^{1-\alpha}\ud r\,\sigma(\ud\omega).
  \end{equation}
  Extended values are permitted. In particular, the formula applies
  to the nonnegative wave density used below.

  The endpoint polar measures are therefore
  $\ud r\,\sigma(\ud\omega)$ and
  $r^{1-\chi}\ud r\,\sigma(\ud\omega)$. Their radial integrals
  are finite near zero because $\chi<2$. Rapid decay of a Schwartz
  function controls their integrals at infinity, uniformly in direction.
  They are thus locally finite and tempered, and their stated scaling
  and evenness follow directly. If $\Gamma$ has a density, the two
  weighted measures also have locally integrable densities.

  To prove positive definiteness of the low endpoint, evenness gives
  the full-sphere line representation
  \begin{equation}\label{E:planar-line-mixture}
    \int f(x)\Gamma_{\rm low}(\ud x)
    =\frac12\int_{\mathbb{S}^1}\int_\R f(r\omega)\ud r
    \,\sigma(\ud\omega).
  \end{equation}
  It holds for nonnegative Borel $f$, and for Schwartz $f$ by absolute
  integrability. For a complex Schwartz function $\varphi$, put
  $\widetilde{\varphi}(x)=\overline{\varphi(-x)}$ and
  $\psi=\varphi*\widetilde{\varphi}$. Fubini in line and perpendicular
  coordinates gives
  \[
    \int_\R\psi(r\omega)\ud r
    =\int_{\omega^\perp}
    \left|\int_\R\varphi(s\omega+v)\ud s\right|^2\ud v\ge0.
  \]
  Schwartz decay justifies all these integrals, uniformly for unit
  $\omega$. Integrating against the finite measure $\sigma$
  in~\eqref{E:planar-line-mixture} proves
  $\Gamma_{\rm low}(\psi)\ge0$. The factor $1/2$ is essential because
  both orientations of each line occur on the full sphere.

  For the static endpoint put $\lambda=\chi-\alpha>0$. For $x\ne0$,
  \[
    |x|^{-\lambda}=\frac1{\Gamma(\lambda/2)}
    \int_0^\infty s^{\lambda/2-1}e^{-s|x|^2}\ud s.
  \]
  For each $s>0$, the measure $e^{-s|x|^2}\Gamma(\ud x)$ is
  positive definite. Indeed, the Fourier transform of
  $e^{-s|x|^2}\psi(x)$ is a positive Gaussian convolution of
  $|\widehat{\varphi}|^2$. Its pairing with the original positive
  spectral measure is nonnegative; Schwartz decay makes the pairing
  finite. Moreover,
  \[
    \int |\psi(x)||x|^{-\lambda}\Gamma(\ud x)
    =\int |\psi(x)|\Gamma_{\rm st}(\ud x)<\infty
  \]
  by the endpoint polar integrability just proved. Tonelli with
  $|\psi|$, followed by Fubini, justifies the Gaussian mixture against
  $\psi$. Thus, $\Gamma_{\rm st}(\psi)\ge0$. This uses smooth
  Gaussian multiplication of the original covariance and a convergent
  mixture, not a fractional power of that covariance.

  We next prove the convolution estimate directly. Use the planar wave
  density
  \[
    G_h(y)=\frac{\mathbf1_{\{|y|<h\}}}{2\pi\sqrt{h^2-|y|^2}},
  \]
  with value zero on the circle. Write
  $z=a\omega+b\omega^\perp$ for a unit perpendicular vector.
  If $|b|<h$, put $A=\sqrt{h^2-b^2}$. Translation along the line gives
  \[
    \int_\R G_h(z-r\omega)\ud r
    =\frac1{2\pi}\int_{-A}^A\frac{\ud s}{\sqrt{A^2-s^2}}
    =\frac12.
  \]
  If $|b|\ge h$, the open support is empty or tangent and the line
  integral is zero. The tangency point has zero line Lebesgue measure.
  Formula~\eqref{E:planar-line-mixture} and nonnegative Tonelli yield
  \[
    (G_h*\Gamma_{\rm low})(z)
    =\frac14\int_{\mathbb{S}^1}
    \mathbf1_{\{|z\cdot\omega^\perp|<h\}}\sigma(\ud\omega)
    \le\frac S4.
  \]
  Evenness, Gaussian convolution, and Tonelli now give
  \[
    \int G_{h,\eta}(\ud y)(p_\epsilon*\Gamma_{\rm low})(y+z)
    =\left[p_{\epsilon+\eta}*(G_h*\Gamma_{\rm low})\right](z)
    \le\frac S4.
  \]
  For $\eta=0$, use the unsmoothed Green measure. The Gaussian average
  has mass one, so the same constant works for all widths.

  Finally, the measure $p_\epsilon(z-x)\Gamma(\ud x)$ is finite.
  Gaussian decay and polynomial radial growth prove this directly;
  the endpoint convolutions are finite for the same reason. The identity
  \[
    \vartheta(\alpha-1)+(1-\vartheta)(\alpha-\chi)=0
  \]
  and absence of an origin atom permit H\"older's inequality on this
  unnormalized positive measure:
  \[
    \begin{split}
      (p_\epsilon*\Gamma)(z)
      &=\int |x|^{\vartheta(\alpha-1)}
      |x|^{(1-\vartheta)(\alpha-\chi)}
      p_\epsilon(z-x)\Gamma(\ud x)\\
      &\le(p_\epsilon*\Gamma_{\rm low})(z)^\vartheta
      (p_\epsilon*\Gamma_{\rm st})(z)^{1-\vartheta}.
    \end{split}
  \]
  This proves Lemma~\ref{L:planar-endpoints}.
\end{proof}

\begin{lemma}[General planar static coefficient input]
  \label{L:planar-static-input}
  Let $\Xi$ be a nonnegative, even, positive-definite tempered Radon
  measure on $\R^2$ with
  $\Xi(rA)=r^{2-\chi}\Xi(A)$, where $1<\chi<2$.
  For static Stratonovich noise with covariance $\Xi$, data $(1,0)$,
  and wave operator $\Delta$, let $U_n(t,x)$ be its ordered integrals,
  with $U_0=1$. There is a finite $C_{\rm st}=C_{\rm st}(\Xi)>0$ such
  that, for $k\ge1$ and $t>0$,
  \begin{equation}\label{E:planar-static-input}
    0\le B_k(t):=\sum_{m=0}^{2k}\E[U_m(t,x)U_{2k-m}(t,x)]
    \le\frac{C_{\rm st}^{\,k}t^{(4-\chi)k}}{(k!)^{3-\chi}}.
  \end{equation}
  Also $B_0=1$.
\end{lemma}

\begin{proof}
  If $\Xi=0$, then $U_n=0$ for $n\ge1$, and hence $B_k=0$ for
  $k\ge1$. The choices $C_{\rm st}=1$ and $B_0=1$ give the
  conclusion. We may therefore assume $\Xi\ne0$.

  Fourier uniqueness transfers covariance homogeneity to its positive
  spectral measure $\mu_\Xi$:
  $\mu_\Xi(rA)=r^\chi\mu_\Xi(A)$. Its unit-ball mass is finite
  because the spectral measure is Radon. On dyadic annuli this gives
  \[
    \int_{\R^2}(1+|\xi|^2)^{-1}\mu_\Xi(\ud\xi)
    \le\mu_\Xi(B_1)
    +2^\chi\mu_\Xi(B_1)\sum_{j\ge0}2^{j(\chi-2)}<\infty.
  \]
  This verifies the static Dalang condition without an angular density.
  The present $\Xi$ also satisfies the source's covariance assumptions:
  it is a nonnegative positive-definite tempered distribution, and
  $1<\chi<2=d$. The source expressly includes generalized covariances
  and uses their heat-regularized interpretation
  \cite{chen.hu:25:hyperbolic}*{p.~2152, (2.18)}.
  Thus the coefficient estimate invoked below is a direct application
  within the source's stated class, not an extension from density kernels.
  From Chen--Hu~\cite{chen.hu:25:hyperbolic}*{Theorem~3.8(i), p.~2165},
  every fixed order exists in $L^2$. The product and Wick formulas
  (2.17) and (2.19), pp.~2151--2152, identify $B_k$ with all pairings
  and all splits of the total order, including self-pairs and empty
  chains. Thus, every coefficient is finite and nonnegative.

  We make explicit the finiteness input in the source's coefficient
  upper rate. The variational constant $\mathcal{M}$ in
  Chen--Hu~\cite{chen.hu:25:hyperbolic}*{p.~2147} is finite under the
  displayed Dalang condition. The source's invocation on p.~2175
  identifies $2^{\chi/(4-\chi)}\mathcal{M}$ with the square-root
  variational quantity covered by
  Chen~\cite{chen:23:exponential}*{Theorem~1.1, p.~2}.
  That theorem explicitly states finiteness under Dalang's condition
  and permits generalized nonnegative positive-definite covariances.
  We import that finiteness, not a sharp value or its proof.

  From Chen--Hu~\cite{chen.hu:25:hyperbolic}*{(5.1), p.~2173,
  and (5.15), p.~2180}, with $p=2$, it follows that
  \[
    B_k(t)=t^{(4-\chi)k}B_k(1),\qquad
    \limsup_{k\to\infty}\frac1k
    \log\left((k!)^{3-\chi}B_k(1)\right)<\infty.
  \]
  Choose a finite $R>0$ larger than this upper limit. For all sufficiently
  large $k$, $(k!)^{3-\chi}B_k(1)\le e^{Rk}$. Increase $e^R$ to a
  finite positive constant dominating the $k$th roots of the finitely
  many remaining quantities. The resulting $C_{\rm st}$
  proves~\eqref{E:planar-static-input} by homogeneity. These are the source's
  general homogeneous-covariance statements, not a Riesz specialization.
  This proves Lemma~\ref{L:planar-static-input}.
\end{proof}

\begin{proposition}[Planar homogeneous-covariance upper bound]
  \label{P:planar-upper}
  Let $d=2$, $0<\alpha_0<1$, and $1<\alpha<2-\alpha_0$.
  Suppose that the nonzero spatial covariance $\Gamma$ is nonnegative,
  even, positive definite and tempered,
  with~\eqref{E:planar-measure-scaling}. Choose and fix
  \[
    \alpha_0<\vartheta<2-\alpha,\qquad
    b_0=\alpha_0/\vartheta,\qquad
    \chi=(\alpha-\vartheta)/(1-\vartheta).
  \]
  Use the endpoint measures and physical angular mass $S$ of
  Lemma~\ref{L:planar-endpoints}. Put
  \[
    Z_{b_0}=\frac2{(1-b_0)(2-b_0)},\qquad
    C_{\rm low}=Z_{b_0}S,\qquad
    C=C_{\rm low}^{\,\vartheta}C_{\rm st}^{\,1-\vartheta},
    \qquad q=3-\alpha,
  \]
  where $C_{\rm st}$ is from Lemma~\ref{L:planar-static-input} for
  $\Xi=\Gamma_{\rm st}$. For the Stratonovich solution with data
  $(1,0)$, every $k\ge1$, $t>0$, and $x\in\R^2$ satisfy
  \begin{equation}\label{E:planar-upper}
    A_k(t)\le\frac{C^kt^{(4-\alpha-\alpha_0)k}}{(k!)^{3-\alpha}},
    \qquad
    \E u^2(t,x)\le\exp\left(qC^{1/q}t^\kappa\right).
  \end{equation}
  Constants may depend on the covariance, $\alpha_0$, and the fixed
  choice of $\vartheta$, but not on $k,t,x$.
\end{proposition}

\begin{proof}
  The parameter interval is nonempty. We have $0<\vartheta<1$,
  $0<b_0<1$, and
  \[
    \chi-\alpha=\frac{\vartheta(\alpha-1)}{1-\vartheta}>0,
    \qquad
    2-\chi=\frac{2-\alpha-\vartheta}{1-\vartheta}>0.
  \]
  Thus, Lemma~\ref{L:planar-endpoints} applies, with its interpolation
  weight equal to $\vartheta$. The original spectral measure has ball
  growth of exponent $\alpha$, by the same Fourier homogeneity argument
  used in Lemma~\ref{L:planar-static-input}. A dyadic sum gives the
  time-dependent spectral condition (1.5) of
  Chen~\cite{chen:author2026:time-dependency}*{p.~3}, since
  $\alpha<2-\alpha_0$. The low endpoint has spectral ball exponent
  one and $b_0<1$; the static endpoint has exponent $\chi<2$.
  Thus, Lemma~\ref{L:joint-fixed-order} applies to the target, and the
  imported static fixed-order theorem is used within its stated range.

  Fix $k\ge1$, $t>0$, and common noise widths $\epsilon,\delta>0$.
  The spatial covariance on each edge has width $2\epsilon$.
  No Green smoothing is needed in dimension two. On the disjoint union
  over $m=0,\ldots,2k$ and $D\in\Pi_k$, define the finite positive
  measure $\nu_{k,t}$ by
  \[
    \int\Phi\ud\nu_{k,t}
    :=\sum_{m=0}^{2k}\sum_{D\in\Pi_k}
    \int_{[0,t]^m_<\times[0,t]^{2k-m}_<}\ud s
    \int\Phi(m,D,s,y)\prod_{l=1}^{2k}G_{h_l}(\ud y_l).
  \]
  Here each chain has its own root, $h_l=s_l-s_{p(l)}$, the $y_l$
  are its increments, and $x_l$ is its cumulative position. A zero-length
  chain has empty products. At fixed times the spatial mass is
  $\prod_lh_l$; bounded time simplexes and finite discrete sums therefore
  make $\nu_{k,t}$ finite.

  For $J\in\{\Gamma,\Gamma_{\rm low},\Gamma_{\rm st}\}$ write
  \[
    H_J=\prod_{(i,j)\in D}(p_{2\epsilon}*J)(x_i-x_j),\qquad
    T_b=\prod_{(i,j)\in D}|s_i-s_j|^{-b}.
  \]
  The Gaussian covariance functions are bounded and continuous at each
  fixed width: their positive spectral measures are tempered, so Gaussian
  weighting makes them finite. Let $Q_\delta$ be the product of the
  target's truncated temporal covariances. The source regularization gives
  $0\le Q_\delta\le T_{\alpha_0}=T_{b_0}^{\,\vartheta}$.
  Lemma~\ref{L:planar-endpoints}, at the common edge width, gives
  $H_\Gamma\le H_{\Gamma_{\rm low}}^\vartheta
  H_{\Gamma_{\rm st}}^{1-\vartheta}$.

  The Gaussian moment formula and the two separate chain reversals in
  Proposition~\ref{P:mixed} identify the target regularized coefficient
  with $\int Q_\delta H_\Gamma\ud\nu_{k,t}$. Define
  \[
    L_k^\epsilon(t)=\int T_{b_0}H_{\Gamma_{\rm low}}\ud\nu_{k,t},
    \qquad
    B_k^\epsilon(t)=\int H_{\Gamma_{\rm st}}\ud\nu_{k,t}.
  \]
  The latter is the actual regularized static coefficient, including
  every split and pairing. The former is only a deterministic integral
  with raw temporal power. H\"older's inequality on the full common
  measure, including its discrete variables, yields
  \begin{equation}\label{E:planar-coefficient-holder}
    A_k^{\epsilon,\delta}(t)
    \le\left(L_k^\epsilon(t)\right)^\vartheta
    \left(B_k^\epsilon(t)\right)^{1-\vartheta}.
  \end{equation}
  No interpolation of different temporal cutoff kernels is asserted.

  We bound $L_k^\epsilon$ directly. Orient each pair by increasing block
  label. Descending integration of increments, as in
  Lemma~\ref{L:d1-spatial}, removes at a closing label its only remaining
  covariance factor. Lemma~\ref{L:planar-endpoints} bounds that integral
  by $S/4$. At an opening label its paired covariance has already been
  removed, so the Green integral is its mass $h_l$. The $k$ opening
  increments sum to at most $2t$. Thus, the common spatial bound is
  \[
    (S/4)^k\prod_{i\in O_D}h_i
    \le(S/2)^k\frac{t^k}{k^k}.
  \]
  The temporal pairing sum is invariant under every permutation of its
  $2k$ labels. Each pairing integrates on the full time cube to
  $(Z_{b_0}t^{2-b_0})^k$. Partitioning by the two within-block orders,
  and then summing all splits, gives
  \[
    \begin{split}
      \sum_{m=0}^{2k}\sum_{D\in\Pi_k}
      \int_{[0,t]^m_<\times[0,t]^{2k-m}_<}T_{b_0}\ud s
      &=\frac{(2k)!}{2^kk!}(Z_{b_0}t^{2-b_0})^k
      \sum_{m=0}^{2k}\frac1{m!(2k-m)!}\\
      &=\frac{2^k}{k!}(Z_{b_0}t^{2-b_0})^k.
    \end{split}
  \]
  Symmetry is used for the sum, not for an individual pairing. The
  integral is finite because $b_0<1$. Multiplication gives
  \begin{equation}\label{E:planar-low-coefficient}
    L_k^\epsilon(t)
    \le\frac{(Z_{b_0}S)^kt^{(3-b_0)k}}{k!\,k^k}
    \le\frac{C_{\rm low}^{\,k}t^{(3-b_0)k}}{(k!)^2}.
  \end{equation}
  At fixed $\epsilon$, bounded covariance and the finite common measure
  make $B_k^\epsilon$ finite as well. These observations also justify
  finiteness in the H\"older estimate.

  We next take fixed-order limits. The target orders converge in $L^2$
  by Lemma~\ref{L:joint-fixed-order}.
  For the static orders the corresponding input is
  Chen--Hu~\cite{chen.hu:25:hyperbolic}*{Theorem~3.8(i), p.~2165}.
  For products of two fixed orders, the inequality
  \[
    \|YZ-Y'Z'\|_1
    \le\|Y-Y'\|_2\|Z\|_2+\|Y'\|_2\|Z-Z'\|_2
  \]
  gives $L^1$ convergence. There are only $2k+1$ split products, and
  a zero-order factor stays equal to one. Hence,
  $A_k^{\epsilon,\delta}(t)\to A_k(t)$ and
  $B_k^\epsilon(t)\to B_k(t)$ as the noise widths vanish. The uniform
  deterministic estimate~\eqref{E:planar-low-coefficient} needs no
  stochastic limit interpretation. Passing to limits
  in~\eqref{E:planar-coefficient-holder} gives
  \[
    A_k(t)\le
    \left(\frac{C_{\rm low}^{\,k}t^{(3-b_0)k}}{(k!)^2}\right)^\vartheta
    B_k(t)^{1-\vartheta}.
  \]
  Only now apply Lemma~\ref{L:planar-static-input}. No monotonicity
  in the spatial width or uniform static smoothed asymptotic was used.

  The parameter identities
  $\alpha=\vartheta+(1-\vartheta)\chi$ and
  $\alpha_0=\vartheta b_0$ imply
  \[
    2\vartheta+(1-\vartheta)(3-\chi)=3-\alpha,\qquad
    \vartheta(3-b_0)+(1-\vartheta)(4-\chi)=4-\alpha-\alpha_0.
  \]
  This yields the coefficient bound in~\eqref{E:planar-upper} with
  $C=C_{\rm low}^\vartheta C_{\rm st}^{1-\vartheta}$.
  The constant coefficient is $A_0=1$. For $q=3-\alpha>1$ and $z\ge0$,
  \[
    \sum_{k\ge0}\frac{z^k}{(k!)^q}
    =\sum_{k\ge0}\left(\frac{z^{k/q}}{k!}\right)^q
    \le\left(\sum_{k\ge0}\frac{z^{k/q}}{k!}\right)^q
    =e^{qz^{1/q}}.
  \]
  Proposition~\ref{P:mixed} supplies the nonnegative full series for
  the target solution. Take $z=Ct^{4-\alpha-\alpha_0}$ and use
  $(4-\alpha-\alpha_0)/q=\kappa$. This proves
  Proposition~\ref{P:planar-upper}.
\end{proof}

\begin{corollary}[Full planar parameter range]\label{C:planar-range}
  In dimension two, under Hypothesis~\ref{H:homog} and the standing
  covariance positivity assumptions, the upper bound
  $\E u^2(t,x)\le\exp(C_2t^\kappa)$ holds throughout
  $0<\alpha<2-\alpha_0$, with a finite constant $C_2$ depending on
  $\alpha_0$ and the spatial covariance.
  A nonnegative generalized covariance is interpreted as the homogeneous
  measure and its Gaussian approximations described above.
\end{corollary}

\begin{proof}
  For $0<\alpha\le1$, apply Proposition~\ref{P:low-alpha-upper}.
  For $1<\alpha<2-\alpha_0$, apply Proposition~\ref{P:planar-upper}.
  If the covariance vanishes, $u=1$ and $C_2=0$ suffices. This proves
  Corollary~\ref{C:planar-range}.
\end{proof}

\begin{remark}[Planar calibrations and remaining goals]\label{R:planar-scope}
  The exponent tends to $(4-\alpha)/(3-\alpha)$ as
  $\alpha_0\downarrow0$, consistently with the static source, without
  an interchange of limits or uniformity claim for the constants.
  For the nonzero higher-exponent case, Cauchy--Schwarz gives
  $\E u(t,x)\le\exp(qC^{1/q}t^\kappa/2)$.
  If the first-moment lower rate is at least $L_*$, this implies
  $2L_*\le qC^{1/q}$. No sharp constant is identified. The existing
  comparisons with Skorohod exponents, in their stated Riesz subclasses,
  concern different solution concepts and are not inputs here. The planar
  endpoint construction
  is dimension-specific; no general higher-exponent result in dimension
  three follows from it. Section~\ref{S:interval-upper} treats the full
  homogeneous-covariance class by a separate argument. The intrinsic
  constant is identified separately in
  Theorem~\ref{T:intrinsic-second-moment}.
\end{remark}

\section{Three-dimensional bounds from covariance endpoints}
\label{S:three-endpoints}

The endpoint constructions and conditional moment transfer are retained
as an alternative route. No general three-dimensional factorization is
asserted. The later full upper and intrinsic formula do not use these
factorizations.

We first construct the product endpoints. Zero coordinate exponents below
mean constant factors, not one-dimensional white noise.

\begin{lemma}[Strict product endpoints]\label{L:product-endpoints}
  Let $0\le a_j<1$ for $j=1,2,3$, let
  $\alpha=a_1+a_2+a_3\in(1,2)$, and choose $0<\vartheta<2-\alpha$.
  Put $\chi=(\alpha-\vartheta)/(1-\vartheta)$ and define
  \begin{equation}\label{E:product-endpoint-vectors}
    \begin{split}
      L_j&=\max\{0,(a_j-1+\vartheta)/\vartheta\},\qquad
      U_j=\min\{1,a_j/\vartheta\},\\
      \Lambda&=\frac{1-\sum_jL_j}{\sum_jU_j-\sum_jL_j},\qquad
      b_j=L_j+\Lambda(U_j-L_j),\qquad
      v_j=\frac{a_j-\vartheta b_j}{1-\vartheta}.
    \end{split}
  \end{equation}
  Then $0<\Lambda<1$, $\sum_j b_j=1$, $\sum_jv_j=\chi$, and
  \[
    a_j=\vartheta b_j+(1-\vartheta)v_j,\qquad
    a_j>0\Longrightarrow 0<b_j,v_j<1,\qquad
    a_j=0\Longrightarrow b_j=v_j=0.
  \]
  For any $c>0$, the ordinary covariance densities
  \[
    \gamma_a(x)=c\prod_{j=1}^3|x_j|^{-a_j},\qquad
    \gamma_b(x)=c\prod_{j=1}^3|x_j|^{-b_j},\qquad
    \gamma_v(x)=c\prod_{j=1}^3|x_j|^{-v_j}
  \]
  are nonnegative, even, positive definite, locally integrable and
  tempered. Their covariance homogeneity exponents are $\alpha,1,\chi$,
  respectively, with $\alpha<\chi<2$. For every $\epsilon>0$ and
  $z\in\R^3$,
  \begin{equation}\label{E:product-gaussian-comparison}
    (p_\epsilon*\gamma_a)(z)
    \le(p_\epsilon*\gamma_b)(z)^\vartheta
    (p_\epsilon*\gamma_v)(z)^{1-\vartheta}.
  \end{equation}
  A factor with exponent zero is defined to be one everywhere.
\end{lemma}

\begin{proof}
  We have $\vartheta<1$. There are at least two positive coordinates,
  since every $a_j<1$ and $\sum_j a_j>1$. At a zero coordinate,
  $L_j=U_j=0$. At a positive coordinate, $L_j<U_j$: if
  $a_j\ge\vartheta$, then $U_j=1$ and $L_j<1$; if
  $a_j<\vartheta$, then $U_j=a_j/\vartheta>0$, and either $L_j=0$
  or $U_j-L_j=(1-\vartheta)/\vartheta>0$.

  Let $I=\{j:L_j>0\}$ and $r=|I|$. For $r=0$ the sum of the lower
  endpoints is zero; for $r=1$ it is less than one. For $r\ge2$,
  \[
    \sum_{j\in I}a_j\le\alpha<2-\vartheta
    \le r-(r-1)\vartheta,
  \]
  because the last inequality is equivalent to
  $(r-2)(1-\vartheta)\ge0$. Therefore,
  \[
    \sum_jL_j
    =\frac{\sum_{j\in I}a_j-r+r\vartheta}{\vartheta}<1.
  \]
  If some $a_j\ge\vartheta$, its upper endpoint equals one and a
  different positive coordinate has positive upper endpoint. Otherwise,
  $\sum_jU_j=\alpha/\vartheta>1$. Hence,
  $\sum_jL_j<1<\sum_jU_j$, which proves $0<\Lambda<1$ and
  $\sum_jb_j=1$. At every positive coordinate,
  $L_j<b_j<U_j$, so $0<b_j<1$. The inequalities
  $b_j<U_j\le a_j/\vartheta$ and
  $b_j>L_j\ge(a_j-1+\vartheta)/\vartheta$ give $0<v_j<1$.
  At a zero coordinate $b_j=v_j=0$. The reconstruction identity is
  immediate, and summing it gives $\sum_jv_j=\chi$. Finally,
  \[
    \chi-\alpha=\frac{\vartheta(\alpha-1)}{1-\vartheta}>0,
    \qquad 2-\chi=\frac{2-\alpha-\vartheta}{1-\vartheta}>0.
  \]

  For any of the three exponent vectors $e$, local integrability is a
  product of one-dimensional integrals with exponents below one.
  For a Schwartz function $\psi$, choose $N>1$ and use
  $|\psi(x)|\le C_N\prod_j(1+|x_j|)^{-N}$. This proves absolute
  integrability against $\gamma_e$ and also temperedness. For each
  active coordinate, $0<e_j<1$, use
  \[
    |u|^{-e_j}=\frac1{\Gamma(e_j/2)}
    \int_0^\infty s^{e_j/2-1}e^{-su^2}\ud s.
  \]
  The product over the active coordinates is a positive mixture of
  Gaussian functions in those coordinates, constant in all other
  coordinates. Each such Gaussian is positive definite. For a complex
  Schwartz $\varphi$, set
  $\psi=\varphi*\widetilde{\varphi}$, where
  $\widetilde{\varphi}(x)=\overline{\varphi(-x)}$.
  The absolute integrability just proved permits Tonelli with $|\psi|$
  and then Fubini for the mixture against $\psi$. Its quadratic form
  is nonnegative. No Euler Gamma factor at exponent zero is introduced.
  Evenness and homogeneity follow from the displayed densities.

  The reconstruction of each exponent and the common amplitude imply
  $\gamma_a=\gamma_b^\vartheta\gamma_v^{1-\vartheta}$ almost
  everywhere; values on singular coordinate planes do not change these
  locally integrable covariances. H\"older's inequality on the Gaussian
  probability measure gives~\eqref{E:product-gaussian-comparison}.
  Its endpoint convolutions are finite by the product integrability and
  Gaussian decay. The amplitude remains $c^\vartheta c^{1-\vartheta}=c$.
  This proves Lemma~\ref{L:product-endpoints}.
\end{proof}

We now take $d=3$, $0<\alpha_0<1$, and $1<\alpha<2-\alpha_0$.
Let $\Gamma$ be a nonnegative, even, positive-definite tempered spatial
covariance, with homogeneity exponent $\alpha$. As a positive distribution
it is a Radon measure satisfying
$\Gamma(rA)=r^{3-\alpha}\Gamma(A)$; a covariance function is identified
with its density measure. Gaussian convolution is used for all covariance
products. Choose and fix
\begin{equation}\label{E:three-parameters}
  \alpha_0<\vartheta<2-\alpha,\qquad
  b_0=\alpha_0/\vartheta,\qquad
  \chi=(\alpha-\vartheta)/(1-\vartheta).
\end{equation}
Then $0<b_0<1$ and $\alpha<\chi<2$, by the identities in the preceding
proof. The zero target covariance is trivial, since then $u=1$.

\begin{hypothesis}[Gaussian covariance comparison]\label{H:three-endpoints}
  There are nonnegative, even, positive-definite tempered endpoint
  covariances $\Gamma_{\rm low}$ and $\Gamma_{\rm st}$ on $\R^3$
  with measure scaling
  \[
    \Gamma_{\rm low}(rA)=r^2\Gamma_{\rm low}(A),\qquad
    \Gamma_{\rm st}(rA)=r^{3-\chi}\Gamma_{\rm st}(A),
  \]
  such that, for every $\epsilon>0$ and $z\in\R^3$,
  \begin{equation}\label{E:three-gaussian-comparison}
    (p_\epsilon*\Gamma)(z)
    \le(p_\epsilon*\Gamma_{\rm low})(z)^\vartheta
    (p_\epsilon*\Gamma_{\rm st})(z)^{1-\vartheta}.
  \end{equation}
\end{hypothesis}

This is a condition on deterministic covariance measures and their Gaussian
convolutions. It assumes no moment estimate. We do not assert that every
homogeneous covariance in dimension three admits these endpoints.

\begin{lemma}[Plane-supported endpoints]\label{L:plane-endpoints}
  Retain~\eqref{E:three-parameters}, let $c>0$, and let $a_1,a_2\ge0$
  satisfy $s=a_1+a_2=\alpha-1$. In coordinates $(y,z)\in\R^2\times\R$,
  put
  \[
    m(\ud y,\ud z)=\ud y\,\delta_0(\ud z),\qquad
    v_j=\frac{a_j}{1-\vartheta},\qquad
    \Gamma_{\rm pl}=c\prod_{j=1}^2|y_j|^{-a_j}m.
  \]
  Zero coordinate powers mean one. Then
  \[
    \Gamma_{\rm low}=cm,\qquad
    \Gamma_{\rm st}=c\prod_{j=1}^2|y_j|^{-v_j}m
  \]
  satisfy Hypothesis~\ref{H:three-endpoints} for $\Gamma_{\rm pl}$.
  In the spectral convention of Lemma~\ref{L:alpha-one-convolution},
  this low endpoint has $V_{\rm low}=c/\pi$.
\end{lemma}

\begin{proof}
  Since $0<s<1-\alpha_0$ and $\vartheta<2-\alpha=1-s$,
  \[
    0\le a_j<1,\qquad 0\le v_j<1,\qquad
    v_1+v_2=\frac{s}{1-\vartheta}=\chi-1<1.
  \]
  A measure $f_e(y)\ud y\,\delta_0(\ud z)$, with
  $f_e(y)=\prod_j|y_j|^{-e_j}$ and $0\le e_j<1$, is locally finite.
  For a Schwartz test function, product-weighted rapid decay proves
  absolute integrability and temperedness. Its scaling exponent as
  a measure is $2-e_1-e_2$. Thus, the three measures in the statement
  have exponents $3-\alpha$, $2$, and $3-\chi$. They are even and
  nonnegative.

  We verify positive definiteness, including the normal Dirac measure.
  Each positive coordinate power has the Gaussian mixture
  \[
    |u|^{-e}=\frac1{\Gamma(e/2)}
    \int_0^\infty r^{e/2-1}e^{-ru^2}\ud r,\qquad 0<e<1;
  \]
  a zero coordinate contributes the positive-definite constant one.
  Consequently, $f_e$ is a positive mixture of positive-definite
  tangential Gaussian functions. For $\varphi\in\mathcal S(\R^3)$,
  its quadratic form against the plane measure is
  \[
    \int_\R\ud z\int_{\R^2}\int_{\R^2}
    f_e(y-y')\varphi(y,z)\overline{\varphi(y',z)}
    \ud y\ud y'.
  \]
  Absolute Fubini follows by setting
  \[
    A(u)=\int_\R\int_{\R^2}
    |\varphi(y+u,z)\varphi(y,z)|\ud y\ud z.
  \]
  Rapid decay gives $A(u)\le C_N\prod_j(1+|u_j|)^{-N}$.
  Hence, $\int f_e(u)A(u)\ud u<\infty$ for $N>1$, by
  one-dimensional integrability. Integrating the nonnegative Gaussian
  quadratic forms proves positive definiteness. This argument includes
  the low endpoint, where both coordinate powers are zero.

  For $\epsilon>0$ and $w\in\R^3$, apply H\"older on the finite
  positive measure $p_\epsilon(w-(y,z))m(\ud y,\ud z)$.
  Its mass is $p_\epsilon^{(1)}(w_3)$. If
  $f(y)=\prod_j|y_j|^{-a_j}$, the identity between ordinary densities
  \[
    cf=c^\vartheta
    \left(cf^{1/(1-\vartheta)}\right)^{1-\vartheta}
  \]
  holds $m$-almost everywhere. Both endpoint convolutions are finite,
  since $v_j<1$ and the Gaussian decays at infinity. H\"older gives
  exactly~\eqref{E:three-gaussian-comparison}; no power of a
  distribution is taken.

  Finally, the low spectral measure is
  \[
    \mu_{\rm low}(\ud\xi)
    =\frac{c}{2\pi}\delta_0(\ud\xi_1)\delta_0(\ud\xi_2)\ud\xi_3.
  \]
  This follows from the unit spectral atom of a constant and the
  one-dimensional Fourier identity for $\delta_0$ in the stated
  convention. Its unit-ball mass is $c/\pi$, so the uniform closing
  bound of Lemma~\ref{L:alpha-one-convolution} is $c/2$.
  This proves Lemma~\ref{L:plane-endpoints}.
\end{proof}

\begin{lemma}[Linear images and finite positive sums]\label{L:endpoint-closure}
  Fix the parameters in~\eqref{E:three-parameters}.
  The covariance comparison of Hypothesis~\ref{H:three-endpoints}
  is preserved by simultaneously pushing the target and its two
  endpoints forward under any invertible linear map $T:\R^3\to\R^3$.
  It is also preserved by finite sums with nonnegative weights, when
  all component comparisons use the same $\alpha,\vartheta,\chi$.
\end{lemma}

\begin{proof}
  First the comparison extends to every centered nondegenerate
  Gaussian probability density $q_\Sigma$ with covariance matrix
  $\Sigma$. Choose $a>0$ below the smallest eigenvalue of $\Sigma$.
  The Gaussian convolution identity gives
  $q_\Sigma=p_a*q_{\Sigma-aI}$. Put $F_J=p_a*J$ for each
  $J\in\{\Gamma,\Gamma_{\rm low},\Gamma_{\rm st}\}$.
  These functions are nonnegative, bounded, and continuous:
  Gaussian weighting makes their positive tempered spectral
  measures finite, and the covariance bound is
  $|F_J(x)|\le F_J(0)<\infty$.
  Tonelli and H\"older on the Gaussian probability measure yield
  \[
    q_\Sigma*\Gamma
    \le q_{\Sigma-aI}*
    \left(F_{\Gamma_{\rm low}}^\vartheta
    F_{\Gamma_{\rm st}}^{1-\vartheta}\right)
    \le(q_\Sigma*\Gamma_{\rm low})^\vartheta
    (q_\Sigma*\Gamma_{\rm st})^{1-\vartheta}.
  \]
  Every convolution here is finite.

  Write $J_T=T_\#J$ and $d_T=|\det T|$. Pushforward preserves
  nonnegativity, evenness, local finiteness, temperedness, and
  homogeneous scaling, since $T$ is invertible and commutes with
  scalar dilation. For positive definiteness, take a complex
  Schwartz function $\varphi$ and put $\psi(y)=\varphi(Ty)$.
  Then
  \[
    (\varphi*\widetilde\varphi)(Ty)
    =d_T(\psi*\widetilde\psi)(y).
  \]
  The quadratic form of $T_\#J$ is therefore $d_T$ times a
  nonnegative quadratic form of $J$.
  With $\Sigma=\epsilon T^{-1}(T^{-1})^\top$, direct Gaussian
  change of variables gives, for every $\epsilon>0$ and $x$,
  \[
    (p_\epsilon*J_T)(x)
    =d_T^{-1}(q_\Sigma*J)(T^{-1}x).
  \]
  Apply the preceding comparison. The two endpoint factors
  contribute $d_T^{-\vartheta}d_T^{-(1-\vartheta)}=d_T^{-1}$,
  which is the target factor. This proves the comparison for
  the three pushed-forward measures.

  For the finite-sum assertion, let
  $\Gamma_i,L_i,S_i$, $1\le i\le N$, be component triples, and let
  $w_i\ge0$. At a fixed width and translation put
  $l_i=(p_\epsilon*L_i)(x)$ and $s_i=(p_\epsilon*S_i)(x)$.
  Finite sums preserve all required covariance properties and scalings.
  Discrete H\"older gives
  \[
    \begin{split}
      p_\epsilon*\left(\sum_iw_i\Gamma_i\right)
      &\le\sum_i(w_il_i)^\vartheta(w_is_i)^{1-\vartheta}\\
      &\le\left(p_\epsilon*\sum_iw_iL_i\right)^\vartheta
      \left(p_\epsilon*\sum_iw_iS_i\right)^{1-\vartheta}.
    \end{split}
  \]
  Zero weights cause no ambiguity, since both powers are positive.
  The all-zero target also satisfies the comparison.
  This proves Lemma~\ref{L:endpoint-closure}.
\end{proof}

The linear maps in Lemma~\ref{L:endpoint-closure} act on the noise
covariances. All moment estimates below still use the original isotropic
wave kernel. Endpoint spectral masses and variational quantities are
computed for the transformed covariances; their values need not be
unchanged by a nonorthogonal map.

For the low endpoint let $V_{\rm low}=\mu_{\rm low}(B_1)$ in the
spectral convention of Lemma~\ref{L:alpha-one-convolution}, and put
\[
  Z_{b_0}=\frac2{(1-b_0)(2-b_0)},\qquad
  C_{\rm low}=2Z_{b_0}\pi V_{\rm low}.
\]
For the actual static endpoint, write
\[
  \mathcal{Q}_{\rm st}(g)
  =\int_{\R^3}\int_{\R^3}g(y+z)^2g(y)^2\ud y
  \,\Gamma_{\rm st}(\ud z),\qquad
  \mathcal{F}_3=\{g\in W^{1,2}(\R^3):\|g\|_2=1\},
\]
using real Sobolev functions, and define
\begin{equation}\label{E:three-static-variational}
  \begin{split}
    \mathcal{M}_{\rm st}
    &=\sup_{g\in\mathcal{F}_3}
    \left\{\mathcal{Q}_{\rm st}(g)^{1/2}-\|\nabla g\|_2^2\right\},\\
    Q&=3-\chi,\qquad \nu_{\rm st}=4-\chi,\qquad
    \Lambda_{\rm st}
    =2\left(\frac{2\sqrt{\mathcal{M}_{\rm st}}}{4-\chi}\right)^{4-\chi}.
  \end{split}
\end{equation}
The functional is precisely Chen--Hu's (1.11), p.~2147, for the endpoint
covariance, with unit gradient penalty. The positive-measure energy above
agrees with the spectral form on every real Sobolev profile by
Lemma~\ref{L:physical-spectral-energy}; thus no density is assigned to a
singular covariance. The lemma also supplies finiteness, since $\chi<2$
gives Dalang's condition as checked below.
Nonnegativity follows by dilating a unit-$L^2$ Schwartz function: its
energy term is nonnegative and its gradient penalty tends to zero.

\begin{proposition}[Conditional three-dimensional transfer]
  \label{P:three-transfer}
  Under the preceding assumptions and Hypothesis~\ref{H:three-endpoints},
  with $\Gamma\ne0$, there is a finite constant $C>0$ such that
  \begin{equation}\label{E:three-transfer}
    A_k(t)\le\frac{C^kt^{(4-\alpha-\alpha_0)k}}{(k!)^{3-\alpha}}
    \quad(k\ge1),\qquad
    \E u^2(t,x)\le\exp\left(qC^{1/q}t^\kappa\right),
    \quad q=3-\alpha.
  \end{equation}
  The estimates hold for all $t>0$ and $x\in\R^3$, with data $(1,0)$.
  The constant may depend on the fixed covariances, $\alpha_0$, and
  $\vartheta$, but not on $k,t,x$. In addition, the explicit variational
  upper constant satisfies
  \begin{equation}\label{E:three-variational-upper}
    \limsup_{t\to\infty}t^{-\kappa}\log\E u^2(t,x)
    \le q\left(C_{\rm low}^{\,\vartheta}
    \Lambda_{\rm st}^{\,1-\vartheta}\right)^{1/q}.
  \end{equation}
  This constant is not asserted sharp and is not substituted into the
  pure all-time exponential bound in~\eqref{E:three-transfer}.
\end{proposition}

\begin{proof}
  We first record the general static input needed here. For a static
  endpoint covariance $\Xi$ of exponent $\chi$, Fourier uniqueness
  gives $\mu_\Xi(rA)=r^\chi\mu_\Xi(A)$ for its positive spectral
  measure. Its unit-ball mass is finite, and
  \[
    \int_{\R^3}(1+|\xi|^2)^{-1}\mu_\Xi(\ud\xi)
    \le\mu_\Xi(B_1)
    +2^\chi\mu_\Xi(B_1)\sum_{j\ge0}2^{j(\chi-2)}<\infty.
  \]
  Thus, the static Dalang condition holds. Let $U_n$ be the source's
  ordered integrals for this covariance. Its nonnegative positive-definite
  tempered-distribution class is explicitly included by the generalized
  covariance convention in
  \cite{chen.hu:25:hyperbolic}*{p.~2152, (2.18)}; its homogeneity degree
  satisfies $0<\chi<2<3$. No density or angular regularity is added here.
  Let $U_0=1$, and set
  $B_k(t)=\sum_{m=0}^{2k}\E[U_m(t,x)U_{2k-m}(t,x)]$.
  If $\Xi=0$, then $B_k=0$ for $k\ge1$, and $C_{\rm st}=1$
  suffices in the bound below. For the remaining static calculation,
  assume $\Xi\ne0$. From Chen--Hu~\cite{chen.hu:25:hyperbolic}*{Theorem~3.8(i), p.~2165,
  and (2.17), (2.19)--(2.22), pp.~2151--2153}, the expectation and
  product rules give finite nonnegative coefficients with every split
  and pairing included; the latter formulas also specify the two-chain
  and measure conventions. Finiteness of
  the variational input follows from
  Chen~\cite{chen:23:exponential}*{Theorem~1.1, p.~2}, which gives a
  finite square-root variational supremum under Dalang's condition.
  Chen--Hu identify that supremum with
  $2^{\chi/(4-\chi)}\mathcal{M}$ on p.~2175. Hence, their
  coefficient-rate constant involving $\mathcal{M}$ is finite.
  For $\Xi=\Gamma_{\rm st}$ this functional is $\mathcal{M}_{\rm st}$
  defined above. Only finiteness, not a sharp value, is needed for the
  all-time coefficient bound.

  From Chen--Hu~\cite{chen.hu:25:hyperbolic}*{(5.1), p.~2173,
  and (5.15), p.~2180}, at $p=2$,
  \[
    B_k(t)=t^{(4-\chi)k}B_k(1),\qquad
    \limsup_{k\to\infty}\frac1k
    \log\left((k!)^{3-\chi}B_k(1)\right)<\infty.
  \]
  For $\Xi\ne0$, choose $R>0$ above this upper limit, then enlarge
  $e^R$ to cover the $k$th roots of the finitely many remaining
  quantities $(k!)^{3-\chi}B_k(1)$. We obtain a finite
  $C_{\rm st}=C_{\rm st}(\Xi)>0$ such that
  \begin{equation}\label{E:three-static-coefficient}
    B_k(t)\le\frac{C_{\rm st}^{\,k}t^{(4-\chi)k}}{(k!)^{3-\chi}},
    \qquad k\ge1,\quad t>0.
  \end{equation}
  Also $B_0=1$. We apply this source bound only after taking the
  fixed-order noise limits, with $\Xi=\Gamma_{\rm st}$.

  For the target, the same spectral scaling calculation has exponent
  $\alpha$. Its dyadic sum for the weight
  $(1+|\xi|^2)^{-(2-\alpha_0)/2}$ is finite because
  $\alpha<2-\alpha_0$. The target fixed-order limit is supplied by
  Lemma~\ref{L:joint-fixed-order}. The endpoint $\Gamma_{\rm low}$ has covariance
  exponent one, with $V_{\rm low},C_{\rm low}$ defined above.
  Finiteness of $V_{\rm low}$ follows from the Radon spectral measure.
  It is positive: otherwise homogeneity gives $\mu_{\rm low}=0$,
  contradicting~\eqref{E:three-gaussian-comparison} and $\Gamma\ne0$.

  Fix $k\ge1$, $t>0$, and positive widths $\epsilon,\delta,\eta$.
  Noise width $\epsilon$ means edge covariance width $2\epsilon$;
  $\delta$ is the target temporal cutoff and $\eta$ is Green smoothing.
  Write $X_n^{\epsilon,\delta,\eta}(t,x)$ for the source's ordered
  integral against its smoothed field $W_{\epsilon,\delta}$, with
  every Green kernel replaced by $G_{h,\eta}$, and set
  $X_0^{\epsilon,\delta,\eta}=1$. Explicitly, the target coefficient is
  \[
    A_k^{\epsilon,\delta,\eta}(t)
    =\sum_{m=0}^{2k}
    \E\left[X_m^{\epsilon,\delta,\eta}(t,x)
    X_{2k-m}^{\epsilon,\delta,\eta}(t,x)\right].
  \]
  On the full disjoint union over all splits $m+n=2k$ and all
  $D\in\Pi_k$, define a common finite positive measure by
  \[
    \int\Phi\ud\nu_{k,t,\eta}
    :=\sum_{m=0}^{2k}\sum_{D\in\Pi_k}
    \int_{[0,t]^m_<\times[0,t]^{2k-m}_<}\ud s
    \int\Phi(m,D,s,y)\prod_{l=1}^{2k}G_{h_l,\eta}(\ud y_l).
  \]
  Each chain has its own root; $h_l=s_l-s_{p(l)}$, $y_l$ is an
  increment, and $x_l$ is the cumulative position in its chain.
  Empty chains use empty products. The spatial mass is $\prod_lh_l$,
  so bounded time simplexes and finite discrete sums prove finiteness.
  This measure does not depend on which covariance is inserted.

  For $J\in\{\Gamma,\Gamma_{\rm low},\Gamma_{\rm st}\}$ set
  \[
    H_J=\prod_{(i,j)\in D}(p_{2\epsilon}*J)(x_i-x_j),\qquad
    T_b=\prod_{(i,j)\in D}|s_i-s_j|^{-b}.
  \]
  If $Q_\delta$ is the product of the target temporal covariances,
  the source cutoff gives $0\le Q_\delta\le T_{\alpha_0}
  =T_{b_0}^{\,\vartheta}$. The covariance hypothesis gives
  $H_\Gamma\le H_{\Gamma_{\rm low}}^\vartheta
  H_{\Gamma_{\rm st}}^{1-\vartheta}$ at the same edge width.
  Define the deterministic low endpoint and the actual regularized
  static coefficient by
  \[
    L_k^{\epsilon,\eta}(t)
    =\int T_{b_0}H_{\Gamma_{\rm low}}\ud\nu_{k,t,\eta},
    \qquad
    B_k^{\epsilon,\eta}(t)
    =\int H_{\Gamma_{\rm st}}\ud\nu_{k,t,\eta}.
  \]
  Gaussian moments and separate chain reversal identify the target
  regularized coefficient with $\int Q_\delta H_\Gamma
  \ud\nu_{k,t,\eta}$. The static identity has temporal covariance
  one and includes self-pairings. H\"older on the entire common measure
  yields
  \begin{equation}\label{E:three-regularized-holder}
    A_k^{\epsilon,\delta,\eta}(t)
    \le\left(L_k^{\epsilon,\eta}(t)\right)^\vartheta
    \left(B_k^{\epsilon,\eta}(t)\right)^{1-\vartheta}.
  \end{equation}
  No stochastic identity is assumed for $L_k^{\epsilon,\eta}$ with
  its raw temporal power, and no relation between different temporal
  cutoff kernels is used.

  Lemma~\ref{L:alpha-one-convolution} applies to the low endpoint
  with no angular-density assumption. Its uniform closing bound is
  $\pi V_{\rm low}/2$. Descending increment integration removes the
  only remaining covariance at each closing label; at each opening
  the paired covariance is already removed and the Green mass is $h_l$.
  The $k$ opening increments sum to at most $2t$. Consequently, the
  common spatial bound is $(\pi V_{\rm low})^kt^k/k^k$, uniformly in
  $\epsilon,\eta$. After summing pairings, the temporal integrand is
  symmetric in all $2k$ labels. Its full cube integral is
  $P_k(Z_{b_0}t^{2-b_0})^k$, where $P_k=(2k)!/(2^kk!)$.
  The block-order factors and the binomial split sum give
  \[
    P_k\sum_{m=0}^{2k}\frac1{m!(2k-m)!}=\frac{2^k}{k!}.
  \]
  Therefore,
  \begin{equation}\label{E:three-low-coefficient}
    L_k^{\epsilon,\eta}(t)
    \le\frac{C_{\rm low}^{\,k}t^{(3-b_0)k}}{k!\,k^k}
    \le\frac{C_{\rm low}^{\,k}t^{(3-b_0)k}}{(k!)^2}.
  \end{equation}
  Here $b_0<1$ makes the raw temporal cube integral finite. At fixed
  spatial width, the static covariance is bounded, so its regularized
  coefficient is finite too. This justifies the finite right side
  in~\eqref{E:three-regularized-holder}.

  We now identify the static inner Green limit with the source's
  prescribed zero-Green-width approximant. Take the source's static
  isonormal noise $W^{\rm st}$ with covariance $\Gamma_{\rm st}$ and set
  $W_\epsilon(x)=W^{\rm st}(p_\epsilon(x-\cdot))$.
  All widths are therefore on the source's Gaussian space, and the
  covariance is $p_{2\epsilon}*\Gamma_{\rm st}$.
  This covariance is bounded and
  continuous, since Gaussian weighting makes its positive tempered
  spectral measure finite. It has a continuous modification. Indeed,
  with $\mu_{\rm st}$ the spectral measure,
  \[
    \E|W_\epsilon(x+h)-W_\epsilon(x)|^2
    \le |h|^2\int_{\R^3}|\xi|^2e^{-\epsilon|\xi|^2}
    \mu_{\rm st}(\ud\xi).
  \]
  The integral is finite by temperedness. Gaussian eighth moments
  are therefore bounded by a constant times $|h|^8$.
  Kolmogorov's continuity criterion in dimension three, applied on
  compact sets and then on a countable exhaustion, gives the claimed
  modification. We choose this version.
  For $n\ge1$ define
  $\Phi_n(\mathbf{x})=\prod_{j=1}^n W_\epsilon(x_j)$ as an $L^2$
  random variable. Gaussian moments show that $\Phi_n$ is continuous
  as a map from $(\R^3)^n$ to $L^2$ and uniformly bounded there:
  if $v_\epsilon=(p_{2\epsilon}*\Gamma_{\rm st})(0)$, then
  \[
    \|\Phi_n(\mathbf{x})\|_2^2\le P_n v_\epsilon^n.
  \]
  The continuity follows by applying the same finite Gaussian moment
  formula to $\E|\Phi_n(\mathbf{x})-\Phi_n(\mathbf{x}')|^2$.
  Its separable continuous image is strongly measurable.

  Let $\mathfrak{g}_{n,t,x}^{\eta}$ be the finite positive ordered
  Green-chain measure, including its time variables, from the
  source's kernel (2.13), with each Green factor smoothed by $p_\eta$.
  For $\eta=0$, its spatial marginal is exactly the measure
  $\mu_n^{t,x}$ specified immediately before (2.22), pp.~2152--2153.
  Its mass is finite because each spatial factor has mass its time
  gap. Thus,
  \[
    U_n^{\epsilon,0}(t,x)
    :=\int\Phi_n(\mathbf{x})
    \mathfrak{g}_{n,t,x}^{0}(\ud\mathbf{s},\ud\mathbf{x})
  \]
  exists as a Bochner integral in $L^2$.
  We verify its agreement with the source's pathwise integral,
  rather than identifying it only by notation. Put
  $\rho=\mathfrak{g}_{n,t,x}^{0}$ and
  $M_n=P_n^{1/2}v_\epsilon^{n/2}$, and denote the pathwise integral
  by $J_n=\int\Phi_n\ud\rho$.
  The continuous field version makes the integrand jointly
  measurable. Since
  \[
    \int\E|\Phi_n|\ud\rho\le M_n\rho(1)<\infty,
    \qquad
    \|J_n\|_2
    \le\int\|\Phi_n\|_2\ud\rho\le M_n\rho(1),
  \]
  the pathwise integral exists almost surely and belongs to $L^2$.
  For every $Y\in L^2$, Cauchy--Schwarz and Fubini give
  \[
    \E[YJ_n]
    =\int\E[Y\Phi_n]\ud\rho.
  \]
  Bochner duality gives the same identity for the $L^2$ integral.
  Taking $Y=J_n-U_n^{\epsilon,0}$ identifies the two random
  variables almost surely. Changing to another jointly measurable
  field modification leaves the integral unchanged by Fubini.
  Since the static integrand is independent of the time variables,
  this is the integral against $\mu_n^{t,x}$ in the source's
  convention and hence its actual smoothed approximant
  $S_{n,\epsilon}$ with common width, from
  Chen--Hu~\cite{chen.hu:25:hyperbolic}*{(3.1), p.~2153,
  and the convention preceding (2.22)}.
  Define $U_n^{\epsilon,\eta}$ by the same formula with
  $\mathfrak{g}_{n,t,x}^{\eta}$, and retain $U_0^{\epsilon,\eta}=1$.

  In the second and mixed moments of these integrals, the Gaussian
  moment factors are bounded continuous functions of all spatial
  positions. For each pair of time vectors, weak convergence of the
  products of Green measures, including mixed products with one width
  already zero, applies to these functions. The masses are unchanged.
  A constant depending only on $n,\epsilon$ times the product of all
  time gaps dominates the resulting time integrals. This is integrable
  on the two bounded time simplexes. Hence, as $\eta\downarrow0$,
  \[
    \E\left[(U_n^{\epsilon,\eta})^2\right]
    \longrightarrow\E\left[(U_n^{\epsilon,0})^2\right],
    \qquad
    \E\left[U_n^{\epsilon,\eta}U_n^{\epsilon,0}\right]
    \longrightarrow\E\left[(U_n^{\epsilon,0})^2\right].
  \]
  Subtracting twice the second limit from the two square terms proves
  $U_n^{\epsilon,\eta}\to U_n^{\epsilon,0}$ in $L^2$.
  This identifies the limit with the source approximant, rather than
  only showing that positive-width approximants are Cauchy.
  For the target we specify the zero-Green-width object as well.
  At fixed $\epsilon,\delta$, its field covariance is
  $\gamma_\delta^0(s-r)(p_{2\epsilon}*\Gamma)(y-z)$, where
  \[
    \gamma_\delta^0(u)
    =\Gamma(\alpha_0)^{-1}\int_0^{1/\delta}
    e^{-\lambda|u|}\lambda^{\alpha_0-1}\ud\lambda,\qquad
    \gamma_\delta^0(0)
    =\frac{\delta^{-\alpha_0}}{\alpha_0\Gamma(\alpha_0)}.
  \]
  Here $\Gamma(\alpha_0)$ is Euler's gamma function.
  The variance
  $v_{\epsilon,\delta}
  =\gamma_\delta^0(0)(p_{2\epsilon}*\Gamma)(0)$ is finite.
  This field has a jointly continuous modification. The temporal
  covariance satisfies
  $\gamma_\delta^0(0)-\gamma_\delta^0(h)\le C_\delta|h|$,
  by $1-e^{-\lambda|h|}\le\lambda|h|$.
  The spatial increment bound just proved applies to
  $p_{2\epsilon}*\Gamma$. The joint increment variance is therefore
  bounded by $C_{\epsilon,\delta}(|h_0|+|h'|^2)$.
  Gaussian twelfth moments are bounded by
  $C_{\epsilon,\delta}|h|^6$ for $|h|\le1$.
  Kolmogorov's criterion in dimension four supplies the version.

  Let $\mathfrak{f}_{n,t,x}^{\eta}$ be the ordered Green measure
  of the target's kernel (2.16), with $s_{n+1}=t$, $x_{n+1}=x$:
  its factors are $G_{s_{j+1}-s_j,\eta}$.
  Define
  \[
    \begin{split}
      \Psi_n(\mathbf s,\mathbf x)
      &=\prod_{j=1}^nW_{\epsilon,\delta}(s_j,x_j),\\
      X_n^{\epsilon,\delta,0}(t,x)
      &=\int\Psi_n(\mathbf s,\mathbf x)
      \mathfrak f_{n,t,x}^{0}(\ud\mathbf s,\ud\mathbf x).
    \end{split}
  \]
  The Gaussian moment bound is
  $\|\Psi_n\|_2^2\le P_nv_{\epsilon,\delta}^n$.
  Joint measurability, finite measure mass, and the preceding
  Fubini argument show that this Bochner integral equals the
  pathwise integral in the target's prescribed convention
  \cite{chen:author2026:time-dependency}*{pp.~13--14}.
  The same definition at positive $\eta$ gives
  $X_n^{\epsilon,\delta,\eta}$ above.
  Its second and mixed $\eta/0$ moments converge by weak Green
  convergence against the bounded continuous Gaussian moment
  functions, with dominating bound a constant times the product
  of the time gaps. Thus,
  \[
    \|X_n^{\epsilon,\delta,\eta}
    -X_n^{\epsilon,\delta,0}\|_2\longrightarrow0.
  \]
  This proves the inner-limit identification with the actual
  target approximant. Both order-zero objects remain one.

  First take this Green limit in~\eqref{E:three-regularized-holder},
  using the uniform bound~\eqref{E:three-low-coefficient}. Next send
  the noise widths to zero. The static fixed-order $L^2$ limit is from
  Chen--Hu~\cite{chen.hu:25:hyperbolic}*{Theorem~3.8(i), p.~2165};
  the target fixed-order limit is from
  Lemma~\ref{L:joint-fixed-order}.
  Products of two fixed orders converge in $L^1$, since
  \[
    \|YZ-Y'Z'\|_1
    \le\|Y-Y'\|_2\|Z\|_2+\|Y'\|_2\|Z-Z'\|_2.
  \]
  The split sums are finite, and zero-order factors remain one.
  We obtain
  \[
    A_k(t)\le
    \left(\frac{C_{\rm low}^{\,k}t^{(3-b_0)k}}{(k!)^2}\right)^\vartheta
    B_k(t)^{1-\vartheta}.
  \]
  Only now use~\eqref{E:three-static-coefficient}. Neither monotonicity
  of spatial smoothing nor a uniform smoothed static asymptotic was
  needed. The identities
  \[
    \begin{split}
      2\vartheta+(1-\vartheta)(3-\chi)&=3-\alpha,\\
      \vartheta(3-b_0)+(1-\vartheta)(4-\chi)&=4-\alpha-\alpha_0
    \end{split}
  \]
  give the coefficient estimate with
  $C=C_{\rm low}^{\,\vartheta}C_{\rm st}^{\,1-\vartheta}$.
  Finally, $A_0=1$, $q=3-\alpha>1$, and
  \[
    \sum_{k\ge0}\frac{z^k}{(k!)^q}
    \le\left(\sum_{k\ge0}\frac{z^{k/q}}{k!}\right)^q
    =e^{qz^{1/q}},\qquad z\ge0.
  \]
  The nonnegative full series of Proposition~\ref{P:mixed}, with
  $z=Ct^{4-\alpha-\alpha_0}$ and
  $(4-\alpha-\alpha_0)/q=\kappa$, yields the moment estimate.
  It remains to prove~\eqref{E:three-variational-upper}. The precise
  upper coefficient rate in Chen--Hu's (5.15), p.~2180, at $p=2$ is
  \[
    \begin{split}
      \limsup_{k\to\infty}
      \left((k!)^Q B_k(1)\right)^{1/k}
      &\le 2^{-Q}2^{\nu_{\rm st}}
      \left(\frac{2\sqrt{\mathcal{M}_{\rm st}}}{\nu_{\rm st}}\right)^{\nu_{\rm st}}\\
      &=\Lambda_{\rm st}.
    \end{split}
  \]
  The factor two follows from $\nu_{\rm st}-Q=1$; the logarithm in
  the source applies to the entire coefficient-rate product.
  Fix $r>0$. There is $N_r\ge1$, depending on the fixed endpoint
  and $r$ but not on $t$, such that
  \[
    B_k(1)\le\frac{(\Lambda_{\rm st}+r)^k}{(k!)^Q},
    \qquad k\ge N_r.
  \]
  Static coefficient homogeneity and the already established
  coefficient H\"older inequality therefore give, simultaneously for
  every $t>0$ and $k\ge N_r$,
  \[
    A_k(t)\le\frac{D_r^k t^{\beta k}}{(k!)^q},\qquad
    D_r=C_{\rm low}^{\,\vartheta}(\Lambda_{\rm st}+r)^{1-\vartheta},
    \qquad \beta=4-\alpha-\alpha_0.
  \]
  For each $1\le k<N_r$ the same inequality with the exact static
  coefficient gives $A_k(t)\le d_kt^{\beta k}$, where
  \[
    d_k=\frac{C_{\rm low}^{\,\vartheta k}
    B_k(1)^{1-\vartheta}}{(k!)^{2\vartheta}}<\infty.
  \]
  Adding $A_0=1$ and the nonnegative series yields
  \[
    \E u^2(t,x)\le P_r(t)+e^{qD_r^{1/q}t^\kappa},\qquad
    P_r(t)=1+\sum_{k=1}^{N_r-1}d_kt^{\beta k}.
  \]
  This finite power sum has $\log P_r(t)/t^\kappa\to0$; its
  exponents need not be integers. The logarithm of a sum of two
  positive terms is at most the larger logarithm plus $\log2$.
  Consequently, the required limsup is at most $qD_r^{1/q}$.
  Let $r\downarrow0$ to obtain~\eqref{E:three-variational-upper}.
  This also covers a zero static rate, without division by that rate.
  The exact static homogeneity makes $N_r$ independent of $t$;
  no target coefficient homogeneity or smoothed static asymptotic was
  invoked. The finitely many low orders were kept, so this argument
  does not replace the all-time constant by the asymptotic one.
  This proves Proposition~\ref{P:three-transfer}.
\end{proof}

\begin{corollary}[Ordinary product and Riesz covariances in dimension three]
  \label{C:three-product-riesz}
  Let $d=3$, $0<\alpha_0<1$, and $1<\alpha<2-\alpha_0$.
  The coefficient and all-time moment estimates in~\eqref{E:three-transfer},
  and the asymptotic estimate in~\eqref{E:three-variational-upper}, hold
  for either of the following spatial covariances, with $c>0$:
  \begin{enumerate}
    \item $\gamma(x)=c\prod_{j=1}^3|x_j|^{-a_j}$, where
      $0\le a_j<1$ and $\sum_j a_j=\alpha$;
    \item $\gamma(x)=c|x|^{-\alpha}$.
  \end{enumerate}
  In the first case the constant depends only on $a_1,a_2,a_3,c,\alpha_0$;
  in the second it depends only on $\alpha,c,\alpha_0$.
  A zero coordinate exponent denotes a constant factor; the case $a_j=1$
  and any interpretation of it as coordinate white noise are excluded.
\end{corollary}

\begin{proof}
  In both cases choose the fixed midpoint
  $\vartheta=(\alpha_0+2-\alpha)/2$ and define $b_0,\chi$
  by~\eqref{E:three-parameters}. Then
  $\alpha_0<\vartheta<2-\alpha$, and all subsequent choices depend
  only on the data in the statement.
  For the product covariance, Lemma~\ref{L:product-endpoints} supplies
  $b,v$ by its explicit interval formula. Its same-amplitude endpoint
  densities $\gamma_b,\gamma_v$ are admissible covariance measures
  of exponents one and $\chi$. Their common-width Gaussian inequality
  is exactly Hypothesis~\ref{H:three-endpoints}.

  For the Riesz covariance take $\gamma_1(x)=c|x|^{-1}$ and
  $\gamma_\chi(x)=c|x|^{-\chi}$. Each degree $e\in\{1,\alpha,\chi\}$
  is less than three, so the corresponding density is locally integrable
  and tempered. Positive definiteness follows from the Gaussian mixture
  \[
    c|x|^{-e}=\frac{c}{\Gamma(e/2)}
    \int_0^\infty s^{e/2-1}e^{-s|x|^2}\ud s.
  \]
  For a Schwartz autocorrelation, absolute integrability follows from
  $e<3$ near zero and rapid decay at infinity. Tonelli and Fubini
  therefore justify integrating the positive Gaussian quadratic forms.
  The affine identity $\alpha=\vartheta+(1-\vartheta)\chi$ gives
  $\gamma_\alpha=\gamma_1^\vartheta\gamma_\chi^{1-\vartheta}$
  almost everywhere, with the same amplitude $c$. H\"older on the
  Gaussian probability measure proves the required common-width
  comparison for every $\epsilon,z$. Thus, in both cases all endpoint
  hypotheses are discharged.
  Proposition~\ref{P:three-transfer} applies. This proves
  Corollary~\ref{C:three-product-riesz}.
\end{proof}

\begin{corollary}[Finite sums of linear images]\label{C:three-finite-images}
  Let $d=3$, $0<\alpha_0<1$, and $1<\alpha<2-\alpha_0$.
  Let $\Gamma_i$, $1\le i\le N$, belong to one of the following
  classes, always with homogeneity exponent $\alpha$:
  \begin{enumerate}
    \item the ordinary products in Corollary~\ref{C:three-product-riesz};
    \item the isotropic Riesz covariances in that corollary;
    \item the plane-supported measures of Lemma~\ref{L:plane-endpoints},
      with $a_1+a_2=\alpha-1$.
  \end{enumerate}
  Let $T_i:\R^3\to\R^3$ be invertible linear maps, and let
  $w_i\ge0$ with $\sum_iw_i>0$. Then the coefficient, all-time
  moment, and nonsharp variational estimates
  \eqref{E:three-transfer}--\eqref{E:three-variational-upper}
  hold for
  \[
    \Gamma=\sum_{i=1}^Nw_i(T_i)_\#\Gamma_i.
  \]
  The constants may depend on all fixed component data, maps and
  weights. The endpoints and their variational quantities are
  those constructed in the proof.
\end{corollary}

\begin{proof}
  Choose the common midpoint
  $\vartheta=(\alpha_0+2-\alpha)/2$, and let $b_0,\chi$ be
  given by~\eqref{E:three-parameters}.
  Lemma~\ref{L:product-endpoints} supplies the ordinary-product
  endpoints. For a Riesz component use $c_i|x|^{-1}$ and
  $c_i|x|^{-\chi}$: the Gaussian-mixture calculation in the
  preceding proof verifies their covariance properties, and
  $\alpha=\vartheta+(1-\vartheta)\chi$ gives their Gaussian
  comparison by H\"older. Lemma~\ref{L:plane-endpoints} supplies
  the plane-supported endpoints. Thus, every component has an
  endpoint triple with these same fixed parameters.

  Apply Lemma~\ref{L:endpoint-closure} first to $T_i$ on each
  triple, then to the finite weighted sums. The resulting endpoints
  are
  \[
    \Gamma_{\rm low}=\sum_iw_i(T_i)_\#\Gamma_{{\rm low},i},
    \qquad
    \Gamma_{\rm st}=\sum_iw_i(T_i)_\#\Gamma_{{\rm st},i}.
  \]
  They satisfy Hypothesis~\ref{H:three-endpoints}. The target is
  nonzero because all components are positive nonzero measures
  and some weight is positive.
  Proposition~\ref{P:three-transfer} now applies to these actual
  target and endpoint measures. No addition or coupling identity
  for random solutions is used.
  This proves Corollary~\ref{C:three-finite-images}.
\end{proof}

[held back until the source author has been told]

\section{Physical and spectral energy for measure covariances}
\label{S:energy-fidelity}

This section justifies the positive-measure energy used
in~\eqref{E:three-static-variational}. It does not assume
Hypothesis~\ref{H:three-endpoints} or the conditional moment bound.
The imported analytic input is the finiteness of the variation on the
right of (1.5), stated in the closing sentence of
Chen~\cite{chen:23:exponential}*{Theorem~1.1, p.~2}.

This source-functional identification does not promote the separate
conditional moment argument or resolve general covariance factorization.

\begin{lemma}[Sobolev energy identification]\label{L:physical-spectral-energy}
  Let $\Xi$ be a nonnegative, even, positive-definite tempered Radon
  covariance on $\R^3$, with
  $\Xi(rA)=r^{3-\chi}\Xi(A)$ for $0<\chi<2$.
  Let $\mu_\Xi$ be its positive even spectral measure in the convention
  $\Xi=\int e^{i\xi\cdot x}\mu_\Xi(\ud\xi)$, understood distributionally,
  and use the Fourier transform
  $\widehat h(\xi)=\int e^{-i\xi\cdot x}h(x)\ud x$.
  For every real $g\in W^{1,2}(\R^3)$,
  \begin{equation}\label{E:physical-spectral-energy}
    \mathcal Q_\Xi(g)
    :=\int_{\R^3}\int_{\R^3}g(y+z)^2g(y)^2\ud y\,\Xi(\ud z)
    =\int_{\R^3}|\widehat{g^2}(\xi)|^2\mu_\Xi(\ud\xi)<\infty.
  \end{equation}
  The physical expression is independent of the Borel representative
  of $g$. There is a finite $C_0\ge0$, depending on $\Xi$, such that
  \begin{equation}\label{E:energy-quartic-bound}
    \mathcal Q_\Xi(g)
    \le\frac12\|g\|_2^2\|\nabla g\|_2^2+C_0\|g\|_2^4.
  \end{equation}
\end{lemma}

\begin{proof}
  Fourier uniqueness gives
  $\mu_\Xi(rA)=r^\chi\mu_\Xi(A)$.
  Since its unit-ball mass is finite, the dyadic estimate with
  $\sum_{j\ge0}2^{j(\chi-2)}$ verifies Dalang's condition.
  For a real Schwartz function $h$ put
  \[
    \mathscr E(h)=\int|\widehat h(\xi)|^2\mu_\Xi(\ud\xi),
    \qquad Q(f)=\mathscr E(f^2).
  \]
  Schwartz Fourier pairing identifies $Q(f)$ with its ordinary
  positive-measure integral. From the finiteness assertion in
  Chen~\cite{chen:23:exponential}*{Theorem~1.1, closing sentence
  for the variation in (1.5), p.~2},
  restricted to real unit-$L^2$ Schwartz profiles, there is $C_0\ge0$
  such that $Q(g)\le\frac12\|\nabla g\|_2^2+C_0$ for $\|g\|_2=1$.
  For $f\ne0$, quartic homogeneity gives
  \[
    Q(f)=\|f\|_2^4Q(f/\|f\|_2)
    \le\frac12\|f\|_2^2\|\nabla f\|_2^2+C_0\|f\|_2^4.
  \]
  The same inequality is immediate for $f=0$.
  Only Schwartz pairings have been used at this point, so this import
  presupposes no energy identification for nonsmooth profiles.
  If $N(f)^2=\|f\|_2^2+\|\nabla f\|_2^2$, it follows that
  $Q(f)^{1/2}\le D N(f)^2$ for some finite $D$.

  We need two different Cauchy--Schwarz inequalities.
  For real Schwartz $f,h$, spectral Cauchy--Schwarz gives
  \[
    \begin{split}
      0\le P(f,h)
      &:=\int\Xi(\ud z)\int f(y+z)^2h(y)^2\ud y\\
      &=\int\widehat{f^2}(\xi)
      \overline{\widehat{h^2}(\xi)}\mu_\Xi(\ud\xi)
      \le Q(f)^{1/2}Q(h)^{1/2}.
    \end{split}
  \]
  Evenness makes the Fourier sign convention in this real pairing
  immaterial. On the other hand, Cauchy--Schwarz on the positive
  measure $\ud y\,\Xi(\ud z)$ gives
  \[
    \mathscr E(fh)
    =\int\Xi(\ud z)\int
    f(y+z)f(y)h(y+z)h(y)\ud y
    \le Q(f)^{1/2}Q(h)^{1/2}.
  \]
  All these are absolutely convergent Schwartz pairings.
  In particular, $\mathscr E(fh)$ is the quadratic energy of $fh$,
  not the quartic expression $Q(fh)$.

  Let $\mathfrak m(\ud y,\ud z)=\ud y\,\Xi(\ud z)$ and define
  \[
    A_f(y,z)=f(y+z)f(y),\qquad B_f(\xi)=\widehat{f^2}(\xi).
  \]
  The measure $\mathfrak m$ is positive and sigma-finite.
  The decomposition
  \[
    A_f-A_h=(f-h)(y+z)f(y)+h(y+z)(f-h)(y)
  \]
  and the bound for $P$ imply
  \[
    \|A_f-A_h\|_{L^2(\mathfrak m)}
    \le D\bigl(N(f)+N(h)\bigr)N(f-h).
  \]
  Since $f^2-h^2=(f-h)(f+h)$, the bound for $\mathscr E$ gives
  \[
    \|B_f-B_h\|_{L^2(\mu_\Xi)}
    \le D N(f-h)N(f+h)
    \le D\bigl(N(f)+N(h)\bigr)N(f-h).
  \]

  Choose real Schwartz $f_n\to g$ in $W^{1,2}$.
  These estimates make both $A_{f_n}$ and $B_{f_n}$ Cauchy in
  their respective $L^2$ spaces. Pass to a subsequence with
  $f_n\to g$ Lebesgue-almost everywhere.
  Translation invariance of Lebesgue measure and sigma-finite Fubini give
  \[
    f_n(y+z)f_n(y)\longrightarrow g(y+z)g(y)
    \quad\text{for }\mathfrak m\text{-almost every }(y,z).
  \]
  Thus, the strong $L^2(\mathfrak m)$ limit is $A_g$.
  The same Fubini argument shows that changing the Borel
  representative of $g$ does not change this limit.

  Also
  \[
    \|f_n^2-g^2\|_1
    \le\|f_n-g\|_2(\|f_n\|_2+\|g\|_2)\longrightarrow0.
  \]
  Hence, $\widehat{f_n^2}\to\widehat{g^2}$ uniformly on all
  frequencies. A subsequence of its strong $L^2(\mu_\Xi)$ limit
  converges $\mu_\Xi$-almost everywhere, and must agree with this
  uniform limit. Consequently, that strong limit is $B_g$.
  For every $n$,
  $\|A_{f_n}\|_{L^2(\mathfrak m)}^2
  =Q(f_n)=\|B_{f_n}\|_{L^2(\mu_\Xi)}^2$.
  Passing to the strong limits proves
  \eqref{E:physical-spectral-energy}, including finiteness.
  Passing the Schwartz quartic bound to the same limit proves
  \eqref{E:energy-quartic-bound}.
  This proves Lemma~\ref{L:physical-spectral-energy}.
\end{proof}

In particular, for $\|g\|_2=1$ the energy is at most
$\|\nabla g\|_2^2/2+C_0$. Therefore, the supremum of
$\mathcal Q_\Xi(g)^{1/2}-\|\nabla g\|_2^2$ is finite.
Applied to $\Xi=\Gamma_{\rm st}$, the profile-by-profile identity
justifies the actual measure-form functional in
\eqref{E:three-static-variational} without assigning a density to
the covariance or borrowing a disputed special-case constant.

\section{A static phase estimate at first variance order}
\label{S:static-phase}

A time-block argument would have to carry both position and velocity.
We establish a uniform estimate for the first variance coefficient with
arbitrary deterministic initial phase. The covariance may be any member
of the original three-dimensional class; no endpoint representation is
assumed. The estimate below is not an all-order propagator bound.



Let $0<\alpha<2$, and let $\Gamma$ be a nonnegative, even,
positive-definite tempered Radon covariance on $\R^3$, satisfying
$\Gamma(rA)=r^{3-\alpha}\Gamma(A)$. Its spectral convention is
$\Gamma=\int e^{i\xi\cdot x}\mu(\ud\xi)$. Put
\begin{equation}\label{E:phase-constants}
  \begin{split}
    V&=\mu(B_1),\qquad M=\Gamma(B_1),\qquad
    R_\alpha=\frac{\alpha\pi V}{2\sin(\pi\alpha/2)},\\
    c_\Gamma&=\frac{(3-\alpha)M}{4\pi},\qquad
    b_\alpha=2^\alpha+\frac{3^{2-\alpha}}{2-\alpha},\qquad
    D_\Gamma=c_\Gamma b_\alpha.
  \end{split}
\end{equation}
Here $B_1$ is the open unit ball in the relevant variable.
The physical mass $M$ and the spectral mass $V$ are not identified.
Let $p_\epsilon$ be the Brownian Gaussian density with covariance
$\epsilon I$, and set
$\Gamma_\epsilon=p_{2\epsilon}*\Gamma$.

\begin{lemma}[Two static contraction bounds]\label{L:phase-contractions}
  For $\lambda>0$, $q\in\R^3$, $a>0$, and $\epsilon>0$,
  \begin{align}
    \int_{\R^3}\frac{\mu(\ud\xi)}{\lambda^2+|q+\xi|^2}
    &\le R_\alpha\lambda^{\alpha-2},
    \label{E:phase-resolvent}\\
    \left|T_\epsilon(a,q)\right|
    &\le D_\Gamma a^{1-\alpha},
    \label{E:phase-trace}\\
    T_\epsilon(a,q)
    &:=\int_{\R^3}e^{iq\cdot x}\Gamma_\epsilon(x)G_a(\ud x)
    =\int_{\R^3}\widehat G_a(q+\xi)e^{-\epsilon|\xi|^2}
    \mu(\ud\xi).\nonumber
  \end{align}
\end{lemma}

\begin{proof}
  Homogeneity and Fourier uniqueness give
  $\mu(B_r)=Vr^\alpha$. In particular, there is no origin atom.
  For $s>0$, Schwartz Fourier pairing yields
  \[
    \int e^{-s|q+\xi|^2}\mu(\ud\xi)
    =\int p_{2s}(x)e^{iq\cdot x}\Gamma(\ud x)
    \le\int p_{2s}(x)\Gamma(\ud x)
    =\int e^{-s|\xi|^2}\mu(\ud\xi).
  \]
  The integrals are finite. Evenness makes the middle integral real,
  and nonnegativity of $\Gamma$ gives the inequality. Multiply by
  $e^{-\lambda^2s}$ and integrate in $s$. Nonnegative Tonelli on
  the spectral side gives the resolvent comparison. At $q=0$ its
  value is
  \[
    \alpha V\int_0^\infty\frac{r^{\alpha-1}}{\lambda^2+r^2}\ud r
    =R_\alpha\lambda^{\alpha-2}.
  \]
  This proves~\eqref{E:phase-resolvent}.

  Since $\mu$ is tempered, its Gaussian weighting is finite. Fourier
  Fubini therefore gives the identity for $T_\epsilon$. The measure
  $\Gamma_\epsilon(x)G_a(\ud x)$ is finite and nonnegative, whence
  $|T_\epsilon(a,q)|\le T_\epsilon(a,0)$.
  The radial distribution function of $\Gamma$ is
  $\Gamma(B_r)=Mr^{3-\alpha}$. Thus, for every nonnegative radial
  Schwartz function $F$,
  \[
    \int F(x)\Gamma(\ud x)
    =(3-\alpha)M\int_0^\infty F(r)r^{2-\alpha}\ud r
    =c_\Gamma\int_{\R^3}F(x)|x|^{-\alpha}\ud x.
  \]
  Apply this to $F=G_a*p_{2\epsilon}$, which is radial and Schwartz.
  Nonnegative Fubini gives
  \[
    T_\epsilon(a,0)
    =c_\Gamma[p_{2\epsilon}*(G_a*|\cdot|^{-\alpha})](0)
    \le c_\Gamma\sup_z(G_a*|\cdot|^{-\alpha})(z).
  \]
  Write $r=|z|$. The spherical wave measure has mass $a$, and direct
  integration over its normal coordinate gives, for $r>0$,
  \[
    (G_a*|\cdot|^{-\alpha})(z)
    =\frac{(a+r)^{2-\alpha}-|a-r|^{2-\alpha}}
    {2r(2-\alpha)}.
  \]
  For $r<a/2$, distances from $z$ to the sphere are at least $a/2$,
  giving the bound $2^\alpha a^{1-\alpha}$. For $r>2a$, they are
  at least $a$, giving $a^{1-\alpha}$. On $a/2\le r\le2a$, the
  displayed formula is at most
  $3^{2-\alpha}a^{1-\alpha}/(2-\alpha)$. These bounds also cover
  the endpoints by continuity and give~\eqref{E:phase-trace}.
  This proves Lemma~\ref{L:phase-contractions}.
\end{proof}

Let $A_\lambda=\lambda^2-\Delta$, and equip deterministic phase pairs
with the norm
\begin{equation}\label{E:phase-norm}
  \|(f,g)\|_\lambda^2
  =\|f\|_2^2+\|A_\lambda^{-1/2}g\|_2^2.
\end{equation}
Let $C_t$ be the Fourier multiplier $\cos(t|\xi|)$.
On one static isonormal Gaussian space with covariance $\Gamma$, use
$W_\epsilon(x)=W(p_\epsilon(x-\cdot))$. Its covariance is exactly
$\Gamma_\epsilon(x-y)$, with spectral measure
$\mu_\epsilon(\ud\xi)=e^{-\epsilon|\xi|^2}\mu(\ud\xi)$.
For real Schwartz $f,g$, define the free position
$w_0(t)=C_tf+G_t*g$ and its phase $Z_0(t)=(w_0(t),\dot w_0(t))$.
The next two regularized static Duhamel phases are
\begin{equation}\label{E:phase-duhamel}
  Z_{j+1}(t)
  =\int_0^t
  \begin{pmatrix}
    G_{t-s}*(W_\epsilon Z_{j,u}(s))\\
    C_{t-s}(W_\epsilon Z_{j,u}(s))
  \end{pmatrix}\ud s,\qquad j=0,1,
\end{equation}
where $Z_{j,u}$ is the position component. At fixed $\epsilon>0$
these are Gaussian-polynomial Bochner integrals in the indicated
$L^2$ phase space.

\begin{proposition}[First variance estimate for arbitrary phase]
  \label{P:static-phase-variance}
  Let $N=\|(f,g)\|_\lambda$. Uniformly in $\epsilon>0$,
  \begin{align}
    \E\|Z_1(h)\|_\lambda^2
    &\le R_\alpha h^2\lambda^{\alpha-2}
    (1+\lambda^2h^2)^2N^2,\label{E:phase-born}\\
    \|\E Z_2(h)\|_\lambda
    &\le\frac{D_\Gamma(1+\lambda^2h^2)h^{3-\alpha}}
    {\lambda(2-\alpha)(3-\alpha)}N.
    \label{E:phase-mean}
  \end{align}
  In particular, put $\lambda=h^{-1}$ and let $K_\epsilon$ be the
  coefficient of $\sigma^2$ in the finite polynomial
  $\E\|Z_0(h)+\sigma Z_1(h)+\sigma^2Z_2(h)\|_\lambda^2$.
  Then
  \begin{equation}\label{E:phase-variance}
    |K_\epsilon|
    \le\left(4R_\alpha+
    \frac{4\sqrt e\,D_\Gamma}{(2-\alpha)(3-\alpha)}\right)
    h^{4-\alpha}\|(f,g)\|_{1/h}^2.
  \end{equation}
\end{proposition}

\begin{proof}
  We use the unnormalized spatial Fourier transform and Plancherel
  measure $(2\pi)^{-3}\ud\eta$.
  At fixed positive smoothing, Gaussian second and fourth moments
  make~\eqref{E:phase-duhamel} integrable: $G_t$ has finite positive
  mass, $C_t$ is an $L^2$ contraction, and
  $\E|W_\epsilon(x)W_\epsilon(y)|^2
  \le3\Gamma_\epsilon(0)^2$.
  These facts, Minkowski and time integration justify the Gaussian
  and Fourier Fubini steps below first for Schwartz data.

  Set $a_s(\eta)=\widehat w_0(s,\eta)$ and
  \[
    e_\lambda(\eta)=|\widehat f(\eta)|^2+
    \frac{|\widehat g(\eta)|^2}{\lambda^2+|\eta|^2}.
  \]
  Cauchy--Schwarz on the two initial coordinates gives
  \[
    |a_s(\eta)|^2\le(1+\lambda^2s^2)e_\lambda(\eta),
  \]
  because the squared norm of their coefficient vector is
  $\cos^2(sq)+(1+\lambda^2/q^2)\sin^2(sq)
  \le1+\lambda^2s^2$, with the continuous value at $q=0$.
  For the two-component output multiplier put
  \[
    k_\tau(r)=\left(\frac{\sin(\tau r)}r,
    \frac{\cos(\tau r)}{\sqrt{\lambda^2+r^2}}\right).
  \]
  Its Euclidean squared norm is
  \[
    |k_\tau(r)|^2
    =\frac{1+\lambda^2\sin^2(\tau r)/r^2}{\lambda^2+r^2}
    \le\frac{1+\lambda^2h^2}{\lambda^2+r^2},\qquad 0\le\tau\le h.
  \]
  Expanding the covariance of the two copies of $W_\epsilon$,
  followed by spatial Plancherel, gives exactly
  \[
    \E\|Z_1(h)\|_\lambda^2
    =\frac1{(2\pi)^3}\int\ud\eta\int\mu_\epsilon(\ud\xi)
    \left|\int_0^h k_{h-s}(|\eta+\xi|)a_s(\eta)\ud s\right|^2.
  \]
  Cauchy--Schwarz in time bounds the last squared norm by
  \[
    \frac{h^2(1+\lambda^2h^2)^2}
    {\lambda^2+|\eta+\xi|^2}e_\lambda(\eta).
  \]
  Now $\mu_\epsilon\le\mu$ and
  Lemma~\ref{L:phase-contractions} give~\eqref{E:phase-born}.

  The contraction inside the mean of $Z_2$ is the convolution
  operator with kernel $G_{s-r}(\ud x)\Gamma_\epsilon(x)$.
  Indeed, this follows directly from
  $\E[W_\epsilon(x)W_\epsilon(y)]=\Gamma_\epsilon(x-y)$
  in the two Duhamel integrals. Its Fourier multiplier is
  $T_\epsilon(s-r,\eta)$, up to the immaterial even sign.
  Its $L^2$ operator norm is therefore at most
  $D_\Gamma(s-r)^{1-\alpha}$.
  Under the isometry $(u,v)\mapsto(u,A_\lambda^{-1/2}v)$,
  $\|k_\tau(|D|)\|_{L^2\to L^2\oplus L^2}
  \le\sqrt{1+\lambda^2h^2}/\lambda$ and
  $\|w_0(r)\|_2\le\sqrt{1+\lambda^2h^2}N$.
  Minkowski and
  \[
    \int_0^h\ud s\int_0^s(s-r)^{1-\alpha}\ud r
    =\frac{h^{3-\alpha}}{(2-\alpha)(3-\alpha)}
  \]
  prove~\eqref{E:phase-mean}.

  Finally, the free phase obeys
  $\|Z_0(h)\|_\lambda\le e^{\lambda h/2}N$.
  To see this, for Schwartz free data differentiate its squared norm.
  The $-\Delta$ terms cancel, leaving
  $2\lambda^2\operatorname{Re}\langle A_\lambda^{-1}\dot w_0,w_0\rangle$,
  whose absolute value is at most $\lambda\|Z_0\|_\lambda^2$.
  Gronwall gives the stated bound. The required coefficient is exactly
  \[
    K_\epsilon=\E\|Z_1(h)\|_\lambda^2+
    2\operatorname{Re}\langle Z_0(h),\E Z_2(h)\rangle_\lambda.
  \]
  Substituting $\lambda=h^{-1}$ into the two estimates proves
  \eqref{E:phase-variance}. This proves
  Proposition~\ref{P:static-phase-variance}.
\end{proof}

The second term in $K_\epsilon$ must be retained; neither its sign nor
monotonicity of the full phase energy in covariance is assumed. The estimates
control both terms at this one variance order. They do not control higher
Gaussian contractions, products of independent time blocks, overlapping
noise levels or the temporal regularization limit. Thus they do not yet
establish Goal~\ref{G:upper}.

\section{All static orders with arbitrary initial phase}
\label{S:static-all-orders}

We now seek all static Duhamel orders, retaining the full spatial
covariance class of Section~\ref{S:static-phase}. The temporal
covariance is not included in this section.
Static estimates alone do not identify the evolution
for overlapping intervals; that step is treated in the next section.

We use one external operator theorem. From Crouzeix--Palencia
\cite{crouzeix.palencia:source2017:numerical}*{author preprint v1,
(3), p.~1, and Theorem~6, pp.~5--6}, if $T$ is a bounded operator on a
complex Hilbert space and $F$ is holomorphic on a neighborhood of
$\overline{W(T)}$, then
\begin{equation}\label{E:cp-input}
  \|F(T)\|\le(1+\sqrt2)\sup_{w\in W(T)}|F(w)|,\qquad
  W(T)=\{\langle Tu,u\rangle:\|u\|=1\}.
\end{equation}
The theorem is imported, not proved here. All operators to which we
apply it below are bounded; no unbounded-operator extension is assumed.

\begin{lemma}[A complex phase bound]\label{L:complex-phase}
  Let $H$ be a complex Hilbert space, $A_0$ a bounded nonnegative
  selfadjoint operator, and $B$ a bounded selfadjoint operator.
  Write $A_\rho=\rho^2+A_0$. Suppose that, for $0<a<1$ and $d>0$,
  \begin{equation}\label{E:abstract-sandwich}
    \|A_\rho^{-1/2}BA_\rho^{-1/2}\|\le d\rho^{a-2},
    \qquad \rho>0.
  \end{equation}
  Put
  \[
    I_a=\int_0^\infty s^{-1/2}(1+s)^{(a-3)/2}\ud s,\qquad
    \delta_a=\min\{1/4,\pi/(8I_a)\}.
  \]
  For $\lambda>0$ and $|z|\le\delta_a\lambda^{2-a}/d$, let
  $L=A_0-zB$. The phase propagator of $u''+Lu=0$ satisfies
  \begin{equation}\label{E:complex-phase-bound}
    \|\mathcal M_z(h)\|_{X_\lambda\to X_\lambda}
    \le100e^{2\lambda h},\qquad
    \|(f,g)\|_{X_\lambda}^2
    =\|f\|^2+\|A_\lambda^{-1/2}g\|^2,\quad h\ge0.
  \end{equation}
  The constant is independent of $H$, $\|A_0\|$ and $\|B\|$.
\end{lemma}

\begin{proof}
  Set $\delta=\delta_a$ and $L_\lambda=L+\lambda^2$.
  For $\kappa=(\lambda^2+t)^{1/2}$,
  \[
    L_\lambda+t
    =A_\kappa^{1/2}(1-zK_\kappa)A_\kappa^{1/2},\qquad
    K_\kappa=A_\kappa^{-1/2}BA_\kappa^{-1/2}.
  \]
  Since $a-2<0$, $\|zK_\kappa\|\le\delta$. Thus these operators are
  invertible and
  \[
    \|A_\kappa^{1/2}(L_\lambda+t)^{-1}\|
    \le\frac1{(1-\delta)\kappa}.
  \]
  Also $\operatorname{Re}\langle L_\lambda u,u\rangle
  \ge(1-\delta)\langle A_\lambda u,u\rangle$.

  Principal inverse square roots are defined on the right half-plane.
  The scalar identity
  $w^{-1/2}=\pi^{-1}\int_0^\infty t^{-1/2}(w+t)^{-1}\ud t$,
  and bounded holomorphic calculus, give
  \[
    Q_z-1
    =\frac1\pi\int_0^\infty t^{-1/2}A_\lambda^{1/2}
    \big[(L_\lambda+t)^{-1}-(A_\lambda+t)^{-1}\big]\ud t,
    \qquad Q_z=A_\lambda^{1/2}L_\lambda^{-1/2}.
  \]
  The integrals converge in operator norm. Indeed, the resolvent
  identity, $\|A_\lambda^{1/2}A_\kappa^{-1/2}\|\le1$, and the
  following ordered factorization give the required integrand bound:
  \[
    \begin{split}
      &A_\lambda^{1/2}
      \big[(L_\lambda+t)^{-1}-A_\kappa^{-1}\big]\\
      &\qquad=A_\lambda^{1/2}A_\kappa^{-1/2}
      (1-zK_\kappa)^{-1}zK_\kappa A_\kappa^{-1/2}.
    \end{split}
  \]
  The four factors have norms at most $1$, $(1-\delta)^{-1}$,
  $|z|d\kappa^{a-2}$ and $\kappa^{-1}$, respectively.
  Thus, the integrand without $t^{-1/2}/\pi$ is bounded by
  \[
    \frac{|z|d}{1-\delta}\kappa^{a-3}.
  \]
  Consequently,
  \[
    \|Q_z-1\|
    \le\frac{|z|d\lambda^{a-2}I_a}{\pi(1-\delta)}
    \le\frac16.
  \]
  In particular, $Q_z$ and $Q_z^{-1}$ have norm at most two.
  Apply the same argument to $L^*=A_0-\overline zB$ and take adjoints.
  It follows that all four operators
  \begin{equation}\label{E:phase-root-comparisons}
    A_\lambda^{1/2}L_\lambda^{-1/2},\quad
    L_\lambda^{-1/2}A_\lambda^{1/2},\quad
    L_\lambda^{1/2}A_\lambda^{-1/2},\quad
    A_\lambda^{-1/2}L_\lambda^{1/2}
  \end{equation}
  have norm at most two. This is a quantitative comparison at the
  bounded cutoffs, not an assumed square-root domain identity.

  We next control the numerical range. For $\|u\|=1$ put
  $s=\|A_0^{1/2}u\|$. Optimizing~\eqref{E:abstract-sandwich} at
  $\rho=s$ gives $|\langle Bu,u\rangle|\le2ds^a$.
  If $s=0$, the same conclusion follows by letting $\rho\downarrow0$.
  Separately, evaluating~\eqref{E:abstract-sandwich} at $\rho=\lambda$
  gives
  \[
    |\langle Bu,u\rangle|
    \le d\lambda^{a-2}(s^2+\lambda^2),\qquad
    |z\langle Bu,u\rangle|\le\delta(s^2+\lambda^2).
  \]
  This is the estimate for the real part; the optimized estimate controls
  the imaginary part. Thus, for $w=x+iy=\langle Lu,u\rangle$,
  \[
    x+\lambda^2\ge(1-\delta)(s^2+\lambda^2),\qquad
    |y|\le2\delta\lambda^{2-a}s^a.
  \]
  Since $s^{2a}\lambda^{2-2a}\le s^2+\lambda^2$,
  \[
    y^2\le\frac{4\delta^2}{1-\delta}\lambda^2(x+\lambda^2)
    \le\frac13\lambda^2(x+\lambda^2),\qquad
    x\ge-\lambda^2/4.
  \]
  Hence $|w|\le x+2\lambda^2$, and either square root of $w$ has
  $|\operatorname{Im}\sqrt w|\le\lambda$.

  The scalar functions
  \[
    C_h(w)=\cos(h\sqrt w),\qquad
    F_h(w)=\sqrt{w+\lambda^2}\frac{\sin(h\sqrt w)}{\sqrt w},\qquad
    H_h(w)=\frac{w}{\sqrt{w+\lambda^2}}
    \frac{\sin(h\sqrt w)}{\sqrt w}
  \]
  are holomorphic on a neighborhood of $\overline{W(L)}$.
  The values at $w=0$ are removable; the only square-root branch
  required is that of $w+\lambda^2$, whose real part is positive.
  On the numerical range,
  \[
    |C_h(w)|\le e^{\lambda h},\qquad
    |F_h(w)|\le2(1+\lambda h)e^{\lambda h},\qquad
    |H_h(w)|\le2e^{\lambda h}.
  \]
  Indeed, $|\operatorname{Im}\sqrt w|\le\lambda$ gives
  $|\cos(h\sqrt w)|,|\sin(h\sqrt w)|\le e^{\lambda h}$.
  The entire identity
  $\sin(h\sqrt w)/\sqrt w=\int_0^h\cos(r\sqrt w)\ud r$
  also gives the bound $he^{\lambda h}$, including $w=0$.
  If $|w|\le\lambda^2/2$, then
  \[
    |F_h(w)|\le\sqrt{3/2}\,\lambda h e^{\lambda h}.
  \]
  If $|w|>\lambda^2/2$, then
  $|w+\lambda^2|/|w|\le3$, so
  $|F_h(w)|\le\sqrt3 e^{\lambda h}$.
  These bounds imply the displayed estimate for $F_h$.
  Finally,
  \[
    \frac{|w|}{|w+\lambda^2|}
    \le1+\frac{\lambda^2}{|w+\lambda^2|}
    \le1+(1-\delta)^{-1}\le7/3,
  \]
  and $H_h(w)=\sqrt w\sin(h\sqrt w)/\sqrt{w+\lambda^2}$ gives
  its stated bound. All identities have their removable values at zero.
  Applying the imported~\eqref{E:cp-input} gives bounds
  $3e^{\lambda h}$, $6(1+\lambda h)e^{\lambda h}$ and
  $6e^{\lambda h}$ for these three operator functions.

  Under the isometry $(u,v)\mapsto(u,A_\lambda^{-1/2}v)$,
  the four phase blocks are
  \[
    C_h(L),\quad
    F_h(L)L_\lambda^{-1/2}A_\lambda^{1/2},\quad
    -A_\lambda^{-1/2}L_\lambda^{1/2}H_h(L),\quad
    A_\lambda^{-1/2}L_\lambda^{1/2}C_h(L)
    L_\lambda^{-1/2}A_\lambda^{1/2}.
  \]
  This is the usual matrix
  $\left(\begin{smallmatrix}C_h(L)&G_h(L)\\-LG_h(L)&C_h(L)\end{smallmatrix}\right)$,
  with $G_h(w)=\sin(h\sqrt w)/\sqrt w$, after weighting.
  In the order displayed, the four block norms are at most
  \[
    3e^{\lambda h},\qquad
    12(1+\lambda h)e^{\lambda h},\qquad
    12e^{\lambda h},\qquad12e^{\lambda h}.
  \]
  For example, the last block has two root-comparison factors of norm
  at most two, with $C_h(L)$ between them. Only functions of $L$ commute;
  no commutation with $A_\lambda$ is used in these ordered products.
  A block operator on $H\oplus H$ has norm at most the sum of its four
  block norms, by the triangle inequality and the norm-one coordinate
  inclusions and projections. Therefore, its norm is at most
  \[
    (39+12\lambda h)e^{\lambda h}
    \le39(1+\lambda h)e^{\lambda h}\le100e^{2\lambda h}.
  \]
  The phase operator itself is the exponential of the bounded block
  generator with rows $(0,1)$ and $(-L,0)$. It is entire in $z$;
  the intermediate square roots are used to estimate it, not to impose
  a branch-dependent definition of that entire operator.
  This proves Lemma~\ref{L:complex-phase}.
\end{proof}

\begin{lemma}[Gaussian cutoff form bound]\label{L:fock-form}
  Retain the covariance and $R_\alpha$ of
  Section~\ref{S:static-phase}. Fix $\epsilon>0$.
  Represent the smoothed real field on independent standard Gaussian
  coordinates as $W_\epsilon(x)=\sum_{i\ge1}g_i e_i(x)$ in $L^2(\Omega)$.
  Let $P_N$ be projection onto Gaussian Hermite degrees at most $N$,
  and $S_b$ spatial Fourier projection onto $|\eta|\le b$.
  For finite $m$, on their joint range set
  \[
    B_{N,m,b}=P_NS_b\Big(\sum_{i=1}^m g_i M_{e_i}\Big)S_bP_N,\qquad
    A_\rho=\rho^2-\Delta .
  \]
  These are bounded selfadjoint operators and, uniformly in
  $\epsilon,m,b$,
  \begin{equation}\label{E:fock-sandwich}
    \|A_\rho^{-1/2}B_{N,m,b}A_\rho^{-1/2}\|
    \le d_N\rho^{\alpha/2-2},\qquad
    d_N=2\sqrt{N+1}\sqrt{R_\alpha}.
  \end{equation}
\end{lemma}

\begin{proof}
  Choose an orthonormal basis of the real isonormal space, which is
  separable, and write $e_i(x)=\E[W_\epsilon(x)g_i]$.
  Then $\sum_i e_i(x)^2=\Gamma_\epsilon(0)=:v_\epsilon$, and
  $|e_i(x)|\le\sqrt{v_\epsilon}$. Thus each multiplication $M_{e_i}$
  is bounded and selfadjoint. Put
  $H_i=A_\rho^{-1/2}M_{e_i}A_\rho^{-1/2}$ on spatial $L^2$.
  Gaussian isometry and spatial Plancherel give
  \[
    \sum_i\|H_i f\|_2^2
    =\frac1{(2\pi)^3}\int
    \frac{|\widehat f(\eta)|^2}{\rho^2+|\eta|^2}
    J_{\rho,\epsilon}(\eta)\ud\eta,\qquad
    J_{\rho,\epsilon}(\eta)
    =\int\frac{e^{-\epsilon|\xi|^2}\mu(\ud\xi)}
    {\rho^2+|\eta+\xi|^2}.
  \]
  This is the covariance calculation for
  $A_\rho^{-1/2}W_\epsilon A_\rho^{-1/2}f$.
  By Lemma~\ref{L:phase-contractions},
  $J_{\rho,\epsilon}\le R_\alpha\rho^{\alpha-2}$.
  Therefore
  $\sum_i H_i^2\le R_\alpha\rho^{\alpha-4}I$
  in quadratic forms. Finite sums have the same upper bound.
  Compression to $S_b$ preserves it: for selfadjoint $H_i$,
  $(S_bH_iS_b)^2\le S_bH_i^2S_b$ on its range.
  Both row and column variances are the same, since these
  operators are selfadjoint.

  For completeness, use normalized Hermite polynomials, so multiplication
  by $g_i$ is $a_i^*+a_i$, with
  $g_i h_k=\sqrt{k_i+1}\,h_{k+e_i}+\sqrt{k_i}\,h_{k-e_i}$.
  On degree $k$, the row map $(v_i)\mapsto\sum_i a_i^*v_i$
  has norm $\sqrt{k+1}$: its product with its adjoint is
  $\sum_i a_i^*a_i=(k+1)I$ on degree $k+1$.
  Composing with the column of spatial operators $S_bH_iS_b$ bounds
  the creation part by
  $\sqrt{k+1}\sqrt{R_\alpha}\rho^{(\alpha-4)/2}$.
  Distinct input degrees have orthogonal output degrees.
  The annihilation part is its adjoint, with the same bound after
  truncation. Adding them on degrees at most $N$ proves
  \eqref{E:fock-sandwich}. Boundedness of $-\Delta$ on $S_b$ is explicit;
  no infinite-frequency operator theorem was used.
  This proves Lemma~\ref{L:fock-form}.
\end{proof}

\begin{lemma}[Exact cutoffs for finite Gaussian words]\label{L:finite-word-cutoff}
  Let $g_{ij}$, $1\le i\le M$, $1\le j\le m_i$, be independent
  standard real Gaussian coordinates, grouped by color $i$, and let
  $\mathscr X$ be a complex Hilbert space. On Gaussian polynomials
  with coefficients in $\mathscr X$ set
  \[
    J_i=\sum_{j=1}^{m_i}M_{g_{ij}}\otimes K_{ij},
  \]
  where each $K_{ij}$ is bounded on $\mathscr X$. Let
  $F_0,\ldots,F_n$ be bounded operators acting only on $\mathscr X$.
  Fix a word $i_1,\ldots,i_n$, and let $r_i$ be the number of its
  occurrences of color $i$. If $N_i\ge r_i$ and $P$ projects each
  color onto total Hermite degree at most $N_i$, then, for every
  $v\in\mathscr X$,
  \begin{equation}\label{E:finite-word-cutoff}
    \begin{split}
      &(I\otimes F_n)(PJ_{i_n}P)(I\otimes F_{n-1})\cdots
      (PJ_{i_1}P)(I\otimes F_0)(1\otimes v)\\
      &\qquad=(I\otimes F_n)J_{i_n}(I\otimes F_{n-1})\cdots
      J_{i_1}(I\otimes F_0)(1\otimes v).
    \end{split}
  \end{equation}
  The equality holds for finite sums and for Bochner integrals of such
  words whenever the displayed vector integrals exist.
\end{lemma}

\begin{proof}
  In normalized Hermite coordinates, multiplication by $g_{ij}$ maps
  $h_{\boldsymbol a}$ to
  $\sqrt{a_{ij}+1}\,h_{\boldsymbol a+e_{ij}}
  +\sqrt{a_{ij}}\,h_{\boldsymbol a-e_{ij}}$; the second term is zero
  if $a_{ij}=0$. Thus it changes the total degree of color $i$ by
  one and leaves all other color degrees unchanged. The operators
  $I\otimes F_l$ leave every Gaussian degree unchanged.
  After the first $l$ insertions, the uncompressed word therefore
  has color-$i$ degree at most
  $r_i(l)=|\{j\le l:i_j=i\}|\le r_i\le N_i$.
  This is an induction starting from degree zero in every color.
  Consequently $P$ is the identity both before and after every
  insertion along that word. Induction on $l$ now proves
  \eqref{E:finite-word-cutoff}. The lowering term has been retained:
  the assertion includes creation followed by annihilation and all
  resulting self-contractions. Linearity and equality of the vector
  integrands prove the last assertion. This is an equality of selected
  finite words, not of full propagators at a fixed cutoff.
  This proves Lemma~\ref{L:finite-word-cutoff}.
\end{proof}

\begin{proposition}[All regularized static phase orders]
  \label{P:static-phase-all-orders}
  Retain the full covariance class of Section~\ref{S:static-phase}.
  For real Schwartz $f,g$, let $Z_n^\epsilon(h)$ be the $n$th
  regularized static Duhamel phase, with the recursion
  \eqref{E:phase-duhamel} for every $n\ge0$. This is an ordinary
  Gaussian polynomial of degree at most $n$, including self-contractions;
  it is not a pure Wick chaos.
  There is an explicit finite constant
  \[
    A_\alpha=\frac{400\sqrt2\,e^2}{\delta_{\alpha/2}}
  \]
  such that, for $n\ge1$, uniformly in $\epsilon>0$,
  \begin{equation}\label{E:all-static-phase-orders}
    \|Z_n^\epsilon(h)\|_{L^2(\Omega;X_{1/h})}
    \le
    \frac{(A_\alpha\sqrt{R_\alpha})^n
    h^{(4-\alpha)n/2}}{(n!)^{(3-\alpha)/2}}
    \|(f,g)\|_{1/h}.
  \end{equation}
  At every fixed positive smoothing and real coupling $\sigma$,
  $\sum_{n\ge0}\sigma^nZ_n^\epsilon(h)$ converges in $L^2$ phase.
  Its squared norm is at most
  \begin{equation}\label{E:all-static-phase-sum}
    (\sqrt e+2)^2
    \exp\left\{6A_\alpha^{2/(3-\alpha)}
    (|\sigma|^2R_\alpha)^{1/(3-\alpha)}
    h^{(4-\alpha)/(3-\alpha)}\right\}\|(f,g)\|_{1/h}^2.
  \end{equation}
\end{proposition}

\begin{proof}
  If $R_\alpha=0$, spectral homogeneity gives $\mu=0$, and every
  positive-order term is zero. Assume $R_\alpha>0$.
  First work at finite Gaussian cutoff $m$, degree cutoff $N$ and
  spatial band $b$, with initial phase $S_b(f,g)$ times the Gaussian
  vacuum $1$. All relevant operators are bounded.
  Lemmas~\ref{L:fock-form} and \ref{L:complex-phase}, with $a=\alpha/2$,
  give a bound $100e^{2\lambda h}$ on the complex coupling circle
  of radius $\delta_{\alpha/2}\lambda^{2-\alpha/2}/d_N$.

  The four phase entries are entire in the coupling, by the power series
  for $\cos(h\sqrt L)$ and $\sin(h\sqrt L)/\sqrt L$ of a bounded $L$.
  Cauchy's formula for their operator-valued series bounds the $n$th
  coefficient by
  \[
    100e^{2\lambda h}
    \left(\frac{d_N}
    {\delta_{\alpha/2}\lambda^{2-\alpha/2}}\right)^n
    \|S_b(f,g)\|_\lambda .
  \]
  The coefficient is exactly the $n$th Duhamel phase from the vacuum.
  Apply Lemma~\ref{L:finite-word-cutoff} with one color, $N=n$,
  the spatial phase Hilbert space as $\mathscr X$, and its free wave
  operators as the $F_l$. It identifies each cutoff Duhamel word
  exactly with its uncompressed word, including self-contractions.
  Dominated time integration preserves this identity.

  Choose $\lambda=n/h$. For any phase $z$,
  $\|z\|_{1/h}\le n\|z\|_{n/h}$ and
  $\|(f,g)\|_{n/h}\le\|(f,g)\|_{1/h}$.
  Also $d_n\le2\sqrt{2n}\sqrt{R_\alpha}$.
  The preceding bound is therefore at most
  \[
    100n\left(\frac{2\sqrt2 e^2}{\delta_{\alpha/2}}\right)^n
    R_\alpha^{n/2}h^{(4-\alpha)n/2}
    n^{-(3-\alpha)n/2}\|(f,g)\|_{1/h}.
  \]
  Since $100n\le200^n$ and $n!\le n^n$, this gives
  \eqref{E:all-static-phase-orders} at the cutoffs.

  We justify removal of those cutoffs at fixed $\epsilon$ and $n$.
  On Gaussian degrees at most $N$, the unweighted field multiplication
  has norm at most $2\sqrt{N+1}\sqrt{v_\epsilon}$, uniformly in $m$,
  by the same creation/annihilation argument applied pointwise in $x$.
  It follows that the noise phase insertion
  $(u,v)\mapsto(0,W_\epsilon u)$, between the required finite degree
  levels, is bounded on $X_\lambda$ by this constant divided by
  $\lambda$. Free phase evolution is bounded by $e^{\lambda h/2}$.
  For finite $m$, $S_b\to I$ strongly and commutes with the free
  propagator. Each fixed Duhamel word therefore converges strongly
  as $b\to\infty$, by dominated time integration.

  Next let $m\to\infty$ on the full Gaussian space.
  The truncated field multiplications converge strongly between
  finite degree levels. To see this, first take a vector depending on
  finitely many Gaussian coordinates. The annihilation tail is then
  zero, while the creation tail is bounded by a constant times
  \[
    \left(\int\sum_{i>m}e_i(x)^2\|F(x)\|^2\ud x\right)^{1/2},
  \]
  which tends to zero by dominated convergence, since the sum is
  bounded by $v_\epsilon$. Such vectors are dense; the uniform
  multiplication bound extends strong convergence to all vectors
  in those degree levels. Dominated time integration again gives
  convergence of every fixed word. The limit is precisely
  $Z_n^\epsilon$, so the estimate survives both limits.
  We assert no zero-smoothing phase limit in this argument.

  Finally, put $\beta=(3-\alpha)/2\in(1/2,3/2)$ and
  $x=A_\alpha|\sigma|\sqrt{R_\alpha}h^{(4-\alpha)/2}$.
  The elementary series satisfies
  \[
    \sum_{n\ge0}\frac{x^n}{(n!)^\beta}
    \le2e^{3x^{1/\beta}}.
  \]
  For $\beta\ge1$, this follows from
  $\sum a_n^\beta\le(\sum a_n)^\beta$ with
  $a_n=x^{n/\beta}/n!$.
  For $\beta<1$, apply H\"older to
  $((2x^{1/\beta})^n/n!)^\beta
  (2^{-\beta n/(1-\beta)})^{1-\beta}$.
  The second geometric sum is at most two.
  Since $\|Z_0(h)\|_{1/h}\le\sqrt e\|(f,g)\|_{1/h}$,
  absolute $L^2$ summation and squaring give
  \eqref{E:all-static-phase-sum}.
  This proves Proposition~\ref{P:static-phase-all-orders}.
\end{proof}

\begin{corollary}[Summable static interaction bounds]
  \label{C:static-interaction}
  Let $\mathcal S_0(t)$ be free phase evolution and, for $\lambda h\le1$,
  define the static interaction map by its convergent series
  \[
    \mathcal I^\epsilon_\sigma(h)(f,g)
    =\mathcal S_0(-h)\sum_{n\ge0}\sigma^n Z_n^\epsilon(h).
  \]
  Put $\gamma=3-\alpha$, $B_\alpha=3eA_\alpha^2$ and
  \[
    \begin{split}
      L_\alpha(h,\lambda)
      &=4eR_\alpha h^2\lambda^{\alpha-2}
      +\frac{4\sqrt eD_\Gamma}{(2-\alpha)(3-\alpha)}
      \frac{h^{3-\alpha}}{\lambda},\\
      x&=B_\alpha\sigma^2R_\alpha h^{4-\alpha},\\
      \mathcal E(h,\sigma,\lambda)
      &=\sigma^2L_\alpha(h,\lambda)
      +(\lambda h)^{-2}x^2e^{\gamma x^{1/\gamma}}.
    \end{split}
  \]
  Uniformly in $\epsilon>0$,
  \begin{equation}\label{E:static-interaction}
    \E\|\mathcal I^\epsilon_\sigma(h)(f,g)\|_\lambda^2
    \le[1+\mathcal E(h,\sigma,\lambda)]\|(f,g)\|_\lambda^2.
  \end{equation}
  If $0<\alpha_0<1$ and $\alpha+\alpha_0<2$, then, for
  $h_j=2^{-j}/\lambda$, $\sigma_j^2=h_j^{-\alpha_0}$ and $T>0$,
  \begin{equation}\label{E:static-block-series}
    \sum_{j\ge0}\frac{T}{h_j}\mathcal E(h_j,\sigma_j,\lambda)<\infty.
  \end{equation}
  For a finite single partition, let $\mathcal M_j(h_j)$ be the static
  phase maps with mutually independent copies of the smoothed field,
  real couplings $\sigma_j$, and $\lambda h_j\le1$. They have continuous
  $L^2$ extensions to independent random initial phases. Then
  \begin{equation}\label{E:independent-static-blocks}
    \E\|\mathcal M_K(h_K)\cdots\mathcal M_1(h_1)(f,g)\|_\lambda^2
    \le
    \exp\left\{\lambda\sum_{j=1}^K h_j+
    \sum_{j=1}^K\mathcal E(h_j,\sigma_j,\lambda)\right\}
    \|(f,g)\|_\lambda^2.
  \end{equation}
  This concerns independent successive blocks on one partition.
  Formula~\eqref{E:static-block-series} only sums individual upper
  bounds across dyadic levels; it does not identify a product with
  an evolution driven by overlapping or repeated fields.
\end{corollary}

\begin{proof}
  Write $N=\|(f,g)\|_\lambda$ and
  $Y_n=\mathcal S_0(-h)Z_n^\epsilon(h)$.
  The free estimate from Section~\ref{S:static-phase} holds for both
  time directions, since its differentiated energy was bounded in
  absolute value. Thus $\|\mathcal S_0(-h)\|_\lambda\le\sqrt e$.
  Since $Y_0=(f,g)$, Proposition~\ref{P:static-phase-variance}
  bounds the complete first variance coefficient of
  $\E\|\sum\sigma^nY_n\|_\lambda^2$ in absolute value by
  $L_\alpha(h,\lambda)N^2$.
  In detail, its first random squared norm is bounded by
  $e$ times~\eqref{E:phase-born}, and its second-order mean
  cross term by $2N\sqrt e$ times~\eqref{E:phase-mean}.

  For $n\ge1$, the norm comparisons when $\lambda h\le1$ and
  \eqref{E:all-static-phase-orders} give
  \[
    \|Y_n\|_{L^2(\Omega;X_\lambda)}
    \le\frac{\sqrt e}{\lambda h}
    \frac{(A_\alpha\sqrt{R_\alpha})^n h^{(4-\alpha)n/2}}
    {(n!)^{\gamma/2}}N.
  \]
  Gaussian symmetry makes
  $\E\langle Y_r,Y_s\rangle_\lambda=0$ if $r+s$ is odd.
  All double series below converge absolutely by these bounds.
  For $r+s=2k$, the elementary factorial inequality
  $r!s!\ge(k!)^2$ shows that the sum of absolute inner products
  is at most
  \[
    \frac{e(2k+1)}{(\lambda h)^2}
    \frac{(A_\alpha^2R_\alpha)^k h^{(4-\alpha)k}}
    {(k!)^\gamma}N^2,\qquad k\ge1.
  \]
  This includes $r=0$ or $s=0$, since $\lambda h\le1$ and
  $\|Y_0\|=N$. The bound $e(2k+1)\le(3e)^k$ therefore controls
  all orders $k\ge2$ by
  \[
    \frac1{(\lambda h)^2}
    \sum_{k\ge2}\frac{x^k}{(k!)^\gamma}N^2
    \le\frac{x^2e^{\gamma x^{1/\gamma}}}{(\lambda h)^2}N^2.
  \]
  Here $\gamma>1$, and
  $\sum_{j\ge0}x^j/(j!)^\gamma\le e^{\gamma x^{1/\gamma}}$.
  Keeping the sharper first coefficient separately proves
  \eqref{E:static-interaction}.

  Finally, set $\beta=4-\alpha-\alpha_0>2$.
  After multiplication by $T/h_j$, the two first-coefficient
  terms in~\eqref{E:static-block-series} are constant multiples of
  \[
    T\lambda^{\alpha-2}h_j^{1-\alpha_0},\qquad
    \frac T\lambda h_j^{2-\alpha-\alpha_0}.
  \]
  The higher-order term is
  \[
    \frac{T(B_\alpha R_\alpha)^2}{\lambda^2}
    h_j^{2\beta-3}
    \exp\{\gamma(B_\alpha R_\alpha)^{1/\gamma}h_j^{\beta/\gamma}\}.
  \]
  The exponential factor is bounded by its value at $h_0$.
  All three powers are positive, so their geometric series converge.
  For the finite partition, write
  $\mathcal M_j(h_j)=\mathcal S_0(h_j)\mathcal I_j(h_j)$.
  Bound~\eqref{E:static-interaction} and
  $\|\mathcal S_0(h_j)\|_\lambda^2\le e^{\lambda h_j}$
  give a bounded linear map from deterministic $X_\lambda$ to
  $L^2(\Omega_j;X_\lambda)$, initially on Schwartz phases and then
  by density. Tensoring with the past probability space extends this
  bound to random initial phases independent of the $j$th field.
  Iteration gives the product of
  $e^{\lambda h_j}(1+\mathcal E(h_j,\sigma_j,\lambda))$.
  The inequality $1+y\le e^y$ for $y\ge0$ proves
  \eqref{E:independent-static-blocks}.
  This proves Corollary~\ref{C:static-interaction}.
\end{proof}

These estimates concern individual static phase and interaction maps.
Their summability alone does not identify the evolution driven by
overlapping interval fields. The coefficient argument in
Section~\ref{S:interval-upper} supplies the separate estimate needed
for that evolution.

\section{Interval fields and the full upper bound}
\label{S:interval-upper}

The intrinsic constant is identified independently in
Theorem~\ref{T:intrinsic-second-moment}.

Write
\[
  \nu=3-\alpha>1,\qquad
  \beta=4-\alpha-\alpha_0>2,\qquad p=2-\alpha_0>1.
\]
Thus, $\beta-\nu=1-\alpha_0>0$.
In this section the spatial dimension is any admissible $d\in\{1,2,3\}$.
The spatial covariance is the nonnegative, even, positive-definite tempered
Radon measure $\Gamma$, with scaling
$\Gamma(rA)=r^{d-\alpha}\Gamma(A)$ and spectral convention
$\Gamma=\int e^{i\xi\cdot x}\mu(\ud\xi)$.
This includes $\Gamma=\delta_0$ when $d=\alpha=1$.
Set
\[
  R_\alpha=\frac{\alpha\pi\mu(B_1)}{2\sin(\pi\alpha/2)},\qquad
  A_\rho=\rho^2-\Delta,\qquad
  \|(f,g)\|_\rho^2=\|f\|_2^2+\|A_\rho^{-1/2}g\|_2^2.
\]
Complex Hilbert inner products are linear in the first slot.

\begin{lemma}[Dimension-independent Gaussian contractions]
  \label{L:interval-contractions}
  Uniformly in positive spatial smoothing and in finite Gaussian-mode
  and spatial Fourier-band cutoffs,
  \begin{equation}\label{E:interval-column}
    \sum_m\|A_\rho^{-1/2}M_{e_m}f\|_2^2
    \le R_\alpha\rho^{\alpha-2}\|f\|_2^2.
  \end{equation}
  Here $W_\epsilon(x)=\sum_m g_me_m(x)$ is an orthonormal-coordinate
  representation of $W(p_\epsilon(x-\cdot))$, whose covariance is
  $\Gamma_\epsilon=p_{2\epsilon}*\Gamma$.
  Consequently, on a Gaussian color that is initially in its vacuum,
  the phase insertion $(u,v)\mapsto(0,W_\epsilon u)$ has norm at most
  $\sqrt{R_\alpha}\rho^{(\alpha-2)/2}$ into its Gaussian $L^2$ phase.
  With Hermite degree of this color truncated at $N$, its sandwiched
  field has operator norm at most
  \begin{equation}\label{E:interval-fock}
    2\sqrt{N+1}\sqrt{R_\alpha}\rho^{\alpha/2-2}.
  \end{equation}
  Both statements remain valid tensoring with any other Hilbert factor.
\end{lemma}

\begin{proof}
  Fourier uniqueness gives $\mu(B_r)=r^\alpha\mu(B_1)$.
  The Gaussian comparison in Lemma~\ref{L:phase-contractions} uses no
  dimension-specific identity:
  \[
    \int e^{-s|\eta+\xi|^2}\mu(\ud\xi)
    =\int p_{2s}^{(d)}(x)e^{i\eta\cdot x}\Gamma(\ud x)
    \le\int e^{-s|\xi|^2}\mu(\ud\xi).
  \]
  Evenness gives a real integral, and physical nonnegativity gives
  the inequality. Integrating against $e^{-\rho^2s}\ud s$ and using
  radial spectral homogeneity yields
  \[
    \sup_\eta\int\frac{\mu(\ud\xi)}{\rho^2+|\eta+\xi|^2}
    \le R_\alpha\rho^{\alpha-2}.
  \]
  No exclusion of a physical origin atom is used.

  Gaussian isometry and unnormalized spatial Plancherel give
  \[
    \sum_m\|A_\rho^{-1/2}M_{e_m}f\|_2^2
    =\frac1{(2\pi)^d}\int|\widehat f(\eta)|^2
    \left(\int\frac{e^{-\epsilon|\xi|^2}\mu(\ud\xi)}
    {\rho^2+|\eta+\xi|^2}\right)\ud\eta .
  \]
  This proves~\eqref{E:interval-column}. A finite mode sum is a
  positive sub-sum. For a Fourier-band projection $S_b$, which commutes
  with $A_\rho$, use $S_bA_\rho^{-1}S_b\le A_\rho^{-1}$ to obtain
  the same inequality for $S_bM_{e_m}S_b$.
  The phase assertion on a new color follows because
  $\sum_mg_m(0,M_{e_m}u)$ has squared norm given by the left side
  of~\eqref{E:interval-column}, and its input is independent of this color.

  Substituting $A_\rho^{-1/2}f$ gives
  \[
    \sum_m(A_\rho^{-1/2}M_{e_m}A_\rho^{-1/2})^2
    \le R_\alpha\rho^{\alpha-4}I.
  \]
  These spatial sandwiches are selfadjoint, so their row and column
  variances agree. The normalized Hermite creation-row norm from
  degree $j$ to degree $j+1$ is $\sqrt{j+1}$, and annihilation is
  its adjoint, as proved in Lemma~\ref{L:fock-form}.
  Composition with the spatial column and addition of the two
  parts prove~\eqref{E:interval-fock}. The same positive operator
  identities hold with an identity on every other Hilbert factor.
  The calculation used only the radial mass $\mu(B_1)$, homogeneity
  and physical nonnegativity. Thus, $R_\alpha$ is the only covariance
  quantity in these estimates. No angular bound or unsmoothed
  multiplication norm has been absorbed into a constant.
  This proves Lemma~\ref{L:interval-contractions}.
\end{proof}

\begin{lemma}[Complex sums and changing phase weights]
  \label{L:interval-complex}
  Let $A_0$ be bounded, nonnegative and selfadjoint, and let $V$ be bounded
  on the same complex Hilbert space. Write $A_\rho=\rho^2+A_0$.
  The complex phase conclusion of Lemma~\ref{L:complex-phase} holds
  for $L=A_0-V$ whenever $V$ is bounded, not necessarily selfadjoint,
  \[
    \|A_\rho^{-1/2}VA_\rho^{-1/2}\|\le D\rho^{a-2},\qquad \rho>0,
    \quad 0<a<1,\quad D\le\delta_a\Lambda^{2-a}.
  \]
  Its bound is $100e^{2\Lambda h}$ in $X_\Lambda$.
  If a piecewise-constant potential is the sum of connected-interval
  fields, assign a positive weight $\omega_i$ to each field present
  and put $\Lambda(t)=\lambda+\sum_i\omega_i\mathbf1_{I_i}(t)$.
  The total loss from changing between these phase norms, starting
  and ending in $X_\lambda$, is at most
  \begin{equation}\label{E:interval-metric}
    \prod_i(1+\omega_i/\lambda).
  \end{equation}
\end{lemma}

\begin{proof}
  The adjoint has the identical sandwich bound, since
  \[
    A_\rho^{-1/2}V^*A_\rho^{-1/2}
    =(A_\rho^{-1/2}VA_\rho^{-1/2})^*.
  \]
  The form estimate at $\rho=\Lambda$ gives
  $\operatorname{Re}\langle(L+\Lambda^2)u,u\rangle
  \ge(1-\delta_a)\langle A_\Lambda u,u\rangle$.
  The shifted operator and its adjoint thus have spectra in the right
  half-plane, where their principal inverse roots are defined.
  Put $K_\kappa=A_\kappa^{-1/2}VA_\kappa^{-1/2}$ and
  $\kappa=(\Lambda^2+t)^{1/2}$. The resolvent difference is exactly
  \[
    (L+\Lambda^2+t)^{-1}-A_\kappa^{-1}
    =A_\kappa^{-1/2}(1-K_\kappa)^{-1}K_\kappa A_\kappa^{-1/2}.
  \]
  Its product on the left with $A_\Lambda^{1/2}$ has norm at most
  $D\kappa^{a-3}/(1-\delta_a)$. The inverse-root integral in
  Lemma~\ref{L:complex-phase} therefore gives the same $1/6$ bound.
  More explicitly, put $L_\Lambda=L+\Lambda^2$ and
  $Q=A_\Lambda^{1/2}L_\Lambda^{-1/2}$. Then
  $\|Q-I\|\le1/6$, so $\|Q\|\le7/6$ and
  $\|Q^{-1}\|\le6/5$ by its Neumann series.
  Taking adjoints under the norm-convergent resolvent integral gives
  $(L_\Lambda^{-1/2})^*=(L_\Lambda^*)^{-1/2}$.
  Apply the same estimate to $L^*=A_0-V^*$ and take adjoints.
  This bounds $L_\Lambda^{-1/2}A_\Lambda^{1/2}$ by $7/6$ and its
  inverse $A_\Lambda^{-1/2}L_\Lambda^{1/2}$ by $6/5$.
  Together with $Q$ and $Q^{-1}=L_\Lambda^{1/2}A_\Lambda^{-1/2}$,
  these are all four ordered comparisons in
  \eqref{E:phase-root-comparisons}, each at most two.

  For a unit vector $u$ put $s=\|A_0^{1/2}u\|$ and
  $\langle Lu,u\rangle=x+iy$. The form estimate at $\rho=\Lambda$
  and, separately, at $\rho=s$ gives
  \[
    |\langle Vu,u\rangle|\le D\Lambda^{a-2}(s^2+\Lambda^2),
    \qquad |\langle Vu,u\rangle|\le2Ds^a.
  \]
  At $s=0$ the second bound follows by $\rho\downarrow0$.
  Thus $x+\Lambda^2\ge(1-\delta_a)(s^2+\Lambda^2)$ and
  $|y|\le2\delta_a\Lambda^{2-a}s^a$. These are the two inequalities
  used for the numerical-range parabola in Lemma~\ref{L:complex-phase}.
  Its scalar bounds and the bounded-operator Crouzeix--Palencia theorem
  apply to $L$ without selfadjointness. The four weighted block formulas
  there use only functions of $L$ and the root comparisons just proved.
  Their norms are at most $3e^{\Lambda h}$,
  $12(1+\Lambda h)e^{\Lambda h}$, $12e^{\Lambda h}$ and
  $12e^{\Lambda h}$. Their sum is at most $100e^{2\Lambda h}$.
  This uses neither selfadjointness of $V$ nor commutation of
  $A_\Lambda$ with $L$.

  For a common phase vector,
  \[
    \|z\|_{\rho_{\rm new}}
    \le\max\{1,\rho_{\rm old}/\rho_{\rm new}\}\|z\|_{\rho_{\rm old}}.
  \]
  At a jump, write $E$ for ending fields, $S$ for starting fields,
  and $R$ for those remaining. The ratio is at most
  \[
    \frac{\lambda+\sum_R\omega_i+\sum_E\omega_i}
    {\lambda+\sum_R\omega_i+\sum_S\omega_i}
    \le1+\sum_E\omega_i/\lambda
    \le\prod_E(1+\omega_i/\lambda).
  \]
  An initial increase of the weight has no loss. Count a final return
  to $X_\lambda$ as an ending jump at $T$.
  Each connected interval ends once, giving~\eqref{E:interval-metric}.
  This proves Lemma~\ref{L:interval-complex}.
\end{proof}

\begin{lemma}[A positive inventory product]\label{L:inventory-product}
  For $k\ge1$, define
  \[
    v_i=i^{-\beta}+k^{-1}i^{-(\beta-1)}
    +k^{\alpha-2}i^{-p},\qquad
    b_{i,l}=\frac{i^{-\beta l}(1+li/k)^2}{(l!)^\nu},\quad l\ge2.
  \]
  There is a finite $C=C(\alpha,\alpha_0)$, independent of $M,k$, such that
  \begin{equation}\label{E:inventory-product}
    [z^k]\prod_{i=1}^M\left(1+v_i z+\sum_{l\ge2}b_{i,l}z^l\right)
    \le\frac{C^k}{(k!)^\nu}.
  \end{equation}
\end{lemma}

\begin{proof}
  Evaluate the positive product at $z=\theta k^\nu$, with $\theta=1/4$.
  Put $P_i=\theta k^\nu i^{-\beta}$ and
  $Q_i=\theta k i^{-p}$. The third singleton term is $Q_i$ because
  $\nu+\alpha-2=1$. The inequality $1+A+B\le(1+A)(1+B)$
  separates the factors $1+Q_i$.
  For $p>1$,
  \[
    \sum_{i\ge1}\log(1+A i^{-p})
    \le\int_0^\infty\log(1+A x^{-p})\ud x
    =A^{1/p}\int_0^\infty\log(1+x^{-p})\ud x.
  \]
  The last integral is finite. Hence their logarithmic contribution
  is at most $Ck^{1/p}\le Ck$.

  If $i\le k$, the remaining factor is at most
  $S_\nu(4P_i)=\sum_{l\ge0}(4P_i)^l/(l!)^\nu$:
  its singleton is at most $2P_i$, and
  $(1+li/k)^2\le(1+l)^2\le4^l$.
  Since $\nu>1$,
  $S_\nu(x)\le e^{\nu x^{1/\nu}}$.
  Therefore
  \[
    \sum_{i\le k}\log S_\nu(4P_i)
    \le\nu(4\theta)^{1/\nu}k\sum_{i\ge1}i^{-\beta/\nu}
    \le Ck,
  \]
  because $\beta/\nu>1$.

  If $i>k$, then $P_i\le\theta$. The remaining singleton tail is at most
  \[
    \theta\left(\frac1{\beta-1}+\frac1{\beta-2}\right)
    k^{\nu+1-\beta}=Ck^{\alpha_0}.
  \]
  Also, uniformly for $0\le P\le1/4$ and $y\ge0$,
  $\sum_{l\ge2}P^l(1+ly)^2/(l!)^\nu\le CP^2(1+y^2)$.
  Summing this bound gives
  \[
    Ck^{2\nu}\left(\frac{k^{1-2\beta}}{2\beta-1}
    +\frac{k^{-2}k^{3-2\beta}}{2\beta-3}\right)
    =Ck^{2\alpha_0-1}\le Ck.
  \]
  Use $\log(1+y)\le y$ for these fine factors.
  The entire product is consequently at most $e^{Ck}$.
  Positivity of its coefficients bounds the $k$th coefficient by
  $\theta^{-k}k^{-\nu k}e^{Ck}\le C^k/(k!)^\nu$.
  This proves Lemma~\ref{L:inventory-product}.
\end{proof}

Let $\mathcal F$ be a finite family of connected intervals $I_i$
meeting $[0,T]$, with lengths $h_i$ sorted decreasingly.
Let $W_i^\epsilon$ be independent copies of the smoothed unit field,
and suppose
\begin{equation}\label{E:interval-inventory}
  h_i\le L T/i,\qquad \sigma_i^2\le c h_i^{-\alpha_0}.
\end{equation}
Write $\mathcal U_{\mathcal F}^\epsilon(T;s)$ for phase evolution with
potential $s\sum_i\sigma_i\mathbf1_{I_i}(t)W_i^\epsilon(x)$.

\begin{lemma}[A fixed degree-split estimate]\label{L:fixed-split}
  Retain the finite interval fields above, with $R_\alpha>0$ and
  $\sigma_i>0$. Fix integers $r_i,q_i,k_i\ge0$ with
  $r_i+q_i=2k_i$, and put $k=\sum_i k_i\ge1$, $\lambda=k/T$.
  Represent $W_i^\epsilon(x)=\sum_jg_{ij}e_{ij}(x)$ as in
  Lemma~\ref{L:interval-contractions}. Retain $m_i$ Gaussian modes,
  a spatial Fourier band $S_b$, and Hermite cutoff $N_i=2k_i$ on
  color $i$. Write $P=\bigotimes_iP_{N_i}$
  and set
  \[
    B_i=P S_b\left(\sum_{j=1}^{m_i}g_{ij}M_{e_{ij}}\right)S_bP,
    \qquad V_{\boldsymbol z}(t)
    =\sum_i z_i\sigma_i\mathbf1_{I_i}(t)B_i.
  \]
  Let $\mathcal M^{\rm cut}_{\boldsymbol z}(T)$ be the phase evolution
  with this bounded potential and $A_0=-\Delta$ on the band. Define
  $U_{\boldsymbol r}v=[\boldsymbol z^{\boldsymbol r}]
  \mathcal M^{\rm cut}_{\boldsymbol z}(T)v$, with the projected
  deterministic initial phase in the Gaussian vacuum. Put
  \[
    \begin{gathered}
      \mathcal I=\{i:k_i>0\},\qquad
      \mathcal C=\{i:k_i=1,\ r_i=q_i=1\},\\
      \mathcal B=\mathcal I\setminus\mathcal C,\qquad
      \ell_i=\mathbf1_{\{r_i>0\}}+\mathbf1_{\{q_i>0\}}.
    \end{gathered}
  \]
  There is a finite $C_{\rm split}=C_{\rm split}(\alpha)$, uniform
  in all these cutoffs and in the finite inventory, such that
  \begin{equation}\label{E:fixed-split-bound}
    \begin{split}
      |\langle U_{\boldsymbol r}v,U_{\boldsymbol q}v
      \rangle_{L^2(\Omega;X_{1/T})}|
      \le{}&k^2 C_{\rm split}^k R_\alpha^k\|v\|_{1/T}^2
      \prod_{i\in\mathcal C}
      (\sigma_i^2h_i^2\lambda^{\alpha-2})\\
      &\quad\times\prod_{i\in\mathcal B}
      \frac{(\sigma_i^2h_i^{4-\alpha})^{k_i}}{(k_i!)^\nu}
      (1+k_i/(\lambda h_i))^{\ell_i}.
    \end{split}
  \end{equation}
  In particular, a singleton used twice on one copy has $\ell_i=1$;
  a higher color has at most two metric factors.
\end{lemma}

\begin{proof}
  We give a bound for each vector coefficient before taking their inner
  product. Every operator below acts on the finite Gaussian-mode, Hermite
  and spatial-band Hilbert space in the statement. In particular, it is
  bounded. Its piecewise-constant evolution is a finite product of block
  exponentials, hence is entire in every amplitude. All coefficient
  extractions in this proof are ordinary power-series extractions.

  An amplitude with $k_i=0$ is evaluated at zero on both copies. If
  $k_i>0$ but $I_i\cap[0,T]$ has zero length, every coefficient with a
  positive power of that amplitude vanishes. The claimed inner product
  is then zero. We may therefore assume that every active interval has
  a positive-length intersection
  $I_i^T=(a_i,b_i)$ with $(0,T)$; endpoint conventions do not affect the
  evolution or its time integrals. Its length is at most $h_i$.

  Write $a=\alpha/2$, and use the positive constant $\delta_a$ in
  Lemma~\ref{L:complex-phase}. For every $i\in\mathcal B$ put
  \begin{equation}\label{E:split-radii}
    \omega_i=\frac{k_i}{h_i},\qquad
    d_i=2\sqrt{2k_i+1}\sqrt{R_\alpha},\qquad
    \varrho_i=\frac{\delta_a\omega_i^{2-a}}{\sigma_i d_i}.
  \end{equation}
  Fix one of the two copies. Its background set is
  $\mathcal A_r=\{i\in\mathcal B:r_i>0\}$ or
  $\mathcal A_q=\{i\in\mathcal B:q_i>0\}$; denote that set by
  $\mathcal A$. Evaluate every unused amplitude at zero. Colors in
  $\mathcal C$ have degree one on this copy. Put $m=|\mathcal C|$.
  Thus there are at most $k$ background and cross colors altogether.

  \emph{Background segments and the common partition.}
  Fix $|z_i|=\varrho_i$ for $i\in\mathcal A$. With the cross amplitudes
  zero, the potential is
  $V_z(t)=\sum_{i\in\mathcal A}z_i\sigma_i\mathbf1_{I_i^T}(t)B_i$.
  Write $P_z(t,s)$ for its evolution, and set
  \[
    \Lambda(t)=\lambda+\sum_{i\in\mathcal A}
    \omega_i\mathbf1_{I_i^T}(t).
  \]
  For each $\rho>0$, Lemma~\ref{L:interval-contractions} gives
  \[
    \|A_\rho^{-1/2}V_z(t)A_\rho^{-1/2}\|
    \le D(t)\rho^{a-2},\qquad
    D(t)=\sum_{i\in\mathcal A}|z_i|\sigma_i d_i
    \mathbf1_{I_i^T}(t)
    \le\delta_a\Lambda(t)^{2-a}.
  \]
  The last step follows from~\eqref{E:split-radii} and
  $\sum x_i^{2-a}\le(\sum x_i)^{2-a}$ for nonnegative $x_i$.
  The spatial resolvents here include the identity on every Gaussian
  factor. This is a deterministic operator inequality on their joint
  Hilbert space; the input can depend on the background fields.

  For the moment fix a tuple $(t_i)_{i\in\mathcal C}$ with
  $t_i\in I_i^T$, all distinct and away from the background endpoints.
  The excluded tuples have Lebesgue measure zero. Form the common
  partition
  \begin{equation}\label{E:split-partition}
    0=\tau_0<\tau_1<\cdots<\tau_M=T
  \end{equation}
  from these times and all background endpoints in $(0,T)$.
  On $(\tau_{j-1},\tau_j)$ let $\Lambda_j$ be the constant value of
  $\Lambda$, and put $P_j=P_z(\tau_j,\tau_{j-1})$.
  There are at most $2|\mathcal A|+m$ interior partition points, so
  $M\le2|\mathcal A|+m+1\le3k+1$.
  Lemma~\ref{L:interval-complex}, with its adjoint bound as stated there,
  gives
  \begin{equation}\label{E:split-segment-product}
    \begin{split}
      \prod_{j=1}^M\|P_j\|_{\mathcal H_{\Lambda_j}\to
      \mathcal H_{\Lambda_j}}
      &\le100^M\exp\left(2\sum_{j=1}^M
      \Lambda_j(\tau_j-\tau_{j-1})\right)\\
      &\le100^{3k+1}e^{4k}=:M_k,
      \qquad \mathcal H_\rho=L^2(\Omega;X_\rho).
    \end{split}
  \end{equation}
  Indeed, the sum in the exponential is exactly
  $\lambda T+\sum_{i\in\mathcal A}\omega_i(b_i-a_i)
  \le k+\sum_{i\in\mathcal A}k_i\le2k$.
  Insertion times refine a partition; they do not repeat this integral.

  \emph{Every identity between phase norms.}
  Put $\Lambda_0=\Lambda_{M+1}=\lambda$.
  At $\tau_j$ let $\mathscr I_j$ be the identity from
  $\mathcal H_{\Lambda_j}$ to $\mathcal H_{\Lambda_{j+1}}$,
  for $0\le j\le M$. Its norm is at most
  \[
    q_j:=\max\{1,\Lambda_j/\Lambda_{j+1}\}.
  \]
  This follows directly from the two components of the phase norm and
  the spectral inequality
  $A_{\Lambda_{j+1}}^{-1}\le q_j^2 A_{\Lambda_j}^{-1}$.
  At an interior background endpoint, let $E_j,S_j,R_j$ denote the
  ending, starting and remaining background colors. Then
  \[
    \frac{\Lambda_j}{\Lambda_{j+1}}
    =\frac{\lambda+\sum_{R_j}\omega_i+\sum_{E_j}\omega_i}
    {\lambda+\sum_{R_j}\omega_i+\sum_{S_j}\omega_i}
    \le1+\sum_{E_j}\omega_i/\lambda
    \le\prod_{i\in E_j}(1+\omega_i/\lambda).
  \]
  The last product is at least one, so it also bounds $q_j$.
  At an insertion-only cut the heights agree and $q_j=1$.
  Initially $q_0=1$. At $T$ the same inequality charges all intervals
  with $b_i=T$ as ending there. Each connected $I_i^T$ ends at precisely
  one such cut. Consequently,
  \begin{equation}\label{E:interval-copy-metric}
    \prod_{j=0}^M q_j
    \le D_{\mathcal A}:=
    \prod_{i\in\mathcal A}(1+k_i/(\lambda h_i)).
  \end{equation}
  This product includes the initial and final conversions. There is no
  new copy of $D_{\mathcal A}$ at an insertion time or an overlapping
  interval's start.

  \emph{The cross-color subspaces and the word norm.}
  Let $\mathscr G_i^{(0)}$ be the vacuum of color $i$ and
  $\mathscr G_i^{(1)}$ its first Gaussian degree. For
  $S\subset\mathcal C$, use the tensor subspace
  \[
    \mathscr Z_S=
    \bigotimes_{i\in\mathcal A}\mathscr G_i^{\le N_i}
    \otimes\bigotimes_{i\in S}\mathscr G_i^{(1)}
    \otimes\bigotimes_{i\in\mathcal C\setminus S}
    \mathscr G_i^{(0)},
  \]
  with every omitted Gaussian color in its vacuum and with the common
  spatial band understood. Each $P_j$ preserves the corresponding
  phase space over $\mathscr Z_S$: its potential acts only on colors in
  $\mathcal A$, and its spatial operators act identically on all cross
  Gaussian factors. The identities $\mathscr I_j$ preserve the same
  tensor subspace.

  Define $J_i(u,w)=(0,\sigma_i B_i u)$ for $i\in\mathcal C$.
  If $i\notin S$, multiplication by its field takes its vacuum into
  first Gaussian degree. The Hermite cutoff $N_i=2$ does not alter this
  step. Thus $J_i$ maps the phase over $\mathscr Z_S$ into the phase
  over $\mathscr Z_{S\cup\{i\}}$.
  Collect all other Gaussian factors into $\mathscr R_i$.
  Every input has the form $1_i\otimes(u,w)$, with
  $(u,w)\in\mathscr R_i\otimes X_\rho$. The cutoffs on other
  colors are identities on its retained degrees, which multiplication
  by the color-$i$ field leaves unchanged. Hence
  \[
    J_i(1_i\otimes(u,w))
    =\sigma_i\sum_{j=1}^{m_i}g_{ij}\otimes
    (0,S_bM_{e_{ij}}S_bu).
  \]
  Orthogonality $\E[g_{ij}g_{il}]=\mathbf1_{\{j=l\}}$ gives
  \[
    \begin{split}
      \|J_i(1_i\otimes(u,w))\|_{\mathcal H_\rho}^2
      &=\sigma_i^2\sum_{j=1}^{m_i}
      \|A_\rho^{-1/2}S_bM_{e_{ij}}S_bu
      \|_{\mathscr R_i\otimes L^2_x}^2\\
      &\le\sigma_i^2R_\alpha\rho^{\alpha-2}
      \|u\|_{\mathscr R_i\otimes L^2_x}^2\\
      &\le\sigma_i^2R_\alpha\rho^{\alpha-2}
      \|1_i\otimes(u,w)\|_{\mathcal H_\rho}^2.
    \end{split}
  \]
  The first inequality is~\eqref{E:interval-column} tensored with
  $\mathscr R_i$ and allows arbitrary dependence on earlier colors.
  Thus, at the insertion time,
  \begin{equation}\label{E:split-fresh-insertion}
    \|J_i\|\le\sigma_i\sqrt{R_\alpha}
    \Lambda(t_i)^{(\alpha-2)/2}
    \le c_i:=\sigma_i\sqrt{R_\alpha}\lambda^{(\alpha-2)/2}.
  \end{equation}
  Starting with $\mathscr Z_\varnothing$, these subspaces describe every
  partial word. They justify each new-color estimate even though the
  current vector depends on the background and earlier cross colors.
  No occupied-color annihilation is estimated by a vacuum bound.

  Equivalently, apply Lemma~\ref{L:finite-word-cutoff} to the cross
  colors, with $\mathscr X$ containing the bounded background Gaussian
  space and the spatial phase space. Background segments act only on
  $\mathscr X$, and each cross color occurs once. Its cutoff is an
  exact identity on every prefix of the selected word. This does not
  identify an untruncated background propagator with a fixed cutoff.

  At an interior cut $\tau_j$ let $B_j^{\rm cut}=J_i$ if
  $\tau_j=t_i$ and let $B_j^{\rm cut}$ be the identity otherwise.
  Apply $B_j^{\rm cut}$ after $\mathscr I_j$; at an insertion cut the
  two heights are equal. The chronological word, as a map from
  $\mathcal H_\lambda$ back to $\mathcal H_\lambda$, is exactly
  \[
    \mathcal W_{\mathcal A}(z,\boldsymbol t)
    =\mathscr I_M P_M B_{M-1}^{\rm cut}\mathscr I_{M-1}P_{M-1}
    \cdots B_1^{\rm cut}\mathscr I_1P_1\mathscr I_0.
  \]
  For $M=1$ this means $\mathscr I_1P_1\mathscr I_0$.
  The rightmost factor acts first; no spatial operators are commuted.
  Multiplying their norms, using the subspaces just specified,
  gives the explicit bound
  \begin{equation}\label{E:split-word-product}
    \begin{split}
      \|\mathcal W_{\mathcal A}(z,\boldsymbol t)v\|_\lambda
      &\le\left(\prod_{j=1}^M\|P_j\|\right)
      \left(\prod_{j=0}^M q_j\right)
      \left(\prod_{i\in\mathcal C}c_i\right)\|v\|_\lambda\\
      &\le M_kD_{\mathcal A}\|v\|_\lambda
      \prod_{i\in\mathcal C}c_i.
    \end{split}
  \end{equation}
  The background norm bound is on the joint Gaussian Hilbert space;
  it is not obtained by conditioning on successive fields.

  \emph{The insertion cube and vector Cauchy formula.}
  Give the cross colors amplitudes $y_i$ and define the vector
  \[
    \Phi_{\mathcal A}(z)
    :=\left[\prod_{i\in\mathcal C}y_i\right]
    \mathcal M^{\rm cut}_{(z,y,0)}(T)v.
  \]
  Variation of constants about $P_z$ and iteration give a Dyson series.
  A monomial of degree one in every $y_i$ uses exactly $m$ insertions,
  with each distinct cross color used once. Hence
  \begin{equation}\label{E:interval-cross-cube}
    \Phi_{\mathcal A}(z)
    =\sum_{\pi}\int_{D_\pi}
    \mathcal W_{\mathcal A}(z,\boldsymbol t)v\,\ud\boldsymbol t,
    \qquad
    D_\pi=\left\{\boldsymbol t\in\prod_{i\in\mathcal C}I_i^T:
    t_{\pi_1}<\cdots<t_{\pi_m}\right\}.
  \end{equation}
  Each ordered Dyson integral has coefficient one. The permutation
  simplices $D_\pi$ partition the cube up to null diagonals. In particular,
  \[
    \sum_\pi |D_\pi|=\prod_{i\in\mathcal C}|I_i^T|
    \le\prod_{i\in\mathcal C}h_i.
  \]
  Minkowski applied to~\eqref{E:interval-cross-cube} and the single-word
  bound~\eqref{E:split-word-product} therefore gives
  \begin{equation}\label{E:interval-cross-vector}
    \|\Phi_{\mathcal A}(z)\|_\lambda
    \le M_kD_{\mathcal A}\|v\|_\lambda
    \prod_{i\in\mathcal C}c_i h_i.
  \end{equation}
  There is no factor $m!$ or $1/m!$ in this estimate. For $m=0$,
  the cube has unit mass and $\Phi_{\mathcal A}(z)=P_z(T,0)v$.

  The vector $\Phi_{\mathcal A}$ is entire in the background amplitudes.
  On the first copy its coefficient is given by the normalized formula
  \begin{equation}\label{E:split-vector-cauchy}
    \begin{split}
      U_{\boldsymbol r}v
      ={}&\left(\prod_{i\in\mathcal A_r}\varrho_i^{-r_i}\right)
      \int_{[0,2\pi]^{\mathcal A_r}}
      e^{-i\sum_{i\in\mathcal A_r}r_i\theta_i}
      \Phi_{\mathcal A_r}((\varrho_i e^{i\theta_i})_i)
      \prod_{i\in\mathcal A_r}\frac{\ud\theta_i}{2\pi}.
    \end{split}
  \end{equation}
  This is precisely the desired coefficient because each cross exponent
  equals one and every omitted exponent is zero. The normalized angular
  measure has total mass one. Thus~\eqref{E:interval-cross-vector}
  bounds $\|U_{\boldsymbol r}v\|_\lambda$ with the additional factor
  $\prod_{i\in\mathcal A_r}\varrho_i^{-r_i}$, and the identical
  formula bounds the second copy using $\mathcal A_q,q_i$.
  No holomorphic formula is applied to a squared norm.

  \emph{The inner product and all constants.}
  Since $\lambda=k/T$ and $k\ge1$,
  \[
    \|w\|_{1/T}\le k\|w\|_\lambda,\qquad
    \|v\|_\lambda\le\|v\|_{1/T}.
  \]
  Cauchy--Schwarz between the two vectors on the same Gaussian space
  now gives, before any constants are absorbed,
  \begin{equation}\label{E:split-before-absorption}
    \begin{split}
      |\langle U_{\boldsymbol r}v,U_{\boldsymbol q}v
      \rangle_{\mathcal H_{1/T}}|
      \le{}&k^2 M_k^2D_{\mathcal A_r}D_{\mathcal A_q}
      \|v\|_{1/T}^2
      \prod_{i\in\mathcal B}\varrho_i^{-2k_i}\\
      &\quad\times\prod_{i\in\mathcal C}
      (R_\alpha\sigma_i^2h_i^2\lambda^{\alpha-2}).
    \end{split}
  \end{equation}
  The radius exponent is $r_i+q_i=2k_i$. The metric product is exactly
  \[
    D_{\mathcal A_r}D_{\mathcal A_q}
    =\prod_{i\in\mathcal B}(1+k_i/(\lambda h_i))^{\ell_i}.
  \]
  In particular, a singleton on only one copy has one ending charge,
  not two. For every $i\in\mathcal B$, $d_i^2\le12k_iR_\alpha$ gives
  \begin{equation}\label{E:split-radius-factorial}
    \begin{split}
      \varrho_i^{-2k_i}
      &=\left(\frac{\sigma_i^2d_i^2}{\delta_a^2}\right)^{k_i}
      \left(\frac{h_i}{k_i}\right)^{(4-\alpha)k_i}\\
      &\le(12\delta_a^{-2})^{k_i}
      (R_\alpha\sigma_i^2h_i^{4-\alpha})^{k_i}
      k_i^{-(3-\alpha)k_i}\\
      &\le(12\delta_a^{-2})^{k_i}
      \frac{(R_\alpha\sigma_i^2h_i^{4-\alpha})^{k_i}}
      {(k_i!)^{3-\alpha}}.
    \end{split}
  \end{equation}
  The last step uses $k_i!\le k_i^{k_i}$.
  Finally,
  \[
    M_k^2=100^{6k+2}e^{8k}\le(100^8e^8)^k,
    \qquad |\mathcal C|+\sum_{i\in\mathcal B}k_i=k.
  \]
  Substituting these inequalities in~\eqref{E:split-before-absorption}
  proves~\eqref{E:fixed-split-bound} with the explicit admissible choice
  \begin{equation}\label{E:split-explicit-constant}
    C_{\rm split}=100^8e^8
    \max\{1,12\delta_{\alpha/2}^{-2}\}.
  \end{equation}
  This constant depends only on $\alpha$. No permutation, Gaussian-mode,
  inventory-size or further degree factor remains. The projected initial
  phase has norm at most the displayed original $\|v\|_{1/T}$.
  This proves Lemma~\ref{L:fixed-split}.
\end{proof}

\begin{proposition}[Uniform interval coefficients]\label{P:interval-coefficients}
  There is $C=C(\alpha,\alpha_0,L,c)$ such that, for real Schwartz phase $v$,
  every $k\ge1$ satisfies
  \begin{equation}\label{E:interval-coefficient-bound}
    \left|[s^{2k}]\E\|\mathcal U_{\mathcal F}^\epsilon(T;s)v\|_{1/T}^2\right|
    \le\frac{C^k R_\alpha^k T^{\beta k}}{(k!)^\nu}\|v\|_{1/T}^2,
  \end{equation}
  uniformly in $\epsilon>0$ and the finite family.
  In particular,
  \begin{equation}\label{E:interval-phase-bound}
    \E\|\mathcal U_{\mathcal F}^\epsilon(T;1)v\|_{1/T}^2
    \le e\exp\{C R_\alpha^{1/\nu}T^{\beta/\nu}\}\|v\|_{1/T}^2.
  \end{equation}
\end{proposition}

\begin{proof}
  Zero noise is trivial; omit any zero $\sigma_i$.
  Enlarge the inventory constant $L$ to $\max\{1,L\}$ if necessary.
  The hypotheses remain true and the final constant may depend on $L$,
  so throughout this proof we may assume $L\ge1$.
  Replacing $(\sigma_i,W_i^\epsilon)$ by
  $(|\sigma_i|,\operatorname{sgn}(\sigma_i)W_i^\epsilon)$ leaves the
  potential unchanged and preserves the joint law of the independent
  real Gaussian fields. Thus, we may assume $\sigma_i>0$.
  We first work with finitely many Gaussian coordinates of each field and
  a bounded spatial Fourier band. Denote their common phase Hilbert space
  by $\mathcal H_\rho=L^2(\Omega;X_\rho)$.
  The initial data are projected to the band. This contracts every
  $X_\rho$ norm; we keep the original $\|v\|_\rho$ on the right of
  the estimates. The projections converge strongly to the original data.

  \emph{Ordinary coefficients and their existence.}
  Fix $\lambda>0$ temporarily. Give interval $i$ its own amplitude
  $z_i$ and write
  \[
    \mathcal U(T;\boldsymbol z)v
    =\sum_{\boldsymbol r\in\N_0^{\mathcal F}}
    \boldsymbol z^{\boldsymbol r}U_{\boldsymbol r}v.
  \]
  These are ordinary power-series coefficients, without factorials
  incorporated in their definition. At fixed smoothing and finite inventory,
  put $v_{\max}=\sup_t\sum_i\sigma_i^2\mathbf1_{I_i}(t)
  \Gamma_\epsilon(0)<\infty$.
  On Gaussian degrees at most $n$, multiplication by the instantaneous
  field has norm at most $2\sqrt{n+1}\sqrt{v_{\max}}$.
  The free phase has norm at most $e^{\lambda h/2}$ in $X_\lambda$,
  and a phase insertion $(u,w)\mapsto(0,Wu)$ costs at most its
  unweighted multiplication norm divided by $\lambda$.
  Thus, on $\max_i|z_i|\le z_*$ the total order-$n$ phase is bounded by
  \begin{equation}\label{E:interval-entire-majorant}
    e^{\lambda T/2}
    \frac{(2z_*\sqrt{n+1}\sqrt{v_{\max}}T/\lambda)^n}{n!}
    \|v\|_\lambda .
  \end{equation}
  The series of these bounds converges for every finite $z_*$.
  Its locally uniform convergence defines an entire vector function.
  We also verify coefficientwise absolute convergence. Fix $z_*>0$ and put
  \[
    K_{2z_*}=\sup_{\max_i|z_i|\le2z_*}
    \|\mathcal U(T;\boldsymbol z)v\|_{\mathcal H_{1/T}}<\infty,
  \]
  using the majorant with its temporary parameter $\lambda=1/T$.
  Normalized vector Cauchy integration on this larger polydisc gives
  \[
    \|U_{\boldsymbol r}v\|_{\mathcal H_{1/T}}
    \le K_{2z_*}(2z_*)^{-|\boldsymbol r|},\qquad
    \sum_{\boldsymbol r}z_*^{|\boldsymbol r|}
    \|U_{\boldsymbol r}v\|_{\mathcal H_{1/T}}
    \le2^{|\mathcal F|}K_{2z_*}.
  \]
  The sum is the product of $|\mathcal F|$ geometric series.
  Cauchy--Schwarz therefore bounds the absolute energy double series
  by $4^{|\mathcal F|}K_{2z_*}^2$. This finite factor justifies the
  coefficient identities at fixed family and smoothing; it does not
  enter the uniform coefficient estimate below.

  Set
  $Q_{\boldsymbol r,\boldsymbol q}
  =\langle U_{\boldsymbol r}v,U_{\boldsymbol q}v
  \rangle_{\mathcal H_{1/T}}$.
  Both vectors use the same Gaussian fields. Independence is between
  distinct colors, not between the two copies in this inner product.
  For real $s$, substitution $z_i=s$ gives the exact identity
  \begin{equation}\label{E:interval-energy-splits}
    [s^{2k}]\E\|\mathcal U(T;s)v\|_{1/T}^2
    =\sum_{|\boldsymbol r|+|\boldsymbol q|=2k}
    Q_{\boldsymbol r,\boldsymbol q}.
  \end{equation}
  Reflection of Gaussian color $i$ multiplies $U_{\boldsymbol r}v$
  by $(-1)^{r_i}$. Hence $Q_{\boldsymbol r,\boldsymbol q}=0$ unless
  $r_i+q_i=2k_i$ for every $i$, where $\sum_i k_i=k$.
  If $k_i=0$, both coefficients are obtained by setting $z_i=0$;
  this removes that field exactly. There are at most $k$ active colors.
  For fixed $\boldsymbol k$, the number of splits is
  $\prod_i(2k_i+1)\le3^k$.

  For this fixed $\boldsymbol k$, truncate the Hermite degree of color $i$
  at $N_i=2k_i$. A word contributing to $U_{\boldsymbol r}$ has
  $r_i\le2k_i$ insertions of color $i$, and the other copy has
  $q_i\le2k_i$. Lemma~\ref{L:finite-word-cutoff}, with the spatial
  phase space as $\mathscr X$ and free phase factors between insertions,
  therefore preserves both selected vector coefficients exactly.
  Their Duhamel time integrals and finite word sums preserve the equality.
  Creation followed by annihilation is retained; there is no
  Hermite-degree limit in this coefficient calculation.

  For the uniform coefficient estimate put $\lambda=k/T$.
  Apply Lemma~\ref{L:fixed-split} to each selected coefficient, retaining
  the original sorted interval labels in the final sum.
  Its factor $\ell_i$ is one for a singleton mean and at most two for
  every higher color. The separate cross factor applies only at
  $(r_i,q_i)=(1,1)$.
  Absorb $k^2C_{\rm split}^k3^kc^k$ into $C^k$, using $k^2\le4^k$.
  After $\sigma_i^2\le c h_i^{-\alpha_0}$, the resulting local weights,
  with this common per-total-order constant understood, are
  \[
    \begin{array}{c|c}
      \text{case}&\text{weight in energy}\\ \hline
      (2,0)\text{ or }(0,2)&R_\alpha h_i^\beta
      (1+1/(\lambda h_i))\\
      (1,1)&R_\alpha\lambda^{\alpha-2}h_i^{2-\alpha_0}\\
      k_i=l\ge2&R_\alpha^l h_i^{\beta l}
      (1+l/(\lambda h_i))^2/(l!)^\nu .
    \end{array}
  \]
  The first metric factor occurs on only one copy; the last costs at
  most one factor on each copy. To justify the length substitution,
  expand the entire higher-degree weight, before its positive constant:
  \[
    h^{\beta l}(1+l/(\lambda h))^2
    =h^{\beta l}+\frac{2l}{\lambda}h^{\beta l-1}
    +\frac{l^2}{\lambda^2}h^{\beta l-2}.
  \]
  Since $\beta>2$ and $l\ge2$, all three powers are positive.
  The singleton mean likewise has powers $\beta,\beta-1$, and
  the cross singleton has power $p=2-\alpha_0>0$.
  Thus each whole local weight increases with $h$; we do not bound
  the inverse-length factor separately. At $h=LT/i$,
  $1+l/(\lambda h)=1+li/(kL)\le1+li/k$, since $L\ge1$.
  The remaining powers of $L$ are absorbed in the allowed $C^k$.
  For a singleton let $m_i,c_i$ be the first and second table weights.
  Every one of its splits is bounded by $m_i+c_i$.
  The higher-degree table weight is already uniform over its splits.
  Hence the previously counted $\prod_i(2k_i+1)\le3^k$ bounds all split
  choices once, using these combined singleton weights; that is the factor
  absorbed into $C^k$ above.
  Substituting $h_i\le LT/i$ and $\lambda=k/T$ therefore extracts
  $C^kR_\alpha^kT^{\beta k}$, leaving $v_i$ at $k_i=1$ and
  $b_{i,l}$ at $k_i=l\ge2$ from Lemma~\ref{L:inventory-product}.

  There is no further multinomial factor: for nonnegative weights
  $w_{i,0}=1$, ordinary multiplication of power series gives exactly
  \[
    \sum_{\sum_i k_i=k}\prod_i w_{i,k_i}
    =[z^k]\prod_i\left(\sum_{l\ge0}w_{i,l}z^l\right).
  \]
  Apply this identity to the sum in~\eqref{E:interval-energy-splits},
  using the two singleton alternatives together in $v_i$.
  Lemma~\ref{L:inventory-product} now proves
  \eqref{E:interval-coefficient-bound} at the finite cutoffs.

  \emph{Identification and summation.}
  Keep positive smoothing, finite inventory and a fixed coefficient.
  The finite-degree multiplication bound used in
  \eqref{E:interval-entire-majorant} is uniform in mode and band cutoffs.
  On finite-coordinate Gaussian vectors the omitted annihilation tail is
  zero and the creation tail tends to zero by its omitted pointwise
  variances and dominated convergence. Density in each finite degree
  extends this strong convergence. Closedness identifies the limit with
  actual multiplication by the measurable smoothed field.
  Fourier projections converge strongly and commute with free evolution.
  Dominated time integration thus identifies every fixed Duhamel word.
  The selected coefficients of the local Hermite truncation were already
  equal to those untruncated words. The full actual series is constructed
  separately using~\eqref{E:interval-entire-majorant}, choosing a sufficient
  degree cutoff anew at each order. A fixed-degree truncated propagator
  is not identified with the full evolution.
  The entire majorant gives convergence uniformly on compact amplitude
  sets. The coefficients estimated above are therefore those of the
  actual finite-interval model, with no zero-smoothing limit at this step.

  The nonuniform number $v_{\max}$ was used only for this identification.
  The uniform coefficient bound contains no such number. Its constants
  come from $\delta_{\alpha/2}$, the fixed phase bound, the inventory
  lemma and $L,c$; covariance enters only through $R_\alpha^k$.
  The zero-order energy is at most $e\|v\|_{1/T}^2$.
  Put $x=CR_\alpha T^\beta$ and $Y=e^{\nu x^{1/\nu}}\ge1$.
  Since $\nu>1$, $\sum_{k\ge0}x^k/(k!)^\nu\le Y$.
  Summing the coefficient bounds in absolute value gives
  \[
    \E\|\mathcal U(T;1)v\|_{1/T}^2
    \le(e+Y-1)\|v\|_{1/T}^2\le eY\|v\|_{1/T}^2.
  \]
  Absorbing $\nu C^{1/\nu}$ into the parameter-only constant proves
  \eqref{E:interval-phase-bound}. This proves
  Proposition~\ref{P:interval-coefficients}.
\end{proof}

\subsection{Finite Gaussian models and their terminal kernels}

For $n\ge1$, define the positive terminal-chain measure
\begin{equation}\label{E:terminal-chain-measure}
  \mathsf g_n^{T,x}(\ud\boldsymbol s,\ud\boldsymbol y)
  =\mathbf1_{[0,T]^n_<}(\boldsymbol s)\ud\boldsymbol s
  \prod_{j=1}^n
  G_{s_{j+1}-s_j}(y_{j+1}-\ud y_j),
  \qquad (s_{n+1},y_{n+1})=(T,x).
\end{equation}
The spatial product is read backwards from $x$. Explicitly, it is the
pushforward of $\prod_{j=1}^nG_{s_{j+1}-s_j}(\ud w_j)$ under
$y_j=x-\sum_{l=j}^n w_l$. This defines the measure also in dimension
three. In dimensions one and two its density is the ordered kernel
$g_n$ in~\eqref{E:expansion}. Set $\mathsf g_0^{T,x}$ equal to unit mass
on the empty tuple. This definition introduces no kernel symmetrization.

\begin{lemma}[The finite terminal-chain Wick formula]\label{L:terminal-wick}
  Let $\mathcal W(s,y)$ be a centered real Gaussian field on
  $[0,T]\times\R^d$, $d=1,2,3$, with covariance
  $\mathcal K(s,y;r,z)$. Suppose that
  $V=\sup_{s,y}\E|\mathcal W(s,y)|^2<\infty$, and that the field is
  jointly continuous in mean square on each open cell of a finite
  partition of $[0,T]$, times $\R^d$.
  Define $Y_0=1$ and
  \[
    Y_n(T,x)=\int\prod_{j=1}^n\mathcal W(s_j,y_j)
    \,\mathsf g_n^{T,x}(\ud\boldsymbol s,\ud\boldsymbol y).
  \]
  These Bochner integrals exist in $L^2(\Omega)$ and satisfy
  \begin{equation}\label{E:terminal-term-majorant}
    \|Y_n(T,x)\|_2
    \le\sqrt{(2n-1)!!}\,V^{n/2}\frac{T^{2n}}{(2n)!},
    \qquad n\ge1.
  \end{equation}
  For $m+n=2k$, concatenate
  $\boldsymbol\tau=(s_1,\ldots,s_m,r_1,\ldots,r_n)$ and
  $\boldsymbol\eta=(y_1,\ldots,y_m,z_1,\ldots,z_n)$. Then
  \begin{equation}\label{E:terminal-wick-formula}
    \E[Y_m(T,x)Y_n(T,x)]
    =\sum_{D\in\Pi_k}\mathcal T_{m,n,D}^{\mathcal K}(T,x),
  \end{equation}
  where, with both chains terminating at $(T,x)$,
  \begin{equation}\label{E:terminal-pairing-integral}
    \begin{split}
      \mathcal T_{m,n,D}^{\mathcal K}
      ={}&\int_{[0,T]^m_<\times[0,T]^n_<}
      \ud\boldsymbol s\,\ud\boldsymbol r
      \int_{(\R^d)^m\times(\R^d)^n}\\
      &\quad\times\prod_{j=1}^m
      G_{s_{j+1}-s_j}(y_{j+1}-\ud y_j)
      \prod_{j=1}^n
      G_{r_{j+1}-r_j}(z_{j+1}-\ud z_j)\\
      &\quad\times\prod_{\{a,b\}\in D}
      \mathcal K(\tau_a,\eta_a;\tau_b,\eta_b).
    \end{split}
  \end{equation}
  Each pairing has coefficient one. If $m+n$ is odd, the expectation
  is zero. Empty chains and the case $m=n=0$ have the usual empty-product
  meaning. If $\mathcal K\ge0$, every integral above is nonnegative.
  Consequently, entrywise comparison $0\le\mathcal K_1\le\mathcal K_2$
  compares all finite partial-order second moments in the same direction.
  The series $\sum_{n\ge0}r^nY_n$ converges absolutely in $L^2$ for
  every real or complex $r$.
\end{lemma}

\begin{proof}
  The mass of $G_h$ is $h$. If $M_n(T)$ is the total mass of
  $\mathsf g_n^{T,x}$, integration at the last vertex gives
  $M_0=1$ and $M_n(T)=\int_0^T(T-s)M_{n-1}(s)\ud s$.
  Induction therefore yields $M_n(T)=T^{2n}/(2n)!$.
  Gaussian moments and H\"older's inequality give
  \[
    \left\|\prod_{j=1}^n\mathcal W(s_j,y_j)\right\|_2
    \le\prod_{j=1}^n\|\mathcal W(s_j,y_j)\|_{2n}
    \le\sqrt{(2n-1)!!}\,V^{n/2}.
  \]
  Mean-square continuity of Gaussian variables implies their continuity
  in every fixed finite $L^p$. Hence, the product is strongly measurable
  in $L^2$ on the stated pieces. The finite kernel mass and the displayed
  bound prove Bochner integrability and~\eqref{E:terminal-term-majorant}.

  Fubini now passes expectation through the product of the two finite
  kernel measures. For the $m+n$ Gaussian variables at their labelled
  vertices, differentiate
  \[
    \E\exp\left(\sum_i t_i\mathcal W(\tau_i,\eta_i)\right)
    =\exp\left(\frac12\sum_{i,j}t_i t_j
    \mathcal K(\tau_i,\eta_i;\tau_j,\eta_j)\right)
  \]
  once in each $t_i$ at zero. Odd total degree gives zero.
  At degree $2k$ the result is the sum over unordered pair partitions,
  with one covariance product per pairing. Orientations and orderings
  of the $k$ pairs cancel the exponential's $2^k k!$ denominator.
  Integration gives~\eqref{E:terminal-wick-formula} with precisely
  the domains and coefficients in~\eqref{E:terminal-pairing-integral}.

  Symmetrizing a chain measure does not change its stochastic integral:
  the product of its $n$ scalar field values is invariant under relabeling.
  Thus, averaging the $n!$ pushforwards of $\mathsf g_n^{T,x}$ with
  coefficient $1/n!$ gives the same $Y_n$. There is no additional $n!$
  factor in~\eqref{E:terminal-wick-formula}, or $m!n!$ in a two-chain
  product. This identifies the ordinary ordered regularized integrals
  and their symmetrized convention in~\eqref{E:expansion}.

  In dimension three one may first replace $G$ by $p_\eta*G$.
  Those positive measures have the same masses and converge weakly to
  $G$. Off the finitely many time cut points, all finite Gaussian moments
  are bounded continuous functions of the spatial variables. Dominated
  convergence for their finite Wick sums proves the same limit for
  the mixed second moments with two Green widths. It gives $L^2$
  convergence to the Bochner integral above, exactly the fixed-noise
  Green convention used in the source.

  If $\mathcal K\ge0$, positivity of the Green measures makes each
  covariance product nonnegative. Comparing them proves the stated
  finite-moment monotonicity, including self-pairs and unequal chains.
  Finally, the ratio of successive right sides of
  \eqref{E:terminal-term-majorant}, with an additional factor $|r|^n$,
  is $|r|\sqrt V T^2/((2n+2)\sqrt{2n+1})$, which tends to zero.
  The zero-variance case is immediate.
  This proves Lemma~\ref{L:terminal-wick}.
\end{proof}

\begin{lemma}[Uniform series tails from scaled moments]\label{L:uniform-series-tail}
  Fix $(T,x)$. For each positive regularization pair $(\epsilon,\delta)$,
  let $Y_n^{\epsilon,\delta}$ be the terms of
  Lemma~\ref{L:terminal-wick} for a field with nonnegative covariance.
  Write $u^{\epsilon,\delta}(r)=\sum_{n\ge0}r^nY_n^{\epsilon,\delta}$.
  Suppose that, for some $r>1$ and finite $B_r$,
  \[
    \sup_{\epsilon,\delta>0}
    \E|u^{\epsilon,\delta}(r)|^2\le B_r,
    \qquad
    Y_n^{\epsilon,\delta}\longrightarrow X_n
    \text{ in }L^2\text{ for each fixed }n.
  \]
  Then $u=\sum_{n\ge0}X_n$ converges absolutely in $L^2$,
  $u^{\epsilon,\delta}(1)\to u$ in $L^2$, and
  \begin{equation}\label{E:uniform-series-tail}
    \|Y_n^{\epsilon,\delta}\|_2,\ \|X_n\|_2
    \le B_r^{1/2}r^{-n},\qquad
    \left\|\sum_{n>N}Y_n^{\epsilon,\delta}\right\|_2,
    \left\|\sum_{n>N}X_n\right\|_2
    \le\frac{B_r^{1/2}r^{-(N+1)}}{1-r^{-1}}.
  \end{equation}
  If also $\E|u^{\epsilon,\delta}(1)|^2\le B_1$ uniformly, then
  $\E|u|^2\le B_1$.
\end{lemma}

\begin{proof}
  Lemma~\ref{L:terminal-wick} gives absolute $L^2$ convergence of every
  regularized series and nonnegative mixed moments.
  Its scaled second moment therefore contains the nonnegative term
  $r^{2n}\E|Y_n^{\epsilon,\delta}|^2$, so
  $r^{2n}\E|Y_n^{\epsilon,\delta}|^2\le B_r$.
  Taking the fixed-order $L^2$ limit proves the same bound for $X_n$.
  The geometric series and the triangle inequality give all estimates
  in~\eqref{E:uniform-series-tail}, including absolute convergence.

  For each $N$, write both full series as their first $N+1$ terms
  and their tails. Their distance is at most
  \[
    \frac{2B_r^{1/2}r^{-(N+1)}}{1-r^{-1}}
    +\left\|\sum_{n=0}^N(Y_n^{\epsilon,\delta}-X_n)\right\|_2.
  \]
  First let $\epsilon,\delta\downarrow0$ at fixed $N$, and then let
  $N\to\infty$. This proves convergence of the full regularized solution;
  it was not assumed. Continuity of the $L^2$ norm passes the bound
  $B_1$ to $u$. This proves Lemma~\ref{L:uniform-series-tail}.
\end{proof}

\begin{theorem}[Full upper scale]\label{T:full-upper}
  Under Hypothesis~\ref{H:homog}, let $u$ be the canonical expansion
  solution~\eqref{E:expansion}, constructed as a Stratonovich mild
  solution in Proposition~\ref{P:mild-construction}. Put
  \[
    R_\alpha=\frac{\alpha\pi\mu(B_1)}{2\sin(\pi\alpha/2)}.
  \]
  For every admissible $d=1,2,3$, there is a finite
  $C=C(\alpha,\alpha_0)$ such that
  \begin{equation}\label{E:full-upper-bound}
    \E u^2(T,x)
    \le e(T+2)^d
    \exp\{C R_\alpha^{1/(3-\alpha)}
    T^{(4-\alpha-\alpha_0)/(3-\alpha)}\},\qquad T\ge1.
  \end{equation}
  In particular, this establishes the unchanged Goal~\ref{G:upper}.
\end{theorem}

\begin{proof}
  Zero noise is trivial. Choose $H_0$ with $6T\le H_0<12T$.
  At lengths $h_j=H_0 2^{-j}$, use the three grids with endpoints
  $h_j(n+(-1)^j t)$, $n\in\mathbb Z$, $t=0,1/3,2/3$.
  They are nested: the difference between the parent and child shifts
  in child units is an integer, since $3t\in\mathbb Z$.
  For $s\ne r$ in $[0,T]$, choose a scale
  $3|s-r|<h_j\le6|s-r|$.
  Boundaries of the three grids at this scale have mutual spacing
  $h_j/3>|s-r|$. Hence at least one grid interval contains both points,
  including their endpoints after choosing a boundary-free grid.
  It follows that
  \begin{equation}\label{E:dyadic-time-majorant}
    |s-r|^{-\alpha_0}
    \le6^{\alpha_0}\sum_{\text{three grids},\,|I|\le H_0}
    |I|^{-\alpha_0}\mathbf1_I(s)\mathbf1_I(r)=:K_\infty(s,r).
  \end{equation}
  For context, the sum is at most $C_{\alpha_0}|s-r|^{-\alpha_0}$ off the diagonal:
  only lengths at least $|s-r|$ contribute, with at most one interval
  per grid and length. Endpoint values do not affect the time integrals.

  Keep intervals meeting $[0,T]$ through depth $J$, and use independent
  static smoothed fields with $\sigma_I^2=6^{\alpha_0}|I|^{-\alpha_0}$.
  Their time covariance is the corresponding partial sum $K_J$.
  The decreasing interval lengths obey $h_i\le78T/i$.
  Indeed, at length $h_j$ there are at most $3(T/h_j+2)$ intervals.
  Summing levels $0,\ldots,j$ bounds their cumulative count by
  \[
    6T/h_j+6(j+1)\le6T/h_j+6\,2^j\le78T/h_j,
  \]
  since $H_0<12T$ and $2^j=H_0/h_j$.
  Each index at level $j$ is at most that cumulative count, which gives
  the asserted decreasing-length bound. Thus, one may take $L=78$
  and $c=6^{\alpha_0}$ in Proposition~\ref{P:interval-coefficients}.
  Proposition~\ref{P:interval-coefficients} applies uniformly in $J,\epsilon$.

  To pass from phase data to constant initial data, choose
  $f_T\in C_c^\infty$ with $0\le f_T\le1$, equal to one on $B_{T+1}$
  and supported in $B_{T+2}$, and set the velocity to zero.
  For $|y|+s<T+1$, $G_s*f_T(y)=s$, so $C_sf_T(y)=1$.
  The support of $G_t$ is contained in $B_t$.
  Along a chain ending at $x\in B_1$ at time $T$, each earlier point
  $(s,y)$ satisfies $|y|+s\le|x|+T<T+1$.
  Thus, its free initial-data factor is one.
  Induction on Duhamel order identifies the position generated
  from $(f_T,0)$ at time $T$ on $B_1$ with the constant-data model
  $u_{J,\epsilon}$.
  This identity can be taken in Gaussian $L^2$ term by term.
  At fixed $J,\epsilon$, each finite-order terminal integral is
  continuous in $x$ as an $L^2(\Omega)$ vector: write its Green
  variables as displacements from $x$, and use continuity of
  $\Gamma_\epsilon$ in its mixed Wick moments. Bounded covariance
  products and the finite terminal Green mass permit dominated
  convergence. These measurable representatives identify the
  $L^2(\Omega;L^2_x)$ position on $B_1$ with the same pointwise
  constant-data terms. The summable bound below passes this identity
  to their series.
  At finite $J,\epsilon$, pointwise convergence for constant data follows
  from the bound
  $\sqrt{(2n-1)!!}\,v_{\max}^{n/2}T^{2n}/(2n)!$
  on the $n$th position term.
  The model is spatially stationary. Consequently,
  \[
    |B_1|\E|u_{J,\epsilon}(T,0)|^2
    \le\E\|u_{f_T,J,\epsilon}(T)\|_2^2
    \le e\,|B_{T+2}|\exp\{C R_\alpha^{1/\nu}T^{\beta/\nu}\}.
  \]

  We now identify the interval-model Wick sums before comparing them.
  Its centered Gaussian noise has covariance
  \[
    \E[W_{J,\epsilon}(s,y)W_{J,\epsilon}(r,z)]
    =\sum_{I\in\mathcal F_J}\sigma_I^2
    \mathbf1_I(s)\mathbf1_I(r)\Gamma_\epsilon(y-z)
    =K_J(s,r)\Gamma_\epsilon(y-z).
  \]
  Lemma~\ref{L:terminal-wick} applies: at fixed $J,\epsilon$ the field
  has bounded variance, is mean-square continuous in space and is
  piecewise continuous in time. Its exact terminal kernels are
  \eqref{E:terminal-chain-measure}, and every term of
  \eqref{E:terminal-pairing-integral} has covariance factor
  $K_J(s_j,s_l)\Gamma_\epsilon(y_j-y_l)$, with coefficient one.
  This comparison is made before any time reversal; $K_J$ need not be
  stationary in time. The position kernels and constant initial data
  are nonnegative. Thus, every such integral, including self-pairings
  and unequal chain lengths, is nonnegative. The pointwise $L^2$ convergence
  proved above identifies the full moment with their nonnegative sum.
  In particular, the moment of every finite partial-order sum is at most
  the full moment, even though samplewise partial sums need not increase.

  From the current author version
  \cite{chen:author2026:time-dependency}*{(2.23)--(2.24), p.~13},
  the actual common noise regularization has covariance
  $\gamma_\delta^0(s-r)\Gamma_\epsilon(y-z)$, where
  \[
    0\le\gamma_\delta^0(t)
    =\Gamma(\alpha_0)^{-1}\int_0^{\delta^{-1}}
    e^{-q|t|}q^{\alpha_0-1}\ud q
    \le |t|^{-\alpha_0}.
  \]
  Here $\Gamma(\alpha_0)$ is the Euler Gamma function.
  At fixed positive $\epsilon,\delta$, first take the source's Green-width
  limit. The bounded continuous covariances, weak convergence of the
  positive Green measures and the dominated finite Wick calculation in
  Lemma~\ref{L:terminal-wick} identify its classical measure-kernel
  Duhamel terms. For the source's continuous field modification, these
  Bochner terms equal the pathwise smoothed integrals: writing $\Phi_n$
  for the product of field values, the Gaussian bound in that lemma gives
  $\int\|\Phi_n\|_2\ud\mathsf g_n^{T,x}<\infty$.
  Tonelli gives pathwise integrability and Minkowski puts the integral
  in $L^2$. Fubini against every $L^2$ test variable and Bochner duality
  identify the two versions. The same argument applies before the
  Green-width limit in dimension three.

  Write $U_N^{\epsilon,\delta}$ for the sum of source terms of orders
  $0,\ldots,N$ after that Green limit. Write $V_{N,J}^\epsilon$ for the
  same partial-order sum of the finite interval model. Both moments are
  finite sums over exactly the same terminal-chain kernels and pairings;
  only the covariance factors differ. By~\eqref{E:dyadic-time-majorant}
  each source covariance factor is bounded by its $K_\infty$ counterpart.
  Since $K_J\uparrow K_\infty$, nonnegative Tonelli at fixed $N$ yields
  \begin{equation}\label{E:interval-source-comparison}
    \E|U_N^{\epsilon,\delta}(T,x)|^2
    \le\lim_{J\to\infty}\E|V_{N,J}^\epsilon(T,x)|^2
    \le\sup_J\E|u_{J,\epsilon}(T,x)|^2\le B(T),
  \end{equation}
  where $B(T)$ is the right side of~\eqref{E:full-upper-bound}.
  The middle inequality uses the positive pairing sum just identified.
  No Gaussian field of covariance $K_\infty\Gamma_\epsilon$ is constructed;
  $K_\infty$ is used only inside these monotone limits of positive integrals.
  This is entrywise comparison of Wick integrals, not covariance order
  for arbitrary initial phases or a coupling of random solutions.

  The same finite-model argument works after multiplying the source
  noise by any real amplitude $a>0$. This replaces $\Gamma$ by
  $a^2\Gamma$ and $R_\alpha$ by $a^2R_\alpha$, without changing its
  homogeneity degree or any parameter-only constant. Thus,
  \begin{equation}\label{E:regularized-scaled-moment}
    \E|u^{\epsilon,\delta}(a;T,x)|^2
    \le B(T;a):=e(T+2)^d
    \exp\{C(a^2R_\alpha)^{1/\nu}T^\kappa\}.
  \end{equation}
  Here the full regularized series exists by
  Lemma~\ref{L:terminal-wick}; it is the ordinary Duhamel series with
  its order-$n$ term multiplied by $a^n$. Taking the finite partial-order
  cutoff to infinity in~\eqref{E:interval-source-comparison} is justified
  at positive regularization by that lemma, not by a theorem about the
  original unsmoothed solution.

  Lemma~\ref{L:joint-fixed-order} supplies the fixed-order construction:
  each $Y_n^{\epsilon,\delta}$ converges in $L^2$ to $X_n=S_n(g_n)$
  as $\epsilon,\delta\downarrow0$, with arbitrary relative rates.
  The bounded-noise Green limit and ordered-kernel convention needed
  to match these terms are already verified in
  Lemma~\ref{L:terminal-wick}.

  Apply Lemma~\ref{L:uniform-series-tail} with $r=2$ and
  $B_r=B(T;2)$. It proves absolute $L^2$ convergence of the series
  defining $u$ in~\eqref{E:expansion} and convergence of the full
  regularized solution to that series. Taking the limit in
  \eqref{E:regularized-scaled-moment} at $a=1$ proves the required bound.
  This series-limit argument is independent of
  Proposition~\ref{P:mixed}, Lemma~\ref{L:crude-corrected}, and the
  source's Section~5 convergence proof. No first-moment asymptotic or
  printed normalization is used. The fixed-order construction just used is proved here from the
  universal pairing bound and the homogeneous norm estimates; neither
  the source's Theorem~4.1 nor its Lemma~4.4 is imported.
  Proposition~\ref{P:mild-construction} separately proves that this
  same series satisfies the source's Definition~2.1: its onefold
  Stratonovich integral equals $u-1$. That construction uses the
  corrected mixed-vertex crude bound for its product and order limits.
  This is a separate dependency from the sharp-scale moment estimate
  just proved; the source's Section~5(ii) proof is not imported.
  The crude constants used for this identification may depend on the
  fixed covariance; they do not enter~\eqref{E:full-upper-bound}.
  No uniqueness assertion is made.

  \emph{Cutoff dependence and the order of limits.}
  The preceding argument uses the following distinct statements.
  \begin{enumerate}[(i)]
    \item At fixed total order $2k$, the coefficient estimates are uniform
      in the Gaussian-mode and spatial-band cutoffs, in the finite interval
      family, and in positive spatial smoothing. The local Hermite cutoff
      $N_i=2k_i$ preserves each selected coefficient exactly; it is an
      algebraic choice, not a degree limit. Lemma~\ref{L:fixed-split} and
      the inventory bound contain no smoothing-dependent variance.
    \item At fixed finite interval family and $\epsilon>0$, mode and band
      limits identify these coefficients with the actual Duhamel words.
      The entire-series majorant in Proposition~\ref{P:interval-coefficients}
      may depend on this family and $\epsilon$, through $v_{\max}$.
      It is used for identification, not as a uniform moment estimate.
      The uniform coefficient bound passes to these limits. Localization
      and positive covariance comparison are applied only after removing
      these cutoffs; positivity of a finite-mode covariance is not assumed.
    \item For the resulting finite-depth interval model, the moment bound
      is uniform in $J,\epsilon$. Fix positive source widths
      $\epsilon,\delta$ and finite partial order $N$. The Green-width limit
      is taken first. The subsequent $J\to\infty$ comparison in
      \eqref{E:interval-source-comparison} is monotone convergence of finite
      positive Wick integrals. At these fixed noise widths,
      $N\to\infty$ is justified by Lemma~\ref{L:terminal-wick}, yielding
      \eqref{E:regularized-scaled-moment}. There is no infinite-depth
      Gaussian field or simultaneous mode-depth limit in this step.
    \item At each fixed $T,x,\Gamma$ and order $n$,
      Lemma~\ref{L:joint-fixed-order} gives qualitative $L^2$ convergence as
      $\epsilon,\delta\downarrow0$, with arbitrary relative rates.
      The bound $B(T;2)$ gives tails uniform in these two widths.
      Lemma~\ref{L:uniform-series-tail} first uses their limit at fixed
      partial order, then sends that order to infinity. The final moment
      bound comes from $B(T;1)$, not the larger tail bound $B(T;2)$.
    \item All identifications above are for fixed $T,x,\Gamma$; no
      convergence rate uniform in $T$ or over covariance shapes is claimed.
      They prove~\eqref{E:full-upper-bound} for every fixed $T\ge1$ with
      the same parameter-only constant. Only after this estimate is proved
      is $T\to\infty$ used for the growth-rate conclusion.
  \end{enumerate}
  The constants come from $L=78$, $c=6^{\alpha_0}$ and the parameter-only
  constants of Proposition~\ref{P:interval-coefficients}; covariance enters
  only through $R_\alpha$.
  The volume ratio is $|B_{T+2}|/|B_1|=(T+2)^d$.
  This proves Theorem~\ref{T:full-upper}.
\end{proof}

\begin{remark}[Claim and calibration boundary]\label{R:full-upper-boundary}
  Theorem~\ref{T:full-upper} asserts a nonsharp upper growth rate.
  It does not identify the sharp constant or require a correction of the
  printed first-moment normalization as an input.
  Its exponent tends to $(4-\alpha)/(3-\alpha)$ as $\alpha_0\downarrow0$.
  Cauchy--Schwarz and the unconditional Jensen inequality remain compatible
  with the nonsharp upper constant; any numeric $L_*$ calibration retains
  the source-normalization qualification stated earlier.
  The Skorohod exponent is compared, not used to identify constants:
  both Gaussian creation and annihilation were retained here.
  The intrinsic identification in Goal~\ref{G:sharp} is proved later in
  Theorem~\ref{T:intrinsic-second-moment}, using a separate argument.
\end{remark}


\section{A static lower comparison and a near-static mean gap}
\label{S:near-static-lower}

The comparison in this section does not identify the intrinsic constant of
Theorem~\ref{T:intrinsic-second-moment}; no novelty or numerical
normalization is claimed.

Fix a nonzero spatial covariance in Hypothesis~\ref{H:homog}, and put
\[
  \begin{gathered}
    \nu=3-\alpha>1,\qquad a_{\max}=\min(1,2-\alpha),\qquad
    \beta(a)=4-\alpha-a,\\
    \kappa(a)=\frac{\beta(a)}\nu,\qquad
    \kappa_{\rm st}=\frac{4-\alpha}\nu.
  \end{gathered}
\]
Here the temporal exponent varies: $u^{(a)}$ denotes our canonical solution
with covariance $|s-r|^{-a}\Gamma$, for $0<a<a_{\max}$.
At $a=0$ define $u^{(0)}=U$ to be the static canonical solution with the
same spatial covariance and initial data $(1,0)$. This endpoint means the
temporal covariance one, not a substitution into $\Gamma_{\mathrm E}(a)$.
The notation $\gamma_{\delta,a}^0$ records the temporal exponent $a$
in the same Laplace-prefix regularization previously denoted by
$\gamma_\delta^0$.

\paragraph{Imported static input.}
From Chen--Hu~\cite{chen.hu:25:hyperbolic}*{Theorem~1.2, (1.9), p.~2147},
the actual static first-mean rate $L_0$ exists and
\begin{equation}\label{E:static-ratio-input}
  0<L_0:=\lim_{t\to\infty}t^{-\kappa_{\rm st}}\log\E U(t,x)<\infty,
  \qquad
  \lim_{t\to\infty}t^{-\kappa_{\rm st}}\log\E U(t,x)^2
  =2^{\kappa_{\rm st}}L_0.
\end{equation}
We use only the common $p^{\kappa_{\rm st}}$ factor for $p=1,2$;
no numerical value of the static variational constant or its white-noise
specialization is adopted. Strict positivity in that formula follows by
using a nonzero Gaussian competitor: its interaction and gradient terms
scale as $A c^{\alpha/2}$ and $B c^2$, with $A,B>0$, so their difference
is positive for small $c$. Finiteness and the moment law are the imported
source result. The static kernel and integral conventions are its
(2.10)--(2.14), p.~2150; the fixed-order limits agree with its
Theorem~3.8(i), p.~2165. We supply the static series convergence needed
below from our regularized fractional-time upper bound, without using
the source's quantitative (4.3). The generalized-covariance convention is explicit
in its (2.18), p.~2152. Our spectral ball law gives
\[
  \int\frac{\mu(\ud\xi)}{1+|\xi|^2}
  \le\mu(B_1)+C_\alpha\mu(B_1)\sum_{j\ge0}2^{j(\alpha-2)}<\infty.
\]
Thus the static Dalang condition holds in every admissible dimension.
Measure homogeneity of degree $d-\alpha$ is equivalent to distributional
homogeneity of degree $-\alpha$, so the source's (1.8) applies in its
explicit generalized-covariance convention. The static object is identified
by its canonical heat-limit expansion; no uniqueness assertion for other
mild solutions is used.

For $a>0$ write $X_n^{(a)}$ for our fixed-order terms; at zero use the
corresponding static terms. Set
\[
  m_k(a)=\E X_{2k}^{(a)}(1,0),\qquad m_0(a)=1.
\]

\begin{lemma}[Raw-power mean coefficients]\label{L:mean-coefficient-holder}
  For every $0\le a<a_{\max}$, the coefficients $m_k(a)$ are nonnegative,
  and
  \begin{equation}\label{E:mean-positive-series}
    \E u^{(a)}(t,x)=\sum_{k\ge0}m_k(a)t^{\beta(a)k}.
  \end{equation}
  The series $F_a(z)=\sum_{k\ge0}m_k(a)z^k$ is finite for every $z\ge0$.
  If $0<a<b<a_{\max}$, then
  \begin{equation}\label{E:mean-coefficient-holder}
    m_k(a)\le m_k(0)^{1-a/b}m_k(b)^{a/b},\qquad k\ge1.
  \end{equation}
\end{lemma}

\begin{proof}
  We first justify the static endpoint and its norm series.
  At positive spatial widths its ordered terms are the bounded-variance
  Gaussian Bochner integrals of Lemma~\ref{L:terminal-wick}, with a
  time-constant field. Lemma~\ref{L:spatial-wick-measures}, applied with
  temporal multiplier one to the diagonal and mixed-width second
  moments, gives a common finite diagram limit. The same Hilbert
  Cauchy argument as in Lemma~\ref{L:joint-fixed-order} therefore gives
  the static fixed-order limits $X_n^{(0)}$, with the source's heat-limit
  convention. This uses no infinite solution series.

  Fix any $b_0\in(0,a_{\max})$ and $\delta_0>0$, and put
  $c=\gamma_{\delta_0,b_0}^0(1)>0$.
  Let $U_N^\epsilon(r;1,x)$ be the static partial series at horizon one
  and noise amplitude $r>1$. Compare its finite Wick sum with that of
  the fractional-time partial series at widths $\epsilon,\delta_0$,
  exponent $b_0$ and amplitude $r/\sqrt c$.
  Since $\gamma_{\delta_0,b_0}^0(s-r')\ge c$ for $s,r'\in[0,1]$,
  every pair factor on the second side dominates the static pair factor.
  Positivity, then the full regularized bound
  \eqref{E:regularized-scaled-moment}, gives
  \[
    \E|U_N^\epsilon(r;1,x)|^2
    \le \E|u^{\epsilon,\delta_0}_{b_0}(r/\sqrt c;1,x)|^2
    \le B_{b_0}(1;r/\sqrt c)<\infty,
  \]
  uniformly in $N,\epsilon$. The notation $B_{b_0}$ means the bound
  in~\eqref{E:regularized-scaled-moment} at temporal exponent $b_0$.
  Both positive-width full series exist by Lemma~\ref{L:terminal-wick}.
  Letting $N\to\infty$ at fixed $\epsilon$ preserves this bound.
  Lemma~\ref{L:uniform-series-tail} now applies to the static family
  (with only the spatial width varying). It proves absolute $L^2$
  convergence of its limiting series at horizon one, with geometric
  coefficient bounds for every $r>1$.
  Static fixed-order homogeneity gives
  \[
    \|X_n^{(0)}(t,x)\|_2
    =t^{(4-\alpha)n/2}\|X_n^{(0)}(1,0)\|_2.
  \]
  Choosing $r>\max\{1,t^{(4-\alpha)/2}\}$ in those bounds proves
  norm summability at every fixed $t>0$. The resulting series has
  precisely the source's canonical static kernels and fixed-order limits.


  For a single chain of length $2k$, use the initial-chain variables of
  Proposition~\ref{P:mixed}. At common positive spatial width $\epsilon$,
  let $\omega_{\epsilon,D}$ be its finite positive spatial Green--Wick
  measure on the unit time simplex, with covariance $\gamma_{2\epsilon}$
  on every pair. It is finite because that covariance is bounded and
  the Green masses are the time gaps. Define
  \[
    m_k^\epsilon(a)=\sum_{D\in\Pi_k}\int
    \prod_{\{j,h\}\in D}|s_j-s_h|^{-a}\ud\omega_{\epsilon,D},
    \qquad 0\le a<a_{\max}.
  \]
  These raw-time integrals are finite. At fixed $\epsilon$ the spatial
  factors and Green masses are bounded on the finite horizon; the
  disjoint pair endpoints give integrable powers on the full time cube
  since $a<1$. Diagonals are null there. On the disjoint union of the
  pairing measures, the time multiplier at $a$ is exactly the $a/b$ power
  of its multiplier at $b$. H\"older's inequality therefore gives
  \[
    m_k^\epsilon(a)\le
    m_k^\epsilon(0)^{1-a/b}m_k^\epsilon(b)^{a/b}.
  \]
  This is a raw-power identity; no exponent-dependent Laplace cutoff or
  Euler Gamma normalization is being interpolated.

  We justify removal of the common spatial width. For each positive
  exponent, the proof of Lemma~\ref{L:joint-fixed-order} gives this
  raw-time limit as well. Indeed, writing $F_{\epsilon,\eta,D}$ for
  the diagram with common temporal cutoff $\eta$,
  \eqref{E:joint-temporal-tail} gives
  \[
    F_{\epsilon,\eta,D}\le F_{\epsilon,0,D}
    \le F_{\epsilon,\eta,D}+r_a(\eta),\qquad r_a(\eta)\longrightarrow0,
  \]
  uniformly in $\epsilon$. First pass to the spatial limit at fixed
  $\eta$, then send $\eta$ to zero. The resulting limit is exactly
  the joint diagram value from that lemma. At zero exponent the
  multiplier is one, so Lemma~\ref{L:spatial-wick-measures} gives the
  spatial limit directly; the positive-width Wick calculation and
  the imported static fixed-order convergence identify it with the
  static expectation. Thus, $m_k^\epsilon(a)\to m_k(a)$ at all three
  fixed exponents $0,a,b$, proving~\eqref{E:mean-coefficient-holder}
  and nonnegativity. No convergence uniform in $a$ is claimed.

  Scaling all times and spatial displacements by $t$ in a regularized
  one-chain diagram gives the factor
  $t^{2(2k)-\alpha k-ak}=t^{\beta(a)k}$ and changes the spatial width
  to $\epsilon/t^2$. Passing to the just established limits proves
  $\E X_{2k}^{(a)}(t,x)=t^{\beta(a)k}m_k(a)$.
  Odd expectations vanish by Wick's formula. For positive $a$ the
  independently proved norm summability in Lemma~\ref{L:vertex-crude}
  justifies the mean-series interchange. At zero the static norm series
  just proved does so, with nonnegative even means. This proves
  \eqref{E:mean-positive-series}. Since $\beta(a)>0$, every $z\ge0$
  equals $t^{\beta(a)}$ for some $t\ge0$, and the series is finite.
  This proves Lemma~\ref{L:mean-coefficient-holder}.
\end{proof}

\begin{lemma}[Type of a positive coefficient series]\label{L:positive-series-type}
  Let $\nu\ge1$, $c_k\ge0$, $c_0=1$, and suppose
  $F(z)=\sum_{k\ge0}c_kz^k<\infty$ for every $z\ge0$. If
  \[
    \tau=\limsup_{z\to\infty}z^{-1/\nu}\log F(z)<\infty,
  \]
  then
  \begin{equation}\label{E:positive-series-type}
    K:=\limsup_{k\to\infty}\big((k!)^\nu c_k\big)^{1/k}<\infty,
    \qquad \tau=\nu K^{1/\nu}.
  \end{equation}
  Conversely, finite $K$ implies the same finite $\tau$ and equality.
\end{lemma}

\begin{proof}
  If $\tau<\infty$, choose $L>\tau$. Since $c_0=1$, $\tau\ge0$,
  and continuity of the power series on compact positive intervals gives
  $F(z)\le C_L e^{Lz^{1/\nu}}$ for all $z\ge0$.
  For $k\ge1$, the inequality $c_kz^k\le F(z)$ at
  $z=(\nu k/L)^\nu$ yields
  \[
    c_k\le C_L e^{\nu k}\left(\frac L{\nu k}\right)^{\nu k}.
  \]
  Monotonicity of $\log x$ and integration on $[1,k]$ give
  \[
    k\log k-k+1\le\log(k!)
    \le k\log k-k+1+\log k.
  \]
  Consequently $K\le(L/\nu)^\nu$. Letting $L\downarrow\tau$ proves
  $K\le(\tau/\nu)^\nu$, including $K=0$ when $\tau=0$.

  Conversely, for any $A>K$ all sufficiently large coefficients obey
  $c_k\le A^k/(k!)^\nu$. Hence, for a polynomial $P$ with nonnegative
  coefficients,
  \[
    F(z)\le P(z)+\sum_{k\ge0}\frac{(Az)^k}{(k!)^\nu}
    \le P(z)+\exp\{\nu(Az)^{1/\nu}\}.
  \]
  The last inequality is the elementary $\ell^\nu$ bound
  $\sum a_k^\nu\le(\sum a_k)^\nu$, applied to
  $a_k=(Az)^{k/\nu}/k!$. The polynomial contributes zero to the
  normalized logarithmic growth. Therefore $\tau\le\nu A^{1/\nu}$;
  let $A\downarrow K$. Combining both inequalities proves the equality
  when either quantity is finite. This proves Lemma~\ref{L:positive-series-type}.
\end{proof}

\begin{proposition}[Static temporal-minimum comparison]\label{P:static-minorant-lower}
  For every $0<a<a_{\max}$, $T>0$ and $p\in\{1,2\}$,
  \begin{equation}\label{E:static-minorant-moment}
    \E[u^{(a)}(T,x)^p]
    \ge\E\left[U\left(T^{1-a/(4-\alpha)},x\right)^p\right].
  \end{equation}
  In particular,
  \begin{equation}\label{E:static-minorant-rate}
    \liminf_{T\to\infty}T^{-\kappa(a)}\log\E[u^{(a)}(T,x)^p]
    \ge p^{\kappa_{\rm st}}L_0,\qquad p=1,2.
  \end{equation}
\end{proposition}

\begin{proof}
  Fix positive common spatial and temporal noise widths $\epsilon,\delta$.
  On $[0,T]$, the source's Laplace-prefix temporal covariance satisfies
  \[
    \gamma_{\delta,a}^0(s-r)\ge c_{\delta,T}:=
    \gamma_{\delta,a}^0(T)>0,\qquad
    c_{\delta,T}\longrightarrow T^{-a}\quad(\delta\downarrow0).
  \]
  Compare the order-$N$ partial series of $u^{(a)}$ with the same partial
  series of a static model having covariance
  $c_{\delta,T}\gamma_{2\epsilon}$.
  At positive widths, the mean or squared moment is a finite Wick sum
  of the same terminal Green kernels and pairings. Every spatial factor
  is the same nonnegative $\gamma_{2\epsilon}$; every time factor on
  the first side is at least $c_{\delta,T}$. Thus, the finite expected
  powers are ordered for $p=1,2$. For $d=3$, remove Green smoothing
  first at these fixed positive noise widths using the bounded covariance
  calculation preceding Lemma~\ref{L:spatial-wick-measures}.

  Now send $(\epsilon,\delta)$ jointly to zero at fixed $N$.
  Lemma~\ref{L:joint-fixed-order} gives the fractional-time $L^2$ limits.
  Static fixed-order $L^2$ convergence gives all static split products
  in $L^1$, by Cauchy--Schwarz. Dependence on $c_{\delta,T}$ is a
  finite polynomial at fixed order, so its limit is the static model
  with noise amplitude $\sigma=T^{-a/2}$. This requires no uniform
  approximation in $T$ or in a varying infinite-order series.
  At every fixed $\sigma,T>0$, static norm homogeneity gives
  \[
    \sigma^n\|X_n^{(0)}(T,x)\|_2
    =\|X_n^{(0)}(\sigma^{2/(4-\alpha)}T,x)\|_2.
  \]
  Thus the amplitude-scaled static norm series is summable at the
  effective time already covered by Lemma~\ref{L:mean-coefficient-holder}.
  Finally let $N\to\infty$ using the two $L^2$ expansions, with the
  static one supplied in Lemma~\ref{L:mean-coefficient-holder}. Means and
  squared moments converge, preserving the finite-order inequality.
  No covariance-order coupling of the two Gaussian fields is asserted.

  Write $U_\sigma$ for the static solution with noise amplitude $\sigma$.
  In its $p$th moment, a total order $2k$ has amplitude factor
  $\sigma^{2k}$ and, by static diagram homogeneity, time factor
  $T^{(4-\alpha)k}$. For $p=1,2$, the finite sums and then the
  convergent nonnegative moment series therefore give the exact identity
  \[
    \E[U_\sigma(T,x)^p]
    =\E[U(\sigma^{2/(4-\alpha)}T,x)^p].
  \]
  Only moments are identified; no spatially indexed random fields are
  coupled. At $\sigma=T^{-a/2}$ this proves
  \eqref{E:static-minorant-moment}. The effective static time tends to
  infinity and
  \[
    \left(T^{1-a/(4-\alpha)}\right)^{\kappa_{\rm st}}
    =T^{\kappa(a)}.
  \]
  The imported static rates~\eqref{E:static-ratio-input} now prove
  \eqref{E:static-minorant-rate}.
  This proves Proposition~\ref{P:static-minorant-lower}.
\end{proof}

\begin{proposition}[Near-static strict gap from the actual mean rate]
  \label{P:near-static-mean-gap}
  Define
  \[
    M(a)=\limsup_{T\to\infty}T^{-\kappa(a)}\log\E u^{(a)}(T,x),\qquad
    K(a)=\limsup_{k\to\infty}\big((k!)^\nu m_k(a)\big)^{1/k}.
  \]
  Then $K(0)=(L_0/\nu)^\nu>0$, and $K(b)<\infty$ for every
  $0<b<a_{\max}$. Fix such a $b$ and choose any finite
  $B_b\ge\max\{2K(0),K(b)\}$. For $0<a<b$,
  \begin{equation}\label{E:near-static-mean-upper}
    M(a)\le L_0\left(\frac{B_b}{K(0)}\right)^{a/(b\nu)}.
  \end{equation}
  In particular, with
  \begin{equation}\label{E:near-static-window}
    a_*:=\frac{b\log2}{\log(B_b/K(0))}\in(0,b],
  \end{equation}
  every $0<a<a_*$ satisfies
  \begin{equation}\label{E:near-static-mean-gap}
    \liminf_{T\to\infty}T^{-\kappa(a)}\log\E[u^{(a)}(T,x)^2]
    >2M(a).
  \end{equation}
\end{proposition}

\begin{proof}
  By Lemma~\ref{L:mean-coefficient-holder}, the substitution
  $z=T^{\beta(a)}$ identifies the normalized logarithmic type of
  $F_a(z)$ with the mean limsup $M(a)$; at zero it equals $L_0$.
  The imported static law and Lemma~\ref{L:positive-series-type} give
  $K(0)=(L_0/\nu)^\nu$.
  For positive $b$, Cauchy--Schwarz and Theorem~\ref{T:full-upper},
  applied at temporal exponent $b$, give $M(b)<\infty$.
  The same type lemma therefore gives $K(b)<\infty$.
  There is no use of a printed first-moment rate constant.

  Multiplying~\eqref{E:mean-coefficient-holder} by $(k!)^\nu$,
  taking $k$th roots and then limsups yields
  \[
    K(a)\le K(0)^{1-a/b}B_b^{a/b}.
  \]
  To justify this even if coefficients vanish, for any $\eta>0$ both
  endpoint root sequences are eventually bounded by $K(0)+\eta$ and
  $B_b+\eta$; take their weighted product and then let $\eta\downarrow0$.
  Lemma~\ref{L:positive-series-type} now gives
  \[
    M(a)=\nu K(a)^{1/\nu}
    \le L_0\left(\frac{B_b}{K(0)}\right)^{a/(b\nu)},
  \]
  proving~\eqref{E:near-static-mean-upper}.
  Since $B_b/K(0)\ge2$, the window in~\eqref{E:near-static-window}
  is positive and at most $b$. For $0<a<a_*$,
  \[
    2M(a)<2L_0\cdot2^{1/\nu}
    =2^{\kappa_{\rm st}}L_0,
  \]
  because $\kappa_{\rm st}=1+1/\nu$.
  Combine this with Proposition~\ref{P:static-minorant-lower} at $p=2$.
  This proves Proposition~\ref{P:near-static-mean-gap}.
\end{proof}

\begin{remark}[Scope and calibrations]\label{R:near-static-scope}
  The static lower comparison holds at every admissible positive temporal
  exponent; the strict gap from twice the actual first-mean limsup is
  asserted only in the nonempty window~\eqref{E:near-static-window}.
  Its endpoint depends on the fixed covariance and the chosen anchor $b$;
  no uniformity over covariance shapes is claimed. As $a\downarrow0$,
  the comparison clock has exponent tending to one, the growth exponent
  tends to $\kappa_{\rm st}$, and the mean upper bound tends to $L_0$.
  The static second-moment constant is exactly $2^{\kappa_{\rm st}}L_0$.

  The gap concerns $\E u$, which is positive by its pairing series;
  no theorem for $\E|u|$ or all moment orders is asserted.
  If an intended source first-mean lower rate $L_*(a)$ is valid, then
  $L_*(a)\le M(a)$, so~\eqref{E:near-static-mean-gap} also improves
  the corresponding Jensen rate $2L_*(a)$ in this window.
  This does not establish the original lower target
  $2^{\kappa_{\rm st}}L_*(a)$, or either sharp bound for arbitrary $a$.
  The later intrinsic formula in Theorem~\ref{T:intrinsic-second-moment}
  does not identify either printed source endpoint. The proof here uses the ordinary
  Stratonovich pairing expansion, including self-contractions; no
  Skorohod result or sibling-project development is made.
\end{remark}


\subsection{Temporal interpolation of the full moment}
\label{S:temporal-type-continuity}

The constant at a fixed positive temporal exponent is identified later in
Theorem~\ref{T:intrinsic-second-moment}.

Retain the fixed nonzero covariance and the notation of this section.
For \(p=1,2\), set \(c_{p,0}(a)=1\) and, for \(k\ge1\),
\begin{equation}\label{E:full-moment-coefficients}
  c_{1,k}(a)=m_k(a),\qquad
  c_{2,k}(a)=\sum_{m=0}^{2k}
  \E[X_m^{(a)}(1,0)X_{2k-m}^{(a)}(1,0)].
\end{equation}
The zero-exponent terms are the static limits constructed in
Lemma~\ref{L:mean-coefficient-holder}.

\begin{lemma}[Interpolation of the full moment coefficients]
  \label{L:full-moment-coefficient-holder}
  For \(0\le a<a_{\max}\) and \(p=1,2\), the coefficients are nonnegative and
  \begin{equation}\label{E:full-moment-positive-series}
    \E[u^{(a)}(t,x)^p]
    =\sum_{k\ge0}c_{p,k}(a)t^{\beta(a)k}<\infty,\qquad t>0.
  \end{equation}
  If \(0\le a_1<a<a_2<a_{\max}\) and
  \(\theta=(a-a_1)/(a_2-a_1)\), then
  \begin{equation}\label{E:full-moment-coefficient-holder}
    c_{p,k}(a)\le
    c_{p,k}(a_1)^{1-\theta}c_{p,k}(a_2)^\theta,\qquad k\ge0.
  \end{equation}
\end{lemma}

\begin{proof}
  Work first at a common positive spatial noise width \(\epsilon\) and
  at unit horizon. For each split \(m+n=2k\) and pairing \(D\), let
  \(\omega_{\epsilon,m,n,D}\) be the finite positive spatial
  Green--Wick measure in the initial-chain convention of
  Proposition~\ref{P:mixed}, with covariance \(\gamma_{2\epsilon}\).
  For \(p=1\) take the disjoint union over the single specified split
  \((m,n)=(0,2k)\) and all pairings. For \(p=2\), take the disjoint union
  over every \(m=0,\ldots,2k\) and all pairings. In particular, the two
  empty-chain orientations are distinct terms for \(p=2\), whereas
  \(p=1\) has just one. Wick's formula has coefficient one for each
  pairing on each ordered domain.

  With \(\omega_{\epsilon,p,k}\) denoting this disjoint-union measure,
  define its raw-time integral by
  \[
    c_{p,k}^{\epsilon}(a)=
    \int \prod_{\{j,h\}\in D}|s_j-s_h|^{-a}
    \ud\omega_{\epsilon,p,k}.
  \]
  The pairing label in the multiplier is that of its component.
  These integrals are finite: the spatial covariances and Green masses
  are bounded on the unit horizons, and the disjoint pair endpoints
  give integrable factors on the full time cube since \(a<1\).
  The multiplier at \(a\) is exactly the product of the endpoint
  multipliers to powers \(1-\theta,\theta\), off null diagonals.
  Hölder's inequality on the disjoint union gives
  \[
    c_{p,k}^{\epsilon}(a)\le
    c_{p,k}^{\epsilon}(a_1)^{1-\theta}
    c_{p,k}^{\epsilon}(a_2)^\theta.
  \]

  For each fixed positive endpoint, the all-chain bound
  \eqref{E:joint-temporal-tail} and the common temporal-cutoff sandwich
  used in Lemma~\ref{L:mean-coefficient-holder} identify the raw-time
  spatial limit with the joint diagram value. This applies to every
  unequal or empty split, not only to a mean diagram. At exponent zero,
  the multiplier is one and Lemma~\ref{L:spatial-wick-measures} gives
  the same limit. The static diagonal and mixed-width Gaussian limits
  identify those diagram values with the split expectations of the
  constructed static terms: products converge in \(L^1\) by
  Cauchy--Schwarz, and the terminal-to-initial chain reversal is the one
  in Proposition~\ref{P:mixed}, applied before removing widths.
  For positive exponents this identification
  is Proposition~\ref{P:mixed}. The union is finite at fixed \(k\);
  passing to the spatial limit proves
  \eqref{E:full-moment-coefficient-holder} and nonnegativity.
  No interpolation of exponent-dependent Laplace prefixes is used.

  Every diagram has \(2k\) time Jacobians, \(2k\) Green scaling factors,
  \(k\) spatial covariance factors and \(k\) temporal factors.
  Thus its homogeneous time degree is
  \(4k-\alpha k-ak=\beta(a)k\), including both empty-chain cases.
  For positive \(a\), the full second-moment series follows from
  Proposition~\ref{P:mixed}; the mean series is
  \eqref{E:mean-positive-series}. At zero, the static norm series gives
  convergence of the finite partial means and squared moments. Each
  finite moment expansion has nonnegative mixed terms, so its increasing
  limit may be regrouped by total order \(2k\). The homogeneity just
  proved then gives~\eqref{E:full-moment-positive-series}.
  This proves Lemma~\ref{L:full-moment-coefficient-holder}.
\end{proof}

For \(p=1,2\) define the actual normalized time growth rates
\begin{equation}\label{E:moment-growth-types}
  \begin{split}
    \overline\Lambda_p(a)&=\limsup_{T\to\infty}
    T^{-\kappa(a)}\log\E[u^{(a)}(T,x)^p],\\
    \underline\Lambda_p(a)&=\liminf_{T\to\infty}
    T^{-\kappa(a)}\log\E[u^{(a)}(T,x)^p].
  \end{split}
\end{equation}
Here \(p=1\) concerns \(\E u\), not \(\E|u|\).

\begin{proposition}[Log-convexity of the upper growth type]
  \label{P:moment-growth-logconvex}
  The functions \(\overline\Lambda_p(a)\), \(p=1,2\), are positive and
  finite on \(0\le a<a_{\max}\). For the endpoints and \(\theta\)
  in Lemma~\ref{L:full-moment-coefficient-holder},
  \begin{equation}\label{E:moment-growth-logconvex}
    \overline\Lambda_p(a)\le
    \overline\Lambda_p(a_1)^{1-\theta}
    \overline\Lambda_p(a_2)^\theta .
  \end{equation}
  In particular, \(\log\overline\Lambda_p\) is convex and
  \(\overline\Lambda_p\) is continuous on \((0,a_{\max})\).
\end{proposition}

\begin{proof}
  Put \(C_p=p^{\kappa_{\rm st}}L_0>0\).
  The imported static law gives
  \(\overline\Lambda_p(0)=\underline\Lambda_p(0)=C_p\).
  Proposition~\ref{P:static-minorant-lower} gives
  \(\underline\Lambda_p(a)\ge C_p\) for positive \(a\).
  The full upper bound gives finiteness for \(p=2\).
  Cauchy--Schwarz gives finiteness for \(p=1\), whose mean is at
  least one by its positive series. Hence all logarithms and rates
  used here are well defined, positive and finite.

  Let \(F_{p,a}(z)=\sum_{k\ge0}c_{p,k}(a)z^k\). It is finite for
  every \(z\ge0\), by Lemma~\ref{L:full-moment-coefficient-holder}.
  Its normalized logarithmic type equals
  \(\overline\Lambda_p(a)\): spatial stationarity makes the moment
  independent of \(x\), while \(z=T^{\beta(a)}\) and
  \(z^{1/\nu}=T^{\kappa(a)}\).
  Lemma~\ref{L:positive-series-type} therefore gives
  \[
    K_p(a):=\limsup_{k\to\infty}
    \big((k!)^\nu c_{p,k}(a)\big)^{1/k}
    =\left(\frac{\overline\Lambda_p(a)}{\nu}\right)^\nu.
  \]
  Multiplying the coefficient interpolation by \((k!)^\nu\),
  taking \(k\)th roots and then limsups gives
  \[
    K_p(a)\le K_p(a_1)^{1-\theta}K_p(a_2)^\theta.
  \]
  More explicitly, the two endpoint root sequences are eventually
  bounded by \(K_p(a_i)+\eta\); let \(\eta\downarrow0\) after taking
  their weighted product. This argument permits zero or oscillating
  coefficient subsequences. Taking the \(1/\nu\) power and multiplying
  by \(\nu\) proves~\eqref{E:moment-growth-logconvex}.

  For completeness, continuity follows directly from secant slopes.
  Write \(f=\log\overline\Lambda_p\). If
  \(L<l\le x<y\le r<R\) are in \((0,a_{\max})\), convexity gives
  \[
    \frac{f(l)-f(L)}{l-L}\le
    \frac{f(y)-f(x)}{y-x}\le
    \frac{f(R)-f(r)}{R-r}.
  \]
  Both outer slopes are finite. They bound the absolute difference
  quotient on each compact interior interval, proving continuity of
  \(f\), and hence of its exponential.
  This proves Proposition~\ref{P:moment-growth-logconvex}.
\end{proof}

\begin{corollary}[Recovery of the static moment constant]
  \label{C:static-moment-constant-continuity}
  Put \(C_p=p^{\kappa_{\rm st}}L_0\), \(p=1,2\).
  For every fixed \(0<b<a_{\max}\) and \(0<a<b\),
  \begin{equation}\label{E:static-constant-envelope}
    C_p\le\underline\Lambda_p(a)\le\overline\Lambda_p(a)
    \le C_p\left(\frac{\overline\Lambda_p(b)}{C_p}\right)^{a/b}.
  \end{equation}
  Consequently,
  \begin{equation}\label{E:static-constant-continuity}
    \lim_{a\downarrow0}\underline\Lambda_p(a)
    =\lim_{a\downarrow0}\overline\Lambda_p(a)=C_p,\qquad p=1,2,
  \end{equation}
  and
  \begin{equation}\label{E:static-moment-ratio-continuity}
    \lim_{a\downarrow0}
    \frac{\underline\Lambda_2(a)}{\overline\Lambda_1(a)}
    =2^{\kappa_{\rm st}}.
  \end{equation}
\end{corollary}

\begin{proof}
  The lower estimate is Proposition~\ref{P:static-minorant-lower}.
  For the upper estimate, apply Proposition~\ref{P:moment-growth-logconvex}
  with endpoints \(0,b\), using
  \(\overline\Lambda_p(0)=C_p\).
  This proves~\eqref{E:static-constant-envelope}.
  The finite ratio \(\overline\Lambda_p(b)/C_p\) is at least one.
  With \(b\) and the covariance fixed, its \(a/b\) power tends to one.
  Squeezing both rates proves~\eqref{E:static-constant-continuity}.
  The numerator and denominator in
  \eqref{E:static-moment-ratio-continuity} tend to
  \(2^{\kappa_{\rm st}}L_0\) and \(L_0>0\), respectively.
  Division gives the asserted ratio.
  This proves Corollary~\ref{C:static-moment-constant-continuity}.
\end{proof}

\begin{remark}[Order of limits and remaining sharp target]
  \label{R:temporal-type-scope}
  The static calibration now concerns the constant, not only the time
  exponent. It is an iterated statement: first take a time liminf or
  limsup at each fixed \(a\), with its own normalization
  \(T^{-\kappa(a)}\), and then send \(a\downarrow0\).
  No uniformity over covariances or \(T\), no simultaneous limit,
  and no existence of the time limit at a fixed positive \(a\) follows.
  Only the upper rate is asserted to be log-convex on the interior.

  Neither \(L_*(a)\) nor \(L^*(a)\) enters this argument.
  The constant \(L_0\) is the actual static first-mean rate.
  Parameter continuity alone does not identify the conjectured curve.
  The separate intrinsic second-moment value is proved in
  Theorem~\ref{T:intrinsic-second-moment}. No all-\(p\), absolute-first-moment,
  Skorohod, novelty or circulation result is claimed.
\end{remark}


\section{A small-order test for direct Brownian clock copying}
\label{S:two-clock-screen}

The result concerns a specified gap-transform substitution. It does not
rule out ordering corrections, a diagonal-only representation,
one-sided/asymptotic use, or the original sharp conjecture.

Theorem~6.1 of \cite{chen:author2026:time-dependency}*{pp.~37--42}
represents the time Laplace transform of a \emph{fixed-order} mean by a
spatial Brownian path and an independent scalar Brownian clock.
The proof uses nonnegative cut sums \(c_l\), obtained from one-chain time
order on p.~38, before the wave-to-heat substitution on p.~39.
Remark~6.3, p.~42, singles out that order as the obstruction for more copies.
We test the direct replacement by two spatial Brownian paths and two scalar
Brownian clocks, without an additional ordering weight.

All transforms below are at fixed total order. We begin with the original
admissible case \(d=\alpha=1\), \(\Gamma=\delta_0\), \(0<a<1\), and
\(G_s(y)=\frac12\mathbf1_{\{|y|<s\}}\).
This is a falsification case for an intended general representation,
not a restriction of Goal~\ref{G:sharp}.

\begin{lemma}[White-space low-order Laplace transforms]
  \label{L:white-clock-laplace}
  The \((1,1)\) cross-pair gap transform is
  \begin{equation}\label{E:white-cross-clock-transform}
    \begin{split}
      K_\times(\theta_1,\theta_2)
      &:=\int_0^\infty\int_0^\infty
      e^{-\theta_1s-\theta_2t}|s-t|^{-a}
      \frac{\min(s,t)}2\ud s\ud t\\
      &=\frac{\Gamma_{\mathrm E}(1-a)}
      {2(\theta_1+\theta_2)^2}
      \big(\theta_1^{a-1}+\theta_2^{a-1}\big),
      \qquad \theta_1,\theta_2>0.
    \end{split}
  \end{equation}
  In particular,
  \(K_\times(\theta,\theta)=
  \Gamma_{\mathrm E}(1-a)/(4\theta^{3-a})\).
  For the empty-plus-length-two self-pair, independent gap damping gives
  \begin{equation}\label{E:white-self-clock-transform}
    K_{\rm self}(\eta_1,\eta_2)
    :=\int_0^\infty\int_0^\infty
    e^{-\eta_1r_1-\eta_2r_2}r_2^{-a}\frac{r_1}2
    \ud r_1\ud r_2
    =\frac{\Gamma_{\mathrm E}(1-a)}
    {2\eta_1^2\eta_2^{1-a}}.
  \end{equation}
\end{lemma}

\begin{proof}
  The spatial cross factor is
  \[
    \int G_s(y)G_t(z)\delta_0(y-z)\ud y\ud z
    =\frac14\int\mathbf1_{\{|y|<s\wedge t\}}\ud y
    =\frac{\min(s,t)}2.
  \]
  Split its time integral into \(s=t+v\) and \(t=s+v\), with \(v>0\).
  Each part is one half the product of
  \[
    \int_0^\infty t e^{-(\theta_1+\theta_2)t}\ud t
    =(\theta_1+\theta_2)^{-2}
  \]
  and
  \(\int_0^\infty e^{-\theta_i v}v^{-a}\ud v
  =\Gamma_{\mathrm E}(1-a)\theta_i^{a-1}\).
  All integrands are nonnegative and finite since \(a<1\), so Tonelli
  justifies the separation. This proves
  \eqref{E:white-cross-clock-transform}.

  For one length-two chain, its delta covariance forces the two positions
  equal. The second Green factor is \(G_{r_2}(0)=1/2\), and integration
  of the first gives mass \(r_1\). The time difference is \(r_2\).
  The two elementary Laplace integrals therefore give
  \eqref{E:white-self-clock-transform}.
  This proves Lemma~\ref{L:white-clock-laplace}.
\end{proof}

The source's analytic time covariance is
\[
  \gamma_a^{\rm an}(z)
  =\big(z\,\operatorname{sgn}\Re z\big)^{-a},\qquad \Re z\ne0,
\]
with the power taken on the right half-plane. For \(r>0,v\ge0\), put
\begin{equation}\label{E:averaged-clock-kernel}
  \Psi_a(r,v)=\frac1{\Gamma_{\mathrm E}(a)}
  \int_0^\infty \lambda^{a-1}e^{-r\lambda-v\lambda^2/2}\ud\lambda.
\end{equation}
From the source's complex Laplace identity
\cite{chen:author2026:time-dependency}*{(6.3), p.~41},
and the Gaussian characteristic function,
\(\Psi_a(r,v)=\E(r+iZ)^{-a}\) when \(Z\) is centered normal with variance \(v\).
Fubini at fixed \(r>0\) is justified by
\(\int_0^\infty\lambda^{a-1}e^{-r\lambda}\ud\lambda<\infty\).
In particular, \(\Psi_a\) is nonnegative, decreases with \(v\), and
\(\Psi_a(r,v)\le r^{-a}\).

Return to an arbitrary nonzero covariance in Hypothesis~\ref{H:homog},
with temporal exponent \(a\), so \(0<a<1\), \(0<\alpha<2\) and
\(a+\alpha<2\). Define
\[
  h_\Gamma(w)=\int e^{-w|\xi|^2/2}\mu(\ud\xi)
  =(p_w*\Gamma)(0),\qquad
  \mathcal R_\Gamma(q)=\int\frac{\mu(\ud\xi)}{q^2+|\xi|^2}.
\]
Both are positive and finite for \(w,q>0\).
Spectral homogeneity gives \(h_\Gamma(w)=w^{-\alpha/2}h_\Gamma(1)\) and
\(\mathcal R_\Gamma(q)=q^{\alpha-2}\mathcal R_\Gamma(1)\).
The actual cross-pair gap transform at common damping is
\[
  K_\Gamma(\theta)=N_2(\theta)^2
\]
with temporal exponent \(a\) in~\eqref{E:damped-norm-definitions}.
This is the spatial-regularization limit of the \((1,1)\) diagram.

Let \(B_1,B_2\) be independent spatial standard Brownian motions.
For auxiliary standard Brownian clocks with
\(\E[\beta_1(u)\beta_2(v)]=\rho\min(u,v)\), \(-1\le\rho\le1\),
independent of the spatial paths, the clock difference has variance
\[
  v_\rho(u,v)=u+v-2\rho\min(u,v).
\]
At common damping \(\theta>0\), the direct unweighted, unrestricted
two-clock covariance substitution yields the averaged candidate
\begin{equation}\label{E:naive-clock-candidate}
  J_{\Gamma,\rho}(\theta)
  :=\frac14\int_0^\infty\int_0^\infty
  e^{-\theta^2(u+v)/2}h_\Gamma(u+v)
  \Psi_a(\theta|u-v|,v_\rho(u,v))\ud u\ud v .
\end{equation}
Values on \(u=v\) do not affect the integral.
The factor \(1/4\) is one factor \(1/2\) for each wave-to-heat gap
transform; \(h_\Gamma(u+v)\) is the spatial average of
\(\Gamma(B_1(u)-B_2(v))\).
This average is interpreted by spatial heat regularization.
For the white covariance it is \((2\pi(u+v))^{-1/2}\).
The analytic covariance, not its absolute-value bound, is being copied.

\begin{proposition}[Obstruction to unweighted constant-correlation clock copying]
  \label{P:clock-copy-obstruction}
  For every covariance and parameters just specified, put
  \begin{equation}\label{E:cross-clock-lambda-weight}
    w_\theta(\lambda)
    =\frac{\lambda^{a-2}}
    {2\theta\Gamma_{\mathrm E}(a)}
    \big(\mathcal R_\Gamma(\theta)
    -\mathcal R_\Gamma(\theta+\lambda)\big),\qquad\lambda>0.
  \end{equation}
  This is a positive integrable density, and
  \begin{equation}\label{E:clock-copy-obstruction}
    \begin{split}
      K_\Gamma(\theta)&=\int_0^\infty w_\theta(\lambda)\ud\lambda,\\
      0<J_{\Gamma,\rho}(\theta)
      &\le J_{\Gamma,1}(\theta)
      =\int_0^\infty
      \frac{2\theta}{2\theta+\lambda}w_\theta(\lambda)\ud\lambda
      <K_\Gamma(\theta).
    \end{split}
  \end{equation}
  When \(\alpha=1\),
  \begin{equation}\label{E:degree-one-clock-loss}
    J_{\Gamma,1}(\theta)=(2-2^a)K_\Gamma(\theta).
  \end{equation}
  Thus this direct analytic clock-copying family, including independent
  clocks and a single shared clock, fails to reproduce the cross-pair
  transform throughout the original nonzero covariance class.
\end{proposition}

\begin{proof}
  First evaluate the actual cross transform. Temporarily smooth the spatial
  covariance, so Fourier and time Fubini are absolute. For \(r=|\xi|\),
  direct integration over \(s=t+v\) and \(t=s+v\) gives
  \[
    \int_0^\infty\int_0^\infty
    e^{-\theta(s+t)-\lambda|s-t|}
    \widehat G_s(\xi)\overline{\widehat G_t(\xi)}\ud s\ud t
    =\frac{2\theta+\lambda}
    {2\theta(\theta^2+r^2)((\theta+\lambda)^2+r^2)} .
  \]
  For example, on the first cone the \(v\)-integral uses
  \[
    \int_0^\infty e^{-(\theta+\lambda)v}
    \sin(r(t+v))\ud v
    =\frac{(\theta+\lambda)\sin(rt)+r\cos(rt)}
    {(\theta+\lambda)^2+r^2}.
  \]
  Integrating the remaining sine-square and sine-cosine terms against
  \(e^{-2\theta t}\), and adding the second cone, gives the displayed
  identity. The value at \(r=0\) is its continuous limit.

  The resulting spectral integrand is nonnegative. Removing the spatial
  Gaussian multiplier and using the raw-time Laplace formula therefore gives
  \[
    \begin{split}
      K_\Gamma(\theta)
      &=\frac1{\Gamma_{\mathrm E}(a)}
      \int_0^\infty\lambda^{a-1}
      \frac{2\theta+\lambda}{2\theta}
      \int\frac{\mu(\ud\xi)}
      {(\theta^2+|\xi|^2)((\theta+\lambda)^2+|\xi|^2)}
      \ud\lambda\\
      &=\int_0^\infty w_\theta(\lambda)\ud\lambda.
    \end{split}
  \]
  The second equality is partial fractions, with
  \((\theta+\lambda)^2-\theta^2=\lambda(2\theta+\lambda)\).
  The smoothing passage is justified by monotone convergence in this
  nonnegative spectral expression and the finite quadratic form in
  Lemma~\ref{L:damped-homogeneous-norms}. Alternatively, homogeneity
  directly bounds the density near zero by a constant times
  \(\lambda^{a-1}\), and at infinity by a constant times
  \(\lambda^{a-2}\). Its strict positivity follows from
  \(\mathcal R_\Gamma(\theta)
  -\mathcal R_\Gamma(\theta+\lambda)>0\), since \(\mu\ne0\).

  The candidate integrals are well defined and positive.
  The bound \(\Psi_a(\theta|u-v|,v_\rho)\le
  (\theta|u-v|)^{-a}\), together with
  \(h_\Gamma(w)=h_\Gamma(1)w^{-\alpha/2}\), supplies an absolute
  majorant. With \(w=u+v\), \(q=u-v\), the Jacobian is \(1/2\) and
  \(-w<q<w\). It is a constant times
  \[
    \int_0^\infty e^{-\theta^2w/2}w^{-\alpha/2}
    \int_{-w}^w|q|^{-a}\ud q\ud w
    =\frac2{1-a}\int_0^\infty
    e^{-\theta^2w/2}w^{1-\alpha/2-a}\ud w<\infty .
  \]
  Here \(a<1\) and \(a+\alpha/2<2\).
  The same bound dominates the spatial heat-regularized averages, whose
  spatial factor is \(h_\Gamma(w+2\epsilon)\le h_\Gamma(w)\).
  This is an averaged spectral bound, not pointwise covariance monotonicity.
  Since \(v_\rho(u,v)\ge|u-v|=v_1(u,v)\), monotonicity of
  \(\Psi_a\) gives \(J_{\Gamma,\rho}\le J_{\Gamma,1}\).

  We compute the latter by nonnegative Tonelli. Write
  \(A=\theta\lambda+\lambda^2/2\). Integration in \(q\) gives
  \(2(1-e^{-Aw})/A\). Also
  \[
    \mathcal R_\Gamma(q)
    =\frac12\int_0^\infty e^{-q^2w/2}h_\Gamma(w)\ud w,
  \]
  by the elementary resolvent integral and spectral Tonelli.
  Consequently,
  \[
    \begin{split}
      J_{\Gamma,1}(\theta)
      &=\frac1{4\Gamma_{\mathrm E}(a)}
      \int_0^\infty\frac{\lambda^{a-1}}A
      \int_0^\infty h_\Gamma(w)
      \left(e^{-\theta^2w/2}
      -e^{-(\theta+\lambda)^2w/2}\right)\ud w\ud\lambda\\
      &=\frac1{\Gamma_{\mathrm E}(a)}
      \int_0^\infty
      \frac{\lambda^{a-2}
      (\mathcal R_\Gamma(\theta)-\mathcal R_\Gamma(\theta+\lambda))}
      {2\theta+\lambda}\ud\lambda\\
      &=\int_0^\infty
      \frac{2\theta}{2\theta+\lambda}w_\theta(\lambda)\ud\lambda.
    \end{split}
  \]
  The \(q\)-integral's factor two cancels its coordinate Jacobian
  \(1/2\); the resolvent identity supplies the other factor two.
  Since \(w_\theta>0\) and \(2\theta/(2\theta+\lambda)<1\) for
  every \(\lambda>0\), the strict inequality follows.

  Finally, if \(\alpha=1\), homogeneity gives
  \(\mathcal R_\Gamma(q)=\mathcal R_\Gamma(1)/q\).
  Substitution in the two densities gives
  \[
    \begin{split}
      K_\Gamma(\theta)
      &=\frac{\mathcal R_\Gamma(1)}
      {2\theta^2\Gamma_{\mathrm E}(a)}
      \int_0^\infty\frac{\lambda^{a-1}}{\theta+\lambda}\ud\lambda,\\
      J_{\Gamma,1}(\theta)
      &=\frac{\mathcal R_\Gamma(1)}
      {\theta^2\Gamma_{\mathrm E}(a)}
      \int_0^\infty\lambda^{a-1}
      \left(\frac1{\theta+\lambda}
      -\frac1{2\theta+\lambda}\right)\ud\lambda .
    \end{split}
  \]
  The real Beta identity
  \[
    \int_0^\infty\frac{x^{a-1}}{x+c}\ud x
    =c^{a-1}\Gamma_{\mathrm E}(a)\Gamma_{\mathrm E}(1-a),
    \qquad c>0,
  \]
  follows by scaling and
  \((r,s)\mapsto(r+s,r/s)\) in the positive product of the two
  Gamma integrals. Their finiteness uses \(0<a<1\).
  Evaluation of these two integrals gives
  \(J_{\Gamma,1}/K_\Gamma=2(1-2^{a-1})=2-2^a\), proving
  \eqref{E:degree-one-clock-loss}.
  This proves Proposition~\ref{P:clock-copy-obstruction}.
\end{proof}

\begin{remark}[Normalization and scope of the obstruction]
  \label{R:clock-copy-scope}
  At the static endpoint define the time covariance directly as one.
  The candidate with \(\Psi_0=1\) gives
  \[
    J_{\Gamma,\rho}(\theta)
    =\int\frac{\mu(\ud\xi)}{(\theta^2+|\xi|^2)^2}
    =K_\Gamma(\theta).
  \]
  This follows by integrating \(w e^{-\theta^2w/2}h_\Gamma(w)/4\)
  spectrally. In the white case it equals \(1/(4\theta^3)\).
  Thus static and homogeneous-degree checks alone miss the positive-\(a\)
  loss. Relative to the shared-clock value \(\rho=1\), the omitted
  cross-pair multiplier is exactly \(1+\lambda/(2\theta)\).
  For smaller correlations the deficit can be larger.
  This does not assert a correction rule at
  higher orders.

  The transforms \(K_\times\) use gap damping. For the auxiliary cutoff
  function
  \[
    F(T_1,T_2)=\int_0^{T_1}\int_0^{T_2}
    |s-t|^{-a}\frac{\min(s,t)}2\ud s\ud t,
  \]
  nonnegative Fubini adds \(1/(\theta_1\theta_2)\) to its double
  external-horizon transform. This function is not an actual unequal-time
  solution correlation. Reversing chains ending at different physical
  times instead shifts the cross covariance to
  \(|T_1-T_2-s+t|^{-a}\).
  Setting the two damping parameters equal is also not the single
  Laplace transform of a diagonal-horizon moment.
  For a self-pair at common gap damping, one external horizon instead
  adds \(1/\theta\), recovering the known first-mean coefficient.

  The proposition rules out exactly the analytic covariance substitution
  in~\eqref{E:naive-clock-candidate}, with product heat-chain measure,
  unrestricted operational-time rectangle and constant Brownian correlation.
  Additional relative-order weights,other derived clock couplings,matrix
  representations,modulus inequalities and their possible asymptotics are
  not covered. In particular, the inequality at this first cross pair
  leaves open a shared-clock lower comparison or asymptotic equivalence
  at higher orders. This finite clock calculation does not identify the
  intrinsic value proved later in Theorem~\ref{T:intrinsic-second-moment}
  with the source's all-moment conjecture.
  This is not a Skorohod result or a no-go for every two-clock method.
\end{remark}


\input{notes/integrated_covariance_foundation}
\input{notes/integrated_wave_variance}
\input{notes/integrated_compact_gaussian}
\input{notes/integrated_actual_operator_driver}
\input{notes/integrated_source_convergence}
\input{notes/integrated_masked_moments}
\input{notes/integrated_constant_phase_young}
\input{notes/integrated_compact_mean_family}
\input{notes/integrated_exact_scaling}
\input{notes/integrated_raw_block_lower}
\input{notes/integrated_unmasked_variational}
\input{notes/integrated_temporal_equilibrium}
\input{notes/integrated_spatial_occupation}
\input{notes/integrated_cameron_mean}
\input{notes/integrated_young_upper_foundation}
\input{notes/integrated_uniform_mean}
\input{notes/integrated_radius_anchor}
\input{notes/integrated_signed_static}
\input{notes/integrated_symplectic_phase}
\input{notes/integrated_gaussian_tubes}
\input{notes/integrated_uniform_products}
\input{notes/integrated_point_transfer}
\input{notes/integrated_signed_moment_upper}
\input{notes/integrated_positive_gram}
\input{notes/integrated_intrinsic_constant}
\input{notes/integrated_occupation_ceiling}
\input{notes/integrated_white_evaluation}

\section{Targets}\label{S:targets}

\begin{goal}[Upper bound at the correct scale]\label{G:upper}
  Under Hypothesis~\ref{H:homog}, prove
  $\limsup_{t\to\infty}t^{-\kappa}\log\E u^2(t,x)<\infty$, ideally with an
  explicit constant.
\end{goal}

Theorem~\ref{T:full-upper} proves this upper bound for every admissible
dimension and homogeneous covariance, independently of the later
variational identification. Earlier explicit bounds for
$0<\alpha\le1$ remain available.

\begin{goal}[Sharp second-moment constant]\label{G:sharp}
  Under Hypothesis~\ref{H:homog}, derive a finite constant
  $C_2(\Gamma,\alpha_0)$ and prove, for every fixed $x \in \R^d$,
  \[
    \lim_{t\to\infty}t^{-\kappa}\log\E u^2(t,x)
    = C_2(\Gamma,\alpha_0).
  \]
  A variational characterization must specify its full domain, covariance
  amplitude, kinetic coefficient and Gaussian action. Derive further
  evaluations and bounds from this formula. For zero covariance,
  $u(t,x) = 1$ and $C_2(0,\alpha_0) = 0$.
\end{goal}

Theorem~\ref{T:intrinsic-second-moment} proves this limit and specifies
its complete positive-control formula.
Theorem~\ref{T:intrinsic-occupation-ceiling},
Corollary~\ref{C:intrinsic-spatial-bracket} and
Theorem~\ref{T:white-moment-bounds} derive bounds from that value.
The original proposed bounds with endpoints
$2^{(4-\alpha)/(3-\alpha)}L_*$ and
$2^{(4-\alpha)/(3-\alpha)}L^*$ remain comparisons with
Conjecture~\ref{Conj:allp}. Matching those endpoints or closing the source's
variational gap is not required to identify the intrinsic value.
No correction of the source's normalization or equality of its energy
domains is adopted.

\section{Established steps and open questions}\label{S:route}

\begin{enumerate}[1.]
  \item \textbf{The mixed expansion and the first obstruction.}
    Section~\ref{S:G0} proves the complete nonnegative mixed expansion
    and an independent convergent solution series. It corrects the
    time-uniformity issue in the source's intermediate estimate.
    The common-per-pairing majorant has exponent $\rho>\kappa$ and cannot
    give the desired scale. This is a restriction on that majorant,
    not on the model or all uses of the source's Theorem~3.1.
  \item \textbf{Calibrations.}
    Section~\ref{S:G1} gives the finite white and Riesz coefficients.
    As $\alpha_0\downarrow0$, the target exponent becomes
    $(4-\alpha)/(3-\alpha)$, the static exponent.
    Proposition~\ref{P:Jensen} is unconditional; its numerical
    $2L_*$ specialization requires the stated first-moment premise.
    Comparisons with the Skorohod model identify time exponents only.
  \item \textbf{The full upper scale.}
    Section~\ref{S:d1-upper} gives explicit bounds when $\alpha\le1$.
    Section~\ref{S:interval-upper} proves the full homogeneous-covariance
    upper scale by independent interval fields, local Gaussian-degree
    estimates and dyadic covariance domination. The latter proof does
    not assume an endpoint representation of the spatial covariance.
  \item \textbf{The intrinsic constant.}
    Sections~\ref{S:actual-operator-driver}--\ref{S:intrinsic-second-moment}
    construct the actual phase/source framework and prove matching
    original point-moment bounds. The upper score uses the original raw
    variance-half action. Finite Gram optimization and positive smoothing
    identify it with the full positive-control lower value.
    The auxiliary label-one score is not identified with an actual
    first-moment limit or Chen's printed constants.
  \item \textbf{Computed bounds and the white example.}
    Section~\ref{S:intrinsic-occupation-ceiling} bounds the same constant
    using the full occupation class and a common spatial energy.
    Section~\ref{S:intrinsic-white-evaluation} evaluates that energy for
    $\Gamma=c\delta_0$ and gives explicit moment bounds and the relative
    width of their formulas. It does not evaluate the intrinsic supremum
    numerically or assert equality at either bound.
  \item \textbf{Source comparisons and scope.}
    The source first-moment normalization
    remains a qualified comparison question. Historical alternatives and
    failed routes above retain their original scope; they are not new
    premises of the intrinsic-limit proof.
\end{enumerate}

\bibliography{All,extra}

\end{document}

===== END TEX FILE: notes/notes_stratonovich_ham_second_moment.tex =====

===== BEGIN TEX FILE: notes/integrated_covariance_foundation.tex =====
\section{Covariance bounds for physically masked wave fields}
\label{S:masked-covariance}

We establish the covariance estimates needed for the operator construction.
Throughout this section, Hypothesis~\ref{H:homog} holds, $a = \alpha_0$,
and $\Gamma \ne 0$. For zero spatial covariance, the spatial spectral
measures and actual noise variances vanish; the purely temporal estimates
remain valid independently of $\Gamma$. We use the unitary Fourier transform
\[
  \widehat f(\xi) = c_d\int_{\R^d}e^{-i\xi\cdot x}f(x)\ud x,
  \qquad c_d = (2\pi)^{-d/2}.
\]
The spectral convention in Hypothesis~\ref{H:homog} means that, for every
complex Schwartz test $\varphi$,
\begin{equation}\label{E:masked-spectral-convention}
  \int_{\R^d}\varphi(x)\Gamma(\ud x)
  = \int_{\R^d}\left(\int_{\R^d}e^{i\xi\cdot x}
  \varphi(x)\ud x\right)\mu(\ud\xi).
\end{equation}
This is an identity of distribution pairings. We will not interchange
two infinite measures in the associated oscillatory expression.

A positive tempered Radon measure has polynomial mass growth. Indeed,
choose a nonnegative compact smooth test that is at least one on the unit
ball, and apply a defining Schwartz seminorm bound for the distribution
to its dilations. Its mass on a ball of radius $R \ge 1$ is bounded by a
power of $R$. Summation over dyadic shells then gives integrability of
$(1+|x|)^{-N}$ for some $N$, and hence absolute integrability of every
Schwartz test. These facts apply to both $\Gamma$ and $\mu$. Smooth cutoffs
converge in the Schwartz topology, so these integrals agree with the
tempered pairings.

\subsection{Translated spectral growth and physical masks}

\begin{proposition}[Translated spectral mass]\label{P:masked-spectral-growth}
  Put
  \[
    M_\Gamma = \int_{\R^d}e^{-|x|^2/4}\Gamma(\ud x),
    \qquad C_\Gamma = \frac{eM_\Gamma}{(2\sqrt{\pi})^d}.
  \]
  Then $0 < M_\Gamma < \infty$, and for $y \in \R^d$ and $r > 0$,
  \begin{align}
    \int_{\R^d}e^{-|\xi-y|^2/r^2}\mu(\ud\xi)
    &= \left(\frac{r}{2\sqrt{\pi}}\right)^d
    \int_{\R^d}e^{-r^2|x|^2/4}e^{-iy\cdot x}\Gamma(\ud x),
    \label{E:masked-gaussian-transform}\\
    0 \le \int_{\R^d}e^{-|\xi-y|^2/r^2}\mu(\ud\xi)
    &\le \frac{r^\alpha M_\Gamma}{(2\sqrt{\pi})^d},
    \qquad \mu(B(y,r)) \le C_\Gamma r^\alpha.
    \label{E:masked-translated-ball}
  \end{align}
  The ball may be open or closed.
\end{proposition}

\begin{proof}
  Temperedness gives finiteness of $M_\Gamma$. Its positivity follows from
  $\Gamma \ne 0$. To check the Fourier constant, set
  $J(b) = \int_\R e^{-Ax^2}e^{ibx}\ud x$ for $A > 0$. Squaring the real
  Gaussian integral and using polar coordinates gives
  $J(0) = \sqrt{\pi/A}$. Differentiation and integration by parts give
  $J'(b) = -bJ(b)/(2A)$. Therefore,
  $J(b) = \sqrt{\pi/A}e^{-b^2/(4A)}$. Taking products over the coordinates
  gives
  \[
    \int_{\R^d}e^{-r^2|x|^2/4}e^{i(\xi-y)\cdot x}\ud x
    = \left(\frac{2\sqrt{\pi}}r\right)^d e^{-|\xi-y|^2/r^2}.
  \]
  Apply~\eqref{E:masked-spectral-convention} to the single Schwartz test
  $e^{-r^2|x|^2/4}e^{-iy\cdot x}$ to obtain
  \eqref{E:masked-gaussian-transform}. Its left side is nonnegative.
  Taking the absolute value on the right removes the complex phase because
  $\Gamma$ is nonnegative. The pushforward of $\Gamma$ by $x \mapsto rx$
  assigns mass $r^{\alpha-d}\Gamma(A)$ to a Borel set $A$. Thus,
  \[
    \int e^{-r^2|x|^2/4}\Gamma(\ud x) = r^{\alpha-d}M_\Gamma.
  \]
  This proves the Gaussian bound. On either ball $B(y,r)$ the integrand
  $e^{-|\xi-y|^2/r^2}$ is at least $e^{-1}$, proving the mass bound.
  This proves Proposition~\ref{P:masked-spectral-growth}.
\end{proof}

Choose and fix a real nonzero Schwartz function $\zeta$. For $R > 0$ put
$\zeta_R(x) = \zeta(x/R)$, $k_R = \widehat{\zeta_R}$ and
$L = \|\widehat\zeta\|_1$. Then
$k_R(u) = R^d\widehat\zeta(Ru)$ and $\|k_R\|_1 = L > 0$. Define
\begin{equation}\label{E:masked-auxiliary-measure}
  \nu_R(\ud\eta) = \rho_R(\eta)\ud\eta,
  \qquad \rho_R(\eta) = c_d^2L\int |k_R(\xi-\eta)|\mu(\ud\xi).
\end{equation}

\begin{proposition}[Auxiliary mask norm]\label{P:masked-auxiliary-norm}
  The measure $\nu_R$ is even, tempered and Radon, with
  \begin{equation}\label{E:masked-auxiliary-growth}
    \nu_R(B(y,r)) \le c_d^2L^2C_\Gamma r^\alpha
  \end{equation}
  for all $y \in \R^d$ and $r > 0$, uniformly in $R > 0$.
  If $H$ is a separable complex Hilbert space and $F$ is an $H$-valued
  Schwartz function, then
  \begin{equation}\label{E:masked-hilbert-fourier}
    \int \|\widehat{\zeta_RF}(\xi)\|_H^2\mu(\ud\xi)
    \le \int \|\widehat F(\eta)\|_H^2\nu_R(\ud\eta).
  \end{equation}
  For a real $H$, the same assertion holds after complexification.
\end{proposition}

\begin{proof}
  Schwartz decay of $k_R$ and polynomial growth of $\mu$ show that
  $\rho_R(\eta)$ is finite at every $\eta$. On compact sets of $\eta$,
  the integrands have a common integrable bound. Dominated convergence
  therefore makes $\rho_R$ continuous, and $\nu_R$ is Radon. Since
  $\zeta$ is real, $k_R(-u) = \overline{k_R(u)}$. Evenness of $\mu$
  gives evenness of $\rho_R$. Tonelli's theorem gives
  \[
    \nu_R(B(y,r)) = c_d^2L\int |k_R(u)|\mu(B(y+u,r))\ud u.
  \]
  Proposition~\ref{P:masked-spectral-growth} and $\|k_R\|_1 = L$ give
  \eqref{E:masked-auxiliary-growth}. Polynomial growth on centered balls
  proves temperedness by the same dyadic argument as above.

  Bochner Fourier integration gives
  \[
    \widehat{\zeta_RF}(\xi)
    = c_d\int k_R(\xi-\eta)\widehat F(\eta)\ud\eta.
  \]
  For scalar Schwartz functions this follows by Fourier inversion and
  absolute integrability. It follows next for finite-rank Hilbert-valued
  functions. For general $F$, take projections onto the successive spans
  of a countable orthonormal basis of its separable range closure.
  They converge pointwise in norm. The Schwartz bounds
  on $F$ dominate the Fourier integrals, proving the identity by dominated
  convergence. In a finite-dimensional space the full identity projection
  suffices; the zero space is immediate. The triangle inequality and
  weighted Cauchy--Schwarz yield
  \[
    \|\widehat{\zeta_RF}(\xi)\|_H^2
    \le c_d^2L\int |k_R(\xi-\eta)|\|\widehat F(\eta)\|_H^2\ud\eta.
  \]
  Integrating against $\mu$ and applying Tonelli's theorem proves
  \eqref{E:masked-hilbert-fourier}. Its right side is finite by Schwartz
  decay and temperedness of $\nu_R$.
  This proves Proposition~\ref{P:masked-auxiliary-norm}.
\end{proof}

\subsection{Temporal completion and the original noise}

\begin{lemma}[Temporal covariance completion]\label{L:masked-time-completion}
  Let $T > 0$. The form
  \[
    \langle f,g\rangle_a
    = \int_0^T\int_0^T f(t)g(s)|t-s|^{-a}\ud t\ud s
  \]
  is positive semidefinite on real compact smooth tests. Its null-quotient
  completion $H_a$ is separable. The inclusion of tests extends continuously
  from $L^2(0,T)$, with
  \begin{equation}\label{E:masked-time-schur}
    \|f\|_a^2 \le \frac{2T^{1-a}}{1-a}\|f\|_2^2.
  \end{equation}
  In its complexification the norm is given by the same double integral
  with $f(t)\overline{f(s)}$. In particular, bounded measurable amplitudes
  on a subinterval, extended by zero, belong to this completion.
\end{lemma}

\begin{proof}
  Write $\Gamma_E$ for Euler's Gamma function. Away from the null diagonal,
  \[
    |t-s|^{-a} = \frac1{\Gamma_E(a)}\int_0^\infty
    \lambda^{a-1}e^{-\lambda|t-s|}\ud\lambda.
  \]
  This follows by substitution in the defining Gamma integral. Moreover,
  \[
    e^{-\lambda|t-s|}
    = \int_{-\infty}^{\min(t,s)}2\lambda
    e^{-\lambda(t-u)}e^{-\lambda(s-u)}\ud u.
  \]
  For each $\lambda > 0$ its quadratic form is an integral of a square.
  All exchanges for compact smooth tests are absolutely integrable because
  the kernel row integral is at most $2T^{1-a}/(1-a)$. The same bound and
  $2|xy| \le |x|^2+|y|^2$ prove~\eqref{E:masked-time-schur}.
  A countable $L^2$-dense family of compact smooth tests is consequently
  dense in $H_a$, proving separability. The complex quadratic form is the
  sum of those of the real and imaginary parts, since symmetry cancels
  the imaginary cross term. Thus, the same bound holds after
  complexification. Smooth density in $L^2$, together with the Schur
  bound on the absolute bilinear form, extends the inclusion and the
  integral identity to $L^2$. This includes the stated interval amplitudes.
  This proves Lemma~\ref{L:masked-time-completion}.
\end{proof}

Let $\mathcal D$ consist of finite sums
$F(t,x) = \sum_j\tau_j(t)f_j(x)$ with real
$\tau_j \in C_c^\infty(0,T)$ and real Schwartz $f_j$.
These give $H_a$-valued Schwartz functions of $x$. Let $W$ denote the
original real isonormal noise in~\eqref{E:cov}.

\begin{proposition}[Completion on the same noise]\label{P:masked-noise-completion}
  The space $\mathcal D$ belongs to the original test-noise completion and
  \begin{equation}\label{E:masked-actual-noise-norm}
    \E W(F)^2 = (2\pi)^d\int
    \|\widehat F(\xi)\|_{H_a^{\mathbb C}}^2\mu(\ud\xi).
  \end{equation}
  Define the auxiliary seminorm
  \[
    N_R(F)^2 = (2\pi)^d\int
    \|\widehat F(\eta)\|_{H_a^{\mathbb C}}^2\nu_R(\ud\eta).
  \]
  Then $F \mapsto W(\zeta_RF)$ extends as a contraction from the
  null-quotient completion for $N_R$ into the original $L^2(\Omega)$.
  The extension is centered and jointly Gaussian. For finitely many real
  $F_1,\ldots,F_m \in \mathcal D$, their actual masked covariance matrix
  is bounded in positive semidefinite order by the matrix of auxiliary
  inner products. This gives covariance comparison for every finite linear
  Gaussian image and every convex norm power $p \ge 1$.
\end{proposition}

\begin{proof}
  For real spatial Schwartz $f,g$, put
  $h(z) = \int f(y+z)g(y)\ud y$. Fourier inversion and Parseval give
  \[
    h(z) = \int e^{i\xi\cdot z}\widehat f(\xi)
    \overline{\widehat g(\xi)}\ud\xi.
  \]
  Therefore,
  \[
    \int e^{i\xi\cdot z}h(z)\ud z
    = (2\pi)^d\widehat f(-\xi)\overline{\widehat g(-\xi)}.
  \]
  Apply~\eqref{E:masked-spectral-convention} to the single test $h$ and
  reflect $\xi$ using evenness of $\mu$. The spatial covariance is thus
  $(2\pi)^d\int\widehat f(\xi)\overline{\widehat g(\xi)}\mu(\ud\xi)$.
  Summing over the finitely many temporal factors gives
  \eqref{E:masked-actual-noise-norm}. Schwartz decay, temperedness and
  temporal integrability justify these pairings. If $W$ is initially
  given only on compact spatial tests, smooth expanding cutoffs converge
  in the Schwartz topology. The spectral form is continuous in that
  topology, admitting $\mathcal D$ in the same completion.

  Proposition~\ref{P:masked-auxiliary-norm}, applied with
  $H = H_a^{\mathbb C}$, gives $\E W(\zeta_RF)^2 \le N_R(F)^2$.
  It annihilates auxiliary-null tests. An auxiliary Cauchy sequence thus
  gives a Cauchy sequence of actual noise evaluations in $L^2(\Omega)$,
  proving the contraction extension and its uniqueness. Every finite
  linear combination of the limits is an $L^2$ limit of centered Gaussian
  variables. Their variances converge, so their characteristic functions
  prove that the limits remain jointly centered Gaussian.

  For the finite family let $A$ be the actual covariance matrix and $B$ the
  auxiliary Gram matrix. Applying the norm inequality to $\sum_i b_iF_i$
  gives $b^{\mathsf T}Ab \le b^{\mathsf T}Bb$ for every real vector $b$.
  Diagonalizing $B-A$ constructs a centered Gaussian vector $Z$ of that
  covariance, independent of the actual evaluation vector $X$, on a product
  space. Then $X+Z$ has covariance $B$. Conditional Jensen gives
  $\E\|X\|^p \le \E\|X+Z\|^p$ for every norm and $p \ge 1$.
  Finite Gaussian moments ensure finiteness of both sides.
  This proves Proposition~\ref{P:masked-noise-completion}.
\end{proof}

The auxiliary completion depends on $R$ and $\zeta$. Its construction
does not define multiplication by $\zeta_R$ on the original noise
quotient. Nor does the finite linear Gaussian comparison assert a
covariance comparison for nonlinear wave solutions.
The auxiliary and original test norms need not dominate one another.
No spatial representative for every auxiliary class, nonnegative physical
inverse covariance for $\nu_R$, or uniform density bound in $R$ is asserted.

\begin{proposition}[A physical mask need not preserve noise-null tests]
  \label{P:masked-quotient-obstruction}
  In the admissible case $d = 2$, $\alpha = 1$, $0 < a < 1$ and
  $\Gamma = \delta_0(\ud x_1)\ud x_2$, there is a real compact smooth
  mask $\zeta$ such that no finite $C$ satisfies
  $\E W(\zeta F)^2 \le C\E W(F)^2$ for every compact smooth test $F$.
\end{proposition}

\begin{proof}
  Fourier inversion on Schwartz tests gives
  $\mu = (2\pi)^{-1}\ud\xi_1\delta_0(\ud\xi_2)$ in the stated spectral
  convention. The measure $\Gamma$ is nonnegative, even, positive definite
  and tempered, with $\Gamma(cA) = c\Gamma(A)$. It therefore satisfies
  Hypothesis~\ref{H:homog} with $\alpha = 1$. This is not spatial white
  noise in dimension two. For real compact smooth $g$, its spatial
  covariance is, by ordinary Fubini,
  \[
    V(g) = \int_\R\left(\int_\R g(x_1,x_2)\ud x_2\right)^2\ud x_1.
  \]
  Choose real even $\chi \in C_c^\infty(\R)$ equal to one on $[-1,1]$
  and zero outside $[-2,2]$. For example, on $1 < r = |x| < 2$ use
  \[
    \chi(x) = \frac{e^{-1/(2-r)}}{e^{-1/(2-r)}+e^{-1/(r-1)}}.
  \]
  The endpoint exponentials vanish to every order, so the plateau pastes
  smoothly. Let $I_\chi = \int(\chi')^2 > 0$ and
  $J_\chi = \int\chi^4 > 0$. Positivity of $I_\chi$ follows because
  $\chi$ is not constant, and $J_\chi \ge 2$. Put
  $g(x) = \chi(x_1)\chi''(x_2)$ and
  $\zeta(x) = \chi(x_1)\chi(x_2)$. Their unmasked marginal vanishes since
  $\int\chi'' = 0$, whereas integration by parts gives the masked marginal
  $-I_\chi\chi(x_1)^2$. Thus,
  $V(g) = 0$ and $V(\zeta g) = J_\chi I_\chi^2 > 0$.
  For a nonzero nonnegative $\tau \in C_c^\infty(0,T)$, set
  $F(t,x) = \tau(t)g(x)$. The temporal factor $\|\tau\|_a^2$ is finite
  and strictly positive because its nonnegative integrand is positive on
  a set of positive two-dimensional measure. Consequently, the full
  unmasked variance is zero and the masked variance is positive.
  This proves Proposition~\ref{P:masked-quotient-obstruction}.
\end{proof}

\subsection{Temporal modulation and continuous wave factors}

Write $\langle x\rangle = \sqrt{1+x^2}$. Let
$I = [s,s+h] \subset [0,T]$, with $0 < h \le 1$. Norms below are those of
the complexified temporal completion in Lemma~\ref{L:masked-time-completion}.

\begin{lemma}[Modulated amplitudes]\label{L:masked-temporal-modulation}
  Let $A \in C^1(I;\mathbb C)$, $M = \sup_I|A|$ and $D = \sup_I|A'|$.
  For every real $\omega$,
  \begin{equation}\label{E:masked-temporal-modulation}
    \|1_IA(t)e^{i\omega t}\|_a^2
    \le C_0(a)h^{2-a}(M+hD)^2\langle h\omega\rangle^{a-1},
    \qquad C_0(a) = \frac{16}{1-a}.
  \end{equation}
  The bound is uniform in $T,s,h,A$ and $\omega$.
\end{lemma}

\begin{proof}
  Put $c(v) = \int_s^{s+h-v}A(u+v)\overline{A(u)}\ud u$ for
  $0 \le v \le h$. Differentiation at the moving endpoint gives
  \[
    c'(v) = -A(s+h)\overline{A(s+h-v)}
    +\int_s^{s+h-v}A'(u+v)\overline{A(u)}\ud u.
  \]
  Thus, $c(h) = 0$, $|c(v)| \le hM^2$ and
  $|c'(v)| \le M^2+hMD$. Splitting the covariance square into its two
  conjugate triangles gives
  \[
    \|1_IA(t)e^{i\omega t}\|_a^2
    = 2\operatorname{Re}\int_0^h v^{-a}e^{i\omega v}c(v)\ud v
    = 2h^{2-a}\operatorname{Re}\int_0^1 y^{-a}e^{i\omega hy}f(y)\ud y,
  \]
  where $f(y) = c(hy)/h$. Set $K = M+hD$. Then $f(1) = 0$ and
  $|f|,|f'| \le K^2$. If $K = 0$ the assertion is immediate. If
  $|\omega h| \le 1$, the last integral is at most $K^2/(1-a)$ in
  absolute value, and $\langle\omega h\rangle^{a-1} \ge 2^{(a-1)/2}$.
  The claimed constant is sufficient in this case.

  Now suppose $k = |\omega h| > 1$. On $[0,1/k]$ the integral is at most
  $K^2k^{a-1}/(1-a)$. On $[1/k,1]$, integrate the exponential by parts.
  The endpoint at one vanishes, while the other endpoint contributes at
  most $K^2k^{a-1}$. The derivative integral, divided by $k$, is bounded by
  \[
    \frac{K^2}k\left(a\int_{1/k}^1 y^{-a-1}\ud y
    +\int_{1/k}^1 y^{-a}\ud y\right)
    \le K^2 k^{a-1}\left(1+\frac1{1-a}\right).
  \]
  Here $k^{-1} \le k^{a-1}$ since $a > 0$. The total is at most
  $4K^2k^{a-1}/(1-a)$. Finally,
  $k^{a-1} \le \sqrt{2}\langle\omega h\rangle^{a-1}$ and
  $8\sqrt{2} \le 16$. Including the factor $2h^{2-a}$ proves the bound
  for either sign of $\omega$.
  This proves Lemma~\ref{L:masked-temporal-modulation}.
\end{proof}

\begin{lemma}[Correlated trigonometric products]\label{L:masked-trig-products}
  Let $r,\rho \ge 0$. Let $P_r$ be either $\cos(rt)$ or $\sin(rt)$,
  and let $Q_\rho$ be either $\cos(\rho t)$ or $\sin(\rho t)$.
  With the amplitude and constant above,
  \begin{align}
    \|1_IAP_rQ_\rho\|_a^2
    &\le C_0(a)h^{2-a}(M+hD)^2\mathcal Q_h(r,\rho),
    \label{E:masked-trig-products}\\
    \mathcal Q_h(r,\rho)
    &:= \langle h(r-\rho)\rangle^{a-1}
    +\langle h(r+\rho)\rangle^{a-1}.
    \label{E:masked-frequency-pair}
  \end{align}
\end{lemma}

\begin{proof}
  Expanding the two trigonometric factors gives four complex exponential
  modes with frequencies $\sigma r+\tau\rho$, $\sigma,\tau \in \{-1,1\}$,
  and coefficients of absolute value $1/4$. In a Hilbert space,
  \[
    \left\|\sum_j c_jv_j\right\|^2
    \le \left(\sum_j|c_j|\right)\sum_j|c_j|\|v_j\|^2.
  \]
  The first coefficient sum is one. Apply
  Lemma~\ref{L:masked-temporal-modulation} to each mode. Two frequencies
  have absolute value $|r-\rho|$ and two have absolute value $r+\rho$.
  This gives one half of the asserted right side, and hence the bound.
  Repeated or zero frequencies are permitted; no orthogonality or
  independence of the modes is used.
  This proves Lemma~\ref{L:masked-trig-products}.
\end{proof}

\begin{lemma}[Continuous sine factors]\label{L:masked-continuous-wave}
  Define $c_r(t) = \cos(rt)$ and
  \[
    b_r(t) = \langle r\rangle\frac{\sin(rt)}r\quad(r > 0),
    \qquad b_0(t) = t.
  \]
  For $F_r \in \{c_r,b_r\}$ and $G_\rho \in \{c_\rho,b_\rho\}$,
  \begin{equation}\label{E:masked-continuous-wave}
    \|1_IF_rG_\rho\|_a^2
    \le C_1(a)(1+T)^4h^{2-a}\mathcal Q_h(r,\rho),
    \qquad C_1(a) = 4\cdot3^{1-a}C_0(a).
  \end{equation}
\end{lemma}

\begin{proof}
  For $r \ge 1$, $b_r$ is a sine times a coefficient at most $\sqrt{2}$.
  For $0 \le r \le 1$, the fundamental theorem of calculus gives
  \[
    b_r(t) = t\langle r\rangle\int_0^1\cos(vrt)\ud v.
  \]
  This includes $r = 0$. Hence, a product $F_rG_\rho$ is a scalar
  coefficient of absolute value at most two times a normalized integral
  of $t^jP_{r'}(t)Q_{\rho'}(t)$, where $j \in \{0,1,2\}$ and
  $|r'-r|,|\rho'-\rho| \le 1$. The integral is over zero, one or two
  copies of $[0,1]$; with no averages, use a one-point probability space.
  Its parameter dependence is continuous in $L^2(0,T)$ by dominated
  convergence. Lemma~\ref{L:masked-time-completion} makes it continuous
  in $H_a$ as well. Thus, the averages are genuine Bochner integrals,
  and their $H_a$ images agree with the pointwise averages by continuity
  of the inclusion. Hilbert Jensen bounds the squared norm of an average
  by the average of the squared norms.

  Apply Lemma~\ref{L:masked-trig-products} to each integrand with $A(t)=t^j$.
  For $j = 0,1,2$, respectively, $M+hD$ is at most
  $1$, $T+1$ and $T^2+2T$. In every case $(M+hD)^2 \le (1+T)^4$.
  For real $x,e$, the triangle inequality and its reverse imply
  \[
    \frac{\langle x\rangle}{1+|e|}
    \le \langle x+e\rangle \le (1+|e|)\langle x\rangle.
  \]
  The changes in $h(r\pm\rho)$ have magnitude at most two, since $h \le 1$.
  Because $a-1 < 0$, each altered bracket to the power $a-1$ is at most
  $3^{1-a}$ times the original one. Apply these comparisons, Hilbert Jensen
  and the squared scalar coefficient bound four to obtain
  \eqref{E:masked-continuous-wave}.
  This proves Lemma~\ref{L:masked-continuous-wave}.
\end{proof}

These estimates concern covariance forms and temporal factors.
Their actual two-phase application is in Section~\ref{S:wave-variance};
the subsequent operator, source and moment results require their
separate proofs. They do not follow from covariance domination alone.

===== END TEX FILE: notes/integrated_covariance_foundation.tex =====

===== BEGIN TEX FILE: notes/integrated_wave_variance.tex =====
\section{Frequency estimates and both wave variance directions}
\label{S:wave-variance}

We now apply the covariance and temporal estimates of
Section~\ref{S:masked-covariance} to the full wave phase. We retain
Hypothesis~\ref{H:homog}, write $a = \alpha_0$, and choose and fix
\begin{equation}\label{E:variance-gamma-range}
  0 < \gamma < \min\left(\frac12,\frac{2-\alpha}{2}\right).
\end{equation}
The interval is nonempty because $\alpha+a < 2$. We use
$\langle\xi\rangle = \sqrt{1+|\xi|^2}$ and set
\begin{equation}\label{E:variance-scale-profile}
  B_\alpha(h) =
  \begin{cases}
    1, & \alpha < 1,\\
    1+\log(1/h), & \alpha = 1,\\
    h^{1-\alpha}, & \alpha > 1,
  \end{cases}
  \qquad 0 < h \le 1.
\end{equation}

\subsection{A scalar row estimate for a measure}

Let $\nu$ be a positive Radon measure satisfying
\begin{equation}\label{E:frequency-translated-growth}
  \nu(B(y,r)) \le C r^\alpha,
  \qquad y \in \R^d,\quad r > 0,
\end{equation}
where $C \ge 0$. If the estimate is initially known for open balls, apply
it at radius $r+\epsilon$ and let $\epsilon \downarrow 0$ to obtain the
closed-ball estimate. Neither evenness nor a density is assumed here.
Using~\eqref{E:masked-frequency-pair}, define
\begin{align}
  \Phi_h(\xi,\eta)
  &:= \frac{\mathcal Q_h(|\xi|,|\eta|)}
  {\langle\xi\rangle\langle\eta\rangle},
  \label{E:frequency-row-kernel}\\
  J_h(\xi)
  &:= \langle\xi\rangle^{2\gamma}
  \int_{\R^d}\Phi_h(\xi,\xi-\lambda)\nu(\ud\lambda).
  \label{E:frequency-row-integral}
\end{align}
These are initially nonnegative extended integrals. In particular, the
notation denotes a pushforward of $\nu$, not integration against an
assumed spectral density.

\begin{proposition}[Uniform scalar row]\label{P:frequency-row}
  There is a finite $K = K(\alpha,a,\gamma)$, independent of
  $d,\nu,C,h$ and $\xi$, such that
  \begin{equation}\label{E:frequency-row-bound}
    \sup_{\xi\in\R^d}J_h(\xi) \le K C B_\alpha(h),
    \qquad 0 < h \le 1.
  \end{equation}
\end{proposition}

\begin{proof}
  If $C = 0$, a countable covering by finite balls gives $\nu = 0$, and
  the result is immediate. Suppose $C > 0$. For each $\xi$, let $\nu_\xi$
  be the pushforward under $\lambda \mapsto \eta = \xi-\lambda$.
  Then $\nu_\xi(B(0,R)) \le CR^\alpha$. For $q \ge 1$, put
  \[
    A_\xi(q) = \int_{|\eta|\le5q}\langle\eta\rangle^{-1}
    \nu_\xi(\ud\eta).
  \]
  Choose $N = \lceil\log_2(5q)\rceil$, so $5q \le 2^N < 10q$.
  Splitting into the unit ball and the annuli
  $2^j < |\eta| \le 2^{j+1}$ gives
  \[
    A_\xi(q) \le C\left(1+2^\alpha
    \sum_{j=0}^{N-1}2^{j(\alpha-1)}\right).
  \]
  The geometric sum is bounded when $\alpha < 1$, is $N$ when
  $\alpha = 1$, and is at most
  $2^{N(\alpha-1)}/(2^{\alpha-1}-1)$ when $\alpha > 1$. Hence,
  \begin{equation}\label{E:frequency-inverse-bessel}
    A_\xi(q) \le K_\alpha C
    \begin{cases}
      1, & \alpha < 1,\\
      1+\log q, & \alpha = 1,\\
      q^{\alpha-1}, & \alpha > 1,
    \end{cases}
  \end{equation}
  with a constant depending only on $\alpha$.

  Set $q = \max(1,|\xi|)$ and $\epsilon = 1-2\gamma > 0$. On
  $|\lambda| \le 4q$ we have $|\eta| \le 5q$. Both bracket powers in
  $\mathcal Q_h$ are at most one, since $a-1 < 0$. The contribution of
  this region to $J_h(\xi)$ is at most
  \[
    2\langle\xi\rangle^{-\epsilon}A_\xi(q)
    \le 2q^{-\epsilon}A_\xi(q).
  \]
  If $\alpha < 1$, this is uniformly bounded by~\eqref{E:frequency-inverse-bessel}.
  If $\alpha = 1$, the bound follows from
  \[
    e^{-\epsilon u}(1+u) \le 1+\frac1{e\epsilon},
    \qquad u = \log q \ge 0,
  \]
  since $u e^{-\epsilon u}$ has maximum $1/(e\epsilon)$. If
  $\alpha > 1$, the remaining power is $q^{\alpha+2\gamma-2}$, whose
  exponent is negative by~\eqref{E:variance-gamma-range}. Thus, the near
  contribution is at most a constant times $C$ in all three cases.

  On the far region write $r = |\lambda| > 4q$. Then
  \[
    |\eta| \ge \frac{3r}4,\qquad
    \big||\eta|-|\xi|\big| \ge \frac r2,\qquad
    |\eta|+|\xi| \ge \frac r2.
  \]
  Each oscillatory bracket is at least $\langle hr\rangle/2$, whereas
  $\langle\eta\rangle^{-1} \le 4/(3r)$ and
  $\langle\xi\rangle^{-\epsilon} \le 1$. Consequently, the far
  contribution is at most
  \[
    \frac43\,2^{2-a}\int_{|\lambda|>4q}
    |\lambda|^{-1}\langle h|\lambda|\rangle^{a-1}\nu(\ud\lambda).
  \]
  Enlarge the domain to $|\lambda| > 1$ and split it into dyadic annuli.
  Applying~\eqref{E:frequency-translated-growth} to their masses bounds
  this expression by a constant depending only on $\alpha,a$ times
  $C S(h)$, where
  \[
    S(h) = \sum_{j=0}^\infty
    2^{j(\alpha-1)}\langle h2^j\rangle^{a-1}.
  \]
  Choose $L = \lfloor\log_2(1/h)\rfloor \ge 0$. For $j \le L$ the
  bracket power is at most one. For $j \ge L+1$ it is at most
  $(h2^j)^{a-1}$. Since $\alpha+a-2 < 0$, the tail is
  \[
    \frac{h^{a-1}2^{(L+1)(\alpha+a-2)}}{1-2^{\alpha+a-2}}
    \le \frac{h^{1-\alpha}}{1-2^{\alpha+a-2}}.
  \]
  The inequality uses $2^{L+1} > 1/h$ and the negative exponent.
  The finite sum is bounded by $1/(1-2^{\alpha-1})$ for $\alpha < 1$,
  by $1+\log_2(1/h)$ for $\alpha = 1$, and by
  \[
    \frac{2^{\alpha-1}h^{1-\alpha}}{2^{\alpha-1}-1}
  \]
  for $\alpha > 1$. Since $h^{1-\alpha} \le 1$ in the first case,
  we obtain $S(h) \le K_{\alpha,a}B_\alpha(h)$. Combining the near and
  far bounds, and using $B_\alpha(h) \ge 1$, proves the assertion and
  finiteness of the original integral. All constants arose from numerical
  shell estimates and are independent of $d$.
  This proves Proposition~\ref{P:frequency-row}.
\end{proof}

\begin{corollary}[A time exponent above one half]\label{C:frequency-time}
  For every
  \begin{equation}\label{E:variance-beta-range}
    \frac12 < \beta < \min\left(1-\frac a2,
    \frac{3-a-\alpha}{2}\right),
  \end{equation}
  there is a finite $K_\beta = K_\beta(\alpha,a,\gamma,\beta)$ such that
  \begin{equation}\label{E:frequency-time-bound}
    h^{2-a}\sup_\xi J_h(\xi) \le K_\beta C h^{2\beta},
    \qquad 0 < h \le 1.
  \end{equation}
\end{corollary}

\begin{proof}
  Both upper endpoints in~\eqref{E:variance-beta-range} exceed one half,
  by $a < 1$ and $\alpha+a < 2$. If $\alpha < 1$, use
  $2-a > 2\beta$ in Proposition~\ref{P:frequency-row}. If $\alpha > 1$,
  use $3-a-\alpha > 2\beta$. For $\alpha = 1$, set
  $\delta = 2-a-2\beta > 0$ and $u = \log(1/h)$. Then
  \[
    h^\delta(1+\log(1/h))
    = e^{-\delta u}(1+u) \le 1+\frac1{e\delta}.
  \]
  This absorbs the critical logarithm. No endpoint value of $\beta$ is used.
  This proves Corollary~\ref{C:frequency-time}.
\end{proof}

\subsection{Actual forms on the full phase}

Choose and fix $T > 0$. Set $\Lambda = (1-\Delta)^{1/2}$,
$s = 1/2$ and $E_r = H^r(\R^d)\times H^{r-1}(\R^d)$. On the
complexification of $E = E_s$, use inner products linear in the first slot.
The map
\[
  Jz(\xi) = \left(\langle\xi\rangle^{1/2}\widehat z_1(\xi),
  \langle\xi\rangle^{-1/2}\widehat z_2(\xi)\right)
\]
is unitary onto $L^2(\R^d;\mathbb C^2)$. The full massless wave group has
Fourier matrix
\begin{equation}\label{E:variance-free-matrix}
  S(t,\xi) =
  \begin{pmatrix}
    \cos(t|\xi|) & \sin(t|\xi|)/|\xi|\\
    -|\xi|\sin(t|\xi|) & \cos(t|\xi|)
  \end{pmatrix},
\end{equation}
where the sine quotient is $t$ at zero. Let $B(b)(u,v) = (0,bu)$.
Choose and fix a real even nonnegative $\zeta \in C_c^\infty(\R^d)$
equal to one on $B_1$ and zero off $B_2$, and put $\zeta_R(x) = \zeta(x/R)$
for $R > 0$. For $I = [t_0,t_0+h] \subset [0,T]$, $0 < h \le 1$, and
Schwartz phases $z,w$, put
\begin{align}
  v_z(t) &= [S(t)z]_1,
  \label{E:variance-displacement}\\
  G_w(t) &= -\frac{\sin(t|D|)}{|D|}\Lambda w_1
  +\cos(t|D|)\Lambda^{-1}w_2,
  \label{E:variance-dual-wave}\\
  F_{z,w}(t,x) &= 1_I(t)v_z(t,x)\overline{G_w(t,x)},
  \qquad \ell_R(I;z,w) = W_{\mathbb C}(\zeta_RF_{z,w}),
  \label{E:variance-actual-form}
\end{align}
where $W_{\mathbb C}(F) = W(\operatorname{Re}F)+iW(\operatorname{Im}F)$.
There is no observation cutoff in this definition.

We first assume $\Gamma \ne 0$. If $\Gamma = 0$, all actual forms and
the column maps below are zero, so their bounds hold directly.
For the nonzero case, let $\nu_R$ be~\eqref{E:masked-auxiliary-measure} and set
\begin{equation}\label{E:variance-actual-growth-constant}
  L_\zeta = \|\widehat\zeta\|_1,\qquad
  C_\nu = c_d^2L_\zeta^2C_\Gamma.
\end{equation}
Proposition~\ref{P:masked-auxiliary-norm} gives a positive even tempered
Radon measure with $\nu_R(B(y,r)) \le C_\nu r^\alpha$, uniformly in $R$.

\begin{proposition}[Actual form and phase kernel]\label{P:actual-wave-form}
  The tests $\zeta_RF_{z,w}$ in~\eqref{E:variance-actual-form} belong to the
  original noise completion. The form $\ell_R$ is linear in $z$ and
  conjugate linear in $w$, and uses the same $W$ as the model.
  For a smooth deterministic coefficient $b$ with
  common compact spatial support and bounded spatial derivatives on $[0,T]$,
  \begin{equation}\label{E:variance-physical-adjoint}
    \langle S(-t)B(b(t))S(t)z,w\rangle_E
    = \int b(t,x)v_z(t,x)\overline{G_w(t,x)}\ud x.
  \end{equation}
  For a real compact smooth $\chi$, multiplication $D_\chi$ on both phase
  entries has adjoint
  \begin{equation}\label{E:variance-cutoff-adjoint}
    D_\chi^{*,E}w
    = \left(\Lambda^{-1}\chi\Lambda w_1,
    \Lambda\chi\Lambda^{-1}w_2\right).
  \end{equation}
  With $U = Jz$, $V = Jw$, $r = |\xi|$, $\rho = |\eta|$ and the
  continuous functions $c_r,b_r$ of Lemma~\ref{L:masked-continuous-wave}, set
  \begin{equation}\label{E:variance-normalized-kernel}
    \mathcal K(t;\xi,\eta)
    = \frac1{\sqrt{\langle\xi\rangle\langle\eta\rangle}}
    \begin{pmatrix}
      -b_rc_\rho & -b_rb_\rho\\
      c_rc_\rho & c_rb_\rho
    \end{pmatrix}(t).
  \end{equation}
  Then
  \begin{equation}\label{E:variance-normalized-covariance}
    \E|\ell_R(I;z,w)|^2
    \le \int\left\|\int\sum_{i,j=1}^2
    1_I\mathcal K_{ij}(\cdot;\eta+\lambda,\eta)
    U_j(\eta)\overline{V_i(\eta+\lambda)}\ud\eta
    \right\|_{H_a^{\mathbb C}}^2\nu_R(\ud\lambda).
  \end{equation}
\end{proposition}

\begin{proof}
  The wave multipliers are smooth at zero through the continuous sine
  quotient, with polynomially bounded frequency derivatives on finite time
  intervals. Bessel multipliers preserve Schwartz space. Thus, $v_z,G_w$
  and their product are continuous in all Schwartz seminorms on $[0,T]$.
  For tests supported in a fixed compact $K$, the absolute spatial pairing
  is bounded by
  \[
    |K|\Gamma(K-K)\|F(t)\|_\infty\|H(u)\|_\infty.
  \]
  Indeed, only $y \in K-K$ contributes to
  $\int\Gamma(\ud y)\int F(t,x)\overline{H(u,x-y)}\ud x$.
  Combine this with the temporal Schur bound and approximate the interval
  indicator and the continuous time dependence by smooth interior temporal
  tests, keeping the spatial support of $\zeta_R$. This admits the masked
  product in the original completion in every allowed dimension.

  We also identify its auxiliary and spectral limits. Approximate a
  Schwartz-valued function on $I$ by time partitions with frozen spatial
  values, and then replace the finitely many indicators by compact smooth
  temporal functions. A diagonal sequence $F_n$ of finite temporal tensors
  converges in $L^2$ time in every Schwartz seminorm. Fourier integration
  by parts and the spatial weighted supremum bounds give, for sufficiently
  large fixed $N$,
  \[
    \|\widehat{F_n-F}(\xi)\|_{L^2(0,T)}
    \le \epsilon_n\langle\xi\rangle^{-N},\qquad \epsilon_n \to 0.
  \]
  Choose $N$ so that the square weight is integrable against both tempered
  measures $\mu$ and $\nu_R$. Lemma~\ref{L:masked-time-completion} gives
  convergence in their spectral $H_a$ norms. Multiplication by the fixed
  $\zeta_R$ preserves these $L^2$ Schwartz-seminorm limits, so the masked
  differences converge in the $\mu$ spectral norm too. The preceding
  compact-support estimate also gives convergence in the actual raw
  completion. Hence, the auxiliary extension and original-noise limit
  agree on these products. Constants for this admission argument may
  depend on $R$; they are not the uniform variance constants below.

  For real tensor tests $f,g$, the Hermitian symmetry of their spatial
  transforms gives
  \[
    A(-\xi) = \overline{A(\xi)},\qquad
    A(\xi) = \langle\widehat f(\xi),\widehat g(\xi)\rangle_{H_a^{\mathbb C}}.
  \]
  Integration against either even $\mu$ or even $\nu_R$ cancels the
  imaginary mixed term. Expanding the squared norm of
  $\widehat f+i\widehat g$, then using the preceding approximation, extends
  Proposition~\ref{P:masked-noise-completion} to the present complex tests:
  \begin{equation}\label{E:variance-complex-noise}
    \E|W_{\mathbb C}(\zeta_RF)|^2
    = (2\pi)^d\int\|\widehat{\zeta_RF}(\xi)\|_{H_a^{\mathbb C}}^2\mu(\ud\xi)
    \le (2\pi)^d\int\|\widehat F(\lambda)\|_{H_a^{\mathbb C}}^2\nu_R(\ud\lambda).
  \end{equation}
  This is a bound for the actual masked noise, not a declaration that its
  law is stationary. Complex linearity of $W_{\mathbb C}$ and linearity of
  $v_z,G_w$ prove the stated sesquilinearity.

  Smooth multiplication is bounded on each Sobolev space: Fourier
  convolution, the inequality
  $\langle\xi\rangle^r\langle\eta\rangle^{-r}
  \le 2^{|r|/2}\langle\xi-\eta\rangle^{|r|}$ and weighted Schwartz decay
  reduce this to the $L^1*L^2$ bound. The free matrix is strongly continuous
  and bounded on $E$ on compact time intervals, directly by its weighted
  Fourier entries. Thus, the ordinary first-response integral exists on
  states. Since
  $S(-t)(0,f)=(-\sin(t|D|)f/|D|,\cos(t|D|)f)$, moving the real
  self-adjoint multipliers and the two Sobolev weights onto $w$ proves
  \eqref{E:variance-physical-adjoint}. The same weighted duality gives
  \eqref{E:variance-cutoff-adjoint}. Inserting this adjoint in $G_w$ is
  the correctly observed form; $D_\chi$ need not be self-adjoint on $E$.
  This deterministic identity does not identify a positive-width source
  with the raw noise or assert a source limit.

  The definitions give exactly
  \begin{align*}
    \widehat v_z(t,\eta)
    &= \langle\eta\rangle^{-1/2}
    [c_\rho(t)U_1(\eta)+b_\rho(t)U_2(\eta)],\\
    \widehat G_w(t,\xi)
    &= \langle\xi\rangle^{-1/2}
    [-b_r(t)V_1(\xi)+c_r(t)V_2(\xi)].
  \end{align*}
  Their product gives~\eqref{E:variance-normalized-kernel}. At zero
  frequencies one uses the continuous sine quotient, not division by zero;
  at $\xi=\eta=0$ the matrix is
  $\left(\begin{smallmatrix}-t&-t^2\\1&t\end{smallmatrix}\right)$.
  Fourier multiplication with the conjugate yields
  \[
    \widehat F_{z,w}(t,-\lambda)
    = c_d1_I(t)\int\sum_{i,j=1}^2\mathcal K_{ij}(t;\eta+\lambda,\eta)
    U_j(\eta)\overline{V_i(\eta+\lambda)}\ud\eta.
  \]
  The spatial integral is absolutely convergent uniformly on the finite
  time interval by Schwartz decay. The Schur bound also makes it a
  Bochner $H_a^{\mathbb C}$ integral. Reflect $\lambda$ using evenness of
  $\nu_R$ in~\eqref{E:variance-complex-noise}. Since $(2\pi)^dc_d^2=1$,
  this proves~\eqref{E:variance-normalized-covariance} with no remaining
  Fourier factor.
  This proves Proposition~\ref{P:actual-wave-form}.
\end{proof}

\subsection{Bessel's inequality and the two variances}

\begin{lemma}[Hilbert-valued finite Bessel inequality]\label{L:phase-bessel}
  Let $H$ be a separable complex Hilbert space, let $\{u_k\}$ be a finite
  orthonormal family in $L^2(\R^d;\mathbb C^2)$, and let
  $g=(g_1,g_2) \in L^2(\R^d;H^2)$. Then
  \begin{equation}\label{E:phase-bessel}
    \sum_k\left\|\int\sum_{j=1}^2u_{k,j}(\eta)g_j(\eta)\ud\eta\right\|_H^2
    \le \int\sum_{j=1}^2\|g_j(\eta)\|_H^2\ud\eta.
  \end{equation}
  The same bound holds with $\overline{u_{k,j}}$ in place of $u_{k,j}$.
\end{lemma}

\begin{proof}
  Expand $g$ in a countable orthonormal basis of $H$. On each scalar
  coefficient apply scalar Bessel to the orthonormal family
  $\{\overline{u_k}\}$, or to $\{u_k\}$ for the conjugated version.
  Scalar finite Bessel follows by subtracting an orthogonal finite
  projection and expanding its nonnegative squared norm. Sum over the
  $H$ basis and use Parseval and nonnegative Tonelli. The Bochner integrals
  exist by $L^2$ Cauchy--Schwarz. A finite-dimensional $H$ uses its finite
  basis, and the zero space is immediate. No independence is involved.
  This proves Lemma~\ref{L:phase-bessel}.
\end{proof}

\begin{proposition}[Both actual variance directions]\label{P:wave-two-variances}
  There is a finite $C_T$, depending on the fixed model, mask,
  $a,\alpha,\gamma,T$, but not on $R,I$ or the orthonormal family, such
  that for every finite complex $E$-orthonormal Schwartz family $\{e_k\}$
  and every Schwartz phase $z$,
  \begin{align}
    \sum_k\E|\ell_R(I;e_k,z)|^2
    &\le C_T h^{2-a}B_\alpha(h)\|z\|_{E_{s-\gamma}}^2,
    \label{E:wave-input-variance}\\
    \sum_k\E|\ell_R(I;z,e_k)|^2
    &\le C_T h^{2-a}B_\alpha(h)\|z\|_{E_{s-\gamma}}^2.
    \label{E:wave-output-variance}
  \end{align}
  For every $\beta$ in~\eqref{E:variance-beta-range}, either right side
  may be replaced by $C_{T,\beta}h^{2\beta}\|z\|_{E_{s-\gamma}}^2$.
\end{proposition}

\begin{proof}
  Each entry in~\eqref{E:variance-normalized-kernel} is a product of two
  continuous wave factors times
  $(\langle\xi\rangle\langle\eta\rangle)^{-1/2}$, with a possible minus
  sign. Lemma~\ref{L:masked-continuous-wave} therefore gives
  \begin{equation}\label{E:variance-kernel-time-bound}
    \|1_I\mathcal K_{ij}(\cdot;\xi,\eta)\|_{H_a^{\mathbb C}}^2
    \le A_T h^{2-a}\Phi_h(\xi,\eta),
    \qquad A_T = C_1(a)(1+T)^4.
  \end{equation}
  The positive even Radon measure $\nu_R$ satisfies the actual growth bound
  \eqref{E:variance-actual-growth-constant}. Thus, all hypotheses of
  Proposition~\ref{P:frequency-row} hold, and
  \begin{equation}\label{E:variance-actual-row-bound}
    \int\Phi_h(\xi,\xi-\lambda)\nu_R(\ud\lambda)
    \le K C_\nu B_\alpha(h)\langle\xi\rangle^{-2\gamma}.
  \end{equation}
  No nonnegative physical inverse covariance of $\nu_R$ is needed.

  The kernels used in Lemma~\ref{L:phase-bessel} belong to its stated
  $L^2$ space for each fixed $\lambda$. Indeed,
  $|c_r(t)| \le 1$ and $|b_r(t)| \le \sqrt{2}\max(1,T)$ on $[0,T]$,
  by the high- and low-frequency representations. The kernels are
  continuous into $L^2(0,T)$ in their frequency variables, hence into
  $H_a^{\mathbb C}$ by Schur. Separability gives strong measurability.
  Multiplication by shifted Schwartz components of $U$ or $V$ then gives
  the required $L^2$ integrability. Later $\lambda$ integrals are of
  nonnegative functions; their finiteness follows from the estimates below.

  First fix $V = Jz$ and let $U_k = Je_k$ be the input family. In
  \eqref{E:variance-normalized-covariance} set
  \[
    g_j^\lambda(\eta) = \sum_{i=1}^2
    1_I\mathcal K_{ij}(\cdot;\eta+\lambda,\eta)
    \overline{V_i(\eta+\lambda)}.
  \]
  Lemma~\ref{L:phase-bessel} and Cauchy--Schwarz over the two output
  components give
  \begin{align*}
    \sum_j\|g_j^\lambda(\eta)\|_{H_a^{\mathbb C}}^2
    &\le 2\sum_{i,j}|V_i(\eta+\lambda)|^2
    \|1_I\mathcal K_{ij}(\cdot;\eta+\lambda,\eta)\|_{H_a^{\mathbb C}}^2\\
    &\le 4A_T h^{2-a}\Phi_h(\eta+\lambda,\eta)
    \sum_i|V_i(\eta+\lambda)|^2.
  \end{align*}
  Change variables $\xi = \eta+\lambda$ in the Lebesgue integral for
  each $\lambda$, apply Tonelli and~\eqref{E:variance-actual-row-bound},
  and use $\|z\|_{E_{s-\gamma}} = \|\langle\xi\rangle^{-\gamma}Jz\|_2$.
  This proves~\eqref{E:wave-input-variance} with $C_T = 4A_TKC_\nu$.

  Next fix $U = Jz$ and let $V_k = Je_k$ be the output family. After
  $\eta = \xi-\lambda$ in~\eqref{E:variance-normalized-covariance}, put
  \[
    f_i^\lambda(\xi) = \sum_{j=1}^2
    1_I\mathcal K_{ij}(\cdot;\xi,\xi-\lambda)U_j(\xi-\lambda).
  \]
  Apply the conjugated version of Lemma~\ref{L:phase-bessel}.
  Cauchy--Schwarz over the two input components bounds its right side by
  \[
    4A_T h^{2-a}\int\Phi_h(\xi,\xi-\lambda)
    \sum_j|U_j(\xi-\lambda)|^2\ud\xi.
  \]
  After the change of variables and Tonelli, the row at fixed $\eta$ is
  $\int\Phi_h(\eta+\lambda,\eta)\nu_R(\ud\lambda)$. Reflect $\lambda$
  using the actual evenness of $\nu_R$ and then use symmetry of $\Phi_h$.
  This row becomes
  $\int\Phi_h(\eta,\eta-\lambda)\nu_R(\ud\lambda)$, which is bounded by
  \eqref{E:variance-actual-row-bound} with $\xi = \eta$. This proves
  \eqref{E:wave-output-variance} with the same $C_T$.

  Use Corollary~\ref{C:frequency-time} for $h^{2-a}$ times the row integral
  at the two applications above to obtain the asserted $h^{2\beta}$ bounds,
  including strict absorption of the critical logarithm. The
  constants are uniform in $R,I$ and family size. The $R$-dependent
  admission estimate was not used as this uniform variance bound.
  This proves Proposition~\ref{P:wave-two-variances}.
\end{proof}

\subsection{Same-noise mean-square columns}

Write $E_r^{\mathrm{real}}$ for the real phase space in dimension $d$.

\begin{proposition}[Column and adjoint-column maps]\label{P:wave-square-columns}
  On the same probability space there are deterministic bounded real
  linear maps
  \[
    m_{R,I},n_{R,I}:E_{s-\gamma}^{\mathrm{real}}\longrightarrow
    L^2(\Omega;E_s^{\mathrm{real}}),
  \]
  with squared bounds $C_T h^{2-a}B_\alpha(h)$, such that, for every
  fixed real Schwartz pair $z,w$,
  \begin{equation}\label{E:variance-square-columns}
    \langle m_{R,I}z,w\rangle_E
    = \ell_R(I;z,w) = \langle z,n_{R,I}w\rangle_E
    \quad\text{in }L^2(\Omega).
  \end{equation}
  Fixed-vector values and finite families of values are centered Gaussian.
\end{proposition}

\begin{proof}
  Choose a countable real Schwartz orthonormal basis $\{e_k\}$ of $E_s$.
  Such a basis follows by Gram--Schmidt from a countable dense Schwartz
  family, discarding zero residuals. Schwartz density follows by smooth
  Fourier cutoff approximation in the weighted $L^2$ norms:
  approximate by compact smooth Fourier coordinates, replace $g(\xi)$
  by $(g(\xi)+\overline{g(-\xi)})/2$, and apply the inverse Bessel/Fourier
  maps. The resulting phases are real Schwartz, and Gram--Schmidt
  preserves that class. The same
  density holds in $E_{s-\gamma}$.

  For fixed real Schwartz $z$, define
  \[
    m_N(z) = \sum_{k\le N}\ell_R(I;z,e_k)e_k,
    \qquad n_N(z) = \sum_{k\le N}\ell_R(I;e_k,z)e_k.
  \]
  Both are finite Gaussian sums on the original $W$. By
  Proposition~\ref{P:wave-two-variances}, their coefficient expected squares
  have finite sum. Orthogonality gives the squared tail norms as the
  corresponding sums of expected squares. Thus, both sequences converge
  in $L^2(\Omega;E_s)$ to $m(z),n(z)$ with the asserted bounds, without
  independence of the coefficients. Finite-sum measurability and separable
  $E_s$ give strong measurability of the limits. The bounded real linear
  maps extend uniquely from Schwartz phases to $E_{s-\gamma}$.

  If $w_N$ is the $E_s$ projection of a Schwartz $w$ onto the first $N$
  basis vectors, then
  $\langle m_N(z),w\rangle_E = \ell_R(I;z,w_N)$. The singleton form of
  \eqref{E:wave-output-variance}, after normalizing $w-w_N$ in $E_s$,
  gives
  \[
    \E|\ell_R(I;z,w-w_N)|^2
    \le C_T h^{2-a}B_\alpha(h)\|z\|_{E_{s-\gamma}}^2\|w-w_N\|_{E_s}^2.
  \]
  The zero residual is immediate. The right side tends to zero, giving
  the first identity in~\eqref{E:variance-square-columns}. For the second,
  project $z$ instead and use the singleton input bound
  \eqref{E:wave-input-variance}. A fixed countable Schwartz orthonormal
  basis and Parseval show basis independence of the constructed limits.

  Continuous linear functionals of the limits, and finite linear
  combinations of such functionals, are $L^2$ limits of centered Gaussian
  variables with convergent variances. Their characteristic functions
  therefore converge to those of centered Gaussians. The same reasoning
  after the bounded input extension proves joint Gaussianity for arbitrary
  fixed inputs and finite families of the two maps.
  This proves Proposition~\ref{P:wave-square-columns}.
\end{proof}

These are maps into $L^2(\Omega;E_s)$ for fixed intervals. No common
uncountable almost-sure version, random bounded operator, Hilbert--Schmidt
realization, time path, source convergence or new solution-moment bound
is inferred by this section alone. Both variance directions are retained
in Section~\ref{S:actual-operator-driver}.

===== END TEX FILE: notes/integrated_wave_variance.tex =====

===== BEGIN TEX FILE: notes/integrated_compact_gaussian.tex =====
\section{Finite Gaussian moments and whole-space Sobolev compactness}
\label{S:compact-gaussian}

We prove the finite Gaussian and compact-cutoff estimates needed to
construct the wave driver. All traces and Schatten norms in this section
are unnormalized. The spatial states remain on $\R^d$, $d \in \{1,2,3\}$.
Here $p$ is an auxiliary Schatten and Gaussian-moment index.
The auxiliary periodic space below is used only to factor a compactly
supported multiplication operator. No infinite Gaussian series or time
path is constructed in this section.

\subsection{Finite Gaussian matrices with both variance powers}

\begin{lemma}[Scalar power estimates]\label{L:gaussian-scalar-powers}
  For $0 < \theta < 1$ and $u,v \ge 0$,
  \begin{equation}\label{E:gaussian-weighted-power}
    u^\theta v^{1-\theta} \le \theta u+(1-\theta)v.
  \end{equation}
  Consequently, if $L > 0$ and $0 \le q \le L$ are integers, then for
  real $x,y$,
  \begin{equation}\label{E:gaussian-integer-power}
    |x|^q|y|^{L-q}
    \le \frac qL|x|^L+\frac{L-q}L|y|^L.
  \end{equation}
  For nonnegative finite sequences, the usual H\"older inequality holds
  with exponents $m$ and $m/(m-1)$, $m > 1$. If $Z \ge 0$ has finite
  expectation $F$ and $0 < r < 1$, then $\E Z^r \le F^r$.
\end{lemma}

\begin{proof}
  If $v > 0$, divide~\eqref{E:gaussian-weighted-power} by $v$ and put
  $t = u/v$. The function $\theta t+1-\theta-t^\theta$ decreases to zero
  at one and then increases, by its derivative
  $\theta(1-t^{\theta-1})$. Continuity covers $t = 0$; if $v = 0$ the
  inequality is immediate. For $0 < q < L$, apply this with
  $u = |x|^L$, $v = |y|^L$ and $\theta = q/L$. The endpoint cases
  $q = 0,L$ are identities, with the ordinary integer convention $a^0=1$.

  To prove finite H\"older, divide the two sequences by their respective
  $\ell^m$ and $\ell^{m/(m-1)}$ norms. If either norm vanishes, the result
  is immediate. Apply~\eqref{E:gaussian-weighted-power} with
  $\theta = 1/m$ to the corresponding normalized powers and sum; the
  sum of products is at most one. Undo the normalization. Finally,
  $F = 0$ gives $Z = 0$ almost surely. If $F > 0$, apply
  \eqref{E:gaussian-weighted-power} to $u = Z/F$, $v = 1$ and
  $\theta = r$, and integrate. The right side has expectation one.
  This proves Lemma~\ref{L:gaussian-scalar-powers}.
\end{proof}

\begin{lemma}[Two Hermitian trace bounds]\label{L:gaussian-trace-bounds}
  Let $B,Y$ be finite Hermitian matrices, $m \ge 2$ an integer, and
  $L = 2m-2$. For integers $0 \le q \le L$,
  \begin{equation}\label{E:gaussian-trace-word}
    \operatorname{Re}\operatorname{Tr}(BY^qBY^{L-q})
    \le \operatorname{Tr}(B^2|Y|^L).
  \end{equation}
  If $D \ge 0$ is Hermitian, then
  \begin{equation}\label{E:gaussian-trace-holder}
    \operatorname{Tr}(D|Y|^{2m-2})
    \le (\operatorname{Tr}D^m)^{1/m}
    (\operatorname{Tr}|Y|^{2m})^{(m-1)/m}.
  \end{equation}
\end{lemma}

\begin{proof}
  Diagonalize $Y$, with real eigenvalues $\lambda_i$, and write $b_{ij}$
  for the entries of $B$ in that basis. Hermitian symmetry gives
  $b_{ji} = \overline{b_{ij}}$. The trace word is the real sum
  \[
    \sum_{i,j}|b_{ij}|^2\lambda_j^q\lambda_i^{L-q}.
  \]
  Bound each product by its absolute value and use
  \eqref{E:gaussian-integer-power}. After interchanging $i,j$, the two
  resulting sums agree because $|b_{ij}|=|b_{ji}|$. Each equals
  $\sum_{i,j}|b_{ij}|^2|\lambda_i|^L
  =\operatorname{Tr}(B^2|Y|^L)$. The two weights sum to one, proving
  \eqref{E:gaussian-trace-word}. No commutation of $B$ and $Y$ is used.

  In the same basis put $d_i = D_{ii} \ge 0$. If $\theta_j$ are the
  nonnegative eigenvalues of $D$, a unitary change of basis gives
  $d_i=\sum_j|U_{ij}|^2\theta_j$. Both row and column sums of
  $|U_{ij}|^2$ equal one. Finite convexity therefore yields
  \[
    \sum_i d_i^m \le \sum_{i,j}|U_{ij}|^2\theta_j^m
    = \operatorname{Tr}D^m.
  \]
  For completeness, the convexity step follows from
  $t^m \ge s^m+ms^{m-1}(t-s)$ for $s,t \ge 0$, obtained by differentiating
  the difference. Average this inequality with $s$ equal to the weighted
  mean. Now apply finite H\"older from Lemma~\ref{L:gaussian-scalar-powers}
  to $\sum_i d_i|\lambda_i|^{2m-2}$. Since
  $(2m-2)m/(m-1)=2m$, the last display proves
  \eqref{E:gaussian-trace-holder}, including zero sums.
  This proves Lemma~\ref{L:gaussian-trace-bounds}.
\end{proof}

\begin{proposition}[Finite Gaussian matrix moment]\label{P:finite-gaussian-matrix}
  Let $A_1,\ldots,A_N$ be complex $o$-by-$n$ matrices, with $o,n,N \ge 1$,
  and let $g_k$ be independent real standard Gaussians. Put
  \[
    X=\sum_k g_kA_k,\qquad V_{\rm out}=\sum_k A_kA_k^*,
    \qquad V_{\rm in}=\sum_k A_k^*A_k.
  \]
  For even $p=2m \ge 2$, with $\|A\|_{S_p}^p=\operatorname{Tr}((A^*A)^m)$,
  \begin{align}
    (\E\|X\|_{S_p}^p)^{1/p}
    &\le \sqrt{p-1}\left(
    \frac{\operatorname{Tr}V_{\rm out}^m+
    \operatorname{Tr}V_{\rm in}^m}{2}\right)^{1/p}
    \label{E:finite-gaussian-average}\\
    &\le \sqrt{p-1}\max\left(
    \|V_{\rm out}^{1/2}\|_{S_p},\|V_{\rm in}^{1/2}\|_{S_p}\right).
    \label{E:finite-gaussian-maximum}
  \end{align}
  The constants are independent of $o,n,N$. The first inequality is an
  equality at $p=2$. Empty or zero families give the zero identity.
\end{proposition}

\begin{proof}
  First suppose $B_k$ are Hermitian and put $Y=\sum_k g_kB_k$ and
  $D=\sum_k B_k^2$. All polynomial moments are finite because Gaussian
  decay dominates every fixed power. Componentwise integration by parts
  against the product Gaussian density gives
  $\E[g_kP(g)]=\E[\partial_kP(g)]$, with zero boundary terms. It applies
  to complex polynomials through their real and imaginary parts; absolute
  polynomial integrability justifies Fubini.

  For $m \ge 2$, put $F=\E\operatorname{Tr}Y^{2m}$ and $L=2m-2$.
  Write $\operatorname{Tr}Y^{2m}=\sum_k g_k
  \operatorname{Tr}(B_kY^{2m-1})$ and differentiate the $2m-1$ factors
  in their order. This gives exactly
  \[
    F=\sum_k\sum_{q=0}^{L}
    \E\operatorname{Tr}(B_kY^qB_kY^{L-q}).
  \]
  The eigenbasis calculation above shows these traces are real.
  The differentiated polynomial is real by conjugation and trace cyclicity.
  No derivative of a spectral absolute value or measurable choice of an
  eigenbasis is needed. The two trace bounds give
  \begin{align*}
    F&\le (2m-1)\E\operatorname{Tr}(D|Y|^{2m-2})\\
    &\le (2m-1)(\operatorname{Tr}D^m)^{1/m}
    \E(\operatorname{Tr}|Y|^{2m})^{(m-1)/m}\\
    &\le (2m-1)(\operatorname{Tr}D^m)^{1/m}F^{(m-1)/m}.
  \end{align*}
  Here $\operatorname{Tr}|Y|^{2m}=\operatorname{Tr}Y^{2m}$, and the last
  inequality is the expectation bound in Lemma~\ref{L:gaussian-scalar-powers}.
  If $F=0$ the conclusion is immediate. Otherwise divide by its positive
  fractional power and raise to $m$ to obtain
  \begin{equation}\label{E:finite-hermitian-gaussian}
    \E\operatorname{Tr}Y^{2m} \le (2m-1)^m\operatorname{Tr}D^m.
  \end{equation}
  For $m=1$, independence gives directly
  $\E\operatorname{Tr}Y^2=\sum_k\operatorname{Tr}B_k^2
  =\operatorname{Tr}D$, proving the same formula as equality.

  For rectangular $A_k$, use the Hermitian dilation
  \[
    B_k=\begin{pmatrix}0&A_k\\A_k^*&0\end{pmatrix},\qquad
    Y=\begin{pmatrix}0&X\\X^*&0\end{pmatrix},\qquad
    D=\operatorname{diag}(V_{\rm out},V_{\rm in}).
  \]
  Finite entrywise summation proves $\operatorname{Tr}(UV)=\operatorname{Tr}(VU)$
  for compatible rectangular matrices. Since
  $(XX^*)^m=X(X^*X)^{m-1}X^*$, it follows that
  \[
    \operatorname{Tr}Y^{2m}=2\operatorname{Tr}((X^*X)^m),\qquad
    \operatorname{Tr}D^m=\operatorname{Tr}V_{\rm out}^m+
    \operatorname{Tr}V_{\rm in}^m.
  \]
  Substitute in~\eqref{E:finite-hermitian-gaussian}, divide by two and
  take the $p$th root. This proves~\eqref{E:finite-gaussian-average}.
  For positive $V$, spectral diagonalization gives
  $\|V^{1/2}\|_{S_p}^p=\operatorname{Tr}V^m$, and the average of two
  nonnegative numbers is bounded by their maximum. At $p=2$,
  $\E\operatorname{Tr}X^*X=\operatorname{Tr}V_{\rm in}
  =\operatorname{Tr}V_{\rm out}$, proving the claimed equality.
  This proves Proposition~\ref{P:finite-gaussian-matrix}.
\end{proof}

\begin{remark}[Both variance directions are necessary]
  \label{R:gaussian-one-variance-test}
  Let $n=16$ and $A_k=e_k^{\mathsf T}$ be the coordinate row matrices.
  The only nonzero singular value of $X$ is $(\sum_k g_k^2)^{1/2}$.
  Gaussian integration by parts gives $\E g^2=1$, $\E g^4=3$, and hence
  \[
    \E\|X\|_{S_4}^4=3n+n(n-1)=n(n+2)=288.
  \]
  Here $V_{\rm out}=n$ and $V_{\rm in}=I_n$. Keeping only the input
  variance in~\eqref{E:finite-gaussian-maximum} would give fourth power
  $9\operatorname{Tr}I_n^2=144$, which is false. Transposing the family
  refutes the corresponding output-only bound. The actual average and
  maximum bounds have fourth powers $1224$ and $2304$, respectively.
  This finite example asserts nothing about a specialized wave estimate.
\end{remark}

\subsection{Whole-space cutoffs through an auxiliary periodic space}

Use the unitary Fourier transform with $c_d=(2\pi)^{-d/2}$ and
$\Lambda=(1-\Delta)^{1/2}$. For real $r$, the norm on $H^r(\R^d)$ is
$\|\langle\xi\rangle^r\widehat u\|_2$. The deterministic cutoff arguments
allow any smoothing order $\gamma > 0$. Fix real $\sigma$ and a real compact
smooth $\chi$.
Singular values $s_j$, $j \ge 1$, are counted with multiplicity, with zeros
appended when necessary. For compact $K$, put
$\|K\|_{S_p}^p=\sum_j s_j(K)^p$.

\begin{lemma}[Cutoff factorization]\label{L:cutoff-factorization}
  Choose a cube $Q_L=(-L/2,L/2)^d$ containing $\operatorname{supp}\chi$
  in its interior, and a real $\psi \in C_c^\infty(Q_L)$ equal to one
  near $\operatorname{supp}\chi$. On the auxiliary torus $\mathbb T_L$ use
  Lebesgue measure and the orthonormal basis
  \[
    e_k(x)=L^{-d/2}e^{i\kappa_k\cdot x},\qquad
    \kappa_k=2\pi k/L,\qquad k \in \mathbb Z^d,
  \]
  with $\|v\|_{H^r(\mathbb T_L)}^2
  =\sum_k\langle\kappa_k\rangle^{2r}|v_k|^2$. Periodization of $\psi u$
  and multiplication of a periodic function by $\chi$ extend to bounded maps
  \begin{equation}\label{E:cutoff-periodic-maps}
    \mathcal P_\psi:H^r(\R^d)\to H^r(\mathbb T_L),\qquad
    \mathcal E_\chi:H^r(\mathbb T_L)\to H^r(\R^d)
  \end{equation}
  for every real $r$. If $\mathcal I_\gamma$ denotes the identity inclusion
  from $H^{\sigma+\gamma}(\mathbb T_L)$ to $H^\sigma(\mathbb T_L)$, then
  \begin{equation}\label{E:cutoff-whole-space-recovery}
    \mathcal E_\chi\mathcal I_\gamma\mathcal P_\psi u=\chi u,
    \qquad u \in H^{\sigma+\gamma}(\R^d).
  \end{equation}
\end{lemma}

\begin{proof}
  For $x,y \in \R^d$ and real $r$, the elementary inequality
  $\langle x\rangle\le\sqrt{2}\langle y\rangle\langle x-y\rangle$ gives
  \begin{equation}\label{E:cutoff-peetre}
    \left(\frac{\langle x\rangle}{\langle y\rangle}\right)^r
    \le 2^{|r|/2}\langle x-y\rangle^{|r|}.
  \end{equation}
  For negative $r$, interchange $x,y$ before raising to $|r|$. Integration
  by parts gives rapid decay of the Fourier transform of every compact
  smooth cutoff. For any lattice spacing $a > 0$ and $N > d$,
  \begin{equation}\label{E:cutoff-lattice-sum}
    \sup_y\sum_{k\in\mathbb Z^d}\langle y-ak\rangle^{-N}<\infty.
  \end{equation}
  Indeed, translate $y$ into a centered lattice cell, where
  $|y|\le a\sqrt d/2$. For $|k|\ge\sqrt d$ we have
  $|y-ak|\ge a|k|/2$. The remaining terms are finite; the tail converges
  by dyadic lattice counting, since there are at most $C_d2^{jd}$ lattice
  points in the $j$th shell in $k$. More precisely, for
  $|k|\ge\sqrt d$, the preceding inequality gives
  \[
    \langle y-ak\rangle^{-N}
    \le \max(1,2/a)^N\langle k\rangle^{-N}.
  \]
  The comparison-series terms are bounded by $2^{-jN}$ on each dyadic
  $k$-shell. Thus, its convergent geometric sum carries constants depending
  on $a,d,N$, as does~\eqref{E:cutoff-lattice-sum}.

  We use the mixed Schur bound for a kernel whose absolute row and column
  integrals are bounded by $M_1,M_2$. Weighted Cauchy--Schwarz at each
  output point, followed by Tonelli, bounds its squared operator norm by
  $M_1M_2$. The same proof works with counting measure on one side and
  Lebesgue measure on the other, first on dense finite or compact inputs.

  For Schwartz $u$, the $k$th coefficient of its cutoff periodization is
  \[
    (\mathcal P_\psi u)_k
    = L^{-d/2}\int\psi(x)u(x)e^{-i\kappa_k\cdot x}\ud x
    = L^{-d/2}\int\widehat\psi(\kappa_k-\xi)\widehat u(\xi)\ud\xi.
  \]
  The $c_d$ from Fourier inversion cancels the $c_d^{-1}$ in the ordinary
  Fourier integral of $\psi$. After weighting, its exact kernel is
  \[
    L^{-d/2}\left(\frac{\langle\kappa_k\rangle}{\langle\xi\rangle}\right)^r
    \widehat\psi(\kappa_k-\xi).
  \]
  For a finite torus polynomial $v$, the normalized Fourier kernel of
  $\mathcal E_\chi v$ is
  \[
    L^{-d/2}\left(\frac{\langle\xi\rangle}{\langle\kappa_k\rangle}\right)^r
    \widehat\chi(\xi-\kappa_k).
  \]
  There is no additional $c_d$ in this kernel. By
  \eqref{E:cutoff-peetre}, each is bounded in absolute value by a rapidly
  decreasing function of its frequency difference, times a fixed constant.
  One Schur quantity is its $L^1$ integral and the other a uniformly
  translated lattice sum, bounded by~\eqref{E:cutoff-lattice-sum}.
  This proves~\eqref{E:cutoff-periodic-maps}, including negative $r$.

  Smooth compact approximation in weighted Fourier $L^2$ proves Schwartz
  density on $\R^d$; weighted sequence truncation proves polynomial density
  on the torus. Hence, these maps extend uniquely. Their distributional
  meanings follow by testing against compact smooth functions and density:
  each periodic coefficient pairs the distribution with a compact smooth
  test. No point sampling of a rough Fourier function is used. The same
  full-Lebesgue Schur argument proves smooth compact multiplication bounded
  on every whole-space $H^r$.

  For Schwartz $u$, the periodic Fourier series of $\psi u$ converges
  smoothly on the cube. Since $\chi\psi=\chi$ and $\chi$ is supported
  strictly inside the cube, multiplying this series by $\chi$ recovers
  $\chi u$ with no alias term. Both sides are bounded from
  $H^{\sigma+\gamma}(\R^d)$ to $H^\sigma(\R^d)$, using the just-proved
  maps, the inclusion and smooth multiplication. Density proves
  \eqref{E:cutoff-whole-space-recovery} on that full domain.
  This proves Lemma~\ref{L:cutoff-factorization}.
\end{proof}

\begin{proposition}[Whole-space cutoff singular values]\label{P:cutoff-singular-values}
  For real $\sigma$ and $\gamma > 0$, the initially Schwartz-defined
  operator $K_{\chi,\sigma,\gamma}=\Lambda^\sigma\chi\Lambda^{-\sigma-\gamma}$
  extends uniquely to a compact operator on $L^2(\R^d)$, and
  \begin{equation}\label{E:cutoff-singular-values}
    s_j(K_{\chi,\sigma,\gamma})
    \le C_{\chi,\sigma,\gamma,d}j^{-\gamma/d},\qquad j \ge 1.
  \end{equation}
  Consequently, $K_{\chi,\sigma,\gamma}\in S_p$ whenever $p \ge 1$
  and $p\gamma > d$.
\end{proposition}

\begin{proof}
  The zero cutoff is immediate. Fix one cube and cutoff pair $L,\psi$ as
  in Lemma~\ref{L:cutoff-factorization}. Its recovery identity gives
  \[
    K_{\chi,\sigma,\gamma}
    =\Lambda^\sigma\mathcal E_\chi\mathcal I_\gamma
    \mathcal P_\psi\Lambda^{-\sigma-\gamma}.
  \]
  In the weighted torus coordinates, $\mathcal I_\gamma$ is diagonal with
  entries $\langle\kappa_k\rangle^{-\gamma}$. Let $Q_n$ retain
  $|k|_\infty\le n$. Its rank is $(2n+1)^d$, and
  \[
    \|(1-Q_n)\mathcal I_\gamma\|
    \le [1+(2\pi/L)^2(n+1)^2]^{-\gamma/2}\longrightarrow0.
  \]
  Replacing the inclusion by $Q_n\mathcal I_\gamma$ gives finite-rank
  $K_n$ converging in norm to $K_{\chi,\sigma,\gamma}$. This proves
  compactness: finite-dimensional images have finite nets of each positive
  radius, and norm approximation transfers those nets to the limiting image
  of the unit ball.

  Put
  \[
    M=\|\mathcal E_\chi:H^\sigma(\mathbb T_L)\to H^\sigma(\R^d)\|
    \|\mathcal P_\psi:H^{\sigma+\gamma}(\R^d)
    \to H^{\sigma+\gamma}(\mathbb T_L)\|.
  \]
  The outer Bessel maps are unitary. For $j \ge 3^d$, choose
  $n=\lfloor j^{1/d}/4\rfloor$. Then
  \[
    (2n+1)^d\le(j^{1/d}/2+1)^d<j,\qquad
    \|K-K_n\|\le M(2L/\pi)^\gamma j^{-\gamma/d}.
  \]
  The second estimate follows from $n+1>j^{1/d}/4$. For a compact
  operator, every rank less than $j$ approximation $F$ satisfies
  $s_j(K)\le\|K-F\|$: the span of the first $j$ right singular vectors
  contains a unit vector in $\ker F$, on which $\|K\cdot\|\ge s_j(K)$.
  If $s_j(K)=0$ the inequality is immediate. For $j<3^d$ use
  $s_j(K)\le\|K\|\le M$. Thus, one may take
  \[
    C_{\chi,\sigma,\gamma,d}
    =M\max(3^\gamma,(2L/\pi)^\gamma).
  \]
  Finally, $\sum_j j^{-p\gamma/d}$ converges for $p\gamma>d$.
  This proves Proposition~\ref{P:cutoff-singular-values}.
\end{proof}

No uniform support-radius constant or endpoint necessity is asserted in
Proposition~\ref{P:cutoff-singular-values}. The periodic inclusion was only
a factor of the recovered whole-space operator.

\subsection{Balanced adjoints and localized variance envelopes}

For $E=H^{1/2}(\R^d)\times H^{-1/2}(\R^d)$ use the physical unitary
coordinates
\[
  J_0(u,v)=(\Lambda^{1/2}u,\Lambda^{-1/2}v),\qquad
  H=L^2(\R^d;\mathbb C^2).
\]
The frequency map $J$ in Section~\ref{S:wave-variance} is
$(\mathcal F\oplus\mathcal F)J_0$. Let $D_\chi$ multiply both phase
entries and define
\begin{align}
  P_\chi&=J_0D_\chi J_0^{-1},\qquad
  D_\gamma=\operatorname{diag}(\Lambda^{-\gamma},\Lambda^{-\gamma}),
  \label{E:compact-balanced-cutoff}\\
  K_{\rm out}&=P_\chi D_\gamma,\qquad
  K_{\rm in}=P_\chi^*D_\gamma.
  \label{E:compact-two-factors}
\end{align}

\begin{proposition}[Both compact envelopes]\label{P:compact-two-envelopes}
  The operator $P_\chi$ is bounded. For the unitary swap $U(v,w)=(w,v)$,
  \[
    P_\chi^*=UP_\chi U,\qquad K_{\rm in}=UK_{\rm out}U.
  \]
  Both factors are compact and have equal $S_p$ norms for $p \ge 1$,
  $p\gamma>d$. For $p \ge 2$, $p\gamma>d$, the positive compact operators
  \[
    B_{\rm out}=P_\chi D_\gamma^2P_\chi^*=K_{\rm out}K_{\rm out}^*,
    \qquad B_{\rm in}=P_\chi^*D_\gamma^2P_\chi=K_{\rm in}K_{\rm in}^*
  \]
  satisfy
  \begin{equation}\label{E:compact-envelope-traces}
    \operatorname{Tr}B_{\rm out}^{p/2}
    =\operatorname{Tr}B_{\rm in}^{p/2}=\|K_{\rm out}\|_{S_p}^p.
  \end{equation}
\end{proposition}

\begin{proof}
  Put $A_\sigma=\Lambda^\sigma\chi\Lambda^{-\sigma}$.
  The full-Lebesgue Schur argument in Lemma~\ref{L:cutoff-factorization}
  shows boundedness for every real $\sigma$. On Schwartz functions,
  self-adjointness of real multiplication and of the Bessel powers gives
  $A_\sigma^*=A_{-\sigma}$. Density and boundedness extend this to the
  actual Hilbert adjoints. No evenness of $\chi$ is needed. Thus,
  \[
    P_\chi=\operatorname{diag}(A_{1/2},A_{-1/2}),\qquad
    P_\chi^*=\operatorname{diag}(A_{-1/2},A_{1/2})=UP_\chi U.
  \]
  The swap commutes with $D_\gamma$, giving the claimed factor identity.
  The blocks of $K_{\rm out}$ are $K_{\chi,1/2,\gamma}$ and
  $K_{\chi,-1/2,\gamma}$. Proposition~\ref{P:cutoff-singular-values}
  gives compactness and $S_p$ membership. The singular values of their
  direct sum form the multiset union, so
  \[
    \|K_{\rm out}\|_{S_p}^p
    =\|K_{\chi,1/2,\gamma}\|_{S_p}^p+
    \|K_{\chi,-1/2,\gamma}\|_{S_p}^p.
  \]
  Unitary conjugation preserves them. Finally, the positive eigenvalues
  of $KK^*$ and $K^*K$ agree with multiplicity: on an eigenspace with
  eigenvalue $\lambda>0$, the maps $K/\sqrt\lambda$ and $K^*/\sqrt\lambda$
  are inverse isometries. Zero eigenvalues contribute nothing to the trace.
  Summing these scalar powers proves~\eqref{E:compact-envelope-traces}.
  This proves Proposition~\ref{P:compact-two-envelopes}.
\end{proof}

We use the usual positive square root of a bounded positive operator and
the spectral decomposition of compact positive operators. The needed
order argument is recorded explicitly.

\begin{lemma}[Compact positive order and trace]\label{L:compact-positive-order}
  If $A,B$ are bounded self-adjoint operators with $0 \le A \le B$
  and $B$ compact positive, then $A$ is compact and
  its ordered eigenvalues satisfy $\lambda_j(A)\le\lambda_j(B)$, including
  zero padding. Consequently, for $t \ge 1$ with finite $\operatorname{Tr}B^t$,
  \begin{equation}\label{E:compact-positive-trace}
    \operatorname{Tr}A^t\le\operatorname{Tr}B^t.
  \end{equation}
\end{lemma}

\begin{proof}
  Let $Q_n$ be finite spectral projections of $B$ whose tails tend to zero
  in norm. Then
  \[
    \|(1-Q_n)A^{1/2}\|^2
    =\|(1-Q_n)A(1-Q_n)\|
    \le\|(1-Q_n)B(1-Q_n)\|\longrightarrow0.
  \]
  Thus, $A^{1/2}$ is a norm limit of finite-rank operators and is compact,
  as is $A$. For compact positive operators, the max-min formula for
  $\lambda_j$ follows in an eigenbasis: the span of the first $j$
  eigenvectors gives the lower bound for the supremum over $j$-dimensional
  subspaces of their minimum Rayleigh quotient, while every such subspace
  meets the orthogonal complement of the first $j-1$ eigenvectors, giving
  the upper bound. Compare the Rayleigh quotients of $A$ and $B$ to obtain
  the eigenvalue inequality. Sum the ordered scalar powers to prove
  \eqref{E:compact-positive-trace}. No inequality $A^t\le B^t$ is asserted.
  This proves Lemma~\ref{L:compact-positive-order}.
\end{proof}

\begin{proposition}[Localized finite variance bounds]\label{P:localized-finite-variance}
  Suppose finitely many bounded operators $Z_\ell$ on $H$ satisfy
  \begin{equation}\label{E:localized-finite-hypotheses}
    P_\chi Z_\ell=Z_\ell=Z_\ell P_\chi,\qquad
    V_{\rm out}:=\sum_\ell Z_\ell Z_\ell^*\le CD_\gamma^2,\qquad
    V_{\rm in}:=\sum_\ell Z_\ell^*Z_\ell\le CD_\gamma^2,
  \end{equation}
  with $C \ge 0$. If $p \ge 2$ and $p\gamma>d$, every $Z_\ell$ is
  compact in $S_p$, the two variances are compact in $S_{p/2}$, and
  \begin{align}
    V_{\rm out}&\le CB_{\rm out},\qquad V_{\rm in}\le CB_{\rm in},
    \label{E:localized-two-envelopes}\\
    \operatorname{Tr}V_{\rm out}^{p/2},\quad
    \operatorname{Tr}V_{\rm in}^{p/2}
    &\le C^{p/2}\|K_{\rm out}\|_{S_p}^p.
    \label{E:localized-trace-bounds}
  \end{align}
\end{proposition}

\begin{proof}
  Left localization gives $V_{\rm out}=P_\chi V_{\rm out}P_\chi^*$.
  Apply positive congruence to the output bound in
  \eqref{E:localized-finite-hypotheses} to get
  $V_{\rm out}\le CP_\chi D_\gamma^2P_\chi^*=CB_{\rm out}$.
  Right localization similarly gives
  $V_{\rm in}=P_\chi^*V_{\rm in}P_\chi\le CB_{\rm in}$.
  Proposition~\ref{P:compact-two-envelopes} and
  Lemma~\ref{L:compact-positive-order} prove compactness and the two trace
  bounds with $t=p/2$. If $C=0$, both variances and every $Z_\ell$ vanish,
  so all assertions are immediate.

  For each $\ell$, $Z_\ell Z_\ell^*\le V_{\rm out}$ is compact by the
  same lemma. Its finite spectral projections $Q_n$ give
  $\|(1-Q_n)Z_\ell\|^2
  =\|(1-Q_n)Z_\ell Z_\ell^*(1-Q_n)\|\to0$.
  Hence, $Z_\ell$ is compact. Its singular values squared are the nonzero
  eigenvalues of $Z_\ell Z_\ell^*$. Comparing with $V_{\rm out}$ and
  summing proves $Z_\ell\in S_p$ with
  $\|Z_\ell\|_{S_p}^p\le\operatorname{Tr}V_{\rm out}^{p/2}$.
  This proves Proposition~\ref{P:localized-finite-variance}.
\end{proof}

The two localization identities are hypotheses here; an actual noise
coefficient family has not yet been shown to satisfy them. In particular,
$P_\chi$ is not assumed self-adjoint or a projection.

\begin{corollary}[Finite Gaussian operators]\label{C:finite-gaussian-operators}
  Under~\eqref{E:localized-finite-hypotheses}, let $g_\ell$ be independent
  real standard Gaussians. For even $p \ge 2$ with $p\gamma>d$, the finite
  sum $X=\sum_\ell g_\ell Z_\ell$ satisfies
  \begin{equation}\label{E:finite-gaussian-operator-bound}
    (\E\|X\|_{S_p}^p)^{1/p}
    \le\sqrt{p-1}\sqrt C\|K_{\rm out}\|_{S_p}.
  \end{equation}
  Its extended norm is measurable, with finite expectation as displayed.
\end{corollary}

\begin{proof}
  Choose finite-rank orthogonal projections $\Pi_n$ from a countable
  orthonormal basis of $H$, with $\Pi_n\to I$ strongly. Put
  $Z_{\ell,n}=\Pi_nZ_\ell\Pi_n$ and $X_n=\sum_\ell g_\ell Z_{\ell,n}$,
  viewed as matrices on $\operatorname{ran}\Pi_n$. Their output variance
  satisfies
  \[
    \sum_\ell\Pi_nZ_\ell\Pi_nZ_\ell^*\Pi_n
    \le\Pi_nV_{\rm out}\Pi_n,
  \]
  since the difference is
  $\sum_\ell\Pi_nZ_\ell(1-\Pi_n)Z_\ell^*\Pi_n\ge0$.
  The input inequality is identical with adjoints interchanged. Compact
  max-min also gives
  $\lambda_j(\Pi_nV\Pi_n)\le\lambda_j(V)$ for positive compact $V$,
  since Rayleigh subspaces inside $\operatorname{ran}\Pi_n$ form a subset
  of all subspaces. Thus, both variance trace powers of these matrices
  are bounded by $C^{p/2}\|K_{\rm out}\|_{S_p}^p$.

  Proposition~\ref{P:finite-gaussian-matrix} applies to these finite
  complex matrices, the same real independent Gaussians and the even $p$.
  Taking the average of the two already bounded trace powers gives
  \begin{equation}\label{E:finite-gaussian-compression-bound}
    \E\|X_n\|_{S_p}^p
    \le(p-1)^{p/2}C^{p/2}\|K_{\rm out}\|_{S_p}^p.
  \end{equation}
  No factor two is added by this average.

  For each Gaussian coordinate vector, $X$ is a finite sum of compact
  operators. Strong convergence of $\Pi_n$ implies $\Pi_nX\Pi_n\to X$
  in operator norm: approximate $X$ by a finite-rank $F$, use uniform
  strong convergence on the finite-dimensional ranges of $F$ and $F^*$,
  and control the remainder using $\|\Pi_n\|\le1$. Singular values are
  norm-Lipschitz. Indeed, their formula
  \[
    s_j(A)=\inf_{\dim L<j}
    \sup_{v\in L^\perp,\ \|v\|=1}\|Av\|
  \]
  follows from compact singular vectors and gives
  $s_j(A)\le s_j(B)+\|A-B\|$, and the reverse bound by interchanging $A,B$.
  Hence, $s_j(X_n)\to s_j(X)$ for each $j$. Fatou for the nonnegative
  singular-value sum gives
  $\|X\|_{S_p}^p\le\liminf_n\|X_n\|_{S_p}^p$, allowing extended infinity.
  These variables are measurable: the finite Gaussian coordinate map
  into operators is norm-continuous, each singular value is continuous,
  and the norm power is their nonnegative measurable sum. Fatou in
  probability and~\eqref{E:finite-gaussian-compression-bound} prove the
  bound and almost-sure finiteness. No $S_p$-Bochner convergence is assumed.
  This proves Corollary~\ref{C:finite-gaussian-operators}.
\end{proof}

\subsection{A nonzero witness and the need for a compact cutoff}

\begin{proposition}[Whole-space cutoff tests]\label{P:cutoff-boundary-tests}
  If $\chi$ equals one on a nonempty open set, there is a nonzero rank-one
  operator satisfying~\eqref{E:localized-finite-hypotheses} with a finite
  common $C$. On the other hand, $\Lambda^{-\gamma}$ on $L^2(\R^d)$ is
  not compact for any $\gamma > 0$.
\end{proposition}

\begin{proof}
  Choose nonzero real $v,f \in C_c^\infty$ supported inside the plateau,
  and put $\widetilde v=(\Lambda^{1/2}v,0)$ and
  $\widetilde w=(\Lambda^{-1/2}f,0)$. Both are Schwartz. The actual block
  formulas give $P_\chi\widetilde v=\widetilde v$ and
  $P_\chi^*\widetilde w=\widetilde w$. Therefore,
  $Zx=\langle x,\widetilde w\rangle\widetilde v$ satisfies
  $P_\chi Z=Z=ZP_\chi$. Its two variances are
  $\|\widetilde w\|^2\widetilde v\otimes\widetilde v^*$ and
  $\|\widetilde v\|^2\widetilde w\otimes\widetilde w^*$. For any Schwartz
  $a$ and any $x \in H$,
  \[
    |\langle x,a\rangle|
    =|\langle D_\gamma x,D_\gamma^{-1}a\rangle|
    \le\|D_\gamma x\|\|D_\gamma^{-1}a\|.
  \]
  The inverse multiplier is applied only to Schwartz $a$, so it belongs
  to $H$. Apply the inequality with $a=\widetilde v,\widetilde w$ to obtain
  the two variance bounds with
  \[
    C=\max\left(
    \|\widetilde w\|^2\|D_\gamma^{-1}\widetilde v\|^2,
    \|\widetilde v\|^2\|D_\gamma^{-1}\widetilde w\|^2\right)<\infty.
  \]
  This witness uses a plateau; no nonzero family is inferred for every
  compact cutoff or identified with an actual source family.

  For noncompactness, take $f$ with nonzero Gaussian Fourier transform.
  Then $g=\Lambda^{-\gamma}f$ is a nonzero Schwartz function. The images
  of translates of $f$ are the same translates of $g$. With
  $T_hg(x)=g(x-h)$, Plancherel gives
  \[
    \langle T_hg,g\rangle
    =\int e^{-i\xi\cdot h}|\widehat g(\xi)|^2\ud\xi
    =c_d^{-1}\widehat{|\widehat g|^2}(h).
  \]
  This tends to zero because $|\widehat g|^2$ is Schwartz. Choose a large
  spacing so that any two distinct translates in
  the resulting sequence have image distance at least $\|g\|$. The input
  norms are identical, but the images have no Cauchy subsequence. This
  disproves compactness.
  This proves Proposition~\ref{P:cutoff-boundary-tests}.
\end{proof}

Thus, the choice $\chi=1$ cannot be substituted into the compact-cutoff
argument. No necessity at the Schatten endpoint $p\gamma=d$ is asserted.
The results concern finite matrices and conditional finite operator sums.
Actual coefficient localization, compact variance tails, an infinite
Gaussian series and time regularity are proved in
Section~\ref{S:actual-operator-driver}; source and Young identification
are proved in Sections~\ref{S:source-driver-convergence}--\ref{S:constant-phase-young}.
They are not consequences of the finite comparison alone.

===== END TEX FILE: notes/integrated_compact_gaussian.tex =====

===== BEGIN TEX FILE: notes/integrated_actual_operator_driver.tex =====
\section{The actual Gaussian operator driver}
\label{S:actual-operator-driver}

We now construct the first interaction driver on the same probability
space as the original noise. Retain Hypothesis~\ref{H:homog}, set
$a=\alpha_0$, $s=1/2$ and $E_r=H^r(\R^d)\times H^{r-1}(\R^d)$,
and initially use real phases $E=E_s$. Let $H_W$ be the real completion
of $C_c^\infty((0,\infty)\times\R^d)$ modulo its covariance-null tests.
The given isonormal process on it is $W$. If $\Gamma=0$, the driver and
all raw forms are zero, so the conclusions below hold directly. Assume
$\Gamma\ne0$ in the construction.

Choose and fix $R,T>0$ and a real even nonnegative
$\zeta\in C_c^\infty(\R^d)$ equal to one on $B_1$ and zero off $B_2$.
The physical mask is $\zeta_R(x)=\zeta(x/R)$. The free group $S(t)$ and
forms $\ell_R$ are those of Section~\ref{S:wave-variance}; both phase
entries and the continuous zero-frequency sine quotient are retained.
Fix parameters
\begin{equation}\label{E:driver-parameters}
  0<\gamma<\min\left(\frac12,\frac{2-\alpha}{2}\right),\qquad
  \frac12<\theta<\beta<\min\left(1-\frac a2,
  \frac{3-a-\alpha}{2}\right).
\end{equation}
The strict intervals are nonempty. The $C^\theta$ norm is the supremum
norm plus the $\theta$-H\"older seminorm.

\begin{proposition}[Same-noise compact operator path]\label{P:actual-operator-driver}
  There is an orthonormal basis $\{f_j\}$ of $H_W$ with real smooth compact
  test representatives, independent standard real Gaussians $g_j=W(f_j)$,
  and deterministic operators $A_j(0,t)$ on $E$ such that
  \begin{equation}\label{E:driver-path-convergence}
    X_N(t):=\sum_{j\le N}g_jA_j(0,t)\longrightarrow M_R(t)
    \quad\text{in }L^p(\Omega;C^\theta([0,T];\mathcal B(E)))
  \end{equation}
  for every finite $p\ge1$. The limit is a centered Gaussian path on the
  original probability space, starts at zero, and has compact values at
  every time on one probability-one path set. For each fixed real Schwartz
  pair $z,w$ and $t\in[0,T]$,
  \begin{equation}\label{E:driver-raw-row}
    \langle M_R(t)z,w\rangle_E=\ell_R((0,t);z,w)
    \quad\text{in }L^2(\Omega).
  \end{equation}
  Long raw intervals mean their actual completed test, equivalently the
  additive unit-interval construction justified below. Different compact
  smooth test bases give indistinguishable paths on the same $W$.
  For constants $C,c>0$ depending on the fixed data but not the basis or $p$,
  \begin{equation}\label{E:driver-gaussian-norm}
    (\E\|M_R\|_{C^\theta}^p)^{1/p}\le C\sqrt p,\qquad
    \E\exp(c\|M_R\|_{C^\theta}^2)<\infty.
  \end{equation}
  Its complexification has the corresponding sesquilinear raw identity.
  Fixed-interval Schatten moments hold at the admissible even indices in
  \eqref{E:driver-fixed-schatten}. Arbitrary $p$ above refers to
  $\mathcal B(E)$, not arbitrary Schatten indices or a Schatten-valued path.
\end{proposition}

\subsection{A test basis and literal covariance coefficients}

\begin{lemma}[Basis in the prescribed quotient]\label{L:driver-noise-basis}
  The nonzero space $H_W$ is separable and infinite-dimensional. It has
  a real orthonormal basis with compact smooth representatives, whose
  evaluations by $W$ are independent standard real Gaussians.
\end{lemma}

\begin{proof}
  For tests supported in $[0,L]\times K$, with $K$ compact, the physical
  covariance and the temporal Schur bound give the absolute estimate
  \begin{equation}\label{E:driver-test-continuity}
    |\langle F,G\rangle_{H_W}|
    \le |K|\Gamma(K-K)\frac{2L^{1-a}}{1-a}
    \|\|F(t)\|_\infty\|_{L^2(0,L)}
    \|\|G(t)\|_\infty\|_{L^2(0,L)}.
  \end{equation}
  Only spatial differences in $K-K$ contribute. On each rational compact
  box inside positive time, rational step approximations followed by compact
  smooth mollifiers at rational scales give a countable uniformly dense
  test collection, supported in a fixed slightly larger box. The estimate
  proves noise-norm approximation. The union over increasing boxes is dense
  in the test completion. This proves separability without assuming the
  covariance form is injective.

  Choose $L\ge1$ with $0<\Gamma(B_L)<\infty$ and nonnegative compact
  smooth $q\ge1$ on $B_{2L+1}$. Then
  \[
    Q_{\rm sp}:=\int\Gamma(\ud y)\int q(x)q(x-y)\ud x
    \ge |B_{L+1}|\Gamma(B_L)>0,
  \]
  and the compact-support estimate makes it finite. For every real compact
  smooth positive-time $\tau$, the tensor identity is
  \[
    \|\tau\otimes q\|_{H_W}^2=Q_{\rm sp}\|\tau\|_a^2.
  \]
  Here the temporal norm is computed on any finite interval containing
  the support of $\tau$. It is strictly positive for
  signed nonzero $\tau$. Indeed, zero-extend this deterministic test and
  use the positive Laplace factorization from
  Lemma~\ref{L:masked-time-completion} to write
  \begin{align*}
    \|\tau\|_a^2
    &=\frac1{\Gamma_E(a)}\int_0^\infty\lambda^{a-1}
    E_\lambda(\tau)\ud\lambda,\\
    E_\lambda(\tau)
    &=\int_\R 2\lambda\left|\int_r^\infty
    e^{-\lambda(t-r)}\tau(t)\ud t\right|^2\ud r.
  \end{align*}
  Signed exchanges are absolutely integrable on the test support, by the
  temporal Schur estimate. If the norm vanished, some $\lambda>0$ would
  have $E_\lambda=0$. Its inner integral $v(r)$ is continuous and satisfies
  $v'=\lambda v-\tau$. Vanishing almost everywhere makes it identically
  zero and forces $\tau=0$. Thus, infinitely many linearly independent
  compact time bumps inject into $H_W$ after multiplication by $q$.

  Apply Gram--Schmidt to a countable dense real test collection, discarding
  zero residuals in the given null quotient. Infinitude gives an infinite
  basis; each representative is a finite linear combination of compact
  smooth tests. The isonormal identity gives $\E g_jg_k=\delta_{jk}$.
  Joint Gaussian characteristic functions then factor, giving independence
  and unit variances. No physical null direction is removed beyond the
  prescribed quotient, and no $H_W$-valued white Gaussian vector is used.
  This proves Lemma~\ref{L:driver-noise-basis}.
\end{proof}

\begin{lemma}[Actual covariance coefficients]\label{L:driver-covariance-coefficients}
  For each basis representative put
  \begin{equation}\label{E:driver-covariance-coefficient}
    H_{j,R}(t,x)=\zeta_R(x)\int_{u>0}|t-u|^{-a}
    \int\Gamma(\ud y)f_j(u,x-y)\ud u.
  \end{equation}
  These functions are real smooth on finite time-space compacts, supported
  spatially in $B_{2R}$, with bounded derivatives there. For smooth compact
  real positive-time $F$, and also for the admitted wave tests of
  \eqref{E:variance-actual-form},
  \begin{equation}\label{E:driver-literal-covariance}
    \E[W_{\mathbb C}(\zeta_RF)g_j]
    =\int H_{j,R}(t,x)F(t,x)\ud t\ud x.
  \end{equation}
  The coefficient on $t\ge0$ depends only on the $H_W$ class of $f_j$.
\end{lemma}

\begin{proof}
  Extend $f_j$ smoothly by zero in time and substitute $v=t-u$.
  The unmasked expression is
  $\int_\R |v|^{-a}\int\Gamma(\ud y)f_j(t-v,x-y)\ud v$.
  On each compact $(t,x)$ set, the integrand involves only bounded $v$
  and a common compact set of $y$. Local Radon mass and local integrability
  of $|v|^{-a}$ allow every mixed derivative to move onto the smooth test.
  Dominated integration proves smoothness and the derivative bounds.
  Multiplication by $\zeta_R$ gives the stated support. Zero extension is
  only of a deterministic test; no negative-time noise is introduced.

  The physical covariance formula and absolute Fubini give
  \eqref{E:driver-literal-covariance} first for real compact tests. The
  compact difference set in $\Gamma$ and integrable temporal singularity
  justify the exchange. For wave tests use the common-support raw
  approximations of Proposition~\ref{P:actual-wave-form}, converging in
  $L^2$ time in the spatial supremum norm after masking. The left side
  converges by noise Cauchy--Schwarz and the right side by the coefficient's
  boundedness on that support. Real and imaginary parts give the complex
  version. If two representatives give the same class, their Gaussian
  difference is zero. Testing the covariance identity against every compact
  smooth $F$ makes the difference of their masked coefficients zero as a
  distribution for $t>0$. Smoothness, then continuity at zero, proves the
  representative assertion on $t\ge0$.
  This proves Lemma~\ref{L:driver-covariance-coefficients}.
\end{proof}

\subsection{Gain, adjoints and actual localization}

\begin{lemma}[Deterministic coefficient operators]\label{L:driver-gain-localization}
  For $I\subset[0,T]$, the statewise integral
  \begin{equation}\label{E:driver-coefficient-operator}
    A_j(I)z=\int_I S(-t)B(H_{j,R}(t))S(t)z\ud t
  \end{equation}
  satisfies, for every real $r$,
  \begin{equation}\label{E:driver-gain-one}
    \|A_j(I)\|_{\mathcal B(E_r,E_{r+1})}
    \le C_{j,r,R,T}|I|.
  \end{equation}
  Its $E_s$ adjoint has the gain
  $E_{2s-r-1}\to E_{2s-r}$, so both operators act from $E_{s-\gamma}$
  to $E$. Choose real compact smooth $\chi=1$ on $B_{2R+T+1}$.
  On every $E_r$,
  \begin{equation}\label{E:driver-actual-localization}
    D_\chi A_j(I)=A_j(I)=A_j(I)D_\chi.
  \end{equation}
  For each fixed Schwartz pair,
  \begin{equation}\label{E:driver-covariance-row}
    \E[g_j\ell_R(I;z,w)]=\langle A_j(I)z,w\rangle_E.
  \end{equation}
\end{lemma}

\begin{proof}
  The full massless wave is strongly continuous and bounded on every
  $E_r$ on finite time intervals. Its normalized off-diagonal Fourier
  entries have sizes at most $C_T$ and one, respectively; continuity and
  domination prove the strong assertion. Multiplication by $H_{j,R}(t)$
  is bounded on every $H^r$, continuously in $t$, by weighted Fourier
  convolution and its compact smooth derivative bounds. Hence,
  $B(H_{j,R}(t)):E_r\to E_{r+1}$ is bounded: its second entry is a
  multiplier of the displacement in $H^r$. The integrand in
  \eqref{E:driver-coefficient-operator} is strongly continuous with values
  in $E_{r+1}$ for each input in $E_r$, and uniformly bounded in that
  operator norm. Statewise Bochner integration
  proves~\eqref{E:driver-gain-one}, including the Lipschitz operator-norm
  primitive $A_j(0,t)$. Norm continuity of $S(t)$ is not needed.

  Under the $E_s$ pairing, the dual of $E_r$ is isometrically
  $E_{2s-r}$, directly by the two Bessel weights. Dualizing the gain-one
  bound therefore gives the asserted adjoint gain. It agrees on Schwartz
  phases with the actual bounded $E_s$ adjoint. Since $\gamma<1$, gain one
  at every index implies the two stated maps from $E_{s-\gamma}$ to $E$.

  For smooth data the free-wave energy on a shrinking ball has nonpositive
  boundary flux: $v\partial_nu-(v^2+|\nabla u|^2)/2\le0$. Vanishing
  initial displacement and velocity give zero velocity and gradient in
  the cone; integration of velocity from the zero displacement gives
  zero displacement there as well. Time reversal gives the backward
  assertion. Thus, both entries of $S(\pm t)$ enlarge supports by at most
  $|t|$. Density and testing against compact smooth functions extend this
  support assertion to Sobolev phases. In particular, for input
  $(1-D_\chi)z$, approximate $z$ by Schwartz phases and retain the factor
  $1-D_\chi$; the approximants vanish on $B_{2R+T+1}$. Their free
  displacement vanishes on $B_{2R}$ throughout $[0,T]$, and the same is
  true in the distributional limit. They contribute nothing to the integral.
  Its output is supported in $B_{2R+T}$, by the support of $H_{j,R}$ and
  backward finite propagation. Since $\chi=1$ on a neighborhood of this
  ball, both identities in~\eqref{E:driver-actual-localization} follow.
  This uses both entries, not a scalar restart or a positivity theorem.

  Finally apply the physical Sobolev pairing
  \eqref{E:variance-physical-adjoint} and
  \eqref{E:driver-literal-covariance} to the state integral. They give
  \eqref{E:driver-covariance-row}. In
  \eqref{E:driver-covariance-coefficient}, the mask is after convolution;
  replacing it by a mask inside $\Gamma*f_j$ would change this identity.
  This proves Lemma~\ref{L:driver-gain-localization}.
\end{proof}

\subsection{Actual finite variances and first-chaos tails}

Put $J_0(u,v)=(\Lambda^{1/2}u,\Lambda^{-1/2}v)$,
$H_0=L^2(\R^d;\R^2)$, $a_j=J_0A_j(I)J_0^{-1}$ and
$P_\chi=J_0D_\chi J_0^{-1}$. The operator
$D_\gamma=\operatorname{diag}(\Lambda^{-\gamma},\Lambda^{-\gamma})$
acts on these physical coordinates. Its two compact envelopes
$B_{\rm out},B_{\rm in}$ are those of
Proposition~\ref{P:compact-two-envelopes}, after complexification when
Schatten norms are used. For $I\subset[0,T]$ with $0<h=|I|\le1$, set
\begin{equation}\label{E:driver-short-variance-budget}
  b_I=C_T h^{2-a}B_\alpha(h),
\end{equation}
where $C_T$ is the uniform-in-$R$ constant in
Proposition~\ref{P:wave-two-variances}.

\begin{lemma}[Both actual variances and their tails]\label{L:driver-actual-variances}
  For every $N$,
  \begin{equation}\label{E:driver-two-variances}
    V_{{\rm out},N}:=\sum_{j\le N}a_ja_j^*\le b_ID_\gamma^2,
    \qquad V_{{\rm in},N}:=\sum_{j\le N}a_j^*a_j\le b_ID_\gamma^2.
  \end{equation}
  The finite families satisfy both actual localizations by $P_\chi$.
  There are bounded positive limits $V_{{\rm out},\infty},V_{{\rm in},\infty}$
  with positive tails $T_{{\rm out},N},T_{{\rm in},N}\to0$ strongly, and
  \begin{equation}\label{E:driver-compact-tail-envelopes}
    T_{{\rm out},N}\le b_IB_{\rm out},\qquad
    T_{{\rm in},N}\le b_IB_{\rm in}.
  \end{equation}
  For each fixed $z\in E_{s-\gamma}$, the real column maps satisfy
  \begin{equation}\label{E:driver-column-expansions}
    m_{R,I}(z)=\sum_jg_jA_j(I)z,\qquad
    n_{R,I}(z)=\sum_jg_jA_j(I)^{*,E}z
    \quad\text{in }L^2(\Omega;E).
  \end{equation}
\end{lemma}

\begin{proof}
  By~\eqref{E:driver-covariance-row}, for real Schwartz $z,w$,
  \[
    \langle X_N(I)z,w\rangle_E
    =\sum_{j\le N}g_j\E[g_j\ell_R(I;z,w)]
    =\mathcal P_N\ell_R(I;z,w),
  \]
  where $\mathcal P_N$ is the orthogonal projection in $L^2(\Omega)$
  onto the span of $g_1,\ldots,g_N$. In particular,
  \[
    \sum_{j\le N}|\langle A_j(I)z,w\rangle_E|^2
    =\E|\langle X_N(I)z,w\rangle_E|^2
    \le\E|\ell_R(I;z,w)|^2.
  \]
  These are projections onto the actual noise-test basis, not source
  regularizations. The two variance bounds of
  Proposition~\ref{P:wave-two-variances}, with the mean-square columns
  of Proposition~\ref{P:wave-square-columns}, apply to these same raw
  forms and the budget~\eqref{E:driver-short-variance-budget}.

  Choose a real Schwartz orthonormal basis $\{e_k\}$ of $E$.
  Fix real Schwartz $w$. For every finite phase truncation $K$,
  \[
    \begin{split}
      \sum_{k\le K}\sum_{j\le N}
      |\langle A_j(I)e_k,w\rangle_E|^2
      &=\sum_{k\le K}\E|\langle X_N(I)e_k,w\rangle_E|^2\\
      &\le\sum_{k\le K}\E|\ell_R(I;e_k,w)|^2
      \le b_I\|w\|_{E_{s-\gamma}}^2,
    \end{split}
  \]
  by~\eqref{E:wave-input-variance}. Let $K\to\infty$.
  Parseval in the phase space and nonnegative monotone convergence,
  with $N$ still finite, give
  \[
    \sum_{j\le N}\|A_j(I)^{*,E}w\|_E^2
    =\E\|X_N(I)^{*,E}w\|_E^2
    \le b_I\|w\|_{E_{s-\gamma}}^2.
  \]
  Conversely, for fixed real Schwartz $z$, use
  \eqref{E:wave-output-variance} with the output basis varying:
  \[
    \begin{split}
      \sum_{k\le K}\sum_{j\le N}
      |\langle A_j(I)z,e_k\rangle_E|^2
      &=\sum_{k\le K}\E|\langle X_N(I)z,e_k\rangle_E|^2\\
      &\le\sum_{k\le K}\E|\ell_R(I;z,e_k)|^2
      \le b_I\|z\|_{E_{s-\gamma}}^2.
    \end{split}
  \]
  The same phase Parseval limit gives
  \[
    \sum_{j\le N}\|A_j(I)z\|_E^2
    =\E\|X_N(I)z\|_E^2
    \le b_I\|z\|_{E_{s-\gamma}}^2.
  \]
  Thus both directions use their respective actual Hilbert-Bessel
  bounds; neither follows from retaining only one variance.

  These inequalities extend at each finite $N$ to the full
  $E_{s-\gamma}$ input space. Indeed,
  Lemma~\ref{L:driver-gain-localization} gives
  $A_j:E_{s-\gamma}\to E_{s+1-\gamma}\subset E$.
  Its adjoint gain, at $r=s+\gamma-1$, gives the same map for
  $A_j^{*,E}$. The inclusion holds since $\gamma<1$.
  Approximate the input by Schwartz phases and pass each of the
  finitely many operator terms to the limit. The resulting constant
  is still $b_I$, independent of $N$; individual $j$-dependent gain
  constants were not summed.
  Restricting to $E$ and using
  $\|z\|_{E_{s-\gamma}}=\|D_\gamma J_0z\|_{H_0}$ gives
  \eqref{E:driver-two-variances} as two operator quadratic inequalities.
  Both localizations follow from~\eqref{E:driver-actual-localization}.
  No self-adjointness or projection property of $P_\chi$ is assumed.

  The coordinates of $m_{R,I}(z)$, for Schwartz $z$, are the literal raw
  forms $\ell_R(I;z,e_k)$ and belong to the closed first chaos $W(H_W)$.
  Their coefficients against $g_j$ are $\langle A_jz,e_k\rangle_E$.
  Parseval in that chaos, followed by Parseval in $E$ and positive Tonelli,
  gives
  \[
    \sum_j\|A_jz\|_E^2=\E\|m_{R,I}(z)\|_E^2,
    \qquad m_{R,I}(z)=\sum_jg_jA_jz\quad\text{in }L^2(\Omega;E).
  \]
  The same argument for the adjoint column gives the other expansion.
  Membership in this first chaos comes from actual linear noise tests,
  not merely Gaussianity. To extend to a fixed $E_{s-\gamma}$ input,
  approximate by Schwartz phases. The finite inequalities extend to that
  space by the gain bounds and have a constant uniform in $N$. Apply them
  to the input difference, then use the Schwartz expansion and continuity
  of $m,n$. This proves~\eqref{E:driver-column-expansions} on the full
  claimed input domain.

  The convergent positive quadratic sums, restricted to $E$ and transported
  by $J_0$, define the bounded positive operators $V_{\cdot,\infty}$ by
  polarization and Riesz. They retain the bounds $b_ID_\gamma^2$.
  Their tails have quadratic forms tending to zero. Since they are uniformly
  bounded and positive,
  $\|T_Nv\|^2\le\|T_N\|\langle T_Nv,v\rangle\to0$.
  Passing to the limit in the finite localization identities gives
  \[
    V_{{\rm out},\infty}=P_\chi V_{{\rm out},\infty}P_\chi^*,\qquad
    V_{{\rm in},\infty}=P_\chi^*V_{{\rm in},\infty}P_\chi,
  \]
  and the same identities for their tails. Positive congruence applied to
  $T_N\le b_ID_\gamma^2$ proves~\eqref{E:driver-compact-tail-envelopes}.

  Complexification preserves these statements and constants. The Hilbert
  norms split into real and imaginary squared norms; real operators extend
  isometrically. A real orthonormal basis complexifies to a complex
  orthonormal basis, preserving singular values and multiplicities. The
  complex column maps have the same bounds and sesquilinear row identities.
  This proves Lemma~\ref{L:driver-actual-variances}.
\end{proof}

\begin{lemma}[Compact domination of positive tails]\label{L:driver-dominated-tails}
  If $0\le T_N\le B$, with positive compact $B\in S_m$, $m\ge1$, and
  $T_N\to0$ weakly, then
  \begin{equation}\label{E:driver-trace-tails}
    \|T_N\|\longrightarrow0,\qquad \operatorname{Tr}T_N^m\longrightarrow0.
  \end{equation}
\end{lemma}

\begin{proof}
  Choose a finite spectral projection $Q$ of $B$ with
  $\|(1-Q)B(1-Q)\|<\epsilon$. Positive quadratic Cauchy--Schwarz gives,
  for unit $x$,
  \[
    \langle T_Nx,x\rangle
    \le2\langle T_NQx,Qx\rangle
    +2\langle T_N(1-Q)x,(1-Q)x\rangle
    \le2\|QT_NQ\|+2\epsilon.
  \]
  Weak convergence makes the finite-dimensional matrix $QT_NQ$ converge
  in norm to zero. Letting $\epsilon\downarrow0$ proves norm convergence.
  Lemma~\ref{L:compact-positive-order} gives
  $\lambda_j(T_N)\le\lambda_j(B)$, while each $\lambda_j(T_N)\to0$ by
  norm convergence. Dominated summation of $\lambda_j(B)^m$ proves the
  trace limit. No order comparison of the operator powers is used.
  This proves Lemma~\ref{L:driver-dominated-tails}.
\end{proof}

\begin{lemma}[Retained finite Gaussian variance powers]\label{L:driver-gaussian-tail-average}
  Let $Z_\ell$ be finitely many compact operators whose two variances
  $V_{\rm out},V_{\rm in}$ belong to $S_{q/2}$, for an even $q\ge2$.
  With independent standard real $g_\ell$,
  \begin{equation}\label{E:driver-retained-gaussian-average}
    \E\left\|\sum_\ell g_\ell Z_\ell\right\|_{S_q}^q
    \le(q-1)^{q/2}\frac{\operatorname{Tr}V_{\rm out}^{q/2}
    +\operatorname{Tr}V_{\rm in}^{q/2}}2.
  \end{equation}
\end{lemma}

\begin{proof}
  Compress by finite-rank orthogonal $Q_k\to I$ strongly. The compressed
  output variance is at most $Q_kV_{\rm out}Q_k$, since their difference
  is $\sum_\ell Q_kZ_\ell(1-Q_k)Z_\ell^*Q_k\ge0$; the input inequality
  is the same with adjoints interchanged. Positive-order and compression
  max-min compare their trace powers with the uncompressed ones.
  Apply Proposition~\ref{P:finite-gaussian-matrix} on the finite range,
  retaining the average. For each finite Gaussian coordinate vector,
  compactness gives operator-norm convergence of the compressed sum to
  the original sum. The singular-value norm-Lipschitz argument in the proof
  of Corollary~\ref{C:finite-gaussian-operators}, then Fatou over singular
  values and probability, proves the displayed bound. The extended norm
  is measurable by the same finite-coordinate continuity argument.
  No infinite Gaussian series or $S_q$-Bochner convergence is assumed.
  This proves Lemma~\ref{L:driver-gaussian-tail-average}.
\end{proof}

\subsection{Actual interval limits on the given probability space}

\begin{lemma}[Fixed-interval operator construction]\label{L:driver-interval-limit}
  For each fixed short interval $I$, $X_N(I)$ converges in every finite
  $L^p(\Omega;\mathcal B(E))$ to a compact-valued centered Gaussian
  operator $X_R(I)$ on the original probability space. For every admissible
  even $q\ge2$, $q\gamma>d$,
  \begin{equation}\label{E:driver-fixed-schatten}
    (\E\|X_R(I)\|_{S_q}^q)^{1/q}
    \le\sqrt{q-1}\sqrt{C_T}\,h^{1-a/2}B_\alpha(h)^{1/2}
    \|K_\chi\|_{S_q},\qquad K_\chi=P_\chi D_\gamma.
  \end{equation}
  Its fixed Schwartz rows equal the actual raw forms in $L^2$.
\end{lemma}

\begin{proof}
  The actual finite families $a_j$, $j\le N$, satisfy every hypothesis
  of Proposition~\ref{P:localized-finite-variance} and
  Corollary~\ref{C:finite-gaussian-operators}: both localizations,
  both weighted variances and the independent real $g_j$ have been
  proved in Lemma~\ref{L:driver-actual-variances}.
  Thus the coefficients are compact, and their finite Gaussian sums
  satisfy~\eqref{E:driver-fixed-schatten}, uniformly in $N$.
  The fixed cutoff norm may depend on $R,T$.

  Fix an admissible even $q\ge2$, $q\gamma>d$.
  Both positive compact envelopes in
  \eqref{E:driver-compact-tail-envelopes} belong to $S_{q/2}$.
  Lemma~\ref{L:driver-dominated-tails} therefore gives
  \[
    \operatorname{Tr}T_{{\rm out},N}^{q/2}\longrightarrow0,
    \qquad
    \operatorname{Tr}T_{{\rm in},N}^{q/2}\longrightarrow0.
  \]
  For $M>N$, put
  $Y_{N,M}=\sum_{j=N+1}^Mg_jA_j(I)$.
  After the unitary $J_0$ transport, its two finite variances are
  \[
    V_{{\rm out},M}-V_{{\rm out},N}\le T_{{\rm out},N},\qquad
    V_{{\rm in},M}-V_{{\rm in},N}\le T_{{\rm in},N}.
  \]
  Lemma~\ref{L:driver-gaussian-tail-average} and positive eigenvalue
  max-min comparison now give the uniform tail estimate
  \[
    \sup_{M>N}\E\|Y_{N,M}\|_{S_q}^q
    \le(q-1)^{q/2}
    \frac{\operatorname{Tr}T_{{\rm out},N}^{q/2}
    +\operatorname{Tr}T_{{\rm in},N}^{q/2}}2
    \longrightarrow0.
  \]
  The average of the two trace powers is retained. The comparison
  uses eigenvalues, not operator monotonicity of the $q/2$ power.
  Since $\|Y_{N,M}\|\le\|Y_{N,M}\|_{S_q}$, this proves genuine
  $L^q(\Omega;\mathcal B(E))$ Cauchy convergence; a uniform moment
  bound alone would not suffice.

  All finite sums lie in the separable operator-norm closed real span
  $\mathcal F_I$ of the countably many deterministic $A_j(I)$.
  Choose $N_k$ increasing so that
  $\|X_{N_{k+1}}(I)-X_{N_k}(I)\|_{L^q\mathcal B(E)}\le2^{-k}$.
  Their $L^1$ norms are summable. Tonelli therefore shows that the
  pointwise operator-norm differences sum absolutely almost surely.
  Completeness gives a limit in $\mathcal F_I$ on the original
  probability space; assign it zero on the exceptional null set.
  It is strongly measurable as a limit of separably valued finite
  Gaussian sums. Fatou and the Cauchy property give convergence of
  the whole sequence in $L^q$ to this limit $X_R(I)$.
  No new noise or probability space has been introduced.
  Limits constructed at different admissible even indices agree by
  uniqueness of convergence in probability. For each requested
  finite $p\ge1$, choose an admissible even $q\ge p$ and use
  Lyapunov to obtain $L^p$ operator-norm convergence to that same limit.
  One fixed Schatten index is not used to infer all moment orders.

  The compact operators are norm closed, so an almost surely
  norm-convergent subsequence makes $X_R(I)$ compact valued.
  Singular-value Fatou applied to the finite uniform bound gives
  \eqref{E:driver-fixed-schatten} at each admissible even $q$.
  Every continuous real linear functional of $X_R(I)$ is an $L^2$
  limit of centered finite Gaussian sums; convergence of means,
  variances and characteristic functions makes it centered Gaussian.
  The same applies to finite linear combinations of these functionals,
  proving joint Gaussianity on the given space.

  For each fixed real Schwartz $z,w$, the scalar rows
  $\langle X_N(I)z,w\rangle_E$ are the orthogonal projections of
  the actual completed raw form $\ell_R(I;z,w)$ onto the complete
  noise basis. That form lies in the original closed first chaos,
  so these projections converge to it in $L^2(\Omega)$.
  Operator-norm $L^2$ convergence also gives convergence to
  $\langle X_R(I)z,w\rangle_E$. Uniqueness of the $L^2$ limit
  identifies these two actual variables on the same space, not
  merely their laws.

  For a fixed long interval, choose a finite partition into intervals
  of length at most one. Their actual indicator tests add to the
  long-interval test except at finitely many endpoints. The masked
  wave products have common compact spatial support, and the temporal
  estimate~\eqref{E:driver-test-continuity} makes those endpoint
  changes have zero raw norm. Raw completion and linearity give
  exact additivity of the actual forms. The deterministic statewise
  coefficient integrals, hence every $X_N$, add on the same partition.
  Passing their finite-sum $L^p$ limits gives the corresponding
  operator additivity and raw-row identity, independently of the
  partition by common refinement. These are statements at each
  fixed interval and partition; no uncountable intersection of
  independently selected null sets is used.
  No long-interval version of the short-$h$ bound is asserted.
  The Schatten conclusion is a fixed-interval moment at admissible
  even indices, not a Schatten-valued path or arbitrary-index claim.
  This proves Lemma~\ref{L:driver-interval-limit}.
\end{proof}

\subsection{Time-path convergence and Gaussian norm bounds}

\begin{lemma}[Actual H\"older path limit]\label{L:driver-holder-limit}
  The finite paths $X_N(t)=X_N((0,t))$ converge in
  $L^p(\Omega;C^\theta([0,T];\mathcal B(E)))$ for every finite $p\ge1$,
  in a separable closed path span on the same probability space. The limit
  starts at zero and has compact values for all times on one path event.
  For sufficiently large even $q_0$, its $C^\theta$ norm has
  $L^q$ bound $C\sqrt q$, uniformly over even $q\ge q_0$ and the basis.
\end{lemma}

\begin{proof}
  Choose $\theta<\eta<\beta$ and an even $q_0\ge2$ with
  $q_0\gamma>d$ and $\beta-\eta-1/q_0>0$. For $q\ge q_0$, the
  singular-value sequence gives
  $\|K_\chi\|_{S_q}\le\|K_\chi\|_{S_{q_0}}$: if the latter is nonzero,
  normalize by it, so every singular value is at most one, and sum its
  $q$th powers. The zero case is immediate. Apply the finite Gaussian
  operator estimate with the time-refined actual variances from
  Proposition~\ref{P:wave-two-variances}. This gives, uniformly in $N$
  and even $q\ge q_0$,
  \begin{equation}\label{E:driver-increment-moments}
    \|X_N(t)-X_N(u)\|_{L^q(\mathcal B(E))}
    \le C\sqrt q\,|t-u|^\beta,\qquad |t-u|\le1.
  \end{equation}
  The constant includes the fixed $S_{q_0}$ cutoff norm and does not
  depend on $q$. Longer increments are finite sums of unit increments,
  with constants depending on $T$.

  Let $D_n(F)$ be the maximum of adjacent increments on the grid
  $kT2^{-n}$, $0\le k\le2^n$. At fine levels $T2^{-n}\le1$, the
  elementary bound for a finite maximum yields
  \[
    \|D_n(X_N)\|_{L^q}
    \le 2^{n/q}C\sqrt q\,(T2^{-n})^\beta.
  \]
  No independence of these increments is used. The finitely many coarse
  levels are controlled by unit partitions. Minkowski and a geometric
  sum therefore give
  \begin{equation}\label{E:driver-dyadic-moment-sum}
    \sup_N\left\|\sum_{n\ge0}2^{n\eta}D_n(X_N)\right\|_{L^q}
    \le C_\eta\sqrt q,
  \end{equation}
  since the fine-level ratio is at most
  $2^{-(\beta-\eta-1/q_0)}<1$.

  For a continuous Banach-valued $F$ starting at zero, this weighted
  dyadic sum controls its $C^\eta$ norm. Approximate two times by dyadic
  points at a scale comparable to their separation. The two grid points
  differ by at most two adjacent increments, and each endpoint's finer
  binary corrections are bounded by the tail sum of $D_n$. Multiplying
  by the separation to the power $-\eta$ bounds that total by the weighted
  sum, up to a constant depending on $T,\eta$. Continuity identifies the
  endpoint limits and also controls the supremum norm from $F(0)=0$.
  The finite paths are Lipschitz by~\eqref{E:driver-gain-one}. Thus,
  \eqref{E:driver-dyadic-moment-sum} gives uniform $L^qC^\eta$ bounds,
  and the triangle inequality gives the same bound for their differences.

  On a fixed finite time grid, Lemma~\ref{L:driver-interval-limit} gives
  $L^q$ convergence of every point value. For continuous $F$,
  \[
    \|F\|_\infty\le\max_k\|F(t_k)\|
    +C(\operatorname{mesh})^\eta\|F\|_{C^\eta}.
  \]
  Apply this to $X_N-X_M$, send $N,M\to\infty$ at a fixed grid, and
  then send the mesh to zero. The uniform $C^\eta$ bound proves sup-norm
  $L^q$ Cauchy convergence. The deterministic interpolation inequality
  \begin{equation}\label{E:driver-holder-interpolation}
    \|F\|_{C^\theta}
    \le C\|F\|_\infty^{1-\theta/\eta}
    \|F\|_{C^\eta}^{\theta/\eta}
  \end{equation}
  follows by bounding each increment by both $2\|F\|_\infty$ and its
  $C^\eta$ bound, and splitting at their balancing scale. Its supremum
  term is controlled too. Scalar H\"older in probability proves the
  $L^qC^\theta$ Cauchy property. For any requested finite $p$, choose an
  even $q\ge\max(p,q_0)$ and use Lyapunov.

  The full H\"older/operator space need not be separable. Nevertheless,
  every finite path lies in the span of the countably many deterministic
  Lipschitz paths $A_j(0,\cdot)$. Their $C^\theta$-closed real span is a
  separable Banach space. In it the same elementary Cauchy/subsequence
  construction as in Lemma~\ref{L:driver-interval-limit} gives a strongly
  measurable limit $M_R$ on the original space. Different $p$ limits agree
  by uniqueness of convergence in probability in the path norm. An almost
  surely $C^\theta$-convergent subsequence converges uniformly in operator
  norm. Finite paths have compact values on short intervals, and on long
  ones by finite additivity. Therefore, the limit has compact values at
  every time on that single path set. It starts at zero. Passing the
  uniform bounds from~\eqref{E:driver-dyadic-moment-sum} through the path
  convergence proves the asserted $C\sqrt q$ bound.
  This proves Lemma~\ref{L:driver-holder-limit}.
\end{proof}

\begin{proof}[Proof of Proposition~\ref{P:actual-operator-driver}]
  Lemmas~\ref{L:driver-noise-basis}--\ref{L:driver-holder-limit} construct
  the stated finite sums and their path limit, with no new probability
  space. Evaluation at a fixed time agrees with the interval limit by
  uniqueness in probability. Its raw row identity is
  \eqref{E:driver-raw-row}, by Lemma~\ref{L:driver-interval-limit}, including
  the long-interval interpretation. The same additivity identifies each
  fixed increment with $X_R(I)$, proving its stated Schatten moment bound.

  The finite paths are Gaussian linear combinations of deterministic paths.
  Every continuous linear functional on their closed path span converges
  in $L^2$ to a centered Gaussian; finite linear combinations do as well.
  Thus, $M_R$ is a centered Gaussian path. The four real pair identities
  give its complexified sesquilinear row identity.

  The construction used only compact smooth representatives, orthonormality
  and completeness, so it applies to any such noise basis. Compare two
  constructions using a fixed countable dense Schwartz phase collection
  and rational times. Both rows equal the same original raw forms.
  A countable null-set union, boundedness of the operators, phase density
  and path continuity give equality at all times on one probability-one
  set. This proves indistinguishability without an assumed common event
  for uncountably many raw evaluations.

  For $p\ge1$, choose even $q\ge\max(p,q_0)$ with
  $q\le p+q_0+2\le(q_0+3)p$. Lemma~\ref{L:driver-holder-limit} and
  Lyapunov give the first bound in~\eqref{E:driver-gaussian-norm}.
  Write its resulting constant as $C_1$ and let $Y=\|M_R\|_{C^\theta}$.
  If $C_1=0$, then $Y=0$ almost surely and the exponential bound is
  immediate. Otherwise,
  $\E Y^{2m}\le(C_1\sqrt{2m})^{2m}$. Since
  $m!\ge(m/e)^m$, as follows by integrating $\log x$ from one to $m$,
  the $m$th term in the exponential series is at most
  $(2ecC_1^2)^m$. For $0<c<1/(2eC_1^2)$, positive Tonelli and the
  geometric series prove the second bound.
  This proves Proposition~\ref{P:actual-operator-driver}.
\end{proof}

All constants here may depend on $R,T$ and the fixed admissible parameters.
No uniform-in-$R$ path-norm estimate or $C^\theta S_q$-valued path is
asserted. This constructs the local masked first driver on the original
noise. Source-cutoff convergence, Young evolution, canonical initial data
and solution-moment asymptotics remain separate parts of the argument.

===== END TEX FILE: notes/integrated_actual_operator_driver.tex =====

===== BEGIN TEX FILE: notes/integrated_source_convergence.tex =====
\section{Convergence of the canonical Gaussian source drivers}
\label{S:source-driver-convergence}

[held back until the source author has been told]

Retain Hypothesis~\ref{H:homog}, the fixed $R,T,\zeta_R,E$ and parameters
of~\eqref{E:driver-parameters}, and the original noise space $H_W$.
Write $\mathscr B_\theta=C^\theta([0,T];\mathcal B(E))$.
Fix one raw test basis $f_j$ and its actual coefficient paths $A_j(t)$
from Proposition~\ref{P:actual-operator-driver}. Thus,
$M_N=\sum_{j\le N}W(f_j)A_j\to M_R$ in every finite $L^p(\mathscr B_\theta)$.
Zero covariance gives zero noises and drivers throughout; assume
$\Gamma\ne0$ in the construction.

\subsection{Gaussian transfer in the full path norm}

\begin{lemma}[Finite Gaussian linear images]\label{L:source-finite-comparison}
  Let $v_1,\ldots,v_N$ lie in a real Banach space and let $\xi$ be a
  centered Gaussian vector with covariance bounded by $CI$, $C\ge0$.
  For independent standard real $g_j$ and $p\ge1$,
  \begin{equation}\label{E:source-finite-comparison}
    \left(\E\left\|\sum_j\xi_jv_j\right\|^p\right)^{1/p}
    \le\sqrt C\left(\E\left\|\sum_jg_jv_j\right\|^p\right)^{1/p}.
  \end{equation}
\end{lemma}

\begin{proof}
  The function $\varphi(x)=\|\sum_jx_jv_j\|^p$ is continuous and convex,
  even when the linear image gives only a seminorm on $\R^N$.
  Its Gaussian expectations are finite by the finite-sum bound.
  On an auxiliary space take an independent centered Gaussian $Z$ of
  covariance $CI-\operatorname{Cov}\xi$. Conditional Jensen gives
  $\E\varphi(\xi)\le\E\varphi(\xi+Z)$. The latter vector has the law of
  $\sqrt C\,g$, proving the claim. The case $C=0$ is immediate.
  This auxiliary comparison changes neither the actual coupling of $\xi$
  nor any nonlinear wave solution.
  This proves Lemma~\ref{L:source-finite-comparison}.
\end{proof}

\begin{proposition}[Actual Gaussian transfer and stability]
  \label{P:source-gaussian-transfer}
  Let $Y$ be a centered Gaussian linear noise on smooth compact positive-time
  tests, on a common coupled space, with
  \begin{equation}\label{E:source-raw-variance-bound}
    \operatorname{Var}Y(F)\le C\|F\|_{H_W}^2.
  \end{equation}
  It extends to $H_W$. The finite paths
  $M_{Y,N}=\sum_{j\le N}Y(f_j)A_j$ converge in every finite
  $L^p(\mathscr B_\theta)$ to an actual centered Gaussian path $M_Y$ with
  compact values at all times on one path event, and
  \begin{align}
    \|M_Y-M_{Y,N}\|_{L^p\mathscr B_\theta}
    &\le\sqrt C\|M_R-M_N\|_{L^p\mathscr B_\theta},\label{E:source-transfer-tail}\\
    \|M_Y\|_{L^p\mathscr B_\theta}
    &\le\sqrt C\|M_R\|_{L^p\mathscr B_\theta}.\label{E:source-transfer-norm}
  \end{align}
  For a fixed real Schwartz pair and time,
  \begin{equation}\label{E:source-transferred-row}
    \langle M_Y(t)z,w\rangle_E=Y(h_{R,t;z,w})\quad\text{in }L^2,
  \end{equation}
  where $h_{R,t;z,w}$ is the literal raw test class
  $\zeta_R1_{(0,t)}v_zG_w$ with the actual adjoint from
  \eqref{E:variance-dual-wave}. The path is basis-independent up to
  indistinguishability, is linear in jointly Gaussian noise families, and
  complexifies sesquilinearly.

  If $(W,Y_n)$ are jointly centered Gaussian, $Y_n$ and $D_n=W-Y_n$
  have uniform bounds of the form~\eqref{E:source-raw-variance-bound},
  and $\operatorname{Var}D_n(F)\to0$ on every smooth compact test,
  then $M_{Y_n}\to M_R$ in every finite $L^p(\mathscr B_\theta)$.
\end{proposition}

\begin{proof}
  The variance bound annihilates raw-null tests and extends $Y$ as a
  bounded linear map into its actual $L^2$ space. Completion preserves
  Gaussian finite-dimensional laws. For each finite raw orthonormal family,
  the covariance of its $Y$ evaluations is bounded by $CI$, by applying
  the variance bound to every real linear combination. Independence of
  $Y(f_j)$ is not assumed.

  Apply Lemma~\ref{L:source-finite-comparison} with $v_j=A_j(\cdot)$ in
  $\mathscr B_\theta$, also to finite tails. The standard comparison vector
  has the law of the raw $W(f_j)$. The already-proved raw path convergence
  makes $M_{Y,N}$ Cauchy in every $L^p$. It lies in the same separable
  closed span of the countably many deterministic paths. The elementary
  Cauchy/subsequence construction of Lemma~\ref{L:driver-holder-limit}
  gives a strongly measurable limit on the actual space of $Y$.
  Different $p$ limits agree by convergence in probability. Passing to
  limits in the finite inequalities gives both displayed bounds. An
  almost surely uniformly convergent subsequence gives compact values
  for all times. Functional $L^2$ limits of Gaussian linear combinations
  prove that the path is Gaussian.

  For real Schwartz $z,w$, the actual coefficient identity is
  \[
    \langle A_j(t)z,w\rangle_E
    =\E[W(h_{R,t;z,w})W(f_j)]
    =\langle h_{R,t;z,w},f_j\rangle_{H_W}.
  \]
  Therefore, the finite transferred row is $Y(P_Nh)$, with $P_N$ the
  raw $H_W$ orthogonal projection. Since $P_Nh\to h$, the noise bound
  gives $Y(P_Nh)\to Y(h)$ in $L^2$. Operator-path $L^2$ convergence
  proves~\eqref{E:source-transferred-row}. Long intervals use the same
  raw completion and endpoint nullity as in Lemma~\ref{L:driver-interval-limit}.
  No filter is commuted through a physical mask or wave group. Four
  real pair identities give the complex assertion. Countably many dense
  Schwartz phases and rational times, followed by phase density and path
  continuity, prove basis indistinguishability.

  For jointly Gaussian $Y,Z$, their real linear combinations have a raw
  variance bound by the $L^2$ triangle inequality. The finite sums are
  linear in the noise, hence so are the path limits. In the stability
  assertion $D_n$ is centered Gaussian by the joint hypothesis. Its
  uniform bound gives
  \[
    \|M_{D_n}-M_{D_n,N}\|_{L^p\mathscr B_\theta}
    \le\sqrt{C_D}\|M_R-M_N\|_{L^p\mathscr B_\theta}.
  \]
  For fixed $N$, the covariance matrix of $(D_n(f_j))_{j\le N}$ is
  positive and bounded by $s_N(n)I$, where
  $s_N(n)=\sum_{j\le N}\operatorname{Var}D_n(f_j)\to0$.
  The finite comparison gives
  $\|M_{D_n,N}\|_{L^p\mathscr B_\theta}
  \le\sqrt{s_N(n)}\|M_N\|_{L^p\mathscr B_\theta}$.
  Choose $N$ large for the uniform tail, then $n$ large for the finite
  head. Linearity identifies $M_{D_n}=M_R-M_{Y_n}$. The same argument
  proves a multiparameter limit whenever each fixed test error tends
  to zero, with no relation between parameter rates.
  This proves Proposition~\ref{P:source-gaussian-transfer}.
\end{proof}

\subsection{The spatial covariance space and a retaining extension}

\begin{lemma}[Original spatial space and heat]\label{L:source-spatial-heat}
  Let $H_\Gamma$ be the real test-null completion with
  \[
    B_\Gamma(f,g)=\int\Gamma(\ud y)\int f(x)g(x-y)\ud x
    =(2\pi)^d\int\widehat f(\xi)\overline{\widehat g(\xi)}\mu(\ud\xi).
  \]
  It is separable and includes Schwartz tests. With
  \begin{equation}\label{E:source-heat-definition}
    p_\varepsilon(x)=(2\pi\varepsilon)^{-d/2}
    e^{-|x|^2/(2\varepsilon)},\qquad C_\varepsilon f=p_\varepsilon*f,
  \end{equation}
  heat is a positive self-adjoint contraction on $H_\Gamma$,
  $I-C_\varepsilon$ is a contraction, and $C_\varepsilon\to I$ strongly.
\end{lemma}

\begin{proof}
  The spectral normalization is the spatial computation in
  Proposition~\ref{P:masked-noise-completion}; its integral is real on
  real tests by evenness of $\mu$. The local bound
  $|B_\Gamma(f,g)|\le |K|\Gamma(K-K)\|f\|_\infty\|g\|_\infty$
  on a common compact support gives separability by countable smooth
  approximation. Expanding smooth cutoffs of a Schwartz test converge
  in Schwartz seminorms, and its covariance correlation pairing converges
  against tempered $\Gamma$. Thus, Schwartz tests enter the same completion.
  The Fourier multiplier of $C_\varepsilon$ is
  $m_\varepsilon(\xi)=e^{-\varepsilon|\xi|^2/2}$.
  On dense Schwartz tests, the displayed norm gives positivity,
  self-adjointness and both contraction bounds. Dominated convergence
  gives strong convergence there; uniform boundedness extends it to the
  completion. This uses no physical mask operator on a noise quotient.
  This proves Lemma~\ref{L:source-spatial-heat}.
\end{proof}

Set $\nu_a(\ud\lambda)=\lambda^{a-1}\ud\lambda/\Gamma_E(a)$ and
\[
  \mathcal G=L^2((0,\infty)_\lambda\times\R_r,
  \nu_a(\ud\lambda)\ud r;H_\Gamma).
\]
This is a real separable Hilbert space: countable simple functions on
rational rectangles with a countable dense spatial collection suffice.

\begin{lemma}[Feature isometry retaining the given noise]\label{L:source-retaining-isometry}
  On finite smooth temporal-spatial tensors define
  \begin{equation}\label{E:source-feature-isometry}
    \Phi F(\lambda,r)=\sqrt{2\lambda}
    \int_{\substack{t>0\\t\ge r}}e^{-\lambda(t-r)}F(t,\cdot)\ud t.
  \end{equation}
  It extends to an isometry $\Phi:H_W\to\mathcal G$ with closed range,
  and the formula represents smooth compact tests almost everywhere.
  On a product extension retaining the original $W$, there is an isonormal
  $\mathcal I$ on $\mathcal G$ with
  \begin{equation}\label{E:source-given-W-retention}
    \mathcal I(\Phi h)=W(h)\quad\text{in }L^2
    \quad\text{for each }h\in H_W.
  \end{equation}
\end{lemma}

\begin{proof}
  The identity
  \[
    \int_{-\infty}^{\min(t,u)}
    2\lambda e^{-\lambda(t+u-2r)}\ud r
    =e^{-\lambda|t-u|}
  \]
  and the raw Laplace formula give
  $\|\Phi F\|_{\mathcal G}^2=\|F\|_{H_W}^2$.
  All signed exchanges for finite tensors are absolutely integrable:
  compact temporal factors give integrals of
  $|\tau(t)\sigma(u)||t-u|^{-a}$, finite for $a<1$, times fixed finite
  spatial inner products. No oscillatory infinite-measure Fubini is used.
  Smooth time partitions on one compact support approximate a general
  smooth spacetime test uniformly by finite tensors. The local covariance
  bound~\eqref{E:driver-test-continuity} proves their density in $H_W$.
  Hence, the isometry extends with closed range.

  For a general smooth compact $F$, those approximants also converge
  uniformly in spatial $H_\Gamma$ norm in time, by local Radon mass.
  For fixed $\lambda,r$, their integrals in~\eqref{E:source-feature-isometry}
  converge in $H_\Gamma$. Meanwhile the isometry gives convergence in
  $\mathcal G$, with an almost everywhere convergent subsequence. Its
  two limits agree, proving the stated formula. The coordinate $r$ is
  auxiliary; no value of raw negative-time noise has been assigned.

  Let $P$ project orthogonally onto $\Phi H_W$. On a product extension
  take an independent isonormal $J$ on $(\Phi H_W)^\perp$, built from
  independent real standard Gaussians on a finite or countable basis.
  Define
  \[
    \mathcal I(g)=W(\Phi^{-1}Pg)+J((I-P)g).
  \]
  Orthogonality and independence make it isonormal on $\mathcal G$ and
  prove~\eqref{E:source-given-W-retention} with the actual original random
  variable, not only its law. For the countable fixed raw basis, these
  equalities hold on one common probability-one set. Thus, the raw
  finite paths and their $L^p$ limits are precisely pullbacks of the
  already constructed raw driver. Cutoff fields may use $J$; they are
  not asserted to be functions of $W$ alone.
  This proves Lemma~\ref{L:source-retaining-isometry}.
\end{proof}

\subsection{Exact joint source law and convergence}

Let $P_\eta$ multiply $\mathcal G$ by $1_{\{\lambda\le\eta^{-1}\}}$.
Let $C_\varepsilon$ act fiberwise on $H_\Gamma$. These commute. For
$\rho=(\varepsilon,\eta)>0$, define
\begin{equation}\label{E:source-cutoff-noises}
  Q_\rho=C_\varepsilon P_\eta,\qquad
  Y_\rho(F)=\mathcal I(Q_\rho\Phi F),\qquad
  D_\rho(F)=\mathcal I((I-Q_\rho)\Phi F)=W(F)-Y_\rho(F).
\end{equation}
The last equality uses the actual retaining coupling. Define
\begin{equation}\label{E:source-covariance-functions}
  \Gamma_e(x)=(p_e*\Gamma)(x),\qquad
  K_\eta(v)=\frac1{\Gamma_E(a)}
  \int_0^{\eta^{-1}}e^{-\lambda|v|}\lambda^{a-1}\ud\lambda.
\end{equation}
The temporal operation is a Laplace prefix, not temporal convolution.

\begin{proposition}[Canonical sources on the retaining space]
  \label{P:source-canonical-convergence}
  The noises in~\eqref{E:source-cutoff-noises} have pointfield realizations
  with joint covariance
  \begin{equation}\label{E:source-joint-covariance}
    \operatorname{Cov}(Y_{\varepsilon,\eta}(t,x),
    Y_{\varepsilon',\eta'}(s,y))
    =K_{\max(\eta,\eta')}(t-s)\Gamma_{\varepsilon+\varepsilon'}(x-y).
  \end{equation}
  Mean-square pointfield integration agrees with $Y_\rho(F)$ on tests.
  Both source and full residual obey
  \begin{equation}\label{E:source-two-dominations}
    \operatorname{Var}Y_\rho(F),\quad\operatorname{Var}D_\rho(F)
    \le\|F\|_{H_W}^2,
  \end{equation}
  and $\operatorname{Var}D_\rho(F)\to0$ for every $F\in H_W$ as
  $\varepsilon,\eta\downarrow0$ at arbitrary relative rates. Consequently,
  for every finite $p\ge1$,
  \begin{equation}\label{E:source-driver-limit}
    M_R^\rho:=M_{Y_\rho}\longrightarrow M_R
    \quad\text{in }L^p(\mathscr B_\theta),\qquad
    M_{D_\rho}=M_R-M_R^\rho.
  \end{equation}
  The source and residual have uniform local Gaussian driver moments and
  square-exponential norms, with constants for fixed $R,T$ and exponents.
\end{proposition}

\begin{proof}
  Apply the spatial distribution identity to a single shifted heat test:
  \[
    \Gamma_e(x)=\int e^{i\xi\cdot x}e^{-e|\xi|^2/2}\mu(\ud\xi).
  \]
  Gaussian spectral moments of every order are finite for tempered $\mu$.
  Thus, this is smooth with bounded derivatives. Since
  $\widehat{p_\varepsilon(x-\cdot)}
  =c_de^{-i\xi\cdot x}e^{-\varepsilon|\xi|^2/2}$, the two heat factors
  in the spatial inner product cancel $(2\pi)^d$ exactly, giving
  \begin{equation}\label{E:source-heat-inner-product}
    B_\Gamma(p_\varepsilon(x-\cdot),p_{\varepsilon'}(y-\cdot))
    =\Gamma_{\varepsilon+\varepsilon'}(x-y).
  \end{equation}
  Evenness of $\mu$ removes the reflected argument.

  For each positive $\rho$ and point $(t,x)$ put
  \begin{equation}\label{E:source-point-feature}
    v_{\rho;t,x}(\lambda,r)
    =1_{\{\lambda\le\eta^{-1}\}}\sqrt{2\lambda}
    e^{-\lambda(t-r)}1_{\{r\le t\}}p_\varepsilon(x-\cdot).
  \end{equation}
  Its squared $\mathcal G$ norm is
  $K_\eta(0)\Gamma_{2\varepsilon}(0)<\infty$.
  Define $Y_\rho(t,x)=\mathcal I(v_{\rho;t,x})$. The common $\lambda$
  range for two such vectors is
  $\lambda\le\min(\eta^{-1},\eta'^{-1})=\max(\eta,\eta')^{-1}$.
  Integrating $r$ gives $e^{-\lambda|t-s|}$, and
  \eqref{E:source-heat-inner-product} gives the spatial factor. This
  proves~\eqref{E:source-joint-covariance} with the prescribed widths and
  raw amplitudes, also for singular Radon and white covariances.

  The point feature is continuous in $\mathcal G$ norm, directly from
  this continuous covariance. Its norm is bounded on compact parameter
  sets. Hence, for a smooth compact spacetime $F$, its Bochner integral
  against $v_{\rho;t,x}$ exists. Integrate the heat translates in $x$,
  then the time feature, to obtain exactly $Q_\rho\Phi F$. Applying the
  bounded map $\mathcal I:\mathcal G\to L^2$ proves the pointfield-test
  identity on the same space. Common-support indicator tests follow by
  raw completion and $L^1$ approximation; bounded point-feature norms and
  the domination below give the same $L^2$ limit.

  Orthogonality of the two $\lambda$ ranges gives, for $g\in\mathcal G$,
  \[
    \|(I-Q_\rho)g\|_{\mathcal G}^2
    =\|(I-P_\eta)g\|_{\mathcal G}^2
    +\|P_\eta(I-C_\varepsilon)g\|_{\mathcal G}^2
    \le\|g\|_{\mathcal G}^2.
  \]
  Also $\|Q_\rho g\|_{\mathcal G}\le\|g\|_{\mathcal G}$. Together with
  the isometry these prove both variance bounds. Disjoint $\lambda$
  ranges are independent; the full heat residual need not be independent
  of the source.

  The $L^2$ tail integral gives $P_\eta\to I$ strongly. Fiberwise heat
  converges strongly on simple $\mathcal G$ functions by
  Lemma~\ref{L:source-spatial-heat}, then on all of $\mathcal G$ by the
  contraction bound. The estimate
  \[
    \|(I-Q_\rho)g\|_{\mathcal G}
    \le\|(I-C_\varepsilon)g\|_{\mathcal G}
    +\|(I-P_\eta)g\|_{\mathcal G}\longrightarrow0
  \]
  holds at arbitrary relative rates. Thus, the residual variance tends
  to zero for every raw $F$. Proposition~\ref{P:source-gaussian-transfer}
  gives~\eqref{E:source-driver-limit} without commuting a filter through
  $\zeta_R$ or a wave group.

  The same comparison gives
  $\|M_R^\rho\|_{L^p\mathscr B_\theta},
  \|M_{D_\rho}\|_{L^p\mathscr B_\theta}
  \le\|M_R\|_{L^p\mathscr B_\theta}$. The raw $\sqrt p$ estimate and
  its even-moment exponential-series argument give uniform Gaussian
  driver bounds. They are statements about $L^p$ equivalence classes
  on the retaining extension, not a simultaneous path event for all
  uncountably many cutoffs.
  This proves Proposition~\ref{P:source-canonical-convergence}.
\end{proof}

\subsection{Regularized pointfields and the ordinary first response}

\begin{lemma}[Regularity for each fixed cutoff]\label{L:source-pointfield-regularity}
  For each fixed $\rho>0$, the pointfield has a version continuous in
  time and smooth in space, with every spatial derivative jointly
  continuous on compact time-space rectangles.
\end{lemma}

\begin{proof}
  For each spatial multiindex $b$, differentiate
  \eqref{E:source-point-feature} in $x$ as a $\mathcal G$ vector.
  All derivatives exist because their spatial squared norms are the
  finite heat moments
  \[
    \int \xi^{2b}e^{-\varepsilon|\xi|^2}\mu(\ud\xi),
  \]
  and the next moments dominate difference quotients. Set
  $Z_b(t,x)=\mathcal I(\partial_x^bv_{\rho;t,x})$.
  At fixed $x$, use $1-e^{-\lambda h}\le\lambda h$ in the finite
  $\lambda$ integral; at fixed $t$, use
  $|e^{i\xi\cdot x}-e^{i\xi\cdot y}|\le|\xi||x-y|$ and the next heat
  moment. The squared triangle inequality gives
  \begin{equation}\label{E:source-derivative-increments}
    \E|Z_b(t,x)-Z_b(s,y)|^2
    \le C_{\rho,b}(|t-s|+|x-y|^2).
  \end{equation}
  This computation uses~\eqref{E:source-joint-covariance}, including its
  spatial width, and applies to singular spectral measures without a
  density assumption.

  Here is a direct continuity construction. In $m=d+1$ parameter
  dimensions on a compact rectangle, even Gaussian $q$th increment
  moments have root bounded by $C\sqrt q$ times the parameter distance
  to the power $1/2$ at small distances. The dyadic grid has at most
  $C_m2^{nm}$ adjacent edges at level $n$. Their maximum has $L^q$
  norm at most $C\sqrt q\,2^{-n(1/2-m/q)}$, with constants for this
  rectangle and fixed $\rho,b$. Choose $q$ large and
  $0<h_0<1/2-m/q$. The sum of these maxima weighted by $2^{nh_0}$
  has finite $L^q$ norm. Binary refinement, using a fixed number of
  adjacent edges per coordinate at each scale, gives a continuous
  extension from dyadic points. At each fixed parameter the extension
  agrees with the given Gaussian variable in $L^2$, by
  \eqref{E:source-derivative-increments}; it is a modification.
  Use countably many nested compact rectangles and all multiindices.
  The versions agree on overlaps on countable dense sets, hence
  everywhere there by continuity, so they patch.

  They are actual derivatives. The $\mathcal G$-valued fundamental
  theorem gives, along a coordinate segment,
  \[
    \partial_x^bv(t,x+he_i)-\partial_x^bv(t,x)
    =\int_0^h\partial_x^{b+e_i}v(t,x+ue_i)\ud u.
  \]
  Apply bounded linear $\mathcal I$ and $L^2$ integration. The continuous
  versions give the same ordinary integral by their Riemann sums, which
  converge both pathwise and in $L^2$. Enforce these identities first on
  countably many rational $t,x,h$ and multiindices, then use joint
  continuity to extend them to every segment in the compact rectangles.
  The ordinary fundamental theorem yields $\partial_iZ_b=Z_{b+e_i}$.
  Thus, all spatial derivatives exist and are jointly continuous with
  time. The versions are for this fixed $\rho$, not a common path event
  over uncountably many source parameters.
  This proves Lemma~\ref{L:source-pointfield-regularity}.
\end{proof}

\begin{proposition}[Actual ordinary source response]\label{P:source-ordinary-response}
  For each fixed $\rho>0$, on its regularity event, put
  $b_\rho(t,x)=\zeta_R(x)Y_\rho(t,x)$. The statewise integral
  \begin{equation}\label{E:source-ordinary-response}
    L_\rho(t)z=\int_0^tS(-u)B(b_\rho(u))S(u)z\ud u
  \end{equation}
  defines an operator-norm Lipschitz path on $E$, and
  $L_\rho=M_R^\rho$ for all $t\in[0,T]$ on one probability-one set.
  In particular, it has the strongly measurable path version supplied
  by the Gaussian construction.
\end{proposition}

\begin{proof}
  The coefficient is compact smooth in space and continuous in time in
  every spatial derivative norm. Multiplication estimates and strong
  continuity of the full free group show that the statewise integral
  exists on every $E_r$. Its operator increments $E_r\to E_{r+1}$
  are bounded by a finite sample constant times $|t-s|$, exactly by the
  statewise gain argument of Lemma~\ref{L:driver-gain-localization}.
  This proves Lipschitz continuity in $\mathcal B(E)$, without requiring
  norm continuity or an operator-norm derivative of $S(t)$.

  At each fixed $u$, the Sobolev duality calculation uses only spatial
  smoothness of $b_\rho(u,\cdot)$. From $S(-u)(0,f)$ and the two Bessel
  weights, for real Schwartz phases,
  \[
    \langle S(-u)B(b_\rho(u))S(u)z,w\rangle_E
    =\int b_\rho(u,x)[S(u)z]_1(x)G_w(u,x)\ud x.
  \]
  Thus, no prior hypothesis of smoothness in time is invoked for this
  instantaneous identity. For complex pairs conjugate the second factor.
  Integrating gives the ordinary source-field integral against the literal
  raw wave test $h_{R,t;z,w}$. For smooth tests, the point-feature integral
  has already been identified with $Y_\rho(F)$. The continuous pointfield
  version has the same integral: compact Riemann sums converge pathwise
  and in $L^2$ to the ordinary and feature integrals, respectively.
  Approximate the indicator wave test in the raw completion with common
  compact spatial support and $L^2$-time spatial supremum error tending
  to zero. Its $L^1$ error also tends to zero. The point-feature norms
  are bounded on that support, so their integrals converge in $\mathcal G$;
  the raw variance domination gives the same $L^2$ limit on the test side.
  Consequently,
  \[
    \langle L_\rho(t)z,w\rangle_E
    =Y_\rho(h_{R,t;z,w})
    =\langle M_R^\rho(t)z,w\rangle_E
    \quad\text{in }L^2.
  \]
  Compare a countable dense Schwartz phase collection and rational times.
  Boundedness and the path continuity of both sides extend this equality
  to all states and all times on one probability-one set. The equality
  is on the actual coupled space, not only in law. The set is for fixed
  $\rho$; the $L^p$ limit in~\eqref{E:source-driver-limit} needs no
  simultaneous version for every source parameter.
  This proves Proposition~\ref{P:source-ordinary-response}.
\end{proof}

The source laws above match the pinned author definitions. The author's
page~9 redefinition keeps the law; the retaining extension was proved in
Lemma~\ref{L:source-retaining-isometry}. The derivative estimate here was
derived from the correct joint covariance, not from the differing spatial
index in the author's page~8 increment display. No source correction is
adopted. All limits are at fixed finite $R,T$. The nonlinear Young flow,
canonical initial datum $(1,0)$ and its solution-moment transfer remain
separate parts of the argument.

===== END TEX FILE: notes/integrated_source_convergence.tex =====

===== BEGIN TEX FILE: notes/integrated_masked_moments.tex =====
\section{Fixed masks and displacement moments}
\label{S:masked-moments}

We retain Hypothesis~\ref{H:homog}, data $(1,0)$, and all its original
dimensions and covariance amplitudes. Fix $\rho=(\epsilon,\eta)>0$ and
the actual source $Y_\rho$ of Proposition~\ref{P:source-canonical-convergence}.
For each fixed $\rho$ use the continuous-time, smooth-space version in
Lemma~\ref{L:source-pointfield-regularity}. Source fields can use the
retaining auxiliary extension; their law and the given raw noise remain
those already constructed. Let $m\in C_c^\infty(\R^d)$ be real with
$0\le m\le1$. It multiplies the physical source after regularization.

Write $X_{\rho,n}^m(t,x)$ for the ordinary ordered displacement integral
with coefficient $mY_\rho$, and $X_{\rho,n}$ for its unmasked version;
both order-zero terms are one. We first construct these integrals.
The positive Green measures $G_d(r,\ud z)$ have mass $r$ and support in
$B_r$, including the sphere measure in $d=3$. These are the source
kernels~\cite{chen:author2026:time-dependency}*{(2.1), (2.3)--(2.5),
p.~7}; the ordered convention and Gaussian pairing formula are
\cite{chen:author2026:time-dependency}*{(2.13)--(2.16), p.~10;
(2.19), p.~12}. We use all pair partitions, including self-pairings.

\begin{lemma}[Actual chains and mixed-order comparison]
  \label{L:masked-chain-comparison}
  The finite ordered integrals are Bochner $L^2$ integrals. For all
  $n,k\ge0$, fixed $t,x,y$ and positive $\rho$,
  \begin{equation}\label{E:masked-order-comparison}
    0\le \E[X_{\rho,n}^m(t,x)X_{\rho,k}^m(t,y)]
    \le \E[X_{\rho,n}(t,x)X_{\rho,k}(t,y)].
  \end{equation}
  Both expectations vanish when $n+k$ is odd. With $q_n$ from
  Lemma~\ref{L:vertex-crude},
  \begin{equation}\label{E:masked-order-bound}
    \|X_{\rho,n}^m(t,x)\|_2\le q_n(t),\qquad
    \|X_{\rho,n}(t,x)\|_2\le q_n(t).
  \end{equation}
\end{lemma}

\begin{proof}
  Let $\nu_n^{t,x}$ be the positive time-space chain measure on
  $0<s_1<\cdots<s_n<t$, with successive spatial factors
  $G_d(s_{j+1}-s_j,\ud z_j)$ and $s_{n+1}=t$, recovering positions
  backwards from $x$. It uses measures rather than sphere densities.
  The order-zero measure has mass one. Integrating the latest vertex
  gives the recursion $f_n(t)=\int_0^t(t-r)f_{n-1}(r)\ud r$; hence,
  \begin{equation}\label{E:masked-chain-mass}
    \nu_n^{t,x}(1)=\frac{t^{2n}}{(2n)!}.
  \end{equation}
  Measurability follows by representing $G_d(r)$ as $r$ times the
  dilation by $r$ of its unit-time probability measure.

  The actual covariance is
  \[
    C_\rho(s,z;r,w)=K_\eta(s-r)\Gamma_{2\epsilon}(z-w),
    \qquad 0\le C_\rho\le c_\rho
    :=K_\eta(0)\Gamma_{2\epsilon}(0)<\infty.
  \]
  Positivity uses the nonnegative Radon measure $\Gamma$ and positive
  heat and Laplace kernels. The upper bound also follows by Gaussian
  Cauchy--Schwarz. H\"older's inequality and scalar Gaussian moments
  bound the absolute expectation of any fixed number of source factors,
  uniformly over their vertices. Applied to $2n$ factors this bounds
  the $L^2$ norm of each $n$-fold product. The field is measurable and
  continuous, so integration against the finite chain measure defines a
  Bochner $L^2$ integral and permits stochastic Fubini between two chains.

  These are the canonical regularized terminal integrals at common noise
  widths. Here is the Green-width identification needed in dimension
  three. At fixed positive $\rho$, replace every Green measure by its
  convolution with a positive heat approximate identity. At fixed times
  the measures converge weakly, preserving masses. Every Wick covariance
  product is bounded by a power of $c_\rho$ and is spatially continuous
  by Lemma~\ref{L:source-pointfield-regularity}. Thus its spatial integrals
  converge. The chain mass integrands from~\eqref{E:masked-chain-mass}
  give an integrable time majorant. Square and cross moments between
  smoothed and unsmoothed integrals converge to the same diagram sum;
  therefore, the random integrals converge in $L^2$. This is precisely
  the Green-before-noise limit in Lemma~\ref{L:joint-fixed-order}.
  It also applies in dimensions one and two if Green smoothing is used.
  No samplewise source bound on heat-kernel tails is needed. Consequently,
  Lemma~\ref{L:vertex-crude} applies to the actual unmasked integrals.

  If $n+k$ is odd, Gaussian centering gives zero. If $n+k=2l$, each
  pair partition $D$ contributes the nonnegative finite integral
  \[
    \int \prod_{\{i,j\}\in D}
    C_\rho(s_i,z_i;s_j,z_j)
    \ud(\nu_n^{t,x}\otimes\nu_k^{t,y}).
  \]
  The masked integrand has the additional factor
  $\prod_{i=1}^{2l}m(z_i)\in[0,1]$. Every vertex appears exactly once,
  irrespective of its chain or partner. Summing gives
  \eqref{E:masked-order-comparison}, including unequal and empty chains
  and every self-pairing. At $n=k=0$ both sides are one.
  Taking $k=n$, $y=x$ and then applying the unmasked bound gives
  \eqref{E:masked-order-bound}. This is a statement about expected
  displacement diagrams; no samplewise solution order or Gaussian
  covariance order is used.
  This proves Lemma~\ref{L:masked-chain-comparison}.
\end{proof}

\begin{proposition}[Ordinary solutions and tested moments]
  \label{P:masked-source-moments}
  The sums $u_\rho^m=\sum_{n\ge0}X_{\rho,n}^m$ and
  $u_\rho=\sum_{n\ge0}X_{\rho,n}$ converge absolutely in $L^2$ and
  have locally continuous versions that are the unique locally continuous
  ordinary mild solutions with coefficients $mY_\rho$ and $Y_\rho$,
  respectively, and data $(1,0)$. For every nonnegative
  $\phi\in C_c^\infty(\R^d)$,
  \begin{align}
    0&\le\E[u_\rho^m(t,x)u_\rho^m(t,y)]
    \le\E[u_\rho(t,x)u_\rho(t,y)],\label{E:masked-two-point}\\
    \E\left|\int\phi(x)u_\rho^m(t,x)\ud x\right|^2
    &\le \|\phi\|_1^2\,\E|u_\rho(t,0)|^2.
    \label{E:masked-average-source}
  \end{align}
  The spatial integral is an actual Bochner $L^2$ integral.
\end{proposition}

\begin{proof}
  Put $Q_T=\sum_{n\ge0}q_n(T)<\infty$, using
  \eqref{E:vertex-summability}. Lemma~\ref{L:masked-chain-comparison}
  proves absolute $L^2$ convergence uniformly in space and widths.
  To identify the sums pathwise, fix $\rho$, a compact observation set
  and a finite horizon $T$. On the source regularity event the coefficient
  is bounded by a finite sample-dependent $M$ on the compact backward-cone
  enlargement. Finite propagation and~\eqref{E:masked-chain-mass} bound
  each Picard term there by $M^nT^{2n}/(2n)!$.
  This series converges uniformly. Each term is continuous by the
  unit-time Green representation and dominated integration. Summing the
  Volterra recursion gives the ordinary mild equation with initial
  displacement one and velocity zero. Iterating the difference equation
  between two continuous solutions bounds its value on the observation
  set by $B M^nT^{2n}/(2n)!$, where $B$ bounds their difference on the
  larger compact cone. Letting $n\to\infty$ proves uniqueness.

  Ordinary Fubini and the absolute product integrability in the preceding
  lemma identify each Bochner term with the pathwise chain integral at a
  fixed terminal point, simultaneously over countably many orders.
  An almost surely convergent subsequence of the $L^2$ partial sums then
  identifies its limit with the continuous Picard version at that point.
  These versions define the solution for all terminal points at this
  fixed $\rho$; no common event over uncountably many widths is needed.

  For either masked or unmasked terms, Cauchy--Schwarz gives
  \[
    \sum_{n,k\ge0}\E|X_{\rho,n}^{(m)}(t,x)
    X_{\rho,k}^{(m)}(t,y)|\le Q_t^2.
  \]
  Products of partial sums converge in $L^1$. Thus the preceding
  lemma passes termwise to~\eqref{E:masked-two-point}.
  The unmasked source law is spatially stationary, and its finite
  Picard integrals commute with translations. Their $L^2$ limits inherit
  stationarity, so
  $\E[u_\rho(t,x)u_\rho(t,y)]\le\E|u_\rho(t,0)|^2$.
  Stationarity is not required of the masked solution.

  Each finite Bochner term is $L^2$-continuous in $x$ by source increment
  continuity on compact cones and dominated Gaussian product moments.
  Uniform $q_n$ tails pass this property to the full sum. Its separable
  $L^2$ image and bound $Q_t$ give the Bochner average. Absolute Fubini
  is justified by $\|\phi\|_1^2Q_t^2$. Integrating the two-point
  inequality against $\phi(x)\phi(y)$ proves~\eqref{E:masked-average-source}.
  This proves Proposition~\ref{P:masked-source-moments}.
\end{proof}

\begin{proposition}[Canonical point-moment limit and conditional transfer]
  \label{P:masked-canonical-transfer}
  At every fixed $t$, at arbitrary relative rates of the two widths,
  \begin{equation}\label{E:masked-unmasked-moment-limit}
    \lim_{\epsilon,\eta\downarrow0}\E|u_\rho(t,0)|^2
    =\E|u(t,0)|^2,
  \end{equation}
  where $u$ is the original canonical Stratonovich solution.
  If the masked averages in~\eqref{E:masked-average-source} converge
  in $L^2$ to $Z_m(t,\phi)$, either at arbitrary rates or along a
  specified sequence with both widths tending to zero, then
  \begin{equation}\label{E:masked-conditional-transfer}
    \E|Z_m(t,\phi)|^2\le\|\phi\|_1^2\,\E|u(t,0)|^2.
  \end{equation}
\end{proposition}

\begin{proof}
  At every fixed pair of orders the actual common-width source law is
  the vertexwise law in Lemma~\ref{L:joint-fixed-order}.
  At terminal $(t,0)$ reverse each chain by
  $s'_j=t-s_{n+1-j}$, $z'_j=-z_{n+1-j}$, and likewise for the
  other chain. Even covariances preserve the reversed differences.
  Relabeling vertices sends each pairing $\{i,j\}$ to
  $\{r(i),r(j)\}$, giving the exact initial-chain convention in
  Proposition~\ref{P:mixed}, also for an empty chain.
  The preceding Green-width identification removes Green smoothing
  first. Lemma~\ref{L:joint-fixed-order} then gives the canonical
  limit of each diagram at arbitrary relative noise-width rates.
  Odd mixed moments stay zero. Hence, at fixed $n,k$,
  \[
    \E[X_{\rho,n}(t,0)X_{\rho,k}(t,0)]
    \longrightarrow \E[X_n(t,0)X_k(t,0)].
  \]
  All absolute mixed moments, before and after the limit, are bounded
  by $q_n(t)q_k(t)$. Given $\delta>0$, choose a finite square of
  orders with the double majorant outside it less than $\delta$.
  On the square the finitely many limits hold jointly; off it both
  tails are bounded by $\delta$. Proposition~\ref{P:mixed}
  identifies the canonical sum, proving
  \eqref{E:masked-unmasked-moment-limit}. This argument uses the
  single-width diagram laws, without assigning a new pathwise
  realization of the entire canonical solution family.

  Finally, $L^2$ convergence of the masked averages implies convergence
  of their second moments by
  \[
    |\E|B|^2-\E|A|^2|
    \le\|B-A\|_2(\|B\|_2+\|A\|_2).
  \]
  Take the same source limit in~\eqref{E:masked-average-source} and
  use~\eqref{E:masked-unmasked-moment-limit}.
  Existence of the masked limit remains an explicit premise here; the
  next section constructs it on a phase containing the constant data.
  This proves Proposition~\ref{P:masked-canonical-transfer}.
\end{proof}

===== END TEX FILE: notes/integrated_masked_moments.tex =====

===== BEGIN TEX FILE: notes/integrated_constant_phase_young.tex =====
\section{Young evolution with constant initial data}
\label{S:constant-phase-young}

We use the fixed $R,T,E,\gamma,\theta,\beta$ of
\eqref{E:driver-parameters}, and choose the allowed even mask
$m=\zeta_R$ with $0\le m\le1$. All constants in this section can depend
on these fixed data, the model and the auxiliary physical cutoffs.
There is no uniform estimate as $R$ or $T$ grows.

\subsection{The distributional phase and its free evolution}

Define the real Hilbert space
\begin{equation}\label{E:constant-phase-space}
  F=E\oplus\R^2,\qquad
  \|(e,c_1,c_2)\|_F^2=\|e\|_E^2+c_1^2+c_2^2,\qquad
  e_0=(0,1,0).
\end{equation}
Its distributional interpretation is
$(e,c_1,c_2)\mapsto(e_1+c_1,e_2+c_2)$.
Let $i:E\to F$ denote $e\mapsto(e,0,0)$ and let $\pi_C:F\to\R^2$
be the constant-coordinate projection.

\begin{lemma}[Constants and finite propagation]\label{L:constant-phase-free}
  The distributional interpretation of $F$ is continuous and injective.
  The space is complete and separable, and $iE$ is closed and proper.
  For every real $\psi\in C_c^\infty(\R^d)$,
  \begin{equation}\label{E:constant-phase-cutoff}
    L_\psi(e,c_1,c_2)=\psi e+(c_1\psi,c_2\psi)
  \end{equation}
  is bounded from $F$ to $E$. The actual free wave group on $F$ is
  \begin{equation}\label{E:constant-phase-free}
    S_F(t)(e,c_1,c_2)=(S(t)e,c_1+tc_2,c_2).
  \end{equation}
  It is strongly continuous and bounded on finite horizons and has
  finite propagation for the total distributional data, including
  local cancellation between $e$ and the constants.
\end{lemma}

\begin{proof}
  A nonzero constant has Fourier transform a nonzero multiple of
  $\delta_0$. Every $H^\sigma$ Fourier transform is locally $L^2$
  near zero, since its weight is bounded above and below there.
  A locally $L^2$ function $f$ cannot represent $\delta_0$: testing
  against $\varphi(\xi/\varepsilon)$, with $\varphi(0)=1$ and
  $\varphi$ compactly supported in $B_1$, bounds its integral by
  \[
    \|f\|_{L^2(B_\varepsilon)}
    \varepsilon^{d/2}\|\varphi\|_2\longrightarrow0,
  \]
  whereas $\delta_0$ gives one. Thus constants lie in neither
  $H^{1/2}$ nor $H^{-1/2}$; the interpretation is injective.
  Sobolev duality and the two test integrals prove continuity into
  distributions, uniformly on bounded families of compact tests.
  Completeness, separability and the closed proper inclusion follow
  from the Hilbert direct sum.

  Multiplication by $\psi$ is bounded on both Sobolev entries.
  Indeed, the Peetre inequalities give
  $\langle\xi\rangle^\sigma\langle\eta\rangle^{-\sigma}
  \le2^{|\sigma|/2}\langle\xi-\eta\rangle^{|\sigma|}$.
  In the unitary Fourier convention its weighted kernel is therefore
  bounded by convolution with the $L^1$ function
  $2^{|\sigma|/2}c_d|\widehat\psi(q)|\langle q\rangle^{|\sigma|}$,
  where $c_d=(2\pi)^{-d/2}$. The $L^1*L^2$ bound applies at
  $\sigma=\pm1/2$; the two constant columns are also in $E$.
  This proves boundedness of~\eqref{E:constant-phase-cutoff}.

  The finite-dimensional block in~\eqref{E:constant-phase-free} and
  the strong, finite-horizon bound for $S(t)$ from
  Lemma~\ref{L:driver-gain-localization} prove the group assertions.
  To verify its physical meaning, for $t>0$ consider the matrix of
  compactly supported distributions
  \[
    \begin{pmatrix}
      \partial_tG_d(t)&G_d(t)\\
      \Delta G_d(t)&\partial_tG_d(t)
    \end{pmatrix}.
  \]
  The source Green convention gives
  $\widehat G_d(t)(\xi)=c_d\sin(t|\xi|)/|\xi|$; hence its convolution
  multiplier is the sine quotient, and the differentiated multipliers
  are $\cos(t|\xi|)$ and $-|\xi|\sin(t|\xi|)$.
  The matrix agrees with $S(t)$ on Schwartz phases. Convolution by a
  compact distribution is continuous on tempered distributions:
  its transpose convolves a Schwartz test with the reflected compact
  distribution, continuously in all Schwartz seminorms. Schwartz
  approximation in $E$ extends the identity to $E$.
  The masses of the four entries are $1,t,0,1$, so constants give
  exactly~\eqref{E:constant-phase-free}. Time reversal handles $t<0$.
  Each entry is supported in $B_{|t|}$, also for the three-dimensional
  sphere kernel. If the total initial distribution vanishes on an
  enlarged region, each translated kernel tests zero there, so the
  evolved total distribution vanishes on the smaller cone. This
  argument permits cancellation between its Sobolev and constant parts.
  This proves Lemma~\ref{L:constant-phase-free}.
\end{proof}

\subsection{Both constant-response columns of the actual driver}

Choose real $\chi\in C_c^\infty$, equal to one on $B_{2R+T+1}$ and
supported in $B_{2R+T+2}$, and choose real compact smooth $\psi=1$
on a neighborhood of $\operatorname{supp}\chi$.
Write $M_E=M_R$ and $M_E^\rho=M_{Y_\rho}$ for the actual paths already
constructed, with the same raw deterministic coefficients.

\begin{proposition}[Actual extended driver]\label{P:constant-phase-driver}
  As identities of continuous operator paths,
  \begin{equation}\label{E:constant-phase-localization}
    D_\chi M_E=M_E=M_ED_\chi,
  \end{equation}
  and the same holds for each fixed $\rho$. Define
  \begin{equation}\label{E:constant-phase-driver}
    A_E=M_EL_\psi,\qquad A=iA_E,\qquad
    A_E^\rho=M_E^\rho L_\psi,\qquad A^\rho=iA_E^\rho.
  \end{equation}
  These are independent of $\psi$, have compact values, and satisfy
  $Ai=iM_E$, $\pi_CA=0$ and their source counterparts.
  In every finite $L^pC^\theta$, $A^\rho\to A$ at arbitrary relative
  source-width rates. Their norms have uniform $\sqrt p$ moment bounds
  and a common finite square-exponential moment. The raw $A$ is
  measurable with respect to the given $W$.
\end{proposition}

\begin{proof}
  Lemma~\ref{L:driver-gain-localization} gives both localizations for
  every deterministic $A_j(0,t)$. The raw finite sums retain them.
  Proposition~\ref{P:source-gaussian-transfer} constructs the source
  finite sums with exactly these coefficients and correlated
  $Y_\rho(f_j)$. Their $C^\theta$ limits preserve both identities.
  A uniformly convergent subsequence, or rational times and continuous
  paths, gives~\eqref{E:constant-phase-localization} for all $t$ on
  one event. Use a separate event for each fixed $\rho$.

  For two choices $\psi,\psi'$, $(L_\psi-L_{\psi'})z\in E$ and
  $D_\chi(L_\psi-L_{\psi'})z=0$. The right localization kills this
  difference. For $z=ie$, $D_\chi D_\psi e=D_\chi e$ and hence
  $Ai=iM_E$. The constant columns are precisely
  $iM_E(\psi,0)$ and $iM_E(0,\psi)$; they are retained.
  Bounded composition preserves compactness and transfers
  \eqref{E:source-driver-limit} and the Gaussian norm bounds to
  \eqref{E:constant-phase-driver}. If $\|X\|_{L^p}\le C\sqrt p$,
  then $\E X^{2n}\le C^{2n}(2n)^n$. Since $n!\ge(n/e)^n$,
  the exponential series gives $\E e^{cX^2}<\infty$ uniformly when
  $2ecC^2<1$. Finally, $A$ is a deterministic bounded transform of
  the original $W$-measurable driver.
  This proves Proposition~\ref{P:constant-phase-driver}.
\end{proof}

\begin{lemma}[Ordinary response on all of $F$]\label{L:constant-source-response}
  For fixed $\rho$ put $b(r)=mY_\rho(r)$ and define
  \[
    B_F(b)(e,c_1,c_2)=(0,b(e_1+c_1))\in E.
  \]
  Then
  \begin{equation}\label{E:constant-source-response}
    A_E^\rho(t)z=\int_0^tS(-r)B_F(b(r))S_F(r)z\ud r
  \end{equation}
  as a statewise strong integral. Its primitive is Lipschitz in
  $\mathcal B(F,E)$ and the identity holds for all states and times
  on one event for this fixed $\rho$.
\end{lemma}

\begin{proof}
  The source regularity gives one compact spatial support for $b$,
  continuity in $L^\infty$ and $L^2$, and bounded spatial derivatives
  on the horizon. Since $e_1\in L^2$ and
  $\|\cdot\|_{H^{-1/2}}\le\|\cdot\|_2$,
  \[
    \|B_F(b)\|_{\mathcal B(F,E)}
    \le\|b\|_\infty+\|b\|_2.
  \]
  Strong continuity and finite-horizon bounds of both free groups make
  the integrand strongly continuous on each state and uniformly bounded
  as an operator. Integrating its bound proves operator-norm Lipschitz
  increments without assuming a Banach-valued operator derivative.

  The total initial distributions of $z$ and $iL_\psi z$ agree on the
  entire enlarged ball where $\psi=1$. Lemma~\ref{L:constant-phase-free}
  gives equality of the free displacements near $\operatorname{supp}m$
  for $0\le r\le T$. Multiplication by $b(r)$ kills the difference.
  Apply Proposition~\ref{P:source-ordinary-response} to the actual
  $E$ state $L_\psi z$ to obtain~\eqref{E:constant-source-response}.
  Separability and rational times, followed by boundedness and
  continuity, give its path identity. This proves the constant columns
  directly; no density of $E$ in $F$ is used.
  This proves Lemma~\ref{L:constant-source-response}.
\end{proof}

\subsection{The exact linear Young equation}

We use the Banach Young estimate
\cite{friz.hairer:20:course}*{Sections~1.4--1.5, 4.1, (4.3),
pp.~13, 61--62}. For $D,V$ with exponent $\theta>1/2$ and bounded
bilinear multiplication, left composition gives
\begin{equation}\label{E:constant-young-estimate}
  \left\|\int_s^t\ud D(r)V(r)-D(s,t)V(s)\right\|
  \le C_\theta[D]_\theta[V]_\theta|t-s|^{2\theta}.
\end{equation}
The Banach spaces here are $\mathcal B(F)$, and multiplication is
bounded with constant one. We derive the linear solution and stability
estimates below rather than invoke a nonlinear bounded-vector-field
theorem.

\begin{proposition}[Linear Young evolution]\label{P:constant-young-linear}
  For every $D\in C^\theta([0,T];\mathcal B(F))$ with $D(0)=0$
  there is a unique $C^\theta$ solution, in the terminal variable, of
  \begin{equation}\label{E:constant-young-equation}
    U_D(t,s)=I+\int_s^t\ud D(r)U_D(r,s).
  \end{equation}
  It has the composition law, invertible values and joint operator-norm
  continuity on $0\le s\le t\le T$. The map $D\mapsto U_D$ is locally
  Lipschitz into the uniform time-triangle norm, and
  \begin{equation}\label{E:constant-young-growth}
    \sup_{s\le t\le T}\|U_D(t,s)\|
    \le C_T\exp\big(C_T(1+\|D\|_{C^\theta})^{1/\theta}\big).
  \end{equation}
\end{proposition}

\begin{proof}
  On an interval $[a,a+\ell]$ use the complete scaled norm
  $N_\ell(V)=\sup\|V\|+\ell^\theta[V]_\theta$ and put
  $I_D(V)(t)=\int_a^t\ud D\,V$.
  Applying~\eqref{E:constant-young-estimate} to every subinterval gives
  \begin{align*}
    \sup\|I_D(V)\|
    &\le[D]_\theta\ell^\theta\sup\|V\|
    +C_\theta[D]_\theta\ell^{2\theta}[V]_\theta,\\
    [I_D(V)]_\theta
    &\le[D]_\theta\sup\|V\|
    +C_\theta[D]_\theta\ell^\theta[V]_\theta.
  \end{align*}
  Thus, with $c_\theta=2\max(1,C_\theta)$,
  \begin{equation}\label{E:constant-young-local}
    N_\ell(I_D(V))
    \le c_\theta[D]_\theta\ell^\theta N_\ell(V).
  \end{equation}
  Take $K\ge1$, $[D]_\theta\le K$, and choose $\ell$ with
  $c_\theta K\ell^\theta\le1/4$. The map
  $V\mapsto V_a+I_D(V)$ is a contraction on the complete affine
  space of paths starting at $V_a$. Its solution satisfies
  $N_\ell(V)\le(4/3)\|V_a\|\le2\|V_a\|$.

  To compare $D,D'$, require both seminorms at most $K$ and write
  $\delta=\|D-D'\|_{C^\theta}$, $W=V-V'$. Subtracting gives
  $W=W_a+I_D(W)+I_{D-D'}(V')$. Absorbing the factor $1/4$ yields
  \begin{equation}\label{E:constant-young-difference}
    N_\ell(W)\le2\|W_a\|
    +2c_\theta\ell^\theta\delta N_\ell(V').
  \end{equation}
  Cover $[s,T]$ by at most $n_{K,T}$ such pieces. If the second
  initial norm is $B$, its norm on piece $j$, indexed from zero,
  is at most $2^{j+1}B$. With $E_j$ the difference at its left
  endpoint, induction gives
  \[
    E_{j+1}\le2E_j+2^{j+2}c_\theta\ell^\theta\delta B,\qquad
    E_j\le2^jE_0+j2^{j+1}c_\theta\ell^\theta\delta B.
  \]
  Equation~\eqref{E:constant-young-difference} gives the same bound
  inside each piece; a shorter final piece only reduces the coefficient.
  For evolutions, $E_0=0$ and $B=1$. The number of pieces is uniform
  in $s,t$, proving local Lipschitz dependence in the full triangle norm.

  Now choose $K=1+\|D\|_{C^\theta}$. At most
  $C_T(1+\|D\|_{C^\theta}^{1/\theta})$ pieces suffice.
  Each multiplies the norm by at most two, giving
  \eqref{E:constant-young-growth}. Uniqueness patches the solutions;
  right multiplication by the preceding evolution gives the
  composition law. On a small piece~\eqref{E:constant-young-local}
  gives $\|U_D-I\|_\infty\le1/3$, so a Neumann series proves local
  invertibility, then products give global invertibility.
  Finally, $U_D(t,s)=U_D(t,0)U_D(s,0)^{-1}$ proves joint norm
  continuity, since $U_D(\cdot,0)$ is continuous and inversion is
  continuous on invertible operators.
  This proves Proposition~\ref{P:constant-young-linear}.
\end{proof}

\begin{proposition}[Actual Gaussian Young and physical flows]
  \label{P:constant-gaussian-flow}
  Apply Proposition~\ref{P:constant-young-linear} to $A,A^\rho$.
  The resulting flows are strongly measurable in uniform triangle norm,
  have every finite norm moment and satisfy
  \begin{equation}\label{E:constant-flow-limit}
    U_{A^\rho}\longrightarrow U_A
    \quad\hbox{in every finite }L^p
    \left(\sup_{0\le s\le t\le T}\|\cdot\|_{\mathcal B(F)}\right).
  \end{equation}
  They preserve the interaction constant coordinates:
  \begin{equation}\label{E:constant-flow-range}
    \pi_CU_A(t,s)=\pi_C,\qquad
    (U_A(t,s)-I)F\subset iE,
  \end{equation}
  and likewise for the source. The physical flow is
  \begin{equation}\label{E:constant-physical-flow}
    P_A(t,s)=S_F(t)U_A(t,s)S_F(-s).
  \end{equation}
  It has composition and strong continuity on states, physical constant
  block $(c_1,c_2)\mapsto(c_1+(t-s)c_2,c_2)$, all finite moments
  and the analogous uniform $L^p$ source convergence.
  Its difference from the free flow has range in $iE$.
\end{proposition}

\begin{proof}
  The original paths lie in separable closed path spans by their Gaussian
  construction. Bounded composition in~\eqref{E:constant-phase-driver}
  and the continuous Young map preserve strong measurability into
  $C(\Delta_T;\mathcal B(F))$, where
  $\Delta_T=\{(t,s):0\le s\le t\le T\}$ has the uniform norm.
  Indeed, the continuous image of the separable driver space has
  separable closure in this triangle space.
  Applying $\pi_C$ to Young Riemann sums gives the first identity
  in~\eqref{E:constant-flow-range}. Each increment applied to any
  state lies in $iE$; closedness of this subspace passes the property
  through sums and limits, giving the second identity.

  Write $X_\rho=\|A^\rho\|_{C^\theta}$ and
  $X_0=\|A\|_{C^\theta}$. Proposition~\ref{P:constant-phase-driver}
  supplies $c_0>0$ and $H_0<\infty$ such that
  \[
    \sup_\rho\E e^{c_0X_\rho^2}\le H_0,\qquad
    \E e^{c_0X_0^2}\le H_0.
  \]
  For $K\ge1$, let $L_K$ be the Lipschitz constant of
  Proposition~\ref{P:constant-young-linear} on the driver ball of
  radius $K$, in the whole time-triangle norm. On
  $\{X_\rho\le K,\ X_0\le K\}$ it gives
  \[
    \|U_{A^\rho}-U_A\|_\infty
    \le L_K\|A^\rho-A\|_{C^\theta}.
  \]
  Consequently, for $\varepsilon>0$ and any finite $q\ge1$,
  Markov and the union bound give
  \[
    \mathbb P(\|U_{A^\rho}-U_A\|_\infty>\varepsilon)
    \le2H_0e^{-c_0K^2}
    +(L_K/\varepsilon)^q\E\|A^\rho-A\|_{C^\theta}^q.
  \]
  At fixed $K$ the second term tends to zero at arbitrary relative
  source-width rates. Only then let $K\to\infty$ to obtain
  convergence in probability. No independence of the raw, source
  and residual drivers is required.

  Put $\nu=1/\theta<2$. For each finite $r\ge1$ and $c>0$,
  there is $C_{r,c}<\infty$ such that
  \[
    rC_T(1+x)^\nu\le cx^2+C_{r,c},\qquad x\ge0.
  \]
  This follows because $(1+x)^\nu/x^2\to0$ as $x\to\infty$,
  while the remainder is bounded on compact intervals.
  Use $c\le c_0$ and~\eqref{E:constant-young-growth} to obtain
  \[
    \sup_\rho\E\|U_{A^\rho}\|_\infty^r<\infty,\qquad
    \E\|U_A\|_\infty^r<\infty.
  \]
  In particular, for fixed finite $p\ge1$ and
  $V_\rho=\|U_{A^\rho}-U_A\|_\infty$, the $2p$ moments of
  $V_\rho$ are uniformly bounded. For every $\varepsilon>0$,
  \[
    \E V_\rho^p
    \le\varepsilon^p+
    (\E V_\rho^{2p})^{1/2}
    \mathbb P(V_\rho>\varepsilon)^{1/2}.
  \]
  The second term tends to zero by convergence in probability;
  then let $\varepsilon\downarrow0$. This proves
  \eqref{E:constant-flow-limit}. The square-exponential bound used
  here is a driver bound; no square-exponential flow bound is needed.

  The free group is strongly continuous and bounded on the horizon.
  Define $\mathcal B_\infty(\Delta_T;\mathcal B(F))$ to be the
  Banach space of all bounded operator families on $\Delta_T$.
  The deterministic map
  \[
    \mathcal L(V)(t,s)=S_F(t)V(t,s)S_F(-s)
  \]
  is bounded linear from $C(\Delta_T;\mathcal B(F))$ into
  this bounded-family space, with norm at most $C_T^2$, where
  $C_T\ge\sup_{|r|\le T}\|S_F(r)\|$.
  Hence it preserves strong measurability on the separable ranges and
  gives, in particular,
  \[
    \|P_{A^\rho}-P_A\|_\infty
    \le C_T^2\|U_{A^\rho}-U_A\|_\infty.
  \]
  All finite moments and uniform $L^p$ convergence therefore transfer
  to the physical flows. This does not place those flows in the
  norm-continuous triangle space or assert operator-norm continuity
  of the free group.
  For each fixed state, joint continuity follows by splitting a
  physical-flow difference into the norm-continuous $U$ difference
  and two strong free-group differences, using the uniform group bound.
  Group cancellation gives composition. The finite constant block
  $J_t(c_1,c_2)=(c_1+tc_2,c_2)$ satisfies $J_tJ_{-s}=J_{t-s}$,
  which gives the asserted physical constant coordinates from
  $\pi_CU_A=\pi_C$. Finally,
  \[
    P_A(t,s)-S_F(t-s)
    =S_F(t)(U_A(t,s)-I)S_F(-s)
  \]
  has range in $iE$, since $S_F(t)iE=iE$.
  This proves Proposition~\ref{P:constant-gaussian-flow}.
\end{proof}

\subsection{Ordinary source solutions and the raw tested observable}

\begin{lemma}[Identification with the ordinary source equation]
  \label{L:constant-source-solution}
  For fixed $\rho$, the displacement distribution of
  $P_{A^\rho}(t,0)e_0$ is the locally continuous ordinary source solution
  $u_\rho^m(t,\cdot)$ from Proposition~\ref{P:masked-source-moments}.
\end{lemma}

\begin{proof}
  In~\eqref{E:constant-source-response} let
  $C(r)=S(-r)B_F(b(r))S_F(r)$. The primitive is $A_E^\rho$.
  For left endpoints $r_j=t_j$, the Young sums applied to a state $v$
  are
  \[
    \sum_j\int_{t_j}^{t_{j+1}}iC(r)U_{A^\rho}(r_j,s)v\ud r.
  \]
  Uniform continuity of $U$ and the uniform bound for $C$ make these
  converge to the strong integral with $U(r,s)v$.
  Thus the Young equation is precisely the ordinary interaction
  integral on states. Multiplying by free groups gives the full-phase
  Duhamel equation. Its unique $C([0,T];F)$ solution follows by the
  bounded-coefficient Picard argument with the strongly continuous,
  bounded free group. No operator-norm derivative of $S_F$ is used.

  More explicitly, put $W_0(t)=e_0$ and, for $n\ge1$,
  \[
    W_n(t)=\int_0^t S_F(t-r)iB_F(b(r))W_{n-1}(r)\ud r.
  \]
  If $B_T=\sup_r\|B_F(b(r))\|_{\mathcal B(F,E)}$, induction on the
  time simplex gives
  $\sup_t\|W_n(t)\|_F\le C_T^{n+1}B_T^nT^n/n!$.
  We take $C_T\ge\max(1,\sup_{|t|\le T}\|S_F(t)\|)$,
  which also supplies the bound at order zero.
  The series converges in $C([0,T];F)$. The Duhamel map there has norm
  at most $C_TB_TT$, so its sum solves the same integral equation and
  equals the ordinary phase by uniqueness.

  Let $X_0(t,x)=1$ and
  $X_n(t)=\int_0^tG_d(t-r)*(b(r)X_{n-1}(r))\ud r$.
  At fixed $n$ these are continuous in time and smooth in space.
  Derivatives fall on the smooth compact factor $bX_{n-1}$;
  Green mass $t-r$ bounds the integrals, while the unit-time measure
  representation gives time continuity. This is induction using only
  finitely many bounded derivatives for each fixed derivative order.
  At $n=0$ the phase displacement is $X_0$. If the equality holds at
  $n-1$, multiplication by smooth $b$ identifies the forcing with
  $(0,f_r)$, where $f_r=b(r)X_{n-1}(r)$ is smooth and compactly supported.
  For a compact smooth test $\varphi$, continuous distributional testing
  of the phase integral yields
  \[
    \langle[W_n(t)]_1,\varphi\rangle
    =\int_0^t\int f_r(y)
    \int G_d(t-r,\ud z)\varphi(y+z)\ud y\ud r
    =\langle X_n(t),\varphi\rangle.
  \]
  Absolute Fubini follows from
  $\|\varphi\|_\infty\|f_r\|_1(t-r)$, integrable on the horizon
  because $f_r$ has one compact support and continuous $L^1$ norm.
  This also covers sphere measures in $d=3$.
  Iterating the scalar recursion gives exactly $X_{\rho,n}^m$,
  with chronological order and all physical mask factors.
  The scalar compact-cone factorial bound gives locally uniform
  convergence to $u_\rho^m$, whereas the phase series converges in
  $F$ and hence in distributions. Their displacement limits agree.
  This proves Lemma~\ref{L:constant-source-solution}.
\end{proof}

\begin{proposition}[Actual raw average and original point moment]
  \label{P:constant-raw-average}
  Let real $\phi\in C_c^\infty(\R^d)$ be nonnegative with integral one.
  The bounded functional and raw random variable
  \begin{equation}\label{E:constant-raw-average}
    O_\phi(e,c_1,c_2)=\langle e_1,\phi\rangle+c_1,\qquad
    Z_m(t,\phi)=O_\phi P_A(t,0)e_0
  \end{equation}
  are well defined, and $Z_m$ is $W$-measurable. At arbitrary
  relative source-width rates, for every finite $p$,
  \begin{equation}\label{E:constant-tested-limit}
    \int\phi(x)u_\rho^m(t,x)\ud x
    \longrightarrow Z_m(t,\phi)\quad\text{in }L^p.
  \end{equation}
  In particular,
  \begin{equation}\label{E:constant-original-point-transfer}
    \E|Z_m(t,\phi)|^2\le\E|u(t,0)|^2.
  \end{equation}
\end{proposition}

\begin{proof}
  Sobolev duality gives
  $\|O_\phi\|\le(\|\phi\|_{H^{-1/2}}^2+1)^{1/2}$.
  The raw driver is $W$-measurable, and the Young and deterministic maps
  above are continuous or bounded measurable on their separable ranges.
  Thus $Z_m$ is $W$-measurable and does not depend on the auxiliary
  $J$ used in source realizations.
  At each fixed $\rho$, Lemma~\ref{L:constant-source-solution}
  identifies the displacement as a distribution with the ordinary
  source solution. Testing by this same $\phi$, with $\int\phi=1$,
  therefore gives the almost sure identity
  \[
    O_\phi P_{A^\rho}(t,0)e_0
    =C_\phi:=\int\phi(x)u_\rho^m(t,x)\ud x.
  \]
  This uses the displacement pairing and its constant displacement
  coordinate in~\eqref{E:constant-raw-average}; it takes no point
  trace of an $H^{1/2}$ state. All identities here are at one fixed
  $\rho$, so no uncountable intersection of source-version events
  is used.

  We verify that $C_\phi$ equals the Bochner $L^2$ average
  $B_\phi$ from Proposition~\ref{P:masked-source-moments}.
  That proposition gives the spatially uniform bound
  $\|u_\rho^m(t,x)\|_2\le Q_t$, with $Q_t$ also independent of
  source widths. Scalar Fubini gives
  \[
    \E\int|\phi(x)u_\rho^m(t,x)|\ud x
    \le Q_t\|\phi\|_1<\infty.
  \]
  Thus the ordinary spatial integral exists almost surely.
  Weighted Cauchy--Schwarz and scalar Fubini also give
  \[
    \E|C_\phi|^2
    \le\|\phi\|_1\int|\phi(x)|\E|u_\rho^m(t,x)|^2\ud x
    \le Q_t^2\|\phi\|_1^2.
  \]
  For every bounded real random variable $\Xi$ on the fixed source
  space, $V\mapsto\E[\Xi V]$ is a continuous functional on $L^2$.
  It therefore commutes with the Bochner integral, while scalar
  Fubini is justified by
  $\|\Xi\|_\infty Q_t\|\phi\|_1$. Consequently,
  \[
    \E[\Xi B_\phi]
    =\int\phi(x)\E[\Xi u_\rho^m(t,x)]\ud x
    =\E[\Xi C_\phi].
  \]
  Both averages are real $L^2$ variables. Taking
  $\Xi=\operatorname{sign}(B_\phi-C_\phi)$ yields
  $\E|B_\phi-C_\phi|=0$, so the two averages agree almost surely.

  Proposition~\ref{P:constant-gaussian-flow} now gives, for every
  finite $p$,
  \[
    \|B_\phi-Z_m(t,\phi)\|_{L^p}
    \le\|O_\phi\|\|e_0\|
    \big\|\|P_{A^\rho}-P_A\|_\infty\big\|_{L^p}
    \longrightarrow0.
  \]
  This is~\eqref{E:constant-tested-limit}, including its $L^2$ case,
  for the actual masked Bochner average, with arbitrary relative
  source-width rates. It supplies the conditional convergence premise
  of Proposition~\ref{P:masked-canonical-transfer} at the same fixed
  mask, horizon, original covariance and observable.
  Since $\phi\ge0$ and $\|\phi\|_1=1$, that proposition gives
  \eqref{E:constant-original-point-transfer}.
  Zero covariance gives the free constant solution and equality.
  All source limits are at fixed mask and horizon, before time
  asymptotics.
  This proves Proposition~\ref{P:constant-raw-average}.
\end{proof}

\begin{proposition}[Compact deterministic base]\label{P:constant-compact-base}
  Let $h\in C([0,T];C_c^\infty(K))$ be real for one fixed compact
  $K$, with all spatial derivatives continuous on that support.
  The statewise primitive
  \[
    A_h(t)=\int_0^t iS(-r)B_F(h(r))S_F(r)\ud r
  \]
  is Lipschitz in $\mathcal B(F)$, takes values with range in $iE$,
  and has a bound $C_T\sup_r(\|h(r)\|_\infty+\|h(r)\|_2)$.
  The flow conclusions above, including moments, source convergence
  and ordinary-source identification, hold for $A_h+gA$ and
  $A_h+gA^\rho$, uniformly on bounded displayed deterministic budgets
  and bounded real $g$. No Cameron-shift identity is asserted here.
\end{proposition}

\begin{proof}
  The estimate for $B_F$ and the strong free groups prove the primitive
  and its Lipschitz bound exactly as in
  Lemma~\ref{L:constant-source-response}. If
  $\|A_h\|_{C^\theta}\le H$, $|g|\le G$ and $X=\|A\|_{C^\theta}$,
  then $\|A_h+gA\|_{C^\theta}\le H+GX$. If $\E e^{cX^2}$ is bounded,
  choose $c'\le c/(2(1+G^2))$ to obtain
  \[
    \E e^{c'\|A_h+gA\|_{C^\theta}^2}
    \le e^{2c'H^2}\E e^{2c'G^2X^2}<\infty.
  \]
  Alternatively $pC(1+H+Gx)^{1/\theta}\le cx^2+C_{p,H,G,c}$
  transfers the Young growth estimate directly to all finite moments.
  Source driver convergence, local Young stability and uniform
  integrability give the same flow convergence. The state-integral
  and Picard-to-chain arguments apply to $h+gmY_\rho$, whose spatial
  support lies in one fixed compact union. These are individual
  estimates and versions, without an uncountable common-parameter
  event. Only $h=0$, $g=1$ enters
  \eqref{E:constant-original-point-transfer}.
  This proves Proposition~\ref{P:constant-compact-base}.
\end{proof}

===== END TEX FILE: notes/integrated_constant_phase_young.tex =====

===== BEGIN TEX FILE: notes/integrated_compact_mean_family.tex =====
\section{Compact mean families and the full-phase spectral gap}
\label{S:compact-mean-family}

Let $I=[0,1]$, let $K_x\subset\R^d$ be compact, and let
$\sigma\mapsto V_\sigma$ be continuous from $I$ into
$C_c^\infty(K_x)$, real and nonnegative. The index $\sigma$ is a
family parameter, distinct from physical propagation time $t$.
Assume that one real $w\in H^1(\R^d)$ with $\|w\|_2=1$ satisfies
\begin{equation}\label{E:compact-common-trial}
  \|\nabla w\|_2^2-\int V_\sigma w^2\le-\varepsilon
  \quad\hbox{for all }\sigma\in I,\qquad \varepsilon>0.
\end{equation}
Put $M=\sup_I\|V_\sigma\|_\infty$ and $H_\sigma=-\Delta-V_\sigma$.
The phases $E,F$, inclusion $i$, data $e_0$ and observable $O_\phi$
are exactly those of Section~\ref{S:constant-phase-young}.
Proposition~\ref{P:constant-compact-base}, with deterministic coefficient
$h=V_\sigma$ and noise amplitude zero, gives the actual ordinary physical
flow $P_\sigma(t)$ on $F$. Its $E$ restriction is $P_\sigma^E(t)$.
Uniqueness of the Duhamel solution makes finite-horizon constructions
agree on overlaps; integer horizons and autonomy give the same
semigroup for every $t\ge0$.

We import the following statements from the \emph{second edition}
of~\cite{teschl:14:mathematical}: Theorem~10.2, p.~258, gives the
self-adjoint $H^2$ operator, lower bound, essential spectrum $[0,\infty)$
and compact smooth core for real compact smooth potentials in the
dimensions considered here. Theorem~10.13, p.~273, gives a simple
positive ground state \emph{if the spectral bottom is an eigenvalue}.
Theorem~4.12 and Corollary~4.13, pp.~140--141, give max--min and
form monotonicity, with the essential threshold used after discrete
eigenvalues end and with the quadratic-form domain allowed.
Uniformity, fractional norms and all applications to $F$ are proved below.

\subsection{The ground family and the actual global phase}

\begin{proposition}[Ground states and a uniform rate gap]
  \label{P:compact-ground-family}
  The common form domain of $H_\sigma$ is $H^1$ with form
  $q_\sigma(u)=\|\nabla u\|_2^2-\int V_\sigma|u|^2$.
  Its bottom $E_1(\sigma)$ is a simple eigenvalue with a unique
  real positive-a.e. normalized ground state $p_\sigma$.
  Let $E_2(\sigma)$ be the second max--min level, set to zero when
  there is no second negative eigenvalue. Then
  \begin{align}
    -M&\le E_1(\sigma)\le-\varepsilon,\qquad
    E_1(\sigma)<E_2(\sigma)\le0,\label{E:compact-energy-levels}\\
    |E_j(\sigma)-E_j(\tau)|
    &\le\|V_\sigma-V_\tau\|_\infty,\qquad j=1,2.
    \label{E:compact-level-continuity}
  \end{align}
  The map $\sigma\mapsto p_\sigma$ is continuous into $H^2$ and
  bounded there. With
  $\lambda_\sigma=\sqrt{-E_1(\sigma)}$ and
  $\mu_\sigma=\sqrt{-E_2(\sigma)}$,
  \begin{equation}\label{E:compact-rate-gap}
    \sqrt\varepsilon\le\lambda_\sigma\le\sqrt M,\qquad
    d_0:=\inf_I(\lambda_\sigma-\mu_\sigma)>0.
  \end{equation}
\end{proposition}

\begin{proof}
  The imported Theorem~10.2 applies to $-V_\sigma$, which is real,
  compactly supported and in $L^2$ for $d\le3$. It gives the stated
  self-adjoint operator on $H^2$ and essential threshold zero.
  Write $c=1+M$ and $A_\sigma=H_\sigma+c\ge1$.
  On $H^2$, integration by parts and the spectral theorem give
  \[
    \|A_\sigma^{1/2}u\|_2^2
    =q_\sigma(u)+c\|u\|_2^2,\qquad
    \|u\|_{H^1}^2\le\|A_\sigma^{1/2}u\|_2^2
    \le c\|u\|_{H^1}^2.
  \]
  Spectral cutoffs $1_{[1,n]}(A_\sigma)u$ show that $H^2$ is a
  core for the half-power form norm. Fourier cutoffs show it is
  dense in $H^1$. The two equivalent completions are therefore
  $D(A_\sigma^{1/2})$ and $H^1$. Both norms dominate $L^2$ and
  give the same $L^2$ limit, so these are equal as subspaces, with
  the displayed form. This verifies the form domain used below.

  The form lower bound and~\eqref{E:compact-common-trial} give
  $-M\le E_1\le-\varepsilon$ by the imported form max--min principle.
  The bottom belongs to the spectrum and lies below the essential
  threshold, so it is an isolated eigenvalue of finite multiplicity.
  Only now apply the imported Theorem~10.13: it is simple with a
  positive ground state. Conjugation preserves the real operator;
  positivity and unit $L^2$ norm fix its real representative.

  Simplicity, isolation and threshold zero give $E_1<E_2\le0$.
  For every common unit form test,
  $|q_\sigma(u)-q_\tau(u)|\le\|V_\sigma-V_\tau\|_\infty$.
  Taking the same infima over orthogonal complements and suprema
  in the source max--min formula proves
  \eqref{E:compact-level-continuity}, including passage of $E_2$
  to the threshold. Compactness gives
  $\Delta_*:=\min_I(E_2-E_1)>0$. Thus
  \[
    \lambda_\sigma-\mu_\sigma
    =\frac{E_2(\sigma)-E_1(\sigma)}
    {\lambda_\sigma+\mu_\sigma}
    \ge\frac{\Delta_*}{2\sqrt M}>0.
  \]
  Here $M\ge\varepsilon>0$, and no division by $\mu_\sigma$ occurs.

  Put $d_V=\|V_\sigma-V_\tau\|_\infty$ and decompose
  $p_\tau=a p_\sigma+r$, with $r\perp p_\sigma$ and $0<a\le1$.
  The variational bound gives
  $q_\sigma(p_\tau)\le E_1(\sigma)+2d_V$, whereas the complementary
  spectral bound gives
  $q_\sigma(p_\tau)\ge E_1(\sigma)+\Delta_*\|r\|_2^2$.
  Hence,
  \begin{equation}\label{E:compact-ground-continuity}
    \|p_\tau-p_\sigma\|_2^2
    =2(1-a)\le2(1-a^2)\le4d_V/\Delta_*.
  \end{equation}
  The eigenfunction equation is
  \[
    (1-\Delta)p_\sigma
    =(1-\lambda_\sigma^2+V_\sigma)p_\sigma.
  \]
  Its right side is continuous in $L^2$ and bounded there by $1+2M$.
  The inverse of $1-\Delta$ is an isometry from $L^2$ to the Bessel
  $H^2$ space, proving the asserted $H^2$ continuity and bound.
  This proves Proposition~\ref{P:compact-ground-family}.
\end{proof}

\begin{lemma}[Uniform fractional phase norms]\label{L:compact-fractional-phase}
  Let $B=1-\Delta$, $c=1+M$ and $A_\sigma=H_\sigma+c$.
  The quarter-power domain is $H^{1/2}$ and
  \begin{equation}\label{E:compact-quarter-power}
    \|B^{1/4}u\|_2\le\|A_\sigma^{1/4}u\|_2
    \le c^{1/4}\|B^{1/4}u\|_2.
  \end{equation}
  The norm
  \begin{equation}\label{E:compact-spectral-phase-norm}
    \|(u,z)\|_{E_\sigma}^2
    =\|A_\sigma^{1/4}u\|_2^2
    +\|A_\sigma^{-1/4}z\|_2^2
  \end{equation}
  is uniformly equivalent to the actual fixed norm on
  $E=H^{1/2}\times H^{-1/2}$, interpreting the negative entry by
  completion.
\end{lemma}

\begin{proof}
  On the common form domain $H^1$, $B\le A_\sigma\le cB$ and all
  three operators are at least one. For positive self-adjoint $T,S$
  with common form domain, $T\le S$ implies
  $(T+t)^{-1}\ge(S+t)^{-1}$ for $t>0$. Indeed,
  \[
    \langle f,(T+t)^{-1}f\rangle
    =\sup_u\{2\operatorname{Re}\langle f,u\rangle
    -q_T(u)-t\|u\|_2^2\};
  \]
  completing the square in the closed form norm proves the identity,
  and comparison of the suprema proves the order.
  Consequently $I-t(T+t)^{-1}\le I-t(S+t)^{-1}$.
  The scalar identity
  \[
    \sqrt x=\frac1\pi\int_0^\infty
    t^{-1/2}\frac{x}{x+t}\ud t
  \]
  follows by $t=xr^2$ and $\int_0^\infty(1+r^2)^{-1}\ud r=\pi/2$.
  Spectral integration and positive Tonelli, first over finite
  intervals and then by monotone convergence, give
  $T^{1/2}\le S^{1/2}$ as forms, including domain inclusions.
  Apply this to $B\le A_\sigma\le cB$ to obtain
  \eqref{E:compact-quarter-power} and equality of the quarter-power
  domains with $H^{1/2}$.

  Under the $L^2$ pairing the dual norm of
  $\|A_\sigma^{1/4}u\|_2$ at $z\in L^2$ is
  $\|A_\sigma^{-1/4}z\|_2$. Cauchy--Schwarz gives the upper bound,
  and a scalar multiple of $A_\sigma^{-1/2}z$ attains it.
  Completion and~\eqref{E:compact-quarter-power} identify this
  negative space with $H^{-1/2}$, uniformly in $\sigma$.
  Adding the squared norms proves the claim.
  This proves Lemma~\ref{L:compact-fractional-phase}.
\end{proof}

\begin{proposition}[The actual complementary wave on $E$]
  \label{P:compact-E-wave}
  Put
  \[
    e_\sigma^E=(p_\sigma,\lambda_\sigma p_\sigma),\qquad
    \ell_\sigma^E(u,z)
    =\frac{\langle p_\sigma,u\rangle+
    \langle p_\sigma,z\rangle/\lambda_\sigma}{2},
    \qquad \Pi_\sigma^E=e_\sigma^E\ell_\sigma^E.
  \]
  These are bounded real objects, continuous in their respective norms,
  with $\ell_\sigma^E(e_\sigma^E)=1$, and
  \begin{align}
    P_\sigma^E(t)e_\sigma^E
    &=e^{\lambda_\sigma t}e_\sigma^E,\qquad
    \ell_\sigma^EP_\sigma^E(t)
    =e^{\lambda_\sigma t}\ell_\sigma^E,\label{E:compact-E-eigen}\\
    \|P_\sigma^E(t)(I-\Pi_\sigma^E)\|_{\mathcal B(E)}
    &\le C(1+t)e^{\mu_\sigma t},\qquad t\ge0.
    \label{E:compact-E-complement}
  \end{align}
  The constant is uniform over $\sigma\in I$.
\end{proposition}

\begin{proof}
  Define real spectral functions $C_t(h),S_t(h)$ by
  $\cos(t\sqrt h),\sin(t\sqrt h)/\sqrt h$ for $h>0$,
  by $1,t$ at zero, and by
  $\cosh(t\sqrt{-h}),\sinh(t\sqrt{-h})/\sqrt{-h}$ for $h<0$.
  The spectral wave matrix is
  \begin{equation}\label{E:compact-spectral-wave}
    \begin{pmatrix}
      C_t(H_\sigma)&S_t(H_\sigma)\\
      -H_\sigma S_t(H_\sigma)&C_t(H_\sigma)
    \end{pmatrix}.
  \end{equation}
  Real potentials, their resolvents and spectral resolutions commute
  with conjugation. All these real functions and positive $A_\sigma$
  powers preserve the actual real phases.

  The spatial projection
  $Q_\sigma^{\mathrm{sp}}=I-|p_\sigma\rangle\langle p_\sigma|$
  commutes with $H_\sigma,A_\sigma$ and is contractive on both
  entries of~\eqref{E:compact-spectral-phase-norm}.
  On its support $h\ge E_2=-\mu_\sigma^2$, the phase isometry gives
  scalar matrix entries
  \[
    C_t(h),\quad \sqrt{h+c}\,S_t(h),\quad
    -hS_t(h)/\sqrt{h+c},\quad C_t(h).
  \]
  For $h\ge0$, use $|S_t(h)|\le\min(t,h^{-1/2})$ and split
  $h\le1$ from $h\ge1$; the lower off-diagonal entry is at most
  one. For $-\mu_\sigma^2\le h<0$, use
  $|C_t(h)|\le e^{\mu_\sigma t}$ and
  $|S_t(h)|\le t e^{\mu_\sigma t}$, with
  $|h|\le M$ and $1\le h+c\le c$.
  Thus the complementary spatial matrix has norm at most
  $C(1+t)e^{\mu_\sigma t}$, including $\mu_\sigma=0$.

  The two spatial ground branches are
  $(p_\sigma,\pm\lambda_\sigma p_\sigma)$. Besides $\Pi_\sigma^E$,
  their projections include the decaying branch
  \[
    (p_\sigma,-\lambda_\sigma p_\sigma)
    \frac{\langle p_\sigma,u\rangle
    -\langle p_\sigma,z\rangle/\lambda_\sigma}{2}.
  \]
  Their sum is the spatial ground projection on both phase entries.
  Both projection norms are uniformly bounded in the spectral phase
  norm because $\sqrt\varepsilon\le\lambda_\sigma\le\sqrt M$
  and $1\le c-\lambda_\sigma^2\le c$. The decaying branch has
  factor $e^{-\lambda_\sigma t}$ and remains in $I-\Pi_\sigma^E$.
  The fractional norm equivalence now proves the stated complement
  estimate for the spectral matrix.

  We identify this matrix with the actual physical flow.
  The same scalar bounds at graph levels
  $(A_\sigma u,A_\sigma^{1/2}z)$ give continuous solutions in
  $H^2\times H^1$. These graph norms are uniformly equivalent to
  the Sobolev norms: the $H^1$ case was proved above, and
  $A_\sigma-B=M-V_\sigma$ is bounded by $M$ while $A_\sigma,B\ge1$.
  Spectral cutoffs give $u_t=z$ in $H^1$ and $z_t=-H_\sigma u$ in
  $L^2$, with continuous derivatives there.
  The free Fourier group on $H^1\times L^2$ has, after its Bessel
  isometry, the same bounded weighted entries and is strongly
  continuous by dominated Fourier convergence. Its generator is
  $(z,\Delta u)$ on $H^2\times H^1$, as the Fourier multipliers
  show. For compact smooth initial data, differentiating the free
  interaction picture at these graph levels gives Duhamel with force
  $(0,V_\sigma u)$. The identity also holds in $E$.
  Multiplication by $V_\sigma$ maps $H^{1/2}$ into $L^2$ and then
  $H^{-1/2}$ with bound $M$, so Picard uniqueness identifies the
  spectral solution with the ordinary $E$ flow on these data.
  Density within $E$ and finite-horizon boundedness extend equality
  to all $E$. No density of $E$ in $F$ is used.
  Finally, the ground branches give~\eqref{E:compact-E-eigen};
  their pairings are continuous because $p_\sigma\in H^2$.
  Continuity and uniform bounds of the displayed vectors and duals
  follow from Proposition~\ref{P:compact-ground-family}.
  This proves Proposition~\ref{P:compact-E-wave}.
\end{proof}

\subsection{The full-phase projection and its complementary flow}

For the constant coordinates write
$C(t)(c_1,c_2)=(c_1+tc_2,c_2)$ and
$D_\sigma(c_1,c_2)=(0,V_\sigma c_1)\in E$.

\begin{proposition}[The full-phase growing projection]
  \label{P:compact-F-projection}
  The actual physical flow satisfies
  \begin{equation}\label{E:compact-F-block}
    P_\sigma(t)(e,c)
    =\left(P_\sigma^E(t)e+
    \int_0^tP_\sigma^E(t-r)D_\sigma C(r)c\ud r,\ C(t)c\right).
  \end{equation}
  Set
  \begin{align}
    f_\sigma&=\frac{\int V_\sigma p_\sigma}{2\lambda_\sigma}>0,
    &\ell_\sigma^C(c)&=
    f_\sigma\left(\frac{c_1}{\lambda_\sigma}
    +\frac{c_2}{\lambda_\sigma^2}\right),
    \label{E:compact-constant-dual}\\
    e_\sigma&=ie_\sigma^E,
    &\ell_\sigma(e,c)&=\ell_\sigma^E(e)+\ell_\sigma^C(c),\qquad
    \Pi_\sigma=e_\sigma\ell_\sigma,\quad Q_\sigma=I-\Pi_\sigma.
    \label{E:compact-F-projection}
  \end{align}
  These vectors, duals and rank-one projections are norm-continuous
  and uniformly bounded, and
  \begin{equation}\label{E:compact-F-eigen}
    \ell_\sigma(e_\sigma)=1,\qquad
    P_\sigma(t)\Pi_\sigma=\Pi_\sigma P_\sigma(t)
    =e^{\lambda_\sigma t}\Pi_\sigma.
  \end{equation}
  For every fixed nonnegative smooth compact $\phi$ of integral one,
  \begin{equation}\label{E:compact-positive-margins}
    \inf_I\ell_\sigma(e_0)>0,\qquad
    \inf_I O_\phi(e_\sigma)>0.
  \end{equation}
\end{proposition}

\begin{proof}
  The constant coordinates obey $C(t)$ because the potential force
  has range in $iE$. To justify variation of constants on the $E$
  component, let $g$ be a continuous $E$ force and substitute the
  ordinary free-Duhamel equation for $P_\sigma^E(t-r)g(r)$ in its
  time integral. With $B_\sigma^E(u,z)=(0,V_\sigma u)$, strong
  $E$-valued Fubini gives
  \begin{align*}
    &\int_0^t\int_r^t S(t-s)B_\sigma^E
    P_\sigma^E(s-r)g(r)\ud s\ud r\\
    &\qquad=\int_0^tS(t-s)B_\sigma^E
    \left[\int_0^sP_\sigma^E(s-r)g(r)\ud r\right]\ud s.
  \end{align*}
  All norms are bounded on the finite triangle, so this exchange is
  absolute in $E$. Thus
  $Y(t)=P_\sigma^E(t)e+\int_0^tP_\sigma^E(t-r)g(r)\ud r$
  solves free Duhamel with force $B_\sigma^EY+g$.
  Take $g(r)=D_\sigma C(r)c$ and adjoin the constant block.
  This is the same $F$ Duhamel equation as the actual ordinary flow;
  uniqueness proves~\eqref{E:compact-F-block}.
  Its finite-horizon bounds are uniform since the family has bounded
  $L^\infty$ and $L^2$ norms on one compact support.

  The integral defining $f_\sigma$ is finite by $L^2$
  Cauchy--Schwarz and positive because $V_\sigma$ is nonzero by
  the common trial and $p_\sigma>0$ a.e. Its coefficients are
  continuous and uniformly bounded by the $H^2$ continuity and
  positive rate floor; no $p_\sigma\in L^1$ assumption is used.
  Directly,
  \begin{align*}
    \ell_\sigma^ED_\sigma C(r)c&=f_\sigma(c_1+rc_2),\\
    \ell_\sigma^C(c)
    &=\int_0^\infty e^{-\lambda_\sigma r}
    f_\sigma(c_1+rc_2)\ud r,\\
    \ell_\sigma^C(C(t)c)
    &=\int_t^\infty e^{\lambda_\sigma(t-r)}
    f_\sigma(c_1+rc_2)\ud r.
  \end{align*}
  These integrals converge absolutely. Applying $\ell_\sigma$ to
  \eqref{E:compact-F-block}, the finite integral and this tail
  combine to give
  $\ell_\sigma P_\sigma(t)=e^{\lambda_\sigma t}\ell_\sigma$.
  The ground mode also gives
  $P_\sigma(t)e_\sigma=e^{\lambda_\sigma t}e_\sigma$ and
  $\ell_\sigma(e_\sigma)=1$, proving~\eqref{E:compact-F-eigen}.
  Bounded bilinear multiplication and the preceding continuous
  coefficients prove norm continuity of all objects.
  Finally,
  $\ell_\sigma(e_0)=f_\sigma/\lambda_\sigma>0$ and
  $O_\phi(e_\sigma)=\int\phi p_\sigma>0$.
  Both are continuous on compact $I$, proving
  \eqref{E:compact-positive-margins}. Positivity is in integrals,
  without a point trace or a one-dimensional ODE.
  This proves Proposition~\ref{P:compact-F-projection}.
\end{proof}

\begin{proposition}[Full-phase complement and parameter control]
  \label{P:compact-F-complement}
  Uniformly over $\sigma$ and $t\ge0$,
  \begin{equation}\label{E:compact-F-complement}
    \|P_\sigma(t)Q_\sigma\|_{\mathcal B(F)}
    \le C(1+t)^3e^{\mu_\sigma t}.
  \end{equation}
  For every fixed $0<\eta<d_0$,
  \begin{equation}\label{E:compact-normalized-complement}
    \|e^{-\lambda_\sigma t}P_\sigma(t)Q_\sigma\|
    \le C_\eta e^{-\eta t}.
  \end{equation}
  For every finite $T_0$,
  \begin{equation}\label{E:compact-parameter-flow}
    \sup_{0\le t\le T_0}\|P_\sigma(t)-P_\tau(t)\|_{\mathcal B(F)}
    \le C_{T_0}
    \big(\|V_\sigma-V_\tau\|_\infty+\|V_\sigma-V_\tau\|_2\big).
  \end{equation}
\end{proposition}

\begin{proof}
  Write $Q_\sigma^E=I-\Pi_\sigma^E$. Split $D_\sigma$ into its
  growing and complementary parts in~\eqref{E:compact-F-block}
  and use the two tail integrals in the preceding proof.
  The exact $E$ component of $P_\sigma(t)Q_\sigma(e,c)$ is
  \begin{equation}\label{E:compact-complement-forcing}
    P_\sigma^E(t)Q_\sigma^Ee
    +\int_0^tP_\sigma^E(t-r)Q_\sigma^ED_\sigma C(r)c\ud r
    -e_\sigma^E\ell_\sigma^C(C(t)c),
  \end{equation}
  and the constant component is $C(t)c$. The final subtraction
  retains the growing response to constants in the projection.
  Since $\|Q_\sigma^ED_\sigma C(r)\|\le C(1+r)$, the integral
  in~\eqref{E:compact-complement-forcing} has norm at most
  \[
    Ce^{\mu_\sigma t}|c|
    \int_0^t(1+t-r)(1+r)\ud r
    =Ce^{\mu_\sigma t}(t+t^2+t^3/6)|c|.
  \]
  The first term is bounded by
  $C(1+t)e^{\mu_\sigma t}\|e\|_E$; the final term and constant
  component by $C(1+t)|c|$. Since $\mu_\sigma\ge0$ this proves
  \eqref{E:compact-F-complement}.
  The boundedness of $(1+t)^3e^{-(d_0-\eta)t}$ proves
  \eqref{E:compact-normalized-complement}. In particular, the
  constant-velocity polynomial is included in this estimate.

  Put $\mathcal B_\sigma=iB_F(V_\sigma)$ and
  $d_{\sigma,\tau}=\|V_\sigma-V_\tau\|_\infty+
  \|V_\sigma-V_\tau\|_2$.
  The bound for $B_F$ gives
  $\|\mathcal B_\sigma-\mathcal B_\tau\|\le d_{\sigma,\tau}$.
  Subtract the two free-Duhamel equations on states. Their difference
  is the sum of the integral with
  $S_F(t-r)\mathcal B_\sigma(P_\sigma(r)-P_\tau(r))$ and that with
  $S_F(t-r)(\mathcal B_\sigma-\mathcal B_\tau)P_\tau(r)$.
  The uniform finite-horizon bounds and scalar Gronwall prove
  \eqref{E:compact-parameter-flow}. The operator norm is measurable:
  separability of $F$ expresses it as the supremum over a countable
  dense set of unit states, each with continuous image.
  Hence Gronwall applies without a $\mathcal B(F)$-valued derivative
  or operator-norm continuity of the free group.
  This proves Proposition~\ref{P:compact-F-complement}.
\end{proof}

\subsection{The original positive raw control and a common trial}

\begin{lemma}[The original mean and raw variance]\label{L:compact-raw-profile}
  Let $\Gamma\ne0$ satisfy Hypothesis~\ref{H:homog}, let $a=\alpha_0$,
  and let real nonnegative nonzero
  $\Psi\in C_c^\infty((0,1)\times\R^d)$ be arbitrary, without a
  separability assumption. Define
  \begin{equation}\label{E:compact-raw-mean}
    h_\sigma(x)=\int_0^1|\sigma-u|^{-a}
    (\Gamma*\Psi(u,\cdot))(x)\ud u,\qquad
    \overline q(x)=\int_0^1\Psi(u,x)\ud u,\qquad Z=W(\Psi).
  \end{equation}
  Then $h$ is smooth in time and space on compact sets, and
  \begin{equation}\label{E:compact-raw-cost}
    0<v_\Psi:=\E Z^2
    =\int_0^1\int\Psi(\sigma,x)h_\sigma(x)\ud x\ud\sigma<\infty.
  \end{equation}
  Against every smooth compact positive-time test $F_0$,
  \[
    \E[W(\Psi)W(F_0)]=\int F_0(s,x)h_s(x)\ud x\ud s.
  \]
  Moreover, on $I$,
  \begin{equation}\label{E:compact-positive-mean-floor}
    h_\sigma\ge\Gamma*\overline q,\qquad
    v_\Psi\ge Q(\overline q)
    :=\int\Gamma(\ud z)\int\overline q(x)\overline q(x-z)\ud x>0.
  \end{equation}
  For every fixed mask, $V_\sigma=m_Rh_\sigma$ is a smooth compact
  family, Lipschitz in $\sigma$ in $L^\infty$ and $L^2$.
\end{lemma}

\begin{proof}
  Choose $A\ge1$ containing the spatial support of $\Psi$ in $B_A$.
  The raw covariance identity and absolute Fubini give the stated
  mean pairing: the two compact tests restrict spatial differences
  to a compact set of finite $\Gamma$ mass, and the time singularity
  is locally integrable since $a<1$. This identifies the actual
  linear covariance mean without evaluating noise at a point.
  The same calculation gives~\eqref{E:compact-raw-cost}.
  Its spatial integrand is bounded in integral by
  $\|\Psi\|_\infty^2|B_A|\Gamma(\overline B_{2A})$,
  and $\int_0^1\int_0^1|\sigma-u|^{-a}\ud u\ud\sigma
  =2/((1-a)(2-a))$, proving finiteness.

  Nonnegative nonzero smooth $\Psi$ has positive integral, so
  $\overline q\ne0$. Nonzero $\Gamma$ charges some ball, and
  homogeneity gives
  $\Gamma(B_1)=r^{\alpha-d}\Gamma(B_r)>0$.
  Thus every origin-centered ball $B_r$, $r>0$, has positive finite mass.
  The continuous compact autocorrelation
  $\int\overline q(x)\overline q(x-z)\ud x$
  is positive at zero and bounded below on some ball.
  This proves $0<Q(\overline q)<\infty$.
  Since $|\sigma-u|^{-a}\ge1$ on the unit time square,
  positive Tonelli gives both inequalities in
  \eqref{E:compact-positive-mean-floor}.

  Extend $\Psi$ by zero in time and write
  \[
    h_s(x)=\int_\R |r|^{-a}
    \int\Gamma(\ud z)\Psi(s-r,x-z)\ud r.
  \]
  On compact $s,x$ sets the relevant $r,z$ range over fixed
  compact sets; $|r|^{-a}$ is integrable there. Every derivative
  falls on the smooth test, not on the singular time kernel.
  Dominated differentiation gives smoothness and continuity of all
  derivatives on compacts. Multiplication by $m_R$ now gives the
  claimed compact family and its fixed-$R$ Lipschitz bounds.
  This proves Lemma~\ref{L:compact-raw-profile}.
\end{proof}

\begin{proposition}[Binding with the original control and cost fixed]
  \label{P:compact-original-common-trial}
  For every $\Psi$ in Lemma~\ref{L:compact-raw-profile}, a sufficiently
  large finite mask $m_R$ gives $V_\sigma=m_Rh_\sigma$ a common
  negative trial~\eqref{E:compact-common-trial}.
  Thus all preceding ground, projection, positive-margin and
  complementary-wave conclusions apply. The actual rate is
  Lipschitz on $I$ and has $\lambda_0>0$.
  The original test $\Psi$, raw variable $Z$ and variance $v_\Psi$
  are unchanged by this choice. The mask can additionally cover any
  fixed compact variational test supports.
\end{proposition}

\begin{proof}
  Choose a real unit $L^2$ function $\psi\in C_c^\infty(B_2)$
  with $\psi\ge c_0>0$ on $B_1$, and put
  $\psi_L(x)=L^{-d/2}\psi(x/L)$, $D_\psi=\|\nabla\psi\|_2^2$,
  where $L\ge\max(1,2A)$. Choose the actual even mask with
  $R\ge2L$, so $V_\sigma=h_\sigma$ on $\operatorname{supp}\psi_L$.
  This is the allowed real mask $0\le m_R\le1$, equal to one on $B_R$
  and with support in $\overline B_{2R}$.
  Positive Tonelli and~\eqref{E:compact-positive-mean-floor} give
  \begin{align}
    \int V_\sigma\psi_L^2
    &\ge c_0^2L^{-d}\int_{B_L}(\Gamma*\overline q)(x)\ud x\nonumber\\
    &=c_0^2L^{-d}\int\overline q(y)\Gamma(B_L-y)\ud y\nonumber\\
    &\ge c_0^2L^{-d}\Gamma(B_{L/2})\int\overline q
    =C_\Gamma L^{-\alpha},\label{E:compact-trial-potential}\\
    C_\Gamma&=c_0^22^{\alpha-d}\Gamma(B_1)\int\overline q>0.\nonumber
  \end{align}
  Here $B_{L/2}\subset B_L-y$ for $|y|\le A$ and $L\ge2A$.
  All covariance masses in the argument are compact and finite.
  The kinetic energy is $D_\psi L^{-2}$. Since $\alpha<2$,
  choose $L$ large enough that
  $\varepsilon_R:=C_\Gamma L^{-\alpha}-D_\psi L^{-2}>0$.
  Then
  \[
    \|\nabla\psi_L\|_2^2-\int V_\sigma\psi_L^2
    \le-\varepsilon_R\quad\hbox{for every }\sigma\in I.
  \]
  Fix this finite $R$ before invoking
  Proposition~\ref{P:compact-ground-family}.
  Its level bound and the mean Lipschitz estimate give
  \[
    |\lambda_\sigma-\lambda_\tau|
    \le\frac{\|V_\sigma-V_\tau\|_\infty}{2\sqrt{\varepsilon_R}}
    \le C_R|\sigma-\tau|.
  \]
  The positive mean integrates the entire time test, so
  $\lambda_0>0$ even though $\Psi(0,\cdot)=0$.
  Only the trial and mask have grown; the raw test, its variable and
  \eqref{E:compact-raw-cost} were fixed first.
  Enlarging $R$ to contain additional fixed compact test supports
  preserves the trial and gives equality of masked and unmasked
  potential energies on those supports. This includes singular
  invariant-direction covariances and the one-dimensional white case.
  It is not an all-strength binding assertion for one fixed compact
  potential. Masks are fixed before source or time asymptotics;
  a later supremum over controls must follow their individual bounds.
  This proves Proposition~\ref{P:compact-original-common-trial}.
\end{proof}

===== END TEX FILE: notes/integrated_compact_mean_family.tex =====

===== BEGIN TEX FILE: notes/integrated_exact_scaling.tex =====
\section{Exact scaling of the canonical solution}
\label{S:exact-canonical-scaling}

\begin{lemma}[Canonical law scaling]\label{L:exact-canonical-scaling}
  Under Hypothesis~\ref{H:homog}, put $a=\alpha_0$,
  $\kappa=(4-\alpha-a)/(3-\alpha)$, and, for $T>0$,
  \[
    \delta=T^{-\kappa},\qquad
    r_T=T\delta=T^{(a-1)/(3-\alpha)}.
  \]
  The law of $u(Tt,r_Tx)$ is the canonical expansion solution
  $V_\delta(t,x)$ with data $(1,0)$ of
  \begin{equation}\label{E:exact-fast-equation}
    \delta^2\partial_t^2V_\delta
    =\Delta V_\delta+\sqrt\delta\,\W V_\delta,
  \end{equation}
  where $\W$ has the original raw covariance. In particular,
  \begin{equation}\label{E:exact-moment-scaling}
    T^{-\kappa}\log\E|u(T,0)|^2
    =\delta\log\E|V_\delta(1,0)|^2.
  \end{equation}
  The assertion is equality in law; it assumes no pathwise uniqueness
  for a full rough solution.
\end{lemma}

\begin{proof}
  At positive widths, time and space dilation of the Gaussian source
  gives covariance amplitude $T^{-a}r_T^{-\alpha}$. This follows
  distributionally from the homogeneous Radon covariance, including
  spatial white noise. Its source cutoffs transform by
  $K_\eta(Ts)=T^{-a}K_{\eta/T}(s)$ and
  $\epsilon\mapsto\epsilon/r_T^2$; the joint maximum-time and
  summed-space width laws are preserved at every vertex.
  The actual Green measure has the scaling
  \[
    G_d(T\tau,r_T\ud z)
    =r_TG_d(\tau/\delta,\ud z).
  \]
  It follows from its degree $1-d$ distributional scaling, also for
  the sphere measure in dimension three. Each terminal Duhamel
  vertex thus contributes
  $Tr_T\,T^{-a/2}r_T^{-\alpha/2}$.
  Substitution of the displayed positive real powers gives
  \[
    T^{-a/2}r_T^{2-\alpha/2}=\sqrt\delta,\qquad
    T^{1-a/2}r_T^{1-\alpha/2}=\delta^{-1/2}.
  \]
  The Green kernel for the forcing in~\eqref{E:exact-fast-equation}
  is $\delta^{-1}G_d((t-s)/\delta)$; after multiplication by
  $\sqrt\delta$ it gives exactly that vertex factor.
  Therefore every finite list of fixed-order coefficients has the
  same joint law under the dilation, including all self-pairings,
  unequal orders and empty chains. At fixed $T,r_T$, remove Green
  smoothing first in dimension three, with its width divided by
  $r_T^2$ on the scaled side. Lemma~\ref{L:joint-fixed-order} and
  the absolute $L^2$ summability in Lemma~\ref{L:vertex-crude} pass
  the identities to the canonical series and its second moment.
  No large-time and source limit are interchanged. This proves the
  law assertion and~\eqref{E:exact-moment-scaling}.
  This proves Lemma~\ref{L:exact-canonical-scaling}.
\end{proof}

===== END TEX FILE: notes/integrated_exact_scaling.tex =====

===== BEGIN TEX FILE: notes/integrated_raw_block_lower.tex =====
\section{Actual raw blocks and the original point lower bound}
\label{S:actual-raw-block-lower}

Fix a nonzero covariance from Hypothesis~\ref{H:homog} and any real
nonnegative nonzero $\Psi\in C_c^\infty((0,1)\times\R^d)$.
Retain the \emph{original} $Z=W(\Psi)$, $v=v_\Psi>0$ and mean $h_s$
of Lemma~\ref{L:compact-raw-profile}. Choose one finite even mask
$m_R\in[0,1]$, equal to one on $B_R$ and supported in $\overline B_{2R}$,
as in Proposition~\ref{P:compact-original-common-trial}.
Then $V_s=m_Rh_s$ has the ground family, rate $\lambda_s$ and full
$F$ projection of Section~\ref{S:compact-mean-family}. Set
\[
  I_R=\int_0^1\lambda_s\ud s,\qquad
  Q_2=\liminf_{T\to\infty}T^{-\kappa}\log\E|u(T,0)|^2.
\]
We will prove $Q_2\ge2I_R-v/2$, for this same control and covariance.
Fix a real nonnegative smooth compact $\phi$ of integral one, the
bounded observable $O_\phi$, and the actual data $e_0=(0,1,0)\in F$.
Both displacement and velocity are retained.
This is the same physical profile $m_R=\zeta_R$ used in the actual
driver and compact mean; no mask is changed in a covariance identity.
The semiscaled $W$ below is the given raw-law noise. The comparison to
the unscaled solution uses equality in law, not samplewise identities
on one probability space for every $T$.

\subsection{The common raw noise and its exact Gaussian shift}

Choose an integer $B\ge1$, later fixed by the cone estimate, and take
$0<\delta<\min(1,1/B)$. Define
\begin{equation}\label{E:raw-block-clocks}
  N=\left\lfloor\frac1{\delta B}\right\rfloor\ge1,\quad
  s_m=m\delta B\ (0\le m\le N),\quad
  \tau=\delta^{-1}-NB\in[0,B),\quad
  g_\delta=\delta^{(1-a)/2}.
\end{equation}
For a smooth compact positive-fast-time test $f$, extended by zero,
put
\begin{equation}\label{E:raw-block-pullback}
  T_{\delta,m}f(s,x)
  =\delta^{a/2-1}f((s-s_m)/\delta,x),\qquad
  W_{\delta,m}(f)=W(T_{\delta,m}f).
\end{equation}
Write $W_{\mathrm{fast}}=W_{\delta,0}$.
Use the same admissible $\gamma,\theta,\beta$ as
\eqref{E:driver-parameters}. Write $A_R(W_{\delta,m})$ for the
actual $F$ first driver obtained by the bounded extension
\eqref{E:constant-phase-driver}, on the local horizon $[0,B]$, and set
\begin{equation}\label{E:raw-block-drivers}
  X_m=g_\delta A_R(W_{\delta,m}),\qquad
  H_m(u)=\int_0^uS_F(-r)iB_F(V_{s_m+\delta r})S_F(r)\ud r.
\end{equation}
The convolution formula for $h$ extends smoothly to $s\in[0,2]$,
covering these means. Ground templates will only use $s_m\in[0,1]$.

\begin{lemma}[Actual coupled Gaussian block inputs]\label{L:raw-block-inputs}
  Each $T_{\delta,m}$ is an isometry of the raw test completion,
  respecting covariance-null tests. All $W_{\delta,m}$ and $Z$
  are on the same given noise space, without an independence assertion.
  Let $\mathcal K(F)$ have the operator norm and let
  $\mathscr B_0=h_0^\theta([0,B];\mathcal K(F))$ be the
  $C^\theta$ closure of zero-initial polygonal compact-operator paths.
  It is a separable Banach space. In
  $\mathscr B_\delta=\mathscr B_0^{N+1}$ with maximum norm,
  $(X,Z)$, $X=(X_m)_{m=0}^N$, is jointly centered Gaussian and
  \begin{equation}\label{E:raw-block-covariance}
    b:=\E[XZ]=\sqrt\delta\,H,\qquad H=(H_m)_{m=0}^N.
  \end{equation}
  Moreover,
  \begin{equation}\label{E:raw-block-moments}
    \|X_m\|_{L^p\mathscr B_0}
    \le C_{R,B}\sqrt p\,g_\delta,\qquad p\ge1.
  \end{equation}
\end{lemma}

\begin{proof}
  Substituting $s=s_m+\delta u$, $t=s_m+\delta r$ in the raw
  covariance gives the factor
  $\delta^{a-2}\delta^2\delta^{-a}=1$.
  Thus the maps extend isometrically through the null quotient.
  Direct test substitution gives
  $W_{\delta,m}(f)=W_{\mathrm{fast}}(f(\cdot-mB,\cdot))$.
  These are literal common-space identities.

  Finite-rank rational matrices in a countable real Hilbert basis
  are dense in $\mathcal K(F)$: for compact $T$,
  $P_nTP_n\to T$ in norm by compactness of $T,T^*$, and finite
  entries admit rational approximation. Polygonal paths with rational
  breakpoints and such matrices give separability of $\mathscr B_0$.
  To approximate breakpoints, use uniform convergence, uniform
  Lipschitz bounds and
  $[f]_\theta\le(2\|f\|_\infty)^{1-\theta}\operatorname{Lip}(f)^\theta$.
  The same inequality puts every zero-initial Lipschitz
  compact-valued path in $\mathscr B_0$ by polygonal approximation.
  The finite raw coefficient paths $iA_jL_\psi$ have these properties.
  Their actual Gaussian sums converge in $L^pC^\theta$ and hence
  in the closed space $\mathscr B_0$. Their laws and the parent
  Gaussian norm bound give~\eqref{E:raw-block-moments}.
  Every finite joint coefficient list with $Z$ is Gaussian on the
  same $W$. Scalar continuous functionals pass through the $L^2$
  limits, preserving Gaussianity by convergence of variances and
  characteristic functions. Thus $(X,Z)$ is the asserted Banach
  Gaussian variable. Cauchy--Schwarz gives
  $\E\|XZ\|\le\|X\|_2\sqrt v<\infty$, so its Bochner covariance exists.

  The original raw covariance and the test pullback give
  \begin{equation}\label{E:raw-block-mean-jacobian}
    \E[W_{\delta,m}(f)Z]
    =\delta^{a/2}\int f(u,x)h_{s_m+\delta u}(x)\ud x\ud u.
  \end{equation}
  Absolute Fubini uses compact supports, local Radon mass and $a<1$.
  This identity extends to the literal driver matrix tests on $E$:
  their time indicator is approximated by smooth bounded tests on one
  compact support, converging in the raw norm by dominated convergence
  against $|u-r|^{-a}\Gamma$; their mean pairings converge as well.
  The actual Sobolev adjoint is the one in
  \eqref{E:driver-covariance-row}. Hence the path covariance is
  $g_\delta\delta^{a/2}H_m=\sqrt\delta\,H_m$ on real Schwartz
  $E$ pairs. For constant inputs the two columns are the same
  $L_\psi$ inputs $(\psi,0)$ and $(0,\psi)$, and total finite
  propagation identifies their deterministic response.
  The span of $E$ and both constant coordinates is dense in $F$;
  $E$ alone is not. Boundedness, rational times and path continuity
  prove~\eqref{E:raw-block-covariance} on all $F$.
  In particular $H=b/\sqrt\delta\in\mathscr B_\delta$.
  This proves Lemma~\ref{L:raw-block-inputs}.
\end{proof}

\begin{proposition}[Change of law on the whole norm-Borel space]
  \label{P:raw-block-gaussian-law}
  For every nonnegative norm-Borel $j$ on all of $\mathscr B_\delta$,
  \begin{equation}\label{E:raw-block-gaussian-law}
    \E j(X)=
    \E\left[e^{-Z/\sqrt\delta-v/(2\delta)}j(X+H)\right].
  \end{equation}
  The equality is valid also as an extended nonnegative integral.
\end{proposition}

\begin{proof}
  For real $s$, the density $e^{-sZ-s^2v/2}$ defines an equivalent
  probability measure $Q_s$ by completing the square in the
  $N(0,v)$ density. For any finite list $\ell$ of continuous real
  coordinates on $\mathscr B_\delta$, the Gaussian vector
  $(\ell(X),Z)$ is equal in law to $(TG,z\cdot G)$ for a finite
  standard Gaussian vector $G$. A positive covariance square root
  gives this representation even when singular; no inverse is used.
  Here $Tz=\ell(b)$ and $|z|^2=v$. Substitution $G'=G+sz$ in its
  density gives
  $\E_{Q_s}f(\ell(X+sb))=\E f(\ell(X))$ for every bounded Borel $f$.

  The matrix entries of each block in a real Hilbert basis at
  rational times, together with $0,B$, generate the norm-Borel
  sigma-field. To see the operator-norm point, for a countable dense
  set $\mathcal D$ of unit vectors obtained from normalized rational
  finite basis combinations,
  $\|T\|=\sup_{u,w\in\mathcal D}|\langle Tu,w\rangle|$.
  These pairings are finite linear combinations of matrix entries.
  Supremum and H\"older norms of continuous paths are suprema over
  rational times and pairs. Thus distance to every fixed element
  of $\mathscr B_\delta$ is coordinate-measurable. Open balls are
  measurable by rational closed-ball approximation, and separability
  makes every open set a countable union of balls from dense centers.
  Conversely the coordinates are continuous.
  The cylinder sets form a generating pi-system; uniqueness of
  probability measures extends the finite-coordinate equality to
  all norm-Borel sets. Simple functions and monotone convergence
  give the identity for nonnegative $j$. Finally take
  $s=\delta^{-1/2}$ and use $sb=H$ from
  \eqref{E:raw-block-covariance}. The map and its deterministic
  translate are defined on the entire input space; there is no
  translated exceptional-domain assumption.
  This proves Proposition~\ref{P:raw-block-gaussian-law}.
\end{proof}

\subsection{Small noisy blocks and an indexed full-phase cone}

For any $x\in\mathscr B_0$ define
$D_x(u)=S_F(u)U_x(u,0)$ by the everywhere-defined linear Young
map of Proposition~\ref{P:constant-young-linear}.
Write $D_m^0=D_{X_m}$ and $D_m^+=D_{X_m+H_m}$.
The latter retains both the mean and the actual residual noise.

\begin{lemma}[Uniform block error]
  \label{L:raw-block-uniform-error}
  Let $M_\delta=\max_{m\le N}\|X_m\|_{\mathscr B_0}$, including
  its factor $g_\delta$. Then $M_\delta\to0$ in every finite $L^q$,
  and, for some $c>0$,
  \begin{equation}\label{E:raw-block-maximum-exponential}
    \sup_\delta\E e^{cM_\delta^2}<\infty.
  \end{equation}
  With the actual deterministic $P_s$ in~\eqref{E:compact-F-block},
  \begin{equation}\label{E:raw-block-operator-error}
    E_{\mathrm{op},\delta}:=
    \max_{m\le N}\sup_{0\le u\le B}
    \|D_m^+(u)-P_{s_m}(u)\|_{\mathcal B(F)}
    \longrightarrow0
    \quad\hbox{in every finite }L^q.
  \end{equation}
\end{lemma}

\begin{proof}
  The maximum and~\eqref{E:raw-block-moments}, with $N+1\le2/\delta$,
  give
  \[
    \|M_\delta\|_p
    \le (N+1)^{1/p}C\sqrt p\,g_\delta
    \le C'\sqrt p\,\delta^{(1-a)/2-1/p}.
  \]
  For fixed $q$, choose $p>\max(q,2/(1-a))$ to prove the first limit.
  No independence is needed. Choose an integer $n_0$ with
  $n_0(1-a)\ge1$. For $n\ge n_0$,
  \[
    \E M_\delta^{2n}
    \le2C^{2n}(2n)^n\delta^{n(1-a)-1}
    \le2C^{2n}(2n)^n.
  \]
  For $1\le n<n_0$, Lyapunov bounds the moment by the appropriate
  power of the $2n_0$ moment. These finitely many terms are bounded.
  For the remaining exponential series, $n!\ge(n/e)^n$ gives
  a geometric tail $2\sum_{n\ge n_0}(2ecC^2)^n$ for small $c$.
  This proves~\eqref{E:raw-block-maximum-exponential}; no such
  assertion is made for the unscaled maximum.

  Let $H_m^{\mathrm{stat}}$ be the primitive for constant potential
  $V_{s_m}$. Compact mean smoothness on $[0,2]$ and the statewise
  primitive bound give
  \[
    \sup_m\max(\|H_m\|_{C^\theta},
    \|H_m^{\mathrm{stat}}\|_{C^\theta})\le H_0,\qquad
    \sup_m\|H_m-H_m^{\mathrm{stat}}\|_{C^\theta}\le C\delta.
  \]
  Indeed, the potential difference is at most $C\delta B$ in
  $L^\infty$ and $L^2$; integration of the bounded free groups
  gives its Lipschitz primitive bound on this fixed horizon.
  On $\{M_\delta\le1\}$, local Young stability on the fixed ball
  of radius $H_0+1$ gives
  $E_{\mathrm{op},\delta}\le C(M_\delta+\delta)$.
  This proves convergence in probability. The global Young bound
  also gives
  \[
    \max_m\sup_{u\le B}\|D_m^+(u)\|
    \le C_B\exp\big(C_B(1+H_0+M_\delta)^{1/\theta}\big).
  \]
  Since $1/\theta<2$, every finite power of this bound is dominated
  by a constant times the exponential in
  \eqref{E:raw-block-maximum-exponential}.
  Uniform higher moments yield uniform integrability, proving
  \eqref{E:raw-block-operator-error}. Suprema are measurable:
  on a countable dense set of unit states each difference is
  continuous in $u$, so rational times and those states suffice.
  Operator-norm continuity of the physical free group is not used.
  Only $s_m\le1$ supplies the ground templates.
  This proves Lemma~\ref{L:raw-block-uniform-error}.
\end{proof}

\begin{lemma}[Indexed cone and terminal displacement]
  \label{L:raw-block-indexed-cone}
  Fix $0<\varrho<1/2$. There are an integer $B\ge1$ and positive
  $\omega,\epsilon_{\mathrm{op}},c_*$ such that the following holds
  for every $N\ge1$. If $\sigma_0,\ldots,\sigma_N\in I$ have
  adjacent distances at most $\omega$ and real bounded operator
  families $D_m(u)$, $0\le u\le B$, satisfy
  \[
    \max_{m\le N}\sup_{0\le u\le B}
    \|D_m(u)-P_{\sigma_m}(u)\|\le\epsilon_{\mathrm{op}},
  \]
  then, for $0\le u\le B$,
  \begin{equation}\label{E:raw-block-positive-product}
    O_\phi D_N(u)D_{N-1}(B)\cdots D_0(B)e_0
    \ge c_*(1-\varrho)^{N-1}
    \exp\left(B\sum_{m<N}\lambda_{\sigma_m}
    +u\lambda_{\sigma_N}\right)>0.
  \end{equation}
  No positivity, composition or independence assumption on the $D_m$
  is required.
\end{lemma}

\begin{proof}
  From~\eqref{E:compact-normalized-complement} fix
  $C_{\mathrm{gap}}\ge1$, $\eta_{\mathrm{gap}}>0$ so the normalized
  complementary norm is at most
  $C_{\mathrm{gap}}e^{-\eta_{\mathrm{gap}}t}$.
  Define positive margins and finite bounds
  \[
    a_*=\inf_I\ell_s(e_0),\quad j_*=\inf_I O_\phi(e_s),\quad
    M_e=\max(1,\sup_I\|e_s\|),\quad
    M_\ell=\max(1,\sup_I\|\ell_s\|).
  \]
  Also put $M_P=\max(1,\sup_I\|\Pi_s\|)$,
  $M_Q=1+M_P$, $M_z=M_e+1$, $E_0=\|e_0\|=1$ and
  $H_{\mathrm{obs}}=\max(1,\|O_\phi\|)$.
  Choose the aperture \emph{first}:
  $\vartheta=\min(1,j_*/(16H_{\mathrm{obs}}C_{\mathrm{gap}}))>0$.
  Next choose integer $B\ge1$ with
  \[
    q_B:=C_{\mathrm{gap}}e^{-\eta_{\mathrm{gap}}B}
    \le\min\left(\frac18,\frac{\vartheta a_*}{8M_QE_0}\right).
  \]
  Choose $\nu>0$ such that
  $\nu M_z\le\min(\varrho/2,\vartheta,1/4)$.
  Uniform continuity of $\ell_s,\Pi_s$ supplies $\omega>0$
  for which adjacent distances at most $\omega$ give both norm
  differences at most $\nu$. Finally choose $\epsilon_{\mathrm{op}}>0$
  satisfying all five budgets
  \begin{align*}
    M_\ell\epsilon_{\mathrm{op}}M_z&\le\varrho/2,&
    M_Q\epsilon_{\mathrm{op}}M_z&\le\vartheta/4,\\
    M_\ell\epsilon_{\mathrm{op}}E_0&\le a_*/2,&
    M_Q\epsilon_{\mathrm{op}}E_0&\le\vartheta a_*/8,&
    H_{\mathrm{obs}}\epsilon_{\mathrm{op}}M_z&\le j_*/8.
  \end{align*}
  All denominators are positive. This order of choices uses the
  normalized complement rather than a growing terminal norm.

  The cone at $s$ consists of $z=Ae_s+r$, with
  $A=\ell_s(z)>0$, $\ell_s(r)=0$ and $\|r\|_F\le\vartheta A$.
  In particular $r=Q_sz$ and $\|z\|\le M_zA$.
  For entrance, $z_1=D_0(B)e_0$, with $b=\sigma_0$, has normalized
  amplitude at least
  $a_*-M_\ell\epsilon_{\mathrm{op}}E_0\ge a_*/2$.
  Its normalized residual is at most
  $q_BM_QE_0+M_Q\epsilon_{\mathrm{op}}E_0
  \le\vartheta a_*/4$.
  Thus it enters the cone with residual ratio at most $\vartheta/2$
  and amplitude at least $e^{\lambda_bB}a_*/2$.

  For an old-cone state $z=Ae_b+r$ and an adjacent index $c$,
  rebase before using the complementary estimate:
  \[
    \ell_c(z)\ge(1-\nu M_z)A,\qquad
    \|Q_cz\|\le\|Q_bz\|+\|(\Pi_b-\Pi_c)z\|
    \le(\vartheta+\nu M_z)A.
  \]
  For the next full block $D$ close to $P_c(B)$, put
  $x=e^{-\lambda_cB}\ell_c(Dz)$ and
  $y=e^{-\lambda_cB}\|Q_cDz\|$.
  Since $\lambda_c>0$, the perturbation and budgets give
  \[
    x\ge(1-\nu M_z-M_\ell\epsilon_{\mathrm{op}}M_z)A
    \ge(1-\varrho)A>A/2,
  \]
  and
  \[
    y\le
    [q_B(\vartheta+\nu M_z)+M_Q\epsilon_{\mathrm{op}}M_z]A
    \le\vartheta A/2.
  \]
  The last inequality uses
  $q_B\le1/8$, $0\le\nu M_z\le\vartheta$ and
  $M_Q\epsilon_{\mathrm{op}}M_z\le\vartheta/4$.
  Together with $\varrho<1/2$, these give $y\le\vartheta x$.
  These are precisely the finite residual and cone-conversion margins;
  the old residual was not assumed to lie in the new kernel.
  Each full block therefore preserves the new cone and multiplies
  its amplitude by at least $e^{\lambda_cB}(1-\varrho)$.

  For the terminal $0\le u\le B$, rebase once more to $c=\sigma_N$.
  The same bounds give $\ell_c(z)\ge3A/4$ and
  $\|Q_cz\|\le2\vartheta A$. Consequently,
  \[
    e^{-\lambda_cu}O_\phi(P_c(u)z)/A
    \ge3j_*/4-2H_{\mathrm{obs}}C_{\mathrm{gap}}\vartheta.
  \]
  The perturbation changes this by at most
  $H_{\mathrm{obs}}\epsilon_{\mathrm{op}}M_z\le j_*/8$.
  Since $16H_{\mathrm{obs}}C_{\mathrm{gap}}\vartheta\le j_*$,
  the result is at least $j_*/2$.
  Combine entrance, all $N-1$ intermediate full blocks and this
  terminal estimate to obtain~\eqref{E:raw-block-positive-product},
  with $c_*=a_*j_*/4$. The induction is empty for $N=1$ and
  the estimate includes $u=0$.
  This proves Lemma~\ref{L:raw-block-indexed-cone}.
\end{proof}

\subsection{Actual source restart and comparison with the original point}

\begin{lemma}[The actual raw restart and source products]
  \label{L:raw-block-restart}
  Fix $\delta,B,N$ and let $L=\delta^{-1}$,
  $L_{\mathrm{ext}}=(N+1)B\ge L$. On this global fast horizon define
  $A_{\mathrm{glob}}=g_\delta A_R(W_{\mathrm{fast}})$.
  Its actual physical flow obeys
  \begin{equation}\label{E:raw-block-restart}
    P_{\mathrm{glob}}(mB+u,mB)=D_m^0(u),\qquad 0\le u\le B.
  \end{equation}
  The analogous identity holds with the deterministic mean
  $V_{\delta t}$ added globally and local drivers $X_m+H_m$.
  Their finite block products, including the last remainder $\tau$,
  are actual source limits in $L^2$, at this fixed $\delta,N$.
\end{lemma}

\begin{proof}
  Take one retaining slow source $Y_{\epsilon,\eta}$ on the
  extension of the given $W$ constructed in
  Section~\ref{S:source-driver-convergence}. Define the actual
  fast and local noises by
  \[
    Y_{\mathrm{fast}}(f)=Y_{\epsilon,\eta}(T_{\delta,0}f),\qquad
    Y_m(f)=Y_{\epsilon,\eta}(T_{\delta,m}f).
  \]
  The pullback isometry and~\eqref{E:source-two-dominations} give
  source and residual variance bounds by $\|f\|_{H_W}^2$.
  The residual tends to zero on each transformed smooth compact test
  at fixed $\delta,m$. Joint Gaussianity is retained.
  Proposition~\ref{P:source-gaussian-transfer} therefore gives the
  actual $L^pC^\theta$ first-driver limits on $[0,L_{\mathrm{ext}}]$
  and on $[0,B]$, including both constant columns.

  Their pointfields are
  $Y_{\mathrm{fast}}(u,x)=\delta^{a/2}Y_{\epsilon,\eta}(\delta u,x)$
  and $Y_m(u,x)=Y_{\mathrm{fast}}(mB+u,x)$.
  Indeed, these follow by change of variables in their test integrals.
  The temporal law is $K_{\eta/\delta}$ because
  $\delta^aK_\eta(\delta r)=K_{\eta/\delta}(r)$;
  the spatial heat law and all joint width rules are unchanged.
  They are continuous in time and smooth in space.
  Their ordinary primitives equal their Gaussian-transfer drivers:
  their actual matrix entries are $Y_m(h_R)$, by the indicator
  approximation used in~\eqref{E:raw-block-mean-jacobian} and the
  point-test integral identity. Total finite propagation extends
  this identity to both constant columns.
  This does not assume a separately chosen retaining extension
  automatically commutes with time dilation.

  Changing the ordinary source integration variable and composing
  the free groups gives the exact identity on $F$
  \[
    S_F(mB)\big[A_{\mathrm{glob}}^{\mathrm{src}}(mB+u)
    -A_{\mathrm{glob}}^{\mathrm{src}}(mB)\big]
    S_F(-mB)=X_m^{\mathrm{src}}(u).
  \]
  No physical mask is commuted through a wave group.
  Restriction, difference and conjugation are bounded maps on
  these fixed-horizon $C^\theta$ spaces. Passing the actual source
  limits gives the same identity for $A_{\mathrm{glob}},X_m$.
  For the finitely many $m$, a convergent subsequence or rational
  times and path continuity gives simultaneous identities in $u$.
  Conjugation norms need only be finite at this fixed $\delta$.

  Conjugate the global interaction Young equation on
  $[mB,mB+u]$ by $S_F(mB)$. Bounded linearity of its Riemann sums
  and that raw identity give the local equation driven by $X_m$.
  Uniqueness identifies it with $U_{X_m}$, proving
  \eqref{E:raw-block-restart}. The ordinary deterministic primitive
  for $V_{\delta t}$ has the identical cocycle with local $H_m$.
  Composition now identifies the full product, with terminal $\tau$.

  For completeness, source convergence of these finite products
  requires no growing-product stability assertion. At fixed $\delta,N$
  let $C\ge1$ be the maximum norm of their source and raw factors,
  and let $e_{\mathrm{src}}$ be the maximum factor difference.
  The parent Young convergence gives every finite moment of $C$
  uniformly in source widths and $e_{\mathrm{src}}\to0$ in every
  finite $L^p$. If $d(n)$ is the difference of the first $n$
  ordered products, then
  \[
    d(n+1)\le C d(n)+C^n e_{\mathrm{src}},\qquad d(0)=0.
  \]
  Extend both finite sequences by identities so the recurrence
  holds for all natural $n$. The finite error-accumulation estimate
  gives $d(N+1)\le(N+1)C^{N+1}e_{\mathrm{src}}$.
  H\"older, using $C$ in $L^{4(N+1)}$ and the error in $L^4$,
  proves $L^2$ convergence. This is only a fixed-$\delta$ source limit.
  Shifted source products may use the fixed raw mean plus the
  regularized noise; no finite-source Cameron mean is substituted.
  This proves Lemma~\ref{L:raw-block-restart}.
\end{proof}

\begin{proposition}[The square observable and canonical comparison]
  \label{P:raw-block-point-comparison}
  Define the signed noise-only and shifted averages
  \[
    U_{\delta,B}
    =O_\phi D_N^0(\tau)D_{N-1}^0(B)\cdots D_0^0(B)e_0,
    \qquad
    Y_{\delta,B}
    =O_\phi D_N^+(\tau)D_{N-1}^+(B)\cdots D_0^+(B)e_0.
  \]
  They have all finite unweighted moments, and
  \begin{align}
    \E U_{\delta,B}^2
    &=\E\left[e^{-Z/\sqrt\delta-v/(2\delta)}
    Y_{\delta,B}^2\right],
    \label{E:raw-block-square-identity}\\
    \E U_{\delta,B}^2
    &\le\E|V_\delta(1,0)|^2
    =\E|u(T,0)|^2,\qquad \delta=T^{-\kappa}.
    \label{E:raw-block-original-comparison}
  \end{align}
  The variance $v$ in the density is the original slow raw variance.
\end{proposition}

\begin{proof}
  On all of $\mathscr B_\delta$ put
  \[
    j_\delta(x)=
    |O_\phi D_{x_N}(\tau)D_{x_{N-1}}(B)\cdots D_{x_0}(B)e_0|^2.
  \]
  The everywhere-defined continuous Young map, fixed-time bounded
  free groups, finite products and bounded $O_\phi$ make $j_\delta$
  continuous and nonnegative on the whole input space.
  Apply Proposition~\ref{P:raw-block-gaussian-law} directly to these
  raw paths. Since $X+H$ is its exact translate, this proves
  \eqref{E:raw-block-square-identity} with the original single
  $Z=W(\Psi)$ and its variance $v$. Finite products of the local
  Young flows have every finite unweighted moment by their Gaussian
  path bounds and H\"older, at fixed $\delta,N$.
  The Gaussian identity itself did not require prior integrability
  of $j_\delta$. No source convergence under its exponential density
  is used.

  To apply the masked comparison at the actual amplitude, put
  $\Gamma_\delta=g_\delta^2\Gamma$ and
  $W'=g_\delta W_{\mathrm{fast}}$.
  This is a nonzero member of the same admissible covariance class,
  with unchanged degree $\alpha$ and temporal parameter $a$.
  Its actual first driver is $g_\delta$ times the original one:
  the raw matrix forms are linear in noise, and basis-independent
  Gaussian transfer and the bounded $F$ extension retain both
  constant columns. The $n$th source chain is multiplied by
  $g_\delta^n$. Thus this is exactly the noise-only model at that
  amplitude.

  We verify the source-limit premise of the masked comparison.
  Keep $\delta,B,N$ fixed and use the single retaining source of
  Lemma~\ref{L:raw-block-restart}. For $m<N$ let
  $F_m=D_m^0(B)$ and put $F_N=D_N^0(\tau)$; write $F_{m,\rho}$
  for the corresponding ordinary source factors, where both source
  widths in $\rho$ tend to zero. Lemma~\ref{L:raw-block-restart}
  and Proposition~\ref{P:constant-gaussian-flow} give factor convergence
  in every finite $L^q$ and uniform bounds for every finite moment
  of their norms. These statements are on the fixed finite horizons
  $[0,(N+1)B]$ and $[0,B]$, and include both constant-response columns.
  Set $n=N+1$ and
  \[
    C_\rho=\max\left(1,\max_{m\le N}\|F_{m,\rho}\|,
    \max_{m\le N}\|F_m\|\right),\qquad
    e_\rho=\max_{m\le N}\|F_{m,\rho}-F_m\|.
  \]
  Then $\sup_\rho\|C_\rho\|_q<\infty$ for every finite $q$, and
  $\|e_\rho\|_q\to0$. Telescoping the actual ordered products gives
  \[
    \|F_{N,\rho}\cdots F_{0,\rho}-F_N\cdots F_0\|
    \le n C_\rho^n e_\rho.
  \]
  Therefore, H\"older with exponents $4n$ and $4$ gives
  \[
    \big\|F_{N,\rho}\cdots F_{0,\rho}-F_N\cdots F_0\big\|_{L^2}
    \le n\|C_\rho\|_{L^{4n}}^n\|e_\rho\|_{L^4}
    \longrightarrow0.
  \]
  No uniform estimate in the growing number $N$ is needed: this
  source limit is completed at each fixed $\delta,N$.
  The physical source identification in
  Lemma~\ref{L:constant-source-solution}, with the same $m_R$ and
  initial state $e_0$, identifies the source product with the tested
  ordinary masked solution at fast time $L=1/\delta$.
  Boundedness of $O_\phi$ and $\|e_0\|=1$ thus identify
  $U_{\delta,B}$ as its actual $L^2$ limit.
  The sources $g_\delta Y_{\mathrm{fast}}$ have the correct law,
  contraction and raw-test limit by Lemma~\ref{L:raw-block-restart}.

  At positive source widths, $0\le m_R\le1$ multiplies each
  nonnegative displacement Wick integrand by the product of its
  vertex masks. Positive Green measures and covariance retain this
  comparison for unequal, self and empty chains as well.
  Proposition~\ref{P:masked-source-moments} gives the tested comparison,
  and the just-proved $L^2$ convergence discharges the premise of
  Proposition~\ref{P:masked-canonical-transfer} at $\Gamma_\delta$.
  Its canonical unmasked moment limit uses the fixed-order joint
  source limits and the absolutely summable order bounds.
  Since $\phi\ge0$ and $\int\phi=1$, these facts give
  \[
    \E U_{\delta,B}^2
    \le\E|u_{\Gamma_\delta}(L,0)|^2.
  \]
  Only the noise-only source products were needed for this passage.
  The shifted raw product is already the everywhere-defined
  $j_\delta(X+H)$ in the Gaussian identity; no tilted source limit
  or change of the original slow $\Psi,Z,v$ has been made.

  The ordinary change from fast $u$ to slow $t=\delta u$, with
  phase $(V,\delta V_t)$, transforms the unmasked source equation
  into the regularized version of~\eqref{E:exact-fast-equation},
  with slow terminal time one. Indeed,
  $g_\delta Y_{\mathrm{fast}}(u)
  =\sqrt\delta\,Y_{\epsilon,\eta}(\delta u)$,
  and its fast cutoff is $\eta/\delta$.
  The canonical fixed-order and absolutely convergent series
  construction passes this law identity at fixed $\delta$ to the
  raw moment, preserving every mixed, unequal, self and empty chain.
  Lemma~\ref{L:exact-canonical-scaling} gives the final equality
  in~\eqref{E:raw-block-original-comparison}.
  The physical scale $r_T=T\delta$ is distinct from the fixed
  mask radius $R$. The mask need not contain the growing backward
  cone: the comparison is a moment inequality, not equality of
  masked and full fields. All source limits preceded this large-time
  comparison.
  This proves Proposition~\ref{P:raw-block-point-comparison}.
\end{proof}

\begin{proposition}[Original point lower rate at the raw half-cost]
  \label{P:raw-block-original-lower}
  For every original positive $\Psi$ and eligible fixed mask $R$
  chosen above, and every fixed $x\in\R^d$,
  \begin{equation}\label{E:raw-block-original-lower}
    \liminf_{T\to\infty}T^{-\kappa}\log\E|u(T,x)|^2
    \ge 2\int_0^1\lambda_s\ud s-\frac{v_\Psi}{2}.
  \end{equation}
\end{proposition}

\begin{proof}
  Fix $e_{\mathrm{rate}}>0$. Choose $0<\varrho<1/2$ with
  $\log(1-\varrho)>-e_{\mathrm{rate}}/3$, then choose the cone
  constants, including an integer $B$ fixed independently of $\delta$,
  from Lemma~\ref{L:raw-block-indexed-cone}.
  The control $\Psi$ and eligible mask $R$ remain fixed throughout.

  Choose a finite $p>2/(1-a)$ and put
  $\gamma_p=p(1-a)/2-1>0$. From~\eqref{E:raw-block-moments} and
  $N+1\le2/\delta$, Markov and the union bound give, for $\eta>0$,
  \[
    \begin{split}
      \mathbb P(M_\delta>\eta)
      &\le\eta^{-p}\sum_{m=0}^N
      \E\|X_m\|_{C^\theta}^p\\
      &\le A_p\eta^{-p}\delta^{\gamma_p},\qquad
      A_p=2(C_{R,B}\sqrt p)^p<\infty.
    \end{split}
  \]
  This estimate concerns the actual coupled blocks; no independence
  is needed. At these fixed data $A_p$ is independent of $\delta$.

  We also specify the deterministic tolerance used with this bound.
  The primitive estimates in Lemma~\ref{L:raw-block-uniform-error}
  give, for the constant-potential primitives $H_m^{\mathrm{stat}}$,
  \[
    \max_m\max(\|H_m\|_{C^\theta},
    \|H_m^{\mathrm{stat}}\|_{C^\theta})\le H_0,\qquad
    \max_m\|H_m-H_m^{\mathrm{stat}}\|_{C^\theta}\le C_B\delta.
  \]
  Apply Proposition~\ref{P:constant-young-linear} on the fixed
  driver ball of radius $H_0+1$ and use the bounded free groups on
  $[0,B]$. There is $L_B\ge1$, depending on these fixed $R,B,\Psi$
  and the admissible exponents, such that on $\{M_\delta\le1\}$,
  \[
    E_{\mathrm{op},\delta}\le L_B(M_\delta+\delta).
  \]
  Set $\eta=\min(1,\epsilon_{\mathrm{op}}/(2L_B))>0$.
  If $\delta\le\epsilon_{\mathrm{op}}/(2L_B)$, then
  $M_\delta\le\eta$ implies
  $E_{\mathrm{op},\delta}\le\epsilon_{\mathrm{op}}$.
  Thus, for the measurable event on the original common space
  \[
    E_\delta=\{E_{\mathrm{op},\delta}\le\epsilon_{\mathrm{op}}\}
    \cap\{|Z|\le\delta^{-1/4}\},\qquad
    p_\delta=\mathbb P(E_\delta),
  \]
  Chebyshev for the same single $Z=W(\Psi)$, with $\E Z^2=v$, gives
  \[
    p_\delta\ge1-A_p\eta^{-p}\delta^{\gamma_p}
    -v\delta^{1/2}\longrightarrow1.
  \]
  This is one union bound, with no independence between blocks or
  from $Z$ and no product of block probabilities.

  Let $C_\lambda$ be a Lipschitz bound for $s\mapsto\lambda_s$.
  Take $\delta$ small enough, in addition to
  $0<\delta<\min(1,1/B)$, that
  \[
    \begin{gathered}
      \delta B\le\omega,\qquad
      \delta\le\epsilon_{\mathrm{op}}/(2L_B),\qquad
      C_\lambda\delta B\le e_{\mathrm{rate}}/3,\\
      \delta|\log c_*|\le e_{\mathrm{rate}}/3,\qquad
      A_p\eta^{-p}\delta^{\gamma_p}+v\delta^{1/2}\le1/2.
    \end{gathered}
  \]
  Every constant has been fixed before this choice. The condition
  involving $C_\lambda$ is vacuous if that constant is zero.
  All source limits in Proposition~\ref{P:raw-block-point-comparison}
  have already been completed at each such fixed $\delta$.

  The indices $s_m=m\delta B$ lie in $I$ with adjacent gaps at most
  $\omega$. On $E_\delta$ the shifted full-$F$ blocks therefore
  satisfy Lemma~\ref{L:raw-block-indexed-cone}, retaining both phase
  entries and the actual final remainder $\tau$. In particular,
  $Y_{\delta,B}>0$, and
  \[
    \delta\log Y_{\delta,B}
    \ge\delta\log c_*+\delta(N-1)\log(1-\varrho)
    +\delta B\sum_{m<N}\lambda_{s_m}
    +\delta\tau\lambda_{s_N}.
  \]
  Since $s_N+\delta\tau=1$, the last two terms are the left Riemann
  sum for $I_R$ on the entire interval, including its last interval
  of length $\delta\tau$, with mesh at most $\delta B$.
  Its error is at most $C_\lambda\delta B$.
  Also $0\le\delta(N-1)\le1/B\le1$, so the logarithmic loss is
  at least $\log(1-\varrho)>-e_{\mathrm{rate}}/3$.
  The two other losses are each at most $e_{\mathrm{rate}}/3$ by
  the choices above. Hence,
  \[
    Y_{\delta,B}\ge
    \exp((I_R-e_{\mathrm{rate}})/\delta)\quad\hbox{on }E_\delta,
  \]
  including the $N=1$ and $\tau=0$ cases of the cone estimate.

  The integrand in~\eqref{E:raw-block-square-identity} is
  nonnegative. On the same $E_\delta$ its linear Gaussian term
  satisfies $-Z/\sqrt\delta\ge-\delta^{-3/4}$.
  Restriction to this event and~\eqref{E:raw-block-original-comparison}
  therefore give the explicit original-point budget
  \[
    \E|u(T,0)|^2\ge\E U_{\delta,B}^2
    \ge p_\delta\exp\left(
    \frac{2I_R-2e_{\mathrm{rate}}-v/2}{\delta}
    -\delta^{-3/4}\right),\qquad \delta=T^{-\kappa}.
  \]
  Here $p_\delta\ge1/2$ for small $\delta$, so
  $-\delta\log2\le\delta\log p_\delta\le0$.
  Multiplying the logarithm of the preceding inequality by $\delta$
  yields
  \[
    \delta\log\E|u(T,0)|^2
    \ge2I_R-2e_{\mathrm{rate}}-v/2
    -\delta^{1/4}+\delta\log p_\delta.
  \]
  Thus the normalized linear penalty is
  $\delta\delta^{-3/4}=\delta^{1/4}\to0$, and
  $\delta\log p_\delta\to0$. The quadratic Gaussian cost is
  precisely half the original raw variance $v$.
  Since $\kappa>0$, $\delta=T^{-\kappa}$ is a bijection between
  all sufficiently large $T$ and all sufficiently small $\delta$.
  This gives the full continuous-time liminf
  $Q_2\ge2I_R-2e_{\mathrm{rate}}-v/2$.
  For each $e_{\mathrm{rate}}$ the argument first fixed its own
  $B=B(e_{\mathrm{rate}})$ and then took $\delta\downarrow0$.
  The original point rate $Q_2$ is independent of $B$; only now let
  $e_{\mathrm{rate}}\downarrow0$. No choice $B=B(\delta)$ is made.

  Finally, spatial translation of all positive-width vertices
  preserves the original noise law, Green kernels and constant
  initial data. The fixed-order $L^2$ and absolute-series limits
  preserve equality of point second moments. Hence zero can be
  replaced by every fixed $x$ in~\eqref{E:raw-block-original-lower}.
  Every control and mask were fixed before asymptotics; a supremum
  over them may follow their individual inequalities.
  This proves Proposition~\ref{P:raw-block-original-lower}.
\end{proof}

===== END TEX FILE: notes/integrated_raw_block_lower.tex =====

===== BEGIN TEX FILE: notes/integrated_unmasked_variational.tex =====
\section{The unmasked Rayleigh rate and positive-control scores}
\label{S:unmasked-variational}

Fix a nonzero covariance satisfying Hypothesis~\ref{H:homog}, including
its original amplitude, and set $a=\alpha_0$. Define the full class
\begin{equation}\label{E:variational-positive-class}
  \mathcal C_{\mathrm{pos}}
  =\{\Psi\in C_c^\infty((0,1)\times\R^d;\R):
  \Psi\ge0,\ \Psi\ne0\}.
\end{equation}
It includes nonseparable tests. It is nonempty: if
$b(z)=e^{-1/(1-z^2)}$ on $|z|<1$ and zero otherwise, then
$b(4s-2)\prod_{j=1}^db(x_j)$ belongs to this class.
All boundary derivatives vanish because exponential decay dominates
every power of $(1-z^2)^{-1}$.
For each $\Psi$ retain the original mean $h_{\Psi,s}$ and raw variance
$v_\Psi=\E W(\Psi)^2$ from~\eqref{E:compact-raw-mean}--%
\eqref{E:compact-raw-cost}. Neither the test nor its covariance is
changed by a physical mask. We write $h_s$ when $\Psi$ is fixed.

\subsection{Global bounds and the unmasked spectral bottom}

\begin{lemma}[Gaussian envelope for the original covariance]
  \label{L:variational-heat-envelope}
  For the normalized heat kernel
  $p_\epsilon(x)=(2\pi\epsilon)^{-d/2}e^{-|x|^2/(2\epsilon)}$,
  \begin{equation}\label{E:variational-heat-envelope}
    (\Gamma*p_\epsilon)(x)
    =\int e^{i\xi\cdot x}e^{-\epsilon|\xi|^2/2}\mu(\ud\xi),
    \qquad
    0\le(\Gamma*p_\epsilon)(x)
    \le(\Gamma*p_\epsilon)(0)<\infty.
  \end{equation}
  The value at zero is strictly positive.
\end{lemma}

\begin{proof}
  A positive tempered Radon measure has polynomial ball growth.
  Indeed, evaluate its tempered bound on a nonnegative smooth cutoff
  equal to one on $B_1$, dilated by $R\ge1$. Its finitely many
  Schwartz seminorms are bounded by $CR^N$, so positivity gives
  a ball-mass bound $CR^N$. Summing dyadic annuli shows that
  $(1+|x|)^{-L}$ is integrable for $L>N$.
  Apply this separately to $\Gamma$ and $\mu$.
  Gaussian weights are therefore integrable against both measures.
  The classical convolution on the left is finite and smooth locally
  in $x$: on compact $x$ sets its translated Gaussian derivatives
  are bounded by any fixed sufficiently fast polynomial weight in
  the integration variable.

  Pair the convolution with a Schwartz test $\varphi$.
  Absolute Fubini is justified by these weights. The resulting
  pairing is that of $\Gamma$ with $p_\epsilon*\varphi$.
  Applying the spectral convention in Hypothesis~\ref{H:homog}
  and the identity
  $\int p_\epsilon(y)e^{-i\xi\cdot y}\ud y
  =e^{-\epsilon|\xi|^2/2}$
  gives exactly the right side of~\eqref{E:variational-heat-envelope}
  as a distribution. The heat kernel is even, so either Fourier
  sign gives that same Gaussian multiplier.
  Its spectral integral is absolutely finite and continuous in $x$
  by dominated convergence. Thus equality of the two continuous
  distributions gives equality at every $x$, without an extra
  normalization factor.
  The physical convolution is nonnegative. Evenness of $\mu$ makes
  the spectral integral real, and its absolute value is bounded by
  its total Gaussian mass, the value at zero.
  Finally $\Gamma\ne0$ and $p_\epsilon>0$ give strict positivity there.
  This proves Lemma~\ref{L:variational-heat-envelope}.
\end{proof}

\begin{lemma}[Global regularity of the original mean]
  \label{L:variational-global-mean}
  Every mixed time and space derivative of $h_s$ is globally bounded
  in space, uniformly on compact time intervals. In particular, for
  $I=[0,1]$ there are finite constants $M,C_\Psi$ such that
  \begin{equation}\label{E:variational-global-mean}
    0\le h_s(x)\le M,\qquad
    \|h_s-h_t\|_\infty\le C_\Psi|s-t|,
    \qquad s,t\in I.
  \end{equation}
\end{lemma}

\begin{proof}
  Extend $\Psi$ by zero in time; its compact support inside $(0,1)$
  makes this a smooth extension. For any mixed derivative $D\Psi$,
  a fixed $\epsilon>0$ and compactness of its common spatial support
  give $|D\Psi(t,x)|\le C_Dp_\epsilon(x)$ for all $t,x$.
  Here the heat kernel has a positive minimum on that support.
  Lemma~\ref{L:variational-heat-envelope} consequently bounds
  $\Gamma*|D\Psi(t,\cdot)|$ uniformly in $t,x$.
  Ordinary local differentiation against the Radon measure gives
  the corresponding derivatives of the convolution.
  After the change $r=s-t$,
  \[
    h_s(x)=\int_\R |r|^{-a}
    (\Gamma*\Psi(s-r,\cdot))(x)\ud r.
  \]
  For $s$ in a compact interval the relevant $r$ lie in a fixed
  bounded interval. The preceding global bound times $|r|^{-a}$
  is integrable since $a<1$.
  Every derivative thus falls on the smooth test and passes through
  the integral by dominated convergence, with the claimed global
  spatial bounds. Nonnegativity follows from positive kernels.
  The bounded time derivative proves the Lipschitz estimate.
  No directional decay of the mean has been inferred.
  This proves Lemma~\ref{L:variational-global-mean}.
\end{proof}

\begin{proposition}[The actual unmasked Rayleigh rate]
  \label{P:variational-unmasked-rate}
  On complex $L^2(\R^d)$, the operator $H_s=-\Delta-h_s$ is
  self-adjoint on $H^2$, with actual form domain $H^1$ and form
  $q_s(f)=\|\nabla f\|_2^2-\int h_s|f|^2$.
  Its spectral bottom $E_s$ is uniformly negative on $I$.
  The positive rate $\lambda_{\Psi,s}=\sqrt{-E_s}$ satisfies
  \begin{equation}\label{E:variational-real-rayleigh}
    \lambda_{\Psi,s}^2
    =\sup_{\substack{f\in H^1(\R^d;\R)\\\|f\|_2=1}}
    \left(\int h_sf^2-\|\nabla f\|_2^2\right).
  \end{equation}
  It is Lipschitz on $I$, and
  $I_\Psi:=\int_0^1\lambda_{\Psi,s}\ud s$ is positive and finite.
  No eigenstate at the unmasked bottom is asserted.
\end{proposition}

\begin{proof}
  The Fourier Laplacian $A=-\Delta$ is self-adjoint on $H^2$,
  being multiplication by $|\xi|^2$ with its maximal domain.
  Multiplication $B_s=-h_s$ is bounded self-adjoint with norm at
  most $M$. Thus $H_s=A+B_s$ is densely defined, symmetric and
  closed on $H^2$; the two graph norms are equivalent under a
  bounded perturbation.
  For real $b>M$,
  \[
    H_s-ib=(I+B_s(A-ib)^{-1})(A-ib).
  \]
  The first factor has a Neumann inverse because
  $\|B_s(A-ib)^{-1}\|\le M/b<1$, and the same holds with $+ib$.
  To check self-adjointness directly, for $u\in D(H_s^*)$ solve
  $(H_s-ib)v=(H_s^*-ib)u$ with $v\in D(H_s)$.
  Then $u-v\in\ker(H_s^*-ib)=\operatorname{Ran}(H_s+ib)^\perp
  =\{0\}$. Hence $D(H_s^*)=D(H_s)$.

  Set $c_{\mathrm{shift}}=1+M$ and $J_s=H_s+c_{\mathrm{shift}}\ge1$.
  Integration by parts on $H^2$ gives
  \[
    \|J_s^{1/2}f\|_2^2=q_s(f)+c_{\mathrm{shift}}\|f\|_2^2,\qquad
    \|f\|_{H^1}^2\le\|J_s^{1/2}f\|_2^2
    \le c_{\mathrm{shift}}\|f\|_{H^1}^2.
  \]
  Spectral cutoffs $1_{[1,n]}(J_s)$ show that $H^2=D(J_s)$
  is a core for the half-power norm; Fourier cutoffs give its
  density in $H^1$. Completion in the equivalent norms identifies
  $D(J_s^{1/2})$ and $H^1$ as actual $L^2$ subspaces, since both
  norms dominate $L^2$. This proves the stated form domain.

  The spectral lower bound gives one direction of the Rayleigh
  identity. For the reverse, nonzero spectral projections in
  $[E_s,E_s+\epsilon]$ give unit $H^2$ vectors with Rayleigh
  values at most $E_s+\epsilon$. The bottom is finite because
  the operator is bounded below and has finite Rayleigh tests.
  Let $\epsilon\downarrow0$. Real tests give the same infimum:
  $q_s(u+iv)=q_s(u)+q_s(v)$, so the quotient is the norm-weighted
  average of the nonzero real quotients.
  This proves the Rayleigh identity with $-E_s$ on the left.
  The following negative floor justifies writing that value as
  $\lambda_{\Psi,s}^2$ in~\eqref{E:variational-real-rayleigh}.

  Proposition~\ref{P:compact-original-common-trial} supplies, for
  this original $\Psi$, one unit compactly supported $w$ and a
  finite plateau mask with a common negative margin $\epsilon_0>0$.
  Its trial has support in $B_{2L}$; choose its plateau radius
  $R_0\ge2L$. The unmasked form on this same $w$ is no larger.
  Consequently $-M\le E_s\le-\epsilon_0<0$, and
  $\sqrt{\epsilon_0}\le\lambda_{\Psi,s}\le\sqrt M$.
  Comparing identical unit form tests gives
  $|E_s-E_t|\le\|h_s-h_t\|_\infty$ and therefore
  \[
    |\lambda_{\Psi,s}-\lambda_{\Psi,t}|
    \le \frac{C_\Psi}{2\sqrt{\epsilon_0}}|s-t|.
  \]
  This also proves positivity and finiteness of $I_\Psi$.
  No compact-potential spectral theorem was applied to $H_s$.
  This proves Proposition~\ref{P:variational-unmasked-rate}.
\end{proof}

\subsection{Removing masks from the numerical lower rate}

\begin{proposition}[Monotone rates and the original point moment]
  \label{P:variational-remove-mask}
  There is an increasing family of admissible radial masks $m_R$
  tending to one, for which the compact ground rates satisfy
  $\lambda_{R,s}\uparrow\lambda_{\Psi,s}$ uniformly on $I$ as $R\to\infty$,
  with the compact ground statements used for $R\ge R_0(\Psi)$.
  For the original canonical solution and any fixed $x$,
  \begin{equation}\label{E:variational-unmasked-point-lower}
    \liminf_{T\to\infty}T^{-\kappa}\log\E|u(T,x)|^2
    \ge2I_\Psi-\frac{v_\Psi}{2}.
  \end{equation}
\end{proposition}

\begin{proof}
  Put $F(t)=e^{-1/t}$ for $t>0$ and zero otherwise, and define
  \[
    \chi(r)=\frac{F(2-r)}{F(2-r)+F(r-1)},\qquad
    m_R(x)=\chi(|x|/R).
  \]
  The denominator is positive. The numerator decreases and the
  second denominator term increases; thus $\chi$ is nonincreasing,
  equals one on $r\le1$, and zero on $r\ge2$.
  Flatness of $F$ at zero gives smoothness. Since $\chi$ is
  constant near zero, $m_R$ is smooth also at the spatial origin.
  These even $[0,1]$ masks increase pointwise to one.

  Choose $R_0$ so the preceding common trial lies in the plateau.
  Every $R\ge R_0$ has the same negative margin.
  For each fixed $R$, the compact-family theorem applies to $m_Rh_s$.
  Its real Rayleigh formula follows from the same real/complex
  quotient argument as~\eqref{E:variational-real-rayleigh}.
  The rates are continuous, positive, at most $\sqrt M$ and
  monotone in $R$. For every fixed real unit $f\in H^1$,
  dominated convergence gives $\int m_Rh_sf^2\to\int h_sf^2$.
  Hence
  \[
    \sup_{R\ge R_0}\lambda_{R,s}^2
    =\sup_{\|f\|_2=1,\ f\in H^1(\R^d;\R)}
    \sup_{R\ge R_0}
    \left(\int m_Rh_sf^2-\|\nabla f\|_2^2\right)
    =\lambda_{\Psi,s}^2.
  \]
  Only two numerical suprema were interchanged.
  Positive square roots give the pointwise rate convergence.
  For $R_n=R_0+n$ and $\epsilon>0$, the increasing open sets
  $\{s:\lambda_{\Psi,s}-\lambda_{R_n,s}<\epsilon\}$ cover compact
  $I$. A finite subcover lies in the largest one, proving uniform
  convergence. Monotonicity extends it to all real $R\to\infty$.
  Therefore $\int_I\lambda_{R,s}\ud s\uparrow I_\Psi$.

  At each fixed $R$ use this very same mask in the driver and mean
  when applying Proposition~\ref{P:raw-block-original-lower}.
  It gives the lower bound with $2\int_I\lambda_{R,s}\ud s-v_\Psi/2$
  for the same original point liminf. Taking the numerical supremum
  over these individual bounds proves
  \eqref{E:variational-unmasked-point-lower}.
  There is no $R(T)$, unmasked noisy wave, uniform-in-mask Gaussian
  estimate or exchange of source and time limits.
  This proves Proposition~\ref{P:variational-remove-mask}.
\end{proof}

\subsection{Full-class dilation and finite positive scores}

\begin{lemma}[Radon and Rayleigh dilation]\label{L:variational-control-dilation}
  For $r>0$ the map
  \begin{equation}\label{E:variational-control-dilation}
    (D_r\Psi)(s,x)=r^{d+2-\alpha}\Psi(s,rx)
  \end{equation}
  is a bijection of $\mathcal C_{\mathrm{pos}}$, with inverse $D_{1/r}$.
  With the same original covariance,
  \begin{equation}\label{E:variational-dilation-values}
    h_{D_r\Psi,s}(x)=r^2h_{\Psi,s}(rx),\qquad
    v_{D_r\Psi}=r^{4-\alpha}v_\Psi,\qquad
    \lambda_{D_r\Psi,s}=r\lambda_{\Psi,s},\quad
    I_{D_r\Psi}=rI_\Psi.
  \end{equation}
\end{lemma}

\begin{proof}
  Positive dilation preserves the full smooth positive nonzero class;
  multiplication of its amplitude powers gives the stated inverse.
  Homogeneity of the physical Radon measure gives, for every
  nonnegative measurable $G$,
  \[
    \int G(ry)\Gamma(\ud y)
    =r^{\alpha-d}\int G(z)\Gamma(\ud z).
  \]
  Indeed, its left pushforward measure on a Borel set $A$ is
  $\Gamma(A/r)=r^{\alpha-d}\Gamma(A)$.
  Positive Tonelli applies this identity inside the temporal
  convolution, giving $h_{D_r\Psi,s}(x)=r^2h_{\Psi,s}(rx)$.
  Now use the \emph{Lebesgue} substitution $z=rx$ in the raw pairing:
  \[
    v_{D_r\Psi}=r^{d+2-\alpha}r^2r^{-d}v_\Psi
    =r^{4-\alpha}v_\Psi.
  \]
  This distinguishes the Radon pushforward from the spatial volume
  factor; it includes singular covariances and white noise.

  The map $U_rf(x)=r^{d/2}f(rx)$ is a unitary bijection on real
  $L^2$, preserving $H^1,H^2$ as sets under its inverse.
  Weak derivatives give
  $\|\nabla U_rf\|_2^2=r^2\|\nabla f\|_2^2$ and
  $\int h_{D_r\Psi,s}(U_rf)^2=r^2\int h_{\Psi,s}f^2$.
  The real Rayleigh bijection proves the squared rate identity;
  the rates are positive, so their square roots and integrals give
  \eqref{E:variational-dilation-values}.
  On $H^2$ this is also
  $H_{D_r\Psi,s}U_r=r^2U_rH_{\Psi,s}$.
  Time has not been rescaled. For compact masks the corresponding
  identity uses
  $m_R(rx)=m_{R/r}(x)$; a fixed mask radius is not invariant.
  This proves Lemma~\ref{L:variational-control-dilation}.
\end{proof}

\begin{proposition}[Positive finite intrinsic lower scores]
  \label{P:variational-positive-scores}
  For $c>0$, the score set
  $\{cI_\Psi-v_\Psi/2:\Psi\in\mathcal C_{\mathrm{pos}}\}$
  is nonempty and bounded above. Its finite real supremum
  $S_c^{\mathrm{pos}}$ is positive and satisfies
  \begin{equation}\label{E:variational-score-homogeneity}
    S_c^{\mathrm{pos}}=c^{(4-\alpha)/(3-\alpha)}S_1^{\mathrm{pos}},
    \qquad
    Q_2\ge S_2^{\mathrm{pos}},
  \end{equation}
  where $Q_2$ is the original point liminf.
  The label-one value is an auxiliary variational score; no actual
  first-moment or source-constant identification is asserted.
\end{proposition}

\begin{proof}
  Write $k=3-\alpha>0$, $q=4-\alpha=k+1$ and $m=q/k>1$.
  Fix one $\Psi_0$ from the nonempty class and put
  $I_0=I_{\Psi_0}>0$, $v_0=v_{\Psi_0}>0$.
  Positivity of the latter is Lemma~\ref{L:compact-raw-profile}.
  For $r_0=(I_0/v_0)^{1/k}>0$, which need not be less than one,
  the exact real-power identity gives
  \[
    I_{D_{r_0}\Psi_0}-v_{D_{r_0}\Psi_0}/2
    =r_0I_0-r_0^qv_0/2=r_0I_0/2>0.
  \]
  This positive score belongs to an actual smooth test.

  For $c>0$ put $r_c=c^{1/k}$ and $K_c=c^m>0$.
  Lemma~\ref{L:variational-control-dilation} and the exact scalar
  powers give, for every $\Psi$,
  \begin{equation}\label{E:variational-score-set-scaling}
    cI_{D_{r_c}\Psi}-v_{D_{r_c}\Psi}/2
    =K_c(I_\Psi-v_\Psi/2).
  \end{equation}
  Since $D_{r_c}$ is a bijection of the entire class, the whole
  $c$-score set is $K_c$ times the whole label-one score set.

  We prove boundedness before taking finite-real suprema.
  The independent existing Theorem~\ref{T:full-upper}, for the
  \emph{same canonical solution}, gives
  \[
    \E|u(T,0)|^2\le e(T+2)^d e^{C_{\mathrm{up}}T^\kappa},
    \qquad T\ge1,\quad C_{\mathrm{up}}<\infty.
  \]
  Its prefactor is negligible: choose $\epsilon=\kappa/2>0$,
  use $\log T\le(T^\epsilon-1)/\epsilon$ and
  $\log(T+2)\le\log T+\log3$ for $T\ge1$, and divide by $T^\kappa$.
  Thus the original point limsup is at most $C_{\mathrm{up}}$.
  One fixed test/mask lower bound gives a finite lower bound for
  $Q_2$, so $Q_2$ is finite. By
  \eqref{E:variational-unmasked-point-lower} every label-two score
  is at most this same $Q_2\le C_{\mathrm{up}}$, uniformly in $\Psi$.
  Equation~\eqref{E:variational-score-set-scaling} at $c=2$
  consequently bounds all label-one scores by $C_{\mathrm{up}}/K_2$.
  The nonempty set has a finite real supremum
  $S_1^{\mathrm{pos}}>0$ by the positive test above.

  For general $c$, set equality and $K_c>0$ show that
  $K_cS_1^{\mathrm{pos}}$ is the supremum: it is an upper bound,
  and every smaller number is exceeded by $K_c$ times a label-one
  score within the corresponding positive distance of its supremum.
  This proves finiteness, positivity and the first identity in
  \eqref{E:variational-score-homogeneity}. Taking the numerical
  supremum of the label-two lower bounds proves the second.
  Although $2^m>2$, the resulting $S_2^{\mathrm{pos}}>2S_1^{\mathrm{pos}}$
  is only an auxiliary-score comparison. It is not a Jensen
  improvement without an actual first-moment identification.
  This proves Proposition~\ref{P:variational-positive-scores}.
\end{proof}

For $\Gamma=0$, the mean, raw variance and Rayleigh rate are zero.
Set all these scores to zero; the free canonical solution $u=1$
has the corresponding zero moment rate. Strict positivity above is
restricted to nonzero covariance. Matching an upper variational rate
and identifying an exact original-point limit remain later steps.

===== END TEX FILE: notes/integrated_unmasked_variational.tex =====

===== BEGIN TEX FILE: notes/integrated_temporal_equilibrium.tex =====
\section{The temporal equilibrium density}
\label{S:temporal-equilibrium}

We use Euler's function
$\Gamma_E(x)=\int_0^\infty u^{x-1}e^{-u}\ud u$, $x>0$,
and $\operatorname{Beta}(x,y)=\int_0^1t^{x-1}(1-t)^{y-1}\ud t$,
$x,y>0$. Both integrals are positive and finite.

\begin{lemma}[Gamma and Beta identities]\label{L:equilibrium-gamma-beta}
  For positive arguments,
  \begin{align*}
    \Gamma_E(x+1)&=x\Gamma_E(x),\\
    \operatorname{Beta}(x,y)
    &=\frac{\Gamma_E(x)\Gamma_E(y)}{\Gamma_E(x+y)},\\
    \Gamma_E(2x)
    &=\frac{2^{2x-1}\Gamma_E(x)\Gamma_E(x+1/2)}{\sqrt\pi}.
  \end{align*}
\end{lemma}

\begin{proof}
  Integration by parts gives the recurrence, with vanishing boundary
  terms. In the positive product Gamma integral, use
  $(u,v)=(Rt,R(1-t))$, with Jacobian $R$; Tonelli gives the
  Beta--Gamma identity. For the last identity, symmetry, then
  $t=(1+v)/2$ and $v^2=w$, give
  $\operatorname{Beta}(x,x)=2^{1-2x}\operatorname{Beta}(1/2,x)$.
  Also $\Gamma_E(1/2)=\int_\R e^{-z^2}\ud z=\sqrt\pi$:
  the substitution $u=z^2$ gives the first equality, and squaring
  the positive Gaussian integral and using polar coordinates gives
  $2\pi\int_0^\infty re^{-r^2}\ud r=\pi$.
  Substituting these into the Beta--Gamma identity proves duplication.
  This proves Lemma~\ref{L:equilibrium-gamma-beta}.
\end{proof}

\begin{lemma}[Exact potential and mass]\label{L:temporal-equilibrium}
  For $0<a<1$ put $r=(1-a)/2$ and, for $0<t<1$,
  \begin{equation}\label{E:temporal-equilibrium-density}
    f_a(t)=\frac{[t(1-t)]^{-r}}{\Gamma_E(r)\Gamma_E(1-r)}.
  \end{equation}
  This positive function belongs to $L^1(0,1)\cap L^2(0,1)$, and
  \begin{align}
    \int_0^1|s-t|^{-a}f_a(t)\ud t&=1
    &&\text{for every }s\in[0,1],\label{E:temporal-equilibrium-potential}\\
    M_a:=\int_0^1f_a(t)\ud t
    &=\frac{\Gamma_E((1+a)/2)}
    {\Gamma_E(1+a)\Gamma_E((1-a)/2)}>0.
    \label{E:temporal-equilibrium-mass}
  \end{align}
\end{lemma}

\begin{proof}
  The positive binomial series
  $(1-z)^{-p}=\sum_{n\ge0}(p)_nz^n/n!$, $p>0$, $0\le z<1$,
  follows directly as follows. Its coefficient ratio gives uniform
  convergence on compact subintervals, including for its derivative.
  Termwise differentiation gives $(1-z)y'=py$, $y(0)=1$;
  hence $(1-z)^py$ is constant one. Here
  $(p)_0=1$, $(p)_n=p(p+1)\cdots(p+n-1)$.
  All terms used below are nonnegative, so Tonelli applies.

  For $0<s<1$ split the integral of
  $|s-t|^{2r-1}[t(1-t)]^{-r}$ into left and right parts.
  In the left part, $t=su$ gives
  \begin{align*}
    L(s)
    &=s^r\int_0^1(1-u)^{2r-1}u^{-r}(1-su)^{-r}\ud u\\
    &=\operatorname{Beta}(1-r,2r)s^r
    \sum_{n\ge0}
    \frac{(r)_n(1-r)_ns^n}{(1+r)_n n!}.
  \end{align*}
  The Beta ratio follows from the Gamma recurrence.
  Since $(r)_n/(1+r)_n=r/(r+n)$, expanding the incomplete Beta
  integral gives
  \[
    L(s)=r\operatorname{Beta}(1-r,2r)B_s(r,r),\qquad
    B_s(r,r)=\int_0^s u^{r-1}(1-u)^{r-1}\ud u.
  \]
  Reflection makes the right part $L(1-s)$, while symmetry gives
  $B_s(r,r)+B_{1-s}(r,r)=\operatorname{Beta}(r,r)$.
  The full integral is therefore
  $r\operatorname{Beta}(1-r,2r)\operatorname{Beta}(r,r)
  =\Gamma_E(r)\Gamma_E(1-r)$.
  All integrals are finite because $-r>-1$ and $2r-1>-1$.
  At $s=0$ the integral is directly
  $\operatorname{Beta}(r,1-r)=\Gamma_E(r)\Gamma_E(1-r)$;
  $s=1$ follows by reflection. This proves
  \eqref{E:temporal-equilibrium-potential}, including the endpoints
  without a limiting argument there.

  Integrability and square integrability follow from
  $-r>-1$ and $-2r=a-1>-1$. Finally,
  \[
    M_a=
    \frac{\operatorname{Beta}(1-r,1-r)}
    {\Gamma_E(r)\Gamma_E(1-r)}
    =\frac{\Gamma_E(1-r)}{\Gamma_E(2-2r)\Gamma_E(r)},
  \]
  which is~\eqref{E:temporal-equilibrium-mass}.
  Its time mass has not been renormalized.
  This proves Lemma~\ref{L:temporal-equilibrium}.
\end{proof}

===== END TEX FILE: notes/integrated_temporal_equilibrium.tex =====

===== BEGIN TEX FILE: notes/integrated_spatial_occupation.tex =====
\section{Physical spatial pairings and the full occupation class}
\label{S:spatial-occupation-foundation}

Retain a nonzero original covariance from Hypothesis~\ref{H:homog}
with its actual amplitude. Set $a=\alpha_0$,
$k=3-\alpha>1$, $q=4-\alpha=k+1$ and $D=q-2a>0$.
The scalar $D$ is fixed. All profiles are real.
The original positive temporal exponent and threshold imply $\alpha<2$;
this is the strict inequality used in the scalar powers and concavity.
The finite positive score $S_1^{\mathrm{pos}}$ is that of
Proposition~\ref{P:variational-positive-scores}.

\begin{lemma}[The physical two-point integral]\label{L:spatial-physical-pair}
  The positive measure $\nu(\ud x,\ud y)=\ud x\,\Gamma(\ud y)$ is
  sigma-finite. For nonnegative functions define
  \begin{equation}\label{E:spatial-physical-pair}
    B_\Gamma(f,h)=\int f(x)h(x-y)\nu(\ud x,\ud y)
  \end{equation}
  initially as an extended nonnegative integral, using finite Borel
  representatives of Lebesgue classes. Its value is representative
  independent. Lebesgue-a.e. convergence transfers to $\nu$-a.e.
  convergence at both positions $x$ and $x-y$.
\end{lemma}

\begin{proof}
  Local finiteness of $\Gamma$ gives sigma-finiteness on exhausting
  balls, and Lebesgue measure is sigma-finite.
  If $N$ is Borel and Lebesgue null, Tonelli applied first in $x$
  gives $\nu\{x\in N\}=0$ and $\nu\{x-y\in N\}=0$, because
  every fixed translate of $N$ is null.
  An arbitrary Lebesgue null set has a Borel null superset.
  Thus arbitrary versions are measurable in the $\nu$ completion
  with the same value, and the same observation applies to the
  exceptional sets of a.e. convergence.
  Signed pairings will be used only after absolute convergence.
  This proves Lemma~\ref{L:spatial-physical-pair}.
\end{proof}

Put $A_{\mathrm{sp}}(g)=B_\Gamma(g^2,g^2)$ and
$b(g)=\|\nabla g\|_2^2$ on $H^1$; initially $A_{\mathrm{sp}}$ is used
only for smooth compact profiles before the extension below.
For smooth compact $z$, write $U_z=\Gamma*z$ in its usual
pointwise sense.

\begin{lemma}[Actual smooth temporal controls]\label{L:spatial-static-controls}
  For every nonnegative nonzero $z\in C_c^\infty(\R^d)$, let
  \[
    \lambda_z(c)^2=
    \sup_{\substack{g\in H^1(\R^d;\R)\\\|g\|_2=1}}
    \left(c\int U_zg^2-b(g)\right),\qquad c>0.
  \]
  This is positive and finite, and $\lambda_z$ is Lipschitz on
  every compact positive $c$ interval. With the exact $M_a$ in
  \eqref{E:temporal-equilibrium-mass},
  \begin{equation}\label{E:spatial-static-score}
    S_1^{\mathrm{pos}}\ge
    \lambda_z(1)-\frac{M_a}{2}B_\Gamma(z,z).
  \end{equation}
\end{lemma}

\begin{proof}
  Choose nonnegative nonzero $f\in C_c^\infty(0,1)$ and $s_0=1/2$.
  Let $k_f(s_0)=\int_0^1|s_0-t|^{-a}f(t)\ud t>0$.
  The actual smooth test $\Psi(t,x)=cf(t)z(x)/k_f(s_0)$
  has mean $cU_z$ at $s_0$.
  Proposition~\ref{P:variational-unmasked-rate} gives boundedness
  of this potential, the displayed real Rayleigh formula, and a
  positive rate for every $c>0$.
  Comparing identical unit tests makes $\lambda_z(c)^2$ Lipschitz
  with constant $\|U_z\|_\infty$.
  On a positive compact interval its rate has a positive floor
  by monotonicity, giving the square-root Lipschitz bound.

  Use the nonincreasing smooth cutoff $\chi$ constructed in the
  proof of Proposition~\ref{P:variational-remove-mask}.
  For integers $n\ge4$, set on $(0,1)$
  \[
    f_n(t)=f_a(t)\chi(1/(nt))\chi(1/(n(1-t))),\qquad
    k_n(s)=\int_0^1|s-t|^{-a}f_n(t)\ud t.
  \]
  Extend $f_n$ by zero. It is smooth compact, vanishes near both
  endpoints, is nonzero, and increases to $f_a$.
  Thus $\Psi_n=f_n\otimes z$ is an actual positive smooth control.
  Monotone convergence and~\eqref{E:temporal-equilibrium-potential}
  give $k_n(s)\uparrow1$ for every $s\in[0,1]$.
  Since the kernel is at least one on the unit square off its
  null diagonal,
  $0<c_0:=\int_0^1f_4\le k_n(s)\le1$.
  The actual mean is $k_n(s)U_z$; hence its actual rate is
  $\lambda_z(k_n(s))$, converging to $\lambda_z(1)$ and bounded
  by that finite number. Dominated convergence gives
  $I_{\Psi_n}\to\lambda_z(1)$.

  The raw cost is exactly the nonnegative Tonelli pairing
  \[
    v_{\Psi_n}=B_\Gamma(z,z)\int_0^1f_n(s)k_n(s)\ud s.
  \]
  Its time integrand increases to $f_a$, so the cost tends to
  $M_aB_\Gamma(z,z)$.
  The spatial factor is finite and positive: its smooth compact
  autocorrelation is positive near zero, and homogeneity scales
  any origin-centered ball of positive $\Gamma$ mass to every
  other positive radius. Such a ball exists by exhaustion.
  Take the limit of the individual inequalities
  $S_1^{\mathrm{pos}}\ge I_{\Psi_n}-v_{\Psi_n}/2$.
  The score differences need not increase.
  No control depends on original large time and no rough
  stochastic evolution has been used.
  This proves Lemma~\ref{L:spatial-static-controls}.
\end{proof}

\begin{proposition}[The finite smooth spatial ratio]
  \label{P:spatial-smooth-ratio}
  For real unit $g\in C_c^\infty(\R^d)$ put
  $R(g)=A_{\mathrm{sp}}(g)/b(g)^{\alpha/2}$.
  Its supremum $R_0$ over these profiles is a positive finite
  real number, and
  \begin{equation}\label{E:spatial-smooth-score}
    S_1^{\mathrm{pos}}\ge
    k\left[
    \frac{R(g)\alpha^{\alpha/2}}{8M_aq^{q/2}}
    \right]^{1/k}.
  \end{equation}
\end{proposition}

\begin{proof}
  The gradient energy $b(g)$ is positive: a nonzero $L^2$ function
  with zero weak gradient would have Fourier transform supported
  only at zero, and hence would vanish.
  Its square is nonnegative nonzero smooth compact, so the
  autocorrelation argument in the preceding proof gives
  $0<A:=A_{\mathrm{sp}}(g)<\infty$.
  With $U_\ell g(x)=\ell^{d/2}g(\ell x)$, the physical changes
  of variables give
  \begin{equation}\label{E:spatial-dilation}
    A_{\mathrm{sp}}(U_\ell g)=\ell^\alpha A,\qquad
    b(U_\ell g)=\ell^2b(g).
  \end{equation}
  The factors in the first identity are $\ell^{2d}$ from
  the two squares, $\ell^{-d}$ from $\ud x$, and
  $\ell^{\alpha-d}$ from the Radon pushforward.

  For $\theta,\ell>0$ choose the actual smooth control
  $z=\theta(U_\ell g)^2$.
  The Rayleigh test $U_\ell g$ gives
  $\lambda_z(1)^2\ge\theta\ell^\alpha A-\ell^2b$,
  while $B_\Gamma(z,z)=\theta^2\ell^\alpha A$.
  For any $L>0$, put $u=\alpha/q>0$ and choose
  \[
    \ell^2=uL^2/b,\qquad
    \theta=(1+u)L^2/(\ell^\alpha A).
  \]
  The radicand is $L^2$. Lemma~\ref{L:spatial-static-controls}
  consequently gives
  \[
    S_1^{\mathrm{pos}}\ge L-CL^q,\qquad
    C=\frac{M_a(1+u)^2}{2R(g)u^{\alpha/2}}>0.
  \]
  Its maximum occurs at $L^k=1/(qC)$ and is
  $(k/q)(qC)^{-1/k}$.
  Since $1+u=4/q$,
  $1/(q^qC)=R(g)\alpha^{\alpha/2}/(8M_aq^{q/2})$,
  proving~\eqref{E:spatial-smooth-score}.
  The already finite $S_1^{\mathrm{pos}}$ bounds every ratio by
  $8M_aq^{q/2}(S_1^{\mathrm{pos}}/k)^k/\alpha^{\alpha/2}$.
  A normalized compact bump supplies a positive ratio.
  This proves positivity and finiteness of $R_0$ before any
  rough spatial extension is invoked.
  This proves Proposition~\ref{P:spatial-smooth-ratio}.
\end{proof}

\begin{proposition}[The physical four-linear extension]
  \label{P:spatial-four-linear}
  For real $f\in H^1(\R^d)$ define
  $N(f)=\|f\|_2^{1-\alpha/4}\|\nabla f\|_2^{\alpha/4}$.
  Every physical square pairing is finite and
  \begin{align}
    A_{\mathrm{sp}}(f)&\le R_0N(f)^4,\label{E:spatial-homogeneous-bound}\\
    0\le B_\Gamma(f^2,h^2)
    &\le\sqrt{A_{\mathrm{sp}}(f)A_{\mathrm{sp}}(h)}.
    \label{E:spatial-square-CS}
  \end{align}
  The actual signed integral
  $C_4(f_1,f_2,f_3,f_4)=B_\Gamma(f_1f_2,f_3f_4)$ is
  absolutely convergent and jointly continuous on $(H^1)^4$, with
  \begin{equation}\label{E:spatial-four-linear}
    \int|f_1(x)f_2(x)f_3(x-y)f_4(x-y)|\ud\nu
    \le R_0\prod_{j=1}^4N(f_j).
  \end{equation}
  The ratio supremum $R_{\mathrm{sp}}$ over all real unit $H^1$
  profiles equals $R_0$. Every nonzero $H^1$ profile has
  $A_{\mathrm{sp}}(f)>0$.
\end{proposition}

\begin{proof}
  For smooth compact $f$, normalization in $R_0$ proves
  \eqref{E:spatial-homogeneous-bound}, including $f=0$.
  All exponents in $N$ are positive and $N(f)\le\|f\|_{H^1}$.
  For smooth compact signed $Q,P$, the absolute correlation is compactly
  supported and bounded by $\|Q\|_2\|P\|_2$.
  Local finiteness of $\Gamma$ therefore makes its physical integral finite.
  Smooth signed covariance is positive: with the ordinary transform
  $\widehat Q_{\mathrm{ord}}(\xi)=\int e^{i\xi\cdot x}Q(x)\ud x$,
  the model convention gives
  \[
    B_\Gamma(Q,Q)=\int|\widehat Q_{\mathrm{ord}}(\xi)|^2\mu(\ud\xi)
    \ge0,\qquad Q\in C_c^\infty(\R^d;\R).
  \]
  Pair $\Gamma$ with the smooth compact correlation to obtain this
  identity; rapid Fourier decay and tempered $\mu$ give finiteness.
  Evenness of $\Gamma$ and $(x,y)\mapsto(x-y,-y)$ give symmetry.
  The quadratic polynomial for $Q+tP$ gives covariance
  Cauchy--Schwarz. In particular, for smooth real $f,h$,
  \[
    0\le B_\Gamma(f^2,h^2)
    \le R_0N(f)^2N(h)^2.
  \]
  The squares of signed smooth profiles are already smooth and
  nonnegative.

  Smooth compact functions are dense in $H^1$. Cutoffs equal to one
  on the radius-$R$ ball, vanishing beyond $2R$ and with gradient
  at most $C/R$, converge by the function and gradient tails and
  the bound $C\|f\|_2/R$ for the extra gradient term.
  Mollification then converges in $H^1$ by $L^2$ translation
  continuity of the function and its weak gradients.
  The space is separable through its closed isometric image
  $f\mapsto(f,\nabla f)$ in $L^2(\R^d)^{d+1}$.

  For arbitrary $f,h\in H^1$ take smooth approximants converging in
  $H^1$ and along a common subsequence Lebesgue-a.e.
  Lemma~\ref{L:spatial-physical-pair} transfers this convergence at
  both positions to $\nu$-a.e. convergence.
  Fatou and continuity of $N$ give
  $B_\Gamma(f^2,h^2)\le R_0N(f)^2N(h)^2<\infty$,
  including the diagonal bound.
  At this stage Fatou supplies an inequality, not continuity.

  Apply ordinary Cauchy--Schwarz under the positive measure $\nu$
  to $f_1(x)f_3(x-y)$ and $f_2(x)f_4(x-y)$.
  The two squared integrals are finite by the last bound; their
  square root is at most $R_0\prod_jN(f_j)$.
  This proves~\eqref{E:spatial-four-linear}, absolute convergence
  and actual multilinearity. Telescoping a difference one argument
  at a time and using $N(f)\le\|f\|_{H^1}$ proves joint continuity.
  Thus $A_{\mathrm{sp}}$ and the square pairings are continuous.
  PSD for smooth compact profiles passes to finite linear combinations of $H^1$ squares
  by this continuity, and its two-profile Cauchy--Schwarz gives
  \eqref{E:spatial-square-CS}.
  This completes the physical pairing argument beyond Fatou.

  Every real unit $H^1$ profile has positive gradient energy by
  the Fourier argument above. The homogeneous bound gives
  $R_{\mathrm{sp}}\le R_0$, and smooth inclusion gives the reverse.
  Normalized smooth approximations preserve the ratio by continuity.
  Finally, for nonzero $f$, choose a bounded set $E$ of finite
  positive measure where $|f|\ge c>0$.
  The correlation of $1_E$ is continuous and positive near zero
  by $L^2$ translation continuity. An origin-centered ball there
  has positive $\Gamma$ mass, so
  $A_{\mathrm{sp}}(f)\ge c^4B_\Gamma(1_E,1_E)>0$.
  This uses a nonnegative integral, not an $H^1$ claim for $1_E$.
  Finiteness was already proved.
  This proves Proposition~\ref{P:spatial-four-linear}.
\end{proof}

\begin{proposition}[The spatial energy and static lower score]
  \label{P:spatial-energy-map}
  Over all real unit $H^1$ profiles define the own energy
  \[
    \mathcal E_{\mathrm{sp}}
    =\sup_{\|g\|_2=1}
    \left(A_{\mathrm{sp}}(g)-\frac{b(g)}2\right).
  \]
  Then
  \begin{equation}\label{E:spatial-energy-map}
    \mathcal E_{\mathrm{sp}}
    =\frac{2-\alpha}{2}\alpha^{\alpha/(2-\alpha)}
    R_{\mathrm{sp}}^{2/(2-\alpha)}
    \in(0,\infty).
  \end{equation}
  In particular,
  \begin{equation}\label{E:spatial-static-energy-score}
    S_1^{\mathrm{pos}}\ge M_a^{-1/k}F_0(\mathcal E_{\mathrm{sp}}),
    \qquad
    F_0(z)=k\left[
    \frac{(2z/(2-\alpha))^{(2-\alpha)/2}}{8q^{q/2}}
    \right]^{1/k},\quad z>0.
  \end{equation}
  The subscript in $F_0$ labels this scalar map; the covariance
  retains its original temporal exponent $a$.
\end{proposition}

\begin{proof}
  Physical change of variables, or smooth approximation and
  Proposition~\ref{P:spatial-four-linear}, extends
  \eqref{E:spatial-dilation} to real $H^1$ profiles.
  For fixed unit $g$, with $A,b>0$, the maximum of
  $\ell^\alpha A-\ell^2b/2$ occurs at
  $\ell^{2-\alpha}=\alpha A/b$ and equals
  \[
    \frac{2-\alpha}{2}\alpha^{\alpha/(2-\alpha)}
    R(g)^{2/(2-\alpha)}.
  \]
  Dilation preserves the whole unit class and includes $\ell=1$.
  Taking both numerical suprema, then profiles with ratio tending
  to $R_{\mathrm{sp}}$, proves~\eqref{E:spatial-energy-map}.
  No optimizer is assumed.
  Smooth ratios also approach $R_{\mathrm{sp}}$ by
  Proposition~\ref{P:spatial-four-linear}.
  Pass them through~\eqref{E:spatial-smooth-score} and substitute
  \[
    R_{\mathrm{sp}}\alpha^{\alpha/2}
    =\left(\frac{2\mathcal E_{\mathrm{sp}}}{2-\alpha}
    \right)^{(2-\alpha)/2}.
  \]
  This gives~\eqref{E:spatial-static-energy-score}.
  This proves Proposition~\ref{P:spatial-energy-map}.
\end{proof}

\subsection{The kernel row and full occupation energy}

Define, for $u\ne0$,
\begin{equation}\label{E:occupation-damped-kernel}
  K_\star(u)=\frac1{\Gamma_E(a)}
  \int_0^\infty
  e^{-(\lambda+\lambda^2/(2D))|u|}
  \lambda^{a-1}\ud\lambda,
\end{equation}
and set $K_\star(0)=0$ for time integration.

\begin{lemma}[Exact row maximum]\label{L:occupation-kernel-row}
  The kernel is even, positive off zero, locally integrable,
  decreasing on $(0,\infty)$, and $K_\star(u)\le|u|^{-a}$ off zero.
  Its exact row maximum on $[0,1]$ is
  \begin{equation}\label{E:occupation-kernel-row}
    \max_{s\in[0,1]}\int_0^1K_\star(s-t)\ud t
    =R_\star:=2\int_0^{1/2}K_\star(u)\ud u\in(0,\infty).
  \end{equation}
\end{lemma}

\begin{proof}
  Dropping the positive quadratic damping bounds the mixture by
  the Gamma integral $|u|^{-a}$.
  Positivity and monotonicity follow directly from the integrand,
  and $a<1$ gives local integrability.
  Put $\Phi(t)=\int_0^tK_\star(u)\ud u$. It is concave because
  its integrand is decreasing on positive arguments.
  The row is $\Phi(s)+\Phi(1-s)\le2\Phi(1/2)$, with equality
  at $s=1/2$. The diagonal value changes no time integral.
  This proves Lemma~\ref{L:occupation-kernel-row}.
\end{proof}

Let $\mathcal O$ be the full class of strongly $H^1(\R^d;\R)$-measurable
fields $s\mapsto g_s$ on $(0,1)$ with
$\|g_s\|_2=1$ a.e. and
$T(g)=\int_0^1b(g_s)\ud s<\infty$.
No time smoothness, common compact support or optimizer condition
is imposed.

\begin{proposition}[The full physical occupation class]
  \label{P:occupation-physical-class}
  The pairings $(s,t)\mapsto B_\Gamma(g_s^2,g_t^2)$ are measurable,
  representative independent and equal to their physical integrals.
  With
  \[
    J(g)=\int_0^1\int_0^1
    K_\star(s-t)B_\Gamma(g_s^2,g_t^2)\ud s\ud t,
  \]
  every $g\in\mathcal O$ satisfies
  \begin{equation}\label{E:occupation-physical-bound}
    0\le J(g)\le R_\star R_{\mathrm{sp}}T(g)^{\alpha/2}<\infty.
  \end{equation}
  The own energy over exactly this full class satisfies
  \begin{equation}\label{E:occupation-own-energy}
    0<\mathcal E_\star^{\mathcal O}
    :=\sup_{g\in\mathcal O}\big(J(g)-T(g)/2\big)
    \le R_\star^{2/(2-\alpha)}\mathcal E_{\mathrm{sp}}<\infty.
  \end{equation}
\end{proposition}

\begin{proof}
  The map $s\mapsto b(g_s)$ is measurable by continuity of the
  squared gradient norm. Also
  $\int_0^1\|g_s\|_{H^1}^2\ud s=1+T(g)$.
  Use a separably valued strong representative and replace
  exceptional null times by one fixed real unit compact bump.
  Joint measurable spatial representatives exist: approximate this
  Bochner $L^2$ field by simple $H^1$-valued functions with
  summable $L^2(0,1;H^1)$ errors, and choose measurable spatial
  versions for their countably many values.
  A subsequence has a measurable spacetime $L^2$ limit, and for
  a.e. $s$ its spatial $L^2$ class is $g_s$.
  Lemma~\ref{L:spatial-physical-pair} makes every pairing
  independent of the spatial versions.
  The continuous pairing map on the separable space $H^1\times H^1$
  from Proposition~\ref{P:spatial-four-linear} consequently gives
  a measurable function of $(s,t)$ agreeing a.e. with the actual
  nonnegative physical integral.

  Set $F(s)=b(g_s)^{\alpha/4}$.
  Equations~\eqref{E:spatial-homogeneous-bound} and
  \eqref{E:spatial-square-CS} give
  $B_\Gamma(g_s^2,g_t^2)\le R_{\mathrm{sp}}F(s)F(t)$.
  Since $0<\alpha/2<1$, concavity on the unit time interval yields
  $\int_0^1F^2=\int_0^1b(g_s)^{\alpha/2}\ud s\le T(g)^{\alpha/2}$.
  Now use $2F(s)F(t)\le F(s)^2+F(t)^2$ and the exact row bound
  \eqref{E:occupation-kernel-row}, whose column bound is the same
  because $K_\star$ is even, to obtain
  \eqref{E:occupation-physical-bound}.
  Positive Tonelli is valid before finiteness is known.
  Null-time modifications affect only a product-null set, so
  they cannot change $J$.

  The scalar maximum of
  $R_\star R_{\mathrm{sp}}T^{\alpha/2}-T/2$ over $T\ge0$
  is $R_\star^{2/(2-\alpha)}\mathcal E_{\mathrm{sp}}$,
  by the same differentiation as~\eqref{E:spatial-energy-map}.
  This bounds the occupation supremum from above.
  For positivity take a constant-in-time unit compact profile
  and its spatial dilation $U_\ell$.
  Its $J$ is $J_0\ell^\alpha A_{\mathrm{sp}}(g)$, where
  $J_0=\int_0^1\int_0^1K_\star(s-t)\ud s\ud t\in(0,\infty)$,
  while $T=\ell^2b(g)$.
  For sufficiently small $\ell>0$, $\alpha<2$ makes
  $J-T/2>0$. Thus the nonempty supremum is a positive finite
  real number. This is a comparison bound; no attaining profile
  or equality in it has been asserted.
  No spatial point trace or rough stochastic evolution was used.
  This proves Proposition~\ref{P:occupation-physical-class}.
\end{proof}

For zero covariance all spatial pairings vanish and set $R_{\mathrm{sp}}=0$.
The spatial and occupation energies are zero suprema of $-b/2$ and $-T/2$:
small spatial dilations of one fixed unit compact profile make these
energies tend to zero, with the profile constant in time for the latter.
No zero-gradient unit state is used. The temporal identities remain
valid, and the moment model is the free case already treated.

===== END TEX FILE: notes/integrated_spatial_occupation.tex =====

===== BEGIN TEX FILE: notes/integrated_cameron_mean.tex =====
\section{The actual compact mean and Cameron block map}
\label{S:actual-cameron-mean}

Retain the nonzero original covariance in Hypothesis~\ref{H:homog},
its amplitude, $a=\alpha_0$, and the actual real phases
$E=H^{1/2}\times H^{-1/2}$ and $F=E\oplus\R^2$.
Write $\Lambda=(1-\Delta)^{1/2}$.
The form $B_\Gamma$ and constant $R_{\mathrm{sp}}$ are those of
Section~\ref{S:spatial-occupation-foundation}.
Let $H_{\mathrm{sp}}$ be the real covariance-null completion of
$C_c^\infty(\R^d)$ with inner product $B_\Gamma$, and $H_t$ the
analogous completion of $C_c^\infty(I)$, $I=(0,1)$, with time
kernel $|s-t|^{-a}$.
Let $H=H_I$ be the completion of smooth tests supported inside
$I\times\R^d$. It embeds isometrically as a closed subspace of
the given raw $H_W$. We retain the given $W$ restricted to it.

Fix $R>0$ and real even $\eta_R\in C_c^\infty(\R^d)$ with
$0\le\eta_R\le1$, equal to one on the radius-$R$ ball and supported
in the closed radius-$2R$ ball. The physical mask is
$m_R=\eta_R^2$. Every driver below takes its mask argument equal to
$m_R$: at this fixed radius the base profile
$\zeta(y)=m_R(Ry)$ meets the earlier hypotheses.
The root $\eta_R$ factors state tests; it does not multiply a raw
noise class. All compactness conclusions here fix $R$.

\subsection{Fractional products and the compact spatial map}

\begin{lemma}[Actual fractional covariance products]
  \label{L:cameron-fractional-products}
  For $\alpha/4<s<1/2$, products of real $H^s$ functions define
  actual elements of $H_{\mathrm{sp}}$, with
  \begin{equation}\label{E:cameron-fractional-product}
    \|fg\|_{H_{\mathrm{sp}}}
    \le C_s^2\sqrt{R_{\mathrm{sp}}}\|f\|_{H^s}\|g\|_{H^s}.
  \end{equation}
  Their Hilbert pairings equal their physical integrals. In particular,
  \begin{equation}\label{E:cameron-fractional-absolute}
    \int|f_1(x)f_2(x)f_3(x-y)f_4(x-y)|\ud x\,\Gamma(\ud y)
    \le C_s^4R_{\mathrm{sp}}\prod_{j=1}^4\|f_j\|_{H^s}.
  \end{equation}
\end{lemma}

\begin{proof}
  First approximate real $H^1$ factors by compact smooth ones.
  The absolute four-linear bound~\eqref{E:spatial-four-linear} and
  covariance PSD make their products Cauchy in $H_{\mathrm{sp}}$,
  with norm at most $\sqrt{R_{\mathrm{sp}}}N(f)N(g)$.
  Expanding product differences proves independence of approximation;
  physical continuity identifies all pairings. PSD for products also
  follows from $fg=((f+g)^2-(f-g)^2)/4$.

  Use real radial Fourier bands $D_0=1_{\{|\xi|<1\}}$ and
  $D_j=1_{\{2^{j-1}\le|\xi|<2^j\}}$, $j\ge1$.
  For $f\in H^s$ put $f_j=D_jf$. Each block is real and in $H^1$.
  Frequency support, Parseval and weighted Cauchy--Schwarz give
  \begin{equation}\label{E:cameron-dyadic-product}
    N(f_j)\le2^{j\alpha/4}\|f_j\|_2,\qquad
    \sum_{j\ge0}N(f_j)\le C_s\|f\|_{H^s}.
  \end{equation}
  Indeed, $\sum_j2^{-2j(s-\alpha/4)}<\infty$, while
  $\sum_j2^{2js}\|f_j\|_2^2\le2^{2s}\|f\|_{H^s}^2$.
  The low block has factor one. No $L^p$ multiplier result is used.
  Also $\sum_j\|f_j\|_2<\infty$ since $s>0$.
  Thus $\sum_j|f_j|$ lies in $L^2$ by Minkowski and monotone
  convergence, and the series is absolutely convergent a.e. with sum $f$.

  Apply the absolute $H^1$ four-linear estimate to each band
  quadruple. The sum of its absolute integrals is at most
  $R_{\mathrm{sp}}\prod_{\ell=1}^4\sum_jN((f_\ell)_j)<\infty$.
  Tonelli and the null-set transfer at both spatial positions in
  Lemma~\ref{L:spatial-physical-pair} identify the physical product
  series, proving~\eqref{E:cameron-fractional-absolute}.
  The double series $\sum_{j,k}f_jg_k$ is also absolutely convergent
  in $H_{\mathrm{sp}}$ by the $H^1$ product bound.
  Its partial sums are products of $H^1$ functions. The absolute
  quadruple calculation identifies their limiting physical pairings
  and gives~\eqref{E:cameron-fractional-product}.
  Compact smooth functions are dense in $H^s$: approximate in
  Fourier space by real Schwartz functions, then cut each off
  compactly in $H^1$ and hence in $H^s$.
  This also proves uniqueness of the bilinear extension.
  This proves Lemma~\ref{L:cameron-fractional-products}.
\end{proof}

\begin{proposition}[Compact spatial mean map]\label{P:cameron-spatial-map}
  The smooth-test map
  \[
    T_{\mathrm{sp}}q=iB_F(m_R(\Gamma*q))
  \]
  extends to a compact linear map
  $T_{\mathrm{sp}}:H_{\mathrm{sp}}\to\mathcal K(F)$, where
  $\mathcal K(F)$ has the operator norm.
  For $z=(z_1,z_2,c_1,c_2)$ and $w=(w_1,w_2,d_1,d_2)$ set
  $w'=\Lambda^{-1}w_2$. Its exact row identity is
  \begin{equation}\label{E:cameron-spatial-row}
    \langle T_{\mathrm{sp}}qz,w\rangle_F
    =\langle q,k(z,w)\rangle_{H_{\mathrm{sp}}},
    \qquad
    k(z,w)=(\eta_Rz_1+c_1\eta_R)(\eta_Rw').
  \end{equation}
\end{proposition}

\begin{proof}
  Fix $s$ with $\alpha/4<s<1/2$; this interval is nonempty because
  the original threshold implies $\alpha<2$.
  For smooth compact $q$, $\Gamma*q$ is locally smooth by
  differentiation under the compactly restricted Radon integral.
  The masked potential is smooth compact.
  The velocity pairing in $E$ has weight $\Lambda^{-1}$;
  hence physical Fubini gives~\eqref{E:cameron-spatial-row}
  on smooth states. Evenness of $\Gamma$ changes
  $B_\Gamma(k,q)$ to $B_\Gamma(q,k)$.
  For general states the localized products are $L^1$, and
  $\Gamma*q$ is bounded on their compact support.
  $L^2$ state approximation passes the physical integral to the
  limit, while Lemma~\ref{L:cameron-fractional-products} passes
  the $H_{\mathrm{sp}}$ pairing. This proves the actual row.

  Multiplication by $\eta_R$ maps bounded $H^{1/2}$ sets to
  precompact $H^s$ sets by Proposition~\ref{P:cutoff-singular-values},
  with gain $1/2-s>0$. This applies to $z_1$ and $w'$.
  The $c_1\eta_R$ family is finite dimensional and compact.
  The closures of both factor families for unit $z,w$ are compact,
  so their products have compact closure $\mathcal L$ in
  $H_{\mathrm{sp}}$ by the fractional product bound.
  The row identity gives
  $\|T_{\mathrm{sp}}q\|\le\sup_{k\in\mathcal L}\|k\|\|q\|$.
  Null covariance classes therefore map to zero.

  For smooth $q$, multiplication by its potential is compact
  $H^{1/2}\to H^{-1/2}$ by the same whole-space cutoff result
  with gain one. Its extra $c_1$ column is finite rank, and the
  instantaneous $c_2$ column is zero. Thus the smooth images
  lie in $\mathcal K(F)$, and so does the bounded extension by
  operator-norm closure.

  Choose a complete smooth-test orthonormal basis of $H_{\mathrm{sp}}$
  by countable compact-support approximation and Gram--Schmidt,
  omitting null classes. Let $Q_n$ project onto its first $n$ terms.
  The row identity yields
  \[
    \|T_{\mathrm{sp}}(I-Q_n)\|
    \le\sup_{k\in\mathcal L}\|(I-Q_n)k\|_{H_{\mathrm{sp}}}
    \longrightarrow0.
  \]
  Strong projection convergence is uniform on compact $\mathcal L$
  by a finite-net argument and $\|I-Q_n\|\le1$.
  Each $T_{\mathrm{sp}}Q_n$ has finite-dimensional range; their
  operator-norm limit is a compact map.
  This is compactness of the map, in addition to compact values.
  This proves Proposition~\ref{P:cameron-spatial-map}.
\end{proof}

\subsection{The actual supported tensor and temporal mean}

\begin{lemma}[Supported raw tensor space]\label{L:cameron-supported-tensor}
  Canonically $H=H_t\otimes H_{\mathrm{sp}}$ as real Hilbert spaces.
  It is separable and admits a complete orthonormal basis $e_j$
  with smooth test representatives supported inside $I\times\R^d$.
  Projection $P_J$ onto its first $J$ elements is also an
  orthogonal projection on $H_W$ by the same finite formula.
\end{lemma}

\begin{proof}
  On separated smooth tests, absolute Fubini makes the raw inner
  product exactly the tensor product after both null quotients.
  Finite sums are dense: approximate a smooth compact spacetime
  test uniformly by smooth time partitions times its spatial slices,
  on one common compact support inside $I\times\R^d$.
  A uniform error $\epsilon$ on spatial compact $A$ has squared
  raw norm at most
  \[
    \epsilon^2|A|\Gamma(A-A)
    \int_I\int_I|s-t|^{-a}\ud s\ud t<\infty.
  \]
  This also gives countable smooth-test density on exhausting
  compact sets, both here and in $H_{\mathrm{sp}}$.
  Gram--Schmidt skipping zeros preserves smooth compact support.
  The isometric embedding into $H_W$ has closed image by completeness;
  its finite orthonormal projection formula remains orthogonal there.
  It is not multiplication by a time indicator and gives no
  independence of disjoint time intervals.
  This proves Lemma~\ref{L:cameron-supported-tensor}.
\end{proof}

\begin{proposition}[The compact temporal mean, without trace class]
  \label{P:cameron-temporal-map}
  Let $K$ on $L^2(I)$ have kernel $|s-t|^{-a}$.
  It is compact, self-adjoint, strictly positive and injective.
  The map $\iota:f\mapsto K^{1/2}f$ extends isometrically from
  $H_t$ onto $L^2(I)$, and the actual temporal mean
  \begin{equation}\label{E:cameron-temporal-map}
    C_t=K^{1/2}\iota:H_t\longrightarrow L^r(I)
  \end{equation}
  is bounded and compact for every $2<r<2/a$.
  The displayed formula first has its $L^2(I)$ meaning; the same
  completed map is then shown to take values compactly in $L^r(I)$.
  The operator $K$ is not trace class and $C_t:H_t\to L^2(I)$
  is not Hilbert--Schmidt.
\end{proposition}

\begin{proof}
  Schur bounds $K$ by its finite row and column integrals.
  The Gamma representation of $|s-t|^{-a}$ and zero extension
  of $f\in L^2(I)$ give strict positivity directly:
  the kernel $e^{-\lambda|v|}$ has quadratic form
  \[
    \int_\R\frac{2\lambda}{\lambda^2+\xi^2}
    |\widehat f(\xi)|^2\ud\xi>0
    \quad(f\ne0,\ \lambda>0)
  \]
  in the unitary Fourier convention.
  Absolute Fubini is justified by Schur applied to $|f(s)f(t)|$.
  Integrating with positive weight
  $\lambda^{a-1}/\Gamma_E(a)$ proves positivity and injectivity.
  Symmetry gives self-adjointness.
  The deterministic truncated kernel
  $K_\epsilon=K1_{\{|s-t|\ge\epsilon\}}$ is square integrable,
  so finite separated-kernel approximations make it compact.
  The Schur norm of $K-K_\epsilon$ is at most
  $2\epsilon^{1-a}/(1-a)$, proving compactness of $K$.
  These truncations are not used as Gaussian covariances.
  Its positive square root is compact by the compact spectral theorem.

  On tests $\|K^{1/2}f\|_2=\|f\|_{H_t}$.
  Smooth-test $L^2$ density and $\ker K=0$ imply that its range
  is dense, so the isometry extends onto $L^2(I)$.
  On tests $C_tf=Kf$, and~\eqref{E:cameron-temporal-map}
  first gives compactness into $L^2$.

  Extend $K_a(v)=|v|^{-a}1_{\{|v|\le1\}}$ to the line.
  It lies in $L^{r/2}$. Scalar Young convolution gives
  \[
    \|g\|_{H_t}^2\le\|K_a\|_{r/2}\|g\|_{r'}^2,\qquad
    r'=r/(r-1).
  \]
  To verify the needed Young inequality, take $u=r/2$, $v=r'$,
  so $u,v<r$ and $1/u+1/v=1+1/r$.
  Split the absolute convolution integrand into
  $(|f|^u|h|^v)^{1/r}$, $|f|^{1-u/r}$ and $|h|^{1-v/r}$.
  H\"older with exponents $r$, $(1/u-1/r)^{-1}$ and
  $(1/v-1/r)^{-1}$, followed by integration and Tonelli, gives
  $\|f*h\|_r\le\|f\|_u\|h\|_v$.
  Covariance Cauchy--Schwarz and $L^r$ duality now imply
  $\|Kf\|_r\le C_{a,r}\|f\|_{H_t}$ on tests.
  Their $Kf$ are bounded by the integrable-kernel row, making
  duality legitimate before completion.
  Density extends the estimate, with $L^2$ value equal to
  \eqref{E:cameron-temporal-map}.
  Choose $r<r_2<2/a$. Compactness into $L^2$ and boundedness
  into $L^{r_2}$ give compactness into $L^r$ by
  $\|u\|_r\le\|u\|_2^\tau\|u\|_{r_2}^{1-\tau}$ with
  $1/r=\tau/2+(1-\tau)/r_2$.

  Finally the orthonormal cell indicators
  $N^{1/2}1_{(j/N,(j+1)/N)}$, $0\le j<N$, have $K$ quadratic
  forms summing to
  $2N^a/((1-a)(2-a))\to\infty$.
  Thus positive $K$ has infinite trace, and $K^{1/2}\iota$
  is not Hilbert--Schmidt into $L^2$.
  No instantaneous $L^2$-valued Gaussian has been introduced.
  This proves Proposition~\ref{P:cameron-temporal-map}.
\end{proof}

\begin{proposition}[The compact time-space mean]\label{P:cameron-full-mean}
  Fix one $2<r<2/a$ throughout this proposition.
  For finite tensors with orthonormal spatial labels define
  \[
    \mathcal U\left(\sum_j f_j\otimes q_j\right)(s)
    =\sum_j(Kf_j)(s)q_j.
  \]
  It extends to a bounded map $H\to L^r(I;H_{\mathrm{sp}})$
  with dimension-free bound.
  The map
  \begin{equation}\label{E:cameron-full-mean}
    T\Phi(s)=T_{\mathrm{sp}}(\mathcal U\Phi(s))
    :H\longrightarrow L^r(I;\mathcal K(F))
  \end{equation}
  is compact. For smooth supported $\Phi$, it is the actual
  multiplier $iB_F(m_Rh_\Phi(s))$, where
  $h_\Phi=|\cdot|^{-a}*(\Gamma*\Phi)$.
  For the supported projections of Lemma~\ref{L:cameron-supported-tensor},
  \begin{equation}\label{E:cameron-compact-tail}
    \epsilon_J:=\|T(I-P_J)\|_{H\to L^r(\mathcal K(F))}
    \longrightarrow0.
  \end{equation}
\end{proposition}

\begin{proof}
  For a finite-dimensional spatial field $g$, positivity of the time
  kernel and scalar Young give
  \[
    \|g\|_{H_t\otimes H_{\mathrm{sp}}}^2
    \le\int_I\int_I|s-t|^{-a}\|g_s\|\|g_t\|\ud s\ud t
    \le C_{a,r}^2\|g\|_{L^{r'}(H_{\mathrm{sp}})}^2.
  \]
  Hilbert Cauchy--Schwarz and finite-dimensional $L^r$ duality give
  $\|\mathcal U\Phi\|_{L^r(H_{\mathrm{sp}})}\le C_{a,r}\|\Phi\|_H$.
  The duality can be checked by the pointwise direction
  $\|\mathcal U\Phi\|^{r-2}\mathcal U\Phi$ and smooth coefficient
  approximation in $L^{r'}$, controlled by the displayed estimate.
  No dimension factor occurs. Tensor density and completeness
  extend this to a strongly measurable Bochner field.
  This time-only map still contains raw spatial labels.
  Spatial covariance is applied once, by $T_{\mathrm{sp}}$.

  The actual physical mean identity on separated tests follows from
  \eqref{E:cameron-spatial-row}. For a smooth spacetime test use
  the separated compact-support approximations in the tensor proof.
  Their uniform errors give uniformly small masked mean errors,
  using the finite time row and locally finite spatial covariance
  on the relevant compact differences. The multiplier bound by
  $L^\infty+L^2$ then gives uniform operator convergence,
  identifying the $L^r$ mean in~\eqref{E:cameron-full-mean}.
  General $H$ controls denote completed operator fields, without a
  pointwise-potential assertion.

  Let $Q_n$ be the spatial projections in the compact-map proof.
  The maps $T_n\Phi=T_{\mathrm{sp}}Q_n\mathcal U\Phi$ approximate
  $T$ in operator norm by the dimension-free bound and
  $\|T_{\mathrm{sp}}(I-Q_n)\|\to0$.
  For fixed $n$, each spatial coordinate extraction $H\to H_t$
  has norm at most one and its image under $C_t$ is precompact
  in $L^r$. Finite combination with the compact operators
  $T_{\mathrm{sp}}q_j$ makes $T_n$ compact.
  Hence $T$ is compact. Scalar time compactness alone tensored
  with an infinite identity would not prove this.

  To prove~\eqref{E:cameron-compact-tail}, if it failed choose
  unit $v_J$ on a subsequence with $\|T(I-P_J)v_J\|$ bounded below.
  The vectors $(I-P_J)v_J$ tend weakly to zero, since their
  pairings with fixed $h$ are bounded by $\|(I-P_J)h\|$.
  Compactness gives a norm-convergent image subsequence with
  weak limit zero, a contradiction.
  This proves Proposition~\ref{P:cameron-full-mean}.
\end{proof}

\subsection{The given-noise residual and its Cameron operator}

Choose integer $B\ge1$ and $0<\delta<\min(1,1/B)$.
Put $N=\lfloor1/(\delta B)\rfloor$, $s_m=m\delta B$,
$\ell_m=B$ for $m<N$ and $\ell_N=\delta^{-1}-NB\in[0,B)$.
The intervals $I_m=[s_m,s_m+\delta\ell_m]$ partition $[0,1]$
up to endpoints. With $Q_J=I-P_J$ on $H_W$ and the literal
pullback~\eqref{E:raw-block-pullback}, define
\[
  Y_{m,J}(f)=W(Q_JT_{\delta,m}f),\qquad
  g_\delta=\delta^{(1-a)/2}.
\]
Fix parameters
\begin{equation}\label{E:cameron-block-parameters}
  \frac12<\theta<\min\left(1-\frac a2,\frac{3-a-\alpha}{2}\right),
  \qquad \frac1{1-\theta}<r<\frac2a,\qquad
  \frac1\theta\le p<2<r .
\end{equation}
These intervals are nonempty.

\begin{lemma}[Actual supported residual paths]
  \label{L:cameron-actual-residual}
  Gaussian transfer with mask $m_R$ and its genuine $F$ extension
  constructs the actual centered Gaussian paths
  \[
    X_{m,J}(u)=g_\delta A_{m_R}(Y_{m,J})(\min(u,\ell_m)),
    \qquad 0\le u\le B.
  \]
  Their finite tuple lies in the separable space
  $\mathscr B_0^{N+1}$, where
  $\mathscr B_0=h_0^\theta([0,B];\mathcal K(F))$.
  Every continuous linear statistic $\ell(X)$ is $W(k_\ell)$
  for some $k_\ell\in H_I$. An empty last interval gives zero.
\end{lemma}

\begin{proof}
  Isometry of the pullback and orthogonality of $Q_J$ give
  $\operatorname{Var}Y_{m,J}(f)\le\|f\|_{H_W}^2$.
  Proposition~\ref{P:source-gaussian-transfer} therefore applies.
  Its finite sums retain both deterministic localizations, and
  their limits retain the true $F$ extension and constant columns.
  Choose $\theta<\beta<\beta_2$ below the upper threshold in
  \eqref{E:cameron-block-parameters}; read the driver theorem at
  exponent $\beta$ with auxiliary $\beta_2$.
  Constant stopping preserves compact values and $C^\beta$
  bounds, hence gives paths in the little $C^\theta$ closure
  by polygonal approximation.
  Its separability is Lemma~\ref{L:raw-block-inputs}.

  As in Lemma~\ref{L:raw-block-inputs}, every observed row's slow
  pullback belongs to $H_I$:
  its time support is in $[0,1]$, and approximating its indicator
  inside $I$ converges in raw norm by dominated convergence
  against the integrable time kernel and locally finite $\Gamma$
  on the common compact support. This includes endpoints.
  Schwartz $E$ states and both true constant columns supply the
  identities, then boundedness extends them to $F$.
  Let $P_H$ be the orthogonal projection onto closed $H_I$.
  Transfer for the noise $f\mapsto W(P_HQ_JT_{\delta,m}f)$
  leaves each observed row unchanged, since its residual slow
  test already lies in $H_I$. Countable states and rational
  times identify the same operator paths.
  This projected-transfer series has coefficient tests in $H_I$.
  Applying $\ell$ gives an $L^2$ limit in the closed isonormal
  image $W(H_I)$, proving the assertion.
  Original global-basis tests were not assumed individually supported.
  No time-support independence or Hilbert-valued noise is used.
  This proves Lemma~\ref{L:cameron-actual-residual}.
\end{proof}

\begin{proposition}[Actual Cameron covariance and averaged bound]
  \label{P:cameron-actual-embedding}
  The actual covariance map $L_{\delta,J}\Phi=\E[XW(\Phi)]$ is
  \begin{equation}\label{E:cameron-actual-covariance}
    (L_{\delta,J}\Phi)_m(u)=\sqrt\delta
    \int_0^{\min(u,\ell_m)}
    S_F(-v)T(Q_J\Phi)(s_m+\delta v)S_F(v)\ud v ,
    \qquad \Phi\in H.
  \end{equation}
  This is a compact-operator Bochner integral.
  Define the exact norm and constants
  \begin{equation}\label{E:cameron-averaged-norm}
    \|x\|_{\delta,p}
    =\left(\delta\sum_{m=0}^N\|x_m\|_{C^\theta}^p\right)^{1/p},
    \quad G_B=\sup_{|v|\le B}\|S_F(v)\|,
    \quad C_B=G_B^2[B^{1-1/r}+B^{1-1/r-\theta}].
  \end{equation}
  Then the actual Gaussian Cameron embedding satisfies
  \begin{equation}\label{E:cameron-averaged-bound}
    \|L_{\delta,J}\Phi\|_{\delta,p}
    \le\sqrt\delta\,C_B(2/B)^{1/p-1/r}
    \epsilon_J\|\Phi\|_H .
  \end{equation}
  Convergence $\epsilon_J\to0$ fixes $R$ and is independent of $\delta$.
\end{proposition}

\begin{proof}
  For smooth supported $\Phi$, $Q_J\Phi$ is another such test.
  The literal pullback covariance~\eqref{E:raw-block-mean-jacobian}
  gives
  \[
    \E[Y_{m,J}(f)W(\Phi)]
    =\delta^{a/2}\int f(v,x)
    h_{Q_J\Phi}(s_m+\delta v,x)\ud x\ud v .
  \]
  Absolute Fubini also holds for signed compact tests.
  Multiplying by $g_\delta$ gives $\sqrt\delta$.
  Literal rows and~\eqref{E:cameron-spatial-row} give
  \eqref{E:cameron-actual-covariance}. The constant-velocity
  input acquires displacement $v$ under $S_F(v)$; the constant
  displacement remains one. Both columns are included.

  Both $S_F$ and its adjoint are strongly continuous on Hilbert $F$.
  In Bessel-unitary $E$ coordinates the Fourier matrix is
  \[
    \begin{pmatrix}
      \cos(v|\xi|)&\langle\xi\rangle\sin(v|\xi|)/|\xi|\\
      -|\xi|\sin(v|\xi|)/\langle\xi\rangle&\cos(v|\xi|)
    \end{pmatrix}.
  \]
  Its continuous zero quotient and common bound $C(1+B)$ apply
  also to its adjoint; dominated convergence proves the assertion.
  The constant block is finite dimensional.
  For compact $A$, conjugation $S_F(-v)AS_F(v)$ is norm continuous:
  strong convergence is uniform on compact images, and the right
  factor follows by adjoints. Joint norm continuity in $(v,A)$
  and uniform bounds give Bochner measurability for the conjugated
  strongly measurable compact-operator field.
  No norm continuity of the free group itself is assumed.

  Write $M=TQ_J\Phi$. H\"older and the primitive increment estimate give
  \begin{equation}\label{E:cameron-local-primitive-bound}
    \|(L_{\delta,J}\Phi)_m\|_{C^\theta}
    \le\sqrt\delta\,C_B\delta^{-1/r}\|M\|_{L^r(I_m)}.
  \end{equation}
  Its primitive exponent is $1-1/r>\theta$.
  Simple compact-operator integrand approximation in $L^r$ puts
  the primitive in $\mathscr B_0$; constant stopping does not
  increase the H\"older norm.
  Affine pullback preserves null sets.
  For fixed $\delta,J$ the actual covariance map is bounded by
  Bochner Cauchy--Schwarz and finite tuple $L^2$ moments.
  The integral is bounded by the displayed estimate, so equality
  on smooth controls extends by density to all $H$.
  Dense states and rational times make it a full operator-path identity.

  Let $H_{\mathrm{seen}}$ be the closed span of the $k_\ell$
  from Lemma~\ref{L:cameron-actual-residual}.
  Then $\ell(L_{\delta,J}\Phi)=\langle k_\ell,\Phi\rangle_H$
  and $\ker L_{\delta,J}=H_{\mathrm{seen}}^\perp$.
  The first-chaos definition of the Cameron space is therefore
  $L_{\delta,J}(H_{\mathrm{seen}})$ with the minimum raw-$H$
  preimage norm. Extra directions are removed by orthogonal
  projection, without an inverse covariance.
  A raw-$H$ operator bound is thus the actual embedding bound.

  Put $t_m=\|M\|_{L^r(I_m)}\ge0$ and $n=N+1\ge2$.
  Finite power mean at exponent $r/p>1$, applied to $t_m^p$, gives
  \[
    \left(\sum_m t_m^p\right)^{1/p}
    \le n^{1/p-1/r}\left(\sum_m t_m^r\right)^{1/r}.
  \]
  The true partition gives $\sum_m t_m^r=\|M\|_{L^r(I)}^r$,
  including an empty last interval, and $n\le2/(\delta B)$.
  Hence the exact $\delta$-weighted norm gives
  \[
    \|L_{\delta,J}\Phi\|_{\delta,p}
    \le\sqrt\delta\,C_B(\delta n)^{1/p-1/r}\|M\|_{L^r}
    \le\sqrt\delta\,C_B(2/B)^{1/p-1/r}
    \epsilon_J\|\Phi\|_H.
  \]
  The $B$ factor remains explicit; covariance and mask occur once.
  This proves Proposition~\ref{P:cameron-actual-embedding}.
\end{proof}

These conclusions fix the radius and make no uniform-radius projection
tail assertion. No concentration estimate or original moment upper bound
follows from this section alone.

===== END TEX FILE: notes/integrated_cameron_mean.tex =====

===== BEGIN TEX FILE: notes/integrated_young_upper_foundation.tex =====
\section{Young perturbations retaining the deterministic endpoint}
\label{S:young-upper-foundation}

Let $\mathcal X$ be any nonzero real Banach space, with its induced
operator norm on $\mathcal B(\mathcal X)$.
Fix $B\ge1$, $1/2<\theta<1$ and $\nu=1/\theta<2$.
All driver paths start at zero and have norm
$\|D\|_\theta=\sup_t\|D(t)\|+[D]_\theta$ on $[0,B]$.
Let $U_D=I+\int\ud D\,U_D$ be the left Young evolution.
The construction in Proposition~\ref{P:constant-young-linear} applies:
its proof needs completeness and operator multiplication of norm one,
with no Hilbert-space assumption.
The primary estimate is
\cite{friz.hairer:20:course}*{Section~1.5, p.~13;
Section~4.1, (4.1)--(4.3), pp.~61--62}.

\begin{lemma}[Refined growth and uniform inverse control]
  \label{L:young-upper-growth}
  With dimension-free constants,
  \begin{equation}\label{E:young-upper-refined-growth}
    \sup_{t\le B}\|U_D(t)\|
    \le\exp\{c_{\theta,B}(d+d^\nu)\},\qquad d=\|D\|_\theta .
  \end{equation}
  For $\|H\|_\theta\le K$, $K\ge1$,
  \begin{equation}\label{E:young-upper-inverse-control}
    \|U_H\|_{C^\theta}+\|U_H^{-1}\|_{C^\theta}
    \le L_{\theta,B,K}<\infty .
  \end{equation}
\end{lemma}

\begin{proof}
  Let $c_\theta=2\max(1,C_\theta)$ for the primary Young constant.
  The complete scaled norm
  $N_\ell(V)=\sup\|V\|+\ell^\theta[V]_\theta$ satisfies
  $N_\ell(\int_a^\cdot\ud D\,V)
  \le c_\theta[D]_\theta\ell^\theta N_\ell(V)$,
  as in~\eqref{E:constant-young-local}.
  If $c_\theta dB^\theta\le1/4$, whole-interval contraction gives
  $\sup\|U_D\|\le(1-c_\theta dB^\theta)^{-1}$ and hence
  $\log\sup\|U_D\|\le2c_\theta B^\theta d$.
  Otherwise take $n_D=\lceil B(4c_\theta d)^\nu\rceil$ equal
  pieces. Their contraction ratios are at most $1/4$ and local
  norms at most $4/3$. The expression inside the ceiling exceeds
  one, so $n_D\le2B(4c_\theta d)^\nu$.
  Composition gives the $d^\nu$ bound. At $d=0$, $U_D=I$,
  proving~\eqref{E:young-upper-refined-growth} without a prefactor.

  On the ball $\|H\|_\theta\le K$ choose one uniform equal
  partition with ratio at most $1/4$.
  Each local evolution $Q$ has $N_\ell(Q)\le4/3$ and
  $\sup\|Q-I\|\le1/3$. Its Neumann inverse is bounded by $3/2$.
  Products give uniform global sup bounds.
  The same scaled estimate bounds local H\"older seminorms.
  Pairs crossing a boundary at distance below $\ell$ split into
  at most two pieces; use
  $h_1^\theta+h_2^\theta\le2^{1-\theta}(h_1+h_2)^\theta$.
  For larger distances use $2\sup\|U_H\|/\ell^\theta$.
  This gives its global $C^\theta$ bound. Finally,
  \[
    U_H^{-1}(t)-U_H^{-1}(s)
    =-U_H^{-1}(t)(U_H(t)-U_H(s))U_H^{-1}(s)
  \]
  bounds the inverse seminorm.
  This proves Lemma~\ref{L:young-upper-growth}.
\end{proof}

\begin{proposition}[Multiplicative upper perturbation]
  \label{P:young-upper-multiplicative}
  If $K\ge1$, $\|H\|_\theta\le K$, $x=\|X\|_\theta$ and
  $A\in\mathcal B(\mathcal X)$, then
  \begin{equation}\label{E:young-upper-multiplicative}
    \|AU_{H+X}(t)\|
    \le\|AU_H(t)\|\exp\{C_{\theta,B,K}(x+x^\nu)\},
    \qquad 0\le t\le B.
  \end{equation}
  This includes noninvertible $A$ and $A=0$ with no extra factor
  when $x=0$.
\end{proposition}

\begin{proof}
  Put $U=U_H$, $R=U^{-1}$ and $G(s)Z=R(s)ZU(s)$.
  Lemma~\ref{L:young-upper-growth} makes $G$ a $C^\theta$ path
  of bounded linear maps on $\mathcal B(\mathcal X)$, uniformly
  bounded on the fixed ball. Thus the Banach Young integral
  \[
    Z(t)=\int_0^tR(s)\ud X(s)U(s)
  \]
  exists, with $\|Z\|_\theta\le L'_{\theta,B,K}x$ and
  $Z_{s,t}=R(s)X_{s,t}U(s)+O(|t-s|^{2\theta})$.
  Put $V=U_Z$. Its and $U$'s Young remainders are
  $V_{s,t}=Z_{s,t}V(s)+O(|t-s|^{2\theta})$ and
  $U_{s,t}=H_{s,t}U(s)+O(|t-s|^{2\theta})$.
  The exact increment of $P=UV$ includes a cross term of order
  $2\theta$. Substitution in the stated left order gives
  \[
    P_{s,t}
    =H_{s,t}P(s)+U(s)R(s)X_{s,t}U(s)V(s)
    +O(|t-s|^{2\theta})
    =(H+X)_{s,t}P(s)+O(|t-s|^{2\theta}).
  \]
  On any partition the remainder sum is bounded by a constant
  times $B\,\operatorname{mesh}^{2\theta-1}\to0$.
  Left sums converge to the Young integral, so uniqueness yields
  $U_{H+X}=U_HU_Z$. This proves the product identity without
  assuming smooth density in the full H\"older norm.
  Apply~\eqref{E:young-upper-refined-growth} to $Z$, then left
  multiply by $A$ and use submultiplicativity.
  No inverse or lower bound for $A$ is required.
  This proves Proposition~\ref{P:young-upper-multiplicative}.
\end{proof}

===== END TEX FILE: notes/integrated_young_upper_foundation.tex =====

===== BEGIN TEX FILE: notes/integrated_uniform_mean.tex =====
\section{Uniform spatial-radius means and Cameron regulation}
\label{S:uniform-mean-regulation}

Retain the original nonzero covariance, amplitude and real spaces of
Section~\ref{S:actual-cameron-mean}. Fix
$\alpha/4<s<1/2$ and put $\beta=1/2-s>0$.
Write $A_s=C_s^2\sqrt{R_{\mathrm{sp}}}$ for the constant in
\eqref{E:cameron-fractional-product}.
Choose a real even smooth compact $\eta$, equal to one on the unit ball,
with $0\le\eta\le1$ and support in the closed radius-two ball.
For $R\ge1$ set $\eta_R(x)=\eta(x/R)$ and $m_R=\eta_R^2$.
In this section the mean acts on $E=H^{1/2}\times H^{-1/2}$.
The constant data columns belong to $F$, outside $E$.
All uniform-radius claims below concern $E$.
The actual spatial map $T_R:H_{\mathrm{sp}}\to\mathcal K(E)$
is the $E$ restriction of Proposition~\ref{P:cameron-spatial-map}.
Its literal row is
\begin{equation}\label{E:uniform-mean-row}
  \langle T_Rqz,w\rangle_E
  =\langle q,k_R(z,w)\rangle_{H_{\mathrm{sp}}},
  \qquad
  k_R(z,w)=(\eta_Rz_1)(\eta_R\Lambda^{-1}w_2).
\end{equation}
Thus the physical mask occurs once, after covariance convolution.

\subsection{Uniform multiplier and spatial tails}

\begin{lemma}[Uniform cutoff and physical mean]
  \label{L:uniform-mean-cutoff}
  For every real $\sigma$, multiplication by $\eta_R$ on $H^\sigma$
  has norm at most
  \[
    M_\sigma=2^{|\sigma|/2}(2\pi)^{-d/2}
    \int_{\R^d}|\widehat\eta(p)|\langle p\rangle^{|\sigma|}\ud p,
  \]
  independently of $R\ge1$. With $M=M_{1/2}$ and $M_0=A_sM^2$,
  \begin{equation}\label{E:uniform-spatial-mean}
    \|k_R(z,w)\|_{H_{\mathrm{sp}}}
    \le M_0\|z\|_E\|w\|_E,\qquad
    \|T_R\|_{H_{\mathrm{sp}}\to\mathcal L(E)}\le M_0 .
  \end{equation}
\end{lemma}

\begin{proof}
  Peetre's inequality bounds the weighted Fourier kernel for
  multiplication by $\eta_R$ by convolution with
  \[
    2^{|\sigma|/2}(2\pi)^{-d/2}
    |\widehat{\eta_R}(q)|\langle q\rangle^{|\sigma|}.
  \]
  Here $\widehat{\eta_R}(q)=R^d\widehat\eta(Rq)$.
  Substitution $p=Rq$ and $\langle p/R\rangle\le\langle p\rangle$
  bound its $L^1$ norm by $M_\sigma$.
  The $L^1*L^2$ inequality proves the assertion on Schwartz
  functions and density extends it to $H^\sigma$.
  The map $w_2\mapsto\Lambda^{-1}w_2$ is an isometry from
  $H^{-1/2}$ to $H^{1/2}$, and $H^{1/2}\hookrightarrow H^s$
  has norm one. Apply the cutoff bound at $\sigma=1/2$ and
  Lemma~\ref{L:cameron-fractional-products} to the two factors
  in~\eqref{E:uniform-mean-row}. Hilbert Cauchy--Schwarz then
  gives the operator bound. This is the existing completed physical
  map: the row agrees on smooth controls and hence on their completion.
  Its compact values at each fixed $R$ are retained.
  This proves Lemma~\ref{L:uniform-mean-cutoff}.
\end{proof}

\begin{lemma}[Uniform heat and frequency tails]
  \label{L:uniform-mean-spatial-tails}
  Let $C_\varepsilon$ be the actual covariance-Hilbert heat
  contraction with Fourier multiplier $e^{-\varepsilon|\xi|^2/2}$.
  There is a real orthogonal projection $P_K$ on $H_{\mathrm{sp}}$
  corresponding to the closed frequency ball $\{|\xi|\le K\}$.
  It commutes with heat. For $K\ge1$, $\varepsilon>0$ and $R\ge1$,
  \begin{align}
    \|T_R(I-C_\varepsilon)\|
    &\le M_h\varepsilon^{\beta/2},
    &M_h&=4A_sM^2\E|G_d|^\beta,\label{E:uniform-mean-heat}\\
    \|T_R(I-P_K)\|
    &\le M_fK^{-\beta},
    &M_f&=\frac{M_h}{1-e^{-1/2}},\label{E:uniform-mean-frequency}
  \end{align}
  where $G_d$ is a standard real $d$-dimensional normal vector.
  Operator norms are from $H_{\mathrm{sp}}$ to $\mathcal L(E)$.
  The projection $P_K$ is allowed to have infinite rank.
\end{lemma}

\begin{proof}
  Translations $\tau_hf(x)=f(x-h)$ extend to strongly continuous
  isometries of the actual $H_{\mathrm{sp}}$.
  Indeed, in its covariance Fourier isometry they multiply by
  $e^{-i\xi\cdot h}$; dominated convergence gives continuity
  on tests, then density and isometry give it on the completion.
  The real subspace is preserved.
  The inequalities $|e^{-it}-1|\le2\min(1,|t|^\beta)$ and
  $|\xi|^\beta\langle\xi\rangle^s\le\langle\xi\rangle^{1/2}$
  show that
  \[
    \|\tau_hf-f\|_{H^s}
    \le2\min(1,|h|^\beta)\|f\|_{H^{1/2}} .
  \]
  Use this for $f=\eta_Rz_1$ and $g=\eta_R\Lambda^{-1}w_2$.
  The product identity
  \[
    \tau_h(fg)-fg=(\tau_hf-f)\tau_hg+f(\tau_hg-g)
  \]
  holds in $H_{\mathrm{sp}}$, first for smooth factors and
  then by the continuous fractional product extension.
  Lemma~\ref{L:uniform-mean-cutoff} gives
  \begin{equation}\label{E:uniform-mean-row-translation}
    \|\tau_hk_R(z,w)-k_R(z,w)\|_{H_{\mathrm{sp}}}
    \le4A_sM^2\min(1,|h|^\beta)\|z\|_E\|w\|_E .
  \end{equation}

  The Bochner integral $\int p_\varepsilon(h)\tau_hk\ud h$
  exists, since the translation orbit is strongly continuous
  and bounded in the separable covariance Hilbert space.
  Its Fourier image is $e^{-\varepsilon|\xi|^2/2}\widehat k$:
  ordinary Gaussian integration proves this on tests and
  contraction extends it to all $k$.
  It is therefore the actual $C_\varepsilon$ of the source construction.
  Heat has variance $\varepsilon$ here; there is no additional
  Fourier normalization factor. Integrating
  \eqref{E:uniform-mean-row-translation} with
  $h=\sqrt\varepsilon G_d$ bounds
  $\|(I-C_\varepsilon)k_R(z,w)\|$ by
  $M_h\varepsilon^{\beta/2}\|z\|_E\|w\|_E$.
  Selfadjointness in~\eqref{E:uniform-mean-row} proves
  \eqref{E:uniform-mean-heat}.

  To construct $P_K$, let $V$ be the closed image of the covariance
  Fourier isometry into $L^2(\mu)$, including its fixed
  $(2\pi)^{d/2}$ factor. No surjectivity is assumed.
  Its formula extends to Schwartz functions: compact cutoff
  approximation converges in Schwartz seminorms, and temperedness
  of $\mu$ controls the Fourier error in $L^2(\mu)$.
  Choose real even radial smooth $\chi_n$, equal to one on
  the closed ball of radius $K$, zero outside radius $K+1/n$,
  and between zero and one.
  For real Schwartz $f$, the function $\chi_n\widehat f$ is
  the transform of another real Schwartz function and so lies in $V$.
  Dominated convergence against $|\widehat f|^2\mu$ gives
  $1_{\{|\xi|\le K\}}\widehat f\in V$.
  The pointwise limit includes the boundary sphere, even if
  $\mu$ charges it. Test density and contraction extend this
  assertion to all of $V$.
  Indicator multiplication is selfadjoint and idempotent on $V$;
  pulling it back defines the asserted real orthogonal $P_K$.
  All Fourier multipliers here commute.

  On $|\xi|>K$ one has
  $1-e^{-|\xi|^2/(2K^2)}\ge1-e^{-1/2}$, whence
  \[
    \|(I-P_K)k\|_{H_{\mathrm{sp}}}
    \le(1-e^{-1/2})^{-1}\|(I-C_{K^{-2}})k\|_{H_{\mathrm{sp}}}.
  \]
  Apply the row heat bound and selfadjointness of $P_K$ in
  \eqref{E:uniform-mean-row} to obtain
  \eqref{E:uniform-mean-frequency}.
  No density of $\mu$, periodic state space or finite rank was used.
  This proves Lemma~\ref{L:uniform-mean-spatial-tails}.
\end{proof}

\subsection{The time tensor and the actual regulator}

\begin{lemma}[Dimension-free Hilbert tensor extension]
  \label{L:uniform-mean-tensor}
  If $H_0,G$ are real Hilbert spaces, $2\le r<\infty$ and
  $A:H_0\to L^r(I)$ is bounded, then
  \[
    \|A\otimes I_G\|_{H_0\otimes G\to L^r(I;G)}\le\|A\|.
  \]
  The tensor extension need not be compact when $A$ is compact.
\end{lemma}

\begin{proof}
  For a finite tensor write $v=\sum_{j=1}^n f_j\otimes e_j$
  with $(e_j)$ orthonormal. Its squared norm is $\sum_j\|f_j\|^2$.
  Let $\gamma_j$ be independent standard real normals and
  $m_r=\E|\gamma_1|^r$. Finite covariance diagonalization gives
  \[
    \E\left\|\sum_j\gamma_j f_j\right\|_{H_0}^r
    \le m_r\left(\sum_j\|f_j\|_{H_0}^2\right)^{r/2}.
  \]
  In fact, if $\lambda_l$ are the covariance eigenvalues and
  $L=\sum_l\lambda_l$, the squared norm has law
  $\sum_l\lambda_l\zeta_l^2$ for independent standard $\zeta_l$.
  For $L>0$, convexity at exponent $r/2\ge1$ bounds
  $(\sum_l(\lambda_l/L)\zeta_l^2)^{r/2}$
  by $\sum_l(\lambda_l/L)|\zeta_l|^r$.
  Taking expectations proves the inequality; $L=0$ is immediate.
  Also $L=\sum_j\|f_j\|^2$.

  Choose measurable representatives of the finitely many $Af_j$.
  Scalar Gaussian moments and Tonelli give
  \begin{align*}
    m_r\int_I\left(\sum_j|Af_j(t)|^2\right)^{r/2}\ud t
    &=\E\left\|A\sum_j\gamma_jf_j\right\|_{L^r}^r\\
    &\le\|A\|^rm_r\left(\sum_j\|f_j\|^2\right)^{r/2}.
  \end{align*}
  Cancel the finite positive $m_r$ and take the $r$th root.
  Finite tensor density and Bochner completeness give the extension.
  The zero space is trivial.
  If $Af\ne0$ and $G$ has an infinite orthonormal sequence $(e_j)$,
  the images of the bounded sequence $f\otimes e_j$ have pairwise
  distance $\sqrt2\|Af\|_{L^r}$. They have no convergent subsequence,
  even when the scalar map $A$ is compact.
  Only finite auxiliary Gaussians were used in the estimate.
  This proves Lemma~\ref{L:uniform-mean-tensor}.
\end{proof}

Recall the actual supported identity $H_I=H_t\otimes H_{\mathrm{sp}}$,
the compact scalar covariance map $C_t:H_t\to L^r(I)$, $2<r<2/a$,
and its completed tensor $U=C_t\otimes I_{H_{\mathrm{sp}}}$ from
Section~\ref{S:actual-cameron-mean}.
On finite smooth tensors $U$ agrees with the earlier $\mathcal U$;
density gives equality of their completed maps.
For block applications fix the same $r$ as in
\eqref{E:cameron-block-parameters}. All $c_t,\varepsilon_J$ and
mean norms below use that one choice.
Choose a smooth-test orthonormal basis of $H_t$ and let $\pi_J$
be its first-$J$ orthogonal projection, with $\pi_0=0$.
Put
\[
  c_t=\|C_t\|,\qquad
  \varepsilon_J=\|C_t(I-\pi_J)\|_{H_t\to L^r(I)},\qquad
  \mathcal T_R=T_RU .
\]

\begin{proposition}[Uniform completed mean regulation]
  \label{P:uniform-mean-regulator}
  On $H_I$ the operators
  \[
    P_{\mathrm{ret}}=\pi_J\otimes P_K,\qquad
    Q_{J,K}=I-P_{\mathrm{ret}}
  \]
  are real orthogonal projections, and $\varepsilon_J\to0$.
  The actual mean is a strongly measurable
  $L^r(I;\mathcal K(E))$ field and satisfies, uniformly for $R\ge1$,
  \begin{equation}\label{E:uniform-completed-mean}
    \|\mathcal T_R\|\le M_0c_t,\qquad
    \|\mathcal T_RQ_{J,K}\|
    \le M_0\varepsilon_J+M_fc_tK^{-\beta}.
  \end{equation}
  These norms have domain $H_I$ and target $L^r(I;\mathcal L(E))$.
\end{proposition}

\begin{proof}
  The tensor projections are selfadjoint, idempotent and contractive
  on finite tensors and hence on their Hilbert completion.
  For the scalar tail, failure of convergence would supply unit
  $v_J$ with $\|C_t(I-\pi_J)v_J\|$ bounded below on a subsequence.
  But $(I-\pi_J)v_J$ tends weakly to zero, since its pairing with
  $h$ is bounded by $\|(I-\pi_J)h\|$.
  Compactness supplies a norm-convergent image subsequence; bounded
  linear scalar observables show its limit is zero, a contradiction.
  Lemma~\ref{L:uniform-mean-tensor} transfers this scalar tail norm
  to the Hilbert-valued time map without a dimension factor.

  For fixed $R$, $T_R$ is bounded into the separable compact-operator
  space on $E$. Composition with the actual Bochner field $U\Phi$
  gives the stated mean and its first bound.
  The exact decomposition is
  \[
    Q_{J,K}=(I-\pi_J)\otimes I+\pi_J\otimes(I-P_K).
  \]
  The first term is bounded by $M_0\varepsilon_J$.
  For the second term use the typed intertwining
  \[
    U(\pi_J\otimes(I-P_K))
    =(I_{L^r}\otimes(I-P_K))(C_t\pi_J\otimes I).
  \]
  It holds first on finite tensors, then by continuity.
  Apply~\eqref{E:uniform-mean-frequency} pointwise, followed by
  Lemma~\ref{L:uniform-mean-tensor} for $C_t\pi_J$, whose norm
  is at most $c_t$. This proves~\eqref{E:uniform-completed-mean}.
  Infinite spatial rank is allowed throughout; neither tensor
  compactness nor uniform-radius compactness has been asserted.
  This proves Proposition~\ref{P:uniform-mean-regulator}.
\end{proof}

\subsection{The given-noise block Cameron embedding}

Use $B,\delta,N,s_m,\ell_m,I_m$ and $\theta,r,p$ exactly as in
\eqref{E:cameron-block-parameters} and its preceding block partition.
Let $i_I:H_I\to H_W$ be the isometric closed inclusion.
On the full raw noise space set
\[
  P_{\mathrm{full}}=i_IP_{\mathrm{ret}}i_I^*,\qquad
  Q_{\mathrm{full}}=I-P_{\mathrm{full}} .
\]
These are genuine orthogonal projections on $H_W$.
Define the actual residual fast noise and stopped $E$ driver by
\begin{equation}\label{E:uniform-actual-residual}
  Y_m(f)=W(Q_{\mathrm{full}}T_{\delta,m}f),\qquad
  X_m(u)=g_\delta A_{m_R}(Y_m)(\min(u,\ell_m)),\qquad
  g_\delta=\delta^{(1-a)/2}.
\end{equation}
Here $T_{\delta,m}$ is the literal raw isometry
\eqref{E:raw-block-pullback}, and $A_{m_R}$ takes its $E$ restriction.
Its isometry is proved in Lemma~\ref{L:raw-block-inputs}.
The symbol $H_{\mathrm{fast}}$ below denotes this same original
covariance norm in fast coordinates, carried isometrically into $H_W$.
The $E$ little H\"older space means the zero-start closure of Lipschitz
compact-operator paths in $C^\theta$ norm. Compact operators on separable
$E$ and polygonal approximation make this closure separable.
The last interval can be empty, in which case $X_N=0$.

\begin{proposition}[Uniform-radius actual Cameron bound]
  \label{P:uniform-actual-cameron}
  The tuple $X=(X_m)_{m=0}^N$ is a centered Gaussian variable in
  the separable little H\"older compact-operator path space on $E$.
  Its actual Bochner covariance $Lh=\E[XW(h)]$, $h\in H_W$, is
  \begin{equation}\label{E:uniform-actual-covariance}
    (Lh)_m(u)=\sqrt\delta\int_0^{\min(u,\ell_m)}
    S_E(-v)\mathcal T_R(Q_{J,K}i_I^*h)(s_m+\delta v)
    S_E(v)\ud v .
  \end{equation}
  In the exact norm
  $\|x\|_{\delta,p}=(\delta\sum_m\|x_m\|_{C^\theta}^p)^{1/p}$,
  its actual Cameron embedding has the uniform-radius bound
  \begin{equation}\label{E:uniform-actual-cameron-bound}
    \|Lh\|_{\delta,p}
    \le\sqrt\delta\,C_{B,E}(2/B)^{1/p-1/r}
    [M_0\varepsilon_J+M_fc_tK^{-\beta}]\|h\|_{H_W},
    \qquad C_{B,E}\le18B^{3-1/r}.
  \end{equation}
  All spatial constants are independent of $R\ge1$.
\end{proposition}

\begin{proof}
  Orthogonality and raw pullback isometry give
  $\operatorname{Var}Y_m(f)\le\|f\|_{H_{\mathrm{fast}}}^2$.
  Gaussian transfer, Proposition~\ref{P:source-gaussian-transfer},
  therefore constructs the drivers on the given $W$, with finite
  path moments at each fixed $R,B,\delta,J,K$.
  Choose an admissible H\"older exponent strictly above $\theta$
  as in Lemma~\ref{L:cameron-actual-residual}; constant stopping
  puts the paths in the separable little $C^\theta$ closure.
  Finite-coefficient constructions and their $L^2$ limits show
  that every continuous linear coordinate is in the first chaos
  of the given $W$.

  Every literal observed row, pulled back to slow time, belongs
  to $H_I$. This is the supported-row approximation from
  Lemma~\ref{L:cameron-actual-residual}, also valid before any
  projection; approximate endpoints inside $I$ against the
  integrable time kernel and locally finite spatial covariance.
  For such a row $k$, exact orthogonality gives
  \[
    \langle Q_{\mathrm{full}}T_{\delta,m}k,h\rangle_{H_W}
    =\langle T_{\delta,m}k,i_IQ_{J,K}i_I^*h\rangle_{H_W}.
  \]
  Directions perpendicular to $H_I$ disappear from this pairing.
  Apply the completed $J=0$ identity
  \eqref{E:cameron-actual-covariance} to $Q_{J,K}i_I^*h$,
  and restrict its input and output to $E$.
  The free $F$ group preserves $E$ and restricts to $S_E$;
  the mean restricts to $\mathcal T_R$.
  This proves~\eqref{E:uniform-actual-covariance}.
  Its amplitude is exactly
  $g_\delta\delta^{a/2}=\sqrt\delta$, on the actual noise $W$.
  Arbitrary projected controls are covered by the completed mean
  identity; no smoothness or finite rank of $P_K$ is required.
  Compact operator values and strong continuity of $S_E$ and
  its adjoint make conjugation norm continuous on compact operators,
  as in Proposition~\ref{P:cameron-actual-embedding}.
  Thus the integral is Bochner measurable.
  Fixed-parameter $L^2$ covariance continuity, dense states and
  rational times identify the entire operator path.

  For explicit free constants, the Bessel-unitary Fourier matrix
  of $S_E(v)$ is the matrix displayed in that proposition.
  For $|v|\le B$, $B\ge1$, the upper off-diagonal entry is at most
  $\sqrt2 B$: use $|\sin(vk)|\le Bk$ for $k\le1$ and
  $\langle k\rangle/k\le\sqrt2$ for $k\ge1$.
  The lower entry is at most one, as are both diagonal entries;
  at zero the sine quotient has value $v$.
  Its Frobenius bound is $\sqrt{3+2B^2}\le3B$.
  Hence $G_{B,E}=\sup_{|v|\le B}\|S_E(v)\|\le3B$.
  With
  \[
    \mathcal M_h(t)=\mathcal T_R(Q_{J,K}i_I^*h)(t),\qquad
    t_m=\|\mathcal M_h\|_{L^r(I_m;\mathcal L(E))},
  \]
  the primitive increment bound and the affine time change give
  \[
    \|(Lh)_m\|_{C^\theta}
    \le\sqrt\delta\,C_{B,E}\delta^{-1/r}t_m,\qquad
    C_{B,E}=G_{B,E}^2[B^{1-1/r}+B^{1-1/r-\theta}]
    \le18B^{3-1/r}.
  \]
  Here $1-1/r>\theta$, constant stopping preserves the bound,
  and the empty block contributes zero.

  Put $n=N+1\ge2$. The finite power-mean inequality at exponent
  $r/p>1$ with nonnegative inputs $t_m^p$ gives
  \[
    \left(\sum_m t_m^p\right)^{r/p}
    \le n^{r/p-1}\sum_m t_m^r,\qquad
    \left(\sum_m t_m^p\right)^{1/p}
    \le n^{1/p-1/r}\left(\sum_m t_m^r\right)^{1/r}.
  \]
  Raising nonnegative terms uses only positive powers, including
  when $t_m=0$. The true partition gives
  $\sum_m t_m^r=\|\mathcal M_h\|_{L^r(I)}^r$ and $\delta n\le2/B$.
  The exact $\delta$ weight therefore yields
  \[
    \|Lh\|_{\delta,p}
    \le\sqrt\delta\,C_{B,E}(\delta n)^{1/p-1/r}\|\mathcal M_h\|_{L^r}
    \le\sqrt\delta\,C_{B,E}(2/B)^{1/p-1/r}
    [M_0\varepsilon_J+M_fc_tK^{-\beta}]\|h\|_{H_W}.
  \]

  Finally let $H_{\mathrm{seen}}$ be the closed span in $H_W$
  of all coefficient tests $k_\ell$ with $\ell(X)=W(k_\ell)$.
  The first-chaos Cameron identification in
  Proposition~\ref{P:cameron-actual-embedding} applies on $H_W$:
  $L$ kills $H_{\mathrm{seen}}^\perp$ and its Cameron space is
  $L(H_{\mathrm{seen}})$ with minimum raw preimage norm.
  Thus $\|Lh\|_{\mathrm{CM}}=\|P_{\mathrm{seen}}h\|_{H_W}$.
  Applying the bound to this minimum-norm representative gives
  precisely the actual Cameron embedding bound, without an
  inverse covariance or finite-dimensional density.
  This proves Proposition~\ref{P:uniform-actual-cameron}.
\end{proof}

The orthogonal $P_{\mathrm{full}}$ and $Q_{\mathrm{full}}$ Gaussian
fields are independent; residual time blocks can remain correlated.
The retained spatial head may have infinite rank.
Heat filtering alone would not give this orthogonal decomposition.
These linear bounds do not bound the expected residual path norm
uniformly on growing masks, nor perform conditioning or integration
over the infinite head. The remaining stochastic, product and
original-point upper estimates require their own proofs.

===== END TEX FILE: notes/integrated_uniform_mean.tex =====

===== BEGIN TEX FILE: notes/integrated_radius_anchor.tex =====
\section{Radius-explicit stochastic first-driver bounds}
\label{S:radius-stochastic-anchor}

Retain every original covariance and amplitude in Hypothesis~\ref{H:homog},
with $a=\alpha_0$, and the real phase $E=H^{1/2}\times H^{-1/2}$.
Use the fixed root profile $\eta$ of Section~\ref{S:uniform-mean-regulation}
and physical mask $m_R=\eta(\cdot/R)^2$, $R\ge1$.
In the variance construction the base mask is $\zeta=\eta^2$.
The balanced unitary is
$J_0(u,v)=(\Lambda^{1/2}u,\Lambda^{-1/2}v)$.
Fix a finite horizon $B\ge1$ and parameters
\begin{equation}\label{E:radius-anchor-parameters}
  0<\gamma<\min\left(\frac12,\frac{2-\alpha}{2}\right),\qquad
  \frac12<\theta<\eta_t<\beta_t<
  \min\left(1-\frac a2,\frac{3-a-\alpha}{2}\right).
\end{equation}
The strict subcritical assumptions make these intervals nonempty.
Fix one even integer $Q\ge2$ such that
\begin{equation}\label{E:radius-anchor-Q}
  Q\gamma>d,\qquad
  \beta_t-\eta_t-\frac1Q>0,\qquad
  Q>\frac{2d}{1-a}.
\end{equation}
Such a $Q$ exists because all three lower thresholds are finite.
It stays fixed as $\delta$ tends to zero.
Constants below may depend on the model, $B,Q$, these exponents and the
fixed auxiliary cutoff profiles. They are independent of the spatial
radius, noise-basis truncation, moment index and deterministic residual
projection unless explicitly stated otherwise.

\subsection{Uniform outer factors and the exact whole-space envelope}

Fix real $\chi_0\in C_c^\infty(\R^d)$, equal to one on $B_1$ and
supported in the closed ball of radius two.
Choose real $\psi_0\in C_c^\infty(\R^d)$, equal to one on a
neighbourhood of $\operatorname{supp}\chi_0$ and supported inside $B_3$.
For $\rho\ge1$ put $\chi_\rho(x)=\chi_0(x/\rho)$,
$\psi_\rho(x)=\psi_0(x/\rho)$ and $L=2\pi\rho$.
Since $3<\pi$, both cutoffs are supported strictly inside the cube
of side $L$. The auxiliary torus has unnormalized $L^2(Q_L,\ud x)$,
orthonormal modes $L^{-d/2}e^{ik\cdot x/\rho}$ and Sobolev weights
$\langle k/\rho\rangle^r$.

\begin{lemma}[Uniform rescaled outer maps]\label{L:radius-outer-maps}
  The cutoff periodization and recovery maps from
  Lemma~\ref{L:cutoff-factorization} satisfy, for every real $r$,
  \[
    \|\mathcal P_{\psi_\rho}:H^r(\R^d)\to H^r(\mathbb T_L)\|
    \le C_{\psi_0,r},\qquad
    \|\mathcal E_{\chi_\rho}:H^r(\mathbb T_L)\to H^r(\R^d)\|
    \le C_{\chi_0,r},
  \]
  independently of $\rho\ge1$.
\end{lemma}

\begin{proof}
  The exact weighted Fourier kernels are
  \begin{align*}
    &L^{-d/2}
    \left(\frac{\langle k/\rho\rangle}{\langle\xi\rangle}\right)^r
    \widehat{\psi_\rho}(k/\rho-\xi),\\
    &L^{-d/2}
    \left(\frac{\langle\xi\rangle}{\langle k/\rho\rangle}\right)^r
    \widehat{\chi_\rho}(\xi-k/\rho).
  \end{align*}
  There is no additional $(2\pi)^{-d/2}$: it cancels between
  Fourier inversion and the ordinary integral in the first kernel,
  while the torus normalization gives the second.
  For either base profile $\phi_0$,
  $\widehat{\phi_\rho}(t)=\rho^d\widehat{\phi_0}(\rho t)$.
  Peetre's inequality~\eqref{E:cutoff-peetre}, also for negative $r$,
  and $\langle(\rho\xi-k)/\rho\rangle\le\langle\rho\xi-k\rangle$
  bound the relevant kernel by
  \[
    C_r\rho^{d/2}F_r(k-\rho\xi),\qquad
    F_r(t)=|\widehat{\phi_0}(\pm t)|\langle t\rangle^{|r|}.
  \]
  The nonnegative $F_r$ is integrable and bounded by arbitrarily
  high inverse powers of $\langle t\rangle$.
  At fixed $k$, integration in $\xi$ gives a bound $C\rho^{-d/2}$.
  At fixed $\xi$, summation in $k$ gives $C\rho^{d/2}$:
  translate $\rho\xi$ into a unit lattice cell and sum a power
  tail of order greater than $d$, as in~\eqref{E:cutoff-lattice-sum}.
  This lattice spacing is one and has no remaining $\rho$ dependence.
  The mixed Schur estimate bounds the operator norm by the square
  root of the product of those two quantities. Their radius powers
  cancel. For recovery the row and column roles are reversed.

  Bounded kernel extension from Schwartz functions and torus polynomials
  gives the full Sobolev maps by density.
  Their distributional meanings are the same cutoff maps as in
  Lemma~\ref{L:cutoff-factorization}; no point sampling of a rough
  Fourier function is used. This includes negative indices.
  This proves Lemma~\ref{L:radius-outer-maps}.
\end{proof}

\begin{proposition}[Radius-explicit compact envelopes]
  \label{P:radius-compact-envelopes}
  For real $\sigma$, $\gamma>0$ and $q\ge1$ with $q\gamma>d$,
  \begin{equation}\label{E:radius-cutoff-Schatten}
    \|\Lambda^\sigma\chi_\rho\Lambda^{-\sigma-\gamma}\|_{S_q}
    \le C_{\sigma,\gamma,q,d,\chi_0,\psi_0}\rho^{d/q}.
  \end{equation}
  In the balanced coordinates of~\eqref{E:compact-two-factors},
  \begin{equation}\label{E:radius-two-envelopes}
    \|K_{\rm in}\|_{S_q}=\|K_{\rm out}\|_{S_q}
    \le C_q\rho^{d/q}.
  \end{equation}
\end{proposition}

\begin{proof}
  The exact recovery identity, with $\chi_\rho\psi_\rho=\chi_\rho$,
  gives
  \[
    \Lambda^\sigma\chi_\rho\Lambda^{-\sigma-\gamma}
    =\Lambda^\sigma\mathcal E_{\chi_\rho}\mathcal I_\gamma
    \mathcal P_{\psi_\rho}\Lambda^{-\sigma-\gamma}.
  \]
  Here $\mathcal I_\gamma:H^{\sigma+\gamma}(\mathbb T_L)
  \to H^\sigma(\mathbb T_L)$ has diagonal singular values
  $\langle k/\rho\rangle^{-\gamma}$.
  The outer Bessel maps are unitary on their indicated Sobolev
  domains. The preceding lemma bounds both other outer maps
  uniformly in $\rho$.
  This is an equality on the full whole-space domain by the
  recovery proof and density, including negative $\sigma$.

  Put $u=q\gamma>d$. If $x\in k+[-1/2,1/2]^d$, then
  \[
    \langle x/\rho\rangle
    \le\sqrt2\langle k/\rho\rangle\langle(x-k)/\rho\rangle
    \le c_d'\langle k/\rho\rangle,\qquad
    c_d'=\sqrt{2(1+d/4)}.
  \]
  Integrate over the unit cubes to obtain
  \begin{equation}\label{E:radius-lattice-volume}
    \sum_{k\in\mathbb Z^d}\langle k/\rho\rangle^{-u}
    \le(c_d')^u\rho^d\int_{\R^d}\langle y\rangle^{-u}\ud y
    \le C_{d,u}\rho^d .
  \end{equation}
  The integral is finite: dyadic annuli outside the unit ball
  give a geometric series with terms bounded by $C_d2^{j(d-u)}$.

  Arrange the inclusion's diagonal values in decreasing order
  $(\lambda_j)$. They tend to zero. Retaining its first $j-1$
  coordinates has rank less than $j$ and error $\lambda_j$.
  Compose this approximation with the bounded outer factors.
  The singular-value approximation argument in
  Proposition~\ref{P:cutoff-singular-values} gives
  $s_j\le C_{\chi_0,\sigma}C_{\psi_0,\sigma+\gamma}\lambda_j$.
  Finite-rank approximation also proves compactness.
  Summing $q$th powers and using~\eqref{E:radius-lattice-volume}
  proves~\eqref{E:radius-cutoff-Schatten}.
  No separate Schatten ideal theorem is needed.

  The two blocks of $K_{\rm out}=P_{\chi_\rho}D_\gamma$
  are the whole-space operators with $\sigma=1/2,-1/2$.
  Their $q$th power norms add, proving its bound.
  Proposition~\ref{P:compact-two-envelopes} gives
  $K_{\rm in}=V K_{\rm out}V$ for the unitary coordinate swap
  $V(z_1,z_2)=(z_2,z_1)$, so their norms agree.
  In~\eqref{E:radius-anchor-parameters}, $\gamma<1/2$ and
  $q\gamma>d$ force $q>2d\ge2$; there is no Hilbert--Schmidt
  conclusion. Neither $P_{\chi_\rho}$ nor its adjoint is assumed
  selfadjoint or idempotent.
  This proves Proposition~\ref{P:radius-compact-envelopes}.
\end{proof}

\subsection{The actual driver and covariance contractions}

Write $M_R(W)=A_{m_R}(W)$ for the actual zero-start $E$ interaction
driver on $[0,B]$ from Proposition~\ref{P:actual-operator-driver}.
The phase remains the whole-space $E$ throughout.

\begin{proposition}[Radius-explicit actual path moments]
  \label{P:radius-actual-moments}
  Under~\eqref{E:radius-anchor-parameters}--\eqref{E:radius-anchor-Q},
  for every finite $v\ge1$,
  \begin{equation}\label{E:radius-actual-path-moments}
    \|M_R(W)\|_{L^v(C^\theta([0,B];\mathcal L(E)))}
    \le C_{Q,B}\sqrt v\,R^{d/Q},\qquad R\ge1.
  \end{equation}
  The constant does not depend on $v$ or $R$.
  This is an $E$ first-driver estimate; the two constant columns on $F$
  require their own estimates. Any later projection used in a Cameron
  comparison must also satisfy its actual orthogonality and covariance
  hypotheses.
\end{proposition}

\begin{proof}
  Use the given raw smooth-test basis from
  Lemma~\ref{L:driver-noise-basis}, $g_j=W(f_j)$, and its
  actual finite paths $M_N=\sum_{j\le N}g_jA_j$.
  These are the same given-noise coefficient paths as in
  Lemma~\ref{L:driver-holder-limit}, not source approximations.
  Choose
  \[
    \rho=2R+B+2\le(B+4)R,\qquad \chi=\chi_0(\cdot/\rho).
  \]
  The plateau covers $B_{2R+B+1}$.
  Thus both literal localization identities
  \eqref{E:driver-actual-localization} hold for this envelope.
  The physical noise mask remains $m_R$.
  Both envelopes $K_{\rm in},K_{\rm out}$ here use this same $\chi_\rho$.

  For an interval $I\subset[0,B]$ of length $0<h\le1$,
  Proposition~\ref{P:wave-two-variances} and
  Lemma~\ref{L:driver-actual-variances} give both finite weighted
  variances with budget $V_{B,\mathrm{var}}h^{2-a}B_\alpha(h)$,
  uniformly in $R,N,I$.
  In particular, the base mask is the same fixed $\eta^2$
  required by that variance theorem. Corollary~\ref{C:finite-gaussian-operators},
  applied in the balanced coordinates, gives for every even $q\ge Q$
  \[
    \|M_N(I)\|_{L^q(S_q)}
    \le\sqrt{q-1}\sqrt{V_{B,\mathrm{var}}}\,
    h^{1-a/2}B_\alpha(h)^{1/2}\|K_{\rm out}\|_{S_q},
  \]
  where $B_\alpha(h)$ is $1$, $1+\log(1/h)$ or $h^{1-\alpha}$
  according as $\alpha<1$, $\alpha=1$ or $\alpha>1$.
  Both actual variances and both localizations have been checked;
  individual basis-dependent coefficient bounds are not summed.

  For $q\ge Q$, the unnormalized Schatten norms obey
  $\|K_{\rm out}\|_{S_q}\le\|K_{\rm out}\|_{S_Q}$.
  Indeed, normalize a nonzero singular-value sequence by its
  $\ell^Q$ norm; each entry is at most one, so its $q$th power
  sum is at most its $Q$th power sum. The zero case is immediate.
  Apply~\eqref{E:radius-two-envelopes} only at the fixed index $Q$.
  Use $\|A\|\le\|A\|_{S_q}$ and $\sqrt{q-1}\le\sqrt q$.
  The balanced Hilbert complexification has the same operator norm
  as its real restriction, and
  $\rho^{d/Q}\le(B+4)^{d/Q}R^{d/Q}$.
  Since $\beta_t$ is strictly below the corresponding short-time
  power, it follows that
  \begin{equation}\label{E:radius-finite-increment}
    \|M_N(t)-M_N(u)\|_{L^q(\mathcal L(E))}
    \le C_{Q,B}\sqrt q\,R^{d/Q}|t-u|^{\beta_t},
    \qquad |t-u|\le1.
  \end{equation}
  At $\alpha=1$, the factor $\sqrt{1+\log(1/h)}$ is absorbed
  by the strict gap $1-a/2-\beta_t>0$.
  For $\alpha>1$, the power is $(3-a-\alpha)/2$.
  These power/log constants are independent of $R,N,q$.
  Longer increments are finite sums of increments of length at
  most one, with constants depending only on the fixed $B$.

  Let $D_n(F)$ be the largest adjacent increment on the grid
  $kB2^{-n}$ of $[0,B]$.
  For fine levels $B2^{-n}\le1$, the finite-maximum bound gives
  \[
    \|D_n(M_N)\|_{L^q}
    \le2^{n/q}C_{Q,B}\sqrt q\,R^{d/Q}(B2^{-n})^{\beta_t}.
  \]
  No independence of increments is used. The sum after multiplication
  by $2^{n\eta_t}$ converges uniformly for even $q\ge Q$, because
  its geometric ratio is at most
  $2^{-(\beta_t-\eta_t-1/Q)}<1$.
  The finitely many coarse levels are controlled by unit partitions.
  The deterministic dyadic chaining argument in
  Lemma~\ref{L:driver-holder-limit} therefore bounds the
  $L^qC^{\eta_t}$ norms by $C_{Q,B}\sqrt q\,R^{d/Q}$.
  Each finite path is continuous and starts at zero, as required there.
  The fixed-horizon embedding $C^{\eta_t}\hookrightarrow C^\theta$
  gives the same estimate in $C^\theta$.

  For each fixed $R$, Lemma~\ref{L:driver-holder-limit} identifies
  $M_R(W)$ as the all-finite-moment $C^\theta$ limit of these
  very $M_N$. Pass the uniform finite-$N$ estimate to this limit.
  Uniform convergence in $R$ is unnecessary: the limiting bound has
  its explicit radius dependence at every $R$.
  For arbitrary $v\ge1$, choose an even $q\ge\max(v,Q)$ with
  $q\le v+Q+2\le(Q+3)v$.
  Lyapunov's inequality gives~\eqref{E:radius-actual-path-moments},
  absorbing $\sqrt{Q+3}$ into the fixed constant.
  This proves Proposition~\ref{P:radius-actual-moments}.
\end{proof}

\begin{corollary}[Actual deterministic covariance residuals]
  \label{C:radius-covariance-residuals}
  Let $Y$ be a centered Gaussian linear noise on the actual coupled
  space, with $\operatorname{Var}Y(f)\le C\|f\|_{H_W}^2$, $C\ge0$.
  Its actual transferred driver satisfies
  \[
    \|M_R(Y)\|_{L^v(C^\theta)}
    \le\sqrt C\,C_{Q,B}\sqrt v\,R^{d/Q}.
  \]
  In particular this holds with $C=1$ for
  $Y_m(f)=W((I-\Pi)T_{\delta,m}f)$, for any deterministic
  orthogonal projection $\Pi$ on the slow $H_W$.
  Its rank may be infinite and it may depend on $\delta,R$.
\end{corollary}

\begin{proof}
  Proposition~\ref{P:source-gaussian-transfer} is a linear Gaussian
  covariance contraction theorem for this same physical mask and
  these same deterministic coefficient maps.
  It bounds the path norm by $\sqrt C$ times the reference
  isonormal driver norm. The reference has the canonical first-driver
  law used in Proposition~\ref{P:radius-actual-moments}; the actual
  $Y$ is not replaced in this comparison. The zero case gives zero
  directly. This proves the first assertion.
  For the second, the actual raw isometry
  \eqref{E:raw-block-pullback}, proved in Lemma~\ref{L:raw-block-inputs},
  and $\|I-\Pi\|\le1$ give
  $\operatorname{Var}Y_m(f)\le\|f\|_{H_W}^2$,
  where the right side is the original raw norm in fast coordinates.
  The joint residuals retain the given slow $W$ and may be correlated.
  They need not lie in the span of an individual fast noise,
  which is not a hypothesis of Gaussian transfer.
  No random noise-dependent projection is used.
  This proves Corollary~\ref{C:radius-covariance-residuals}.
\end{proof}

\subsection{The growing-radius expected-norm anchor}

\begin{proposition}[Actual averaged block mean tends to zero]
  \label{P:radius-mean-anchor}
  Fix integer $B\ge1$ and use the true block partition $B,\delta,N,\ell_m$ of
  Section~\ref{S:actual-cameron-mean}, with
  $0<\delta<\min(1,1/B)$ and $N=\lfloor1/(\delta B)\rfloor$.
  For $Y_m$ as in Corollary~\ref{C:radius-covariance-residuals},
  put
  \[
    X_m(u)=g_\delta M_R(Y_m)(\min(u,\ell_m)),\qquad
    Z_\delta=\left(\delta\sum_{m=0}^N
    \|X_m\|_{C^\theta}^p\right)^{1/p},\qquad
    g_\delta=\delta^{(1-a)/2},
  \]
  for any fixed $p\ge1$. Then
  \begin{equation}\label{E:radius-mean-anchor}
    \E Z_\delta\le(2/B)^{1/p}C_{Q,B}\sqrt p\,
    g_\delta R^{d/Q}.
  \end{equation}
  In particular, for $R_\delta=\delta^{-1}+2$,
  \begin{equation}\label{E:radius-mean-anchor-decay}
    2\E Z_\delta
    \le2(2/B)^{1/p}C_{Q,B}\sqrt p\,3^{d/Q}
    \delta^{e_{\rm anchor}}\longrightarrow0,\qquad
    e_{\rm anchor}=\frac{1-a}{2}-\frac dQ>0 .
  \end{equation}
  Both bounds are uniform in the deterministic orthogonal projection.
\end{proposition}

\begin{proof}
  Stopping a zero-start interaction primitive and extending it
  constantly to $B$ does not increase its supremum or H\"older
  seminorm. An empty last interval gives the zero path.
  Probability normalization and Lyapunov give
  \begin{align*}
    \E Z_\delta
    &\le(\E Z_\delta^p)^{1/p}
    =\left(\delta\sum_{m=0}^N
    \E\|X_m\|_{C^\theta}^p\right)^{1/p}\\
    &\le[\delta(N+1)]^{1/p}g_\delta
    C_{Q,B}\sqrt p\,R^{d/Q}.
  \end{align*}
  This is linearity for a finite sum; no time-block independence
  or maximum over blocks is used.
  Since $\delta B<1$, we have $N\ge1$ and
  $N+1\le2/(\delta B)$, proving~\eqref{E:radius-mean-anchor}.

  Now $R_\delta\le3/\delta$ because $\delta<1$.
  The last condition in~\eqref{E:radius-anchor-Q} is equivalent to
  $Q(1-a)>2d$. Dividing by $2Q>0$ gives
  $e_{\rm anchor}>0$.
  Substitute this radius into~\eqref{E:radius-mean-anchor}
  to obtain~\eqref{E:radius-mean-anchor-decay}.
  The estimate holds at each fixed $B,p,Q$ and model, uniformly
  in every deterministic residual projection.
  This proves Proposition~\ref{P:radius-mean-anchor}.
\end{proof}

These bounds concern the expected first-driver norm on $E$.
They do not give an $F$ estimate with constant initial-data columns.
The radius substitution is numerical; cone coverage and source-to-point
transfer require their separate arguments.
No concentration, infinite-head Gaussian integration or nonlinear moment
upper bound follows from this section alone.
The constants need not be uniform as $Q,B$ tend to infinity or as model
parameters approach an endpoint. For zero covariance, the actual drivers
and stochastic bounds vanish directly.

===== END TEX FILE: notes/integrated_radius_anchor.tex =====

===== BEGIN TEX FILE: notes/integrated_signed_static.tex =====
\section{Signed rough static potentials and the physical wave}
\label{S:signed-static-wave}

Fix the original nonzero covariance and a finite physical mask $m_R$
as in Section~\ref{S:actual-cameron-mean}.
For real $q\in C_c^\infty(\R^d)$ put
$V_q=m_R(\Gamma*q)$ and
$L_q(u,v,c_1,c_2)=(0,V_q(u+c_1),0,0)$ on $F=E\oplus\R^2$.
Let $\mathcal V_R$ be the operator-norm closure of these operators
in $\mathcal K(F)$. It is a closed real linear space.
No positivity is imposed on $q$.

\begin{lemma}[The actual limiting multiplier]\label{L:signed-limiting-multiplier}
  Every $L\in\mathcal V_R$ determines a unique real
  $V\in H^{-1/2}$ supported in $\operatorname{supp}m_R$.
  It has the actual multiplier action
  $L(u,v,c_1,c_2)=(0,Vu+c_1V,0,0)$, where multiplication
  extends from tests to $H^{1/2}\to H^{-1/2}$.
  For $k=\|L\|$, its symmetric pairing obeys
  \begin{equation}\label{E:signed-multiplier-form}
    |v_V(u,w)|\le k\|u\|_{H^{1/2}}\|w\|_{H^{1/2}} .
  \end{equation}
\end{lemma}

\begin{proof}
  Choose $L_{q_n}\to L$. The constant-displacement vector has
  norm one, so $\|V_{q_n}-V_{q_j}\|_{H^{-1/2}}\le\|L_{q_n}-L_{q_j}\|$.
  Thus, $V_{q_n}\to V$ in $H^{-1/2}$.
  Testing outside the fixed compact mask support preserves that support.
  Every zero column of $L_{q_n}$ remains zero.
  Its displacement multipliers converge in
  $\mathcal L(H^{1/2},H^{-1/2})$ to a map of norm at most $k$.
  For compact smooth $u$, smooth multiplication is bounded on
  $H^{-1/2}$ by Lemma~\ref{L:cutoff-factorization}.
  Hence, $V_{q_n}u\to Vu$ there, identifying the limiting map
  on tests and then uniquely on $H^{1/2}$ by density.
  The constant column recovers $V$ and proves uniqueness.
  On compact smooth $u,w$, the pairing is $\langle V,uw\rangle$,
  denoted $v_V(u,w)$, so it is symmetric. Its bound and symmetry extend by density.
  Complexification preserves the operator norm by splitting real
  and imaginary parts in the Hilbert norms. The pairing extends
  sesquilinearly to a Hermitian form; its diagonal is the sum of
  the real and imaginary diagonal values.
  This proves Lemma~\ref{L:signed-limiting-multiplier}.
\end{proof}

\begin{proposition}[Closed form and quarter-power phase]
  \label{P:signed-closed-form}
  Let $K\ge\max(1,\|L\|)$ and $c=2+K^2$.
  On complexified $L^2$ the form
  \[
    q_V(u)=\|\nabla u\|_2^2-v_V(u,u),\qquad Q(q_V)=H^1,
  \]
  represents a unique self-adjoint $H_V$.
  With $A=H_V+c$ and $L_K=3(1+K^2)$,
  \begin{align}
    A&\ge1,\qquad D(A^{1/2})=H^1,\label{E:signed-form-domain}\\
    \tfrac12\|u\|_{H^1}^2
    &\le q_V(u)+c\|u\|_2^2\le L_K\|u\|_{H^1}^2,\label{E:signed-form-bounds}\\
    D(A^{1/4})&=H^{1/2},\qquad
    2^{-1/4}\|u\|_{H^{1/2}}
    \le\|A^{1/4}u\|_2\le L_K^{1/4}\|u\|_{H^{1/2}}.
    \label{E:signed-quarter-phase}
  \end{align}
  The negative dual completion is $H^{-1/2}$.
  No $H^2$ operator domain is asserted.
\end{proposition}

\begin{proof}
  Put $b=\|u\|_2$, $z=\|u\|_{H^1}$.
  Fourier Cauchy--Schwarz and~\eqref{E:signed-multiplier-form} give
  \[
    \|u\|_{H^{1/2}}^2\le bz,\qquad
    |v_V(u,u)|\le Kbz\le\tfrac12z^2+\tfrac12K^2b^2 .
  \]
  The last scalar inequality is the weighted arithmetic--geometric
  mean inequality at weights $1/2,1/2$ and nonnegative bases
  $z^2,(Kb)^2$, including zero norms.
  Since $q_V=z^2-b^2-v_V(u,u)$, it follows that
  \[
    q_V+cb^2\ge\tfrac12z^2+(1+K^2/2)b^2,\qquad
    q_V+cb^2\le\tfrac32z^2+(1+3K^2/2)b^2\le L_Kz^2.
  \]
  The lower bound dominates both $z^2/2$ and $b^2$.
  Thus, this densely defined Hermitian form is semibounded
  and its shifted norm is equivalent to the complete $H^1$ norm.
  It is closed in the definition of~\cite{teschl:14:mathematical}*{p.~80}.
  From~\cite{teschl:14:mathematical}*{Theorem~2.14, p.~81, (2.63)},
  it represents a unique self-adjoint $H_V$.
  This representation is independent of the admissible shift.
  From that book's Theorem~3.6 and~(3.51)--(3.53), p.~109,
  applied after shifting, we obtain~\eqref{E:signed-form-domain}.
  Here $A\ge1$ is initially its form lower bound.
  A bounded spectral slice below one would produce a unit
  $D(A)$ test contradicting that form bound; hence it is also
  the spectral lower bound. Lemma~\ref{L:signed-spectral-wave}
  records the full bottom argument.

  Set $B_0=1-\Delta$. On the common form domain,
  $\tfrac12B_0\le A\le L_KB_0$.
  We prove the needed square-root comparison rather than assuming
  an order rule for arbitrary operator powers.
  For $T_0,S_0\ge1$ with common form domain and $q_{T_0}\le q_{S_0}$,
  completing the square in the shifted form norm gives
  \[
    \langle f,(T_0+t)^{-1}f\rangle
    =\sup_u\{2\operatorname{Re}\langle f,u\rangle
    -q_{T_0}(u)-t\|u\|^2\}
    \ge\langle f,(S_0+t)^{-1}f\rangle,\quad t>0 .
  \]
  The scalar identity
  $\sqrt x=\pi^{-1}\int_0^\infty t^{-1/2}x/(x+t)\ud t$
  follows by $t=xv^2$.
  Positive spectral integration and Tonelli now imply
  $T_0^{1/2}\le S_0^{1/2}$ as forms, with their domain inclusions:
  $I-t(T_0+t)^{-1}\le I-t(S_0+t)^{-1}$.
  Apply this to $(B_0,2A)$ and $(A,L_KB_0)$.
  Both operators in each pair are at least one.
  The resulting inequalities give~\eqref{E:signed-quarter-phase},
  including equality of its domains.
  For $v\in L^2$ the $L^2$-duality norm against
  $\|A^{1/4}u\|_2$ is $\|A^{-1/4}v\|_2$:
  Cauchy--Schwarz gives the upper bound, and $u=A^{-1/2}v$
  gives equality after normalization.
  Duality and completion therefore identify the negative phase.
  Uniqueness of the form, resolvent and spectral calculus makes
  these constructions commute with real conjugation.
  This proves Proposition~\ref{P:signed-closed-form}.
\end{proof}

\begin{lemma}[The actual bottom and spectral wave]\label{L:signed-spectral-wave}
  Write $P_V^E$ for the evolution in~\eqref{E:signed-spectral-matrix},
  and $S_E$ for the free restriction from Lemma~\ref{L:constant-phase-free}.
  Put
  \[
    \beta(V)=\inf_{\substack{u\in H^1\\\|u\|_2=1}}q_V(u),
    \qquad \lambda(V)=\sqrt{-\beta(V)} .
  \]
  Then $\beta(V)=\inf\operatorname{spec}H_V$ and
  $-K^2\le\beta(V)\le0$.
  The spectral wave on $E$ has the bound
  \begin{equation}\label{E:signed-E-wave}
    \|P_V^E(t)\|\le8(1+K)^2(1+t)e^{\lambda(V)t},\qquad t\ge0.
  \end{equation}
\end{lemma}

\begin{proof}
  For unit $u$, $z=\|u\|_{H^1}\ge1$ gives
  $q_V(u)\ge z^2/2-1-K^2/2\ge-(1+K^2)/2\ge-K^2$.
  Conversely dilate a unit compact smooth bump and translate its
  whole support outside $\operatorname{supp}m_R$.
  Its potential pairing is zero and its kinetic energy tends to zero.
  Thus, $\beta\le0$. Real and complex form infima agree because
  a complex diagonal splits into the two real diagonals.
  The spectral form formula in~\cite{teschl:14:mathematical}*{(3.52)--(3.53)}
  identifies this form infimum with the spectral bottom.
  For clarity, a bounded spectral slice below the form lower bound
  would give a unit form test violating that bound.
  Conversely the form integral is bounded below by the spectral infimum.
  The spectrum is nonempty: a unit vector's scalar spectral measure
  has mass one and a support point, and normalized projections onto
  arbitrarily small bounded neighborhoods give approximate eigenvectors,
  excluding a bounded inverse there.
  Conversely, off the closed PVM support $\Sigma$ the Borel function
  $(h-z)^{-1}$, set to zero off $\Sigma$, is bounded for real
  $z\notin\Sigma$, as is $h/(h-z)$ on $\Sigma$.
  Its calculus maps into $D(H_V)$ and is a two-sided resolvent inverse
  on the appropriate domains. Thus the spectrum is precisely $\Sigma$.
  Hence, $\lambda\le K$ and every spectral value $h$ has $h+c\ge2$.

  Use the phase norm
  $\|(u,v)\|_{E_A}^2=\|A^{1/4}u\|_2^2+\|A^{-1/4}v\|_2^2$.
  With $M_K=L_K^{1/4}$, the preceding proposition and its dual give
  $M_K^{-1}\|z\|_E\le\|z\|_{E_A}\le M_K\|z\|_E$.
  The condition-number cost is
  $M_K^2=\sqrt{3(1+K^2)}\le2(1+K)$.
  Define $C_t(h),S_t(h)$ by
  $\cos(t\sqrt h),\sin(t\sqrt h)/\sqrt h$ for $h>0$,
  by $1,t$ at zero, and by
  $\cosh(t\sqrt{-h}),\sinh(t\sqrt{-h})/\sqrt{-h}$ for $h<0$.
  In the $E_A$ isometry the wave matrix is
  \begin{equation}\label{E:signed-spectral-matrix}
    \begin{pmatrix}
      C_t(h)&\sqrt{h+c}\,S_t(h)\\
      -hS_t(h)/\sqrt{h+c}&C_t(h)
    \end{pmatrix}.
  \end{equation}
  For $h\ge0$, the entries are bounded using
  $|C_t|\le1$, $|S_t|\le\min(t,h^{-1/2})$,
  $\sqrt{h+c}|S_t|\le1+\sqrt c\,t$ and
  $|hS_t|/\sqrt{h+c}\le1$; at zero the off-diagonals are
  $\sqrt c\,t,0$.
  For $\beta\le h<0$, they are bounded using
  $|C_t|\le e^{\lambda t}$, $|S_t|\le te^{\lambda t}$,
  $\sqrt{h+c}|S_t|\le\sqrt c\,te^{\lambda t}$ and
  $|hS_t|/\sqrt{h+c}\le Ke^{\lambda t}$.
  There is no division by $\lambda$.
  Since $\sqrt c\le2K$, each entry is at most
  $2(1+K)(1+t)e^{\lambda t}$.
  Bounded Borel calculus from~\cite{teschl:14:mathematical}*{Theorem~3.1,
  pp.~102--103, (3.18)--(3.21)}, the two-by-two matrix norm
  bound and the condition-number cost give~\eqref{E:signed-E-wave}.
  Functions can be set to zero off the spectral support.
  Spectral dominated convergence gives strong continuity, and
  scalar addition identities give the group property.
  The same matrix and bounds apply on the weighted graph levels
  $D(A^{1/2})\times L^2$ and $D(A)\times D(A^{1/2})$.
  Spectral cutoffs justify their extensions and continuity there.
  This proves Lemma~\ref{L:signed-spectral-wave}.
\end{proof}

\begin{proposition}[Identification with the actual physical wave]
  \label{P:signed-physical-wave}
  The spectral wave in Lemma~\ref{L:signed-spectral-wave} is the
  actual bounded-perturbation, equivalently Young, physical wave on $E$.
  Its actual extension on $F$ satisfies
  \begin{equation}\label{E:signed-F-wave}
    \|P_V(t)\|_{\mathcal L(F)}
    \le16(1+K)^4(1+t)^3e^{\lambda(V)t},\qquad t\ge0.
  \end{equation}
  Both constant response columns are included.
\end{proposition}

\begin{proof}
  The imported form representation
  \cite{teschl:14:mathematical}*{Theorem~2.14, p.~81, (2.63)},
  tested against compact smooth functions,
  gives $H_Vu=-\Delta u-Vu$ in distributions for $u\in D(H_V)$.
  Such $u$ lies in $H^1$ and $Vu\in H^{-1/2}$.
  Consequently $(1-\Delta)u=H_Vu+Vu+u\in H^{-1/2}$,
  so $D(H_V)\hookrightarrow H^{3/2}$.
  The embedding is graph-continuous: by~\eqref{E:signed-form-bounds},
  $\|u\|_{H^1}^2\le2\langle Au,u\rangle
  \le\|Au\|_2^2+\|u\|_2^2$, and the distributional equation
  bounds the $H^{3/2}$ norm by this graph norm.

  The generator of the free $E$ group is
  $A_0(u,v)=(v,\Delta u)$ on $H^{3/2}\times H^{1/2}$.
  Indeed, differentiate its Fourier matrix after a frequency cutoff,
  dominate by that graph norm and remove the cutoff.
  Conversely any strong generator derivative has those distributional
  components; they require $v\in H^{1/2}$ and
  $\Delta u\in H^{-1/2}$, hence $u\in H^{3/2}$.
  No operator-norm differentiability of the group is used.

  Start spectral data in $D(A)\times D(A^{1/2})=D(H_V)\times H^1$.
  The preceding graph-level estimates give continuous graph trajectories
  and $C^1$ trajectories in $H^1\times L^2$, with
  $u_t=v$, $v_t=-H_Vu$.
  This follows first on bounded spectral cutoffs and then uniformly
  on finite horizons in the graph norms by spectral dominated
  convergence and~\cite{teschl:14:mathematical}*{Theorem~3.2, p.~104,
  (3.29)--(3.33)}. The projections $1_{[1,n]}(A)$ approximate
  every graph datum and the same weighted matrix bounds control
  all cutoff tails on those horizons.
  Graph embedding gives continuity in $D(A_0)$ and
  $z_t=A_0z+L_Ez$ in $E$, where $L_E=L|_E$.
  The strong-group chain rule on this domain yields
  \[
    S_E(-t)z(t)=z(0)+\int_0^t S_E(-s)L_Ez(s)\ud s .
  \]
  Graph data are dense in $E$: spectral cutoffs make $D(A)$
  dense in $D(A^{1/2})=H^1$, and $H^1$ is dense in both
  $H^{1/2}$ and $H^{-1/2}$.
  Boundedness on finite horizons extends this identity to all $E$.
  Volterra uniqueness by Picard iteration identifies the physical wave.
  No $D(A^{3/4})=H^{3/2}$ assertion is needed.

  On $F$, bounded $L$ and strongly continuous $S_F$ similarly
  define a unique Duhamel flow. On $[0,T]$, the $n$th Volterra
  term has bound $C_T^{n+1}\|L\|^nT^n/n!$.
  Uniqueness makes horizons consistent and gives composition.
  Its interaction primitive is
  $\int_0^t S_F(-s)LS_F(s)\ud s$.
  Compactness of $L$, and strong continuity of the group and
  its adjoint, give norm-continuity of the conjugated compact operator,
  as in Proposition~\ref{P:cameron-actual-embedding}.
  Thus, this primitive is Lipschitz and its ordinary equation is
  exactly the actual Young equation.

  For initial $(e,c_1,c_2)$ the constant coordinates are
  $(c_1+tc_2,c_2)$ and the $E$ component is
  \[
    P_V^E(t)e+\int_0^t P_V^E(t-s)(0,V(c_1+sc_2))\ud s .
  \]
  The bounded $E$-valued Fubini argument proving
  \eqref{E:compact-F-block} applies: substitute the $E$ Duhamel
  formula under this integral and interchange the absolutely
  bounded finite time triangle. It solves the full system,
  and uniqueness identifies it. No ground positivity or gap is used.
  The forcing norm is at most $K(1+s)|(c_1,c_2)|$.
  Since $\lambda\ge0$ and
  $\int_0^t(1+t-s)(1+s)\ud s\le(1+t)^3$, the full norm is at most
  \[
    (1+t)^3e^{\lambda t}
    \{8(1+K)^2\|e\|+[8K(1+K)^2+1]|(c_1,c_2)|\}.
  \]
  Scalar Cauchy--Schwarz and $\sqrt{8^2+9^2}<13$ bound this
  by $13(1+K)^3(1+t)^3e^{\lambda t}\|(e,c_1,c_2)\|_F$.
  This implies the stated sufficient bound.
  This proves Proposition~\ref{P:signed-physical-wave}.
\end{proof}

===== END TEX FILE: notes/integrated_signed_static.tex =====

===== BEGIN TEX FILE: notes/integrated_symplectic_phase.tex =====
\section{The actual symplectic phase and block-mean baseline}
\label{S:actual-symplectic-phase}

Retain the original model, covariance amplitude, physical mask $m_R$
and real $E=H^{1/2}\times H^{-1/2}$.
Fix finite $R,T>0$ and admissible exponents as in
\eqref{E:driver-parameters}.
Let $M=M_R(W)$ be the given-noise first interaction path on $E$,
and $M^\rho$ its retaining-source paths from
Proposition~\ref{P:source-gaussian-transfer} and the source construction.
Here $\rho$ is the positive heat/Laplace smoothing pair.
The retaining construction and ordinary rows are those of
Lemma~\ref{L:source-retaining-isometry},
Lemma~\ref{L:source-pointfield-regularity} and
Proposition~\ref{P:source-ordinary-response}.
The full $F$ driver and Young evolution are fixed by
Proposition~\ref{P:constant-phase-driver} and
Proposition~\ref{P:constant-young-linear}; their actual $E$ restrictions
are used here. Complexifications commute with conjugation, so these
real restrictions are the physical phases.
For fixed $\Phi$ in the full positive-time raw $H_W$ and real $c$ set
\begin{equation}\label{E:symplectic-combined-driver}
  \begin{aligned}
    Z&=W(\Phi),\qquad D_\Phi=\E[ZM],\qquad
    D_\Phi^\rho=\E[ZM^\rho],\\
    D&=cM+D_\Phi,\qquad D^\rho=cM^\rho+D_\Phi^\rho .
  \end{aligned}
\end{equation}
All these are actual operator paths on $E$.
The covariance mean is not a pointwise raw potential.
Write $U_D$ for left Young evolution and
$P_D(t,s)=S_E(t)U_D(t,s)S_E(-s)$.

\begin{lemma}[Free wave form and compact Young baseline]
  \label{L:symplectic-free}
  There is a bounded isometric skew-adjoint $J_E$ on $E$,
  with $J_E^2=-I$, such that
  \[
    \omega(z,w)=\langle z,J_Ew\rangle_E
    =\langle u,g\rangle_{H^{1/2},H^{-1/2}}
    -\langle f,v\rangle_{H^{1/2},H^{-1/2}},
    \quad z=(u,v),\quad w=(f,g).
  \]
  The actual free group preserves $\omega$.
  For bounded real smooth $b$, the force $B(b)(u,v)=(0,bu)$
  obeys $\omega(B(b)z,w)+\omega(z,B(b)w)=0$.

  Let $1/2<\theta<1$ and let
  $X\in C^\theta([0,T];\mathcal K(E))$ start at zero, with
  $U_X$ its left Young evolution. Then
  \begin{equation}\label{E:symplectic-compact-young-baseline}
    U_X(t,s)-I\in\mathcal K(E),\qquad
    \|S_E(t)U_X(t,s)S_E(-s)\|
    \ge\|S_E(t-s)\|\ge1,\qquad 0\le s\le t\le T .
  \end{equation}
  More generally, for finitely many such zero-start paths $X_j$
  on $[0,B]$ and lengths $0\le\ell_j\le B$, put
  $P_j=S_E(\ell_j)U_{X_j}(\ell_j,0)$. Then
  \begin{equation}\label{E:symplectic-compact-product-baseline}
    P_N\cdots P_0-S_E\Big(\sum_{j=0}^N\ell_j\Big)\in\mathcal K(E),
    \qquad
    \|P_N\cdots P_0\|
    \ge\left\|S_E\Big(\sum_{j=0}^N\ell_j\Big)\right\|\ge1 .
  \end{equation}
  These norm bounds require neither Gaussian nor Hamiltonian drivers.
\end{lemma}

\begin{proof}
  The balanced map $C_{\rm bal}(u,v)=(\Lambda^{1/2}u,\Lambda^{-1/2}v)$
  is an onto real isometry to $L^2\times L^2$.
  Define $J_{\rm symp}(q,p)=(p,-q)$ and
  $J_E=C_{\rm bal}^{-1}J_{\rm symp}C_{\rm bal}$.
  This gives all stated operator properties and
  $J_E(f,g)=(\Lambda^{-1}g,-\Lambda f)$.
  The two displayed dualities follow from the balanced $L^2$ pairing.
  No $L^2$ pairing of a general distributional velocity is taken.

  In balanced Fourier coordinates, the free matrix is
  \[
    W_t(\xi)=
    \begin{pmatrix}
      \cos(tk)&\langle\xi\rangle\sin(tk)/k\\
      -k\sin(tk)/\langle\xi\rangle&\cos(tk)
    \end{pmatrix},\qquad k=|\xi|.
  \]
  At zero it is $\left(\begin{smallmatrix}1&t\\0&1\end{smallmatrix}\right)$,
  by the continuous sine quotient.
  Direct matrix multiplication gives
  $W_t^{\mathsf T}J_{\rm symp}W_t=J_{\rm symp}$, since its
  determinant is $\cos^2(tk)+\sin^2(tk)=1$, also at zero.
  The entries are real, even and bounded on finite time horizons.
  Integrating the identity against real-phase Fourier vectors
  with Hermitian symmetry is legitimate by $L^2$ Cauchy--Schwarz.
  It gives $\omega(S_E(t)z,S_E(t)w)=\omega(z,w)$ on all $E$.
  Equivalently one may first use Schwartz phases and then density.
  No rough generator derivative or frequency-zero trace is used.

  Finally $\|bu\|_{H^{-1/2}}\le\|bu\|_2
  \le\|b\|_\infty\|u\|_{H^{1/2}}$.
  Actual duality for these $L^2$ functions gives the absolutely
  integrable cancellation $-\int fbu+\int ubf=0$.
  This is skewness for $\omega$, not for the $E$ Hilbert inner product.
  The Young construction of
  Proposition~\ref{P:constant-young-linear} applies on
  $\mathcal L(E)$: its proof uses completeness and operator
  multiplication of norm one, exactly as on $\mathcal L(F)$.
  For fixed $s,t$, each left Young sum
  \[
    \sum_j\big(X(t_{j+1})-X(t_j)\big)U_X(t_j,s)
  \]
  is compact. The sums converge in operator norm to
  $U_X(t,s)-I$, so closedness of the compact ideal gives the first
  assertion in~\eqref{E:symplectic-compact-young-baseline}.
  Bounded composition then shows that the physical endpoint differs
  from $S_E(t-s)$ by a compact operator.

  We prove the required compact-perturbation bound for this actual
  whole-space phase. Translations $\tau_y$ on both entries are
  isometries on $E$ and commute with $S_E(h)$.
  For fixed $z,w\in E$, their translated pairing is the Fourier
  transform of an $L^1$ function: the two weighted Fourier products
  are integrable by Cauchy--Schwarz in the Bessel norms.
  Approximation of that function in $L^1$ by compact smooth
  functions, followed by integration by parts for the approximants,
  proves $\langle\tau_yz,w\rangle_E\to0$ as $|y|\to\infty$.
  Thus $\tau_yz$ tends weakly to zero. For compact $K$,
  $\|K\tau_yz\|\to0$: otherwise compactness supplies a
  norm-convergent subsequence with nonzero norm, while bounded
  linear testing makes its limit zero. For unit $z$ it follows that
  \[
    \|S_E(h)+K\|
    \ge\liminf_{|y|\to\infty}\|(S_E(h)+K)\tau_yz\|
    \ge\|S_E(h)z\|.
  \]
  Taking the supremum over $z$ gives
  $\|S_E(h)+K\|\ge\|S_E(h)\|$.
  The isometric velocity reversal $\mathcal R(u,v)=(u,-v)$
  satisfies $S_E(-h)=\mathcal R S_E(h)\mathcal R$ by the full
  free Fourier matrix. The group law yields
  $1\le\|S_E(-h)\|\|S_E(h)\|=\|S_E(h)\|^2$.
  This proves~\eqref{E:symplectic-compact-young-baseline}.

  Finally $P_j-S_E(\ell_j)$ is compact. Telescoping the finite
  ordered product against its free product gives a finite sum of
  bounded--compact--bounded products, hence a compact difference.
  Only the free factors are combined by the group law; no noisy
  factors are commuted. The same translation argument proves
  \eqref{E:symplectic-compact-product-baseline}.
  A zero length gives $P_j=I$. All assertions are at fixed finite
  horizons and products; no uniform compact approximation in a
  radius, horizon or number of factors is asserted.
  This proves Lemma~\ref{L:symplectic-free}.
\end{proof}

\begin{lemma}[Actual covariance means and source primitives]
  \label{L:symplectic-source-mean}
  The expectations in~\eqref{E:symplectic-combined-driver} are
  Bochner defined and
  \begin{equation}\label{E:symplectic-mean-convergence}
    \|D_\Phi^\rho-D_\Phi\|_{C^\theta}
    \le\|\Phi\|_{H_W}\|M^\rho-M\|_{L^2C^\theta}\longrightarrow0 .
  \end{equation}
  For each positive $\rho$, there is a deterministic real
  time-continuous, spatially smooth $h_\Phi^\rho$ such that
  \begin{equation}\label{E:symplectic-source-primitive}
    D_\Phi^\rho(t)
    =\int_0^t S_E(-r)B(m_Rh_\Phi^\rho(r))S_E(r)\ud r .
  \end{equation}
  This is the actual statewise primitive and defines a Lipschitz
  operator path. The combined source coefficient is
  $b^\rho=m_R(cY^\rho+h_\Phi^\rho)$.
\end{lemma}

\begin{proof}
  Separable Gaussian path moments give
  $\E\|ZM\|_{C^\theta}\le\|\Phi\|_{H_W}\|M\|_{L^2C^\theta}$,
  and the same holds for sources.
  Bochner Cauchy--Schwarz gives~\eqref{E:symplectic-mean-convergence}.
  Covariance contraction also gives the uniform source bound
  $\|D_\Phi^\rho\|_{C^\theta}
  \le\|\Phi\|_{H_W}\|M\|_{L^2C^\theta}$.

  The retaining construction has an isometry
  $j_{\rm src}:H_W\to\mathcal G$ and an isonormal process
  $\mathcal I$ with $\mathcal I(j_{\rm src}h)=W(h)$.
  Its actual source pointfield is $Y^\rho(t,x)=\mathcal I(v_{\rho;t,x})$,
  with continuous $\mathcal G$-valued spatial derivatives at positive widths.
  Consequently
  \[
    h_\Phi^\rho(t,x)=\E[W(\Phi)Y^\rho(t,x)]
    =\langle j_{\rm src}\Phi,v_{\rho;t,x}\rangle_{\mathcal G}
  \]
  has the claimed regularity. Bounded linear testing commutes
  with those derivatives. After multiplication by $m_R$ the
  coefficient has one compact support and bounded derivatives on $[0,T]$.

  On Schwartz states, the row of the right side of
  \eqref{E:symplectic-source-primitive} is the integral of
  $h_\Phi^\rho$ against the literal masked source wave product.
  Ordinary Fubini is justified by
  $\E|ZY^\rho(t,x)|\le\|\Phi\|_{H_W}
  \sqrt{\E|Y^\rho(t,x)|^2}$ and bounded point variance
  on this fixed compact set at positive widths.
  The source test and indicator approximation extends this to
  the actual completed rows by Gaussian Cauchy--Schwarz and
  covariance contraction. Hence, this row is the row of
  $\E[ZM^\rho(t)]$.
  Countable dense states and rational times, then continuity,
  identify the operator path.
  The uniformly bounded integrand gives its Lipschitz bound.
  This identifies the combined source coefficient exactly.
  The combined source is generally noncentered and the mask occurs once.
  This proves Lemma~\ref{L:symplectic-source-mean}.
\end{proof}

\begin{proposition}[Actual source conservation]\label{P:symplectic-source}
  At each fixed positive $\rho$, on one probability-one set for
  the fixed $c,\Phi,R,T$, the physical source flow satisfies
  \[
    P_{D^\rho}(t,s)^*J_EP_{D^\rho}(t,s)=J_E,
    \qquad 0\le s\le t\le T .
  \]
\end{proposition}

\begin{proof}
  Intersect the source coefficient regularity event with the
  event identifying its actual first primitive with the ordinary
  primitive for all times and states.
  The source construction supplies both at this fixed $\rho$.
  On their intersection $b^\rho$ has a common compact support,
  is continuous in supremum norm and is uniformly bounded on $[0,T]$.
  Thus,
  $C_b(r)=S_E(-r)B(b^\rho(r))S_E(r)$ is uniformly bounded
  and strongly continuous on states.
  Lemma~\ref{L:symplectic-free} gives
  $\omega(C_b(r)z,w)+\omega(z,C_b(r)w)=0$ for all $r,z,w$.

  The actual source and mean primitive identities identify the
  Young state equation with
  $U(t,s)e=e+\int_s^t C_b(r)U(r,s)e\ud r$.
  Indeed, replace each driver increment in a Young sum by its
  statewise integral. The error is bounded by the uniform coefficient
  bound times the uniform continuity error of $U$ on the partition.
  Each state trajectory is therefore $C^1$, with derivative
  $C_b(t)U(t,s)e$, by the strong-integral difference quotient.
  Differentiating the bounded bilinear form
  $\omega(U(t,s)e,U(t,s)f)$ gives zero.
  This holds on the same path set for all states and time pairs,
  since the bounded ordinary evolution is defined there on all $E$.
  Free conjugation gives the displayed physical identity.
  No uncountable intersection of state-dependent null sets or
  derivative of the free generator on a rough state was used.
  This proves Proposition~\ref{P:symplectic-source}.
\end{proof}

\begin{proposition}[Raw conservation, inverse and norm baseline]
  \label{P:symplectic-raw}
  For the fixed parameters in~\eqref{E:symplectic-combined-driver},
  on one probability-one set,
  \begin{equation}\label{E:symplectic-raw-conservation}
    P_D(t,s)^*J_EP_D(t,s)=J_E,\qquad
    \|P_D(t,s)\|\ge1,\qquad 0\le s\le t\le T .
  \end{equation}
  The flow is invertible. For $c=0$ these assertions are deterministic
  for every fixed $\Phi$.
\end{proposition}

\begin{proof}
  We first identify a closed real linear constraint on the actual driver.
  Write
  \[
    \mathfrak g_J=\{A\in\mathcal L(E):A^*J_E+J_EA=0\}.
  \]
  The coefficient $H_{j,R}$ in
  \eqref{E:driver-covariance-coefficient} is real and smooth.
  Free conservation gives $S_E(-r)^*J_E=J_ES_E(r)$ and
  $J_ES_E(-r)=S_E(r)^*J_E$.
  Lemma~\ref{L:symplectic-free} therefore makes
  $S_E(-r)B(H_{j,R}(r))S_E(r)$ belong to $\mathfrak g_J$.
  Testing the statewise integral in
  \eqref{E:driver-coefficient-operator} against two states shows
  $A_j(0,t)\in\mathfrak g_J$ for every $j,t$.
  No operator-norm derivative of the free group is taken.
  The real finite sums in~\eqref{E:driver-path-convergence} obey
  the same constraint. The map $A\mapsto A^*J_E+J_EA$ is bounded
  on the path space, so their $L^2C^\theta$ limit $M$ obeys it
  at all times on one probability-one path set.

  The mean is a Bochner expectation since
  $\E\|W(\Phi)M\|_{C^\theta}
  \le\|\Phi\|_{H_W}\|M\|_{L^2C^\theta}<\infty$.
  Bounded real linear maps commute with this expectation, hence
  $D_\Phi(t)\in\mathfrak g_J$ for every $t$.
  Thus, $D=cM+D_\Phi$ starts at zero and is a $C^\theta$ path
  in $\mathfrak g_J$ on that path set. Complex Gaussian
  coefficients are not used. All these variables remain on the given $W$.

  The proof of Proposition~\ref{P:constant-young-linear} applies
  on $\mathcal L(E)$, with multiplication of norm one.
  Fix any $s$ and put $V(r)=U_D(r,s)$ for $r\ge s$.
  The Young remainder on $[u,v]\subset[s,T]$ gives
  \[
    V(v)-V(u)=D_{u,v}V(u)+R_{u,v},\qquad
    \|R_{u,v}\|\le C|v-u|^{2\theta}.
  \]
  The exact increment of $V^*J_EV$ has first-order term
  $V(u)^*(D_{u,v}^*J_E+J_ED_{u,v})V(u)=0$.
  Its remaining terms have norm at most $C'|v-u|^{2\theta}$,
  using the bounded $C^\theta$ norm of $V$.
  Their sum on a partition is at most
  $C'(t-s)\operatorname{mesh}^{2\theta-1}$, which tends to zero.
  Therefore $U_D(t,s)^*J_EU_D(t,s)=J_E$.
  This deterministic argument applies to every time pair on the same
  driver path; it requires no state-dependent null sets.
  Free conservation in Lemma~\ref{L:symplectic-free} gives
  \eqref{E:symplectic-raw-conservation}, including
  $1=\|J_E\|\le\|P_D(t,s)\|^2$.

  Invertibility comes from the local Young Neumann pieces and
  their finite products, followed by the free inverse; it is not
  inferred from conservation in infinite dimension.
  For $c=0$ the path and the argument are deterministic for each $\Phi$.
  Zero covariance gives the free flow directly. At each fixed $\delta$
  one may take the given reference $W\circ T_{\delta,0}$,
  $R=\delta^{-1}+2$, $T=\delta^{-1}$, $c=g_\delta$ and $\Phi=0$.
  No uniform-radius or control-budget assertion follows.
  This proves Proposition~\ref{P:symplectic-raw}.
\end{proof}

\begin{proposition}[The exact completed block mean]\label{P:symplectic-block-mean}
  Use the true partition $B,\delta,N,s_m,\ell_m$ of
  Section~\ref{S:actual-cameron-mean}, with integer $B\ge1$.
  Let $i_I:H_I\to H_W$ be the supported closed inclusion and
  $T_m=T_{\delta,m}:H_{\rm fast}\to H_W$ the actual raw isometry;
  $H_{\rm fast}$ has the same original covariance in fast coordinates.
  For $\Phi\in H_I$ set
  \[
    W_m(f)=W(T_mf),\qquad
    \phi_m=\delta^{-a/2}T_m^*i_I\Phi,\qquad
    \mathcal T_E\Phi=i^*T\Phi\,i ,
  \]
  where $T$ is the actual full $F$ mean of
  Proposition~\ref{P:cameron-full-mean}.
  Define
  \begin{equation}\label{E:symplectic-block-primitive}
    H_{m,E}(\Phi)(u)=\int_0^{\min(u,\ell_m)}
    S_E(-v)\mathcal T_E\Phi(s_m+\delta v)S_E(v)\ud v .
  \end{equation}
  With $M_m=M_R(W_m)$ and
  $D_{\phi_m}(u)=\E[M_m(u)W_m(\phi_m)]$, one has
  \begin{equation}\label{E:symplectic-block-direction}
    D_{\phi_m}(\min(u,\ell_m))=H_{m,E}(\Phi)(u),\qquad 0\le u\le B .
  \end{equation}
  Consequently the actual pure-mean endpoint obeys
  \[
    \|S_E(\ell_m)U_{H_{m,E}(\Phi)}(\ell_m,0)\|\ge1 .
  \]
\end{proposition}

\begin{proof}
  The raw pullback~\eqref{E:raw-block-pullback} has covariance
  factor $\delta^{a-2}\delta^2\delta^{-a}=1$, hence respects
  nulls and extends isometrically from fast to slow raw space.
  Its Hilbert adjoint is a contraction.
  Thus, $\|\phi_m\|\le\delta^{-a/2}\|\Phi\|$ is finite
  at fixed $\delta$, without a uniform control-radius assertion.
  The actual fast noise remains on the same given $W$.
  For applying the preceding propositions, construct retaining
  sources with $W_m$ as the given reference, extending by an
  independent auxiliary source while retaining all base variables.
  No slow-source pullback is presumed; the raw covariance direction
  is independent of the auxiliary realization.

  The mean $T\Phi$ has range in closed $iE$.
  By Proposition~\ref{P:cameron-full-mean}, bounded compression
  passes its strong measurability, $L^r$ bound and compact operator
  values to $\mathcal T_E\Phi\in L^r(I;\mathcal K(E))$.
  Choose the full parameter package~\eqref{E:cameron-block-parameters}.
  Its intervals are nonempty because $\theta<1-a/2$ and
  $\theta>1/2$; $p$ only instantiates that package here.
  The compact-conjugation argument makes
  \eqref{E:symplectic-block-primitive} a Bochner integral, and
  the $L^r$ primitive estimate gives $C^\theta$, since
  $1-1/r>\theta$. Affine pullback preserves null sets.
  Its integrand is compact valued almost everywhere; closedness of
  $\mathcal K(E)$ under Bochner integration makes $H_{m,E}(\Phi)$
  a zero-start compact-valued path, also after constant stopping.

  Here $A_{F,m}$ is the full $F$ interaction driver from
  Proposition~\ref{P:constant-phase-driver}, and $H_{m,F}$
  is its stopped completed mean primitive in
  \eqref{E:cameron-actual-covariance}.
  The completed identity~\eqref{E:cameron-actual-covariance}
  at raw projection rank zero gives, for $0\le u\le\ell_m$,
  \[
    \E[g_\delta A_{F,m}(u)W(i_I\Phi)]
    =\sqrt\delta\,H_{m,F}(\Phi)(u).
  \]
  Compress through $i$ using the actual driver intertwining,
  $S_Fi=iS_E$, and the mean range in $iE$ preserved by $S_F$.
  Bochner expectation commutes with this bounded compression.
  The constant columns are retained in the full $F$ driver and mean
  until this compression; they are inactive only on the $iE$ inputs.
  Since $g_\delta\delta^{a/2}=\sqrt\delta$ and $g_\delta>0$,
  division gives the unscaled covariance
  \begin{equation}\label{E:symplectic-unscaled-covariance}
    \E[M_m(u)W(i_I\Phi)]
    =\delta^{a/2}H_{m,E}(\Phi)(u),\qquad u\le\ell_m .
  \end{equation}
  The factor here is $\delta^{a/2}$, not $\sqrt\delta$.
  Completion in the earlier covariance identity permits every
  $\Phi\in H_I$, without positivity or smoothness.

  The operator $T_mT_m^*$ is the orthogonal projection onto
  the raw isometry's closed range. Thus,
  $W((I-T_mT_m^*)i_I\Phi)$ is orthogonal to the entire fast
  first chaos. Every continuous linear coordinate of $M_m$
  is an $L^2$ limit of finite $W_m$-basis sums.
  Its covariance with this difference vanishes.
  Bochner covariance exists by $L^2$ path moments, and bounded
  linear functionals separate its values. Hence,
  \[
    \E[M_m(u)W(i_I\Phi)]
    =\E[M_m(u)W_m(T_m^*i_I\Phi)] .
  \]
  Multiply by $\delta^{-a/2}$ and use
  \eqref{E:symplectic-unscaled-covariance} to obtain
  \eqref{E:symplectic-block-direction} on $[0,\ell_m]$,
  then stop both sides. No unstopped equality beyond $\ell_m$
  is asserted.

  Apply Lemma~\ref{L:symplectic-free} directly to the zero-start
  compact-valued path $H_{m,E}(\Phi)$ on $[0,B]$.
  Its actual physical endpoint has norm at least
  $\|S_E(\ell_m)\|\ge1$.
  If $\ell_m=0$, the endpoint is the identity and its norm is one.
  The radius may be chosen $\delta^{-1}+2$ after fixing $\delta$;
  all identities are fixed-parameter instances.
  This proves Proposition~\ref{P:symplectic-block-mean}.
\end{proof}

For zero covariance the drivers and covariance means vanish, and the
claims reduce directly to the free identity in Lemma~\ref{L:symplectic-free}.
These results give a norm baseline and its exact completed mean
application. They provide no uniform control-radius budget, stochastic
moment upper bound or nonlinear product ratio by themselves.

===== END TEX FILE: notes/integrated_symplectic_phase.tex =====

===== BEGIN TEX FILE: notes/integrated_gaussian_tubes.tex =====
\section{Actual Gaussian control tubes and Rayleigh transfer}
\label{S:actual-gaussian-tubes}

We first state the Gaussian geometry with its exact covariance scale.
Let $H$ be real separable Hilbert, $W$ its given isonormal process,
and $X$ a strongly measurable centered Gaussian variable in a real
separable Banach space $\mathscr B$, with $\E\|X\|^2<\infty$.
Assume every continuous linear coordinate has the form
$\ell(X)=W(k_\ell)$, $k_\ell\in H$.
Fix $0<\delta<1$ and write
\begin{equation}\label{E:tube-covariance-scale}
  Ch=\E[XW(h)]=\sqrt\delta\,\mathcal M_\delta h,\qquad
  H_{\rm seen}=\overline{\operatorname{span}\{k_\ell\}},\qquad
  E_0=\overline{C(H)} .
\end{equation}
Assume $\mathcal M_\delta:H\to\mathscr B$ is compact.
All Hilbert balls below are closed.

\subsection{The genuine Wiener realization}

\begin{proposition}[First-chaos realization on the actual support]
  \label{P:tube-wiener-realization}
  The variable $X$ lies in $E_0$ almost surely, with a centered
  Radon Gaussian law of full support there.
  Its genuine Cameron space and norm are
  \begin{equation}\label{E:tube-cameron-space}
    H_{\rm CM}=C(H_{\rm seen}),\qquad
    \|Ch\|_{\rm CM}=\|P_{\rm seen}h\|_H .
  \end{equation}
  This support triple is an abstract Wiener realization, including
  the measurable-norm condition.
\end{proposition}

\begin{proof}
  The zero law has $C=0$ and $E_0=\{0\}$ and is immediate.
  A countable norming family exists in $\mathscr B^*$:
  choose a dense sequence on the unit sphere and apply Hahn--Banach
  at each point. Approximation gives
  $\|x\|=\sup_j|\ell_j(x)|$.
  Norms of differences from a countable dense set show that these
  coordinates generate the Borel sets.
  Consequently $X$ is measurable in the completion of $\sigma(W(H))$.
  Fix an orthonormal basis $(e_j)$ of $H$ and set
  $\mathcal G_j=\sigma(W(e_1),\ldots,W(e_j))$.
  In finite dimension these sums and projections stabilize at the dimension.
  Bochner conditional expectations need no Radon--Nikodym property here:
  define them first on finite-valued simple variables using scalar
  conditional expectations, then extend by the $L^2$ norm contraction.
  Simple approximation supplies their scalar testing identities.
  Gaussian regression and the countable norming family give
  \begin{equation}\label{E:tube-finite-regression}
    X_j=\E[X\mid\mathcal G_j]
    =\sum_{l\le j}W(e_l)Ce_l,\qquad X_j\longrightarrow X
    \quad\hbox{in }L^2(\mathscr B).
  \end{equation}
  To justify convergence, finite-coordinate scalar events approximate
  all events in the generated sigma field: the class of events whose
  indicators are approximable in $L^2$ is a monotone class containing
  the finite-coordinate algebra. Approximate a Bochner variable by
  simple variables and use the conditional $L^2$ contraction.

  Bounded testing gives $\ell(Ch)=\langle k_\ell,h\rangle$.
  Thus, $\ker C=H_{\rm seen}^\perp$, and $C$ is injective on
  $H_{\rm seen}$. The closed first chaos generated by $X$ is
  exactly $W(H_{\rm seen})$.
  Its covariance image therefore has the first-chaos norm
  in~\eqref{E:tube-cameron-space}; unused directions are removed
  by the orthogonal projection, without an inverse covariance.
  This is the genuine Cameron image under the first-chaos definition.
  The finite sums in~\eqref{E:tube-finite-regression} lie in
  $E_0$, so $L^2$ convergence and an almost-sure subsequence
  put $X$ in that closed space almost surely.
  Functionals on $E_0$ extend to $\mathscr B$ by Hahn--Banach,
  so restriction preserves the scalar laws and first chaos.

  Its law is tight. For each radius $2^{-j}$ choose a finite union
  of balls of mass greater than $1-\varepsilon2^{-j-1}$,
  using a countable cover of the separable space.
  The intersection of the corresponding finite closed unions
  is closed and totally bounded and has mass at least $1-\varepsilon$.
  Completeness makes it compact.
  Metric Borel regularity on these compact sets, followed by tightness,
  gives a Radon law.
  To prove full support, the tail $X-X_j$ is independent of the
  finite Gaussian head: every tail coordinate has label
  $(I-P_j)k_\ell$, orthogonal to $e_1,\ldots,e_j$.
  Joint Gaussianity and countable Borel coordinates give Banach
  tail independence.
  Given $h$ and $\varepsilon>0$, choose $j$ with
  $\|CP_jh-Ch\|<\varepsilon/3$ and
  $\mathbb P(\|X-X_j\|<\varepsilon/3)>0$.
  The finite head has positive probability in every ball about
  $CP_jh$, even if its covariance is singular:
  the preimage under its finite linear map contains an open ball
  about the coefficient vector of $P_jh$.
  Independence proves positivity of every ball about $Ch$.
  Closure proves that the support is all of $E_0$.

  We check the measurable norm explicitly.
  In $H_{\rm seen}$ put $V_j=\operatorname{span}\{P_{\rm seen}e_l:l\le j\}$.
  Any finite orthonormal family $(h_k)$ in $V_j^\perp$
  is also orthogonal to $e_1,\ldots,e_j$.
  The same regression and Bochner Jensen argument gives
  \[
    \E[X-X_j\mid W(h_k),\hbox{ all }k]
    =\sum_k W(h_k)Ch_k,\qquad
    \E\left\|\sum_kW(h_k)Ch_k\right\|^2
    \le\E\|X-X_j\|^2 .
  \]
  For any $\varepsilon>0$ choose $j$ so that the right side
  is less than $\varepsilon^3$.
  Markov bounds the probability that this finite sum has norm
  exceeding $\varepsilon$ by $\varepsilon$, uniformly over every
  such finite orthonormal family.
  Since $C:H_{\rm seen}\to H_{\rm CM}$ is isometric, the excluded
  finite-dimensional Cameron subspace is $C(V_j)$.
  This is the measurable-norm tail condition for the dense Hilbert
  image, whose Banach completion is $E_0$.
  The characteristic functional of the law is
  $\E e^{i\ell(X)}=\exp(-\|k_\ell\|_H^2/2)$.
  These facts give the stated actual abstract Wiener realization.
  The zero space has the direct zero-law interpretation.
  This proves Proposition~\ref{P:tube-wiener-realization}.
\end{proof}

\subsection{Closed tubes and exact half-action geometry}

We import the set-enlargement theorem
\cite{friz.hairer:20:course}*{Theorem~11.6, p.~190},
with footnote~3 on p.~190; p.~191 supplies the following context.
For an abstract Wiener space, a Borel $A$ of positive mass and
its Cameron unit ball $\mathcal K$, it states
\[
  \mu((A+t\mathcal K)^c)
  \le\overline\Phi_{\rm N}(\widehat a+t),\qquad
  \widehat a=\Phi_{\rm N}^{-1}(\mu(A)),\quad t\ge0 .
\]
Here $\Phi_{\rm N}$ is the standard normal distribution function;
the same page gives $\overline\Phi_{\rm N}(y)\le e^{-y^2/2}$
for $y\ge0$. This theorem is imported, not proved here.
It concerns Gaussian input sets, not Gaussianity of a nonlinear wave.
We verify Borel measurability of every enlargement we use.

\begin{lemma}[Compact images and attained tube radii]
  \label{L:tube-closed-geometry}
  Suppose the law of $X$ is nonzero and put
  \[
    b_\delta=2\E\|X\|,\qquad
    A_\delta=\{x\in E_0:\|x\|\le b_\delta\},\qquad
    \mathcal T_r=A_\delta+\mathcal M_\delta(\overline B_H(r)).
  \]
  Every $\mathcal T_r$ is closed.
  The extended distance
  $d_\delta(x)=\inf\{r\ge0:x\in\mathcal T_r\}$ satisfies
  \begin{equation}\label{E:tube-attained-radius}
    \{d_\delta\le r\}=\mathcal T_r,\qquad
    \mathbb P(d_\delta(X)>r)\le e^{-r^2/(2\delta)},\quad r\ge0 .
  \end{equation}
  In particular, $d_\delta$ is lower semicontinuous and finite almost surely.
\end{lemma}

\begin{proof}
  A compact map from a separable Hilbert space sends a closed bounded
  ball to a compact set, including closedness of the image.
  Indeed, diagonal orthonormal coordinates and Fatou give a weakly
  convergent subsequence of any bounded sequence, with limit still
  in the ball. Compactness gives norm-convergent image subsequences,
  and bounded scalar testing identifies every limit with the image
  of that weak limit. This proves sequential compactness.
  Closed $A_\delta$ plus a compact image is closed: along a converging
  sequence of sums, extract the compact component and pass the
  residual into the closed base set.

  Membership in $\mathcal T_r$ implies $d_\delta\le r$.
  Conversely, if $d_\delta(x)\le r$, choose $h_j$ with
  $\|h_j\|\le r+1/j$ and $x-\mathcal M_\delta h_j\in A_\delta$.
  A weak subsequence has limit $h$ of norm at most $r$;
  compactness gives $\mathcal M_\delta h_j\to\mathcal M_\delta h$.
  Closedness of the residual proves membership in $\mathcal T_r$.
  This also covers $r=0$ and proves least finite-radius attainment.
  Closed sublevels give lower semicontinuity and Borel measurability.

  The nonzero law has $b_\delta>0$, and Markov gives
  $\mu(A_\delta)\ge1/2$.
  Projection onto $H_{\rm seen}$ removes all unused raw directions,
  so~\eqref{E:tube-cameron-space} gives the exact set identities
  \[
    \mathcal K=C(\overline B_H(1))
    =\sqrt\delta\,\mathcal M_\delta(\overline B_H(1)),\qquad
    \mathcal T_r=A_\delta+(r/\sqrt\delta)\mathcal K .
  \]
  These are Borel enlargements by the preceding closedness.
  The imported theorem applies to the genuine realization in
  Proposition~\ref{P:tube-wiener-realization}.
  Since $\widehat a\ge0$, it yields~\eqref{E:tube-attained-radius}.
  The value $\widehat a=+\infty$ is allowed when $\mu(A_\delta)=1$.
  The tail tends to zero, proving almost-sure finiteness.
  No Cameron embedding constant changes the half action.
  This proves Lemma~\ref{L:tube-closed-geometry}.
\end{proof}

\begin{proposition}[Rayleigh transfer including jumps and zero law]
  \label{P:tube-rayleigh-transfer}
  Let $F:E_0\to\R$ be Borel and let $G:[0,\infty)\to\R$
  be Borel and nondecreasing.
  If $F(x)\le G(r)$ for every $x\in\mathcal T_r$ and every $r\ge0$,
  then
  \begin{equation}\label{E:tube-rayleigh-transfer}
    \E e^{F(X)/\delta}
    \le\int_0^\infty\frac r\delta
    \exp\left(\frac{G(r)-r^2/2}{\delta}\right)\ud r .
  \end{equation}
  For zero law use $E_0=\{0\}$, $C=\mathcal M_\delta=0$;
  the same conclusion holds when $F(0)\le G(0)$.
\end{proposition}

\begin{proof}
  The auxiliary Rayleigh variable $\mathcal R_\delta$ with density
  $(r/\delta)e^{-r^2/(2\delta)}$, $r>0$, has mass one and
  survival function $e^{-r^2/(2\delta)}$ by direct integration.
  It is a scalar stochastic dominator, not a raw-Hilbert Gaussian norm.
  For every level $t\ge0$, the upper level set of $e^{G(r)/\delta}$
  is an upper interval, possibly empty or the whole halfline.
  An open endpoint is controlled by~\eqref{E:tube-attained-radius}.
  At a positive closed endpoint $c$, let $s\uparrow c$:
  \[
    \mathbb P(d_\delta(X)\ge c)
    =\lim_{s\uparrow c}\mathbb P(d_\delta(X)>s)
    \le e^{-c^2/(2\delta)}
    =\mathbb P(\mathcal R_\delta\ge c).
  \]
  Rayleigh has no atoms, and at the closed endpoint zero both
  probability bounds are one.
  On the null event $\{d_\delta(X)=\infty\}$ define
  $e^{G(d_\delta(X))/\delta}$ to be one. No value of $G$ at infinity
  is needed and no expectation changes.
  Layer cake and Tonelli therefore order the expectations of
  $e^{G(d_\delta(X))/\delta}$ and $e^{G(\mathcal R_\delta)/\delta}$,
  even when $G$ jumps or expectations are infinite.
  Least-radius attainment gives $F(X)\le G(d_\delta(X))$
  almost surely. No measurable selection of a control or residual is needed.
  This proves~\eqref{E:tube-rayleigh-transfer}.
  For zero law, $X=0$ and $F(0)\le G(0)\le G(r)$;
  normalization of the Rayleigh density proves the claim directly.
  In particular, $F(0)$ need not be zero.
  This proves Proposition~\ref{P:tube-rayleigh-transfer}.
\end{proof}

\subsection{The actual wave tuple and its globally defined endpoint}

Retain all original covariances and amplitudes.
Use the exponents and fixed even $Q$ in
\eqref{E:radius-anchor-parameters}--\eqref{E:radius-anchor-Q};
put $\nu=1/\theta$ and choose
$(1-\theta)^{-1}<r_t<2/a$, $\nu\le p<2<r_t$.
All these intervals are nonempty by the strict subcritical assumptions.
Fix integer $B\ge1$ and the true partition
$\delta,N,s_m,\ell_m$ from Section~\ref{S:actual-cameron-mean}.
Set $L_\delta=\delta^{-1}$ and eventually $R_\delta=L_\delta+2$.
On the same given slow $W$ define the full, unprojected input
\begin{equation}\label{E:tube-actual-input}
  W_m(f)=W(T_{\delta,m}f),\qquad
  X_m(u)=g_\delta M_R(W_m)(\min(u,\ell_m)),\qquad
  g_\delta=\delta^{(1-a)/2}.
\end{equation}
Write $P_{\delta,E}^R$ for the actual physical $E$ flow driven by
$g_\delta M_R(W\circ T_{\delta,0})$ on the global fast horizon $[0,L_\delta]$.
Let $\mathscr B_\delta$ be the finite product of zero-start
little $C^\theta([0,B];\mathcal K(E))$ spaces, with exact norm
\[
  \|x\|_{\delta,p}=\left(\delta\sum_{m=0}^N
  \|x_m\|_{C^\theta}^p\right)^{1/p}.
\]

\begin{proposition}[Eligibility of the actual E law]
  \label{P:tube-actual-law}
  The tuple $X_\delta=(X_m)$ satisfies the preceding Gaussian
  hypotheses with $H=H_I$ and
  \begin{align}
    (\mathcal M_\delta\Phi)_m(u)
    &=\int_0^{\min(u,\ell_m)}
    S_E(-v)\mathcal T_R\Phi(s_m+\delta v)S_E(v)\ud v,
    \label{E:tube-actual-mean}\\
    \E[X_\delta W(\Phi)]&=\sqrt\delta\,\mathcal M_\delta\Phi .
    \label{E:tube-actual-covariance}
  \end{align}
  Its actual support is
  $E_{0,\delta}=\overline{C_\delta(H_I)}\subset\mathscr B_\delta$,
  where $C_\delta\Phi=\E[X_\delta W(\Phi)]
  =\sqrt\delta\,\mathcal M_\delta\Phi$.
  The actual map $\mathcal M_\delta$ is compact at each fixed radius
  and parameters. At $R=R_\delta$,
  \begin{equation}\label{E:tube-typical-radius}
    b_\delta=2\E\|X_\delta\|_{\delta,p}
    \le C_{Q,B,p}\delta^{(1-a)/2-d/Q}\longrightarrow0 .
  \end{equation}
\end{proposition}

\begin{proof}
  Compact operators on separable Hilbert $E$ form a separable
  operator-norm space: finite-rank rational matrices in an
  orthonormal basis are dense.
  Polygonal paths give separability of the little H\"older closure.
  The actual construction is a $C^\theta$ limit of zero-start
  Lipschitz finite coefficient paths; stopping at $\ell_m$
  and extending constantly preserves this space and gives zero
  for an empty final interval.
  Gaussian transfer retains the given $W$ for all finitely many blocks.
  Every finite collection of linear statistics is an $L^2$ limit
  of joint first-chaos Gaussians, hence jointly centered Gaussian.
  The finite tuple has finite $L^2$ norm by the fixed-parameter
  path moments in Corollary~\ref{C:radius-covariance-residuals}.
  The raw Hilbert space $H_I$ is separable by
  Lemma~\ref{L:cameron-supported-tensor}.
  No separability of all $\mathcal L(E)$ or full $C^\theta$ is claimed.

  The actual $E$ mean field $\mathcal T_R$ is the compression
  of Proposition~\ref{P:cameron-full-mean}; it is compact into
  $L^{r_t}(I;\mathcal K(E))$ at fixed $R$.
  Proposition~\ref{P:uniform-mean-regulator} gives
  $\|\mathcal T_R\|\le C_{\rm mean}=M_0\|C_t\|$ independently of $R\ge1$.
  Compact conjugation, affine time pullback and
  $1-1/r_t>\theta$ make the primitive in
  \eqref{E:tube-actual-mean} bounded from that field space to
  $\mathscr B_\delta$, with constant stopping.
  Composition proves compactness of $\mathcal M_\delta$.
  There is no uniform-radius compactness assertion.

  The rank-zero identity~\eqref{E:cameron-actual-covariance},
  compressed to $E$ as in Proposition~\ref{P:symplectic-block-mean},
  gives~\eqref{E:tube-actual-covariance}.
  Its scale is exactly $g_\delta\delta^{a/2}=\sqrt\delta$.
  Every stopped row's slow pullback lies in $H_I$ by the
  inside-$I$ endpoint approximation of Lemma~\ref{L:cameron-actual-residual}.
  Countable matrix coordinates and rational times identify the
  tuple in the closed first chaos $W(H_I)$, so every linear
  statistic has its label there.
  Equivalently, apply that lemma at $J=0$ on $F$ and compose
  any $E$-tuple statistic with the bounded $E$-compression.
  This is actual same-$W$ covariance, without a block-independence
  assumption or a raw time-indicator multiplier.
  Proposition~\ref{P:tube-wiener-realization} therefore applies
  to this exact law on its support.
  Finally Proposition~\ref{P:radius-mean-anchor}, with zero
  residual projection, gives~\eqref{E:tube-typical-radius}.
  The third fixed-$Q$ guard $Q>2d/(1-a)$ makes this exponent positive;
  the first two supply the path moments and chaining.
  Fast directions used for the symplectic baseline do not replace
  this global $H_I$ action or get summed as separate costs.
  Zero covariance gives zero drivers and means directly.
  This proves Proposition~\ref{P:tube-actual-law}.
\end{proof}

\begin{lemma}[The actual endpoint functional]\label{L:tube-actual-endpoint}
  For every $x\in\mathscr B_\delta$ define
  \[
    \begin{aligned}
      P_m(x_m)&=S_E(\ell_m)U_{x_m}(\ell_m,0),\qquad
      \mathcal P_\delta(x)=P_N(x_N)\cdots P_0(x_0),\\
      F_\delta(x)&=2\delta\log\max(1,\|\mathcal P_\delta(x)\|).
    \end{aligned}
  \]
  This is a finite continuous functional on all tuples.
  For the actual input it satisfies
  \begin{equation}\label{E:tube-global-endpoint}
    \mathcal P_\delta(X_\delta)
    =P_{\delta,E}^R(L_\delta,0),\qquad
    e^{F_\delta(X_\delta)/\delta}
    =\|P_{\delta,E}^R(L_\delta,0)\|^2 .
  \end{equation}
  These are almost-sure identities for each fixed admissible
  $\delta,R,B$, without a simultaneous event over all parameter choices.
\end{lemma}

\begin{proof}
  Generic Young evolution is globally defined and locally Lipschitz
  in every $C^\theta$ driver. Finite products, fixed-time free
  factors, norm and $\log\max(1,\cdot)$ preserve continuity.
  Thus, $F_\delta$ is defined even off every Gaussian full-measure set.
  Every $x_m$ in this ambient space is a zero-start compact-valued
  $C^\theta$ path. The finite-product assertion of
  Lemma~\ref{L:symplectic-free} gives, for every such tuple,
  \[
    \|\mathcal P_\delta(x)\|
    \ge\left\|S_E\Big(\sum_{m=0}^N\ell_m\Big)\right\|\ge1 .
  \]

  Lemma~\ref{L:raw-block-restart}, in its noise-only case, applies
  to this same full input with base physical profile $\eta^2$.
  To check the exact objects, use its single retaining slow source
  and pull it back by $T_{\delta,0}$ and $T_{\delta,m}$.
  At fixed $\delta$ the global fast source pointfield is
  $\delta^{a/2}Y^\rho(\delta u,x)$ and its local restriction is
  its time shift by $mB$.
  Their ordinary Duhamel flows have the same massless free groups,
  amplitude $g_\delta$ and mask $m_R$.
  Source limits are taken on the fixed finite extended horizon
  $(N+1)B$ and on each local $B$ before composing the finitely
  many factors. The actual raw cocycle from that lemma therefore
  gives the ordered physical $F$ product with the true remainder.
  The full drivers and free groups intertwine through the closed
  isometry $i:E\to F$, including the source limits.
  Restricting the product and using injectivity of $i$ gives
  the first identity in~\eqref{E:tube-global-endpoint}.
  Both fast velocity and displacement remain in each factor.
  No mask was commuted through a free group, and the time blocks
  remain correlated on the same $W$.
  For zero covariance every input is zero and the ordered factors
  are $S_E(\ell_m)$, whose product is $S_E(L_\delta)$.

  The lower bound already established for every tuple removes
  the maximum at $X_\delta$. Together with the first identity,
  this proves the second identity in~\eqref{E:tube-global-endpoint}.
  No fixed-radius Gaussian-operator rate or source-to-point result
  is an input to this restart argument.
  This proves Lemma~\ref{L:tube-actual-endpoint}.
\end{proof}

\subsection{Uniform coarse envelope and the exact radial integral}

\begin{proposition}[Coarse tube envelope and actual operator moment]
  \label{P:tube-coarse-envelope}
  On the actual support $E_{0,\delta}$ let $A_\delta$ be its
  closed ball of radius $b_\delta$ and put
  \[
    G_\delta(r)=
    \sup_{\substack{a\in A_\delta\\\|\Phi\|_{H_I}\le r}}
    F_\delta(a+\mathcal M_\delta\Phi).
  \]
  This is finite, nondecreasing and Borel.
  There is $C_{\rm env}<\infty$, independent of $\delta$ and $R\ge1$,
  such that
  \begin{equation}\label{E:tube-coarse-envelope}
    G_\delta(r)\le C_{\rm env}(1+b_\delta^\nu+r^\nu),\qquad
    \E\|P_{\delta,E}^R(L_\delta,0)\|^2
    \le\int_0^\infty\frac r\delta
    e^{(G_\delta(r)-r^2/2)/\delta}\ud r .
  \end{equation}
\end{proposition}

\begin{proof}
  Put $G_B=\sup_{|v|\le B}\|S_E(v)\|$ and
  $C_{\rm pr}=G_B^2[B^{1-1/r_t}+B^{1-1/r_t-\theta}]$.
  The lower bound $G_B\ge1$ follows directly from $S_E(0)=I$.
  Proposition~\ref{P:uniform-actual-cameron} gives
  $1\le G_B\le3B$, $C_{\rm pr}\le18B^{3-1/r_t}$.
  Its primitive estimate, now without the covariance factor
  $\sqrt\delta$, gives
  \begin{equation}\label{E:tube-primitive-sum}
    \delta\sum_m h_m^{r_t}
    \le(C_{\rm pr}C_{\rm mean})^{r_t}\|\Phi\|_{H_I}^{r_t},
    \qquad h_m=\|(\mathcal M_\delta\Phi)_m\|_{C^\theta}.
  \end{equation}
  Indeed, each primitive norm is at most
  $C_{\rm pr}\delta^{-1/r_t}
  \|\mathcal T_R\Phi\|_{L^{r_t}(I_m)}$.
  Raising to $r_t$ cancels the $\delta$ weight, and the true
  partition sums to the full field norm, including an empty cell.

  The generic Banach Young bound supplies $c_Y=c_Y(B,\theta)>0$
  with $\log\|U_d(u,0)\|\le c_Y(1+\|d\|_{C^\theta}^{\nu})$
  for $u\le B$. This follows from
  \eqref{E:young-upper-refined-growth} and
  \eqref{E:constant-young-growth} by
  $d\le1+d^\nu$ and
  $(1+d)^\nu\le2^{\nu-1}(1+d^\nu)$.
  It applies on $\mathcal L(E)$ with multiplication norm one,
  without Gaussian, positivity or Hamiltonian assumptions on $d$.
  For $a\in A_\delta$ put $v_m=\|a_m\|_{C^\theta}$ and
  $n=N+1$. Convexity and submultiplicativity give
  \[
    F_\delta(a+\mathcal M_\delta\Phi)
    \le2\delta n(\log G_B+c_Y)
    +2^\nu c_Y\delta\sum_m(v_m^\nu+h_m^\nu).
  \]
  The upper expression is nonnegative, so it also bounds the
  logarithm with the maximum at one.
  The exact finite weighted power-mean inequalities are
  \begin{align*}
    \delta\sum_m v_m^\nu
    &\le(\delta n)^{1-\nu/p}\|a\|_{\delta,p}^\nu,\\
    \delta\sum_m h_m^\nu
    &\le(\delta n)^{1-\nu/r_t}
    \left(\delta\sum_m h_m^{r_t}\right)^{\nu/r_t}.
  \end{align*}
  They use exponents $p/\nu\ge1$, $r_t/\nu>1$ and
  nonnegative inputs $v_m^\nu,h_m^\nu$, followed by positive powers.
  Zero norms and empty cells cause no negative powers;
  $\delta>0$ and $n\ge2$, including the case $p=\nu$.
  Since $\delta n\le2/B$, these bounds and
  \eqref{E:tube-primitive-sum} give
  $F_\delta(a+\mathcal M_\delta\Phi)
  \le D_0+D_1b_\delta^\nu+D_2r^\nu$, where
  \begin{align*}
    D_0&=2(2/B)(\log G_B+c_Y),\\
    D_1&=2^\nu c_Y(2/B)^{1-\nu/p},\\
    D_2&=2^\nu c_Y(2/B)^{1-\nu/r_t}
    (C_{\rm pr}C_{\rm mean})^\nu .
  \end{align*}
  Hence $C_{\rm env}=1+D_0+D_1+D_2$ is independent of
  $\delta,R$ and proves the coarse bound for every admissible
  $\delta$, not just when $b_\delta$ is small.
  The supremum sets are nonempty and this bound makes their
  suprema finite. Monotonicity gives Borel measurability without
  asserting attainment of these suprema.
  The definition bounds $F_\delta$ on every closed tube.
  Apply Proposition~\ref{P:tube-rayleigh-transfer} and
  \eqref{E:tube-global-endpoint} to obtain the operator-moment bound.
  For zero law its direct case applies, with no assumption that
  the free endpoint norm is one.
  This proves Proposition~\ref{P:tube-coarse-envelope}.
\end{proof}

\begin{lemma}[Exact Rayleigh tail budget]\label{L:tube-rayleigh-tail}
  Suppose $G$ is Borel and $G(r)\le A_0+Cr^\nu$, $C\ge0$, $1<\nu<2$.
  If $M>0$ and $4C\le M^{2-\nu}$, then
  \begin{equation}\label{E:tube-rayleigh-tail}
    \int_M^\infty\frac r\delta
    e^{(G(r)-r^2/2)/\delta}\ud r
    \le4e^{(A_0-M^2/4)/\delta}.
  \end{equation}
  In particular the operator-moment bound in
  \eqref{E:tube-coarse-envelope} is finite at fixed parameters.
\end{lemma}

\begin{proof}
  The finite scalar cutoff inequality gives, for $r\ge M$,
  $Cr^\nu-r^2/2\le-M^2/8-r^2/8$.
  Its exact guards are $M>0$, $r\ge M$, $C\ge0$,
  $1<\nu<2$ and $4C\le M^{2-\nu}$.
  Indeed, $r^{2-\nu}\ge M^{2-\nu}\ge4C$ gives
  $Cr^\nu\le r^2/4$, while $r^2\ge M^2$ splits the
  remaining $-r^2/4$ into the two displayed negative terms.
  Analytically,
  $-\frac{\ud}{\ud r}[4e^{-r^2/(8\delta)}]
  =(r/\delta)e^{-r^2/(8\delta)}$.
  Integrating gives the front factor $4e^{-M^2/(8\delta)}$;
  multiplication by $e^{(A_0-M^2/8)/\delta}$ proves
  \eqref{E:tube-rayleigh-tail}.
  Such a cutoff exists since $2-\nu>0$.
  On $[0,M]$ the growth bound gives $G(r)\le A_0+CM^\nu$,
  so the integral is finite there as well.
  Apply this to $A_0=C_{\rm env}(1+b_\delta^\nu)$ and
  $C=C_{\rm env}$ in the preceding proposition.
  No infinite-dimensional Gaussian density is used.
  This proves Lemma~\ref{L:tube-rayleigh-tail}.
\end{proof}

\begin{lemma}[The raw half-action supremum]\label{L:tube-half-action}
  For finite $J:H\to\R$ bounded above on every raw ball,
  let $g_J(r)=\sup_{\|h\|\le r}J(h)$. In the extended reals,
  \[
    \sup_{r\ge0}\{g_J(r)-r^2/2\}
    =\sup_{h\in H}\{J(h)-\|h\|_H^2/2\}.
  \]
\end{lemma}

\begin{proof}
  For the lower inequality take $r=\|h\|$.
  For the upper inequality, every $\|h\|\le r$ gives
  $J(h)-r^2/2\le J(h)-\|h\|^2/2$.
  Take first the ball supremum and then the radius supremum.
  Each ball is nonempty with finite supremum, so no
  infinity-minus-infinity expression occurs.
  No compactness, rank or density assumption is needed.
  This proves Lemma~\ref{L:tube-half-action}.
\end{proof}

The Gaussian transfer retains the half of the single global raw action.
The coarse envelope is not the sharp spectral/product envelope.
Its application to the original canonical point moment, and the sharp
envelope and variational comparison, require their separate proofs.

===== END TEX FILE: notes/integrated_gaussian_tubes.tex =====

===== BEGIN TEX FILE: notes/integrated_uniform_products.tex =====
\section{Uniform spectral rates and phase products}
\label{S:uniform-physical-products}

Retain every original covariance and amplitude.
Set $E=H^{1/2}\times H^{-1/2}$, $F=E\oplus\R^2$,
and $m_R=\eta(\cdot/R)^2$, $R\ge1$, with the same fixed root profile.
Choose
\[
  \begin{aligned}
    &\frac12<\theta<\min(1-a/2,(3-a-\alpha)/2),\qquad \nu=1/\theta,\\
    &(1-\theta)^{-1}<r<2/a,\qquad \nu\le p<2<r .
  \end{aligned}
\]
Choose auxiliary exponents
$0<\gamma<\min(1/2,(2-\alpha)/2)$ and
$\theta<\beta<\min(1-a/2,(3-a-\alpha)/2)$ for the actual phase construction.
The original strict threshold makes these intervals nonempty.
Write $i_I:H_I\to H_W$ for the supported closed inclusion.
For nonzero covariance the actual field is
\[
  \mathcal T_R=T_R(C_t\otimes I_{H_{\rm sp}}),\qquad
  \|\mathcal T_R\|_{H_I\to L^r(I;\mathcal K(E))}
  \le C_{\rm mean}=M_0\|C_t\| ,
\]
by Proposition~\ref{P:uniform-mean-regulator}.
For zero covariance set $H_{\rm sp}=H_I=\{0\}$ and
$M_0=C_{\rm mean}=0$. Means and their rates are then zero,
and mean flows are free; no nonzero-noise estimate is needed for that case.
The residual comparisons below still act on the nonzero phase $E$.

\subsection{The actual E class and its own spectral constants}

For real smooth compact $q$ let $V_q=m_R(\Gamma*q)$,
$M_q:H^{1/2}\to H^{-1/2}$ be its multiplier and
$L_q^E(u,v)=(0,M_qu)$.
Let $\mathcal V_{E,R}$ be their operator-norm closure in $\mathcal K(E)$.

\begin{lemma}[Unique potential and fixed-radius lift]\label{L:uniform-E-lift}
  Each $L\in\mathcal V_{E,R}$ has the form $L(u,v)=(0,Mu)$,
  with $\|L\|=\|M\|=:k$, and determines a unique real
  $V\in H^{-1/2}$ supported in $\operatorname{supp}m_R$.
  The actual symmetric pairing satisfies
  \begin{equation}\label{E:uniform-E-pairing}
    |v_V(u,w)|\le k\|u\|_{H^{1/2}}\|w\|_{H^{1/2}} .
  \end{equation}
  It has a lift $L_F$ in the exact class of
  Section~\ref{S:signed-static-wave}, with $L_Fi=iL$.
  Lift constants may depend on $R$ and are used only for identification.
  Here $v_V(u,w)=\langle Vu,w\rangle_{H^{-1/2},H^{1/2}}$ on real
  states, with its Hermitian extension on complex states.
\end{lemma}

\begin{proof}
  For zero covariance, $L=M=V=L_F=0$ gives the claims directly.
  If $L_n^E\to L$, the zero columns persist and $M_n\to M$
  in $\mathcal L(H^{1/2},H^{-1/2})$, with the stated norm equality.
  At fixed $R$ choose real compact smooth $\chi_R=1$ near
  $\operatorname{supp}m_R$.
  Since $M_n\chi_R=V_n$,
  $\|V_n-V_j\|_{H^{-1/2}}\le\|\chi_R\|_{H^{1/2}}\|M_n-M_j\|$.
  Thus, $V_n\to V$, with the same support by testing outside it.
  Smooth multiplication on $H^{-1/2}$ identifies $Mu=Vu$
  on compact tests, then on $H^{1/2}$ by density.
  The identity $M\chi_R=V$ gives uniqueness; symmetry and
  \eqref{E:uniform-E-pairing} pass to the limit.

  The original $F$ operators are
  $(u,v,c_1,c_2)\mapsto(0,M_nu+c_1V_n,0,0)$.
  Their differences are bounded by
  $(1+\|\chi_R\|_{H^{1/2}})\|M_n-M_j\|$.
  They therefore converge in the old $F$ class and give the lift.
  This bound is allowed to grow with $R$; it will enter no uniform estimate.
  Dense smooth raw controls and bounded completion of $T_R$
  also show that all completed mean fields lie in
  $\mathcal V_{E,R}$ almost everywhere.
  Bochner averages preserve this closed linear class.
  Complexification preserves $k$ by the Hilbert real/imaginary splitting.
  The real symmetric pairing becomes Hermitian and its diagonal
  splits into the two real diagonals.
  This proves Lemma~\ref{L:uniform-E-lift}.
\end{proof}

\begin{proposition}[Spectral rate in E]
  \label{P:uniform-E-spectral}
  For $L\in\mathcal V_{E,R}$ put
  \[
    \beta(V)=\inf_{\substack{u\in H^1\\\|u\|_2=1}}
    \{\|\nabla u\|_2^2-v_V(u,u)\},\qquad \lambda(L)=\sqrt{-\beta(V)} .
  \]
  If $K\ge\max(1,k)$, the actual physical wave satisfies, for $t\ge0$,
  \begin{equation}\label{E:uniform-E-static-bound}
    -K^2\le\beta(V)=\inf\operatorname{spec}H_V\le0,\qquad
    \|P_V^E(t)\|\le8(1+K)^2(1+t)e^{\lambda(L)t}.
  \end{equation}
  If two such operators have norms at most $K$, then
  \begin{equation}\label{E:uniform-E-rate-continuity}
    |\beta(V)-\beta(W)|\le(K+2)\|L_V-L_W\|,\qquad
    |\lambda(L_V)-\lambda(L_W)|
    \le\sqrt{(K+2)\|L_V-L_W\|}.
  \end{equation}
  Every quantitative constant here uses the $E$ norm alone.
\end{proposition}

\begin{proof}
  We derive the budgets without transferring a quantitative $F$ bound.
  With $b=\|u\|_2$, $z=\|u\|_{H^1}$, Fourier Cauchy--Schwarz gives
  $\|u\|_{H^{1/2}}^2\le bz$.
  Equation~\eqref{E:uniform-E-pairing} and the half-weight
  arithmetic--geometric mean inequality give
  $|v_V(u,u)|\le Kbz\le z^2/2+K^2b^2/2$.
  The weights are $1/2,1/2$, bases $z^2,(Kb)^2\ge0$;
  positive powers include zero norms.
  For $q_V=\|\nabla u\|_2^2-v_V(u,u)$ and $c=2+K^2$,
  \begin{equation}\label{E:uniform-E-form-budget}
    \tfrac12z^2+(1+K^2/2)b^2
    \le q_V(u)+cb^2
    \le\tfrac32z^2+(1+3K^2/2)b^2
    \le3(1+K^2)z^2 .
  \end{equation}
  This is a densely defined closed semibounded Hermitian form
  on full $H^1$: its shifted norm is equivalent to the complete $H^1$ norm.
  The lower bound dominates $2b^2$, since $z\ge b$ and $K\ge1$.
  From~\cite{teschl:14:mathematical}*{Theorem~2.14, p.~81, (2.63)}
  and Theorem~3.6, p.~109, (3.51)--(3.53), it represents a
  unique self-adjoint $H_V$ with $A=H_V+c\ge2$ and $D(A^{1/2})=H^1$.
  Closedness uses the definition on that book's p.~80.
  The spectral meaning of $A\ge2$ follows from bounded spectral slices:
  a nonzero slice below two would give a unit vector in $D(A)$
  contradicting the form lower bound. The bottom argument below
  uses the same representation.

  Put $B_0=1-\Delta$ and $L_K=3(1+K^2)$.
  The common forms obey $\tfrac12B_0\le A\le L_KB_0$.
  For positive self-adjoint $T,S\ge1$ with ordered forms,
  completing the square gives
  \[
    \langle f,(T+t)^{-1}f\rangle
    =\sup_u\{2\operatorname{Re}\langle f,u\rangle-q_T(u)-t\|u\|^2\}
    \ge\langle f,(S+t)^{-1}f\rangle .
  \]
  The identity
  $\sqrt x=\pi^{-1}\int_0^\infty t^{-1/2}x/(x+t)\ud t$
  follows by $t=xv^2$.
  Positive spectral integration and Tonelli give square-root
  form order, with domain inclusions, from
  $I-t(T+t)^{-1}\le I-t(S+t)^{-1}$.
  Apply this to $(B_0,2A)$ and $(A,L_KB_0)$, both pairs at least one:
  \[
    D(A^{1/4})=H^{1/2},\qquad
    2^{-1/4}\|u\|_{H^{1/2}}\le\|A^{1/4}u\|_2
    \le L_K^{1/4}\|u\|_{H^{1/2}} .
  \]
  Under the $L^2$ pairing the dual norm is $\|A^{-1/4}v\|_2$,
  by Cauchy--Schwarz and the equality test $u=A^{-1/2}v$.
  Completion gives $H^{-1/2}$.
  Thus, with $M_K=L_K^{1/4}$, the phase norm
  $\|(u,v)\|_{E_A}^2=\|A^{1/4}u\|_2^2+\|A^{-1/4}v\|_2^2$
  lies between $M_K^{-2}\|(u,v)\|_E^2$ and $M_K^2\|(u,v)\|_E^2$.
  The condition cost is $M_K^2=\sqrt{3(1+K^2)}\le2(1+K)$.

  For unit $L^2$ data, $b=1$ and $z\ge1$.
  The form budget gives $q_V\ge z^2/2-1-K^2/2\ge-K^2$.
  A dilated compact unit bump translated wholly off the potential
  support has zero potential pairing and kinetic energy tending to zero,
  so $\beta\le0$.
  Complex form infima agree with real ones: dividing each complex
  diagonal by its squared norm is the convex combination of the
  two normalized real diagonals, omitting zero parts.
  The spectral form formulas identify $\beta$ with the spectral
  bottom by bounded spectral slices.
  There are support points because scalar spectral measures of unit
  vectors have mass one; their arbitrarily small bounded slices
  give approximate eigenvectors and the reverse form bound.
  If $\Sigma$ denotes the closed PVM support and real $z\notin\Sigma$,
  the Borel function $f_z(h)=(h-z)^{-1}$ on $\Sigma$, zero outside,
  is bounded, as is $hf_z(h)$.
  Its calculus has range in $D(H_V)$ and supplies both inverse identities
  for $H_V-z$ on their respective domains. Thus no such $z$ is spectral;
  the approximate eigenvectors give the other inclusion.
  Hence $\lambda\le K$ and $h+c\ge2$ on the spectrum.

  Define $\operatorname{Cos}_t(h),\operatorname{Sin}_t(h)$ by
  $\cos(t\sqrt h),\sin(t\sqrt h)/\sqrt h$ for $h>0$,
  by $1,t$ at zero and by
  $\cosh(t\sqrt{-h}),\sinh(t\sqrt{-h})/\sqrt{-h}$ for $h<0$.
  In the $E_A$ isometry the matrix is
  \[
    \begin{pmatrix}
      \operatorname{Cos}_t(h)&\sqrt{h+c}\operatorname{Sin}_t(h)\\
      -h\operatorname{Sin}_t(h)/\sqrt{h+c}&\operatorname{Cos}_t(h)
    \end{pmatrix}.
  \]
  For $h\ge0$, its off-diagonals have bounds $1+\sqrt c\,t$ and one;
  at zero their values are $\sqrt c\,t,0$.
  For $\beta\le h<0$, the entries are bounded using
  $|\operatorname{Cos}_t|\le e^{\lambda t}$,
  $|\operatorname{Sin}_t|\le te^{\lambda t}$,
  upper off-diagonal at most $\sqrt c\,te^{\lambda t}$,
  and lower at most $Ke^{\lambda t}$.
  Since $\sqrt c\le2K$, each entry is at most
  $2(1+K)(1+t)e^{\lambda t}$.
  Set these entries to zero off the closed spectral support
  before applying bounded Borel calculus.
  From~\cite{teschl:14:mathematical}*{Theorems~3.1--3.2,
  pp.~102--104, (3.18)--(3.33)}, their matrix norm is at most
  twice that entry bound, and the condition cost gives
  \eqref{E:uniform-E-static-bound}.
  Spectral dominated convergence and scalar addition give the group.

  Denote the spectral matrix evolution by $P_V^E(t)$.
  It is the actual physical $E$ wave.
  The fixed-$R$ lift in Lemma~\ref{L:uniform-E-lift} belongs
  to the precise class in Proposition~\ref{P:signed-physical-wave}.
  Its form is this same $q_V$ and has the same self-adjoint
  representative by uniqueness, regardless of the lift's larger shift.
  On dense bounded spectral cutoffs the two waves have the same
  $\operatorname{Cos},\operatorname{Sin}$ functions of $H_V$.
  Boundedness extends equality to all $E$.
  The old graph-core Duhamel identification therefore applies;
  no lift norm or $\chi_R$ constant entered the budgets above.
  Conjugation commutes with the real structures, so real restrictions
  are the actual phases.
  For compact $L$, finite-rank approximation and strong continuity of
  the free group and its adjoint make
  $v\mapsto S_E(-v)LS_E(v)$ norm continuous on finite intervals.
  Its primitive is Lipschitz. Its Young equation is therefore the
  ordinary bounded-interaction equation by
  Proposition~\ref{P:constant-young-linear}.
  This identifies the averaged static baseline without transferring
  any lift norm into the uniform budgets.

  Finally, take a unit $\varepsilon$-minimizer for $W$,
  $0<\varepsilon\le1$. Since $\beta(W)\le0$, it has $q_W\le1$.
  Thus $z^2-1-Kz\le1$, which forces $z\le K+2$.
  The multiplier difference changes its form by at most
  $\|L_V-L_W\|\|u\|_{H^{1/2}}^2\le(K+2)\|L_V-L_W\|$.
  Take infima, let $\varepsilon\downarrow0$ and reverse $V,W$.
  The square-root inequality on nonnegative $-\beta$ gives
  \eqref{E:uniform-E-rate-continuity}.
  For zero covariance the class is $\{0\}$, $H_V=-\Delta$ and
  $\beta=\lambda=0$; the free wave gives the claims directly.
  This proves Proposition~\ref{P:uniform-E-spectral}.
\end{proof}

\subsection{Scalar-time averaging and actual mean budgets}

\begin{proposition}[Uniform completed-field averaging]\label{P:uniform-rate-averaging}
  Use the true slow partition $I_m$ with mesh at most $\delta B$.
  Let $\mathcal A_\delta$ average over each positive-length cell;
  an empty final cell is ignored.
  Put $\omega_\delta=\|(\mathcal A_\delta-I)C_t\|_{H_t\to L^r(I)}$.
  At fixed $B$, $\omega_\delta\to0$.
  For $M\ge0$, if $\|\Phi\|_{H_I}\le M$, $W_R=\mathcal T_R\Phi$,
  $\overline W_R=\mathcal A_\delta W_R$ and $Z=C_{\rm mean}M$, then
  \begin{align}
    \|W_R\|_{L^r},\ \|\overline W_R\|_{L^r}&\le Z,\qquad
    \|\overline W_R-W_R\|_{L^r}\le M_0M\omega_\delta=:\Omega_\delta(M),
    \label{E:uniform-field-averaging}\\
    \operatorname{Rate}_R(\Phi)&=\int_I\lambda(\mathcal T_R\Phi(s))\ud s,
    \label{E:uniform-mean-rate}\\
    \int_I|\lambda(\overline W_R)-\lambda(W_R)|\ud s
    &\le\sqrt{3+2Z}\sqrt{\Omega_\delta(M)}=:\Lambda_\delta(M)\to0 .
    \label{E:uniform-rate-averaging}
  \end{align}
  These errors are uniform in $R\ge1$.
  The rate is finite, nonnegative and continuous on $H_I$.
\end{proposition}

\begin{proof}
  Bochner averaging is a contraction on $L^r(I;\mathscr Z)$
  for any Banach $\mathscr Z$, by Jensen.
  For continuous fields on $[0,1]$, its error is bounded by
  the modulus of continuity at the mesh.
  Simple-field approximation, followed by continuous approximation
  of scalar indicators in $L^r$, proves density of those fields.
  The contraction gives strong convergence for every Bochner field.
  In the scalar case it is uniform on the compact closure of
  $C_t$'s unit-ball image, by a finite net and
  $\|\mathcal A_\delta-I\|\le2$. This proves $\omega_\delta\to0$.

  On finite tensors, integration commutes with the fixed bounded $T_R$:
  \[
    \mathcal A_\delta^{\mathcal K(E)}
    T_R(C_t\otimes I)\Phi
    =T_R((\mathcal A_\delta C_t)\otimes I)\Phi .
  \]
  The dimension-free Hilbert tensor bound in
  Lemma~\ref{L:uniform-mean-tensor}, and $\|T_R\|\le M_0$,
  extend this typed identity to the completed $H_I$.
  Applying it to the difference gives~\eqref{E:uniform-field-averaging}.
  Averages remain in the same closed $E$ operator class.
  Only scalar-time compactness was used; the tensor map is not
  claimed compact. Nor does this assert noncompactness of a composite
  spatial family: each fixed-radius completed mean is compact.

  For any two such fields, apply~\eqref{E:uniform-E-rate-continuity}
  with the pointwise bound
  \[
    K(s)=\max(1,\|W_1(s)\|,\|W_2(s)\|).
  \]
  Cauchy--Schwarz gives
  \[
    \int_I|\lambda(W_1)-\lambda(W_2)|
    \le\sqrt{3+\|W_1\|_{L^1}+\|W_2\|_{L^1}}\,
    \sqrt{\|W_1-W_2\|_{L^1}} .
  \]
  Continuity of $\lambda$ on the class makes these quantities measurable.
  Since $|I|=1$, this proves~\eqref{E:uniform-rate-averaging}.
  It also proves rate continuity, while
  $\lambda(L)\le\max(1,\|L\|)$ gives
  $\operatorname{Rate}_R(\Phi)\le1+C_{\rm mean}\|\Phi\|$.
  For zero covariance the fields and rate errors are zero directly.
  This proves Proposition~\ref{P:uniform-rate-averaging}.
\end{proof}

For the remaining proofs use the full parameter package and true
$B,\delta,N,\ell_m,I_m$ partition of Section~\ref{S:actual-cameron-mean}.
For $W_R=\mathcal T_R\Phi$ define
\[
  H_m(u)=\int_0^{\min(u,\ell_m)}
  S_E(-v)W_R(s_m+\delta v)S_E(v)\ud v,\qquad
  P_m^{\rm mean}=S_E(\ell_m)U_{H_m}(\ell_m,0).
\]

\begin{lemma}[Explicit physical primitive and growth budgets]
  \label{L:uniform-product-budgets}
  Write $G_B=\sup_{|v|\le B}\|S_E(v)\|$ and
  $C_B=G_B^2[B^{1-1/r}+B^{1-1/r-\theta}]$.
  Then $1\le G_B\le3B$, $C_B\le18B^{3-1/r}\le32B^{3-1/r}$
  and $C_BB^{1/r}\ge B$.
  The stopped primitives lie in the zero-start little H\"older space and
  \begin{equation}\label{E:uniform-product-primitive}
    \|H_m\|_\theta\le a_m:=C_B\delta^{-1/r}\|W_R\|_{L^r(I_m)},
    \qquad\delta\sum_m a_m^r\le C_B^r\|W_R\|_{L^r}^r .
  \end{equation}
  There is a fixed $C_{\rm gr}=C_{\rm gr}(\theta)>0$ such that
  \begin{equation}\label{E:uniform-product-growth}
    \log\|S_E(\ell)U_D(\ell,0)\|
    \le C_{\rm gr}B(1+\|D\|_\theta^\nu),\qquad 0\le\ell\le B .
  \end{equation}
  Here $D$ is any zero-start $C^\theta([0,B];\mathcal L(E))$ path;
  no Gaussian or Hamiltonian hypothesis is imposed on this growth bound.
  The actual mean endpoints have $\|P_m^{\rm mean}\|\ge1$.
\end{lemma}

\begin{proof}
  The balanced free matrix has upper entry
  $\langle k\rangle\sin(vk)/k$ and lower $-k\sin(vk)/\langle k\rangle$.
  Splitting $k\le1$ and $k\ge1$ bounds the upper by $\sqrt2 B$,
  while the lower and diagonals have bound one.
  At zero the off-diagonals are $v,0$.
  The Frobenius bound gives $G_B\le\sqrt{3+2B^2}\le3B$;
  $S_E(0)=I$ gives $G_B\ge1$.
  The stated $C_B$ inequalities follow, including
  $C_BB^{1/r}=G_B^2(B+B^{1-\theta})\ge B$.
  H\"older in time with $1-1/r>\theta$, the affine time change,
  compact conjugation and constant stopping prove
  \eqref{E:uniform-product-primitive}; the true partition sums
  the $r$th powers, with zero on an empty cell.

  For the explicit Young budget put $d=\|D\|_\theta$ and
  $c_\theta=2\max(1,C_{\rm Young})$,
  as in the local estimate proving Lemma~\ref{L:young-upper-growth}.
  If $c_\theta dB^\theta\le1/4$, whole-interval contraction gives
  $\log\sup\|U_D\|\le\log(4/3)<1/2$.
  Otherwise at most $2B(4c_\theta d)^\nu$ contraction pieces
  have norm at most $4/3$.
  Combine their logarithms with $\log G_B\le\log(4B)$.
  For example
  $C_{\rm gr}=4+\log4+2(4c_\theta)^\nu$ gives
  \eqref{E:uniform-product-growth}, since $B\ge1$.
  This is the generic algebra argument on $\mathcal L(E)$
  with multiplication norm one, not an unspecified radius-dependent bound.

  Finally Proposition~\ref{P:uniform-mean-regulator} gives
  $W_R\in L^r(I;\mathcal K(E))$ for each fixed $R,\Phi$.
  The compact conjugation and stopped Bochner primitive used above
  therefore make each $H_m$ a zero-start compact-valued
  $C^\theta$ path. Lemma~\ref{L:symplectic-free} gives
  $\|P_m^{\rm mean}\|\ge\|S_E(\ell_m)\|\ge1$,
  deterministically for each $\Phi$.
  This norm bound needs no fast covariance direction or action estimate.
  An empty endpoint is $I$; zero covariance gives the free endpoint.
  This proves Lemma~\ref{L:uniform-product-budgets}.
\end{proof}

\subsection{Full blocks, the true last cell and polynomial control balls}

\begin{proposition}[Finite-mesh physical mean-product bound]
  \label{P:uniform-mean-product}
  Fix $B$ as above, $M\ge0$ and $K\ge1$, and put $Z=C_{\rm mean}M$.
  Uniformly for $R\ge1$, $\|\Phi\|\le M$,
  \begin{align}
    \delta\sum_{m=0}^N\log\|P_m^{\rm mean}\|
    -\operatorname{Rate}_R(\Phi)
    \le{}&\frac{L_{B,K}}B+
    C_{\rm gr}32^r Z^rB^{3r}(K^{-r}+K^{\nu-r})\notag\\
    &+\Lambda_\delta(M)+C(\theta,B,K)E_\delta+
    \operatorname{Last}_\delta,\label{E:uniform-mean-product}
  \end{align}
  where $L_{B,K}=\log16+4\log(1+K)+3\log(1+B)$ and
  \begin{align*}
    E_\delta&=(2/B)^{1-1/r}C_B\Omega_\delta(M)
    +(2/B)^{1-\nu/r}C_B^\nu\Omega_\delta(M)^\nu,\\
    \operatorname{Last}_\delta&=
    C_{\rm gr}B[\delta+C_B^\nu Z^\nu\delta^{1-\nu/r}].
  \end{align*}
  The last three terms vanish as $\delta\downarrow0$ at fixed $B,K,M$.
\end{proposition}

\begin{proof}
  On each positive-length cell use its own Bochner average $\overline M_m$;
  set it to zero on an empty cell and form the constant-field primitive
  $\overline H_m$.
  Put $e_m=C_B\delta^{-1/r}
  \|W_R-\overline W_R\|_{L^r(I_m)}$.
  Jensen and~\eqref{E:uniform-product-primitive} give
  \[
    \|\overline H_m\|_\theta\le a_m,\quad
    \|H_m-\overline H_m\|_\theta\le e_m,\quad
    \delta\sum e_m^r\le C_B^r\Omega_\delta(M)^r,\quad
    \delta\sum a_m^r\le D_M:=C_B^rZ^r .
  \]
  Finite power mean at exponents $r$ and $r/\nu>1$,
  with nonnegative inputs $e_m,e_m^\nu$, gives
  $\delta\sum_m(e_m+e_m^\nu)\le E_\delta$.
  Here $n=N+1\ge2$, $\delta>0$ and $\delta n\le2/B$;
  all subsequent powers are positive and zero errors are allowed.

  On full cells only,
  $\|\overline M_m\|\le(\delta B)^{-1/r}\|W_R\|_{L^r(I_m)}
  =a_m/(C_BB^{1/r})\le a_m/B$.
  Split full indices $m<N$ into good $a_m\le K$ and bad $a_m>K$.
  On a good block, Proposition~\ref{P:young-upper-multiplicative}
  applies with base $\overline H_m$, perturbation $H_m-\overline H_m$
  and the actual left multiplier $S_E(B)$.
  The baseline is the actual static wave of $\overline M_m$
  by Proposition~\ref{P:uniform-E-spectral}.
  Here $\|\overline M_m\|\le K/B\le K$, whereas
  $\|\overline H_m\|_\theta\le a_m\le K$.
  The spectral estimate gives
  \[
    \|S_E(B)U_{\overline H_m}(B,0)\|
    \le8(1+K)^2(1+B)e^{B\lambda(\overline M_m)}.
  \]
  Consequently,
  \[
    \log\|P_m^{\rm mean}\|
    \le L_{B,K}+B\lambda(\overline M_m)
    +C(\theta,B,K)(e_m+e_m^\nu).
  \]
  This sufficient prefactor follows from the bound in $E$,
  $8(1+K)^2(1+B)$, by enlarging it.
  Since $\delta N\le1/B$, the prefactors sum to at most $L_{B,K}/B$.
  Nonnegativity of $\lambda$ gives
  $\delta\sum_{\rm good}B\lambda(\overline M_m)
  \le\int_I\lambda(\overline W_R)
  \le\operatorname{Rate}_R(\Phi)+\Lambda_\delta(M)$.
  Bad and last rate cells can be dropped in this upper bound.

  On bad full cells~\eqref{E:uniform-product-growth} gives
  $C_{\rm gr}B(1+a_m^\nu)$.
  Because $a_m>K\ge1$ and $r>\nu$,
  $1+a_m^\nu\le(K^{-r}+K^{\nu-r})a_m^r$.
  Their weighted sum is bounded by
  $C_{\rm gr}BC_B^rZ^r(K^{-r}+K^{\nu-r})$.
  The inequality $C_B\le32B^{3-1/r}$ yields the displayed bad-block term.

  If $\ell_N=0$, the last endpoint is $I$ and
  $\log\|I\|=0$.
  Otherwise use the actual stopped path, not its frozen full-cell formula.
  Since $a_N\le C_B\delta^{-1/r}Z$, its weighted logarithm is at most
  $\operatorname{Last}_\delta$ by~\eqref{E:uniform-product-growth}.
  This tends to zero because $\nu<r$, even for arbitrarily short
  last cells; no division by that cell length occurs.
  Combining these estimates proves~\eqref{E:uniform-mean-product}.
  All constants are independent of $R$.
  This proves Proposition~\ref{P:uniform-mean-product}.
\end{proof}

\begin{corollary}[Every polynomial control radius]\label{C:uniform-polynomial-balls}
  For $c_{\rm ball}>0$, $\kappa_{\rm ball}\ge0$ put
  $M_B=c_{\rm ball}B^{\kappa_{\rm ball}}$.
  Then
  \[
    \limsup_{\substack{B\to\infty\\B\in\mathbb N}}
    \limsup_{\delta\downarrow0}
    \sup_{\substack{R\ge1\\\|\Phi\|\le M_B}}
    \left\{\delta\sum_m\log\|P_m^{\rm mean}\|
    -\operatorname{Rate}_R(\Phi)\right\}\le0 .
  \]
\end{corollary}

\begin{proof}
  Choose $s>r(3+\kappa_{\rm ball})/(r-\nu)$ and $K_B=B^s$.
  At each fixed $B$, the inner $\delta$ limit has a fixed finite
  radius and threshold, so the last three errors in
  \eqref{E:uniform-mean-product} vanish first.
  Its bad terms become
  \[
    C_{\rm gr}32^r C_{\rm mean}^r c_{\rm ball}^r
    \{B^{r(3+\kappa_{\rm ball})-sr}
    +B^{r(3+\kappa_{\rm ball})+s(\nu-r)}\}.
  \]
  Both exponents are negative: the second by choice and the first
  because $s>3+\kappa_{\rm ball}$.
  Also
  $L_{B,K_B}/B\le[\log16+7\log2+(4s+3)\log B]/B\to0$.
  Thus, the outer integer-$B$ limit gives the claim.
  No diagonal choice $B_\delta,M_\delta$ is asserted.
  At fixed parameters all primitive maps are bounded linear into
  separable little H\"older products. Young local dependence
  and positive endpoint norms make the displayed logarithms continuous;
  the rate is continuous by Proposition~\ref{P:uniform-rate-averaging}.
  Growth bounds make each control-ball supremum finite.
  A countable dense subset of each closed Hilbert ball has the
  same supremum. Supremum over $R$ is an ordinary deterministic
  real supremum, not a random measurability or compact-family claim.
  This proves Corollary~\ref{C:uniform-polynomial-balls}.
\end{proof}

\subsection{Arbitrary small residual paths and the ordered product}

\begin{proposition}[Residual comparison and the integrated rate]
  \label{P:uniform-arbitrary-residual}
  Let $x_m$ be arbitrary zero-start little $C^\theta$ compact-operator
  paths on $[0,B]$, put $v_m=\|x_m\|_\theta$ and
  $Y=(\delta\sum_m v_m^p)^{1/p}$.
  Define
  \[
    P_m^{\rm pert}=S_E(\ell_m)U_{H_m+x_m}(\ell_m,0),\qquad
    z_{\rm rat}=\prod_m\frac{\|P_m^{\rm pert}\|}{\|P_m^{\rm mean}\|}.
  \]
  For fixed integer $B\ge1$, $M\ge0$ and every $K_{\rm res}\ge1$,
  \begin{align}
    \delta\log\max(1,z_{\rm rat})\le{}&
    C_{K_{\rm res}}[(2/B)^{1-1/p}Y+(2/B)^{1-\nu/p}Y^\nu]\notag\\
    &+c_BD_M(K_{\rm res}^{-r}+K_{\rm res}^{\nu-r}),
    \label{E:uniform-residual-ratio}
  \end{align}
  uniformly in $R\ge1$, $\|\Phi\|\le M$.
  The finite constants may be written
  $C_{K_{\rm res}}=C(\theta,B,K_{\rm res})$ and
  $c_B=2^{\nu-1}C_{\rm gr}B$.
  Here $D_M=C_B^r(C_{\rm mean}M)^r$.
  If $b_\delta\ge0$ is any deterministic function of $\delta$ tending to zero
  at each fixed $B$, $M_B$ is as in
  Corollary~\ref{C:uniform-polynomial-balls}, and
  $\mathcal F=2\delta\log\max(1,\|P_N^{\rm pert}\cdots P_0^{\rm pert}\|)$,
  then
  \begin{equation}\label{E:uniform-residual-integrated-rate}
    \limsup_{\substack{B\to\infty\\B\in\mathbb N}}
    \limsup_{\delta\downarrow0}
    \sup_{\substack{R\ge1,\ \|\Phi\|\le M_B\\Y\le b_\delta}}
    \{\mathcal F-2\operatorname{Rate}_R(\Phi)\}\le0 .
  \end{equation}
  No Gaussian, Cameron or Hamiltonian condition on the residuals is imposed.
\end{proposition}

\begin{proof}
  All endpoint norms are positive by the actual Young and free inverses.
  On every cell with $a_m\le K_{\rm res}$ apply
  Proposition~\ref{P:young-upper-multiplicative} with base $H_m$,
  perturbation $x_m$ and left multiplier $S_E(\ell_m)$.
  It gives logarithmic ratio at most
  $C(\theta,B,K_{\rm res})(v_m+v_m^\nu)$.
  On cells with $a_m>K_{\rm res}$ use
  \eqref{E:uniform-product-growth},
  $(a_m+v_m)^\nu\le2^{\nu-1}(a_m^\nu+v_m^\nu)$
  and the actual mean denominator $\|P_m^{\rm mean}\|\ge1$.
  The logarithmic ratio is at most $c_B(1+a_m^\nu+v_m^\nu)$,
  with $c_B$ independent of $K_{\rm res},R,\delta,\Phi,M$.
  Increase $C_{K_{\rm res}}$ to dominate both good and bad
  residual constants. Summation gives a nonnegative bound
  \[
    \log\max(1,z_{\rm rat})
    \le C_{K_{\rm res}}\sum_m(v_m+v_m^\nu)
    +c_B\sum_{a_m>K_{\rm res}}(1+a_m^\nu).
  \]
  The bad sum times $\delta$ is at most
  $D_M(K_{\rm res}^{-r}+K_{\rm res}^{\nu-r})$.
  Finite power mean at exponents $p\ge1$ and $p/\nu\ge1$,
  with nonnegative inputs $v_m,v_m^\nu$, gives
  $\delta\sum v_m\le(2/B)^{1-1/p}Y$ and
  $\delta\sum v_m^\nu\le(2/B)^{1-\nu/p}Y^\nu$.
  This includes $p=\nu$, zero entries and the true empty block,
  with no singular powers. It proves~\eqref{E:uniform-residual-ratio}.

  The product $A_{\rm prod}=\prod_m\|P_m^{\rm mean}\|$ is at least one.
  Submultiplicativity, without commutation, gives
  \[
    \begin{aligned}
      \max(1,\|P_N^{\rm pert}\cdots P_0^{\rm pert}\|)
      &\le A_{\rm prod}\max(1,z_{\rm rat}),\\
      \mathcal F-2\delta\sum_m\log\|P_m^{\rm mean}\|
      &\le2\delta\log\max(1,z_{\rm rat}).
    \end{aligned}
  \]
  At fixed $B,M,K_{\rm res}$ the residual terms vanish on $Y\le b_\delta$.
  Let $\delta\downarrow0$ first and then $K_{\rm res}\to\infty$.
  Since $r>\nu$, the residual excess has limsup at most zero,
  uniformly in $R,\Phi$.
  Now take $M=M_B$ at each fixed $B$ and combine with
  Corollary~\ref{C:uniform-polynomial-balls}; a supremum of sums
  is no larger than the sum of the suprema.
  The outer integer-$B$ limit proves~\eqref{E:uniform-residual-integrated-rate}.
  The endpoint functional is continuous on all tuples by generic
  Young local dependence, including nonphysical residuals.
  Nothing was multiplied as scalar displacement moments.
  This proves Proposition~\ref{P:uniform-arbitrary-residual}.
\end{proof}

These are uniform deterministic $E$-phase product estimates.
Their Gaussian Rayleigh application, original point transfer and
signed-positive score comparison are proved separately in
Sections~\ref{S:actual-gaussian-tubes}--\ref{S:intrinsic-second-moment}.

===== END TEX FILE: notes/integrated_uniform_products.tex =====

===== BEGIN TEX FILE: notes/integrated_point_transfer.tex =====
\section{The original point moment and the growing-cone phase}
\label{S:original-point-transfer}

Retain all original covariances and amplitudes.
Write $a=\alpha_0$, $\kappa=(4-\alpha-a)/(3-\alpha)>1$.
Fix the auxiliary parameters of the preceding Gaussian and product
sections once, in their strict admissible gaps.
For $0<\delta<1$ put
\[
  L=\delta^{-1},\quad R=L+2,\quad T_\delta=\delta^{-1/\kappa},
  \quad g=\delta^{(1-a)/2},\quad \Gamma_\delta=g^2\Gamma .
\]
Use the same real even root $\eta$, set $\psi=\eta(\cdot/R)$,
$m=\psi^2$, $z=(\psi,0)\in E$, $D=B_1(0)$ and $v_d=|D|>0$.
Let $W_{\rm fast}=W\circ T_{\delta,0}$ on the given slow probability
space, and let $P_\delta$ be the actual physical $E$ endpoint at time
$L$ driven by $gM_R(W_{\rm fast})$, with physical noise mask $m$ once.
The datum $\psi$ is not the auxiliary cutoff used to extend the driver
to constant columns on $F$.

\begin{lemma}[Actual restriction and fixed-parameter finiteness]
  \label{L:point-actual-finiteness}
  For nonzero covariance, the actual $E$ flow and its source flows
  are the closed isometric restrictions of their actual $F$ extensions.
  Their operator norms and differences are measurable, and
  \begin{equation}\label{E:point-fixed-finiteness}
    1\le\E\|P_\delta\|_{\mathcal L(E)}^2<\infty .
  \end{equation}
\end{lemma}

\begin{proof}
  Let $A_F=gA_{F,R}(W_{\rm fast})$ be the scaled full driver.
  Linearity and Proposition~\ref{P:constant-phase-driver} give $A_Fi=iD_E$,
  with $D_E=gM_R(W_{\rm fast})$, and $S_F(t)i=iS_E(t)$.
  The extension uses a cutoff $\widetilde\psi=1$ near its larger
  localization, not the datum $\psi$.
  Applying $i$ to the state Young sums and using uniqueness gives
  $U_F(t,s)i=iU_E(t,s)$, then $P_F(t,s)i=iP_E(t,s)$.
  The same argument applies to sources.
  Closedness and isometry imply
  $\|P_E\|\le\|P_F\|$ and the analogous difference bound;
  density of $E$ in $F$ is neither true nor used.
  The continuous Young map on its separable path span, followed by
  bounded physical conjugation and restriction, gives measurable
  endpoint norms and uniform time-triangle difference norms.
  No operator-norm continuity of the free group is assumed.
  Young Neumann pieces and the free inverse also give invertibility.

  We check a direct finiteness input, without a fixed-mask asymptotic rate.
  Take $B=1$ in Propositions~\ref{P:tube-actual-law}
  and~\ref{P:tube-coarse-envelope} and Lemma~\ref{L:tube-rayleigh-tail}.
  Every $0<\delta<1$ satisfies their clock condition.
  The global endpoint in~\eqref{E:tube-global-endpoint} is exactly
  this $P_\delta$: the same given $W_{\rm fast}$, amplitude $g$,
  root $\eta$, one mask $m$, massless $E$ phase, and horizon $\delta^{-1}$.
  We use the same admissible $\theta$ and actual driver version.
  Literal row identities, rational times and Young uniqueness identify
  versions if a smaller common admissible exponent is used.
  Thus, the finite radial bound applies to this actual endpoint,
  not merely an equal-law copy.
  At these fixed parameters the actual driver
  $gM_R(W_{\rm fast})$ is a zero-start compact-valued
  $C^\theta([0,L];\mathcal K(E))$ path on its path event.
  Lemma~\ref{L:symplectic-free} gives
  $\|P_\delta\|\ge\|S_E(L)\|\ge1$ almost surely,
  proving~\eqref{E:point-fixed-finiteness}.
  This use requires no $F$-norm rate along growing radii.
  Source convergence and source uniform integrability are checked next,
  separately from this raw endpoint finiteness.
  This proves Lemma~\ref{L:point-actual-finiteness}.
\end{proof}

\begin{lemma}[The same retaining fast sources]\label{L:point-fast-sources}
  At each fixed $\delta$, take one retaining slow source
  $Y_{\epsilon,\tau}$ and define
  \[
    Y_{\rm fast}(t,x)=\delta^{a/2}Y_{\epsilon,\tau}(\delta t,x).
  \]
  Its actual physical $E$ flows $P_E^{\epsilon,\tau}$ with coefficient
  $m gY_{\rm fast}$ satisfy
  \begin{equation}\label{E:point-source-flow-limit}
    \E\sup_{0\le s\le t\le L}
    \|P_E^{\epsilon,\tau}(t,s)-P_E(t,s)\|^2\longrightarrow0
    \quad\hbox{as }(\epsilon,\tau)\to(0,0).
  \end{equation}
  The unmasked field $gY_{\rm fast}$ has the canonical source law
  for covariance $\Gamma_\delta$, spatial width $\epsilon$
  and temporal width $\tau/\delta$.
\end{lemma}

\begin{proof}
  Testwise this field is $Y_{\epsilon,\tau}(T_{\delta,0}f)$.
  The raw isometry and source domination give source and residual
  variances bounded by $\|f\|_{H_{\rm fast}}^2$, with residual variance
  tending to zero at fixed $\delta$ on every smooth compact test.
  The Gaussian transfer Proposition~\ref{P:source-gaussian-transfer}
  therefore gives actual driver convergence in every finite $L^pC^\theta$,
  retaining $W_{\rm fast}$ literally.
  Multiplication by fixed $g$ and the bounded $F$ extension preserve it.
  The transfer bound and Proposition~\ref{P:actual-operator-driver}
  also give uniform source $\sqrt p$ path moments at these fixed
  $\delta,R,L$.
  The moment-series argument yields square-exponential path norms.
  Young local dependence gives probability convergence on driver balls;
  the growth exponent $1/\theta<2$ and those tails give uniform
  flow moments of every finite order and uniform integrability.
  The proof of Proposition~\ref{P:constant-gaussian-flow} applies
  to this very pullback family.
  Restriction from $F$ then proves~\eqref{E:point-source-flow-limit}.
  No uniform-in-$\delta$ source bound or exchange of limits is asserted.

  This source is also the actual ordinary response for all $E$ data.
  On Schwartz states its first primitive has row $gY_{\rm fast}(h_R)$.
  The source indicator approximation and bounded point variances at
  positive widths identify it with the statewise integral
  $\int_0^t S_E(-r)B(mgY_{\rm fast}(r))S_E(r)\ud r$.
  Fubini uses $\E|ZY|\le\|Z\|_2\|Y\|_2$ when Gaussian testing is needed.
  Countable dense states, rational times and continuity give the full
  ordinary-primitive identity, as in Proposition~\ref{P:source-ordinary-response}.
  Lemma~\ref{L:constant-source-solution} and
  Proposition~\ref{P:symplectic-source} then identify the Young equation
  with the ordinary interaction equation on $E$.

  In the temporal kernel
  $K_\tau(v)=\Gamma_{\rm E}(a)^{-1}
  \int_0^{\tau^{-1}}e^{-\lambda|v|}\lambda^{a-1}\ud\lambda$,
  substitution $\lambda'=\delta\lambda$ gives
  \[
    \delta^aK_\tau(\delta v)=K_{\tau/\delta}(v).
  \]
  Hence $gY_{\rm fast}$ has covariance
  $K_{\tau/\delta}(t-s)(p_{2\epsilon}*\Gamma_\delta)(x-y)$.
  The shared-width maximum and spatial heat-sum conventions persist
  for two sources.
  Positive multiplication by $g^2$ preserves every original covariance
  class, including spatial white noise.
  At fixed $\delta$, $(\epsilon,\tau/\delta)\to(0,0)$.
  The full source point-moment limit
  in Proposition~\ref{P:masked-canonical-transfer} thus applies to this
  single-source law and its continuous version; no newly reconstructed
  auxiliary family for $\Gamma_\delta$ is required.
  This proves Lemma~\ref{L:point-fast-sources}.
\end{proof}

\begin{lemma}[Compact-data source identification]\label{L:point-compact-source}
  For fixed $\delta,\epsilon,\tau$, the displacement
  $v_{\epsilon,\tau}(t,x)=(\operatorname{pr}_1P_E^{\epsilon,\tau}(t,0)z)(x)$
  has a jointly measurable continuous version and satisfies the ordinary
  scalar mild equation with coefficient $b=mgY_{\rm fast}$
  and initial data $(\psi,0)$.
\end{lemma}

\begin{proof}
  On the fixed source regularity event, $b$ is smooth in space,
  has common compact support in $B_{2R}$, and is continuous in time
  in every bounded spatial derivative norm on $[0,L]$.
  Choose integer $k>d/2+1$ and $E_k=H^k\times H^{k-1}$.
  Its Bessel-unitary free matrix is
  \[
    \begin{pmatrix}
      \cos(t|\xi|)&\langle\xi\rangle\sin(t|\xi|)/|\xi|\\
      -|\xi|\sin(t|\xi|)/\langle\xi\rangle&\cos(t|\xi|)
    \end{pmatrix}.
  \]
  The zero sine quotient is $t$; finite-horizon bounds and dominated
  Fourier convergence give a strongly continuous group on $E_k$.
  Leibniz and the derivative-norm equivalence, obtained by expanding
  $(1+|\xi|^2)^{k-1}$ and Parseval, give
  \[
    \|b(t)f\|_{H^{k-1}}
    \le C_k\max_{|j|\le k-1}\|\partial^jb(t)\|_\infty
    \|f\|_{H^{k-1}} .
  \]
  Thus $B(b(t))$ is a norm-continuous bounded force on $E_k$,
  with a finite uniform sample bound $B_L$.
  For $Z_0=S(t)z$ and
  $Z_{n+1}(t)=\int_0^tS(t-r)B(b(r))Z_n(r)\ud r$,
  \[
    \sup_{t\le L}\|Z_n(t)\|_{E_k}
    \le C_L^{n+1}B_L^nL^n\|z\|_{E_k}/n! .
  \]
  This series converges in $C_tE_k$.
  Iterating a homogeneous Volterra difference proves uniqueness.
  Its continuous embedding into $E$ and ordinary $E$ uniqueness
  identify the sum with $P_E^{\epsilon,\tau}(t,0)z$.

  Fourier Cauchy--Schwarz gives
  $\|\widehat f\|_1\le\|f\|_{H^k}
  (\int\langle\xi\rangle^{-2k}\ud\xi)^{1/2}<\infty$.
  Fourier inversion and dominated convergence imply continuous bounded
  displacement, and the same holds for velocity since $k-1>d/2$.
  The source derivatives on the compact support form a measurable
  $C_tC_x^{k-1}$ random element, by countable evaluations and continuity.
  Picard iteration and local norm estimates make its phase sum measurable
  in $C_tE_k$; the Fourier embedding gives joint measurability.
  These high norms are used only at positive source widths.

  The first component of Duhamel is, distributionally,
  \[
    v(t)=\cos(t\sqrt{-\Delta})\psi+
    \int_0^t G_d(t-r)*[b(r)v(r)]\ud r .
  \]
  Here $G_d(h)$ is the positive Green measure of mass $h$
  and support in $B_h$, including the sphere measure for $d=3$.
  The product $bv$ is continuous compactly supported, with finite
  uniform $L^1$ and supremum bounds.
  Against a compact smooth $\phi$, absolute Fubini is bounded by
  $\int_0^t\|\phi\|_\infty\|b(r)v(r)\|_1(t-r)\ud r<\infty$.
  Writing $G_d(h)$ as $h$ times the dilation of its unit-time
  probability measure proves continuity of the convolution term.
  The free term is continuous by the Fourier embedding.
  Thus the distributional identity agrees everywhere with the
  pointwise continuous mild versions.
  No Green density in $d=3$ or raw Sobolev point trace is used.
  This proves Lemma~\ref{L:point-compact-source}.
\end{proof}

\begin{proposition}[Cone identity and an average of squares]
  \label{P:point-source-cone}
  Let $u_{\epsilon,\tau}^{\rm full}$ be the unmasked source solution
  with coefficient $gY_{\rm fast}$ and data $(1,0)$.
  At the fixed parameters, almost surely,
  \[
    v_{\epsilon,\tau}=u_{\epsilon,\tau}^{\rm full}
    \quad\hbox{on }\mathcal C=
    \{(t,x):0\le t\le L,\ |x|\le1+L-t\}.
  \]
  Consequently
  \begin{equation}\label{E:point-source-square-average}
    \E\|\operatorname{pr}_1P_E^{\epsilon,\tau}(L,0)z\|_{L^2(D)}^2
    =v_d\,\E|u_{\epsilon,\tau}^{\rm full}(L,0)|^2<\infty .
  \end{equation}
\end{proposition}

\begin{proof}
  Proposition~\ref{P:masked-source-moments}, applied through the exact
  source law of Lemma~\ref{L:point-fast-sources}, gives the locally
  continuous measurable full solution and its $L^2$ point Picard sum.
  The pathwise cone argument uses the realized pullback field; the point
  second moments depend only on its Gaussian covariance through those
  Bochner chain sums.
  We place no global unmasked field in $E$ or $F$.
  The cone is causally closed: a predecessor at distance at most $t-s$
  has norm at most $1+L-s$.
  Its spatial projection lies a positive distance inside the plateau
  of both $\psi$ and $m$.

  The total initial difference $(\psi-1,0)$ is represented in
  $E$ plus constants by $(\psi,0)+(-1,0)$.
  Every entry of the full free phase kernel is a compactly supported
  distribution in $B_t$, and the top-left is $\partial_tG_d(t)$.
  Since $|x|+t\le1+L=R-1$ on the cone, its entire translated
  kernel support lies in the region where this total datum vanishes.
  Lemma~\ref{L:constant-phase-free} therefore gives
  $\cos(t\sqrt{-\Delta})\psi(x)=1$ there.
  Testing the $E$ and constant summands separately would not give
  this total finite-propagation statement.

  The two mild equations have the same coefficient on the cone.
  For their difference $w$, causal closure gives the homogeneous
  Green integral equation there.
  Put $H=\sup_{\mathcal C}|w|$ and
  $M=\sup_{\mathcal C}|gY_{\rm fast}|$, both finite sample constants.
  Iteration with the positive Green measures gives
  $|w(t,x)|\le HM^nt^{2n}/(2n)!$.
  Indeed the mass recursion is $f_0=1$,
  $f_{n+1}(t)=\int_0^t(t-r)f_n(r)\ud r=t^{2n+2}/(2n+2)!$.
  The factorial ratio forces this bound to zero on the fixed cone.
  No positivity of the sample coefficient or expectation of a global
  source supremum is required.

  At time $L$ the cone contains $D$.
  Tonelli and spatial stationarity of the unmasked single-source law
  give~\eqref{E:point-source-square-average}.
  Finiteness is the full source point-moment bound.
  This is an integral of squares, not a squared average or
  a covariance comparison with a masked model.
  Events are for each fixed $\delta,\epsilon,\tau$.
  This proves Proposition~\ref{P:point-source-cone}.
\end{proof}

\begin{proposition}[Exact original point transfer and polynomial cost]
  \label{P:original-point-transfer}
  For every original model, including zero covariance,
  \begin{align}
    \E|u_\Gamma(T_\delta,0)|^2
    &=v_d^{-1}\E\|\operatorname{pr}_1P_\delta z\|_{L^2(D)}^2,
    \label{E:original-point-transfer}\\
    &\le v_d^{-1}\|\psi\|_{H^{1/2}}^2\E\|P_\delta\|^2,\notag\\
    \limsup_{T\to\infty}T^{-\kappa}\log\E|u_\Gamma(T,x)|^2
    &\le\limsup_{\delta\downarrow0}\delta\log\E\|P_\delta\|^2
    \quad\hbox{for every fixed }x .
    \label{E:original-point-rate-reduction}
  \end{align}
\end{proposition}

\begin{proof}
  Assume nonzero covariance until the last paragraph, and fix $\delta$.
  Equation~\eqref{E:point-source-flow-limit} gives
  convergence of the source displacement in $L^2(\Omega;L^2(D))$,
  since $\|\operatorname{pr}_1e\|_{L^2(D)}\le\|e\|_E$.
  Expected squared norms converge by Cauchy--Schwarz applied to their
  difference times their sum.
  Separately, the full source point-moment limit
  \eqref{E:masked-unmasked-moment-limit} at covariance $\Gamma_\delta$
  gives convergence of the right side of
  \eqref{E:point-source-square-average} to
  $v_d\E|u_{\Gamma_\delta}(L,0)|^2$.
  Both cutoffs $(\epsilon,\tau/\delta)$ tend to zero at fixed $\delta$.
  Thus the two limits in the equal prelimit moments give
  \[
    \E|u_{\Gamma_\delta}(L,0)|^2
    =v_d^{-1}\E\|\operatorname{pr}_1P_\delta z\|_{L^2(D)}^2 .
  \]

  The law normalization is the consequence of
  Lemma~\ref{L:exact-canonical-scaling} and the canonical-series
  time change proved in Proposition~\ref{P:raw-block-point-comparison}.
  Explicitly, for $\delta=T^{-\kappa}$ and $r_T=T\delta$,
  $V_\delta$ has the law of $u_\Gamma(Tt,r_Tx)$ and equation
  \eqref{E:exact-fast-equation}.
  At positive source widths, $U(t,x)=V_\delta(\delta t,x)$ has
  coefficient $\sqrt\delta\,Y_{\epsilon,\tau}(\delta t,x)
  =gY_{\rm fast}(t,x)$.
  The fixed-order and absolutely convergent canonical-series
  argument passes this time change to the point moment at fixed $\delta$.
  Hence $\E|u_\Gamma(T_\delta,0)|^2=\E|u_{\Gamma_\delta}(L,0)|^2$.
  This is a law/moment identity, not a pathwise same-noise identity.
  It preserves all mixed, unequal, self and empty Stratonovich chains
  and the Green-before-noise convention in $d=3$.
  The shrinking $r_T$ is not the mask radius $R$;
  no spatial Jacobian occurs at point zero.
  The phase/operator inequality now proves~\eqref{E:original-point-transfer}.

  Parseval and the inhomogeneous Bessel weights give, for $R\ge1$,
  \[
    \|\psi\|_{H^{1/2}}^2\le\|\psi\|_{H^1}^2
    =R^d\|\eta\|_2^2+R^{d-2}\|\nabla\eta\|_2^2
    \le C_\eta R^d,\quad C_\eta=\|\eta\|_2^2+\|\nabla\eta\|_2^2>0.
  \]
  This includes the negative $d-2$ power in $d=1$.
  For $\operatorname{DataPref}_\delta=v_d^{-1}C_\eta(\delta^{-1}+2)^d$,
  \[
    \delta\log\operatorname{DataPref}_\delta
    =\delta\log(C_\eta/v_d)+d\delta[\log(1+2\delta)-\log\delta]\to0 .
  \]
  The nontrivial term follows by $t=-\log\delta$ and
  $te^{-t}\to0$, since $e^t\ge t^2/2$.
  The original point moment is at least one: its nonnegative full
  pairing expansion contains the unit empty pair of chains.
  It is finite by~\eqref{E:original-point-transfer} and
  \eqref{E:point-fixed-finiteness}.
  Thus logs are defined without subtracting infinite quantities.
  Since $\alpha<2<3$, $a<1$, we have $\kappa>1$ and
  $\delta\mapsto T_\delta$ is a decreasing bijection
  $(0,1)\to(1,\infty)$ with inverse $\delta=T^{-\kappa}$.
  Taking logs and this change of parameter proves
  \eqref{E:original-point-rate-reduction} at zero.
  Original canonical spatial stationarity, proved in
  Proposition~\ref{P:raw-block-original-lower}, extends it to every fixed $x$;
  no stationarity of the masked operator is assumed.

  For zero covariance, $u=1$, all drivers vanish and $P_\delta=S_E(L)$.
  The same total free cone argument gives the spatial-square identity.
  Lemma~\ref{L:symplectic-free} gives $\|S_E(L)\|\ge1$,
  and its Fourier matrix gives $\|S_E(L)\|\le C(1+L)$.
  Thus $0\le\delta\log\|S_E(\delta^{-1})\|^2\to0$ and
  both claims hold directly without a nonzero-noise import.
  This proves Proposition~\ref{P:original-point-transfer}.
\end{proof}

===== END TEX FILE: notes/integrated_point_transfer.tex =====

===== BEGIN TEX FILE: notes/integrated_signed_moment_upper.tex =====
\section{The original upper bound by a moving signed raw score}
\label{S:original-signed-score-upper}

Keep all auxiliary choices fixed as in the Gaussian tube construction,
including $\alpha/4<s_{\rm sp}<1/2$, the admissible $\theta,\nu,r,p$,
and the three fixed even-$Q$ guards.
The mean bound $C_{\rm mean}$ is independent of $R,B,\delta$;
it may depend on those fixed auxiliary parameters and the model.
The space $H_I$ has the ORIGINAL covariance $\Gamma$.
Its norm is not reweighted by $g$ and is not a sum of fast block costs.
Let $R_\delta=\delta^{-1}+2$ and
$M_\delta=\E\|P_\delta\|_{\mathcal L(E)}^2$.
For every fixed integer $B$ the actual Gaussian block tuple has typical
radius $b_{\delta,B}=2\E\|X_{\delta,B}\|_{\delta,p}\to0$.
Its endpoint is the same $P_\delta$ for every $B$ by
Lemma~\ref{L:tube-actual-endpoint}, not a $B$-dependent surrogate.
Write $\mathcal M_{\delta,B,R}$ for the normalized actual mean tuple
in~\eqref{E:tube-actual-mean}, with the indicated block length and radius.
Write $\mathcal F_{\delta,B}$ for the everywhere-defined endpoint
functional $F_\delta$ of Lemma~\ref{L:tube-actual-endpoint}.

\begin{lemma}[Signed score and quantitative radial envelope]
  \label{L:signed-score-envelope}
  For $R\ge1$ define the own score
  \begin{equation}\label{E:signed-raw-score}
    \mathcal S_R=\sup_{\Phi\in H_I}
    \{2\operatorname{Rate}_R(\Phi)-\|\Phi\|_{H_I}^2/2\},
    \qquad V_{\rm up}=\limsup_{\delta\downarrow0}\mathcal S_{R_\delta}.
  \end{equation}
  Then $0\le\mathcal S_R,V_{\rm up}\le2+2C_{\rm mean}^2<\infty$.
  The actual tube envelope $G_{\delta,B}$ of
  Proposition~\ref{P:tube-coarse-envelope} satisfies, uniformly in
  $R\ge1$ (in particular at the actual stochastic radius $R_\delta$),
  \begin{equation}\label{E:signed-polynomial-envelope}
    G_{\delta,B}(\rho)\le A_0+A_1B^{3\nu}\rho^\nu
    +\eta_B b_{\delta,B}^\nu ,
  \end{equation}
  for $0<\delta<\min(1,1/B)$ and every $\rho\ge0$, where
  \[
    \begin{aligned}
      A_0&=4C_{\rm gr},\\
      A_1&=2^{\nu+1-\nu/r}C_{\rm gr}32^\nu C_{\rm mean}^\nu,\\
      \eta_B&=2^{\nu+1-\nu/p}C_{\rm gr}B^{\nu/p}.
    \end{aligned}
  \]
  The score is not identified here with an author constant or a positive score.
\end{lemma}

\begin{proof}
  The mean is linear, so $\mathcal T_R0=0$.
  Its free form has nonnegative gradient energy and spectral bottom zero;
  thus $\operatorname{Rate}_R(0)=0$.
  Proposition~\ref{P:uniform-rate-averaging} gives
  $\operatorname{Rate}_R(\Phi)\le1+C_{\rm mean}\|\Phi\|$.
  With $q=\|\Phi\|\ge0$,
  \[
    2\operatorname{Rate}_R(\Phi)-q^2/2
    \le2+2C_{\rm mean}q-q^2/2
    =2+2C_{\rm mean}^2-(q-2C_{\rm mean})^2/2 .
  \]
  The coarser inequality also follows from half-weight
  arithmetic--geometric mean at bases $q^2,(2C_{\rm mean})^2$,
  with nonnegative weights and bases, including zeros.
  The zero control gives the lower bound.
  No optimizer, finite rank, positive control or convergence of
  $\mathcal S_{R_\delta}$ is assumed.
  The finite ceiling is auxiliary-parameter dependent and need not be sharp.

  For $\|a\|_{\delta,p}\le b_{\delta,B}$, $\|\Phi\|\le\rho$ set
  $v_m=\|a_m\|_\theta$ and
  $h_m=\|(\mathcal M_{\delta,B,R}\Phi)_m\|_\theta$.
  The quantitative physical bound~\eqref{E:uniform-product-growth},
  already including the free factor, and convexity give
  \[
    \mathcal F_{\delta,B}(a+\mathcal M_{\delta,B,R}\Phi)
    \le2C_{\rm gr}B\delta n
    +2^\nu C_{\rm gr}B\delta\sum_m(v_m^\nu+h_m^\nu).
  \]
  Its upper expression is nonnegative, so it controls the maximum at one.
  The true primitive estimate and weighted power mean give
  \begin{align*}
    \delta\sum v_m^\nu&\le(2/B)^{1-\nu/p}b_{\delta,B}^\nu,\\
    \delta\sum h_m^\nu&\le(2/B)^{1-\nu/r}
    (32B^{3-1/r}C_{\rm mean}\rho)^\nu .
  \end{align*}
  The exponents are $p/\nu\ge1$, $r/\nu>1$, inputs nonnegative,
  $n=N+1\ge2$, $\delta>0$, and $\delta n\le2/B$.
  Zeros and $p=\nu$ are legal.
  The first constant is $4C_{\rm gr}$.
  In the mean term the factors $B^{\nu/r}$ and $B^{-\nu/r}$
  cancel exactly, leaving $B^{3\nu}$.
  These computations give the displayed coefficients and
  \eqref{E:signed-polynomial-envelope}, uniformly for all radii.
  They use no unspecified $c_Y(B)$ or quantitative $F$ estimate.
  This proves Lemma~\ref{L:signed-score-envelope}.
\end{proof}

\begin{proposition}[Finite-delta bulk and exact tail]
  \label{P:signed-moment-bulk-tail}
  For fixed integer $B\ge1$, $0<\delta<\min(1,1/B)$ and $M>0$,
  define the deterministic number
  \[
    \mathcal E_{\delta,B,M}=
    \max\left(0,\sup_{\substack{R\ge1,\ \|\Phi\|\le M\\
    \|x\|_{\delta,p}\le b_{\delta,B}}}
    [\mathcal F_{\delta,B}(x+\mathcal M_{\delta,B,R}\Phi)
    -2\operatorname{Rate}_R(\Phi)]\right).
  \]
  It is finite. For every polynomial
  $M_B=c_{\rm ball}B^{\kappa_{\rm ball}}$, with $c_{\rm ball}>0$,
  $\kappa_{\rm ball}\ge0$, one has
  \begin{equation}\label{E:signed-error-limit}
    e_B:=\limsup_{\delta\downarrow0}\mathcal E_{\delta,B,M_B}
    \ \text{finite and nonnegative},\qquad e_B\longrightarrow0 .
  \end{equation}
  If $4A_1B^{3\nu}\le M^{2-\nu}$, then
  \begin{equation}\label{E:signed-finite-moment}
    M_\delta\le
    \frac{M^2}{2\delta}
    e^{(\mathcal S_{R_\delta}+\mathcal E_{\delta,B,M})/\delta}
    +4e^{(A_0+\eta_Bb_{\delta,B}^\nu-M^2/4)/\delta}.
  \end{equation}
\end{proposition}

\begin{proof}
  The polynomial envelope and nonnegative rate make this supremum
  finite. It is an ordinary deterministic real number, not a
  random uncountable-radius supremum.
  At fixed $R$ the inner functions are continuous in controls and paths;
  no measurable maximizing selector or joint $\delta,R$ measurability is needed.
  The zero control and zero path have rate zero and
  $\mathcal F_{\delta,B}(0)\ge0$, so the untruncated supremum
  is already nonnegative.
  The actual anchor $b_{\delta,B}\to0$ at fixed $B$ satisfies
  Proposition~\ref{P:uniform-arbitrary-residual} exactly.
  Its polynomial-radius conclusion gives $\limsup_B e_B\le0$.
  At fixed $B$, the polynomial envelope bounds the inner limsup by
  a finite number, and $e_B\ge0$ then proves~\eqref{E:signed-error-limit}.

  The exact actual-law tube bound is
  \[
    M_\delta\le\int_0^\infty\frac{\rho}{\delta}
    e^{(G_{\delta,B}(\rho)-\rho^2/2)/\delta}\ud\rho .
  \]
  For every $\rho\le M$, every actual base-ball $a$ and
  $\|\Phi\|\le\rho$,
  \[
    \mathcal F_{\delta,B}(a+\mathcal M_{\delta,B,R_\delta}\Phi)-\rho^2/2
    \le2\operatorname{Rate}_{R_\delta}(\Phi)-\|\Phi\|^2/2
    +\mathcal E_{\delta,B,M}
    \le\mathcal S_{R_\delta}+\mathcal E_{\delta,B,M}.
  \]
  Taking suprema and integrating $\rho/\delta$ over $[0,M]$
  gives the first term of~\eqref{E:signed-finite-moment},
  even if $M^2/(2\delta)<1$.
  This used $\rho^2\ge\|\Phi\|^2$, not equality or an optimizer.
  For the tail apply Lemma~\ref{L:tube-rayleigh-tail} with
  $C=A_1B^{3\nu}$ and intercept $A_0+\eta_Bb_{\delta,B}^\nu$.
  All cutoff guards hold: $M>0$, $\rho\ge M$, $C\ge0$,
  $1<\nu<2$, $4C\le M^{2-\nu}$.
  Its analytic integration retains both the front factor four
  and the exponent $-M^2/4$.
  Adding bulk and tail proves the finite-delta bound.
  No infinite-dimensional density or Laplace principle is used.
  This proves Proposition~\ref{P:signed-moment-bulk-tail}.
\end{proof}

\begin{proposition}[Two limits on the same actual moment]
  \label{P:signed-operator-upper}
  The actual global operator moment obeys
  \[
    0\le\liminf_{\delta\downarrow0}\delta\log M_\delta
    \le\limsup_{\delta\downarrow0}\delta\log M_\delta
    \le V_{\rm up}\le2+2C_{\rm mean}^2 .
  \]
\end{proposition}

\begin{proof}
  Choose any $c_{\rm ball}>0$ and
  $\kappa_{\rm ball}>3\nu/(2-\nu)$, and set
  $M_B=c_{\rm ball}B^{\kappa_{\rm ball}}$.
  The cutoff in Proposition~\ref{P:signed-moment-bulk-tail}
  holds for all sufficiently large integers $B$.
  For $A_1=0$ this is immediate; otherwise its side ratio is
  \[
    \frac{M_B^{2-\nu}}{4A_1B^{3\nu}}
    =\frac{c_{\rm ball}^{2-\nu}}{4A_1}
    B^{\kappa_{\rm ball}(2-\nu)-3\nu}\longrightarrow\infty .
  \]
  Both constants and the strictly positive exponent are retained.
  At such a fixed $B$, a positive sum is at most twice its larger term.
  Taking $\delta\log$ of~\eqref{E:signed-finite-moment} therefore gives
  \begin{align*}
    \delta\log M_\delta\le\delta\log2+
    \max\{&
    \mathcal S_{R_\delta}+\mathcal E_{\delta,B,M_B}
    +\delta\log(M_B^2/(2\delta)),\\
    &A_0+\eta_Bb_{\delta,B}^\nu-M_B^2/4+\delta\log4\}.
  \end{align*}
  At fixed $B$, $b_{\delta,B}\to0$.
  All logarithmic normalizers vanish, including
  $\delta\log(M_B^2/(2\delta))
  =\delta\log(M_B^2/2)-\delta\log\delta\to0$.
  The last limit follows from $te^{-t}\le2/t$ for $t=-\log\delta>0$.
  Finite score and error bounds permit limsup subadditivity, giving
  \[
    \limsup_{\delta\downarrow0}\delta\log M_\delta
    \le\max\{V_{\rm up}+e_B,\ A_0-M_B^2/4\}.
  \]
  The left side has no $B$: actual restart identifies every block
  product with this SAME $P_\delta$.
  Now let integer $B\to\infty$. We have $e_B\to0$, $M_B\to\infty$
  and finite $V_{\rm up}\ge0$.
  This gives the asserted upper bound, while $M_\delta\ge1$
  gives the nonnegative lower bound.
  The order was $\delta$ first at fixed block length, ball and thresholds,
  then $B$; no diagonal or limit of $\mathcal S_{R_\delta}$ was assumed.
  This proves Proposition~\ref{P:signed-operator-upper}.
\end{proof}

\begin{proposition}[The original point upper by the own signed score]
  \label{P:original-signed-point-upper}
  For every original admissible model and every fixed $x$,
  \[
    \limsup_{T\to\infty}T^{-\kappa}
    \log\E|u_\Gamma(T,x)|^2
    \le\limsup_{\delta\downarrow0}\mathcal S_{\delta^{-1}+2}
    \le2+2C_{\rm mean}^2 .
  \]
  For zero covariance the two normalized moments and the signed score
  have rate zero.
\end{proposition}

\begin{proof}
  Proposition~\ref{P:original-point-transfer} bounds the original
  point moment by $\operatorname{DataPref}_\delta M_\delta$,
  with $\delta\log\operatorname{DataPref}_\delta\to0$.
  Its source-first, full-chain and canonical law proof is the input here,
  not a raw $E$ point trace.
  The decreasing bijection $T_\delta=\delta^{-1/\kappa}$ has inverse
  $\delta=T^{-\kappa}$. Take logs, normalized limsup and
  Proposition~\ref{P:signed-operator-upper}.
  Original canonical spatial stationarity from
  Proposition~\ref{P:raw-block-original-lower} gives every fixed $x$.
  The moment is at least one by its full expansion and finite by the bound,
  so no logarithm or difference of infinite quantities is hidden.

  For $\Gamma=0$ set $C_{\rm mean}=0$ directly.
  Then $H_I=\{0\}$, $\operatorname{Rate}_R=\mathcal S_R=V_{\rm up}=0$,
  $u=1$ and $P_\delta=S_E(\delta^{-1})$.
  The free lower and upper bounds give
  $0\le\delta\log M_\delta
  \le2\delta\log[C(1+\delta^{-1})]\to0$.
  This direct proof needs no nonzero Gaussian or nondegenerate
  Cameron assumption; the free functional at zero may exceed zero.
  The formal $a\downarrow0$ exponent is $(4-\alpha)/(3-\alpha)$,
  with no new endpoint-in-$a$ theorem asserted.
  The Jensen and lower bounds remain valid.
  This proves Proposition~\ref{P:original-signed-point-upper}.
\end{proof}

The moving score remains an own signed raw variational value.
Its positive-control comparison, exact limit and identification of the
derived constant require the subsequent variational arguments.

===== END TEX FILE: notes/integrated_signed_moment_upper.tex =====

===== BEGIN TEX FILE: notes/integrated_positive_gram.tex =====
\section{Finite optimization with nonnegative Gram entries}
\label{S:finite-positive-gram}

Let $H$ be any real Hilbert space, $\mathcal I$ a finite index set,
$k_i\in H$, $\ell_i>0$ and $b_i\ge0$.
Write $C_{ij}=\langle k_i,k_j\rangle$ and assume $C_{ij}\ge0$ for every
pair. The Gram matrix is symmetric and positive semidefinite, since
$\sum_{i,j}a_iC_{ij}a_j=\|\sum_i a_i k_i\|^2$.
Put $t_+=\max(t,0)$ and define
\begin{equation}\label{E:finite-gram-score}
  \mathfrak F_C(\Phi)
  =2\sum_{i\in\mathcal I}\ell_i
  \sqrt{(\langle\Phi,k_i\rangle-b_i)_+}-\|\Phi\|^2/2,
  \qquad \mathscr S(C)=\sup_{\Phi\in H}\mathfrak F_C(\Phi).
\end{equation}
Let $\mathcal J=\{i:k_i\ne0\}=\{i:C_{ii}>0\}$.
Zero labels contribute zero because $b_i\ge0$.
Empty index sets, singular Grams and $H=\{0\}$ are allowed.
For nonempty $A\subset\mathcal J$ and $w_i>0$, set
\begin{equation}\label{E:finite-gram-dual}
  D_A^C(w)=\sum_{i\in A}\frac{\ell_i^2}{w_i}
  -\sum_{i\in A}b_iw_i
  +\frac12\sum_{i,j\in A}w_iC_{ij}w_j,
  \qquad d_A^C=\inf_{w_i>0}D_A^C(w).
\end{equation}
Set $d_\varnothing^C=0$.

\begin{lemma}[Scalar and Hilbert identities]\label{L:gram-scalar-algebra}
  For real $\ell$, $w>0$ and $t\ge0$,
  \begin{equation}\label{E:gram-sqrt-dual}
    2\ell\sqrt t\le\ell^2/w+wt.
  \end{equation}
  For $\Phi,z\in H$,
  \begin{equation}\label{E:gram-hilbert-square}
    \langle\Phi,z\rangle-\|\Phi\|^2/2
    =\|z\|^2/2-\|\Phi-z\|^2/2\le\|z\|^2/2.
  \end{equation}
  For finite real $w_i$,
  $\|\sum_iw_ik_i\|^2=\sum_{i,j}w_iC_{ij}w_j$.
\end{lemma}

\begin{proof}
  Since $\sqrt w>0$ and $\sqrt{wt}=\sqrt w\sqrt t$,
  \[
    0\le(\ell/\sqrt w-\sqrt{wt})^2
    =\ell^2/w+wt-2\ell\sqrt t.
  \]
  This includes $t=0$. If $\ell,t>0$, equality holds for
  $w=\ell/\sqrt t$.
  Expanding $\|\Phi-z\|^2$ proves~\eqref{E:gram-hilbert-square}.
  Bilinearity of the real inner product proves the finite Gram identity.
  These identities use neither compactness of a Hilbert ball nor an
  inverse covariance matrix.
  This proves Lemma~\ref{L:gram-scalar-algebra}.
\end{proof}

\begin{lemma}[Interior dual minimum]\label{L:gram-dual-minimum}
  Each nonempty $A\subset\mathcal J$ has a unique positive minimizer
  $w^A$ of $D_A^C$. At this minimizer,
  \begin{equation}\label{E:gram-dual-stationarity}
    \sum_{j\in A}C_{ij}w_j^A-b_i
    =\frac{\ell_i^2}{(w_i^A)^2}>0,\qquad i\in A.
  \end{equation}
\end{lemma}

\begin{proof}
  Put $c_i=C_{ii}>0$ and $K_A=\sum_{i\in A}b_i^2/c_i$.
  Nonnegative entries and positive weights give
  \[
    D_A^C(w)\ge
    \sum_i\left(\ell_i^2/w_i-b_iw_i+c_iw_i^2/2\right).
  \]
  Completing the square in $c_iw_i^2/4-b_iw_i$ yields
  \begin{equation}\label{E:gram-dual-coercivity}
    D_A^C(w)\ge
    \sum_i\ell_i^2/w_i+\frac14\sum_i c_iw_i^2-K_A.
  \end{equation}
  Thus no coordinate can approach zero or infinity in a bounded sublevel
  while a different negative term hides its growth.
  Take $w^0=(1,\ldots,1)$, $d_0=D_A^C(w^0)$ and $L_A=d_0+K_A$.
  Equation~\eqref{E:gram-dual-coercivity} at $w^0$ gives
  $L_A\ge\sum_i\ell_i^2+\sum_i c_i/4>0$.
  Every $w$ with $D_A^C(w)\le d_0$ satisfies
  \[
    \ell_i^2/L_A\le w_i\le\sqrt{4L_A/c_i}.
  \]
  The sublevel is nonempty and closed inside this compact box, which
  lies in the open positive orthant. A minimizing sequence chosen in
  the sublevel has a convergent subsequence there. Continuity attains
  its infimum. Outside this sublevel the values exceed $d_0$, so the
  minimum is global on the entire positive orthant.

  The function is smooth in that orthant.
  Its Hessian on a nonzero vector $\xi$ has value
  \[
    \sum_i\frac{2\ell_i^2}{w_i^3}\xi_i^2
    +\sum_{i,j}\xi_iC_{ij}\xi_j>0.
  \]
  The first term is strictly positive and the second is a squared
  Hilbert norm. Restriction to any nonconstant line segment is
  strictly convex, proving uniqueness.
  Each coordinate permits both signs of a small perturbation at the
  interior minimum. Differentiation gives
  $-\ell_i^2/w_i^2-b_i+\sum_jC_{ij}w_j=0$.
  This is~\eqref{E:gram-dual-stationarity}.
  This proves Lemma~\ref{L:gram-dual-minimum}.
\end{proof}

\begin{proposition}[Positive conic maximizer]\label{P:gram-positive-optimizer}
  The finite real value in~\eqref{E:finite-gram-score} satisfies
  \begin{equation}\label{E:gram-active-duality}
    \mathscr S(C)=\max_{A\subset\mathcal J}d_A^C .
  \end{equation}
  If a maximizing subset is empty, $\Phi=0$ attains the score.
  If a maximizing subset $A$ is nonempty, a maximizer is
  $\Phi_A=\sum_{i\in A}w_i^A k_i$ with strictly positive coefficients.
  No uniqueness of the primal maximizer or maximizing subset is asserted.
\end{proposition}

\begin{proof}
  For arbitrary $\Phi$, let
  $A(\Phi)=\{i:\langle\Phi,k_i\rangle>b_i\}$.
  It is contained in $\mathcal J$.
  All other score terms vanish, including equality at the threshold.
  If $A(\Phi)$ is empty, $\mathfrak F_C(\Phi)=-\|\Phi\|^2/2\le0$.
  Otherwise, for any positive $w$ on $A=A(\Phi)$, set
  $t_i=\langle\Phi,k_i\rangle-b_i>0$ and $z=\sum_{i\in A}w_ik_i$.
  Lemma~\ref{L:gram-scalar-algebra} gives
  \[
    \mathfrak F_C(\Phi)
    \le\sum_i\ell_i^2/w_i-\sum_i b_iw_i
    +\langle\Phi,z\rangle-\|\Phi\|^2/2
    \le D_A^C(w).
  \]
  This holds for every positive $w$, so
  $\mathfrak F_C(\Phi)\le d_A^C$.
  There are finitely many subsets and their values are finite by
  Lemma~\ref{L:gram-dual-minimum}.
  Taking the supremum bounds $\mathscr S(C)$ above by their maximum.

  Conversely, $\mathfrak F_C(0)=0=d_\varnothing^C$.
  For nonempty $A$, take its dual minimizer.
  Equation~\eqref{E:gram-dual-stationarity} makes every label in $A$
  strictly active at $\Phi_A$, with
  $\sqrt{\langle\Phi_A,k_i\rangle-b_i}=\ell_i/w_i^A$.
  Both inequalities in the preceding display are then equalities
  for the sum restricted to $A$, since $z=\Phi_A$.
  This restricted score equals $d_A^C$.
  All omitted labels contribute nonnegative terms to the full score,
  hence $\mathfrak F_C(\Phi_A)\ge d_A^C$, even if this value is negative.
  Maximizing over $A$, including the empty set, proves
  \eqref{E:gram-active-duality} and the asserted attainment.
  For a maximizing nonempty subset the upper and lower bounds force
  $\mathfrak F_C(\Phi_A)=d_A^C$; no outside inactivity was assumed.
  All-zero labels give $\mathscr S(C)=0$ directly.
  This proves Proposition~\ref{P:gram-positive-optimizer}.
\end{proof}

\begin{lemma}[Real Gram realization]\label{L:gram-realization}
  Every finite real symmetric positive semidefinite matrix is the Gram
  matrix of vectors in a finite-dimensional real Hilbert space.
  When its entries are nonnegative, the value $\mathscr S(C)$ is
  independent of its realization.
\end{lemma}

\begin{proof}
  Induct on the size, with the empty matrix realized in $\{0\}$.
  Diagonal entries are nonnegative.
  If all vanish, testing on $e_i+t e_j$ gives $2tC_{ij}\ge0$ for
  every real $t$, hence $C=0$, realized by zero vectors.
  Otherwise permute a positive diagonal $c$ into the first position
  and write $C=\left[\begin{smallmatrix}c&v^{\mathsf T}\\v&A\end{smallmatrix}\right]$.
  The Schur complement $B=A-vv^{\mathsf T}/c$ is positive semidefinite:
  test the original quadratic form on $(-v^{\mathsf T}y/c,y)$.
  Realize $B$ by vectors $u_i$ using the induction hypothesis.
  Then $k_1=(\sqrt c,0)$ and
  $k_i=(v_i/\sqrt c,u_i)$ for the other indices realize $C$.
  Undo the permutation.
  Entries of $B$ need not be nonnegative; this construction requires
  neither nonnegative coordinates nor complete positivity.

  In any realization, $C_{ii}=0$ means $k_i=0$, so its entire row
  vanishes. Formula~\eqref{E:gram-active-duality} depends only on
  $C,\ell,b$ and these eligible indices. It therefore proves
  realization independence whenever the entries are nonnegative,
  which is the scope in which $\mathscr S(C)$ is used.
  This proves Lemma~\ref{L:gram-realization}.
\end{proof}

\begin{proposition}[Entrywise Gram comparison]\label{P:gram-entrywise-comparison}
  Let $C,D$ be real symmetric positive semidefinite matrices on the
  same finite index set, with $0\le C_{ij}\le D_{ij}$.
  With the same $\ell_i>0,b_i\ge0$,
  \[
    \mathscr S(C)\le\mathscr S(D).
  \]
  No positive-semidefinite order on $D-C$ is required.
\end{proposition}

\begin{proof}
  Lemma~\ref{L:gram-realization} defines both values.
  Their eligible sets satisfy $\mathcal J_C\subset\mathcal J_D$.
  For nonempty $A\subset\mathcal J_C$ and positive weights,
  \[
    D_A^D(w)-D_A^C(w)
    =\frac12\sum_{i,j\in A}w_i(D_{ij}-C_{ij})w_j\ge0.
  \]
  Taking infima gives $d_A^C\le d_A^D$.
  The empty values are both zero.
  Taking maxima and using the inclusion of eligible families proves
  the claim by Proposition~\ref{P:gram-positive-optimizer}.
  This includes the appearance of previously zero labels.
  This proves Proposition~\ref{P:gram-entrywise-comparison}.
\end{proof}

\begin{remark}[Exact checks and scope]\label{R:gram-controls}
  The empty value is essential: for one label with $C=1$,
  $\ell=1/10,b=4$, the nonempty dual has
  $D(4)=-3199/400<0$, whereas the primal score at zero is zero.
  Global concavity is unavailable: for $k=\ell=b=1$ the score
  $2\sqrt{(\phi-1)_+}-\phi^2/2$ decreases on $[0,1]$ and has infinite
  positive right slope at one.
  For $k=\ell=1,b=0$, differentiation on $\phi>0$ gives the maximum
  $3/2$ at $\phi=1$; on $\phi\le0$ the score is nonpositive.
  Doubling the cost changes the positive critical point to $2^{-2/3}$
  and the maximum to $3\,2^{-4/3}$.
  Finally $C=I_2$, $D=\left[\begin{smallmatrix}1&1/2\\1/2&1\end{smallmatrix}\right]$
  are nonnegative positive semidefinite Grams but $D-C$ has eigenvalues
  $1/2,-1/2$. These are finite analytic checks, not a covariance-order
  theorem for physical waves.

  The scalar, finite Gram, conditional active upper and half-quadratic
  entrywise deductions have existing local Lean certificates at their
  exact hypotheses. Dual coercivity, calculus, attainment, realization
  and the infimum/maximum argument above remain analytic proofs.
  No new kernel fact or formalization of the physical application follows
  merely from these certificates.
\end{remark}

===== END TEX FILE: notes/integrated_positive_gram.tex =====

===== BEGIN TEX FILE: notes/integrated_intrinsic_constant.tex =====
\section{The positive-control formula for the original moment limit}
\label{S:intrinsic-second-moment}

Retain every original covariance and amplitude.
Write $a=\alpha_0$, $I=(0,1)$, $K(s,t)=|s-t|^{-a}$ and
$H_I=H_t\otimes H_{\mathrm{sp}}$ for the original raw covariance.
Keep the uniform $E$ mean $\mathcal T_R=T_R(C_t\otimes I)$ and
$C_{\rm mean}=M_0\|C_t\|$ of Section~\ref{S:uniform-physical-products},
with exactly the fixed $r$ chosen there. In particular $2<r<2/a$.
To distinguish it from the map below, write $J_R=T_R$.
For a bounded multiplier $V:H^{1/2}\to H^{-1/2}$ write
$B_E(V)(u,v)=(0,Vu)$, the actual $E$ operator of
Lemma~\ref{L:uniform-E-lift}.
The physical mask is $m_R=\eta(\cdot/R)^2$, used once.
Let $\mathcal C_{\mathrm{pos}}$ be the full nonseparable class
in~\eqref{E:variational-positive-class}.
For $\Psi$ in that class, retain its unmasked mean $h_{\Psi,s}$,
raw variance $v_\Psi$, integrated full-gradient rate $I_\Psi$ and
positive scores $S_c^{\mathrm{pos}}$ from
Section~\ref{S:unmasked-variational}.
No first-moment or author-constant interpretation of the label one
is assumed.
We assume $\Gamma\ne0$ through the following comparison lemmas.
The theorem treats zero covariance directly.

\begin{lemma}[Raw inclusion and the actual smooth mean]
  \label{L:positive-raw-embedding}
  For any real Hilbert space $G$ there is a bounded map
  $J_G:L^2(I;G)\to H_t\otimes G$ with
  \begin{equation}\label{E:positive-bochner-inclusion}
    \|J_GF\|^2
    =\int_{I^2}K(s,t)\langle F(s),F(t)\rangle_G\ud s\ud t
    \le K_0\|F\|_{L^2(I;G)}^2,\qquad K_0=\frac{2^a}{1-a}.
  \end{equation}
  The natural inclusion puts every $\Psi\in\mathcal C_{\mathrm{pos}}$
  in $H_I$, with
  \begin{equation}\label{E:positive-raw-mean}
    \|\Psi\|_{H_I}^2=v_\Psi,\qquad
    \mathcal T_R\Psi(s)=B_E(m_Rh_{\Psi,s})\quad\hbox{a.e. }s.
  \end{equation}
  For each fixed smooth $\Psi$ the right side gives a canonical
  version for every $R\ge1$ and every $s\in I$.
\end{lemma}

\begin{proof}
  Direct integration and concavity of $x^{1-a}$ give
  \[
    \int_I K(s,t)\ud t
    =\frac{s^{1-a}+(1-s)^{1-a}}{1-a}\le K_0 .
  \]
  For scalar $f\ge0$, Cauchy--Schwarz against $K(s,t)\ud t$ and then
  Tonelli give $\|Kf\|_2\le K_0\|f\|_2$.
  The same estimate for absolute values bounds the bilinear integral
  by $K_0\|f\|_2\|g\|_2$.
  Approximate scalar $L^2(I)$ functions by real $C_c^\infty(I)$
  functions. This bound makes their raw test-null classes Cauchy
  in $H_t$, defines the bounded inclusion, and identifies its pairing
  with the integral. Finite $G$-valued tensors then give
  \eqref{E:positive-bochner-inclusion}. Simple fields are dense in
  Bochner $L^2(I;G)$; the same bound on differences extends $J_G$.
  Absolute bilinear continuity extends the integral identity as well.

  For $G=H_{\mathrm{sp}}$, the Bochner integral
  $\int_IK(s,t)F(t)\ud t$ exists almost everywhere: its norm is
  bounded by $K\|F\|(s)$, which belongs to $L^2$.
  Simple-field approximation and the Schur estimate give a strongly
  measurable $L^2$ version and a bounded map of norm at most $K_0$.
  On smooth finite tensors it agrees with
  $(C_t\otimes I)J_G$ by the actual covariance definition.
  Approximation by such tensors converges in $L^2(I;G)$.
  The integral converges there by Schur; the completed tensor map
  converges in $L^r(I;G)$ by Lemma~\ref{L:uniform-mean-tensor}
  and~\eqref{E:positive-bochner-inclusion}, hence also in $L^2$.
  Uniqueness of the $L^2$ limit identifies these versions.
  In particular the integral belongs to $L^r$.

  Choose a closed ball $B$ containing all spatial supports of $\Psi$.
  For real smooth $q$ supported there, the physical covariance gives
  \begin{equation}\label{E:positive-local-spatial-bound}
    \|q\|_{H_{\mathrm{sp}}}^2
    \le |B|\,\Gamma(B-B)\|q\|_\infty^2.
  \end{equation}
  Indeed in $\int\ud x\int\Gamma(\ud y)q(x)q(x-y)$ only
  $x\in B,y\in B-B$ contribute. Absolute values and local finiteness
  prove the bound, including white and singular Radon covariances.
  Thus $t\mapsto\Psi_t$ is continuous, bounded and compactly supported
  as an $H_{\mathrm{sp}}$-valued field, and belongs to $L^2$.
  Its image under $J_{H_{\mathrm{sp}}}$ is the original raw test class
  of $\Psi$. Indeed, the separated compact smooth approximants in
  Lemma~\ref{L:cameron-supported-tensor} converge uniformly on one common
  compact support. The local bound above and the temporal Schur estimate
  give convergence both in $L^2(I;H_{\mathrm{sp}})$ and in the original
  covariance norm. Their finite tensor identifications therefore have
  this same limit.
  Formula~\eqref{E:positive-bochner-inclusion} and absolute Fubini give
  \[
    \|\Psi\|_{H_I}^2
    =\int_{I^2}K(s,t)\langle\Psi_s,\Psi_t\rangle_{H_{\mathrm{sp}}}
    \ud s\ud t
    =\int_{I\times\R^d}\Psi(s,x)h_{\Psi,s}(x)\ud x\ud s=v_\Psi.
  \]
  The compact spatial supports and~\eqref{E:positive-local-spatial-bound}
  make all these absolute integrals finite.

  Test the spatial row~\eqref{E:uniform-mean-row} first with displacement
  $f$ and dual second component $\Lambda g$, with $f,g$ compact smooth.
  The row product is $m_Rfg$, so the preceding temporal identity gives
  \[
    \left\langle\int_IK(s,t)\Psi_t\ud t,m_Rfg\right\rangle_{H_{\mathrm{sp}}}
    =\int m_Rh_{\Psi,s}fg .
  \]
  This Fubini step has two fixed compact supports and integrable time
  kernel. Both resulting operators are bounded on $E$: the left by
  the mean theorem, the right by the bounded smooth $h_{\Psi,s}$
  and compact smooth mask. Dense states extend the identity to $E$.
  For this fixed $\Psi$ the temporal integral exists at every $s$,
  with norm at most $K_0\sup_t\|\Psi_t\|_{H_{\mathrm{sp}}}$.
  Applying $J_R$ gives the explicit version in
  \eqref{E:positive-raw-mean} for every $R,s$.
  For each $R$ it agrees with the completed $L^r$ mean class.
  This makes no simultaneous-version assertion over all rough controls.
  This proves Lemma~\ref{L:positive-raw-embedding}.
\end{proof}

\begin{lemma}[Actual finite labels and entrywise order]
  \label{L:positive-physical-gram}
  Take a finite partition of $I$ with nonempty cells $I_i$,
  lengths $\ell_i>0$ and $\sum_i\ell_i=1$, and real
  $f_i\in C_c^\infty(\R^d)$ with $\|f_i\|_2=1$.
  Put
  \[
    h_i=\mathbf1_{I_i}/\ell_i,\quad b_i=\|\nabla f_i\|_2^2,\quad
    k_i^R=h_i\otimes(m_Rf_i^2),\quad
    k_i^\infty=h_i\otimes f_i^2 .
  \]
  These are elements of $H_I$. If $v_L$ is the multiplier form
  of~\eqref{E:uniform-E-pairing}, then for every $\Phi\in H_I$,
  \begin{equation}\label{E:positive-label-row}
    \langle\Phi,k_i^R\rangle_{H_I}
    =\ell_i^{-1}\int_{I_i}v_{\mathcal T_R\Phi(s)}(f_i,f_i)\ud s .
  \end{equation}
  The Grams $C^R_{ij}=\langle k_i^R,k_j^R\rangle$ and
  $D_{ij}=\langle k_i^\infty,k_j^\infty\rangle$ satisfy
  $0\le C^R_{ij}\le D_{ij}$ entrywise.
\end{lemma}

\begin{proof}
  Lemma~\ref{L:positive-raw-embedding} puts $h_i$ in $H_t$.
  The compact smooth spatial factors lie in $H_{\mathrm{sp}}$
  by its test definition and~\eqref{E:positive-local-spatial-bound}.
  On a smooth finite tensor, use~\eqref{E:uniform-mean-row}
  with $z=(f_i,0)$ and $w=(0,\Lambda f_i)$.
  Its row is $(\eta_Rf_i)(\eta_R\Lambda^{-1}\Lambda f_i)=m_Rf_i^2$.
  Temporal integration gives the pairing with $h_i$.
  This proves~\eqref{E:positive-label-row} on dense tensors.
  Its right side is a bounded raw functional, with bound
  $\ell_i^{-1/r}C_{\rm mean}\|\Phi\|\|f_i\|_{H^{1/2}}^2$
  by Hölder and~\eqref{E:uniform-completed-mean}.
  The left side is bounded by Hilbert Cauchy--Schwarz.
  Thus the identity extends to the completed $H_I$.
  The form is the actual displacement form by
  Lemma~\ref{L:uniform-E-lift}.

  Each Gram is symmetric positive semidefinite.
  Its entries factor into the temporal pairing of nonnegative
  $h_i,h_j$ and the physical spatial covariance pairing.
  The kernels $K,\Gamma$ and $f_i^2,f_j^2$ are nonnegative;
  $0\le m_R\le1$. Tonelli therefore gives the entrywise order.
  The physical pairing already contains $\Gamma$, and the row
  cancellation introduces no additional Fourier factor.
  Zero labels are permitted.
  All hypotheses of Proposition~\ref{P:gram-entrywise-comparison}
  are met, without assuming $D-C^R$ is positive semidefinite.
  This proves Lemma~\ref{L:positive-physical-gram}.
\end{proof}

\begin{lemma}[Uniform optimizer norm and positive smoothing]
  \label{L:positive-uniform-optimizer}
  Put $M=4C_{\rm mean}+4$.
  The supremum defining $\mathcal S_R$ may be restricted to
  $\|\Phi\|\le M$, uniformly in $R$.
  For every finite trial family in Lemma~\ref{L:positive-physical-gram},
  the unmasked finite score has a maximizer $\Phi_D$ with
  $\|\Phi_D\|\le M$. It is zero or is a positive conic combination
  of the $k_i^\infty$. In the latter case it is approximable in $H_I$
  by tests in $\mathcal C_{\mathrm{pos}}$.
\end{lemma}

\begin{proof}
  Put $C=C_{\rm mean}$ and $q=\|\Phi\|$.
  Proposition~\ref{P:uniform-rate-averaging} gives
  \[
    2\operatorname{Rate}_R(\Phi)-q^2/2
    \le2+2Cq-q^2/2<2-2q<0\quad(q>M).
  \]
  The zero control gives zero, proving the restriction.

  Denote the finite unmasked objective by $\mathfrak F_D$.
  Proposition~\ref{P:gram-positive-optimizer} supplies an attained
  maximum at zero or a positive conic sum $\Phi_D$.
  Choose a finite $R'\ge1$ whose plateau contains all supports of $f_i$.
  Then $k_i^{R'}=k_i^\infty$.
  Write $W_i=\ell_i^{-1}\int_{I_i}\mathcal T_{R'}\Phi(s)\ud s$.
  The row identity and real Rayleigh formula imply, for every $\Phi$,
  \begin{align*}
    \mathfrak F_D(\Phi)
    &\le2\sum_i\ell_i\lambda(W_i)-q^2/2\\
    &\le2+2\sum_i\ell_i\|W_i\|-q^2/2
    \le2+2Cq-q^2/2 .
  \end{align*}
  For fixed $f_i$, the map $L\mapsto v_L(f_i,f_i)$ is bounded linear;
  hence the form of the Bochner average is the average form.
  Here $\lambda(L)\le\max(1,\|L\|)\le1+\|L\|$,
  the norm of an average is bounded by the average norm, and
  the $L^1$ mean norm is at most its $L^r$ norm.
  No time-averaging error or concavity of the positive-part square root
  enters this estimate. Since the maximum is nonnegative, its optimizer
  lies in the same ball of radius $M$, independently of the partition,
  profiles and $R'$.

  On a nonzero branch write
  $\Phi_D=\sum_{i\in A}w_i h_i\otimes f_i^2$, with $w_i>0$.
  Extend $h_i$ by zero, convolve with a nonnegative compact smooth
  approximate identity, and multiply by smooth cutoffs
  $0\le\chi_j\le1$ compactly supported in $I$, tending pointwise to one.
  The resulting nonnegative $h_{i,j}\in C_c^\infty(I)$ converge to $h_i$
  in $L^2$: the error is bounded by the convolution error plus
  $\|(\chi_j-1)h_i\|_2$, which tends to zero by domination.
  Set $\Psi_j=\sum_{i\in A}w_i h_{i,j}f_i^2$.
  Finite tensor estimates and~\eqref{E:positive-bochner-inclusion}
  give $\Psi_j\to\Phi_D$ in $H_I$.
  The positive conic sum has positive squared norm, since at least
  one eligible diagonal is positive and all Gram entries are nonnegative.
  Thus $\Psi_j\ne0$ eventually, so $\Psi_j\in\mathcal C_{\mathrm{pos}}$.
  Costs converge.
  The integrated rate continuity proved in
  Proposition~\ref{P:uniform-rate-averaging} gives
  \begin{equation}\label{E:positive-rate-continuity}
    |\operatorname{Rate}_{R'}(\Psi_j)-\operatorname{Rate}_{R'}(\Phi_D)|
    \le\sqrt{3+C\|\Psi_j\|+C\|\Phi_D\|}
    \sqrt{C\|\Psi_j-\Phi_D\|}\longrightarrow0 .
  \end{equation}
  This estimate is uniform in $R'$.
  It asserts no uniform derivative bound on the smooth approximants.
  The zero branch will use $S_2^{\mathrm{pos}}\ge0$ directly.
  This proves Lemma~\ref{L:positive-uniform-optimizer}.
\end{proof}

\begin{proposition}[Signed scores bounded by the positive score]
  \label{P:positive-signed-comparison}
  For every $R\ge1$,
  \begin{equation}\label{E:positive-signed-comparison}
    \mathcal S_R\le S_2^{\mathrm{pos}} .
  \end{equation}
\end{proposition}

\begin{proof}
  Use uniform partitions with $n\ge2$ cells of length $1/n$.
  They are the $B=1,\delta=1/n$ partitions in
  Proposition~\ref{P:uniform-rate-averaging}, with the empty last cell omitted.
  That proposition gives $e_n\to0$, independent of $R$, such that
  \[
    \left|\operatorname{Rate}_R(\Phi)
    -\sum_i\ell_i\lambda\left(\ell_i^{-1}
    \int_{I_i}\mathcal T_R\Phi(s)\ud s\right)\right|\le e_n
    \quad(\|\Phi\|\le M).
  \]
  Fix $R,\Phi,n$, with $\|\Phi\|\le M$, and denote these averages by $W_i$.
  Real compact smooth unit trials are dense in the real $H^1$ unit sphere:
  truncate by cutoffs tending to one, whose gradient errors tend to zero,
  then mollify in $H^1$ and normalize in $L^2$.
  Continuity of the multiplier form in $H^{1/2}$ and hence $H^1$
  proves
  \[
    \lambda(W_i)=
    \sup_{\substack{f\in C_c^\infty(\R^d;\R)\\\|f\|_2=1}}
    \sqrt{(v_{W_i}(f,f)-\|\nabla f\|_2^2)_+}.
  \]
  The real Rayleigh supremum is nonnegative by
  Proposition~\ref{P:uniform-E-spectral}, so the positive part
  does not change its supremum.
  For $\varepsilon>0$ choose one near-maximizing $f_i$ per cell
  with error at most $\varepsilon$ in the square root.
  This is a finite choice, not a measurable continuum optimizer.
  Since $\sum_i\ell_i=1$, the weighted trial error contributes
  $2\varepsilon$ to the next inequality.
  Lemma~\ref{L:positive-physical-gram} gives
  \[
    2\operatorname{Rate}_R(\Phi)-\|\Phi\|^2/2
    \le\mathfrak F_{C^R}(\Phi)+2e_n+2\varepsilon .
  \]
  Optimize this finite objective and use entrywise Gram comparison:
  \[
    \mathfrak F_{C^R}(\Phi)
    \le\mathscr S(C^R)\le\mathscr S(D)=\mathfrak F_D(\Phi_D).
  \]
  This compares optimized values, not the same individual control.
  Lemma~\ref{L:positive-uniform-optimizer} proves
  $\|\Phi_D\|\le M$ before time averaging is used again.
  Choose $R'$ covering the finite supports as in that lemma.
  The label row, Rayleigh bound and the same uniform averaging estimate give
  \begin{equation}\label{E:positive-finite-optimizer-bound}
    \mathfrak F_D(\Phi_D)
    \le2\operatorname{Rate}_{R'}(\Phi_D)-\|\Phi_D\|^2/2+2e_n .
  \end{equation}

  If $\Phi_D=0$, its finite score is zero.
  Otherwise use its positive smooth approximants $\Psi_j$.
  Lemma~\ref{L:positive-raw-embedding} identifies their actual mean
  with $B_E(m_{R'}h_{\Psi_j,s})$ and their raw cost with $v_{\Psi_j}$.
  Since $h_{\Psi_j,s}\ge0$ and $0\le m_{R'}\le1$, real $H^1$ form order gives
  $\operatorname{Rate}_{R'}(\Psi_j)\le I_{\Psi_j}$.
  Thus
  $2\operatorname{Rate}_{R'}(\Psi_j)-\|\Psi_j\|^2/2
  \le S_2^{\mathrm{pos}}$.
  Rate and cost convergence pass this inequality to $\Phi_D$.
  Together with~\eqref{E:positive-finite-optimizer-bound} and the
  separate zero branch this yields
  \[
    2\operatorname{Rate}_R(\Phi)-\|\Phi\|^2/2
    \le S_2^{\mathrm{pos}}+4e_n+2\varepsilon .
  \]
  All finite choices were made after fixing $n,R,\Phi$.
  The right side is independent of those choices.
  Let $\varepsilon\downarrow0$, take the supremum over the raw ball,
  use Lemma~\ref{L:positive-uniform-optimizer}, and then let $n\to\infty$.
  This proves~\eqref{E:positive-signed-comparison}.
  Finiteness of the positive score was already proved from the
  independent old canonical upper in
  Proposition~\ref{P:variational-positive-scores}, not from this conclusion.
  This proves Proposition~\ref{P:positive-signed-comparison}.
\end{proof}

\begin{proposition}[Cutoff removal for the optimized score]
  \label{P:positive-score-cutoff}
  The possibly nonmonotone mask family satisfies
  \[
    \lim_{R\to\infty}\mathcal S_R=S_2^{\mathrm{pos}}.
  \]
\end{proposition}

\begin{proof}
  Fix $\Psi\in\mathcal C_{\mathrm{pos}}$ before taking $R$ or moment limits.
  Use the explicit mean version of Lemma~\ref{L:positive-raw-embedding}.
  Its rate $\lambda_R(s)$ obeys
  $0\le\lambda_R(s)\le\lambda_{\Psi,s}$ by real form order.
  For each real compact smooth unit $f$, $m_R=1$ on its support for
  every sufficiently large $R$. The Rayleigh formula therefore gives
  \[
    \liminf_{R\to\infty}\lambda_R(s)^2
    \ge\int h_{\Psi,s}f^2-\|\nabla f\|_2^2.
  \]
  Compact trial density and~\eqref{E:variational-real-rayleigh}
  identify the supremum of the right side as $\lambda_{\Psi,s}^2$.
  Hence $\lambda_R(s)\to\lambda_{\Psi,s}$ for these versions.
  The global smooth-source bound
  $H_\Psi=\sup_{s,x}h_{\Psi,s}(x)<\infty$ gives
  $\lambda_R(s)\le\sqrt{H_\Psi}$.
  Dominated convergence yields
  $\operatorname{Rate}_R(\Psi)\to I_\Psi$.
  Neither monotonicity of $m_R$ nor an unmasked ground eigenfunction was used.

  The raw representative and cost $\|\Psi\|^2=v_\Psi$ are independent of $R$.
  Thus
  $\liminf_R\mathcal S_R\ge2I_\Psi-v_\Psi/2$ for each fixed test.
  Given $\varepsilon>0$, choose one fixed test with score greater than
  $S_2^{\mathrm{pos}}-\varepsilon$; the finite supremum admits such a test.
  Take the liminf and then $\varepsilon\downarrow0$.
  Proposition~\ref{P:positive-signed-comparison} supplies the reverse limsup.
  This proves Proposition~\ref{P:positive-score-cutoff}.
\end{proof}

\begin{theorem}[Intrinsic original second-moment constant]
  \label{T:intrinsic-second-moment}
  For every original admissible model with data $(1,0)$ and fixed $x$,
  \begin{equation}\label{E:intrinsic-second-moment-limit}
    \lim_{T\to\infty}T^{-(4-\alpha-a)/(3-\alpha)}
    \log\E|u_\Gamma(T,x)|^2
    =C_2(\Gamma,a)=S_2^{\mathrm{pos}}
    =2^{(4-\alpha)/(3-\alpha)}S_1^{\mathrm{pos}}.
  \end{equation}
  Its complete positive-control formula is
  \begin{align}
    C_2(\Gamma,a)
    &=\sup_{\Psi\in\mathcal C_{\mathrm{pos}}}
    \left\{2\int_I
    \sqrt{\sup_{\substack{f\in H^1(\R^d;\R)\\\|f\|_2=1}}
    \left(\int h_{\Psi,s}f^2-\|\nabla f\|_2^2\right)}
    \ud s-\frac{v_\Psi}{2}\right\},
    \label{E:intrinsic-positive-formula}\\
    h_{\Psi,s}(x)
    &=\int_I|s-t|^{-a}(\Gamma*\Psi_t)(x)\ud t,\qquad
    v_\Psi=\int_{I\times\R^d}\Psi(s,x)h_{\Psi,s}(x)\ud x\ud s.
    \notag
  \end{align}
  Here $\mathcal C_{\mathrm{pos}}$ consists of all nonzero nonnegative
  real $C_c^\infty(I\times\R^d)$ tests, including nonseparable ones.
  The covariance retains its actual amplitude, the kinetic term has
  coefficient one, and the Gaussian action is $v_\Psi/2$.
  For nonzero covariance $0<C_2<\infty$.
  For $\Gamma=0$ the constant and moment rate are zero.
\end{theorem}

\begin{proof}
  Assume first $\Gamma\ne0$.
  Proposition~\ref{P:original-signed-point-upper}, followed by
  Proposition~\ref{P:positive-score-cutoff} with $R=\delta^{-1}+2$,
  bounds the original point limsup by $S_2^{\mathrm{pos}}$.
  Proposition~\ref{P:variational-positive-scores} bounds the original
  point liminf below by this same value.
  Both are for the same canonical Stratonovich solution, exponent,
  original covariance and variance-half action.
  Their source-first identifications retain all mixed, unequal, self
  and empty chains and both phase components with initial data $(1,0)$.
  The original spatial stationarity proved in
  Proposition~\ref{P:raw-block-original-lower} extends both bounds to
  every fixed $x$.
  Thus the limit exists and equals $S_2^{\mathrm{pos}}$.
  Its homogeneity, positivity and finiteness are
  Proposition~\ref{P:variational-positive-scores}.
  Formula~\eqref{E:variational-real-rayleigh} and the definition of the
  original raw variance give~\eqref{E:intrinsic-positive-formula}.

  If $\Gamma=0$, $H_I=\{0\}$, all means, variances and rates vanish,
  $\mathcal S_R=S_c^{\mathrm{pos}}=0$, and $u=1$.
  Both formulas are direct zero identities.
  This proves Theorem~\ref{T:intrinsic-second-moment}.
\end{proof}

The label-one score is auxiliary; the theorem does not identify it with
an actual first-moment limit or with Chen's printed constants.
It neither repairs a source energy normalization nor asserts a Jensen
improvement. The exponent formally tends to $(4-\alpha)/(3-\alpha)$
as $a\downarrow0$; no interchange with the static moment limit is claimed.
The explicit bounds and full calibration are separate from this
identification.

===== END TEX FILE: notes/integrated_intrinsic_constant.tex =====

===== BEGIN TEX FILE: notes/integrated_occupation_ceiling.tex =====
\section{Occupation bounds for the intrinsic constant}
\label{S:intrinsic-occupation-ceiling}

Retain all original models and amplitudes, put $a=\alpha_0$,
$q=4-\alpha>2$, $k=3-\alpha=q-1>1$ and $m=q/k$.
The temporal kernel is $K(s,t)=|s-t|^{-a}$ on $I=(0,1)$;
its diagonal value may be set to zero.
Let $\mathcal O$ be the full strongly $H^1$-measurable unit-profile
class defined before Proposition~\ref{P:occupation-physical-class}.
Here we use the \emph{raw} kernel, defining
\begin{equation}\label{E:raw-occupation-definitions}
  \begin{aligned}
    A(g)&=\int_{I^2}K(s,t)B_\Gamma(g_s^2,g_t^2)\ud s\ud t,\\
    C_{\rm occ}&=\sup_{g\in\mathcal O}
    \frac{A(g)}{T(g)^{\alpha/2}},&
    \mathcal E_\zeta^{\mathcal O}
    &=\sup_{g\in\mathcal O}\{A(g)-\zeta T(g)\},\qquad \zeta>0.
  \end{aligned}
\end{equation}
The scalar penalty $\zeta$ is not a spatial mask.
These objects differ from the earlier damped-kernel energy.
Assume $\Gamma\ne0$ until the direct zero case below.

\begin{lemma}[Full-profile squares in the original raw space]
  \label{L:occupation-raw-square}
  There is a continuous map $Q:H^1(\R^d;\R)\to H_{\mathrm{sp}}$ with
  \[
    \langle Q(f),Q(h)\rangle_{H_{\mathrm{sp}}}
    =B_\Gamma(f^2,h^2),\qquad
    \|Q(f)\|^2=A_{\mathrm{sp}}(f).
  \]
  For $g\in\mathcal O$, the element
  $\rho_g=J_{H_{\mathrm{sp}}}(s\mapsto Q(g_s))$ belongs to the original
  $H_I$ and satisfies
  \begin{equation}\label{E:occupation-raw-identities}
    \|\rho_g\|_{H_I}^2=A(g),\qquad
    \langle\Psi,\rho_g\rangle_{H_I}
    =\int_I\int_{\R^d}h_{\Psi,s}(x)g_s(x)^2\ud x\ud s
  \end{equation}
  for every $\Psi\in\mathcal C_{\mathrm{pos}}$. In particular,
  \[
    \langle\Psi,\rho_g\rangle_{H_I}\le\sqrt{v_\Psi A(g)}.
  \]
\end{lemma}

\begin{proof}
  Approximate $f$ in $H^1$ by real compact smooth $f_n$.
  Proposition~\ref{P:spatial-four-linear} gives
  \[
    \|f_n^2-f_l^2\|_{H_{\mathrm{sp}}}^2
    =C_4(f_n-f_l,f_n+f_l,f_n-f_l,f_n+f_l)
    \le R_{\mathrm{sp}}N(f_n-f_l)^2N(f_n+f_l)^2\to0.
  \]
  Here $N$ is continuous on $H^1$ and $N(f)\le\|f\|_{H^1}$.
  Completeness defines $Q(f)$; interlacing two approximating sequences
  proves independence. Passing the physical four-linear continuity
  and Hilbert pairings to limits proves the first identities.
  The same difference bound, first for smooth approximants and then
  by passage to the limit, proves continuity of $Q$.

  Thus $F_g(s)=Q(g_s)$ is strongly measurable.
  Writing $b_s=\|\nabla g_s\|_2^2$, the unit norm and
  $0<\alpha/2<1$ give
  \[
    \int_I\|F_g(s)\|^2\ud s
    \le R_{\mathrm{sp}}\int_I b_s^{\alpha/2}\ud s
    \le R_{\mathrm{sp}}T(g)^{\alpha/2}<\infty .
  \]
  Lemma~\ref{L:positive-raw-embedding} now constructs $\rho_g$ and
  identifies its squared norm with the physical $A(g)$.
  Joint measurability and representative independence follow from
  the continuous physical pairing on $(H^1)^2$.
  Absolute time integrability follows from the same Schur bound.

  Choose one compact smooth $\chi$ equal to one on all spatial
  supports of $\Psi_t$. For real $f\in H^1$, smooth approximation gives
  \[
    \langle\Psi_t,Q(f)\rangle_{H_{\mathrm{sp}}}
    =\lim_n B_\Gamma(\Psi_t,f_n^2)
    =C_4(\chi,\Psi_t,f,f)=B_\Gamma(\Psi_t,f^2).
  \]
  Proposition~\ref{P:spatial-four-linear} justifies these absolute
  integrals and limits.
  Polarizing~\eqref{E:positive-bochner-inclusion} gives
  \[
    \langle\Psi,\rho_g\rangle
    =\int_{I^2}K(s,t)\langle\Psi_t,Q(g_s)\rangle_{H_{\mathrm{sp}}}
    \ud t\ud s .
  \]
  The absolute integrand is bounded by the product of two
  $H_{\mathrm{sp}}$ norms against $K$, integrable by Schur and
  $L^2$ Cauchy--Schwarz.
  Evenness of $\Gamma$ and Tonelli for the nonnegative physical
  integrands yield~\eqref{E:occupation-raw-identities}.
  Hilbert Cauchy--Schwarz with $\|\Psi\|^2=v_\Psi$ proves the bound.
  No rough occupation is inserted into a stochastic flow.
  This proves Lemma~\ref{L:occupation-raw-square}.
\end{proof}

\begin{proposition}[Raw occupation energy and dilation]
  \label{P:raw-occupation-energy}
  With $K_0=2^a/(1-a)$,
  \[
    0<C_{\rm occ}\le K_0R_{\mathrm{sp}}<\infty .
  \]
  Moreover
  \begin{align}
    \mathcal E_\zeta^{\mathcal O}
    &=D_\zeta C_{\rm occ}^{2/(2-\alpha)},&
    D_\zeta&=\frac{2-\alpha}{2}
    \left(\frac{\alpha}{2\zeta}\right)^{\alpha/(2-\alpha)},
    \label{E:raw-occupation-energy}\\
    C_{\rm occ}
    &=\left(\frac{2\mathcal E_\zeta^{\mathcal O}}{2-\alpha}\right)^{(2-\alpha)/2}
    \left(\frac{2\zeta}{\alpha}\right)^{\alpha/2}.
    \label{E:raw-occupation-ratio}
  \end{align}
  In particular $\mathcal E_\zeta^{\mathcal O}>0$ is finite and
  equals $\zeta^{-\alpha/(2-\alpha)}\mathcal E_1^{\mathcal O}$.
\end{proposition}

\begin{proof}
  A unit $H^1$ profile has positive gradient energy:
  a zero weak gradient makes it constant, and an $L^2$ constant
  on $\R^d$ is zero. Hence $0<T(g)<\infty$.
  Spatial covariance Cauchy--Schwarz gives
  $B_\Gamma(g_s^2,g_t^2)\le
  R_{\mathrm{sp}}b_s^{\alpha/4}b_t^{\alpha/4}$.
  Schur with row bound $K_0$, then concavity, proves
  \begin{equation}\label{E:raw-occupation-bound}
    0\le A(g)\le K_0R_{\mathrm{sp}}T(g)^{\alpha/2}.
  \end{equation}
  A fixed compact smooth unit profile, constant in time, belongs to
  $\mathcal O$ and has positive $A$ by
  Proposition~\ref{P:spatial-four-linear}. This proves positivity
  and finiteness of $C_{\rm occ}$.

  The map $(U_\ell g)_s(x)=\ell^{d/2}g_s(\ell x)$ is an $H^1$
  isomorphism preserving unit mass and strong measurability.
  It has inverse $U_{1/\ell}$ and is a bijection on $\mathcal O$.
  The physical Radon change of variables gives
  \[
    A(U_\ell g)=\ell^\alpha A(g),\qquad
    T(U_\ell g)=\ell^2T(g).
  \]
  Indeed the two densities contribute $\ell^{2d}$, $\ud x$ contributes
  $\ell^{-d}$, and the pushforward of $\Gamma$ contributes
  $\ell^{\alpha-d}$. Approximation extends the identity to full $H^1$.
  Taking the union over $g,\ell$ leaves the class unchanged.
  For fixed $A,T>0$, the derivative of
  $A\ell^\alpha-\zeta T\ell^2$ has the sign of
  $\alpha A-2\zeta T\ell^{2-\alpha}$.
  Its global maximum occurs at
  $\ell=(\alpha A/(2\zeta T))^{1/(2-\alpha)}$ and equals
  $D_\zeta[A/T^{\alpha/2}]^{2/(2-\alpha)}$.
  For $A=0$ the supremum is zero as $\ell\downarrow0$.
  Bounding every ratio by $C_{\rm occ}$ gives one inequality in
  \eqref{E:raw-occupation-energy}.
  Fixed ratios approaching its positive supremum give the other
  by continuity of the positive power.
  Algebra gives~\eqref{E:raw-occupation-ratio} and the penalty scaling.
  No optimizer or minimax interchange is assumed.
  This proves Proposition~\ref{P:raw-occupation-energy}.
\end{proof}

\begin{lemma}[Countable Rayleigh near-occupations]
  \label{L:occupation-rayleigh-selection}
  For fixed $\Psi\in\mathcal C_{\mathrm{pos}}$ and every $\varepsilon>0$
  there is $g_\varepsilon\in\mathcal O$ such that
  \begin{equation}\label{E:occupation-rayleigh-selection}
    I_\Psi^2+T(g_\varepsilon)
    \le\sqrt{v_\Psi A(g_\varepsilon)}+\varepsilon .
  \end{equation}
\end{lemma}

\begin{proof}
  The real $H^1$ space is separable, for example by its isometric
  embedding $f\mapsto(f,\nabla f)$ into a finite product of $L^2$ spaces.
  Compact smooth density therefore supplies a countable real family.
  Discard zero and normalize each member in $L^2$ to obtain $f_j$
  dense in the $L^2$-unit $H^1$ class. Normalization preserves convergence
  because the approximating $L^2$ norms tend to one.
  Put $b_j=\|\nabla f_j\|_2^2$ and
  $R_j(s)=\int h_{\Psi,s}f_j^2-b_j$.
  Bounded-potential form continuity and
  Proposition~\ref{P:variational-unmasked-rate} give
  $\lambda_{\Psi,s}^2=\sup_jR_j(s)$.
  The canonical functions are measurable, indeed continuous.
  Let $U_j=\{s:R_j(s)>\lambda_{\Psi,s}^2-\varepsilon\}$,
  $A_1=U_1$ and $A_j=U_j\setminus\bigcup_{i<j}U_i$.
  These first-index cells are Borel and cover $I$.
  Put $g_\varepsilon(s)=f_j$ on $A_j$.
  Finite-valued truncations using $f_1$ on the remaining cells
  converge pointwise in $H^1$, proving strong measurability.
  A null-set representative may be filled by $f_1$.

  With $H_\Psi=\sup_{s,x}h_{\Psi,s}(x)<\infty$, the selection implies
  \[
    b(g_\varepsilon(s))
    <\int h_{\Psi,s}g_\varepsilon(s)^2-\lambda_{\Psi,s}^2+\varepsilon
    \le H_\Psi+\varepsilon .
  \]
  Thus it belongs to the actual $\mathcal O$.
  Integrating the near-Rayleigh inequality, using
  Lemma~\ref{L:occupation-raw-square}, gives
  \[
    \int_I\lambda_{\Psi,s}^2\ud s+T(g_\varepsilon)
    \le\langle\Psi,\rho_{g_\varepsilon}\rangle+\varepsilon
    \le\sqrt{v_\Psi A(g_\varepsilon)}+\varepsilon .
  \]
  Time Cauchy--Schwarz on the unit interval gives
  $I_\Psi^2\le\int_I\lambda_{\Psi,s}^2\ud s$.
  This proves~\eqref{E:occupation-rayleigh-selection}.
  No eigenvector, continuum selector or limiting occupation is required.
  This proves Lemma~\ref{L:occupation-rayleigh-selection}.
\end{proof}

For $0\le b<q/2$ define $F_b(0)=0$ and
\begin{equation}\label{E:occupation-scalar-map}
  F_b(z)=k\left[
  \frac{(q-2b)^{(q-2b)/2}}{8(q-b)^{q-b}}
  \left(\frac{2z}{2-\alpha}\right)^{(2-\alpha)/2}
  \right]^{1/k},\qquad z>0.
\end{equation}
At $b=0$ this is exactly the map in~\eqref{E:spatial-static-energy-score}.
The display parameter $b$ does not change the actual temporal exponent $a$.

\begin{theorem}[The computed occupation ceiling]\label{T:intrinsic-occupation-ceiling}
  For every positive score coefficient $\mathfrak c$,
  \begin{align}
    S_{\mathfrak c}^{\mathrm{pos}}
    &\le U_{\mathfrak c}
    :=\mathfrak c^m k
    \left[\frac{\alpha^{\alpha/2}C_{\rm occ}}{8q^{q/2}}\right]^{1/k}
    \label{E:occupation-score-ceiling}\\
    &=\mathfrak c^m(2\zeta)^{\alpha/(2k)}
    F_0(\mathcal E_\zeta^{\mathcal O}),\qquad \zeta>0.\notag
  \end{align}
  In particular the actual original moment constant satisfies
  $C_2(\Gamma,a)\le U_2$ for every original model.
  This ceiling is not asserted to be attained or equal to $C_2$.
\end{theorem}

\begin{proof}
  Fix $\Psi$ and write $v=v_\Psi$, $C=C_{\rm occ}$ and $\beta=\alpha/4$.
  Lemma~\ref{L:occupation-rayleigh-selection} gives
  $I_\Psi^2\le\sqrt{vC}T^\beta-T+\varepsilon$ for some $T>0$.
  Bound it by the supremum over all $T\ge0$ before sending
  $\varepsilon\downarrow0$.
  If $v=0$, that supremum is zero.
  If $v>0$, the derivative
  $\beta\sqrt{vC}T^{\beta-1}-1$ strictly decreases from infinity to $-1$.
  Its unique positive zero is
  $T_*=(\beta\sqrt{vC})^{1/(1-\beta)}$.
  The global maximum equals
  $(q/4)(\alpha/4)^{\alpha/q}(vC)^{2/q}$.
  In both cases,
  \[
    I_\Psi\le Dv^{1/q},\qquad
    D=\sqrt{q/4}(\alpha/4)^{\alpha/(2q)}C^{1/q}.
  \]
  The scalar function $\mathfrak c Dv^{1/q}-v/2$ vanishes at zero,
  tends to minus infinity, and has strictly decreasing derivative.
  Its unique positive maximum is at
  $v_*=(2\mathfrak c D/q)^{q/k}$, with value $kv_*/2$.
  Direct positive-power algebra gives
  \[
    (2D/q)^q=q^{-q/2}(\alpha/4)^{\alpha/2}C .
  \]
  Since $k+\alpha=3$, the maximum is precisely $U_{\mathfrak c}$
  in~\eqref{E:occupation-score-ceiling}, with denominator eight.
  Substitution of~\eqref{E:raw-occupation-ratio} gives the second form,
  retaining the factor $(2\zeta)^{\alpha/(2k)}$.
  Take the supremum over the actual smooth positive-control class.
  Theorem~\ref{T:intrinsic-second-moment} identifies
  $C_2=S_2^{\mathrm{pos}}$, proving the moment ceiling.
  The penalty factor cancels its energy scaling, so the ceiling
  is independent of $\zeta$.
  This proves Theorem~\ref{T:intrinsic-occupation-ceiling}.
\end{proof}

\begin{corollary}[A common spatial-energy bracket]
  \label{C:intrinsic-spatial-bracket}
  With the same original covariance and $M_a$ of
  \eqref{E:temporal-equilibrium-mass},
  \begin{equation}\label{E:intrinsic-spatial-bracket}
    2^m M_a^{-1/k}F_0(\mathcal E_{\mathrm{sp}})
    \le C_2(\Gamma,a)
    \le2^m K_0^{1/k}F_0(\mathcal E_{\mathrm{sp}}).
  \end{equation}
  For $\Gamma\ne0$ there is also the own-energy comparison
  \[
    C_2\le2^mF_0(\mathcal E_{1/2}^{\mathcal O})
    <2^mF_a(\mathcal E_{1/2}^{\mathcal O}).
  \]
\end{corollary}

\begin{proof}
  Insert $C_{\rm occ}\le K_0R_{\mathrm{sp}}$ into
  \eqref{E:occupation-score-ceiling} and use
  \eqref{E:spatial-energy-map}.
  This gives the upper bracket; the lower is
  \eqref{E:spatial-static-energy-score} multiplied by $2^m$,
  using Theorem~\ref{T:intrinsic-second-moment}.
  Both concern one common spatial energy, not an assumed first moment.

  For completeness put
  \[
    \Delta=\tfrac12[q\log q+(q-2a)\log(q-2a)]
    -(q-a)\log(q-a)>0.
  \]
  Here $a>0$ and $q-2a>2-a>1$.
  The existing scalar strict-log-gap deduction applies at exactly
  these guards, without $q\ge3$.
  Equivalently the strict midpoint convexity of $x\log x$ on
  positive arguments, whose second derivative is $1/x$, gives the sign.
  Subtracting logarithms in~\eqref{E:occupation-scalar-map} gives
  \[
    \log(F_a(z)/F_0(z))=\Delta/k,\qquad
    \frac{\mathfrak c^mF_a(\mathcal E_\zeta^{\mathcal O})}{U_{\mathfrak c}}
    =\exp\!\left(\frac{\Delta-(\alpha/2)\log(2\zeta)}{k}\right).
  \]
  At $\zeta=1/2$ this and the ceiling prove the strict comparison.
  At $\zeta=1$ the comparison is not universally favorable.
  For $\alpha=5/4,a=1/2,d=2$,
  \[
    8[\Delta-(\alpha/2)\log2]
    =\log\frac{11^{11}7^7}{2^5 9^{18}}<0,
  \]
  since $11^{11}7^7=234966429149994773$ and
  $2^5 9^{18}=4803028329503971872$.
  This contrasts computed bounds; it refutes no actual moment inequality.
  This proves Corollary~\ref{C:intrinsic-spatial-bracket}.
\end{proof}

For $\Gamma=0$, all raw means and scores vanish and $C_2=0$.
Here $Q=0$, $A=0$ and $C_{\rm occ}=0$.
The supremum of $-\zeta T(g)$ is zero: dilate a fixed unit compact
profile by $\ell^{d/2}f(\ell x)$ and let $\ell\downarrow0$.
The same argument gives $\mathcal E_{\mathrm{sp}}=0$ and the earlier
damped energy zero, without using a zero vector as a unit profile.
With $F_b(0)=0$, every non-strict bound above is the zero identity.
These own energies are not identified with Chen's printed energies.

===== END TEX FILE: notes/integrated_occupation_ceiling.tex =====

===== BEGIN TEX FILE: notes/integrated_white_evaluation.tex =====
\section{Spatial white noise: energy and explicit moment bounds}
\label{S:intrinsic-white-evaluation}

Take $d=\alpha=1$ and $\Gamma=c\delta_0$, $c\ge0$, with temporal kernel
$|s-t|^{-a}$, $0<a<1$, and data $(1,0)$.
The parameter $c$ is covariance mass; the coefficient of unit noise
would be $\sqrt c$. No additional temporal normalization is inserted.
The wave kinetic coefficient is one.
For real unit $f\in H^1(\R)$ put
$A=\int_\R f^4$ and $b=\int_\R(f')^2$.
The physical covariance is $A_{\mathrm{sp}}(f)=cA$.

\begin{lemma}[The full-profile CDF square identity]\label{L:white-cdf-square}
  Every such $f$ has $A<\infty$.
  With $\mathsf F(x)=\int_{-\infty}^xf(y)^2\ud y$, for every real $z$,
  \begin{equation}\label{E:white-cdf-square}
    0\le\int_\R[f'-zf(1-2\mathsf F)]^2
    =b-2zA+z^2/3 .
  \end{equation}
\end{lemma}

\begin{proof}
  On a bounded interval the weak derivative $f'$ is $L^1$ by
  Cauchy--Schwarz. Its integral primitive has weak derivative $f'$
  by Fubini. Subtracting it from $f$ gives a function of weak derivative
  zero, hence constant almost everywhere: test against derivatives
  of compact smooth primitives of all zero-integral test functions.
  The resulting locally absolutely continuous representatives patch on
  overlaps, giving one continuous representative.
  Thus $\rho=f^2$ is locally absolutely continuous with
  $\rho'=2ff'\in L^1(\R)$, while $\rho\ge0$ and $\int\rho=1$.
  Integrability of $\rho'$ makes $\rho$ Cauchy on each infinite tail,
  so it has finite limits at both ends.
  Its $L^1$ integrability forces both limits to be zero.
  It is therefore bounded, and
  $A=\int\rho^2\le\|\rho\|_\infty\int\rho<\infty$.

  Now $0\le\mathsf F\le1$, $\mathsf F'=\rho$ continuously,
  and its limits are zero and one.
  The derivative of $\rho(1-2\mathsf F)$ is
  $\rho'(1-2\mathsf F)-2\rho^2\in L^1$.
  Its endpoint limits vanish.
  Integrating on $[-R,R]$ and sending $R\to\infty$ gives
  \[
    \int_\R f'f(1-2\mathsf F)=A .
  \]
  The polynomial $P(y)=y-2y^2+(4/3)y^3$ has derivative $(1-2y)^2$.
  The chain rule and the endpoints of $\mathsf F$ give
  \[
    \int_\R f^2(1-2\mathsf F)^2=P(1)-P(0)=1/3 .
  \]
  Absolute integrability holds since this integrand is bounded by $f^2$.
  For each real $z$, both terms in the square in
  \eqref{E:white-cdf-square} are in $L^2$, and their cross product is
  absolutely integrable. Expansion and the two preceding identities
  prove the formula. Neither positivity of $f$ nor strict increase
  of its CDF is required.
  This proves Lemma~\ref{L:white-cdf-square}.
\end{proof}

\begin{proposition}[Exact white spatial energy]\label{P:white-spatial-energy}
  For $c>0$,
  \[
    R_{\mathrm{sp}}=c/\sqrt3,\qquad
    \mathcal E_{\mathrm{sp}}=c^2/6.
  \]
  Both values are zero at $c=0$.
\end{proposition}

\begin{proof}
  Substitution $z=3A$ into~\eqref{E:white-cdf-square} gives
  $3A^2\le b$.
  This is the exact premise and conclusion of the existing conditional
  WhiteCDF square deduction.
  Here $A>0$, since $A=0$ would imply $f=0$ a.e.
  Also $b>0$: zero derivative makes its continuous representative
  constant and hence zero in $L^2$, contradicting unit mass.
  Thus $A/\sqrt b\le1/\sqrt3$.

  For $\ell>0$ use the real smooth $H^1$ profile
  $f_\ell(x)=\sqrt{\ell/2}\operatorname{sech}(\ell x)$,
  with $f_\ell'=-\ell\tanh(\ell x)f_\ell$.
  Set $t=\tanh(\ell x)$, so $\ud t=\ell\operatorname{sech}^2(\ell x)\ud x$.
  Direct integration gives
  \[
    \int f_\ell^2=\frac12\int_{-1}^1\ud t=1,\quad
    \int f_\ell^4=\frac\ell4\int_{-1}^1(1-t^2)\ud t=\ell/3,\quad
    \int(f_\ell')^2=\frac{\ell^2}2\int_{-1}^1t^2\ud t=\ell^2/3.
  \]
  The ratio is attained, proving $R_{\mathrm{sp}}=c/\sqrt3$.
  The physical Dirac measure introduces no Fourier constant or
  nonintegrable kernel $|x|^{-1}$.
  The existing conditional energy deduction applies to $3A^2\le b$:
  \[
    cA-b/2\le cA-\tfrac32A^2
    =c^2/6-\tfrac32(A-c/3)^2\le c^2/6 .
  \]
  At $\ell=c>0$ the profile attains $c^2/6$.
  These are full $H^1$ energy profiles; compact approximation equality
  is Proposition~\ref{P:spatial-four-linear}, not a claim that the
  noncompact profile itself is a compact stochastic control.
  At $c=0$ the ratio is zero and the energy is $\sup(-b/2)=0$,
  approached by $f_\ell$ as $\ell\downarrow0$.
  No zero-scale profile is used as a unit vector.
  The CDF, integral and attainment arguments remain analytic;
  the two finite conditional deductions do not formalize them.
  This proves Proposition~\ref{P:white-spatial-energy}.
\end{proof}

\begin{theorem}[Explicit white moment bounds]\label{T:white-moment-bounds}
  For the same original point limit,
  \begin{equation}\label{E:white-moment-bounds}
    \frac23\sqrt{\frac{c}{M_a}}\le C_2(c,a)
    \le\frac23\sqrt{cK_0(a)},\qquad
    K_0(a)=\frac{2^a}{1-a},\quad
    M_a=\frac{\Gamma_E((1+a)/2)}
    {\Gamma_E(1+a)\Gamma_E((1-a)/2)} .
  \end{equation}
  Its time exponent is $(3-a)/2$. These are bounds, not a numerical
  evaluation of the intrinsic supremum.
\end{theorem}

\begin{proof}
  Here $q=3,k=2,m=3/2$.
  Formula~\eqref{E:spatial-static-energy-score} gives
  \[
    F_0(z)=2\left[\frac{(2z)^{1/2}}{8\,3^{3/2}}\right]^{1/2}.
  \]
  For $c>0$, $\sqrt{2\mathcal E_{\mathrm{sp}}}=c/\sqrt3$, hence
  $F_0(\mathcal E_{\mathrm{sp}})=\sqrt c/(3\sqrt2)$ and
  $2^mF_0(\mathcal E_{\mathrm{sp}})=(2/3)\sqrt c$.
  Substitution into Corollary~\ref{C:intrinsic-spatial-bracket}
  proves~\eqref{E:white-moment-bounds} in the original units.
  All Gamma factors are positive finite for $0<a<1$.
  At $c=0$, $u=1$ and $C_2=0$ by
  Theorem~\ref{T:intrinsic-second-moment}; both displayed bounds vanish.
  This proves Theorem~\ref{T:white-moment-bounds}.
\end{proof}

\begin{corollary}[Uniform relative width of the bound formulas]
  \label{C:white-relative-width}
  For $c>0$, the ratio of the upper and lower formulas is
  \[
    \sqrt{K_0(a)M_a}
    \le\left[\frac{\sqrt\pi}{2\Gamma_E(5/4)^2}\right]^{1/2},
  \]
  with equality at $a=1/2$.
\end{corollary}

\begin{proof}
  Duplication and recurrence from Lemma~\ref{L:equilibrium-gamma-beta} give
  \[
    \Gamma_E(1+a)
    =\frac{2^a\Gamma_E((1+a)/2)\Gamma_E(1+a/2)}{\sqrt\pi},
    \qquad
    (1-a)\Gamma_E((1-a)/2)=2\Gamma_E((3-a)/2).
  \]
  Therefore
  \[
    K_0(a)M_a
    =\frac{\sqrt\pi}{2\Gamma_E(1+a/2)\Gamma_E((3-a)/2)} .
  \]
  Put $x=1+a/2$, $y=(3-a)/2$, so $x,y>0$ and $x+y=5/2$.
  In Euler's Gamma integral the $L^2(0,\infty)$ functions
  $t^{(x-1)/2}e^{-t/2}$ and $t^{(y-1)/2}e^{-t/2}$
  have squared norms $\Gamma_E(x),\Gamma_E(y)$ and inner product
  $\Gamma_E(5/4)$.
  Cauchy--Schwarz, positivity, inversion and the increasing square root
  prove the bound. At $a=1/2$, $x=y=5/4$, giving equality.
  Replacing $a$ by $1-a$ exchanges these two arguments, so only this
  ratio of bound formulas is symmetric, not the moment constant or exponent.
  This proves Corollary~\ref{C:white-relative-width}.
\end{proof}

This example retains the all-model theorem rather than replacing its scope.
The formal static exponent is $3/2$ as $a\downarrow0$; no interchange
of long-time and temporal-endpoint limits is asserted.
Jensen holds for the same canonical solution, while $S_1^{\mathrm{pos}}$
remains auxiliary.
The read-only Skorohod comparison at strict spatial Riesz exponent below
one does not cover this spatial-white endpoint.
A separate white-time problem cannot be substituted for $0<a<1$.
No new Skorohod result, source correction or certified decimal enclosure
is claimed.

===== END TEX FILE: notes/integrated_white_evaluation.tex =====
