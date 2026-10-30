# A weighted scalar frequency row under translated spectral growth

COMPLETE CANDIDATE, not adopted before independent full proof review.
This is an analytic measure estimate. No actual Gaussian operator variance,
Schatten norm, time path, Young flow or moment asymptotic is identified.

## 1. Explicit hypotheses and target

Let d in {1,2,3}, a=alpha_0 in (0,1), 0<alpha<d or alpha=d=1, and
alpha+a<2. Suppose a positive Radon measure nu on R^d satisfies

    nu(B(y,r)) <= C r^alpha  for every y and r>0,                     (1)

with C>=0. No density, evenness, homogeneity or physically nonnegative
inverse covariance is assumed. Closed balls satisfy the same bound if
initially only open balls were meant: enclose the closed ball in radius
r+epsilon and take epsilon down to zero in the numerical upper bound.
Fix

    0<gamma<min(1/2,(2-alpha)/2),  epsilon=1-2gamma>0.

Use <z>=sqrt(1+|z|^2). For 0<h<=1 define the nonnegative extended integral

 J_h(xi)=<xi>^(2gamma) int
  [<h(|xi|-|eta|)>^(a-1)+<h(|xi|+|eta|)>^(a-1)]
                      /(<xi><eta>) nu(d(xi-eta)).                   (2)

The notation denotes eta=xi-lambda, lambda distributed according to nu;
it does not posit a density or use a Jacobian. Write

 B_alpha(h)=1                       if alpha<1,
            1+log(1/h)              if alpha=1,
            h^(1-alpha)             if alpha>1.                     (3)

**Proposition 1.** There is a finite K=K(alpha,a,gamma), independent of
d,nu,C,h,xi, such that

    sup_xi J_h(xi) <= K C B_alpha(h).                               (4)

The zero measure case is immediate. If C=0, (1) forces nu=0 by covering
R^d with countably many finite balls, so it is included.

## 2. Inverse-Bessel integrals on expanding translated balls

For each xi, denote the pushforward in eta by nu_xi. From (1),
nu_xi(B(0,R))<=C R^alpha. For q>=1 put

    A_xi(q)=int_{|eta|<=5q} <eta>^-1 nu_xi(deta).

Let N=ceil(log_2(5q)), so 5q<=2^N<10q. Split into the unit ball and the
annuli 2^j<|eta|<=2^(j+1), j=0,...,N-1. The unit ball contributes at most
C. Each annulus contributes at most 2^(-j) C 2^((j+1)alpha). Consequently

    A_xi(q)<=C[1+2^alpha sum_{j=0}^{N-1}2^(j(alpha-1))].            (5)

All steps apply to singular measures, since only mass bounds were used.
For alpha<1, the sum is at most 1/(1-2^(alpha-1)). For alpha=1, it is N,
which is at most log_2 q+log_2 5+1. For alpha>1 it is at most
2^(N(alpha-1))/(2^(alpha-1)-1), and 2^N<10q. Thus there is finite
K_alpha independent of xi,d,nu such that

 A_xi(q)<=K_alpha C * [1               if alpha<1;
                       1+log q        if alpha=1;
                       q^(alpha-1)    if alpha>1].                 (6)

These estimates are proved directly; no integrability theorem is imported.

## 3. The near-frequency contribution

Fix xi and q=max(1,|xi|); q <= <xi> <= sqrt(2)q. Split the lambda integral
in (2) into |lambda|<=4q and |lambda|>4q. On the near region,
|eta|=|xi-lambda|<=5q. Each bracket to exponent a-1 is at most 1, because
a-1<0. Therefore the near contribution is bounded by

    2<xi>^(-epsilon) A_xi(q) <=2q^(-epsilon) A_xi(q).                (7)

For alpha<1, (6) makes this at most a constant times C since q>=1.
For alpha=1, put u=log q>=0. Then

 q^(-epsilon)(1+log q)=exp(-epsilon u)(1+u)
                    <=1+1/(e epsilon),

because u exp(-epsilon u) has maximum 1/(e epsilon), obtained by a direct
derivative calculation. For alpha>1, (7) is bounded by a constant times
C q^(alpha+2gamma-2), and the exponent is negative by the stipulated gamma
range. Thus in all cases the near contribution is at most K_near C,
uniformly over h,xi,d. This includes all small and resonant frequencies;
no oscillatory decay was needed on this region.

## 4. The far-frequency contribution and the time scale

Write r=|lambda|>4q. Then

 |eta|>=r-|xi|>=3r/4,
 ||eta|-|xi||>=r-2|xi|>=r/2,
 |eta|+|xi|>=3r/4>=r/2.

