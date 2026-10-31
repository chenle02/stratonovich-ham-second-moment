# Radius-explicit stochastic first-driver moments and a growing-mask mean anchor

UNREVIEWED COMPLETE CANDIDATE. SA1-SA3 were frozen and tested before this
proof, in reviews/2026-10-31-radius-stochastic-anchor/. Earlier review debt
was cleared by the completed/adjudicated GC statement and U full gates.
This proof uses neither the GC transfer nor the U Cameron estimate: its
inputs are the already accepted cutoff, actual variance/driver and Gaussian-
transfer constructions. It needs its own FULL independent source/type/
actual-application gate. No growing-R moment exponential or sharp-point
upper is claimed. The full original all-model objective stays ACTIVE.

## 1. Model, exact assertions and accepted inputs

Use ALL original nonzero H:homog Gamma/amplitudes,d in{1,2,3},0<a<1,
0<alpha<d or alpha=d=1,alpha+a<2. W is the GIVEN real raw isonormal noise.
Set Lambda=(1-Delta)^(1/2),E=H^(1/2) x H^(-1/2),with unitary Fourier and
balanced unitary J0(u,v)=(Lambda^(1/2)u,Lambda^(-1/2)v). The free wave is
massless and carries both phase components. Fix real even eta smooth
compact,0<=eta<=1,eta1 onB1,suppB2; physical mask m_R=eta(x/R)^2 ONCE,
R>=1. The base mask zeta in the accepted variance result is eta^2, not eta.

Choose fixed finite B>=1 and exponents
 0<gamma<min(1/2,(2-alpha)/2),
 1/2<theta<eta_time<beta_time<min(1-a/2,(3-a-alpha)/2).
They exist by the original strict subcritical conditions. Choose ONE FIXED
even integer Q>=2 with
 Q gamma>d, beta_time-eta_time-1/Q>0.                         (1)
For the final growing-mask application additionally choose
                         Q>2d/(1-a).                       (2)
All three conditions are possible: their finite lower thresholds have a
finite maximum, and arbitrarily large even integers exist. Constants may
depend on Q and all fixed parameters, including B, but NEVER on R>=1,
noise basis size, a moment v below, or a deterministic raw residual
projection. Q is chosen before delta tends to zero; no endpoint uniformity
as a tends to1 or alpha+a tends to2 is asserted.

We prove:
- For chi_rho(x)=chi0(x/rho),rho>=1,chi0 real smooth,1 onB1,suppB2,
  the actual balanced compact envelopes satisfy, for fixed q>=1,qgamma>d,
    ||P_chi D_gamma||S_q=||P_chi^* D_gamma||S_q<=C_q rho^(d/q). (3)
  Here D_gamma=diag(Lambda^-gamma,Lambda^-gamma),P_chi=J0DchiJ0^-1.
- The ACTUAL first driver M_R(W) on[0,B] satisfies, for every finite v>=1,
    ||M_R(W)||L^v(Ctheta(B(E)))<=C_(Q,B) sqrt(v) R^(d/Q).      (4)
  For a centered Gaussian contraction Y with VarY(f)<=C||f||H^2, the same
  holds for its actual transferred driver with the extra factor sqrt(C).
- For the actual correlated projected block tuple in Section6, its delta-
  weighted norm Z_delta satisfies
    E Z_delta<=(2/B)^(1/p) C_(Q,B) sqrt(p) g_delta R^(d/Q),    (5)
  for every fixed tuple p>=1,g_delta=delta^((1-a)/2). In particular at
  R_delta=delta^-1+2 and with (2), 2E Z_delta tends to0.

Direct OWN accepted inputs, exact scope:
A. compact-sobolev-cutoff.md Sections2-5,scientific6718a16: unitary Fourier
   periodization/recovery kernels and exact WHOLE-SPACE factorization,
   compact singular-value approximation bound,real balanced adjoints and
   both input/output compact envelopes. Its constants were fixed-cutoff;
   the radius-explicit constants are derived here, not attributed to A.
B. actual-two-variance-forms.md Proposition1,scientific227d4bc: BOTH actual
   finite-family variance bounds, with constants EXPLICITLY independentR,
   for the same m_R and balanced E. No HS assumption or original spectral
   density is required. Its auxiliary covariance construction is not a
   replacement noise law or nonlinear covariance comparison.
