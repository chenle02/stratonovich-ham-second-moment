# Actual temporal controls and the finite smooth spatial ratio

This is an author mathematical derivation for independent inspection at scientific source `8ce03ae09cca984b32aaddf3da0a6ded07f47ebc`. Supplied derivations and finite checks are claims to verify. The two conclusions are the actual static-control inequality in `L:spatial-static-controls` (PROOF136) and the positive finite smooth ratio in `P:spatial-smooth-ratio` (PROOF137). No rough spatial extension or identification of an auxiliary label-one score with a first-moment constant is used.

## 1. Objects and the exact input contracts

Keep the original nonzero nonnegative, even, positive-definite tempered Radon covariance Γ from `H:homog`, in d∈{1,2,3}, with Γ(cE)=c^(d−α)Γ(E), 0<α<d or α=d=1, 0<a=α0<1 and α+a<2. In particular 0<α<2. The covariance amplitude, Laplacian coefficient one and given real isonormal noise W are unchanged. Put q=4−α>2 and k=q−1=3−α>1.

The full control class in `E:variational-positive-class` is C_pos={Ψ∈C_c∞((0,1)×R^d;R): Ψ≥0, Ψ≠0}; it includes all separable controls used below. `L:compact-raw-profile` (117) identifies their actual mean and raw variance:

    h_(Ψ,s)(x)=∫_0^1 |s−t|^(−a)(Γ*Ψ(t,·))(x) dt,
    v_Ψ=E W(Ψ)^2=∫_0^1∫ Ψ(s,x)h_(Ψ,s)(x) dx ds.

This is an actual covariance identity with W, not a pointwise noise potential or a variance inferred from an auxiliary field. The half cost in a score is v_Ψ/2; the variance formula itself has no half.

`L:variational-global-mean` (128) gives boundedness of every smooth control mean globally in space. `P:variational-unmasked-rate` (129) identifies the actual bottom of −Δ−h_(Ψ,s), self-adjoint on complex H² with form domain H¹, through the real unit-H¹ Rayleigh formula

    λ_(Ψ,s)^2=sup_(g∈H¹ real, ||g||₂=1)
                  (∫h_(Ψ,s)g²−||∇g||₂²)>0.

The rate is finite and positive for every s∈[0,1]. Its positivity uses an actual common negative trial for the original homogeneous mean (`P:compact-original-common-trial`,118); it is not an all-strength binding assertion for one fixed compact potential. There is no assertion that the unmasked bottom is an eigenvalue. The plateau argument behind this input uses potential gain C L^(−α) and kinetic cost D L^(−2), so α<2 is the required inequality even for singular covariances.

`P:variational-positive-scores` (132) has already constructed the finite positive real number

    S=S_1^pos=sup_(Ψ∈C_pos)(I_Ψ−v_Ψ/2),
    I_Ψ=∫_0^1 λ_(Ψ,s) ds,      0<S<∞.

For this application its actual finiteness is a named input: the independent `T:full-upper` (051) bounds the same canonical second moment; `P:variational-remove-mask` (130) bounds every label-two score by that same point liminf; full-class dilation (131) transfers that upper bound to the label-one scores. None of this input requires the later rough spatial pairing extension138 or energy map139. This is the order of dependence used below, not an appeal to a spatial energy inequality that is being proved here.

For spatial tests use the physical pairing from `L:spatial-physical-pair` (135):

    B_Γ(f,h)=∫Γ(dy)∫ f(x)h(x−y) dx.

Only smooth compact nonnegative functions are paired below, so absolute finiteness follows directly from compact autocorrelations and local finiteness of Γ. No H¹ four-linear extension is assumed. The exact temporal inputs are `L:equilibrium-gamma-beta` (133) and `L:temporal-equilibrium` (134). The latter is reconstructed next, including its endpoints and its unnormalized mass.

## 2. Exact temporal density, all endpoint values, and its mass

Let r=(1−a)/2∈(0,1/2), D_r=Γ_E(r)Γ_E(1−r), and

    f_a(t)=[t(1−t)]^(−r)/D_r,       0<t<1.

Here Γ_E is Euler's Gamma function, distinct from the spatial measure Γ. The endpoint powers −r>−1 and −2r=a−1>−1 show f_a∈L¹∩L². It is positive and smooth inside (0,1), with integrable endpoint singularities; it is not itself an admissible compact temporal control.

