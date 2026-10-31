# Actual coupled raw blocks, positive cone growth and point lower rate

ACCEPTED at the scoped full analytic/source/type/application gate:
Opus5.5/HIGH, twelve PASS checks, PASS_WITH_NOTES, no required repairs,
516.106 seconds at source d4d876e. Exact evidence and seven optional
clarifications are in reviews/2026-10-31-raw-block-event/.
The frozen scientific candidate is retained unchanged. The statement gate
was separate. Full original all-dimensional sharp/source goal remains ACTIVE.

## 1. Exact theorem, spaces and named inputs

Use nonzero original H:homog Gamma, d=1,2,3, a in(0,1),
0<alpha<d or alpha=d=1, alpha+a<2. Fix ANY nonnegative nonzero real
Psi in C_c^infinity((0,1)xR^d). W is the GIVEN raw-law Gaussian noise
in the semiscaled variables. No samplewise equality to an original
unscaled noise at every physical time is asserted. Put

 Z=W(Psi), v=E Z²,
 h_s(x)=int_0^1 |s-r|^-a (Gamma*Psi(r,.))(x)dr.

Choose one finite even [0,1] mask m_R as in the accepted compact mean
theorem. With V_s=m_R h_s, s in I=[0,1], let lambda_s be its positive
ground rate and I_R=int_0^1 lambda_s ds. The theorem proposed here is

 Q2:=liminf_(T->infinity)T^(-kappa)log E|u(T,0)|²>=2I_R-v/2,
                  kappa=(4-alpha-a)/(3-alpha),                  (1)

for every such fixed Psi and eligible mask, with the ORIGINAL raw v/Psi
unchanged. This is not yet identification with source L_* or a sharp upper.

OWN accepted inputs, not re-certified here:
- compact-mean-ground-family.md, scientificbfbd472/adoptionab6596f: v>0
  finite; mean h_s smooth on compact time/spatial sets; common finite-R
  positive ground family for V_s, uniform lambda>=l>0, real F projections,
  normalized complementary bound, norm-continuous frame, positive original
  entrance and displacement-test margins, and actual lambda Lipschitz on I.
- actual-operator-driver.md and source-operator-convergence.md: actual raw
  SAME-W first drivers, finite Lipschitz compact-valued coefficient paths,
  Lp Ctheta operator convergence/sqrt(p) moments; literal raw noise-matrix
  forms; Gaussian transfer under variance/error contraction and testwise
  convergence; retaining heat/Laplace sources and ordinary first responses.
- fixed-mask-young-constant-phase.md: EXACT real Hilbert phase
  F=E directsum R², E=H1/2 x H-1/2, embedding i:E->F, free group S_F,
  physical source/Young identity and all-finite-Lp source convergence;
  local Lipschitz Young map and exp(C||driver||^(1/theta)) bound; compact
  deterministic bases. The driver range is iE; E is not dense in F.
- fixed-mask-moment-transfer.md F1-F3: noise-only source average comparison
  and raw L2 tested-average-to-canonical-point inequality at unit amplitude.
- direct-event-calibration.md Section1(S)-(M), scientific9d77f90: exact
  canonical LAW scaling, all original covariance measures, including all
  mixed orders/self-pairings and Green-before-noise convention in d3.

Fix real phi>=0 smooth compact, integral1. In F write e0=(0,1,0), ||e0||=1,
O_phi(z,c1,c2)=<z1,phi>+c1. It is bounded. All source limits below are
at FIXED delta and finite horizons BEFORE delta tends to0. No point trace
on H1/2, noise-Hilbert mask multiplier, HS path assumption or covariance
order of nonlinear waves is used.

## 2. Actual fast-noise pullbacks and local clocks

Fix an integer B>=1, later chosen from the cone. Let
0<delta<min(1,1/B), N=floor(1/(delta B))>=1,
s_m=m delta B,0<=m<=N, tau=1/delta-NB in[0,B). Put g_delta=delta^((1-a)/2).
For a smooth compact positive-fast-time test f extend it by zero and set

 T_(delta,m)f(s,x)=delta^(a/2-1)f((s-s_m)/delta,x),
 W_(delta,m)(f)=W(T_(delta,m)f).                               (2)

