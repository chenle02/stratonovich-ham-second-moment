# Calibration replay for PROOF010 and PROOF013–019

Author-only mathematical replay at exact science `8ce03ae09cca984b32aaddf3da0a6ded07f47ebc`. The main TeX is byte-identical to `b4b6efc`; bindings and exact current label/proof locators are in `source-binding.json`. This packet has precisely three subaims: A, the homogeneous-Laplace numerical majorant; B, the Riesz finite coefficients; C, the closing/opening and low-spatial-exponent upper bounds and first-mean calibration. All of these own proof steps are already written in the source. The work below makes the calculations, constants, dependencies and limits explicit; it does not manufacture a missing theorem or change a proof.

No new provider, review dispatch, Article/ref/sibling change, full clone, literature search, Lean or HPC work is used. Original calibration MEDIUM and the later ungraded LIMITED record are not upgraded by this author replay. The assigned current171 scoped-HIGH inventory is workflow context, not a mathematical premise or a claim that these eight bodies are independently accepted.

## A. PROOF010: exact norm scaling, factorial power and scoped no-go

### A1. Actual inputs and their hypotheses

Write a=α0, β=4−α−a>2, and κ=β/(3−α). Keep every original d∈{1,2,3} and homogeneous nonnegative even positive-definite tempered Radon covariance Γ with original amplitude, 0<α<d or α=d=1, 0<a<1, α+a<2. Let μ be its positive even spectral measure in the convention Γ=∫exp(iξ·x)μ(dξ), distributionally. Zero covariance is handled directly below.

The named local inputs are PROOF004 `L:damped-homogeneous-norms`, PROOF006 `L:joint-fixed-order`, and the earlier independently constructed/mild-identified series and mixed expansion. The norm lemma applies because the strict original threshold ensures α<2, a>0 and α+a<2. It proves the full norm finiteness for every Laplace parameter θ>0 and the smoothing/truncation upper bounds, not merely a large-θ estimate. PROOF006 includes unequal and empty chains and the Green-before-noise convention; the actual given-noise coupling gives fixed-order L² convergence, hence mixed products converge in L¹. The solution series was already norm-summable before this majorant is used; no finiteness is proved circularly from the final intrinsic constant.

The source Theorem3.1 is an imported universal pairing inequality with its original first-norm hypotheses. At application, first keep positive edge spatial widths, so the spectral measures are Gaussian-weighted and finite; keep finite temporal Laplace domains with measure λ^(a−1)dλ/Γ_E(a). Nonnegative heat covariances and temporal kernels are retained. The local translated-covariance lemma214 supplies the production Case2 bound with coefficient one and independent predecessor origins. Its actual temporal offset A−B remains; neither the source's offset-free intermediate equality nor PSD of a shifted cross kernel is assumed. The N2 norm uses independent spatial variables x,y, as explicitly defined in the current source. The other source induction steps remain imported with their stated hypotheses.

The actual norms are

    N0(θ)=∫_0∞ e^(−θs) G_s(R^d) ds,
    N1(θ)=Γ_E(a)^(-1)∫_0∞ λ^(a−1)∫[(θ+λ)²+|ξ|²]^(-1) μ(dξ)dλ,
    N2(θ)²=∫_0∞∫_0∞ e^(−θ(s+t))|s−t|^(−a)
                    ∫Ghat_s(ξ) overline(Ghat_t(ξ)) μ(dξ)dsdt.

Here G_s has mass s and Ghat_s(ξ)=sin(s|ξ|)/|ξ| with value s at zero. These formulas use measures, including the actual d3 sphere kernel, not an assigned Green density. The Euler Gamma factor is part of the original temporal covariance normalization.

### A2. Scale every norm and the actual pairing factors

Spectral homogeneity is μ(cA)=c^α μ(A). Consequently

    N0(θ)=θ^(−2),
    N1(θ)=θ^(α+a−2)N1(1),
    N2(θ)²=θ^(α+a−4)N2(1)²=θ^(−β)N2(1)².                    (A.1)

