# Actual growing-mask moment upper bounded by the own signed raw score

UNREVIEWED COMPLETE PROOF CANDIDATE. UR1-UR4 statement/source/type gate
3e8c036/adoptionf9b05fc passed actualOpus5.5/HIGH,17checks,1321.599s,
no requiredrepairs. All8notes adjudicated BEFORE this proof. Original same
attempt returned after providerretry,not a manually restarted review.
This NEW moment proof requires its OWN FULL independent gate before use.
It does not identify source constants,positive scores or an exactlimit.
Original all-Gamma/d1/2/3 sharp/source goal remains ACTIVE.

## 1. Original model,fixed choices and the same physical endpoint

Keep every original H:homog covariance Gamma and its amplitude: even,
nonnegative,positive definite,homogeneous tempered Radon,d=1,2,3,
0<a=alpha_0<1,0<alpha<d or alpha=d=1,alpha+a<2. Gamma=0 is treated
explicitly in Section8. All spaces are real,unitary Fourier,
 E=Hhalf x Hminus-half, H_I=H_t tensor H_sp,
where H_I is the supported slow raw Hilbert completion for ORIGINAL Gamma.
Its norm is not reweighted by g_delta,and is not a sum of fast-block costs.
Fix the accepted smooth even root eta_root,0<=eta_root<=1,eta_root=1 onB1,
suppeta_root subsetB2. Physical noise mask m_R=eta_root(x/R)^2 is used ONCE,
after source smoothing; both displacement and fast velocity are retained.

Choose and HOLD FIXED all auxiliary parameters before delta,B,R limits:
 alpha/4<s_sp<1/2,
 0<gamma<min(1/2,(2-alpha)/2),
 1/2<theta<eta_time<beta_time<min(1-a/2,(3-a-alpha)/2),
 nu=1/theta,1/(1-theta)<r<2/a,nu<=p<2<r,
and a fixed EVEN Q with Qgamma>d,beta_time-eta_time-1/Q>0,
Q>2d/(1-a). Every strict gap exists under the original hypotheses.
Let C_mean be U(17)'s E mean-operator bound for these fixed s_sp,r and
fixed model/cutoff choices. It is independent of R,B,delta but may depend
on the displayed auxiliary choices. The coarse ceiling2+2C_mean^2 below
is NOT an intrinsic or sharp model constant. The score itself is defined
using the actual canonical completed mean of the fixed physical model and
mask family,not a reweighted raw norm or an auxiliary F-column norm.

For 0<delta<1 put L_delta=delta^-1,R_delta=delta^-1+2,
g_delta=delta^((1-a)/2). P_delta is the ACTUAL given-W global E physical
endpoint at L_delta,with this mask/amplitude,as in accepted GC(1)-(2).
Write
                       M_delta=E||P_delta||B(E)^2.          (1)
For each integer B>=1,delta<min(1,1/B),use N=floor(1/(delta B)),
s_m=m delta B,ell_m=B for m<N,ell_N=delta^-1-NB in[0,B),n=N+1.
The actual block Gaussian tuple is X_delta,B of accepted BT(11),stopped
at true ell_m and constantly extended to[0,B],on the SAME W. Its norm is
 ||x||delta,p=(delta sum_m||x_m||Ctheta^p)^(1/p).
Set b_delta,B=2E||X_delta,B||delta,p. From OWN SA Section1(1)-(2),(4),
proof of(4)inSection4,and the actual anchor Section6(19)-(20),or BT(17),
 b_delta,B<=C_(Q,B,p)delta^((1-a)/2-d/Q)->0                 (2)
at EACH fixed B. All Q conditions are independent B/delta; the constant
in(2) need not be uniform B. No diagonal B_delta is asserted.

Direct accepted OWN imports,used at their exact scopes:
- US (uniform-e-spectral-products.md),Sections3-8: actual signed rate,
  uniform E field bound,physical Young growth(19),weighted primitives,
  and alltuple small-residual/polynomial-ball conclusion(33).
