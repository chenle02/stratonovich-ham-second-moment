# Falsification and normalization controls

Actual d2 singular covariance delta_x1 tensorLeb_x2 passes H:homog with
alpha1 and arbitrary a<1. Exact off-axis ball mass sqrt((r^2-y2^2)_+)/pi;
Gaussian spectral integral r/(2sqrtpi) exp(-y2^2/r^2). Nine center/radius
cases agree with the physical Gaussian transform and proposed ball bound.
Nine centered Riesz cases in d1/2/3 verify constants independently using
radial Gamma integrals and the explicit Fourier density (diagnostic only,
not a density assumption in target). Four Gaussian SCHWARTZ mask cases
R1/2/4/8 compare actual physical variance, spectral variance INCLUDING
(2pi)^d, and candidate auxiliary bound on f=exp(-|x|^2/2)(x2^2-1).
Gaussian mask is not compact: separate C-infinity compact plateau test
checks exact marginal-zero mechanism and integration by parts int chi chi''
=-int chi'^2 numerically at 60 digits. Positive JI^2 is recorded in JSON.
No claim numeric tests prove theorems; analytic proof must cover all centers,
all radii/scales, singular measures, Hilbert-valued convolution and completion.
No operator variance, Schatten trace, Young path or nonlinear moment tested.
Script ran locally to successful JSON; no new Lean check: these obligations
are analytic/distributional; do not create a trivial implementation-mirror
formal seam or imply old scalar/matrix Lean proofs verify these claims.