For N1 use λ=θu, ξ=θη: the temporal measure supplies θ^a, the spectral measure θ^α and the denominator θ². For N2 use s=u/θ,t=v/θ,ξ=θη: dsdt contributes θ^(−2), the temporal power θ^a, the spectral measure θ^α, and the two wave factors θ^(−2). This yields θ^(α+a−4), with no dimensional density factor. N0 follows directly from ∫e^(−θs)s ds.

The local finiteness checks are the actual ones: the N1 radial resolvent integral is finite for0<α<2, and its remaining λ integral is finite at zero by a>0 and at infinity by α+a<2. For N2, on |ξ|≤1 use |Ghat_s|≤s, and outside use |Ghat_s|≤|ξ|^(−1), with ∫_(|ξ|>1)|ξ|^(−2)μ(dξ)=αV/(2−α). The time singularity is integrable because a<1. Integrating time first gives a nonnegative covariance quadratic form at each ξ, so Gaussian spectral damping and temporal Laplace-domain restrictions decrease these norm bounds. This is a positive quadratic-form statement, not pointwise monotonicity in the physical smoothing width.

In a source pairing partition the class counts satisfy q0=q1 and q0+q2/2=k at total order2k. Its norm product is `(2N0N1)^q0 N2^q2`. By (A.1), both 2N0N1 and N2² have degree−β. Choose

    K≥max{2N1(1),N2(1)²},   K>0.

Then every such product is at most K^k θ^(−βk). On finite chains, the exponential gap weights telescope to e^(−θ(terminal1+terminal2))≥e^(−2θt). Extend only the nonnegative regularized integral to infinite simplices. Summing the P_k pairings gives

    E[X_m(t,x)X_n(t,x)]≤P_k K^k e^(2θt) θ^(−βk),  m+n=2k.    (A.2)

This applies first at positive noise widths; remove the d3 Green width at fixed noise widths, then remove the noise widths by PROOF006. Products pass in L¹ and finite splits/pairings pass individually. In d1/2 only noise widths are needed. The estimates are uniform at those stages. An empty chain has terminal time zero, so e^(2θt) remains a harmless common upper factor.

Crucially θ is allowed to be small here: we use the exact full homogeneous norms, not the older large-θ crude inequalities or the source's disputed all-t uniformity assertion for its bound(5.4).

### A3. Explicit factorial comparison and actual exponent

Define exactly the source's numerical majorant

    B_K(t)=1+Σ_(k≥1)(2k+1)P_k K^k inf_(θ>0)[e^(2θt)θ^(−βk)].

Its relation to the solution is an upper bound, not an equality. Differentiating 2θt−βk logθ gives the global minimum at θ=βk/(2t), of value

    e^(βk)(2t/(βk))^(βk).

Let Q=β−1=3−α−a>1 and D=K e^β(2/β)^β. The kth nonconstant summand can be written exactly as

    (2k+1)(P_k/k!) D^k t^(βk)
          [(k!)^β/k^(βk)] /(k!)^Q.                            (A.3)

The elementary inequalities

    1≤P_k/k!≤2^k,  1≤2k+1≤3^k,
    e^(−βk)≤(k!)^β/k^(βk)≤1

follow from P_k=∏_(j≤k)(2j−1), k!≤k^k, and log(k!)≥∫_1^k logx dx≥klogk−k. Thus with explicit positive constants

    A=K(2/β)^β,       B=6K e^β(2/β)^β,

    Σ_(k≥0)(A t^β)^k/(k!)^Q ≤ B_K(t)
                           ≤ Σ_(k≥0)(B t^β)^k/(k!)^Q.         (A.4)

