# Complete author working020–023 and S065/S078 roles

2026-11-04, exact af97 source. This working fills the actual OWN details that the new Unit A native public record explicitly did not independently re-derive in limitation4:021's full smoothing/optimality argument and023's anisotropic PD/Fatou passage.020's conditional transfer and022's precise Riesz application are also reconstructed. This is author mathematics and source adjudication, not a native supplement, review vote, source edit or confidence conversion. External author Theorem3.1 may remain a named imported theorem after its exact hypotheses/use are matched; its entire induction is not an OWN reproof obligation.

## 0. Falsification and exact scopes

The local convolution property is STRONGER than H:homog. For α=6/5, the isotropic Riesz kernel has the stated finite d2/d3 spatial bounds, but the anisotropic kernel c|x1|^(−9/10)|x2|^(−3/10), constant in x3 when d3, has the same homogeneous degree and is nonnegative PD/local-Radon, yet fails the property. With a_t=α₀=1/4 these are all within original α+a_t<2. Their difference is not existence/moment finiteness or the target time exponent; the independent051 upper remains a separate route.

At the d2 radial threshold α=3/2 the tangency integral is logarithmically divergent, not finite by an endpoint substitution. By contrast the d3 isotropic sharp constant is finite there: M3=c sqrt2. M2 is only the explicit sufficient bound, not an asserted optimal maximum. The uniform d3 sharp constant is a supremum over positive smoothing widths, approached as they vanish; no positive-width maximizer or equality at a fixed positive width is claimed.

For Γ0 the actual solution is1 and all A_k,k≥1 vanish directly. The formal S065 property requests some M>0; the zero covariance satisfies it with ANY M>0. No division by a zero Riesz amplitude, nonzero field, covariance norm or variance is needed. Nonzero Riesz/counterexample clauses below explicitly use c>0.

## 1. Model and local property, with unambiguous parameters

In020 take d=2 or3,0<a_t<1,1<α<2−a_t and the full original nonnegative even PD homogeneous tempered Radon covariance Γ. Put

    δ=α−1∈(0,1), q=3−α=2−δ>1,
    β=4−α−a_t=3−δ−a_t>2, κ=β/q.

Here δ is an EXPONENT, not a noise width. Let p_ε be centered Gaussian density of covariance εI, γ_ε=p_ε*Γ, G_(h,η)=p_η*G_h, G_(h,0)=G_h. The extra S065/H:spatial-maximum is

    ∃M>0 ∀h>0 ∀z∈Rd ∀ε>0 ∀η≥0:
      0≤∫G_(h,η)(dy)γ_ε(y+z)≤M h^(−δ).             (Hmax)

The SAME M covers every translation and both widths, including separate positive covariance widths on different pairing edges and distinct Green widths. It is formally CONTEXT, logically an ADDITIONAL LOCAL PROPERTY, not the original global S064 given.

Choose

    1/(1−a_t)<r<1/δ, r'=r/(r−1), θ=a_t r'<1,
    u=1−δr/2∈(1/2,1).

