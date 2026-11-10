# Independent correspondence review: Lean statement ledger vs manuscript

I reviewed all 88 rows against the provided Lean sources (all compile no-sorry; proof correctness not at issue), `claims.yaml`, and the full manuscript (main `.tex` plus every `\input` module). Fidelity of every "What it states" cell to the actual Lean type was checked individually; label mappings were checked against the cited TeX.

## Section A — row-by-row (ledger order)

```
  1 | ActualEvent.finite_error_accumulation          | FIDELITY: OK | MAPPING: OK | recurrence d(n+1)<=C d n+C^n e used verbatim in L:raw-block-restart
  2 | ActualEvent.moderate_penalty                   | FIDELITY: OK | MAPPING: OK | δ·δ^(-3/4)=δ^(1/4) linear penalty in P:raw-block-original-lower
  3 | AllAlphaMoment.moment_lower                    | FIDELITY: OK | MAPPING: ABSENT-CONFIRMED | 2a^2/(D+4a) form not in revision
  4 | AllAlphaMoment.rational_gap                    | FIDELITY: OK | MAPPING: ABSENT-CONFIRMED | D+4a/D+2a rationals not in revision
  5 | ClockFilter.resolvent_partial_fraction         | FIDELITY: OK | MAPPING: OK | (2θ+λ)/(2θ(θ²+r²)((θ+λ)²+r²)) partial fraction in P:clock-copy-obstruction
  6 | ClockFilter.clock_filter_bounds                | FIDELITY: OK | MAPPING: OK | 0<2θ/(2θ+λ)<1 used there
  7 | ClockFilter.strict_filter_integral             | FIDELITY: OK | MAPPING: OK | strict J<K via a.e. positive weight
  8 | DampedLower.exact_margin                       | FIDELITY: OK | MAPPING: ABSENT-CONFIRMED | 9·2^28<157^3·5^4 not in revision
  9 | DampedLower.pi_cube_certificate                | FIDELITY: OK | MAPPING: ABSENT-CONFIRMED | π^3 bound absent
 10 | DampedLower.rational_pi_gain                   | FIDELITY: OK | MAPPING: ABSENT-CONFIRMED | absent
 11 | DimensionalMatrix.backward                     | FIDELITY: OK | MAPPING: ABSENT-CONFIRMED | absent
 12 | DimensionalMatrix.coupling                     | FIDELITY: OK | MAPPING: ABSENT-CONFIRMED | absent
 13 | DimensionalMatrix.forward                      | FIDELITY: OK | MAPPING: ABSENT-CONFIRMED | absent
 14 | DimensionalMatrix.full_interaction             | FIDELITY: OK | MAPPING: ABSENT-CONFIRMED | absent
 15 | DirectEvent.kappa_gt_one                       | FIDELITY: OK | MAPPING: OK | κ>1 only; κ∈(1,2) upper not checked (see F5)
 16 | DirectEvent.physical_scale                     | FIDELITY: OK | MAPPING: OK | r_T=T·δ=T^((a-1)/(3-α)) in L:exact-canonical-scaling
 17 | DirectEvent.noise_scale                        | FIDELITY: OK | MAPPING: OK | T^(-a/2)r_T^(2-α/2)=√δ verbatim
 18 | DirectEvent.vertex_scale                       | FIDELITY: OK | MAPPING: OK | T^(1-a/2)r_T^(1-α/2)=δ^(-1/2) verbatim
 19 | DirectEvent.gauge_inverse                      | FIDELITY: OK | MAPPING: ABSENT-CONFIRMED | no "gauge" in manuscript
 20 | DirectEvent.gauge_drift                        | FIDELITY: OK | MAPPING: ABSENT-CONFIRMED | absent
 21 | DirectEvent.monodromy                          | FIDELITY: OK | MAPPING: ABSENT-CONFIRMED | no monodromy/pulse matrices
 22 | FiniteYoung.weighted_natural_powers            | FIDELITY: OK | MAPPING: OK | exactly E:gaussian-integer-power in L:gaussian-scalar-powers
 23 | GaussianTail.cutoff_density_split              | FIDELITY: OK | MAPPING: OK | guards M,x,C,ν,4C≤M^(2-ν) verbatim in L:tube-rayleigh-tail
 24 | GlobalOmega.envelopePolynomial                 | FIDELITY: OK | MAPPING: ABSENT-CONFIRMED | absent
 25 | GlobalOmega.envelopeDenom                      | FIDELITY: OK | MAPPING: ABSENT-CONFIRMED | absent
 26 | GlobalOmega.envelopeRational                   | FIDELITY: OK | MAPPING: ABSENT-CONFIRMED | absent
 27 | GlobalOmega.left_certificate                   | FIDELITY: OK | MAPPING: ABSENT-CONFIRMED | absent
 28 | GlobalOmega.right_certificate                  | FIDELITY: OK | MAPPING: ABSENT-CONFIRMED | absent
 29 | GlobalOmega.polynomial_pos                     | FIDELITY: OK | MAPPING: ABSENT-CONFIRMED | absent
 30 | GlobalOmega.rational_lt_one                    | FIDELITY: OK | MAPPING: ABSENT-CONFIRMED | absent
 31 | HermiteWord.raw_support                        | FIDELITY: OK | MAPPING: OK | degree-per-color abstraction of L:finite-word-cutoff
 32 | HermiteWord.cut_eq_raw                         | FIDELITY: OK | MAPPING: OK | idem
 33 | InteractionDriver.temporal_range               | FIDELITY: OK | MAPPING: WEAK | certifies only 1-a/2 endpoint of E:driver-parameters (F3)
 34 | InteractionDriver.variance_norm                | FIDELITY: OK | MAPPING: OK | √(C h^(2-a) L²) normalization in L:driver-interval-limit
 35 | InteractionDriver.holder_parameters            | FIDELITY: OK | MAPPING: WEAK | midpoint instance only; paper uses arbitrary η (F4)
 36 | InteractionDriver.dyadic_ratio                 | FIDELITY: OK | MAPPING: OK | 0<2^-(H-m-1/p)<1 ratio (midpoint note)
 37 | InteractionDriver.gaussian_prefactor           | FIDELITY: OK | MAPPING: ABSENT-CONFIRMED | no Gaussian mixture in driver section
 38 | InteractionDriver.gaussian_exponent            | FIDELITY: OK | MAPPING: ABSENT-CONFIRMED | absent
 39 | InteractionDriver.box_margin                   | FIDELITY: OK | MAPPING: ABSENT-CONFIRMED | 2/p; manuscript uses d/Q (F7)
 40 | InteractionDriver.box_scale                    | FIDELITY: OK | MAPPING: ABSENT-CONFIRMED | idem
 41 | JointTilt.tilt_exponent                        | FIDELITY: OK | MAPPING: OK | completing-square scalar core (claims disclaims Gaussian integrals)
 42 | JointTilt.wrong_sign_error                     | FIDELITY: OK | MAPPING: WRONG | not used in P:raw-block-gaussian-law (F1)
 43 | JointTilt.wrong_cost_error                     | FIDELITY: OK | MAPPING: WRONG | not used (F1)
 44 | JointTilt.shifted_amplitude                    | FIDELITY: OK | MAPPING: OK | g_δ·δ^(a/2)=√δ in L:raw-block-inputs
 45 | LocalFlow.noise_order                          | FIDELITY: OK | MAPPING: ABSENT-CONFIRMED | absent
 46 | LocalFlow.schur_row                            | FIDELITY: OK | MAPPING: ABSENT-CONFIRMED | absent
 47 | LocalFlow.schur_column                         | FIDELITY: OK | MAPPING: ABSENT-CONFIRMED | absent
 48 | LocalFlow.schur_rescale                        | FIDELITY: OK | MAPPING: ABSENT-CONFIRMED | absent
 49 | LocalFlow.source_overlap                       | FIDELITY: OK | MAPPING: ABSENT-CONFIRMED | absent
 50 | LocalFlow.source_white_obstruction             | FIDELITY: OK | MAPPING: ABSENT-CONFIRMED | absent
 51 | LocalFlow.source_tail_obstruction              | FIDELITY: OK | MAPPING: ABSENT-CONFIRMED | absent
 52 | MiddleCross.certificate_pos                    | FIDELITY: OK | MAPPING: ABSENT-CONFIRMED | absent
 53 | MiddleCross.parameter_identity                 | FIDELITY: OK | MAPPING: ABSENT-CONFIRMED | absent
 54 | MiddleCross.parameter_numerator_pos            | FIDELITY: OK | MAPPING: ABSENT-CONFIRMED | absent
 55 | MiddleCross.difference_identity                | FIDELITY: OK | MAPPING: ABSENT-CONFIRMED | absent
 56 | MiddleCross.resolvent_difference               | FIDELITY: OK | MAPPING: ABSENT-CONFIRMED | absent
 57 | MiddleCross.root_numerator_pos                 | FIDELITY: OK | MAPPING: ABSENT-CONFIRMED | absent
 58 | MiddleCross.middle_bound                       | FIDELITY: OK | MAPPING: ABSENT-CONFIRMED | absent
 59 | MovingCone.residual_budget                     | FIDELITY: OK | MAPPING: OK | q_B≤1/8, e≤ϑ/4 budget in L:raw-block-indexed-cone
 60 | MovingCone.cone_conversion                     | FIDELITY: OK | MAPPING: OK | (1-ρ)A≤x, y≤ϑA/2 → y≤ϑx verbatim
 61 | MovingCone.terminal_margin                     | FIDELITY: OK | MAPPING: OK | 16Kϑ≤j, 3j/4-2Kϑ-e≤y terminal estimate
 62 | OccupationForm.potential_budget                | FIDELITY: OK | MAPPING: ABSENT-CONFIRMED | absent
 63 | OccupationForm.shifted_coercivity              | FIDELITY: OK | MAPPING: ABSENT-CONFIRMED | absent
 64 | PhaseResponse.rough_phase_choice               | FIDELITY: OK | MAPPING: ABSENT-CONFIRMED | absent
 65 | PhaseResponse.balanced_phase                   | FIDELITY: OK | MAPPING: ABSENT-CONFIRMED | absent
 66 | PhaseResponse.energy_boundary                  | FIDELITY: OK | MAPPING: ABSENT-CONFIRMED | absent
 67 | PhaseResponse.four_component_gram              | FIDELITY: OK | MAPPING: ABSENT-CONFIRMED | distinct from E:variance-normalized-kernel
 68 | PhaseResponse.two_frequency_average            | FIDELITY: OK | MAPPING: ABSENT-CONFIRMED | absent
 69 | PhaseResponse.frequency_window                 | FIDELITY: OK | MAPPING: ABSENT-CONFIRMED | absent
 70 | PositiveGram.scalar_sqrt_dual                  | FIDELITY: OK | MAPPING: OK | L:gram-scalar-algebra E:gram-sqrt-dual
 71 | PositiveGram.gram_norm_square                  | FIDELITY: OK | MAPPING: OK | same-lemma Gram identity
 72 | PositiveGram.active_upper_bound                | FIDELITY: OK | MAPPING: OK | conditional upper bound in P:gram-positive-optimizer proof
 73 | PositiveGram.half_weighted_entrywise_mono       | FIDELITY: OK | MAPPING: OK | (1/2)Σw(D-C)w≥0 in P:gram-entrywise-comparison
 74 | ProjectionResidual.projection_gap              | FIDELITY: OK | MAPPING: ABSENT-CONFIRMED | constants absent
 75 | ProjectionResidual.tilted_gap                  | FIDELITY: OK | MAPPING: ABSENT-CONFIRMED | absent
 76 | RawValueCeiling.exact_gap                      | FIDELITY: OK | MAPPING: ABSENT-CONFIRMED | integer instance absent
 77 | RawValueCeiling.strict_log_gap                 | FIDELITY: OK | MAPPING: OK | Δ>0 in C:intrinsic-spatial-bracket
 78 | RawVariational.dilation_factors                | FIDELITY: OK | MAPPING: OK | d=1 dilation bookkeeping (ledger discloses)
 79 | RawVariational.label_score                     | FIDELITY: OK | MAPPING: OK | c^{1/k} homogenization E:variational-score-set-scaling
 80 | RawVariational.positive_score                  | FIDELITY: OK | MAPPING: OK | r_0 I_0 - r_0^q v_0/2 > 0
 81 | RawVariational.strict_label_factor             | FIDELITY: OK | MAPPING: OK | 2^m>2, m=(4-α)/(3-α)
 82 | TerminalCross.polynomial_identity              | FIDELITY: OK | MAPPING: ABSENT-CONFIRMED | absent
 83 | TerminalCross.polynomial_pos                   | FIDELITY: OK | MAPPING: ABSENT-CONFIRMED | absent
 84 | TerminalCross.rate_le                          | FIDELITY: OK | MAPPING: ABSENT-CONFIRMED | absent
 85 | TerminalCross.exponential_difference           | FIDELITY: OK | MAPPING: ABSENT-CONFIRMED | absent
 86 | TerminalCross.terminal_bound                   | FIDELITY: OK | MAPPING: ABSENT-CONFIRMED | absent
 87 | WhiteCDF.cdf_square_bound                      | FIDELITY: OK | MAPPING: WEAK | conclusion 3A²≤b is used in P:white-spatial-energy, not L:white-cdf-square (F2)
 88 | WhiteCDF.energy_upper                          | FIDELITY: OK | MAPPING: OK | cA-b/2≤c²/6 in P:white-spatial-energy
```

