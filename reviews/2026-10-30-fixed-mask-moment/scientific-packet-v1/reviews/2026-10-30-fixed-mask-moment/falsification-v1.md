# Falsification and investment decision

PRE-NAMED OBSTRUCTION: a physical mask need not decrease a Gaussian covariance
in PSD order; signed wave/phase factors can reverse a putative comparison.
The surviving proposed mechanism is restricted to displacement kernels,
data (1,0), nonnegative original Gamma, and positive source point covariance.

Actual model: d2, Gamma=delta_x1 tensor Leb_x2, alpha=1,a=.5. This is an
original admissible nonisotropic Radon covariance with invariant x2.
Source epsilon=.1,delta=.2. All spatial quadrature nodes have x1=0;
the Gaussian variables at the two x2 nodes coincide, consistently with the
actual heat/Laplace covariance. Four times .2,.4,.6,.8, horizon1, two spatial
nodes x2=0,.1, terminals0,.05; all evaluated G2 factors are strictly inside
their light cones. A smooth radial mask can have sampled values1,.5 at
these nodes. Every quadrature weight is positive.

PASS 100 mixed moments of chain orders0..4, total up to8. Forty-eight
odd-total rows vanish. Unequal orders/empty chains, including (0,2),(0,4),
and self-pairings within (2,2), are all retained by the full Wick recursion.
Even nonzero nontrivial rows strictly decrease. No Monte Carlo is used.
Fifty-digit working arithmetic / thirty printed digits are not certified
accuracy; no continuum discretization error estimate is supplied. These
controls test the exact finite pairing mechanism only.

NEGATIVE CONTROL: same-time point covariance before masking is c*ones(2,2).
After mask diag(1,.5), the difference has eigenvalues -c/4,c; so PSD order
is FALSE within the actual original model. Signed observable Z(x0)-Z(x1)
has raw variance0 and masked variance c/4>0. This is an actual field-linear
observable, not a claimed velocity solution counterexample. It excludes
arbitrary signed-kernel monotonicity and is consistent with F1/F2.

Object check: F3 controls the original stationary POINT second moment through
a positive spatial average of displacement, not through point Sobolev
evaluation or a velocity trace. It assumes, rather than proves, existence
of the limiting masked observable. No first-chaos-only growth claim or
time-block independence is needed. The old full-spatial-class static phase
variance tool remains distinct; its mean term cannot be discarded.

Decision: SURVIVES as a statement target, pending independent statement
review before long proof. No all-order continuum result is adopted.