For 0<s<1 consider the unnormalized left potential. Since −a=2r−1, t=su gives

    L(s)=∫_0^s (s−t)^(2r−1)[t(1−t)]^(−r) dt
        =s^r∫_0^1 (1−u)^(2r−1)u^(−r)(1−su)^(−r) du.

The nonnegative binomial series and Tonelli give

    L(s)=Beta(1−r,2r)s^r
           Σ_(n≥0) (r)_n(1−r)_n s^n / ((1+r)_n n!).

Indeed the beta integral for term n is Beta(1−r+n,2r), whose ratio to Beta(1−r,2r) is (1−r)_n/(1+r)_n. On the other hand, expanding (1−u)^(r−1) in the incomplete beta integral shows

    B_s(r,r)=∫_0^s u^(r−1)(1−u)^(r−1) du
            =(s^r/r) Σ_(n≥0) (r)_n(1−r)_n s^n/((1+r)_n n!),

because (r)_n/(1+r)_n=r/(r+n). Thus L(s)=r Beta(1−r,2r)B_s(r,r). Reflection makes the right potential L(1−s). Symmetry gives B_s(r,r)+B_(1−s)(r,r)=Beta(r,r). The full unnormalized potential is therefore

    r Beta(1−r,2r)Beta(r,r)
      =r [Γ_E(1−r)Γ_E(2r)/Γ_E(1+r)]
           [Γ_E(r)^2/Γ_E(2r)]
      =Γ_E(r)Γ_E(1−r)=D_r.

All integrals used here have integrable endpoint powers and every series exchange is nonnegative. At s=0 a separate direct calculation gives

    ∫_0^1 t^(−a)[t(1−t)]^(−r) dt
      =∫_0^1 t^(r−1)(1−t)^(−r) dt
      =Beta(r,1−r)=D_r.

At s=1 reflection gives the same value. These are endpoint computations, not an unjustified limit of an interior formula. Consequently

    ∫_0^1 |s−t|^(−a) f_a(t) dt=1,       every s∈[0,1].       (2.1)

Its actual mass is

    M_a=∫_0^1 f_a
       =Beta(1−r,1−r)/D_r
       =Γ_E(1−r)/(Γ_E(2−2r)Γ_E(r))
       =Γ_E((1+a)/2)/(Γ_E(1+a)Γ_E((1−a)/2))>0.              (2.2)

In particular this mass is not replaced by one. The kernel is at least one on the unit square away from its null diagonal, so (2.1) also implies M_a≤1. For a>0 it is strictly less than one because the positive integrand sees |s−t|<1 almost everywhere.

## 3. Static spatial potentials: boundedness, actual positive rate, and Lipschitzness

Fix nonnegative nonzero z∈C_c∞(R^d), and put U_z=Γ*z. This is an actual smooth potential. Choose one nonnegative nonzero f∈C_c∞(0,1), fix s0=1/2, and set

    k_f(s0)=∫_0^1 |s0−t|^(−a) f(t) dt∈(0,∞).

For any c>0, Ψ_c(t,x)=c f(t)z(x)/k_f(s0) belongs to C_pos and its exact mean at s0 is cU_z. Input128 therefore makes U_z globally bounded, and129 gives

    Λ(c):=λ_z(c)^2
         =sup_(g∈H¹ real, ||g||₂=1)(c∫U_zg²−b(g))∈(0,∞),
    b(g)=||∇g||₂².                                         (3.1)

The construction works for each c; it does not infer positive rate for arbitrarily weak compact potentials in dimensions2/3. The potential here is the original unmasked homogeneous convolution. Its actual spectral positivity is supplied by129 under that exact type of mean.

Let H=||U_z||∞. Positivity of U_z and comparison of identical unit form tests imply monotonicity of Λ and

    |Λ(c)−Λ(d)|≤H|c−d|,         0<Λ(c)≤cH.                  (3.2)

For a compact positive interval [c_−,c_+], Λ(c)≥Λ(c_−)>0. Hence

    |λ_z(c)−λ_z(d)|
      =|Λ(c)−Λ(d)|/(sqrt(Λ(c))+sqrt(Λ(d)))
      ≤H|c−d|/(2λ_z(c_−)).                                 (3.3)

