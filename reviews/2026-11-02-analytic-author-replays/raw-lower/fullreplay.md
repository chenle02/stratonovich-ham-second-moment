# Expanded author replay of PROOF125–126

This derives the fixed-control lower rate from the stated local construction results, including the probability estimate. It is an external author expansion of the existing argument, not an independent review, a provider retry, a MAIN coverage upgrade, or an Article edit. Scientific source is `b4b6efccacbbccd8f747225330e9ccb27bc097a6`; exact current/source bindings accompany this file.

Write a=α₀, κ=(4−α−a)/(3−α), with every original admissible d∈{1,2,3}, homogeneous nonnegative covariance Γ and original amplitude. Assume Γ≠0. Fix a nonzero nonnegative real Ψ∈C_c∞((0,1)×Rᵈ), without a separability assumption. Its original slow-noise variable, mean and cost are

    Z=W(Ψ),       v=EZ²=∫Ψ(s,x)h_s(x) dx ds>0,
    h_s(x)=∫₀¹ |s−t|^(−a)(Γ*Ψ_t)(x) dt.

All of these remain fixed throughout the block/source/asymptotic construction. Pick an eligible finite even mask 0≤m_R≤1, equal to1 on B_R and zero off B_2R, and put V_s=m_Rh_s. Let λ_s be the positive growing rate of −Δ−V_s, and I_R=∫₀¹λ_s ds. The desired conclusion is

    liminf_(T→∞) T^(−κ) log E|u(T,x)|² ≥ 2I_R−v/2.       (A)

The rate uses kinetic coefficient1, and the action will be exactly half the ORIGINAL raw variance.

## Local inputs and their exact roles

The source files are retained under `source/notes/`.

| Local input | Pinpoint | Statement consumed |
|---|---|---|
| Original mean and eligible mask | `integrated_compact_mean_family.tex:445`, L:compact-raw-profile;515, P:compact-original-common-trial | The above v is finite positive; V_s is compact smooth and Lipschitz in s in L∞ and L²; a sufficiently large fixed mask gives a common negative H¹ trial. Thus λ_s is Lipschitz and bounded below by a positive constant. |
| Full F growing projection and complement | same file:289, P:compact-F-projection;379, P:compact-F-complement | On F=E⊕R², E=H¹ᐟ²×H⁻¹ᐟ², P_s(t)Π_s=e^(λ_st)Π_s, Π_s=e_sℓ_s, ℓ_s(e_s)=1. The families e_s,ℓ_s,Π_s are norm-continuous; infℓ_s(e₀)>0 and inf O_φ(e_s)>0. The normalized complement is ≤C_gap e^(−η_gap t), uniformly in s,t≥0. Constants and velocity remain in F. |
| Actual given-noise drivers and sources | `integrated_actual_operator_driver.tex`, P:actual-operator-driver; `integrated_source_convergence.tex`, P:source-gaussian-transfer and P:source-ordinary-response | Actual first drivers are centered first-chaos operator paths, with Cθ moments C√p and source limits on the same retained W; ordinary positive-width sources have the stated covariance and primitive. |
| Everywhere-defined Young map and physical interpretation | `integrated_constant_phase_young.tex:204`, P:constant-young-linear;278, P:constant-gaussian-flow;342, L:constant-source-solution | For θ>1/2, every Cθ driver has a continuous locally Lipschitz left Young evolution, with growth exp(C(1+‖D‖)^(1/θ)); source flows converge in every finite Lᵖ on fixed horizons. Positive-width physical flows solve the actual ordinary masked wave equation with data e₀=(0,1,0). |
| Masked expected-square comparison | `integrated_masked_moments.tex:24,103,168` | Positive Green measures and nonnegative covariance give entrywise Wick comparison after inserting factors m_R∈[0,1]. Canonical unmasked second moments are source limits. Any constructed L² masked-average limit inherits the comparison. |
| Exact canonical scaling | `integrated_exact_scaling.tex:4`, L:exact-canonical-scaling | At δ=T^(−κ), the canonical semiscaled equation δ²V_tt=ΔV+√δ W V has E|V_δ(1,0)|²=E|u(T,0)|². |

These are genuine local imported statements with supplied proof bodies. The compact spectral input ultimately uses the explicitly stated Teschl theorems; Young integration uses the bounded-bilinear Young estimate. Reproving those external theorems is not required to replay their particular local applications here. No intrinsic-limit theorem or target lower conclusion is an input.

## 1. Actual coupled blocks and exact shift

