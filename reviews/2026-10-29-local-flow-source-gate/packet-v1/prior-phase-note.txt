# The first Gaussian response in a physical phase norm

Status: accepted scoped analytic/source/type/application review, eight
checks HIGH at source0ae116c. See
reviews/2026-10-29-phase-response/adjudication.md. These are first-response regularity/operator tests for the direct
Stratonovich lower-bound route. They do not construct an all-order random
flow, its remainder, an event lower bound or a sharp moment constant.

Fix0<a<1 and a nonzero original homogeneous covariance Gamma of degree
alpha, with alpha+a<2. Its spectral measure is mu. The temporal covariance
here is RAW |u-v|^-a, without the factor H(2H-1). Let t>0 be fixed and put
<r>=(1+r^2)^(1/2). We use the unitary spatial Fourier transform and the
spectral convention Gamma(x)=integral exp(i xi.x)mu(dxi).

## 1. A direct combined temporal calculation

For r>=0 define S(r),C(r) as the temporal quadratic norms of sin(ru) and
cos(ru) on[0,t], respectively, with kernel |u-v|^-a. Both are nonnegative.
Their sum is exactly

    J(r)=S(r)+C(r)
        =2 integral_0^t (t-v)v^(-a)cos(rv)dv.                (J)

This sum, rather than a velocity criterion guessed from a position theorem,
is the useful phase calculation. Define positive finite constants

    A_a=2/Gamma(a) integral_0^infinity z^a/(1+z^2)dz,
    B_a=4/Gamma(a) integral_0^infinity z^(a-1)/(1+z^2)dz.

For every r>0,

    |J(r)-A_a t r^(a-1)| <= B_a r^(a-2).                   (E)

To prove this, insert v^-a=Gamma(a)^(-1) integral_0^infinity
exp(-lambda v)lambda^(a-1)dlambda in(J). Absolute integrability follows
from integral_0^t(t-v)v^-a dv<infinity, so complex Fubini is legitimate.
Writing z=lambda-ir gives

    J(r)=2/Gamma(a) Re integral_0^infinity lambda^(a-1)
           [t/z-(1-exp(-zt))/z^2]dlambda.                  (F)

The real part of t/z is t lambda/(lambda^2+r^2); its integral is exactly
A_a t r^(a-1). The remaining term is bounded by
4/Gamma(a) integral lambda^(a-1)/(lambda^2+r^2)dlambda
=B_a r^(a-2). Each separated integral is absolutely convergent for0<a<1.
This proves(E). In particular, for r>=2B_a/(A_a t),

    (A_a t/2)r^(a-1) <= J(r) <= (3A_a t/2)r^(a-1).         (W)

The constants can equivalently be written
A_a=pi/[Gamma(a)cos(pi a/2)], B_a=2pi/[Gamma(a)sin(pi a/2)], by the Euler
beta integral after z^2 substitution. These evaluations are not needed for
the bounds. At r=0, J(0)=2t^(2-a)/[(1-a)(2-a)]. The complex sesquilinear extension of the temporal Fourier norm
identity in the held Balan--Tudor AppendixA, equation lemmaA1, gives strict
positivity of J(r) at each r: apply it to exp(iru)1_[0,t]. Its Fourier
transform is not zero, and the weight |tau|^(a-1) is positive a.e. Continuity
follows by dominated convergence in(J). Set r_0=2B_a/(A_a t)>0.
Compactness on[0,r_0] and(W) therefore yield

    J(r) is comparable to <r>^(a-1),  r>=0,                (U)

with positive constants depending on a,t. Dividing the source identity by
its alpha_H=H(2H-1), H=1-a/2, matches our raw normalization.

## 2. The localized position-velocity phase threshold

Let W^L be the orthogonal SPATIAL spectral cutoff |xi|<=L of the common
Gaussian noise. This is a linear Gaussian probe; its physical covariance
need not be pointwise nonnegative. No higher-order Wick domination is used.
Define its first position and velocity responses by the deterministic
Gaussian integrals

    Z_L(t)=integral_0^t G_(t-u) W^L(du),
    Y_L(t)=integral_0^t partial_t G_(t-u) W^L(du).           (P)

At finite L these are well defined. The second is the mean-square time
derivative of the first: the sine kernel has derivative cosine and zero
boundary value; difference quotients converge in the temporal Gaussian
Hilbert norm, using compact spatial spectrum and the integrable time kernel.
In the limit Y may be a spatial distribution rather than a pointwise field.

