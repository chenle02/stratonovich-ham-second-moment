# Actual point transfer185–189: complete author replay

This replays existing scientific af97, not a new theorem, source change, review or grade. The five complete statements/proofs and their actual input contracts were read; exact delimiters, modules and hypotheses are bound separately. All214OWN/240formal/13joins and original model/future gates remain assigned.

## 1. Fixed parameters and actual inputs

Let a=alpha0 in(0,1), alpha+a<2, d=1,2,3 and the original nonnegative even PD homogeneous tempered Radon Gamma (including amplitude, singular/angular spectra and d=alpha=1 white). Initially Gamma is nonzero. Fix0<delta<1 and set

    L=delta^-1, R=L+2, T_delta=delta^(-1/kappa),
    kappa=(4-alpha-a)/(3-alpha)=1+(1-a)/(3-alpha)>1,
    g=delta^((1-a)/2), Gamma_delta=g^2 Gamma.

Choose the source's real even root eta with0<=eta<=1, equal1 onB1, zero offB2; psi(x)=eta(x/R), m=psi^2, z=(psi,0) in E=H^(1/2)×H^(-1/2), D=B1 and v_d=|D|. The datum psi is NOT the larger cutoff used to extend the driver to F=E⊕R². Fix the093 strict tuple:0<gamma<min(1/2,(2-alpha)/2) and1/2<theta<beta<min(1-a/2,(3-a-alpha)/2). For the tube input fix theta<eta_t<beta_t in the same upper gap, an even Q with Q gamma>d, beta_t-eta_t-1/Q>0 and Q>2d/(1-a), and (1-theta)^-1<r_t<2/a, q_Y<=p_bl<2, where q_Y=1/theta. These choices exist by the strict gaps; eta_t is a time exponent, not the root eta. A smaller common theta>1/2 may identify earlier versions. q_Y<2 is not the intrinsic exponent3-alpha.

The following are actual proved local input contracts, not new external axioms or full-parent review credit:

*093/095/098: the literal same-W compact zero-start C^theta driver, uniform sqrt(p) source/residual path bounds at each FIXED(R,L), and actual L^p C^theta convergence for jointly Gaussian dominated retaining sources. Both phases/adjoint row and arbitrary relative noise widths are included. Sources/residuals need not be independent.
*099/100/104–109: positive-width source fields have jointly continuous spatial derivatives; the ordinary primitive has the actual source rows; F is a closed isometric extension with both constant-response columns, strong free groups and bounded localization; Young flow is locally Lipschitz with growth exp(C(1+driver norm)^q_Y). No density of E in F or free-group norm continuity.
*101–103/008: positive Green-measure Bochner chains, all Wick pairings with coefficient1 and widths-uniform summable order bounds q_n for each fixed model/horizon. Source point moments tend to the canonical point moment after Green-first removal, with arbitrary relative noise widths. This is a point-MOMENT statement, not unmasked noisy-wave convergence in E.
*165,173–176: a fixed compact Young driver gives endpoint norm at least its free norm>=1; the actual same-W E block tuple and restarted endpoint obey the coarse Gaussian radial bound. For B=1 its clock conditions cover every0<delta<1; an empty last cell is zero. Its endpoint is the very P_delta below, not an equal-law surrogate.119/125 give canonical scaling after fixed-order/absolute-series limits;126 supplies original canonical spatial stationarity.

These contracts are used at their stated domains. In particular neither193 nor any intrinsic C2 identity is an input. No rough point trace or global unmasked E/F solution is assumed.

## 2.185: closed E restriction, measurability and finiteness

The interpretation of F sends(e,c0,c1) to(e_displ+c0,e_vel+c1). Constants are not Sobolev vectors, so i(e)=(e,0,0) is a closed proper isometry. On F,

    S_F(t)(e,c0,c1)=(S_E(t)e,c0+t c1,c1).

Choose chi=1 onB_(2R+L+1), supported inB_(2R+L+2), and tildepsi=1 near supp(chi), as105 requires. For this larger extension cutoff and actual driver D_E=gM_R(W_fast),105 gives A_F=i D_E L_tildepsi, A_F i=iD_E and S_F(t)i=iS_E(t). Right localization proves A_F i=iD_E; range(A_F)⊂iE alone does not kill constants. Its two constant columns are iD_E(tildepsi,0) and iD_E(0,tildepsi), generally nonzero. The same identities hold for each retaining source.

