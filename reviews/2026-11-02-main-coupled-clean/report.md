# Audit Report — Stratonovich Hyperbolic Anderson Second Moment (214-proof coupled argument)

## (1) Overall mathematical conclusion and decisive findings

**Conclusion.** Within the supplied text-only scope, the main-chain mathematical argument is **internally coherent and, at the level audited, sound**: it produces

- a full upper bound at the correct scale \(t^{\kappa}\), \(\kappa=\frac{4-\alpha-\alpha_0}{3-\alpha}\), for all admissible \(d\in\{1,2,3\}\), homogeneous covariances satisfying \(\alpha+\alpha_0<2\) (with \(\alpha=d=1\) white allowed), data \((1,0)\);
- a matching lower bound;
- the identification of the limit as \(C_2(\Gamma,\alpha_0)=S_2^{\mathrm{pos}}=2^{(4-\alpha)/(3-\alpha)}S_1^{\mathrm{pos}}\), with the displayed positive-control variational formula, action \(v_{\Psi}/2\), kinetic coefficient \(1\), both entries retained, and \(\Gamma=0\Rightarrow C_2=0\).

**Decisive findings.**

1. **No fatal mathematical contradiction** was found in the final matched chain. The three load-bearing links are:
   - the independent full upper `T:full-upper` (PROOF051), whose proof does not use the later variational identification (no circularity);
   - the signed-score upper \(\limsup \le S_2^{\mathrm{pos}}\), via `P:original-signed-point-upper` (193) + `P:positive-score-cutoff` (203) + `P:positive-signed-comparison` (202);
   - the positive-control lower \(Q_2\ge S_2^{\mathrm{pos}}\) via `P:raw-block-original-lower` (126) + `P:variational-remove-mask` (130) + `P:variational-positive-scores` (132).
   The finiteness of \(S_2^{\mathrm{pos}}\) is obtained from the independent `T:full-upper` (051) inside (132), not from the matching step itself.

2. The homogeneity \(S_c^{\mathrm{pos}}=c^{(4-\alpha)/(3-\alpha)}S_1^{\mathrm{pos}}\) (PROOF131/132) is verified exactly, giving the stated amplitude scaling and hence the \(2^{(4-\alpha)/(3-\alpha)}\) factor.

3. **Source-edition dispositions.** The imported theorems are used within their stated scopes (details in §4). Two source-display corrections are needed and are supplied by the manuscript themselves: Chen-author (3.5) prints \(G(s,x)G(t,x)\) with a duplicated spatial variable (the manuscript replaces it by independent \(x,y\), which is the mathematically necessary reading), and the Case-2 time-shift \((\sigma_i,\sigma_j)\mapsto(\sigma_i,\sigma_j,0)\) equality. `T:full-upper` loses the offset \(A-B\) admitted by the manuscript's own `L:translated-covariance-CS` (214); the manuscript correctly replaces that source step. The excluded edition `chen-arxiv-v1` is not used as the Theorem-1.2 authority.

4. **Honest limits.** The operator-theoretic cylinder (driver construction, source retention, tubes, symplectic conservation, three-transfer) contains long functional-analysis arguments. I audited the statements, key constants, parameter guards, and input/discharge logic, but not every \(\varepsilon\) of the Bochner/operator-convergence layers. These are marked `LIMITED`, not silently folded into the verdict. Nothing here substitutes a full independent cold review or numeric certification.

---

## (2) Per-proof ledger (214 rows)

Status keys: **CHECKED** = I reconstructed the local argument and its input use; **LIMITED** = statement/input logic and key estimates checked, but not every operator-convergence/\(\varepsilon\) step re-derived; **FLAW** = a specific defect identified; **NOT_READ** = not independently inspected.

