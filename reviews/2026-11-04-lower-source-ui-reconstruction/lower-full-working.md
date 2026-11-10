# Actual lower chain119–126: author reconstruction

This is author mathematics for the eight current deductions, not a reviewer verdict, source change or new theorem. The precise driver/Young/ground clauses consumed below are separated in prerequisite-clauses.md. They are inputs with explicit application checks, not assumed whole-parent acceptance. Original data are(1,0); d=1,2,3;0<a=alpha0<1;0<alpha<d oralpha=d=1;alpha+a<2. Gamma is the original even nonnegative PD homogeneous tempered Radon measure, Gamma(cA)=c^(d−alpha)Gamma(A). No density, finite total mass, Riesz structure or separable control is assumed.

##0. Falsification first and the fixed objects

For constant physical phase the free matrix is C(t)=[[1,t],[0,1]], with displacement row(1,t). This is the intended two-column control, not a claim that the phase started at(1,0) becomes(1,t). C(2) applied to(0,1) has displacement2, whereas resetting velocity between two unit blocks loses it. A scalar product of displacement values cannot represent this matrix product. For the constant-coefficient algebraic toy u''=lambda u, the first displacement responses to the two initial columns arelambda t²/2 andlambda t³/6; the second cannot be dropped. This is a finite-phase falsification, not a constant-potential assertion inside the original homogeneous SPDE class.

The exact original white calibration from current003 is retained: forGamma=c delta0, c0=c/[(1−a)(2−a)(3−a)], E X1²=c0t^(3−a), E X2=c0t^(3−a)/2. The two empty orientations plus the cross term give2c0t^(3−a). A source comparison omitting self/empty terms therefore fails already at total order2. We reuse that exact written calculation rather than retest an unchanged formula.

Fix Gamma nonzero and a real nonnegative nonzero Psi in Cc-infinity((0,1)×Rd), extended byzero. On the original isonormal space put Z=W(Psi),

 h_s(x)=integral_0^1 |s−r|^(−a)(Gamma*Psi_r)(x)dr,
 v=E Z²=integral Psi_s(x)h_s(x)dxds.

For compact tests, absolute Fubini uses only local Radon mass and integrability of|s−r|^(−a); hence0<v<infinity and E[W(f)Z]=integral f h. Derivatives fall on the extended smooth test, so h is smooth on compact s,x sets, including0<=s<=2. Actual117/118 supply a FIXED finite mask0<=m_R<=1, one onB_R, supportedB_2R, for whichV_s=m_Rh_s has a common negative trial. The originalPsi,Z,v do not change with this choice. We retain this R for the entire argument.

Use E=H^(1/2)×H^(−1/2), F=E direct-sum R², inclusioni, e0=(0,1,0), and bounded O_phi(e,c)=integral phi u_e+c1, withphi>=0 smooth compact andintegralphi=1. The free constant block is C(t). Actual112–118 supply rate lambda_s>=lambda_*>0, Lipschitz in s∈[0,1], real rank-one Pi_s=e_s ell_s with ell_s(e_s)=1, Q_s=I−Pi_s,

 P_s(t)Pi_s=Pi_sP_s(t)=exp(lambda_s t)Pi_s,
 ||exp(−lambda_s t)P_s(t)Q_s||<=C_gap exp(−eta_gap t),
 a_*=inf ell_s(e0)>0, j_*=inf O_phi(e_s)>0.

All these are actual full-F flow quantities. Write I_R=integral_0^1lambda_s ds. No point evaluation of an E-function is used.

##1.119: canonical scaling at each fixedT

Put kappa=(4−alpha−a)/(3−alpha)>0, delta=T^(−kappa), r=Tdelta=T^((a−1)/(3−alpha)). At positive source widths a change(s,y)=(Tt,rx) gives the Gaussian covariance amplitude T^(−a)r^(−alpha). This is distributional Radon homogeneity; it includes spatial white. The normalized pulled-back field has the original raw covariance. Temporal cutoffs obey K_eta(Tt)=T^(−a)K_(eta/T)(t), spatial heat widths becomeepsilon/r², and both the maximum-time and summed-space joint width rules are preserved.