These are actual functionals on the SAME W as Z. In the raw covariance
inner product, s=s_m+delta u,t=s_m+delta r gives factors
delta^(a-2)delta²delta^(-a)=1, with spatial Gamma unchanged. Thus T is an
isometry on tests, respects nulls and extends to the raw-H completion.
W_(delta,m) is isonormal with the original raw covariance, but the noises
are NOT declared independent. Let W_fast=W_(delta,0). Direct test
substitution gives W_(delta,m)(f)=W_fast(f(.-mB,.)), with its supported
shift. This is an actual common-space identity, not only stationarity in law.

Choose accepted auxiliary gamma and Holder exponents
0<gamma<min(1/2,(2-alpha)/2),
1/2<theta<beta<min(1-a/2,(3-a-alpha)/2).
Let A_R(W_(delta,m)) be the actual masked first driver on F, local clock
u in[0,B], and define

 X_m=g_delta A_R(W_(delta,m)),
 H_m(u)=int_0^u S_F(-r)iB(V_(s_m+delta r))S_F(r)dr.            (3)

Here B(V):F->E is the actual multiplier (0,V(z1+c1)); the integral is
strong on states. h_s and V_s extend smoothly to s in[0,2] by their
same convolution formula. Since s_m<=1 and delta B<1, this extension
covers every clock in(3); no ground family outside I is assumed. H_m
starts at0 and is operator-norm Lipschitz, with uniform Ctheta norm for
these delta,m: the compact base bound uses sup_(s<=2)(||V_s||infinity+||V_s||2).

The slow equation is delta² V_tt=Delta V+sqrt(delta) W V. At a block
t=s_m+delta u its phase is (V,delta V_t), and its local derivative-noise
coefficient is sqrt(delta) W(s_m+delta u), equivalently g_delta W_(delta,m)
under(2). Both displacement and FAST velocity will pass between blocks;
the state is never replaced by a scalar solution value.

## 3. Separable compact-operator input and the actual mean covariance

Let K(F) have the OPERATOR norm. It is separable: in a real countable
Hilbert basis, finite-rank rational matrices are dense. Indeed compact T
has P_n T P_n->T in norm, using finite-basis projections P_n and compactness
of T,T*, after which finite entries can be approximated rationally.
Let B0=h0^theta([0,B];K(F)) be the Ctheta closure of zero-initial polygonal
K(F)-valued paths. It is a closed Banach space and separable. Rational
breakpoints and rational finite matrices approximate each polygonal path.
For the breakpoint approximation use uniform error tending to0 and a
uniform Lipschitz bound; the elementary inequality
[f]_theta<=(2||f||infinity)^(1-theta)Lip(f)^theta proves Ctheta convergence.
The same observation puts every zero-initial Lipschitz compact-valued path
in B0. This is NOT a separability assertion about all B(F) Holder paths.

Accepted finite raw coefficient paths on F are i A_j Lpsi, Lipschitz and
compact-valued, with their Gaussian sums converging in Lp Ctheta. Hence
each actual X_m belongs to B0 and is strongly measurable there. Its law
is g_delta times the raw-driver law, giving for all p>=1

          ||X_m||_(Lp B0)<=C_R,B sqrt(p)g_delta.               (4)

Let B_delta=B0^(N+1) with maximum norm, X=(X_m)_(m<=N).
Every finite coefficient list of all X_m together with Z consists of
functionals of the same isonormal W. It is jointly centered Gaussian.
The L2 path limits preserve this for every continuous linear functional
on B_delta (variances and scalar characteristic functions converge).
Thus (X,Z) is an actual jointly Gaussian Banach/scalar variable, not just
a covariance majorant. Its Bochner mean b=E[XZ] exists since
E||XZ||<=||X||L2 sqrt(v)<infinity and B_delta is separable.

For a smooth compact fast-time test f the raw covariance and(2) give

 E[W_(delta,m)(f)Z]
  =delta^(a/2-1)int f((s-s_m)/delta,x)h_s(x)ds dx
  =delta^(a/2)int f(u,x)h_(s_m+delta u)(x)du dx.                (5)

The derivative-noise Jacobian here is essential. Absolute Fubini follows
from a<1, compact test supports and locally finite Gamma. Apply(5) to the
literal raw matrix kernels of the accepted first driver: for Schwartz
E inputs/tests they are smooth bounded spatially compact wave products
times a time indicator. Smooth bounded approximations of the indicator
converge in raw H by dominated convergence against |u-r|^-a Gamma; their
pairings with the smooth h on that compact converge as well. Thus(5)
holds for the actual completed matrix kernels, using their actual E-adjoint.
It gives

                    b_m(u)=sqrt(delta) H_m(u).                 (6)

