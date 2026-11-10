# Compact mean potential: ground family and full-phase complement

FROZEN STATEMENT TARGET ONLY; no new analytic proof adopted. The original
all-dimensional sharp p2 goal remains ACTIVE. This supplies deterministic
inputs for a later actual growing-block Gaussian event, not that event.

Let d=1,2,3 and U be fixed nonzero nonnegative real C_c^infinity(R^d).
Fix 0<b0<=b1<infinity, K=[b0,b1]. REQUIRE a real unit L2 trial w in H1 and
epsilon>0 with int|grad w|²-b0 int U w²<=-epsilon. This common negative
trial is a hypothesis of G1-G4; G5 supplies it for actual original profiles
without changing their Gaussian tilt. No automatic all-strength binding
of every FIXED compact d3 potential is asserted.

Use E=H^(1/2)xH^(-1/2) and EXACT accepted F=E directsum R², embedded as
e+(c1,c2), from notes/fixed-mask-young-constant-phase.md, scientific8ad5094/
adoption5969da5. Let P_b(t) be its ACTUAL deterministic physical wave flow
with potential bU and free massless wave generator. P_b^E(t) is its restriction
to E. All phases/functions real, with complex spectral theory restricted
to real invariant subspaces. Write H_b=-Delta-bU on L2, domain H2.

## G1. Common ground, uniform gap and parameter continuity

H_b is self-adjoint, bounded below and has essential spectrum[0,infinity),
with C_c^infinity a core. Its bottom E1(b)<0 is isolated/simple and has the
unique positive-a.e. normalized real eigenfunction p_b. Define E2(b) by
the second max-min level, using threshold0 if there is no second negative
eigenvalue. Then

 -b1||U||infinity<=E1(b)<=-epsilon,
 E1(b)<E2(b)<=0, |Ej(b)-Ej(c)|<=||U||infinity|b-c|, j=1,2.

The ground-state choice b->p_b is continuous in L2 AND H2. The energy gap
Delta=inf_K(E2-E1)>0. Set lambda_b=sqrt(-E1(b)), mu_b=sqrt(-E2(b))>=0.
There are l,L,d0>0 with l<=lambda_b<=L and lambda_b-mu_b>=d0 uniformly.
No second bound state or nonzero mu_b is presumed. No p_b in L1 or uniform
spatial tail estimate is assumed or needed for this target's functional.

Exact proposed imported inputs are Teschl2014 SECOND edition Theorem10.2
p258, Theorem10.13 p273 CONDITIONAL on an existing ground eigenvalue, and
Theorem4.12 pp140-141 including its quadratic-form-domain formulation.
All uniformity, existence from the trial, continuity and parameter bounds
remain deductions to prove, not verbatim imported source theorems.

## G2. Global Sobolev complementary physical wave

On E put e_b^E=(p_b,lambda_b p_b) and

 ell_b^E(v,z)=(<p_b,v>+<p_b,z>/lambda_b)/2,
 Pi_b^E=e_b^E ell_b^E, Q_b^E=I-Pi_b^E.

Pairings are the L2-extended Sobolev dualities, not point traces. Uniformly
over b in K and t>=0,

 ||P_b^E(t)Q_b^E||B(E)<=C(1+t)exp(mu_b t).                    (G2)

This removes only the GROWING ground phase, retaining its decaying partner.
It is not just projection off p_b on both L2 entries. Re-prove at R^d the
fractional graph comparison for H_b+c versus1-Delta and spectral wave
calculus, including spectral parameter0. The accepted old
spectral-complement-transfer.md Sections2-3 is d1 prior METHOD, not already
an all-dimensional theorem. Identify the spectral flow with the actual
physical Duhamel flow, rather than use an unrelated spectral process.

## G3. Full-F growing projection, entrance and tested positivity

Write i:E->F, e_b=i e_b^E. For c=(c1,c2) set C(t)c=(c1+t c2,c2) and
D_b c=(0,bU c1) in E. The exact full physical flow has block form

 P_b(t)(e,c)=(P_b^E(t)e+K_b(t)c,C(t)c),
 K_b(t)c=int_0^t P_b^E(t-r)D_b C(r)c dr.

