# Weighted two-wave boundary probe

Date: 2026-10-28 UTC. Status: **PARTIAL — q < alpha-1 falsified; remaining
q range open**. This is an author-side bounded diagnostic, pending independent
review. It is not an accepted manuscript theorem or a no-go for moment growth.
No manuscript, sibling, source PDF, registry or git changes were made.

Skills applied: falsification-first-differentiated-routes and
numerics-gate-before-proof-investment. Exact positive-measure bounds settle
this restricted falsification, so no singular Monte Carlo or clipping was used.
The inherited source audit's REFRAME permits this bounded test, not an all-order
proof wave or a novelty claim.

## Exact object and candidate

For the two-dimensional wave density

  G_h(y) = 1_(|y|<h) / (2 pi sqrt(h^2-|y|^2)),

write

  I_alpha(h;Z,W) = integral_0^h du integral_R^2 dy
                    G_u(y) G_(h-u)(Z-y) |W-y|^(-alpha).

The proposed(WC) asserts, for fixed alpha in[3/2,2) and q in(1/2,1),

  I_alpha(h;Z,W) <= C_(alpha,q) h^(2q-alpha) G_h(Z)^(2q-1),

uniformly in h>0 and the spatial displacements Z,W, at least almost everywhere.
The full project additionally imposes alpha+alpha0<2 and0<alpha0<1/2.
This probe does not drop the spatial weight or use a one-wave supremum.
The exact scaling is I_alpha(lambda h;lambda Z,lambda W)
=lambda^(1-alpha) I_alpha(h;Z,W), agreeing with the displayed right side.
Thus h=1 is a faithful normalization, not a change of target.

## 1. Positive-measure near-front lower bound

Let0<epsilon<1/8 and e1=(1,0). Take the OPEN spatial configuration sets

  |Z-(1-epsilon)e1| < epsilon/16,
  |W| < epsilon/16.

Restrict the integration to

  epsilon/4 < u < epsilon/2,     |y| < epsilon/16.

This has positive time-space measure. Both wave factors are supported there:
|y|<u, while

  1-9epsilon/8 < |Z-y| < 1-7epsilon/8 < 1-u.

Since sqrt(u^2-|y|^2)<=u<=epsilon/2,

  G_u(y) >= 1/(pi epsilon).

Also

  0 < (1-u)^2-|Z-y|^2
      <= 1-(1-9epsilon/8)^2 <= 9epsilon/4,

so

  G_(1-u)(Z-y) >= 1/(3 pi sqrt(epsilon)).

Finally |W-y|<epsilon/8, hence |W-y|^(-alpha)>=8^alpha epsilon^(-alpha).
The single point y=W can be assigned extended value infinity without affecting
this lower bound. Multiplying by the integration cell's volume
(epsilon/4) pi(epsilon/16)^2 gives the uniform explicit estimate

  I_alpha(1;Z,W)
    >= [8^alpha/(3072 pi)] epsilon^(3/2-alpha).                 (LB)

No asymptotic approximation, interchange of singular limits or numerical
quadrature appears in(LB).

## 2. Consequence for the exponent q

On the same Z-neighborhood,

  |Z| <= 1-15epsilon/16,
  1-|Z|^2 >= 15epsilon/16.

Because2q-1>0,

  G_1(Z)^(2q-1)
    <= A_q epsilon^(1/2-q),
  A_q = (2 pi)^(-(2q-1)) (16/15)^(q-1/2).

Thus(WC) would imply

  [8^alpha/(3072 pi A_q)] epsilon^(1+q-alpha) <= C_(alpha,q).

If q<alpha-1 the left side tends to infinity as epsilon tends to zero.
For any proposed finite C, the violation holds on an OPEN product of Z,W
balls for all sufficiently small epsilon. Therefore it is not merely an
exceptional point violating an otherwise almost-everywhere bound.

**Necessary condition:** q>=alpha-1. This does not prove sufficiency.
For alpha=3/2 it imposes no restriction beyond q>1/2. For every alpha>3/2
it eliminates the nonempty interval1/2<q<alpha-1. For example, alpha=7/4
eliminates q<3/4, but says nothing against q>=3/4. If one insists on a
single q<1 for all alpha arbitrarily close to2, that stronger uniform-q
version is impossible. The original candidate permits q to depend on alpha,
so that stronger version is not attributed to it.

