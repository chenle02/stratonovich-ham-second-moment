# Physical energy036 and the independent dyadic upper049–051

Author reconstruction, 2026-11-04, exact af97. Assigned OWN036/049/050/051 are worked here, conditional on precisely exposed earlier OWN/external clauses. Source051 uses the finite-interval coefficient/Fock route044–048, not the later Gaussian-tube/Rayleigh route170–177. The initial dispatch summary conflated those routes; this is an author-summary correction, not a manuscript defect or reason to repair source. Complete upstream parents remain CURRENT obligations, not accepted imports. No model review, source edit or grade is made.

## 0. Falsification, domains and normalization

For Γ=0, u=1 and all positive noise orders vanish. The final bound e(T+2)^d≥1 is consistent without a nonzero-covariance or spectral division argument. For d1 white Γ=cδ, μ=c dξ/(2π), μ(B1)=c/π and R1=c/2. Thus the eventual exponent is C(c/2)^½ T^((3−a)/2), not an L² norm rate silently substituted for the raw second moment.

A low-order check prevents a Skorohod shortcut. In the static a=0 calibration (a boundary calculation, not an assertion of the theorem at a=0), G1(t,x)=½1_(|x|<t) gives

    E X1(T,0)²=c∫[(T−|y|)_+/2]²dy=cT³/6,
    E X2(T,0)= (c/2)∫₀ᵀ(T−s)∫₀ˢdu ds=cT³/12.

The total order-two second-moment coefficient is E X1²+2E X2=cT³/3. Dropping unequal/empty-chain self-pairs would lose half. For an admissible nonzero temporal exponent, the same two-vertex mean is

    E X2=cT^(3−a)/[2(1−a)(2−a)(3−a)],

so the empty-chain cross term remains nonzero. This is a finite calibration, not a new all-order moment formula.

C23(1.4)'s square-root variation and(1.5)'s quartic variation are not interchangeable constants. For a homogeneous spatial degree χ, covariance amplitude b scales their optimized values as b^(2/(4−χ)) and b^(2/(2−χ)), respectively, by unit-L² spatial dilation. At χ=3/2,b=2 these factors are2^(4/5) and16.036 uses ONLY quartic finiteness as a seed;027/033's separate square-root application is not replaced.

## 1.036: the imported seed has its actual generalized-covariance hypotheses

Here the statement is specifically on R³: Ξ is nonnegative, even, PD, tempered Radon, Ξ(rA)=r^(3−χ)Ξ(A),0<χ<2; μΞ is its positive even spectral measure. Zero Ξ is direct. No temporal covariance or Hthree factorization is needed. Fourier transforms in THIS lemma are UNNORMALIZED, hhat(ξ)=∫exp(−iξ·x)h(x)dx. Hence the physical/spectral pairing below has NO extra(2π)^3 factor; the unitary wave convention used elsewhere must not be imported into it.

Fourier uniqueness gives μΞ(rA)=r^χμΞ(A). Its locally finite unit-ball mass and

    Σ(j≥0)2^(−2j) μΞ(B_(2^(j+1)))
       ≤const μΞ(B1) Σ(j≥0)2^(j(χ−2))<∞

verify Dalang's ∫(1+|ξ|²)⁻¹μΞ(dξ)<∞. The held C23 Theorem1.1/p2 explicitly admits generalized nonnegative PD covariances, with F_d the full unit-L² H¹ class, and says both variations(1.4),(1.5) are finite. Restrict its(1.5) conclusion to REAL UNIT-L² SCHWARTZ profiles. This supplies some finite C0≥0 with

    Q(f)≤½||∇f||₂²+C0, ||f||₂=1,
    Q(f)=E(f²), E(h)=∫|hhat(ξ)|²μΞ(dξ).

Only smooth pairings have been used. We do not import an already identified nonsmooth physical energy, entire books or the C23 numerical value as a model constant. Quartic scaling in f gives, for every real Schwartz f including0,

    Q(f)≤½||f||₂²||∇f||₂²+C0||f||₂⁴.               (1)