For Q≥1, Σ z^k/(k!)^Q≤[Σ z^(k/Q)/k!]^Q=exp(Qz^(1/Q)). For a lower bound at large z choose k=floor(z^(1/Q)/2). Once z^(1/Q)≥4, k≥z^(1/Q)/4 and k!≤k^k gives the one summand at least2^(Qk). Hence

    c t^ρ≤log B_K(t)≤C t^ρ,       ρ=β/(β−1)
      =(4−α−a)/(3−α−a)>κ.                                    (A.5)

Indeed ρ−κ=βa/[(3−α−a)(3−α)]>0. The factorial denominator is `(k!)^(3−α−a)`, not `(k!)^(3−α)`. The missing factor is `(k!)^a`, up to exponential-in-k constants. The2k+1 split count is exponential-absorbable and is not the cause of this loss.

This is a no-go for this **separately optimized uniform pairing majorant**, because log B_K/t^κ diverges. It is not a lower bound on E u², does not rule out refined grouping before estimates, and does not refute the actual target-scale theorem. At p1, using an empty chain changes e^(2θt) to e^(θt), the optimum to βk/t and only an exponential-in-k constant; Q is unchanged. As a↓0, both ρ and κ tend to(4−α)/(3−α), an exponent comparison only. No large-time/static limit is exchanged.

A concrete allowed full-model scale check is d3,α=3/2,a=1/4: β=9/4, Q=5/4, ρ=9/5 and κ=3/2. The majorant gap is visible even though that higher-α model is outside subaimC. If Γ=0, use u=1 directly. Choosing an unnecessarily positive K would still make a growing numerical majorant; that says nothing about free-solution growth.

## B. PROOF013: actual Riesz finite coefficients and their normalization

Keep d1,0<α<1,0<a<1 and γ(y)=c_α |y|^(−α), c_α>0; then α+a<2 automatically. Write β=4−α−a. These are the exact Riesz assumptions, not all homogeneous covariances or a source-constant identification.

### B1. The two-noise formulas

Set p=2−α. Two elementary antiderivatives in the rectangle give

    ∫_(−s)^s∫_(−r)^r |y−z|^(−α)dy dz
       =2[(s+r)^p−|s−r|^p]/[(1−α)(2−α)].

Multiplying the two G factors1/2 and c_α gives the actual spatial covariance integral

    I(s,r)= c_α[(s+r)^(2−α)−|s−r|^(2−α)]
                        /[2(1−α)(2−α)].                       (B.1)

The integrand is locally integrable at y=z because α<1. For the1+1 term, double the triangle s>r and put v=s−r. The factor2 cancels the2 in (B.1), and r ranges from0 to t−v. Therefore

    E X1²= c_α/[(1−α)(2−α)] ∫_0^t v^(−a)
       {[(2t−v)^(3−α)−v^(3−α)]/[2(3−α)]
                                      −(t−v)v^(2−α)}dv.        (B.2)

The bracket is the exact integral over r of `(2r+v)^(2−α)−v^(2−α)` and is nonnegative. There is no extra symmetry factor.

For the0+2 chain with positive increments r,v, the first spatial Green mass is r and

    ∫G(v,z)c_α|z|^(−α)dz=c_α v^(1−α)/(1−α).

The temporal pairing is v^(−a). Thus with λ=2−α−a>0,

    E X2= c_α/(1−α) ∫_(r,v>0,r+v<t) r v^(λ−1)drdv
         =c_α/[2(1−α)] ∫_0^t (t−v)²v^(λ−1)dv
         =c_α t^(λ+2)/[(1−α)λ(λ+1)(λ+2)].                    (B.3)

The last step uses `[1/λ−2/(λ+1)+1/(λ+2)]/2=1/[λ(λ+1)(λ+2)]`. Since λ+2=β, this is exactly the source formula. The full order-two coefficient is E X1²+2E X2, including both empty-chain placements; this is not an orthogonal-chaos coefficient.

### B2. Every order-four integral: the real normalization

For m+n=4, use four positive time gaps h in the source's unit domain H_m, with separate chain roots and each nonempty chain's gap sum<1. Define S_l as its cumulative time and Y_l=Σ_(i in its own prefix)h_i U_i, with U_i independent uniform variables on[−1,1]. For each fixed h_l>0,

    G(h_l,z_l)dz_l = h_l · Law(h_l U_l).

