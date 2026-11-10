# Author challenge: fixed-order spatial and joint noise foundation

Examined `stratonovich-fixed-order-foundation-replay-20261103/fullreplay.md`, SHA256 `f8c0fb9d68d0a4c1153f94a0ea4a929c423c914a15c728e95f89ee7f104ebb06`, against exact scientific source `8ce03ae09cca984b32aaddf3da0a6ded07f47ebc`, proofs004/005/006/214. The main source SHA256 is `364753242f9d02e57036af586ab8e777b184d897862750d3170d79f028067914`; its working bytes matched `git show` at that commit. This is an adversarial author-side check, not an independent model-family review, grade or adoption decision. No frozen/source/provider/Git action was taken.

No actual counterexample or mathematical defect was established in the assigned foundation chain. The justified closures and the precise imported boundary follow.

## 1. Brownian pair elimination and the factorial test

The elimination is valid because the largest REMAINING observation is later than every other remaining observation. Conditional on those others, the increment from the previous remaining time is independent of them. Taking the UNIFORM heat bound removes dependence on both endpoints of the selected pair. Only then are both endpoints removed. The expectation of the remaining factors is their ordinary Brownian marginal. There is no continued conditioning on a deleted future observation and hence no hidden Brownian-bridge variance.

Each chosen largest endpoint is distinct. Its gap to the preceding remaining observation is at least its own original adjacent gap, so its negative power can be bounded by that adjacent gap's negative power. Exactly j distinct gaps receive exponent−c, c=α/2<1. Including the first and final slack gaps gives total Dirichlet parameter(2−c)j+1. Thus the simplex integral is Γ_E(1−c)^j T^((2−c)j)/Γ_E((2−c)j+1). Multiplication by all(2j)! labeled chronological orderings is correct; no pairing factorial is added or removed.

I recomputed the white j2 check. The sequential, crossing and nested covariance determinants are bd,bc+bd+cd,c(b+d). The ordered integrals at T=1 are1/12,1/36,1/24. For crossing, radial integration contributes1/6 and the shape integral isπ/3, giving1/36 after the density factor1/(2π). The stated substitution reduces that shape integral to−π/3+(8/3)∫_0^(π/2)(1+3sin²θ)^(−1)dθ=π/3. Each matching type occurs8 times, so the exact moment is8(1/12+1/36+1/24)=11/9. The proposed uniform Brownian bound is24·(1/2)/6=2. These Fraction values were recalculated locally. Therefore this requested falsification does not refute the bound.

## 2. Spatial positive Laplace measure and its loose fixed-order bound

At positive vertex widths, every edge has a finite Gaussian-weighted spectral measure. Expanding the finitely many covariance factors and using damped positive Green masses justifies absolute Fourier/Laplace Fubini. Only AFTER the wave Laplace transform is the integrand a nonnegative product of resolvents. Width monotonicity is asserted there, not for γ_b(x) pointwise.

The wave-to-Brownian identity has the correct normalization: (1/2)∫_0^∞exp(−q²u/2)exp(−u|ξ|²/2)du=(q²+|ξ|²)^(−1). For2k edges this gives2^(−2k). Each inserted Brownian-horizon integral is2, so the second factor is1/4, including an empty chain. Enlarging ordered Brownian domains to cubes is an inequality with no shuffle factorial. Spectral Cauchy–Schwarz bounds the cross occupation by the two self occupations; physical nonnegativity supplies its sign. Independence is used only for the two auxiliary Brownian paths after this bound.

The resulting U_k is finite at fixed k. In white amplitudeone its bracket constant is2, so U1=25/4 and U2=11025/16. These large numbers are valid loose bounds; they are not claimed sharp, homogeneous in amplitude, uniform in k, or usable as an all-order estimate. The actual diagrams still have exactly k covariance factors. The separate zero-covariance case prevents the harmless constant term in this upper bound from being misread as nonzero diagram mass.

## 3. Compactification, uniqueness and all relevant faces

The compact-cube argument includes the mass moment L_D(0), not just positive integer moments. Bernstein polynomials with the explicit variance bound establish uniform polynomial density and uniqueness of the compact cluster measure. General real λ transforms already converge by domination under the integrable F_0; consequently testing ∏y_l^t and sending t↓0 proves that every infinity face y_l=0 is null. Continuity at λ=0 is the essential no-loss step. Closed neighborhoods and portmanteau then control pullback tails. This does give finite-measure weak convergence in the original nonnegative gap variables, not merely vague convergence of a possibly mass-losing family.

