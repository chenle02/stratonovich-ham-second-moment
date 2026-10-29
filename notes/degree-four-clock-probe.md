# Degree-four shared-clock probe

Status: the exact reductions and the nine-diagram partial comparison passed
source-bound Opus5.5/HIGH review at d016a34, all eight checks passing. The
full fifteen-term lower comparison and the original sharp target remain open.
Sections 1–6a and the numerical experiments use the admissible test case
d = α = 1, Γ = δ₀, 0 ≤ a < 1, θ = 1. Section 6b uses the original
covariance/dimension class and arbitrary θ>0.
This note concerns auxiliary chain-gap transforms, not physical unequal-time
correlations or a diagonal-horizon moment Laplace transform.

## 1. The fifteen diagrams and their forty-eight cones

For a split m+n=4, label the first chain 0,…,m−1 and the second m,…,3.
Each chain is ordered forward from time/position zero. Each of the three
pair partitions 01·23, 02·13, 03·12 occurs once with Wick coefficient one.
Thus the full Stratonovich degree-four sum has fifteen diagrams, including
both empty-chain orientations, the unequal chains and the self-pairs.

Decompose each two-chain time domain into its labelled global shuffles.
An ordered color string of length four specifies a shuffle; there are
choose(4,m) strings for split m. On each string, pairing the four global
positions gives three partitions. The inverse map reads the color string
and relabels each endpoint in chain order. Consequently the fifteen diagrams
decompose into 3·Σₘ choose(4,m)=48 distinct cones. No extra binomial factor
is attached to a cone. Pair labels must be carried along when shuffling;
fixed unequal Laplace parameters cannot silently be interchanged.

On a cone write τⱼ=r(x₀+⋯+xⱼ), j=0,…,3, where r>0, all xⱼ>0 and Σxⱼ=1.
Write tⱼ=x₀+⋯+xⱼ, and let ℓ be the sum of the last t on every nonempty
chain. Then 1≤ℓ≤2, and the four-time Jacobian is r³ dr dx, where dx is
ordinary three-dimensional simplex measure. For the two forward-oriented
pairs (i,j),(k,l), put δ₁=tⱼ−tᵢ, δ₂=tₗ−tₖ, and
o=max(0,min(tⱼ,tₗ)−max(tᵢ,tₖ)).

## 2. Exact physical spatial factor

The white wave kernel is Gₛ(y)=1{|y|<s}/2. Identify the two endpoints of
each pair in space, giving two free pair positions X,Y. A first vertex of
a chain gives a root constraint |X|<t or |Y|<t. A transition between
different pairs gives |X−Y|<t_new−t_old; a transition within the same pair
gives Gₛ(0)=1/2 and no additional inequality. Let A,B be the minimum root
bounds on X,Y, with an absent bound interpreted as infinity, and C the
minimum transition bound on X−Y, again infinity when absent. The spatial
factor at normalized times is V=area{these constraints}/16. At general
times it is r²V.

If B=∞ the area is 4AC, and if A=∞ it is 4BC. If C=∞ it is 4AB.
The underlying rooted chain graph ensures these expressions have finite
factors. Otherwise put L=min(A,B), H=max(A,B). The area is

    4LC                              if C ≤ H−L,
    4LC − (C−H+L)²                   if H−L < C < H+L,
    4LH                              if C ≥ H+L.

To verify this, intersect the rectangle with the two half-planes
X−Y<C and Y−X<C. Equivalently integrate, for −A<X<A, the length of
[-B,B]∩[X−C,X+C]. In the first case the narrow strip has constant width
across the shorter side. In the middle case subtract the two corner
triangles; simplifying gives the displayed polynomial. In the last case
both half-plane constraints are redundant. This also proves the formulas
with a missing root bound by integrating in the unbounded coordinate.
In every case 0<V≤1/4 since every finite bound is at most one.

Spatial Gaussian regularization gives the same factor in the limit.
Use each pair's first position and its endpoint difference as coordinates,
with Jacobian one. The two difference mollifiers have mass one; the free
first positions both lie in [-r,r] on the wave support, giving the uniform
spatial bound r²/4. Off the constraint boundaries, which are null in the
two free positions for positive gaps, the mollifiers converge to the stated
identified-position integral. The time domination in §5 justifies removing
regularization after integration. No spatial density replacement is involved.