The map from spatial increments to vertices is triangular within each chain and has determinant one. Thus for D=A,B,C,

    J_(m,n,D)(t)=c_α² t^(2β) ∫_(H_m)(∏_(l=1)^4 h_l)
       ·∏_({j,q}∈D)|S_j−S_q|^(−a)
       ·E_U[∏_({j,q}∈D)|Y_j−Y_q|^(−α)]dh.                     (B.4)

The four uniform probability laws already contain(1/2)^4=1/16. Multiplying by another1/16 would be wrong. The U coordinates are independent integration variables, but the two differences Y_j−Y_q need not be independent; their product remains inside the expectation. All five ordered splits and all three pair partitions are specified, including unequal/empty chains and self-pairings, with the finite multiplicities from the existing white-order4 replay.

Scaling time and space contributes t^8 from four time and four spatial integrations; two spatial covariance factors give t^(−2α) and two temporal factors t^(−2a). The total is t^(8−2α−2a)=t^(2β). This is the homogeneous finite-order scale, not a moment asymptotic constant.

For finiteness, revert to the vertex variables. At unit time each vertex lies in[−1,1]. Enlarge the ordered time domains to[0,1]^4 and the spatial domain to[−1,1]^4 and bound each Green factor by1/2. Because each pair uses disjoint labels, Tonelli gives the finite majorant

    c_α²/16 ·[2/((1−a)(2−a))]²
              ·[2^(3−α)/((1−α)(2−α))]².                       (B.5)

This proves finite nonnegative integrability without a numerical quadrature. At a fixed strictly positive h, the spatial map is invertible and the two paired vertex differences are independent linear coordinates after a linear change, so their singular powers are integrable as well; no statistical independence of those differences is asserted. Pair-time coincidences lie on null hyperplanes, with integrability supplied by a<1.

### B3. Static and white endpoint checks, only at the stated normalization

At fixed α<1 the same integrable majorant with a replaced by any fixed ā∈(0,1) permits a↓0 in these finite coefficients. For p=2−α,

    ∫_[0,1]²[(s+r)^p−|s−r|^p]dsdr
       =(2^(p+2)−4)/[(p+1)(p+2)].

Insert this in (B.1) and add twice (B.3) at a=0. The static unit-time order-two coefficient is

    c_α 2^(3−α)/[(1−α)(2−α)(3−α)(4−α)],                       (B.6)

and its time factor is t^(4−α). No fixed α1 normalization is silently assumed in (B.1)–(B.6).

Only if one chooses the source's explicit normalization c_α=(1−α)/2 do the white limits follow. For (B.3), c_α/(1−α)=1/2 and λ→1−a, giving `E X2→c0 t^(3−a)/2`, where c0=[(1−a)(2−a)(3−a)]^(-1). In (B.2), the prefactor tends to1/2 and the bracket tends to(t−v)². For fixed t and α near1 the bracket is uniformly bounded, so C v^(−a) is integrable and dominated convergence gives

    E X1²→(1/2)∫_0^t v^(−a)(t−v)²dv=c0 t^(3−a).

These are the two already computed white coefficients. Formula(B.6) correspondingly tends to1/3 at unit time. Unnormalized |y|^(−α) is not δ0. This packet does not infer an order-four α↑1 limit from these two formulas or interchange a static/white/large-time limit; (B.5) is a fixed-α finiteness argument, not such a convergence proof.

The existing full white calibration supplies only the finite checks M2=t³/3 and M4=11t⁶/540 and the exact split/pairing counts. No all-order identity or closed moment formula is inferred from them.

## C. PROOF014–019: spatial integration, temporal symmetry and low-α constants

### C1. Descending-label integration: exactly one covariance at a closing