| ID | Label | Status | Examined | Consumed premises | Limitation |
|---|---|---|---|---|---|
| 1 | P:Jensen | CHECKED | 366–392 | vertex-crude (008), expansion | conditional \(L_*\) correctly flagged |
| 2 | P:mixed | CHECKED | 436–509 | joint-fixed-order (006), crude (007) | nonneg series; relies on 005/006 |
| 3 | L:white-test | CHECKED | 513–538 | none | explicit check correct |
| 4 | L:damped-homogeneous-norms | CHECKED | 586–674 | homogeneity | \(N_2\ge0\), powers correct |
| 5 | L:spatial-wick-measures | LIMITED | 941–1101 | heat/wave transforms | measure limit heavy; plausible |
| 6 | L:joint-fixed-order | LIMITED | 1103–1198 | Thm3.1, (004) | regularization passes plausible |
| 7 | L:crude-corrected | CHECKED | 1208–1269 | Thm3.1, (004) | pairing-count bound correct |
| 8 | L:vertex-crude | CHECKED | 1273–1345 | Thm3.1, (004) | correct |
| 9 | P:mild-construction | LIMITED | 1347–1515 | vertex-crude (008), 006 | green/width order plausible |
| 10 | P:envelope | CHECKED | 1525–1600 | 004, Thm3.1 | exponent \(\rho>\kappa\) correct |
| 11 | P:white-four | LIMITED | 1682–1744 | none | table not fully recomputed |
| 12 | L:static-four | LIMITED | 1746–1837 | white-four | sums verified; sectors compressed |
| 13 | P:riesz-small | LIMITED | 1841–1925 | none | explicit formulas plausible |
| 14 | L:d1-spatial | CHECKED | 2062–2136 | none | optimizer bound correct (note AGM mislabel) |
| 15 | P:d1-upper | CHECKED | 2147–2234 | 006,014 | symmetry/count correct |
| 16 | L:low-alpha-convolution | CHECKED | 2251–2309 | homogeneity | layer-cake correct |
| 17 | L:alpha-one-convolution | CHECKED | 2311–2373 | homogeneity | endpoint \(\pi V/2\) correct |
| 18 | P:low-alpha-upper | CHECKED | 2375–2464 | 016,017,006 | correct |
| 19 | C:d1-first-calibration | CHECKED | 2489–2528 | 015,018 | correct |
| 20 | P:higher-transfer | LIMITED | 2596–2750 | spatial max (H) | parameter bookkeeping verified |
| 21 | L:higher-riesz | LIMITED | 2754–2829 | none | constants plausible |
| 22 | C:higher-riesz | LIMITED | 2831–2864 | 020,021 | PSD mixture correct |
| 23 | P:higher-obstructions | LIMITED | 2866–2930 | none | counterexamples plausible |
| 24 | L:static-holder-input | CHECKED | 3000–3046 | Chen–Hu 3.8/5.1/5.15 | aligned to edition |
| 25 | P:static-holder-upper | LIMITED | 3048–3242 | 024,017 | interpolation verified |
| 26 | L:planar-endpoints | LIMITED | 3290–3447 | homogeneity | weighting plausible |
| 27 | L:planar-static-input | CHECKED | 3449–3518 | Chen–Hu, Chen2023 | Dalang and rate check |
| 28 | P:planar-upper | LIMITED | 3520–3699 | 026,027 | parallel to 025 |
| 29 | C:planar-range | CHECKED | 3701–3716 | 018,028 | assembly correct |
| 30 | L:product-endpoints | LIMITED | 3747–3848 | none | interval algebra plausible |
| 31 | L:plane-endpoints | LIMITED | 3885–3967 | none | plausible |
| 32 | L:endpoint-closure | CHECKED | 3969–4040 | none | pushforwards/sums correct |
| 33 | P:three-transfer | LIMITED | 4081–4492 | Chen–Hu, Chen2023 | static coefficient id heavy |
| 34 | C:three-product-riesz | LIMITED | 4494–4542 | 030,033 | follows |
| 35 | C:three-finite-images | LIMITED | 4544–4595 | 032,033 | follows |
| 36 | L:physical-spectral-energy | CHECKED | 4644–4768 | Chen2023 Thm1.1 | finiteness import precise |
| 37 | L:phase-contractions | LIMITED | 4808–4878 | homogeneity | \(R_\alpha\) verified; trace bound outline |
| 38 | P:static-phase-variance | LIMITED | 4906–5012 | 037 | heavy but plausible |
| 39 | L:complex-phase | LIMITED | 5042–5228 | Crouzeix–Palencia | operator calculus heavy |
| 40 | L:fock-form | LIMITED | 5230–5295 | 037,039 | creation/annihilation plausible |
| 41 | L:finite-word-cutoff | CHECKED | 5297–5343 | none | induction correct |
| 42 | P:static-phase-all-orders | LIMITED | 5345–5462 | 039,040,041 | plausible |
| 43 | C:static-interaction | LIMITED | 5464–5586 | 042,038 | geometric series verified |
| 44 | L:interval-contractions | LIMITED | 5620–5692 | 037 | plausible |
| 45 | L:interval-complex | LIMITED | 5694–5785 | 039 | non-selfadjoint extension plausible |
| 46 | L:inventory-product | LIMITED | 5787–5848 | none | structure ok; constants not all |
| 47 | L:fixed-split | LIMITED | 5860–6223 | 044,045,041 | very heavy |
| 48 | P:interval-coefficients | LIMITED | 6225–6421 | 046,047 | heavy |
| 49 | L:terminal-wick | CHECKED | 6440–6545 | none | standard Wick; correct |
| 50 | L:uniform-series-tail | CHECKED | 6547–6593 | 049 | correct |
| 51 | T:full-upper | LIMITED | 6595–6834 | 048,049,050,006,009 | assembly verified; dyadic coverage ok |
| 52 | L:mean-coefficient-holder | LIMITED | 6914–7026 | Chen–Hu, 005/006 | plausible |
| 53 | L:positive-series-type | CHECKED | 7028–7072 | none | correct |
| 54 | P:static-minorant-lower | LIMITED | 7074–7145 | Chen–Hu 1.2, 006 | amplitude/clock correct |
| 55 | P:near-static-mean-gap | CHECKED | 7147–7205 | 052,053, full-upper | algebra correct |
| 56 | L:full-moment-coefficient-holder | LIMITED | 7247–7324 | 002,005 | plausible |
| 57 | P:moment-growth-logconvex | CHECKED | 7337–7397 | 053,056 | correct |
| 58 | C:static-moment-constant-continuity | CHECKED | 7399–7434 | 054,057 | correct |
| 59 | L:white-clock-laplace | CHECKED | 7477–7532 | none | explicit transforms correct |
| 60 | P:clock-copy-obstruction | LIMITED | 7594–7751 | none | degree-1 loss computed; heavy |
| 61 | P:masked-spectral-growth | CHECKED | 35–80 (cf) | homogeneity | correct |
| 62 | P:masked-auxiliary-norm | CHECKED | 91–142 | 061 | Hilbert norm correct |
| 63 | L:masked-time-completion | CHECKED | 146–187 | none | Schur correct |
| 64 | P:masked-noise-completion | LIMITED | 195–255 | 062,063 | plausible |
| 65 | P:masked-quotient-obstruction | CHECKED | 265–304 | none | counterexample correct |
| 66 | L:masked-temporal-modulation | CHECKED | 312–359 | 063 | correct |
| 67 | L:masked-trig-products | CHECKED | 361–391 | 066 | correct |
| 68 | L:masked-continuous-wave | CHECKED | 393–439 | 066,067 | correct |
| 69 | P:frequency-row | LIMITED | 47–145 (wv) | growth of \(\nu\) | heavy shell sums |
| 70 | C:frequency-time | CHECKED | 147–172 | 069 | \(\beta\)-gap correct |
| 71 | P:actual-wave-form | LIMITED | 221–357 | 062,064,068 | heavy |
| 72 | L:phase-bessel | CHECKED | 361–382 | none | correct |
| 73 | P:wave-two-variances | LIMITED | 384–477 | 069,071,072 | heavy |
| 74 | P:wave-square-columns | LIMITED | 483–547 | 073 | plausible |
| 75 | L:gaussian-scalar-powers | CHECKED | 14–48 (cg) | none | correct |
| 76 | L:gaussian-trace-bounds | CHECKED | 50–95 | 075 | correct |
| 77 | P:finite-gaussian-matrix | CHECKED | 97–179 | 076 | IBP dilation correct |
| 78 | L:cutoff-factorization | CHECKED | 208–307 | none | Schur correct |
| 79 | P:cutoff-singular-values | CHECKED | 309–366 | 078 | correct |
| 80 | P:compact-two-envelopes | CHECKED | 392–437 | 079 | correct |
| 81 | L:compact-positive-order | CHECKED | 443–471 | none | correct |
| 82 | P:localized-finite-variance | CHECKED | 473–513 | 080,081 | correct |
| 83 | C:finite-gaussian-operators | CHECKED | 519–579 | 077,082 | correct |
| 84 | P:cutoff-boundary-tests | CHECKED | 583–632 | 079 | correct |
| 85 | L:driver-noise-basis | LIMITED | 59–121 (aod) | 063 | separability plausible |
| 86 | L:driver-covariance-coefficients | LIMITED | 123–165 | none | plausible |
| 87 | L:driver-gain-localization | LIMITED | 169–237 | support propagation | plausible |
| 88 | L:driver-actual-variances | LIMITED | 255–340 | 073,074 | plausible |
| 89 | L:driver-dominated-tails | CHECKED | 342–367 | 081 | correct |
| 90 | L:driver-gaussian-tail-average | CHECKED | 369–395 | 077 | correct |
| 91 | L:driver-interval-limit | LIMITED | 399–459 | 077,088,089,090 | plausible |
| 92 | L:driver-holder-limit | LIMITED | 463–553 | 073,088,091 | dyadic chaining plausible |
| 93 | P:actual-operator-driver | LIMITED | 27–55,555–591 | 085–092 | heavy |
| 94 | L:source-finite-comparison | CHECKED | 21–42 (sc) | none | Jensen shift correct |
| 95 | P:source-gaussian-transfer | LIMITED | 44–134 | 094 | plausible |
| 96 | L:source-spatial-heat | CHECKED | 138–169 | spectral conv | correct |
| 97 | L:source-retaining-isometry | LIMITED | 179–236 | 096 | plausible |
| 98 | P:source-canonical-convergence | LIMITED | 256–360 | 095,096,097 | pointfield law verified |
| 99 | L:source-pointfield-regularity | LIMITED | 364–425 | 098 | plausible |
| 100 | P:source-ordinary-response | LIMITED | 427–482 | 098,099 | plausible |
| 101 | L:masked-chain-comparison | CHECKED | 23–100 (mm) | 049 | correct |
| 102 | P:masked-source-moments | LIMITED | 102–165 | 049,101 | plausible |
| 103 | P:masked-canonical-transfer | CHECKED | 167–221 | 006,101 | conditional premise clearly stated |
| 104 | L:constant-phase-free | CHECKED | 23–96 (cpY) | none | correct |
| 105 | P:constant-phase-driver | LIMITED | 106–147 | 093,095 | plausible |
| 106 | L:constant-source-response | LIMITED | 149–187 | 100,104 | plausible |
| 107 | P:constant-young-linear | CHECKED | 204–275 | Friz–Hairer | standard Young; correct |
| 108 | P:constant-gaussian-flow | LIMITED | 277–337 | 107,105 | plausible |
| 109 | L:constant-source-solution | LIMITED | 341–405 | 108 | plausible |
| 110 | P:constant-raw-average | LIMITED | 407–461 | 109,103 | plausible |
| 111 | P:constant-compact-base | LIMITED | 463–499 | 108 | plausible |
| 112 | P:compact-ground-family | LIMITED | 36–124 (cmf) | Teschl 10.2/10.13/4.12/4.13 | plausible |
| 113 | L:compact-fractional-phase | CHECKED | 126–178 | Teschl spectral | square-root order correct |
| 114 | P:compact-E-wave | LIMITED | 180–280 | 112,113 | plausible |
| 115 | P:compact-F-projection | LIMITED | 288–376 | 114 | plausible |
| 116 | P:compact-F-complement | LIMITED | 378–441 | 114,115 | plausible |
| 117 | L:compact-raw-profile | CHECKED | 445–512 | none | correct |
| 118 | P:compact-original-common-trial | CHECKED | 514–574 | 117,112 | scaling floor correct |
| 119 | L:exact-canonical-scaling | CHECKED | 4–61 (es) | 006,008 | correct |
| 120 | L:raw-block-inputs | LIMITED | 55–126 (rbl) | 093,105 | plausible |
| 121 | P:raw-block-gaussian-law | CHECKED | 128–172 | 120 | shift sign verified |
| 122 | L:raw-block-uniform-error | LIMITED | 182–253 | 108,107 | plausible |
| 123 | L:raw-block-indexed-cone | CHECKED | 255–372 | 114–116 | budget algebra correct |
| 124 | L:raw-block-restart | LIMITED | 376–466 | 098,108 | plausible |
| 125 | P:raw-block-point-comparison | LIMITED | 468–552 | 121,124,103,119 | plausible |
| 126 | P:raw-block-original-lower | LIMITED | 554–635 | 121–125 | moderate-deviation lower check partial |
| 127 | L:variational-heat-envelope | CHECKED | 23–70 (uv) | spectral conv | correct |
| 128 | L:variational-global-mean | CHECKED | 72–108 | 127 | correct |
| 129 | P:variational-unmasked-rate | CHECKED | 110–186 | 118, Teschl | Rayleigh correct |
| 130 | P:variational-remove-mask | CHECKED | 190–249 | 126,129 | supremum exchange legit |
| 131 | L:variational-control-dilation | CHECKED | 253–303 | homogeneity | powers correct |
| 132 | P:variational-positive-scores | CHECKED | 305–375 | 130,131, full-upper | scaling correct |
| 133 | L:equilibrium-gamma-beta | CHECKED | 9–33 (te) | none | correct |
| 134 | L:temporal-equilibrium | CHECKED | 35–101 | 133 | potential=1 verified |
| 135 | L:spatial-physical-pair | CHECKED | 13–37 (so) | none | correct |
| 136 | L:spatial-static-controls | CHECKED | 45–110 | 129,134 | \(M_a\) factor correct |
| 137 | P:spatial-smooth-ratio | CHECKED | 112–170 | 136 | correct |
| 138 | P:spatial-four-linear | CHECKED | 172–265 | 135,137 | correct |
| 139 | P:spatial-energy-map | CHECKED | 267–319 | 138 | correct |
| 140 | L:occupation-kernel-row | CHECKED | 332–352 | none | correct |
| 141 | P:occupation-physical-class | CHECKED | 361–431 | 138,140 | correct |
| 142 | L:cameron-fractional-products | CHECKED | 29–84 (cam) | 138 | correct |
| 143 | P:cameron-spatial-map | CHECKED | 86–153 | 078,142 | compactness correct |
| 144 | L:cameron-supported-tensor | CHECKED | 157–185 | none | correct |
| 145 | P:cameron-temporal-map | CHECKED | 187–264 | 133,62 | compact \(C_t\) correct |
| 146 | P:cameron-full-mean | CHECKED | 266–337 | 143,145 | correct |
| 147 | L:cameron-actual-residual | LIMITED | 359–407 | 095 | plausible |
| 148 | P:cameron-actual-embedding | LIMITED | 409–512 | 146,147 | power-mean inequality verified |
| 149 | L:young-upper-growth | CHECKED | 17–65 (yuf) | Friz–Hairer | correct |
| 150 | P:young-upper-multiplicative | CHECKED | 67–110 | 149 | correct |
| 151 | L:uniform-mean-cutoff | CHECKED | 28–65 (um) | 142 | correct |
| 152 | L:uniform-mean-spatial-tails | CHECKED | 67–161 | 151 | heat projection correct |
| 153 | L:uniform-mean-tensor | CHECKED | 165–209 | none | correct |
| 154 | P:uniform-mean-regulator | CHECKED | 229–279 | 145,151,152,153 | correct |
| 155 | P:uniform-actual-cameron | LIMITED | 308–425 | 147,154 | heavy |
| 156 | L:radius-outer-maps | CHECKED | 44–95 (ra) | 078 | correct |
| 157 | P:radius-compact-envelopes | CHECKED | 97–167 | 156,079 | correct |
| 158 | P:radius-actual-moments | LIMITED | 175–277 | 073,088,092,157 | dyadic chaining heavy |
| 159 | C:radius-covariance-residuals | CHECKED | 279–313 | 095,158 | correct |
| 160 | P:radius-mean-anchor | CHECKED | 317–372 | 159 | correct |
| 161 | L:signed-limiting-multiplier | LIMITED | 13–45 (ss) | none | plausible |
| 162 | P:signed-closed-form | LIMITED | 47–129 | Teschl 2.14/3.6 | plausible |
| 163 | L:signed-spectral-wave | LIMITED | 131–210 | 162 | plausible |
| 164 | P:signed-physical-wave | LIMITED | 212–302 | 163, constant phase | plausible |
| 165 | L:symplectic-free | CHECKED | 34–85 (sym) | none | matrix symplectic correct |
| 166 | L:symplectic-source-mean | LIMITED | 87–146 | 098 | plausible |
| 167 | P:symplectic-source | LIMITED | 148–186 | 165,166 | plausible |
| 168 | P:symplectic-raw | LIMITED | 188–274 | 107,108,165 | plausible |
| 169 | P:symplectic-block-mean | LIMITED | 276–382 | 146,168 | plausible |
| 170 | P:tube-wiener-realization | LIMITED | 21–124 (gt) | none | heavy |
| 171 | L:tube-closed-geometry | CHECKED | 144–200 | Borell, 170 | correct |
| 172 | P:tube-rayleigh-transfer | CHECKED | 202–247 | 171 | layer-cake correct |
| 173 | P:tube-actual-law | LIMITED | 275–352 | 146,155,160 | compactness heavy |
| 174 | L:tube-actual-endpoint | LIMITED | 354–412 | 124,168 | plausible |
| 175 | P:tube-coarse-envelope | LIMITED | 416–507 | 148,172,174 | plausible |
| 176 | L:tube-rayleigh-tail | CHECKED | 509–542 | none | scalar cutoff correct |
| 177 | L:tube-half-action | CHECKED | 544–562 | none | correct |
| 178 | L:uniform-E-lift | LIMITED | 38–81 (up) | 161 | plausible |
| 179 | P:uniform-E-spectral | LIMITED | 83–243 | 162,163 | plausible |
| 180 | P:uniform-rate-averaging | LIMITED | 247–314 | 154,179 | plausible |
| 181 | L:uniform-product-budgets | LIMITED | 325–388 | 169,150 | plausible |
| 182 | P:uniform-mean-product | LIMITED | 392–482 | 150,179,180,181 | heavy |
| 183 | C:uniform-polynomial-balls | CHECKED | 484–523 | 182 | limit algebra correct |
| 184 | P:uniform-arbitrary-residual | LIMITED | 527–614 | 150,182 | heavy |
| 185 | L:point-actual-finiteness | CHECKED | 21–67 (pt) | 173–176,168 | correct |
| 186 | L:point-fast-sources | LIMITED | 69–139 | 095,098,106 | plausible |
| 187 | L:point-compact-source | LIMITED | 141–212 | 099 | high-regularity plausible |
| 188 | P:point-source-cone | LIMITED | 214–276 | 102,104,187 | cone iteration plausible |
| 189 | P:original-point-transfer | LIMITED | 278–366 | 184,188 | prefactor \(R^d\to0\) correct |
| 190 | L:signed-score-envelope | CHECKED | 22–96 (smu) | 175,181 | constants verified |
| 191 | P:signed-moment-bulk-tail | CHECKED | 98–166 | 190,176 | correct |
| 192 | P:signed-operator-upper | CHECKED | 168–219 | 185,189,191 | limits order correct |
| 193 | P:original-signed-point-upper | CHECKED | 221–260 | 189,192 | correct |
| 194 | L:gram-scalar-algebra | CHECKED | 28–55 (pg) | none | correct |
| 195 | L:gram-dual-minimum | CHECKED | 57–107 | 194 | coercivity correct |
| 196 | P:gram-positive-optimizer | CHECKED | 109–157 | 195 | duality correct |
| 197 | L:gram-realization | CHECKED | 159–188 | 196 | Schur complement correct |
| 198 | P:gram-entrywise-comparison | CHECKED | 190–214 | 196,197 | correct |
| 199 | L:positive-raw-embedding | CHECKED | 26–123 (ic) | 151,152 | correct |
| 200 | L:positive-physical-gram | CHECKED | 125–175 | 179,199 | entrywise order correct |
| 201 | L:positive-uniform-optimizer | CHECKED | 177–247 | 179,196,198 | correct |
| 202 | P:positive-signed-comparison | LIMITED | 249–332 | 198,200,201 | finite approx chain heavy |
| 203 | P:positive-score-cutoff | CHECKED | 334–371 | 129,202 | continuity correct |
| 204 | T:intrinsic-second-moment | CHECKED | 373–428 | 193,203,132 | assembly correct given prior |
| 205 | L:occupation-raw-square | CHECKED | 24–98 (oc) | 138,199 | correct |
| 206 | P:raw-occupation-energy | CHECKED | 100–164 | 141,205 | dilation correct |
| 207 | L:occupation-rayleigh-selection | CHECKED | 166–216 | 200,129 | correct |
| 208 | T:intrinsic-occupation-ceiling | CHECKED | 228–280 | 206,207 | scalar max correct |
| 209 | C:intrinsic-spatial-bracket | CHECKED | 282–334 | 139,208 | correct |
| 210 | L:white-cdf-square | CHECKED | 13–59 (we) | none | identity correct |
| 211 | P:white-spatial-energy | CHECKED | 61–108 | 210 | \(c/\sqrt3\), \(c^2/6\) correct |
| 212 | T:white-moment-bounds | CHECKED | 110–138 | 209,211 | (2/3) factors correct |
| 213 | C:white-relative-width | CHECKED | 140–173 | 133,212 | CS at \(a=1/2\) correct |
| 214 | L:translated-covariance-CS | CHECKED | 708–802 | none | feature-map CS correct |