Indeed g_delta delta^(a/2)=sqrt(delta). The unchanged finite lemma
JointTilt.shifted_amplitude checks the coefficient divided by sqrt(delta),
with its actual guard delta>0. No source fBm normalization constant enters.

For constant F inputs, the accepted driver extension uses Lpsi, taking
the two columns to (psi,0),(0,psi) in E. These are Schwartz inputs, so the
same computation applies; finite propagation identifies the deterministic
primitive on F. E inputs plus both constants are dense in F, whereas E
alone is not. Boundedness and rational-time equality extend(6) to all F
inputs/output tests and all times. Both sides are Ctheta operator paths,
so(6) holds as a FULL path identity. It also proves H=b/sqrt(delta) belongs
to B_delta, without presuming a new Schatten or HS path.

## 4. Gaussian change of law on ALL norm-Borel inputs

We prove the exact path-space statement. For real s put
dQ_s/dP=exp(-sZ-s²v/2). Completing the square for the real N(0,v) density
gives total mass1; the density is positive/finite, so Q_s and P are equivalent.
For finitely many real continuous coordinates l of X, (l(X),Z) has a
finite centered Gaussian law, equal IN LAW to (T G,z.G), where G is
a finite standard normal vector. A covariance square root supplies this
even if the joint covariance is singular; no covariance inverse is used.
Then Tz=l(b), |z|²=v. Substitution G'=G+s z in its ordinary normal density
gives, for every bounded Borel f,

                   E_Qs f(l(X+s b))=E f(l(X)).                (7)

To pass to norm-Borel laws, use each block's matrix entries in a real
Hilbert basis at rational times together with0,B. These countably many
continuous linear coordinates generate the norm-Borel sigma-field on
B_delta. Here is the operator-norm detail: for a countable dense set D
of unit vectors obtained from normalized rational FINITE basis combinations,
||T||op=sup_(u,w in D)|<Tu,w>|. Each such expression is a finite combination
of matrix entries, not merely the largest individual entry. Supremum and
Holder norms of continuous paths are suprema over rational times/pairs.
Thus the distance to every fixed B_delta element is coordinate-measurable.
Open balls are measurable by rational closed-ball approximation; separability
makes every open set a countable union of such balls with dense centers.
Conversely each coordinate is continuous. This proves the sigma-field claim,
without copying an HS sum-of-squares norm formula.

Finite coordinate cylinders form a pi-system generating that sigma-field.
The two laws in(7) agree there, so pi-lambda uniqueness gives agreement
on all norm-Borel sets. Simple functions and monotone convergence now give
for EVERY nonnegative norm-Borel j on ALL B_delta,

 E j(X)=E[exp(-sZ-s²v/2)j(X+s b)],
 E j(X)=E[exp(-Z/sqrt(delta)-v/(2delta))j(X+H)]                (8)

in the second line s=1/sqrt(delta) and(6) are used. Either side may initially
be infinite. The deterministic translate lies in B_delta, and all inputs
are defined there; no translated exceptional-domain set or Banach conditional
expectation/RNP assumption is used. Equivalent measures preserve version
null sets. This proves the actual SAME-Z identity, not just an MGF check.

## 5. Actual Young blocks and uniform scaled-maximum estimates

For x in B0 define its physical local flow D_x(u)=S_F(u)U_x(u,0), using
the accepted globally defined linear Banach Young map on operator paths.
Put D_m^0=D_(X_m), D_m^+=D_(X_m+H_m). The latter is the actual compact
base V_(s_m+delta u) plus retained noise, by the deterministic-base input
and(3). It is not an independent noise copy or a discarded residual.
For arbitrary x in B0 this same definition makes sense on ALL F, even if
x has no special spatial compatibility; this will define the Borel j.

Let M_delta=max_(m<=N)||X_m||B0. It INCLUDES g_delta. By(4), for p>=1,

 ||M_delta||Lp<=(N+1)^(1/p)C sqrt(p)g_delta
                 <=C' sqrt(p)delta^((1-a)/2-1/p).             (9)

We used N+1<=2/delta for B>=1,delta<1. No independence was used. For every
fixed q choose p>max(q,2/(1-a)); (9) and norm monotonicity give
M_delta->0 in Lq and probability.

The uniform square-exponential bound needs more than a union on each term
starting at degree2. Choose integer n0 with n0(1-a)>=1. For n>=n0, (4) gives

 E M_delta^(2n)<=(N+1)C^(2n)(2n)^n g_delta^(2n)
          <=2C^(2n)(2n)^n delta^(n(1-a)-1)<=2C^(2n)(2n)^n.