Keep the two block-ordered chains, with each chain's own root zero. For each vertex l write h_l=s_l−s_(p(l)) and spatial increment y_l=x_l−x_(p(l)). Every position uses only earlier increments in its own chain. Work first at positive edge Gaussian noise widths; for d3 keep positive Green width as required. The covariance factors and Green kernels are nonnegative. Orient each pair(i,j) by i<j and call i an opening and j a closing.

Integrate **all** increments in the order2k,…,1. The invariant before label l is that precisely the pair factors whose closing endpoint is≤l remain; all removed bounds depend on h only. At a closing l, its own edge has x_l−x_i=y_l+z with z independent of y_l. Every other remaining endpoint is<l and therefore independent of y_l. Thus its one covariance can be bounded by the closing convolution. At an opening l, its partner was larger and its covariance was removed already; every remaining factor is independent of y_l. Integration gives only the Green mass h_l. This reasoning applies to self- and cross-pairs and to empty/unequal chains, because the second root is not the first chain's last vertex. Tonelli justifies every nonnegative integration.

For d1 Riesz, the integral of the even decreasing |x|^(−α) over any interval of length2h is maximal when centered. One direct proof writes |x|^(−α) by layer cake: each superlevel set is a centered interval, and its overlap with an interval of fixed length is largest at zero; Tonelli preserves that inequality. Hence

    sup_z ∫G(h,y)c_α|y+z|^(−α)dy=c_α h^(1−α)/(1−α).

For a Gaussian convolution γ_ε, Tonelli averages these shifted integrals against the mass-one Gaussian, so the same upper bound holds for every ε>0. For white covariance γ_ε=c_δ p_ε,

    sup_z ∫G(h,y)c_δp_ε(y+z)dy≤c_δ/2.

No pointwise δ0 value is used. With k openings and k closings, the actual bound is

    S_D,ε(h)≤[c_α/(1−α)]^k ∏_(open)h_i ∏_(close)h_j^(1−α)   (α<1),
    S_D,ε(h)≤(c_δ/2)^k ∏_(open)h_i                            (α=1). (C.1)

### C2. Exact weighted AGM, not an unweighted substitution

Let b=2−α and H=Σ_l h_l≤2t. For α<1 assign unnormalized weights w_l=1 at openings and w_l=1−α at closings; their total is bk. Apply weighted AGM to **h_l/w_l** with normalized weights w_l/(bk). It gives

    ∏h_l^(w_l)≤[H/(bk)]^(bk)∏w_l^(w_l)
       ≤[2t/(bk)]^(bk)(1−α)^((1−α)k).                         (C.2)

The relaxed maximum has h_l proportional to w_l; it need not obey equality in each individual chain's horizon constraint, so only an upper bound is used. Multiplying the Riesz prefactor in(C.1) produces

    S_D,ε(h)≤K_sp^k t^(bk)/k^(bk),
    K_sp=c_α 2^(2−α)(1−α)^(−α)/(2−α)^(2−α).                   (C.3)

At α=1 do not apply a zero closing weight in the positive-weight AGM proof. Directly ∏_(open)h_i≤(2t/k)^k, so(C.1) yields(C.3) with b=1 and K_sp=c_δ. This avoids an undefined zero-weight expression.

### C3. Symmetrize the whole temporal pairing sum, then count the splits

Write

    F_k(s)=Σ_(D∈Π_k) ∏_({i,j}∈D)|s_i−s_j|^(−a),
    Z=2/[(1−a)(2−a)].

Every label permutation bijects Π_k, so F_k is fully symmetric. A single temporally weighted diagram generally is not symmetric; the common spatial maximum(C.3) must be extracted first. Every pairing has disjoint endpoints, giving

    ∫_[0,t]²|s−r|^(−a)dsdr=Z t^(2−a),
    ∫_[0,t]^(2k)F_k=P_k (Z t^(2−a))^k.

Order within the two blocks only. The m!n! block permutations give congruent regions, ties are null and the integrand is integrable. Therefore

    ∫_([0,t]^m_<×[0,t]^n_<) F_k
       =P_k (Zt^(2−a))^k/(m!n!),        m+n=2k.                (C.4)

