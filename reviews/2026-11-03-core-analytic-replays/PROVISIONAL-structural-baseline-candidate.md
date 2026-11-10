# Candidate: compact Young perturbations of the free E wave

This is an author-side proof-simplification candidate at scientific source `8ce03ae09cca984b32aaddf3da0a6ded07f47ebc`. It is not adoption, a new goal, a source amendment or an independent review. The original Γ class, dimensions, covariance amplitude, positive-control class and C2 objective remain unchanged. The main norm-only argument below is independent of symplectic conservation; a separate real Young-Lie proof of conservation is given afterwards.

## 1. Exact phase and Young hypotheses

Work on the nonzero infinite-dimensional real Hilbert phase

    E=H^(1/2)(R^d)×H^(−1/2)(R^d),       d∈{1,2,3},

with the actual inhomogeneous Bessel norm. Fix finite T and θ>1/2. Let X∈C^θ([0,T];K(E)) start atzero, where K(E) has the operator norm. Source107's Banach-algebra Young construction applies directly on L(E), with left order

    U_X(t,s)=I+∫_s^t dX(r)U_X(r,s).

It supplies operator-norm Young integration, bounded C^θ terminal trajectories, composition and actual invertibility from local Neumann pieces. No Gaussian, Hamiltonian or positivity property is needed for the norm-only argument. Nor is a bounded norm of X independent of any model parameter needed.

The physical free group is S_E(t), the actual massless wave on both phase entries. It is bounded on each finite horizon and strongly continuous. Neither its operator-norm continuity nor an operator-norm generator derivative is assumed.

## 2. The Young perturbation is compact at every endpoint

Every increment X(v)−X(u) is compact. Every left Young sum

    Σ_[u,v] (X(v)−X(u))U_X(u,s)

is a finite sum of products compact×bounded, hence compact. Its limit in operator norm is the Young integral. Since K(E) is operator-norm closed,

    U_X(t,s)−I∈K(E),       every0≤s≤t≤T.                    (2.1)

The proof needs compact-valued increments and norm convergence of the Young sums; convergence on states alone would not suffice. There is no claim of a uniform compact approximation as R,T or the number of blocks grows.

Consequently

    S_E(t)U_X(t,s)S_E(−s)−S_E(t−s)
       =S_E(t)(U_X(t,s)−I)S_E(−s)∈K(E).                   (2.2)

Only bounded composition with fixed free factors was used.

## 3. Translation proves the exact free-norm lower bound

Let τ_y act on both phase entries by translation. It is an isometry on E and commutes with S_E(t), because translation commutes with the Bessel weights and the full wave Fourier matrix. For any z,w∈E,

    〈τ_yz,w〉_E=∫exp(−iξ·y)f_(z,w)(ξ)dξ,

where f_(z,w)∈L¹ by weighted L² Cauchy–Schwarz. Riemann–Lebesgue gives τ_yz⇀0 as|y|→∞. Compactness then implies||Kτ_yz||→0 for every fixed compact K: a nonzero-norm subsequence would have a norm-convergent compact-image subsequence, whose weak limit must beK0=0, a contradiction.

For every unit z and fixed free time t,

    ||S_E(t)+K||≥liminf_(|y|→∞)||(S_E(t)+K)τ_yz||
                 ≥||S_E(t)z||.

Taking the supremum over z gives

    ||S_E(t)+K||≥||S_E(t)||.                                (3.1)

This is an infinite-Rd translation argument. It is not a theorem that arbitrary compact perturbations cannot reduce arbitrary operator norms.

For the second inequality define the isometric velocity reversal J_vel(u,v)=(u,−v). The full free matrix gives S_E(−t)=J_vel S_E(t)J_vel. The group law therefore yields

    1=||I||≤||S_E(−t)|| ||S_E(t)||=||S_E(t)||².

Thus, combining(2.2)–(3.1),

    ||S_E(t)U_X(t,s)S_E(−s)||≥||S_E(t−s)||≥1.               (3.2)

The lower constantone is exact and independent of the compact perturbation norm. It remains valid when the covariance iszero, with the free phase unchanged. Atzero time the endpoint isI.

## 4. Finite block products need no restart or Hamiltonian hypothesis for this bound

