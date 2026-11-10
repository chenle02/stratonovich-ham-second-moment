# Independent AUTHOR check of the four actual variance calculations

2026-11-04; exact science af97. Read the complete frozen22,708B `full-working.md`, full prerequisite table and analytical controls against actual covariance foundation and wave source. The checked deductions are PROOF069/071/073/074;070/072 and the relevant061–068 application clauses were also checked. No concrete mathematical/source mismatch was found in those assigned calculations under their exposed hypotheses. This is a bounded author check, not an independent-family review, proof acceptance, confidence recommendation or075–093 path construction.

Exact capsule SHA74fe15e7428c9e7368977296c14eb4b276155b76873a2ad2565e03d5fda1b54c. Exact source anchors and independently recomputed body/statement/module hashes are in `bindings.json`. All frozen capsule members and current28 module hashes were verified unchanged after this read-only audit.

## 1. Actual spectral/temporal premises and numerical constants

The translated estimate uses BOTH positivity properties in their actual places: μ is positive for spectral integrals; physical Γ≥0 permits removal of the Gaussian test's phase. Directly,

    ∫exp(−|ξ−y|²/r²) μ(dξ)
      =(r/(2√π))^d∫exp(−r²|x|²/4)exp(−iy·x) Γ(dx).

The homogeneity pushforward is r^(α−d), hence the right absolute value is ≤r^α MΓ/(2√π)^d. The Gaussian is ≥e⁻¹ on the ball, yielding CΓ=eMΓ/(2√π)^d, uniformly in center. This is not a radial/angular-density assumption. Positive α rules out spectral atoms by the small-ball bound; it does not rule out the physical white atom. Real ζ gives even |k_R|. Tonelli and ||k_R||₁=Lζ give the actual auxiliary growth Cν=c_d²Lζ²CΓ for every R>0. It is this growth, not an R-uniform bound on the auxiliary density, that is consumed by069/073.

The displayed resolvent calibration is consistent: μ(B_r)=V r^α gives ∫(ρ²+|ξ|²)⁻¹μ(dξ)=Rα ρ^(α−2), Rα=απV/[2sin(πα/2)]. The translated-growth inequality follows instead from layercake with2C∫r^(α+1)/(ρ²+r²)²dr, giving the same α factor times C, not an asserted homogeneous identity for ν_R. For white cδ in d1, V=c/π and R1=c/2. The units/covariance amplitude are retained.

For temporal modulation, differentiating the moving endpoint really gives |c'|≤M²+hMD and f(1)=0. For k=|hω|>1 the split/IBP terms are bounded by

    K² k^(a−1)[1/(1−a)+1+1+1/(1−a)]
      ≤4K² k^(a−1)/(1−a), K=M+hD.

Restoring2h^(2−a) and k^(a−1)≤√2〈k〉^(a−1) costs at most8√2/(1−a), below C0=16/(1−a). For k≤1 the direct2/(1−a) estimate and bracket lower bound also fit C0. These are bounds for the temporal norm SQUARED. Trigonometric coefficient sum is one and weighted Hilbert Cauchy gives half of the stated Q_h bound; using the larger displayed bound is safe. Repeated/resonant frequencies are not orthogonalized.

The low-frequency b_r representation has coefficient≤√2 per sine quotient, hence≤2 for a product and squared cost4. For t^j, j=0,1,2, M+hD≤1,T+1,T²+2T, respectively, whose squares are ≤(1+T)^4. Altered h(r±ρ) changes by at most2. Bracket comparability costs3^(1−a). Thus C1=4·3^(1−a)C0 and A_T=C1(1+T)^4 are genuine upper bounds, including frequencyzero.

## 2. PROOF069: near/far exponents and the critical logarithm

Source: wave LF56–145. The compact near region uses only the pushed measure's centered growth. With q=max(1,|ξ|), N=ceil(log₂(5q)),

    Aξ(q)≤C[1+2^α Σ(j<N)2^(j(α−1))].

This is constant for α<1, O(1+logq) for α=1 and O(q^(α−1)) for α>1. Multiplication by2q^(−ε), ε=1−2γ>0, bounds the first two cases, using max_(u≥0)u exp(−εu)=1/(eε). In the third case the exponent is α+2γ−2<0. No dependence on an invented shell density or dimension enters K.

On |λ|=r>4q the three inequalities |ξ−λ|≥3r/4, ||ξ−λ|−|ξ||≥r/2 and |ξ−λ|+|ξ|≥r/2 are all valid. Since a−1<0, the two Q brackets contribute2^(2−a), and the inverse Bessel denominator contributes4/(3r). Thus the exact far prefactor before shell masses is(4/3)2^(2−a). A dyadic shell mass contributes at most2^α C, so one admissible aggregate K is

    K = N_(α,γ) + (4/3)2^(2−a+α) E_(α,a),

