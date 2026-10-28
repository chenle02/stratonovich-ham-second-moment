# A d3 obstruction to naive radial degree lowering

Date:2026-10-28 UTC. Status: **AUTHOR CHECK / UNREVIEWED**.
Scoped verdict: the proposed explicit example does show that multiplying an
admissible degree3/2 covariance by |x|^(1/2) need not preserve positive
definiteness in d3. The primary short argument in Section2a uses only the
standard boundedness of a Gaussian-smoothed positive-definite covariance.
The previously written sphere argument is retained in Sections3–5 and uses
the accepted project Lemma L:alpha-one-convolution as an additional check.
This is not a moment-growth no-go,
not a defect in the Riesz interpolation, and not a proof that no different
d3 endpoint construction can work. Separate review remains required.

No canonical notes, frozen packets or source files were changed.

## 1. The original covariance is admissible

In R3 set

  a1=9/10,  a2=3/5,  alpha=a1+a2=3/2,
  gamma(x)=|x1|^(-a1)|x2|^(-a2), independent of x3.

Values on the singular planes may be set arbitrarily when regarding gamma
as a locally integrable density. Since0<a1,a2<1, gamma is locally integrable,
nonnegative and even. It is homogeneous of degree-alpha and tempered.
For instance, integrating its product-coordinate singularities against a
sufficiently rapidly decaying product weight is finite.

Its positive definiteness can be justified without multiplying distributions.
For0<a<1 and x!=0 use

  |x|^(-a)=Gamma(a/2)^(-1)
             integral_0^infinity s^(a/2-1) exp(-s x^2) ds.

Apply this separately to x1,x2. Every Gaussian
exp(-s x1^2-t x2^2), constant in x3, is a positive-definite function on R3.
For a complex Schwartz phi and psi=phi*tildephi, the integral of gamma|psi|
is finite. Tonelli with |psi| and Fubini therefore justify the double positive
mixture against psi. Each Gaussian quadratic form is nonnegative, so
integral gamma(x)psi(x)dx>=0. Thus gamma is a positive-definite tempered
covariance. The source spectral condition holds for alpha0=1/4, since
alpha+alpha0=7/4<2. The original covariance is within the project's
homogeneous existence range.

## 2. The radially lowered density has all the easy endpoint properties

Define

  F(x)=|x|^(1/2)|x1|^(-9/10)|x2|^(-3/5).

It is nonnegative, even and homogeneous of degree-1. It is locally integrable:
on a bounded ball the factor |x|^(1/2) is bounded, and gamma is integrable.
Its mass scales as

  integral_(|x|<=R) F(x)dx = R^2 integral_(|x|<=1) F(x)dx.

Consequently F is a tempered positive measure, and
integral (1+|x|)^(-N)F(x)dx<infinity for N>2. This also proves the required
finite angular integral in its degree-one polar disintegration; no uniform
angular density is asserted. The only disputed property is positive
definiteness.

## 2a. Primary short contradiction: a fixed Gaussian smoothing grows at infinity

This additional check was proposed by the root after the sphere proof below
was written. It preserves that earlier argument and avoids depending on the
degree-one convolution lemma for the conclusion.

Use Gaussian variance1:

  p_1(v)=(2 pi)^(-3/2) exp(-|v|^2/2),
  z_L=(0,0,L), L>=1,
  Q_L=[1,2] x [1,2] x [L,L+1].

The box has Lebesgue volume1. For every y in Q_L,

  |y|>=y3>=L,
  |y1|^(-9/10)|y2|^(-3/5)>=2^(-9/10-3/5)=2^(-3/2),
  |z_L-y|^2=y1^2+y2^2+(L-y3)^2<=4+4+1=9.

Consequently, all inequality directions are lower bounds in the convolution:

  F(y)>=L^(1/2)2^(-3/2),
  p_1(z_L-y)>=(2 pi)^(-3/2)exp(-9/2),

and nonnegativity permits restriction to Q_L. Therefore

  (p_1*F)(z_L)
    >= integral_Q_L p_1(z_L-y)F(y)dy
    >= C L^(1/2),
  C=2^(-3/2)(2 pi)^(-3/2)exp(-9/2)>0.                    (B)

By Section2's polynomial mass bound, (p_1*F)(0) is finite. In fact the same
bound ensures p_1*F is finite and continuous at every point.

Suppose F were positive definite as a tempered distribution, with positive
tempered spectral measure mu_F in the project convention. Gaussian convolution
then has the finite positive spectral measure

  exp(-|xi|^2/2)mu_F(dxi).

It follows directly by the triangle inequality for its Fourier integral that

  |(p_1*F)(z)|
    <= integral exp(-|xi|^2/2)mu_F(dxi)
     = (p_1*F)(0) < infinity,  for every z.

This contradicts(B) as L tends to infinity. Thus F is not positive definite.
Equivalently, one could use the2x2 positive-semidefinite covariance inequality
for the Gaussian-smoothed covariance, after first establishing that it is
positive definite. Gaussian convolution preserves that property because its
Fourier multiplier is nonnegative, not because arbitrary spatial translations
would preserve positive definiteness.

This proof uses no sphere singularity, epsilon limit, or degree-one wave
convolution bound. It is a second mathematical mechanism checked by the same
GPT-family authors, not an additional independent-review vote.

## 3. Its shifted unit-sphere convolution is infinite

Use the source normalization G_1^(3)(dy)=sigma_1(dy)/(4 pi), where sigma_1
is unit-sphere surface measure. Choose

  z=(-1,0,3).

For every |y|=1, y3+3>=2, hence |y+z|>=2. Away from the singular set,

  F(y+z) >= sqrt(2) |y1-1|^(-9/10)|y2|^(-3/5).