Fix an integer B≥1, later chosen by the deterministic cone. For 0<δ<min(1,1/B), define

    N=floor(1/(δB)),  s_m=mδB,  τ=δ⁻¹−NB∈[0,B),
    g_δ=δ^((1−a)/2),  0≤m≤N.

The raw pullback T_m f(s,x)=δ^(a/2−1)f((s−s_m)/δ,x) has covariance multiplier δ^(a−2)δ²δ^(−a)=1. It is therefore an isometry through the covariance-null quotient. Set W_m(f)=W(T_mf) and W_fast=W_0; these are coupled restrictions of the SAME original W, not independent block noises.

Let A_R(W_m) be the actual full-F interaction driver, and put

    X_m=g_δ A_R(W_m),
    H_m(u)=∫₀ᵘ S_F(−r)iB_F(V_(s_m+δr))S_F(r) dr.

Means are smooth on the slightly extended slow interval[0,2], so this is defined for all u≤B even for the last block. The covariance calculation on actual raw tests is

    E[W_m(f)Z]=δ^(a/2)∫ f(u,x)h_(s_m+δu)(x) dx du.

The actual source/driver row identification, then bounded extension to both constant columns, yields

    E[X_m Z]=g_δ δ^(a/2)H_m=√δ H_m.                    (1)

Thus the vector (X,Z) is jointly centered Gaussian on the separable norm-Borel space B_δ=(h₀θ([0,B];K(F)))^(N+1). Its deterministic covariance vector b=E[XZ] is √δH. The same Ψ,Z,v occur in every coordinate and every δ.

For completeness, tilt by exp(−tZ−t²v/2). On any finite list of continuous path coordinates, represent the jointly Gaussian vector as (AG,z·G), allowing singular covariance, with G standard and Az equal to the coordinate covariance with Z. Substituting G'=G+tz in the Gaussian density shows that X+tb under the tilt has the original law of X. Countable matrix coordinates at rational times generate the entire norm-Borel field: the operator norm is a supremum over a countable dense set of unit-state pairs; the Hölder norm is a supremum over rational time pairs; separability then makes open sets countable unions of measurable balls. A generating-cylinder/monotone-class argument therefore extends the law identity to every nonnegative norm-Borel function j. With t=δ^(−1/2), (1) gives

    E j(X)=E[ exp(−Z/√δ−v/(2δ)) j(X+H) ].              (2)

This is exact, including extended nonnegative integrals. The cost is v/(2δ), not v/δ. No independence and no Hilbert-valued Gaussian random vector are used. This is P:raw-block-gaussian-law, raw source129–176, with its Gaussian step written out.

## 2. Vanishing block errors and an explicit event probability

Define D_x(u)=S_F(u)U_x(u,0), D_m⁰=D_(X_m), D_m⁺=D_(X_m+H_m). At fixed R,B,Ψ and admissible θ, the given driver moments give, for any p≥1,

    ‖max_m‖X_m‖_Cθ‖_p
      ≤(N+1)^(1/p) C_R,B √p g_δ
      ≤C'_R,B √p δ^((1−a)/2−1/p).                    (3)

The first inequality uses max x_m^p≤Σx_m^p, not independence. Write M_δ=max_m‖X_m‖. For a fixed p>2/(1−a), set γ=p(1−a)/2−1>0. Markov gives the concrete bound

    P(M_δ>η)≤A_p η^(−p) δ^γ,                         (4)

with a finite constant independent of small δ at these fixed data.

Freeze the deterministic potential on block m at V_(s_m). Its primitive H_m^stat and H_m have uniformly bounded Cθ norm H₀. The potential difference on u≤B is ≤CδB in L∞ and L²; statewise integration against bounded finite-horizon free groups gives ‖H_m−H_m^stat‖_Cθ≤C_Bδ. Young stability on the ball of radius H₀+1 therefore implies, on M_δ≤1,

    E_op,δ:=max_m sup_(u≤B)‖D_m⁺(u)−P_(s_m)(u)‖
          ≤L_B(M_δ+δ).                               (5)

This comparison freezes only the deterministic mean; it does not discard the residual noise. For any fixed cone tolerance ε_op>0, choose η=min(1,ε_op/(2L_B)) and δ≤ε_op/(2L_B). Then M_δ≤η implies E_op,δ≤ε_op. Combining (4) with EZ²=v gives, for

    E_δ={E_op,δ≤ε_op} ∩ {|Z|≤δ^(−1/4)},

    p_δ:=P(E_δ)≥1−A_p η^(−p)δ^γ−vδ^(1/2)→1.          (6)