The positive Green measure satisfies G(Ttau,r dz)=rG(tau/delta,dz), also for the d3 sphere measure. Time JacobianT and Gaussian amplitude give the per-vertex coefficient

 Tr T^(−a/2)r^(−alpha/2)=delta^(−1/2),
 T^(−a/2)r^(2−alpha/2)=sqrt(delta).

The latter identity follows since−a/2+(a−1)(4−alpha)/[2(3−alpha)]=−kappa/2. Thus the transformed equation is delta² Vtt=Delta V+sqrt(delta) W V, data(1,0); its forcing kernel isdelta^(−1)G((t−s)/delta), so its noisy vertex factor isdelta^(−1/2), exactly as above. This proves finite-list fixed-order JOINT laws, not just individual variances: the source field is jointly Gaussian under the one dilation, and all polynomial kernels transform with it. Self, unequal and empty chains remain included.

For fixedT,r remove d3 Green smoothing FIRST, then arbitrary-relative noise widths via006. Absolute L2 order summability008 passes finite-list laws to the canonical series and second moments. No widths/time limit is interchanged and no uniqueness of a rough PDE is invoked. Consequently law[u(Tt,rx)]=law[V_delta(t,x)], and

 T^(−kappa)log E|u(T,0)|²=delta log E|V_delta(1,0)|².

This is equality in law for each fixedT, not a simultaneous samplewise coupling of all scaled solutions on W.

##2.120: the actual coupled block Gaussian vector

Choose an integer B>=1, subsequently fixed, and0<delta<min(1,1/B). Let N=floor(1/(delta B))>=1, s_m=m delta B, tau=delta^(−1)−NB in[0,B), g=delta^((1−a)/2). For positive-time compactfast tests define

 T_m f(s,x)=delta^(a/2−1) f((s−s_m)/delta,x),
 W_m(f)=W(T_m f), W_fast=W_0.

In the raw covariance, two test factors give delta^(a−2), two time Jacobiansdelta², and the temporal kernel delta^(−a). Their product is1. Therefore T_m is an isometry through the null quotient and W_m has the original raw law. Also T_0[f(·−mB)]=T_mf exactly, so W_m(f)=W_fast(f(·−mB)) on the SAME W. No block independence is present or required.

Fix admissible0<gamma<min(1/2,(2−alpha)/2),1/2<theta<beta_H<min(1−a/2,(3−a−alpha)/2). On[0,B] take the actual full-F linear driverA_R and set

 X_m=g A_R(W_m),
 H_m(u)=integral_0^u S_F(−r)i B_F(V_(s_m+delta r)) S_F(r)dr.

Here s_m+delta r<=1+delta B<2. The ground templates only use s_m∈[0,1]. Let B0 be the Ctheta-closure of zero-initial polygonal compact-operator paths, and B_delta=B0^(N+1) with maximum norm. K(F) is separable: P_nTP_n→T for compactT andT*, followed by rational finite matrix approximations. Rational polygonal paths are dense in B0; moving breakpoints is controlled by[f]_theta<=(2||f||infty)^(1−theta)Lip(f)^theta. Thus B_delta is separable.

The actual finite coefficient paths are zero-initial Lipschitz compact-valued paths. Their Gaussian sums converge in LpCtheta into this closed space by093/095/105. Joint finite coordinates withZ are Gaussian; L2 limits preserve all joint characteristic functions. Therefore(X,Z) is a genuine centered Banach-Gaussian vector. From the raw same-law bound,

 ||X_m||_(Lp B0)<=C_(R,B)sqrt(p) g, p>=1,

with C independent ofdelta,m; the blocks can be maximally correlated. E||XZ||<infinity follows by L2 Cauchy–Schwarz, so b=E[XZ] is a Bochner covariance.

Substitution in the ACTUAL covariance with originalZ gives

 E[W_m(f)Z]=delta^(a/2) integral f(u,x)h_(s_m+delta u)(x)dxdu.