## 3. Exact shared-clock spatial and temporal factors

Use two independent spatial Brownian paths B₀,B₁ and one shared, independent
scalar Brownian clock β. A pair difference has the sign of its forward
global order. Let M be its two-by-eight charge matrix: column (c,h) records
the coefficient of the independent Brownian increment on global gap h of
spatial path c in each pair difference. Explicitly a vertex at global
position j contributes its endpoint sign to columns (c,0),…,(c,j).
At normalized times the covariance of the two pair differences is

    C_B = M diag(x₀,x₁,x₂,x₃,x₀,x₁,x₂,x₃) Mᵀ.

Write d=det C_B. Cauchy–Binet gives the positive polynomial
Σ_{p<q} det(M_p,M_q)² x_{p mod 4} x_{q mod 4}. The two columns at the
distinct right endpoints j,l, on their endpoint paths, have determinant
±1: order the pairs by their right endpoints and the resulting two-column
matrix is triangular with diagonal entries one. Thus d≥xⱼxₗ>0.
The joint spatial δ expectation at time scale r is 1/(2π r√d).

The scalar clock increments have variances rδ₁,rδ₂ and covariance ro≥0.
For a>0, apply the positive real Gamma integral to each analytic power
(rδ+iZ)^(−a), taking the right-half-plane branch. Absolute Fubini at each
strictly positive real part follows by dropping the characteristic factor.
The joint Gaussian characteristic function then gives, at operational
scale r and θ=1,

    T_a(r,x) = Γ(a)^(−2) ∫₀∞∫₀∞ λ^(a−1)ν^(a−1)
      exp[−r(λδ₁+νδ₂)−r(λ²δ₁+ν²δ₂+2λνo)/2] dλ dν.

The printed right side of source (6.2) omits its Laplace damping;that
normalization is not an input here. Every gap transform used in this note
retains its own exponential damping.

This derivation also fixes the product expectation: it is not a product
of separate clock expectations. It is consistent with current-author
equation (6.3), printed p.41; no modulus covariance or printed (6.2)
normalization is used. At a=0 define T₀=1 directly.

Every wave-to-heat gap contributes 1/2; four gaps give 1/16. The candidate
on this ordered operational cone is therefore

    J_g(a) = 1/(32π) ∫ dx d^(−1/2)
             ∫₀∞ r² exp(−rℓ/2) T_a(r,x) dr.

This defines a candidate, not an identity with the actual wave diagram.

## 4. The implemented exact angular representations

The actual wave cone has damping exp(−rℓ), two time covariances
r^(−2a)(δ₁δ₂)^(−a), spatial factor r²V and time Jacobian r³. Hence

    I_g(a) = Γ(6−2a) ∫ V (δ₁δ₂)^(−a) ℓ^(2a−6) dx.                 (W)

For the candidate, put

    c_a = 2^(a/2−1) Γ(a/2)/Γ(a),
    Y₁,Y₂ independent with Yᵢ=√(2 Gᵢ), Gᵢ~Gamma(a/2,rate 1),
    G~Gamma(3−a,rate 1), independent of the Yᵢ,
    S=√δ₁ Y₁+√δ₂ Y₂,     ρ=o/√(δ₁δ₂).

The substitutions λ=Y₁/√(rδ₁), ν=Y₂/√(rδ₂) in the Gamma integral use
∫₀∞ y^(a−1)e^(−y²/2)dy=2^(a/2−1)Γ(a/2). Integrating the remaining
r^(2−a)e^(−rℓ/2) by a normalized Gamma variable yields

    J_g(a) = [c_a² Γ(3−a) 2^(3−a)/(32π)]
      ∫ (δ₁δ₂)^(−a/2) ℓ^(a−3) d^(−1/2)
         E exp[−√(2G/ℓ) S−ρY₁Y₂] dx.                           (H)

All transformed integrands are nonnegative, so Tonelli applies. At a=0
use c₀=1, Y₁=Y₂=0, yielding J_g(0)=∫[1/(2πℓ³√d)] dx. This endpoint
is defined separately, without a Gamma(0) substitution.