For 1<=n<n0 use Lyapunov, E M_delta^(2n)<=
(E M_delta^(2n0))^(n/n0), uniformly bounded. In exp(c M_delta²) the finitely
many low terms are therefore bounded, while n!>=(n/e)^n bounds the high
tail by 2sum_(n>=n0)(2e c C²)^n. For sufficiently small c>0,

                    sup_delta E exp(c M_delta²)<infinity.    (10)

This is not asserted for the UNSCALED maximum M_delta/g_delta.

Let H_m^stat be the deterministic primitive of constant V_(s_m). Accepted
compact-base bounds and mean smoothness on[0,2] imply

 sup_m max(||H_m||Ctheta,||H_m^stat||Ctheta)<=H0<infinity,
 sup_m||H_m-H_m^stat||Ctheta<=C_(Psi,R,B)delta.                (11)

Indeed ||V_(s_m+delta r)-V_(s_m)||infinity+||.||2<=C delta B for r<=B;
integrating bounded free groups gives a Lipschitz primitive difference,
hence its Ctheta bound on this fixed B. The static primitive uses the same
supremum over s<=2 of ||V_s||infinity+||V_s||2, so the same H0 bounds it.
Strong state integrals suffice.
On {M_delta<=1}, the accepted local Lipschitz Young estimate on the fixed
driver ball H0+1, followed by the bounded S_F(u), gives

 Eop_delta:=max_m sup_(u<=B)||D_m^+(u)-P_(s_m)(u)||B(F)
                 <=C_(Psi,R,B)(M_delta+delta).                (12)

This proves convergence in probability. For Lq, use the global Young bound:
max_m sup_u||D_m^+(u)||<=C_B exp(C_B(1+H0+M_delta)^(1/theta)).
Since 1/theta<2, for every finite r, the rth power is bounded by a constant
times exp(c M_delta²), with c from(10). Thus the maximum physical norms have
uniform moments of EVERY finite order. The deterministic P_s norms on[0,B]
are uniformly bounded. Higher moments give uniform integrability of
Eop_delta^q, and probability convergence gives

                        Eop_delta->0 in every finite Lq.     (13)

Suprema in these statements are measurable: F is separable, and for a
countable dense unit state set, u->(D_m^+(u)-P_(s_m)(u))z is continuous.
Supremum over states and rational u (plus endpoints) equals the full
operator/time supremum. No individual physical path is claimed norm-
continuous in time. The only ground templates used have s_m<=1; mean
arguments up to2 in(11) require no spectral statement outside I.

## 6. New-F indexed cone, every full block and terminal remainder

We re-establish the actual cone on F, not import the old d1 space. From
the accepted family fix C_gap>=1,eta_gap>0 so
||exp(-lambda_s t)P_s(t)Q_s||<=C_gap exp(-eta_gap t), all s in I,t>=0.
Let

 a_*=inf_I ell_s(e0)>0, j_*=inf_I O_phi(e_s)>0,
 M_e=max(1,sup||e_s||), M_l=max(1,sup||ell_s||),
 M_P=max(1,sup||Pi_s||), M_Q=1+M_P, M_z=M_e+1,
 E0=||e0||=1, H_obs=max(1,||O_phi||).

Fix 0<rho<1/2. Choose FIRST vartheta=min(1,j_*/(16H C_gap))>0.
Next choose INTEGER B>=1 large enough that

 q_B=C_gap exp(-eta_gap B)<=min(1/8,vartheta a_*/(8M_Q E0)).        (14)

Choose nu>0 with nu M_z<=min(rho/2,vartheta,1/4). Uniform continuity of
ell,Pi on compact I supplies omega>0 so adjacent distance<=omega gives
both norm differences<=nu (halve a strict modulus radius if needed).
Finally choose epsilon_op>0 satisfying all five positive budgets

 M_l epsilon_op M_z<=rho/2, M_Q epsilon_op M_z<=vartheta/4,
 M_l epsilon_op E0<=a_*/2, M_Q epsilon_op E0<=vartheta a_*/8,
 H_obs epsilon_op M_z<=j_*/8.                                   (15)

The minimum of the five ratios is positive. Aperture was chosen BEFORE B,
using the normalized complementary estimate, never an exp(CB) terminal norm.

