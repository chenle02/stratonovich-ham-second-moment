# Given-noise F extension, Young flow limit, and ordinary-source joins

Author-only mathematical replay, bound to scientific revision b4b6efccacbbccd8f747225330e9ccb27bc097a6. It expands existing PROOF105 and108, with109/110 joins, rather than adding a theorem or changing a proof. Source modules are frozen verbatim under `frozen-inputs/` and bound by `bindings.json`. There is no reviewer call, acceptance decision, confidence upgrade, source/ref edit, or new Lean/Skorohod/HPC claim.

The actual new coupled MAIN report has120 CHECKED and94 LIMITED rows and supplies no canonical verdict/confidence contract. Its105 and108–111 rows are LIMITED/outline. The earlier bounded Young report remains PASS_WITH_NOTES/MEDIUM. Neither is replaced by this author replay. The three subaims below provide the explicit analytic steps a later depth review could check.

## Setting and checked local inputs

Fix R,T>0 and the original admissible d∈{1,2,3}, covariance Γ and amplitude, a=α0∈(0,1), α+a<2. Use E_r=H^r×H^(r−1), E=E_(1/2), and the exact strict driver parameters

    0<γ<min(1/2,(2−α)/2),
    1/2<θ<β<min(1−a/2,(3−a−α)/2).

Let m=ζ_R be the allowed real even compact mask, 0≤m≤1, with support in the closed B_(2R). Set F=E⊕R², i(e)=(e,0,0), π_C(e,c1,c2)=(c1,c2), e0=(0,1,0). The total distribution of (e,c1,c2) is (e1+c1,e2+c2). Write D_χ for multiplication by χ on BOTH E entries. Choose χ=1 on B_(2R+T+1), supported in B_(2R+T+2), and ψ∈Cc∞ equal to1 on a neighborhood of suppχ. All constants below may depend on these fixed data.

The replay uses the following actual local statements under their exact guards. These are named proved inputs, not newly postulated gaps:

- `P:actual-operator-driver`, actual-driver LF27–55/555–591: the given original W produces M_E in every finite Lp Cθ(B(E)), with √p bounds, a finite square-exponential norm, and a separable closed span of countably many deterministic coefficient paths. Both phase entries are used; arbitrary p concerns operator norm.
- `L:driver-gain-localization`, LF169–237: each deterministic coefficient path has D_χ A_j=A_j=A_jD_χ, on both entries. The shrinking-cone support radius is2R+T; the extra1 in χ's plateau provides a margin. Statewise integrals use bounded strong free groups, not operator-norm continuity.
- `L:source-retaining-isometry`, source-convergence LF185–239, and `P:source-canonical-convergence`, LF256–360: one retaining product extension has actual I(Φh)=W(h), source Yρ(F)=I(QρΦF), and residual Dρ=W−Yρ. Qρ=CεPη has the given heat/Laplace-prefix normalization. Source and residual variances are bounded by the raw norm and the residual variance tends to0 at arbitrary relative ε,η rates. The heat residual need NOT be independent of the source.
- `P:source-gaussian-transfer`, LF44–134: with these joint centered Gaussian noises, the same deterministic A_j and correlated Yρ(f_j) produce M_Eρ→M_E in every finite Lp Cθ. Uniform source √p and square-exponential bounds hold. These are actual coupled variables, not just equal laws. Source evaluations are not assumed independent.
- `L:constant-phase-free`, constant-phase-young LF23–96: F is a separable Hilbert space with an injective continuous distributional interpretation, iE is closed/proper, Lψ:F→E is bounded, and S_F(t)(e,c1,c2)=(S(t)e,c1+tc2,c2) is a bounded strongly continuous group on finite horizons. Its finite propagation applies to TOTAL distributions, including local cancellation of e and constants.
- `L:source-pointfield-regularity` and `P:source-ordinary-response`, source-convergence LF364–482: for fixedρ, mYρ has one compact spatial support, spatial derivatives continuous with time, and finite sample derivative bounds. Its statewise ordinary interaction primitive equals M_Eρ on one all-state/all-time event for that fixedρ.
- The imported Banach Young estimate `E:constant-young-estimate` has θ>1/2 and bounded bilinear left composition. `P:constant-young-linear`, LF204–275, derives the actual linear equation, local stability and growth from it. We consume that ordinary Young estimate as an explicit imported theorem under matching hypotheses; this replay does not demand its re-proof. No commutation of integrator increments and integrands is used.
- `P:masked-source-moments`, masked-moments LF102–165: for fixedρ, the Picard sum is the unique locally continuous ordinary source solution. Its fixed-point L2 bound Q_t is uniform in space and widths; its spatial average is Bochner L2. `P:masked-canonical-transfer`, LF167–221, assumes precisely L2 convergence of that masked average and concludes its moment bound using the canonical unmasked point-moment limit. That premise will be supplied below, not assumed.

