# Review Result
Category: proof-readability-equivalence
Model: deepseek-v4-pro
Verdict: PASS
Confidence: high

The NEW module is an additive explanatory rewrite of the OLD module. The eight assigned statements are textually unchanged. Every new sentence I checked is either a step recapitulation or a correctly derived detail of a step that was already present. No constant (1/4, 4/3, 2, 1/3), domain, limiting order, or zero-case qualifier is lost or altered. The only caveats are scope caveats (assigned proofs rely on unassigned upstream propositions), not rewrite defects.

## L:constant-phase-free

- Old reading: COMPLETE
- New reading: COMPLETE
- Public reconstruction: COMPLETE
- Original-step coverage:
  1. Injectivity. A nonzero constant has Fourier transform a nonzero multiple of δ0. For u ∈ H^σ, ⟨ξ⟩^σ û ∈ L² and ⟨ξ⟩^σ is bounded above/below on a neighborhood of 0, so û is locally L² there. Test a locally L² f against φ(ξ/ε), φ(0)=1, supp φ ⊂ B₁: |∫f φ(ξ/ε)dξ| ≤ ‖f‖_{L²(B_ε)} ε^{d/2} ‖φ‖₂ → 0, while δ0 yields 1. Hence constants ∉ H^{1/2}, H^{-1/2}. If (e₁+c₁, e₂+c₂)=0 then c₁=-e₁∈H^{1/2}, c₂=-e₂∈H^{-1/2}, contradiction unless c₁=c₂=0; so the interpretation is injective. Continuity into distributions follows by Sobolev duality plus two test integrals; completeness, separability, closedness/properness of iE follow from the Hilbert direct sum E⊕R². (Both OLD LF 37–51 and NEW LF 37–55.)
  2. Cutoff bound. Peetre: ⟨ξ⟩^σ⟨η⟩^{-σ} ≤ 2^{|σ|/2}⟨ξ−η⟩^{|σ|}. In the unitary convention (c_d=(2π)^{-d/2}), the weighted kernel of multiplication by ψ is dominated by convolution with the L¹ function 2^{|σ|/2}c_d|ψ̂(q)|⟨q⟩^{|σ|}; the L¹∗L² bound applies at σ=±1/2. Smooth compact ψ belongs to both Sobolev spaces, so the two constant columns map into E. This proves boundedness of E:constant-phase-cutoff.
  3. Free group and propagation. The finite block of E:constant-phase-free is (c₁,c₂)↦(c₁+tc₂,c₂), giving a group. S_F uses the strong, finite-horizon bound of Lemma L:driver-gain-localization (unassigned input). On Schwartz phases the matrix [[∂ₜG_d, G_d],[ΔG_d, ∂ₜG_d]] equals S(t); its convolution multipliers are cos(t|ξ|), sin(t|ξ|)/|ξ|, −|ξ|sin(t|ξ|), cos(t|ξ|). The masses are 1, t, 0, 1, so constants produce c₁+tc₂, c₂. Each entry is supported in B_|t| (the d=3 Green kernel is a sphere measure inside B_|t|); vanishing of the total initial distribution on an enlarged region forces the evolved total distribution to vanish on the smaller cone, including the Sobolev/constant cancellation.
- Argument preservation: PRESERVED (all three steps retained).
- New explanations: JUSTIFIED. The NEW insertions “Time reversal handles t<0 with the same support bound” (cos is even, sin is odd: the same formula and support bound hold for S(-|t|)) and “The support property concerns the total distribution, not its chosen decomposition” are correct, and directly support the lemma’s cancellation claim.
- Evidence: NEW LF 37–104 vs OLD LF 37–88; equations E:constant-phase-cutoff, E:constant-phase-free; the Peetre constant 2^{|σ|/2} and masses 1,t,0,1 are unchanged and numerically correct.
- Lost steps/qualifiers: none identified within this read. Pre-existing terseness: the injectivity argument relies on the δ0-vs-locally-L² test, which is present and valid.

## P:constant-phase-driver