Apply i to the E state Young sums. Their limits solve the F equation with initial ie, so Young uniqueness gives U_F(t,s)i=iU_E(t,s). Free conjugation gives P_F(t,s)i=iP_E(t,s). Thus

    ||P_E||<=||P_F||,
    sup_triangle||P_E^rho-P_E||<=sup_triangle||P_F^rho-P_F||.

This does not use density in F. The driver lives in a separable closed path span; the interaction Young map is continuous into uniform-triangle operator families. Physical conjugation V(t,s)↦S_F(t)V(t,s)S_F(-s) is a bounded linear map into bounded operator families, norm at most C_L². It therefore preserves strong measurability on the separable range, so endpoint norms/differences are measurable. S_F is only strongly continuous; physical flows need not be operator-norm continuous. Local Young Neumann inverses and the free inverse give invertibility on E.

For the source185 finiteness route, use the actual173–175 restart at B=1, R=delta^-1+2. Its support/CM map retains the original W_fast and sqrt(delta) covariance, not independent blocks. If b_delta=2E||X_delta||<infinity,175 gives

    E||P_delta||² <= integral_0^infinity (r/delta)
      exp{[A0+C_env r^q_Y-r²/2]/delta} dr,
    A0=C_env(1+b_delta^q_Y).

At these fixed parameters choose K>0 with4C_env<=K^(2-q_Y). On[0,K] the integral is at most K²/(2delta) exp{(A0+C_env K^q_Y)/delta}. On[K,infinity] it is at most4exp{(A0-K²/4)/delta}, by integrating -(d/dr)[4exp(-r²/(8delta))]. Both are finite. The fixed-parameter108 flow moment argument below independently gives the same finiteness; no point-transfer or fixed-mask asymptotic rate is borrowed. The actual D_E is compact-valued C^theta: every Young Riemann sum for U-I is compact, so its operator-norm limit is compact. Translations on E are unitary, tend weakly to0 and commute with S_E; a compact perturbation of S_E(L) therefore has norm at least ||S_E(L)||. The isometric velocity flip conjugates S_E(L) to S_E(-L), and the group law gives ||S_E(L)||>=1. This is165 at the actual fixed parameters. All constants here may depend on fixed delta; no F-norm growth-rate estimate is asserted.

## 3.186: actual pullback, operator convergence and uniform integrability

For a fast test f supported inside(0,L), define

    (T_delta f)(s,x)=delta^(a/2-1) f(s/delta,x).

The substitutions s=delta t,r=delta u in the raw covariance show ||T_delta f||_Hslow=||f||_Hfast: delta^(a-2) delta² delta^-a=1. Extend this isometry by completion (endpoint rows use their admitted completed labels, not an arbitrary raw indicator multiplier), set W_fast(f)=W(T_delta f), and use the SAME retaining source Y_(epsilon,tau) to define

    Y_fast(t,x)=delta^(a/2)Y_(epsilon,tau)(delta t,x),
    c_(epsilon,tau)=gY_fast=sqrt(delta)Y_(epsilon,tau)(delta t,x).

Testwise Y_fast(f)=Y_(epsilon,tau)(T_delta f).098 therefore gives source and full residual variances<=||f||² and residual variance→0. The retaining coupling may have a correlated heat residual; only the domination and actual joint Gaussianity are used.095 transfers these facts through the SAME deterministic operator coefficients. At fixed delta, g,R,L and the bounded F extension give A_F^rho→A_F in every finite L^p C^theta. This is a limit on the actual retaining space with given W, not just a law comparison.

Here is the UI step explicitly. Put X_rho=||A_F^rho||_Ctheta and X=||A_F||_Ctheta. For a finite fixed-parameter A, ||X_rho||_p,||X||_p<=A sqrt(p). Hence

    E exp(c X_rho²) <= sum_n (2e c A²)^n < infinity

