# Full current037/038 supplement: exact reuse and application checks

AUTHOR working only, scientific source af97. The complete current037/038 statements, proofs and setup were read, not just the clauses consumed by039–048. Their FULL existing mathematical reconstructions are literally compiled in complete-reused-clauses.json: B-phase-root-working§037 and§038 plus its finite mean-term control. These are authored calculations, not a source-presence/old-grade certificate. The frozen039–048 bundle is unchanged. No MAIN/HIGH/whole37B acceptance, source/model/runtime/Git/CLI/config action or new theorem follows.

##1. Exact claim class; no hidden model reduction

Source setup main4787–4806: static spatial Gamma is a nonnegative, even, positive-definite tempered Radon covariance on R³ withGamma(rA)=r^(3−alpha)Gamma(A),0<alpha<2. Spectral convention isGamma=integral exp(i xi.x)mu(dxi), unnormalized Fourier fhat=integral exp(−i xi.x)f(x)dx; phase Plancherel measure is(2pi)^−3deta. No Hthree, angular density, Riesz-only representation, full-dimensional spectral support or finite original spectral total is assumed. Neither036's H1 energy identification nor its C23 quartic theorem is a premise.

This class includes EVERY original admissible R³ spatial covariance. Its static statements are broader than the original fixed-positive-alpha0 temporal model in that they do not requirealpha+alpha0<2 or even introducealpha0; all0<alpha<2 are admitted statically. They are narrower in DIMENSION than the full original d1/2/3 goal: the physical trace proof below is the R³ sphere calculation. Source044 separately supplies the dimension-free resolvent/column facts needed by the full interval upper chain. Do not infer a d1/d2 D_Gamma formula from the presence of this source.

The source sentence “no origin atom” followsmu(B_r)=Vr^alpha and concerns the SPECTRALmu. Sincealpha>0 andmu(B1)<infinity,mu({0})=0. In this R³ class the physicalGamma also has no point atom by its positive degree3−alpha>1, but may be singular on planes or other sets; this is not a density assumption. The ORIGINAL d1 white covariance c delta0 has physical origin massc and is allowed globally, while its spectralmu=c dxi/(2pi) has no origin atom. Nothing here excludes it from the project; it is not a three-dimensional alpha<2 point-white covariance (R³ delta0 would havealpha3).

Keep distinct physicalM=Gamma(B1) and spectralV=mu(B1). They are not identified with each other or a variational quantity. Define

    R_alpha=alpha pi V/[2sin(pi alpha/2)],
    c_Gamma=(3−alpha)M/(4pi),
    b_alpha=2^alpha+3^(2−alpha)/(2−alpha),
    D_Gamma=c_Gamma b_alpha.

All are for the ACTUAL covariance amplitude. Gamma0 givesmu0,R=D0 andzero positive-order terms directly. No division byR is used in037/038. Constants need not stay uniform asalpha approaches0/2 orlambda approaches0.

##2.037: spectral resolvent and physical trace are BOTH fully covered

### Spectral part

For everylambda>0,q inR³, physical nonnegativity/evenness and Schwartz Gaussian pairing give

    integral exp(−s|q+xi|²)mu(dxi)
      =integral p_(2s)(x)exp(iq.x)Gamma(dx)
      ≤integral p_(2s)(x)Gamma(dx)
      =integral exp(−s|xi|²)mu(dxi).

No angular density appears. Integrate exp(−lambda²s)ds and use nonnegative spectral Tonelli. Radial STIELTJES massmu(B_r)=Vr^alpha gives

    sup_q integral mu(dxi)/(lambda²+|q+xi|²)
       ≤alpha V integral_0^infinity r^(alpha−1)/(lambda²+r²)dr
       =R_alpha lambda^(alpha−2).

This is source037 LF4824–4842 and FULL existing root-working§037. Independent-upperA1 rederives the same scalar resolvent in all original dimensions; it does NOT supply the following trace calculation. Physical origin atoms were not excluded in that dimension-free Gaussian argument.