Time reversal u->1-u, followed by y->Z-y, gives
I_alpha(1;Z,W)=I_alpha(1;Z,Z-W). Consequently the same obstruction holds
for W within epsilon/16 of Z. This symmetry is a change of variables in the
actual integral, not a diagram-relabeling assumption.

## 3. The obstruction lies within admissible order-four geometry

In the previous merge diagnostic, take a=1,b=2,T=4,t=5, x=0,z=Z,w=W.
Then h=b-a=1 and tau=T-b=2. For the displayed neighborhoods,
|w-z|<2, so the outer Green factor G_tau(w-z) is positive; G_a(x)>0 also.
The other covariance |z-x|^(-alpha) is finite and positive. The small
u-cell corresponds to v=a+u in(a,b), so it is a legitimate vertex2 position
in the chain, not a forbidden remote configuration.

The fractional temporal factor satisfies

  (T-v)^(-alpha0) = (3-u)^(-alpha0) >= 3^(-alpha0).

It therefore preserves(LB), up to the fixed factor c3^(-alpha0), for the
weighted merge Wtilde. The proposed(WC-time) upper bound costs only the
fixed factor2^(-alpha0), so it too fails for q<alpha-1. These configurations
have open spatial neighborhoods, and the fixed positive outer time gaps can
also be perturbed. No positivity conclusion depends on the value at a single
covariance singularity.

Crucially, the remaining diagram average still integrates Z,W and the outer
times. Their shrinking-volume effects have not been estimated here. Hence a
failure of this UNIFORM conditional bound does not imply divergence of the
full order-four diagram, failure of the second-moment scale, or impossibility
of a nonuniform envelope followed by remaining spatial averaging.

## 4. Coincident displacement check: I_alpha(1;0,0) is finite for alpha<2

This case is not another counterexample. Polar coordinates and Tonelli give

  I_alpha(1;0,0)
    = (1/(2 pi)) integral_0^(1/2) r^(1-alpha) K(r) dr,
  K(r) = integral_r^(1-r)
           du / sqrt((u^2-r^2)((1-u)^2-r^2)).

For0<r<=1/4, symmetry about u=1/2 yields twice the integral over[r,1/2].
There1-u-r>=1/4 and1-u+r>=1/2. Consequently

  K(r) <= 4 sqrt(2) integral_r^(1/2) du/sqrt(u^2-r^2)
       = 4 sqrt(2) arcosh(1/(2r))
       <= 4 sqrt(2) log(1/r).

For1/4<=r<1/2, use u+r>=2r>=1/2 and1-u+r>=2r>=1/2:

  K(r) <= 2 integral_r^(1-r)
                 du/sqrt((u-r)(1-r-u)) = 2 pi.

The last integral is the elementary beta integral after affine rescaling.
Thus I_alpha(1;0,0) is finite, since
integral_0^(1/4) r^(1-alpha)log(1/r)dr<infinity exactly when alpha<2.
This proves finiteness at this configuration only. It does not prove a
uniform-W bound, give the optimal constant, or establish(WC) for the surviving
q range. Rescaling gives I_alpha(h;0,0)=h^(1-alpha)I_alpha(1;0,0).

## 5. Probe table and stopping point

| Kill test | Result and exact scope |
|---|---|
| Homogeneous h scaling of(WC) | PASS: both sides have degree1-alpha. |
| Strongly unequal two-wave times near a front | FAIL for q<alpha-1, by explicit positive-measure cell. |
| Almost-everywhere rather than pointwise interpretation | Still FAIL for q<alpha-1: the violated spatial configuration sets are open. |
| Remote-point admissibility in original crossing diagram | PASS: tau=2 and the given outer configuration retain positive outer Green factors. |
| Coincident Z=W=0 integrability | PASS for alpha<2 via exact radial/time majorant. |
| Symmetric endpoint W=Z | Same necessary condition, by exact time/space reversal. |
| Endpoint q=alpha-1 and range q>alpha-1 | OPEN: no counterexample or upper bound established. |
| Uniform Gaussian-smoothing version | OPEN; no limiting uniformity certified here. |
| Closure of a pairing-removal algorithm / factorial budget | NOT TESTED. |
| Consequence for full moment conjecture | NONE. |

Verdict: PARTIAL. The root's suggested endpoint exponent is confirmed by an
explicit lower bound, and it narrows the permitted q interval. A proof wave
must not use q<alpha-1. Nothing in this diagnostic licenses an all-order
argument for q>=alpha-1, and no stronger counterexample in that surviving
interval was established during this bounded probe.