A stronger diagnostic fixes λ,ν≥0 before fractional integration. Put
L=λδ₁+νδ₂ and Q=λ²δ₁+ν²δ₂+2λνo. Direct radial integration gives

    I_g[λ,ν] = Γ(6) ∫ V/(ℓ+L)^6 dx,
    J_g[λ,ν] = 1/(16π) ∫ 1/[√d (ℓ/2+L+Q/2)^3] dx.             (F)

The parameters in (F) are attached to the original diagram's pair labels
before shuffling. The fractional diagram is Γ(a)^(−2) times its integral
against λ^(a−1)ν^(a−1)dλdν. A failure of a per-parameter or pointwise
comparison would not by itself refute the fractionally averaged inequality.

## 5. Finiteness and the sampling law

The two pairs have distinct right endpoints j,l. Since δ₁≥xⱼ, δ₂≥xₗ,
V≤1/4 and 1≤ℓ≤2, the integrand of (W) is bounded by
constant·(xⱼxₗ)^(−a), integrable for a<1. This proves the physical time
domination used in §2 as well, after the finite radial Gamma integral.

For (H), the exponential random factor is at most one. By d≥xⱼxₗ,
its integrand is bounded by constant·(xⱼxₗ)^(−(1+a)/2), also integrable.
This independently proves finiteness of the candidate and all Tonelli
passages after the positive Gaussian average.

The script samples x~Dirichlet(η,η,η,η), using four independent unit-rate
Gamma variables normalized by their sum. Relative to dx the density is
Γ(4η)/Γ(η)^4 · ∏xᵢ^(η−1), and the evaluator includes its reciprocal.
Under 0<η<1−a, the squared estimator for (H), including its independent
Y and G draws, is bounded after multiplication by this density by

    constant · (xⱼxₗ)^(−a−η) ∏_{i≠j,l} xᵢ^(1−η).

Every exponent exceeds −1. Thus this sampling law has finite second moment.
For (W) the corresponding endpoint exponents are 1−η−2a>−1 under the
same restriction. For (F), the candidate endpoint exponents are −η and
the actual integrand is bounded; η<1 suffices. These are mathematical
integrability checks, not a statistical confidence theorem for scrambled
Sobol estimates. The reported replicate standard errors are diagnostics.

## 6. Independent static and low-order calibrations

At a=0 integrate each original physical chain gap before space:
∫₀∞e^(−s)Gₛ(z)ds=e^(−|z|)/2. Let A₀,B₀ count roots on the two pair
positions and C₀ count transitions between them. The diagram is

    (1/16)∫∫ exp[−A₀|X|−B₀|Y|−C₀|X−Y|] dX dY
      = (A₀+B₀+C₀)/[4(A₀+B₀)(A₀+C₀)(B₀+C₀)].                 (S)

To verify (S), split the plane into the two orders on the positive quadrant,
their negative reflections and the two opposite-sign quadrants. The three
integrals before reflection are respectively
1/[(A₀+B₀)(A₀+C₀)], 1/[(A₀+B₀)(B₀+C₀)] and
1/[(A₀+C₀)(B₀+C₀)]. Multiplying their sum by 2/16 gives (S).
All denominator sums are positive for these rooted graphs.

The candidate has the same static diagram: introduce independent operational
gap increments and Fourier-transform the two spatial δ constraints, first
at positive spatial Gaussian regularization. All time/Fourier exchanges are
then absolute. Integrate each heat gap: its factor
(1/2)∫e^(−(1+ξ²)u/2)du is the same resolvent 1/(1+ξ²) as the wave gap.
The resulting product of four resolvents is nonnegative; remove the Gaussian
multiplier by monotone convergence in the resulting nonnegative Fourier
integral. The limit on the wave side is the unmollified position integral:
§2 already proves that identification by dominated convergence, including
at a=0. On the Brownian side, each positive pair-mollification width ε gives
joint spatial covariance rC_B+2εI. Its density at zero increases to
1/(2πr√d) as ε decreases to zero. This follows directly from the eigenvalues
of the positive matrix rC_B; the dominating limit is integrable by §5.
Thus monotone (or dominated) convergence identifies the Brownian limit too.
No conclusion about physical-space mollifier monotonicity is used.
The Fourier product is integrable: the
map from four chain positions to four chain increments is invertible,
and the two disjoint pair differences have rank two. Thus two columns of
its two-by-four charge matrix give independent linear momentum forms L₁,L₂.
The product of all four resolvents is at most
1/[(1+L₁²)(1+L₂²)], integrable after this invertible linear change in the
two Fourier variables. This argument does not assert absolute Fourier/time
Fubini for the unsmoothed oscillatory wave kernels. The finite table is in
diagram-table.md. Summing
its fifteen values gives 11/6. This is a GAP-transform sum, not a coefficient
of the diagonal-horizon second moment.

