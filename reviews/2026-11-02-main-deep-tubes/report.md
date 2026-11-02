# Review Result — deepseek

- category: paper-review-deepseek
- model: deepseek/deepseek-v4-pro
- verdict: PASS_WITH_NOTES
- confidence: HIGH

## Critical findings

None. I found no false identity, no sign error, no boundary-term error, no incorrect constant, and no invalid asymptotic step in the eight target proofs. The δ-scaling (√δ covariance, r²/(2δ) half-action, e^{F/δ} = ‖endpoint‖²), the Rayleigh transfer, the power-mean envelope, the tail budget, and the half-action supremum all check out algebraically.

## Noncritical findings

1. **PROOF170 measurable-norm check is terse.** It correctly instantiates Gross's finite-dimensional-tail characterization (finite ON families in V_j^⊥, regression, Jensen, Markov ε³/ε²=ε) but never states the abstract "measurable norm" criterion it is verifying. Mathematically equivalent; a one-line recall of the characterization would improve auditability.
2. **PROOF173 compactness and the √δ covariance identity are interface-referenced, not re-derived.** They are delegated to P:cameron-full-mean (compact T into L^{r_t}(I;𝒦(E)) at fixed R), P:symplectic-block-mean (E[M_m(u)W(i_IΦ)] = δ^{a/2}H_{m,E}(Φ)), and P:uniform-mean-regulator (‖𝒯_R‖ ≤ C_mean). I verified these interfaces are consistent and spot-checked the key computations, but the prerequisite bodies are not exhaustively re-derived here (permitted by scope; flagged below).
3. **PROOF174 endpoint cocycle is interface-referenced.** It rests on L:raw-block-restart (noise-only cocycle) plus the closed-isometry intertwining P_F i = i P_E and P:symplectic-raw giving ‖endpoint‖ ≥ 1. Consistent at the interface; not re-derived.
4. **C_env is B-dependent.** D_0, D_1, D_2 depend on B (via G_B, C_pr, c_Y(B,θ), 2/B factors). The stated "independent of δ and R≥1" is exactly true; the statement correctly does **not** claim uniformity in B. No overclaim, but the B-dependence should be kept explicit in any downstream use.
5. **COARSE-vs-C_gr distinction respected.** PROOF175 uses only the fixed-B generic Young constant c_Y = c_Y(B,θ); it never conflates this with the later quantitative C_gr(θ) growth bound. Correct per scope.

## Checked derivations

**PROOF170 (P:tube-wiener-realization).**
- Regression X_j = Σ_{l≤j}W(e_l)C e_l: E[ℓ(X_ω)]-orthogonality gives E[X W(e_l)] = C e_l; with (W(e_l)) iid N(0,1), ⟂ regression is exact.
- ker C = H_seen^⊥: ℓ(Ch)=⟨k_ℓ,h⟩ ∀ℓ ⟺ Ch=0 ⟺ h⊥span{k_ℓ}; C injective on H_seen.
- Cameron norm ‖Ch‖_CM = ‖P_seen h‖: minimum-norm preimage; mon-injective on H_seen; since M_δ = M_δ∘P_seen, unused directions killed.
- L² convergence via monotone class + simple approximation + conditional L² contraction (no RNP needed). Tail label of ℓ(X−X_j) is (I−P_j)k_ℓ ⊥ {e_l}_{l≤j}; joint Gaussianity + countable separability ⟹ Banach tail independence.
- Full support with singular head covariance: positivity obtained from an open ball in the **domain** ℝ^j around the coefficient vector of P_jh (not from inverse image), so singular covariance is harmless. Independence turns this into positivity of every ball about Ch.
- Measurable-norm tail: E‖Σ_k W(h_k)Ch_k‖² ≤ E‖X−X_j‖² < ε³ (conditional-expectation contraction), Markov ⟹ P(‖·‖>ε) ≤ ε uniformly; C:H_seen→H_CM isometric; characteristic functional exp(−‖k_ℓ‖²/2). **All correct.**

