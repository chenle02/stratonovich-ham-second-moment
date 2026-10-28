# Planar endpoint covariance screen

Date:2026-10-28 UTC. Status: **SURVIVES / UNREVIEWED**.
Decision: **REFRAME to a bounded covariance-endpoint lemma in d=2 only**.
No defect was found in the proposed planar endpoint construction after the
checks below. This is GPT-family source/statement screening, not independent
scientific review, a proof of the full moment theorem, or a novelty claim.
The Riesz review packet and canonical notes were not changed.

## 1. Exact covariance contract and source compatibility

Let d=2,1<alpha<2 and let gamma be a nonzero, even, nonnegative, positive-
definite tempered covariance distribution, homogeneous of degree-alpha.
Because it is nonnegative as a distribution, it is a locally finite Radon
measure. Its measure scaling is

  gamma(lambda A)=lambda^(2-alpha) gamma(A), lambda>0.

Do not confuse this with the density formula gamma(lambda x)=lambda^(-alpha)
gamma(x). If gamma is an ordinary locally integrable covariance function,
read gamma(dx)=gamma(x)dx; both constructed endpoints below are then ordinary
locally integrable functions as well. No extension to singular measures is
needed to obtain the function-covariance case.

The source framework is not restricted to bounded or isotropic covariance
functions. The current Chen author PDF, pp2–3, posits possibly generalized
Gaussian noise, nonnegative covariance gamma, a spectral measure and
homogeneity. Page13 explicitly discusses generalized covariance objects and
the Gaussian approximation definition. The published static Chen–Hu source,
pp2145–2147 and2151–2153, likewise permits generalized noise/covariance and
states its homogeneous theorem without angular-density or isotropy assumptions.
Thus a positive homogeneous measure covariance with its spectral interpretation
matches the stated generalized framework. A final statement must make that
interpretation explicit rather than writing an undefined pointwise product of
distributions. If the project scope is read as function covariances only, the
function-preservation observation above avoids enlarging it.

Source identities (unchanged):
- Chen author: `sources/chen-2026-author/aap-chen-2025.pdf`, SHA256
  `5f7385ca451e643a1f3ff31835e4ee52b2708b5d2e3652eec3fb5d3958b97b6c`.
  Pages2–3 newly rendered/viewed in `planar-source-pages/`; p13 was actually
  rendered/viewed in the preceding source-followup.
- Chen–Hu publisher: `../SPDEForge/sources/chen_hu-25-hyperbolic/published-24-AOP1758.pdf`,
  SHA256 `58b152d78cd0d54d82b991933b3eaece86e1ed2b44fe09882c14eba921e97e22`.
  The pages listed above were actually rendered/viewed in this session's
  earlier static-source audit. This screen does not re-prove its theorems.

The accepted project degree-one convolution lemma explicitly has no isotropy
or angular-density requirement. The static source coefficient bound(S) in
`source-audit.md` is likewise for general nonnegative positive-definite
homogeneous covariance, not merely Riesz: its specialization to Riesz in that
audit was a choice of endpoint, not an additional printed source hypothesis.

## 2. Polar measure and local integrability checks

Since2-alpha>0 and gamma is locally finite, scaling forces gamma({0})=0.
Define the finite even angular measure

  sigma(E)=(2-alpha) gamma({x:0<|x|<=1,x/|x| in E}).

Then polar rectangles have the masses corresponding to

  gamma(dx)=r^(1-alpha) dr sigma(domega), r>0, omega in S^1.

Indeed sector mass up to radius R is R^(2-alpha) times its unit-radius mass;
subtract two radii and differentiate/integrate the scalar power. This determines
the measure on polar rectangles. Finiteness of sigma comes from the unit ball.

Fix beta with alpha<beta<2 and define actual weighted measures

  Gamma_low(dx)=|x|^(alpha-1) gamma(dx),
  Gamma_st(dx)=|x|^(alpha-beta) gamma(dx).

They have polar forms dr sigma(domega) and r^(1-beta)dr sigma(domega),
respectively. Both are locally finite, even, nonnegative and tempered; their
homogeneity degrees are1 and beta. The potentially singular weight defining
Gamma_st is justified by beta<2, not by a formal multiplication of distributions.
For any Schwartz psi, both weighted measures integrate |psi| absolutely: the
radial powers are integrable at0 and rapid decay handles infinity uniformly
in direction. These observations supply the absolute-Fubini conditions below.

## 3. Degree-one endpoint: line-mixture positivity

Evenness gives the exact formula, for a Schwartz test function f,

  integral f(x) Gamma_low(dx)
    = (1/2) integral_S1 sigma(domega) integral_R f(r omega)dr.       (L)

**The factor1/2 is required** when sigma is the even measure on the full sphere;
a mixture over unoriented lines can absorb that normalization differently.
This is the only normalization correction needed in the root's informal outline.

