# Static052–058: published source fidelity and normalization

The retained PUBLISHED Chen–Hu result uses RAW integer moments E[U(t,x)^p], not L^p norms. Its p=1/p=2 ratio is2^kappa_st. The matching af97 application in052–058 is faithful on this point; no normalization or version repair is needed. This is author source/application work, not an independent model-family review, manuscript change, grade or whole-goal clearance.

The scoped theorem-source verdict is VERIFIED: Theorem1.2/(1.9)'s raw-p interpretation, p-dependence, relevant model/data/heat-limit conventions and the p=1,2 use here. This does not reopen/adopt the numerical value of the common variational constant or settle the already recorded general-theorem/white-corollary numerical hold. Those values are not premises of052–058.

## Exact edition and reading boundary

Xia Chen and Yaozhong Hu, “Hyperbolic Anderson equations with general time-independent Gaussian noise: Stratonovich regime,” Annals of Probability53(6)(2025),2144–2195, DOI10.1214/24-AOP1758. Actual retained version-of-record PDF:553495bytes,52pages, SHA25658b152d78cd0d54d82b991933b3eaece86e1ed2b44fe09882c14eba921e97e22. Its title/authors/DOI/journal header were checked on rendered PDFpage1. No arXiv-v1/old llm-pack formula substitutes for the publication.

Rendered and actually viewed: PDFpages1,4,9,22,31,37,40,41,42 (journal2144,2147,2152,2165,2174,2180,2183–2185). The existing111795-byte published-primary context was read at the introduction/Section5 relevant statements and upper argument; new text extracted from the same PDF covers the complete2180–2185 lower argument, including2181–2182. Those two pages were text-read, not given an invented image-reading credit. The source common-Laplace/spectral input remains an imported published result; this is not a fresh proof audit of every52-page argument or of every cited book.

The complete actualaf97 statements/proofs052–058 and surrounding imported-static/order-of-limits paragraphs were read. Source bodies, source-manifest, primary text, PDF, skill and all viewed page images have separate hashes in bindings.json. Images here authenticate source formulas only; they clear no manuscript source/image/Kimi/cold gate. All writes are external to Article/held point packet/source/foreign WIP.

## Hypotheses and object matching

The source equation(1.1),journal2145, has wave coefficientDelta (not halfDelta), unit noise strength and data u0=1,u1=0. It is Stratonovich, with a real time-INDEPENDENT centered Gaussian spatial noise. Standing assumptions are d=1,2,3 and nonnegative even PD covariancegamma, with spectral measuremu and Dalang integral int mu(dxi)/(1+|xi|²)<infinity. Theorem1.2 assumes gamma(cx)=c^-alpha gamma(x),0<alpha<min(2,d), or alpha=d=1 white. Eq(2.18),2152, explicitly admits generalized gamma by Gaussian-heat limits; the measure/sphere discussion at that page coversd3. Thus it is not a covariance-function-density-only theorem.

Our original nonzero homogeneous tempered positive RadonGamma meets that convention: Gamma(cA)=c^(d-alpha)Gamma(A) means distributional homogeneity of degree-alpha. Its spectral ball law mu(B_r)=r^alpha mu(B1) gives

    int mu(dxi)/(1+|xi|²)
      <=mu(B1)+C_alpha mu(B1)sum_(j>=0)2^((alpha-2)j)<infinity.

No angular density or finite total spectral mass is required. The window a_max=min(1,2-alpha)>0 is feasible; a=a_max/4,b=a_max/2 is an explicit interpolation witness. For example d=alpha=1 spatial white permits a=1/4,b=1/2. A singular d3 plane covariance withalpha=1 is equally within the generalized spatial class. ZeroGamma is excluded from this section's strictly positive L0/ratio statements; its solution1 is handled directly elsewhere, not by dividing by L0=0.

