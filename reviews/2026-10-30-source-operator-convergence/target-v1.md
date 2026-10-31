# Canonical source DRIVER convergence: frozen target

UNREVIEWED statements before longproof. Full original sharp/all-dimensional
objective retained. d1/2/3,canonicalH:homog Gamma (nonzero;zero trivial),
a=alpha_0 in(0,1),alpha+a<2,0<alpha<d oralpha=d=1. SAME given realW on
positive-time rawtestHilbert H=H_W, physicallymasked zeta_R, R>0,T>0 fixed,
E=H^1/2 xH^-1/2, fullMASSLESS wave. Choose admissiblegamma,beta,theta as
accepted actual-operator-driver.md, 1/2<theta<beta. Work in
Btheta=C^theta([0,T];B(E)), with compactvalues. This is FIRSTdriver only.

S0 GENERIC GAUSSIAN TRANSFER (no stationarity/smoothCMmean assumption):
Fix once a RAW H-ONbasis f_j withCcsmoothpositive-time representatives and
RAW deterministic operators A_j(t) from accepted actual-operator-driver.md.
Thus M_W,N=sum_(j<=N)W(f_j)A_j converges in Lp(Btheta),EVERYfinitep>=1.
Let Y be a centeredGaussian linear noise on initialrawtests, on the same
coupled space, VarY(F)<=C||F||_H^2, C>=0. Extend Y continuously to H.
Source evaluations Y(f_j) may be CORRELATED. Define
 M_Y,N=sum_(j<=N)Y(f_j) A_j(t), keeping RAW A_j, not Y-CMcoefficients.
Seek actual Lp(Btheta) limit M_Y with
 ||M_Y-M_Y,N||_LpBtheta<=sqrt(C)||M_W-M_W,N||_LpBtheta,
 ||M_Y||_LpBtheta<=sqrt(C)||M_W||_LpBtheta.
Finite-dimensional Gaussian covariancecomparison/Jensen on the convex
function ||sum c_j A_j(.)||_Btheta^p is the proposed proof; no independence
ofY(f_j), no Banach conditionalexpectation or infinite Gaussianmeasure
comparison theorem assumed. Limits live in same separableclosedspan of
RAW A_j(.) paths. Prove Gaussian/compact-valued/actualfieldmatrixcompat
 <M_Y(t)z,w>=Y(h_R,t;z,w), h_R the literal RAW noise test zeta_R times
waveproduct with actualSobolevadjoint. No commutation ofnoisefilters with
physicalcutoff/wave. Basisindependence bymatrixforms, linearity on jointly
Gaussian fieldfamilies, Gaussianpathnormbounds follow at exactscope.
If (W,Y_n) jointlycenteredGaussian, VarY_n<=C_Yraw, Var(W-Y_n)<=C_Eraw
uniform, and E|(W-Y_n)(F)|²->0 on smoothcompactrawtests, prove
 M_Yn->M_W in EVERYfiniteLp(Btheta). Uniformtailcomparison plus finite
RAWbasis coordinate convergence, not sourceCMsmoothing, should suffice.
This is linear-driver covarianceorder, NEVER nonlinearwave momentorder.

S1 GIVEN-W RETAINING canonical coupling, strongerthan source's law-only
redefinition: H_Gamma realspatialtestnullquotient with
 B_Gamma(f,g)=intGamma(dy)int f(x)g(x-y)dx,
 spectralnormalization (2pi)^d int fhat conjghat dmu.
Letnu_a(dlambda)=lambda^(a-1)dlambda/Gamma_E(a), and
 G=L2((0,infinity)_lambda xR_r,nu_a dr;H_Gamma),
 PhiF(lambda,r)=sqrt(2lambda)int_(t>0,t>=r) exp[-lambda(t-r)]F(t,.)dt.