Approximate the driver's indicator/matrix tests on one compact set in the raw norm. Dominated convergence uses|u−r|^(−a)Gamma and the actual Sobolev adjoint. This extends the identity to all real Schwartz E-matrix entries. The two F columns are the actual constant-response tests(psi,0),(0,psi); total finite propagation and105 give the identical mean identity on them. E alone is not dense in F, whereas E plus BOTH constants spansF. Boundedness, dense real states and rational times extend to all paths. Since g delta^(a/2)=sqrt(delta),

 b_m=E[X_mZ]=sqrt(delta)H_m, so b=sqrt(delta)H.

Only the operator response is masked; neitherPsi norZ norv is replaced by a masked control.

##3.121: one Gaussian change of law on the whole norm-Borel space

For real s define dQ_s/dP=exp(−sZ−s²v/2). Completing the scalar Gaussian square gives a positive density of expectation1, hence equivalent measures. For finitely many continuous real coordinatesell, represent(ell(X),Z)=(TG,z·G) in law using a finite standardGaussianG and a positive covariance square root, even if the covariance is singular. ThenTz=ell(b),|z|²=v. The Gaussian density substitution G'=G+sz yields

 E_Qs f(ell(X+s b))=E f(ell(X))

for bounded Borel f. No inverse covariance or independence is needed.

Basis matrix entries at rational times generate the norm-Borel sigma field ofB_delta: operator norm equals the supremum of pairings over countably many rational finite unit vectors; the path supremum/Hölder seminorm are suprema over rational times/pairs. Thus distance to a fixed path is coordinate measurable. Separable norm-open sets are countable unions of balls, and every coordinate is continuous. A generating-pi-system argument extends the identity to all Borel sets, then simple functions and monotone convergence to every nonnegative norm-Borel j, including infinite integrals. Taking s=delta^(−1/2), sb=H gives

 E j(X)=E[exp(−Z/sqrt(delta)−v/(2delta)) j(X+H)].

The Young map below exists on the WHOLE path space, including every deterministic translate. There is no translated exceptional-domain assumption and no source approximation under this density.

##4.122: actual maximum, exponential budget and frozen mean

Write M_delta=max_(m<=N)||X_m||B0. N+1<=2/delta gives, without independence,

 ||M_delta||p <=(sum_m E||X_m||^p)^(1/p)
 <=2^(1/p) C sqrt(p) delta^((1−a)/2−1/p).

For any fixed finiteq choose a fixedp>max(q,2/(1−a)); Lyapunov then impliesM_delta→0 inLq. For a uniform square-exponential bound choose integern0 with n0(1−a)>=1. For n>=n0,

 E M_delta^(2n)<=2 C^(2n)(2n)^n delta^(n(1−a)−1)
 <=2 C^(2n)(2n)^n.

The finitely many lower moments are bounded by Lyapunov from the2n0 moment. Since n!>=(n/e)^n, the exponential-series tail is at most2sum_(n>=n0)(2e c C²)^n. Choose0<c<1/(2eC²). This proves sup_delta E exp(cM_delta²)<infinity for the SCALED maximum, not the unscaled one.

Let H_m^stat be the primitive forV_(s_m). The fixed-R Lipschitz bound in L-infinity andL2 gives ||V_(s_m+delta r)−V_(s_m)||<=C delta B for0<=r<=B. Statewise integration with the bounded free groups on[0,B] yields

 max_m(||H_m||Ctheta+||H_m^stat||Ctheta)<=H0,
 max_m||H_m−H_m^stat||Ctheta<=C_B delta.

For example the difference primitive has Lipschitz boundC delta B and supremum boundC delta B²; multiplying byB^(1−theta) controls its Hölder seminorm. Constants depend on fixedR,B,Psi,exponents, notdelta,m. No norm continuity of the free group is used.