For s in I define the actual two-entry cone by z=A e_s+r,
A=ell_s(z)>0,ell_s(r)=0,||r||F<=vartheta A. Equivalently r=Q_s z.
Take any N>=1, adjacent indices sigma_0,...,sigma_N within omega, and
real bounded D_m(u) with sup_(m,u<=B)||D_m(u)-P_(sigma_m)(u)||<=epsilon_op.
No positivity/composition/independence of these D is assumed.

Entrance: z1=D_0(B)e0 has normalized amplitude
exp(-lambda_b B)ell_b(z1)>=a_*-M_l epsilon_op E0>=a_*/2,
where b=sigma_0. By commutation and(14)-(15), its normalized residual is
at most q_B M_Q E0+M_Q epsilon_op E0<=vartheta a_*/4.
Thus z1 is in the first cone with residual ratio<=vartheta/2 and amplitude
at least exp(lambda_b B)a_*/2. No constant was put in global E.

For z=A e_b+r in the old cone, ||z||<=M_z A. Rebase to adjacent c BEFORE
using the complementary estimate:

 ell_c(z)>=(1-nu M_z)A,
 ||Q_c z||=||Q_b z+(Pi_b-Pi_c)z||<=(vartheta+nu M_z)A.          (16)

For a full D within epsilon_op of P_c(B), the normalized new amplitude
x=exp(-lambda_c B)ell_c(Dz)>=(1-nu M_z-M_l epsilon_op M_z)A
>=(1-rho)A>A/2, since lambda_c>0. Its normalized residual y satisfies

 y=exp(-lambda_c B)||Q_c Dz||
 <=[q_B(vartheta+nu M_z)+M_Q epsilon_op M_z]A<=vartheta A/2.    (17)

The last coefficient inequality is the unchanged MovingCone.residual_budget
with theta=vartheta,q=q_B,d=nu M_z,e=M_Q epsilon_op M_z. Every guard is
given in(14)-(15), including d>=0. MovingCone.cone_conversion, with a=A,
x as above,y as in(17),rho<1/2, gives x>0,y<=vartheta x. Thus Dz belongs
to the new cone, with actual amplitude at least exp(lambda_c B)(1-rho)A.
The old residual was not incorrectly assumed in the new kernel.

For terminal 0<=u<=B, rebase once more to c=sigma_N. Equation(16) gives
ell_c(z)>=3A/4,||Q_c z||<=2vartheta A. The eigenmode and normalized
complementary estimate yield

 exp(-lambda_c u)O_phi(P_c(u)z)/A>=3j_*/4-2H C_gap vartheta.

The perturbation changes this by at most H_obs epsilon_op M_z. Apply the
unchanged MovingCone.terminal_margin with j=j_*,K=H_obs C_gap,
e=H_obs epsilon_op M_z and y=exp(-lambda_c u)O_phi(D_N(u)z)/A;
its 16K vartheta<=j and e<=j/8 guards follow from the choices. It gives
O_phi(D_N(u)z)>=(j_*/2)exp(lambda_c u)A>0. Induct(17) after entrance:

 O_phi(D_N(u)D_(N-1)(B)...D_0(B)e0)
 >=c_*(1-rho)^(N-1)
       exp(B sum_(m<N)lambda_(sigma_m)+u lambda_(sigma_N)),
                   c_*=a_*j_*/4>0.                           (18)

For N=1 the induction is empty; u=0 is included. This proves A1 on the
EXACT new F,e0,O_phi. It is a positive observable statement, not just norm
growth, and it does not multiply scalar solution-value moments.

## 7. Induced common sources and the actual raw restart identity

Fix delta,B,N throughout this section and put L=1/delta,
L_ext=(N+1)B>=L. On this GLOBAL fast horizon let
A_glob(t)=g_delta A_R(W_fast)(t). Its constants may depend on this finite
L_ext; no uniform-in-delta estimate for A_glob is needed.

We derive source compatibility, rather than assert that a retaining
extension automatically commutes with time scaling. Take one accepted
retaining SLOW heat/Laplace source Y_(epsilon,eta) on an extension retaining
the given W. For a fast test f set Y_fast(f)=Y_(epsilon,eta)(T_(delta,0)f),
and Y_m(f)=Y_(epsilon,eta)(T_(delta,m)f). For each of these actual coupled
fields, isometry(2) and the accepted slow-field contractions give

 Var(Y_m(f)), Var((Y_m-W_(delta,m))(f))<=||f||H²,
             Var((Y_m-W_(delta,m))(f))->0                     (19)

