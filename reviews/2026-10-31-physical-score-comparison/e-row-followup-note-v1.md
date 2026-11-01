# Post-fit spatial E-row calibration

This NEW check was run AFTER the fit review and the initial author proof
draft. It is not retroactively part of the pre-proof screen or native
reviewer's read coverage. The old V1 script/data were not rerun or changed.

The reviewer correctly observed that V1's two compared spatial quantities
shared one computed factor. The followup explicitly forms a deterministic
periodic spectral E row. For d1 white Gamma=3delta_0 and control
h_0 tensor exp(-x²), it constructs the mean potential
V=3*time_pair*m_R*exp(-x²) ONCE, Lz=(0,Vf), z=(f,0), w=(0,Lambda f),
Lambda(k)=sqrt(1+k²), and the Hminus-half metric multiplier Lambda^-1.
The result is compared to a SEPARATELY integrated multiprecision raw
covariance pairing on the compact trial support. Unequal cells2/5,3/5
and the transition-region bump exercise the same ell and physical mask.

512/1024/2048-node grids on[-4,4] have residuals about1.067e-9,
3.586e-13 and2.558e-17 against that raw pairing. The actual E row is
about0.491263078927454. Holding it fixed, wrong raw full-amplitude,
omitted cell division and double-mask formulas differ by about0.983,
0.197 and0.0846. A wrong E metric without Lambda^-1 differs by about1.087.
Both implementations still share model parameters; this is a deterministic
calibration with one-sided contrasts, not an empirical covariance
measurement or a proof of the source normalization.

FFT arithmetic is float64; raw quadrature uses70working digits. No
computer-certified error bound, continuum operator convergence, solution
simulation, Gaussian process construction, global optimization or statistical
confidence follows. The analytic row and all-dimensional application in
the new proof carry PB1. Full per-grid outputs and library versions are
retained; source SHA is bound. Exit0.

FULL review clarification: the Lambda factors cancel exactly in the correct
discrete row. Ortho Parseval therefore reduces it to a periodic trapezoid
sum of V*f², compared with the separately implemented adaptive quadrature.
The wrong-metric contrast is the check that exercises the metric choice.
The2048-node residual is at the float64 roundoff floor, not evidence of
that many digits of integration accuracy. Neither observation changes the
raw outputs or supplies a continuum operator certificate.