uniformly in rho when2e c A²<1; the same holds for X. On a driver ball radius K, Young stability gives D_rho=||U^rho-U||_triangle<=L_K||A^rho-A||_Ctheta. Thus

    P(D_rho>epsilon)<=2H exp(-cK²)
       +(L_K/epsilon)^p E||A^rho-A||_Ctheta^p.

First send widths→0 at fixed K, then K→infinity. For every finite j, the inequality jC(1+x)^q_Y<=c x²+C_j (q_Y<2) and Young growth give uniformly bounded jth moments of U^rho and U. Therefore

    E D_rho^p <= epsilon^p
        +(E D_rho^(2p))^(1/2) P(D_rho>epsilon)^(1/2) -> epsilon^p.

Let epsilon→0, then conjugate by bounded free groups and restrict to E. This proves the actual uniform-triangle L² operator convergence asserted in186 and all finite flow moments. These bounds are uniform only in source widths at FIXED delta,R,L. The high spatial derivative/supremum bounds used later need not remain bounded as widths vanish and are not the source of this UI.

The ordinary equation is for all E data, not only109's constant datum. Source-row testing uses E|Z Y_fast(t,x)|<=||Z||2||Y_fast(t,x)||2, finite positive-width point variance and actual completed indicator approximations; no independence or filter-through-mask identity is used. At positive widths106 gives the statewise primitive A_F^rho(t)=integral i S_E(-r)B_F(b(r))S_F(r)dr, b=mc_rho. Here ||B_F(b)||<=||b||infinity+||b||2; both constant columns are present. In the Young sums replace U(t_j,s)e by U(r,s)e inside that integral: the error is bounded by a constant times sum_j Delta_j^(1+theta), tending to0. Thus the Young integral is the strong ordinary interaction integral on every state. Free conjugation yields full-phase Duhamel. Countable dense states/rational times and continuity give one event at each fixed source. Ordinary bounded-coefficient uniqueness identifies this with the actual source E flow; no operator-norm derivative of S is used.

The actual covariance law is also exact. With

    K_tau(v)=Gamma_E(a)^-1 integral_0^(1/tau)
                      exp(-lambda|v|)lambda^(a-1)dlambda,

lambda'=delta lambda gives delta^a K_tau(delta v)=K_(tau/delta)(v). Thus c_rho has covariance K_(tau/delta)(t-s) Gamma_delta,2epsilon(x-y), where Gamma_delta,2epsilon=p_(2epsilon)*Gamma_delta. For two sources the temporal width is max(tau,tau')/delta and the spatial width epsilon+epsilon'. All amplitudes and the given W are retained. At fixed delta both(epsilon,tau/delta)→0 at arbitrary relative rates. Its continuous Gaussian single-source law is exactly the source law at covariance Gamma_delta; point moment calculations depend on that law, not on constructing a new auxiliary family there.

## 4.187: positive-width high-Sobolev construction and scalar identification

Fix delta,epsilon,tau and the source regularity event. Then b=mc_rho is continuous in time with every spatial derivative continuous on[0,L]×R^d and one compact support B_(2R). Let integer k>d/2+1, m_k=k-1 and E_k=H^k×H^(k-1). Minimal k may be2 in d1,3 in d2/d3; k=3 works throughout. In Bessel-unitary coordinates the free matrix is

    [ cos(tq)       <xi> sin(tq)/q ]
    [ -q sin(tq)/<xi>      cos(tq) ],  q=|xi|.

The zero sine quotient equals t. The diagonal entries are<=1, the lower-left<=1; splitting q<=1 and q>=1 bounds the upper-right by sqrt(2)(1+|t|). Consequently C_L=4(1+L) bounds the operator on E_k (and E) for |t|<=L. Pointwise multiplier continuity and Fourier domination prove strong group continuity, not operator-norm continuity.

An explicit product constant is available. Parseval gives

    ||f||_(H^m)^2=sum_(|beta|<=m) c_beta ||partial^beta f||2²,
    c_beta=m!/[(m-|beta|)! beta!].

All c_beta>=1. Leibniz, D_m(b)=max_(|j|<=m)||partial^j b||infinity, and sum_(gamma<=beta)binom(beta,gamma)=2^|beta| give

    ||bf||_(H^m) <=(1+4d)^(m/2) D_m(b)||f||_(H^m),

