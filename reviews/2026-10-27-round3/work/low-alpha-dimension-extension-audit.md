# Low-alpha dimension extension: independent audit

[held back: collaborators' unpublished work]

## Exact scope

Let d be 1, 2 or 3. Retain the paper's noise assumptions:

- 0<alpha0<1;
- gamma is a real nonnegative, nonnegative-definite tempered covariance
  distribution, with the author convention
  gamma(x)=integral exp(i xi.x) mu(dxi);
- mu is the associated positive Radon spectral measure;
- gamma is homogeneous of degree -alpha, now with **0<alpha<1**.

Homogeneity for a distribution is understood under dilation in the usual
pullback sense; for a positive covariance measure this is equivalently
spatial-measure scaling of degree d-alpha. This is not an assumption that
gamma or mu has a radial density. The source existence condition
alpha+alpha0<2 follows in this subrange but may be retained explicitly.

Set V=mu({xi: |xi|<=1}). Local finiteness gives V<infinity. If V=0, scaling
forces mu=0 and the noise-free conclusion is trivial. Otherwise V>0.

For h>0, G_h is the positive wave-kernel measure. From the author's (2.3)–(2.5),

    integral G_h(dy) = h,
    Fourier(G_h)(xi) = sin(h|xi|)/|xi|,

with value h at xi=0. In d=3 it is the sphere measure divided by 4*pi*h;
no Lebesgue-density assertion is being made.

## 1. Spectral homogeneity and the ball-mass formula

Fourier uniqueness transfers the distributional homogeneity to

    mu(c A) = c^alpha mu(A)                  for every c>0 and Borel A.

Indeed, gamma(c x) is the Fourier transform of the pushforward of mu under
xi->c xi, whose value on A is mu(A/c). Equality with c^(-alpha) gamma gives
mu(A/c)=c^(-alpha)mu(A). This argument uses uniqueness for tempered spectral
measures, not pointwise convergence of the unsmoothed Fourier integral.

Taking A to be the unit ball gives

    mu(B_R) = V R^alpha, R>0.                              (L1)

In particular mu({0})=0 by continuity from above on a finite ball and
R down to zero. The radial pushforward of mu has distribution function
V R^alpha, hence radial integration uses alpha*V*r^(alpha-1)dr. This does
not assert rotational invariance: an anisotropic or lower-dimensional
spectral measure may have exactly this same radial distribution function.
The source's p.3 radial integral formula agrees with this normalization.

## 2. Exact radial integral without any density assumption

For r>=0, define 1/r=+infinity at r=0. The layer-cake identity is

    min(h,1/r) = integral_0^h 1_{r<=1/u} du.

An endpoint of the indicator makes no difference to the u-integral.
Tonelli and (L1) therefore give, exactly,

    integral min(h,1/|xi|) mu(dxi)
      = integral_0^h mu(B_(1/u)) du
      = V integral_0^h u^(-alpha) du
      = [V/(1-alpha)] h^(1-alpha).                        (L2)

All integrands are nonnegative. Finiteness holds precisely for alpha<1
for this upper envelope (unless V=0). Equivalently, splitting at r=1/h
gives V h^(1-alpha) from the small ball and
alpha*V/(1-alpha) h^(1-alpha) from the tail. Omitting the small-ball term
would give an incorrect constant.

This calculation is valid for general positive Radon mu with the ball-mass
scaling; no angular disintegration or surface-density assumption is needed.

## 3. Uniform convolution bound and positivity

Let gamma_epsilon=gamma*p_epsilon, with a probability Gaussian and epsilon>0.
Its spectral multiplier has the form exp(-c_epsilon |xi|^2), between zero
and one. The measure mu_epsilon is finite: polynomial ball growth makes
its Gaussian-weighted total mass finite. Thus Fourier Fubini with the finite
wave measure is justified at each epsilon>0:

    integral G_h(dy) gamma_epsilon(y+z)
      = integral exp(i xi.z) Fourier(G_h)(xi)
                   exp(-c_epsilon |xi|^2) mu(dxi).

The real-space integral is nonnegative because **gamma>=0 as a distribution**
and G_h is positive. A positive tempered distribution is a positive Radon
measure, and convolution with the positive Gaussian preserves nonnegativity.
Positive definiteness alone would not supply this fact.

Using |sin(h r)|/r <= min(h,1/r) and (L2), one obtains

    0 <= integral G_h(dy) gamma_epsilon(y+z)
       <= [V/(1-alpha)] h^(1-alpha),                      (L3)

uniformly in z and epsilon. The bound comes from the absolute value of the
Fourier integral, not from pretending its oscillatory integrand is positive.
There is no extra Fourier-normalization factor: V uses the source's mu,
which already includes any normalization constants.

For the source's regularized wave kernel G_(h,eta)=p_eta*G_h,
Fourier(G_(h,eta)) has one more Gaussian multiplier bounded by one, and
its mass remains h. Consequently (L3) also holds uniformly in eta>0.
Each pair may have a different covariance-smoothing parameter; the same
bound applies to every one of them.

One may also infer a bounded continuous limiting convolution from dominated
convergence in the absolutely integrable Fourier expression. That is not
needed to assign pointwise products to unsmoothed generalized covariances:
the full diagram estimates below can remain at the regularized level and
pass through the source's defining limits.

## 4. Dimension-three limits and coordinate bookkeeping

For eta>0 the Green kernels are nonnegative functions, so the spatial
increment change of variables is an ordinary triangular block map with
absolute determinant one. Each vertex position depends only on earlier
increments in its own chain. The root's descending endpoint elimination
therefore applies verbatim using (L3) for a closing variable and mass h
for an opening variable.

The bound is uniform in eta, epsilon and the temporal truncation parameters.
In d=3 the correct transfer is:

1. Fix every noise-smoothing parameter. Send eta to zero in the source's
   inner L2 limit (pp.13–14). Then products of two factors converge in L1
   by Cauchy–Schwarz, and their expectation inequalities pass to the limit.
2. Send the noise-smoothing parameters to zero using the fixed-order L2
   limits of the source's Theorem4.1, and again use L1 product convergence.

The existence of the inner limit is also directly compatible with the
measure formulation: at fixed noise smoothing, the covariance functions
are bounded and continuous, G_(h,eta) converges weakly to G_h with mass h,
and the Gaussian moment integrands are bounded continuous products. At
fixed time vectors, product-measure weak convergence applies. On a bounded
time simplex the products of masses are integrable, giving a uniform
dominator depending on the fixed noise smoothing. No assertion of a
Lebesgue density for the limiting sphere kernel is required.

In d=1 and d=2 the extra eta step is unnecessary. Alternatively, after
fixing noise smoothing one can write the spatial integral directly over
the product of positive increment measures G_(h_l)(dy_l); the same
conditional integration argument applies. Keeping the eta-first route
matches the pinned author's definition and is easiest to audit.

At the temporal stage, replace any vertex-dependent truncated covariance
by the common full |s-r|^(-alpha0) kernel **before** using the symmetry of
the full temporal Wick sum. The replacement is monotone and preserves
nonnegativity. The claim is not that differently truncated Wick sums are
already symmetric.

## 5. Transfer to the target-scale estimate

Let M=V/(1-alpha). A pairing on 2k vertices has k opening and k closing
endpoints, so the spatial elimination gives

    S_D(h) <= M^k product_open h_l product_close h_l^(1-alpha).

Because 0<alpha<1 and sum_l h_l<2t, weighted AM–GM gives the same common
bound as in the d=1 draft:

    S_D <= Ksp^k t^((2-alpha)k) k^(-(2-alpha)k),
    Ksp = V 2^(2-alpha)(1-alpha)^(-alpha)/(2-alpha)^(2-alpha).  (L4)

No dimensional factor is missing: the opening wave mass is h in every
one of d=1,2,3, and the closing convolution has power h^(1-alpha).
All dependence on spatial dimension/angular measure is allowed in V.

After (L4), sum every pairing first. The temporal Wick sum is fully
permutation symmetric. For split (m,n), its ordered-domain integral is
1/(m!n!) times the cube integral. The latter equals

    [(2k)!/(2^k k!)] [Z t^(2-alpha0)]^k,
    Z=2/[(1-alpha0)(2-alpha0)].

Summing m+n=2k yields 2^(2k)/(2k)!, and hence

    A_k(t) <= (2 Z Ksp)^k t^((4-alpha-alpha0)k)
                     /[k! k^((2-alpha)k)]
            <= (2 Z Ksp)^k t^((4-alpha-alpha0)k)/(k!)^(3-alpha).

The root's nonnegative-series comparison, with q=3-alpha, now gives

    E u(t,x)^2
      <= exp{(3-alpha)(2 Z Ksp)^(1/(3-alpha)) t^kappa},
    kappa=(4-alpha-alpha0)/(3-alpha).                     (L5)

The total-order-zero term is one; inequalities dividing by k are used only
for k>=1. Empty chains present no special difficulty. This supplies the
same target-scale upper bound in d=1,2,3 for **all** nonnegative homogeneous
covariances of degree -alpha with 0<alpha<1, in the source's sense. It makes
no sharp-constant claim and still needs independent scientific review.

## Boundary and falsification checks

- An anisotropic example is gamma(x)=c|x1|^(-alpha), independent of the other
  coordinates, for 0<alpha<1. Its spectral measure is supported on an axis,
  not a full-dimensional radial density. The Fourier and ball-mass arguments
  still apply. This is a useful test that no isotropy hypothesis was smuggled in.
- For an ordinary Riesz covariance in d=1, the real-space bound used in the
  frozen draft may be sharper than (L3). The extension is allowed to have a
  larger constant; it is not a contradiction or an equality assertion.
- As alpha approaches one, the absolute-Fourier envelope (L2) diverges for
  fixed V>0. It cannot prove the white endpoint. The d=1 white covariance
  retains its separate elementary bound c/2 and the frozen d=1 argument.
- Failure of this envelope at alpha>=1 does not prove failure of the actual
  convolution estimate, much less failure of the target-scale result.
  Oscillatory cancellation can make a convolution finite even when its
  absolute Fourier envelope diverges. No alpha>=1 extension is claimed.
- Nonnegative definiteness without gamma>=0 is insufficient for the
  nonnegative-diagram comparison used here. The paper supplies both, and
  both must appear in the extension's assumptions.
- The first-moment/asymptotic constant gaps and the missing higher-alpha
  d=2,3 regime remain untouched. The static exponent calibration agrees,
  but no uniform alpha-to-one or alpha0-to-zero constant is asserted.

## Source correspondence and limitations

Authority: `sources/chen-2026-author/aap-chen-2025.pdf`, SHA256
`5f7385ca451e643a1f3ff31835e4ee52b2708b5d2e3652eec3fb5d3958b97b6c`.
Rendered pages3,7,13,14 were inspected for this audit:

- p.3: homogeneity and the radial spectral-integral reduction;
- p.7: Fourier transform (2.3), mass (2.4), positivity/measure form (2.5);
- pp.13–14: spatial covariance smoothing (2.24) and the two-step d=3
  generalized-kernel definition.

The source's fixed-order L2 convergence remains an imported analytic input;
this memo checks the extension's application, not the whole source proof.
The root's frozen d=1 proof and its review packet were not edited. Any
addition of (L3)–(L5) to the manuscript must be frozen and reviewed on its
own enlarged scope. No Skorohod statement or formal-verification result was
developed in this task.

STATUS: DONE_WITH_CONCERNS — the low-alpha, all-dimensions extension appears
valid with the stated positivity and spectral conventions; cross-family
acceptance and manuscript integration remain pending.