This proves the required Lipschitzness with the actual positive lower floor. No bound at c=0 and no unmasked ground eigenvector are used.

## 4. Actual compact temporal approximants and their raw cost

Use the same smooth nonincreasing χ as in130: χ(v)=1 for v≤1, χ(v)=0 for v≥2, and 0≤χ≤1. Its standard flat exponential construction ensures smoothness at both transitions. For n≥4 define

    f_n(t)=f_a(t)χ(1/(nt))χ(1/(n(1−t))),     0<t<1,
    f_n=0 outside (0,1),
    k_n(s)=∫_0^1 |s−t|^(−a)f_n(t) dt.                       (4.1)

The first cutoff is zero for t≤1/(2n), and the second is zero for t≥1−1/(2n). Between these neighborhoods all factors are smooth, so zero extension is C_c∞(0,1). Each f_n is nonnegative and nonzero: near t=1/2 and n≥4 both χ factors equal one. As n increases each reciprocal argument decreases, so both χ factors increase. For each fixed t∈(0,1), they are eventually exactly one. Thus f_n↑f_a pointwise inside the interval, with 0≤f_n≤f_a.

For every s∈[0,1], including both endpoints, nonnegative MCT and (2.1) give k_n(s)↑1. Let

    c0=∫_0^1 f_4(t) dt>0.

The subscript4 means the n=4 cutoff function, not the fourth power of f_a. Since |s−t|^(−a)≥1 off the null diagonal and f_n≥f_4,

    0<c0≤k_n(s)≤1,              every n≥4, every s∈[0,1].   (4.2)

Every Ψ_n(t,x)=f_n(t)z(x) is an actual member of C_pos. Its exact original covariance mean is h_(Ψ_n,s)=k_n(s)U_z. Uniqueness of the actual Rayleigh value (3.1), rather than a choice of eigenstate, identifies its rate with λ_z(k_n(s)). Bounds (3.2)–(3.3) on the fixed interval[c0,1] show this rate converges pointwise to λ_z(1), is bounded by λ_z(1), and is measurable (indeed continuous for each fixed n by the smooth-mean input). Dominated convergence gives

    I_(Ψ_n)=∫_0^1 λ_z(k_n(s)) ds →λ_z(1).                    (4.3)

The rates and their integrals also increase by monotonicity. No uniform convergence of k_n is needed for this step.

Positive Tonelli applied to the actual raw variance117 gives exactly

    v_(Ψ_n)=B_Γ(z,z) ∫_0^1 f_n(s)k_n(s) ds
           =B_Γ(z,z)∫_0^1∫_0^1
                         f_n(s)f_n(t)|s−t|^(−a) dt ds.       (4.4)

The full square already contains both time orderings. There is no extra factor2 or1/2 in (4.4). The nonnegative product f_n(s)k_n(s) increases to f_a(s) at every interior s; assign any finite endpoint values on the two null endpoints. Therefore MCT gives

    v_(Ψ_n) ↑ M_a B_Γ(z,z).                                  (4.5)

The spatial factor is a strictly positive finite number. To see this directly, define C_z(y)=∫z(x)z(x−y)dx. Translation continuity in L² makes C_z continuous; C_z(0)=||z||₂²>0 and its compact support is contained in K−K for K=supp z. Also 0≤C_z(y)≤||z||₂². Local finiteness gives B_Γ(z,z)≤||z||₂² Γ(K−K)<∞. For some ρ>0, C_z≥||z||₂²/2 on B_ρ. Nonzero Γ charges an origin-centered ball by exhaustion; homogeneity then gives positive finite mass to every positive-radius origin ball:

    Γ(B_ρ)=ρ^(d−α)Γ(B_1)>0.

Consequently B_Γ(z,z)≥(||z||₂²/2)Γ(B_ρ)>0. This uses origin-centered mass, not positive mass for every translated ball. In the permitted white case Γ=cδ0 with c>0, the same conclusion is the direct identity B_Γ(z,z)=c∫z²>0; no claim that Γ has no atom at zero is used.

Each actual smooth control satisfies S≥I_(Ψ_n)−v_(Ψ_n)/2 by the defining score supremum. Equations(4.3)–(4.5) therefore imply

    S≥λ_z(1)−(M_a/2)B_Γ(z,z).                               (4.6)