### Physical trace part

At POSITIVEepsilon, Gamma_epsilon=p_(2epsilon)*Gamma is a bounded nonnegative smooth function with Gaussian-weighted spectralmeasuremu_epsilon=exp(−epsilon|xi|²)mu. Its finite total isv_epsilon=V Gamma_E(1+alpha/2)epsilon^(−alpha/2). Thus Fourier Fubini is absolutely justified for

    T_epsilon(tau,q)=integral exp(iq.x)Gamma_epsilon(x)G_tau(dx)
       =integral Ghat_tau(q+xi)exp(−epsilon|xi|²)mu(dxi), tau>0.

The measureGamma_epsilon(x)G_tau(dx) is finite NONNEGATIVE, hence|T_epsilon(tau,q)|≤T_epsilon(tau,0). This is a Fourier-of-positive-measure bound, not positivity of T at everyq or of an arbitrary-phase evolution.

F=G_tau*p_(2epsilon) is radial Schwartz. Homogeneity of the PHYSICALmeasure gives its radial pushforward (3−alpha)M r^(2−alpha)dr, so

    integral F Gamma=c_Gamma integral F(x)|x|^(−alpha)dx.

Only RADIAL test integrals are equated; it is NOT an assertionGamma=c_Gamma|x|^(−alpha)dx as measures. Apply nonnegative Fubini to obtain

    T_epsilon(tau,0)
      =c_Gamma[p_(2epsilon)*(G_tau*|.|^(−alpha))](0)
      ≤c_Gamma sup_z(G_tau*|.|^(−alpha))(z).

The R³ wave measure has mass tau and sphere normalization1/(4pi tau). Direct integration forr=|z|>0 gives

    (G_tau*|.|^(−alpha))(z)
      =[(tau+r)^(2−alpha)−|tau−r|^(2−alpha)]/[2r(2−alpha)].

At r0 use its limit tau^(1−alpha). Forr<tau/2 bound by2^alpha tau^(1−alpha); forr>2tau bound bytau^(1−alpha); on the middle region use3^(2−alpha)tau^(1−alpha)/(2−alpha). Thus|T_epsilon|≤D_Gamma tau^(1−alpha), uniformlyepsilon,q. The sphere singularity atr=tau is integrable precisely becausealpha<2. The complete root-working§037/source037 LF4844–4878 includes all these steps. No physical heat pointwise monotonicity, peak-at-zero wave bound, Gamma density or unregularized product of two singular measures is used.

A useful falsification: foralpha3/2,tau1 the Riesz convolution has value1 atr0 butsqrt2 atr1. The wave convolution need NOT maximize at the origin. This does not contradict the valid spectral Gaussian/resolvent maximum above. D_Gamma uses a uniform wave supremum, not the false centre-only assertion or H:spatial-maximum.

##3.038: exact general-lambda Born term with BOTH phase entries

The actual data are deterministic real Schwartz f,g andN²=||f||2²+||A_lambda^−½g||2²,A_lambda=lambda²−Delta. Positive-width static W_epsilon has covarianceGamma_epsilon; it is the SAME field throughout both Duhamel insertions. At fixedepsilon its second/fourth Gaussian moments, G_t's finite measure mass and scalarC_t L² contraction justify the actual phase Bochner/Fourier integrations. Its point variance may diverge asepsilon→0; it is used only for existence, not the final uniform constants.

Put e_lambda(eta)=|fhat|²+|ghat|²/(lambda²+|eta|²). The free position coefficient obeys

    |a_s(eta)|²≤(1+lambda²s²)e_lambda(eta),

because the TWO-input coefficient vector has square normcos²(sq)+(1+lambda²/q²)sin²(sq)=1+lambda²sin²(sq)/q². Its zero-mode value is1+lambda²s². Omitting the velocity input would lose this calculation.

