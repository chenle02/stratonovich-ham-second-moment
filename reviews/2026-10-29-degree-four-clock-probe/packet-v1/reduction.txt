# Degree-four shared-clock probe

Status: candidate internal reductions and numerical evidence, not a proved
lower comparison. The original fixed-positive-time-exponent sharp target
and its full dimension/covariance scope remain unchanged. This note works
in the admissible test case d = α = 1, Γ = δ₀, with 0 ≤ a < 1 and θ = 1.
It is about auxiliary chain-gap transforms, not physical unequal-time
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
(δ+iZ)^(−a), taking the right-half-plane branch. Absolute Fubini at each
strictly positive real part follows by dropping the characteristic factor.
The joint Gaussian characteristic function then gives, at operational
scale r and θ=1,

    T_a(r,x) = Γ(a)^(−2) ∫₀∞∫₀∞ λ^(a−1)ν^(a−1)
      exp[−r(λδ₁+νδ₂)−r(λ²δ₁+ν²δ₂+2λνo)/2] dλ dν.

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
multiplier by monotone convergence on both sides. It is integrable: the
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
remaining factor r/2; their independent gap integrals give this product.
No factorization of all other diagrams is presumed.

The independent polygon-clipping audit checks 288 exact rational geometric
cases against the evaluator. A separate Brownian min-time covariance
calculation checks the same 288 determinants against the positive polynomial.
Ninety executed numerical calibrations cover all fifteen static diagrams,
the one-chain positive-a cases and the stated actual factorizations. Their
diagnostic tolerance is stated in audit.json; it is not a certified enclosure.

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

The still-unproved statement is that the full shared-clock degree-four
Stratonovich sum is bounded above by the actual sum for every a∈(0,1).
Neither this finite experiment nor the exact reductions prove it. An
all-degree comparison, its original covariance-class extension, a balanced
external-horizon transfer and the sharp asymptotic constant remain further
obligations. No Skorohod result, source-normalization correction or novelty
claim is made. The canonical 110-page notes are unchanged by this memo.
