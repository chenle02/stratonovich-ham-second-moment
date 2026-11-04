# Rough real potentials and the actual uniformly bounded E wave

Author reconstruction of existing164/178/179, scientificaf97. This is not a new theorem, source correction, independent review or acceptance. Keep every original admissible d=1,2,3, homogeneous nonnegative even PD tempered Radon covariance, its amplitude, white/singular angular cases and zero covariance. The operator argument is for the actual REAL SIGNED multiplier class, not only positive Cameron means. The analytic hypotheses are membership in that compact supported multiplier closure; an arbitrary distribution in H^-1/2 is not automatically such a multiplier. Temporal parameters enter the subsequent mean application, not the standalone form construction.

Write H=L²(Rᵈ;C), Λ=(1−Δ)^(1/2), B0=1−Δ, E=H^1/2×H^-1/2 and F=E⊕R². Duals are taken under the L² pairing; all real spaces are complexified by real/imaginary splitting. For fixedR, K_R=supp(m_R), m_R=η(./R)²,0≤m_R≤1. The original smooth coefficients are V_q=m_R(Γ*q), q realCc∞, and L_q^E(u,v)=(0,V_qu). Let V_E,R be their operator-norm closure in K(E). This is a closed real linear space. It is already an actual physical class, not a new stationary noise or a density model.

##1. Falsification and normalization guards

At spectral h=0, the weighted wave matrix below has upper-right entry√c t, not0. Thus the factor1+t and the continuous sine quotient atzero cannot be dropped, even when the spectral bottom rateλ iszero. No division byλ is legitimate in that branch.

Positive FORM order does not give arbitrary operator-power order. In two dimensions take T=diag(1,2), S=T+[[1,1],[1,1]]. Then S−T isPSD, but S²−T²=[[4,5],[5,6]] has determinant−1. We use only the resolvent-integral square-root FORM argument, with its domains; no A^(3/4)=H^3/2 identity is inferred.

Scalar compactness does not imply tensor compactness: A:R→Lʳ(I), A1=1 is rankone, but (A⊗Id_G)(1⊗e_j) has pairwise distance√2 for an infinite orthonormal family inG. Scalar averaging of thisA is nevertheless exact. This is why mean/operator bounds below require a tensor NORM estimate, not tensor compactness.

##2. The actual potential, uniqueness and the fixed-R lift (178)

Take L_n=L_qn^E→L. The zero columns persist; there is M:H^1/2→H^-1/2 with L(u,v)=(0,Mu), and k=||L||=||M||: test the first column for the reverse norm inequality. Choose realχ_R∈Cc∞ equal1 nearK_R. Since M_nχ_R=V_n,

    ||V_n−V_j||_(H^-1/2) ≤ ||χ_R||_(H^1/2) ||M_n−M_j||.

Hence V_n→V inH^-1/2, real and supported inK_R (test outsideK_R). For compact smoothu, multiplication byu is bounded onH^-1/2. Thus V_nu→Vu there, while M_nu→Mu; consequently Mu=Vu ontests. Its extension to allH^1/2 is precisely the bounded mapM, not an independently asserted product of two arbitrary distributions. Density gives uniqueness. Also Mχ_R=V, so the potential is independent of the chosenχ_R. The real symmetric pairing extends to

    v_V(u,w)=<Mu,w>,   |v_V(u,w)|≤k||u||_(H^1/2)||w||_(H^1/2).

The complex extension is Hermitian and preservesk: ||M(a+ib)||²=||Ma||²+||Mb||². Its diagonal is the sum of the real diagonals.

The corresponding F operators are L_n^F(e,c1,c2)=(0,M_ne1+c1V_n,0,0). Their differences have norm at most(1+||χ_R||_(H^1/2))||M_n−M_j||. They therefore converge to a compactL_F in the precise oldF closure, with L_Fi=iL, i:E→F. This FINITE-R lift can cost arbitrarily largeχ_R constants asR grows. It supplies identification only; k_F orχ_R is never substituted into the uniformE estimates below. Both constant response columns of the eventual flow remain, although the instantaneous forcing has onlyc1.

##3. Closed H¹ form and its exact budgets

