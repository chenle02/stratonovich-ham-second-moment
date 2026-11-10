# Worked supplement for the actual-driver analytic interfaces

Author-only preparation. No manuscript/source changes and no new provider. The actual DeepSeek PROOF085–093 report remains PASS_WITH_NOTES/MEDIUM, with its nine raw FULL rows and eleven PASS checks unchanged. Its report-only fixed-q/Lp error is preserved and identified below. This supplement expands calculations already present in the unchanged source; it asserts no newly discovered defect.

Source bindings, exact revision equality, raw-review and adjudication hashes are in `bindings.json`. The current driver, wave-variance and compact-Gaussian files equal their bytes at both887fbfbe and53bf01b; current HEAD at inspection was e444a278706dc4ee0fb4e1913b2b307815ef611f. Stable identities are proof-index-v3 PROOF087 `L:driver-gain-localization`, PROOF092 `L:driver-holder-limit`, and the relevant assembly in PROOF093 `P:actual-operator-driver`.

## What the MEDIUM report actually left limited

The raw report does not declare these nine proofs unchecked. It says it reconstructed them and located no mathematical defect. It treats free-wave finite propagation in DRV03/087 as an admitted classical PDE input; it also says it reconstructed the dyadic-to-Hölder characterization in DRV08/092, while still listing that classical fact and upstream interfaces not re-derived as reasons for MEDIUM confidence. Thus “neither analytic fact was independently checked at all” would overstate the record.

| Place | Own proof/application not fully expanded in raw review | Ordinary prerequisite interface, not another omitted driver proof |
|---|---|---|
| 085/086 | Report says full reconstruction; compact-smooth null-class extension at t=0 is a nonblocking clarification | Covariance completion and local temporal integrability are explicitly used |
| 087 | Raw review admits the full two-entry finite-propagation theorem, rather than displaying its flux/density proof; gain and Hilbert-adjoint indices were reconstructed | The free group is the actual massless two-entry group in `E:variance-free-matrix`; no positivity/comparison theorem |
| 088 | Raw review reconstructs actual projection, both variance directions, first-chaos expansion and tails | `P:wave-two-variances`, `P:wave-square-columns`, `P:compact-two-envelopes` are used as earlier proved lemmas; their full proofs were not re-derived in this unit |
| 089/090 | Raw review reconstructs compact domination and Gaussian compression/Fatou | `L:compact-positive-order`, `P:finite-gaussian-matrix`, `C:finite-gaussian-operators` are normal earlier theorem interfaces |
| 091 | Raw review reconstructs tail Cauchy, compactness and long-interval additivity | `P:localized-finite-variance` and `C:finite-gaussian-operators` must be applied with the proved localization/variance guards; their internal proofs need not be repeated inside 091 |
| 092 | Raw review says dyadic characterization was reconstructed, but its displayed check does not spell out binary approximation, coarse grids and the finite-grid/interpolation Cauchy proof | The strict β-refinement of `P:wave-two-variances` supplies increment moments; the deterministic path argument below is own work at this interface |
| 093 | Its p-dependent even-q selection and exponential series were worked correctly in DRV09 | Raw DRV07's phrase “one even q gives all Lp” is false by monotonicity; it is not what source091/093 proves |

A review of the explicit calculations below could add a precise independent check of the classical admission and the path-construction interface. Simply asking another run to repeat “all nine FULL” and return HIGH would add no specified mathematical coverage. Nothing here promotes the original grade. Existing valid upstream proof evidence should be consumed by its actual bindings; lack of repetition in this driver review is not itself a new gap in those upstream lemmas.

## Exact setup and guards

Use the actual original model, d∈{1,2,3}, a=α0∈(0,1), α+a<2, and its allowed homogeneous covariance. Fix R,T>0. Let s=1/2, E_r=H^r(R^d)×H^(r−1)(R^d), E=E_s. The free phase group in `E:variance-free-matrix` is

    S(t,ξ) = [[cos(t|ξ|),       sin(t|ξ|)/|ξ|],
              [−|ξ|sin(t|ξ|),   cos(t|ξ|)    ]],

