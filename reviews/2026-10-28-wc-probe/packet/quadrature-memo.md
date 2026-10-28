# Exact-time reduction and floating endpoint diagnostics

Status: author-side derivation/diagnostics, pending independent review.
No new manuscript theorem, uniform upper bound, or moment result is claimed.
The numerical rows are not rigorous enclosures and do not replace the
positive-measure lower-bound argument in boundary-probe.md.

## Object and time reduction

Write I_alpha(Z,W) for the left side of(WC) at h=1. For a=|y|,
b=|Z-y| and a+b<1, define the time-integrated density

  K_Z(y) = integral_a^(1-b) du /
    [4 pi^2 sqrt((u^2-a^2)((1-u)^2-b^2))].

It is zero off the open ellipse a+b<1. Tonelli gives
I_alpha(Z,W)=integral K_Z(y)|W-y|^(-alpha)dy, with extended values allowed.
Put L=1-a-b and u=a+L sin(theta)^2. For a,b>0 this yields exactly

  K_Z(y) = (1/(2 pi^2)) integral_0^(pi/2)
    [(2a+L sin(theta)^2)(2b+L cos(theta)^2)]^(-1/2) dtheta.

To verify the elliptic form, put A=2a,C=2b, then t=tan(theta).
The integral becomes integral_0^infinity
[(A+(A+L)t^2)(C+L+Ct^2)]^(-1/2)dt.
Substitute t=sqrt(A/(A+L))*tan(psi). Thus

  K_Z(y) = K(m)/(2 pi^2 sqrt(D)),
  D=(1+a-b)(1-a+b),   m=1-4ab/D,
  K(m)=integral_0^(pi/2) [1-m sin(psi)^2]^(-1/2)dpsi.

The script uses scipy.special.ellipkm1(4ab/D), avoiding rounding m to1.
It independently checks this formula against the original theta integral at
four nonsingular points. Endpoints a=0 or b=0 have the extended logarithmic
value; quadrature nodes never evaluate them. Omitting these null points is
not a proof of integrability, which must be established analytically.

## Spatial quadrature at W=0

Set Z=(z,0),0<=z<1 and y=r(cos(phi),sin(phi)). The ellipse support is

  0<r<R(phi), R(phi)=(1-z^2)/(2(1-z cos(phi))).

The Riesz factor combines with polar area as r^(1-alpha)dr dphi. With
r=R(phi)v^p, p=4/(2-alpha), the radial measure is exactly
R(phi)^(2-alpha)*p*v^3 dv. Symmetry reduces phi to[0,pi] with factor2.
No clipping, deletion of large samples or stochastic sampling is used.

Two angular parameterizations are evaluated: ordinary phi=pi*v, and
phi=2 arctan(c tan(psi)), c=sqrt((1-z)/(1+z)),0<psi<pi/2,
with Jacobian2c/(cos(psi)^2+c^2 sin(psi)^2). Each is evaluated with
64,128,256 Gauss-Legendre nodes in each of the two spatial variables.

## Calibration and error boundary

The same evaluator at alpha=0 is compared with the unweighted identity

  integral_0^1 (G_u*G_(1-u))(Z)du = sqrt(1-|Z|^2)/(4pi), |Z|<1.

A transform check of this normalization: the spatial Fourier transform of
G_t is sin(t rho)/rho; its temporal self-convolution is
[sin(t rho)-t rho cos(t rho)]/(2rho^3), with the rho=0 limit t^3/6.
The Fourier transform of 1_(|Z|<t)sqrt(t^2-|Z|^2)/(4pi) is the same.
The latter follows by expanding J0 in the polar Fourier integral and
integrating each beta integral; absolute convergence on compact radii
permits termwise integration. Integrating the proposed density over space
also gives t^3/6, matching integral_0^t u(t-u)du. This calibration is
separate from the weighted inequality and claims no uniform weighted bound.

Maximum relative discrepancy for direct-theta versus elliptic evaluation:
1.43e-15. Maximum unweighted-control errors over both angular maps and
z=0,.5,.9,.99,.999,.9999:

| nodes | maximum observed relative error |
|---|---|
|64|1.69e-4|
|128|2.40e-5|
|256|9.15e-6|

These are observed discrepancies, NOT certified error bounds. Resolution
agreement cannot exclude a missed layer at other configurations. Rounding,
elliptic evaluation and quadrature error are all floating-point sources.
No Monte Carlo confidence interval applies. The test is restricted to W=0,
Z=(1-epsilon,0), not a search of every remote point.

## Endpoint observations

Values of epsilon^(alpha-3/2) I_alpha((1-epsilon,0),0), using256nodes:

|alpha|epsilon=.1|.01|.001|.0001|
|---|---:|---:|---:|---:|
|1.5|1.060904|1.075669|1.087507|1.092010|
|1.6|1.429181|1.419063|1.423357|1.425121|
|1.75|2.905504|2.839667|2.835056|2.834899|
|1.9|14.066559|13.703863|13.669558|13.666187|

For these weighted rows, the maximum256-node angular-map discrepancy is
below5e-9; the maximum128-to256 plain-map relative change is below6.5e-6.
These diagnostics are consistent with the endpoint scaling lower bound.
They do NOT prove an asymptotic equivalence or sufficiency of q>=alpha-1.
Even at q=.95, ratios may be large (about61.6 at alpha=1.9,epsilon=.0001);
finite parameter-dependent constants are allowed by(WC), so this is not a
counterexample. No claim about sharp constants follows.

Evidence: quadrature.py (actual evaluator), quadrature-results.json (all
parameters/controls/refinements). Reproduction uses uv with numpy and scipy;
no global package or system configuration is changed.