Define physicalD_x(u)=S_F(u)U_x(u,0). On{M_delta<=1},107 local Lipschitz stability on the fixed driver ballH0+1 (or any larger fixed radius>=1) gives

 Eop_delta=max_m sup_(u<=B)||D_(X_m+H_m)(u)−P_(s_m)(u)||
 <=L_B(M_delta+delta).

Thus Eop_delta→0 in probability. With nuY=1/theta<2, the globalYoung estimate gives max_m sup_u||D_(X_m+H_m)(u)||<=C exp(C(1+H0+M_delta)^nuY). For any finitepowerq, the elementary dominationA x^nuY<=c x²+C_A bounds itsqth moment using the just-proved exponential budget; choosing a higher finitepower gives uniform integrability. Hence Eop_delta→0 in every finiteLq. Suprema are measurable through countably many dense states and rationaltimes; strong physical continuity on states suffices.

##5.123: full-F entrance, rebase and actual terminaltau

Fix0<rho<1/2. Set Me=max(1,sup||e_s||), Ml=max(1,sup||ell_s||), MP=max(1,sup||Pi_s||), MQ=1+MP,Mz=Me+1,Hobs=max(1,||O_phi||),E0=||e0||=1. Choose the aperture FIRST:

 vartheta=min(1,j_*/(16Hobs Cgap)).

Next choose integerB>=1 so qB=Cgap exp(−etagap B)<=min(1/8,vartheta a_*/(8MQ E0)). Choose epsilon_par>0 with epsilon_par Mz<=min(rho/2,vartheta,1/4). Uniform continuity ofell,Pi suppliesomega>0 so adjacent parameter changes<=omega imply both norm differences<=epsilon_par. Finally choose epsilon_op>0 satisfying

 Ml epsilon_op Mz<=rho/2, MQ epsilon_op Mz<=vartheta/4,
 Ml epsilon_op E0<=a_*/2, MQ epsilon_op E0<=vartheta a_*/8,
 Hobs epsilon_op Mz<=j_*/8.

These are fixed positive budgets. They use the NORMALIZED complement; no growing terminal norm enters the aperture choice.

For indices sigma_m with adjacent gaps<=omega, suppose real boundedD_m(u) are within epsilon_op ofP_(sigma_m)(u) for everym,u∈[0,B]. The cone atb consists of z=Ae_b+r, A=ell_b(z)>0, ell_b(r)=0, ||r||<=vartheta A. Consequently||z||<=Mz A.

Entrance z1=D0(B)e0 has normalized amplitude at leasta_*−Ml epsilon_op E0>=a_*/2, and normalized residual at mostqB MQ E0+MQ epsilon_op E0<=vartheta a_*/4. Therefore z1 belongs to the cone, with residual ratio<=vartheta/2 and amplitude>=exp(lambda_(sigma0)B)a_*/2.

For an old cone atb and adjacentc, rebase BEFORE applyingPc:

 ell_c(z)>=A−||ell_c−ell_b||||z||>=(1−epsilon_par Mz)A,
 ||Q_cz||<=||Q_bz||+||Pi_b−Pi_c||||z||
 <=(vartheta+epsilon_par Mz)A.

For a full next blockD close toP_c(B), put x=exp(−lambda_cB)ell_c(Dz), y=exp(−lambda_cB)||Q_cDz||. Since lambda_c>0, exp(−lambda_cB)<=1. Commutation ofP_c withPi_c and the normalized complement give

 x>=(1−epsilon_par Mz−Ml epsilon_op Mz)A>=(1−rho)A>A/2,
 y<=[qB(vartheta+epsilon_par Mz)+MQ epsilon_op Mz]A
 <=(vartheta/4+vartheta/4)A=vartheta A/2<=vartheta x.

The next cone is preserved, and its amplitude gains exp(lambda_cB)(1−rho). The old residual was never assumed inkerell_c.

For the terminal0<=u<=B rebase once more: ell_c(z)>=3A/4,||Q_cz||<=2vartheta A. Hence

 exp(−lambda_cu)O_phi(P_c(u)z)/A
 >=3j_*/4−2Hobs Cgap vartheta.

