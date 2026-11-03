# Fixed physical masks, ordinary source moments and canonical transfer

This author mathematical reconstruction concerns PROOF101 `L:masked-chain-comparison`, PROOF102 `P:masked-source-moments` and PROOF103 `P:masked-canonical-transfer` at scientific source `8ce03ae09cca984b32aaddf3da0a6ded07f47ebc`. Its calculations and finite controls are claims for independent inspection. The application to110 is checked after its masked-average convergence premise is constructed independently.

## 1. Original model, source and named input contracts

Retain `H:homog`: d∈{1,2,3}, 0<a=α0<1, α+a<2, and the original nonnegative even positive-definite tempered Radon spatial covariance Γ, with 0<α<d or α=d=1. Preserve its amplitude, the massless wave with coefficient Δ, data(1,0) and the given real raw noise W. The positive Green measure G_d(r,dz) has mass r and support in the radius-r ball; in d3 it is the sphere measure, not an ordinary spatial density. At r>0,

    G_d(r,·)=r (D_r)_#P_d,      D_r(ω)=rω,      P_d=G_d(1,·),

where P_d is a probability measure supported in the closed unit ball. Set G_d(0)=0. This is the source wave normalization, not a heat semigroup normalization.

Fix positive noise widths ρ=(ε,η). The actual pointfield Y_ρ is supplied by `P:source-canonical-convergence` (098) on the retaining extension; its raw restriction remains the original W. At this fixed ρ, `L:source-pointfield-regularity` (099) gives a jointly measurable version continuous in time and smooth in space on every compact rectangle, on one event for this ρ. No simultaneous path event for all uncountably many source widths is assumed.

Its exact joint source covariance is

    Cov(Y_(ε,η)(s,z),Y_(ε',η')(r,w))
       =K_max(η,η')(s−r) Γ_(ε+ε')(z−w),
    Γ_e=p_e*Γ,
    K_η(h)=Γ_E(a)^(−1)∫_0^(1/η) e^(−λ|h|)λ^(a−1)dλ.         (1.1)

For a single ρ, put C_ρ=K_η Γ_(2ε). Positive physical kernels give C_ρ≥0 pointwise. Heat-tempered integrability gives Γ_(2ε)(0)<∞, while K_η(0)=η^(−a)/(aΓ_E(a))<∞. Gaussian Cauchy–Schwarz, or the even positive spectral representation, gives

    0≤C_ρ(s,z;r,w)≤c_ρ:=K_η(0)Γ_(2ε)(0)<∞.                 (1.2)

This bound is for fixed ρ and need not remain bounded as widths vanish. Uniformity in widths below will instead come from the named fixed-order input008.

Fix a deterministic real m∈C_c∞(R^d) with 0≤m≤1. The coefficient is b_ρ(s,z)=m(z)Y_ρ(s,z), with m multiplying the physical field after noise regularization. It is not a filter inserted inside p_ε*Γ, a covariance mask before smoothing, or an operator commuting through a wave group. The unmasked coefficient is Y_ρ. Both use order-zero displacement1.

`L:joint-fixed-order` (006) constructs all canonical two-chain diagram limits, including unequal/empty chains, jointly at arbitrary positive vertexwise spatial and temporal width rates; Green smoothing is removed first at fixed noise widths. It also constructs canonical fixed-order X_n on W. `L:vertex-crude` (008) provides constants C,θ0 independent of all noise widths and spatial terminal points such that

    ||Y_n^(vertex widths)(t,x)||₂≤q_n(t),
    q_n(t)=exp(θ0t) C^(n/2)t^n/sqrt(n!)  (n≥1),
    q_0(t)=exp(θ0t)≥1,
    Σ_(n≥0) sqrt(n+1) q_n(T)<∞,         fixed finite T.        (1.3)

The same bound holds for canonical X_n. `P:mixed` (002) identifies their canonical mixed-order sums, with all self-pairings and both chains' own initial roots, and the convergent canonical second-moment series. These are named proved local inputs; their actual width/order/normalization contracts are what this reconstruction consumes. No Skorohod orthogonality is available.

## 2. Positive terminal-chain measure and its exact mass

For n≥1 use 0<s1<⋯<sn<t, with s_(n+1)=t. Write r_j=s_(j+1)−s_j and integrate independent ω_j with law P_d. Starting from z_(n+1)=x, recover

    z_j=z_(j+1)−r_jω_j
       =x−Σ_(h=j)^n r_hω_h.