Let ℓ_m≥0 and x_m∈C^θ([0,B];K(E)), x_m(0)=0, for finitely many indices. Put P_m=S_E(ℓ_m)U_(x_m)(ℓ_m,0). By(2.1), P_m=S_E(ℓ_m)+K_m with compact K_m. The algebraic telescoping difference of the ordered product and the free ordered product is a finite sum of bounded×compact×bounded terms. No factors need commute. The FREE factors multiply by the group law, giving

    P_N⋯P_0−S_E(Σ_mℓ_m)∈K(E),
    ||P_N⋯P_0||≥||S_E(Σ_mℓ_m)||≥1.                         (4.1)

This is pointwise at every fixed finite partition, even when its number of factors depends on a fixed δ. No convergence uniform in N or δ is used. An empty last interval gives P_N=I exactly.

In source173/174 the ambient space itself is a finite product of little C^θ compact-operator paths. Thus(4.1) applies to EVERY tuple in that ambient space, not only the actual Gaussian input. It would permit the equality

    2δlog max(1,||P_N⋯P_0||)=2δlog||P_N⋯P_0||

throughout that precise compact-path domain. It does not justify removing max from a generic extension to arbitrary L(E)-valued residual paths. Keeping the current max definition remains harmless and robust.

## 5. Actual source inputs satisfy the compactness hypotheses at fixed parameters

**Raw and transferred drivers.** Source093 constructs the real M_R as a C^θ path limit of compact-valued finite coefficient paths, with compact values at all times on one event. Source095 constructs actual covariance-contracted source/block drivers with the same coefficients. Stopping preserves compact values and C^θ regularity. Therefore every fixed-parameter actual tube tuple173 satisfies section4 on its existing path event. No block independence is required.

**Covariance means.** For a real Φ∈H_W, Z=W(Φ) and D_Φ=E[ZM_R] are Bochner defined because

    E||ZM_R||_(C^θ)≤||Φ||_(H_W)||M_R||_(L²C^θ)<∞.

The closed path subspace C^θ([0,T];K(E)) is preserved by this Bochner expectation. Thus D_Φ is compact-valued with zero start. The path is deterministic for each Φ. This uses finite fixed-R,T moments, not a uniform growing-R tail or a pointwise rough potential.

**Completed block means.** For every real Φ∈H_I, the actual E completed field Tcal_RΦ belongs to L^r(I;K(E)) by143/146 and its E compression, with r>(1−θ)^(−1). Compact conjugation by the strongly continuous free group and its adjoint is norm continuous on compact operators. Hence

    H_m(u)=∫_0^min(u,ℓ_m)
           S_E(−v)Tcal_RΦ(s_m+δv)S_E(v)dv

is a genuine compact-operator Bochner primitive. Its exponent1−1/r>θ gives C^θ regularity, zero start and constant extension afterℓ_m. Every Φ has finite Hilbert norm; its local primitive bound is C_Bδ^(−1/r)||Tcal_RΦ||_(L^r(I_m)). No positivity or smoothness of Φ is required. Compactness of the CONTROL MAP is stronger than needed here: compact operator VALUES of this primitive suffice.

These are fixed-R/fixed-horizon statements. At R=δ^(−1)+2 each δ instance still has finite radius/horizon; section3 needs no uniform compact approximations, rates or tail decay. It does not replace093's operator/path existence,173's Gaussian law/support eligibility or the separate stochastic expected-norm anchor.

The quantitative work remains on E. Range in iE does not annihilate constant INPUT columns on F, and there is no reverse E→F norm lift. The present translation proof does not assert a corresponding full-F free-norm identity: translations of constant coordinates are not weakly null.

## 6. Exact source consumers and what can actually shorten

At source8ce the potential replacement points are:

- **169 `P:symplectic-block-mean`**, `integrated_symplectic_phase.tex`, proof306–382, especially its final application of168 at371–379. Its norm-only conclusion follows directly from compact H_m and(3.2) without representing H_m as a fast covariance direction or invoking source conservation. Its OTHER asserted equality D_(φ_m)(stopped)=H_m remains substantive and is not proved by compactness.
- **174 `L:tube-actual-endpoint`**, `integrated_gaussian_tubes.tex`, proof375–412, final invocation of168 at405–410. The norm baseline for the ordered product follows from(4.1). Its identification of that product with the actual global endpoint still needs the existing raw restart/coupling argument124. Compactness proves no restart identity.
- **181 `L:uniform-product-budgets`**, `integrated_uniform_products.tex`, proof346–388, final use of169 at376–387. For pure completed means compact H_m and(3.2) give the denominator baseline directly. Its explicit C_B/C_gr and primitive budgets are unchanged. The generic growth statement for arbitrary L(E)-valued D remains generic, with no norm baseline inferred there.