where the sine quotient at zero is t, so this is u_t=v, v_t=Δu with wave speed1. Let B(b)(u,v)=(0,bu). For the actual smooth covariance coefficient H_{j,R}(t), its spatial support lies in B_{2R}. The coefficient operator is `E:driver-coefficient-operator`

    A_j(I)z = ∫_I S(−t) B(H_{j,R}(t)) S(t)z dt,   I⊂[0,T].

Source `E:driver-gain-one` gives bounded gain E_r→E_{r+1}, and its primitive A_j(0,t) is operator-norm Lipschitz. It does not require operator-norm continuity of S(t).

The actual parameters are `E:driver-parameters`

    0<γ<min(1/2,(2−α)/2),
    1/2<θ<β<min(1−a/2,(3−a−α)/2).

Choose θ<η<β, so 0<θ<η<β<1, and choose even q0≥2 such that

    q0 γ>d,      δ0:=β−η−1/q0>0.

All statements below keep R,T and these strict parameters fixed. Neither a uniform growing-R path norm nor a Cθ Schatten-valued path is claimed.

## A. Full two-entry free-wave support and actual localization

This expands source087 LF216–229, within its complete LF169–237 statement/proof.

**Smooth cone calculation.** Let (u,v) be a smooth free-wave phase and fix a center x0 and radius ρ>0. Set

    e(t,x)=(v(t,x)^2+|∇u(t,x)|^2)/2,
    E_ρ(t)=∫_{|x−x0|<ρ−t} e(t,x) dx,       0≤t<ρ.

The PDE gives ∂_t e=div(v∇u). The moving boundary has normal speed−1, so the divergence theorem and differentiation under the smooth moving domain give

    dE_ρ/dt = ∫_{|x−x0|=ρ−t} (v∂_n u−e) dS ≤0,

because 2v∂_n u≤v²+(∂_n u)²≤v²+|∇u|². This is the exact flux inequality in the manuscript. The d1 formula is the same boundary identity with two endpoints.

If both initial entries vanish on B_ρ(x0), then E_ρ(0)=0 and nonnegative E_ρ(t)≤0. Smoothness implies v=0 and ∇u=0 throughout the shrinking cone. For any fixed x with |x−x0|<ρ−t, its vertical segment (τ,x), 0≤τ≤t, stays in that cone, so

    u(t,x)=u(0,x)+∫_0^t v(τ,x)dτ=0.

Thus both entries vanish there. Zero initial displacement is indispensable: gradient energy alone would permit a nonzero spatial constant. Zero initial velocity is also indispensable: u(0)=0 alone permits immediate nonzero displacement.

For compactly supported smooth initial phase with support K, take x with dist(x,K)>t, choose t<ρ<dist(x,K), and apply the cone calculation at center x. Both entries vanish at (t,x). Therefore support grows by at most t. With J(u,v)=(u,−v), the Fourier matrix gives S(−t)=J S(t) J, so the same support assertion holds backward in time. This does not invoke positivity or scalar solution-value multiplication.

**Sobolev extension needed here.** The actual group is bounded and strongly continuous on each E_r over finite time intervals. Hence smooth phases approximate any phase in E_r and their propagated phases converge in E_r, consequently as distributions in both entries. A distributional limit of phases vanishing on a fixed open set also vanishes there, by testing each entry against compact smooth functions supported in that set.

For the right cutoff identity, use precisely the manuscript's support-preserving approximation. Let z_n be Schwartz phases converging to z in E_r; multiplication by 1−χ is bounded on both component Sobolev spaces. Then (1−D_χ)z_n→(1−D_χ)z, and every approximant vanishes on B_{2R+T+1} because χ=1 there. The cone calculation shows both propagated entries vanish on B_{2R+T+1−t}, which contains B_{2R} for 0≤t≤T. Distributional convergence retains this vanishing. Thus

    B(H_{j,R}(t)) S(t)(1−D_χ)z=0,
    A_j(I)(1−D_χ)z=0.

