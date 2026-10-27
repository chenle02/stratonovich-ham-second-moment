# Alpha-one boundary: independent dimension-extension audit

[held back: collaborators' unpublished work]

## Scope and conclusion of the convolution audit

Let d be 1,2 or3. Retain the source's real Gaussian, stationary spatial
covariance gamma, which is nonnegative and nonnegative definite as a tempered
distribution. Assume gamma is homogeneous of degree -1. Its positive Radon
spectral measure mu is therefore homogeneous of degree1 and **even**. Use the
source convention gamma(x)=integral exp(i xi.x) mu(dxi), and put

    V = mu({xi: |xi|<=1}) < infinity.

For the positive wave kernel G_h, covariance Gaussian regularization
gamma_epsilon, and optional Green regularization G_(h,eta)=p_eta*G_h,

    0 <= integral G_(h,eta)(dy) gamma_epsilon(y+z)
       <= pi V/2                                               (B1)

uniformly in h>0, z in R^d, epsilon>0 and eta>=0. Eta=0 denotes the
unregularized positive wave measure. The zero-noise case V=0 is trivial.
No angular density or isotropy is assumed. This includes admissible
higher-dimensional degree-one covariances, not full spatial white noise in
d=2 or3 (whose homogeneity degree would instead be d).

## 1. Polar measure and exact normalization

As in the low-alpha audit, Fourier uniqueness gives

    mu(cA)=c mu(A), c>0.

Local finiteness and this scaling imply mu({0})=0. Define an angular measure
on the unit sphere by

    sigma(E) = mu({xi: 0<|xi|<=1, xi/|xi| in E}).

It is finite, and sigma(S^(d-1))=V. For every R>0,

    mu({xi: 0<|xi|<=R, xi/|xi| in E})=R sigma(E).

Hence the polar pushforward of mu is **dr times sigma(dtheta)** on
(0,infinity) times the sphere. One can verify this first on radial intervals
and angular Borel sets, then use uniqueness of measures. There is no extra
factor alpha at alpha=1 and no missing sphere-area factor: all angular mass
is included in sigma.

Since gamma is the covariance of a real stationary field, gamma(-x)=gamma(x)
as distributions. Fourier uniqueness gives mu(-A)=mu(A), and consequently
sigma(-E)=sigma(E). Thus integration of exp(i r theta.z) against sigma equals
integration of cos(r theta.z). This replacement introduces **no factor2**;
both antipodal directions are already present in sigma.

This evenness is essential to the displayed real-cosine formula. Do not infer
it solely from positivity of an arbitrary spectral measure for a complex
field. The project's real covariance supplies it.

## 2. Gaussian Fourier calculation

The source's wave transform is

    Fourier(G_h)(xi)=sin(h|xi|)/|xi|,
    integral G_h=h.

The covariance and Green Gaussian regularizations contribute a combined
multiplier exp(-a|xi|^2) for some a>0 (with the variance convention p_s,
a is half the sum of the relevant Gaussian variances). Its exact parameter
name is immaterial, but its positivity is not.

At each positive smoothing, mu with this multiplier has finite total mass.
Since G_h is a finite positive measure, Fourier Fubini is justified before
removing any smoothing. Evenness and the polar representation then give

    integral G_(h,eta)(dy) gamma_epsilon(y+z)
      = integral sigma(dtheta) I_a(h,theta.z),

    I_a(h,b) = integral_0^infinity
                   exp(-a r^2) [sin(hr)/r] cos(br) dr.         (B2)

Near zero sin(hr)/r is bounded by h, and at infinity the Gaussian makes
the radial integral absolutely integrable. This is not the divergent
absolute-envelope estimate used below alpha1: the oscillation is retained
until the one-dimensional integral is evaluated.

Let

    g_h(v) = (1/2) 1_{|v|<h},
    p_(2a)(v) = (4 pi a)^(-1/2) exp(-v^2/(4a)).

Under the one-dimensional Fourier convention used by the source,
Fourier(g_h)(r)=sin(hr)/r and Fourier(p_(2a))(r)=exp(-a r^2).
Fourier inversion of their integrable convolution gives

    (g_h*p_(2a))(b)
      = (1/(2pi)) integral_R
           exp(i r b) exp(-a r^2) sin(hr)/r dr
      = (1/pi) I_a(h,b).

Therefore the exact normalization is

    I_a(h,b) = pi (g_h*p_(2a))(b).                          (B3)

The sign in the inversion exponential has no effect here because the
integrand after pairing r and -r is even. Since p_(2a) is a probability
density and 0<=g_h<=1/2,

    0<=I_a(h,b)<=pi/2,

which proves (B1) after integrating sigma, whose total mass is V.
The real-space nonnegativity also follows directly from gamma>=0 and the
positive Green/Gaussian kernels; that source assumption remains available
for the full diagram argument.

For a direct constant check, (B3) is equivalently

    I_a(h,b) = (pi/4) [erf((h+b)/(2 sqrt(a)))
                              + erf((h-b)/(2 sqrt(a)))].

In particular at b=0 and fixed h>0 it tends to pi/2 as a decreases to zero.
Thus pi V/2 is sharp for this uniform convolution estimate whenever V>0;
sharpness of this local estimate says nothing about sharp moment constants.

## 3. White and dimensional normalization checks

For d=1 and gamma=c delta_0, the source normalization is
mu(dxi)=c dxi/(2pi). Polar coordinates have the two directions +1,-1,
each with angular mass c/(2pi), so

    V=c/pi,       pi V/2=c/2.

This recovers exactly the elementary white-space convolution bound, with
no spurious factor2. It also checks that sigma counts both directions.

For isotropic degree-one Riesz covariance c/|x|, V=c in d=2 and V=2c/pi
in d=3, hence M=pi c/2 and M=c respectively. One way to check the spectral
normalization, without guessing a dimension-dependent Fourier factor, is to
use the distributional identity gamma=pi*integral sigma(dtheta)delta(theta.x),
obtained from one-dimensional Fourier inversion along each direction. If
sigma=w times surface measure, the angular delta integral is
area(S^(d-2))/|x|. Thus c=pi*w*area(S^(d-2)), while V=w*area(S^(d-1));
areas 2,2pi,4pi give the displayed values. These constants can also be
checked directly at z=0:

- d=2: integral_0^h c(h^2-r^2)^(-1/2) dr=pi c/2;
- d=3: the wave sphere mass is h and c/|y|=c/h on that sphere, giving c.

The main proof does not use these Riesz normalizations; it uses V directly.
An angular atomic measure is equally allowed. For example, the spectral
measure of a covariance depending only on one spatial coordinate is
concentrated on an axis, and (B2)–(B3) still apply unchanged.

## 4. Descending spatial integration and moment transfer

At alpha=1 the common closing-variable bound is now

    M=pi V/2,

while an opening variable integrates the wave mass h. The vector-increment
change of variables remains triangular separately within each chain. The
root's induction invariant (remaining covariance factors have both endpoints
at most the current label) therefore gives

    S_D(h) <= M^k product_open h_l.