Coordinate-zero faces r_l=0 are handled by a DIFFERENT transform limit: send only λ_l→∞. Its resolvent factor tends tozero pointwise and F_0 dominates. On the finite-measure side the same limit is exactly the mass of r_l=0. This proof does not rely on pointwise vanishing of a limiting spatial density. In particular, white empty-plus-two J_self=c_w r1/2 can remain nonzero as r2↓0 while that face has zero measure; the replay explicitly permits this.

The undamped ρ_D, not ν_D, is homogeneous. The factors are c^(2k) from Green measures, c^(2k) from gap Jacobians and c^(−αk) from covariances. Thus its degree is(4−α)k. Vague convergence on compact tests is enough to pass this identity to ρ_D. A compact part of a positive horizon face ℓ_i=T>0 would have disjoint dilates of uniformly positive mass in one compact set, contradicting local finiteness. For an empty chain ℓ_empty=0 identically: the positive-T face isempty, whereas its zero-level face carries the whole measure. The replay and exact source statement restrict the horizon-face claim to T>0, so this potential counterexample is not a defect.

The finite-horizon region is bounded even if one chain isempty because all actual coordinates belong to the other chain. Its boundary consists of the already excluded coordinate-zero and positive horizon faces. The exponential undamping factor is bounded there. The extra cutoff argument for a φ continuous only inside the positive orthant supplies the necessary extension step without assuming continuity across a face.

## 4. Independent-origin estimate214 and coefficientone

At a fixed temporal cap and finite spatial edge measure, the explicit feature map has norm squared m_L and inner product κ_L(t−s)γ_e(x−y). Its Bochner integral against L¹ tests is legitimate, and Hilbert Cauchy–Schwarz gives constantone. Translation invariance applies to each SELF pairing by translating both variables over the full time line. Applying it separately to the two different translates leaves their origins distinct in the cross pairing. Thus no positivity of an independently shifted cross kernel, shared-origin assumption or origin-dependent coefficient enters.

Increasing bounded test truncations and temporal caps is legitimate because the tests and physical kernels are nonnegative. It also covers zero self norms without division. The spatial measure is kept finite and smoothed throughout this local proof; no unregularized distribution is removed inside214.

The control γ=1,κ=e^(−|t|), tests1_(0,1), origins0 and2 gives self norm squared2/e and cross value(e−1)²/e³, as claimed. This is a test of214's finite-covariance hypotheses, not an assertion that constant spatial covariance belongs to the original α>0 model. Repeating the same spatial x in both Green factors would leave a free infinite y-integral; the actual norm uses G(s,x)G(t,y). The local proof therefore supplies the needed final source Case2 inequality with coefficientone while explicitly avoiding the printed offset-dropping equality and the repeated-variable typo.

## 5. Damped norms and the marked-edge budget

The N1 beta integral is exact: radial spectral integration gives R_α(θ+λ)^(α−2), and integration in λ with weightλ^(a−1)/Γ_E(a) yields θ^(α+a−2)R_αΓ_E(2−α−a)/Γ_E(2−α). Its finiteness uses a>0 and α+a<2, with no angular density assumption.

I recomputed the independent-variable time integrals: I0=Γ_E(1−a)θ^(a−2), and Ist=(2−a)Γ_E(1−a)θ^(a−4)/2. The low/high frequency split then gives exactly the stated N2(1)² upper bound. The full N2 scaling is θ^(α+a−4), independent of the nonhomogeneous low/high upper bound. Each time quadratic form at a fixed frequency is nonnegative by the positive Laplace mixture. It is therefore valid to remove Gaussian spatial/Green multipliers only AFTER that time integration. This avoids the false pointwise monotonicity argument for oscillatory wave transforms.

The first tail A_M is the exact positive N1 tail. The second B_M² tends tozero by the displayed absolute majorant and is nonnegative by the tail quadratic form. The scalar upper tail Bbar_M² is consistent: with p=1+λ the time integrals are1/p and(1/p+1/p²)/2. At M=0 its two terms recover(2−a)Γ_E(1−a)/2 plus the high-frequency contribution. No missing square or Gamma factor was found.

Source Theorem3.1 explicitly assigns each covariance edge once to a first norm or twice to second norms. Since the mass norms at θ=1 areone, H=max(1,2A,B²) bounds each unmarked edge. The marked possibilities are2A_M H^(k−1) and B_M²H^(k−1), not B_M H^(k−1). The sum of k marked-edge errors and the independent undamping loss therefore give

    k exp(T1+T2) H^(k−1)(2A_(1/η)+B_(1/η)²).