## Section B — numbered findings

**F1 — MAJOR — over-mapping of diagnostic identities.** `JointTilt.wrong_sign_error`, `JointTilt.wrong_cost_error`.
- Lean: `wrong_sign_error … (r^2*w+2*r*s*c+s^2*v)/2) - r^2*w/2 = 2*r*s*c`; `wrong_cost_error … = -s^2*v/2`.
- TeX (`integrated_raw_block_lower.tex`, proof of `P:raw-block-gaussian-law`): the entire argument is "the density `e^{-sZ-s^2v/2}` defines an equivalent probability measure `Q_s` by completing the square in the `N(0,v)` density" plus a joint-Gaussian substitution. There is **no** sign-reversal or double-cost computation anywhere in the manuscript.
- Problem: the index maps these two to `P:raw-block-gaussian-law`, implying the paper uses them. It never does; they are self-imposed sanity checks ("what a sign error/doubled cost would leave behind"), acknowledged only in the ledger's module prose — which contradicts the index's label assignment.
- Fix: reclassify `wrong_sign_error` and `wrong_cost_error` as "no direct label" (or a new explicit "diagnostic, not in manuscript" status); leave only `tilt_exponent` under `P:raw-block-gaussian-law`.

**F2 — MINOR — label imprecision.** `WhiteCDF.cdf_square_bound`.
- Lean hypothesis `∀z, 0 ≤ b - 2zA + z²/3`; conclusion `3A² ≤ b`.
- TeX (`integrated_white_evaluation.tex`): `L:white-cdf-square` is the *identity* `E:white-cdf-square`; the step "Substitution z=3A into E:white-cdf-square gives 3A² ≤ b" occurs in the proof of **`P:white-spatial-energy`**.
- Fix: relabel to `P:white-spatial-energy` (or state explicitly that the identity is the supplied hypothesis `L:white-cdf-square` and the deduction is used in `P:white-spatial-energy`). The row's own "Inputs left outside Lean" already hints at this split.