**PROOF171 (L:tube-closed-geometry).**
- Closed Hilbert ball weakly sequentially compact (diagonal coordinates + Fatou for ‖limit‖ ≤ r); compact M_δ maps to compact closed image; closed + compact sum closed.
- {d≤r}=T_r incl. r=0 via h_j with ‖h_j‖≤r+1/j, weak limit ‖h‖≤r, M_δ h_j→M_δ h, residual closed. Attainment holds.
- Markov: μ(A_δ) ≥ 1−E‖X‖/(2E‖X‖) = 1/2.
- Exact K = C(B_H(1)) = √δ M_δ(B_H(1)); M_δ(B_H(r)) = (r/√δ)K ⟹ T_r = A_δ + (r/√δ)K.
- Imported Friz–Hairer Th. 11.6 (verified in the embedded carrier, physical p.190 incl. footnote 3): μ((A+tK)^c) ≤ Φ̄(â+t), â = Φ^{-1}(μ(A)) ∈ (−∞,∞], with â ≥ 0 (μ(A)≥1/2) ⟹ Φ̄(â+r/√δ) ≤ Φ̄(r/√δ) ≤ exp(−r²/(2δ)); â=+∞ (μ(A)=1) handled. a.s. finiteness from tail→0. **Correct.**

**PROOF172 (P:tube-rayleigh-transfer).**
- Rayleigh density (r/δ)e^{−r²/(2δ)} has mass 1 and survival e^{−r²/(2δ)} (exact antiderivative).
- Stochastic domination at closed positive endpoints: P(d≥c)=lim_{s↑c}P(d>s) ≤ e^{−c²/(2δ)}=P(R≥c) (Rayleigh atomless); closed zero both =1; ∞-null set defined without G(∞).
- Layer-cake/Tonelli with upper level sets of e^{G/δ} being upper intervals (empty/(c,∞)/[c,∞)/halfline); justification valid for jumping G and infinite expectations.
- Attainment ⟹ F(X) ≤ G(d(X)) a.s., no measurable selection. Zero-law: F(0)≤G(0)≤G(r), Rayleigh mass ⟹ identity. **Correct.**

**PROOF173 (P:tube-actual-law).**
- E[𝒳_δ W(Φ)] = g_δ·δ^{a/2}H = √δ M_δΦ: consistent with P:symplectic-block-mean (M_m = M_R(W∘T_{δ,m}), E[M_m(u)W(i_IΦ)] = δ^{a/2}H_{m,E}(Φ)); g_δ δ^{a/2} = √δ exact (g_δ = δ^{(1−a)/2}).
- Compactness of M_δ at fixed R: compact T (E-compression of compact full mean) ∘ bounded conjugation/pullback/primitive (1−1/r_t > θ), composition compact; E-compression bounded (range of T in iE). No uniform-R compactness claimed. Correct.
- Separability (finite-rank rational matrices, polygonal little-Hölder closure) and zero-start; joint first-chaos Gaussianity of all blocks (same W; no independence needed); labels in H_I via L:cameron-actual-residual.
- Expected radius: P:radius-mean-anchor, zero projection ⟹ E Z_δ ≤ (2/B)^{1/p}C√p·g_δ R^{d/Q}; R_δ = δ^{-1}+2 ≤ 3/δ ⟹ b_δ ≤ C_{Q,B,p}δ^{(1−a)/2−d/Q}→0 since Q > 2d/(1−a). I re-derived the linearity/power-mean step in the anchor; exponent sign correct. **Correct.**

**PROOF174 (L:tube-actual-endpoint).**
- F_δ continuous on all B_δ: generic Young (θ>1/2) locally Lipschitz; product/norm/log max(1,·) continuous.
- Ordered product P_δ(x)=P_N…P_0 with P_m = S_E(ℓ_m)U_{x_m}(ℓ_m,0) matches restart cocycle P_glob(NB+τ,0)=D_{X_N}(τ)…D_{X_0}(B); E-restriction via closed isometry i (P_F i = i P_E); local source pointfield = time shift by mB of global δ^{a/2}Y^ρ(δu,·); source limits on fixed (N+1)B before composition. True partial last cell τ.
- P:symplectic-raw (c=g_δ, Φ=0, T=L_δ) ⟹ ‖endpoint‖≥1 ⟹ e^{F_δ/δ} = ‖endpoint‖². Zero law: free product S_E(L_δ), norm ≥ 1 by symplectic identity (no claim it equals 1). **Correct.**

