# Given-W operator-driver closure088/091/092/093

Author mathematical reconstruction, 2026-11-04, science af97. The four assigned CURRENT OWN deductions are088(two actual variances),091(actual interval operator limit),092(actual Holder path) and093(the assembled given-noise Gaussian path). The needed089/090 tail and retained-average calculations are worked explicitly below. Current069–074 variance/column clauses and075–087 Gaussian/cutoff/coefficient clauses remain named OWN prerequisites with precise applications, not accepted full parents. This is not a model review, new theorem, source edit or scientific grade.

## 0. Falsification before the construction

Three finite/infinite-dimensional controls prevent shortcuts.

(1) For16 coordinate row matrices A_k=e_k^T, X=Σg_kA_k has ||X||S4^4=(Σg_k²)². Its expectation is16(16+2)=288. The input variance alone would give9 Tr(I16²)=144, false. The actual two-variance average is9(16²+16)/2=1224; transposition reverses the bad direction. Thus both variance directions must survive the actual-noise projection and Gaussian estimate.

(2) Norm convergence does not imply trace-power convergence: T_n=n^(−1/m)P_n on a rank-n subspace has ||T_n||→0 but Tr T_n^m=1. Even decreasing positive tails can fail without a trace-class-power envelope: T_N=diag(j^(−1/m)1_(j>N)) tends strongly/in norm to0, while Tr T_N^m=∞. A FIXED B∈S_m dominating all tails is essential. It cannot be replaced by a different finite-rank projection at each stage.

(3) Positive order cannot be raised to an arbitrary operator power. For

    A=[[1,1/2],[1/2,1/4]],  B=diag(2,1/2),

A≥0 and B−A=[[1,−1/2],[−1/2,1/4]]≥0. But (B²−A²)22=1/4−5/16=−1/16. Thus0≤A≤B does not imply A²≤B². Eigenvalue/trace comparisons below use max-min, not this false inference.

Finally actual074 fixed-input columns are not random bounded operators. On l², Σ(j≤N)g_j(e_j⊗e_j) has both fixed-input L² bounds≤||z||², but its norm is max(j≤N)|g_j| and has no finite almost-sure bounded limit. Here the variance envelope is I, not compact. Source localization and compact domination are substantive, not bookkeeping.

## 1. Exact objects, coefficients and exposed input clauses

Let a=α₀; original H:homog retains d=1,2,3, 0<a<1, 0<α<d or α=d=1, α+a<2, and the original nonnegative even positive-definite homogeneous tempered Radon Γ with positive even spectral μ. White/singular/nonradial measures and all covariance amplitudes remain. Γ0 is direct at the end. Fix finite R,T and the source's real even smooth mask ζ_R, physical multiplication AFTER covariance convolution. Set s=1/2, E_r=H^r×H^(r−1), E=E_s, and choose

    0<γ<min(1/2,(2−α)/2),
    1/2<θ<β<min(1−a/2,(3−a−α)/2).

The upper β endpoints exceed1/2. Every constant below may depend on these fixed data, Γ/amplitude and auxiliary cutoffs. No growing-R/T, endpoint-gamma, or endpoint-time uniformity is asserted.

Let H_W be the prescribed covariance-null quotient completion, W the GIVEN real isonormal process. OWN085 provides real compact smooth ONB representatives f_j; g_j=W(f_j) are independent standard real Gaussians. Independence is only of this orthonormal raw-noise coordinate family, not of spatial phase columns, increments, sources or blocks. No H_W-valued identity-covariance Gaussian vector is introduced.

OWN086 supplies the literal covariance coefficient

    H_j,R(t,x)=ζ_R(x)∫(u>0)|t−u|^(−a)
                         ∫Γ(dy)f_j(u,x−y)du,
    E[g_j W_C(ζ_RF)]=∫H_j,R F.

The masked coefficient is smooth on finite compacts with common spatial support B2R. This holds for signed smooth f_j: zero-extend this deterministic test in time and shift its derivatives onto f_j in the locally integrable |v|^(−a) convolution; the spatial difference set has finite Radon mass. This is not an extension of stochastic noise to negative times. The actual coefficients depend only on the H_W class. Moving ζ_R into Γ*f_j would change this row and is not permitted.