The empty-chain factorial is0!=1. The pairing recurrence and split sum are

    P_k=(2k−1)P_(k−1)=(2k)!/(2^k k!),
    Σ_(m=0)^(2k)1/[m!(2k−m)!]=2^(2k)/(2k)!.

Their product is exactly2^k/k!, not an additional shuffle factor. Checks: k1 gives1·2=2, k2 gives3·(2/3)=2, and k3 gives15·(4/45)=4/3, agreeing with2^k/k! in each case.

Multiplying(C.3) and(C.4) and summing splits gives, for the actual regularized moments,

    A_k(t)≤(2ZK_sp)^k t^((b+2−a)k)/[k! k^(bk)]
          =(2ZK_sp)^k t^(βk)/[k! k^(bk)].                       (C.5)

Here β=b+2−a=4−α−a. Since k!≤k^k and b>0,

    k! k^(bk)≥(k!)^(b+1)=(k!)^(3−α).

With q=3−α=b+1 and A0=1, nonnegative series and the elementary ℓ^q/ℓ^1 inequality yield the **pure all-time** bound

    E u²(t,x)≤exp(U2 t^κ),
    U2=q(2ZK_sp)^(1/q),       κ=β/q.                            (C.6)

This U2 is the source section's explicit nonsharp upper-bound constant, not an assertion that the later intrinsic constant C2 equals it. No asymptotic static coefficient-rate constant is inserted into(C.5) or(C.6).

### C4. The all-dimensional closing bound for0<α<1

Now let Γ be any original covariance with0<α<1 in d1/2/3; no density or isotropy is assumed. Spectral uniqueness gives μ(cA)=c^αμ(A), so with V=μ(B1)<∞,

    μ(B_R)=V R^α,    μ({0})=0.

Layer cake and Tonelli give the exact radial integral

    ∫min(h,|ξ|^(−1))μ(dξ)
       =∫_0^h μ(B_(1/u))du
       =V∫_0^h u^(−α)du=V h^(1−α)/(1−α).                      (C.7)

The endpoint of each indicator has zero effect on the u integral. This uses the radial mass function, not a density of μ on R^d or on the sphere.

For γ_ε=p_ε*Γ, ε>0, and G_(h,η)=p_η*G_h, η≥0, Fourier Fubini is justified by the finite Gaussian-weighted spectral measure and the finite Green mass. In the original convention there is no additional(2π)^d factor:

    ∫G_(h,η)(dy)γ_ε(y+z)
       =∫e^(iξ·z)e^(-(ε+η)|ξ|²/2) sin(h|ξ|)/|ξ| μ(dξ).

Take the absolute value and use |sin(hr)|/r≤min(h,1/r). The physical integral is nonnegative since Γ and G are positive measures. Equation(C.7) therefore proves a uniform closing bound M h^(1−α) with M=V/(1−α). It is uniform in z,ε,η and includes η=0 and the d3 sphere measure. Oscillatory signs are not declared positive. c_α from the special Riesz physical bound and V from this general spectral bound are different quantities and are not equated.

### C5. Degree one: preserve the Gaussian-Abel oscillation and angular mass

At α=1, homogeneity gives μ(cA)=cμ(A), μ({0})=0. Define the finite angular measure

    σ(E)=μ{0<|ξ|≤1, ξ/|ξ|∈E}.

Its mass is V, it is even, and a polar rectangle(r1,r2]×E has mass(r2−r1)σ(E). Uniqueness of measures on these generating rectangles gives the genuine measure decomposition `μ(dξ)=dr σ(dθ)`. σ may be atomic; no angular density or isotropy is used.

Use A=(ε+η)/2>0, retaining the Gaussian factor. Evenness gives

    ∫G_(h,η)(dy)γ_ε(y+z)=∫ I_A(h,θ·z)σ(dθ),
    I_A(h,v)=∫_0∞ e^(−Ar²) sin(hr)cos(rv)/r dr.                 (C.8)