**F3 — MINOR — partial parameter-range certification.** `InteractionDriver.temporal_range`.
- Lean: `0<a<1 ⟹ 1/2 < 1-a/2 < 1`.
- TeX (`integrated_actual_operator_driver.tex`, `E:driver-parameters`): requires `1/2 < θ < β < min(1-a/2, (3-a-α)/2)` with `0<γ<min(1/2,(2-α)/2)`; the Lean certifies only the `1-a/2` endpoint and neither the `(3-a-α)/2` endpoint nor the strict nesting `θ<β`.
- Fix: add a note that `temporal_range` certifies only the upper endpoint `1-a/2`; the remaining nonemptiness/nesting is outside Lean.

**F4 — MINOR — midpoint vs interval (already disclosed, needs index-level clarity).** `InteractionDriver.holder_parameters`, `InteractionDriver.dyadic_ratio`.
- Lean fixes `m = (H+θ)/2` and checks `H-m-1/p>0`, `p>2`.
- TeX (`integrated_actual_operator_driver.tex`, `L:driver-holder-limit`): "Choose `θ<η<β` and an even `q_0` with `q_0γ>d` and `β-η-1/q_0>0`" — `η` is an *arbitrary* interior point, not the midpoint.
- Problem: the ledger's module paragraph already discloses this, but the index reads `L:driver-holder-limit → holder_parameters, dyadic_ratio`, so a reader consulting only the index sees a stronger claim than the paper supports.
- Fix: append to the InteractionDriver module paragraph that the paper's `L:driver-holder-limit` treats the exponent as an arbitrary interior point and the Lean rows certify only the midpoint instance.

