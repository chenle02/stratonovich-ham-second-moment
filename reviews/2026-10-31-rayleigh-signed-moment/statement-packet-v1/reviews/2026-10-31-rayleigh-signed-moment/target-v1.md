# UR1-UR4 exact signed-score moment target, BEFORE diagnostics

UNREVIEWED statements,not a theorem or premise. Original all-model sharp/
source goal unchanged. Accepted BT transfer and US1-US4 uniform-E tools
are inputs,not an automatic moment theorem. No signed-positive/source
normalization or intended constant identification.

## Actual original model and common endpoint

ALL original H:homog Gamma/amplitudes,d=1,2,3,0<a<1,0<alpha<d or
alpha=d=1,alpha+a<2; zero covariance separately included. Real E=Hhalf x
Hminus-half,unitary Fourier,physical mask m_R=eta_root(x/R)^2 ONCE after
smoothing. Given supported slow raw Hilbert H_I,actual SAME-W fast noise.
Set 0<delta<1,L_delta=delta^-1,R_delta=delta^-1+2,
g_delta=delta^((1-a)/2). Let P_delta be GC's actual global E physical
endpoint on[0,L_delta],with mask R_delta and amplitude g_delta,and
 mathfrakM_delta=E||P_delta||B(E)^2.
It is the SAME endpoint/moment for every block size B below,by BT(19)/GL
noise-only restart and E/F intertwining,not a B-dependent surrogate.
Both displacement and fast velocity,all temporal correlations retained.
No raw point trace,independent blocks or finiteGaussian head.

Fix compatible exponents ONCE:
 0<gamma<min(1/2,(2-alpha)/2),
 1/2<theta<eta_time<beta_time<min(1-a/2,(3-a-alpha)/2),
 nu=1/theta,1/(1-theta)<r<2/a,nu<=p<2<r.
Choose a fixed EVEN Q with Qgamma>d,beta_time-eta_time-1/Q>0,
Q>2d/(1-a),before delta and B. For each integer B>=1 and
0<delta<min(1,1/B),use accepted true clocks N=floor(1/(delta B)),
ell_m=B for m<N,ell_N=delta^-1-NB in[0,B),including partial/empty cells.

X_(delta,B) is the ACTUAL fullnoise E block tuple on R_delta from BT,
in its separable little-theta-Holder K(E) space with norm
 ||x||_(delta,p)=(delta sum||x_m||theta^p)^(1/p).
 b_(delta,B)=2E||X_(delta,B)||_(delta,p)
 <=C_(Q,B,p)delta^((1-a)/2-d/Q)->0 at each fixed B.
Constants may grow with B. No uniform-in-B anchor or diagonal choice.
At fixed delta,B,its exact covariance is sqrt(delta)H_(delta,B,R_delta)
on H_I,where H is the normalized deterministic mean primitive of US.
BT's genuine seen-CM/support/closedtube/Rayleigh law applies,including
zero-law F(0) nonzero. No R-uniform compactness asserted.

Let F_(delta,B)(x)=2delta log max(1,||ordered actual Young block product||)
be the globally defined generic Young functional on ALL tuples. The
actual X gives exp(F/delta)=||P_delta||^2 by SP. Put
 A_(delta,B)={a in actualsupport:||a||delta,p<=b_(delta,B)},
 G_(delta,B)(rho)=sup_(a in A,||Phi||HI<=rho)
                  F_(delta,B)(a+H_(delta,B,R_delta)Phi).
It is finite,nondecreasing,Borel by BT. Its accepted bound is
 mathfrakM_delta<=int_0^infty (rho/delta)
                     exp((G_(delta,B)(rho)-rho^2/2)/delta)drho.
The Rayleigh auxiliary is not a Hilbert Gaussian norm.

## UR1: own signed score,polynomial coarse envelope and small tube error

For each R>=1 let Rate_R be the US integrated signed spectral rate of
mathcalT_R Phi,with uniform ||mathcalT_R||HI->Lr(K(E))<=C_mean. Define
 S_R=sup_(Phi in H_I)[2Rate_R(Phi)-||Phi||HI^2/2].
Then 0<=S_R<=2+2C_mean^2,without a maximizer or finite rank. This is
an OWN signed score,not authorL^*,a positive score or actual p1 identity.
 V_upper=limsup_(delta->0)S_(R_delta) is finite and nonnegative;
no convergence of S_(R_delta) is assumed.

Use Ctheta>0 from US(19),independent B/delta/R,and define explicit
 A0=4Ctheta,
 A1=2^(nu+1-nu/r)Ctheta32^nu C_mean^nu>=0,
 eta_B=2^(nu+1-nu/p)Ctheta B^(nu/p).
For all admissible delta,B,rho>=0,
 G_(delta,B)(rho)<=A0+A1 B^(3nu)rho^nu+eta_B b_(delta,B)^nu.   (UR1a)