Choose K≥max(1,k), c=2+K² and L_K=3(1+K²). For u∈H¹ write b=||u||₂,z=||u||_(H¹). Fourier Cauchy–Schwarz gives ||u||_(H^1/2)²≤bz. Therefore

    |v_V(u,u)|≤Kbz≤z²/2+K²b²/2,
    q_V(u)=||∇u||²−v_V(u,u)=z²−b²−v_V(u,u),
    z²/2+(1+K²/2)b² ≤ q_V(u)+cb²
      ≤ 3z²/2+(1+3K²/2)b² ≤ L_K z².                    (1)

The shifted norm is equivalent to the COMPLETEH¹ norm. The form is densely defined, Hermitian and semibounded, and is CLOSED in the sense of Teschl printedp80. Theorem2.14p81/(2.63) represents it by a unique selfadjointH_V. Its operator domain consists of u∈H¹ for which the formfunctional is represented by a vector inL²; this is not a declaration D(H_V)=H². Shifting the same form does not change that representative.

Teschl3.6p109/(3.51)–(3.53) gives the PVM and form integral. For A=H_V+c, (1) and z≥b imply q_A≥(3/2+K²/2)b²≥2b². A nonzero bounded spectral slice below2 would supply a unitD(A) vector contradicting this form bound. Thus A≥2 spectrally, and

    D(A^1/2)=H¹,   (1/2)B0≤A≤L_K B0 AS FORMS onH¹.       (2)

No smoothness ofV, H² domain or ground eigenstate was used.

##4. Ordered resolvents, quarter domains and the negative phase

For positive selfadjointT,S≥1 with common formdomain and q_T≤q_S, square completion in the form norm gives, for t>0,

    <f,(T+t)^−1 f>
      =sup_u {2Re<f,u>−q_T(u)−t||u||²}
      ≥<f,(S+t)^−1 f>.                                  (3)

The maximizer is (T+t)^−1f∈D(T), so the supremum identity applies on the entire formdomain. Hence I−t(T+t)^−1≤I−t(S+t)^−1. The scalar identity

    √x=(1/π)∫₀∞ t^−1/2 x/(x+t)dt

follows by t=xv². Positive spectral integration/Tonelli gives the corresponding extended quadratic forms. If u∈D(S^1/4), itsS integral isfinite, so theT integral isfinite; hence u∈D(T^1/4) and ||T^1/4u||²≤||S^1/4u||². This derives the DOMAIN INCLUSION as well as the inequality; it is not multiplication of noncommuting operators.

Apply this to(B0,2A) and(A,L_KB0) in(2). The two inclusions give

    D(A^1/4)=H^1/2,
    2^−1/4||u||_(H^1/2)≤||A^1/4u||₂≤L_K^1/4||u||_(H^1/2). (4)

For v∈L², its dual norm against ||A^1/4u|| is ||A^−1/4v||: Cauchy–Schwarz gives≤, and u=A^−1/2v (then normalized) gives equality. Completion is thereforeH^-1/2, with inverse comparison constants. Put M_K=L_K^1/4; sinceK≥1 alsoM_K≥2^1/4. Thus

    ||(u,v)||_EA²=||A^1/4u||²+||A^−1/4v||²,
    M_K^−1||z||_E≤||z||_EA≤M_K||z||_E,
    M_K²=√(3(1+K²))≤2(1+K).                              (5)

All products invoked here are justified by the PVM calculus or bounded maps on these declared domains. We claim neither D(A^3/4)=H^3/2 nor any equality of the operator domain withH².

##5. Real Rayleigh bottom, spectral support and escape trials

For ||u||₂=1, (1) gives q_V(u)≥z²/2−1−K²/2≥−K². Choose a fixed compact smooth unit bumpg. Dilate to g_L(x)=L^−d/2 g(x/L), then translate its ENTIRE support offK_R. Its potential pairing iszero and its kinetic energy isL^−2||∇g||²→0. Therefore

    −K²≤β(V):=inf_(realH¹,||u||₂=1) q_V(u)≤0.             (6)