The perturbationD_N−P_c changes this by at mostHobs epsilon_op Mz<=j_*/8. Since2Hobs Cgap vartheta<=j_*/8, the result is>=j_*/2. Multiplying entrance, N−1 full conversions and terminal estimate gives

 O_phi D_N(u)D_(N−1)(B)...D0(B)e0
 >=c_*(1−rho)^(N−1)
   exp(B sum_(m<N)lambda_(sigma_m)+u lambda_(sigma_N)),
 c_*=a_*j_*/4>0.

This proves all quantifiers of123 for everyN>=1 and everyu∈[0,B], includingN1 andu0. No positivity, composition, independence or scalar moment multiplication was assumed for the approximatingD_m. The proof lives on the full phase and its actual spectral projection.

##6.124: actual source restart and fixed finite ordered-product limit

Fixdelta,B,N now; L=1/delta andLext=(N+1)B>=L. Take ONE retaining sourceY_(epsilon,eta) on the givenW extension from097; define its fast/local versions by the actual pullbacksT0,Tm. They obey source and residual variance domination becauseTm is an isometry, and the residual tends tozero on every transformed compact test at fixeddelta,m.095 therefore supplies actual global/local driver convergence in every finiteLpCtheta, including105’s two constant columns. No independently resampled cutoff family is introduced.

The pointfields satisfy Yfast(u,x)=delta^(a/2)Y_(epsilon,eta)(delta u,x), Ym(u,x)=Yfast(mB+u,x). The fast temporal width iseta/delta, since delta^aK_eta(delta r)=K_(eta/delta)(r); spatial widths and every joint width rule are unchanged. These continuous-time/smooth-space fields have ordinary primitives equal to their transferred drivers: test against the literal matrix integrands, approximate their indicators in raw norm and use109/110 ordinary-source identification. This is a checked application of095/097/105/109/110 at each fixed finite horizon, not an assumption that arbitrary retaining extensions commute with dilation.

For Aglob^src=g A_R(Yfast), ordinary integration and free group composition give EXACTLY

 S_F(mB)[Aglob^src(mB+u)−Aglob^src(mB)]S_F(−mB)=X_m^src(u).

The mask remains inside the physical force; it is not commuted throughS_F. Restriction/difference/conjugation are bounded maps at this fixeddelta,Lext, so the same identity passes to actual rawCtheta driver limits. Finitely many blocks and rationaltimes plus continuity make the identities simultaneous. Adding the fixed deterministic meanV_(delta t) gives localH_m by the same change of variables.

Conjugate each global interaction Young equation byS_F(mB). Bounded linearity of its Riemann sums and the last identity give precisely the local equation driven byX_m, orX_m+H_m.107 uniqueness therefore yields the physical restart

 Pglob(mB+u,mB)=D_(X_m)(u),

and its shifted counterpart. Composition identifies the ordered products at endpointNB+tau=L, retaining the ACTUALtau. Conjugation constants need only be finite for this fixeddelta; no uniform-in-delta global product bound has been assumed.

Here is the full source PRODUCT passage, not just convergence of individual factors. For n=N+1 let F_m be the raw factors atB(m<N) ortau(m=N), andF_(m,src) their actual ordinary-source factors.108 and the just-checked transfer give factor convergence in every finiteLq and uniform finite moments under the ORIGINAL probability measure. Put

 Csrc=max(1,max_m||F_(m,src)||,max_m||F_m||),
 esrc=max_m||F_(m,src)−F_m||.

For this finite set, sup_src||Csrc||q<infinity and||esrc||q→0 for every finiteq. Telescoping in the actual order gives product error<=n Csrc^n esrc (each one-factor replacement has at mostn−1 other factors, andCsrc>=1). Hölder with1/2=1/4+1/4 yields

 ||product_src−product_raw||L2
 <=n ||Csrc||_(L^(4n))^n ||esrc||L4→0.

This completes the product limit at FIXEDdelta,N before ANY change of law or time asymptotic. Constants may grow withn/delta. There is no triangular-array source estimate. Shifted source products, if used for restart, add the fixed raw mean deterministically and converge underP; no finite-source Cameron mean replacesH.

