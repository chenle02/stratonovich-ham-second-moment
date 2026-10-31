# Fixed noise masks and displacement-moment transfer

COMPLETE CANDIDATE: not adopted before independent full proof review.
This is an internal positive-Wick consumer, not a new comparison method.
The original all-dimensional sharp second-moment goal remains ACTIVE.

## 1. Precise scope and inputs

Use original H:homog in d=1,2,3: a in(0,1), alpha+a<2,
0<alpha<d or alpha=d=1, and nonnegative even homogeneous positive-definite
tempered Radon Gamma. Data are (1,0). Fix rho=(epsilon,delta)>0 and the
actual source Y_rho of accepted source-operator-convergence.md Theorem2.
The family can use an auxiliary Gaussian extension retaining given W;
it need not be determined by W alone. Here only its exact joint source law
and its continuous-time, spatially smooth version for each fixed rho enter.

Named accepted inputs, not re-proved:
- Author p7 (2.3)-(2.5): positive displacement Green measures G_d(r,dz),
  supported in |z|<=r with mass r. In d3 these are sphere measures.
- Author p10 (2.13)-(2.16): ordered chain convention with X_0=1;
  p12 (2.19): finite Gaussian Wick formula, ALL pair partitions and odd zero.
- OWN canonical notes L:joint-fixed-order: arbitrary joint vertexwise noise
  width limits of the fixed-order diagrams, unequal/empty chains included,
  with Green smoothing removed first in d3. OWN P:mixed identifies their
  full diagonal sum with the original canonical moment E|u(t,0)|^2.
- OWN L:vertex-crude/E:vertex-crude: uniformly in x and all positive widths,
  the unmasked nth regularized integral has L2 norm <=q_n(t), where
  q_n(t)=exp(theta_0 t) C^(n/2)t^n/sqrt(n!) for n>=1,
  q_0(t)=exp(theta_0 t), and Q_T=sum_n q_n(T)<infinity.

We explicitly derive the full regularized moment limit below. It is NOT
imported as an already accepted source-solution consumer. No author-energy
normalization or sharp constant is an input.

Fix real m in C_c^infinity, 0<=m<=1. It multiplies the PHYSICAL source
coefficient after smoothing. Let X_(rho,n)^m(t,x) be its ordinary ordered
Duhamel integral, and X_(rho,n) the version with m=1. Both zero-order
terms are1. The conclusions are F1-F3 in the frozen target: all mixed-order
and full-solution two-point displacement expectations decrease under m;
positive averages are bounded by the full stationary point second moment;
any L2 limit of masked averages inherits this bound for canonical raw u.

## 2. Actual finite-chain integrals and Green-before-noise matching

For each terminal(t,x), let nu_n^(t,x) be the positive time-space chain
measure on 0<s_1<...<s_n<t, with successive spatial factors
G_d(s_(j+1)-s_j,dy_j), j=1,...,n, where s_(n+1)=t and positions are recovered
backward from x. This uses successive positive measures, not products of
sphere densities. Its mass, independent of x and d, is

             nu_n^(t,x)(1)=t^(2n)/(2n)!.                         (1)

Indeed mass at order0 is1. Integrating the latest vertex gives the recursion
f_n(t)=int_0^t(t-s) f_(n-1)(s)ds, which yields (1) by integrating monomials.
Measurability follows, for example, by writing each positive wave measure
as r times the pushforward under z->rz of its fixed unit-time probability
measure; d3 uses the unit sphere. No Green smoothing is necessary here.

Write c_rho=K_delta(0)Gamma_(2epsilon)(0)<infinity. The actual covariance is

 C_rho(s,z;r,w)=K_delta(s-r)Gamma_(2epsilon)(z-w)>=0,
                         |C_rho|<=c_rho.                       (2)

Nonnegativity uses the NONNEGATIVE Radon Gamma and positive heat kernel,
and K_delta>=0. The upper bound also follows by Gaussian Cauchy--Schwarz.
For each fixed finite N, Holder's inequality and scalar Gaussian moments
bound E product_(i<=N)|Y_rho(s_i,z_i)| by a finite constant depending only
on N,c_rho. Apply the same estimate to 2n factors to bound the L2 norm of
each n-fold source product uniformly in its vertices. Thus integration
against nu_n is a legitimate Bochner L2 integral. Source continuity gives
the needed strong measurability. This constructs X_(rho,n)^m and its
unmasked version and justifies stochastic Fubini for any two finite chains.