For169 retain all scale and domain checks even if its final norm line is shortened. T_m:H_fast→H_W is an isometric embedding and T_m* a contraction, so

    φ_m=δ^(−a/2)T_m*i_IΦ,
    ||φ_m||≤δ^(−a/2)||Φ||_(H_I)<∞    at fixedδ.

The unscaled covariance identity is E[M_m W(i_IΦ)]=δ^(a/2)H_m. Multiplying by g_δ=δ^((1−a)/2) produces sqrt(δ)H_m. These are distinct identities; compactness or a norm lower bound cannot determine which scale is correct. The original action remains one global raw H_I norm, not a sum of independent block costs. No new covariance/action calibration follows from(3.2).

Likewise this candidate does not prove173's supported labels, mean-map compactness, abstract Wiener realization, expected Gaussian radius or exact Rayleigh half action. Those remain their own claims. It only removes a stronger conservation theorem from the dependency of three norm-only uses.

## 7. Optional localization proof of the same baseline

Suppose an actual interaction driver also has X(t)=X(t)D_χ on the whole fixed horizon, as in the existing right localization for M_R. For a fixed state z with D_χz=0, the constant interaction trajectoryV(r)=z solves its Young state equation because every increment of X annihilates z. Uniqueness gives U_X(t,s)z=z. This does not require D_χ to be self-adjoint or a projection.

Choose a compact smooth TWO-ENTRY physical phase z. For a general initial time s, S_E(−s)z still has compact support in a finite enlargement by full forward/backward propagation of displacement AND velocity. A sufficiently distant translate satisfies D_χτ_y S_E(−s)z=0. Since translations commute with S_E,

    P_X(t,s)τ_yz=S_E(t−s)τ_yz

exactly for these far data. Compact smooth phases are dense in E, so taking their normalized suprema proves the same free-norm baseline. This alternative uses actual right localization, not an assertion that every compact operator localizes. For a covariance mean, right localization passes through the bounded Bochner expectation; for a completed mean primitive it can pass from smooth controls through the existing bounded primitive completion at fixed parameters. The compact perturbation proof is shorter when compact-valued path existence is already available.

## 8. Separate direct REAL Young-Lie proof for168

Compactness alone does NOT prove P*J_EP=J_E. To obtain that stronger identity use the actual real bounded symplectic operator

    J_E(f,g)=(Λ^(−1)g,−Λf),
    J_E*=−J_E, J_E²=−I, ||J_E||=1,
    g_J={A∈L(E real):A*J_E+J_EA=0}.

This is a closed REAL linear subspace. Source165's balanced Fourier calculation verifies S_E(t)*J_ES_E(t)=J_E. For every real smooth bounded h, the actual force B(h) obeys B(h)*J_E+J_EB(h)=0 by the physical cancellation−∫fhu+∫uhf=0.

For source093's actual real test-noise basis, the covariance coefficient H_(j,R)(r,x) is real smooth compact. Therefore C_j(r)=S_E(−r)B(H_(j,R)(r))S_E(r) is J-skew by free conservation. Its statewise integral A_j(0,t) is J-skew: integrate the bounded scalar identity on each pair of states. This needs no operator-norm derivative of S_E. Every finite Gaussian sum Σ_j g_jA_j is J-skew since g_j is real. Its actual C^θ path limit M_R stays in the closed J-skew path subspace on one event for the fixed R,T; a uniformly convergent subsequence or the continuous map A↦A*J_E+J_EA proves this for ALL times.

For real Φ∈H_W the Bochner covariance D_Φ=E[W(Φ)M_R] stays in the same closed real linear path subspace by the finite norm bound in section5. Thus cM_R+D_Φ is J-skew-valued for every fixed real c,Φ, with no pointwise raw potential, no Φ positivity and no source smoothing needed in this step. The same coefficient argument also works for actual real transferred sources, whose coefficients may be correlated.

Now let any fixed real C^θ path D start atzero and have increments in g_J. Source107 gives U=U_D. On a subinterval[u,v], Young's remainder has

    ΔU=D_(u,v)U(u,s)+R_(u,v),
    ||R_(u,v)||≤C_θ[D]_θ[U]_θ|v−u|^(2θ).

