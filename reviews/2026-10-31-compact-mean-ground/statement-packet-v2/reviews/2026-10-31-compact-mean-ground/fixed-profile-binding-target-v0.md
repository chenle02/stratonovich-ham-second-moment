# Fixed original q, larger mask: proposed common-trial subtarget

UNREVIEWED STATEMENT/FEASIBILITY TARGET, not an adopted proof. Freeze this
with the ground/projection/complement theorem and obtain the independent
statement gate before long proof. It strengthens the earlier preparatory
example by keeping the Gaussian spatial tilt q FIXED.

Original nonzero H:homog Gamma, d1/2/3, alpha+a<2, so alpha<2. Fix real
normalized g in C_c^infinity, q=g², supp q contained in B_A, and b0>0.
Choose a normalized real compact smooth psi supported in B2 with
psi>=c0>0 on B1. Let Dpsi=int|grad psi|² and psi_L=L^(-d/2)psi(x/L).
Choose L>=max(1,2A) and R>=max(A,2L), with the actual even [0,1] mask
m=zeta_R,1 on B_R. Set U_R=m(Gamma*q). q and the raw CM cost NEVER change.

Proposed exact common-trial bound:

 int U_R psi_L² >= C_G L^(-alpha),
 C_G=c0² * 2^(alpha-d) * Gamma(B1) * int q >0,
 <psi_L,(-Delta-bU_R)psi_L>
       <=Dpsi L^(-2)-b0 C_G L^(-alpha) <0, all b>=b0,

once L is chosen sufficiently large. The mechanism to check is positive
Tonelli plus B_(L/2) contained in B_L-y for y in supp q and homogeneous
ball mass Gamma(B_(L/2))=(L/2)^(d-alpha)Gamma(B1). Compactness/smoothness/
nonzero U_R and Gamma(B1)>0 also need explicit derivation; do not assume
radial angular density or global decay of Gamma*q. This is compatible with
singular invariant-direction covariances and the d1 white endpoint.

The chosen R is finite and fixed before time/source asymptotics. Also
int U_R g²=int(Gamma*q)g², since m=1 on supp g, so the original variational
Rayleigh score is unchanged. Enlarging the cutoff does not replace the raw
Gaussian covariance/cost. This does NOT assert every FIXED compact U binds
at every positive strength. It asserts existence of an adequate finite mask
for each fixed ORIGINAL q and positive lower strength b0.

New check-fixed-profile-trial.py tests an actual original singular d3 model
with q and b=.1 FIXED at all six scales. Only the normalized trial width
and mask grow. A nonnegative trial energy becomes negative at large scales;
35/60-working-digit consistency, no rigorous quadrature/eigenvalue bound.
The previous check-actual-trial.py rescaled q itself and was only a basic
example, not evidence for this stronger fixed-q quantifier. Both retained.

If accepted and proved, this common trial may let the compact-ground family
use any fixed near-optimal q without changing its raw cost. The actual
source-time tilt, Gaussian event/cost, all-alpha variational lower constant,
sharp upper and intended source-energy map still need their own gates.