The unmasked integral is exactly the canonical regularized Y_n at common
noise widths, including the Green-before-noise convention. To check this
in d3, first mollify each Green measure by a positive heat approximate
identity. At fixed times, these finite positive spatial measures converge
weakly, with their masses unchanged. Every Wick covariance product at fixed
rho is bounded and continuous in all spatial vertices, by (2). The same
holds for mixed moments of smoothed and unsmoothed chain integrals. Their
spatial integrals therefore converge. For time integration, (2) times the
finite chain mass integrands is an integrable majorant, by (1). Both square
moments and the cross moment converge to the same unsmoothed diagram sum;
hence the smoothed random integrals converge in L2 to the integral just
constructed. This identifies it with the canonical Green-width limit.
The same argument works in d1/2 if smoothing is used. It does not assume a
samplewise bound on the source over the noncompact tails of a heat kernel.
Consequently the named unmasked q_n bound applies to this actual integral.

## 3. All mixed orders, including self-pairings

Fix n,k,t,x,y. If n+k is odd, Gaussian centering and Wick give zero for both
mixed expectations. If n+k=2l, combine the two positive chain measures.
For each pair partition D of all 2l vertices, stochastic Fubini gives the
unmasked contribution

        int product_({i,j} in D) C_rho(s_i,z_i;s_j,z_j)
                                   d(nu_n^(t,x) tensor nu_k^(t,y)). (3)

It is nonnegative and finite by (1)-(2). For the masked contribution the
integrand acquires exactly

                       product_(i=1,...,2l) m(z_i).               (4)

Every vertex appears once, irrespective of its partner or chain. Since
(4) lies in[0,1], each masked contribution lies between0 and its unmasked
counterpart. Sum over all pair partitions. This proves F1, including n=0
or k=0, all unequal orders and all self-pairings. For n=k=0 both terms
equal1. This proves the mixed-order displacement comparison.

In particular at x=y and k=n,

             ||X_(rho,n)^m(t,x)||_2<=q_n(t).                     (5)

There is no assertion of PSD ordering of the two Gaussian covariances,
samplewise ordering of their solutions, or monotonicity for signed wave
or arbitrary full-phase kernels.

## 4. Full source solutions and positive tested observables

Equation (5) and the unmasked bound give absolute L2 convergence of both
series, uniformly in x at each fixed t and uniformly in rho. Define their
sums u_rho^m(t,x) and u_rho(t,x). They are the actual ordinary mild solutions.
Here is the identification without a global source-supremum moment bound.

Fix rho and a compact observation set in[0,T]xR^d. On the probability-one
regularity event, the source is continuous and bounded on the compact
backward-cone enlargement of this set. Let M be that finite, sample-dependent
bound for |mY_rho| or |Y_rho|. Finite propagation keeps every chain within
the enlargement. Thus the absolute nth Picard term is bounded there by

                         M^n T^(2n)/(2n)!.                       (6)

The deterministic series converges uniformly on the compact observation
set. Each term is continuous, by the fixed-unit-wave-measure representation
and dominated integration, so its sum is locally continuous. Summing its
Volterra recursion is justified by (6) and gives the ordinary mild equation
with free displacement1 and zero initial velocity. Uniqueness among locally
continuous mild solutions follows by iterating the difference equation on
the same finite cone: if its supremum is B, the difference is at most
B M^n T^(2n)/(2n)! for every n, hence zero. The L2 partial-sum limit and
this pathwise limit coincide almost surely at each fixed(t,x), by an almost
sure subsequence of L2 convergence. These continuous solution versions may
be used simultaneously for all(t,x) at this fixed rho; no common null set
over uncountably many rho is claimed or needed. This proves identification.

For either solution, the double expectation series is absolutely convergent:

 sum_(n,k) E|X_(rho,n)^(m)(t,x)X_(rho,k)^(m)(t,y)|<=Q_t^2.         (7)