For a nonzero real chi in C_c^infinity(R^d) and any real s, put

    Q_s(L)=E[||chi Z_L(t)||_(H^s)^2
               +||chi Y_L(t)||_(H^(s-1))^2].              (Q)

Then

    sup_L Q_s(L)<infinity iff 2s+alpha+a<3.                 (T)

In the finite case the pair converges in L2 of that local phase space. At
the equality Q_s(L) is comparable to log L for large L; above it Q_s(L) is
comparable to L^(2s+alpha+a-3). These are squared-norm growth rates.

Here is a proof retaining localization and singular spectral measures.
The isometry in the held Balan--Tudor Gaussian Hilbert construction, with
the raw time normalization, gives position spectral variance S(r)/r^2 and
velocity variance C(r), r=|xi|. The position value at r=0 is read by continuity.
For any real v,

    w_(chi,v)(xi)=||chi exp(i xi.x)||_(H^v)^2
       =integral <xi+zeta>^(2v)|chi_hat(zeta)|^2 dzeta
       is comparable to <xi>^(2v).                        (K)

The upper bound follows from Peetre's inequality and rapid Fourier decay
of chi. For the lower bound restrict zeta to a fixed ball on which the
Fourier L2 mass is positive, and use the reverse Peetre bound. Constants
are positive and independent of xi. Thus Q_s(L) is comparable to

    integral_(|xi|<=L) [<r>^(2s)S(r)/r^2
                         +<r>^(2s-2)C(r)]mu(dxi).         (I)

For r>=1 the bracket lies between <r>^(2s-2)J(r) and twice that quantity.
This uses nonnegativity of EACH temporal quadratic norm, not a pointwise
sign of the oscillating trigonometric factors. Low frequencies are bounded:
sin(ru)/r is bounded by t and cosine by one, and mu has finite compact mass.
By(U), the high-frequency weight is comparable to r^(2s+a-3).

Fourier homogeneity gives mu(cA)=c^alpha mu(A), also when Gamma has no
angular density. Indeed Fourier transforming the homogeneous covariance
distribution and changing variables in its test functions gives this
measure scaling. Since alpha>0, mu has no atom at zero. Some, hence every,
dyadic annulus has finite positive mass when Gamma is nonzero. For any real
beta, the integral of r^beta on the n-th dyadic annulus is its unit-annulus
integral times2^(n(beta+alpha)). Summing this geometric series proves(T)
and the logarithmic/power cutoff rates. Differences of cutoffs are orthogonal
Gaussian spectral tails; the same finite integral makes them Cauchy in L2
of the local Hilbert phase. This proves the assertion for all original d1--3
covariances without an isotropic-density restriction. Zero covariance is a
trivial exception and is excluded from the equivalence.

For the usual energy phase s=1, the criterion is alpha+a<1, not alpha+a<2.
Its squared cutoff norm grows as log L at alpha+a=1 and as L^(alpha+a-1)
above. This rejects a cutoff-uniform FIRST-RESPONSE energy estimate in the
missing range. It does not, by itself, assert phase failure of the full
solution at each nonzero amplitude or refute an estimate in another norm.

Writing b=alpha+a in(0,2), a concrete rougher choice is

    s_0=1-b/4,  1/2<s_0<1,
    2s_0+b<3,  2s_0+b-3=(b-2)/2<0.                       (C)

In d1, H^(s_0) admits bounded local point evaluation, and the free wave
group preserves H^(s_0) x H^(s_0-1). For the latter, use its Fourier matrix
with entries cos(tr),sin(tr)/r,-r sin(tr),cos(tr): the inhomogeneous weights
bound every entry uniformly on compact time intervals, including r=0.
This is only a feasible FIRST-response phase, not invariance under the
full random equation. In d2, a local Hilbert Sobolev phase that also embeds
pointwise requires alpha+a<1 to have s>d/2 and(T). In d3 no such s exists
for positive alpha+a. That is a limitation of this Sobolev point-evaluation
strategy, not nonexistence of the known random field or of other norms.

## 3. A temporal modulation bound for the operator test

If f is C1 on[0,t] with bounded ||f||_infinity+||f'||_L1, the same temporal
Fourier identity gives

    ||f(u)cos(ru)||_a^2+||f(u)sin(ru)||_a^2
       <=C_(a,t,f) <r>^(a-1),                             (B)