The deterministic operators are statewise strong integrals

    A_j(I)z=∫_I S(−t)B(H_j,R(t))S(t)z dt,
    B(b)(u,v)=(0,bu).

OWN087 gives A_j:E_r→E_(r+1) bounded by C_j,r,R,T |I|, an operator-norm Lipschitz primitive. The E_s adjoint has domain gain E_(2s−r−1)→E_(2s−r). Specifically choose r=s−γ for A_j, and r=s+γ−1 in the adjoint statement: BOTH map E_(s−γ) to E_(s+1−γ)⊂E_s because γ<1. These are finite-j domain estimates; their constants will NOT be summed over noise coordinates.

The actual Sobolev adjoint in the covariance row is the earlier071 one: G_w=−(sin(t|D|)/|D|)Λw₁+cos(t|D|)Λ⁻¹w₂, with the two E weights Λ,Λ⁻¹, not displacement S(t)w. Thus

    E[g_j ell_R(I;z,w)]=〈A_j(I)z,w〉E,
    ell_R=W_C(ζ_R1_I v_z conjugate G_w).

Both wave entries/zero sine quotient and the actual gain orientations of073 are retained. This application uses literal completed tests on the original W.

Choose real χ=1 on B_(2R+T+1), compact smooth. The full free two-entry wave has finite propagation; input(1−Dχ)z has zero free displacement on B2R for0≤t≤T, while output S(−t)B(H_j,R)S(t)z is supported in B_(2R+T). Therefore

    Dχ A_j=A_j=A_j Dχ.

This is a deterministic identity on all E_r. Both phase entries and the strict plateau margin matter. Dχ is not assumed a projection or self-adjoint on E. The identities survive actual adjoints in their proper order.

In physical unitary coordinates set

    J₀(u,v)=(Λ^½u,Λ^−½v), H₀=L²(Rd;R²),
    a_j=J₀A_jJ₀⁻¹, P=J₀DχJ₀⁻¹,
    D=diag(Λ^−γ,Λ^−γ).

OWN078–080 provide the exact two factors/envelopes

    Kout=PD, Kin=P*D,
    Bout=P D²P*=Kout Kout*,
    Bin=P* D²P=Kin Kin*.

P=diag(Λ^½χΛ^−½,Λ^−½χΛ^½). Real χ implies P*=UPU for the phase swap U, which commutes with D. Hence Kin=UKoutU; their singular values agree, but the operators/envelopes need not be identical. Each K belongs S_q when q≥1 and qγ>d, with singular values O(j^(−γ/d)). For q≥2, Tr Bout^(q/2)=Tr Bin^(q/2)=||Kout||Sq^q. These are fixed-whole-space-cutoff facts; D alone is noncompact, and the cutoff norm can depend on R,T. No compactness of a scalar time operator tensor identity is used.

## 2.088: actual noise projection, then phase Parseval, in BOTH directions

Put X_N(I)=Σ(j≤N)g_j A_j(I) and b_I=C_T h^(2−a)Bα(h), 0<h=|I|≤1, where Bα=1,1+log1/h,h^(1−α) in the three α regimes. The exact073/074 input is

    Σ_k E|ell(e_k,w)|²≤b_I ||w||E_(s−γ)²,
    Σ_k E|ell(z,e_k)|²≤b_I ||z||E_(s−γ)²,

for every finite E_s-ON Schwartz phase family, and actual fixed-input columns m,n into L²(Ω;E_s) with the corresponding rows. The finite noise projection is

    〈X_N z,w〉=Σ(j≤N)g_j E[g_j ell(z,w)]
              =𝒫_N ell(z,w),

where 𝒫_N projects onto span(g₁,…,g_N) in L²(Ω). Consequently Σ(j≤N)|〈A_jz,w〉|²≤E|ell(z,w)|². This is actual raw-noise projection, not source smoothing.

Keep N FINITE, fix Schwartz w, sum the preceding inequality over a finite phase ON family e_k in the INPUT slot. The first073 direction gives

    Σ(k≤K)Σ(j≤N)|〈A_j e_k,w〉|²≤b_I||w||E_(s−γ)².

Let K→∞. Phase Parseval and nonnegative Tonelli yield

    Σ(j≤N)||A_j* w||E²≤b_I||w||E_(s−γ)².              (1out)