---

## (3) Coupled premise/application graph for the final upper and lower bounds

### Lower bound (final value \(C_2=S_2^{\mathrm{pos}}\))

```
masked spatial Wick measures [005]
      -> joint fixed order [006]  -> (all ordering/regularization limits)

Chen-author Thm 3.1 (imported)  -----+
Chen-author (co)variance conventions ----+--> fixed-order construction [006,008]

driver parameters [wave variance 069-074]
      -> actual operator driver [085-093]
      -> constant phase/Young [104-111]
            -> raw block inputs [120]
                  -> Gaussian shift law [121]
                  -> block error [122], cone lifting [123], source restart [124]
                        -> raw block point comparison [125]
                              -> raw block original lower [126]

compact ground family [112-118] (Teschl imports)
      -> unmasked Rayleigh rate [129]
            -> remove masks [130]
                  -> positive variational scores [132]
                        -> Q2 >= S2^pos  (and S2 = 2^{(4-α)/(3-α)} S1)
```

The lower bound’s own finiteness of \(S_2^{\mathrm{pos}}\) is not used; only positivity/floating test is local.

### Upper bound (final value \(C_2=S_2^{\mathrm{pos}}\))

```
Crouzeix–Palencia Thm 6 (imported) -> complex phase [039] -> interval complex [045]
        -> fixed split [047] -> interval coefficients [048]
              -> full upper T:full-upper [051]   (independent, supplies finiteness to [132])

Cameron spatial/temporal operators [142-146]
        -> uniform mean regulator [154]
              -> uniform actual Cameron [155]
                    -> radius anchor [156-160]
                          -> tube actual law [173]
                                -> tube coarse envelope [175] (Borell/Young imports)
                                      -> signed score envelope [190]
                                            -> signed bulk-tail [191]
                                                  -> signed operator upper [192]

point-transfer cone [185-189] reduces original point to operator moment M_δ
symplectic raw [168] supplies ||P_δ|| >= 1

        -> original signed point upper [193]:  limsup point <= limsup_δ S_{R_δ}

positive Gram comparison [194-198]
        -> positive signed comparison [202]:  S_R <= S2^pos for all R
              -> positive score cutoff [203]:  lim_R S_R = S2^pos
                    => limsup point <= S2^pos
```