If Γ=0, M_E and every source/extended driver are0, all Young interaction flows areI, and the physical flow isS_F. The source solution is1 and the normalized average is1. Thus the zero case is direct. Continue with nonzero Γ without discarding the zero-case conclusions.

## Subaim1 — PROOF105: the actual F extension, both columns and its measurability

**Localization in the path norm.** On each deterministic A_j(·), the two localization identities hold as continuous operator paths. Finite sums preserve them for any coefficients, including correlated Yρ(f_j). The maps X↦D_χX−X and X↦XD_χ−X are bounded linear on Cθ(B(E)). Consequently their path-norm limits are0 in Lp, hence0 almost surely as paths. One raw event therefore carries both identities for every t and every E state. For each fixedρ, its source identities have such an event as well. This argument does not take an uncountable intersection overρ.

Define the deterministic bounded map

    Lψ(e,c1,c2)=(ψe1+c1ψ, ψe2+c2ψ) ∈E.

Boundedness follows from compact-smooth Sobolev multiplication on H^(±1/2) and the two fixed constant columns. On the localization event put

    A_E=M_E Lψ,   A=i A_E,
    A_Eρ=M_Eρ Lψ, Aρ=i A_Eρ.

For another admissible ψ′, D_χ(Lψ−Lψ′)=0: its two components are χ(ψ−ψ′)(e_k+c_k), which vanish as distributions since χ(ψ−ψ′)=0. Hence M_E(Lψ−Lψ′)=M_E D_χ(Lψ−Lψ′)=0. This proves ψ-independence on every state, without pretending E is dense in F. The same algebra works for each fixed sourceρ. In particular D_χDψ=D_χ, so

    A i=i M_E Dψ=iM_E,        π_C A=0.

The two constant-response columns are exactly

    A(0,1,0)=iM_E(ψ,0),
    A(0,0,1)=iM_E(0,ψ).

The second column is not dropped. Its free input has displacement r after time r, even though the instantaneous multiplication B(b)(u,v)=(0,bu) uses displacement only. These are columns of a compact operator F→F because M_E(t) is compact E→E and i,Lψ are bounded. There is no assertion that constants themselves lie in E.

**Norms, Gaussian nature and the given noise.** With Cψ=||Lψ|| and ||i||=1,

    ||Aρ−A||_{Lp Cθ(B(F))} ≤Cψ ||M_Eρ−M_E||_{Lp Cθ(B(E))} →0,
    ||Aρ||_{Lp Cθ}, ||A||_{Lp Cθ} ≤C sqrt(p).

For X equal to any one of these nonnegative driver norms, E X^(2n)≤C^(2n)(2n)^n. Since n!≥(n/e)^n,

    E exp(cX²) ≤1+∑_{n≥1}(2ecC²)^n <∞

for any sufficiently small c with2ecC²<1, uniformly overρ. This is a SUFFICIENT condition, not necessity or an optimal threshold.

All raw finite sums are functions of the actual W(f_j). The common separable closed path span of their deterministic coefficients gives a strongly measurable limit, hence M_E is measurable with respect to the completed σ-field generated by W. Bounded composition gives the same property for A. On the retaining extension it is exactly the pullback of this original variable; it does not acquire dependence on auxiliary J. Aρ may depend on J. Finite real Gaussian linear combinations and L2 functional limits show that A and Aρ are centered Gaussian driver paths, but their nonlinear solution flows below are not claimed Gaussian.