Define the chain measure ν_n^(t,x) by pushing forward

    1_(0<s1<⋯<sn<t) (∏_(j=1)^n r_j) ds1⋯dsn
                    P_d(dω1)⋯P_d(dωn).                    (2.1)

This is a positive finite Borel measure: positions are continuous functions of the displayed parameters. It uses G_d measures even on spheres. Define ν_0 to be the one-point empty-chain measure of mass1. The mass f_n(t) is independent of x. Integrating the latest vertex time s_n=r first leaves the earlier terminal chain with horizon r and gives

    f_0(t)=1,
    f_n(t)=∫_0^t (t−r)f_(n−1)(r)dr.

Induction and elementary beta integration yield

    f_n(t)=t^(2n)/(2n)!,                                    (2.2)

because ∫_0^t(t−r)r^(2n−2)dr=t^(2n)/((2n−1)(2n)). In particular the first masses are1,t²/2,t⁴/24,t⁶/720. There is no extra time-simplex factorial or chain shuffle; those order constraints are already part of ν_n.

All chain vertices lie in the compact causal cone of(t,x), since |z_j−x|≤t−s_j. For unmasked and masked terms define formally

    F_n=∏_(j=1)^n Y_ρ(s_j,z_j),
    F_n^m=(∏_(j=1)^n m(z_j))F_n,
    X_(ρ,n)^(m)(t,x)=∫F_n^(m)dν_n^(t,x).                    (2.3)

The next section makes these actual L² integrals before using Wick's formula.

## 3. Gaussian products, strong measurability and stochastic Fubini

For n≥1, Hölder with n factors and the scalar Gaussian moment formula give the uniform vertex bound

    E∏_(j=1)^n |Y_ρ(s_j,z_j)|²
       ≤∏_(j=1)^n(E|Y_ρ(s_j,z_j)|^(2n))^(1/n)
       ≤(2n−1)!! c_ρ^n.                                   (3.1)

No independence of vertex values is assumed. Masks only decrease absolute products. Thus every integrand in(2.3) is L², with norm at most sqrt((2n−1)!!) c_ρ^(n/2), uniformly over all vertices.

The covariance is continuous, so source increments converge in L² as their spacetime points converge. A centered Gaussian increment's L^(2n) norm is its standard deviation times the fixed scalar Gaussian constant. For products, telescope one factor at a time and use Hölder with all n factors at exponent2n:

    ||∏Y_j−∏Y'_j||₂
       ≤Σ_j ||Y_j−Y'_j||_(2n)
                  ∏_(i≠j)max(||Y_i||_(2n),||Y'_i||_(2n)).    (3.2)

Consequently the product map is continuous into L² on the vertex parameter space. The continuous mask factors preserve this property. That parameter space is separable metric; its continuous L² image has separable closure. This proves strong measurability without assuming the ambient L²(Ω) is separable. Formula(3.1) and the finite mass(2.2) give integrability of its L² norm, hence the Bochner L² integrals(2.3) exist. Their order-zero terms are1.

For two chains, multiplication is a continuous bilinear map L²×L²→L¹. More concretely, for their integrands F,G,

    ∫∫E|FG| dν_n dν_k
       ≤(∫||F||₂dν_n)(∫||G||₂dν_k)<∞.                     (3.3)

Simple-function approximation of the Bochner integrals, or scalar stochastic Fubini justified by(3.3), therefore gives

    E[X_(ρ,n)^(m)(t,x) X_(ρ,k)^(m)(t,y)]
       =∫ E[F_n^(m)F_k^(m)] d(ν_n^(t,x)⊗ν_k^(t,y)).         (3.4)

This precedes the moment comparison; Fubini is not inferred from a merely formal Wick expansion. Empty-chain integrals are included as constants.

## 4. Green heat is removed first: actual L² identification

At the fixed positive ρ, convolve any Green edge G_d(r) with a positive heat approximate identity p_τ. Its mass stays r, but its support need not remain compact. Nevertheless (3.1) is uniform over all spatial vertices, so the heat-smoothed terminal integrals are still Bochner L² integrals with the same finite chain masses. No samplewise estimate on Y_ρ outside a compact set is needed to define them.

Fix the time vectors in a square or cross moment of two terminal chains. As every positive Green width tends to zero, each heat-smoothed edge measure converges weakly to G_d(r), preserving its finite mass. Products of these measures converge weakly, and the affine reconstruction of vertex positions preserves convergence. Every Wick diagram integrand is a bounded continuous spatial function: it is a finite product of C_ρ factors, and, in the masked case, continuous factors m at every vertex. Its absolute value is at most c_ρ^l when there are2l total vertices. Thus the spatial integral of every diagram converges.

After spatial integration a common bound is c_ρ^l times the product of Green edge masses; summing the finitely many pairings adds only the finite factor(2l−1)!!. Its time integral is bounded by the product of chain masses(2.2). Dominated convergence proves convergence of every square and cross moment. For a fixed order n, the smoothed square moment, the unsmoothed square moment and their cross moment all tend to the same diagram sum D_n. Hence

    E|X_(ρ,n)^(Green τ)−X_(ρ,n)|²→D_n+D_n−2D_n=0.           (4.1)

The same statement holds with physical vertex masks. This identifies the Bochner integral with the canonical Green-before-noise terminal integral at the positive noise widths, rather than merely proving an unnamed Cauchy property. In d3, weak convergence is to the actual sphere Green measure. In d1/2 the same argument applies if a Green smoothing was introduced. A sample bound on heat tails, a full-dimensional sphere density and an exchange with the noise-width limit are all unnecessary.

By098 the finite Gaussian joint source law is exactly the source vertexwise law: common spatial width ε gives edge width2ε, common temporal width η gives K_η, and cross widths use ε+ε' and max(η,η'). Equality of these finite laws passes to the Bochner chain integrals by their simple-function approximations. Therefore the width-uniform bound008 applies to the actual unmasked X_(ρ,n) after(4.1):

    ||X_(ρ,n)(t,x)||₂≤q_n(t).                               (4.2)