This sharper B-growth comes from US(19),not an unquantified BT c_Y(B).

For every M>0 define deterministic fulltuple error
 E_(delta,B,M)=max(0,sup_(R>=1,||Phi||<=M,||x||delta,p<=b_(delta,B))
 [F_(delta,B)(x+H_(delta,B,R)Phi)-2Rate_R(Phi)]).
All these suprema finite/Borel in controls,not random selections. For
ANY c_ball>0,kappa_ball>=0,M_B=c_ball B^kappa_ball,US4b implies
 e_B:=limsup_(delta->0)E_(delta,B,M_B)>=0 finite,
                         lim_(integer B->infty)e_B=0.      (UR1b)
No prescribed diagonal B_delta; each M_B fixed in the inner delta limit.

## UR2: finite-delta bulk plus tail,with every normalizer

For ANY M>0 satisfying 4A1 B^(3nu)<=M^(2-nu),and all admissible delta,
 mathfrakM_delta
 <= M^2/(2delta)*exp((S_(R_delta)+E_(delta,B,M))/delta)
    +4exp((A0+eta_B b_(delta,B)^nu-M^2/4)/delta).            (UR2)
Bulk requires G(rho)-rho^2/2<=S_Rdelta+E for ALLrho<=M,using the raw
half-action and fulltube bound. No attained sup/control selector needed.
Tail reuses the exact old scalar GaussianTail.cutoff_density_split at
x=rho>=M>0,C=A1 B^(3nu)>=0,1<nu<2 and that cutoff condition,then the
analytic Rayleigh primitive from BT(26). Front4 and M^2/4 retained.
MathfrakM_delta is finite,>=1 by BT/SP and zero-case free bound.

## UR3: actual operator-moment asymptotic with moving signed score

Choose kappa_ball>3nu/(2-nu),c_ball>0,M_B=c_ball B^kappa_ball.
Cutoff holds for all sufficiently large B,not necessarily everyB. Use
the US3 schedule s>r(3+kappa_ball)/(r-nu) for its mean threshold when
applying UR1b. At each fixed B,delta->0 FIRST; then integer B->infty.
 0<=liminf_delta delta log mathfrakM_delta
   <=limsup_delta delta log mathfrakM_delta<=V_upper<infty. (UR3)
Explicitly control delta log(M_B^2/(2delta)),delta log4,delta log2,
eta_B b_delta,B^nu and moving S_Rdelta+E. Do not infer convergence of
S_Rdelta,swap limits or compare different B-dependent moments. No
unproved infinite-dimensional Laplace principle/density/entropy claim.

## UR4: ORIGINAL point second moment at canonical scale

For kappa_scale=(4-alpha-a)/(3-alpha),every fixed x inR^d,
 limsup_(T->infty)T^(-kappa_scale)log E|u_Gamma(T,x)|^2
                            <=V_upper<=2+2C_mean^2.        (UR4)
Use EXACT accepted GC(3)-(4),T_delta=delta^(-1/kappa_scale),polynomial
data factor A_delta=v_d^-1 C_eta(delta^-1+2)^d with delta logA_delta->0,
canonical stationarity and source limits FIRST. Full mixed/self/empty
Stratonovich chains retained. No raw point trace or F3lower reversal.
ZeroGamma has u=1,S_R=0,freeoperator polynomialgrowth and V_upper=0.

## Required falsification/evidence before proof

Freeze statements BEFORE diagnostics. Small scalar Rayleigh integrals
with moving/nonmoving profiles must check exact normalization and
finite-delta normalizer cost; a finite-delta equality to supaction is not
a Laplace upper proof. A bounded oscillating score must keep limsup,not
arbitrary subsequence value or an assumed limit. Check B-polynomial cutoff
with both constants and exponent (eventual,not all B); include A1=0.
An exact two-parameter array must refute unjustified diagonalization.
Old front4/quarterexponent fixture is reused,not rerun unchanged.

Numerical quadratures/finite profiles/arrays are analytic-mechanism
comparators,not actual wave/PDE/AWS simulations or enclosures. Compare
unrounded precision objects,retain perprecision residuals/maximizingcases,
count duplicate/zero cases honestly,no statisticalconfidence from rows.
Complete old kernel/publictypes/axioms and actual guards supplied; no new
Lean/compiler/count74facts20seams/L0. Limiting/integral/operator claims
remain ANALYTIC. Source-model/primary fit and own FULL proof review required.

Signed-positive variational/maskremoval,intended author energy/domain/
normalization/constants and conditional exact limit remain OPEN. This
component pursues the original goal,does not replace its constants. No
p1 label identity,Skorohod/contact/HPC/companion/sourcefix/TeX/PDF/wiki/bib/
sibling/publication action. All-model originalgoal ACTIVE.