A complex diagonal splits into its two real diagonals, and normalization gives a convex combination, ignoringzero parts. Hence real and complex infima agree; Cc∞ realtrials are dense for this form becauseH¹ convergence givesH^1/2 convergence.

The spectral form integral is bounded below by the spectral support infimum. Conversely arbitrarily small bounded PVM slices near a supportpoint give form tests with values arbitrarily close to it. Such normalized slices also give approximate eigenvectors, excluding a bounded inverse at supportpoints. Off the closedPVM supportΣ, (h−z)^−1 and h/(h−z) are bounded onΣ; set themzero outsideΣ. Teschl's Borel calculus maps the inverse intoD(H_V) and supplies both inverse identities on their proper domains. ThusΣ is the spectrum and β(V)=inf specH_V. Put λ=√(−β); then0≤λ≤K and h+c≥2 onΣ. Compact support supplies the escape trial; no ground eigenvalue or positivity ofV is required.

##6. The actual weighted spectral wave and its uniform constant

For spectralh define C_t(h),S_t(h) as cos(t√h),sin(t√h)/√h ifh>0, as1,t ifh=0, and cosh(t√−h),sinh(t√−h)/√−h ifh<0. In the EA isometry diag(A^1/4,A^−1/4), the phase matrix is

    [ C_t(h)                 √(h+c) S_t(h) ]
    [ −h S_t(h)/√(h+c)       C_t(h)        ].             (7)

Forh≥0, |C_t|≤1, |S_t|≤min(t,h^−1/2). The upper offdiagonal is≤1+√c t, the lower≤1; atzero they are√c t,0. For β≤h=−r²<0, r≤λ≤K and c−r²≥2. Thus

    |C_t|≤e^(λt), |S_t|≤t e^(λt),
    √(h+c)|S_t|≤√c t e^(λt),
    |h S_t|/√(h+c)=r sinh(rt)/√(c−r²)≤K e^(λt).

Since√c≤2K, EVERYentry is≤2(1+K)(1+t)e^(λt). A2x2matrix with entry boundB has Hilbert operator norm≤2B. Set the functionszero offΣ before bounded Borel calculus. Teschl3.1–3.2 then gives a bounded matrix onEA; the condition-number cost(5) yields

    ||P_V^E(t)|| ≤ 8(1+K)²(1+t)e^(λt),  t≥0.             (8)

This is an E-only estimate. Negative times use|t| in the same bounds. Scalar addition identities give the group; uniformly bounded-on-finite-horizon spectral domination gives strong continuity. The same conjugated matrix applies to D(A^1/2)×L² and D(A)×D(A^1/2): multiply the two coordinates by A^1/2,1 or A,A^1/2 respectively. Spectral cutoffs justify the domains and graph continuity. No operator-norm continuity of the free group or unmasked groundstate is asserted.

##7. D(H_V)⊂H^3/2, graph-core Duhamel and identification (164)

Teschl2.14/(2.63), tested oncompact smooth functions, gives H_Vu=−Δu−Vu distributionally foru∈D(H_V). Suchu∈H¹ and Vu=Mu∈H^-1/2. Hence

    B0u=H_Vu+Vu+u∈H^-1/2,
    D(H_V)↪H^3/2.                                      (9)

This is graph-continuous. Indeed (1) gives ||u||_H¹²≤2<Au,u>≤||Au||²+||u||², and

    ||u||_H^3/2=||B0u||_H^-1/2
      ≤||H_Vu||₂+||u||₂+k||u||_H^1/2
      ≤C(K,c)(||Au||₂+||u||₂).

The RHS distribution was only shown inH^-1/2; replacing it byL² and invoking anH² domain theorem would be unjustified.

The freeE group has generator A0(u,v)=(v,Δu) onH^3/2×H^1/2. Fourier cutoffs differentiate its matrix with graph-norm domination. Conversely anE strong generator derivative has these distributional components, requiringv∈H^1/2 andΔu∈H^-1/2; together withu∈H^1/2 this yieldsu∈H^3/2. Thus the generator domain is exact, with no operator-norm differentiation.