The source and raw drivers all take values in one separable closed path space obtained by applying X↦iXLψ to the countable deterministic path span. This controls Bochner measurability despite nonseparability of the full operator/Hölder ambient space. The conclusions concern each fixedρ and Lp equivalence classes; arbitrary-rate convergence needs no common path version for every positive pair of widths.

**Constant-column support test, needed for the ordinary join.** Let bρ(r)=mYρ(r). Define B_F(b)(e,c1,c2)=(0,b(e1+c1)) in E. Then

    ||B_F(b)||_(F→E) ≤||b||∞+||b||2,

using H^(1/2)⊂L2 and ||f||_Hminus≤||f||2. The total distributions of z and iLψz differ by(1−ψ)(e1+c1,e2+c2), zero on B_(2R+T+1). Full two-entry propagation therefore makes their free displacements equal on B_(2R) for0≤r≤T. This uses total distributional cancellation, not separate support assertions for its Sobolev and constant summands. Multiplication by bρ kills the difference.

For fixedρ, source regularity makes

    Cρ(r)=S(−r) B_F(bρ(r)) S_F(r) : F→E

strongly continuous on each state with a finite uniform operator bound. Its statewise Bochner integral is operator-norm Lipschitz, because

    ||∫_u^t Cρ(r)z dr||_E ≤|t−u| sup_r||Cρ(r)|| ||z||_F.

This does not require Cρ to be an operator-norm Bochner integrand or S to be norm continuous. Applying the actual ordinary E-response to Lψz and using the support equality gives

    A_Eρ(t)z=∫_0^t Cρ(r)z dr.

For the displacement constant column the integrand is S(−r)(0,bρ(r)); for the velocity constant column it is S(−r)(0,r bρ(r)). A dense countable set in F consists of a dense countable subset of iE together with rational constant coordinates. Fixed-ρ source identities at rational times, boundedness, and continuity extend to every state/time on one event. There is no use of the false assertion that the proper closed iE is dense in F.

## Subaim2 — PROOF108: measurable Young flows and the complete retaining-source limit

Write Δ_T={(t,s):0≤s≤t≤T}, X=Cθ_0([0,T];B(F)), and Y=C(Δ_T;B(F)) with uniform operator norm. The Young equation is

    U_D(t,s)=I+∫_s^t dD(r) U_D(r,s),

with increments acting on the LEFT. Its hypotheses hold for A,Aρ: paths start at0, θ>1/2, and multiplication in B(F) is bounded bilinear with constant1.

**Concrete stability on a driver ball.** Fix K≥1 and ||D||_Cθ,||D′||_Cθ≤K. Put cθ=2max(1,Cθ) and choose a piece length ℓ≤min(T,(4cθK)^(−1/θ)). On a piece use Nℓ(V)=sup||V||+ℓ^θ[V]_θ. The Young estimate gives

    Nℓ(I_D V)≤cθ K ℓ^θ Nℓ(V)≤Nℓ(V)/4.

Thus the local solution has Nℓ(V)≤2||V_a||. For W=V−V′, δ=||D−D′||_Cθ, subtraction and absorption give

    Nℓ(W)≤2||W_a||+2cθ ℓ^θ δ Nℓ(V′).

Use at most n_K pieces, with n_K depending only on K,T,θ and uniformly bounded for every start s. On piece j, Nℓ(V′)≤2^(j+1) for an identity initial operator. Induction gives

    E_j≤j 2^(j+1)cθ ℓ^θ δ,

where E_j is the endpoint difference. The same local estimate controls interior times. A sufficient finite Lipschitz constant is an enlargement of (n_K+1)2^(n_K+2)cθ ℓ^θ. Hence

    ||U_D−U_D′||_Y ≤L_K ||D−D′||_X,

uniformly on the ENTIRE time triangle, not merely for one start time. Choosing K=1+||D||_X makes n_K≤C_T(1+||D||_X^(1/θ)); multiplication of at most n_K factors bounded by2 gives the source growth bound

    ||U_D||_Y ≤C_T exp(C_T(1+||D||_X)^(1/θ)).