For N(f)²=||f||₂²+||∇f||₂², one may take D=sqrt(C0+1/8), since b²g²≤(b²+g²)²/4. Thus Q(f)^½≤D N(f)². C0/D may depend on Ξ; they do NOT enter the parameter-only coefficient C in051.

## 2.036: TWO Cauchy inequalities and strong full-H¹ extension

For real Schwartz f,h define

    P(f,h)=∫Ξ(dz)∫ f(y+z)²h(y)²dy.

Schwartz distributional pairing and evenness identify P with∫hat(f²)conjugate(hat(h²))dμΞ. Physical Ξ≥0 gives P≥0; spectral Cauchy gives

    P(f,h)≤Q(f)^½ Q(h)^½.                            (2)

This is different from Cauchy on the positive measure m(dy,dz)=dy Ξ(dz), which gives

    E(fh)=∫ f(y+z)f(y)h(y+z)h(y)dm
           ≤Q(f)^½ Q(h)^½.                          (3)

E(fh) is quadratic in the PRODUCT fh, not the quartic Q(fh). All Schwartz pairings are absolutely integrable. Positivity of E follows independently from the positive spectral measure.

Set A_f(y,z)=f(y+z)f(y), B_f(ξ)=hat(f²)(ξ). Decompose

    A_f−A_h=(f−h)(y+z)f(y)+h(y+z)(f−h)(y).

By(1)/(2), each term's L²(m) norm is at most D N(f−h)N(f) or D N(h)N(f−h). By f²−h²=(f−h)(f+h), equation(3) similarly yields

    ||A_f−A_h||L²m≤D[N(f)+N(h)]N(f−h),
    ||B_f−B_h||L²μ≤D N(f−h)N(f+h)
                   ≤D[N(f)+N(h)]N(f−h).             (4)

Now let real Schwartz f_n→g in H¹. Both A_fn,B_fn are strong L² Cauchy by(4). Take a subsequence f_n→g Lebesgue-a.e. For EACH fixed z the exceptional sets in y and y+z are Lebesgue-null by translation. Sigma-finite Fubini for dy Ξ(dz), integrating Lebesgue y first, gives A_fn→g(y+z)g(y) m-a.e. Thus the strong limit is the actual physical A_g. The same argument proves independence from the Borel representative of g. It does NOT assert that a Lebesgue-null set is Ξ-null; Ξ may be singular.

Also ||f_n²−g²||₁≤||f_n−g||₂(||f_n||₂+||g||₂)→0. Unnormalized Fourier transforms therefore converge uniformly at ALL frequencies. An a.e. subsequence of the strong L²(μΞ) limit must equal this uniform limit, even when μΞ is singular. The strong spectral limit is precisely hat(g²), not an unspecified completion class. Since ||A_fn||²=Q(f_n)=||B_fn||², pass strong norms to get

    ∫Ξ(dz)∫g(y+z)²g(y)²dy
      =∫|hat(g²)|² μΞ(dξ)<∞.                        (5)

Passing(1) gives the same quartic bound for ALL real H¹ g. No prior finite-energy assumption is imposed on g.

For a singular normalization control, take Ξ=cδ₀(dx1)dx2dx3, χ=1, μΞ=(c/(2π))dξ1δ₀(dξ2)δ₀(dξ3), and g=g1⊗g_perp. Both sides of(5) equal c∫g1⁴·||g_perp||₂⁴, by one-dimensional unnormalized Plancherel. This tests a spectral line/physical plane with no density fiction. It is not d3 spatial white, which has degree3 and is outside χ<2. For unit-L² g, (1) also implies finiteness of sup[Q(g)^½−||∇g||₂²] by maximizing sqrt(x/2+C0)−x over x≥0; it does not identify its value with C0 or C23(1.4).

## 3. Exact earlier interval/Fock clause needed by051

For the original d1/2/3 covariance Γ, define

    Rα=απ μ(B1)/[2sin(πα/2)],
    ν=3−α>1, β=4−α−a>2, p=2−a>1,
    Xρ norm²=||f||₂²+||(ρ²−Δ)^(-1/2)g||₂².

