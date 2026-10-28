# Spatial maximum probe: Riesz covariance and anisotropic obstruction

Date: 2026-10-27. Bounded worker report; self-contained spatial calculation,
not a reviewed manuscript theorem. Only this report is an output of this
worker. No git operations, messages, manuscript/sibling edits or Lean work.

**STATUS: DONE_WITH_CONCERNS.** The spatial input is proved below for d=3
isotropic Riesz throughout the requested range, and for d=2 isotropic Riesz
only below alpha=3/2. The complementary d=2 maximum is falsified, including
uniform Gaussian smoothing. Arbitrary anisotropic homogeneous covariance
cannot be substituted, even when it is a locally integrable function.
Cross-family review and the root's moment-theorem/literature gates remain
outstanding. No originality or moment theorem is claimed here.

## 1. Precise scope and normalization

Write gamma(x)=c|x|^(-alpha), c>0. The wave measures have mass h:

```text
d=2: G_h(dy) = 1_{|y|<h} dy / [2 pi sqrt(h²-|y|²)],
d=3: G_h(dy) = surface_measure_{|y|=h}(dy) / (4 pi h).
```

Let p_epsilon be the centered mass-one Gaussian with covariance epsilon I,
gamma_epsilon=p_epsilon*gamma, G_(h,eta)=p_eta*G_h, and G_(h,0)=G_h.
The input being tested is

```text
sup_z integral G_(h,eta)(dy) gamma_epsilon(y+z)
  <= M h^(1-alpha),   h>0, epsilon>0, eta>=0.                 (SP)
```

Constants are independent of h, z, epsilon and eta, but depend on c and
alpha. This is a supremum over spatial translations, not over time gaps.

| Covariance | Spatial maximum result | Intersection with requested range |
|---|---|---|
| d3 isotropic Riesz | Finite for 0<alpha<2; exact constant below for 1<alpha<2 | All 1<alpha<2-alpha0 |
| d2 isotropic Riesz | Finite exactly for 0<alpha<3/2, within the Riesz function range 0<alpha<2 | 1<alpha<min(3/2,2-alpha0) |
| General anisotropic homogeneous, d2 or d3 | Homogeneity/positivity alone do not imply (SP) for any fixed 1<alpha<2 | Counterexamples also satisfy alpha+alpha0<2 whenever alpha0<2-alpha |

Thus the d2 obstruction leaves a requested subrange only when alpha0<1/2.
At alpha0>=1/2 the requested strict threshold already keeps alpha<3/2.
Anisotropy is not itself a prohibition: for example any nonnegative covariance
bounded above by C|x|^(-alpha) inherits the corresponding Riesz bound by
Tonelli. No necessary-and-sufficient classification of all anisotropies is
claimed. The table gives exact scope for isotropic Riesz and a counterexample
to a universal extension.

The wave scaling G_h(h A)=h G_1(A) gives

```text
(G_h*gamma)(z) = c h^(1-alpha) F_d(z/h),
F_d(w) = integral G_1(dy) |y+w|^(-alpha).
```

Evenness permits either sign in the convolution. All integrals below are
nonnegative extended integrals, so Tonelli applies before finiteness is known.

## 2. First falsification tests

Do not infer a maximum at zero from radiality: wave measures are not radially
decreasing densities. In d3 the exact values are

```text
F_3(0)=1,
F_3(e_1)=2^(1-alpha)/(2-alpha)>1,       1<alpha<2.
```

In d2 the centered integral is finite for every alpha<2:

```text
F_2(0) = integral_0^1 r^(1-alpha)/sqrt(1-r²) dr
       = (1/2) B(1-alpha/2,1/2).
```

Nevertheless the boundary value is infinite for alpha>=3/2. A centered-only
test therefore misses the obstruction. Both tests use a single convolution;
no higher-order diagram or Holder bookkeeping is needed.

## 3. Dimension three: exact supremum for 1<alpha<2

For r=|z|>0, spherical coordinates about z give