For either oscillatory frequency omega in (2),
<h omega> >= (1/2)<hr>. Since a-1<0, its power is at most
2^(1-a)<hr>^(a-1). Also <eta>^-1<=4/(3r) and
<xi>^(-epsilon)<=1. The far contribution is consequently at most

    (4/3)2^(2-a) int_{|lambda|>4q}
                       |lambda|^-1 <h|lambda|>^(a-1) nu(dlambda).

Enlarge the domain to |lambda|>1. On the dyadic annulus
2^j<|lambda|<=2^(j+1), the inverse radius is at most 2^(-j) and the
negative-power bracket is at most <h2^j>^(a-1). Bound its mass by
C 2^((j+1)alpha). Thus the far term is at most a constant depending only
on alpha,a times C S(h), where

    S(h)=sum_{j=0}^infinity 2^(j(alpha-1))<h2^j>^(a-1).             (8)

There is no hidden density or angular integration in this shell estimate.
Choose L=floor(log_2(1/h))>=0, so 2^L<=1/h<2^(L+1). For j<=L bound
the bracket power by 1. For j>=L+1 bound it by (h2^j)^(a-1). The latter
geometric series converges because alpha+a-2<0, and has sum

 h^(a-1) 2^((L+1)(alpha+a-2))/(1-2^(alpha+a-2))
       <= h^(1-alpha)/(1-2^(alpha+a-2)).                            (9)

The last inequality uses 2^(L+1)>1/h and the NEGATIVE exponent
alpha+a-2, so its direction is as displayed.

For the finite low-frequency sum: if alpha<1, it is at most
1/(1-2^(alpha-1)); if alpha=1 it equals L+1<=1+log_2(1/h); if alpha>1
it is at most

    2^(alpha-1)h^(1-alpha)/(2^(alpha-1)-1).

Together with (9), and h^(1-alpha)<=1 in the alpha<1 case, these give
S(h)<=K_far B_alpha(h). Combining with (7), and using B_alpha(h)>=1,
proves (4) and finiteness of the original nonnegative integral. Every
constant arose from numerical shell bounds involving alpha,a,gamma, so
none depends on d. This proves Proposition 1.

## 5. Scalar time consequence strictly above one half

**Corollary 2.** For any beta with

    1/2<beta<min(1-a/2,(3-a-alpha)/2),

there is finite K_beta depending on alpha,a,gamma,beta such that

    h^(2-a) sup_xi J_h(xi) <=K_beta C h^(2beta),  0<h<=1.           (10)

*Proof.* The beta interval is nonempty: a<1 makes 1-a/2>1/2, while
alpha+a<2 makes (3-a-alpha)/2>1/2. If alpha<1, (4) times h^(2-a) has
exponent 2-a>2beta. If alpha>1 its exponent is 3-a-alpha>2beta. Powers
of h in (0,1] decrease when their exponents increase, so (10) follows in
both cases. If alpha=1, put delta=2-a-2beta>0. For u=log(1/h)>=0,

 h^delta(1+log(1/h))=exp(-delta u)(1+u)<=1+1/(e delta).

Apply this to the critical logarithm in (3). No endpoint beta is claimed.
This proves Corollary 2.

## 6. Model use, diagnostics and limits

From the separately accepted spectral-mask-covariance-foundation.md,
Proposition 2, the actual auxiliary nu_R satisfies the NAMED hypothesis
(1) with C=c_d^2 L_zeta^2 C_Gamma, uniformly over R>0. That is the full
input required for this analytic estimate; no physical positivity of the
inverse auxiliary covariance or stationarity of the actual masked noise
has been assumed. Corollary 2 alone is not a Gaussian increment estimate
until the actual four-component phase covariances are derived and matched.
It proves no Schatten/path regularity or flow theorem.

The original diagnostic v1 omitted lambda=2|xi| while incorrectly claiming
all resonances were split. Its genuine independent FAIL/HIGH report is
retained. Corrected v2 explicitly splits that resonance and its width1/h
neighbors;12 d1 quadratures at30/50-digit working precision agree within
1e-10. This is not certified quadrature accuracy. C=2/alpha is recorded
for those full-line spectral densities; raw J/B is not J/(CB). Separate15
xi0 radial-mass controls have angular mass1 (centered mass r^alpha/alpha),
with alpha1.25 in d2/3. They are spectral measures, not physical covariance
formulas. No nonzero-xi alpha>1, singular-measure or near-threshold numerical
coverage was claimed; those cases follow from the proof's measure bounds.
No numerical string is quoted as a theorem constant or certified digits.

Still open: actual temporal modulation/continuous low modes, both Gaussian
operator variance directions, localized Schatten moments and source tails,
Banach-valued time path and fixed-space causal flow, source compatibility,
all-dimensional lower bounds, sharp upper constants and source variational
normalization/domain/label issues. Original full goal remains active.
No new Lean formal coverage, official companion, Skorohod result, contact,
HPC, canonical TeX/PDF/wiki edit, public release or whole-paper clearance.