This phase Xρ is NOT the later E=H½×H⁻½/F constant extension or a Gaussian-tube input space. The independent upper does not need those constructions.

The precise048 clause is: for independent static Gaussian COLORS W_i^ε, with finite interval inventory sorted by length h_i≤LT/i and σ_i²≤c h_i^(−a), every real Schwartz phase v has

    |[s^(2k)]E||U_F^ε(T;s)v||_(1/T)²|
       ≤C^k Rα^k T^(βk)/(k!)^ν ||v||_(1/T)², k≥1,   (6)
    E||U_F^ε(T;1)v||_(1/T)²
       ≤e exp(C Rα^(1/ν) T^(β/ν))||v||_(1/T)².      (7)

C depends only on α,a,L,c, not dimension, family size, positive smoothing or finite mode/band cutoffs. Covariance shape/amplitude enters only through Rα. Each color is static while its interval is active; repeated/overlapping intervals are NOT independent successive time blocks.43's independent-successive-block corollary cannot replace048.

The actual matching of earlier clauses is substantive.044 uses physical Γ≥0 in the translated heat/resolvent estimate and radial spectral homogeneity to obtain Rαρ^(α−2) for every original dimension/white/singular model. Its Fock bound is2sqrt(N+1)sqrt(Rα)ρ^(α/2−2).045/047 apply the bounded complex-phase theorem with a_sp=α/2∈(0,1), all four ordered inverse-root comparisons, bounded Fourier band and finite Hermite cutoffs; only CPv1 Theorem6/(3), constant1+sqrt2, is imported there. No unbounded CP extension is assumed.

For fixed total degree2k, let r_i+q_i=2k_i,Σk_i=k. These are ordinary amplitude coefficients, without embedded factorials. Gaussian reflection kills a term unless every color's combined degree is even, even though the two copies use the SAME colors. There are at most k active colors and ∏(2k_i+1)≤3^k splits.041 preserves the selected vector coefficients EXACTLY at Hermite cutoff N_i=2k_i; creation/annihilation self-pair words stay. This is an algebraic selected-word equality, not a degree-limit identification of a full propagator.

Background colors may already be occupied: their complex phase bound is an operator bound on the full joint Gaussian/phase Hilbert space, not a fresh-vacuum estimate. A singleton cross color is inserted once on each copy and is fresh at that insertion;044 applies tensoring with all other, possibly occupied, factors. The common partition has at most3k+1 pieces; its integrated weight is≤2k, so M_k=100^(3k+1)e^(4k) is a ONE-copy bound and two-copy Cauchy uses its square/e^(8k).

The047 bound contains Rα^k ONCE globally. After σ_i²≤c h_i^(−a) and λ=k/T the actual local energy weights are

    singleton(2,0)/(0,2): Rα h_i^β(1+1/(λh_i)),
    singleton(1,1):       Rα λ^(α−2)h_i^(2−a),
    k_i=l≥2: Rα^l h_i^(βl)(1+l/(λh_i))²/(l!)^ν.      (8)

The first metric factor is on only one copy, higher colors cost at most one per copy. Expanding h^(βl)(1+l/(λh))² gives powers βl,βl−1,βl−2, all positive for l≥2. Singleton powers β,β−1 and2−a are also positive. Thus substitute h_i≤LT/i in the WHOLE weight; bounding its inverse-length factor separately would be wrong. Absorb k²,3^k,c^k,L-powers into C^k, retaining all labels. This extracts Rα^kT^(βk), leaving

    v_i=i^(−β)+k⁻¹i^(−(β−1))+k^(α−2)i^(−p),
    b_i,l=i^(−βl)(1+li/k)²/(l!)^ν.

OWN046's positive product coefficient≤C^k/(k!)^ν applies because p>1,β>2 and β/ν>1. Ordinary multiplication of the local generating series already counts Σk_i=k; no extra multinomial is allowed. This is the exact use that yields(6), not positivity of arbitrary-phase coefficients. Summing absolute energy coefficients uses Σx^k/(k!)^ν≤exp(νx^(1/ν)) for ν>1; free order0≤e and e+Y−1≤eY give(7).