For a>0, the two one-chain orientations are calibrated separately against
the previously derived one-chain degree-four coefficients multiplied by
Γ(7−2a). The pure self-pair (2,2) actual value is Γ(1−a)²/4. The actual
(1,3) pairing 01·23 and its reversed-chain counterpart are Γ(1−a)²/8:
the spatial factor splits into the cross-root factor min(s,t)/2 and the
remaining factor h/2, where h is the middle transition gap; their independent
gap integrals give this product.
No factorization of all other diagrams is presumed.

The independent polygon-clipping audit checks 288 exact rational geometric
cases against the evaluator. A separate Brownian min-time covariance
calculation checks the same 288 determinants against the positive polynomial.
The geometry audit shares the evaluator's root/transition extraction logic;
its independence concerns polygon integration,not that shared graph encoding.
The static hand/table recount and the new original-chain anchors check the
constraint semantics separately. Ninety executed numerical calibrations cover all fifteen static diagrams,
the one-chain positive-a cases and the stated actual factorizations. Their
diagnostic tolerance is stated in audit.json; it is not a certified enclosure.

## 6a. Exact fixed-parameter calibration family

A fixed-parameter diagram admits a closed rational equality anchor whenever
all its positively charged temporal pairs lie within one and the same
chain. Zero-parameter pairs still carry their spatial δ constraints. For
an edge ending at vertex e, put q_e=1+Σλ_p, where the sum is over charged
intra-chain pairs whose interval crosses that chain edge. Every q_e≥1.
The physical exponential time factors then split into exp(−Σq_e s_e).
The shared-clock Gaussian average has the corresponding sum of squared
cut charges, so the heat damping is exp(−Σq_e² u_e/2). There is no clock
charge on the other chain. Consequently the wave and heat gap integrals
have the identical Fourier multiplier 1/(q_e²+ξ_e²) on every edge. Apply
the positive-width Fubini and zero-width limits just proved. This establishes
I[λ,ν]=J[λ,ν] for this family; it is not an equality for arbitrary cross
charges or charges on both chains.

Let A,B be the sums of q_e over root edges into each pair position and C
the sum over edges between different positions. Same-position edges affect
the denominator product but not the spatial exponential. Integrating the
four wave resolvents and using the six-plane-cone calculation gives

    I[λ,ν]=J[λ,ν]
      = (A+B+C)/[4(A+B)(A+C)(B+C) ∏_e q_e].                    (A)

There are 129 such diagram/parameter anchors in the sixteen-point grid.
They are generated directly on the original labelled chains, independently
of the global-cone area and Brownian determinant evaluators. They detect
errors of the individual integrals, not merely errors of their ratio.
The original coarse fixed-lambda run has up to 3.06% actual relative error
and 0.424% shared relative error against these exact values. It is retained
as a coarse diagnostic; a near-unit ratio is not an accuracy certificate.

## 6b. Nine-diagram comparison in the original covariance class

This subsection uses the ORIGINAL nonzero, nonnegative, positive-definite
homogeneous Radon covariance Γ in d=1,2,3, with 0<a<1, α+a<2, and θ>0.
It does not replace that class by the white-space test case. All identities
are first established at a common spatial smoothing width ε>0, choosing
spectral multiplier exp(−ε|ξ|²). Limits are
specified below. The shared clock and forward pair orientation are unchanged. Explicitly,
for four ordered operational vertices s, let U,V be the last times of the
nonempty chains (zero for an empty chain), Δ₁,Δ₂ the lengths of the forward
pair intervals, O their overlap, and H_Γ(s) the spatial Brownian average of
the two Γ factors. Interpret H_Γ as the nonnegative spatial heat-regularized
limit. The fixed-parameter candidate is

    J^Γ_{m,D}(θ;λ,ν) = (1/16) ∫ e^(−θ²(U+V)/2) H_Γ(s)
      exp[−θ(λΔ₁+νΔ₂)−(λ²Δ₁+ν²Δ₂+2λνO)/2] ds.