- BT (borell-tube-rayleigh-transfer.md),Sections4-7: actual E Gaussian
  support/CM/compactmean eligibility,exact covariance=sqrt(delta)H_delta,
  closed control tubes,Borel radial envelope and Rayleigh integral(25).
  In particular BT(19)-(20),from noise-only GL restart and actual E/F
  restriction/SP baseline,identifies the ordered block product at X with
  P_delta and its norm>=1. This is the SAME P_delta for EVERY fixed B.
- GC (growing-cone-point-upper-transfer.md),(3)-(4),(21)-(25),Section8:
  exact ORIGINAL point/source-first/all-chain transfer,polynomialdata
  cost,inverse kappa parametrization and canonical spatial stationarity.
No theorem about a B-dependent surrogate or independent blocks is used.
No common probability-one event over uncountable delta is required: at
EACH fixed delta,B these identities give the same numerical moment(1).
The model/source limits in these imports are taken FIRST at fixed delta.

## 2. Signed raw score,coercivity and its moving limsup

Let mathcalT_R:H_I->Lr(I;K(E)),I=(0,1),be the actual completed E mean,
||mathcalT_R||<=C_mean. From OWN US1/US2,its integrated signed spectral
rate is Rate_R(Phi)>=0,continuous,and
 Rate_R(0)=0, Rate_R(Phi)<=1+C_mean||Phi||HI.
Define the OWN score and its moving limsup by
 S_R=sup_(Phi in H_I)[2Rate_R(Phi)-||Phi||HI^2/2],
                     V_upper=limsup_(delta->0)S_(R_delta). (3)
Phi=0 gives S_R>=0. For q=||Phi||>=0,C_mean>=0,
 2Rate_R(Phi)-q^2/2
 <=2+2C_mean q-q^2/2
  =2+2C_mean^2-(q-2C_mean)^2/2<=2+2C_mean^2.                (4)
The inequality also follows from the supplied COMPLETE Mathlib weighted
AMGM public type at weights1/2,1/2,bases q^2,(2C_mean)^2>=0. Its finite
use fits all guards including zeros; the square-completion identity is
ordinary algebra,not a newly compiled declaration. Therefore
                   0<=S_R,V_upper<=2+2C_mean^2<infinity.   (5)
No maximizer,finite raw rank,positivity of Phi or convergence of S_Rdelta
is assumed. These scores refer to the fixed mask family and actual mean;
there is no identification with intended author L^*,positive occupations,
actual p1 moments or a source energy convention.

## 3. Generic functional,Gaussian tube and a polynomial coarse bound

For ALL zero-start little-theta-Holder compact-operator tuples define
 F_delta,B(x)=2delta logmax(1,||P_N(x_N)...P_0(x_0)||),
 P_m(x_m)=S_E(ell_m)U_(x_m)(ell_m).
This is the generic Young map,continuous on the full tuple space. For
R>=1,let H_delta,B,R Phi be US's actual normalized mean tuple. BT gives
Cov(X,W(Phi))=sqrt(delta)H_delta,B,R_delta Phi. Its genuine seen-CM norm,
not a mere embedding bound,gives the exact HALF raw action.

Let A_delta,B be the closed ball of radius b_delta,B in the actual
Gaussian support,and put
 G_delta,B(rho)=sup_(a in A_delta,B,||Phi||HI<=rho)
              F_delta,B(a+H_delta,B,R_delta Phi).
From BT the radial function G is finite,nondecreasing,Borel,and
 M_delta<=int_0^infinity (rho/delta)
                      exp((G_delta,B(rho)-rho^2/2)/delta)drho. (6)
The Rayleigh radius is an auxiliary stochastic dominator,not an H-valued
Gaussian norm. No selector/attained supremum or differentiable G needed.
PRIMARY Friz-Hairer2020 Theorem11.6 printed190 is imported THROUGH BT's
proved exact application,including closed enlargements/footnote. We do
not assert a new isoperimetric theorem or redo its AWS construction.

We need QUANTITATIVE B-growth,not BT's unquantified c_Y(B). From US(19)
there is Ctheta=Ctheta(theta)>0,independent B,delta,R and otherwise
model data,with
 log||S_E(ell)U_D(ell)||<=Ctheta B(1+||D||theta^nu),ell<=B.