**F5 — MINOR — one-sided κ bound.** `DirectEvent.kappa_gt_one`.
- Lean proves `(4-α-a)/(3-α) > 1` only.
- TeX (main file, `E:kappa`): `κ := (4-α-α_0)/(3-α) ∈ (1,2)`; the upper bound `κ<2` is also asserted and unverified.
- Fix: state in the row that only `κ>1` is checked; the `κ<2` direction is outside Lean.

**F6 — MINOR — definition count scoping.** The ledger's "Totals: 88 declarations (82 theorems, 6 definitions)" and only 6 definition rows, while the package additionally defines `kappa`, `delta`, `radius`, `temporalH`, `midpoint`, `mixC`, `dyadicFactor`, `phaseIndex`, `noiseOrder`, `sourceSigma`, `actualMeanCoeff`, `projectedLower`, `numP`, `numN`, `polynomial`, `gauge`, `drift`, `pulseZero`, `pulseTwo`, `bump`, `counts`, `raw`, `cut`, and the MiddleCross/GlobalOmega auxiliary functions. These carry scaling conventions relied on by the documented rows.
- Fix: add a Scope sentence clarifying that auxiliary named definitions are not given ledger rows but the 82-theorem count is complete.

**F7 — MINOR — confirmatory near-miss, no fix required.** `InteractionDriver.box_margin`, `InteractionDriver.box_scale`.
- Lean margin uses `p>4/(1-a) ⟹ (1-a)/2 - 2/p > 0` and `δ^((1-a)/2)(δ^(-2))^(1/p)`.
- TeX (`integrated_radius_anchor.tex` `E:radius-mean-anchor-decay`, `integrated_gaussian_tubes.tex` `P:tube-actual-law`): margin is `e_anchor = (1-a)/2 - d/Q` with `Q(1-a)>2d`, i.e., `d/Q` in place of `2/p`.
- These are **different** facts; the ledger's "no direct label" assignment is correct. Recorded for the record so the resemblance is not mistaken for a mapping.