For a complex Schwartz phi, set tildephi(x)=conjugate(phi(-x)) and
psi=phi*tildephi. Fubini in coordinates x=s omega+v gives

  integral_R psi(r omega)dr
    = integral_(omega-perp) |integral_R phi(s omega+v)ds|^2 dv >=0.

All integrals are absolutely controlled by Schwartz decay. Insert this into(L)
and integrate the finite positive angular measure. Thus Gamma_low is positive
definite. This check uses the *physical covariance's* polar angular measure,
not the spectral measure from the existing degree-one proof; confusing those
two angular measures would invalidate the identification of constants.

## 3a. Direct planar wave bound from the physical line mixture

This self-contained local integral avoids spectral normalization entirely.
Let

  G_h^(2)(v)=1_(|v|<h)/(2 pi sqrt(h^2-|v|^2)), h>0,
  S=sigma(S^1)=(2-alpha)gamma(B_1).

Choose a unit vector omega and either unit perpendicular omega_perp. Decompose
z=a omega+b omega_perp. If |b|<h, set A=sqrt(h^2-b^2)>0. Translation in the
line coordinate then gives

  integral_R G_h^(2)(z-r omega)dr
    = (1/(2 pi)) integral_(-A)^A (A^2-s^2)^(-1/2)ds
    = (1/(2 pi))*pi = 1/2.

If |b|>h the support is empty. At |b|=h, the open-disk representative is zero
along the line, apart from a possible arbitrary value at its single tangency
point; that point has zero line Lebesgue measure. Taking the kernel to be zero
on the circle gives the literal formula

  integral_R G_h^(2)(z-r omega)dr
    = (1/2)1_(|z dot omega_perp|<h).                            (LW)

The same value results for any change at the finitely many circle-line
intersection points. No limiting interior value is asserted at tangency. The
Gaussian-averaged application below is insensitive to a boundary representative.

By nonnegative Tonelli and the exact half-line-mixture factor in(L),

  (G_h^(2)*Gamma_low)(z)
    := integral_R2 G_h^(2)(z-x)Gamma_low(dx)
     = (1/2) integral_S1 sigma(domega)
           integral_R G_h^(2)(z-r omega)dr
     = (1/4) integral_S1 1_(|z dot omega_perp|<h)sigma(domega)
     <= S/4.                                                   (PW)

This holds for all h>0,z in R2 with the stated representative and also defines
the bounded density of the measure convolution. It is a physical-space
calculation for Gamma_low; no Fourier convention, spectral angular measure,
or identification of S with spectral ball mass V is used.

For covariance Gaussian smoothing epsilon>0 and Green smoothing eta>=0,
nonnegative Tonelli, associativity with the Gaussians, and their convolution
rule yield

  integral_R2 G_(h,eta)(dy)(p_epsilon*Gamma_low)(y+z)
    = [p_(epsilon+eta)*(G_h^(2)*Gamma_low)](z)
    <= S/4.                                                    (PW-sm)

Here p_0 is interpreted as the identity point mass when needed; in the displayed
application epsilon+eta>0. The sign in y+z is harmless because the wave measure
and its Gaussian smoothing are even. The mass-one Gaussian average preserves
the constant. Finiteness follows directly from(PW), so no unproved integrability
of a separate formal convolution is being assumed. The source convention where
noise width epsilon produces covariance width2epsilon merely substitutes that
positive width and does not change the bound.

**Proposed coefficient application, not a new moment-theorem claim.** In the
existing degree-one coefficient bookkeeping the spatial convolution constant
M gives K_sp=2M and coefficient constant2 Z_(b0)K_sp=4 Z_(b0)M. Thus(PW-sm)
would give

  C_low=Z_(b0) S,
  Z_(b0)=2/[(1-b0)(2-b0)], 0<b0<1.

Equivalently the inherited coefficient format is
C_low^k t^((3-b0)k)/(k! k^k), bounded above by the same numerator/(k!)^2.
This line records substitution into the existing framework only. A full planar
interpolation theorem must still give its regularized diagram, limit and
coefficient-summation argument and pass independent review. In particular,
S=(2-alpha)gamma(B_1) is the original covariance's physical angular mass;
it has not been equated to the endpoint spectral mass V.

## 4. Static endpoint: Gaussian-mixture positivity

Put lambda=beta-alpha>0. Away from0,

  |x|^(-lambda) = 1/Gamma(lambda/2)
      integral_0^infinity s^(lambda/2-1) exp(-s|x|^2) ds.

For each s>0, exp(-s|x|^2)gamma is positive definite: its Fourier transform
is a positive Gaussian convolution with the original positive spectral measure.
Equivalently, its value on phi*tildephi is nonnegative. This product is a
well-defined smooth multiplication of the original tempered distribution.
For psi=phi*tildephi, absolute integrability of
integral |psi(x)| |x|^(-lambda) gamma(dx) follows from Section2. Hence Tonelli
with |psi| and then Fubini justify integrating those nonnegative quadratic forms
against s^(lambda/2-1)ds. The result is Gamma_st(psi)>=0.