- Old reading: COMPLETE
- New reading: COMPLETE
- Public reconstruction: COMPLETE
- Original-step coverage:
  1. Localization. Lemma L:driver-gain-localization (unassigned) gives D_χ A_j(I) = A_j(I) = A_j(I)D_χ for each deterministic coefficient; finite sums retain this; the source finite sums of P:source-gaussian-transfer use the same coefficients and correlated Y_ρ(f_j); C^θ limits preserve the identities; a uniformly convergent subsequence (or rational times + continuity) gives E:constant-phase-localization for all t on one event, with a separate event for each fixed ρ.
  2. ψ-independence and column retention. For two cutoffs, (L_ψ−L_ψ′) z ∈ E and χ(ψ−ψ′)=0, since both are 1 on a neighborhood of supp χ; hence D_χ(L_ψ−L_ψ′)=0 and M_E D_χ kills the difference. For z=ie, χψe=χe, so A i = iM_E. The constant columns iM_E(ψ,0), iM_E(0,ψ) are retained; range(i) has zero constant coordinates, hence π_C A = 0.
  3. Bounds and measurability. Bounded composition preserves compactness; E:source-driver-limit transfers to A^ρ→A in every finite L^pC^θ. √p moments give E X^{2n} ≤ C^{2n}(2n)^n; since n! ≥ (n/e)^n, E e^{cX²} = Σ c^n E X^{2n}/n! ≤ Σ(2ecC²)^n < ∞ for 2ecC²<1. A is a bounded deterministic transformation of the W-measurable path.
- Argument preservation: PRESERVED.
- New explanations: JUSTIFIED. The added sentence “The range of i has zero constant coordinates, which also gives π_C A=0” is correct: A=iA_E maps F into iE, and π_C iE={0}.
- Evidence: NEW LF 130–168 vs OLD LF 114–135; E:constant-phase-localization, E:constant-phase-driver.
- Lost steps/qualifiers: none identified. Upstream reliance on L:driver-gain-localization and P:source-gaussian-transfer is stated and its hypotheses match; their internal proofs are unassigned.

## L:constant-source-response

- Old reading: COMPLETE
- New reading: COMPLETE
- Public reconstruction: COMPLETE
- Original-step coverage:
  1. Operator bound. b(r)=mY_ρ(r) has one compact support, L^∞∩L² continuity. For (e,c₁,c₂), the nontrivial output is b(e₁+c₁) in the second slot. Since e₁∈L² and ‖·‖_{H^{-1/2}}≤‖·‖₂, ‖b(e₁+c₁)‖_{H^{-1/2}} ≤ ‖b e₁‖₂+|c₁|‖b‖₂ ≤ (‖b‖∞+‖b‖₂)‖(e,c₁,c₂)‖_F. Hence ‖B_F(b)‖_{B(F,E)} ≤ ‖b‖∞+‖b‖₂.
  2. Statewise integral. The integrand S(-r)B_F(b(r))S_F(r) is strongly continuous on states and uniformly bounded as an operator; increments are bounded by sup_r‖·‖ |t−s|, giving the Lipschitz primitive without a Banach-valued operator derivative.
  3. Finite-propagation replacement. The total initial distributions of z and iL_ψ z agree where ψ=1 (the enlarged ball); L:constant-phase-free gives equal free displacements near supp m for 0≤r≤T; multiplication by b kills the difference; P:source-ordinary-response (unassigned) applied to L_ψ z gives E:constant-source-response. Rational times + continuity give all states/times on one fixed-ρ event.
- Argument preservation: PRESERVED.
- New explanations: JUSTIFIED. The NEW intro “replace each initial state by its localized Sobolev representative near the coefficient support” is a faithful restatement of Step 3.
- Evidence: NEW LF 184–217 vs OLD LF 151–173; E:constant-source-response.
- Lost steps/qualifiers: none identified; the “no density of E in F” qualifier is retained in both.

## P:constant-young-linear