Start spectral data in D(A)×D(A^1/2)=D(H_V)×H¹. By(7) on the graphlevels and PVM cutoffs1_[1,n](A), z(t) is continuous there and C¹ inH¹×L², with u_t=v,v_t=−H_Vu. Teschl3.2/(3.29)–(3.33) justifies multiplication of the unbounded spectral factors on these domains; uniform finite-horizon tail domination removes cutoffs. By(9), z is continuous inD(A0), C¹ inE and

    z_t=A0 z+L_E z.

The strong-group chain rule on this graphdomain gives

    S_E(−t)z(t)=z(0)+∫₀ᵗ S_E(−s)L_Ez(s)ds,
    z(t)=S_E(t)z(0)+∫₀ᵗS_E(t−s)L_Ez(s)ds.               (10)

Graphdata are dense inE: D(A) is dense inD(A^1/2)=H¹ by spectral cutoffs, andH¹ is dense in bothH^1/2 andH^-1/2. Finite-horizon bounds for the two groups and boundedL_E extend(10) by dominated Bochner integration to everyE datum. Picard iteration bounds the nth difference by C_T^(n+1)k^nT^n/n!, proving Volterra uniqueness. Thus the spectral wave is the ACTUAL bounded-perturbation physicalE wave. No D(A^3/4) identity or roughH² assertion is needed.

At fixedR the lift from§2 has this SAME closedform, so uniqueness of the form representative gives the sameH_V even if its oldF construction used a larger shiftc_F. On bounded spectral cutoffs both waves use the same C_t(H_V),S_t(H_V); boundedness/density extends equality toE. The qualitative lift identifies the old physical/Young construction; neither its norm norχ_R appears in(1)–(8).

##8. Both constant columns, compact conjugation and Young equality

OnF boundedL_F and strongly continuousS_F define a unique statewise Duhamel flow by the same factorial Picard bound, with consistent finite horizons. Its constant coordinates are(c1+tc2,c2). ItsE component is EXACTLY

    P_V^E(t)e+∫₀ᵗP_V^E(t−s)(0,V(c1+sc2))ds.             (11)

Substitute theE Duhamel formula under this integral and use boundedE-valued Fubini on the finite time triangle; this solves the fullF equation, so uniqueness identifies it. The c2 response is notzero: it enters throughsc2 even thoughL_F itself has no directc2 column. For the oldF norm letK_F≥max(1,||L_F||); then||V||_H^-1/2≤K_F. Using(8) withK_F and ∫₀ᵗ(1+t−s)(1+s)ds=t+t²+t³/6≤(1+t)³ gives

    ||P_V^F(t)||≤13(1+K_F)³(1+t)³e^(λt)
                 ≤16(1+K_F)^4(1+t)³e^(λt).             (12)

This recovers164's sufficientF bound, not anR-uniform estimate.

For a compactL and a strongly continuous groupS on a Hilbertspace, strong continuity ofS andS* plus finite-rank approximation give norm continuity of S(−t)LS(t). For rankone terms it is continuity of the two vectors; uniform boundedness on finite horizons handles compact tails. Hence D(t)=∫₀ᵗS(−s)LS(s)ds is operator-norm C¹, in particular Lipschitz. The linear Young equation driven byD is the ordinary interaction equation with derivativeS(−t)LS(t). Its unique solution from107 is the interaction form of the Duhamel flow. This applies to the actual compactE class and fixedR compactF lift; it does not assert norm continuity of the free physical group, or a norm-continuous interaction for every noncompact boundedL.

##9. Uniform real Rayleigh/rate continuity (179)

Take V,W in the actualE class with operator norms≤K, K≥1, and d=||L_V−L_W||. Choose a unit real epsilon-minimizer forW,0<epsilon≤1. Sinceβ(W)≤0, q_W(u)≤1. The sharper bound q_W(u)≥z²−1−Kz implies z²−Kz−2≤0, hence z≤K+2. The multiplier difference changes its form by at most

    |q_V(u)−q_W(u)|≤d||u||_H^1/2²≤(K+2)d.

Thusβ(V)≤β(W)+epsilon+(K+2)d; let epsilon down0 and reverseV,W. Consequently

    |β(V)−β(W)|≤(K+2)d,
    |λ(L_V)−λ(L_W)|≤√((K+2)d).                          (13)