The source's ordered kernels/ordinary Gaussian products are(2.10)–(2.14),2150; its heat-limit generalized pairing convention is(2.18),2152. Theorem3.8(i)/(3.23),2165, gives the fixed-order L² limit for arbitrary spatial widths. The af97 static terms use the SAME heat-limit kernels with all self-pairings.052 independently proves absolute static series convergence from the fractional regularized upper and scaled-moment tails; it does not borrow the source's quantitative(4.3). The resulting static U is identified by its canonical coefficients and L² sum, without uniqueness of all rough mild solutions.

## What Theorem1.2 and its proof actually normalize

Put nu=3-alpha>1, q=4-alpha=nu+1 and kappa_st=q/nu. Theorem1.2/(1.9),2147, prints

    lim_(t->infinity) t^(-kappa_st) log E[U(t,x)^p]
      = p^kappa_st L0,             p=1,2,...,
    L0=lim t^(-kappa_st)log E U(t,x)>0.

No1/p stands outside the logarithm. Eq(1.10) is a DIFFERENT statement: high absolute moments as p->infinity at fixedt. The L^p inequality on printed2178 compares realp to its next even integer for that high-moment statement. It does not change(1.9) into an L^p-norm theorem. Forp=2, E U²=E|U|² but ||U||2=(E U²)^(1/2); forp=1, ||U||1=E|U| need not equal the signed mean E U. No pathwise positivity is assumed in052–058.

The fixed-p proof independently confirms the same normalization. Define the RAW coefficient

    A_(p,n)(t1,...,tp)
      =sum_(l1+...+lp=2n) E product_j S_lj(g_lj(.,tj,0)),
    a_(p,n)=A_(p,n)(1,...,1).

Section5 begins on2173 with exactly E U(t)^p=sum_n a_(p,n)t^(qn), a positive series, including zero orders/empty chains. There is no norm root and no extra factorial in this definition. Its common-time degree is qn by(5.1).

For the joint Laplace integral J_(p,n)=int exp(-sum t_j)A_(p,n)(t)dt, (5.14)+(5.16) give(5.21),2183:

    (J_(p,n)/n!)^(1/n) -> J_Gamma=2 M^(q/2),

with the SAME positive finite Gamma-dependent base at every fixed integerp. Here M denotes only the source's printed common variational object; no numerical evaluation is adopted. In the lower argument, fixed-p factors C_delta^-p and polynomial composition counts have nth-root limit1. They do not secretly divide log moments byp.

Eq(5.12),2179, is the exact key:

    int_(R+^p)exp(-sum t_j)(min_j t_j)^(qn)dt
      =p^(-qn)Gamma_E(1+qn).

It follows from min ofp unit exponential times having parameterp. Eq(5.13)/(5.15) supplies the upper bound for a_(p,n) with this factor. Lemma5.3/(5.22),2183–2185, supplies the matching lower bound. Its probability measure is normalized by the full joint Laplace integral, and its lifetimes concentrate near t_j=qn/p, not qn. The printed denominator sum_j(1-theta_j)^(-2) in(5.23) is retained. Differentiation atzero gives each component q/p: the numerator derivative is2, its denominator is p, multiplied byq/2. Chernoff upper estimates plus the good rate's uniquezero at(q/p,...,q/p) give exponentially concentrated rectangles; no missing Gärtner–Ellis lower equality is needed for that upper concentration. On those rectangles monotonicity and common-time homogeneity reduce the integral to the displayed min-time integral, producing the same p^(qn) in the lower coefficient bound. This matches rendered(5.22), not an older generated TeX that might omit1/p.

Stirling gives Gamma_E(1+qn)=(n!)^q q^(qn)exp(o(n)). Combining upper/lower yields

    ((n!)^nu a_(p,n))^(1/n)
      -> p^q J_Gamma/q^q
       =p^q 2^(-nu)(2sqrt(M)/q)^q.

The positive-series type formula (source5.4–5.5,2174; independently proved in our053) gives nu times the1/nu power. Therefore the RAW growth type is p^(q/nu)L0. A hypothetical norm interpretation would instead produce p^(q/nu-1)L0=p^(1/nu)L0. It is a different observable.

Consequently the exact needed source import is

    raw static first mean rate=L0,
    raw static second moment rate=2^kappa_st L0,
    static L² NORM rate=2^(kappa_st-1)L0.