**PROOF175 (P:tube-coarse-envelope).**
- log‖P_m‖ ≤ log G_B + c_Y(1+‖x_m‖^ν); convexity (a+b)^ν ≤ 2^{ν−1}(a^ν+b^ν) ⟹ free term 2δn(log G_B+c_Y) + 2^ν c_Y δΣ(v_m^ν+h_m^ν); RHS ≥ 0 controls log max(1,·).
- Power means δΣv^ν ≤ (δn)^{1−ν/p}‖a‖^ν, δΣh^ν ≤ (δn)^{1−ν/r_t}(δΣh^{r_t})^{ν/r_t} (exponents p/ν≥1, r_t/ν>1; legal at p=ν; zeros fine).
- Primitive sum: h_m ≤ C_pr δ^{−1/r_t}‖𝒯_RΦ‖_{L^{r_t}(I_m)}, δΣh_m^{r_t} ≤ (C_pr C_mean)^{r_t}‖Φ‖^{r_t} (affine Jacobian δ^{-1} cancels the δ weight; true partition). C_pr = G_B²[B^{1−1/r_t}+B^{1−1/r_t−θ}], G_B ≤ 3B, C_pr ≤ 18B^{3−1/r_t} from P:uniform-actual-cameron.
- δn ≤ 2/B (n=N+1); D_0, D_1, D_2 exact; C_env = 1+D_0+D_1+D_2 independent of δ, R (B-dependent) ⟹ G_δ(r) ≤ C_env(1+b_δ^ν+r^ν). G_δ nondecreasing ⟹ Borel; supreme finite (no attainment claimed). Rayleigh transfer + global endpoint ⟹ operator-moment bound. **Correct.**

**PROOF176 (L:tube-rayleigh-tail).**
- r^{2−ν} ≥ M^{2−ν} ≥ 4C ⟹ Cr^ν ≤ r²/4; r² ≥ M² splits the remaining −r²/4 into −M²/8−r²/8 ⟹ Cr^ν−r²/2 ≤ −M²/8−r²/8.
- −(d/dr)[4e^{−r²/8δ}] = (r/δ)e^{−r²/8δ} exact; ∫_M^∞(r/δ)e^{−r²/8δ}dr = 4e^{−M²/8δ}; total 4e^{(A_0−M²/4)/δ}. Cutoff exists (2−ν>0); [0,M] finite; C=0 case valid. **Correct.**

**PROOF177 (L:tube-half-action).**
- Lower: r=‖h‖, g_J(‖h‖)≥J(h). Upper: ‖h‖≤r ⟹ J(h)−r²/2 ≤ J(h)−‖h‖²/2; sup over ball then over r. J finite-valued, bounded above on balls ⟹ no ∞−∞. No compactness/rank/attainment/continuity used. **Correct.**

## Required fixes before production gate