The second line uses |√x−√y|≤√|x−y| for x,y≥0 and includeszero rates without division. Realcompact smooth unit trials are dense in the realH¹ unit sphere; continuity ofv_V onH^1/2 makes their Rayleigh supremum the same. Therefore

    λ(L)=sup_(realCc∞,||f||₂=1) √((v_V(f,f)−||∇f||²)_+),
    λ(L)≤max(1,||L||).

No eigenfunction atβ and no unmasked groundstate is needed. All constants in(8),(13) use the actualE norm, notF or fixedR cutoffs.

##10. Completed means: separate the three maps and their norms

For the actual model fix s with α/4<s<1/2. The earlier physical fractional-product input is ||fg||_Hsp≤A_s||f||_Hs||g||_Hs, A_s=C_s²√R_sp. It is a stated proved INPUT here, not a consequence of179. Its finiteness for the original covariance precedes the intrinsic comparison. The uniform cutoff Fourier kernel is bounded by2^(|σ|/2)(2π)^(-d/2)|hatη_R(ξ−ζ)|<ξ−ζ>^|σ|. Since hatη_R(q)=Rᵈhatη(Rq), its L¹ norm is≤the fixedM_σ from source150. Thus the actual spatial row

    k_R(z,w)=(η_R z1)(η_R Λ^−1 w2)

obeys ||k_R(z,w)||_Hsp≤M0||z||_E||w||_E, M0=A_s M_(1/2)². Here Λ^−1:H^-1/2→H^1/2 is an isometry and H^1/2↪H^s contracts. Covariance-Hilbert Cauchy–Schwarz gives the ACTUAL T_R:H_sp→K(E), ||T_R||≤M0 uniformlyR≥1. This row identifies on smoothq the potential m_R(Γ*q): the mask occurs ONCE AFTER covariance convolution. Completion gives the same map, not Γ*(m_R q), an arbitrary raw-quotient masking map or a new field. Compact values at fixedR come from the earlier actual spatial-map construction; uniform boundedness is not uniform-radius compactness.

Let I=(0,1), K_a(t,u)=|t−u|^−a. Fix the source's one exponent2<r<2/a (for block uses also (1−θ)^−1<r, with the sameθ>1/2). There are three DIFFERENT maps:

* The Bochner inclusion 𝒥_G:L²(I;G)→H_t⊗G obeys
  ||𝒥_GF||²=∫K_a(t,u)<F(t),F(u)>dtdu≤K0||F||²_L²,
  K0=2^a/(1−a), by the scalar row integral and Schur. First construct on smooth finite tensors, then dense Bochner simple fields. Absolute bilinear Schur continuity identifies the limit. No surjectivity of this inclusion is claimed.
* The completed covariance map C_t:H_t→Lʳ(I) is the actual scalar map from the time package. For any real HilbertG,

      ||C_t⊗Id_G||_(H_t⊗G→Lʳ(I;G))≤c_t:=||C_t||.

  Indeed for finite Φ=Σf_j⊗e_j with orthonormale_j, finite standard real normalsγ_j and m_r=E|γ|^r give

      m_r∫(Σ|C_tf_j|²)^(r/2)
        =E||C_tΣγ_jf_j||_Lʳ^r
        ≤c_t^r E||Σγ_jf_j||_Ht^r
        ≤c_t^r m_r(Σ||f_j||²)^(r/2).

  The last step diagonalizes the finite covariance and uses convexity at r/2≥1 on its normalized eigenvalues; the zero trace case isdirect. Cancelm_r and complete by finite-tensor density. No spatial dimension/rank factor or Hilbert-valued Gaussian noise is introduced. This is a NORM bound, not compactness of the tensor.
* The operator mean is 𝒯_R=T_R(C_t⊗Id_Hsp), so

      ||𝒯_R Φ||_(Lʳ(I;K(E)))≤C_mean||Φ||_HI,
      C_mean=M0 c_t,                                    (14)

  uniformlyR. c_t alone does not bound the physical operator mean; nor is√K0 the norm ofT_R.