```text
(G_h*gamma)(z)
 = (c h/2) integral_{-1}^1 (r²+h²+2rh u)^(-alpha/2) du
 = c [(r+h)^(2-alpha)-|r-h|^(2-alpha)] / [2r(2-alpha)].   (3.1)
```

At r=0 the continuous value is c h^(1-alpha); at r=h the integral is finite
exactly for alpha<2. Put q=2-alpha in (0,1) and scale h=1. For 0<r<1,

```text
F_3(r) = [(1+r)^q-(1-r)^q]/(2qr)
       = (1/(2r)) integral_{-r}^r (1+s)^(q-1) ds.
```

The function f(s)=(1+s)^(q-1) is strictly convex on (-1,infinity).
The integral of a convex function on [-r,r] is at most the integral of its
endpoint chord, hence

```text
F_3'(r) = [r(f(r)+f(-r))-integral_{-r}^r f(s) ds]/(2r²) >= 0.
```

Strict convexity makes this positive for 0<r<1. For r>1, every distance
sqrt(r²+1+2ru) is increasing in r, since r+u>0. Its negative alpha power
is decreasing; integration shows that F_3(r) is decreasing for r>1.
Formula (3.1) is continuous at r=1 because q>0. Consequently

```text
sup_z (G_h*gamma)(z)
 = c 2^(1-alpha)/(2-alpha) h^(1-alpha),
M_3 = c 2^(1-alpha)/(2-alpha).                              (3.2)
```

This is the optimal unsmoothed constant, and also the optimal constant if
one constant must work for every positive Gaussian smoothing width: the
approximate-identity limit at a maximizing shift recovers the unsmoothed
value (or use the Fatou argument in Section 5).

For completeness, finiteness for 0<alpha<=1 follows directly from (3.1)
and its finite limits at r=0,1 and infinity; the exact maximum calculation
above is asserted only for 1<alpha<2. In the remaining ordinary d3 Riesz
range 2<=alpha<3, the value at r=h diverges: locally its spherical integral
contains integral_0^delta rho^(1-alpha) d rho. Thus alpha<2 is the exact
positive-exponent threshold for a uniform d3 Riesz maximum.

## 4. Dimension two: finite constant below 3/2 and sharp failure above

### 4a. Uniform small-ball mass bound

For every center w in R² and 0<R<=1/4,

```text
G_1(B(w,R)) <= 2 R^(3/2).                                  (4.1)
```

Here is an elementary proof with all constants. Rotate w=(a,0), a>=0.
If a<1/2, the ball is contained in {|y|<3/4}, so its G_1 density is at
most 2/(pi sqrt(7)); its mass is at most 2R²/sqrt(7)<=2R^(3/2).
If a>=1/2, write y=(x,v). On the ball, |v|<=R and x>=a-R>=1/4.
For each v put L=sqrt(1-v²). The part in the unit disk has x<L, and

```text
1-x²-v² = (L-x)(L+x),
L+x >= sqrt(15/16)+1/4 > 1.
```

The horizontal slice has length at most 2R. Integrating (L-x)^(-1/2)
over any interval of that length lying below L gives at most 2sqrt(2R).
The v-range has length at most 2R. After multiplying by 1/(2pi), the mass
is at most (2sqrt(2)/pi)R^(3/2)<=2R^(3/2). Empty slices cause no issue.
This proves (4.1), uniformly even for centers outside the disk.

### 4b. Layer-cake estimate and explicit constant

For every t>0 and R_0>0,

```text
t^(-alpha) <= R_0^(-alpha)
               + alpha integral_0^{R_0} r^(-alpha-1) 1_{t<r} dr.
```

Apply this with t=|y+w|, R_0=1/4, integrate against the mass-one G_1,
and use (4.1). For 0<alpha<3/2 this yields