##7.125: raw square identity and same canonical point comparison

Define on allB_delta

 j_delta(x)=|O_phi D_(x_N)(tau)D_(x_(N−1))(B)...D_(x0)(B)e0|².

107 makes this continuous, everywhere defined and nonnegative: finite products/free groups/observable are bounded operations at the stated times. Thus121 applies directly to rawX, giving

 E U_delta²=E[exp(−Z/sqrt(delta)−v/(2delta))Y_delta²],

where U_delta usesX_m andY_delta usesX_m+H_m. Their every finite unweighted moment follows from Gaussian path square-exponentials and nuY<2, then finite-product Hölder. The identity itself holds without pre-assuming j integrable. Its density involves the SINGLE ORIGINALZ andv, not a sum of block costs and not a masked variance.

For the comparison use ONLY the noise-only source product limit just proved. W'=gWfast has covariance|u−r|^(−a)Gamma_delta withGamma_delta=g²Gamma, the same original admissible class anddegreealpha. Driver linearity and105 ensure actual full-F factors at this amplitude; every n-vertex source chain gainsg^n. At fixed positive widths109 identifies the ordered source product tested byO_phi with the ordinary masked solution of coefficientg m_RYfast, data(1,0), atL. Its tested average converges inL2 toU_delta by the4n/4 estimate. This discharges exactly103’s conditional premise, not merely a driver-only convergence statement.

For clarity the positive-width scalar inequality is

 E|integral phi(x)u_src^m(L,x)dx|²
 =integral phi(x)phi(y)E[u_src^m(L,x)u_src^m(L,y)]dxdy
 <=integral phi(x)phi(y)E[u_src(L,x)u_src(L,y)]dxdy
 <=E|u_src(L,0)|².

The first comparison102 is termwise Wick positivity with one vertex mask0<=m_R<=1, positive Green measures/covariance and every unequal/self/empty pairing. The last uses Cauchy–Schwarz and stationarity of the UNMASKED field with||phi||1=1; masked stationarity or Gaussian PSD order is not asserted. Absolute series/Green-first integrability justifies the displayed interchanges.103 removes noise widths at arbitrary relative rates using006/008 for the unmasked canonical moment, andL2 convergence of the masked average gives

 E U_delta²<=E|u_(Gamma_delta)(L,0)|².

This is an observable inequality, not a rough point trace or an F-norm comparison. There is no tilted-source limit: the shifted raw Y_delta was already j_delta(X+H) in121.

On the actual ordinary sources gYfast(u)=delta^((1−a)/2)delta^(a/2)Yslow(delta u)=sqrt(delta)Yslow(delta u). With slow t=delta u and phase(V,delta V_t), the source equation is the119 semiscaled equation;L=1/delta corresponds to slowtime1. Fixed-order/source and absolute-series limits at this FIXEDdelta preserve that canonical law.119 then gives

 E U_delta²<=E|V_delta(1,0)|²=E|u(T,0)|²,
 delta=T^(−kappa).

As a fixed-order power check, m+n=2k gives g^(2k)L^(beta_time k)=delta^((1-a-beta_time)k)=delta^(-(3-alpha)k)=T^(beta_time k), with beta_time=4-alpha-a. The original covariance amplitude is retained insideGamma; it is not absorbed intoPsi orv.

The physical dilationr_T=Tdelta is not the mask radiusR. The fixed mask need not cover a growing backward cone: only moment domination was used. All source limits are finished before the large-time step.

##8.126: event probability, all losses and the single raw half-action

Fix an arbitrary rate-error e>0. Choose0<rho<1/2 withlog(1−rho)>−e/3, then fix its cone constantsB,omega,epsilon_op,c_* as in§5. Psi andR stay fixed. Choose one finitep>2/(1−a), setgamma_p=p(1−a)/2−1>0. Markov plus a UNION bound gives, for fixedeta>0,

 P(M_delta>eta)<=eta^(−p)sum_(m<=N)E||X_m||^p
 <=A_p eta^(−p)delta^gamma_p,
 A_p=2(C_(R,B)sqrt(p))^p.