Both separate components converge, so their differences converge; those differences need not be monotone. This is a limit of numerical inequalities for actual smooth controls. Neither the endpoint-singular f_a⊗z nor a rough stochastic evolution is substituted into the admissible class. Every n is fixed before using its score inequality, and no n is made a function of the original large time.

## 5. Smooth ratio: positive numerator and denominator, exact physical scaling

Let g∈C_c∞(R^d;R) with ||g||₂=1. Its energy b=||∇g||₂² is positive: b=0 would imply |ξ|²|ĝ(ξ)|²=0 a.e., hence ĝ=0 away from the Lebesgue-null singleton{0}, so g=0 in L², a contradiction. Put A=B_Γ(g²,g²). The preceding autocorrelation argument applied to z=g² proves 0<A<∞ without a rough energy inequality. Define the positive finite ratio

    R(g)=A/b^(α/2).

For ℓ>0 put g_ℓ=U_ℓg, where U_ℓg(x)=ℓ^(d/2)g(ℓx). It is again real smooth compact with unit L² norm. Ordinary Lebesgue substitution gives b(g_ℓ)=ℓ²b. In the physical covariance pairing, first put X=ℓx, and then use the actual Radon pushforward

    ∫F(ℓy)Γ(dy)=ℓ^(α−d)∫F(Y)Γ(dY).

The two squared profiles contribute ℓ^(2d), dx contributes ℓ^(−d), and the covariance pushforward contributes ℓ^(α−d). Thus

    A(g_ℓ)=ℓ^α A.                                           (5.1)

This includes singular covariance measures and cδ0 in d=α=1. Replacing the covariance pushforward by a fictitious d-dimensional density substitution would give a different, incorrect power. In particular R(g_ℓ)=R(g), while A and b individually change.

## 6. Full amplitude/scale choice and both scalar optimizations

For θ,ℓ>0 the test z=θ g_ℓ² is a genuine nonnegative nonzero compact smooth spatial test, so (4.6) applies. Testing its actual Rayleigh supremum with the same unit g_ℓ gives

    λ_z(1)²≥θ ℓ^α A−ℓ²b,
    B_Γ(z,z)=θ²ℓ^α A.                                      (6.1)

The trial inequality supplies a lower bound; no claim that g_ℓ realizes the spectral bottom is made. Fix L>0 and initially any u>0. Choose

    ℓ²=uL²/b,
    θ=(1+u)L²/(ℓ^α A).                                     (6.2)

All quantities are finite and positive. The trial radicand is exactly L². The actual rate is positive, hence λ_z(1)≥L. Since ℓ^α A=R(g)u^(α/2)L^α, the half raw cost is

    (M_a/2)θ²ℓ^α A
       =[M_a(1+u)²/(2R(g)u^(α/2))] L^(4−α)=C(u)L^q.

Equation(4.6) therefore proves, for every L>0 and u>0,

    S≥L−C(u)L^q,
    C(u)=M_a(1+u)²/(2R(g)u^(α/2))>0.                         (6.3)

For fixed g, minimizing C(u) improves this lower bound. The logarithmic derivative of its u-dependent part is

    2/(1+u)−α/(2u)=(qu−α)/(2u(1+u)).

It is negative before u*=α/q and positive after. The factor diverges as u↓0, and as u→∞ it grows like u^(2−α/2)=u^(q/2), so this is its global minimum. In particular 1+u*=4/q. No optimizer for g or for the original control class is assumed.

Put C=C(u*). For L>0, F(L)=L−CL^q has derivative 1−qCL^(q−1). Its unique maximum is at L*=(qC)^(−1/k); it tends to0 as L↓0 and to−∞ as L→∞. Since C L*^q=L*/q,

    max F=(k/q)(qC)^(−1/k)
         =k[1/(q^q C)]^(1/k).                               (6.4)

In the last equality q=k+1, so the exterior q factor is absorbed as q^(k+1)=q^q. Substituting u*=α/q gives

    q^q C = [M_a/(2R)] q^q (16/q²)(q/α)^(α/2)
           =8M_a q^(q+α/2−2)/(R α^(α/2))
           =8M_a q^(q/2)/(R α^(α/2)),                       (6.5)

