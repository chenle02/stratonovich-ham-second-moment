# Review Result — deepseek

- category: paper-review-deepseek
- model: deepseek/deepseek-v4-pro
- verdict: PASS_WITH_NOTES
- confidence: MEDIUM

## Critical findings

1. **No located false identity, sign error, or incorrect constant in the parts I could verify.** The manuscript's own "actual constants and calibrations" — which this review was explicitly tasked to audit — all check out where I worked them: the white-noise first/second-order coefficients (`L:white-test`: 𝔼X₁²=c₀t^{3−α₀}, 𝔼X₂=c₀t^{3−α₀}/2, total order-2 = 2c₀t^{3−α₀}); the G0 majorant exponent ρ=(4−α−α₀)/(3−α−α₀)>κ; the missing factorial power (k!)^{-α₀} diagnosis; the d1-upper factorial identity k!·k^{bk}≥(k!)^{3−α}; the canonical law scaling δ=T^{−κ}, r_T=T^{1−κ} with both vertex factors T^{−a/2}r^{2−α/2}=√δ and T^{1−a/2}r^{1−α/2}=δ^{−1/2}; the Rayleigh/CDF identity ∫[f′−zf(1−2F)]²=b−2zA+z²/3; the exact white spatial energy R_sp=c/√3, E_sp=c²/6 and the double-sided bound (2/3)√(c/M_a)≤C₂≤(2/3)√(cK₀); the relative-width Gamma/Cauchy–Schwarz bound with equality at a=½; the temporal-equilibrium identity ∫|s−t|^{−a}f_a=1 with M_a=Γ((1+a)/2)/(Γ(1+a)Γ((1−a)/2)); the Gram dual stationarity and entrywise comparison; and the scalar score homogeneity S_c^pos=c^{(4−α)/(3−α)}S₁^pos (dilation I→rI, v→r^{4−α}v). All internally consistent.
2. **Complete certification of 213 proofs is not achievable in one text-only pass.** Roughly two-thirds of the proof bodies — concentrated in the operator-driver (SEC19), Cameron regulation (SEC29,31), Gaussian tubes (SEC35), uniform products (SEC36), point transfer (SEC37), signed-score upper (SEC38) and symplectic baseline (SEC34) — I can follow structurally but cannot verify rigour at the level of each limiting exchange, Bochner-integral exchange, and spectral-calculus application. Per the mandated protocol I mark them NOT_FULLY_CHECKED rather than pass them. The **global conclusion (Theorem T:intrinsic-second-moment) is therefore INCONCLUSIVE at a HIGH acceptance standard**, though it is supported by consistent architecture, non-circular dependencies, and clean spot checks.
3. **VISUAL/source-image coverage is zero in this run.** This text-only model sees no PNG/PDF image, no rendered 84-page manuscript page, and no of the 257 rendered-page obligations. I therefore cannot certify that the primary sources were read from rendered pages (as `SOURCE-MANIFEST.md` itself instructs, formulas must be read from rendered pages, not the PDF text layer). This is a hard coverage gap — the extracted source text explicitly warns "PDF extraction may garble mathematics." I flag, not as a located manuscript error, but as an unresolved verification boundary.
4. **Strength-of-claim vs. verification state (honesty check — passes, with a caveat).** The manuscript honestly *does not* claim closure: abstract and README state whole-argument and cold reviews remain pending; the label-one score is explicitly not identified with an actual first moment; no source normalization is adopted; no source-author correspondence or circulation is claimed. The caveat an adversarial reviewer must record: Theorem T:intrinsic-second-moment (an exact limit for *every* admissible covariance in d=1,2,3) is substantially stronger than any published result, and its proof rests on a ~60-section chain in which many load-bearing steps are characterized internally as "ANALYTIC/informal" arguments (see `lean-progress/BOUNDARIES.md`), not formalized. This is not a located defect, but it is the single largest risk to correctness.

## Noncritical findings