Define the POSITIVE scalar f_b=b int U p_b/(2lambda_b) and the full
continuous functional

 ell_b(e,c)=ell_b^E(e)+f_b(c1/lambda_b+c2/lambda_b²),
 Pi_b=e_b ell_b, Q_b=I-Pi_b.

Then ell_b(e_b)=1, Pi_b is a bounded rank-one projection, and

 P_b(t)e_b=exp(lambda_b t)e_b,
 ell_b P_b(t)=exp(lambda_b t)ell_b,
 P_b(t)Pi_b=Pi_b P_b(t)=exp(lambda_b t)Pi_b.

The maps b->e_b,ell_b,Pi_b are continuous in F,F*,B(F) and uniformly
bounded on K. The original data e0=(0,1,0) has uniform positive entrance
inf_K ell_b(e0)>0. For any fixed phi>=0 real C_c^infinity, integral1,
O_phi(e,c)=<e1,phi>+c1 is bounded on F and inf_K O_phi(e_b)>0.
Strict positivity is used in integrals, not asserted via a d1 ODE in d3.

The constant part of ell_b is ESSENTIAL: it is defined through compact
forcing U and p_b in L2, so no integration of a ground state against a
non-Sobolev constant or hidden p_b in L1 is needed. Dropping this part
is rejected by the finite wave/constant controls, not accepted as a method.

## G4. Full-F complementary estimate

For all t>=0, uniformly b in K,

 ||P_b(t)Q_b||B(F)<=C(1+t)^3 exp(mu_b t),
 ||exp(-lambda_b t)P_b(t)Q_b||B(F)<=C_eta exp(-eta t)          (G4)

for some eta>0, e.g. any eta<inf_K(lambda_b-mu_b). Retain both the
constant forcing and the subtracted growing ground response in deriving
the block remainder. Ground-state norm growth alone is insufficient.
Also for each finite T0,

 sup_(0<=t<=T0)||P_b(t)-P_c(t)||B(F)<=C_T0|b-c|.

This is parameter continuity, not operator-norm time continuity of the
free wave group. G1-G4 together would meet the exact deterministic inputs
of the existing abstract moving-block cone, but do not themselves establish
random operator error bounds, products on growing horizons or raw event cost.

## G5. Actual original covariance profile and a fixed-q common trial

Let Gamma be any NONZERO original H:homog covariance, a in(0,1),
alpha+a<2, with 0<alpha<d or alpha=d=1. Fix real
unit g in C_c^infinity and q=g², supp q contained in B_A. The original raw
spatial score

 Q(g)=int Gamma(dz) int q(x)q(x-z)dx

is finite/strictly positive. For the actual even[0,1] physical mask m_R=1
on B_R, U_R=m_R(Gamma*q) is nonnegative smooth compact and nonzero once R
covers supp g. Also int U_R g²=Q(g); mask acts AFTER convolution.

For ANY prescribed b0>0 the SAME fixed q admits a sufficiently large but
finite R and a normalized real compact trial w giving the common negative
trial hypothesis for U_R. A proposed explicit route: fix unit real psi
supported in B2 with psi>=c0>0 on B1, let w=psi_L=L^(-d/2)psi(x/L),
L>=max(1,2A), R>=max(A,2L). Then

 int U_R psi_L² >= C_G L^(-alpha),
 C_G=c0² 2^(alpha-d)Gamma(B1) int q >0,
 int|grad psi_L|²-b0 int U_R psi_L²
      <=Dpsi L^(-2)-b0 C_G L^(-alpha)<0

for large L because alpha<2. Verify Gamma(B1)>0, smoothness and all
finite/positive Tonelli/scaling steps, including singular/invariant-direction
covariances and the d1 white endpoint. q and its ORIGINAL raw Gaussian
cost do not change. Only the mask and the auxiliary existence trial widen;
R is fixed before time/source asymptotics. No assertion that every fixed
compact potential binds at every strength, or change of optimizing q to
force a gap. This does not compute or replace the full raw CM cost.

## Boundaries

No probability/event/shifted canonical identity, lower asymptotic rate or
sharp upper/source-energy constant follows until later gates. No scalar
solution moment multiplication or arbitrary-phase covariance ordering.
Original full goal retained; no new Lean fact/package/companion/HPC/contact/
Skorohod/source correction/TeX/PDF/wiki/publication or novelty claim.