All suprema are norm-Borel by the separable path construction (or countable dense state/rational-time testing of the physical differences). This is a union bound on the actual coupled space; E_op,δ and Z need not be independent. No exponential small-ball estimate is necessary.

The stronger all-finite-Lᵖ convergence stated in L:raw-block-uniform-error follows by its uniform square-exponential maximum estimate and the Young growth exponent1/θ<2. For (6), the elementary polynomial estimate (4) already suffices.

## 3. Deterministic cone, including entrance and terminal remainder

Here are the budgets behind L:raw-block-indexed-cone (raw source256–373), rather than treating the cone as multiplication of scalar moments. Let

    a_*=inf_s ℓ_s(e₀)>0,  j_*=inf_s O_φ(e_s)>0,
    M_e=max(1,sup‖e_s‖), M_ℓ=max(1,sup‖ℓ_s‖),
    M_P=max(1,sup‖Π_s‖), M_Q=1+M_P, M_z=M_e+1,
    E₀=‖e₀‖=1, H_obs=max(1,‖O_φ‖).

Fix 0<ρ<1/2. Set aperture θ_c=min(1,j_*/(16H_obs C_gap)). Choose integer B large enough that

    q_B=C_gap exp(−η_gap B)
       ≤min(1/8, θ_c a_*/(8M_QE₀)).

Choose ν>0 with νM_z≤min(ρ/2,θ_c,1/4), then index separation ω>0 so that |b−c|≤ω implies both ‖ℓ_b−ℓ_c‖ and ‖Π_b−Π_c‖ are ≤ν. Finally choose ε_op>0 so

    M_ℓ ε_op M_z≤ρ/2,       M_Q ε_op M_z≤θ_c/4,
    M_ℓ ε_op E₀≤a_*/2,      M_Q ε_op E₀≤θ_c a_*/8,
    H_obs ε_op M_z≤j_*/8.                             (7)

All are compatible because every margin is positive. The cone at b consists of z=Ae_b+r, A=ℓ_b(z)>0, ℓ_b(r)=0, ‖r‖≤θ_c A; hence ‖z‖≤M_z A.

Entrance: for z₁=D₀(B)e₀, the normalized amplitude is ≥a_*−M_ℓ ε_op E₀≥a_*/2. The normalized residual is ≤q_BM_QE₀+M_Q ε_op E₀≤θ_c a_*/4. Thus z₁ enters the cone with amplitude ≥e^(λ_(s₀)B)a_*/2 and residual ratio≤θ_c/2. This uses the full-F positive coefficient ℓ_s(e₀), including the growing response to constant displacement. Dropping constant columns would destroy this entrance argument.

Rebase before each subsequent block. For adjacent b,c,

    ℓ_c(z)≥(1−νM_z)A,
    ‖Q_cz‖≤(θ_c+νM_z)A.

The old residual is not assumed to be in the new kernel. For D close to P_c(B), write x=e^(−λ_cB)ℓ_c(Dz), y=e^(−λ_cB)‖Q_cDz‖. The projection identity and (7) give

    x≥(1−νM_z−M_ℓε_opM_z)A≥(1−ρ)A>A/2,
    y≤[q_B(θ_c+νM_z)+M_Qε_opM_z]A≤θ_c A/2≤θ_c x.

Thus the new cone is preserved and amplitude multiplies by at least (1−ρ)e^(λ_cB). This is an operator/state induction retaining displacement AND velocity, not a stochastic product factorization.

For the final interval u∈[0,B], rebase to c=s_N. Then ℓ_c(z)≥3A/4 and ‖Q_cz‖≤2θ_c A. The normalized complement bound holds even at u=0, so

    e^(−λ_cu)O_φ(P_c(u)z)/A
        ≥3j_*/4−2H_obs C_gap θ_c.

Perturbation costs at most H_obs ε_opM_z≤j_*/8. Since 2H_obs C_gapθ_c≤j_*/8, the result is ≥j_*/2. Combining entrance, N−1 subsequent full blocks and this terminal estimate yields

    Y_δ:=O_φD_N⁺(τ)D_(N−1)⁺(B)⋯D₀⁺(B)e₀
       ≥c_*(1−ρ)^(N−1)
         exp[BΣ_(m<N)λ_(s_m)+τλ_(s_N)]>0,
    c_*=a_*j_*/4.                                    (8)

The induction includes N=1 and τ=0. No positivity of noisy block operators, composition property for arbitrary comparison blocks, or independence is required. For the actual blocks, (8) holds on E_δ once δB≤ω. The indices lie in the compact family interval[0,1], including endpoints; the empty final interval is retained correctly.