This positive inequality is valid for integration in the extended sense.
Projection of G_1^(3) onto the first two coordinates gives exactly

  G_1^(2)(du dv)
    = 1_(u^2+v^2<1) du dv / (2 pi sqrt(1-u^2-v^2)).

Indeed the upper and lower sphere graphs each contribute surface Jacobian
(1-u^2-v^2)^(-1/2), and their sum is divided by4 pi. Since the original
covariance is independent of x3, this gives

  integral G_1^(3)(dy) gamma(y+z)
    = (1/(2 pi)) integral_(u^2+v^2<1)
        |1-u|^(-a1)|v|^(-a2) / sqrt(1-u^2-v^2) du dv.

Set h=1-u, so0<h<2, and then v=sqrt(2h-h^2)w. Tonelli and the elementary
beta integral yield the exact extended-valued identity

  integral G_1^(3)(dy) gamma(y+z)
    = B((1-a2)/2,1/2)/(2 pi)
        integral_0^2 h^(-a1)(2h-h^2)^(-a2/2) dh.

Here B(1/5,1/2) is finite and positive. Near0,2h-h^2<=2h, so the radial
integrand is bounded below by

  2^(-3/10) h^(-9/10-3/10)=2^(-3/10)h^(-6/5).

Its integral diverges. Therefore both the original shifted gamma integral
and the shifted F integral are infinite. For F, the shift in the third
coordinate is essential to this simple comparison: it keeps the multiplying
radial factor bounded away from zero near the tangency singularity.

## 4. Gaussian smoothing recovers F almost everywhere on the shifted sphere

Let p_epsilon be the centered Gaussian density with covariance epsilon I,
and F_epsilon=p_epsilon*F. For each fixed epsilon>0, this is finite,
nonnegative and continuous; Gaussian decay controls the tempered positive
measure F, uniformly for convolution centers in a compact set.

For a fixed x with x1*x2!=0, F is continuous in a neighborhood of x. We give
the tail control because F is NOT bounded at spatial infinity near its
singular planes. Choose delta>0 smaller than the distance of x to those
planes. For0<epsilon<=1 and |x-y|>=delta,

  p_epsilon(x-y)
    <= (2 pi epsilon)^(-3/2)
       exp(-delta^2/(4 epsilon)) exp(-|x-y|^2/4).

The Gaussian-weighted integral of F(y) on the right is finite by its
polynomial-mass bound. The prefactor
 epsilon^(-3/2) exp(-delta^2/(4epsilon)) tends to zero. Thus the tail
contribution vanishes as epsilon decreases to0. On |x-y|<delta, continuity
bounds the difference from F(x); first let epsilon decrease to0 and then
let delta decrease to0. The Gaussian tail multiplying the constant F(x)
also vanishes. Hence

  F_epsilon(x) -> F(x) whenever x1*x2!=0.

On the sphere shifted by z, the excluded equations are y1=1 and y2=0.
The first gives one tangent point and the second a great circle. Both have
zero sphere surface measure. Consequently F_epsilon(y+z)->F(y+z) for
G_1^(3)-almost every y. Fatou's lemma now gives

  infinity = integral G_1^(3)(dy)F(y+z)
    <= liminf_(epsilon->0) integral G_1^(3)(dy)F_epsilon(y+z).

The finite-epsilon integrals are finite; their lower limit is infinite.
No monotonicity in epsilon has been assumed, and no infinite value at a
single point is being used to infer divergence.

## 5. Contradiction with positive definiteness

Suppose for contradiction that F were positive definite. By Section2 it
would then satisfy all covariance hypotheses of the accepted degree-one
convolution lemma L:alpha-one-convolution in the project notes, d=3.
Its positive spectral measure mu_F would be Radon with

  V_F=mu_F({xi:|xi|<=1})<infinity.

That lemma, with h=1 and Green smoothing eta=0, gives

  0 <= integral G_1^(3)(dy) F_epsilon(y+z) <= pi V_F/2

for every epsilon>0 and every shift z. This contradicts Section4.
Therefore F is not positive definite as a tempered distribution.

The imported lemma is used exactly at its declared scope: nonnegative,
even, positive-definite homogeneous covariance of degree1, arbitrary angular
spectral measure, Gaussian covariance smoothing, and allowed eta=0. Its proof
retains oscillatory Fourier structure before the one-dimensional Gaussian
inversion; the divergent absolute spectral envelope is not substituted here.
This memo is a separate use of that accepted lemma, not a new independent
verification of its whole proof.

## 6. Claim boundary and falsification record

| Check | Outcome |
|---|---|
| Original gamma nonnegative/PD/local integrability | PASS by explicit product-Gaussian mixture and a1,a2<1. |
| Original model existence parameters | PASS at alpha0=1/4,alpha=3/2. |
| F degree1/nonnegative/local finite/tempered | PASS; these properties alone do not imply PD. |
| Fixed Gaussian lower bound at infinity | PASS with explicit positive C and growth sqrt(L); contradicts the standard PD covariance bound. |
| Shifted sphere divergence | PASS with exact beta reduction and exponent6/5>1. |
| Approximate identity despite growth/singular planes | PASS by weighted Gaussian tail estimate and local continuity. |
| Uniform mollified degree-one convolution if F PD | Imported accepted lemma gives it; Fatou contradicts it. |
| Naive d3 radial-lowering construction | FALSIFIED for this explicit gamma. |
| General d3 moment upper bound or other endpoint choices | NOT DECIDED. |

No new SPDE estimate or Skorohod result is claimed. This obstruction belongs
with the planar endpoint material for separate review, and must not be added
to an existing frozen Riesz packet or described as an accepted result before
that review.