The displayed source bound is a conservative majorant. Local Young uniqueness and invertibility give the composition law and joint operator-norm continuity of U_D. No norm continuity of the free group is used in these estimates.

**Strong measurability and a genuine triangle supremum.** The random drivers belong almost surely to the separable closed X-subspace from Subaim1. The locally Lipschitz Young map is continuous there; the closure of its image is separable in Y, since the image of a countable dense set is dense in its image. Composition gives strongly measurable Y-valued U_A,U_Aρ. The triangle supremum is a measurable norm; for these norm-continuous triangle functions it may also be computed on a fixed countable dense triangle grid. No Gaussian cylindrical random vector in an operator space is postulated.

Applying π_C to the finite Young sums gives π_C(U_D−I)=0 for D=A,Aρ because π_C dD=0. As kerπ_C=iE is closed, (U_D−I)F⊂iE. These are pathwise operator identities on the construction event.

**Convergence in probability, without changing the coupling.** Let Xρ=||Aρ||_X, X0=||A||_X, and choose c0,H0>0 such that supρ E exp(c0 Xρ²), E exp(c0 X0²)≤H0. On the event Xρ,X0≤K, local Lipschitz stability applies. For ε>0 and any finite q≥1,

    P(||U_Aρ−U_A||_Y>ε)
      ≤2H0 exp(−c0K²)
        +(L_K/ε)^q E||Aρ−A||_X^q.

At fixed K the second term tends to0 at arbitrary relative source-width rates. Then K→∞ removes the first term. There is no independence requirement between raw, source and residual drivers, and no nonlinear covariance comparison is being used.

**Uniform moments and Lp convergence.** Put ν=1/θ<2. For every finite r and any c>0 there is a finite C_(r,c) with

    rC_T(1+x)^ν ≤ c x²+C_(r,c),   x≥0.

Indeed the ratio(1+x)^ν/x² tends to0 at infinity, and the remainder is bounded on a compact x interval. Taking c≤c0 proves supρ E||U_Aρ||_Y^r<∞ and E||U_A||_Y^r<∞ for every r. To make uniform integrability explicit, fix p and use r=2p. For Vρ=||U_Aρ−U_A||_Y and any ε>0,

    E Vρ^p ≤ε^p+(E Vρ^(2p))^(1/2) P(Vρ>ε)^(1/2).

The second factor tends to0 and its moment factor is uniformly bounded. Let ε↓0. Thus U_Aρ→U_A in every finite Lp(Y), the exact `E:constant-flow-limit`. The source square-exponential driver bound is the input; no square-exponential FLOW bound is inferred. The strict inequality1/θ<2 is essential to this particular argument.

**Physical conjugation and strong versus norm continuity.** Define

    P_D(t,s)=S_F(t)U_D(t,s)S_F(−s).

The deterministic map L:V↦[(t,s)↦S_F(t)V(t,s)S_F(−s)] is bounded linear from Y into B∞(Δ_T;B(F)), the Banach space of all bounded triangle families, with norm≤C_T². Its target need not be C(Δ_T;B(F)). Therefore L transfers strong measurability on separable ranges, every finite uniform moment, and Lp convergence without asserting that S_F is operator-norm continuous.

For each fixed state z, statewise joint continuity follows by splitting the difference into three terms:

    S_F(t_n)(U(t_n,s_n)−U(t,s))S_F(−s_n)z,
    S_F(t_n)U(t,s)(S_F(−s_n)−S_F(−s))z,
    (S_F(t_n)−S_F(t))U(t,s)S_F(−s)z.

The first tends to0 by norm continuity of U and bounded free groups, the second by strong continuity on z, and the third by strong continuity on one fixed vector. This is the precise continuity claimed. Group cancellation gives physical composition. The finite constant block J_t(c1,c2)=(c1+tc2,c2) and π_CU=π_C yield J_tJ_(−s)=J_(t−s), so both physical constants are retained. Finally

    P_A(t,s)−S_F(t−s)=S_F(t)(U_A(t,s)−I)S_F(−s)

