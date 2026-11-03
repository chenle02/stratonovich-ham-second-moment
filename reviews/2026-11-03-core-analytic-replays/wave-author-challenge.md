# Author challenge of the full061–074 wave-variance reconstruction

Read in full: `stratonovich-full-wave-variance-replay-20261103/worked-replay.md`, SHA256 `10a59a3b8e6ffac4ae4ac57d2ee701567b7da80a26cfde83dba2f43d3991a62c`, and its falsification controls. This is a bounded adversarial author calculation against scientific source8ce, not an independent model review or grade. The frozen replay and source were not edited. No provider, Git, repository, packet or clone action was taken.

## Outcome

I found no counterexample or false numerical upper bound in the stated original covariance/parameter class. The displayed K=N_(α,γ)+(4/3)2^(2−a+α)E_(α,a), C₀=16/(1−a), C₁=4·3^(1−a)C₀, A_T=C₁(1+T)⁴, K_β and C_T=4A_TKC_ν are valid sufficient constants with the dependencies claimed. Below are the independent checks and the scope qualifications that prevent a stronger, unjustified conclusion.

## 1. Falsification controls and indispensable hypotheses

At zero frequency the actual kernel is [−t,−t²;1,t]. In particular K₂₁=1, so ||1_(0,h)K₂₁||²H_a=Z_a h^(2−a), Z_a=2/[(1−a)(2−a)]. The unsquared norm scales as h^(1−a/2); an unsquared estimate of order h^(2−a) is false at small h. The new replay consistently estimates the squared norm. Actual source073 at `integrated_wave_variance.tex:406–410` already displays the squared norm. Thus any historical unsquared supplement wording must be distinguished from the present TeX; this check identifies no new source073 defect.

For a=1/2 the polynomial time-norm coefficients for tʲ, j=0,1,2, are exactly8/3,16/21,64/165. Indeed the double integral is 2Beta(j+1,1−a)h^(2j+2−a)/(2j+2−a). With A₁=2048√3, the squared ratio in the replay's false-unsquared witness at h=2^(−32) is exactly2²⁷/9>1. The witness diagnoses the convention rather than challenging the correctly squared inequality.

Physical Γ≥0 is used essentially in the proof of uniform translated spectral growth: it permits taking the absolute value of the single Gaussian Fourier pairing inside the physical Γ integral. Positive spectral measure plus centered homogeneity alone would not suffice. For example, an even measure on a spectral line with density |r|^(α−1)dr, α>1, is homogeneous of degreeα, but its unit-ball mass centered far out on that line grows as |r|^(α−1). Its inverse Fourier object is outside the stipulated nonnegative Radon physical class. This is an outside-class guard, not a counterexample to the source.

The allowed d3 plane Γ=c dx₁dx₂δ₀(dx₃), α=1, remains inside the class. Its spectral measure is c/(2π) times δ₀(dξ₁)δ₀(dξ₂)dξ₃, whose translated-ball mass is at most cr/π. Its physical Gaussian mass is4πc, yielding the same C_Γ=ec/(2√π) as d1 white noise. No full-dimensional density, angular density or finite spectral mass is needed. The product-mask null-vector examples also check: integrating χχ″ gives −∫(χ′)², so a raw-null marginal can acquire positive variance after physical masking. The proof correctly uses an auxiliary norm comparison, not an assumed bounded mask on the original raw quotient.

## 2. Exact spectral/Fourier and auxiliary constants

With the unitary Fourier convention and Γ=∫e^(iξ·x)μ(dξ), the Gaussian transform gives

    ∫e^(−|ξ−y|²/r²)μ(dξ)
      =[r/(2√π)]ᵈ ∫e^(−r²|x|²/4)e^(−iy·x)Γ(dx).

Homogeneity of the physical Radon pushforward gives r^(α−d), hence the complete factor is r^α. On a radius-r ball the Gaussian is at least e⁻¹. Consequently C_Γ=eM_Γ/(2√π)ᵈ is correct; no oscillatory interchange of two infinite measures is used. The auxiliary density c_d²L∫|k_R(ξ−η)|μ(dξ) has translated-growth constant C_ν=c_d²L²C_Γ because ||k_R||₁=L for every R>0. Real ζ and even μ make this auxiliary measure even; ζ need not supply an original spectral density.

For real spatial tests the physical covariance is B_Γ(f,g)=(2π)ᵈ∫fhat overline(ghat)dμ. This factor is retained in the noise norm. Multiplication of the two wave Fourier factors contributes c_d, so their squared covariance contributes c_d²; (2π)ᵈc_d²=1 cancels exactly. The argument at −λ and subsequent reflection in an even measure are legitimate. There is neither a missing volume factor nor an extra c_d in the final actual-row inequality.