## 4. Finite cutoffs, actual ordinary coefficients and the nonuniform majorant

At fixed finite inventory and ε>0, Γ_ε^cov=p_(2ε)*Γ is bounded continuous and nonnegative. Write W_i^ε in actual Gaussian coordinates, retaining finitely many modes and a bounded spatial Fourier band first. Initial data are band-projected, contracting every Xρ norm. The CP/Fock bounds above are uniform in these cutoffs. Their finite-mode covariances need NOT be pointwise nonnegative, so no position-Wick comparison is performed yet.

The actual entire-series identification is separate from(6). Put v_max=sup_t Σ_i σ_i²1_Ii(t) Γ_ε^cov(0)<∞. At total Gaussian degree≤n, multiplication has norm≤2sqrt(n+1)sqrt(v_max), and a phase insertion costs1/λ. Free phase norm is≤exp(λh/2), not a contraction. On amplitude polydiscs max|z_i|≤z_* a total order-n phase majorant is

    exp(λT/2)[2z_*sqrt(n+1)sqrt(v_max)T/λ]^n/n!
       ×||v||λ.                                   (9)

Its nth root is O(n^(−1/2)), so the series is entire. It is allowed to depend on the finite family/ε; it is used for coefficient identification only, NEVER the uniform target bound.

At fixed order, omitted annihilation modes vanish on finite-coordinate Gaussian vectors, while the creation tail tends to0 by the omitted pointwise variance and dominated convergence. Finite-degree density extends strong convergence; closed multiplication identifies the actual field. Fourier-band projections converge strongly and commute with free evolution. Dominated time integration identifies the actual fixed Duhamel words, including both displacement and velocity. The selected Hermite coefficients already equal these words; a single fixed-degree truncated propagator is not asserted to be the full evolution. The entire bound(9) and vector Cauchy on a larger polydisc supply absolute coefficient/energy double-series convergence at the fixed ε/family. Consequently(6)/(7) hold for the actual finite-inventory field after cutoff removal.

These are ordinary bounded-cutoff/then-actual Duhamel constructions. No raw PDE pathwise uniqueness, source095/F-Young argument or later spectral/tube operator is substituted. Only after the mode/band limit is the actual covariance Γ_ε^cov nonnegative and suitable for the terminal positive position comparison.

## 5.049: exact positive terminal measure, all mixed Wick terms and coefficient1

For a chain ending at(T,x), the positive measure g_n^(T,x) is the backward pushforward of∏_j G_(s(j+1)−s_j)(dw_j) on0<s1<…<sn<T under y_j=x−Σ_(l≥j)w_l. This defines the object for d3 sphere Green just as for the density cases; g0 has unit mass on an empty tuple. Since G_h has mass h,

    M0(T)=1, Mn(T)=∫₀ᵀ(T−s)M_(n−1)(s)ds
                  =T^(2n)/(2n)!.                   (10)

Let the centered real field have sup point variance V<∞ and mean-square continuity on the open cells of a finite time partition times Rd. Gaussian moments and Holder give

    ||Π(j=1..n)W(s_j,y_j)||₂
       ≤Π||W(s_j,y_j)||_(2n)
       ≤sqrt((2n−1)!!) V^(n/2).

Products are strongly L² measurable (Gaussian increments give continuity in every finite moment); the finite terminal measure makes them Bochner integrable. Thus

    ||Y_n||₂≤b_n:=sqrt((2n−1)!!)V^(n/2)T^(2n)/(2n)!.

The ratio |r|b_(n+1)/b_n=|r|sqrt(V)T²/[(2n+2)sqrt(2n+1)]→0. Every regularized Σr^nY_n converges absolutely in L², for every complex/real r. V can diverge with removed cutoffs; this is not yet a uniform canonical tail estimate.

For m+n=2k, differentiate exp(½Σt_it_j K_ij) once at each of its labeled vertices. At odd degree the moment is0; at2k, the exponential's 2^k k! denominator is canceled by the orientations/orderings of its unordered pairs. Every pair partition has coefficient1, with covariance products including self-pairs within a chain and unequal/empty chains. Gaussian Holder and the finite chain masses justify expectation through both measures. These are products of ordinary Gaussian variables, not homogeneous orthogonal Itô chaoses.