This includes the physical free factor. Its right side is nonnegative,
so submultiplicativity controls max1 of the ordered product as well.
For any R,||Phi||<=rho,||a||delta,p<=b_delta,B,write
v_m=||a_m||theta,h_m=||(H_delta,B,R Phi)_m||theta. Convexity and US(17)-(18)
give
 F_delta,B(a+H Phi)
 <=2Ctheta B delta n+2^nu Ctheta B delta sum(v_m^nu+h_m^nu),
 delta sum h_m^r<=(32B^(3-1/r)C_mean rho)^r.                (7)
The complete old finite powermean type at exponents p/nu>=1,r/nu>1,
nonnegative norm^nu,positive outer powers and delta>0,n>=2 gives
 delta sum v_m^nu<=(2/B)^(1-nu/p)b_delta,B^nu,
 delta sum h_m^nu<=(2/B)^(1-nu/r)(32B^(3-1/r)C_mean rho)^nu.
All zero entries and p=nu are allowed. Since delta n<=2/B,define
 A0=4Ctheta,
 A1=2^(nu+1-nu/r)Ctheta32^nu C_mean^nu>=0,
 eta_B=2^(nu+1-nu/p)Ctheta B^(nu/p).
The B^(nu/r) and B^(-nu/r) factors cancel EXACTLY,so(7) yields
 F_delta,B(a+H_delta,B,R Phi)
              <=A0+A1 B^(3nu)rho^nu+eta_B b_delta,B^nu.    (8)
In particular this bounds G for ALLrho and all admissible delta. No F
constant-column bound,Gaussian/non-Hamiltonian restriction on a,or uniform
spatial compactness entered. A1=0 is allowed. This proves UR1a.

## 4. Uniform fulltuple error on control balls

For M>0 define the deterministic real number
 E_delta,B,M=max(0,sup_(R>=1,||Phi||HI<=M,||x||delta,p<=b_delta,B)
 [F_delta,B(x+H_delta,B,R Phi)-2Rate_R(Phi)]).              (9)
The supremum is finite by(8) and Rate>=0. The inner functions are
continuous in Phi,x at each fixed R,delta,B by US Section7. E is not a
random variable or a function of controls after supremizing; no Borel
claim about an uncountable R-supremum is needed. Only G's monotone Borel
property is used in the radial integral. There is no joint delta/R
measurability assertion or implicit measurable maximizing control.

Let c_ball>0,kappa_ball>=0,M_B=c_ball B^kappa_ball. By(2),the array
b_delta,B meets OWN US4b(33)'s fixed-B vanishing-residual hypothesis.
That result is uniform R and uses the actual mean/SP denominator and
arbitrary fulltuple residuals. Its exact polynomial radius condition is
US3's s_threshold>r(3+kappa_ball)/(r-nu),each fixed B before delta.
Thus,for the untruncated supremum T_delta,B in(9),
 limsup_(integer B->infinity)limsup_(delta->0)T_delta,B<=0.
The untruncated supremum is itself>=0: Phi=x=0 is allowed,Rate_R(0)=0
and F>=0. Max with0 is therefore harmless. Equation(8)
and(2) bound limsup_delta E at each fixed B,so
 e_B:=limsup_(delta->0)E_delta,B,M_B is finite,>=0,
                         lim_(integer B->infinity)e_B=0. (10)
Indeed limsup_B e_B<=0 and e_B>=0 force that limit. All radii/thresholds
are fixed during the inner limit; their constants may grow rapidly B.
This proves UR1b. No uniform-B stochastic anchor or diagonal limit.

## 5. Finite-delta compact-radius integral and exact tail

Fix B,admissible delta,M>0. For EVERYrho<=M,EVERYa in A_delta,B and
||Phi||<=rho,the definition(9) at R=R_delta gives
 F_delta,B(a+H Phi)-rho^2/2
 <=2Rate_(R_delta)(Phi)-||Phi||HI^2/2+E_delta,B,M
 <=S_(R_delta)+E_delta,B,M.