The domain is the product of the two ordered positive chain time simplices.
This definition permits extended values before finiteness is proved;the nine
terms used here are finite by the identities and bounds below. It specifies
the same shared clock as before,not a new two-chain representation theorem.

Imported already-proved input from the canonical clock-screen proposition:
write R(q)=∫μ(dξ)/(q²+|ξ|²) and

    Q(λ)=∫ μ(dξ)/[(θ²+|ξ|²)((θ+λ)²+|ξ|²)].

The actual cross-pair gap transform and its shared-clock counterpart at fixed
λ≥0 are respectively K(λ)=(2θ+λ)Q(λ)/(2θ) and Q(λ). Here Q(0) is the
continuous zero-parameter value. These are the TWO-POINT identities already
derived in P:clock-copy-obstruction; their scalar partial-fraction and filter
steps also have local Lean checks. Positivity/finiteness and the precise
measure correspondence remain analytic inputs from that proved proposition.
The single self-pair transform is

    S(ν)=R(θ+ν)/θ².

For S, integrate the first wave gap's mass r₁ to obtain 1/θ² and then use
the wave resolvent at θ+ν on the second gap. At positive smoothing the
Fourier/time Fubini is absolute, and the resulting resolvent expression is
positive. Equivalently its heat expression integrates the first operational
gap to 2/θ² and the second to 2R(θ+ν), with prefactor 1/4.

First consider (2,2), pairing 01·23. The actual pure-self diagram is
S(λ)S(ν). In the candidate the spatial averages are independent increment
averages h_Γ(u)h_Γ(v). Its shared clock factor is the product of the two
marginal factors times exp(−λνo), where o is the overlap of the two forward
self intervals. Dropping this last factor bounds the candidate by
S(λ)S(ν). At λν>0 the inequality is strict: the overlap-positive operational
region is open and has positive volume, and all other averaged factors are
strictly positive for Γ≠0. This proves the pure-self comparison.

Next take (1,3), pairing 01·23: its first pair connects the two root vertices,
and its second pair joins the last two vertices of the long chain. Attach
λ to the cross pair and ν to the self pair. Translation invariance permits
independent spatial increments after the long chain's root. Integrating the
middle wave gap gives its mass, and the last self increment is independent
of the roots. Temporal factors also separate. Thus the actual diagram is

    I_A(λ,ν)=K(λ)S(ν).

For the candidate, let the operational root times be u,v and the remaining
long-chain gaps w,z. Its spatial average is h_Γ(u+v)h_Γ(z): the self increment
on (v+w,v+w+z) is independent of B₁(u)−B₂(v). The clock increments are the
forward intervals between u,v and between v+w,v+w+z. Their covariance is
their nonnegative overlap. Dropping exp(−λνo) bounds the clock product by
the product of its marginals. The middle heat gap contributes 2/θ²; the
root integral is 4Q(λ) and the last self integral 2R(θ+ν). Including 1/16,

    J_A(λ,ν) ≤ Q(λ)S(ν)
               = [2θ/(2θ+λ)] I_A(λ,ν).                        (P)

This is strict below I_A whenever λ>0. Swapping chain names proves the
same assertion for (3,1), pairing 03·12, with the cross parameter attached
to that cross pair.

These factorizations for generalized Γ do not multiply two singular
spatial measures pointwise. Work with Γ_ε first. The independent-increment
averages are h_ε(t)=∫e^(−(t/2+ε)|ξ|²)μ(dξ). They increase to h_Γ(t).
R_ε and Q_ε likewise increase to their finite positive spectral limits.
All candidate integrands after clock averaging are nonnegative, so monotone
convergence passes to their limits. On the actual side the factorizations
hold at every positive width; the products of these resolvent limits identify
the existing fixed-order Green–Wick limits. No pointwise monotonicity of
Γ_ε(x) is asserted. To make the actual-side damping limit explicit, at
θ≥1 its exponential test function relative to the finite measure ν_D is
bounded and continuous. For θ<1 rescale all chain times and positions by
1/θ. Homogeneity gives

    I^Γ(θ;λ,ν)=θ^(−(8−2α)) I^Γ(1;λ/θ,ν/θ).