since sum c_beta4^|beta|=(1+4d)^m. Density passes the inequality to H^m. Set B_L=(1+4d)^((k-1)/2) sup_(r<=L)D_(k-1)(b(r))<infinity. Then B(b)(f,v)=(0,bf) is norm-continuous on E_k with norm<=B_L, retaining both phase entries.

For Z0(t)=S(t)z and Z_(n+1)(t)=integral_0^t S(t-r)B(b(r))Z_n(r)dr, induction on the time simplex gives

    ||Z_n(t)||_Ek <= C_L^(n+1) B_L^n t^n ||z||_Ek/n!.

The series converges in C([0,L];E_k), bounded by C_L exp(C_L B_L L)||z||_Ek, and solves Duhamel. A homogeneous difference bounded by H0 is at most H0(C_L B_L t)^n/n!, hence zero. The continuous embedding E_k→E and ordinary E uniqueness identify its sum with P_E^rho(t,0)z.

Fourier Cauchy–Schwarz gives ||fhat||1<=||f||_(H^s)(integral<xi>^(-2s)dxi)^(1/2) for s>d/2. Fourier inversion therefore embeds H^k and H^(k-1) continuously into bounded continuous functions; both displacement and velocity are continuous, and H^k also gives continuous first spatial derivatives. This is used ONLY at positive widths. The coefficient is a measurable C_t C_x^(k-1)(B_(2R)) random element: derivative evaluations on countable dense grids determine its Borel structure and all versions are continuous. Picard iteration/local product bounds make the solution map locally continuous into C_tE_k, hence strongly measurable. Fourier embedding then gives a jointly measurable continuous displacement version (and velocity). No raw E point trace has been introduced.

The first Duhamel component distributionally reads

    v(t)=cos(t sqrt(-Delta))psi
           +integral_0^t G_d(t-r)*[b(r)v(r)]dr.

Here G_d(h) is a positive measure of mass h, support B_h; G_d(0)=0. For f_r=b(r)v(r), continuity/compact support give finite uniform L1 and sup bounds. Testing against phi in Cc-infinity, absolute Fubini is bounded by ||phi||infinity integral_0^t(t-r)||f_r||1 dr<infinity. The unitary Fourier multiplier of this convolution is the sine quotient (the Green Fourier c_d is canceled by the convolution normalization). Writing G_d(h)=h(dilate_h)_#mu_d, mu_d a unit-time probability measure, proves continuity of the integral jointly in(t,x) by dominated convergence. Both sides are continuous, so the distribution identity is the everywhere pointwise ordinary scalar mild equation. This includes d3 spheres without a Green density or sample heat-tail estimate.

## 5.188: TOTAL datum, exact cone equality, then an integral of squares

The unmasked positive-width scalar full solution uses c_rho, data(1,0), and exists locally by102. To see precisely what is used, on each compact backward-cone enlargement its continuous coefficient has finite sample bound M. Green mass recursion gives term bound M^n t^(2n)/(2n)!, hence locally uniform Picard convergence and uniqueness by the same factorial iteration. No global supremum, E/F unmasked solution or expectation of that sample bound is needed. The Bochner Gaussian chains coincide with this version: bounded point variance bounds each finite product in L² by sqrt((2n-1)!!)V^(n/2), and finite chain mass permits Fubini. An almost surely convergent subsequence identifies pointwise L² and continuous Picard sums. At fixed positive widths, Green-heat versus measure-kernel mixed second moments have bounded continuous Wick integrands and the same finite chain masses. Weak Green convergence therefore gives their L² identification BEFORE noise limits, including d3 spheres, without a sample heat-tail estimate.

Use the FULL closed cone C={(t,x):0<=t<=L, |x|<=1+L-t}. A predecessor y=x-z, |z|<=t-r, satisfies |y|<=1+L-r, so C is causally closed. Throughout C the coefficients b=mc_rho and c_rho agree. For the initial difference one must use TOTAL data(psi-1,0)=((psi,0),-1,0) in E plus constants. The physical free phase kernel entries are

    [ partial_t G_d(t)    G_d(t) ]
    [ Delta G_d(t)       partial_t G_d(t) ],

