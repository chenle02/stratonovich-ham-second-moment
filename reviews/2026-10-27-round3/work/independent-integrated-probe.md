# Independent integrated probe: fold the spatial tree, retain the time reflection

Status: **unreviewed mathematical reconnaissance**, not manuscript acceptance,
not a G:upper proof, and not a new Skorohod result. This probe uses only the
Stratonovich all-pairing coefficients from reviewed G0/G1. It does not replace
the previously recorded pointwise-concatenation or uniform-diagram no-gos.
A non-GPT review is still required for every deduction below.

## Finding

In d=1 there is a concrete spatial folding operation that removes the known
support defect of chronological concatenation. It gives a bound by a single
geometric wave chain, with no order-dependent Jacobian loss, **but the
physical time covariance becomes reflected about a center inside the joining
gap**. The center depends on the integration variables.

At the static endpoint the reflection disappears and this gives a coarse
integrated two-chain-to-one-chain bound. At fractional time the missing step
is now a precise reflected-time integral comparison. Merely replacing the
reflected covariance by the ordinary one is false even at total order two.
No proof of an exponential-in-order cost for that replacement emerged.

## Exact map and domain, for one nonempty split

Fix d=1, m,n>=1, N=m+n=2k, horizon t>0. The first chain has times
0<s1<...<sm<t and positions x1,...,xm; the second has
0<r1<...<rn<t and positions y1,...,yn. Both roots are spatial zero.
Write

- a=s1, b=r1;
- u_i=s_i-s_(i-1), i=2,...,m;
- v_j=r_j-r_(j-1), j=2,...,n;
- U=sum_(i=2)^m u_i, V=sum_(j=2)^n v_j;
- q=min(a,b), c=a+b.

The new geometric chain visits the original vertices in the order

    xm, x_(m-1), ..., x1, y1, y2, ..., yn.

Its N incoming time gaps are

    H = (q, u_m, u_(m-1), ..., u_2, c, v_2, ..., v_n).

Thus H1=q and H_(m+1)=c. Empty internal strings are omitted. The first
chain's sum U is now H2+...+Hm, and V=H_(m+2)+...+HN.

Split the original time domain into a<b and b<a (the equality set is null).
The map (a,b)->(q,c) has absolute Jacobian **one** on each branch. Reversing
the internal gap string also has absolute Jacobian one. The two image
domains, in N ordinary gap variables, are

    D0: H_i>0, c>2q, q+U<t, c-q+V<t;       (a=q, b=c-q)
    D1: H_i>0, c>2q, c-q+U<t, q+V<t.       (a=c-q, b=q)

There is no discarded simplex factorial and no binomial-shuffle multiplier.
The branches are summed, not identified as disjoint in H-space. In either
branch

    sum H_i = q+U+c+V = q+sm+rn < 3t.

## Spatial inequality, including its normalization

For the one-dimensional wave kernel G_h(z)=1/2*1_{|z|<h},

    (G_a * G_b)(z)
      = (1/4) length([-a,a] intersect [z-b,z+b])
      <= min(a,b) G_(a+b)(z) = q G_c(z).                  (F1)

Both sides vanish outside |z|<a+b, and the intersection length is at most
2min(a,b). This is an inequality of nonnegative functions, with the exact
1/2 normalization retained.

Translate all noise-vertex positions by -xm and use z=-xm as the old root
coordinate. The full linear coordinate change has absolute Jacobian one.
The first noise vertex becomes fixed at zero. Since every spatial covariance
is a function of a difference, none depends on z. The only two factors
containing z are the original root edges, with lengths a and b. Integrating
z combines them into G_a*G_b; applying (F1) leaves q G_c at the joining
edge. All other Green factors are exactly the reversed first-chain factors
and forward second-chain factors. Their reversal is legitimate because G is
even in its spatial variable.

The resulting q times an (N-1)-edge rooted-relative integral equals the
N-edge single-chain spatial integral with the initial gap q: translate all
new positions by its first noise position and use integral G_q=q. Therefore,
for every fixed original time vector and every pairing D, the original
spatial integral is bounded by the spatial integral of the geometric chain
with gaps H and the transported pairing pi(D). Here pi reverses the first
block of labels and leaves the second in forward order.

This uses translation-invariant nonnegative spatial covariance, not a
pointwise comparison between two different chronological supports. For white
space the argument can first be applied with the same smoothed covariance
used in G0, then passed to the finite-dimensional contracted integral. For
d=1 Riesz covariance with 0<alpha<1 the fixed-time integrals are ordinary
locally integrable nonnegative integrals. No d=2 or d=3 extension is claimed.

## The temporal covariance after folding

Let tau_j=H1+...+Hj be the new chronological noise times. Define

    eta0 = 2q+U on D0,
    eta1 = c+U  on D1.

In either case eta=q+sm, lies strictly between tau_m and tau_(m+1), and the
old physical time at new vertex j is

    physical_time(j) = |tau_j-eta|.

Indeed, on the reversed first block tau_j=q+sm-s_i, and on the second block
tau_j=q+sm+r_l. Thus every temporal factor is preserved **exactly** as

    ||tau_i-eta| - |tau_j-eta||^(-alpha0).                (F2)

Pairs lying within one original chain keep the usual |tau_i-tau_j| factor.
Pairs crossing the two original chains become

    |2eta-tau_i-tau_j|^(-alpha0),

with a singularity on a reflected diagonal. Dropping that diagonal is not a
support repair or a harmless change of notation.