Expand the exact increment of U*J_EU. Its first-order term is

    U(u,s)*[D_(u,v)*J_E+J_ED_(u,v)]U(u,s)=0.

The remaining two linear R terms and the quadratic ΔU term have norm at most C|v−u|^(2θ), with a finite constant at this fixed path/horizon. Summing on any partition gives a bound C(t−s)mesh^(2θ−1)→0. Consequently U_D(t,s)*J_EU_D(t,s)=J_E. Free conjugation gives the actual physical identity P_D(t,s)*J_EP_D(t,s)=J_E for all time pairs, deterministically for this path. For the stochastic driver the fixed-parameter J-skew path event already handles every state and time; there is no new uncountable intersection.

Invertibility still comes from107's short Young Neumann pieces and finite products, NOT from the identity alone. A symplectic isometric embedding need not be onto in infinite dimension. Norm≥1 follows from this stronger identity as before, but is already available from the structurally weaker compact argument.

This is a possible shorter proof of168's conservation statement from the actual coefficient/path construction. It does not establish or delete166's explicit source-mean primitive,167's ordinary source statement, Gaussian flow moments, source convergence, or the E/F intertwining wherever those are independently required. Any implementation would need its own source/application review; no manuscript proof is removed here.

## 9. Falsification and limits of the candidate

1. In finite dimensions every matrix is compact. With S=I and X(t)=−tI, U=e^(−t)I has norm<1. Thus “compact perturbation implies norm≥free norm” is false without the actual infinite-Rd translation hypothesis. Even on an abstract infinite Hilbert space, S=diag(2,1,1,…) and compact K=diag(−1,0,0,…) reduce norm2 to1; commutation with a weakly-null translation family is essential to(3.1).

2. On the actual E, the noncompact X(t)=−tI gives P(1,0)=e^(−1)S_E(1). The valid free Frobenius estimate is||S_E(1)||≤sqrt5<e, so this endpoint contracts. General noncompact residual paths must retain the max in a robust envelope.

3. Compactness does not imply conservation. Let q=(φ,0),p=(0,Λφ) with real compact smooth||φ||_(H^(1/2))=1. They are E-orthonormal and ω(q,p)=1. For the compact rank-one driver X(t)=−tP_q, Uq=e^(−t)q and Up=p, so ω(Uq,Up)=e^(−t)≠1. Nevertheless the infinite-space norm baseline still follows from sections2–3.

4. Arbitrary phase compression need not preserve J-skewness. On R4 with J4=[[0,I2],[−I2,0]], A=diag(I2,−I2) satisfies AᵀJ4+J4A=0. Compressing to the first two position coordinates gives I2, for which I2ᵀJ2+J2I2=2J2≠0. These exact finite matrices were recomputed locally. The actual direct Lie argument instead checks the physical E coefficients themselves.

5. A complex coefficient cannot be treated as a real Lie coefficient. For B(b)=[[0,0],[b,0]], B(b)*J2+J2B(b)=diag(b−overline(b),0). It vanishes for real b but not b=i. The actual W,basis coefficients,c and Φ above are real; complexification is not an independent complex-noise coupling argument.

6. The physical S_E group is not norm continuous atzero. The proofs use its strong continuity, finite-horizon bounds, translation commutation and (for means) compact conjugation, never norm continuity.

The candidate gives an actual simplification of the NORM-only dependencies169/174/181, conditional on their already stated compact-path/mean inputs. The optional direct Young-Lie argument provides conservation separately. It changes no original Γ model, scale, Gaussian action, variational domain or constant claim. It provides no whole-paper, image or cold-reading clearance and no Skorohod/sibling result.

Exact current source fingerprints checked against `git show 8ce03ae…`: `integrated_symplectic_phase.tex`=`8a570afa0b1d2d95ab26cb92d8f7700520598056e48e865b6c492105153d16be`; `integrated_gaussian_tubes.tex`=`b1dd4e41c4c5c6ca12e81482694b5b5a2af2cdbf98a56aa91ea6288a03a98598`; `integrated_uniform_products.tex`=`5c03545c565dee67266226ec11e272cd20628dcc5e586b0ea268f9c3b0f77ca5`. All paths are under `notes/`. This candidate file is the only persistent output of the exploration; no Article/Git/provider/packet files were changed.