- Old reading: COMPLETE
- New reading: COMPLETE
- Public reconstruction: COMPLETE
- Original-step coverage:
  1. Young remainder. ∫_s^t dD V = D(s,t)V(s)+R with ‖R‖ ≤ C_θ[D]_θ[V]_θ|t−s|^{2θ} (E:constant-young-estimate).
  2. Scaled-norm contraction. I_D(V)(t)=∫_a^t dD V. Using V=V(a)+(V−V(a)), sup‖I_D(V)‖ ≤ [D]_θℓ^θ sup‖V‖ + C_θ[D]_θℓ^{2θ}[V]_θ. The seminorm bound is [I_D(V)]_θ ≤ [D]_θ sup‖V‖ + C_θ[D]_θℓ^θ[V]_θ. Multiply the second by ℓ^θ and add: N_ℓ(I_D(V)) ≤ 2[D]_θℓ^θ sup‖V‖ + 2C_θ[D]_θℓ^{2θ}[V]_θ ≤ c_θ[D]_θℓ^θ N_ℓ(V) with c_θ=2max(1,C_θ) (E:constant-young-local). The NEW sentence “For the supremum estimate … For the seminorm estimate … add” is exactly this computation and is correct.
  3. Contraction. With [D]_θ≤K and c_θKℓ^θ≤1/4, T(V)=V_a+I_D(V) is a contraction of modulus ≤1/4 on the complete affine space. From V=V_a+I_D(V), N_ℓ(V)≤‖V_a‖+N_ℓ(V)/4 gives N_ℓ(V)≤(4/3)‖V_a‖≤2‖V_a‖. The NEW “subtracting two images removes the initial value … Image starts at V_a because the integral vanishes at the left endpoint” statements are correct.
  4. Two-driver comparison. W:=V−V′ satisfies W=W_a+I_D(W)+I_{D−D′}(V′) by bilinearity. Absorbing the first term (coefficient ≤1/4): N_ℓ(W) ≤ (4/3)‖W_a‖+(4/3)c_θδℓ^θN_ℓ(V′) ≤ 2‖W_a‖+2c_θℓ^θδN_ℓ(V′) (E:constant-young-difference). The NEW “Move it to the left … Replacing 4/3 by two” explanation is correct.
  5. Patching. Cover [s,T] by ≤n_{K,T} pieces; E_{j+1}≤2E_j+2^{j+2}c_θℓ^θδB and E_j≤2^jE_0+j2^{j+1}c_θℓ^θδB follow by induction. For evolutions E_0=0, B=1; the piece count is uniform in s,t, proving local Lipschitz in the triangle norm.
  6. Growth. K=1+‖D‖_{C^θ}; ≤C_T(1+‖D‖^{1/θ}) pieces; each multiplies the norm by ≤2, so the product is bounded by an exponential in the piece count, giving E:constant-young-growth.
  7. Flow properties. Uniqueness patches; right multiplication by the preceding evolution gives composition. On a small piece N_ℓ(I_D(V))≤(1/4)(4/3)=1/3, so ‖U_D−I‖∞≤1/3, the Neumann series gives local invertibility, products give global invertibility, and U_D(t,s)=U_D(t,0)U_D(s,0)^{-1} plus continuity of inversion gives joint norm continuity.
- Argument preservation: PRESERVED.
- New explanations: JUSTIFIED. All inserted derivations above check out; constants 1/4, 4/3, 2, 1/3 are used exactly as in OLD and are correct.
- Evidence: NEW LF 249–328 vs OLD LF 205–256; E:constant-young-local, E:constant-young-difference, E:constant-young-growth.
- Lost steps/qualifiers: none identified within this read.

## P:constant-gaussian-flow

