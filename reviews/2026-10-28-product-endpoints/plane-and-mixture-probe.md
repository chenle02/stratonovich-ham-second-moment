# Covariance endpoints for plane-supported measures and finite positive sums

Date: 2026-10-28. Status: complete local deterministic argument, **unreviewed**.
This is not part of the currently frozen Section 9 review packet. It neither
extends its accepted scope nor supplies a general representation theorem.
No stochastic, Skorohod, sharpness, novelty or Lean claim is made.

## Falsification before generalization

The ordinary-product lemma deliberately excludes a coordinate exponent one:
substituting it into its density or Gamma mixture would be invalid. Instead
take an actual measure, with coordinates x=(y,z) in R²×R,

    Gamma_a(dy,dz) = c |y_1|^(-a_1)|y_2|^(-a_2) dy delta_0(dz),
    c>0, a_j>=0, s=a_1+a_2 in (0,1), alpha=1+s.

Each a_j<1 follows from s<1. A zero coordinate exponent means one. At the
specific admissible test a=(1/2,0), alpha0=1/4, the midpoint theta=3/8 gives
v=(4/5,0), beta=9/5. The low covariance is the plane Lebesgue measure times
c, and the static covariance has tangential exponents v and the SAME normal
delta. Gaussian convolution factors as an ordinary 2D convolution times
p_epsilon^(1)(z). Its normal factor is reproduced exactly because
theta+(1-theta)=1. There is no fractional power of a delta distribution.
The exact parameter controls are independently executable in
plane-and-mixture-controls.py. They are finite algebra controls, not an
analytic or independent scientific certificate.

## 1. Plane-supported endpoint construction

Fix alpha0 in (0,1), s in (0,1-alpha0), and theta in (alpha0,1-s).
Set alpha=1+s, beta=1+s/(1-theta), v_j=a_j/(1-theta). Then

    alpha0 < theta < 2-alpha,
    1 < alpha < beta < 2,
    0 <= v_j < 1, sum v_j = beta-1.

Define the three measures on R³ using the COMMON underlying measure
m(dy,dz)=dy delta_0(dz):

    Gamma_a = c f m,       f(y)=product_j |y_j|^(-a_j),
    Gamma_low = c m,
    Gamma_st = c f^(1/(1-theta)) m.

All are positive, even, locally finite and tempered. For Gamma_a and
Gamma_st, local finiteness follows by the two one-dimensional integrals
with coordinate exponents below one; for Gamma_low it is immediate.
Rapid Schwartz decay gives absolute integrability at infinity. Under
isotropic dilation of a Borel set A, their measure scaling exponents are
respectively 2-s=3-alpha, 2=3-1, and 2-s/(1-theta)=3-beta.

They are positive definite as tempered distributions. Here is a direct
argument including the normal delta. The tangential density f_e for an
active exponent vector e has the positive Gaussian mixture

    product_(j:e_j>0) [Gamma(e_j/2)^(-1)
      integral_0^infinity t^(e_j/2-1) exp(-t y_j²) dt].

Zero coordinates are constant one, and the empty mixture gives the constant
function. Every Gaussian in that mixture is a positive-definite function
on R². For phi in Schwartz(R³), its quadratic form against f_e(y)dy delta_0(dz)
can be written

    integral_R dz integral_R² integral_R²
      f_e(y-y') phi(y,z) conjugate(phi(y',z)) dy dy'.

For each z the inner form is nonnegative. Absolute Fubini is justified by
the rapid decay of the Schwartz autocorrelation and the local coordinate
integrability. Integrating the positive Gaussian forms proves the assertion.
Multiplication by c preserves it. This also proves the low endpoint case.

For each epsilon>0 and x in R³, the measure

    q_x(dy,dz) = p_epsilon^(3)(x-(y,z)) m(dy,dz)

is finite (its total mass is p_epsilon^(1)(x_3)). On this measure apply
Holder to the ORDINARY tangential densities:

    c f = c^theta [c f^(1/(1-theta))]^(1-theta)  m-a.e.