where the constant can be uniform on a bounded C1 set. To see this, the
Fourier transform of f1_[0,t] is bounded by C min(1,|tau|^-1), using one
integration by parts including its two endpoint values. Multiplication by
exp(iru) shifts this transform. It suffices to bound
integral |tau|^(a-1)/(1+|tau-r|^2)dtau by C_a<r>^(a-1). For |r|>=2 split
|tau-r|<=|r|/2, then |tau|<=2|r| in the complement, then |tau|>2|r|.
The three bounds are O(|r|^(a-1)), O(|r|^(a-2)) and O(|r|^(a-2)),
respectively. Bounded r follows by local integrability at tau=0 and the
integrable tail |tau|^(a-3). For the real factors used here, symmetry gives the exact identity
||f cos(ru)||_a^2+||f sin(ru)||_a^2=||f exp(iru)||_a^2. For complex f, use
the half-sum of the two opposite modulation norms. Output factors at t-u
are a trigonometric rotation, or a constant unimodular phase followed by
negative frequency. These observations prove(B) without an unnecessary
triangle estimate for the real sum.

## 4. The localized first response OPERATOR in d1

Now take d1, so0<alpha<=1 and0<a<1. In d1 a nonzero even homogeneous
spectral measure of degree alpha has density c|q|^(alpha-1)dq, c>0; the
white endpoint has alpha1. This follows by scaling the distribution
function on each half-line and differentiating r^alpha; there is no atom
at zero. Let E_s=H^s(R) x H^(s-1)(R), with1/2<s<=1. Let S(t) be the FREE
wave phase group and define, initially for Schwartz phase data v,

    N_L(t)v=diag(chi,chi) integral_0^t
        S(t-u) [0; W^L(du) (S(u)v)_1].                    (O)

This is the zero-background first Gaussian response, not an assumed random
flow. It extends to a Gaussian Hilbert--Schmidt operator E_s->E_s with a
cutoff-uniform L2 bound and an L2 Hilbert--Schmidt limit iff

    2s+alpha+a<3.                                         (H)

Under the original alpha+a<2, the choice(C) therefore PASSES the localized
first-response operator test for the entire d1 range, including white space.
It also has all finite Gaussian Lp moments uniformly in L. No all-order
remainder or nonzero-background operator estimate is asserted.

We give the operator proof, since(Q) alone would not justify it. For input
frequency k and noise frequency q let r=k+q. The output carrier after chi
is chi_hat(p-r). The temporal matrix before phase weights is the outer product

    [sin((t-u)|r|)/|r|; cos((t-u)|r|)]
       [cos(u|k|), sin(u|k|)/|k|].                        (D)

At finite noise cutoff, the Gaussian Hilbert isometry and spatial Plancherel
give the expected squared Hilbert--Schmidt norm as1/(2pi) times the
integral of the four temporal quadratic norms against dk mu(dq). This fixed
prefactor comes from the unitary inverse transform of the input data and
is retained in the comparison constants. The output weights are precisely
w_(chi,s)(r),w_(chi,s-1)(r), and input weights <k>^(-2s),<k>^(2-2s).
This is justified first for bounded input/output Fourier windows. Those
norms increase to the full squared Hilbert--Schmidt norm; the estimates
below make the limit finite at fixed L. Thus no full flow or bounded operator
is assumed in order to define N_L.

In the region |r|,|k|>=1, (K) makes the weighted integrand comparable to

    <r>^(2s-2)<k>^(-2s)
       [J(|q|)+J(|2k+q|)]/2.                              (G)

For completeness, summing the FOUR unweighted component Gram factors at
times u,v gives cos(|r|(u-v))cos(|k|(u-v)). Product-to-sum gives the two
J terms in(G), since the unordered absolute frequencies are |q| and |2k+q|.
The high-mode normalization factors <r>/|r| and <k>/|k| lie in[1,sqrt2].
Each individual temporal quadratic norm is nonnegative, so these bounded
constant factors preserve two-sided comparability after summation. This
does not take absolute values of the oscillating time integrand.

By(U), it remains to integrate, for j=1,2,

    I_1=integral dk dq <k+q>^(2s-2)<k>^(-2s)
                     |q|^(alpha-1)<q>^(a-1),
    I_2=integral dk dq <k+q>^(2s-2)<k>^(-2s)
                     |q|^(alpha-1)<2k+q>^(a-1).            (A)