```text
sup_w F_2(w)
 <= 4^alpha + 2alpha integral_0^{1/4} r^(1/2-alpha) dr
  = 4^alpha + [2alpha/(3/2-alpha)] 4^(alpha-3/2).

M_2 = c {4^alpha + [2alpha/(3/2-alpha)] 4^(alpha-3/2)}.        (4.2)
```

This explicit constant is deliberately not optimized. It proves the full
uniform input in precisely the claimed subrange, after Section 5.

### 4c. Boundary obstruction, including alpha=3/2

Take h=1 and the shift z=-e_1, so the covariance singularity meets the
boundary at y=e_1. Use y=e_1+r(cos(theta),sin(theta)). Restrict to

```text
0<r<1/2,    2pi/3<=theta<=4pi/3.
```

On this wedge -1<=cos(theta)<=-1/2 and

```text
0 < 1-|y|² = -2r cos(theta)-r² <= 2r.
```

The Jacobian is r, and |y-e_1|=r. Consequently

```text
F_2(-e_1) >= [1/(3sqrt(2))] integral_0^{1/2} r^(1/2-alpha) dr.
                                                               (4.3)
```

The integral diverges logarithmically at alpha=3/2 and as a power for
alpha>3/2. Combined with (4.2), this proves the exact threshold. This is
an ordinary positive integral; oscillatory Fourier cancellation cannot
restore the missing supremum.

## 5. Gaussian smoothing: preservation and failure

For any nonnegative locally integrable covariance used above, Tonelli gives

```text
integral G_(h,eta)(dy) gamma_epsilon(y+z)
 = integral p_(epsilon+eta)(w) (G_h*gamma)(z-w) dw.           (5.1)
```

The sign of w can be reversed because the Gaussian is even. Thus a finite
unsmoothed supremum is preserved by mass-one averaging. Equations (3.2)
and (4.2) prove (SP), uniformly in both widths, including eta=0. This also
handles covariance widths such as 2epsilon or epsilon+epsilon': their
particular naming is immaterial. The estimate is independent of limit order;
any SPDE construction's prescribed eta-first order remains the root's task.

Conversely, Gaussian smoothing does not rescue a uniform constant in the
failure cases. At every point off the singular set, gamma_epsilon(x)
converges to gamma(x), by continuity and the Gaussian approximate identity.
These gamma are locally integrable and have at most tempered growth, so
the Gaussian integrals are finite at each positive width. The exceptional
singular set has zero G_1 measure for the fixed shifts used in Sections 4
and 6. Fatou therefore gives, with eta=0,

```text
liminf_{epsilon -> 0} integral G_1(dy) gamma_epsilon(y+z)
 >= integral G_1(dy) gamma(y+z) = infinity.                  (5.2)
```

For a formulation requiring eta>0, the same conclusion follows with
epsilon=eta tending to zero, because (5.1) is equivalently G_1 integrated
against gamma_(epsilon+eta). Thus the counterexamples refute uniformity,
not finiteness at a fixed positive regularization.

## 6. Function-valued anisotropic obstruction for every alpha>1

Choose 0<a,b<1 and define

```text
d2: gamma(x)=c|x_1|^(-a)|x_2|^(-b),
d3: gamma(x)=c|x_1|^(-a)|x_2|^(-b), independent of x_3,
alpha=a+b.
```

These are nonnegative locally integrable homogeneous tempered functions.
They are nonnegative definite: for 0<a<1,

```text
|u|^(-a) = [1/Gamma(a/2)] integral_0^infinity t^(a/2-1) exp(-t u²) dt
```

as a locally integrable distribution. Each Gaussian is positive definite;
positive mixtures and tensor products preserve this property. Constancy
in x_3 corresponds to a positive delta spectral factor in that coordinate.
They therefore meet the positivity and homogeneity assumptions used here;
they need not meet stronger assumptions such as being finite away from the
origin, which are not imposed in the project notes.

For d2, shift the covariance by -e_1, put u=1-y_1 and v=y_2. The disk is
0<u<2, |v|<sqrt(2u-u²). Direct integration, using v=sqrt(2u-u²)w, gives