No independence is used. The p choice cannot be dropped: e.g.a1/2,p6 givesgamma_p1/2>0, whereasp2 givesnegative exponent and no decay from this bound.

Take L_B>=1 from§4 and fixeta=min(1,epsilon_op/(2L_B)). Ifdelta<=epsilon_op/(2L_B), M_delta<=eta impliesEop_delta<=epsilon_op. On the original common space let

 E_delta={Eop_delta<=epsilon_op} intersection{|Z|<=delta^(−1/4)},
 p_delta=P(E_delta).

Chebyshev for the SAMEZ givesP(|Z|>delta^(−1/4))<=v delta^(1/2). Thus

 p_delta>=1−A_p eta^(−p)delta^gamma_p−v delta^(1/2)→1.

This is one event and one union bound, not a product of block probabilities. All norms/events are norm-Borel by§2–4. Choose delta sufficiently small so simultaneouslydelta<min(1,1/B),delta B<=omega,delta<=epsilon_op/(2L_B),C_lambda delta B<=e/3,delta|log c_*|<=e/3 and the last two probability errors sum<=1/2. Every constant has already been fixed.

OnE_delta the actual shifted operators satisfy§5 withsigma_m=s_m, soY_delta>0 and

 delta logY_delta>=delta logc_*+delta(N−1)log(1−rho)
   +delta B sum_(m<N)lambda_(s_m)+delta tau lambda_(s_N).

BecauseNdelta B+delta tau=1, the final two terms form a left Riemann sum on the ENTIRE[0,1], including the terminal interval of lengthdelta tau. Its error is<=C_lambda delta B (even half that bound follows by summing squared mesh lengths). Also0<=delta(N−1)<=1/B<=1; since the logarithm is negative, this loss is>=log(1−rho)>−e/3. Entrance and Riemann losses are each>=−e/3. Therefore

 Y_delta>=exp((I_R−e)/delta) onE_delta.

This includesN1 andtau0. Keeping the actual remainder ensures the exact endpoint, not an unstated shortened-horizon object.

The raw identity integrand is nonnegative. OnE_delta,−Z/sqrt(delta)>=−delta^(−3/4). Restricting the SAME identity and then using§7 gives

 E|u(T,0)|²>=p_delta exp((2I_R−2e−v/2)/delta−delta^(−3/4)).

For small delta,p_delta>=1/2, so−delta log2<=delta logp_delta<=0. Thus

 delta log E|u(T,0)|²
 >=2I_R−2e−v/2−delta^(1/4)+delta logp_delta.

Both final errors tend tozero. The Gaussian quadratic action isv/2 ONCE. Squaring the observable doubles its deterministic rate, not the density cost; blocks andZ are not independent. SinceT↦delta=T^(−kappa) bijects all sufficiently large positive realT with all sufficiently small positive delta, this gives the continuous-time liminfQ2>=2I_R−2e−v/2. For each e we first fixedB=B(e) and then tookdelta→0. Q2 is independent ofB; only now sende→0:

 Q2>=2 integral_0^1lambda_s ds−v_Psi/2.

Spatial translation of every positive-width vertex preserves the unmasked raw law and data; fixed-order and absolute-series limits preserve point second moments. Hence this holds for each fixed originalx. A supremum over controls/masks can follow their individual inequalities, never precede their fixed-data limits.

IfGamma=0, the canonical solution is identically1 andQ2=0 directly. The nonzero-ground/positive-variance construction above is not invoked in that branch. For nonzeroGamma the local-Radon mean/common trial and actual driver parameter window hold for every originald1/2/3, including white and singular spectra. No covariance amplitude was normalized away. No actual gap was located in these eight deductions under the precisely listed OWN input clauses. This is a bounded author reconstruction, not whole214 verification, a confidence label, source-pixel coverage or completion of the project.