For bounded q the k tails are integrable (at worst k^-2 in I_1); the q
singularity is integrable since alpha>0. For |q|>=2 use evenness to assume
q>0 and split into four sectors:

- |k|<=q/4: |k+q| and |2k+q| are comparable to q. Since2s>1, integrating
  <k>^(-2s) is bounded. After the q weight both tails are bounded by a
  constant times q^(2s+alpha+a-4).
- |k+q|<=q/4: |k| and |2k+q| are comparable to q. The integral of
  <k+q>^(2s-2) over this interval is O(q^(2s-1)), because2s-2>-1.
  Both resulting tails are O(q^(alpha+a-3)).
- Both previous inequalities fail and |k|<=2q: the two phase weights
  multiply to at most Cq^-2. For I_1 the interval length is O(q); for I_2
  the integral of <2k+q>^(a-1) is O(q^a). Again the tails are
  O(q^(alpha+a-3)).
- |k|>2q: |k+q| and |2k+q| are comparable to |k|. The k tails are
  O(q^-1) in I_1 before its temporal factor, and O(q^(a-2)) in I_2.
  Both produce O(q^(alpha+a-3)).

These bounds are integrable when2s+alpha+a<3; it also implies alpha+a<2
since s>1/2. This proves the high/high upper bound. If |r|<=1 but |k|
is large, (B), with uniformly bounded low-frequency C1 factors from(D),
bounds that sector by integral <k>^(alpha+a-2-2s)dk, finite since2s>1>
alpha+a-1. If |k|<=1 and |r| is large the corresponding tail is
integral <r>^(2s+alpha+a-4)dr, finite under(H). Both modes bounded is finite
by local integrability of |q|^(alpha-1). This completes all frequency sectors.

For necessity, restrict input k to[1,2] and q sufficiently large. The exact
four-component norm and(U) give a positive lower bound times
integral q^(2s+alpha+a-4)dq. It diverges at and above equality in(H).
The same estimates show logarithmic cutoff growth at equality and power
L^(2s+alpha+a-3) above, within alpha+a<2. Orthogonal noise tails show L2
Hilbert--Schmidt convergence in the finite case. The Gaussian isometry
construction makes the limit a Gaussian Hilbert--Schmidt-valued variable.
Choose its measurable Hilbert--Schmidt representative for each cutoff and
the limit. On a countable dense Schwartz set, the isometry identifies its
values with(O); intersecting those countably many full-measure sets gives
one operator version agreeing there. Continuity extends that version to
E_s. Agreement in L2 for each deterministic Schwartz input follows by the
same isometry. No simultaneous versions of uncountably many formal input
integrals are assumed.

All finite Gaussian Lp bounds follow without independence of components:
for any finite orthonormal expansion in that Hilbert space, Minkowski in
L^(p/2), p>=2, bounds its squared Lp norm by the scalar normal p-moment
constant times the sum of component variances. Monotone convergence passes
to the full norm; smaller positive p follow from L2. Finally operator norm
is bounded by Hilbert--Schmidt norm. This proves the stated first-response
operator assertion.

## 5. A balanced endpoint and the actual moment observable

The endpoint phase E_(1/2)=H^(1/2) x H^(-1/2) also passes the d1
first-response operator test throughout alpha+a<2. To prove this, repeat
Section4 with s=1/2. In the first two bullet sectors of Section4, the formerly bounded/power k or r
integrals are now O(log(2+q)); the high-q tails are bounded by

    C q^(alpha+a-3)log(2+q).                               (V)

The other sectors have the same or smaller bound. The low/high and high/low
tails are q^(alpha+a-3), and bounded modes stay finite. These are integrable
when alpha+a<2. The same Gaussian isometry and orthogonal-tail argument
therefore give the cutoff-uniform Hilbert--Schmidt limit and all finite Lp
bounds. No claim about logarithmic cutoff rates at the excluded alpha+a=2
endpoint is made here.

Point evaluation is not bounded on H^(1/2), but the ORIGINAL moment target
can use a smooth average. Let rho>=0 be smooth, compactly supported and of
unit mass. For the canonical original solution and any T,R>0,

    E|integral rho(x)u(T,Rx)dx|^2 <= E|u(T,0)|^2.            (M)