```text
(G_1*gamma)(-e_1)
 = c B((1-b)/2,1/2)/(2pi)
      * integral_0^2 u^(-a) (2u-u²)^(-b/2) du.             (6.1)
```

The beta factor is the finite integral
integral_{-1}^1 |w|^(-b)(1-w²)^(-1/2) dw. At u=2 the integral is finite
because b/2<1. At u=0 it is finite if and only if

```text
a+b/2<1, equivalently 2a+b<2.
```

Equality gives logarithmic divergence; strict reversal gives power
divergence. In the finite case (6.1) equals

```text
c B((1-b)/2,1/2)/(2pi)
  * 2^(1-a-b) B(1-a-b/2,1-b/2).
```

For d3 the projection of G_1 on its first two coordinates is exactly the
d2 G_1: the upper and lower sphere graphs each have surface Jacobian
(1-|y|²)^(-1/2), and their sum divided by 4pi is the d2 density. Since
gamma ignores the third coordinate, its convolution at (-1,0,0) equals
(6.1). Thus the same obstruction works in both dimensions.

For EVERY prescribed alpha in (1,2), choose explicitly

```text
a = [1+max(2-alpha,alpha-1)]/2,    b=alpha-a.
```

Then 0<a,b<1, a+b=alpha, and a>2-alpha, whence 2a+b=alpha+a>2.
For example alpha=1.2, a=0.9, b=0.3 gives 2a+b=2.1. This refutes
the universal high-alpha spatial maximum even where d2 isotropic Riesz
passes. Equation (5.2) establishes failure uniform in Gaussian smoothing.
The condition 2a+b<2 above characterizes this particular pole integral,
not a full supremum criterion for all shifts of product covariances.

The distributional example in the earlier transfer note can also be made
precise without multiplying a delta at a tangent pole. In d2 or d3 take
gamma=delta_0(x_1)|x_2|^(-b), 0<b<1, with independence of x_3 in d3.
For a transverse shift -r e_1, 0<r<1, the projected disk calculation gives

```text
(G_1*gamma)(-r e_1)
 = B((1-b)/2,1/2)/(2pi) * (1-r²)^(-b/2).
```

This tends to infinity as r increases to 1. This last observation is
supplementary: the ordinary function example already proves the needed
no-go, including Gaussian smoothing, without distributional restriction
issues at tangency.

## 7. Local primary-source search and originality boundary

This was a bounded local search for the convolution input, not the root's
broader literature gate. Search terms included Riesz, convolution, maximum,
shifted suprema and spherical kernels. Primary source text inspected:

- `sources/llm_pack/chen_hu-25-hyperbolic.tex` and
  `sources/llm_pack/chen-25-time-dependency.tex`: no directly matching
  uniform translated single-wave Riesz estimate was identified in this
  search. The latter is superseded v1 under `sources/SOURCE-MANIFEST.md`;
  no author-version theorem is imported from it here.
- `sources/llm_pack/balan_conus-16-intermittency.tex` and
  `sources/llm_pack/chen_deya_ea-23-hyperbolic.tex`: related moment and
  convolution/Strichartz material, but no matching input located.
- `../SPDEForge/sources/balan-22-stratonovich/Stratonovich-wave.tex`,
  condition `C-cond` and `sup-ineq` near lines 182--197, homogeneity
  discussion near lines 226--230, and shifted Fourier estimates near
  lines 840, 898--899, 946--954. These use the absolute spectral envelope
  with K_mu=integral(1+|xi|²)^(-1/2)mu(dxi); the source explicitly restricts
  homogeneous alpha to (0,1) for this condition. It does not supply the
  present high-alpha physical-space maximum. The already-pinned project
  report `reviews/2026-10-27-round3/recon/balan-contraction-input.md`
  agrees with that distinction; its full trace argument was not duplicated.