The raw/auxiliary completion is typed correctly: the auxiliary Cauchy sequence maps by contraction to actual original-W evaluations; no injectivity of the original test seminorm is assumed. The compact-support raw admission estimate can depend on R and is used only to establish membership/identify that actual row. The uniform variance constant comes from the separate translated-frequency bound, not from that admission estimate.

## 3. Temporal modulation and continuous zero mode

For c(v)=∫_s^(s+h−v)A(u+v)overline(A(u))du, differentiating the moving upper endpoint gives exactly the replay's boundary term −A(s+h)overline(A(s+h−v)). Thus |c′|≤M²+hMD≤(M+hD)² and c(h)=0. Rescaling supplies the factor2h^(2−a) in the squared temporal norm.

For k=|hω|>1, the small interval contributes at most K_A²k^(a−1)/(1−a). Integration by parts on[1/k,1] gives a lower-boundary contribution K_A²k^(a−1) and derivative contribution at most K_A²k^(a−1)[1+1/(1−a)]. Their sum is ≤4K_A²k^(a−1)/(1−a). Conversion to the bracket costs at most√2 and the two covariance triangles cost2, so the proposed16/(1−a) exceeds the required8√2/(1−a). For k≤1 the needed factor is at most2√2/(1−a), also smaller. No cancellation or differentiability of an indicator is assumed.

The four trig modes have total coefficient absolute sum one. Hilbert Cauchy gives at most half the displayed Q_h bound, so keeping C₀Q_h is conservative. At low r, b_r=t<r>∫₀¹cos(vrt)dv, including b₀=t; at high r its sine coefficient is at most√2. Products therefore cost at most4 after squaring. The time amplitude tʲ, j≤2, obeys (M+hD)²≤(1+T)⁴. Both frequency arguments shift by at most2 after the low-frequency averaging, and <x+e>≥<x>/(1+|e|) costs at most3^(1−a). This verifies every factor in C₁ and A_T. No zero mode is lost and the temporal bound is a norm SQUARED throughout.

## 4. Adversarial check of the explicit069 near/far constant

Let q=max(1,|ξ|), ε=1−2γ. The unit ball plus dyadic shells up to2ᴺ, N=ceil(log₂(5q)), gives exactly C[1+2^αΣ_(j<N)2^(j(α−1))]. The proposed D_α bounds this for all q≥1: use the infinite geometric sum for α<1; for α=1 use N<ln(10q)/ln2 and D₁≥2/ln2; for α>1 use2ᴺ<10q and absorb the added1 in q^(α−1). The inequality <ξ>^(−ε)≤q^(−ε) has the correct direction because ε>0.

In the near region, the two bracket powers are at most one. For α<1, q^(−ε)≤1. For α=1, e^(−εu)(1+u)≤1+1/(eε). For α>1, α−1−ε=α+2γ−2<0. These give exactly N_(α,γ). The logarithm absorbed here is a high-row-frequency logarithm; it is distinct from the small-h logarithm below.

For r=|λ|>4q, |η|≥3r/4, ||η|−|ξ||≥r/2 and |η|+|ξ|≥r/2. Each bracket is at least<hr>/2, so Q_h≤2^(2−a)<hr>^(a−1). The inverse Bessel factor gives4/(3r). On shell(2ʲ,2^(j+1)] its mass is at most C2^((j+1)α); multiplying by2^(−j) produces the required spatial exponent j(α−1) and the coefficient (4/3)2^(2−a+α). Replacing α−1 by a−1 would fail at the allowed higher-α example and is not done here.

Put L=floor(log₂(1/h)), t*=α+a−2<0. The high-shell upper tail is h^(a−1)2^((L+1)t*)/(1−2^t*)≤h^(1−α)/(1−2^t*) because2^(L+1)>1/h and t*<0. For the low shells, use the convergent geometric sum for α<1, L+1≤(1+ln(1/h))/ln2 for α=1, and 2^(α−1)h^(1−α)/(2^(α−1)−1) for α>1. The proposed E_(α,a) follows in all three cases. Since B_α(h)≥1, the independent near and far upper bounds add to the displayed K with no missing factor. No dimension or angular information entered this scalar argument.

For the strict β window, the remaining power gaps are 2−a−2β>0 for α<1 and3−a−α−2β>0 for α>1. At α=1, the same elementary logarithmic maximum with d=2−a−2β gives exactly K_β=K[1+1/(ed)]. These constants may diverge as strict parameters approach endpoints; no endpoint uniformity is claimed or needed.

## 5. Two actual raw Bessel orientations and factor4

The true Sobolev adjoint is G_w=−sin(t|D|)Λw₁/|D|+cos(t|D|)Λ⁻¹w₂. In unitary phase coordinates it gives the explicit kernel [−b_rc_ρ,−b_rb_ρ;c_rc_ρ,c_rb_ρ]/√(<ξ><η>). Each entry therefore has the squared temporal bound A_Th^(2−a)Φ_h.