The common constant cancels in the first/second RAW ratio. The existing white-corollary numerical normalization discrepancy is neither used nor resolved by this calculation; both printed forms retain the same p exponent. There is no identification here with the fractional auxiliary S1pos.

## Full052–058 application readback

052 constructs the static endpoint separately: temporal covariance1, not evaluation of Gamma_E(a) atzero. Fixed-order heat-limit convergence comes from the positive spatial Wick construction and source3.8(i). At horizon1, chooseb0>0, positive temporal widthdelta0 and c=K_(delta0,b0)(1)>0. The fractional source at amplitude r/sqrt(c) dominates the static source amplitude r in every finite positive Wick diagram. Its existing enlarged-amplitude bound is uniform inN and spatialwidth. Positive static mixed moments and fixed-order L² limits then give ||X_n^(0)(1)||2<=sqrt(B)r^-n. Choose r>max(1,t^(q/2)); static degree qn/2 proves absolute norm summability at every fixedt. No static infinite series was assumed in this construction.

For m_k(a)=E X_(2k)^(a)(1), the raw temporal multipliers on the SAME positive spatial/Green disjoint-union measure are product_edges|s_j-s_h|^-a. At a=theta b they equal the b multiplier to theta. Ordinary Holder gives m_k(a)<=m_k(0)^(1-a/b)m_k(b)^(a/b), first at fixed spatialwidth. Raw-time limits at each FIXED positive endpoint use the uniform-in-spatialwidth temporal-tail sandwich from006; endpointzero uses the static multiplier1. There is no interpolation of exponent-dependent EulerGamma or Laplace-prefix normalizations, and no uniform-in-a convergence is asserted. Diagram scaling gives m_k(a)t^((q-a)k), so E u^(a)(t)=F_a(t^(q-a)).

053 is internal positive-series mathematics. For F(z)=sum c_kz^k, c_k>=0, nu>=1, the exponential type tau and K=limsup((k!)^nu c_k)^(1/k) satisfy tau=nu K^(1/nu). Bounding c_kz^k by Cexp(Lz^(1/nu)) atz=(nu k/L)^nu and elementary Stirling gives one direction; the series sum x^k/(k!)^nu<=exp(nu x^(1/nu)) gives the reverse. The factorial power isnu, notq, because the q-time Gamma growth has already been divided byn! in the coefficient calculation.

054 compares RAW means/squares, not norms. At fixed horizonT and positive widths, K_(delta,a)(s-r)>=K_(delta,a)(T)=c_(delta,T), tending to T^-a. Every finite diagram is nonnegative with the same spatial factors, so the finite expectedp powers are ordered forp=1,2. Green is removed first. At fixed order the static side is polynomial in its amplitude sqrt(c_(delta,T)), so joint noise-width removal gives a static covariance amplitude T^-a; only then pass the two absolutely L² series at fixedT. No covariance-PSD coupling or samplewise solution order is used.

Static total order2k has amplitude factor sigma^(2k) and time degreeqk. Thus for the actual static moment

    E[U_sigma(T)^p]=E[U(sigma^(2/q)T)^p],  p=1,2.

Set sigma=T^-a/2, T_eff=T^(1-a/q). Then T_eff^kappa_st=T^kappa(a), kappa(a)=(q-a)/nu. The published RAW rates give Lambda_lower_p(a)>=p^kappa_st L0 for EVERY admissiblea. There is no lost1/p and no need for a uniform small-amplitude theorem: the static moment clock identity is exact at each fixedT.

055 concerns the ACTUAL signed mean M(a)=limsup T^-kappa(a)log E u^(a), not E|u| and not S1pos. At a=0,053 gives K(0)=(L0/nu)^nu>0. At an anchorb, Cauchy–Schwarz plus the independent full second-moment upper gives finite M(b), hence finiteK(b). For any B_b>=max(2K(0),K(b)), Holder/root-limsup gives

    M(a)<=L0(B_b/K(0))^(a/(b nu)).