For the output support, y_t=B(H_{j,R}(t))S(t)z has both entries supported in the closed B_{2R}, with first entry zero. It belongs to E_{r+1}. Approximate it by convolution with compact smooth approximate identities of radius ε, so its approximants are supported in B_{2R+ε} and converge in E_{r+1}. Apply the smooth backward support theorem, pass to the distributional limit, and then let ε decrease: S(−t)y_t is supported in B_{2R+t}. For a compact test outside B_{2R+T}, every integrand pairing is zero; the statewise Bochner integral therefore has both entries supported in B_{2R+T}.

Since χ is identically1 on a neighborhood of this closed ball,

    D_χ A_j(I)=A_j(I)=A_j(I)D_χ

on every E_r, exactly `E:driver-actual-localization`. This uses ordinary multiplication on both entries. It does not assert that the Hilbert-space adjoint D_χ^{*,E} equals D_χ: the actual Bessel-weighted adjoint remains the one in `E:variance-cutoff-adjoint`.

## B. Dyadic control, finite-grid convergence and moment indices

This expands source092 LF472–553 and the existing source093 LF577–589.

**Deterministic dyadic control.** For continuous Banach-valued F with F(0)=0, put Δ_n=T2^(−n), t_k^n=kΔ_n, and

    D_n(F)=max_{0≤k<2^n} ||F(t_{k+1}^n)−F(t_k^n)||,
    Z_η(F)=∑_{n≥0}2^(nη)D_n(F).

For 0≤u<v≤T choose n with Δ_{n+1}<v−u≤Δ_n. Let π_n(t)=Δ_n floor(t/Δ_n), retaining π_n(T)=T. The two level-n grid points differ by at most two adjacent intervals. Also π_{m+1}(t)−π_m(t) is either zero or one adjacent level-(m+1) interval. Continuity therefore yields

    ||F(v)−F(u)|| ≤2D_n(F)+2∑_{m>n}D_m(F)
                  ≤2∑_{m≥n}D_m(F).

Since (v−u)^(−η)<T^(−η)2^((n+1)η),

    [F]_η ≤2^(1+η) T^(−η) Z_η(F),
    ||F||_{Cη} ≤2^(1+η)(1+T^(−η)) Z_η(F).

The supremum estimate uses F(0)=0. It would fail for a nonzero constant F if that condition were dropped. For the finite paths X_N, operator-norm Lipschitzness already gives continuity and finite Z_η because η<1, so this use is not circular. This is a sufficient weighted-sum control; no converse norm equivalence is needed.

**Uniform moment sum including coarse levels.** The strict β-version of `P:wave-two-variances`, finite Gaussian operator estimate, and q0γ>d give, for all even q≥q0 and all N,

    ||X_N(t)−X_N(u)||_{Lq(B(E))} ≤C sqrt(q)|t−u|^β,  |t−u|≤1.

The fixed cutoff norm is uniform in q: ||K_χ||_{S_q}≤||K_χ||_{S_q0}. This follows by normalizing the singular-value sequence by its S_q0 norm and using x^q≤x^q0 for 0≤x≤1; the zero case is direct. The time-refined variance constant and the finite Gaussian factor sqrt(q−1) introduce no further q-dependent constant.

Set n_f=max(0,ceil(log2 T)), so Δ_n≤1 for n≥n_f. The finite-maximum bound, without independence, gives

    ||D_n(X_N)||_{Lq}
       ≤(∑_{k<2^n} E||increment_k||^q)^(1/q)
       ≤2^(n/q) C sqrt(q) T^β 2^(−nβ).

Minkowski and 1/q≤1/q0 bound the fine-level sum by

    C sqrt(q) T^β ∑_{n≥n_f}2^(−n(β−η−1/q))
       ≤ C sqrt(q) T^β/(1−2^(−δ0)).

For each coarse level n<n_f, partition each adjacent interval into at most ceil(T) intervals of length≤1. Minkowski bounds each long increment by C sqrt(q)ceil(T). Taking its finite grid maximum costs at most 2^(n/q0). Hence the coarse contribution is bounded by

    C sqrt(q)ceil(T) ∑_{0≤n<n_f}2^(n(η+1/q0)),

a finite constant times sqrt(q), independent of N,q and the test basis. This proves `E:driver-dyadic-moment-sum` and the uniform Lq Cη estimate with every constant's dependence visible. Differences X_N−X_M have at most twice that bound.