## 4. Source restart and the comparison of PROOF125

At fixed δ,B,N use ONE retaining slow source Y_(ε,η) on the extension of the given W. Define its fast and local sources by literal raw-test pullbacks, not by separately chosen noise realizations:

    Y_fast(u,x)=δ^(a/2)Y_(ε,η)(δu,x),
    Y_m(u,x)=Y_fast(mB+u,x).

Their temporal law is K_(η/δ), since δ^a K_η(δr)=K_(η/δ)(r); heat widths and joint endpoint-width laws remain correct. At fixed δ,m the transformed tests converge in the prescribed raw completion. Source transfer supplies actual LᵖCθ driver limits on the finite extended horizon (N+1)B and each local horizon B.

The ordinary primitive identity gives, with A_glob=g_δ A_R(W_fast),

    S_F(mB)[A_glob(mB+u)−A_glob(mB)]S_F(−mB)=X_m(u).

This follows by changing the integration variable and composing the free groups; no mask is commuted through a wave group. Fixed-horizon source convergence passes this identity to the raw drivers. Conjugating Young sums and using uniqueness gives

    P_glob(mB+u,mB)=D_m⁰(u).

The mean primitive has the same cocycle. Composition therefore gives the true ordered products with final τ, including both constant-response columns.

The necessary source-product convergence is only at FIXED δ,N. If C≥1 bounds all finite source/raw factor norms and e_src is the maximal factor error, telescoping (or its elementary recurrence) bounds the difference of n=N+1 factors by n C^n e_src. Every finite moment of C is uniformly bounded in source widths and e_src→0 in every finite Lᵖ. Explicitly,

    ‖n C^n e_src‖₂
       ≤n ‖C‖_(4n)^n ‖e_src‖₄→0.

No estimate uniform in the growing number N is needed, because the source limit has already been completed before δ↓0.

Define the noise-only average U_δ=O_φD_N⁰(τ)⋯D₀⁰(B)e₀. The local Young map is defined everywhere, so the function j(x)=|O_φD_(x_N)(τ)⋯D_(x₀)(B)e₀|² is a nonnegative norm-Borel function on the whole block space. Applying (2) directly to the RAW paths gives

    E U_δ²=E[exp(−Z/√δ−v/(2δ))Y_δ²].                  (9)

This identity does not require weighted source convergence. Only the NOISE-ONLY product is passed to a masked ordinary-source limit for comparison; the shifted product already exists as an everywhere-defined raw Young function. Finite unweighted product moments follow from the Gaussian path bounds and Young growth. Formula(2) itself was valid before imposing integrability.

For comparison, put Γ_δ=g_δ²Γ and W'=g_δW_fast. At fixed δ this is an admissible covariance of the same degree and original dimension, and its source/driver is exactly the amplitude-scaled one: each driver is multiplied by g_δ and each nth chain by g_δ^n. The source restart identifies U_δ as the L² limit of the masked ordinary solution average at fast time L=δ⁻¹. This discharges the explicit masked-limit premise of P:masked-canonical-transfer; it is not an assumed rough masked solution.

At positive source widths, every expected displacement Wick diagram has nonnegative covariance and positive Green factors. The masked diagram adds ∏_vertices m_R(x_i)∈[0,1], including within-chain, cross-chain, unequal and empty-chain terms. Summing with absolute L² tails gives the two-point comparison. Integrating against φ(x)φ(y)≥0 and using stationarity/Cauchy–Schwarz for the unmasked source yields

    E|∫φ(x)u_src^mask(L,x)dx|²
      ≤‖φ‖₁² E|u_src(L,0)|².

Here ‖φ‖₁=1. Fixed-order joint source limits plus the summable q_n(L)q_k(L) majorant pass the unmasked second moment to its canonical value. The constructed masked L² limit passes its squared norm as well. Hence

    E U_δ²≤E|u_(Γδ)(δ⁻¹,0)|².                        (10)

There is no pathwise solution comparison or arbitrary-phase Gaussian covariance order in this step.

Under the fast-to-slow time substitution t=δu, g_δY_fast(u)=√δY_(ε,η)(δu). With phase (V,δV_t), the unmasked source equation therefore becomes δ²V_tt=ΔV+√δY_(ε,η)V with initial data(1,0). At fixed δ the canonical diagram/source limits and absolute series preserve this law identity. Exact canonical scaling with δ=T^(−κ), r_T=Tδ gives

    E|u_(Γδ)(δ⁻¹,0)|²=E|V_δ(1,0)|²=E|u(T,0)|².       (11)