- Old reading: COMPLETE
- New reading: COMPLETE
- Public reconstruction: COMPLETE
- Original-step coverage:
  1. Measurability and ranges. Paths A,A^ρ lie in separable closed path spans by the Gaussian construction; bounded composition plus the continuous Young map preserve strong measurability into C(Δ_T;B(F)) (continuous image of a separable space has separable closure). Applying π_C to Young Riemann sums gives π_CU_A=π_C; each increment applied to any state has range in iE, and closedness passes this through sums/limits, giving (U_A−I)F⊂iE.
  2. Convergence in probability. X_ρ=‖A^ρ‖_{C^θ}, X_0=‖A‖_{C^θ}; P:constant-phase-driver gives sup_ρ E e^{c₀X_ρ²}, E e^{c₀X_0²} ≤ H_0. With L_K the Young Lipschitz constant on the radius-K ball, on {X_ρ≤K, X_0≤K} one has ‖U_{A^ρ}−U_A‖∞ ≤ L_K‖A^ρ−A‖_{C^θ}. Hence P(‖U_{A^ρ}−U_A‖∞>ε) ≤ P(X_ρ>K)+P(X_0>K)+P(L_K‖A^ρ−A‖>ε) ≤ 2H_0e^{-c₀K²}+(L_K/ε)^q E‖A^ρ−A‖^q. Fix K (second term vanishes at arbitrary relative widths), then K→∞ gives convergence in probability. The NEW union-bound/Markov explanation is correct.
  3. L^p strengthening. ν=1/θ<2; for r≥1, c>0 there is C_{r,c} with rC_T(1+x)^ν ≤ c x²+C_{r,c} (since (1+x)^ν/x²→0). Using c≤c₀ and E:constant-young-growth gives sup_ρ E‖U_{A^ρ}‖∞^r, E‖U_A‖∞^r < ∞. Hence the 2p moments of V_ρ=‖U_{A^ρ}−U_A‖∞ are uniformly bounded; split E V_ρ^p ≤ ε^p + (E V_ρ^{2p})^{1/2}P(V_ρ>ε)^{1/2} (Cauchy–Schwarz), use convergence in probability, then ε↓0. This is E:constant-flow-limit. The NEW derivations are correct.
  4. Physical flow. L(V)(t,s)=S_F(t)V(t,s)S_F(-s) is bounded linear C(Δ;B(F))→B_∞(Δ;B(F)) with norm ≤C_T². So ‖P_{A^ρ}−P_A‖∞ ≤ C_T²‖U_{A^ρ}−U_A‖∞ and measurability/moments/L^p convergence transfer. The range identity P_A(t,s)−S_F(t−s)=S_F(t)(U_A(t,s)−I)S_F(-s) has range in iE because S_F preserves iE (the NEW “rightmost factor changes the input, leftmost preserves iE” comment is right). Strong state continuity is by splitting into the norm-continuous U difference and two strong free-group differences; J_tJ_{−s}=J_{t−s} gives the constant block; J_t(c₁,c₂)=(c₁+tc₂,c₂) is correct.
- Argument preservation: PRESERVED.
- New explanations: JUSTIFIED. All four Steps mirror the OLD deductions; the added justifications (union bound, moment transfer, range inclusion) are mathematically sound.
- Evidence: NEW LF 359–481 vs OLD LF 287–380; E:constant-flow-limit, E:constant-flow-range, E:constant-physical-flow, E:constant-young-growth.
- Lost steps/qualifiers: none identified. The qualification “no operator-norm continuity of the free group is asserted” is retained.

## L:constant-source-solution