This use of008 is not a claim that c_ρ is uniform in ρ.

## 5. Every mixed Wick diagram and every physical vertex mask

For odd n+k, the centered joint Gaussian moment in(3.4) is zero. For n+k=2l≥2, Wick's formula sums over every labeled perfect pairing D of all2l vertices, with coefficient one for each. It includes within-chain self-pairs and cross-pairs, unequal chain lengths and an empty chain. A diagram has unmasked value

    ∫ ∏_({i,j}∈D) C_ρ(s_i,z_i;s_j,z_j) d(ν_n⊗ν_k)≥0.        (5.1)

The masked product has exactly one extra factor m(z_i) for every vertex. Since a pairing uses every vertex once,

    ∏_({i,j}∈D)m(z_i)m(z_j)=∏_(i=1)^(2l)m(z_i)∈[0,1].      (5.2)

This factor is independent of which pairing was chosen. Nonnegativity of every covariance factor in(5.1) gives diagramwise and then mixed-order comparison

    0≤E[X_(ρ,n)^m(t,x)X_(ρ,k)^m(t,y)]
      ≤E[X_(ρ,n)(t,x)X_(ρ,k)(t,y)].                         (5.3)

At n=k=0 both expectations are1. For odd total order they are both0. Taking k=n,y=x and using(4.2) gives

    ||X_(ρ,n)^m(t,x)||₂≤q_n(t).                             (5.4)

This is a positive expected-diagram comparison for displacement terms. It asserts neither pathwise solution order nor a positive-semidefinite ordering of Gaussian covariance matrices. Indeed masking a finite covariance C by DCD can leave C−DCD indefinite; an explicit algebra control is given below. Self-pairings cannot be discarded: already the mixed0+2 expectation need not vanish.

## 6. Local ordinary Picard solution and uniqueness

Fix this ρ, a compact observation set K and a finite horizon T. On the source regularity event use the compact causal region

    D={ (s,y): 0≤s≤T, dist(y,K)≤T−s }.

Every backward cone from a point of D remains in D. The source is samplewise continuous there, so M=sup_D|Y_ρ| is finite; it also bounds |mY_ρ|. This is a local sample bound at fixed ρ. It is not used for the heat-smoothed kernels from section4.

Define ordinary pathwise Picard terms by X_0^path=1 and

    X_n^path(t,x)=∫_0^t∫G_d(t−s,dz)
                        b_ρ(s,x−z) X_(n−1)^path(s,x−z)ds,    (6.1)