For precision, define the nonnegative single-geometric-chain Wick integrand

    W_k(H;eta)
      = sum_(D in Pi_k) integral_(R^N)
          product_(j=1)^N G_(Hj)(zj-z_(j-1))
          product_((i,j) in D)
            ||tau_i-eta|-|tau_j-eta||^(-alpha0) gamma(zi-zj) dz,

with z0=0 and the same covariance normalization as the paper. The preceding
map yields the concrete candidate inequality

    E[X_m(t,x) X_n(t,x)]
      <= integral_D0 W_k(H;eta0(H)) dH
         + integral_D1 W_k(H;eta1(H)) dH.                (F3)

The pairing transport is a bijection of the complete Pi_k, so all self-pairs
are retained. This is the intended Stratonovich consumer of the map. It is
not being developed here for a restricted pure-cross sum.

Important limitation: eta depends on H and on the branch. The right side is
not automatically a coefficient of a solution driven by one fixed reflected
noise field. Even if eta were fixed, Chen's ordinary stationary-time
first-moment theorem would not apply without a separate comparison. F3 alone
therefore does not prove MC or DT from the route screen.

## Lowest-order test: spatial folding is exact in white space

Take m=n=1, gamma=delta_0, t=1, and write a0=alpha0. The original spatial
integral is min(a,b)/2=q/2. The folded single-chain spatial integral is also
q/2, so (F1) is an equality at the contracted spatial difference zero.

Here H=(q,c), the two branches give 0<q<1 and 2q<c<1+q, and the temporal
factor (F2) is (c-2q)^(-a0). Hence the original coefficient becomes exactly

    I_diff(a0)
      = integral_0^1 dq integral_(2q)^(1+q) q(c-2q)^(-a0) dc
      = 1/[(1-a0)(2-a0)(3-a0)],

which agrees with G0. The factor q, rather than q/2, comes from the two
Jacobian-one branches. This independently checks the normalization and map.

If one incorrectly replaces the reflected factor by the ordinary-chain
factor c^(-a0), the same domain gives

    I_sum(a0) = L(a0)/(3-a0),
    L(a0) = integral_0^1 z(1+z)^(-a0) dz
          = (2^(2-a0)-1)/(2-a0) - (2^(1-a0)-1)/(1-a0).

At a0=1/2,

    I_diff / I_sum = 2+sqrt(2) > 1.                      (F4)

Thus deleting the reflected-time dependence with unit constant is false for
the **integrated** expression, even though the spatial transformation is
exact in this example. Pointwise, the ratio is unbounded as c decreases to
2q at fixed q>0, on positive-measure neighborhoods of the reflected diagonal.
No fixed pointwise factor can fix that replacement. As a0 increases to one,
L(a0) tends to 1-log(2), so the integrated ratio diverges like
1/[(1-a0)(1-log(2))]. This only says that a parameter-uniform comparison between these two
integrals on the same folded domain is impossible. It does not compare with
the full ordinary-chain integral on its larger simplex, and a fixed-parameter
exponential-in-order cost is not refuted.

This is a new test of the explicit spatial-folding operation, not a repeat of
the earlier failed chronological pointwise concatenation.

A useful contrasting check is available at this same lowest order. In white
space the two contracted root endpoints coincide, so the joining Green
factor is evaluated at spatial difference zero and is 1/2 for *every*
positive joining time. Therefore a different map

    (a,b) -> (q=min(a,b), d=|a-b|)

is covariance-aware: it has Jacobian one on each branch, maps the square to
q,d>0 with q+d<t, retains spatial factor q/2 and temporal factor d^(-a0),
and gives exactly E X1(t)^2 = 2 E X2(t). This recovers the known G0 identity
as an explicit map. It does not iterate automatically: for higher orders a
joining edge need not have coincident endpoints, and replacing c=a+b by
|a-b| then reintroduces a spatial support problem. Any successful continuation
would need a pairing-dependent or grouped operation, not an indiscriminate
shortening of every joining edge. This example is why F4 must not be promoted
to an impossibility theorem for integrated mean comparisons.

## Static calibration and the surviving obligation

At alpha0=0, W_k(H;eta) is independent of eta and is the ordinary static
single-chain Wick integrand. Since D0,D1 are each subsets of the simplex
sum H<3t, F3 gives

    E[X_m(t,x)X_n(t,x)]_(static) <= 2 E X_(2k)(3t,x)

for every nonempty split. Empty splits are already first-moment terms.
Summing all splits gives the coarse static comparison

    A_k(t) <= 2(2k+1) a_k(3t).

For homogeneous spatial covariance, a_k(3t)=3^((4-alpha)k)a_k(t), so this has
only exponential cost in k. The purpose is a consistency check of the map,
not a novelty claim about the already-known static asymptotics.

For fixed 0<alpha0<1 the precise unresolved step is to bound the two reflected
integrals in F3 by C^(k) times the ordinary single-chain coefficient, with C
allowed to depend on alpha0 and the spatial covariance. The time map, Jacobian,
domain and covariance change are now explicit. The all-order reflected-time
comparison remains unproved. Pointwise domination is unavailable, and no
argument was found that controls its integrated cost uniformly in k.

An appealing but insufficient observation is that time reflection/restriction
can be bounded on suitable fractional covariance Hilbert spaces. Positive-
semidefinite covariance order alone does not imply entrywise Wick-sum order
for the wave functional. No such Gaussian comparison was assumed here.

## Scope and disposition

[held back: collaborators' unpublished work]

STATUS: DONE_WITH_CONCERNS — a concrete integrated folding inequality and its
remaining covariance obstacle have been identified; non-GPT review required.