For fixed z, use the SECOND073 direction with e_k in the OUTPUT slot to obtain independently

    Σ(j≤N)||A_j z||E²≤b_I||z||E_(s−γ)².              (1in)

Neither estimate is inferred from the other. For each finite N the gain/domain estimates above extend (1out)/(1in) by Schwartz approximation to all E_(s−γ), with the SAME b_I independent of N. Individual coefficient gain constants are only used for continuity of finitely many terms; no divergent sum of those constants is hidden.

Restrict to E_s and transport by J₀. Since ||z||E_(s−γ)=||D J₀z||H₀, the quadratic inequalities are

    Vout,N=Σ(j≤N)a_j a_j* ≤b_I D²,
    Vin,N =Σ(j≤N)a_j* a_j ≤b_I D².                   (2)

Left localization gives Vout,N=P Vout,N P*; right localization gives Vin,N=P* Vin,N P. Positive congruence, without P=P* or P²=P, therefore supplies

    Vout,N≤b_I Bout,  Vin,N≤b_I Bin.                 (3)

This is the precise two-envelope application of OWN082. Both envelopes and the actual coefficient localizations are needed; one cannot assign Bout to both sides by treating Dχ as an E-orthogonal projection.

## 3.088: actual first-chaos columns and positive strong tails

For fixed Schwartz z, each coordinate〈m(z),e_k〉=ell(z,e_k) lies in the CLOSED FIRST CHAOS W(H_W), because it is an actual completed linear noise test. Its g_j coefficient is〈A_jz,e_k〉. Parseval in that chaos followed by phase Parseval gives

    Σ_j||A_jz||E²
      =Σ_k Σ_j |E[g_j ell(z,e_k)]|²
      =Σ_k E|ell(z,e_k)|²
      =E||m(z)||E²,
    m(z)=Σ_jg_jA_jz in L²(Ω;E).                      (4)

The same argument with the INPUT variance gives n(z)=Σ_jg_j A_j* z. This uses actual first-chaos membership, not the false assertion that every Gaussian variable on a space is in the given W chaos. For a fixed rough z∈E_(s−γ), approximate by Schwartz z_l. Equations(1) uniformly in N control the input error; continuity of m,n and (4) for z_l identify the same expansions for z. This does not promote m,n to samplewise bounded operators.

The increasing quadratic sums in (2) define bounded positive Vout,∞/Vin,∞ by polarization/Riesz. On H₀ put Tdot,N=Vdot,∞−Vdot,N. Then0≤Tdot,N≤b_ID², their quadratic forms tend to zero, and

    ||Tdot,N v||²≤||Tdot,N||〈Tdot,Nv,v〉→0.           (5)

The uniform norm bound follows from(2) and ||D||≤1. Thus tails converge STRONGLY. Passing the finite congruences to the limit gives Tout,N=P Tout,N P*, Tin,N=P* Tin,N P. Applying congruence to their D² bounds yields

    0≤Tout,N≤b_I Bout,  0≤Tin,N≤b_I Bin.             (6)

The envelopes are FIXED as N→∞. They are not noise-dependent/moving projections. Real operators complexify isometrically, and the real ON basis becomes a complex ON basis without doubling singular-value multiplicities. The same inequalities/constants hold on the complexified H₀ used for traces.

## 4.089/090: compact-dominated TRACE powers and retained Gaussian average

Fix ONE admissible even q≥2 with qγ>d, and m=q/2. In general only Tr T_N^m is claimed finite; Tr T_N need not be finite. A tail dominated by B=b_I Bout (or b_I Bin) satisfies B∈S_m. For a finite spectral projection Q of B with ||(1−Q)B(1−Q)||<ε, positive quadratic Cauchy–Schwarz gives, on unit vectors,

    〈T_Nx,x〉≤2||QT_NQ||+2ε.

Weak convergence (already strong in(5)) makes the finite matrix QT_NQ converge to0 in norm. First N→∞ at fixed Q, then ε↓0 proves ||T_N||→0. OWN081's compact-order/max-min clause gives compactness and λ_j(T_N)≤λ_j(B), while ||T_N||→0 gives λ_j(T_N)→0 for each fixed j. Dominated summation, not power order, yields

    Tr Tout,N^m→0,  Tr Tin,N^m→0.                    (7)