Cauchy--Schwarz and (5) prove (7), with the analogous unmasked bound.
Products of the partial sums converge in L1 by their L2 convergence.
Termwise F1 and (7) therefore give

 0<=E[u_rho^m(t,x)u_rho^m(t,y)]
                         <=E[u_rho(t,x)u_rho(t,y)].               (8)

Spatial stationarity of u_rho follows from the stationary Gaussian source
law and translation-covariance of the finite Picard integrals, then their
L2 limits. It is not asserted for u_rho^m. Cauchy--Schwarz now gives

       E[u_rho(t,x)u_rho(t,y)]<=E|u_rho(t,0)|^2.                 (9)

Let phi>=0 be smooth compactly supported. The locally continuous versions
are jointly measurable; their uniform pointwise L2 bound Q_t and separable
Bochner integration give actual L2 averages. Their second moment is the
double phi-weighted integral of the two-point expectation: absolute Fubini
is justified by ||phi||_1^2 Q_t^2. Multiply (8)-(9) by phi(x)phi(y) and
integrate to obtain

 E|int phi(x)u_rho^m(t,x)dx|^2
                      <=||phi||_1^2 E|u_rho(t,0)|^2.             (10)

The proof uses no point Sobolev evaluation in any dimension. It proves F2.

## 5. New full unmasked moment limit and conditional transfer

Fix t. At every fixed n,k, the exact common-rho source covariance in (2)
matches the canonical vertexwise source convention. Section2 supplies the
Green-before-noise identification. By OWN L:joint-fixed-order, each even
diagram tends to its finite canonical limit as epsilon,delta->0 at arbitrary
relative rates. Odd mixed moments remain zero. Hence the finite sum at
orders n,k tends to the canonical E[X_n(t,0)X_k(t,0)] of OWN P:mixed.
This requires only the single-rho diagram laws, not a new claim that the
canonical solution is a pathwise function of the entire auxiliary family.

The absolute mixed moments are uniformly bounded by q_n(t)q_k(t), whose
double sum is Q_t^2<infinity. Given any eta>0 choose a finite square of
orders with the double majorant outside that square <eta. On the square,
the finitely many diagram limits hold jointly at arbitrary cutoff rates;
outside it both the prelimit and canonical tails are bounded by eta.
Thus (7), the finite-square limit and OWN P:mixed prove

       lim_(epsilon,delta->0) E|u_rho(t,0)|^2=E|u(t,0)|^2.        (11)

This is a NEW written consumer of the accepted fixed-order and summability
inputs, not an imported earlier full-source theorem.

Finally suppose the masked average in (10) converges in L2 to A_m(t,phi),
either at arbitrary rates or along one specified sequence of widths both
tending to zero. Its second moment then converges: use
|E|B|^2-E|A|^2|<=||B-A||_2(||B||_2+||A||_2).
Take that limit in (10), using (11), to get

 E|A_m(t,phi)|^2<=||phi||_1^2 E|u(t,0)|^2.                      (12)

This proves F3. It assumes, rather than proves, existence of the masked
raw L2 limit; its identification with a W-measurable Young flow is a further
obligation. At unit phi mass, any lower bound for this tested observable
is a lower bound for the original canonical point second moment. Every
source limit here is at fixed t before time asymptotics.

## 6. Remaining goal and evidence limits

Finite positive-chain diagnostics test the pairing mechanism at orders0..4
on each chain in one actual admissible singular d2 model; they do not prove
the continuum comparison or certify quadrature accuracy. PSD and signed
observable negative controls are compatible with this restricted theorem.
No new finite-only Lean check would certify the Wick/measure/solution limit
arguments; the recorded 71 facts/18 seams and L0 status are unchanged.

The all-dimensional Young flow on constant initial data, actual masked raw
observable, compact-potential ground family and full-phase cone, Gaussian
tilt/event/cost and all-alpha variational comparison still need their own
gates. Even their completion would leave the sharp upper constant and
intended author-energy dictionary open. No main-goal completion, exact
limit, source repair, Skorohod development, private companion, HPC, contact,
TeX/PDF/wiki update or publication clearance is asserted.