has range in iE because S_F(t)iE=iE. Uniform Lp physical-flow convergence follows directly from the bounded map L.

**Deterministic shifts are a budget estimate, not a new noise law.** For a fixed real compact h as in111 and bounded real g, the deterministic primitive A_h is Lipschitz with a fixed budget H, and |g|≤G gives ||A_h+gA||_X≤H+G X0. The same holds for Aρ. If c′≤c0/(2(1+G²)),

    E exp(c′||A_h+gA||_X²)
      ≤exp(2c′H²) E exp(2c′G²X0²)<∞.

The difference is g(Aρ−A), so the preceding stability and integrability argument works uniformly on these displayed bounded budgets. The shift need not be centered Gaussian, and the flow is nonlinear; no Cameron-change-of-measure or distributional identity is used. The ordinary coefficient is h+gmYρ with one compact union of supports. Only h=0,g=1 enters the unshifted original-point comparison below. This context is not a full new replay/acceptance of111.

## Subaim3 — PROOF109/110: the actual ordinary-source phase and the raw average

Fix oneρ and intersect its source regularity, retaining-response and path-construction events. All reasoning in this subaim is then deterministic on that event until expectations are taken. One may intersect again over any prescribed countable source sequence, never over all positiveρ.

**Young sums become a statewise Bochner integral.** The primitive A_Eρ has increments ∫Cρ(r)dr. For fixed s,z and a partition, its Young sum is

    ∑_j ∫_(t_j)^(t_(j+1)) iCρ(r)U_Aρ(t_j,s)z dr.

The difference from ∫_s^t iCρ(r)U_Aρ(r,s)zdr is at most

    (t−s) sup_r||Cρ(r)|| · ω_U(mesh) ||z||,

where ω_U is the operator-norm time modulus of U on the compact triangle. It tends to0. The ordinary integral is a Bochner F integral on states: Cρ is strongly continuous on fixed states, uniformly bounded, and U is norm continuous, so their product applied to z is continuous. There is no need for time Hölder regularity of Cρ or an operator-norm derivative of S_F.

Multiplication by S_F(t) gives the F-valued Duhamel equation. For e0 at time0 its free part is S_F(t)e0=e0. With B_T=sup_r||B_F(bρ(r))|| and C_T≥max(1,sup_|r|≤T||S_F(r)||), define W0(t)=e0 and

    W_n(t)=∫_0^t S_F(t−r)iB_F(bρ(r))W_(n−1)(r)dr.

Induction on the ordered simplex gives sup_t||W_n(t)||≤C_T^(n+1)B_T^nT^n/n!. The sum converges in C([0,T];F). The integral map is bounded there by C_TB_TT, so the sum satisfies Duhamel. Iterating the difference equation between two solutions gives the same factorial estimate times their finite sup norm, tending to0. Thus it is the unique continuous F phase. This is ordinary bounded-coefficient uniqueness, not an invented uniqueness theorem for a rough SPDE.

**Phase-to-scalar identification is by tests, not point traces.** Let X0=1 and X_n(t)=∫_0^t G_d(t−r)*(bρ(r)X_(n−1)(r))dr. At each fixed n the scalar term is continuous in time, smooth in space; compact support of b and finitely many bounded derivatives permit induction using the positive finite Green measures of mass t−r. If W_(n−1)'s displacement is X_(n−1), its forcing is(0,f_r) with f_r=bρ(r)X_(n−1)(r), one compact support and continuous L1 norm. For every compact smooth φ, bounded distributional testing of the phase Bochner integral gives

    <[W_n(t)]_1,φ>
      =∫_0^t∫ f_r(y)∫G_d(t−r,dz)φ(y+z)dy dr
      =<X_n(t),φ>.

Absolute Fubini is justified by ||φ||∞||f_r||1(t−r), integrable on the horizon. This includes the d3 sphere measure; no Green density is needed. The scalar recursion is exactly the chronological source Picard chain with its physical mask at every vertex. The local compact-cone bound M^nT^(2n)/(2n)! gives locally uniform scalar convergence to uρm, while the phase series converges in F and hence as distributions. Their displacement distributions agree. This proves109's version identification without evaluating an H^(1/2) state at a point.