### Matching and imports

- `T:intrinsic-second-moment` [204] pairs [132] (lower) with [193]+[203] (upper).
- Imported-theorem nodes: Chen-author Thm 3.1; Chen–Hu Thm 1.2/(5.1)/(5.15)/(3.8)/(2.17)/(2.19)/(2.22); Chen2023 Thm 1.1; Crouzeix–Palencia Thm 6; Friz–Hairer Young §4.1 and Borell Thm 11.6; Teschl 2.14/3.6/4.12–4.13/10.2/10.13. Balan–Conus appears only as a comparison remark, not a premise.

### Unresolved edges, cycles, uniformity/order

- **No cycle.** `T:full-upper` [051] does not depend on the final variational value; it is used only to bound \(S_2^{\mathrm{pos}}\) in [132]. The matching [202]/[203] does not feed back into [051].
- **Order of limits** in the upper bound is \(\delta\downarrow0\) at fixed \(B\), then \(B\to\infty\) ([191]/[192]); mask removal is \(R\to\infty\) after the time liminf/limsup ([130]/[203]). No interchange of these orders is asserted.
- **Unresolved (audit-level, not mathematical) edges** are the heavily compressed operator-convergence layers listed in §6; I do not certify them independently.

---

## (4) External theorem-family dispositions

