# Static coefficient rate and interpolated asymptotic constant

Date:2026-10-28 UTC. Status: **CHECK PASSES / UNREVIEWED LOCAL DEDUCTION**.
This is a bounded source/algebra check, conditional on the correctly established
coefficient Hölder transfer and endpoint hypotheses. It is not a new theorem
acceptance, a sharp-constant claim, or an independent cross-family review.
No canonical source or frozen review packet was modified.

## 1. Pinned printed formulas and parsing

Source: Chen–Hu(2025), *Stratonovich hyperbolic Anderson equations*, published
PDF `../SPDEForge/sources/chen_hu-25-hyperbolic/published-24-AOP1758.pdf`,
SHA256 `58b152d78cd0d54d82b991933b3eaece86e1ed2b44fe09882c14eba921e97e22`.
The rendered pages2147 and2180 were viewed again for this check, using the
retained images in `../2026-10-28-static-holder/source-pages/`.
The supporting coefficient homogeneity is source(5.1),p2173; the finite-order
upper estimate supporting the log parsing is(5.13),p2179.

Let Gamma_st be the actual static endpoint covariance of degree beta in(1,2),
with its actual amplitude, in d3 (the same algebra applies to an admissible
d2 endpoint). Put

  Q=3-beta, Nu=4-beta=Q+1,
  M=M[Gamma_st],
  A=2 sqrt(M)/Nu.

M is the source variational functional(1.11),p2147, with gradient penalty1:

  M = sup_(g in F_d) { [integral Gamma_st(x-y)g(x)^2g(y)^2 dxdy]^(1/2)
                       -integral |grad g|^2 dx },
  F_d={g in W^(1,2):integral |g|^2=1}.

Finiteness is pinned separately in
`../2026-10-28-static-holder/source-finiteness-supplement.md`.
No replacement of M by the disputed one-dimensional spatial-white value is
made; beta in(1,2) and d3 are distinct from that case.

For full total-order2k coefficients B_k, source(5.15) is the log of the WHOLE
positive coefficient-rate product

  (1/2)^Q p^Nu A^Nu,

not log((1/2)^Q) multiplied by the remaining factors. This parsing is also
confirmed by the pre-asymptotic bound(5.13) and Theorem1.2(1.9).
At p2,

  (1/2)^Q 2^Nu A^Nu = 2^(Nu-Q) A^Nu = 2 A^Nu.

Therefore the root's expression is correct:

  Lambda_st=2*(2 sqrt(M)/(4-beta))^(4-beta),
  limsup_(k->infinity) [(k!)^Q B_k(1)]^(1/k) <= Lambda_st.        (S-rate)

The root form follows from the logarithmic rate by exponentiation (or directly
from(5.13)); zero coefficients cause no problem with the root formulation.
We only need the upper rate, although the source states the full rate in(5.3).

As a separate normalization check, Theorem1.2 at p2 gives

  L_st=(Q/2)*2^(Nu/Q)*A^(Nu/Q)
      =Q*2^(1/Q)*A^(Nu/Q)
      =Q*Lambda_st^(1/Q),                                    (S-time)

since Nu=Q+1. The two printed statements therefore agree with the proposed
coefficient rate and contain no missing factor2.

## 2. The asymptotic upper constant does not need unknown low-order constants

Fix admissible endpoint parameters once and for all:

  0<theta<1, b0=alpha0/theta<1,
  alpha=theta+(1-theta)beta,
  q=3-alpha=2theta+(1-theta)Q,
  nu=4-alpha-alpha0=theta(3-b0)+(1-theta)Nu,
  kappa=nu/q.

Assume the actual coefficient transfer has been established after the required
regularized limits:

  A_k(t) <= [C_low^k t^((3-b0)k)/(k!)^2]^theta
               [B_k(t)]^(1-theta),   k>=1,t>0.                (H)

The target A_k are the full mixed-moment coefficients, not an assumed raw
singular-integral representation. Source(5.1) supplies the exact STATIC
identity B_k(t)=B_k(1)t^(Nu k) for all t>0. No target coefficient homogeneity
identity is necessary for the following upper-bound argument.

For each eta>0,(S-rate) gives a finite N=N(eta,endpoint) such that

  B_k(1) <= (Lambda_st+eta)^k/(k!)^Q,  k>=N.

Hence, simultaneously for every t>0 and k>=N,

  A_k(t) <= D_eta^k t^(nu k)/(k!)^q,
  D_eta=C_low^theta (Lambda_st+eta)^(1-theta).                  (T)

**The order threshold N is independent of t.** This is where the all-time
static coefficient homogeneity is used. Merely invoking a large-time bound
whose threshold depended on k would not establish(T).

For each1<=k<N, (H) gives the finite bound

  A_k(t) <= d_k t^(nu k),
  d_k=C_low^(theta k) B_k(1)^(1-theta)/(k!)^(2theta).

Together with A_0=1 and the nonnegative moment series, this yields

  E u(t,x)^2 <= P_eta(t)+sum_(k>=N) D_eta^k t^(nu k)/(k!)^q
             <= P_eta(t)+exp(q D_eta^(1/q)t^kappa),
  P_eta(t)=1+sum_(1<=k<N) d_k t^(nu k).

P_eta is a finite power sum, equivalently a polynomial in t^nu; its exponents
need not be integers. Thus log(P_eta(t))/t^kappa tends to0. The last series
bound is the standard positive-sequence inequality
sum z^k/(k!)^q <= exp(q z^(1/q)) for q>1. Its use does not require a
sharp Mittag–Leffler asymptotic.

For a nontrivial low endpoint C_low>0, D_eta>0, so taking log, dividing by
t^kappa and letting t increase gives

  limsup_(t->infinity) t^(-kappa)log E u(t,x)^2
    <= q [C_low^theta (Lambda_st+eta)^(1-theta)]^(1/q).

Then let eta decrease to0. The verified candidate constant is

  q [C_low^theta Lambda_st^(1-theta)]^(1/q).                   (U)

The zero covariance case is separately trivial. The eta argument also handles
a zero static upper rate without dividing by M or Lambda_st.

## 3. Scope and required qualifications

- (U) is an **explicit variational, generally nonsharp upper constant**, in terms
  of the actual low endpoint constant and actual static endpoint variational
  functional. It is not the conjectured sharp p2 constant.
- The construction parameters are fixed before taking k or t to infinity.
  No uniform bound as beta approaches2, b0 approaches1, or theta approaches
  an endpoint is asserted. Optimization over parameters is not performed here.
- Finitely many low coefficients may depend on eta and the endpoint covariance;
  they disappear at the large-time scale because their contribution is a finite
  power sum. They cannot be omitted if claiming an all-time pure exponential
  bound with this precise asymptotic constant.
- All-time STATIC homogeneity and a finite-order coefficient inequality are
  sufficient. Neither target raw singular-coefficient equality nor a uniform
  static large-time theorem in a smoothing parameter is required.
- This scalar deduction does not by itself validate any endpoint factorization,
  common-measure Hölder step, source identification or SPDE limit. Those remain
  the premises of the separately reviewed transfer argument.

No further source search, numerical experiment or canonical edit was needed
for this check.