In particular, for ε>0 choose a finite eigenvalue head J with Σ(j>J)λ_j(B)^m<ε, then N so the finitely many λ_j(T_N)^m sum<ε. This explicitly controls the ACTUAL trace power. The norm-only and false-power-order examples in section0 explain why (7) cannot be abbreviated to an operator-norm assertion.

The needed Gaussian tail estimate keeps the average. Let Z_l be a FINITE compact coefficient family with Vout/Vin∈S_m. For finite-rank orthogonal Q_k→I,

    Σ_l Q_k Z_l Q_k Z_l* Q_k ≤ Q_k Vout Q_k,

because the difference isΣ_l Q_kZ_l(1−Q_k)Z_l*Q_k≥0; the input inequality interchanges adjoints. Compression max-min and OWN081 compare trace powers. Apply OWN077's finite Gaussian MATRIX bound on ran Q_k:

    E||Σ_l g_l Q_kZ_lQ_k||Sq^q
       ≤(q−1)^(q/2)[Tr Vout^m+Tr Vin^m]/2.           (8)

For each fixed Gaussian coordinate vector, the sum is compact, so its compressions converge in OPERATOR NORM, by finite-rank approximation and strong convergence on finite-dimensional ranges. Singular values are norm-Lipschitz. Fatou over their nonnegative q-powers and then probability passes (8) toΣg_lZ_l. No infinite Gaussian series, S_q-Bochner convergence or independence of compressed matrix entries was presumed. This derives090 as a finite-compression application of077/081.

## 5.091: genuine original-space operator Cauchy limit

OWN082/083 applies to the actual finite coefficients in(2)/(3), so every A_j(I) and finite sum X_N(I) is compact; for each admissible even q,

    || ||X_N(I)||Sq ||Lq
       ≤√(q−1) √b_I ||Kout||Sq.                     (9)

This is only a uniform moment bound and does not itself prove convergence. For M>N, use the SAME original g_j and set Y_NM=Σ(j=N+1..M)g_j A_j. Its two finite variances are bounded by Tout,N and Tin,N, respectively. Equations(7)/(8) and eigenvalue comparison give the actual uniform Cauchy estimate

    sup(M>N) E||Y_NM||Sq^q
      ≤(q−1)^(q/2)[Tr Tout,N^(q/2)+Tr Tin,N^(q/2)]/2
      →0.                                          (10)

Since operator norm≤S_q norm, this proves Lq(B(E)) Cauchy convergence, not merely a weak limit or equality in distribution.

The operator-norm closed real span F_I of countably many deterministic A_j(I) is separable. Choose N_k with ||X_(N(k+1))−X_(N(k))||Lq≤2^(−k). The L1 differences sum, so Tonelli makes their pointwise operator-norm differences summable almost surely. Completeness gives a limit on the ORIGINAL Ω in F_I; assign0 on the exceptional set. It is strongly measurable and W-measurable (in the completed given-noise sigma field), since every finite sum is. Fatou with (10) passes convergence of the WHOLE N sequence in Lq. An almost-sure norm-convergent subsequence and norm-closedness of K(E) give compact values.

For different admissible even q, limits agree by uniqueness of probability convergence. For every requested finite p choose an admissible even q≥p, obtain the same Lp operator limit X_R(I) by Lyapunov. A single fixed q cannot supply all moment orders. Singular-value Fatou in (9) gives exactly the fixed-interval statement

    || ||X_R(I)||Sq ||Lq
      ≤√(q−1)√C_T h^(1−a/2)Bα(h)^½||Kout||Sq,        (11)

at admissible even q only. It is not a Schatten-valued path assertion.

For each FIXED Schwartz z,w, the finite row is𝒫_N ell_R(I;z,w). The completed raw test ell belongs to W(H_W), so these projections converge in L² to THAT actual variable. Operator-norm L² convergence also gives row limit〈X_R(I)z,w〉. Uniqueness in L² proves the literal row identity on the given W, not an equal-law copy. Scalar continuous functionals are L² limits of finite Gaussian sums, and finite combinations stay Gaussian; hence X_R(I) is centered Gaussian and jointly Gaussian for fixed finite families.

For a long interval choose a FINITE partition into short intervals. Indicator tests add except at finitely many endpoints; the compact-support/time-Schur raw continuity gives those changes zero raw norm. Deterministic coefficient statewise integrals add exactly. Passing finite-sum Lp limits yields operator/raw-row additivity, independently of the partition by common refinement. This defines each fixed long interval without claiming the short-h bound at h>1 or taking uncountable null-set intersections.