where N bounds the displayed near calculation and E bounds S(h)/Bα(h) in the capsule. For L=floor(log₂1/h), high shells have exponent b=α+a−2<0:

    h^(a−1)2^((L+1)b)/(1−2^b)
      ≤h^(1−α)/(1−2^b).

Low shells give constant,1+log₂1/h, or a constant times h^(1−α) in the three α cases. For α<1 the extra h^(1−α)≤1; for α=1 it is constant; for α>1 it agrees with Bα. This checks every regime, including h=1,L=0. Natural-log/base2 conversion is absorbed into K, not silently set equal. Constants may diverge at the excluded α/γ/a boundary gaps; none are asserted uniform there.

The time exponent window in070 is precisely β_H>1/2 below both1−a/2 and(3−a−α)/2. For α=1, d₀=2−a−2β_H>0 gives h^d₀(1+log1/h)≤1+1/(ed₀). Endpoint β_H is not supplied. These conditions follow from the original a<1,α+a<2 and the strict gain range; no weaker endpoint claim is made.

## 3. PROOF071: actual W, the Sobolev adjoint and Fourier cancellation

Source: wave LF258–357. The actual covariance completion, not a new stationary masked field, is used. For the compactly supported masked product, |K|Γ(K−K) times the two spatial supremum norms and temporal Schur bound admits smooth temporal approximations, including interval endpoints. The separate finite-tensor approximation in all Schwartz seminorms gives ε_n〈ξ〉^(−N) Fourier domination. With N large, both tempered μ and ν_R integrate its square. Multiplication by fixed ζ_R preserves this convergence. Thus the raw and auxiliary limits coincide for the actual products; no bounded multiplier on the original raw-null quotient is inferred. The admission constants may depend on R, unlike the final variance estimate.

With inner products linear in the first slot and E=H½×H⁻½,

    S(−t)(0,f)=(−sin(t|D|)f/|D|, cos(t|D|)f).

Moving the E weights to w yields G_w=−(sin/|D|)Λw₁+cos Λ⁻¹w₂. The minus sign and unequal Λ/Λ⁻¹ weights are necessary. Similarly Dχ*E w=(Λ⁻¹χΛw₁, ΛχΛ⁻¹w₂), not ordinary multiplication by χ. The normalized v/G products consequently give exactly

    K=(〈ξ〉〈η〉)^(-1/2)
       [[−b_r c_ρ,−b_r b_ρ],[c_r c_ρ,c_r b_ρ]],
    K(t;0,0)=[[-t,−t²],[1,t]].

For F=v_z conjugate(G_w), the convolution is Fhat(−λ)=c_d∫ΣK_ij U_j(η)conjugate(V_i(η+λ))dη. Even ν_R reflects the spectral argument, and the actual covariance factor(2π)^d cancels the product coefficient squared c_d² EXACTLY. The final normalized bound therefore has ν_R and no additional Fourier factor. Its already defined c_d² in Cν is not removed again.

Complexification is W_C(F)=W(ReF)+iW(ImF) on the same W. Its squared modulus needs no independence. On the spectral side, for real f,g the imaginary mixed term is odd by A(−ξ)=conjugate A(ξ), and even μ/ν_R cancels it. This checks the actual complex variance formula without pretending real/imaginary noises independent. The free group is strongly continuous and bounded on E at finite T; neither E-unitarity nor norm continuity is used.

## 4. PROOF073: both actual Bessel orientations and the factor4

Source: wave LF401–477. For each fixed λ the shifted Schwartz components and finite-horizon bounds on c,b give actual L²(dη;H_a²) kernels. Temporal Schur gives strong measurability/continuity there. The later ν_R integral is a nonnegative Tonelli integral whose finiteness is proved by069, not assumed in advance.

First fix V=Jz in the output slot, vary U_k=Je_k. Set g_j=Σ_i K_ij conjugate V_i. Hilbert-valued Bessel uses the conjugate scalar ON family for coefficients without conjugation; Cauchy over i costs2 and summing j costs2. Hence

    Σ_j||g_j||Ha²≤4A_T h^(2−a)Φ_h(η+λ,η)|V(η+λ)|².

After ξ=η+λ and the row estimate this gives the input-family variance bounded by

    4A_T K Cν h^(2−a)Bα(h)∫〈ξ〉^(−2γ)|Jz(ξ)|²dξ.

Next fix U=Jz and vary the OUTPUT family V_k. Use f_i=Σ_jK_ijU_j, with the conjugated Bessel version. The same two component costs give4, but after changing variables its row is ∫Φ_h(η+λ,η)ν_R(dλ). The displayed equality uses ACTUAL evenness of ν_R, then Φ symmetry:

    ∫Φ_h(η+λ,η)ν_R(dλ)
      =∫Φ_h(η,η−λ)ν_R(dλ).