C. actual-operator-driver.md Sections3-10,scientific93d71e4: SAME-W smooth
   raw-basis coefficient construction,physical localization(12),BOTH
   weighted finite variance envelopes(16),finite Schatten Gaussian bound(19),
   fixed-R allLp Ctheta convergence to the actual first driver and dyadic
   path argument. We track the previously suppressed cutoff radius here.
D. source-operator-convergence.md Theorem1,scientificda9d464: Gaussian
   covariance contraction transfers all fixed-parameter path moments with
   factor sqrt(C), including actual correlated coefficients and separable
   Gaussian paths. No nonlinear/source-solution comparison is imported.
E. raw-block-event-lower.md Section2 and upper-cameron-compactness.md C3:
   actual slow/fast isometry, true block/last-length conventions, stopping
   interaction primitives and delta-weighted tuple norm. No block independence.

## 2. Uniform rescaled periodization and recovery factors

Fix chi0 as above. Choose real psi0 smooth compact,1 on a neighbourhood
of suppchi0,supported inside B3. Since 3<pi, its support lies inside the
cube(-pi,pi)^d. For rho>=1 put L=2pi*rho,psi_rho(x)=psi0(x/rho).
Both physical cutoffs lie strictly inside Q_L and chi_rho psi_rho=chi_rho.

Use the auxiliary torus T_L with UNNORMALIZED L2(Q_L,dx),ONbasis
 e_k(x)=L^(-d/2)exp(i k.x/rho), k inZ^d,
and Sobolev weights <k/rho>^r. This torus is only a factorization device;
no random/state problem on R^d is replaced by a periodic one.

For any real Sobolev index r, accepted A gives the weighted kernels of
P_psi:H^r(R^d)->H^r(T_L) and E_chi:H^r(T_L)->H^r(R^d):
 L^(-d/2)(<k/rho>/<xi>)^r psihat_rho(k/rho-xi),
 L^(-d/2)(<xi>/<k/rho>)^r chihat_rho(xi-k/rho).                (6)
There is no additional c_d: it cancels in the first kernel and the torus
basis normalization gives the second. We KEEP the L^(-d/2) factor.
Since phihat_rho(t)=rho^d phihat0(rho t),Peetre's inequality for either sign
of r gives an envelope for each kernel of the form
 C_r rho^(d/2) F_r(k-rho xi),
            F_r(t)=|phihat0(+-t)|<t>^|r|,                   (7)
with fixed constants and phi0 equal to the relevant base cutoff. Indeed
<xi-k/rho>^|r|=<(rho xi-k)/rho>^|r|<=<rho xi-k>^|r| for rho>=1.
F_r is integrable and has a rapidly decreasing bound; smoothness of its
absolute value at zeros is unnecessary.

In the P kernel, integrate (7) in xi at fixed k to obtain C rho^(-d/2).
At fixed xi its sum over k is at most C rho^(d/2), because
sup_y sum_(k inZ^d)F_r(k-y)<infinity for a fixed rapidly decreasing F_r.
The latter follows by translating y into a unit lattice cell and summing
a power tail of order greater than d, as in accepted A Section2(9).
For E the two row/column roles are reversed. The mixed Schur bound is
the square root of the product of these two bounds; their reciprocal rho
powers cancel. Therefore there are constants INDEPENDENT rho>=1 with
 ||P_psi:H^r(R^d)->H^r(T_L)||<=C_(psi0,r),
 ||E_chi:H^r(T_L)->H^r(R^d)||<=C_(chi0,r).                    (8)
This includes every negative index used below. Bounded kernel extension
and the same Schwartz/torus-polynomial density as A identify the maps
on their full Sobolev domains; no sampling of rough Fourier functions is
assumed. This is the new uniform-factor audit, not a consequence of the
middle diagonal lattice sum alone.

## 3. Exact whole-space envelope and the small volume power

For sigma real let I_gamma be the inclusion
H^(sigma+gamma)(T_L)->H^sigma(T_L). Its diagonal singular values are
 <k/rho>^-gamma. The accepted exact recovery, first on Schwartz data then