with b_ρ=mY_ρ or Y_ρ. Recursion(2.2), applied inside the causal region, proves

    |X_n^path(t,x)|≤M^n t^(2n)/(2n)!,
    Σ_n sup_D|X_n^path|≤Σ_n M^nT^(2n)/(2n)!<∞.              (6.2)

For M>0 the last sum is cosh(Tsqrt(M)); for M=0 it is1. Each term is continuous. One direct proof rescales ordered time coordinates by t and uses the fixed unit-time Green probability representation: vertex locations and source values depend continuously on(t,x), while their products are bounded on a slightly enlarged compact cone. Ordinary dominated integration applies; at t=0 the factor t^(2n) gives continuity for n≥1.

Uniform convergence gives a locally continuous sum. The uniform series bound permits summation inside the finite Volterra integral, so its sum solves u=1+G*(b_ρu), with initial displacement1 and velocity0. For two locally continuous solutions on this cone, let w be their difference and B=sup_D|w|<∞. Iterating w=G*(b_ρw) gives

    |w(t,x)|≤B M^n t^(2n)/(2n)!→0.

This proves local uniqueness. Exhausting by integer horizons and compact balls and using uniqueness on overlaps gives the locally continuous ordinary solution globally for this fixed ρ. The argument does not require a globally bounded unmasked source.

The pathwise and Bochner terms agree at each fixed terminal point. The continuous field version is a modification of the Gaussian pointfield at each vertex; joint measurability and scalar Fubini pass that identification to the finite chain measure. Moreover

    E∫|F_n|dν_n≤∫||F_n||₂dν_n<∞,
    E|∫F_n dν_n|²≤ν_n(1)∫E|F_n|²dν_n<∞.

Testing against bounded random variables and applying scalar Fubini identifies this ordinary chain integral with the Bochner integral(2.3). Thus all orders agree simultaneously at a fixed terminal point. Their partial sums converge pathwise by(6.2) and in L² by(5.4),(1.3); uniqueness of convergence in probability identifies the L² sum with that pathwise Picard value. The resulting locally continuous field is a version of the L² sum at every fixed point. No uncountable intersection of terminal-point or source-width exceptional sets is used to define this version.

## 7. Absolute double sums, stationarity and actual Bochner averages

For fixed t set Q=Σ_(n≥0)q_n(t)<∞. Bounds(4.2),(5.4) give absolute L² convergence of both solution series, uniformly in spatial points and positive widths. For either family, Cauchy–Schwarz gives

    Σ_(n,k≥0)E|X_(ρ,n)^(m)(t,x)X_(ρ,k)^(m)(t,y)|≤Q².       (7.1)

Products of finite partial sums converge in L¹: if U_N→u in L² at both terminal points, then

    ||U_N(x)U_N(y)−u(x)u(y)||₁
      ≤||U_N(x)−u(x)||₂||U_N(y)||₂
         +||u(x)||₂||U_N(y)−u(y)||₂→0.

Consequently mixed expectations sum to the actual two-point moment, and(5.3) passes to

    0≤E[u_ρ^m(t,x)u_ρ^m(t,y)]≤E[u_ρ(t,x)u_ρ(t,y)].         (7.2)

Only the unmasked law is stationary in space: its source covariance depends on spatial differences, and translation of both terminal points commutes with every finite chain integral. Finite Gaussian laws, then L² limits, therefore preserve spatial stationarity. No equivariant coupling with raw W is needed for this marginal law assertion. Cauchy–Schwarz gives

    E[u_ρ(t,x)u_ρ(t,y)]
      ≤||u_ρ(t,x)||₂||u_ρ(t,y)||₂=E|u_ρ(t,0)|².              (7.3)

The masked solution need not be stationary.

For each finite order, x↦X_(ρ,n)^m(t,x) is L²-continuous: use the fixed unit-time parameters in(2.1), translate all vertex positions with x, apply product increment estimate(3.2) and continuity of mask factors, then dominate by the fixed Gaussian product bound(3.1) under the finite chain measure. For the full sum choose a large finite order first; uniform q_n tails then transfer this continuity. Hence x↦u_ρ^m(t,x) is an L²-continuous map with ||u_ρ^m(t,x)||₂≤Q and separable image closure (images of a countable dense subset of R^d suffice). It is strongly measurable as an L²-valued map.