None blocking. Two optional clarity items:
1. In PROOF170, state the measurable-norm criterion being verified (Gross's finite-dimensional-tail form) in one sentence before the tail computation.
2. In PROOF175, add explicit notation "C_env = C_env(B)" or a remark "B fixed; constants may grow with B" so the "independent of δ and R" clause cannot be misread as B-uniform.

## One-line summary

All eight actual-Gaussian tube/Rayleigh proofs (170–177) are mathematically sound with correct δ-scalings, signs, power-mean and Rayleigh-tail constants, the Borell scale √δ, the expected-radius decay exponent (1−a)/2−d/Q, and honest scope statements (no uniform-R compactness, no sharp-envelope or point-transfer overclaim); the only caveats are interface-flagged prerequisites (compact mean field, √δ covariance, restart cocycle, symplectic norm ≥ 1) that were verified at the statement/derivation interface rather than re-derived line-by-line.

## Proof statuses (PROOF170–177)

- PROOF170 P:tube-wiener-realization: **CHECKED**
- PROOF171 L:tube-closed-geometry: **CHECKED**
- PROOF172 P:tube-rayleigh-transfer: **CHECKED**
- PROOF173 P:tube-actual-law: **CHECKED** (compactness + √δ covariance interface-verified)
- PROOF174 L:tube-actual-endpoint: **CHECKED** (restart cocycle + symplectic baseline interface-verified)
- PROOF175 P:tube-coarse-envelope: **CHECKED**
- PROOF176 L:tube-rayleigh-tail: **CHECKED**
- PROOF177 L:tube-half-action: **CHECKED**

## TUB01–TUB14 checks

- TUB01 (PROOF170 finite first-chaos regression, no RNP): **PASS**
- TUB02 (support/Cameron/AWS, singular-head full support, measurable norm): **PASS**
- TUB03 (closed tubes, weak-sequ. compactness, r=0 attainment, no selection): **PASS**
- TUB04 (exact Borell offset/scale, √δ unit ball, â≥0 incl μ(A)=1, no variance proxy): **PASS**
- TUB05 (Rayleigh mass/survival, jumps via closed endpoints, zero law F(0) not forced 0): **PASS**
- TUB06 (actual Gaussian eligibility: separability, same-W joint first chaos, labels H_I, rank-zero √δ): **PASS**
- TUB07 (expected radius via radius-anchor, Q>2d/(1−a), δ^{(1−a)/2−d/Q}→0): **PASS**
- TUB08 (global endpoint F_δ continuous on all B_δ, true last cell, F→E intertwining, norm≥1): **PASS**
- TUB09 (coarse constants G_B≤3B, C_pr≤18B^{3−1/r_t}, C_mean, c_Y(B,θ) generic): **PASS**
- TUB10 (exact moment transfer: 2^ν c_Y δ-sum, D_0,D_1,D_2, C_env uniform in δ,R): **PASS**
- TUB11 (tail 4e^{(A_0−M²/4)/δ}, 2−ν>0 cutoff, no Gaussian density): **PASS**
- TUB12 (global half-action sup equality, no ∞−∞, no compactness/rank): **PASS**
- TUB13 (hypotheses/adversarial/source ledger; Theorem 11.6 + footnote 3 only, 11.7 unused): **PASS**
- TUB14 (eight-proof depth/scope; prerequisites reference-only; no verdict/status premises, no gap-closing assumptions): **PASS**

## Completion and limitations statement

- I audited only the line-numbered target excerpts of `integrated_gaussian_tubes.tex` (packet lines 1–570) plus the embedded bounded-context prerequisites and the embedded Friz–Hairer carrier (physical pp. 190–191: Theorem 11.6, footnote 3, and the standard-normal tail Φ̄(y) ≤ e^{−y²/2}). I did not open Progress.md/Review.md/any reviews directory or `packet.md` itself, and used no tools, numerics, delegation, or external sources.
- **Exhaustively re-derived:** the regression/Cameron identification, full-support, Borell/√δ scale, Rayleigh transfer with jumps, expected-radius exponent, endpoint continuity/cocycle, coarse envelope (all power-mean and Young constants), Rayleigh tail, and half-action lemma.
- **Verified at statement/interface level but NOT exhaustively re-derived (flagged, as the scope permits):** (i) P:cameron-full-mean compactness of 𝒯_R into L^{r_t}(I;𝒦(E)) at fixed R and its E-compression; (ii) E:cameron-actual-covariance / P:symplectic-block-mean rank-zero identity E[X_m W(i_IΦ)] = δ^{a/2}H_{m,E}(Φ); (iii) P:radius-actual-moments ‖M_R(Y)‖_{L^p(C^θ)} ≤ C√p R^{d/Q} under the three fixed-Q guards (the anchor's linearity/power-mean step I did re-derive); (iv) L:raw-block-restart noise-only cocycle and its source-limit argument; (v) P:symplectic-raw conservation/norm≥1 limit passage. All five were read in the supplied bodies and their statements match the usage; no contradiction surfaced.
- **Citations verified in-project:** Theorem 11.6 + footnote 3 (Borell set enlargement, outer-measure caveat) are present in the embedded `friz-hairer.txt`; Theorem 11.7 (generalized Fernique) is present but correctly **not** used. The distinction "Borell set enlargement, not Theorem 11.7" is respected.
- **Honesty/overclaim check:** the eight proofs contain no overclaim. The closing paragraph of the target section explicitly defers the sharp spectral/product envelope, the original point-moment transfer, and the variational comparison to separate proofs; "no uniform-radius compactness," "each fixed-parameter event only," and "coarse envelope not sharp" are all stated truthfully. Historical review/status annotations in the surrounding manuscript are not used as mathematical premises in any of the eight proof bodies.