by (8) and density on the full whole-space Sobolev domain, gives
 K_(sigma,gamma,rho)=Lambda^sigma chi_rho Lambda^(-sigma-gamma)
    =Lambda^sigma E_chi I_gamma P_psi Lambda^(-sigma-gamma). (9)
The outer Bessel maps are unitary on the relevant spaces. Multiplication
by chi_rho recovers the original R^d function on its support, so (9) is
an exact whole-space equality including negative sigma, not an aliasing
or Galerkin approximation.

Here is a radius-explicit diagonal trace bound. Put u=qgamma>d. For the
unit cube C_k=k+[-1/2,1/2]^d and x in C_k,rho>=1,Peetre gives
 <x/rho><=sqrt(2)<k/rho><(x-k)/rho>
               <=c_d' <k/rho>, c_d'=sqrt(2(1+d/4)).
It follows by integration over the unit cubes that
 sum_k <k/rho>^-u
    <=(c_d')^u int_Rd <x/rho>^-u dx
    =(c_d')^u rho^d int_Rd <y>^-u dy
    =C_(d,u)rho^d<infinity.                                (10)
The last integral is finite by dyadic annuli: outside the unit ball,
the jth annulus has volume at most C_d2^(jd) and weight at most2^(-ju).
This proves a finite constant for every fixed u>d without any hidden rho.

Let lambda_j be the diagonal values of I_gamma in decreasing order. They
tend to0, so its first j-1 spectral coordinates give a rank<j approximation
with operator error lambda_j. Compose it with the outer factors of (9).
Accepted singular-value approximation gives
 s_j(K_(sigma,gamma,rho))<=C_(chi0,sigma)C_(psi0,sigma+gamma)lambda_j.
Summing qth powers and (10) therefore prove
 ||K_(sigma,gamma,rho)||S_q<=C_(sigma,gamma,q,d)rho^(d/q).     (11)
This is also a direct proof of the needed ideal bound; no new Schatten
ideal theorem is presumed. The finite-truncation approximation proves
compactness, and both positive/negative sigma are covered by (8).

The balanced envelope P_chi D_gamma has the two blocks sigma=1/2,-1/2.
Its q-power norm is the SUM of the two block q-power norms, so (11) proves
its bound (3). Accepted A's actual adjoint identities give
 P_chi^*=swap P_chi swap, Kin=swap Kout swap,
because D_gamma commutes with swap. Thus input and output envelopes have
the same norm and (3) follows. P_chi is not declared selfadjoint or a
projection. No unsupported positive-operator-power order is used.
This proves SA1 for the exact whole-space cutoff envelopes.

## 4. Radius-explicit moments of the ACTUAL first driver

Fix the local horizon[0,B]. Accepted C constructs deterministic coefficient
paths A_j from a complete smooth RAW-H ONbasis, with g_j=W(f_j) independent
standard real Gaussians. Let M_N=sum_(j<=N)g_j A_j. These are actual SAME-W
finite paths, not regularized-source approximations or independent time
increments. Both localization identities hold for any real chi equal1
on B_(2R+B+1). Choose
       rho=2R+B+2, chi=chi0(./rho).                         (12)
This satisfies that plateau condition, and rho<=(B+4)R for R>=1.
The physical noise mask is still m_R; chi is only the observation envelope.

By accepted B and C(16), BOTH finite input/output weighted variances have
constant C_B independent of R,N and time interval. For an interval I of
length h<=1 in[0,B], accepted C(19) gives for any EVEN q>=Q,
 ||M_N(I)||Lq(S_q)
  <=sqrt(q-1) sqrt(C_B) h^(1-a/2) B_alpha(h)^(1/2)
                                      ||Kout||S_q,         (13)
where B_alpha(h)=1 for alpha<1,1+log(1/h) for alpha=1,and h^(1-alpha)
for alpha>1. This is the same actual model and the same two variances;
no j-dependent source/derivative constants are summed.

For q>=Q, monotonicity of the UNNORMALIZED Schatten norms gives
||Kout||S_q<=||Kout||S_Q. For clarity, normalize its singular values by
their l^Q norm; all are at most1 and their q-power sum is at most their
Q-power sum. The zero case is trivial. Using SA1 with the SINGLE fixed
index Q, then (12), gives
 ||M_N(t)-M_N(s)||Lq(B(E))
       <=C_(Q,B) sqrt(q) R^(d/Q)|t-s|^beta_time,             (14)
for |t-s|<=1,uniformN,R and EVEN q>=Q. The temporal power follows from
the strict beta_time range: it is below1-a/2 for alpha<1,below
(3-a-alpha)/2 for alpha>1,and the logarithm at alpha=1 is absorbed by
the strictly smaller power. All constants in that elementary power/log
bound are fixed; no R or q occurs there. Coarse increments longer than1
are sums of finitely many unit increments, with constants depending on B.

We retain the path step explicitly. Let D_n(F) be the largest adjacent
increment on the grid kB2^-n of[0,B]. For fine levels with B2^-n<=1,
 ||D_n(M_N)||Lq<=2^(n/q) C_(Q,B)sqrt(q)R^(d/Q)(B2^-n)^beta_time.
There is no independence in this maximum bound. Multiplication by
2^(n eta_time) and summation is uniformly finite for all even q>=Q,
because the geometric ratio is at most
             2^(-(beta_time-eta_time-1/Q))<1.               (15)
The finitely many coarse levels are bounded by the unit partition.
For a continuous zero-start Banach path, the deterministic dyadic chaining
estimate in accepted C Section9 gives its C^eta_time norm at most a
constant times this weighted sum. It follows that
 sup_N ||M_N||Lq(Ctheta(B(E)))
                      <=C_(Q,B)sqrt(q)R^(d/Q),             (16)
using theta<eta_time and the fixed-horizon Holder embedding.

For each FIXED R, accepted C constructs the SAME actual M_R as the allLp
Ctheta limit of these M_N. Passing (16) to that limit yields the same
bound for M_R for every even q>=Q. Uniformity of the convergence in R
is NOT needed or claimed: the limiting inequality has a constant uniform
in R because the finite-N bounds had the explicit form (16).
For arbitrary finite v>=1,choose an even q>=max(v,Q) with
q<=v+Q+2<=(Q+3)v. Lyapunov and (16),absorbing sqrt(Q+3) into the FIXED
constant, give (4). This proves SA2 for the actual noise W, including
Gaussian sqrt(v) growth with a radius exponent d/Q chosen arbitrarily
small by fixing a large enough Q. Constants may grow with Q.

## 5. Actual covariance contractions and arbitrary deterministic residuals

Let Y be any centered Gaussian linear noise on fast raw tests on the
actual coupled space,with VarY(f)<=C||f||H^2,C>=0. It may have correlated
basis coefficients or use an auxiliary retaining Gaussian extension.
Accepted Gaussian-transfer Theorem1 constructs its compact-valued first
path with the SAME deterministic masked coefficients and gives
 ||M_R(Y)||Lv(Ctheta)<=sqrt(C)||M_R(W_ref)||Lv(Ctheta).       (17)
W_ref is any actual isonormal reference with the original raw covariance,
whose norm law is the SAME canonical first-driver law; no nonlinear
comparison or equal-law replacement of Y is made. Its norm bound is (4).
Thus (17) proves the asserted contraction form with sqrt(C) and constants
independent of the particular contraction. C=0 gives zero directly.
This is an accepted LINEAR Gaussian comparison applied to the quantitative
bound, not a new moment comparison for solutions.

For the block construction let W again denote the GIVEN slow noise on H_W,
and Pi any DETERMINISTIC orthogonal projection there. It may have infinite
rank and may depend on delta,R; it is not random conditioning on W. The
accepted raw isometry gives
 Y_m(f)=W((I-Pi)T_(delta,m)f), VarY_m(f)<=||f||H_fast^2.       (18)
These residuals are jointly Gaussian on the same W and may be correlated
across m. They need not belong to the minimal span of W_(delta,m),which
is not a hypothesis of Gaussian transfer. Equation(17) therefore applies
with C=1 to every actual residual, uniformly in m and Pi.

## 6. The actual weighted block mean anchor at R_delta

Take integer B>=1,0<delta<min(1,1/B),N=floor(1/(delta B)),n=N+1,
s_m=m delta B,ell_m=B for m<N,ell_N=1/delta-NB in[0,B).
Each interaction path M_R(Y_m) starts at0. Stop it atell_m and extend it
constantly to[0,B]; stopping does not increase its supremum or Holder
seminorm. The last empty block gives the zero path. Define
 X_m=g_delta M_R(Y_m) stopped in this way,
 g_delta=delta^((1-a)/2),
 Z_delta=(delta sum_(m=0)^N||X_m||Ctheta^p)^(1/p),p>=1 fixed. (19)
All norms are the actual E driver/operator norms. No field is replaced
by a pointwise Gaussian potential or an HS object.

By probability normalization,Lyapunov,and linearity of expectation of the
FINITE sum,with no time-block independence,
 E Z_delta <=(E Z_delta^p)^(1/p)
   =(delta sum_m E||X_m||Ctheta^p)^(1/p)
   <=(delta n)^(1/p) g_delta C_(Q,B)sqrt(p)R^(d/Q).
Since delta B<1,n<=2/(delta B),this gives exactly (5). All delta weights
and the factor (2/B)^(1/p) remain explicit; a maximum over blocks is not
substituted for this averaged Banach norm. This is SA3 for any R>=1.

Now put R_delta=delta^-1+2<=3/delta. With Q fixed to satisfy (2),
 zeta=(1-a)/2-d/Q>0.
Indeed Q>2d/(1-a),with positive Q and1-a,is equivalent to
Q(1-a)>2d. Dividing by2Q proves the strict positive difference. Hence
 2E Z_delta<=2(2/B)^(1/p)C_(Q,B)sqrt(p)3^(d/Q)delta^zeta->0. (20)
The power bound is at every fixed B,p,model,Q. In particular it is uniform
in the deterministic raw projection,including the infinite-spatial-rank
projection from the separate accepted Cameron estimate. No bound uniform
in Q,a->1,B->infinity or random projections is claimed.

## 7. Evidence boundary and the remaining original goal

This is a complete UNREVIEWED analytic candidate for SA1-SA3. Its use of
accepted fixed-R constructions is explicit: variance was already uniformR;
the cutoff envelope and finite-N/time-chain constants have now been tracked.
The torus diagonal was only the middle factor of an exact whole-space
identity. Its lattice diagnostics are NOT operator/Schatten singular values
of Kout and are not stochastic simulations. The outer Schur factors are
proved uniformly in Sections2-3,not inferred from those measurements.

The retained diagnostics cover18lattice sums,3exact small-mode multiplicity
calibrations and9exact scalar feasibility/decay checks. Their analytic
remainder expression was evaluated in floating arithmetic,not certified.
Six cases show that Qgamma>d alone is insufficient for the desired decay;
this is a moment-index choice failure,not a no-go for the original problem.
Near a=1,the convergence in (20) may be extremely slow and constants large;
we claim only fixed-parameter asymptotics. No unchanged experiment was rerun.

No new Lean declaration/compiler/count is claimed. The new functional-
analytic factorization/singular-value/lattice/path/Gaussian and weighted-
expectation steps are analytic. Elementary positive real-power/Archimedean
parameter reasoning is written explicitly,not labeled kernel-certified.
The accepted finite Gaussian/Schatten theorem is reused through its already
reviewed actual operator application,not promoted to a new formal result.
74acceptedfinitefacts20seams/L0 PROPOSED and companion decision4 unchanged.

Equation(20) supplies only the missing EXPECTED norm anchor. It does not
itself supply a uniform Cameron bound or Gaussian concentration/exponential
estimate; that is a separate theorem using both budgets with its own gate.
There is no infinite retained-head Gaussian integration,localization/entropy,
nonlinear product upgrade or original sharp point-moment upper here.
GC transfer has separately passed its FULL gate; SP remains frozen.
If Gamma=0,the actual first drivers vanish and all stochastic bounds here
are zero directly; SA1 is deterministic and unchanged. Intended
source-energy normalization,matching sharp constants and conditional exact
limit remain OPEN. No contact,Skorohod development,HPC,companion,TeX/PDF/wiki/
bib/sourcePDF/sibling/publication action or whole-goal completion claim.