We used rho^2>=||Phi||^2,not an equality or an optimizer. Taking suprema
and integrating (rho/delta) over[0,M] gives
 int_0^M (rho/delta)exp((G(rho)-rho^2/2)/delta)drho
 <=M^2/(2delta)*exp((S_(R_delta)+E_delta,B,M)/delta).        (11)
This holds even if M^2/(2delta)<1. No finite-delta Laplace principle.

Assume 4A1 B^(3nu)<=M^(2-nu). Set C=A1 B^(3nu)>=0. For rho>=M>0,
1<nu<2 and that cutoff are EXACT guards of the unchanged local kernel
StratonovichHAMAudit.GaussianTail.cutoff_density_split. It gives
 C rho^nu-rho^2/2<=-M^2/8-rho^2/8.
Using(8),
 G(rho)-rho^2/2<=A0+eta_B b_delta,B^nu-M^2/8-rho^2/8.
The following integration is ANALYTIC,not certified by the scalar kernel:
 -d/drho[4exp(-rho^2/(8delta))]=(rho/delta)exp(-rho^2/(8delta)).
Its limit at infinity is0,so
 int_M^infinity (rho/delta)exp((G(rho)-rho^2/2)/delta)drho
       <=4exp((A0+eta_B b_delta,B^nu-M^2/4)/delta).         (12)
This is the same accepted BT(26) primitive with the new verified C. Front4
and the M^2/4 exponent are both retained. The cutoff C=0 causes no exception.
Together(6),(11),(12) prove the fully finite-delta bound
 M_delta<=M^2/(2delta)exp((S_(R_delta)+E_delta,B,M)/delta)
             +4exp((A0+eta_B b_delta,B^nu-M^2/4)/delta).   (13)
Each term is positive and finite. Separately BT(24)-(26) with nu<2 gives
finite M_delta at every fixed delta; SP/BT give M_delta>=1. This proves UR2.

## 6. The two limits on ONE actual moment

Now choose kappa_ball>3nu/(2-nu) and ANY c_ball>0. Set M_B=c_ball B^kappa_ball.
Then M_B>0,diverges asB->infinity,and the cutoff holds for all sufficiently
large integers B. If A1=0,it is immediate. Otherwise divide its sides:
 M_B^(2-nu)/(4A1 B^(3nu))
 =c_ball^(2-nu)/(4A1)*B^(kappa_ball(2-nu)-3nu)->infinity.  (14)
The exponent is STRICTLY positive. This argument uses both constants and
the exponent,not illustrative nu=3/2 tests or validity at all small B.

For each sufficiently large FIXED B apply(13) at M_B. Positive U,V obey
U+V<=2max(U,V),so log monotonicity and delta>0 give
 delta log M_delta<=delta log2+
 max{S_(R_delta)+E_delta,B,M_B+delta log(M_B^2/(2delta)),
     A0+eta_B b_delta,B^nu-M_B^2/4+delta log4}.             (15)
At fixed B,(2) gives eta_B b_delta,B^nu->0. Also delta log4,delta log2->0,
 delta log(M_B^2/(2delta))
              =delta log(M_B^2/2)-delta logdelta->0.
For completeness let t=-logdelta->infinity: -delta logdelta=t exp(-t)->0,
since exp(t)>=t^2/2 for t>0. No normalization factor has been omitted.
Using finite bounds(5),(10),limsup subadditivity and the max inequality,
 U_moment:=limsup_(delta->0)delta log M_delta
                    <=max{V_upper+e_B,A0-M_B^2/4}.         (16)
There is NO B on the left: BT's actual restart identified every B product
with the SAME global P_delta in(1). We are not comparing surrogate moments.
Let integer B->infinity in(16). Equation(10) gives e_B->0,(14) gives
M_B->infinity,while V_upper>=0 is finite by(5). Thus
              0<=liminf_delta delta log M_delta
                <=U_moment<=V_upper<=2+2C_mean^2.           (17)
The lower bound follows from M_delta>=1. The precise order was delta first
at each fixed B/ball/threshold,then B. No convergence of S_Rdelta was
assumed; its MOVING limsup in(3) is retained. No diagonal B_delta or
infinite-dimensional Gaussian density/Laplace theorem was used. This proves UR3.