Symmetrizing a chain averages its n! pushforwards with factor1/n!, while the scalar product of its n field values is invariant. Hence it gives the SAME random variable, with no additional n! or m!n! in the mixed formula. If K≥0, all the resulting displacement integrals are nonnegative, since Green measures and constant-data kernel factors are positive. Entrywise0≤K1≤K2 therefore compares each finite PARTIAL-ORDER second moment, including n≠m,0+n and self-pairs. It does not order arbitrary phases or samplewise solutions.

For d3 remove Green heat smoothing FIRST at fixed bounded noise covariance: weak convergence of positive Green measures, unchanged masses and bounded continuous finite Gaussian Wick products give convergence of the two mixed Green-width moments and hence L² convergence to the actual Bochner measure integral. Piecewise-time cut points are Lebesgue-null. This does not replace the sphere by a density or remove noise smoothing simultaneously.

## 6.050: enlarged-amplitude geometric tails BEFORE canonical full-series limits

Suppose a real r>1 has a prelimit uniform bound B_r≥E|Σr^nY_n^(ε,δ)|². At fixed positive widths049 gives absolute L² double convergence and nonnegative mixed moments. Thus its full second moment contains the nonnegative diagonal term r^(2n)E|Y_n|², so

    ||Y_n^(ε,δ)||₂≤sqrt(B_r)r^(−n).

The fixed-order L² limit006 passes the same bound to X_n. Summing geometric tails gives

    ||Σ(n>N)Y_n||₂, ||Σ(n>N)X_n||₂
       ≤sqrt(B_r)r^(−(N+1))/(1−r⁻¹).                (11)

At fixed N first remove BOTH noise widths at arbitrary relative rates; its finite head converges in L² by006. Only afterward N→∞ removes the two uniform tails(11). This constructs absolute L² convergence of the canonical series and full regularized-to-canonical convergence; it is not assumed from source Section5. If B1 separately bounds the unscaled moments, norm continuity passes B1, not the larger B_r, to the final canonical moment.

The conditional050 lemma is written before051, but its B_r premise is supplied by the finite prelimit models in051 BEFORE it is applied; that presentation order is not a cycle. The enlarged amplitude is a NOISE multiplier, not the moment order. In051 r=2 changes Γ to4Γ and Rα to4Rα. B(T;2) supplies tails; B(T;1) supplies the final theorem. Confusing these with an L² norm or a p=2 static source constant would change factors.

## 7.051: dyadic temporal majorant and actual independent color inventory

Choose6T≤H0<12T and h_j=H0 2^(−j),j≥0. For t=0,1/3,2/3, grid endpoints are h_j(n+(−1)^j t). Parent endpoints in child units differ from the child shift by3(−1)^j t, an integer, so each individual grid is nested. Across the three grids, boundaries at a level have spacing h_j/3.

For s≠r choose3|s−r|<h_j≤6|s−r|; such a scale exists because H0≥6T. The segment between s,r is shorter than h_j/3, so at least one grid has no boundary there and an interval containing both endpoints. Therefore

    |s−r|^(−a)
       ≤K∞(s,r):=6^a Σ_(threegrids,|I|≤H0)|I|^(−a)1_I(s)1_I(r). (12)

At most one interval per grid/length contributes off the diagonal, so also K∞≤[3·6^a/(1−2^(−a))]|s−r|^(−a), up to irrelevant endpoint choices. K∞ is an extended nonnegative numerical kernel. Its diagonal is infinite; no Gaussian field with this point covariance is constructed.

Retain the finite intervals meeting[0,T] through depth J. Give EACH interval its independent static spatial field W_I^ε with σ_I²=6^a|I|^(−a). Then

    W_Jε(s,y)=Σ_I σ_I1_I(s)W_I^ε(y),
    Cov(W_Jε(s,y),W_Jε(r,z))=K_J(s,r)Γ_ε^cov(y−z),
    K_J↑K∞.