The mask radius R and original physical scaling r_T are distinct. No mask covering the growing backward cone is needed: (10) is a moment inequality, not an equality of masked and unmasked fields. The comparison changes neither the original slow Z nor v in (9).

## 5. Full probability/rate budget and normalization

Fix any e>0. Choose ρ with −log(1−ρ)<e/3, and then choose B,ω,ε_op,c_* by the cone budgets. They are fixed before δ↓0. Besides δ<min(1,1/B), choose δ small enough that

    δB≤ω,
    δ≤ε_op/(2L_B),
    C_λ δB≤e/3,
    δ|log c_*|≤e/3,
    A_pη^(−p)δ^γ+vδ^(1/2)≤1/2.                       (12)

Every constant is finite for fixed Ψ,R,B; if C_λ=0 the corresponding requirement is vacuous. The source/width limits in §4 have already been taken at each such fixed δ.

On E_δ, taking the logarithm of (8) gives

    δlogY_δ ≥ δlogc_*+δ(N−1)log(1−ρ)
               +δBΣ_(m<N)λ_(s_m)+δτλ_(s_N).

The last two terms are exactly the left Riemann sum on[0,1], including the last interval lengthδτ and mesh≤δB. Lipschitz continuity of λ bounds its error by C_λδB. Since 0≤δ(N−1)≤1/B≤1 and log(1−ρ)<0, the normalized cone loss is ≥log(1−ρ)>−e/3. The other two losses are ≤e/3 each by(12). Thus

    Y_δ≥exp((I_R−e)/δ) on E_δ.                        (13)

On the SAME event, −Z/√δ≥−δ^(−3/4). Restricting the nonnegative integrand of(9), and then using(10)–(11), gives the explicit lower bound

    E|u(T,0)|² ≥ E U_δ²
      ≥p_δ exp[(2I_R−2e−v/2)/δ−δ^(−3/4)].             (14)

No product of block probabilities has appeared. From(6),(12), p_δ≥1/2 for smallδ and δlogp_δ→0. Multiplying the log of(14) byδ yields

    δlogE|u(T,0)|²
       ≥2I_R−2e−v/2 −δ^(1/4)+δlogp_δ.

The moderate-deviation linear term costs δ^(1/4)→0; the fixed Gaussian quadratic action costs precisely v/2. Since δ=T^(−κ) is a bijection from all sufficiently large T to all sufficiently smallδ, this is a liminf over the full continuous time parameter, not a selected time sequence. Therefore

    Q₂≥2I_R−2e−v/2.

The original point rate Q₂ is independent of the auxiliary block length B. For every e the argument used its own FIXED B(e) and first took δ↓0. Only now let e↓0. This proves(A); it does not take a simultaneous B(δ) limit. Spatial stationarity of the canonical flat-data solution gives the same second moment at every fixed x, preserving(A).

## 6. Later mask/control optimization and remaining obligations

For PROOF126, Ψ and an eligible R were fixed before all source and time limits. If one subsequently removes the mask, the existing P:variational-remove-mask (`integrated_unmasked_variational.tex:190–248`) chooses an increasing smooth plateau-mask family and shows I_R↑I_Ψ by real Rayleigh form order, the bounded smooth global mean and compact-time convergence. Applying(A) separately at each fixed R and then taking the numerical supremum gives Q₂≥2I_Ψ−v_Ψ/2. Only after each individual control bound may one take a numerical supremum over Ψ. There is no R(T), source/time exchange, uniform-radius driver estimate, or changed action.

**Author conclusion:** I find no remaining mathematical gap in the Gaussian/probability/comparison passage of PROOF125–126 once the exact local inputs listed above are consumed. Equations(4),(6),(12)–(14) give the formerly compressed probability/error budget explicitly. The argument does not require independence, an external large-deviation principle, covariance monotonicity for arbitrary phases, or a new Skorohod result.

**Remaining obligations:** This new external expansion has not itself received an independent cross-family mathematical/application review or been integrated into production. The MAIN report’s raw LIMITED classification of126 is unchanged. Root must decide how to use this replay and retain the independent checks of the local driver/source, spectral-cone and canonical-scaling inputs; this author reconstruction does not certify them by vote or demand reproof of their cited external theorems. Full214/whole-argument, source-image/render and cold-review gates remain separate. Zero covariance is the direct case u=1 and rate0, outside the nonzero-control binding construction used above. No Article/source/provider/ref mutation or sibling/Skorohod work occurred.
