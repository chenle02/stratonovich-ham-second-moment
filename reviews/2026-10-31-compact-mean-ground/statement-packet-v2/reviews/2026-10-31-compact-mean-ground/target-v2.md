# Compact potential families: the full positive-tilt ground-phase target

FROZEN REVISED STATEMENT ONLY, not an adopted proof. Scalar target v1 passed
its statement gate (12HIGH218.396s) but is not sufficient for the existing
GENERAL positive tilt class. No long scalar proof was started. This version
retains that class rather than developing only separable profiles. All
source/model/sharp-goal boundaries of the project remain in force.

## F1. Exact deterministic family

Let d=1,2,3, I=[0,1], K_x one compact set, and sigma->V_sigma a continuous
map I->C_c^infinity(K_x), real and nonnegative. REQUIRE a common real
unit-L2 w in H1 and epsilon>0 with

 int|grad w|²-int V_sigma w²<=-epsilon for EVERY sigma in I.

The parameter sigma is an INDEX, not the physical propagation time t or
a noise coupling. Set M=sup_sigma||V_sigma||infinity<infinity and
H_sigma=-Delta-V_sigma on H2. Use EXACT accepted F=E directsum R²,
E=H1/2 x H-1/2, i:E->F, from fixed-mask-young-constant-phase.md,
scientific8ad5094/adoption5969da5. P_sigma(t) is its ACTUAL deterministic
physical wave with frozen coefficient V_sigma; P_sigma^E its E restriction.
The later genuinely time-varying/random flow is a separate consumer.

## F2. Ground, gap and actual global-E complementary wave

H_sigma is self-adjoint/bounded below, essential spectrum[0,infinity),
C_c^infinity a core. Its bottom E1(sigma)<=-epsilon is isolated/simple,
with unique normalized positive-a.e. real ground p_sigma. Let E2 be the
second max-min level, using threshold0 when no second negative eigenvalue.
Then -M<=E1<E2<=0, and for j=1,2,

 |Ej(sigma)-Ej(tau)|<=||V_sigma-V_tau||infinity.

The maps p_sigma into L2 AND H2 are continuous. Put lambda_sigma=sqrt(-E1),
mu_sigma=sqrt(-E2)>=0. Uniformly sqrt(epsilon)<=lambda_sigma<=sqrt(M),
Delta=inf_I(E2-E1)>0 and d0=inf_I(lambda-mu)>0. No second bound state,
positive mu, p_sigma in L1 or spatial tail estimate is assumed.

On E set e_sigma^E=(p_sigma,lambda_sigma p_sigma),
ell_sigma^E(v,z)=(<p_sigma,v>+<p_sigma,z>/lambda_sigma)/2,
Pi_sigma^E=e_sigma^E ell_sigma^E. Uniformly sigma,t>=0,

 ||P_sigma^E(t)(I-Pi_sigma^E)||B(E)<=C(1+t)exp(mu_sigma t).

This is the ACTUAL physical wave and fractional Sobolev phase, not just an
L2 estimate. Remove only the GROWING ground branch; retain its decaying
partner and handle spectral threshold0. Old d1 spectral-complement-transfer
Sections2-3 is a METHOD comparator, not an all-dimensional theorem input.

Named imported sources: Teschl2014 SECOND edition10.2,p258 (real compact
V=-V_sigma),10.13,p273 CONDITIONAL on an existing ground eigenvalue, and
4.12/4.13,pp140-141 (common quadratic-form domain H1/max-min). Existence
from the trial, continuity, uniformity and physical/fractional applications
are deductions to prove, not claimed verbatim source conclusions.

## F3. Exact full-F projection and complementary bound

For c=(c1,c2), C(t)c=(c1+t c2,c2), D_sigma c=(0,V_sigma c1) in E,

 P_sigma(t)(e,c)=(P_sigma^E(t)e+int_0^t P_sigma^E(t-r)D_sigma C(r)c dr,C(t)c).

Define f_sigma=int V_sigma p_sigma/(2lambda_sigma)>0 and

 ell_sigma(e,c)=ell_sigma^E(e)+f_sigma(c1/lambda_sigma+c2/lambda_sigma²),
 e_sigma=i e_sigma^E, Pi_sigma=e_sigma ell_sigma, Q_sigma=I-Pi_sigma.