At fixed J,ε this field has finite point variance, spatial mean-square continuity and only finitely many time cut points;049 applies. Independent colors do not make overlapping time segments independent.

At level j at most3(T/h_j+2) intervals meet[0,T]. Cumulative counts through j obey

    Σ(l≤j)3(T/h_l+2)≤6T/h_j+6(j+1)
       ≤6T/h_j+6·2^j<78T/h_j.

Sorting decreasing h_i therefore gives h_i≤78T/i. Thus048 applies with the EXACT inventory constants L=78,c=6^a, uniformly in J and ε. This is the origin of the parameter-only C(α,a); no finite-family or point-variance constant enters it.

## 8.051: compact data, ordinary spatial locality and the correct volume factor

Take real f_T∈Cc∞,0≤f_T≤1, equal1 on B_(T+1), supported in B_(T+2), initial phase(f_T,0). If |y|+s<T+1 then G_s*f_T(y)=s because G_s has mass s/support B_s, and consequently C_s f_T(y)=1. Every earlier chain vertex ending at x∈B1 at time T obeys |y|+s≤|x|+T<T+1. Its free initial factor is therefore exactly1. Iterating the full-phase Duhamel construction identifies each POSITION coefficient on B1 with the constant-data terminal integral of049. Velocity remains in the phase estimate/word construction; this scalar final identity is not a scalar phase restart.

At fixed J,ε the terminal coefficients are L²-continuous in x by displacing Green variables and using bounded continuous covariance products in their mixed moments. The bounds b_n above are uniform in x. Thus their pointwise L² series and its restriction in L²(Ω;L²(B1)) agree, and the actual phase series from048 has that same position representative termwise. No point trace of a rough E/F phase, global boundedness of a stationary potential, or rough PDE uniqueness is used.

Spatial stationarity of the actual finite-interval FIELD and its constant-data kernels gives

    |B1| E|u_Jε(T,0)|²
       =E∫_(B1)|u_Jε(T,x)|²dx
       ≤E||u_(fT),Jε(T)||₂²
       ≤e exp(C Rα^(1/ν)T^(β/ν))||(f_T,0)||_(1/T)².

Since||(f_T,0)||_(1/T)²=||f_T||₂²≤|B_(T+2)|, divide by |B1| to get the desired e(T+2)^d prefactor. No f_T derivative or F-lift norm is hidden. The finite model's actual full moment is the nonnegative sum of ALL terminal mixed pairings from049; finite partial-order moments are≤it, despite samplewise partial sums not being monotone.

## 9.051: source Green-first identification, positive comparison, then full limits

The held author common noise regularization has covariance

    K_δ(s−r)Γ_ε^cov(y−z),
    K_δ(v)=Γ_E(a)⁻¹∫₀^(δ⁻¹)e^(−q|v|)q^(a−1)dq,
    0≤K_δ(v)≤|v|^(−a).

Here Γ_E is Euler's Gamma function and Γ_ε^cov=p_(2ε)*Γ is the SINGLE-field covariance, consistent with the spatial sum-of-widths convention. At positive ε,δ it is bounded and continuous. The author's(2.23)–(2.24),p13 supplies this exact source law, not a new unsmoothed theorem.

Remove the source Green-width cutoff first. The actual Bochner terminal integrals and continuous-source pathwise smoothed integrals agree: Gaussian product bounds give∫||ΠW||₂dg_n<∞; Tonelli gives pathwise integrability and Minkowski gives L². Fubini against every L² test variable identifies the two versions. Apply the same weak-Green/mixed-moment argument as049, including d3 sphere measure. Thus fixed noise widths give EXACTLY the source's ordinary measure-kernel terms, not only a diagram with a similar name.

For a fixed partial order N, let U_N^(ε,δ) be its source sum and V_N,J^ε its finite-interval counterpart. Their finite second moments have the SAME terminal measures and all coefficient-one pairings; only temporal covariance factors differ. Equations(12) and K_J↑K∞, with nonnegative Tonelli, yield

    E|U_N^(ε,δ)(T,x)|²
       ≤lim(J→∞)E|V_N,J^ε(T,x)|²
       ≤sup_J E|u_Jε(T,x)|²
       ≤B(T):=e(T+2)^d exp(C Rα^(1/ν)T^(β/ν)).        (13)