Under the phase isometry(u,v)→(u,A_lambda^−½v), the TWO-output vector is

    k_tau(r)=(sin(tau r)/r,cos(tau r)/sqrt(lambda²+r²)),
    |k_tau(r)|²=[1+lambda²sin²(tau r)/r²]/(lambda²+r²)
                  ≤(1+lambda²h²)/(lambda²+r²),0≤tau≤h.

Continuous zero-frequency values are retained. Gaussian covariance+Plancherel gives EXACTLY

 E||Z1(h)||lambda²
 =(2pi)^−3 integral deta integral mu_epsilon(dxi)
       |integral_0^h k_(h−s)(|eta+xi|)a_s(eta)ds|².

This is a STATIC field, so the time expression is a squared integral, not a temporal-white isometry. Time Cauchy–Schwarz and the two coefficient bounds give h²(1+lambda²h²)² e_lambda/(lambda²+|eta+xi|²). Nowmu_epsilon≤mu in this POSITIVEspectral integral and037's resolvent imply

    E||Z1(h)||lambda²
       ≤R_alpha h²lambda^(alpha−2)(1+lambda²h²)²N².

The proof is GENERALlambda,h>0. No relationlambda h=1 has yet been imposed. This full Born calculation is source0384930–4970 and root-working§038, not a consequence of a scalar first-response norm alone.

##4.038: the separate mean contraction and first variance coefficient

Inside E Z2, expectation of W_epsilon(x)W_epsilon(y) producesGamma_epsilon(x−y)G_(s−r)(x−dy). Its convolution multiplier isT_epsilon(s−r,eta) (even sign immaterial). Therefore its L² operator norm is≤D_Gamma(s−r)^(1−alpha), without assigning a favourable sign to the subsequent phase inner product.

The outputk is bounded bysqrt(1+lambda²h²)/lambda; free positionw0(r) bysqrt(1+lambda²h²)N. Minkowski and the exact ordered integral

    integral_0^h ds integral_0^s dr (s−r)^(1−alpha)
       =h^(3−alpha)/[(2−alpha)(3−alpha)]

yield the OTHER general-lambda estimate

    ||E Z2(h)||lambda
      ≤D_Gamma(1+lambda²h²)h^(3−alpha)N/
           [lambda(2−alpha)(3−alpha)].

alpha<2 is exactly the local lag-integrability condition. This is an actual SAME-field self-contraction, not pure-Wick orthogonality or an independent-next-field substitution. Both Born and mean estimates survive allpositiveepsilon without dependence onv_epsilon.

The coefficient ofsigma² inE||Z0+sigma Z1+sigma²Z2||lambda² is exactly

    K_epsilon=E||Z1||lambda²+2Re<Z0,EZ2>lambda.

The mean term is not optional. Atlambda=1/h, Born≤4R_alpha h^(4−alpha)N²; mean≤2D_Gamma h^(4−alpha)N/[(2−alpha)(3−alpha)]; free||Z0||≤sqrt(e)N. Thus

    |K_epsilon|≤[4R_alpha+4sqrt(e)D_Gamma/((2−alpha)(3−alpha))]
                    h^(4−alpha)N².

This is a FIRST coefficient, not all-order phase growth or covariance monotonicity. The complete existing root-working§038 includes the same general estimates, specialization and exactmean control. B-phase source-support is a useful map but not the full derivation; independent-upperB1 is a fixed-cutoff/finite-degree identification argument and does not replace these Born/mean calculations.

##5. Free growth in BOTH directions and actual consumer boundaries

For Schwartz free data, differentiateE(t)=||u||²+<A_lambda^−1v,v>,u'=v,v'=Delta u. The Delta terms cancel, leaving

    E'=2lambda²Re<A_lambda^−1v,u>,
    |E'|≤2lambda||u|| ||A_lambda^−½v||≤lambda E.