The scalar row alone did not require evenness; this particular equality does. One need not claim evenness is an optimal hypothesis for every possible variant. Both rows now put the SAME weight on the FIXED z frequency. It is exactly ||z||E_(s−γ)², reducing both phase Sobolev entries by γ, while the ON family remains in E_s. No gain is incorrectly assigned to that family and no adjoint row is identified before reflection.

Thus the capsule's C_T=4C1(a)(1+T)^4 K(α,a,γ)c_d²Lζ²CΓ matches source. It is independent of R,I,h and family size, but depends on the actual amplitude, mask shape, d,a,α,γ,T. Strict070 separately yields either h^(2β_H) bound. These are second moments of actual raw forms, not arbitrary-phase covariance monotonicity.

## 5. PROOF074: actual fixed-input L² columns, not a random operator

Source: wave LF500–547. Real Fourier symmetrization and smooth frequency cutoffs give dense real Schwartz phases; Gram–Schmidt preserves this class. For a real ON basis e_k,

    m_Nz=Σ(k≤N)ell(z,e_k)e_k,
    n_Nz=Σ(k≤N)ell(e_k,z)e_k.

Orthogonality in the PHASE space gives each L²(Ω;E_s) tail squared exactly as the sum of its coefficient variances. No covariance cross terms remain because inner products of distinct e_k vanish, not because Gaussian coefficients are independent. The two073 estimates make those sums finite, so the limits are strongly measurable actual random vectors. Linearity and the weaker-input norm bound extend to deterministic bounded maps E_(s−γ)→L²(Ω;E_s).

For fixed Schwartz z,w, project w to w_N in the first identity and normalize its E_s residual. The OUTPUT singleton bound gives E|ell(z,w−w_N)|²≤C_T h^(2−a)Bα||z||E_(s−γ)²||w−w_N||E_s²→0. Project z instead and use the INPUT singleton for the second identity. The resulting pairings hold in L² for fixed Schwartz pairs; no E_s pairing of two arbitrary rough E_(s−γ) inputs is asserted. A countable Schwartz ON test basis and Parseval establish basis independence of the actual random-vector limits. Finite linear combinations are original-W first-chaos variables; their L² limits, including input extensions, have converging characteristic functions/variances and remain jointly centered Gaussian.

This does not supply a common samplewise bounded operator, random Hilbert–Schmidt operator, compact realization or Ctheta/Schatten path. Those require the separate075–093 construction. The prerequisite table correctly excludes those later steps as premises of these four calculations.

## 6. Analytical falsification checks and original model scope

At zero frequency the sine quotient is t and K21=1. Direct integration gives ||1_I||Ha²=2h^(2−a)/[(1−a)(2−a)]. At high equal frequencies cos(rt)² has a constant half. Its squared temporal norm tends to ||1_I||Ha²/4: the oscillatory part tends to zero by the modulated estimate (or the L¹-kernel Riemann–Lebesgue argument), and its mixed term then vanishes by Hilbert Cauchy. An r+ρ-only bound would incorrectly tend to zero.

For original d1 white Γ=cδ, μ=c dξ/(2π), ν_R=cLζ²dξ/(4π²). At ξ=0 the row is2∫〈hλ〉^(a−1)/〈λ〉ν_R(dλ). On1≤|λ|≤1/h, h≤1/2, its integrand is at least2^(a/2)/|λ|. Hence the generic row genuinely has a positive logarithmic lower bound; a uniform replacement for B1 is false. This is not a lower bound or sharpness assertion for every actual phase form.

The finite anisotropic two-dimensional control is also correctly limited: A=|e1><e2| gives ||A*z||²=|z1|² bounded by |z1|²+L^(−2γ)|z2|², while ||Ae2||²=1 requires a constant≥L^(2γ) in the other direction. It explains why the two estimates are separate, not a counterexample to the source's actual wave estimate.

For the admissible d3 directional covariance Γ=cδ₀(dx₁)dx₂dx₃, α=1 and0<a<1, μ=(c/(2π))dξ₁δ₀(dξ₂)δ₀(dξ₃). Its ball mass is≤cr/π with equality for centers on the line, R1=c/2, and physical Γ is nonnegative PD and homogeneous. This checks the translated-measure/no-density application directly, without any claim of an angular density or finite total μ. It is only a normalization/domain check, not a new stochastic moment theorem. Γ0 gives all forms/columns/ν_R zero directly; temporal completion itself remains valid.

No counterexample to an assigned capsule deduction or source069/071/073/074 was found under the exact original assumptions. No correction to the frozen capsule/source is requested. The check does not clear all preceding covariances as full independently reviewed parents, later075–093/path/source/solution steps, native HIGH/Kimi, source pixels/visual/cold, or the full214/240/13 goal. No private model reasoning was read and no model/network/CLI/source/Git/runtime action was taken.