No covariance-PSD order for arbitrary phases, stationary time law for K_J, Gaussian solution coupling, infinite-depth field or independent-block shortcut is asserted. Positivity is applied AFTER finite mode/band identification, at the full actual spatial covariance.

At these FIXED positive noise widths,049 permits N→∞. The same argument with any positive noise amplitude b replaces Γ by b²Γ, Rα by b²Rα and order n by b^n, without changing α,a,L,c. Hence

    E|u^(ε,δ)(b;T,x)|²
       ≤B(T;b)=e(T+2)^d exp(C(b²Rα)^(1/ν)T^κ),
    κ=β/ν=(4−α−a)/(3−α).                            (14)

This is a prelimit bound at every fixed T,x,Γ, uniform in widths. It was not borrowed from the canonical solution whose moment is being proved.

Now OWN006 provides actual fixed-order L² convergence Y_n^(ε,δ)→X_n, arbitrary relative widths, after Green smoothing is removed. Apply050 with r=2 and B_r=B(T;2). It constructs the full canonical series limit using(11). Passing the unscaled B(T;1) from(14) gives

    E u(T,x)²≤e(T+2)^d
       exp[C Rα^(1/(3−α))T^((4−α−a)/(3−α))], T≥1.    (15)

This moment proof does NOT use OWN002 full mixed-series justification,007 crude bound,008 width-uniform crude tails or source Section5 convergence. Existing OWN009 supplies the PARALLEL mild designation of the SAME series using006/008 and its onefold Green/product limits; that designation is not a numerical-rate premise of(15). SourceTheorem4.1/Lemma4.4 are not imports replacing the local006 fixed-order construction, whose actual upstream inputs are the author's universal pairing inequality3.1 and own homogeneous norms004/005/214. No raw-solution uniqueness is inferred.

The order of limits is: fixed total coefficient and finite family/smoothing, identify actual mode/band limits; actual finite J model bound uniform J,ε; fixed source widths and finite N remove source Green width first; J→∞ only inside finite positive Wick integrals; N→∞ at those positive widths by049; use006 at each fixed n and B(T;2) tails to remove noise widths then n-cutoff; pass B(T;1); ONLY THEN T→∞. No rate uniform in T or covariance shape is needed for these identifications. The final C is parameter-only because048 used L78/c6^a and Rα carried the covariance dependence.

## 10. Calibration and route boundary

For α=1 white, R1=c/2,ν=2,κ=(3−a)/2; replacing noise by bW gives covariance b²Γ and upper exponential amplitude b^(2/ν), not a raw/norm p-moment confusion. As a↓0 the exponent tends(4−α)/(3−α), consistent with the static comparison, but constants need not be uniform in a and no joint time/a limit is claimed. Jensen and actual first-moment comparisons remain separate; no printed Chen L or actualp1/auxiliary S1 equality is forced. The upper constant in(15) is nonsharp and is not an evaluation of intrinsic C2.

036 has its own R3/χ energy domain and C23 quartic seed; it does not introduce an unknown shape constant into051. Chen–Hu static asymptotics and Teschl compact/rough spectral/ground inputs belong to other source routes/comparisons and remain full-goal reading/application obligations, but are not direct premises of this independent051 proof. The later Gaussian-Rayleigh/tube route is also distinct and may not be used to prove the finiteness that051 supplies upstream to132/137.

No assigned-step source gap was found under the exact exposed earlier OWN/external clauses. This reconstruction does not accept complete004–006/214 or039–048 parents, prove their books, replace all214 current assignments by imported signatures, or clear any native HIGH/Kimi/source-pixel/visual/cold/whole-goal gate. It supplies explicit physical/spectral H¹ extension, coefficient-one terminal Wick/Green identity, prelimit enlarged-amplitude tails and same-canonical all-model upper closure on the actual written route.