| Import | Edition examined | Exact source statement | Application observed | Verdict |
|---|---|---|---|---|
| Chen-author Thm 3.1, (3.3)–(3.6) | held 64p author file | two-chain pairing bound with partition \(Q_0,Q_1,Q_2\), finite \(\mu_{j,k}\), Laplace temporal domains | used in 006/007/008 after regularization | **consistent**; N2 corrects the repeated-\(x\) display |
| Chen-author Thm 4.1, Lemma 4.4, App A.1 | held author file | fixed-order \(L^2\) limit, (4.3) | **not imported analytically** (manuscript proves its own 006/007) | correctly excluded |
| Chen-author (1.5), homogeneity ⇒ \(\alpha+\alpha_0<2\) | author file | stated | hypothesis guard | consistent |
| Chen–Hu Thm 1.2 (1.9) | published AOP53 2144–2195 | \(t^{-(4-\alpha)/(3-\alpha)}\log E u^p \to \frac{3-\alpha}{2}p^{\frac{4-\alpha}{3-\alpha}}(2\sqrt{\mathcal M}/(4-\alpha))^{\frac{4-\alpha}{3-\alpha}}\) | static rates \(p=1,2\) in 054/057 | consistent; \(E U^2\) rate \(=2^{\kappa_{st}}L_0\) matches \(p=2\) |
| Chen–Hu (5.1), (5.15) | published | total-order-\(2k\) scaling and factorial coefficient rate | 024/027/033 | consistent; \(p=2\) gives rate \(\le 2(2\sqrt{\mathcal M}/(4-\chi))^{4-\chi}\) |
| Chen–Hu Thm 3.8(i); (2.17),(2.19),(2.22) | published | fixed-order \(L^2\) limit under Dalang; product/Wick with generalized-covariance heat convention (2.18) | static fixed orders | consistent |
| Chen–Hu p. 2175 dilation \(E_{1/2}=2^{\chi/(4-\chi)}\mathcal M\) | published | half-gradient square-root identification | 027/033 | consistent; homogeneity check verified |
| Chen2023 Thm 1.1, (1.4)/(1.5) | published EJP | finiteness of both variational suprema under Dalang, generalized \(\gamma\ge0\) | static finiteness; 036 energy bound | consistent |
| Crouzeix–Palencia v1 Thm 6 | author v1, (3) p. 1, Thm 6 pp. 5–6 | \(\|f(T)\|\le(1+\sqrt2)\sup_{W(T)}|f|\) for bounded \(T\) | 039/045 | consistent |
| Friz–Hairer §4.1 (4.3); §1.4–1.5; Thm 11.6 p. 190 | 2020 2nd ed | Young estimate \(\| \int_s^t Y\,dX - Y_sX_{s,t}\|\le C [Y]_\beta[X]_\alpha|t-s|^{\alpha+\beta}\); Borell enlargement \(\mu((A+rK)^c)\le\bar\Phi(\hat a+r)\) | 107/149/150/171 | consistent |
| Teschl 2.14 p. 81; 3.6 (3.51)–(3.53) p. 109; 4.12/4.13 pp. 140–141; 10.2 p. 258; 10.13 p. 273 | 2nd ed 2014 | closed-semibounded-form operator; spectral form domain; max–min; Schrödinger self-adjoint/\(\sigma_{ess}\)=\([0,\infty)\); simple positive ground state | 112–116, 162–164, 179 | consistent |
| Balan–Conus Thm 2.1(b) p. 1492 | AOP44(2016) | Skorohod upper exponent \((2H+2-a)/(3-a)\) | **comparison only** (014/023/024 remarks) | not a premise; constant/normalization not imported |