## 6.092: uniform moment indices and dyadic all-time control

Choose θ<η<β and an even q₀≥2 satisfying q₀γ>d and β−η−1/q₀>0. This is possible in the strict original windows. For every even q≥q₀,

    ||Kout||Sq≤||Kout||Sq₀,

by monotonicity of the singular-value sequence lq norms (normalize by the Sq₀ norm; zero norm is direct). Apply the finite Gaussian bound to the time-refined073 budget b'_I=C_T,β h^(2β), not to individual j-dependent Lipschitz constants. It follows uniformly in N, even q≥q₀ and short increments that

    ||X_N(t)−X_N(u)||LqB(E)≤C√q |t−u|^β.            (12)

The constant contains the FIXED Sq₀ cutoff norm and is independent of q, N and the chosen smooth noise basis. Long increments are finite sums of unit pieces, costing only a T-dependent constant.

On the grid t_(n,k)=kT2^(−n), let D_n(F)=max(k<2^n)||F(t_(n,k+1))−F(t_(n,k))||. A finite maximum is bounded by the lq sum, without independence. At fine levels T2^(−n)≤1,

    ||D_n(X_N)||Lq≤2^(n/q) C√q (T2^(−n))^β.

Minkowski gives

    sup_N ||Σ(n≥0)2^(nη)D_n(X_N)||Lq≤Cη√q,          (13)

since the fine ratio is≤2^(−(β−η−1/q₀))<1. There are only finitely many coarse levels; finite unit partitions give the same uniform-in-q bound there.

Here is the deterministic chaining step, rather than a Kolmogorov signature. For continuous zero-start F and two times separated by r, choose grid size h_n comparable to r, h_n≤r<2h_n. The approximating grid points differ by at most two adjacent increments; the finer binary corrections of the two endpoints cost≤2Σ(k>n)D_k. Consequently

    ||F(t)−F(u)||≤2D_n+2Σ(k>n)D_k
       ≤C_T,η r^η Σ(k≥0)2^(kη)D_k.

Continuity identifies the binary endpoint limits. Taking u=0 also controls sup||F||. Each finite X_N is Lipschitz from its finitely many deterministic coefficient paths, so this applies with no path modification. Equations(12)/(13) yield uniform Lq Cη bounds, and twice that bound for X_N−X_M. Constants remain independent of N,M,q≥q₀ and the noise basis.

## 7.092: fixed grid FIRST, mesh SECOND, then lower Holder exponent

For a fixed finite grid,091 gives Lq convergence at each point, hence the maximum difference there tends to0 as N,M→∞. Deterministically,

    ||F||∞≤max_grid||F(t_k)||+C mesh^η||F||Cη.

Apply to F=X_N−X_M and use the uniform bound from(13). Send N,M→∞ at that fixed grid, then mesh→0. This proves Lq sup-norm Cauchy convergence. No interchange of a diverging grid with noise truncation is asserted.

The deterministic interpolation bound is

    ||F||Cθ≤C ||F||∞^(1−θ/η)||F||Cη^(θ/η).           (14)

For an increment use min(2||F||∞,[F]η r^η), split at the balancing r and include the supremum term; constants may depend on the fixed horizon. Ordinary Holder in probability at the SAME q gives

    || ||F||Cθ ||Lq
       ≤C || ||F||∞ ||Lq^(1−θ/η)
             || ||F||Cη ||Lq^(θ/η) →0.              (15)

For arbitrary finite p, choose even q≥max(p,q₀) and use Lyapunov. Thus the full sequence X_N converges in every finite Lp Cθ norm, not just pointwise/law or a subsequence.

Every finite path belongs to the span of the countably many deterministic Lipschitz paths A_j(0,·). Their Cθ-closed real span F_path is a separable Banach space, even though the ambient Holder/operator space need not be separable. The summable-subsequence construction used in091 therefore gives a strongly measurable W-measurable limit M_R on the original Ω. All p limits agree in probability in that path norm.

Choose one almost surely Cθ-convergent subsequence; it converges uniformly in operator norm. Each finite path has compact values for ALL t: each deterministic coefficient has actual localization/compactness at every short interval and finite additivity on long ones. Norm-closedness of K(E) therefore gives compact values of M_R at ALL times on that SINGLE path event. M_R(0)=0. This is not a union over individually selected time-null sets.