Here the average exists as an L2(Omega)-valued Bochner integral. At positive
noise widths each fixed-order terminal coefficient is spatially L2-continuous,
by Gaussian mean-square continuity and integration against the fixed finite
terminal Green measure. The errors in the joint fixed-order L2 limits are
independent of the terminal spatial point by stationarity of the entire
common-width Gaussian family. Thus the canonical fixed-order limits are
L2-continuous in x. Applying the named prior positive mixed expansion at an
amplified covariance gives uniform-in-x geometric norm tails, since every
coefficient norm and the amplified second moment are stationary. Consequently
u(T,x) is L2-continuous, with its L2 norm independent of x. More explicitly,
the amplified input is Prop P:mixed at c^2 Gamma, c>1, which still satisfies
H:homog. Degree-n homogeneity makes its diagonal c^(2n)E X_n^2 at most
B_c=E|u_c(T,0)|^2; hence ||X_n(T,x)||_2<=sqrt(B_c)c^(-n), uniformly in x.
This uses no uniform-regularization tail hypothesis. The Bochner
triangle inequality gives
||integral rho(x)u(T,Rx)dx||_2 <= integral rho(x)||u(T,Rx)||_2dx
=||u(T,0)||_2, proving(M). No positivity of the random solution is assumed.
This is a Bochner L2 statement; no simultaneous pointwise version is needed.

Here V_delta(t,x) denotes u(Tt,Rx), with delta=T^(-kappa),R=Tdelta and
kappa=(4-alpha-a)/(3-alpha), as in notes/direct-event-calibration.md.
Inequality(M) itself holds for every T,R>0 independently of that rescaling.
For this V_delta, the average is a delta-dependent physical average of
unit L1 mass, so there is NO lost factor R^d. Its fixed rescaled test rho
defines a bounded linear functional on every local H^s, by Sobolev duality
with the smooth test. Thus a direct event lower bound for the actual squared
average would lower-bound the original POINTsecond moment. This does not
replace the target by an averaged-moment target. The phase embeddings noted
in Section2 limit a point-evaluation strategy, not this averaged observable.
The full random flow and the required averaged event growth remain unproved.

The proved candidate tests can be compared as follows; the operator column
is only d1 and every entry concerns the FIRST response.

| Phase | Local field criterion | d1 localized operator | Moment observable |
| --- | --- | --- | --- |
| H1 x L2 | alpha+a<1 | Same strict criterion | Point in d1, or average |
| H^(s_0) x H^(s_0-1) | alpha+a<2 for the choice(C) | Cutoff-uniform HS | Point in d1, or average |
| H^(1/2) x H^(-1/2) | alpha+a<2 | Cutoff-uniform HS, endpoint log sectors | Smooth average via(M) |

## 6. Endpoint and scope calibrations

The dynamic criterion is for FIXED a>0. At a=0 the temporal kernel is one
and direct integration instead gives

    J_0(r)=2(1-cos(rt))/r^2.                                (Z)

In particular the static first-response energy phase is finite for alpha<2,
using J_0<=4/r^2 and homogeneous spectral tails. There is no contradiction:
A_a tends to zero and the asymptotic window in(W) is not uniform as a
decreases to zero. Do not insert a=0 into the fixed-positive-a criterion.
No Gamma(0) is used. This is a phase calibration, not a changed static
moment exponent or a new moment constant. The accepted Jensen and other
moment calibrations remain unchanged.

The first response comes from the ordinary Stratonovich expansion under
data(1,0); at this order it is the same additive Gaussian integral. No
Skorohod second-moment or large-time result is developed here. Its local
energy failure rules out a cutoff-uniform estimate that also bounds this
first response. It does not, without further hypotheses, prove failure of
the full nonlinear-in-noise solution in that phase at each amplitude.

The localized d1 Hilbert--Schmidt pass is a necessary feasibility step,
not an all-order transfer map, a remainder bound near a deterministic
Cameron--Martin profile or an event with the required probability cost.
Global initial data1 are not in E_s; for a first-response test on a compact
observation set, smooth initial data equal to1 on its entire t-backward
cone give the same response there by finite propagation of the FREE group.
This does not supply the missing full random-flow localization argument.
Dimensions2/3 and point evaluation need their own operator/observable test.
The original all-covariance sharp target remains unchanged and open.