- Old reading: COMPLETE
- New reading: COMPLETE
- Public reconstruction: COMPLETE
- Original-step coverage:
  1. Young-to-ordinary. C(r)=S(-r)B_F(b(r))S_F(r); the primitive is A_E^ρ. Young sums over left endpoints r_j=t_j are Σ_j∫_{t_j}^{t_{j+1}} iC(r)U(r_j,s)v dr; continuity of U and boundedness of C make them converge to the strong integral with U(r,s)v, so the Young equation is the ordinary interaction integral on states. Multiplying by the free groups gives the Duhamel equation; a bounded-coefficient Picard argument with the strongly continuous, bounded free group gives a unique C([0,T];F) solution (no operator-norm derivative of S_F).
  2. Phase Picard. W₀=e₀, W_n(t)=∫₀^t S_F(t−r)iB_F(b(r))W_{n−1}(r)dr. The ordered n-fold time simplex has volume t^n/n! (NEW sentence, correct: ∫_{0<r_1<⋯<r_n<t} dr = t^n/n!); induction gives sup_t‖W_n‖ ≤ C_T^{n+1}B_T^nT^n/n!; the series converges in C([0,T];F); the Duhamel map has norm ≤C_TB_TT, so the sum solves and equals the ordinary phase by uniqueness.
  3. Scalar chains. X₀(t,x)=1, X_n(t)=∫₀^t G_d(t−r)∗(b(r)X_{n−1}(r))dr. These are time-continuous and space-smooth (derivatives fall on the smooth compact factor bX_{n−1}; Green mass t−r and the unit-time measure representation give time continuity). At the induction step the forcing is (0,f_r) with f_r=b(r)X_{n−1}(r), and testing gives ⟨[W_n(t)]₁,φ⟩ = ∫₀^t∫f_r(y)∫G_d(t−r,dz)φ(y+z)dy dr = ⟨X_n,φ⟩; Fubini is justified by ‖φ‖∞‖f_r‖₁(t−r); sphere measures in d=3 are covered. Iteration reproduces X^m_{ρ,n}; the scalar compact-cone factorial bound gives locally uniform convergence to u_ρ^m; the phase series converges in F, hence in distributions, so the displacement limits agree.
- Argument preservation: PRESERVED.
- New explanations: JUSTIFIED. The added simplex-volume sentence is correct and directly justifies the n! denominator.
- Evidence: NEW LF 496–559 vs OLD LF 395–444.
- Lost steps/qualifiers: none identified. The d=3 sphere-measure qualifier and “no operator-norm derivative of S_F” are retained.

## P:constant-raw-average

- Old reading: COMPLETE
- New reading: COMPLETE
- Public reconstruction: COMPLETE
- Original-step coverage:
  1. Functional and measurability. By Sobolev duality ‖O_φ‖ ≤ (‖φ‖²_{H^{-1/2}}+1)^{1/2}. The original path is W-measurable and the Young/deterministic maps are measurable on separable ranges, so Z_m=O_φP_A(t,0)e₀ is W-measurable and independent of the auxiliary J. At fixed ρ, L:constant-source-solution makes the displacement distribution equal u_ρ^m; since ∫φ=1, O_φ pairs with the total displacement, so O_φP_{A^ρ}(t,0)e₀ = C_φ := ∫φ u_ρ^m dx a.s. (no point trace is taken).
  2. Ordinary = Bochner average. P:masked-source-moments gives ‖u_ρ^m(t,x)‖₂≤Q_t uniformly in x and widths. Then E∫|φ u_ρ^m|dx ≤ Q_t‖φ‖₁<∞ (ordinary integral exists a.s.) and E|C_φ|² ≤ ‖φ‖₁∫|φ(x)|E|u_ρ^m(t,x)|²dx ≤ Q_t²‖φ‖₁². For bounded real Ξ, V↦E[ΞV] is continuous on L² and commutes with the Bochner integral; scalar Fubini is justified by ‖Ξ‖∞Q_t‖φ‖₁. Thus E[ΞB_φ]=∫φE[Ξu_ρ^m]dx=E[ΞC_φ]; with Ξ=sign(B_φ−C_φ), B_φ=C_φ a.s.
  3. Original limit and transfer. ‖B_φ−Z_m‖_{L^p} ≤ ‖O_φ‖‖e₀‖‖‖P_{A^ρ}−P_A‖∞‖_{L^p} → 0 for every finite p (E:constant-tested-limit). The L² case supplies the convergence premise of P:masked-canonical-transfer at the same fixed mask, horizon, covariance, and observable; that proposition then gives E|Z_m|²≤‖φ‖₁²E|u(t,0)|²=E|u(t,0)|². Zero covariance gives the free constant solution and equality.
