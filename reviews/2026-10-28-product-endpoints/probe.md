# Product-covariance endpoint factorization: bounded probe

Date:2026-10-28 UTC. Status: **SURVIVES / UNREVIEWED AUTHOR CHECK**.
Decision: **PROCEED to a separately reviewed algebra/covariance lemma**, not to
claim a full SPDE theorem. The explicit interval construction has no defect
under the strict assumptions below. This is GPT-family work, not another
cross-family vote. No canonical notes, existing packet or sibling was edited.

## 1. Exact contract

Let a=(a1,a2,a3), with0<=a_j<1, and

  1<alpha=sum_j a_j<2,
  0<theta<2-alpha,
  beta=(alpha-theta)/(1-theta).

We seek exponent vectors b,v with

  sum b_j=1, sum v_j=beta,
  a_j=theta b_j+(1-theta)v_j,
  a_j>0 implies0<b_j,v_j<1,
  a_j=0 implies b_j=v_j=0.

The letter v denotes the root's proposed static exponent vector c, to keep it
separate from the positive covariance amplitude C. Since alpha>1 and each
coordinate is below1, at least two coordinates are active. Also theta<1.

## 2. The interval construction and all strictness checks

Define

  L_j=max(0,(a_j-1+theta)/theta),
  U_j=min(1,a_j/theta).

If a_j=0, then L_j=U_j=0. If a_j>0, then L_j<U_j:
- When a_j>=theta, U_j=1 and L_j<1 because a_j<1.
- When a_j<theta, U_j=a_j/theta>0. If L_j=0 the claim is immediate;
  otherwise U_j-L_j=(1-theta)/theta>0.

**Lower-sum check.** Let I={j:L_j>0}, m=|I|. For m=0 the sum is0.
For m=1 it is strictly below1 by the preceding coordinate check.
For m>=2,

  sum_(j in I) a_j <= alpha < 2-theta
    <= m-(m-1)theta,

where the last inequality is equivalent to(m-2)(1-theta)>=0. Therefore

  sum_j L_j
    = [sum_(j in I) a_j-m+m theta]/theta <1.

**Upper-sum check.** If some a_j>=theta then U_j=1, and a different active
coordinate has positive U, so sum U_j>1. If every a_j<theta, then
sum U_j=alpha/theta>1 because alpha>1>theta. Equality a_j=theta belongs
to the first case and causes no failure.

Set

  lambda=(1-sum L_j)/(sum U_j-sum L_j),
  b_j=L_j+lambda(U_j-L_j),
  v_j=(a_j-theta b_j)/(1-theta).

The strict sum bounds give0<lambda<1 and sum b_j=1. For each active
coordinate,L_j<b_j<U_j; hence0<b_j<1. Since b_j<U_j<=a_j/theta,
v_j>0. Since b_j>L_j>=(a_j-1+theta)/theta,v_j<1. At a zero coordinate,
b_j=v_j=0 exactly. Finally,

  sum v_j=(alpha-theta)/(1-theta)=beta,
  beta-alpha=theta(alpha-1)/(1-theta)>0,
  2-beta=(2-alpha-theta)/(1-theta)>0.

Thus1<alpha<beta<2 and all endpoint requirements hold. The strict assumptions
are load-bearing: theta=2-alpha gives beta=2, and a_j=1 need not leave a
strict coordinate interval. Neither excluded endpoint is certified here.

## 3. Exact rational controls

`check.py` uses only Python fractions.Fraction. `checks.json` records:
- 2,985 valid grid cases with a_j in{0,1/10,...,9/10}, including540 cases
  with at least one zero coordinate;
- theta equal to1/1000,1/10,1/2,9/10,999/1000 times(2-alpha), exercising
  both strict parameter boundaries;
- all possible active-lower-set sizes0,1,2,3;
- five additional exact cases near a_j=1,near alpha=1,near alpha=2,
  repeated/equal exponents and zero coordinates.

Every case checks both strict sum inequalities, exact reconstruction, exact
endpoint sums, all coordinate bounds and zero-coordinate preservation.
These finite controls support the algebra inspection but do not prove the
continuous parameter statement or any positive-definiteness/SPDE claim.

For the covariance used in the radial-lowering obstruction,

  a=(9/10,3/5,0), theta=1/4,

this construction gives

  b=(5/7,2/7,0),
  v=(101/105,74/105,0), beta=5/3.