## 7. Original canonical point moment,all Stratonovich chains

From accepted GC(3),(21)-(25),with kappa_scale=(4-alpha-a)/(3-alpha)>1,
T_delta=delta^(-1/kappa_scale),psi=eta_root(x/R_delta),
 E|u_Gamma(T_delta,0)|^2
 <=v_d^-1||psi||Hhalf^2 M_delta
 <=A_delta M_delta,
 A_delta=v_d^-1 C_eta R_delta^d,
 C_eta=||eta_root||2^2+||grad eta_root||2^2>0.
GC proves this through the actual full-source point limit and E/F/cone/
compact-data identification,not a raw Sobolev point trace or reversed F3.
All source limits are taken FIRST at each fixed delta; all mixed,unequal,
self and empty Stratonovich chains are retained.

GC(24)-(25) gives delta log A_delta->0. Explicitly
 delta log A_delta=delta log(C_eta/v_d)
                   +d delta[log(1+2delta)-logdelta]->0.
Because alpha<2<3 and a<1,kappa_scale>1. The inverse map delta=T^-kappa_scale
is a decreasing bijection(0,1)->(1,infinity),with T^-kappa_scale=delta.
GC Section6 also gives the original point second moment>=1 by its full-
chain/source argument. Its logarithm is defined and finite by this bound.
Take logs,then normalized limsup and(17):
 limsup_(T->infinity)T^-kappa_scale log E|u_Gamma(T,0)|^2
                                 <=V_upper<=2+2C_mean^2.   (18)
GC Section8's ORIGINAL canonical spatial stationarity extends this to every
fixed x. No stationarity of a masked operator is presumed. This proves UR4.
The formal a->0 exponent is (4-alpha)/(3-alpha); no new literature
attribution or boundary-in-a theorem is asserted. Accepted p1/Jensen/lower
bounds remain unchanged; (18) is an OWN signed-score upper,not source L^*.

## 8. Zero covariance,evidence and original scope

If Gamma=0,actualnoise/means vanish,H_I={0},Rate_R=0,S_R=V_upper=0.
Canonical u=1. P_delta=S_E(delta^-1),whose norm is>=1 and <=C(1+delta^-1)
by GC Section8/SP's free symplectic baseline. Therefore
 0<=delta log M_delta<=2delta log[C(1+delta^-1)]->0.
This proves(17)-(18) directly,without importing nonzero Gaussian hypotheses.
The free observable F_delta,B(0) need not be0; BT explicitly includes this
zero-law case. No Hilbert-valued white Gaussian or nondegenerate CM assumption.

All8statement notes adjudicated: exactSApinpoints,fixeds_sp/r-dependent
ceiling,deterministicEsup versusBorelG,oldcompleteAMGMfit and actualnormalizer/
cutoff scope are explicit. Fourwrong_normalizer_rows in the diagnostics
are ANALYTIC restatements,not separatelycomputed wrong-density quadratures.
The fourzero-profile quadratures are actualevaluator checks. No rerun.
Perprecisionresiduals/maxcases retained;18scalar quadratures,48illustrative
cutoffconfigs,12arrayrows/11configs are not PDE/AWS evidence or statistical
samples/enclosures. Oldtailfixture is unchanged and REUSED,NOT rerun.

All Gaussian/integral/limsup/Young/operator/source/point claims remain
INFORMAL analysis requiring this note's FULL independent gate. Old local
GaussianTail and generalMathlibHolder/AMGM publictypes/axioms used only at
stated guards; no newkernel/compiler/count74facts20seams/L0 or official
companion. SelectedPRIMARY11.6 import belongs to acceptedBT,not proved here.

Signed-positive variational comparison/mask removal,intended author energy/
domain/normalization/constants and conditional exactlimit remain OPEN.
Independent PG finite proposal/screen is NOT a premise of any line above.
No actual p1 labelidentity,sourceenergyrepair,Skorohod/contact/HPC/companion/
TeX/PDF/wiki/bib/sourcePDF/sibling/publication action. Original goal ACTIVE.