- `../SPDEForge/sources/dalang_sanz-sole-09-holder-sobolev/dalang_sanz-sole-09-holder-sobolev.tex`:
  related Riesz-potential estimates, notably two-wave expressions and
  squared Fourier multipliers (e.g. near lines 2676, 2707--2714). These
  are not interchangeable with the single-wave translated supremum.
  A limited search of the local Dalang--Sanz-Sole book source did not
  identify the exact input either.

All sibling access was read-only. No claim that these elementary sphere
potential calculations are original, and no claim of an exhaustive negative
literature result. The proof here stands independently of source theorem
numbering; the root should retain its separate literature gate.

## 8. Reproducible small diagnostic

The following Python-standard-library diagnostic was executed. Numerical
quadrature is only a normalization check, never proof of convergence or
divergence. The boundary wedge diagnostic evaluates the exact lower bound
(4.3) with an inner cutoff. Constants below use c=h=1.

```python
import math
N = 200000
for alpha in (1.2, 1.5, 1.8):
    q = 2-alpha
    error = 0.0
    for r in (.25, .75, 1.25, 2.0):
        numeric = sum((r*r+1+2*r*(-1+(i+.5)*2/N))**(-alpha/2)
                      for i in range(N))/N
        exact = ((r+1)**q-abs(r-1)**q)/(2*r*q)
        error = max(error, abs(numeric-exact))
    print(alpha, 2**(1-alpha)/(2-alpha), error)
for alpha in (1.25, 1.5, 1.75):
    values = []
    for eps in (1e-2, 1e-4, 1e-6):
        b = 1.5-alpha
        v = math.log(.5/eps) if b == 0 else (.5**b-eps**b)/b
        values.append(v/(3*math.sqrt(2)))
    print(alpha, values)
for alpha in (1.1, 1.2, 1.5, 1.9):
    a = (1+max(2-alpha, alpha-1))/2
    b = alpha-a
    print(alpha, a, b, 2*a+b)
```

Observed d3 results:

| alpha | Exact M_3/c | Maximum absolute quadrature discrepancy |
|---|---:|---:|
| 1.2 | 1.088188204 | 2.637e-10 |
| 1.5 | 1.414213562 | 4.998e-10 |
| 1.8 | 2.871745887 | 9.092e-10 |

Observed d2 wedge lower bounds:

| alpha | cutoff 1e-2 | cutoff 1e-4 | cutoff 1e-6 |
|---|---:|---:|---:|
| 1.25 | 0.494662346 | 0.698523839 | 0.762990504 |
| 1.5 | 0.922072665 | 2.007521687 | 3.092970710 |
| 1.75 | 1.860228750 | 8.306895195 | 28.693044480 |

The product example generated (a,b,2a+b)=(.95,.15,2.05), (.9,.3,2.1),
(.75,.75,2.25), (.95,.95,2.85) at alpha=1.1,1.2,1.5,1.9 respectively.
The exact inequalities in Sections 4 and 6 are the actual falsification.

## 9. Handoff and proof boundaries

The root may use M_3 from (3.2) in its conditional spatial-input theorem
for the full requested isotropic d3 range, and M_2 from (4.2) only for
the stated d2 subrange. All closing-gap powers remain h^(1-alpha), with
negative exponent for alpha>1. There is no uniform bound over h approaching
zero; the root's separate time-integration argument must handle those powers.

The failed d2 and anisotropic estimates are failures of (SP), not failures
of the Stratonovich second-moment theorem, existence, finite-order time
integrability, or target asymptotics. A divergent supremum at a tangential
shift need not survive integration in the remaining spatial/time variables.
No lower moment-growth conclusion follows from these counterexamples.

Holder combinatorics, summation of diagrams, regularized SPDE limit passages,
sharp asymptotic constants, novelty and formal verification are outside this
worker's proof claim. The root's `reviews/2026-10-27-round4/recon/holder-calculation.md`
is the separate Holder handoff, not an input validated by this report.
The current manuscript's accepted alpha<=1 scope is unchanged.