This radial integral is absolutely convergent at A>0. Both antipodal directions are already counted by σ; taking the even cosine introduces no second angular factor.

Let g_h(v)=1/2 ·1{abs(v)<h} and p_(2A)(v)=(4πA)^(-1/2)exp(−v²/(4A)). Their ordinary Fourier transforms are sin(hr)/r and exp(−Ar²). The exact one-dimensional inversion factor gives

    (g_h*p_(2A))(v)=(1/(2π))∫_R e^(irv)e^(−Ar²)sin(hr)/r dr
                   =I_A(h,v)/π.

Since p_(2A) has mass one and0≤g_h≤1/2,

    0≤I_A(h,v)≤π/2,
    0≤∫G_(h,η)(dy)γ_ε(y+z)≤πV/2.                              (C.9)

Equivalently I_A=(π/2)∫_(−h)^h p_(2A)(v−u)du, an explicit Gaussian-Abel evaluation. At v=0 and A↓0 this tends toπ/2, checking the coefficient, but no unsmoothed absolutely convergent integral is substituted into the proof. The divergent absolute envelope at α=1 is `V∫_0^h du/u`; that is why(C.7) cannot be used at the endpoint or replaced by a limit in its constant.

For d1 white Γ=c_δδ0, μ(dξ)=c_δdξ/(2π), hence V=c_δ/π and the closing bound is c_δ/2, exactly the d1 physical result. In d2/3 degree one does not mean full spatial white noise; for example the d3 plane measure dx1dx2 δ0(dx3) is permitted, with atomic angular spectral measure. As a finite endpoint check, the d3 wave measure is surface measure on the radius-h sphere divided by4πh. A horizontal belt of height du has surface area2πh du, so its normal-coordinate marginal is1/2 on[−h,h]. For Γ=c dx1dx2 δ0(dx3), direct physical Gaussian convolution therefore gives `(c/2)∫_(−h)^h p_(ε+η)^(1)(u+z3)du≤c/2`. Its spectral V is c/π and(C.9) gives the same c/2. This tests the singular-angular/antipodal normalization without replacing the sphere measure by a full-dimensional density.

### C6. General low-α constants, actual limits and all-time summation

Apply the same descending-label invariant in vector increments. For α<1 substitute M=V/(1−α) in(C.1)–(C.2); for α=1 use the closing constant M=πV/2 and ordinary AGM on openings. The results are

    K_sp,gen= V 2^(2−α)(1−α)^(−α)/(2−α)^(2−α),  α<1,
              πV,                                             α=1.

The temporal calculation is unchanged by dimension. Thus(C.5) and(C.6) hold with K_sp,gen and U2,gen=q(2ZK_sp,gen)^(1/q). This is PROOF018's actual all-time conclusion for all original homogeneous covariances with0<α≤1 in d1/2/3; it is not a proof for α>1.

For the limits, at positive noise widths the original Gaussian field has bounded continuous covariance, and its finite products are continuous as L² random vectors by the finite Gaussian moment formula. The actual ordered Green measure has finite mass; integrating the vector product against it defines the zero-Green-width approximant on the same given Gaussian space. In d3 use positive η for the ordinary-density estimates first. At fixed noise widths, products of Green measures converge weakly against bounded continuous Gaussian covariance products, with masses equal to∏h_l. A fixed constant times that product dominates on the bounded time simplex. The same argument for mixed moments against the actual η=0 approximant proves **identification of the L² limit**, not just an unnamed Cauchy property. This is exactly the earlier fixed-order construction convention. Then remove noise widths with PROOF006 and pass products in L¹ by

    ||YZ−Y'Z'||_1≤||Y−Y'||_2||Z||_2+||Y'||_2||Z−Z'||_2.

Finite splits/pairings pass through those limits. No spatial-width monotonicity or source/time-limit interchange is used. In d1/2 only noise limits are needed. At η=0 the d3 object remains a Green measure, never an ordinary sphere density.