**Finite-grid Cauchy before interpolation.** Fix q and a finite grid of mesh δ. For F=X_N−X_M,

    ||F||∞ ≤ max_i||F(t_i)|| + δ^η [F]_η.

Every grid value tends to zero in Lq as N,M→∞ by `L:driver-interval-limit`; its finite maximum does too, since its Lq norm is bounded by the q-sum of the finitely many point-value Lq norms. The second term is bounded by 2C sqrt(q)δ^η. First send N,M→∞ at fixed grid, then δ→0. This gives Lq C0 Cauchy convergence; no claim that pointwise convergence alone gives uniform convergence is used.

**Deterministic interpolation and probability Hölder.** Put λ=θ/η∈(0,1), A=||F||∞, B=||F||_{Cη}. Every increment is bounded by both 2A and B|t−u|^η. The inequality min(x,y)≤x^(1−λ)y^λ gives

    [F]_θ ≤(2A)^(1−λ) B^λ,
    ||F||_{Cθ} ≤(1+2^(1−λ)) A^(1−λ) B^λ.

The supremum term is included because A≤B. Apply scalar Hölder with exponents 1/(1−λ),1/λ to the qth moment to obtain

    ||F||_{Lq Cθ} ≤C ||A||_{Lq}^(1−λ) ||B||_{Lq}^λ →0.

Thus source092's Cθ Cauchy passage uses the same q, not an unmentioned larger moment. The limit lies in the separable Cθ-closed span of the countably many deterministic Lipschitz paths A_j(0,·). Almost-sure Cθ subsequence convergence gives one uniform path event for compact values at all times, not separate uncountably many exceptional sets. No separability of all B(E) or of the full Hölder space is presumed.

**Select q separately for each requested p.** For arbitrary finite p≥1, choose

    q=2 ceil(max(p,q0)/2).

It is an admissible even index, q≥p and q≥q0, with q≤p+q0+2≤(q0+3)p. Then Lyapunov gives Lp convergence and

    || ||M_R||_{Cθ} ||_{Lp} ≤C sqrt(q)≤C sqrt(q0+3)sqrt(p).

This is source093's actual argument. A fixed-q Lq bound by monotonicity gives only p≤q; it does not give every p. The raw DRV07 sentence claiming otherwise is a report error already adjudicated, and remains unchanged in the raw report.

For Y=||M_R||_{Cθ}, its resulting bound with constant C1 gives E Y^(2m)≤(C1 sqrt(2m))^(2m). Using m!≥(m/e)^m, the mth positive term of E exp(cY²) is bounded by (2ecC1²)^m. Therefore any 0<c<1/(2eC1²) gives a convergent geometric majorant. If C1=0, Y=0 almost surely. This is an operator-norm Hölder-path estimate only, not an arbitrary Schatten-index path assertion.

## Checks and remaining disposition

A concrete allowed tuple is d=1 spatial white covariance α=1, a=1/2, γ=1/4, θ=9/16, η=5/8, β=11/16 and even q0=32. Here α+a<2; the upper β endpoint is3/4; q0γ=8>1; δ0=1/32>0. No endpoint estimate or critical-log equality is used. For example p=1 uses q=32, p=33 uses q=34, and p=100 uses q=100. This exhibits why the raw fixed-q wording must not replace the source selection. The F(0)=0 constant-function check and the two-entry/constant-displacement checks above prevent the two usual analytic shortcuts.

No own mathematical defect is established. This is a concrete expansion of existing source calculations and a precise separation of earlier-lemma interfaces from the two classical analytic facts identified by the raw report. A further targeted review would add mathematical coverage only if it actually verifies the full Sobolev/distribution support extension and the dyadic/coarse-grid/interpolation/p-dependent-moment bridge against the current source. Repeating already covered algebra or requiring all upstream lemmas to be re-proved merely to obtain HIGH would not resolve a newly identified gap.

The independent MEDIUM limitation, raw error, and root's no-HIGH-adoption decision remain. This supplement has not been independently reviewed, gives no new source-image/global/cold/fullgoal credit, and authorizes no review dispatch on its own. Root disposition is pending.
