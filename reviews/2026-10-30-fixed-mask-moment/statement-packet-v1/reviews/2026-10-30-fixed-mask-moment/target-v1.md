# Fixed physical noise mask: displacement-moment transfer target

FROZEN STATEMENT TARGET ONLY. No new proof or theorem adoption yet.
Original full sharp p2 goal remains ACTIVE.

Use the full original H:homog class: d=1,2,3; a in (0,1);
0<alpha<d or alpha=d=1; alpha+a<2; Gamma nonnegative even homogeneous
positive-definite tempered Radon covariance, including invariant-direction
and singular measures. Zero Gamma is harmless. Data are exactly (1,0).
Use the SAME actual centered Gaussian source field Y_rho(t,x) from accepted
notes/source-operator-convergence.md, rho=(epsilon,delta)>0. Its joint law
is the author's Laplace-slice/heat law, not temporal convolution. At one rho,

 C_rho(s,x;t,y)=K_delta(s-t) Gamma_(2epsilon)(x-y)>=0 pointwise.

Fix m in C_c^infinity(R^d), real, 0<=m<=1, independent of time and rho.
No multiplier on the original noise Hilbert quotient is presumed. Its
physical location in the coefficient is m(x)Y_rho(t,x), AFTER smoothing.
The unmasked coefficient is Y_rho. Write X_(rho,n)^m(t,x) for the nth
ordinary ordered Duhamel integral with displacement Green measures G_d,
coefficient mY_rho, data (1,0), and X_(rho,0)^m=1. Write X_(rho,n) for
the unmasked version. Green kernels are UNSMOOTHED; in d3 interpret their
iterated products by successive integration of the positive sphere measures.

## F1. Every mixed-order displacement diagram

For ALL n,k>=0,t>=0,x,y in R^d,

 0 <= E[X_(rho,n)^m(t,x) X_(rho,k)^m(t,y)]
      <= E[X_(rho,n)(t,x) X_(rho,k)(t,y)].                 (F1)

Odd n+k gives zero on both sides. All pair partitions are retained,
including self-pairings within a chain and all unequal and empty chains.
Each term is a finite integral. In each even-order diagram the mask is
the product over ALL n+k physical vertices, independent of the pairing.
The claimed mechanism is positive Green measures and POINTWISE positive
source covariance, NOT positive-semidefinite covariance domination.

## F2. Full regularized solutions and positive averages

For every fixed rho,t,x, the two Picard series converge absolutely in L2.
The masked diagonal obeys the SAME uniform q_n(t) bound as the unmasked
diagonal in canonical notes L:vertex-crude/E:vertex-crude, for all rho,x.
Both sums agree pointwise almost surely with the locally continuous mild
solutions of the corresponding ordinary continuous-time, spatially smooth
potential wave equations with data (1,0). Unmasked source samples need only
be bounded on fixed compact backward cones, not on all of R^d. At fixed
rho this identification should use the bounded-cone Picard factorial bound
and L2 subsequences, not assume exponential moments of global source suprema.
Denote the sums u_rho^m and u_rho. Then

 0 <= E[u_rho^m(t,x)u_rho^m(t,y)]
      <= E[u_rho(t,x)u_rho(t,y)].                         (F2a)

For every real phi in C_c^infinity(R^d), phi>=0,
the Bochner averages exist and

 E|int phi(x)u_rho^m(t,x)dx|^2
       <= ||phi||_1^2 E|u_rho(t,0)|^2.                  (F2b)

Use spatial stationarity of the UNMASKED solution and Cauchy--Schwarz;
the masked solution is generally not stationary. No pathwise comparison
of the two solutions is claimed. Bounds hold for fixed t before asymptotics.

## F3. Conditional raw tested-observable transfer

The canonical notes L:joint-fixed-order plus uniform summable q_n imply
lim_(rho->0) E|u_rho(t,0)|^2=E|u(t,0)|^2, the original canonical
Stratonovich solution moment, at arbitrary relative cutoff rates. This is
a moment assertion from the accepted canonical construction and exact joint
source law, not an asserted new pathwise identification of all objects.

Suppose, on the retaining extension, SOME random variable A_m(t,phi) has

 int phi(x)u_rho^m(t,x)dx -> A_m(t,phi) in L2

as rho->0, or along one specified cutoff sequence with both widths going
to zero. Then

 E|A_m(t,phi)|^2 <= ||phi||_1^2 E|u(t,0)|^2.              (F3)

In particular unit-mass phi allows a lower bound for the full canonical
point moment from a FIXED-mask tested observable. Existence of this masked
raw limit, its identification with a Young flow, a local phase containing
constant1, tilted shifts, deterministic ground states, growing products,
and lower-bound rates/constants are NOT conclusions of this target.

## Boundaries and falsification obligations

No arbitrary-phase or velocity covariance monotonicity, PSD comparison,
positivity of a random solution sample, factorization across time blocks,
point evaluation from H^(1/2), raw physical-noise multiplier, or extension
outside positive-kernel dimensions is inferred. The proposed comparison
has NO claim of independent theorem novelty: it is an internal consequence
of familiar positive Wick diagrams needed at the actual moment consumer.

Finite controls use an ACTUAL admissible d2 covariance with an invariant
direction. Orders 0..4 on each chain (total up to8) include unequal/empty
chains and all pairings. They are finite positive quadrature controls,
not a certified approximation to the continuum PDE. Negative controls show
PSD covariance ordering fails and signed observables can reverse the order.
Sharp upper and lower constants/source normalization remain open; no Lean
upgrade, companion, HPC, contact, source repair or publication transaction.