Thus

    (p_epsilon*Gamma_a)(x)
      <= (p_epsilon*Gamma_low)(x)^theta
         (p_epsilon*Gamma_st)(x)^(1-theta).

Both endpoint integrals are finite: a Gaussian integrates each locally
integrable tangential product power, and its normal delta factor is finite.
This verifies exactly the deterministic Hypothesis 9.2, including its common
width and translation quantifiers, for this plane-supported family. It does
not rely on the ordinary-product endpoint lemma at exponent one.

An orthogonal change of coordinates preserves positivity, temperedness,
homogeneity and the isotropic Gaussian. The same verification holds for
any rotated plane-supported covariance with these tangential coordinates.

Normalization control: in the source convention Gamma(x)=int exp(i xi.x)mu(dxi),
the low endpoint c delta_0(x_3), constant in x_1,x_2, has

    mu_low = c/(2pi) delta_0(dxi_1)delta_0(dxi_2) dxi_3,
    V_low = mu_low(B_1) = c/pi.

Indeed (2pi)^(-1)int exp(i xi_3 x_3)dxi_3=delta_0(x_3), while constants
have spectral unit atoms. The degree-one convolution bound pi V_low/2
therefore equals c/2. Directly, G_h in d3 has normal marginal
(1/2)1_{(-h,h)}(z)dz: spherical coarea or the uniform normal coordinate
of surface measure gives this density, its mass is h, and Gaussian averaging
is at most 1/2. This independently matches c/2. This normalization check is
not needed to establish the endpoint hypothesis.

## 2. Finite positive-sum closure of the endpoint condition

Let Gamma_i, i=1,...,N, be target covariances with the SAME homogeneity
exponent alpha and the SAME fixed theta. Suppose admissible endpoints L_i,S_i
of exponents 1,beta verify the common-Gaussian comparison for each i. Let
w_i>=0 be finite constants. Define

    Gamma = sum_i w_i Gamma_i,
    L = sum_i w_i L_i,
    S = sum_i w_i S_i.

Finite sums preserve nonnegativity, evenness, positive definiteness, local
finiteness, temperedness and the stated homogeneous scalings. At any fixed
epsilon,x, put l_i=(p_epsilon*L_i)(x), s_i=(p_epsilon*S_i)(x). These are finite
and nonnegative. Discrete Holder gives

    (p_epsilon*Gamma)(x)
      <= sum_i w_i l_i^theta s_i^(1-theta)
       = sum_i (w_i l_i)^theta (w_i s_i)^(1-theta)
      <= (sum_i w_i l_i)^theta (sum_i w_i s_i)^(1-theta).

Terms with zero weight are zero; the equality uses 0<theta<1 and has no
negative-power convention at zero. Hence (L,S) verify the required comparison.
All-zero target is the separately trivial case. This is closure of a
DETERMINISTIC sufficient condition, not a moment mixture/coupling identity.
It never requires moments of a noise sum to be sums of moments.

For a common alpha, the ordinary-product and Riesz constructions of Section 9
allow every theta in (alpha0,2-alpha). The plane-supported construction above
allows the same interval. A common midpoint theta can therefore be used for
finite positive sums of rotated members of these families. The resulting
covariance can fail to be a single product or an isotropic Riesz covariance.

## 3. What is still missing for the full goal

No assertion is made that every nonnegative positive-definite homogeneous
covariance in d3 is such a finite sum, or that these sums are dense in the
needed topology. Even a covariance approximation would need suitable uniform
endpoint bounds before it could yield the general moment theorem. A countable
or integral-mixture extension requires locally finite tempered endpoint sums;
these cannot be inferred merely from local finiteness of the target sum.

The proper reopen condition for a representation route is an actual positive
decomposition or a general endpoint construction, together with controlled
low/static endpoint masses (and the resulting coefficient constants). The
existing radial-lowering counterexample is not bypassed by calling an unknown
representation dense. The original arbitrary-covariance d3 target stays open.

No canonical notes, frozen reviewer packet, source PDF, sibling Article,
private Lean package or author communication was modified by this probe.
