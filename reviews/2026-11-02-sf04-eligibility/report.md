# Review Result — deepseek

- category: paper-review-deepseek
- model: deepseek/deepseek-v4-pro
- verdict: PASS_WITH_NOTES
- confidence: MEDIUM

## Critical findings

No blocking mathematical defect was found **inside the assigned actual-law/application chain** (E01–E10). The chain now closes: all 17 formerly omitted upstream claims are present with complete proofs, the imported Teschl/Friz–Hairer statements are applied with their exact hypotheses, and the author’s rebuttals of the prior report’s findings E07/E08 are **mathematically correct**. I do not reproduce the earlier PASS_WITH_NOTES/MEDIUM as a vote; it remains preserved and is not upgraded.

Items that remain gate-level open (not defects of this scoped chain, but required before any full release):

1. **SF04-01/07/11 and all 21 image obligations remain unverified.** No PNG is supplied in this text-only packet; edition/title/copyright/pagination/printed-offset attestation is impossible here. This is a hard full-SF04 gate.
2. **Imported primary theorems are applied, not re-proved.** Teschl 2.14/3.1–3.2/3.6/4.12–4.13/10.2/10.13 and Friz–Hairer Thm 11.6 and (4.1)–(4.3) are checked for exact-hypothesis fit but their proofs are, by scope, not audited.
3. **External imports outside the embedded packet** — Chen–Hu Theorem 3.8(i)/(5.1)/(5.15)/Thm 1.2 and Chen 2023 Thm 1.1 (finiteness) — appear in auxiliary sections (`L:static-holder-input`, `L:planar-static-input`, `P:three-transfer`) and in calibration remarks. They are **not inputs** to the main intrinsic-constant chain, but if whole-argument clearance is claimed they must be supplied or explicitly bounded as non-input.
4. Meta-claims of “existing local Lean certificates” (`R:gram-controls`, `P:white-spatial-energy`) are unverifiable from this packet and read as work-flow metadata inside a mathematics file; they should be removed or re-scoped.

## Noncritical findings

- **Loose generic constant naming** (`L:signed-score-envelope` uses `C_gr`; `P:tube-coarse-envelope` uses `c_Y=c_Y(B,θ)`). Both are legitimate finite bounds; the passage “These computations give the displayed coefficients” absorbs constants by enlargement. Acceptable, but the same-name/different-name transition should be made explicit to avoid an apparent constant mismatch.
- **`P:uniform-mean-product` good-block prefactor phrasing** (“its norm bound is at most K/B ≤ K”) is loose; the actual prefactor `L_{B,K}=log16+4log(1+K)+3log(1+B)` dominates the true `8(1+K/ B)^2(1+B)` bound. Correct in substance, confusingly worded.
- **`P:white-spatial-energy`/`R:gram-controls`** interleave “existing conditional deductions/certificates” between the analytic proof and the claim; the analytic content checks out (sech profile attains `R_sp=c/√3`, energy `c²/6`), but the certification sentences are foreign to the mathematics and should be segregated.
- **Abstract phrasing** “component proofs have passed scoped independent reviews” is honest and hedged (fresh whole-argument and cold reviews remain pending); no overclaim found.

## Checked derivations

- **Raw-noise completion and driver.**
  - Temporal covariance completion (Schur bound `2T^{1−a}/(1−a)`, separability) `L:masked-time-completion`; actual-noise spectral form `(2π)^d∫‖F̂(ξ)‖²_{H_a^C}μ(dξ)` `P:masked-noise-completion`.
  - Translation/spectral-growth mask bounds `P:masked-spectral-growth`; auxiliary `ν_R` control `P:masked-auxiliary-norm`.
  - `A_j(I)`: gain `E_r→E_{r+1}`, `D_χ` localization, `E[g_j ℓ_R(I;z,w)]=⟨A_j(I)z,w⟩` `L:driver-gain-localization` — correct, mask after convolution, both phase entries.
- **Gaussian driver construction.**
  - `X_N→M_R` in `L^p(C^θ)`; row identity `⟨M_R(t)z,w⟩=ℓ_R((0,t);z,w)`; `κ_p≤C√p`, square-exponential moment `P:actual-operator-driver` + `L:driver-holder-limit`. Finite-Gaussian `S_p` bounds with **both** output/input variances (`P:finite-gaussian-matrix`, explicit fourth-moment counterexample `R:gaussian-one-variance-test`) are correct.
  - `L:cutoff-factorization`/`P:cutoff-singular-values`: torus factorization, singular value bound `C j^{−γ/d}`, `S_p` for `pγ>d` — correct; `Λ^{−γ}` noncompactness witness valid.
  - `P:source-gaussian-transfer`: variance-bound extension and path transfer, `√C` comparison, tail/stability — correct.