If V=0, homogeneity gives μ(B_R)=0 for every R, hence μ=Γ=0 and u=1. The direct free result replaces any formula requiring V>0. Nonzero Γ has V>0 by homogeneity/exhaustion.

### C7. PROOF019: one-chain coefficient and conditional Jensen comparison

For the mean, one ordered chain of length2k has total gap sum≤t, not2t. Replace t by t/2 only in the spatial maximum. Its spatial factor is K_*^k t^(bk)/(2^(bk)k^(bk)), with K_* the appropriate d1 or general constant above. The temporal pairing sum on the one ordered simplex is

    P_k(Zt^(2−a))^k/(2k)!=(Zt^(2−a))^k/(2^k k!).

Consequently

    E X_(2k)(t,x)≤(ZK_*/2^(b+1))^k t^(βk)/[k! k^(bk)]
                ≤(ZK_*/2^q)^k t^(βk)/(k!)^q.                  (C.10)

Odd expectations vanish. The previously justified L² series permits termwise expectation; the even terms are nonnegative. Summing gives

    E u(t,x)≤exp(U1 t^κ),
    U1=q(ZK_*/2^q)^(1/q),
    U2/U1=[2^(q+1)]^(1/q)=2^((4−α)/(3−α)).                     (C.11)

For nonzero covariance U1>0 and(4−α)/(3−α)>1, so2U1<U2. If the actual first-moment lower rate is at least a valid L, then L≤U1 and2L≤2U1<U2. Specializing L to the printed source label L_* remains **conditional on its intended normalization/lower-bound premise**. Actual Jensen uses E u²≥(E u)²; E u≥1 follows from the even positive pairing expansion, not from assuming sample-path positivity of the wave solution.

[held back until the source author has been told]

### C8. Finite checks and boundary scope

For unit white covariance, the exact A1 coefficient is2c0 while(C.5) gives2Z, with ratio Z/c0=2(3−a)>4. At a=1/2, Z=8/3,c0=8/15 and the ratio is5. At the static white endpoint, k2 in the **first** coefficient bound is(2Z)^2/[2!·2²]=1/2, while the coarser `(k!)^q` bound is1. Both exceed the exact finite coefficient11/540 from the full27-sector replay. These are deliberately nonsharp normalization checks.

With c_α=(1−α)/2, the d1 Riesz constant becomes `2^(1−α)(1−α)^(1−α)/(2−α)^(2−α)` and tends to1 as α↑1, matching unit white covariance. Without that normalization no white endpoint identification is made. The low-α general endpoint uses the separate Abel argument; its α<1 constant need not have a finite degree-one limit. As a↓0, κ tends to(4−α)/(3−α), the static exponent; no interchange with a large-time limit or uniformity of constants is asserted.

The source's comparison to a Skorohod exponent is read-only context with a different covariance normalization and solution concept. No Skorohod theorem, constant or solution is proved or identified here. Keeping self-pairings and empty-chain terms is essential already at total order two. The explicit bounds here are nonsharp pure all-time bounds; no asymptotic coefficient-rate constant is silently substituted into them.

## Disposition

The eight requested own arguments are fully worked through above under their exact source hypotheses. No additional mathematical gap or source error was found in this bounded replay. The principal distinction is structural: subaimA proves growth of a formal majorant with the wrong factorial power, while subaimC preserves a spatial k-power and sums temporal pairings before ordering to obtain the correct scale. SubaimB and the white packet check only finite coefficients and conditional endpoint normalizations.

This is author evidence and a constant/dependency crosswalk. It gives no independent confidence upgrade, image/render/cold credit, new review dispatch or whole-argument acceptance. The named norm/fixed-order/source-theorem inputs remain imports with their existing proof/application limits; no pointless reproof of those sources is claimed. The original all-model objective and every remaining gate, including the live six-proof review's unchanged candidate, remain intact.