Then ell_sigma(e_sigma)=1; Pi_sigma is a bounded rank-one projection;
P_sigma(t)e_sigma=exp(lambda_sigma t)e_sigma and
ell_sigma P_sigma(t)=exp(lambda_sigma t)ell_sigma. Thus
P_sigma(t)Pi_sigma=Pi_sigma P_sigma(t)=exp(lambda_sigma t)Pi_sigma.
e_sigma,ell_sigma,Pi_sigma are norm-continuous/bounded in F,F*,B(F).
For e0=(0,1,0), inf_I ell_sigma(e0)>0. Every fixed smooth compact real
phi>=0, integral1, has bounded O_phi(e,c)=<e1,phi>+c1 and
inf_I O_phi(e_sigma)>0. Positivity is in integrals; no d1 ODE is used.

Uniformly sigma,t>=0,

 ||P_sigma(t)Q_sigma||B(F)<=C(1+t)^3 exp(mu_sigma t),
 ||exp(-lambda_sigma t)P_sigma(t)Q_sigma||B(F)<=C_eta exp(-eta t)

for any fixed 0<eta<d0. Retain and subtract the constant-forcing growing
response explicitly; no p in L1 is required for f_sigma. Also for fixed T0,

 sup_(0<=t<=T0)||P_sigma(t)-P_tau(t)||B(F)
  <=C_T0 (||V_sigma-V_tau||infinity+||V_sigma-V_tau||2).

This yields uniform parameter continuity; it is NOT time-norm continuity
of the free wave group. All statements need proof. The scalar bU case is
included by V_sigma=b(sigma)U, but does not replace this family target.

## F4. FULL original positive raw tilt, fixed profile and cost

Let Gamma be NONZERO original H:homog, d1/2/3, a in(0,1),
0<alpha<d or alpha=d=1, alpha+a<2. Fix ANY nonnegative nonzero real
Psi in C_c^infinity((0,1)xR^d), not assumed a product of time/space tests.
Its ORIGINAL raw Gaussian variable is Z=W(Psi), variance v_Psi. Define

 h_sigma(x)=int_0^1 |sigma-u|^-a (Gamma*Psi(u,.))(x)du,
 q_avg(x)=int_0^1 Psi(u,x)du, supp q_avg contained in B_A.

Then q_avg is nonzero nonnegative smooth compact. Its raw spatial score
Q(q_avg)=int Gamma(dz)int q_avg(x)q_avg(x-z)dx is finite/positive,
0<Q(q_avg)<=v_Psi<infinity, and h_sigma>=Gamma*q_avg for ALL sigma in I.
The mean formula is the linear covariance/CM mean of the GIVEN raw W
test Psi; it is not Psi(sigma,.) or a redefined product profile.

Choose the actual real even [0,1] physical mask m_R,1 on B_R, supported
in B_(2R), and set V_sigma=m_R h_sigma AFTER both convolutions. For each
fixed sufficiently large R it is a continuous (indeed smooth) I-family in
C_c^infinity(B_(2R)), nonnegative and nonzero. This actual family and
its lambda_sigma are Lipschitz in sigma; this is not asserted for arbitrary
merely continuous families without the actual smooth-test construction. For sufficiently large but
FINITE R it satisfies the COMMON negative-trial hypothesis of F1, with
Psi, q_avg, Z and v_Psi UNCHANGED.

Proposed explicit common trial: unit compact smooth psi supported in B2,
psi>=c0>0 on B1; w=psi_L=L^(-d/2)psi(x/L), L>=max(1,2A),R>=max(A,2L).
Positive Tonelli and homogeneous ball masses should give, for EVERY sigma,

 int V_sigma psi_L² >= C_G L^(-alpha),
 C_G=c0²2^(alpha-d)Gamma(B1)int q_avg>0,
 energy <=Dpsi L^(-2)-C_G L^(-alpha)<0 for large L, since alpha<2.

Verify Gamma(B1)>0 from any charged ball and homogeneity, all singular/
invariant-direction cases and the white endpoint. Only trial/mask widen,
never the original Psi. The cutoff may be chosen to cover any additional
fixed compact variational test supports, preserving int V_sigma g_sigma²
=int h_sigma g_sigma² there. This is not all-strength binding for a single
fixed compact potential or optimization of a masked Gaussian covariance.
R is fixed before source/time asymptotics. No nonlinear shifted-flow or
Girsanov/event identity follows merely from this linear mean construction.

## Boundaries

F1-F4 would supply deterministic indexed-family cone inputs for the ENTIRE
existing positive tilt class, not only products. Random block errors,
growing products, actual same-Z event/cost and all-alpha variational lower
remain further gates. Sharp upper/source normalization/exact limit remain
open. No scalar moment multiplication, arbitrary-phase covariance ordering,
new Lean/package/companion/HPC/contact/Skorohod/source fix/TeX/PDF/wiki/
publication or independent novelty claim. Full original goal ACTIVE.