compactly supported in B_t with masses1,t,0,1. On C, |x|+t<=L+1=R-1: the entire translated support lies strictly inside the plateau where psi-1 vanishes. Thus the total free difference is zero there, in particular cos(t sqrt(-Delta))psi(x)=1. Separately evolving/bounding the E part and constant part would miss this cancellation. No assertion that (psi-1) belongs to H^(1/2) is made.

For w=v-u_full the two scalar equations now have identical free term and coefficient on C. Let H=sup_C|w| and M=sup_C|c_rho|, finite sample constants by continuity. Iterating the homogeneous Green equation yields

    |w(t,x)|<=H M^n t^(2n)/(2n)! for every n.

Indeed f0=1 and f_(n+1)(t)=integral_0^t(t-r)f_n(r)dr=t^(2n+2)/(2n+2)!. The ratio M t²/[(2n+2)(2n+1)] tends to0, so w=0 on C. This uses neither coefficient positivity nor a moment of H or M. It retains the same realized source coefficient in the two equations; equality in law alone would not prove this cone identity.

At time L, C contains D. The unmasked source is spatially stationary; translating its finite scalar chains and then their L² sums preserves the law. Its point second moment is finite by102. Joint measurability and Tonelli therefore give the exact identity

    E||pr1 P_E^rho(L,0)z||_L²(D)²
      =integral_D E|u_full^rho(L,x)|²dx
      =v_d E|u_full^rho(L,0)|² < infinity.

This is an INTEGRAL OF SQUARES, not |integral phi u|², and uses no masked-field stationarity, point covariance order, Jensen bound or old masked-average comparison. Events are for each fixed(delta,epsilon,tau); no common event for uncountably many widths is asserted.

## 6.189: two actual moment limits, THEN canonical scaling

First keep delta fixed.186 and the bounded map pr1:E→L²(D) give

    Z_rho=pr1 P_E^rho(L,0)z|D -> Z=pr1 P_delta z|D
                   in L²(Omega;L²(D)).

Hence |E||Z_rho||²-E||Z||²|<=||Z_rho-Z||_L²(||Z_rho||_L²+||Z||_L²)→0. This requires no point evaluation of Z.

Separately103 applies to the exact unmasked source law Gamma_delta at horizon L and widths(epsilon,tau/delta). To expose its order-limit justification, let Q=sum_n q_n^(Gamma_delta)(L)<infinity, Q_N=sum_(n<=N)q_n and r_N=Q-Q_N. Every absolute mixed moment is bounded by q_n q_k. Outside the finite order square the bound is Q²-Q_N²<=2Q r_N, both before and after the limit. At fixed n,k the Green-first Gaussian diagrams converge to the canonical ones by006, including odd-zero, unequal/self/empty chains. Thus the finite-square limit followed by N→infinity proves convergence of the full point second moment. The constants Q may depend on fixed delta; no delta-uniform tail is needed.

Taking THESE TWO LIMITS in the exact188 identity proves

    E|u_(Gamma_delta)(L,0)|²=v_d^-1 E||Z||_L²(D)².

Gamma_delta labels this scalar source law; P_delta still uses gM_R(W_fast) on the original raw noise, with g already included once. Only afterward use119/125's canonical law scaling. Set delta=T^-kappa and r_T=Tdelta. Original dilation yields V_delta(t,x) with law u_Gamma(Tt,r_Tx) and slow equation delta² V_tt=Delta V+sqrt(delta) W V. The actual Green scaling is G_d(T h,r_T dz)=r_T G_d(h/delta,dz). The per-vertex factors obey

    T^(-a/2) r_T^(2-alpha/2)=sqrt(delta),
    T^(1-a/2) r_T^(1-alpha/2)=delta^(-1/2).

These identities use kappa(3-alpha)=4-alpha-a. The source time widths become tau/T and spatial heat widths epsilon/r_T² under the original dilation. At fixed T the finite-order joint Gaussian laws, Green-before-noise and absolute canonical-series bounds pass the dilation to the full moment; all self/unequal/empty orders remain. Next U(t,x)=V_delta(delta t,x) has speed1 and coefficient sqrt(delta)Y_(epsilon,tau)(delta t,x)=gY_fast, with fast velocity U_t=delta V_t. At fast time L its slow time is1. Consequently

    E|u_Gamma(T_delta,0)|²=E|u_(Gamma_delta)(L,0)|²
       =v_d^-1 E||pr1 P_delta z||_L²(D)².