- **Source and retaining construction.**
  - `Φ:H_W→𝒢` retaining isometry with `2λ∫_{−∞}^{min(t,u)}e^{-λ(t+u−2r)}dr=e^{−λ|t−u|}`; source/residual domination; `D_ρ→0` at arbitrary rates; joint covariance `K_{max(η,η')}(t−s)Γ_{ε+ε'}(x−y)`; same-W retention `I(Φh)=W(h)` (`P:source-canonical-convergence`, `L:source-retaining-isometry`) — correct.
  - `P:source-ordinary-response`, `P:masked-source-moments`, `P:masked-canonical-transfer`: Bochner/ordinary identification, `LGauss` same-W with fixed-order diagram limits; no new pathwise realization asserted.
- **Mean/Cameron/regulator chain.**
  - `L:cameron-supported-tensor` (tensor/full-basis), `P:cameron-full-mean` (compact `H→L^r(I;K(F))`, tail `ε_J→0`), `P:uniform-mean-regulator` (`Q_{J,K}` decomposition, `M_Θ ε_J + M_f c_t K^{-β}`) — correct.
  - `P:uniform-actual-cameron`: covariance `(Lh)_m(u)=√δ∫S_E(−v) T_R(Q_{J,K}i_I^* h)(s_m+δv)S_E(v)dv`; `C_{B,E}≤18B^{3−1/r}`; `‖Lh‖_{δ,p}≤√δ C_{B,E}(2/B)^{1/p−1/r}[M_Θε_J+M_fc_tK^{−β}]‖h‖` — scale `g_δδ^{a/2}=√δ` verified.
- **Residual/anchor.**
  - `L:cameron-actual-residual` (first-chaos labels in `H_I`, closed projection transfer), `C:radius-covariance-residuals` (`√C` transfer; `(I−Π)` contraction), `P:radius-mean-anchor` (`E Z_δ≤(2/B)^{1/p}C√p g_δ R^{d/Q}`; decay exponent `(1−a)/2−d/Q>0` from `Q>2d/(1−a)`) — correct.
- **Wiener/Borell.**
  - `P:tube-wiener-realization`: `H_CM=C(H_seen)`, `‖Ch‖_CM=‖P_seen h‖_H`, full support, measurable-norm tail — correct. `L:tube-closed-geometry`: `T_r=A_δ+M_δ(B̄_H(r))=A_δ+(r/√δ)K`; `μ(A_δ)≥1/2`, `â≥0`; `P(d_δ(X)>r)≤e^{−r²/(2δ)}` from Thm 11.6 + `Φ̄≤e^{−y²/2}` — **half-action δ-scale correct**. `P:tube-rayleigh-transfer` (Rayleigh density `(r/δ)e^{−r²/(2δ)}`, layer-cake for monotone `G`, endpoint/jumps/zero law) — correct.
- **Endpoint/symplectic/raw.**
  - `L:symplectic-free` (`ω=⟨·,J_E·⟩`, isometric skew `J_E²=−I`, free group and real-multiplier skewness) — correct. `P:symplectic-source/raw` conservation `P*J_EP=J_E` ⇒ `‖P‖≥1`, invertible — correct. `P:symplectic-block-mean`: unscaled factor is `δ^{a/2}` (not `√δ`); fast-direction `φ_m=δ^{−a/2}T_m^*i_IΦ`; endpoint `≥1` from the deterministic `c=0` symplectic instance — factors cross-check correctly.
  - `P:raw-block-gaussian-law` (`E j(X)=E[e^{−Z/√δ−v/(2δ)}j(X+H)]`, `b=√δH`), `L:raw-block-uniform-error`, `L:raw-block-indexed-cone` (aperture-then-`B` choice, normalized complement budget), `L:raw-block-restart`, `P:raw-block-point-comparison`, `P:raw-block-original-lower` (Riemann error `C_RδB`, `|Z|≤δ^{−1/4}`, `δ^{−3/4}` penalty) — internally consistent; no scalar-moment multiplication in products (operator norms only), both phase entries retained.