No assumption that arbitrary fractional powers of gamma are positive definite
is used. Positivity of the original covariance is used here, whereas the
line-mixture construction of Gamma_low only needs the nonnegative even angular
measure. Gamma_st can be singular along existing angular supports; this is not
an obstruction to local finiteness or the generalized covariance construction.

With their positive spectral measures, homogeneity gives endpoint spectral ball
growth of degree1 and beta. The low endpoint satisfies the fractional-time
spectral condition when b0<1; the static endpoint satisfies Dalang when beta<2.
This is exactly the source parameter criterion. The constants depend on the
actual angular covariance, not merely on alpha or beta.

## 5. Gaussian interpolation check

Choose alpha0<theta<2-alpha and put

  b0=alpha0/theta,
  beta=(alpha-theta)/(1-theta).

Then0<theta<1,0<b0<1 and alpha<beta<2. The identity needed for the radial
weights is

  theta(alpha-1)+(1-theta)(alpha-beta)=0.

For fixed z and epsilon>0 use the finite measure

  nu_(z,epsilon)(dx)=p_epsilon(z-x) gamma(dx).

It need not have mass1; Hölder's conjugate exponents1/theta and1/(1-theta)
are valid on this finite positive measure. Since gamma has no atom at0,

  (p_epsilon*gamma)(z)
    = integral [|x|^(alpha-1)]^theta
               [|x|^(alpha-beta)]^(1-theta) nu_(z,epsilon)(dx)
    <= (p_epsilon*Gamma_low)(z)^theta
       (p_epsilon*Gamma_st)(z)^(1-theta).                       (H)

Endpoint integrals are finite by the tempered/local-integrability checks. This
is a statement about weighted measures and Gaussian convolution; it never
assigns a pointwise fractional power to a singular covariance distribution.
The same covariance width must be used on each target/endpoints edge. Common
noise smoothing therefore uses edge width2epsilon everywhere, exactly as in
the already audited Riesz interpolation setup.

This screen checks(H) and endpoint admissibility only. It does not certify the
subsequent all-pairing Hölder transfer, mixed-moment limits or full coefficient
bound for the generalized endpoint pair. Those steps must be stated in a fresh
complete candidate and reviewed; they must not be silently appended to the
currently running Riesz review.

## 6. Defect-first controls and precise boundary

| Control | Result |
|---|---|
| Unspecified product of distributions | Avoided: gamma is a positive Radon measure; weighted endpoints are locally finite measures. |
| Atom at0 times singular radial weight | Excluded by positive homogeneity exponent2-alpha and local finiteness. |
| Missing line-mixture factor | Corrected: full even sphere requires1/2 in(L). |
| Direct planar wave normalization | PASS locally: line integral1/2, hence total bound sigma(S1)/4; Gaussian averaging preserves it. |
| Arbitrary noninteger covariance powers | Not used; both endpoint PD arguments are explicit and different. |
| Static weight not locally integrable | Ruled out precisely by beta<2; endpoint beta=2 excluded. |
| Gaussian Hölder assumes normalized gamma measure | Not required; ordinary Hölder applies to nu_(z,epsilon). |
| Function-only source interpretation | Endpoints preserve functions whenever the starting gamma is a function; no silent source-class enlargement needed. |
| Generalized source interpretation | Consistent with explicit source smoothing framework, but state distributional homogeneity/measure weights clearly in the candidate. |
| Dimension3 reuse of line-mixture argument | NOT VALIDATED: physical polar measure becomes r dr after the same weighting, not dr. No d3 conclusion. |

A useful exact non-isotropic control is the original product covariance
|x1|^(-a1)|x2|^(-a2),0<a1,a2<1,a1+a2=alpha: its angular density is finite
as a measure despite unbounded axial values, so the low endpoint construction
remains meaningful. This is a consistency example, not a newly computed
moment estimate. The earlier spatial-supremum obstruction is not contradicted:
this endpoint strategy changes the covariance before applying the lower-degree
bound; it does not assert a finite supremum for the original higher-degree one.

The zero covariance is separately trivial; it need not be normalized into an
angular probability measure. No covariance normalization or arbitrary common
constant is hidden in this screen.

## Disposition

The covariance-level proposal **survives** this bounded mathematical and
source-class screen for d2. The next permitted research unit is a complete,
source-bound planar endpoint lemma with independent review, followed by an
explicit application of the existing interpolation framework. No full planar
moment theorem, full G:upper closure, general d3 extension, sharp constant,
novelty claim or Riesz-review promotion follows from this report.
