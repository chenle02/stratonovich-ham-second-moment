# Order-four crossing-pair merge diagnostic

Date: 2026-10-28 UTC. Status: **PARTIAL — naive unweighted spatial merge fails**.
This is an author-side dependency diagnostic, not an accepted new theorem,
all-order estimate, numerical result, or claim against the moment conjecture.
No manuscript or sibling files were changed.

Skills applied: falsification-first-differentiated-routes and
numerics-gate-before-proof-investment. The disputed step is a literal removal
of a variable-dependent factor. Exact inspection settles that question, so no
singular Monte Carlo estimate or clipping experiment was run.

## 1. The exact diagram

Use the root-forward conventions of the existing notes, E:mixed-diagram:
s0=0, y0=0, with the first chain empty. Let d=2,
gamma(v)=c|v|^(-alpha), c>0, 0<alpha0<1/2,
3/2<=alpha<2-alpha0. Write

  G_h(v) = 1_(|v|<h) / (2 pi sqrt(h^2-|v|^2)).

The contribution of split (0,4) and D={(1,3),(2,4)} is exactly

  J(t) = c^2 integral_(0<s1<s2<s3<s4<t) ds1 ds2 ds3 ds4
    integral_(R^2)^4 dy1 dy2 dy3 dy4
      G_s1(y1)
      G_(s2-s1)(y2-y1)
      G_(s3-s2)(y3-y2)
      G_(s4-s3)(y4-y3)
      (s3-s1)^(-alpha0) (s4-s2)^(-alpha0)
      |y3-y1|^(-alpha) |y4-y2|^(-alpha).

There is no 4!, 2!, extra pairing count, or terminal Green factor: this is
one pairing in one ordered-chain split, not the full fourth-order coefficient.
The unused terminal gap only restricts s4<t. This convention follows the
already recorded reversed/root-forward representation, not the original
terminal-to-(t,x) convention applied a second time.

## 2. Merge vertex2 while fixing its neighbors and remote partner

Put a=s1, b=s3, T=s4 and x=y1, z=y3, w=y4, so 0<a<b<T<t.
The exact inner merge is

  W(a,b,T;x,z,w)
    = c integral_a^b dv (T-v)^(-alpha0)
        integral_R^2 dy G_(v-a)(y-x) G_(b-v)(z-y) |w-y|^(-alpha).

Thus Tonelli gives the exact nonnegative representation

  J(t) = c integral_(0<a<b<T<t) da db dT
    integral_(R^2)^3 dx dz dw
      G_a(x) G_(T-b)(w-z)
      (b-a)^(-alpha0) |z-x|^(-alpha)
      W(a,b,T;x,z,w).

The two factors for edge(1,3) are outside the merge exactly. The two factors
for edge(2,4) remain inside because v,y are precisely vertex2's coordinates.
The vertex4 Green factor is outside the merge but still constrains w and T.

## 3. What can and cannot be pulled outside

| Factor | Exact pullout? | Legitimate bound / obstruction |
|---|---|---|
| (b-a)^(-alpha0), c|z-x|^(-alpha) | Yes | Neither contains v or y. |
| G_a(x), G_(T-b)(w-z) | Yes | They do not contain the merged vertex2. |
| (T-v)^(-alpha0) | No, not as an equality | Since a<v<b<T, it is at most (T-b)^(-alpha0). This is a valid upper pullout, with a singular constant as the remaining gap T-b tends to zero. |
| c|w-y|^(-alpha) | No | It varies with y and has no finite uniform essential supremum on all admissible merge lenses. |

The spatial obstruction is not merely the isolated point y=w. For an explicit
interior configuration take t=5, a=1, b=3, T=4, x=(0,0), z=(1/2,0),
w=(1/4,0), and v near2. Then y=w lies strictly inside both wave supports,
and |w-z|<T-b as required by the outer Green factor. The Riesz factor has
infinite essential supremum in every neighborhood of w. This persists for an
open neighborhood of the fixed parameters and remote point; replacing it by
its supremum is not a finite estimate. The actual y-integral is a different
question: its isolated Riesz singularity is locally integrable for alpha<2.
No divergence of W or J is inferred from this essential-supremum failure.