where q+α/2−2=q/2 follows from q=4−α. Combining(6.3)–(6.5) gives precisely

    S≥k [ R(g) α^(α/2)/(8M_a q^(q/2)) ]^(1/k).              (6.6)

The denominator8 comes from the half raw cost together with (1+u*)²=16/q². The temporal mass M_a is the actual mass(2.2); covariance amplitude remains inside A and R.

## 7. Finiteness before extension and the exact scope of the conclusion

Every smooth unit g has a positive finite ratio and satisfies(6.6). Since the already defined S is a finite positive real number, monotonicity of positive powers yields the uniform smooth bound

    R(g)≤[8M_a q^(q/2)/α^(α/2)] (S/k)^k<∞.                  (7.1)

The set of real smooth compact unit profiles is nonempty: normalize any nonzero real compact bump. Its ratio is positive by section5. Thus its supremum R0 exists as a finite real number with 0<R0<∞. No maximizer is claimed. The proof has not used finiteness of B_Γ on arbitrary H¹ profiles, a covariance Cauchy–Schwarz inequality for rough products,138 or139. Rather (7.1) is the finite smooth input that138 subsequently extends.

For Γ=0, all costs and rates vanish and the original free solution has zero moment rate; the strict positive statements and division by A belong only to the stated Γ≠0 case. For nonzero Γ, all parameters a,α,d and all supports are fixed in each constructed test. The scalar choices θ,ℓ,L produce actual individual tests; the proof does not assert a single common mask, uniform stochastic path bound over these tests, or any interchange with a large-time limit.

S_1^pos remains an auxiliary positive-control score. Nothing here identifies it with the actual first-moment constant, Chen's source labels, or a prescribed variational normalization. The conclusion is the two local static-control/smooth-ratio statements under their actual named proved input contracts, preserving d1/2/3, white and singular-angle covariances and original amplitude.

## 8. Explicit finite and boundary controls

1. For a=1/2, r=1/4. The endpoint potential's unnormalized beta factor is Beta(1/4,3/4)=Γ_E(1/4)Γ_E(3/4), while M_a=Γ_E(3/4)/(Γ_E(3/2)Γ_E(1/4)). These are different constants. Dividing the density by M_a to make it probability mass one would change its potential from1 to1/M_a and would invalidate the unchanged cost calculation.
2. The n=4 cutoff is identically f_a on[1/4,3/4], so c0≥∫_(1/4)^(3/4) f_a>0. At s=0 its kernel is t^(−a); its full integrable endpoint exponent is −a−r=r−1, not −a alone. No endpoint value f_a(0) is used.
3. For Γ=cδ0 in d1, B(z,z)=c||z||₂² and A(g_ℓ)=cℓ∫g⁴. For Γ=c dx1dx2 δ0(dx3) in d3, α=1 and Γ(B_ρ)=cπρ²>0. This covariance can give U_z no decay in the first two directions and can vanish on translated balls off its support. Neither behavior obstructs the origin-autocorrelation or actual unmasked-Rayleigh arguments; neither an everywhere-positive ball mass nor an unmasked eigenstate may be inserted.
4. At α=1, q=3,k=2,u*=1/3, and(6.6) becomes S≥2sqrt(R/(24sqrt(3)M_a)). The exponent identity is3+1/2−2=3/2. At α=3/2, q=5/2,k=3/2,u*=3/5, and the identity is5/2+3/4−2=5/4. The latter spatial exponent is admissible, for example in d3 with a=1/4; the proof is not restricted to low spatial exponents.
5. In the scalar optimization alone take q=3,C=1/3, so F(L)=L−L³/3. Its critical value is L*=1 and F*=2/3; values at L=1/2 and2 are11/24 and−2/3. This checks both representations in(6.4). These arbitrary scalar values are not a claimed realization of a temporal mass or a covariance profile.
6. Separate increasing sequences need not have increasing differences: I=(1,3/2,7/4) and half costs=(1/10,1,6/5) have scores=(9/10,1/2,11/20). Thus convergence of both actual components, rather than score monotonicity, is the valid step in(4.6).

The accompanying standard-library Fraction code independently checks the rational exponent identities, derivative signs at rational u values, scalar maximizing example, covariance-dilation exponent cancellation and the nonmonotone-difference control. Such finite controls do not replace the analytic endpoint, same-control raw-cost or spectral-domain proofs above.