The example checks covariance factorization only. If it is used with a
fractional-time parameter, additionally require alpha0<theta; do not set
alpha0=theta and claim a valid time endpoint.

## 4. Endpoint covariances and same-amplitude Gaussian Hölder

For C>0 define ordinary locally integrable densities on R3,

  gamma_a(x)=C product_j |x_j|^(-a_j),
  gamma_b(x)=C product_j |x_j|^(-b_j),
  gamma_v(x)=C product_j |x_j|^(-v_j),

with each zero exponent denoting the constant factor1, including at that
coordinate's zero. Values on the remaining singular coordinate planes do not
change the associated locally integrable distributions. All three are
nonnegative, even and homogeneous of their respective degrees alpha,1,beta.
Each active exponent lies in(0,1), so local integrability is a product of
one-dimensional locally integrable factors; a sufficiently decaying product
weight proves temperedness.

Each endpoint is positive definite. For every active exponent e in(0,1),
use the positive Gaussian-mixture identity

  |u|^(-e)=Gamma(e/2)^(-1)
      integral_0^infinity s^(e/2-1)exp(-s u^2)ds.

Multiplying the finitely many active coordinate integrals gives a positive
mixture of Gaussian functions in those coordinates, constant in the others.
Each component is positive definite on R3. For a Schwartz autocorrelation
psi=phi*tildephi, product local integrability and rapid decay give
integral gamma_endpoint|psi|<infinity. Tonelli with |psi| and Fubini thus
justify the mixture against psi, proving its quadratic form nonnegative.
This argument includes zero exponents without a meaningless Gamma(0) factor.

The reconstruction and same amplitude give, almost everywhere,

  gamma_a=gamma_b^theta gamma_v^(1-theta).

Therefore for a common Gaussian covariance width epsilon>0 and every z,

  (p_epsilon*gamma_a)(z)
    <= (p_epsilon*gamma_b)(z)^theta
       (p_epsilon*gamma_v)(z)^(1-theta).

This is ordinary Hölder on the Gaussian probability measure; its endpoint
integrals are finite. The amplitude on the right is C^(theta+1-theta)=C,
so no extra noise-strength factor is hidden. Using one common noise width
means common edge covariance width2epsilon, as in the source convention.
The construction varies the coordinate exponents, not fractional powers of
an arbitrary covariance distribution.

## 5. Source compatibility and prospective time parameters

The exact Chen–Hu publisher source and rendered pages are already bound in
`../2026-10-28-static-holder/source-audit.md` and `source-evidence.json`:
SHA256 `58b152d78cd0d54d82b991933b3eaece86e1ed2b44fe09882c14eba921e97e22`.
Its model/Theorem1.2,pp2145–2147, covers nonnegative positive-definite
homogeneous covariance in d=1,2,3 with degree below min(2,d), data(1,0).
There is no isotropy or all-coordinate-strict-positivity hypothesis. The product
endpoint gamma_v has degree beta<2 and is a genuine covariance, so its
spectral Dalang condition and the general static coefficient result(5.1),
(5.15),pp2173/2180, apply at the source/application level. Their constant can
depend on the full exponent vector v,C,d,not merely its sum beta.

For an eventual fractional-time target with0<alpha0<2-alpha, choose
alpha0<theta<2-alpha and set b0=alpha0/theta<1. The degree-one endpoint
gamma_b then meets the accepted P:low-alpha-upper hypotheses in d3.
The already audited static fixed-order Gaussian smoothing and mixed-product
limits are compatible with these *general* product covariances; no uniform
large-time bound in smoothing width is claimed or needed. A full candidate
must state the common-measure diagram transfer and limiting argument again
at this widened covariance scope, rather than treating this screen as its
scientific review.

## 6. What this does and does not change

The failed d3 Euclidean radial lowering used |x|^(alpha-1)gamma_a(x).
The present gamma_b is a different function with altered coordinate powers.
The valid factorization above therefore does not contradict that obstruction.
It is restricted to the ordinary product family (including independent
coordinates with exponent0). It does not show that every general homogeneous
d3 covariance admits admissible endpoints.

No full moment upper theorem, sharp constant, novelty, Skorohod result or
Lean certificate is claimed. Before any SPDE theorem promotion, freeze and
independently review the complete product-family covariance lemma and its
interpolation application. The current planar/Riesz packets remain separate.