For F∈L²(I;G), Schur first makes K_aF anL² Bochner field. On smooth finite tensors it equals(C_t⊗Id)𝒥_GF. ApproximateF inL². The integral converges inL² by Schur; the completed tensor image converges inLʳ with boundc_t√K0||F||_L². Since r>2 on the unitinterval, uniqueness of theL² limit identifies the two versions. Thus the integral is inLʳ for THIS fixedr, not because Schur alone gains arbitrary integrability. An arbitrary Φ∈H_I still need not have a literal fieldΦ_t.

Dense finite smooth raw tensors have means in the closed real linearclass V_E,R almost everywhere. TheLʳ operator-norm convergence from(14) has an almost-everywhere convergent subsequence, so closedness places each completed mean in the SAMEclass a.e. Strong measurability follows from the actual Bochner field and boundedT_R. For a fixed cellJ, its Bochner average remains inV_E,R: finite simple sums lie there and its norm limit does too. Every such average therefore has the unique supportedV, real symmetric pairing, bound(8) and rate(13). For fixedf,g, evaluation L↦v_L(f,g) is bounded linear, so it commutes with this average. FixedR χ_R may identify the averaged distribution, but is not needed to estimate it. This makes the mean/average hypotheses used by201 literal.

For completeness, scalar compactness ofC_t plus averaging contractions gives ω_n=||(P_n−I)C_t||→0, by a finite net on its compact unit-ball image. Tensor norm control and boundedT_R give ||P_nW_R−W_R||_Lʳ≤M0||Φ||ω_n uniformlyR. For two actual mean fields, (13) with K(t)=max(1,||W1(t)||,||W2(t)||), followed by time Cauchy–Schwarz, yields

    ∫|λ(W1)−λ(W2)|
      ≤√(3+||W1||_L¹+||W2||_L¹) √(||W1−W2||_L¹).        (15)

Thus on ||Φ||≤M the averaging error is≤√(3+2C_mean M)√(M0 M ω_n). This uses no tensor or growing-radius compactness. Choosing K=max(1,||L||) in(6), not an arbitrary largerK, also gives λ(L)≤1+||L|| and Rate_R(Φ)≤1+C_mean||Φ||. All mean constants may depend on the fixed original covariance/amplitude, a,r and rootprofile; they are independent ofR and any trial partition/gradient.

##11. Exact imported inputs and remaining scope

The held Teschl SECOND EDITION2014 excerpts used here are: printedp80/physicalPDF92 (closed form definition), Theorem2.14/(2.63) printedp81/physical93 (closed semibounded form representation); Theorems3.1–3.2/(3.18)–(3.33) printedpp102–104/physical114–116 (bounded/unbounded Borel calculus, spectral domination and product domains); Theorem3.6/(3.51)–(3.53) printedp109/physical121 (spectral/form representation). Their hypotheses were checked above. Those named book theorems remain imported, not re-proved here.

Teschl10.2 printedp258 (H² domain/essential spectrum for its FUNCTION-potential hypotheses), max-min4.12/4.13 and ground10.13 printedp273 are NOT inputs to this rough-domain argument. They apply elsewhere to smooth compact potentials after an actual negative eigenbottom is established, and cannot be used to declare H² or an unmasked groundstate here. The form/domain/resolvent/quarterphase and graph-core application steps above are the owned calculations.

For Γ=0 the actual covariance space H_sp=H_I={0}, T_R=C_mean=0 and the actual potential class is{0}. E itself remains the nonzero phase space. H_V=−Δ, β=λ=0, the wave isfree and its constantF coordinates evolve as(c1+tc2,c2). No nonzero Gaussian, positive cost or eigenbottom assumption is invoked. White/singular angular covariances require no density at any step: they enter only the already typed physical product/mean construction, while the wave argument uses the resulting actual multipliers. Signed potentials are allowed throughout; no positive covariance/PSD comparison of nonlinear waves was inferred.

All estimates and identities here are at their stated fixedR or uniformE scope. No globalR F norm, literal pointwise rough noise potential, arbitrary H^-1/2 multiplier, H² domain equality, tensor compactness or unmasked ground eigenfunction has been added. This replay changes no source bytes and supplies no review verdict or completion credit.