[held back: collaborators' unpublished work]

## Checked derivations

Fully or substantially verified (constants/signs/boundary/limit-order):

- `L:white-test`, `P:envelope`, `P:d1-upper`, `C:d1-first-calibration` (2C₁,∗<C₂,∗ via (4−α)/(3−α)>1).
- `L:exact-canonical-scaling` (both scaling exponents), `L:variational-control-dilation` (I→rI, v→r^{4−α}v, λ→rλ), `P:variational-positive-scores` (r₀ chosen so the score halves; S_c^pos=c^mS₁^pos, m=(4−α)/(3−α)).
- `L:white-cdf-square`, `P:white-spatial-energy`, `T:white-moment-bounds`, `C:white-relative-width`.
- `L:temporal-equilibrium` (mass formula; s=0 and s=1 endpoint checks).
- `L:equilibrium-gamma-beta` (duplication/recurrence applications).
- `L:gram-scalar-algebra`, `L:gram-dual-minimum`, `P:gram-positive-optimizer`, `P:gram-entrywise-comparison`.
- Source imports: `E:cp-input` (Crouzeix–Palencia (3) and Theorem 6), Friz–Hairer Young (4.3) and Borell 11.6/footnote, Teschl 2.14/3.6/4.12/4.13/10.2/10.13 — all match the embedded excerpts at the stated hypotheses.
- Two-chain expansion `P:mixed` convention vs. source Theorem 4.1(4.3)/Theorem 3.1 inclusion of cross-pairings and independent chain roots.
- Arithmetic of `P:near-static-mean-gap` window (a_∗=b log2/log(B_b/K(0))⟹2^{κ_st}L₀ comparison).

## Required fixes before production gate

1. **Fresh whole-argument mathematical review + independent cold read** (manuscript's own open item) — explicitly including the NOT_FULLY_CHECKED proof set below, with special attention to the δ-before-B/limsup orderings and the Gaussian-tube Borell/Rayleigh application.
2. **Complete rendered source-image/page verification**: read the Chen author PDF (SHA 5f7385ca…), Chen–Hu p.2147, Balan–Conus p.1492, Chen-2023 Theorem 1.1, Crouzeix–Palencia pp.1,5–6, Teschl exact pages, Friz–Hairer p.190/4.3 from **rendered** pages; re-confirm every citation the text extracted from PDF layers. This run cannot do it.
3. **Adjudicate the top-risk proofs individually** (status below), most importantly: `L:inventory-product`, `L:fixed-split`, `P:interval-coefficients`, `T:full-upper` (interval-field upper), `P:tube-wiener-realization`, `P:tube-coarse-envelope`, `P:uniform-arbitrary-residual`, `P:original-point-transfer`, `P:positive-signed-comparison`, `P:signed-operator-upper`.
4. **Explicit statement in the notes** making the upper-bound's non-circularity watertight at the sentence level (it is asserted, and I confirmed the dependency tree, but a one-line cross-reference ledger inside the TeX would harden it).
5. Resolve whether the "kinetic coefficient one / variance-half action" phrase in the abstract is a *definition* of the derived formula or a pre-derived property; it is currently a retroactive description of what the computation yields.

## One-line summary

The intrinsic-limit architecture is coherent and non-circular and every concrete calibration/constant/source-fidelity point I could verify is correct, but two-thirds of the 213 proof bodies lie in an operator/Young/Gaussian-tube chain I cannot fully certify in a single text-only pass, and with zero image/render coverage the global HIGH-standard acceptance remains INCONCLUSIVE — hence PASS_WITH_NOTES at MEDIUM.

---

## 63 named checks

- SEC01 Model/assumptions — PASS (model, κ∈(1,2), homogeneity, white endpoint correct).
- SEC02 What is known — PASS (source statements quoted with qualification; v1 trap honored).
- SEC03 Gate G0 — PASS (white test, P:mixed, G0 obstruction exponent/count-factorial correct).
- SEC04 Gate G1 — PASS_WITH_NOTES (order-2 terms verified; order-4 tables not re-derived row-by-row).
- SEC05 G2 α≤1 — PASS (factorial power, C₂ arithmetic verified; spectral α≤1 bounds structurally OK).
- SEC06 Higher α convolution — PASS (conditional scope honored; obstructions logically consistent).
- SEC07 Static interpolation — PASS (affine exponents and χ interpolation checked).
- SEC08 Planar d=2 — PASS (endpoint/weight algebra consistent).
- SEC09 d=3 endpoints — NOT_FULLY_CHECKED (product/plane/finite-image combinatorics long).
- SEC10 Measure spectral energy — PASS_WITH_NOTES (Sobolev identification plausible; full limit not re-verified).
- SEC11 Static first-variance — PASS (phase-variance K_ε coefficient and constants consistent).
- SEC12 All static orders — NOT_FULLY_CHECKED (Crouzeix–Palencia application; hypotheses match source but function-calculus details long).
- SEC13 Interval full upper — NOT_FULLY_CHECKED (dyadic domination, inventory, split lemmas; exponent verified, interior not).
- SEC14 Near-static lower — PASS (Hölder/type/log-convex arithmetic verified).
- SEC15 Clock-copy screen — PASS (white Laplace transforms and the 2−2^a degree-one loss verified).
- SEC16 Masked covariance — PASS_WITH_NOTES (modulation/trig bounds; completion details long).
- SEC17 Wave variances — NOT_FULLY_CHECKED (both directions, row measure estimates).
- SEC18 Compact Gaussian — PASS_WITH_NOTES (Gaussian matrix/trace logic; whole-space Schatten estimates long).
- SEC19 Operator driver — NOT_FULLY_CHECKED (path/Hölder/tails; longest technical proof).
- SEC20 Source convergence — NOT_FULLY_CHECKED (retaining isometry/pointfield regularity).
- SEC21 Masked moments — PASS_WITH_NOTES (comparison/logic clear; limits standard).
- SEC22 Constant-phase Young — NOT_FULLY_CHECKED (Young linear/nonlinear solution chain).
- SEC23 Compact mean family — PASS_WITH_NOTES (Teschl imports match; full-phase projections long).
- SEC24 Exact scaling — PASS (verified).
- SEC25 Raw-block lower — NOT_FULLY_CHECKED (Gaussian law tilt, cone induction).
- SEC26 Unmasked variational — PASS (Rayleigh/dilation/score scalars verified).
- SEC27 Temporal equilibrium — PASS (verified).
- SEC28 Spatial occupation — PASS_WITH_NOTES (energy maps/row max verified; four-linear extension long).
- SEC29 Cameron mean — NOT_FULLY_CHECKED (fractional products, temporal compactness, embedding).
- SEC30 Young upper foundation — PASS_WITH_NOTES (refined growth/multiplicative perturbation logically consistent).
- SEC31 Uniform mean regulation — NOT_FULLY_CHECKED (uniform-radius regulator/tensor bounds).
- SEC32 Radius anchor — NOT_FULLY_CHECKED (radius-explicit Schatten/dyadic chaining).
- SEC33 Signed static wave — NOT_FULLY_CHECKED (H^{−1/2} multiplier form, spectral wave).
- SEC34 Symplectic phase — NOT_FULLY_CHECKED (conservation limit, block-mean baseline).
- SEC35 Gaussian tubes — NOT_FULLY_CHECKED (AWS realization, Borell application, Rayleigh).
- SEC36 Uniform products — NOT_FULLY_CHECKED (E-spectral rates, good/bad blocks, residual ratio).
- SEC37 Point transfer — NOT_FULLY_CHECKED (cone identity, square-average, growing-cone).
- SEC38 Signed-score upper — NOT_FULLY_CHECKED (moving score, two-limit operator upper).
- SEC39 Positive Gram — PASS (verified).
- SEC40 Intrinsic constant — PASS_WITH_NOTES (formula/homogeneity verified; relies on NOT_FULLY_CHECKED chain).
- SEC41 Occupation ceiling — PASS_WITH_NOTES (raw energies and white bracket substitution verified; selection/equality details long).
- SEC42 White evaluation — PASS (verified).
- SEC43 Targets/status — PASS (honest statements).
- SEC44 Established steps/open — PASS (honest route summary).

[held back until the source author has been told]

## 213-row proof-coverage ledger (concise)

Status: **CK**=CHECKED, **NF**=NOT_FULLY_CHECKED (coherent, not fully verified in this pass), **F**=FAIL (none located). Keyed to `proof-index-v1.txt` labels.

- P001 Jensen — CK (summability + nonnegativity).
- P002 P:mixed — CK (two-chain Wick/roots vs Thm 4.1).
- P003 L:white-test — CK.
- P004 L:damped-homogeneous-norms — CK·NH (scalings verified; tail limits std).
- P005 L:spatial-wick-measures — NF.
- P006 L:joint-fixed-order — NF.
- P007 L:crude-corrected — CK·NH (P_n n^{−2n}≤2^n/n! and e^{2θt} step verified).
- P008 L:vertex-crude — CK·NH (ratio test verified).
- P009 P:mild-construction — NF.
- P010 P:envelope — CK.
- P011 P:white-four — NF (table not re-derived).
- P012 L:static-four — NF (not all integrals re-checked).
- P013 P:riesz-small — CK·NH (order-2 evaluated; order-4 generic).
- P014 L:d1-spatial — CK·NH (descending-label invariant, AM-GM).
- P015 P:d1-upper — CK.
- P016 L:low-alpha-convolution — CK·NH.
- P017 L:alpha-one-convolution — CK·NH (πV/2 and c_δ=πV matching checked).
- P018 P:low-alpha-upper — CK·NH.
- P019 C:d1-first-calibration — CK.
- P020 P:higher-transfer — NF.
- P021 L:higher-riesz — NF.
- P022 C:higher-riesz — CK·NH (PD mixture).
- P023 P:higher-obstructions — CK·NH (divergence cases plausible).
- P024 L:static-holder-input — CK·NH (import usage only).
- P025 P:static-holder-upper — CK·NH (affine exponent algebra).
- P026 L:planar-endpoints — NF.
- P027 L:planar-static-input — CK·NH.
- P028 P:planar-upper — NF.
- P029 C:planar-range — CK (case split).
- P030 L:product-endpoints — NF.
- P031 L:plane-endpoints — NF.
- P032 L:endpoint-closure — NF.
- P033 P:three-transfer — NF.
- P034 C:three-product-riesz — CK·NH (endpoints discharged).
- P035 C:three-finite-images — NF.
- P036 L:physical-spectral-energy — NF.
- P037 L:phase-contractions — CK·NH (resolvent/sphere formulas).
- P038 P:static-phase-variance — CK·NH.
- P039 L:complex-phase — NF (Crouzeix application).
- P040 L:fock-form — NF.
- P041 L:finite-word-cutoff — CK·NH (degree bookkeeping).
- P042 P:static-phase-all-orders — NF.
- P043 C:static-interaction — NF.
- P044 L:interval-contractions — NF.
- P045 L:interval-complex — NF.
- P046 L:inventory-product — NF.
- P047 L:fixed-split — NF.
- P048 P:interval-coefficients — NF.
- P049 L:terminal-wick — CK·NH (mass t^{2n}/(2n)!, Wick coefficients).
- P050 L:uniform-series-tail — CK·NH.
- P051 T:full-upper — NF (interior).
- P052 L:mean-coefficient-holder — CK·NH (raw-power Hölder).
- P053 L:positive-series-type — CK·NH.
- P054 P:static-minorant-lower — CK·NH.
- P055 P:near-static-mean-gap — CK.
- P056 L:full-moment-coefficient-holder — NF.
- P057 P:moment-growth-logconvex — CK·NH (type-calculus).
- P058 C:static-moment-constant-continuity — CK·NH.
- P059 L:white-clock-laplace — CK.
- P060 P:clock-copy-obstruction — CK.
- P061 P:masked-spectral-growth — CK·NH.
- P062 P:masked-auxiliary-norm — CK·NH.
- P063 L:masked-time-completion — CK·NH.
- P064 P:masked-noise-completion — NF.
- P065 P:masked-quotient-obstruction — CK·NH (d=2,α=1 example).
- P066 L:masked-temporal-modulation — NF.
- P067 L:masked-trig-products — NF.
- P068 L:masked-continuous-wave — NF.
- P069 P:frequency-row — NF.
- P070 C:frequency-time — CK·NH (strict β gaps).
- P071 P:actual-wave-form — NF.
- P072 L:phase-bessel — CK (finite Bessel).
- P073 P:wave-two-variances — NF.
- P074 P:wave-square-columns — NF.
- P075 L:gaussian-scalar-powers — CK.
- P076 L:gaussian-trace-bounds — CK·NH.
- P077 P:finite-gaussian-matrix — CK·NH (dilation computation).
- P078 L:cutoff-factorization — NF.
- P079 P:cutoff-singular-values — NF.
- P080 P:compact-two-envelopes — CK·NH.
- P081 L:compact-positive-order — CK.
- P082 P:localized-finite-variance — CK·NH.
- P083 C:finite-gaussian-operators — NF.
- P084 P:cutoff-boundary-tests — CK·NH (noncompactness example).
- P085 L:driver-noise-basis — CK·NH.
- P086 L:driver-covariance-coefficients — NF.
- P087 L:driver-gain-localization — NF.
- P088 L:driver-actual-variances — NF.
- P089 L:driver-dominated-tails — CK·NH.
- P090 L:driver-gaussian-tail-average — NF.
- P091 L:driver-interval-limit — NF.
- P092 L:driver-holder-limit — NF.
- P093 (dup of P092) — NF.
- P094 L:source-finite-comparison — CK (Gaussian convex).
- P095 P:source-gaussian-transfer — NF.
- P096 L:source-spatial-heat — CK·NH.
- P097 L:source-retaining-isometry — NF.
- P098 P:source-canonical-convergence — NF.
- P099 L:source-pointfield-regularity — NF.
- P100 P:source-ordinary-response — NF.
- P101 L:masked-chain-comparison — CK·NH.
- P102 P:masked-source-moments — NF.
- P103 P:masked-canonical-transfer — CK·NH.
- P104 L:constant-phase-free — CK·NH.
- P105 P:constant-phase-driver — NF.
- P106 L:constant-source-response — NF.
- P107 P:constant-young-linear — NF.
- P108 P:constant-gaussian-flow — NF.
- P109 L:constant-source-solution — NF.
- P110 P:constant-raw-average — NF.
- P111 P:constant-compact-base — NF.
- P112 P:compact-ground-family — CK·NH (Teschl import; gap arith verified).
- P113 L:compact-fractional-phase — NF.
- P114 P:compact-E-wave — NF.
- P115 P:compact-F-projection — NF.
- P116 P:compact-F-complement — NF.
- P117 L:compact-raw-profile — CK·NH.
- P118 P:compact-original-common-trial — CK·NH (L^{−α} vs L^{−2} margin).
- P119 L:exact-canonical-scaling — CK.
- P120 L:raw-block-inputs — NF.
- P121 P:raw-block-gaussian-law — NF.
- P122 L:raw-block-uniform-error — NF.
- P123 L:raw-block-indexed-cone — NF.
- P124 L:raw-block-restart — NF.
- P125 P:raw-block-point-comparison — NF.
- P126 P:raw-block-original-lower — NF.
- P127 L:variational-heat-envelope — CK·NH.
- P128 L:variational-global-mean — CK·NH.
- P129 P:variational-unmasked-rate — CK·NH.
- P130 P:variational-remove-mask — NF.
- P131 L:variational-control-dilation — CK.
- P132 P:variational-positive-scores — CK.
- P133 L:equilibrium-gamma-beta — CK.
- P134 L:temporal-equilibrium — CK.
- P135 L:spatial-physical-pair — CK·NH.
- P136 L:spatial-static-controls — NF.
- P137 P:spatial-smooth-ratio — CK·NH (dilation algebra).
- P138 P:spatial-four-linear — NF.
- P139 P:spatial-energy-map — CK·NH.
- P140 L:occupation-kernel-row — CK.
- P141 P:occupation-physical-class — NF.
- P142 L:cameron-fractional-products — NF.
- P143 P:cameron-spatial-map — NF.
- P144 L:cameron-supported-tensor — CK·NH.
- P145 P:cameron-temporal-map — NF.
- P146 P:cameron-full-mean — NF.
- P147 L:cameron-actual-residual — NF.
- P148 P:cameron-actual-embedding — NF.
- P149 L:young-upper-growth — CK·NH.
- P150 P:young-upper-multiplicative — NF.
- P151 L:uniform-mean-cutoff — NF.
- P152 L:uniform-mean-spatial-tails — NF.
- P153 L:uniform-mean-tensor — CK·NH (dimension-free tensor).
- P154 P:uniform-mean-regulator — NF.
- P155 P:uniform-actual-cameron — NF.
- P156 L:radius-outer-maps — NF.
- P157 P:radius-compact-envelopes — NF.
- P158 P:radius-actual-moments — NF.
- P159 C:radius-covariance-residuals — NF.
- P160 P:radius-mean-anchor — NF.
- P161 L:signed-limiting-multiplier — NF.
- P162 P:signed-closed-form — NF.
- P163 L:signed-spectral-wave — NF.
- P164 P:signed-physical-wave — NF.
- P165 L:symplectic-free — CK·NH.
- P166 L:symplectic-source-mean — NF.
- P167 P:symplectic-source — NF.
- P168 P:symplectic-raw — NF.
- P169 P:symplectic-block-mean — NF.
- P170 P:tube-wiener-realization — NF.
- P171 L:tube-closed-geometry — NF.
- P172 P:tube-rayleigh-transfer — NF.
- P173 P:tube-actual-law — NF.
- P174 L:tube-actual-endpoint — NF.
- P175 P:tube-coarse-envelope — NF.
- P176 L:tube-rayleigh-tail — CK·NH (scalar cutoff; guard algebra verified).
- P177 L:tube-half-action — CK.
- P178 L:uniform-E-lift — NF.
- P179 P:uniform-E-spectral — NF.
- P180 P:uniform-rate-averaging — NF.
- P181 L:uniform-product-budgets — NF.
- P182 P:uniform-mean-product — NF.
- P183 C:uniform-polynomial-balls — NF.
- P184 P:uniform-arbitrary-residual — NF.
- P185 L:point-actual-finiteness — NF.
- P186 L:point-fast-sources — NF.
- P187 L:point-compact-source — NF.
- P188 P:point-source-cone — NF.
- P189 P:original-point-transfer — NF.
- P190 L:signed-score-envelope — NF.
- P191 P:signed-moment-bulk-tail — NF.
- P192 P:signed-operator-upper — NF.
- P193 P:original-signed-point-upper — NF.
- P194 L:gram-scalar-algebra — CK.
- P195 L:gram-dual-minimum — CK.
- P196 P:gram-positive-optimizer — CK.
- P197 L:gram-realization — CK.
- P198 P:gram-entrywise-comparison — CK.
- P199 L:positive-raw-embedding — NF.
- P200 L:positive-physical-gram — NF.
- P201 L:positive-uniform-optimizer — NF.
- P202 P:positive-signed-comparison — NF.
- P203 P:positive-score-cutoff — NF.
- P204 T:intrinsic-second-moment — CK·NH (formula/homogeneity/zero-case correct; chain NOT_FULLY_CHECKED).
- P205 L:occupation-raw-square — NF.
- P206 P:raw-occupation-energy — CK·NH (Λ exponent algebra).
- P207 L:occupation-rayleigh-selection — NF.
- P208 T:intrinsic-occupation-ceiling — CK·NH (D, F₀, U_c exponents verified).
- P209 C:intrinsic-spatial-bracket — CK·NH (log-gap algebra exact; integers not machine-verified).
- P210 L:white-cdf-square — CK.
- P211 P:white-spatial-energy — CK.
- P212 T:white-moment-bounds — CK.
- P213 C:white-relative-width — CK.

Counts: **FAIL 0**, **CHECKED/CK·NH 78**, **NOT_FULLY_CHECKED 135**.

---

### Explicit coverage/depth/source limitations

- Text-only; no image/edition/render verification (VISUAL01 unperformed), so all four source checks are textual-fidelity only, against the embedded PDF-text carriers that themselves warn of formula garbling.
- No tool/delegation/build/numerics used; exact-integer identities (e.g., 11¹¹7⁷, 2⁵9¹⁸) verified at exponent/algebra level, not by independent machine computation.
- No cold read, no whole-argument gate, no novelty/circulation/news/or public-release clearance claimed. No substitution of any other model or reviewer; no prior report/vote treated as proof.