There are k opening variables and sum h_l<2t. Ordinary AM–GM, with no
negative or zero weights inserted into a weighted formula, gives

    S_D <= (2M)^k t^k k^(-k),
    Ksp=2M=pi V.                                         (B4)

The same bound holds with every Gaussian regularization. In d=3 take the
source's Green eta limit first at fixed noise smoothing, using L2 convergence
and L1 convergence of products, and then take the noise-smoothing limit.
The Fourier multiplier estimate is uniform at both stages; G_(h,eta) keeps
mass h. The measure-valued sphere kernel is never treated as a density.
At fixed smoothing, the inner weak-kernel limit can also be justified using
bounded continuous covariance products and finite Green masses, as detailed
in the low-alpha audit.

Replace temporal truncations by the common full |s-r|^(-alpha0) kernel
before using symmetry. With Z=2/[(1-alpha0)(2-alpha0)], the full all-pairing
sum and all two-chain splits then give, for k>=1,

    A_k(t) <= (2 Z pi V)^k t^((3-alpha0)k)/(k!)^2.

Adding the k=0 term and applying the same nonnegative-series inequality gives

    E u(t,x)^2
      <= exp{2 sqrt(2 Z pi V) t^((3-alpha0)/2)}.           (B5)

This is the desired kappa scale at alpha=1. The proposed upper constant is
coarse; no sharp-constant statement is being made. Empty-chain cases are
included exactly as in the d=1 proof. The full Stratonovich pairing sum,
including domestic pairings, remains the object being bounded.

## 5. Boundary and acceptance conditions

1. Combined with the separately justified alpha<1 argument, the natural
   scope is **0<alpha<=1 in d=1,2,3**, under the source covariance assumptions.
   In d=1 the alpha=1 case is the spatial-white endpoint. In d=2,3 it is the
   degree-one homogeneous class, not full-dimensional white noise.
2. The alpha<1 absolute-Fourier constant diverges as alpha approaches one.
   The endpoint is obtained by the new exact oscillatory calculation, not
   by taking a limit in that divergent bound. No parameter-uniform constant
   across alpha=1 is asserted.
3. Nothing here covers alpha>1. No exploration of that regime was undertaken.
4. Mu need not have a Lebesgue density or uniform angular component. Its
   evenness, degree-one homogeneity and finite angular mass must be stated.
5. Gamma>=0 remains part of the source assumptions used for nonnegative
   diagram comparisons; no complex-field or sign-changing extension is claimed.
6. The eta-first definition, source fixed-order L2 limits, and G0 mixed-series
   identity remain explicit imported analytic inputs.
7. This boundary extension needs a new frozen scientific review scope. It is
   not included retroactively in the unchanged d=1 candidate or its review.
8. No Skorohod theorem, Lean certificate, novelty judgment or circulation
   clearance is claimed by this audit.

Source correspondence is the same hash-pinned author PDF used in the prior
low-alpha memo: (1.3) for the spectral convention, (2.3)–(2.5) for the wave
transform and mass, (2.24) for Gaussian covariance smoothing, and pp.13–14
for the dimension-three kernel approximation. The new polar/Gaussian integral
calculation above is supplied explicitly rather than attributed to the source.

STATUS: DONE_WITH_CONCERNS — the alpha-one convolution bound and its
all-dimensions transfer appear correct; independent scientific acceptance
and manuscript integration remain pending.