for each smooth compact f as epsilon,eta->0. The same holds globally for
Y_fast,W_fast. Testwise convergence is on the ACTUAL transformed smooth
slow test, with delta,m fixed. Joint Gaussianity is retained. Generic
Gaussian transfer from source-operator-convergence.md Theorem1 therefore
gives actual Lp Ctheta first-driver convergence on [0,L_ext] and [0,B]
respectively, including the bounded F extension and all constant columns.

The source pointfields are
Y_fast(u,x)=delta^(a/2)Y_(epsilon,eta)(delta u,x),
Y_m(u,x)=Y_fast(mB+u,x). Their covariance is the canonical heat law and
K_(eta/delta) in the fast clock, since delta^a K_eta(delta r)=K_(eta/delta)(r).
The shared-width maximum and spatial heat-width sum laws are preserved.
They are continuous in time/spatially smooth on compact sets. Their actual
ordinary first responses equal the Gaussian-transfer drivers: both have
matrix entries Y_m(h_R), using time-indicator approximation as in Section3,
then the same finite-propagation constant-column extension. This argument
uses actual point-test integrals and(19), not a new source CM basis or
mere equality of source laws.

For these ordinary source primitives, changing the integration variable
from mB+r to r and composing free groups gives the exact identity on F

 S_F(mB)[A_glob^source(mB+u)-A_glob^source(mB)]S_F(-mB)
                                      =X_m^source(u).         (20)

No mask is commuted through a wave group. Pass the actual Lp Ctheta limits
from(19) through the bounded restriction/difference/conjugation maps at
this FIXED delta,N. For the finitely many m the resulting raw identity is

 S_F(mB)[A_glob(mB+u)-A_glob(mB)]S_F(-mB)=X_m(u).              (21)

A simultaneous path set in u is obtained by a convergent subsequence or
rational times plus path continuity; no common null set for all real delta
or all source parameters is required. Conjugation norms can be large as
delta decreases, but are finite here before the source limit.

Conjugate the global Young interaction evolution on [mB,mB+u] by S_F(mB).
Equation(21) and bounded linearity of Young Riemann sums show that it
solves the local Young equation driven by X_m, initially I. Uniqueness
identifies it with U_(X_m). Thus the GLOBAL physical raw flow satisfies

             P_glob(mB+u,mB)=S_F(u)U_(X_m)(u,0)=D_m^0(u).    (22)

Composition gives the actual full-phase product at time L, with the last
remainder tau. The deterministic primitive for V_(delta t) has the same
ordinary cocycle with local H_m, so the identical argument applies to
X_m+H_m and the actual compact-base shifted flow D_m^+.

For clarity, these products are also actual source limits in L2 at fixed
delta,N. Parent source/Young convergence gives local factor differences
tending to0 in every finite Lp, with all factor moments uniformly bounded
in the source cutoffs. For the finite list of N+1 factors (full B or final
tau), let C>=1 be their maximum source/raw norm and let e_src>=0 be the
maximum factor difference. If d(n) is the norm difference of the first
n ordered products, prefix norms are <=C^n and
d(n+1)<=C d(n)+C^n e_src, d(0)=0. Extend BOTH factor sequences by identities
past their finite ends; the same recurrence holds for all natural n.
ActualEvent.finite_error_accumulation then gives

                   d(N+1)<=(N+1)C^(N+1)e_src.                (23)

By Holder its L2 norm tends to0: the L^(4(N+1)) moment of C is uniformly
finite at fixed delta,N, while ||e_src||L4->0. This explicit recurrence is optional: global driver convergence and the
accepted source/Young interface also give the same L2 premise directly.
It is ONLY a fixed-delta source-product estimate, not closeness of a whole growing stochastic
product to its deterministic product as delta->0. Source shifted products
may use the FIXED raw mean V plus regularized noise; no finite-source
Cameron translation with the wrong regularized mean is assumed. Only the
noise-only canonical average will be compared with the full point solution.

## 8. Actual squared average, Gaussian cost and point comparison

On ALL B_delta define

 j_delta(x)=|O_phi D_(x_N)(tau)D_(x_(N-1))(B)...D_(x_0)(B)e0|².

The everywhere-defined Young map is continuous into finite-time operators,
each free S_F at a fixed time is bounded, finite products are continuous,
and O_phi is bounded. Hence j_delta is continuous/nonnegative on ALL
the input space, not just a subset of compatible noise trajectories.
Let U_delta be that signed noise-only product average and Y_delta the
same signed product with X_m+H_m. From(8),

 E U_delta²=E[exp(-Z/sqrt(delta)-v/(2delta))Y_delta²].          (24)