---

## (5) Repairs / concrete source locations, and (separately) presentation notes

**Repairs (already supplied inside the manuscript, and correct).**

1. **Chen-author (3.5), p. 14 (physical), second Green factor repeats \(x\).** The manuscript’s `L:damped-homogeneous-norms` (main file lines ~586–612) and `Remark R:source-case2-time-shift(ii)` use independent spatial variables \(G(s,x)G(t,y)\). This is the correct pairing; the printed duplicate is a source display defect. Location: main file, `R:source-case2-time-shift(ii)` (lines within 708–802 region) and the definition `E:damped-norm-definitions`.
2. **Chen-author Theorem 3.1 Case 2 time-shift.** The manuscript states the source’s first Case-2 equality omits the predecessor time offset \(A-B\) (main file, `R:source-case2-time-shift(i)`, lines within 708–802), and replaces it by `L:translated-covariance-CS` (214), which retains the offset through the feature-map Cauchy–Schwarz with coefficient one. This is a genuine repair of a source equality; the retained comparison is correct.
3. **Chen-author Remark 5.1/(5.4) uniformity issue.** `R:source-uniformity` (main file, ~513–522 region) correctly identifies that the printed \(C\) “independent of \(n,t\)” is inconsistent with the white-order-one test (003); the manuscript repairs via `P:crudeCorrected` (007) with explicit \(\theta_0\). Not a premise of the main scale argument.
4. **Excluded edition.** `chen-arxiv-v1` Theorem 1.2 differs; the manuscript never uses it as authority. Correctly excluded in `source-editions.json`.