For real φ∈C_c∞, the Bochner average B_φ=∫φ(x)u_ρ^m(t,x)dx exists because ∫|φ| ||u_ρ^m||₂≤Q||φ||₁. Scalar Fubini also gives the ordinary pathwise average C_φ almost surely, and weighted Cauchy–Schwarz gives

    E|C_φ|²≤||φ||₁∫|φ(x)|E|u_ρ^m(t,x)|²dx≤Q²||φ||₁².

For every bounded real random variable Ξ,

    E[Ξ B_φ]=∫φ(x)E[Ξu_ρ^m(t,x)]dx=E[Ξ C_φ],

with absolute Fubini bounded by ||Ξ||∞Q||φ||₁. Taking Ξ=sign(B_φ−C_φ) proves B_φ=C_φ almost surely. This identifies the actual Bochner and ordinary averages without assuming a point trace on a Sobolev phase.

If φ≥0, then φ(x)φ(y)≥0, so the ordered two-point comparison(7.2) can be integrated against this product as stated. Absolute Fubini is bounded by ||φ||₁²Q². Using(7.3) gives

    E|∫φ(x)u_ρ^m(t,x)dx|²
      ≤||φ||₁² E|u_ρ(t,0)|².                               (7.4)

The nonnegative-test assumption is used in this direct integration of an ordered covariance comparison. It is not replaced by stationarity of the masked field or by samplewise positivity of the solution.

## 8. Exact terminal-to-initial reversal and canonical fixed orders

Work at the common terminal point(t,0). On a chain of length n define, for1≤j≤n,

    s'_j=t−s_(n+1−j),       z'_j=−z_(n+1−j),
    (s'_0,z'_0)=(0,0).

The time map has absolute Jacobian1 and takes the ordered terminal simplex bijectively to the initial ordered simplex. The old last edge G_d(t−s_n,d(−z_n)) becomes G_d(s'_1,dz'_1); every other old edge becomes the next successive primed increment. The Green measure change is the corresponding affine pushforward, not a substitution into a sphere density. Apply the same transformation separately to the second chain of length k. Empty chains have the identity transformation and no variables.

Let r be the vertex permutation reversing each chain internally. For any old paired vertices, both the time and spatial differences are the negatives of their corresponding primed differences, since both chains have the same terminal time and point. Evenness of K_η and Γ_(2ε) preserves each covariance factor. Each pairing D maps to

    r(D)={ {r(i),r(j)} : {i,j}∈D }.

This is a bijection of all labeled pair partitions and is an involution. It adds no coefficient, chain shuffle or multiplicity, and it keeps self- and cross-pairings and both separate initial roots. These facts also hold before removal of noise widths.

Section4 first removes Green smoothing at positive ρ. The exact source law(1.1) then matches006's vertexwise regularization law in the initial-chain convention, with common spatial/temporal widths as a special case. Thus006 gives, at arbitrary relative ε,η→0, the limit of every fixed diagram. With002's canonical diagram identity, for fixed n,k,

    E[X_(ρ,n)(t,0)X_(ρ,k)(t,0)]→E[X_n(t,0)X_k(t,0)].        (8.1)

Odd totals stay0 and n=k=0 stays1. This is an equality of source-family diagram laws and numerical moment limits. It does not assign a new pathwise realization of the whole canonical solution family or claim ordinary u_ρ→u pathwise.

## 9. Finite square first, width limit next, infinite order last

The absolute mixed moments on both sides of(8.1) are bounded by q_n(t)q_k(t). Put

    Q_N=Σ_(n=0)^N q_n(t),       r_N=Q−Q_N→0.

The double majorant outside the order square{0,…,N}² is exactly

    Q²−Q_N²=r_N(Q+Q_N)≤2Q r_N.                              (9.1)

First fix N. Its finitely many limits(8.1) hold jointly as the two source widths vanish at arbitrary relative rates. Both infinite-order tails have absolute value at most(9.1). Consequently

    |E|u_ρ(t,0)|²−E|u(t,0)|²|
      ≤|Σ_(n,k≤N)(E X_(ρ,n)X_(ρ,k)−E X_nX_k)|+4Q r_N.       (9.2)

Given a tolerance, choose N for the last term; then take the width limit on the finite square. This proves the actual point-moment limit of103. The canonical infinite sum is002's original solution series, and its norm summability is supplied independently by008. No covariance-order argument, interchange of infinite orders with a merely pointwise limit, or new whole-family coupling is used.