This constant can depend on fixed order, horizons and the actual covariance. It is uniform in all vertex spatial widths, temporary temporal caps and Green widths. A pairing count is not needed for a single diagram; it is only a finite multiplicity when stochastic moments are summed.

The original white check is exact: A= c_wΓ_E(1−a)/2, B²=c_wΓ_E(1−a)/4. With a=1/2,M=1 the marked tails are A_M=c_w sqrtπ/4 and B_M²=c_w sqrtπ/8. The empty-plus-two diagram equals A_M; the cross1+1 diagram equals B_M². Thus the source's factor2 and the marked second-norm square are retained correctly.

## 6. Joint noise limit and actual common coupling

At fixed η>0 the temporal multiplier is bounded continuous, so the spatial measure limit applies. Positivity and the uniform marked remainder give0≤b_D−b_D(η)≤E(η). For arbitrary smaller temporal vertex widths, both F_(ε,δ,D)−F_(ε,η,D) and b_D−b_D(η) lie in[0,E(η)]. Their difference consequently has absolute value at most E(η). This verifies the replay's one-E remainder in(7.3); it is not a missing factor2. Choosing η first, then the spatial widths, while only requiring every temporal width<η, proves a joint arbitrary-rate limit.

At positive vertex noise widths the direct terminal Green-measure integrals exist as Bochner L² integrals by Gaussian Hölder and the exact chain mass T^(2n)/(2n)!. Green-heat smoothing is removed at these fixed noise widths using bounded continuous Wick covariance products and the SAME square/cross moment limits. No sample bound at heat tails or sphere density is used. Only then are noise widths removed.

The same-family covariance is essential and is retained: spatial widths add and temporal prefixes intersect through the maximum. The feature-space realization is fixed once and retains the given W literally on its raw test image. Mixed moments of two different vertex-width vectors use that same joint family. After the two terminal reversals, both diagonal moments and the cross moment have the same finite diagram limits, so their L² difference tends to Q_n+Q_n−2Q_n=0. Independent equal-law sources would fail this argument; the replay does not use them.

The precise same-W statement checked here is convergence on one fixed retaining probability space with the original W unchanged. It does not assert that each positive-width cutoff field is a function of W alone, nor independence from every conceivable alternative extension. The identification with S_n(g_n) is through the stated canonical regularization definition and its ordered/common-width restriction. No SPDE pathwise/PDE uniqueness theorem or all-order series is needed. No stronger sigma(W)-measurability statement for a whole unregularized solution family was used in this challenge.

## 7. Named input boundary and original scope

The imported universal input is held author-version Theorem3.1,(3.6),pp14–15, with finite positive edge spectral measures having nonnegative physical inverse transforms, positive temporal Laplace domains, nonnegative relative-gap functions and finite mass/first/second norms. The replay independently verifies the corrected independent-variable/independent-origin Cauchy–Schwarz input214. Other source induction/first-norm properties remain named imports; this challenge is not an independent reproof of the entire universal theorem. Its edge-assignment multiplicities were checked directly in the held statement.

Other inputs are ordinary Gaussian/Brownian independent-increment identities, Fourier uniqueness for finite positive measures, standard finite-measure weak convergence, and Hilbert/Bochner completeness. The spatial bound005 is obtained before the universal pairing theorem and is independent of it. The later temporal construction uses005 plus004/214 and that explicitly imported inequality. There is no dependency on source Theorem4.1, Lemma4.4, Section5 series identification, the independent sharp upper, or an intrinsic constant.

The proofs use only radial mass homogeneity of μ; singular angular measures are permitted. They retain d1white, d3sphere Green measures and singular invariant-direction covariances such as c dx1dx2δ0(dx3). Actual covariance amplitude is unchanged. Γ=0 and total orderzero are direct separate cases, so no H^(−1) marked expression or division by a zero covariance parameter is invoked.

The tested foundation joins close under these exact named inputs. This finding certifies neither those imported theorem proofs nor any all-order/asymptotic/whole-paper claim. It supplies no cross-family review, source-image or cold-reading credit. The frozen replay and source remained unchanged.

Exact current targets:004 `L:damped-homogeneous-norms`, statement586–612/proof614–674;005 `L:spatial-wick-measures`,941–957/959–1101;006 `L:joint-fixed-order`,1103–1112/1114–1198;214 `L:translated-covariance-CS`,708–719/721–802, all in `notes/notes_stratonovich_ham_second_moment.tex` at the source hash stated above.