All unweighted moments needed at this fixed delta are finite: finite
products of the block flows have moments by Holder and the Gaussian/Young
bounds. The identity also follows for nonnegative j without prior
integrability. Neither it nor its use restricts a signed first moment.

We justify comparison at amplitude g_delta rather than borrow a g=1 formula
without checking it. Put Gamma_delta=g_delta² Gamma and given fast noise
W'=g_delta W_fast. For each fixed positive delta it is a NONZERO member
of the SAME admissible covariance class, with degree alpha and temporal a
unchanged. Its actual first driver is g_delta times the old one: literal
matrix forms are linear in the noise, and basis-independent bounded
extension including the two true constant columns gives equality on F.
Equivalently specialize the accepted Gaussian transfer to g_delta W_fast.
The canonical nth source chain is multiplied by g_delta^n, so this is
precisely the noise-only model at the stated amplitude, not a new solution.

By(22)-(23) and the accepted source/PDE identity, U_delta is the L2 limit
of the tested actual masked ordinary-source solution with noise W' at
FAST time L. Apply UNIT-amplitude F3 of fixed-mask-moment-transfer.md to
Gamma_delta and this actual source limit. Its sources can be g_delta Y_fast;
they have the correct heat/Laplace law, contraction and raw test limit.
Consequently

                    E U_delta²<=E|u_(Gamma_delta)(L,0)|².     (25)

Recognizing Gamma_delta here does NOT change the original SLOW Psi,Z,v
used in(5)-(8),(24). It only describes the SAME noise-only fast law.
In particular the Gaussian cost in(24) is never replaced by g_delta²v.

The ordinary source change from fast u to slow t=delta u, with phase
(V,delta V_t), identifies the unmasked fast law with the canonical solution
of delta² V_tt=Delta V+sqrt(delta) W V at slow time1. Indeed
g_delta Y_fast(u)=sqrt(delta)Y_(epsilon,eta)(delta u), and the fast source
cutoff is eta/delta. The accepted canonical-series construction passes
this identity at fixed delta to raw second moments, preserving all mixed
orders/self-pairings. No full-solution pathwise uniqueness is assumed.
Thus(25) is E U_delta²<=E|V_delta(1,0)|². Finally the exact accepted
calibration, for delta=T^(-kappa) and spatial r_T=T delta, gives

 E U_delta²<=E|u(T,0)|²,
 T^(-kappa)log E|u(T,0)|²=delta log E|V_delta(1,0)|².          (26)

r_T is not the fixed mask R. A fixed R does not contain the growing
backward cone; we have used a MOMENT INEQUALITY, not equality of masked
and full fields. Phi has mass1, so no spatial-volume loss appears. Source
limits were taken at fixed delta before this large-time comparison.

## 9. Positive event, terminal remainder and original raw lower rate

Fix e_rate>0. Choose rho in(0,1/2) with log(1-rho)>-e_rate/3, then the
actual cone parameters of Section6, including fixed B. For small delta,
adjacent indices s_m=m delta B lie in I with gaps<=omega. Let

 C_delta={Eop_delta<=epsilon_op},
 E_delta=C_delta intersect {|Z|<=delta^(-1/4)}.

Equation(13) gives P(C_delta)->1. Chebyshev gives
P{|Z|>delta^(-1/4)}<=v delta^(1/2)->0. Hence P(E_delta)->1 by a union
bound, not independence from Z or between blocks. Events are measurable
by the countable-state/rational-time argument in Section5, and are on
the same raw W space as the Gaussian identity.

On E_delta the ACTUAL shifted blocks meet the cone hypotheses, so(18)
with final u=tau gives a positive Y_delta and

 delta log Y_delta>=delta log c_*+delta(N-1)log(1-rho)
                  +delta B sum_(m<N)lambda_(s_m)+delta tau lambda_(s_N).

The last two terms are the left Riemann sum for I_R on the partition with
mesh<=delta B, including the final interval length delta tau. The actual
lambda is Lipschitz on I, so its error is at most C_R delta B. Also
0<=delta(N-1)<=1/B<=1, so the loss term is >=log(1-rho)>-e_rate/3.
For sufficiently small delta, both C_R delta B and delta|log c_*| are
<=e_rate/3. Thus, on E_delta,

                     Y_delta>=exp((I_R-e_rate)/delta).        (27)

N=1 needs no middle induction, and tau=0 is included in the cone theorem.
No signed norm-growth substitute is used for this observable lower bound.