- Argument preservation: PRESERVED.
- New explanations: JUSTIFIED. The Step-2 functional/Bocher argument is the same as OLD and is correct.
- Evidence: NEW LF 585–661 vs OLD LF 470–532; E:constant-raw-average, E:constant-tested-limit, E:constant-original-point-transfer.
- Lost steps/qualifiers: none identified. Same fixed mask/horizon/coupling, arbitrary relative width rates, and the conditional transfer premise are all retained.

## P:constant-compact-base

- Old reading: COMPLETE
- New reading: COMPLETE
- Public reconstruction: COMPLETE
- Original-step coverage:
  1. Deterministic primitive. A_h(t)=∫₀^t iS(-r)B_F(h(r))S_F(r)dr inherits the B_F estimate and strong free-group boundedness exactly as in L:constant-source-response; it is operator-Lipschitz in B(F), is range-iE-valued, and has bound C_T sup_r(‖h(r)‖∞+‖h(r)‖₂).
  2. Shifted driver control. If ‖A_h‖_{C^θ}≤H, |g|≤G, X=‖A‖_{C^θ}, then ‖A_h+gA‖_{C^θ}≤H+GX. From (H+GX)²≤2H²+2G²X² and c′≤c/(2(1+G²)) (so 2c′G²≤c), E e^{c′‖A_h+gA‖²} ≤ e^{2c′H²}E e^{2c′G²X²}<∞. The NEW derivation of this inequality is correct and the deterministic factor is uniform on bounded H,G. The alternative pC(1+H+Gx)^{1/θ}≤cx²+C_{p,H,G,c} (since 1/θ<2) transfers the Young growth estimate to finite moments.
  3. Transfer. Source operator-path convergence, local Young stability and uniform integrability give the same flow convergence; the state-integral and Picard-to-chain arguments apply to h+gmY_ρ with one fixed compact support union. These are individual versions without an uncountable common-parameter event; no Cameron-shift identity is asserted, and only h=0, g=1 enters E:constant-original-point-transfer.
- Argument preservation: PRESERVED.
- New explanations: JUSTIFIED. The two added sentences (“(H+GX)²≤2H²+2G²X² … choice of c′ …”, and the alternative moment transfer) are correct.
- Evidence: NEW LF 679–713 vs OLD LF 550–569.
- Lost steps/qualifiers: none identified. The no-Cameron-shift and no-uncountable-parameter-event qualifiers are retained.

## AUDIT dispositions

No AUDIT comments remain in this module. I found no AUDIT-worthy issue introduced by the rewrite. Any observations below are scope limits or pre-existing terseness, not defects:

1. The assigned proofs invoke unassigned upstream results (L:driver-gain-localization, P:source-gaussian-transfer, P:source-ordinary-response, P:masked-source-moments, P:masked-canonical-transfer, P:actual-operator-driver). I checked that each is applied under its stated hypotheses; their internal proofs are not part of this assignment and were not re-certified.
2. L:constant-phase-free states the masses 1,t,0,1 tersely; the Fourier-at-zero justification is implicit but valid, and the NEW text does not alter it.
3. The phrase “one event” arguments (P:constant-phase-driver, L:constant-source-response) rely on rational times + continuity; this is standard and retained identically in both revisions.

## Findings and limits

Scope: all eight assigned proof pairs were read completely in both OLD and NEW forms; each target deduction was reconstructed from public equations and estimates, with unassigned inputs used only after hypothesis checks. Argument preservation is PRESERVED for all eight; every newly added explanatory assertion examined is JUSTIFIED under the same hypotheses. Constants (1/4, 4/3, 2, 1/3, Peetre 2^{|σ|/2}, c_d=(2π)^{-d/2}, the exponential condition 2ecC²<1), limiting orders, domains, and zero cases are unchanged.

Limits: this review does not certify the unassigned baseline modules’ proofs, Lean quotation correspondence, primary-source PDF/images, rendered pages, or whole-book truth. No prior verdict or worker QA was supplied and none was assumed. No defect introduced by the NEW revision was found; the rewrite is a faithful, more explicitly structured version of the OLD proofs.