## Section C — overall verdict

**PASS_WITH_CONCERNS.**

Severity counts: CRITICAL 0, MAJOR 1 (F1), MINOR 6 (F2–F7).

All 88 rows were checked; none skipped. Fidelity of every "What it states" / `claims.yaml` summary to the actual Lean type is correct across all rows. The single substantive defect is over-mapping of the two diagnostic `JointTilt.wrong_*` identities to `P:raw-block-gaussian-law` (F1); the remaining findings are precision/disclosure issues rather than false statements. The "no direct label" assignments (53 rows) are accurate: the flagged near-misses (`box_margin/box_scale` 2/p vs. d/Q, `dilation_factors` d=1, `holder_parameters` midpoint) do not correspond to any labeled statement and are correctly kept out of the label index, with appropriate module-level disclaimers.

Confidence: **MEDIUM.** Reason: all Lean-to-ledger fidelity checks were done declaration-by-declaration (high confidence), and the flagged/manuscript-critical mappings (`ClockFilter`, `MovingCone`, `WhiteCDF`, `PositiveGram`, `RawVariational`, `DirectEvent`, `GaussianTail`, `FiniteYoung`, `ActualEvent`, `RawValueCeiling`) were verified against quoted TeX; but the 53 "no direct label" confirmations rely on careful manual reading of a very long manuscript without a tool-assisted exact search, so a stray re-used computation could in principle have escaped notice.