The path is in the little-θ Holder closure of Lipschitz paths. Explicitly, on the convergence event and for ε>0 choose N with[M_R−X_N]θ<ε. Then

    sup(0<|t−u|≤r) ||M_R(t)−M_R(u)||/|t−u|^θ
       ≤ε+Lip(X_N) r^(1−θ) →ε.

Let ε↓0. This supplementary observation follows from the actual Cθ convergence, without a new Gaussian regularity theorem. It does not make the whole ambient Holder space separable or supply any Schatten path norm.

Passing(13) through lower-exponent path convergence/Fatou yields

    || ||M_R||Cθ ||Lq≤C√q, even q≥q₀.                (16)

The actual proof uses a higher η for tight dyadic control and a lower θ for convergence; no endpoint η=β−1/q₀ or θ=η is taken.

## 8.093: Gaussianity, actual versions, all p and square-exponential norm

Fixed-time evaluation of the path limit equals the interval limit by probability uniqueness, so its fixed Schwartz rows and increments retain the actual completed raw forms, including long-interval additivity and the fixed-interval moment(11). Continuous real linear functionals on F_path applied to X_N are finite linear Gaussian combinations. L² convergence gives convergence of means/variances and characteristic functions; finite linear combinations of functionals do too. Thus M_R is a centered Gaussian random element on this ACTUAL separable path span, not only a collection of pointwise Gaussian rows. Four real pair identities give the complex sesquilinear row identity.

For two compact-smooth ON noise bases, both constructions have the same original raw rows. Choose one countable dense Schwartz phase set and rational times. The countable union of row exceptional sets is null. Boundedness extends phase equality from the dense set, and path continuity extends from rational to all times. The two paths are indistinguishable on Ω. This is pairwise basis independence; no common event across uncountably many bases/raw tests is required. Because(12)/(13) uses only the uniform wave variance/projection/compact cutoff bounds, the final moment constants do not depend on that chosen basis.

For p≥1 select even q≥max(p,q₀) with q≤p+q₀+2≤(q₀+3)p. Lyapunov and(16) give || ||M_R||Cθ ||Lp≤C₁√p. If C₁=0 the path is0. Otherwise

    E||M_R||Cθ^(2m)≤C₁^(2m)(2m)^m,
    Eexp(c||M_R||Cθ²)
       ≤Σ(m≥0)(2ecC₁²)^m<∞, 0<c<(2eC₁²)⁻¹,         (17)

using m!≥(m/e)^m and positive Tonelli. This proves the exact norm square-exponential input needed later by the source/UI seam; it is not a square-exponential bound for a nonlinear Young flow and does not re-prove095.

## 9. Zero branch, model scope, and what remains an input

For Γ=0 the raw quotient is the zero space, all raw forms/drivers/coefficient families vanish, and one takes M_R≡0 directly. There is no need to invent an infinite ON basis in that case. All moment, path, compactness, row and exponential assertions then hold trivially; deterministic free wave evolution is separate. For nonzero Γ, the actual085 basis/086 convolution/localization arguments only use local Radon mass, time integrability and the specified physical/spectral positivity. They admit white and singular non-density covariances; no finite total Γ or μ, angular density or factorization is imposed.

This reconstruction gives the source/UI consumer093 its actual given-W compact-valued Cθ path, convergent finite coefficients at EVERY finite Lp, literal covariance rows, basis-independent versions, Gaussian √p and square-exponential norm. The two actual variances, fixed compact envelopes, trace-power tail domination, interval Cauchy limit and dyadic grid/mesh order are displayed, rather than substituted by a declaration that the operator exists.

The full proofs of069–074 and075–087 remain separate CURRENT OWN obligations. This work matches their precise applications, does not accept those full parents, and does not derive a common random operator from074 columns alone. It creates no Ctheta-Schatten path, arbitrary-index Schatten theorem, Hilbert–Schmidt claim, scalar-time-tensor compactness, source convergence theorem or nonlinear solution moment bound. No source gap has been found in the assigned088/091/092/093 deductions under the exposed clauses. No model review/grade, whole214/240/13, Kimi, visual/source-pixel or fresh-cold gate is cleared.