Suppose now that the actual masked Bochner averages converge in L² to Z_m, along a specified width sequence with both widths vanishing or at arbitrary rates. Then

    |E|B_ρ|²−E|Z_m|²|
      ≤||B_ρ−Z_m||₂(||B_ρ||₂+||Z_m||₂)→0.

Take the same limit in(7.4), use(9.2), and obtain

    E|Z_m|²≤||φ||₁²E|u(t,0)|².                              (9.3)

Existence of this masked L² limit is an explicit premise of103. Its proof alone establishes neither a raw masked evolution nor source-average convergence.

## 10. The application to110 has an independent existence input

For the fixed admissible phase mask m and horizon in `P:constant-gaussian-flow` (108), actual source physical flows P_(A^ρ) converge to P_A in every finite L^p uniform triangle norm. This is an input about the retaining source drivers and the Young map, independent of103's conditional transfer. `L:constant-source-solution` (109) identifies the displacement distribution of P_(A^ρ)(t,0)e0 with the ordinary source solution from102, using the actual smooth source coefficient and ordinary Duhamel uniqueness. It does not use103.

For φ≥0 smooth compact with ∫φ=1, the bounded phase functional is O_φ(e,c1,c2)=〈e1,φ〉+c1, with norm bounded by sqrt(||φ||_(H^(−1/2))²+1). The constant coordinate is necessary because data1 is not in H^(1/2) on whole space. There is no point evaluation of a Sobolev state. The distributional identification109 and the Bochner/ordinary average identification in section7 give, at each fixed ρ,

    B_ρ=∫φ u_ρ^m=O_φ P_(A^ρ)(t,0)e0.

Therefore108 directly proves

    ||B_ρ−O_φ P_A(t,0)e0||_p
      ≤||O_φ||||e0|| || ||P_(A^ρ)−P_A||_∞ ||_p→0,

in particular in L². This supplies103's convergence premise. Only after this independent construction does110 apply(9.3), at the same mask, horizon, original covariance, widths and φ, to obtain E|Z_m|²≤E|u(t,0)|². The raw limiting driver is W-measurable and the deterministic/Young maps retain this, so the limit is a raw W-variable even though individual source realizations may use the retaining auxiliary Gaussian extension. No assertion about an unmasked noisy path limit is needed. This is the noncircular existence-versus-comparison order of the application.

## 11. Finite falsification controls and scope

1. The exact chain masses for n0,…,3 are1,t²/2,t⁴/24,t⁶/720. They follow from the convolution recursion, not a new binomial shuffle. The supplied polynomial arithmetic checks these masses independently.
2. A rank-one centered Gaussian vector with every coordinate equal to one standard real Gaussian has every covariance entry1. Its order-four Wick sum is3; the unequal0+2 mixed moment is1,1+3 is3, and total odd3 is0. These finite algebra controls rule out imposing orthogonality on different Stratonovich orders. They are not claimed to be a new admissible time-fractional model.
3. For four deterministic vertex masks(1,1/2,1/3,1), every pairing's mask product is1/6, so its rank-one order-four Wick value is3/6=1/2. The factor is attached to every vertex, including a vertex paired within its own chain. Enumeration also checks that within-chain reversal is a pairing bijection for unequal/empty splits.
4. Let C=[[1,1],[1,1]] and M=diag(1,0). Then C−MCM=[[0,1],[1,1]] has determinant−1; the vector(1,−1) has quadratic value−1. Thus the inference C−MCM≥0 is false even for a nonnegative PSD C. This is a finite algebra counterexample to covariance-order reasoning, not an assertion that this matrix is a new admissible α0-covariance model. Positive Wick diagram comparison uses(5.1)–(5.2) instead.
5. For a numerical summable majorant q_n=2^(−n), Q=2 and r_N=2^(−N), the exact outside-square sum is4r_N−r_N²≤4r_N=2Q r_N. This tests(9.1), not an assumption about the actual q_n. The actual source bound is(1.3).

All statements above keep masks and horizons fixed. Γ=0 gives the deterministic free solution1 directly. No sharp constant, Skorohod theorem, samplewise monotonicity, covariance PSD order, uniform growing-mask estimate, heat-tail sample bound, or unconditional masked source limit follows from these three local statements.