- **Rebuttal adjudication (E07/E08), accepted.**
  - Spectral projection contractivity in `‖·‖_{E_σ}`: `Q_σ^sp` is a spectral projection of `H_σ`, so it commutes with `A_σ=H_σ+c`; hence `‖A_σ^{±1/4}Qz‖≤‖QA_σ^{±1/4}z‖≤‖A_σ^{±1/4}z‖`, valid on `L²` and by spectral completion on the dual entry. Prior “contractive” defect is **rejected**.
  - `E_2` continuity through the essential threshold: `|q_σ−q_τ|≤‖V_σ−V_τ‖_∞`, common-form inf/sup commute with uniform translation, Teschl 4.12 carries the essential-threshold level. Accepted.
  - `Γ(B_1)>0`: nonzero Radon `Γ` plus exhaustion of `R^d` by origin-centered balls gives `Γ(B_n)>0`; homogeneity `Γ(B_1)=n^{α−d}Γ(B_n)>0`; local finiteness bounds it. Correct with the origin-centered interpretation now stated at line 11677–11680.
  - Small-`d` log: `x≤1/4 ⇒ −log(1−x)≤x/(1−x)≤4x/3≤2x`, with the zero-residual need for vanishing at 0. Accepted.
  - `δN≤1/B` vs `δn<2/B`: `N` full cells (`m<N`), `n=N+1` all cells; power-means over all cells get `2/B` (line 16560), good/full-cell prefactor counts get `N≤1/B` (line 16581), last cell handled at 16596–16602. No factor-2 error.
- **Scaling/final constants.**
  - `L:exact-canonical-scaling`: vertex factors `T^{-a/2}r_T^{2−α/2}=√δ`, `T^{1−a/2}r_T^{1−α/2}=δ^{-1/2}` verified algebraically (`r_T=T^{(a−1)/(3−α)}`).
  - Gram duality `S(C)=max_A d_A^C` (`P:gram-positive-optimizer`), dual stationarity `ΣC_ijw_j−b_i=ℓ_i²/w_i²`, entrywise comparison — verified, including the explicit counterexample rationale in `R:gram-controls`.
  - White `R_sp=c/√3`, `E_sp=c²/6` (sech attainment); `C_2` bounds `(2/3)√(c/M_a)≤C_2≤(2/3)√(cK_Θ(a))`; relative-width bound with equality at `a=1/2` — algebra verified.

## E01–E10 determinations

