# S1-S4 pre-proof falsification

Statements only, not a theorem. Pre-named obstructions: assuming roughH2;
using a positive ground/gap theorem for signed potentials; zero spectral
bottom; missing polynomial time/potential factor; wrong fractional weights;
point sampling of an Lr mean instead of averaging; constants hidden in L2.

Executed check-spectral-v1.py locally via uv/mpmath:
60 scalar spectral-matrix rows, K2/8, h=-4,-.25,0,.25,4,64, t0,.25,1,4,16,
40/70digits with relative precision differences<1e-25. Actual evaluator
forms the FULL Euclidean2x2 induced norm, after exp(-lambda*t) normalization,
with shifted offdiagonal weights sqrt(h+c), reciprocal. Bound checked is
ONLY the spectral-FIBER envelope8(1+K)(1+t), not S2's full F operator.
Ten h0 rows match the independent exact Jordan norm formula; all t0 rows
are exactly1. Determinant identity residual retained. Tiny discriminant
negativity is clipped at0 for rounding; no rigorous interval/error enclosure.
No actual potential, CM field, continuum spectral operator or SPDE computed.

Four exact rational sqrt guards: epsilon1/n²,lambda1/n,n2,4,16,256 give
lambda/epsilon=n, consistent with failure of uniform Lipschitz at0. These
are scalar spectral tests, not compact mean eigenvalues. Twelve exact
rational form-budget rows check the shifted .5-to-3(1+K²) bounds in scalar
z=||u||H1 and exclude approximate minimizer z>K+2. They do not prove the
Fourier interpolation or infinite-dimensional form result.

Analytic guards, not coded quadrature: free constant-velocity input gives
||tau(t)||>=sqrt(1+t²), so no uniform C exp(lambda*t) at lambda0 with no
polynomial. Lr-equivalent representative1_Q is0 a.e. but all rational left
point samples are1; raw point sampling is not an a.e.-defined freezing map.
Bochner averages in S4 avoid this defect. Neither guard claims actual CM
realizability or refutes the original sharp moment objective.

Survival: proposed polynomial time factor, sqrt rate continuity, actual
rough domain/form and averaged-field interface survive these finite/simple
guards. Complete analytic proof and independent statement/full gates still
required. Existing original white uniformR fixed-projection obstruction
retained; no growing-mask upgrade or original point upper from this screen.