Prove isometry H->G by OUfactorization/Laplace, first on tensors then
completion; r is AUXILIARY, not negative-time rawnoise. GivenW, extend it
on a possibly enlarged probabilityspace to isonormalI onG via independent
Gaussian on(PhiH)^perp, retaining I(PhiF)=W(F) inL2 for everyfixedF.
H_Gamma may have nulls/singularspectra; no density/injectivity assumed.
HeatC_epsilon onH_Gamma has multiplier exp(-epsilon|xi|²/2),
P_delta onG multiplies1_(lambda<=delta^-1), commuting withheat.
Q_rho=C_epsilon P_delta, rho=(epsilon,delta)>0.
Define Y_rho(F)=I(Q_rho PhiF), D_rho(F)=I((1-Q_rho)PhiF).
Rawtestfunctions are not themselves multiplied by zeta_R until literal
matrixevaluation; physicalfieldmask stays AFTER field smoothing.

S2 EXACT AUTHOR parameterdictionary and source law, no temporalconvolution:
 p(epsilon,x)=(2pi epsilon)^(-d/2)exp(-|x|²/(2epsilon)), author(1.20),p5;
 K_delta(t)=Gamma_E(a)^-1 int_0^(delta^-1) exp(-lambda|t|)lambda^(a-1)dlambda,
 Gamma_epsilon=p_epsilon*Gamma.
The pointfield vector inG should be
 v_rho;t,x(lambda,r)=1_(lambda<=delta^-1)sqrt(2lambda)
          exp[-lambda(t-r)]1_(r<=t) p_epsilon(x-.) inH_Gamma.
It has finite norm, yields I(v) and testintegrals equal Y_rho(F).
Check (2.9),(2.11),pp8-9, EXACTLY:
 Cov(Y_e,d(t,x),Y_e',d'(s,y))
   =K_(max(d,d'))(t-s) Gamma_(e+e')(x-y).
In particular source selfcovGamma_2epsilon, notGamma_epsilon. Prove Radon
extension and given-W preservation here; don't present those as proved by
an author paragraph that says only 'without changing distribution'.
No rawpoint W(t,x) evaluation is defined by this formula.

S3 linear domination/convergence on H at arbitrary relativeepsilon,delta rates:
 VarY_rho(F)<=VarW(F), VarD_rho(F)<=VarW(F), VarD_rho(F)->0.
Use orthogonal lambda tails and spatialheat contraction, strongP_delta/C_epsilon.
Only W-W_delta is independent ofW_delta. Heat makes W-Y_rho generally
CORRELATED withY_rho; don't discard that crosscovariance. No claimcutoffs
measurable in the MINIMALrawW Gaussian span. Fields jointlyGaussian on
one common enlarged space, rawW and rawoperatorpath retained bypullback.
Apply S0 on literal h_R,z,w to get
 M_R^(epsilon,delta)->M_R in allfiniteLp(Btheta), uniform Gaussian sqrtp/
exponential localpathnorms for source and residual paths. FixedR,T only,
no large-time/regularization limit interchange and no uniformRclaim.
No need covariance of residual to be a physically nonnegative measure.

S4 CLASSICALfirstresponse for epsilon,delta>0: actual pointfield version
Y_rho continuous intime and C_infinityinspace on compactcones; spatial
derivatives jointlycontinuous. Need proof from heat spectralmoments and
finite-lambda Gaussianincrements, not assumed from meregenericdomination.
Then ordinary stateintegral
 int_0^t S(-u)B(zeta_R Y_rho(u,.))S(u)du
is a bounded-operator Lipschitzpath onE and agrees indistinguishably with
M_R^rho on the SAMEspace. ActualSobolevadjoint/testintegral/GaussianFubini/
countabledensepairs prove identity, not just equallaw. No opnormcontinuity
of S(t) or unproved differentiation ofrawnoise needed. This is LINEAR
firstresponse, not a nonlinear solution/Youngflow identity.

Before longproof: independently audit S0-S4/objects/model/sourceimages.
No newsource-OP theorem adopted at this stage. Canonicalu(source)limit,
Youngflow/canonicalinitial(1,0)/testedaverages/pointmoment transfer,
growingcone/groundgap/d2d3lower/sharpupper/sourceenergy/conditionalexactlimit
remain OPEN. No E1/2 point evaluation in d2/3. No newLeanmodule/71facts18seams
upgrade, companion/HPC/contact/Skorohod/sourcefix/TeX/PDF/wiki/publicrelease/
wholepaper clearance. Authorfirstmean/exactlimit/conjecture NOTimported.