At positive smoothing the width becomes εθ², which tends to zero through
the same admissible joint spatial limit. Thus the θ=1 identification also
implies the one at every θ>0;no unbounded-test-function weak-convergence
claim is needed. The candidate has the same scaling,with operational times
rescaled by 1/θ². The covariance class supplies finite R and Q, and the
accepted fixed-order construction supplies the diagram identification.

Fractionally average λ,ν with positive measure
Γ(a)^(−2)λ^(a−1)ν^(a−1)dλdν. The self integral is finite: near zero its
density is bounded by a constant times ν^(a−1), and at infinity R(θ+ν)
has order ν^(α−2), integrable because α+a<2. The cross integral is finite
by the imported two-point proposition. Tonelli therefore gives

    J_self(a) < I_self(a),
    J_A(a) ≤ J_cross(a) S_a < K_cross(a) S_a = I_A(a),          (P-a)

where S_a=Γ(a)^(−1)∫₀∞ν^(a−1)S(ν)dν is the positive fractional self
integral. The strict cross
comparison is precisely the already-proved two-point result; its locally
Lean-checked deductions need not be re-proved here. In the degree-one case
α=1 it gives the explicit bound J_A(a)≤(2−2^a)I_A(a).

The six one-chain diagrams (three for each empty-chain orientation) are
exact from the fixed-pair computation in current-author §6, pp.38–41,
before the final global symmetrization. Its physical external-horizon factor
is 1/θ, while the operational one is 2/θ²; these cancel the source θ/2
when the physical gap transform is recovered, leaving exactly 1/16.
That source calculation is imported,
not claimed as new here. Together with the pure-self diagram and the two
asymmetric root/self diagrams above, nine of the fifteen terms now satisfy
a shared-clock ≤ actual comparison; the three newly treated mixed terms
are strict for positive a. Strictness at zero width follows from the limiting positive h_Γ on
the overlap-positive region;it is not inferred by taking a limit of strict
inequalities. This partial comparison is included in the scoped eight-check review above. The remaining SIX mixed diagrams are not controlled by it.
In particular, a lower inequality for these nine terms alone does not prove
the comparison of the full fifteen-term sum, its all-order extension, or
the sharp constant.

## 7. Numerical result and the unresolved theorem

The pilot used four independent scrambled replicates of 2^14 points. The
refined run used eight replicates of 2^18 points, η=1/8, a=0,1/8,1/4,1/2,3/4.
It recovered the exact static total 11/6 within its diagnostic error. At the
four positive exponents the total shared/actual ratios were approximately
0.97117, 0.93809, 0.86072, 0.76992. No clipping was used. Per-diagram outputs
and largest-draw fractions are retained. Some near-equality differences are
below numerical resolution and are not claimed strict.

The stronger (F) screen tested sixteen pairs in {0,0.1,1,10}². It found
no mixed-diagram negative difference exceeding eight replicate standard
errors. Ratios slightly above one near expected equalities are retained,
not suppressed. This is survival of a finite test, not a per-parameter proof.

The original coarse fixed-lambda run and a denser run with a different
Dirichlet density are both retained. The denser run uses eight replicates
of2^17points and η=1/2,valid for the fixed-parameter formula (F). The129exact
anchors reduce its maximum actual relative error to0.0456%,but its maximum
shared relative error is1.15%. Thus this change of density improved one
estimator while worsening the other. Neither run certifies near-equalities;
no tolerance was loosened and no value clipped. The positive-a fractional
experiment is a separate sampler with its own90calibrations.

The still-unproved statement is that the full shared-clock degree-four
Stratonovich sum is bounded above by the actual sum for every a∈(0,1).
Neither this finite experiment nor the exact reductions prove it. An
all-degree comparison, its original covariance-class extension, a balanced
external-horizon transfer and the sharp asymptotic constant remain further
obligations. No Skorohod result, source-normalization correction or novelty
claim is made. The canonical 110-page notes are unchanged by this memo.