The SQUARE integrand in(24) is nonnegative. Restrict it to E_delta; there
-Z/sqrt(delta)>=-delta^(-3/4). Therefore, writing p_delta=P(E_delta),

 E U_delta²>=p_delta
    exp((2I_R-2e_rate-v/2)/delta-delta^(-3/4)).                (28)

For small delta, p_delta>=1/2 and delta log p_delta->0. The unchanged
ActualEvent.moderate_penalty, with delta>0, verifies
delta*(delta^(-1/4)/sqrt(delta))=delta^(1/4)->0. Multiply logarithms in(28)
by delta and take lower limits at FIXED e_rate and its associated B:

 liminf_(delta->0)delta log E U_(delta,B)²>=2I_R-2e_rate-v/2.    (29)

Here U_(delta,B) makes the chosen block size explicit; (24)-(28) use this
same variable. By(26), the B-INDEPENDENT original point rate Q2 is at
least the right side of(29) for EACH fixed e_rate. Only NOW let e_rate
down0. Thus no limit involving a B-dependent variable is silently reused.
The bijection delta=T^(-kappa), kappa>0, covers all sufficiently large T.
This proves(1) for EACH
fixed original positive Psi and eligible finite R. A later supremum over
tests/masks follows per-test inequalities; no uniform mask or exchange
of source/time limits was used. By canonical spatial stationarity the
point0 can be replaced by any fixed original x: at every positive source
cutoff, translating all spatial vertices preserves the noise law, wave
kernels and constant initial data. The named fixed-order L2 limits and
absolute series limit preserve equality of these point second moments.
This is the stationarity assertion used here. This proves A1-A6.

## 10. Exact finite reuse and remaining original goal

The nine existing finite facts keep their COMPLETE public types and
previously reviewed source/axiom bytes, bound in lean-reuse-readiness-v0.json.
There is no new compiler or fact-count claim. Actual consumers here are:
- MovingCone.residual_budget, cone_conversion, terminal_margin: the exact
  substitutions/positive guards in Section6, on the new F norm parameters.
  These check scalar margins, not the infinite-dimensional cone hypotheses.
- JointTilt.shifted_amplitude: delta>0 in(6), using g_delta and the actual
  covariance factor delta^(a/2), not a standard-normalized fBm primitive.
- JointTilt.tilt_exponent: finite Gaussian MGF sign/half-variance algebra
  underlying(7), with actual real variances/covariances. wrong_sign_error
  and wrong_cost_error remain diagnostic identities; they do not prove
  the Gaussian Borel law, which was established separately in Section4.
- ActualEvent.finite_error_accumulation: Section7's FIXED-delta source
  factors, C>=1,e_src>=0,d(0)=0 and the all-n identity extension. It is
  not used to claim a whole growing noisy product is close to a deterministic
  one in norm; cone growth, not that false comparison, handled delta->0.
- ActualEvent.moderate_penalty: positive delta in(28)-(29), checking the
  normalized same-Z penalty only, not Chebyshev or Gaussian tilting.

All operator/source/Gaussian/Young/continuum/event claims are ANALYTIC,
not formalized by those scalar facts.71facts18seams/L0 unchanged; official
private companion still separately gated. Finite d1 raw-completion/MGF
controls are falsification aids, not a proof of these general claims.

Result(1) is a raw positive-test original-point lower functional in ALL
original admissible dimensions/covariances, retaining the full nonseparable
positive class. Variational unmasking/occupation optimization, all-alpha
scalar bridge, intended author-energy dictionary, sharp upper constant and
conditional exact limit remain OPEN. A formal p-scaling of a score does not
prove an actual p1 lower or equality with source L_*; no such claim is made.
No Skorohod/source repair/contacts/HPC/package/companion/TeX/PDF/wiki/
publication or whole-paper clearance. Original full goal remains ACTIVE.

Calibration scope: kappa tends to (4-alpha)/(3-alpha) as a tends to0,
the required time-independent scale (canonical notes, R:full-upper-boundary).
No optimized static constant is asserted. The separate Jensen inequality
E u²>=(E u)² and its rate implication are proved in the canonical notes,
P:Jensen, with numerical L_* specialization explicitly conditional on its
intended first-mean premise. See calibration-context-v1.txt for the exact
unchanged excerpt. A particular unoptimized test score need not exceed an
independently valid Jensen rate; both lower bounds may be combined by their
maximum. No p1 theorem is replaced, and no equality with the distinct
Skorohod model is inferred. Sharp-constant calibrations remain obligations
for later promotion.
