# Unverified static-moment Hölder route

Root candidate,2026-10-28 UTC. NOT a proof or accepted result. This proposes
a bounded source/application check before investing further in weighted
vertex elimination. The full target range remains unchanged.

## Possible new range and exact proposed mechanism

Focus d2 isotropic Riesz gamma(x)=c|x|^(-alpha),3/2<=alpha<2,
0<alpha0<(2-alpha)/2. Choose

  1/(1-alpha0) < r < 2/alpha,  r'=r/(r-1).

This interval is nonempty exactly when alpha+2alpha0<2. It is strictly
smaller than the full standing range alpha+alpha0<2, so even success would
be partial progress, not completion or a redefinition of Goal G:upper.

For a fixed pairing D, times s and split m+n=2k, write S_D(s) for the spatial
integral of the two Green chains against the k covariance factors. Its
positive Green-product measure has mass M(s)=product_l h_l. Jensen on the
normalized finite measure suggests

  S_D(s)^r <= M(s)^(r-1) S_D^[gamma^r](s).

Here gamma^r is a genuine Riesz covariance of degree alpha*r<2 in d2.
This step is NOT asserted for arbitrary homogeneous covariances, whose
noninteger powers need not be valid covariances. Since sum_l h_l<=2t,

  M(s)^(r-1) <= (t/k)^(2k(r-1)), k>=1.

Let B_k^[alpha*r](t) be the full total-order2k STATIC Stratonovich second-
moment coefficient (all pairings and all splits) at covariance gamma^r.
The needed source-grounded input is

  B_k^[alpha*r](t) <= C^k t^((4-alpha*r)k)/(k!)^(3-alpha*r).

It might follow from the published static second-moment growth theorem,
homogeneity, coefficient positivity and optimization in t. This implication,
the exact static model normalization, and the mixed coefficient identity must
be checked, not presumed from a theorem title.

On the full discrete measure of splits and pairings times their ordered time
simplexes, Holder would combine the resulting spatial L^r estimate with

  sum_(m=0)^(2k) sum_D integral_Omega(m,2k-m) T_D(s)^(r') ds
    = (2^k/k!) [Z_theta t^(2-theta)]^k,
  theta=alpha0*r'<1, Z_theta=2/[(1-theta)(2-theta)].

This identity uses symmetry only after summing ALL temporal pairings, and
sum_m 1/(m!(2k-m)!)=2^(2k)/(2k)! with
P_k=(2k)!/(2^k k!). It preserves the original temporal Wick-sum mechanism.

Proposed bookkeeping:

  factorial power = [2(r-1)+3-alpha*r]/r + 1/r' = 3-alpha,
  time power = [2(r-1)+4-alpha*r]/r + (2-alpha0*r')/r'
             = 4-alpha-alpha0.

If all analytic/source steps hold, this yields the target coefficient scale
and hence the desired upper time exponent in the stated PARTIAL regime.
Neither these formal balances nor a successful numerical sample proves it.

## Mandatory checks before a proof claim

1. Read the exact Chen-Hu static p2 theorem, its hypotheses and version; verify
   d2 Riesz alpha*r<2, flat initial data, covariance normalization and solution.
2. Establish the static mixed coefficient identity, positivity and homogeneity;
   derive the coefficient bound from the actual all-time/large-time source
   bound without assuming uniformity at an excluded endpoint.
3. At common Gaussian covariance smoothing use Jensen
   (p_epsilon*gamma)^r <= p_epsilon*(gamma^r). Check how fixed-order limits
   pass on both static and fractional-time sides; do not assume monotonicity
   in epsilon or silently identify all generalized integrals with Lebesgue ones.
4. Exercise all total-order2/4 splits, including empty chains, to catch missing
   masses, factorials or the constant order. No Skorohod projection is involved.
5. Record exact dependence on r,alpha,alpha0,c, and distinguish this partial
   range from the harder band(2-alpha)/2<=alpha0<2-alpha.
6. Obtain independent cross-family review of a complete candidate before
   promotion. This note is author-side reconnaissance only.

[held back: collaborators' unpublished work]

## Sharper two-input interpolation candidate (supersedes the range above)

Still UNVERIFIED, not a proof. Rather than raising spatial covariance and
paying for the product-Green mass, apply Holder directly on the common
positive measure over all splits, pairings, time simplexes and Green spatial
products. For1<alpha<2-alpha0 choose

  alpha0 < theta < 2-alpha,
  b0=alpha0/theta in(0,1),
  beta=(alpha-theta)/(1-theta) in(1,2).

Then alpha=theta*1+(1-theta)*beta and alpha0=theta*b0. Riesz kernels obey
exactly gamma_alpha=gamma_1^theta gamma_beta^(1-theta), with the same
amplitude c. Formally this gives coefficient log-convexity:

  A_k(alpha,alpha0) <= A_k(1,b0)^theta B_k(beta,0)^(1-theta).

The known degree-one coefficient bound has factorial exponent2 and time
exponent3-b0. The required static bound has factorial exponent3-beta and
time exponent4-beta. Their convex combinations are precisely3-alpha and
4-alpha-alpha0. Thus this candidate could cover the ENTIRE higher-alpha
Riesz range in d2 (and d3 if its limit convention matches), not merely the
smaller wedge above. It still does not automatically cover arbitrary
anisotropic covariances: their noninteger powers need not be covariances.

Important regularization nuance: do not assert exact log-convexity of the
source's cutoff temporal kernels. Instead gamma^0_(alpha0,delta)(t)
<=|t|^(-alpha0)=(|t|^(-b0))^theta. Gaussian spatial averaging gives

  (p_epsilon*gamma_alpha)(x)
    <= (p_epsilon*gamma_1)(x)^theta
       (p_epsilon*gamma_beta)(x)^(1-theta)

by Holder on the Gaussian probability measure. Then the first endpoint is
a deterministic degree-one diagram sum with unsmoothed temporal factor b0
and Gaussian-smoothed spatial covariance; its existing Section5 proof
appears uniform in the spatial width, so it may be bounded directly without
identifying an unregularized-time stochastic model. The second endpoint is
the static regularized coefficient at beta. Its fixed-order limit must be
checked in the actual static source. One can pass to that limit after the
inequality; no uniform-in-epsilon static large-time theorem or monotonicity
of covariance smoothing should be assumed.

For d3, use the same positive Green-product measure in Holder and remove
Green smoothing at fixed noise smoothing before taking noise limits. Each
endpoint's existence/convergence and the role of the common epsilon must be
verified. The source/application audit is pending. No whole-moment bound,
newly accepted coefficient inequality or novelty claim is made by this note.