Hence ||S0(t)||lambda≤exp(lambda|t|/2), t inR. Density extends the bounded free group to the X_lambda completion; tensoring with a Gaussian/past Hilbert factor is harmless because this is a DETERMINISTIC free map. This is not CP applied to an unbounded operator and not an assertion of operator-norm continuity. Atlambda h≤1,||S0(−h)||≤sqrt(e), as required by043. The scalarcosineC_t is an L² contraction; the TWO-entry phase is not. Zero-frequency pure velocity gives norm ratio sqrt(1+(lambda h)²)>1, which falsifies a free contraction shortcut.

037 spatialR is used by040;044 independently rederives the all-dimensional version for047/048.038's general Born AND mean clauses are used by043, whose interactions may havelambda h<1; thelambda=1/h specialization alone cannot supply that application.042/048 reuse only the free growth/local finite-degree calculations as needed, not038's first variance as an all-order premise. No old full-parent stamp is supplied by these local uses; this supplement checks the FULL037/038 source claims separately.

The Born/mean noise estimates are stated for deterministic initial phase. An independent random phase can be handled by tensoring/conditioning on the independent past where the later result explicitly does so. An initial phase already depending on the CURRENTfield cannot silently use the same deterministic variance estimate; occupied Gaussian/Fock bounds are needed. The free deterministic group bound itself has no such independence restriction.

Finite Gaussian-mode or Fourier-band compression can destroy physical covariance positivity/stationarity. The037 trace/038 calculation is for the ACTUAL full smoothed field, not an asserted positive physical compressed covariance. In043, the actual Zn_epsilon are already identified after042's cutoff passage.047/048 instead use their joint-Hilbert bounded complex/Fock argument, not an unjustified compressed-trace or independent successive-block shortcut.

##6. Concrete singular case, endpoint controls and status

Take the admissible R³ plane covarianceGamma=delta0(dx1)dx2dx3,alpha1. Thenmu=(2pi)^−1dxi1 tensor delta0(dxi2)tensor delta0(dxi3), V=1/pi whileM=pi. ThusR=1/2,c_Gamma=1/2,D_Gamma=5/2; physical/spectral masses are visibly DIFFERENT. The shifted resolvent is1/[2sqrt(lambda²+q2²+q3²)]≤1/(2lambda). Gamma_epsilon(x)=p_(2epsilon)^(1)(x1); pushing the sphereG_tau ontox1 gives(1/2)1_[−tau,tau]dx1, so

    T_epsilon(tau,0)=(1/2)erf(tau/(2sqrt(epsilon)))≤1/2
                      ≤D_Gamma tau^0.

This is a genuine singular/non-density covariance test; the source's radial-test method covers it without assumingGamma is isotropic. d1 physical-white origin atoms remain allowed globally as described in§1. Gamma0 givesZ1=Z2=K0; at h0 take these zero terms and S0(0)=I directly, never evaluatelambda=h^−1. Tau0 is a null Duhamel boundary; defineG0=0, not0^(1−alpha) whenalpha>1. No unregularized trace product of singular measures or zero-smoothing phase limit is asserted.

UnderGamma→bGamma, M,V,R,D allscale byb; Z1 bysqrt(b), E Z2 andK byb, preserving actual amplitude. The exact finite mean/velocity control from the existing note gives Born5h4/4 plusmean h4/12=4h4/3 atlambda1/h forw''=sigma Z w,data(1,0). This is a finite algebra test OUTSIDEthe original spatialalpha>0 class, not an SPDE estimate. Dropping the velocity or mean terms fails that test.

No actual gap was found in the full037/038 deductions under their precise STATICR³ hypotheses. This completes the two exposed source inputs as author working, not native review acceptance. The bookkeeping is21static/alternative OWN+10core039–048+4upper OWN+THESE2=37B OWN;35groups alone were not fullB37. Alloriginal214/240/13/model/C2 and MAIN/Kimi/visual/sourcepixels/cold/project gates remain unchanged and open. The frozen originalcore is untouched.