The interval is nonempty because δ+a_t<1. Here θ is a temporal-pair exponent for Holder, not the later Young path regularity. Define

    Zθ=2/[(1−θ)(2−θ)],
    D_u=e²(e/u)^(2u),
    K=12M[Gamma_E(1−δr)D_u]^(1/r) Zθ^(1/r').        (1)

u is the source's local a-variable; it is not a_t or a spatial degree. These are finite nonsharp transfer constants, and all inequalities below keep zero errors/empty chains.

## 2.020: descending spatial integration, independent roots and Holder on BOTH labels/time

Fix m+n=2k,k≥1, two separately ordered chains rooted at0 and positive regularization widths. Each spatial covariance edge has the actual sum of its two positive endpoint heat widths; its time factor is bounded by |s_i−s_j|^(−a_t). In d3 keep Green measures smoothed first. All covariance/Green factors are nonnegative, so Tonelli applies even before finiteness is shown.

Label the two chains in blocks, preserving each chain's own chronological labels. Orient each pairing by increasing BLOCK label, not by physical time across chains, with opening/closing sets O_D,C_D. Descend through labels. At label l, all remaining covariance endpoints have labels≤l. If l is a closing vertex, exactly its own pair depends on the current vector increment y_l, as γ_(ε_e)(y_l+z). Other shifts may depend on previously retained increments, but Hmax is uniform in z. It removes that edge with factor M h_l^(−δ). If l is opening, its own pair was already removed and no remaining edge depends on y_l; its Green integral is the MASS h_l. The fact each chain has its own origin is retained in this argument, including an empty chain.

Thus

    S_D(h)≤M^k Π_(i∈O_D)h_i Π_(j∈C_D)h_j^(−δ)
      ≤M^k(2t/k)^k H_D(h), H_D=Π_closing h_j^(−δ).   (2)

The k opening increments sum to at most the two-chain total2t; AM–GM gives the last inequality. This is not the low-α spatial integration lemma, nor a centered-only convolution maximum.

Write T_D(s)=Π_pairs|s_i−s_j|^(−a_t), Ω_mn=[0,t]^m_<×[0,t]^n_<. Apply Holder ON counting measure D times time Lebesgue measure:

    Σ_D∫Ω H_D T_D
       ≤(Σ_D∫Ω H_D^r)^(1/r)(Σ_D∫Ω T_D^(r'))^(1/r'). (3)

Separating the pairing count twice or symmetrizing a single H_D T_D would be incorrect.

Suppose chain1/chain2 have k1/k2 closing increments, k1+k2=k. The gap transformation in each chain has determinant1; include its unused terminal gap with Dirichlet parameter1. A closing increment has parameter1−δr>0, every other increment has parameter1. Iterated beta integration gives

    ∫Ω H_D^r
      =Gamma_E(1−δr)^k t^[(2−δr)k]
       /[Gamma_E(1+m−δr k1)Gamma_E(1+n−δr k2)].     (4)

Empty chains contribute Gamma_E(1)=1. Both arguments are positive and average to1+uk. Cauchy on the positive Gamma integral gives Gamma((x+y)/2)²≤Gamma(x)Gamma(y), so the denominator is≥Gamma(1+uk)². Explicitly

    Gamma_E(1+uk)≥∫_(uk)^(uk+1) x^(uk)e^(−x)dx
       ≥e⁻¹(u/e)^(uk) k^(uk)
       ≥e⁻¹(u/e)^(uk)(k!)^u.

Since k≥1 its square is≥D_u^(−k)(k!)^(2−δr). Let P_k=(2k)!/(2^k k!); summing(4) yields

    Σ_D∫Ω H_D^r
      ≤P_k[Gamma_E(1−δr)D_u]^k t^[(2−δr)k]
           /(k!)^(2−δr).                           (5)

For the temporal factor, the SUM Σ_D T_D^(r') is symmetric in all2k labels: any permutation bijects the pairings. On the full cube each disjoint-pair integral factors into k copies of

    ∫₀ᵗ∫₀ᵗ|s−v|^(−θ)dsdv=Zθ t^(2−θ).

Sorting within the two blocks therefore gives

    Σ_D∫Ω T_D^(r')=P_k[Zθ t^(2−θ)]^k/(m!n!)
       ≤P_k[Zθ t^(2−θ)]^k/(k!)².                   (6)

The final inequality holds also for m=0 or n=0: factorial log-convexity or the product ratio for m=k+j,n=k−j gives m!n!≥(k!)². No individual diagram symmetry is assumed.

Combining(2)/(3)/(5)/(6), P_k≤2^k k! and k^k≥k! cancel the extra pairing/opening factorials exactly. The time exponent is

    1+(2−δr)/r+(2−θ)/r'=3−δ−a_t=β,

and the remaining denominator exponent is

    (2−δr)/r+2/r'=2−δ=q.

Each fixed split is thus≤[4M(Gamma_E(1−δr)D_u)^(1/r)Zθ^(1/r')]^k t^(βk)/(k!)^q. There are2k+1≤3^k splits, yielding A_k(t)≤K^k t^(βk)/(k!)^q with K exactly(1), uniformly in ALL the actual endpoint covariance/Green widths.

## 3.020: width/order passage and full conditional moment

At fixed positive noise widths in d3, remove Green heat smoothing first. Spatial covariance products are bounded continuous, Green measures converge weakly with massesΠh_l, and the finite time simplex integrals are dominated by a constant timesΠh_l. Mixed Green widths give the same limit, hence actual L² Cauchy convergence. Then current OWN006 gives joint fixed-order noise-width L² limits at arbitrary relative rates, under H:homog and not a low-α assumption. Products pass in L¹ through

    ||YZ−Y'Z'||₁≤||Y−Y'||₂||Z||₂+||Y'||₂||Z−Z'||₂.

All split/pairing sums at this fixed order are finite, so their uniform estimate passes to canonical A_k. Empty chain0 is the constant1. In d2 only the noise limit is needed. OWN002 supplies the same canonical nonnegative full mixed series, with all unequal and self-pairings, using the separately constructed fixed orders. For z≥0,q>1,

    Σ(k≥0) z^k/(k!)^q
      =Σ(z^(1/q)^k/k!)^q≤(Σz^(1/q)^k/k!)^q
      =exp(q z^(1/q)).

With A0=1,z=Kt^β, obtain Eu²(t,x)≤exp(qK^(1/q)t^κ), all t>0, all fixed x. The conclusion is CONDITIONAL on Hmax for a general original covariance. The whole independent006/002 proofs remain named OWN inputs; source Theorem3.1 is a legitimate external theorem behind that construction after exact edgewise hypotheses/use matching, not an induction that this bounded author task must reprove.

## 4.021: actual Green measures, scaling and the FULL d3 maximum

The source Green convention is

    G_h^2(dy)=1_(|y|<h)dy/[2πsqrt(h²−|y|²)],
    G_h^3(dy)=σ_h(dy)/(4πh),

with mass h and G_h(hA)=hG1(A). For isotropic γ(x)=c|x|^(−α),c>0, unsmoothed convolution equals c h^(1−α)F_d(z/h), where F_d(w)=∫G1^d(dy)|y+w|^(−α). This is a sphere MEASURE in d3, not a surface-density replacement by volume.

In d3 let ρ=|w|,v=2−α∈(0,1). Rotational invariance and u=cos angle give

    F3(ρ)=½∫_(−1)^1(1+ρ²+2ρu)^(−α/2)du
       =[(1+ρ)^v−|1−ρ|^v]/(2vρ), ρ>0.             (7)

Atρ=0 the limit is1. For0<ρ<1 this is the average of f(s)=(1+s)^(v−1) on[−ρ,ρ]. Here f''>0, so the endpoint chord bounds its integral byρ[f(ρ)+f(−ρ)]. Therefore

    F3'(ρ)=[ρ(f(ρ)+f(−ρ))−∫_(−ρ)^ρ f]/(2ρ²)≥0.

Forρ>1, each distance sqrt(1+ρ²+2ρu) has positive derivative(ρ+u)/distance, so its negative α-power decreases for every u∈[−1,1]. Thus F3 decreases there. Formula(7) is continuous atρ=1 since v>0, as well as at0, and consequently

    sup_w F3(w)=F3(e1)=2^(1−α)/(2−α).               (8)

The unsmoothed maximizing shifts have |z|=h: the singularity touches the sphere, rather than sitting at the center. It is integrable on that sphere exactly because α<2. This gives M3=c2^(1−α)/(2−α) as an unsmoothed bound. It does not claim the maximizing translation of a positive-width convolution is the same.

## 5.021: uniform d2 sufficient bound, including outside centers

For0<R≤1/4 prove G1^2(B(w,R))≤2R^(3/2) for EVERY w∈R². Rotate w=(A,0),A≥0. If A<1/2 the ball lies in |y|<3/4; the Green density is≤2/(πsqrt7), so its mass≤2R²/sqrt7≤2R^(3/2).

If A≥1/2, write y=(x,v). On the ball |v|≤R and x≥A−R≥1/4. Set L=sqrt(1−v²). Where the disk intersects the ball,1−|y|²=(L−x)(L+x), with L+x≥(sqrt15+1)/4>1. Each horizontal slice has length≤2R. The decreasing-distance-to-L singularity has integral≤2sqrt(2R) on any such slice, while |v| ranges over length≤2R. Including1/(2π), the mass is≤(2sqrt2/π)R^(3/2)≤2R^(3/2). This covers disks partly outside the wave disk and centers outside it; empty intersections are harmless.

For α∈(1,3/2), layer cake gives, for every w,

    F2(w)≤4^α+α∫₀^(1/4)R^(−α−1)G1^2(B(−w,R))dR
       ≤4^α+[2α/(3/2−α)]4^(α−3/2).                (9)

G1 has mass1; the term4^α controls distances≥1/4. Thus M2 is c times(9). It is a SUFFICIENT explicit bound, not a claimed optimal value or a claimed maximizing shift. No d2 optimizer computation is needed to establish it. The divergence of the bound as α↑3/2 reflects the actual threshold proved below.

## 6.021: ALL smoothing widths and sharp M3, without a supremum/limit swap

Positivity/Tonelli and Gaussian variance addition give for every h,z,ε>0,η≥0

    ∫G_(h,η)(dy)γ_ε(y+z)
       =∫p_(ε+η)(w)(G_h*γ)(z−w)dw.                (10)

The averaging kernel has MASS1. Equations(8)/(9) therefore preserve the same M_d h^(1−α) bound uniformly over both widths and translations. This also covers each independently summed endpoint covariance width in020. Scaling is consistent with dimensionless smoothing(ε+η)/h²; no density of G3 is inserted.

At each positive width the radial smoothing is globally finite: the positive Gaussian mixture gives

    (p_ε*|·|^(−λ))(x)
      =Gamma_E(λ/2)⁻¹∫₀∞s^(λ/2−1)(1+2εs)^(−j/2)
                     exp[−s|x|²/(1+2εs)]ds
      ≤C_(j,λ) ε^(−λ/2)<∞, 0<λ<j.

The integral is integrable at0 by λ>0 and at∞ by λ<j. Product smoothings below inherit this finite uniform-in-x bound from their one-dimensional factors. Thus the obstruction is the lack of a bound UNIFORM IN widths, never an infinite value at a fixed positive width.

For the lower/optimality passage, here is the complete approximate-identity argument. Let f(y)=|y|^(−λ) in R^j,0<λ<j, and fix x≠0. Choose a small neighborhood U=B(x,ρ),ρ<|x|/2. There f is uniformly continuous and bounded; its Gaussian average differs from f(x) by a local modulus plus f(x) times a Gaussian outside-U probability. On |y|<|x|/2,

    p_ε(x−y)≤(2πε)^(−j/2)exp(−|x|²/(8ε)),

and ∫_(|y|<|x|/2)|y|^(−λ)dy<∞, so this contribution tends0. On the rest outside U the function is bounded by(|x|/2)^(−λ), and its Gaussian mass is≤P(|sqrtε Z|≥ρ)→0. First ε↓0 and thenρ↓0 proves p_ε*f(x)→f(x) at EVERY x≠0. This is pointwise, not uniform through the singularity.

Fix h=1 and z=e1, an UNSMOOTHED maximizing shift from(8), and choose η=0. For G1^3-a.e.y, y+e1≠0; the exception is one sphere point, of surface measure0. Approximate identity and positive Fatou imply

    liminf(ε↓0)∫G1^3(dy)γ_ε(y+e1)
       ≥∫G1^3(dy)c|y+e1|^(−α)=M3.                 (11)

The upper bound(10) is≤M3 for every ε, hence the integrals actually tendM3. For ANY proposed M<M3 choose ε small enough that this positive-width integral exceeds M; this contradicts Hmax at h1. Thus M3 is the SHARP uniform constant over all shifts/h/widths. No smaller constant can work even though ε=0 itself is not an allowed covariance width. If Green widths must also be strictly positive, take η=ε; equation(10) replaces the covariance width by2ε and the SAME Fatou argument applies.

There is no need to choose a maximizer z_ε for each smoothed function, prove its convergence, or interchange sup_z with ε-limit. A fixed unsmoothed maximizer plus a global averaging upper bound suffices. For general h the lower value scales h^(1−α); fixing h1 already proves optimality of a uniform M.

## 7.022: full model admissibility and precise application windows

For c|x|^(−α),0<α<d, local integrability at0 and rapid Schwartz decay at∞ give a nonnegative even homogeneous tempered Radon covariance. Its PD property is OWN work: use

    |x|^(−α)=Gamma_E(α/2)⁻¹∫₀∞s^(α/2−1)e^(−s|x|²)ds.

For complex Schwartz φ put tildeφ(x)=conjugate φ(−x), ψ=φ*tildeφ. Since ∫|x|^(−α)|ψ(x)|dx<∞, Tonelli with |ψ| justifies absolute mixture integrability and complex Fubini. Every Gaussian e^(−s|x|²) has positive Fourier measure, hence nonnegative quadratic integral against ψ. The mixture is therefore PD as a tempered distribution; it is not merely a pointwise formal mixture statement.

In d3 the Hmax discharge is1<α<2; intersect original α+a_t<2 to get1<α<2−a_t. In d2 it is1<α<3/2; intersect to get1<α<min(3/2,2−a_t). In these exact Riesz classes021 supplies Hmax with M_d, so020 applies. Source022 is a corollary on those classes; Hmax is not an unproved additional assumption LEFT OVER after its stated Riesz discharge. It remains a conditional-general-transfer METHOD, not an all-covariance theorem.

## 8.023: radial d2 tangency divergence, including the endpoint

Set h1,z=−e1 and write y=e1+ρ(cosφ,sinφ),0<ρ<1/2,2π/3≤φ≤4π/3. Then

    1−|y|²=−2ρcosφ−ρ²,
    0<ρ−ρ²≤1−|y|²≤2ρ.

The wedge lies inside the disk, polar Jacobian isρ, angular length is2π/3, and |y−e1|=ρ. Thus for3/2≤α<2

    ∫G1^2(dy)c|y−e1|^(−α)
       ≥c/(3sqrt2)∫₀^(1/2)ρ^(1/2−α)dρ=∞.          (12)

At α3/2 the integral is exactly of logarithmic type. This unsmoothed divergence alone is NOT yet a refutation of Hmax, which requires positive covariance widths. The pointwise heat convergence above applies with j2,λ=α<2 for every y≠e1. A single point is G1^2-null, so Fatou at η0 gives

    liminf(ε↓0)∫G1^2(dy)γ_ε(y−e1)=∞.                (13)

Each positive-width convolution is finite, but for every M>0 all sufficiently small widths exceed M at this fixed h,z. Hence no UNIFORM M exists. Taking η=ε instead gives the same result via width sum2ε. The counterexample is compatible with the original temporal threshold whenever0<a_t<2−α; it does not refute the general moment upper route051.

## 9.023: an anisotropic nonnegative PD counterexample for EVERY1<α<2

Choose

    a1=(1+max(2−α,α−1))/2, a2=α−a1.

Both max arguments lie in(0,1), so a1<1 and a1>max(2−α,α−1). Also a1<1<α. Thus0<a1,a2<1 and

    a1+a2/2=(α+a1)/2>1.                             (14)

Define γ(x)=c|x1|^(−a1)|x2|^(−a2),c>0, independent of x3 in d3. It is locally integrable by the two a_j<1 tests, even/nonnegative, and homogeneous degree−α. For a complex Schwartz autocorrelation ψ choose N>1 with |ψ(x)|≤C_N Π_(j=1..d)(1+|x_j|)^(−N). Then∫γ|ψ| is finite by a product of 1D integrals, including the constant third coordinate. This proves temperateness and supplies the absolute integrability needed below; a false global bound away from the origin is NOT used (γ is unbounded along its axes at arbitrarily large distances).

Apply the one-dimensional Gaussian mixture identity separately in coordinates1,2. Tonelli with |ψ| and the preceding finite integral justify their product mixture and complex Fubini. Each integrand exp(−s1x1²−s2x2²), times the constant function1 in x3 when present, has positive Fourier measure (Gaussian factors times δ0 in the unused frequency). It has nonnegative quadratic integral against ψ. Thus γ is genuinely PD in BOTH d2 and d3. It is a valid original covariance for any0<a_t<2−α, not an assumed endpoint factorization or a signed/invalid covariance.

At h1,z=−e1 put u=1−y1∈(0,2) and A(u)=2u−u². In the disk, y2=√A(u) w. Tonelli and the exact Jacobian give

    ∫G1^2(dy)γ(y−e1)
      = c B((1−a2)/2,1/2)/(2π)
         ×∫₀² u^(−a1)(2u−u²)^(−a2/2)du.            (15)

Indeed the inner w integral is∫_(−1)^1|w|^(−a2)(1−w²)^(−1/2)dw=B((1−a2)/2,1/2), finite because a2<1. Near0, A(u)=u(2−u), so the remaining integrand is comparable to u^(−a1−a2/2). It diverges by(14); the other endpoint is integrable since a2/2<1. This identifies the precise tangential obstruction, not merely a pointwise infinite axis value.

Project the unit sphere measure G1^3 onto(y1,y2). Each graph y3=±sqrt(1−|y_perp|²) has surface Jacobian(1−|y_perp|²)^(−1/2). The two graphs and division by4π give exactly G1^2, with the equator surface-null. Since γ ignores x3, the d3 convolution equals the d2 integral(15) and diverges. No volume density is assigned to G3.

Finally the positive-width statement needs its OWN approximation argument. Gaussian factorization gives exactly

    (p_ε^d*γ)(x)
       =c Π_(j=1,2)(p_ε^1*|·|^(−a_j))(x_j),        (16)

and the third heat coordinate integrates to1. Each factor is finite and converges at x_j≠0 by the proved1D approximate-identity lemma. Thus convergence to γ holds away from its singular coordinate hyperplanes. Their shifted preimages under y↦y−e1 have G1^2 measure0; in d3 use the exact projection to G1^2 to obtain the same null statement. Fatou therefore gives infinite lower limit of the smoothed convolution in BOTH dimensions at this fixed h,z. For two strictly positive widths takeη=ε and use(10)/(16). For every proposed M>0 some positive widths—and in fact all sufficiently small equal widths—violate Hmax. This is the required failure with legitimate smooth positive covariance widths, not an inference from ε=0 alone.

## 10. S065/S078 scientific roles and native-depth boundary

S065 is not an OWN theorem or the original global given.020 ASSUMES the property;021 DISCHARGES it for the stated Riesz classes;022 APPLIES that discharge;023 REFUTES a proposed all-model extension via admissible counterexamples. The property/refutation roles are different from accepting a hypothesis as true inside its own counterexample. S078 is a CONTEXT remark with genuine scientific conditions, not an invented additional proof.

Under Hmax,020 and Cauchy–Schwarz give Eu≤exp[qK^(1/q)t^κ/2]. If the intended first-moment lower bound liminf t^(−κ)logEu≥L_* holds with its qualified constant, then2L_*≤qK^(1/q). This is conditional on that source normalization/first lower bound; no actualp1/S1pos/Chen constant is forced. M3 is SHARP only for the uniform SPATIAL convolution property; the moment K in(1) and M2 remain nonsharp/sufficient. No sharp moment constant is identified.

[held back: collaborators' unpublished work]

Native publicLF191 explicitly says the full021 optimality and023 PD/Fatou steps were accepted as correctly constructed rather than independently re-derived. The displayed endpoint/divergence signatures atLF116 do not fill those OWN deductions. Conversely this is a review-depth limitation, not a manuscript gap: the source's fixed-shift/Fatou method is sufficient and the calculations above complete it under its actual assumptions. The native finite/algebra/acyclic confidence cannot be promoted to fullA mathematical reconstruction by this author work. No native rewrite, supplement/call, confidence upgrade or whole214/240/13 clearance follows.