**Presentation notes (not defects):**

- The weighted bound in `L:d1-spatial` (“weighted AM-GM”) is in fact the Lagrange optimizer for \(\prod h_i \prod h_j^{1-\alpha}\); the labelling is misleading but the displayed bound is valid.
- Several “source-fidelity” remarks assert defects in the primary extraction; since the extraction itself may garble mathematics (per `scope.txt`), I treated only the mathematically forced corrections (3)–(4) above as repairs, not the anecdotal ones.

---

## (6) Honest reading limits and what this report cannot establish

- **Not fully reconstructed (LIMITED, outline-level only):** 005, 006, 009, 020–021, 025–028, 030–035, 037–040, 042–048, 051, 052, 054, 056, 060, 064, 069, 071–074, 085–093, 095, 097–100, 102, 105–111, 112, 114–116, 120, 122, 124–126, 147–148, 155, 158, 161–164, 166–170, 173–175, 178–182, 184, 186–189, 202. For these I verified the stated hypotheses, key constants, parameter guards, and the actual premise/discharge wiring, but did not re-derive every Bochner-integral, weak-limit, almost-sure event, or \(\varepsilon\)-estimate.
- **Specifically uninspected at full depth:** the last operator-convergence step in the Hölder path limit (092/093); the joint-almost-sure unification in source conservation (167/168); the uncompressed measurability/cylinder identification in the Gaussian tube support (170/173); the precise static coefficient constant transfer inside three-transfer (033).
- **What this report cannot establish:** (i) source-pixel/final-manuscript render correctness; (ii) any numeric enclosure of \(C_2\) beyond the white bounds \((2/3)\sqrt{c/M_a}\le C_2\le(2/3)\sqrt{cK_0(a)}\); (iii) equality of the auxiliary \(S_1^{\mathrm{pos}}\) with an actual first-moment limit or any Chen printed first-moment constant — the manuscript explicitly does **not** claim this; (iv) a final cold-review verdict replacing a full independent line-by-line re-proof of all 214 items.

**Bottom line.** The supplied coupled argument is coherent and its final constant-matching chain is fully wired, with all imported theorems used inside their published scopes. I found no decisive fatal flaw in the main chain; the residual uncertainty is concentrated in the long operator-theoretic cylinder (driver/source/tube/symplectic), which remains only outline-verified in this audit.