The constructions can be unified with countable dense test families, rational/dyadic times and all integer orders; boundedness, distributional testing and continuity then give all tests/times on the fixed-ρ event. Alternatively the coefficient-by-coefficient argument is a deterministic identity once a regular coefficient sample is fixed. Neither route requires E to be dense in F. The original scalar versions at each fixed point are the same L2 classes supplied by `P:masked-source-moments`.

**Scalar and Bochner spatial averages are the same variable.** Fix t and φ≥0 in Cc∞ with integral1. The displacement observable

    Oφ(e,c1,c2)=<e1,φ>+c1

is bounded with norm≤sqrt(||φ||²_Hminus+1). It sees the constant displacement, and no c2 term at the observation instant. By108, OφP_Aρ(t,0)e0 converges in every Lp to Z_m(t,φ)=OφP_A(t,0)e0, since its difference is bounded by ||Oφ||||e0|| times the uniform physical-flow difference. Z_m is measurable with respect to the given W alone by the raw construction and the measurable Young/deterministic maps; it is not a function of auxiliary J.

For precision, compare the ordinary spatial integral to the previously defined Bochner L2 average. The map x↦uρm(t,x) is L2-continuous by finite-chain source continuity and uniform q_n tails, has separable L2 image on suppφ, and has norm≤Q_t. Thus its Bochner integral Bφ exists. The continuous scalar solution version is jointly measurable in(ω,x): approximate x by rational grids, use measurability at countably many grid points and path continuity. It agrees with the L2 variable at each fixed x; no all-x null-set identification is necessary for the following Fubini argument.

Its ordinary integral Cφ is integrable because

    E∫|φ(x)uρm(t,x)|dx≤Q_t||φ||1.

Weighted Cauchy–Schwarz gives E|Cφ|²≤Q_t²||φ||1². For any bounded real random variable Ξ, the continuous L2 functional V↦E[ΞV] commutes with the Bochner integral. Absolute scalar Fubini therefore gives

    E[ΞBφ]=∫φ(x)E[Ξuρm(t,x)]dx=E[ΞCφ].

Choose Ξ=sign(Bφ−Cφ), legitimate since both are real L2 variables. Then E|Bφ−Cφ|=0. Thus the phase observable, ordinary scalar integral and Bochner L2 average are exactly the same variable for this fixedρ and t. Norm convergence of phases consequently supplies the actual L2 premise of `P:masked-canonical-transfer`.

That local proposition now applies with φ≥0, ||φ||1=1, fixed mask and horizon, both widths tending to0 at arbitrary relative rates, and the same original covariance/canonical solution. It gives

    E|Z_m(t,φ)|²≤E|u(t,0)|².

The comparison is the SECOND MOMENT OF A SPATIAL AVERAGE. It is not an equality with an average of pointwise second moments. Masked stationarity is not assumed, a rough-state point trace is not used, and the unmasked canonical point-moment limit remains the named earlier input (its mixed/unequal/self/empty-chain content is not erased). Source limits are taken before large-time asymptotics. No matching first-moment or Chen-constant claim follows here.

## Status and remaining obligations

The replay exposes105's two constant columns, support/localization and strong measurability;108's exact driver-ball probability estimate, uniform integrability, triangle supremum and strong physical continuity; and109/110's statewise integral, Picard/distribution and scalar-versus-Bochner joins. No genuine omitted OWN step or false source statement was found in these arguments. The required local driver/source/masked theorems remain explicitly named premises; the imported bounded-bilinear Young estimate is not a missing local theorem merely because it is cited.

This is author evidence for later targeted depth review, not independent verification or acceptance. Remaining evidential work is to independently audit these expanded steps and their exact consumed interfaces if required by root, while retaining the new MAIN LIMITED rows, the older bounded MEDIUM report, source-image/global/cold obligations and all original-model scope. No automatic review, grade upgrade, source change, simultaneous uncountable-parameter event, global-radius estimate, arbitrary Schatten path claim, or Skorohod/Lean conclusion is supplied.