This is law/moment equality, not pathwise same-noise equality of spatially scaled rough solutions or a PDE-uniqueness claim. r_T shrinks, R grows; they are different scales. Point zero contributes no spatial Jacobian.

The phase inequality gives E|u_Gamma(T_delta,0)|²<=v_d^-1||psi||_(H^(1/2))^2 E||P_delta||². Parseval yields

    ||psi||_(H^(1/2))^2<=||psi||_(H^1)^2
       =R^d||eta||2²+R^(d-2)||grad eta||2²<=C_eta R^d,
    C_eta=||eta||2²+||grad eta||2²>0.

This handles d1's negative d-2 exponent because R>=1. For DataPref_delta=v_d^-1 C_eta(delta^-1+2)^d,

    delta log DataPref_delta
      =delta log(C_eta/v_d)
         +d delta[log(1+2delta)-log(delta)] ->0.

The only nontrivial term is delta|logdelta|=t exp(-t)→0. Canonical E|u|²>=1 by its nonnegative full pairing sum and empty-chain term;185 makes the upper finite. Logs therefore involve finite positive quantities. The map delta↦T_delta is a bijection(0,1)→(1,infinity), so no subsequence or diagonal is involved. Taking logarithms proves the source189 limsup reduction at0. Original canonical spatial stationarity from126 extends it to every fixed x; the masked operator is not declared stationary.

## 7. Falsification controls and precise scope

Green masses are h in all dimensions: d1 has(1/2)1_(|z|<h)dz; d2 polar integration of(2pi)^-1(h²-|z|²)^(-1/2) gives h; d3 has surface measure/(4pi h), area4pi h². Thus chain masses at n=0,1,2,3 are1,t²/2,t^4/24,t^6/720 even for the sphere. At h=0 the Green measure is0.

For d1 white Gamma=c delta0, Gamma_(2epsilon)(0)=c(4pi epsilon)^(-1/2). For an admissible singular d3 check take Gamma=Lebesgue_(x1,x2) tensor delta0(x3), degree d-alpha=2, alpha=1, a<1; it is even/nonnegative/tempered with spectral support on the third axis. Its covariance quadratic form is integral_dx3 (integral_dx1dx2 f(x1,x2,x3))²>=0, proving PD. Its heat covariance is(4pi epsilon)^(-1/2)exp(-x3²/(4epsilon)), so all fixed-width derivative moments are finite without any angular density or finite TOTAL spectral mass. The fast point variance is

    g² K_(tau/delta)(0)Gamma_(2epsilon)(0)
       =delta K_tau(0)Gamma_(2epsilon)(0),
    K_tau(0)=tau^-a/[a Gamma_E(a)],

matching c_rho=sqrt(delta)Y(delta t). The Green masses and cone argument remain three-dimensional, not a lower-dimensional replacement wave.

For Gamma=0, all noises/drivers vanish and P_delta=S_E(L). The TOTAL free cone argument gives pr1 S_E(L)(psi,0)=1 on D, so both sides of the exact moment identity are1. The zero-frequency free matrix is the shear[[1,L],[0,1]], not a contraction.165 and the Fourier bound give1<=||S_E(L)||<=4(1+L), hence delta log||S_E(delta^-1)||²→0. No division by a nonzero covariance, nondegenerate Gaussian law or noisy convergence theorem is needed.

The limit order is immutable: fixeddelta/source regularity and Green-first identifications; source widths→0 at fixed(delta,R,L) in each of the two actual moment limits; canonical law/scaling at fixeddelta; only then delta→0. High-Sobolev/source derivative constants may diverge with widths, and UI constants may diverge with delta. No rough point trace, global unmasked E wave, delta-uniform UI, pathwise full-family source convergence, masked-average substitution or rough-solution PDE-uniqueness assumption has entered. The stated steps close under the exact local input contracts; their broader parent proofs/review remain assigned separately.
