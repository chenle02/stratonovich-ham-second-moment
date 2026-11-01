# SP current calibration scope

Use the corrected physical-coordinate symplectic-controls-v2.json, not
v1 as physical calibration. Four exact rational Hamiltonian/Cayley products
preserve the canonical skew matrix and have determinant1. Each exact
physical-generator/Bessel similarity is checked. Three false variants
(velocity removal,nonsymmetric force,identical phase weights) have nonzero
rational defects. Approximate60digit operator norms are diagnostics only.
V1 mismatch/evaluator repair retained; no new run of unchanged v2 tests.

SP4 new block-direction-controls-v1.json covers three exact rational delta/a
pairs times three slow controls. Fast Gaussian-coordinate pullback T has
orthonormal columns, its adjoint is a contraction, and the unseen residual
is orthogonal. Six nonzero cases detect missing delta^(-a/2) direction
factor and wrong sqrt(delta) in the unscaled covariance. Three orthogonal
zero-signal cases cannot detect those factors and are labeled accordingly.
These finite Gaussian coordinates are NOT an approximation or proof of
the actual time-fractional raw covariance/isometry/source/phase operator.

No new numerical enclosure, stochastic simulation or finite Lean theorem.
All analytic source/conservation/application and reviewer gates pending.