- **E01: PASS_WITH_NOTES.** Original raw-noise/source construction is eligible. `P:masked-noise-completion` (7911), `L:driver-covariance-coefficients`/`L:driver-gain-localization` (9535), `P:actual-operator-driver` (9393), `P:source-gaussian-transfer` (10011), `L:cutoff-factorization` (8929), `P:cutoff-singular-values` (9030). Upstream `L:damped-homogeneous-norms` (585) and `L:joint-fixed-order` (876) inspected. Note: `P:masked-quotient-obstruction` (7981) correctly prevents substituting a Hilbert-bounded mask on the whole noise quotient.
- **E02: PASS_WITH_NOTES.** `L:source-retaining-isometry` (10146) gives genuine same-W retention; `P:source-canonical-convergence` (10223) exact joint law; `P:source-ordinary-response` (10394); masked chain/moment/transfer 10485/10564/10629. same-W vs same-law is kept distinct (e.g., 12356 “equality in law, not samplewise identities”; 17071 law/moment identity). External Chen–Hu coefficients are used only in non-input auxiliary routes.
- **E03: PASS.** `L:cameron-supported-tensor` (13561), `P:cameron-full-mean` (13670), `P:uniform-mean-regulator` (14267), `P:uniform-actual-cameron` (14346); minimum raw preimage norm via `ker L=H_seen^⊥` (13888–13914). Scaling `√δ` and `g_δ=δ^{(1−a)/2}` are exact throughout.
- **E04: PASS.** `L:cameron-actual-residual` (13763), `C:radius-covariance-residuals` (14755, actual `C:` prefix), `P:radius-mean-anchor` (14793); `P:radius-actual-moments` (14651) and the three fixed-`Q` guards (14494–14499) verified; decay exponent `(1−a)/2−d/Q>0` correct.
- **E05: PASS.** `P:tube-wiener-realization` (15581), `L:tube-closed-geometry` (15704), `P:tube-rayleigh-transfer` (15762). Thm 11.6 applied to the genuine first-chaos realization with `â≥0`; Borel/closed tubes, `√δ` half-action, `e^{−r²/(2δ)}`, and zero-law case all faithful to the supplied Friz p.190 extract.
- **E06: PASS.** `L:raw-block-restart` (12209), `P:raw-block-gaussian-law` (11961), `P:raw-block-point-comparison` (12301), `L:symplectic-free` (15202), `P:symplectic-source` (15316), `P:symplectic-raw` (15356), `P:symplectic-block-mean` (15444). Both displacement and velocity components are retained; endpoint norm `≥1` and operator-norm product comparisons are used, not scalar displacement-moment multiplication.
- **E07: PASS.** All three author rebuttals accepted (projection contractivity in the `A_σ`-weighted norm by commutation; `E_2` max–min continuity through the threshold; `Γ(B_1)>0` via origin-centered exhaustion + homogeneity). The prior report’s items 1–3 there are rejected without constant change.
- **E08: PASS.** Both rebuttals accepted (small-`d` log `≤2x` for `x≤1/4`; `N` full cells vs `n=N+1` all cells with the correct `1/B` vs `2/B` usages and separate last-cell treatment). The prior report’s items 4–5 are rejected.
- **E09: PASS_WITH_NOTES.** All 17 formerly missing inputs are present and checked: `P:radius-mean-anchor`, `P:uniform-actual-cameron`, `P:cameron-full-mean`, `P:uniform-mean-regulator`, `L:cameron-supported-tensor`, `L:cameron-actual-residual`, `C:radius-covariance-residuals`, `L:raw-block-restart`, `P:symplectic-raw`, `P:symplectic-block-mean`, `L:symplectic-free`, `P:masked-canonical-transfer`, `P:masked-source-moments`, `P:source-gaussian-transfer`, `P:source-ordinary-response`, `L:cutoff-factorization`, `L:driver-gain-localization`. Additional inspected dependencies: `P:masked-noise-completion`, `P:masked-spectral-growth`, `P:wave-two-variances`, `L:driver-holder-limit`, `L:source-spatial-heat`, `P:constant-phase-driver`, `P:constant-young-linear`, `P:constant-compact-base`, `P:compact-ground-family`, `L:compact-fractional-phase`, `P:compact-F-projection/complement`, `P:uniform-E-spectral`, `L:uniform-product-budgets`, `P:uniform-mean-product`, `P:uniform-arbitrary-residual`, `L:positive-raw-embedding`, `L:positive-physical-gram`, `P:positive-signed-comparison`, `P:positive-score-cutoff`, `T:intrinsic-second-moment`. Remaining gaps are the out-of-scope image/edition gates and the external non-input imports listed above; residual risk is complete-text vs verified-proof on the very large but standard spectral-tensor/Banach-Gaussian material.
- **E10: PASS_WITH_NOTES.** The actual-law/application followup closes with no internal circularity found (full-upper ⇒ score finiteness ⇒ lower/upper comparison ⇒ cutoff removal; no step presupposes `T:intrinsic-second-moment`). Prior report and confidence are preserved unchanged. No SF04-01/07/11, full-SF04, whole-synthesis, cold, novelty, goal-clearance, or image credit is claimed.

## Required fixes before production gate

1. Supply and display-verify all 21 assigned PNGs (SF04-01/07/11 and the edition/copyright/pagination plates); text hashes are not visual attestation. Hard gate for full SF04; not changed by this pass.
2. If any whole-argument/full-clearance claim is made, supply or bound the imported Chen–Hu Theorem 3.8(i)/(5.1)/(5.15)/Thm 1.2 and Chen 2023 Thm 1.1 finiteness; currently these are auxiliary and are not inputs to `T:intrinsic-second-moment`, but that boundary must be stated in release metadata.
3. Remove or re-scope the in-manuscript “existing local Lean certificates” sentences (17620, 18519) — they are unverifiable workflow claims, not mathematics.
4. Editorial: unify the generic Young-growth constant naming between `P:tube-coarse-envelope` and `L:signed-score-envelope`, and tighten the “K/B ≤ K” prefactor sentence in `P:uniform-mean-product`.
5. (Optional) Add one explicit sentence in `L:compact-raw-profile` that the positivity test `Γ(B_1)>0` follows from origin-centered exhaustion plus homogeneity; the argument is already implied and author-correct, but the in-text “some ball” wording should be pinned to the origin-centered reading.

## One-line summary

The previously incomplete SF04-10 actual-law/application chain now closes on the full 28-file packet: all 17 formerly omitted inputs are present and logically coherent, the Teschl/Friz applications are faithful to their exact hypotheses, and the author’s E07/E08 rebuttals are accepted — leading to PASS_WITH_NOTES/MEDIUM for this scoped followup, with the image/edition gates (SF04-01/07/11) and full-SF04/synthesis/cold clearance remaining open and the prior report preserved unchanged.