# Residual norm pre-proof scalar controls and scope

Existing check-rank-one-v0.py was executed previously:18actual Gaussian
norm integrals Y=sqrt(delta)epsilon|G|,eta1,nu1/1.5/1.8,epsilon.5/1,
delta.1/.03/.01, at40/60workingdigits. The integrator subtracts the exact
saddle for stability and integrates0..infinity; nu1 is independently
checked against2exp(A²/(2delta))Phi(A/sqrt(delta)). Workingprecision
agreement is NOT a computer-certified quadrature/tail/roundoff bound or
all-parameter theorem. The nu1 row is a scalar calibration, not theta1
in the actual driver. No old integrator rerun after unchanged data.

New check-bound-v1.py evaluates the PROPOSED finite-delta sufficient bound
on all18preserved Gaussian rows. All satisfy it; its constant is deliberately
nonsharp and no optimality inferred. New3actual CLOSED-FORM Gaussian moments
Y=g_delta|G|,a.5,nu1 illustrate that mean->0 and ordinary uniform small
square-exponential integrability do NOT imply a finite normalized1/delta
logmoment from those hypotheses alone. This is a wrong-CM-scale counter,
not a failure of the actual averaged driver from C3.

Exact negative guards: at nu2 the Gaussian integral has exponent
(eta epsilon²-1/2)G² and diverges if eta epsilon²>=1/2, including equality.
At nu>2 any positive coefficient dominates the Gaussian quadratic at
infinity and diverges. Infinity is NOT sampled numerically. At nu1.5 the
rank-one exact saddle coefficient27/32 scales epsilon6; the false stronger
bound27epsilon7 fails at epsilon1/100 (exact rational fixture). This checks
the covariance-radius power, not the full operator theorem.

These are actual Gaussian norm/cost controls, not a point solution moment,
operator projection optimization or nonlinear flow computation. All C3
and transfer/moment/ambient/support/tail integration hypotheses still need
source/type/application proof and FULL independent review. No Frobenius/
HS/entry maximum substitutes for the Banach path norm. Original full
all-Gamma/point-upper/growing-cone/signed-control/source-constant gaps remain.