All root-sequence limits can be justified by eventually bounding each endpoint by its finite limsup+epsilon; no nonzero-coefficient division is needed. Since B_b/K(0)>=2, a*=b log2/log(B_b/K(0)) lies in(0,b]. For0<a<a*, 2M(a)<2L0*2^(1/nu)=2^kappa_st L0. Combine054 atp=2. This is a strict gap from twice the actual RAW mean limsup, in that window only; it does not compare an absolute first moment or establish all fixed-a source constants.

056 uses the FULL raw second-moment coefficients c_(2,k)=sum_(m=0)^(2k)E[X_m X_(2k-m)]. Both empty-chain orientations and unequal/self contractions are included with pairing coefficient1. The disjoint-union positive measures admit the same Holder interpolation between any a1<a<a2; no diagonal-chaos/orthogonality shortcut is used. With c_(1,k)=m_k the two entire series have time degree(q-a)k.

057 applies053 with the same fixednu to each series. Its type is precisely the normalized RAW moment upper rate Lambda_upper_p(a), since z=T^(q-a) and z^(1/nu)=T^kappa(a). Coefficient log-convexity passes through factorial roots/limsup, giving log-convexity of the POSITIVE FINITE upper rates. Lower positivity is054's C_p=p^kappa_stL0; upper finiteness is independent051 plus Cauchy–Schwarz for the mean. Interior continuity is then an elementary finite-convex-function conclusion.

058 fixesGamma and an anchorb BEFORE takinga->0. Forp=1,2,

    C_p<=Lambda_lower_p(a)<=Lambda_upper_p(a)
       <=C_p[Lambda_upper_p(b)/C_p]^(a/b).

The finite bracket is>=1; squeeze gives both rates tending toC_p. Their ratio Lambda_lower_2/Lambda_upper_1 tends to2^kappa_st because L0>0. These are ITERATED statements: time liminf/sup at each fixeda using its OWN T^-kappa(a), thena->0. They establish no time-limit existence at fixeda from interpolation alone, no uniformity inT/covariance, no diagonal limit and no fixed-a all-p law. The later intrinsic theorem separately treatsp=2.

## Falsifications and auxiliary-score boundary

1. Foralpha=1, nu=2: the source RAW second/first rate ratio is2sqrt(2), while the L²-norm/raw-mean ratio issqrt(2). Misusing the latter as a raw second rate would violate E U²>=(E U)², which forces a raw rate at least2L0. No disputed numerical value ofL0 enters this check.
2. In d1 static whiteGamma=c delta0, unit-time order2 gives E X1²=c/6 and E X2=c/12, hence c_(2,1)=c/3 andm1=c/12. Omitting empty/self/unequal terms gives the wrong coefficient. The finite ratio4 is NOT an asymptotic rate estimate; it is only a diagram-normalization control.
3. T^kappa_st/T^kappa(a)=T^(a/nu). Along a=c/logT this tends toe^(c/nu), not1. Likewise T_eff/T tends toe^(-c/q). Thus endpoint exponent convergence alone cannot justify substituting static normalization in a simultaneous limit.058 expressly uses the correct iterated order.
4. L0 is the actual static RAW first-mean rate. M(a) is the fractional actual RAW mean limsup. S1pos(Gamma,a) is an auxiliary full-positive-control score with variance-half action; label-scaling S_cpos=c^kappa_st S1pos does not identify S1pos with M(a) at fixed positivea. Static Chen–Hu M is yet another spatial variational object. No equality between these objects is silently adopted. If one separately combines058 with the already-statedp2 intrinsic identity, S1pos(a)->L0 is a boundary consistency consequence, not a fixed-a actualp1 theorem.

No source or application defect was identified in the raw-moment/Lp normalization use of052–058. Existing source-version and numerical-normalization qualifications remain. The exact needed imported clauses and local interpolation arguments are separated in application-matrix.json; no manuscript, held packet, grade, runtime, provider, six-repo, correspondence, Skorohod, Lean or HPC action occurred. Full214/240/13/originalmodels/actualC2 and independent whole/source-image/Kimi/cold gates remain.