For individually fixed configurations with remote point w at positive distance
d from the entire spatial merge support, c d^(-alpha) is an upper bound.
The diagram has no standing positive-separation assumption, so this does not
supply a usable global pullout. Nor may one replace |w-y|^(-alpha) by
|w-x|^(-alpha) or |w-z|^(-alpha) without a separately proved inequality:
those quantities are finite in the displayed interior configuration while
the former is unbounded as y approaches w.

Conclusion: BNZ's unweighted two-wave estimate cannot be substituted directly
for W. The temporal factor admits a gap-dependent upper bound; the spatial
factor is the unresolved weighted-convolution obligation.

## 4. Exact weighted object and a concrete sufficient inequality to test

Translation invariance reduces the object to h=b-a>0, tau=T-b>0,
Z=z-x, W=w-x:

  Wtilde_(h,tau)(Z,W)
    = c integral_0^h du (h+tau-u)^(-alpha0)
        integral_R^2 dy G_u(y) G_(h-u)(Z-y) |W-y|^(-alpha).

Its scaling is

  Wtilde_(lambda h,lambda tau)(lambda Z,lambda W)
    = lambda^(1-alpha-alpha0) Wtilde_(h,tau)(Z,W).

This is obtained by the displayed changes u=lambda v, y=lambda Y and the
wave-density scaling G_(lambda h)(lambda y)=lambda^(-1)G_h(y); it is a
normalization check on the exact diagnostic, not the missing upper bound.

One explicit *sufficient candidate*, not a necessary condition for the desired
moment theorem and not claimed true, is: for a suitable fixed q in (1/2,1),
there exists C_(alpha,q)<infinity such that for every h>0 and Z,W in R^2,

  integral_0^h du integral_R^2 dy
    G_u(y) G_(h-u)(Z-y) |W-y|^(-alpha)
      <= C_(alpha,q) h^(2q-alpha) G_h(Z)^(2q-1).                 (WC)

The support/boundary convention is the usual almost-everywhere kernel one;
it must be specified in any eventual theorem. The constant must be uniform in
both displacements and in h. A regularized version would also need uniformity
in every covariance smoothing width before a limit argument could use it.
For the exact unsmoothed diagnostic, (WC) would imply the precise clock-aware
bound

  W(a,b,T;x,z,w)
    <= c C_(alpha,q) (T-b)^(-alpha0)
         (b-a)^(2q-alpha) G_(b-a)(z-x)^(2q-1).                 (WC-time)

Every factor and parameter is retained: c is explicit, alpha0 remains in the
remote-gap cost, q is fixed, and the spatial constant may depend on alpha,q
but not on x,z,w,a,b,T. Both sides of (WC-time) have scaling degree
1-alpha-alpha0. The allowed q range for (WC), if any, is an OPEN question;
BNZ's q in (1/2,1) does not automatically validate this weighted version.
In particular, no wave-front, unequal-gap, or uniform-remote-point check of
(WC) has been passed by this memo.

The less restrictive route would keep a nonconstant envelope B_(h,tau)(Z,W)
for Wtilde and prove its integrability against the *remaining* measure
G_a(x)G_tau(w-z)h^(-alpha0)c|z-x|^(-alpha) da db dT dx dz dw.
This may succeed even if the uniform-W candidate (WC) fails. Merely naming B
as Wtilde itself is an identity, not an advance. A future proposal must state
an independently usable B and its integrability/constant budget. This memo
stops before such a construction.

## 5. Falsification record and stop boundary

| Test | Result |
|---|---|
| Exact factorization of edge(2,4) outside vertex2 merge | FAIL: both coordinates occur in the edge. |
| Finite temporal upper pullout for fixed positive remote gap | PASS: cost (T-b)^(-alpha0), not a time-independent constant. |
| Uniform finite spatial-supremum pullout | FAIL: explicit interior lens configuration above. |
| Applicability of unweighted BNZ lemma directly to weighted W | FAIL: object mismatch. |
| Weighted inequality (WC) | OPEN: neither proved nor numerically tested. |
| Consequence for full second-moment target | NONE: no moment no-go asserted. |

The naive direct substitution is falsified at a single legitimate Stratonovich
order-four diagram. The broader integrated-wave route survives only as an
explicit weighted estimate to be tested. No all-order proof or extension of
this diagnostic is undertaken.

Sources: notes E:mixed-diagram and P:mixed; the source audit in this directory;
BNZ v2 Lemma4.3 (4.7), p20; Balan (2022) AppendixC pp2687–2688. These source
references do not assert that (WC) is printed in either paper.