For the input-varying family, g_j=Σ_i K_ij overline(V_i). Cauchy over the two i values costs2; summing the two j values costs a further2. Thus Σ_j||g_j||²≤4A_Th^(2−a)Φ_h|V|². Hilbert-valued Bessel first, then the Lebesgue change ξ=η+λ and nonnegative Tonelli, gives the069 row directly at ξ. These are finite component sums, not a dimension or phase-family-size factor.

For the output-varying family, f_i=Σ_jK_ijU_j and the conjugated Bessel version give the same factor4. The remaining row is initially ∫Φ_h(η+λ,η)ν_R(dλ), not the row already estimated. Reflection λ↦−λ uses the actual even ν_R, and symmetry of Φ_h then yields ∫Φ_h(η,η−λ)ν_R(dλ). Only now may069 be applied at η. The replay performs both steps explicitly. The scalar069 theorem itself does not require evenness; the second wave application does. No equality of the two random variances is asserted.

The weighted output integral is exactly ||z||²E_(s−γ), because both balanced phase weights decrease byγ. Consequently C_T=4A_TKC_ν and C_(T,β)=4A_TK_βC_ν have the stated uniformities in R, interval position, phase-family size, future noise truncation and Gaussian moment index. Their model/profile/amplitude and strict-exponent dependence is explicit.

## 6. Actual columns and source-premise names

Phase orthogonality, not independence of scalar coefficients, makes the L²(Ω;E) column tails equal sums of expected squares. Finite-family073 bounds those sums, so both maps exist on the original space, extend continuously from Schwartz to E_(s−γ), and retain the original first-chaos coordinate identities. A finite E projection preserves Schwartz phases; the singleton variance estimates justify passage back to the literal raw row. This is a fixed-input L² map, not yet a random operator on all inputs on an uncountable common event.

The adjoint indices also check: under the E_s pairing, the dual of E_r is E_(2s−r), so a gain E_r→E_(r+1) gives adjoint gain E_(2s−r−1)→E_(2s−r). Direct r=s−γ and adjoint r=s+γ−1 are different substitutions, both giving the needed E_(s−γ) input. Individual coefficient constants are not summed.

The names in index-v6 agree with this chain:061 `P:masked-spectral-growth`;062 `P:masked-auxiliary-norm`;063 `L:masked-time-completion`;064 `P:masked-noise-completion`;065 `P:masked-quotient-obstruction`;066 `L:masked-temporal-modulation`;067 `L:masked-trig-products`;068 `L:masked-continuous-wave`;069 `P:frequency-row`;070 `C:frequency-time`;071 `P:actual-wave-form`;072 `L:phase-bessel`;073 `P:wave-two-variances`;074 `P:wave-square-columns`. The replay actually reconstructs these local steps rather than substituting a later path/Young/point conclusion. It consumes the original spectral representation, standard Fourier/Bochner/Hilbert facts and stated raw completion; no later093/095 theorem is used to prove its own variance premises.

## 7. Finite diagnostics and limits of the check

A separate standard-library calculation checked35 near-annulus geometric bounds and102 positive shell sums plus their analytic geometric remainder, covering α=.2,.5,.99,1,1.01,1.5,1.8, admissible a=.1,.5,.9, h=2^(−m) for m=0,1,2,10,30,90, and q from1 to10⁸. All passed; the largest shell-upper/E B ratio was0.9159130826630488. These diagnostics are not a proof for all parameters; section4's inequalities are that proof.

Independent numerical evaluation reproduces K=63.16888131585168 and K_β=249.07714337905713 at α=1,a=1/2,γ=1/4,β=11/16; K=168.22279372426624 at the higher-α tuple; K=40.53265991548223 at the low-α tuple. C_T/L_ζ² equals109386.42740878522 for d1 white amplitudeone and2770.7905748661947 for the d3 plane amplitudeone. The displayed decimal approximations are diagnostics, while exact formulas define the bounds.

No new gap was found in this bounded061–074 reconstruction. It restores the explicit wave-row working that was only a named input in the downstream new driver closure. This author check does not imply any later operator/path tail, growing-radius bound, source/Young/canonical moment construction, sharp constant, whole/image/cold clearance, or project completion.

## Custody

The frozen input SHA256 was independently checked against the requested hash. All28 ACTIVE TeX file lengths/hashes match the retained science8ce bindings, and all14 actual061–074 proof-body hashes match index-v6 under its exact leading/trailing-LF convention. These are byte checks, distinct from the mathematical deductions above. The source-bindings artifact SHA256 is `ed1e9d9289a334f165bfa355a56a21e4f25b6ca91c64d3be210a94540892e678`; falsification.md SHA256 is `aad64479a777334b9be56bcaec0808c68814107a3e76fc76d3ba260923867348`. No Git operation was used. This challenge is UTF-8, LF, final LF.
