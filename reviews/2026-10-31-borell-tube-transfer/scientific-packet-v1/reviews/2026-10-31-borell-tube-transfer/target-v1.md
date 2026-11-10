# BT1-BT3: exact Gaussian tube and Rayleigh transfer for the actual E law

FROZEN UNREVIEWED STATEMENTS before diagnostics or proof. This is a
Gaussian-input transfer component of the original all-model sharp-point
program. It does NOT assert the missing sharp nonlinear wave envelope.
The earlier conditional route plan is not a premise.

## BT1. Exact raw-control tube geometry and radial expectation bound

Fix 0<delta<1. Let H be a real separable Hilbert space, W its isonormal
process, and X a centered strongly measurable Gaussian variable in a real
separable Banach space B, with E||X||^2<infinity. Every continuous linear
coordinate of X belongs to the first chaos of the GIVEN W. Let
 L h=E[X W(h)]=sqrt(delta) K h,
where K:H->B is bounded and compact. Define H_seen as the closed span of
the coordinate labels k_l, so ker L=H_seen^perp. Work on the actual support
B0=closure L(H), with the genuine abstract Wiener realization
 H_CM=L(H_seen), ||Lh||CM=||P_seen h||H.
This realization must be proved/checked in the actual application, not
inferred from a covariance norm bound alone. Compactness is at EACH
fixed delta; no uniform compactness of a moving family is assumed.

Put b=2E||X||, A={x inB0:||x||<=b}. For the zero law use the elementary
case separately. Otherwise b>0 and mu(A)>=1/2. Let closed raw balls have
radius r>=0 and define
 T_r=A+K(Ball_H(r)), D(x)=inf{r>=0:x inT_r}, infempty=infinity.
Propose: T_r is closed/Borel, {D<=r}=T_r, and D is measurable and finite
almost surely. Because K kills unused raw directions, its ball image is
exactly the seen-ball image. The TRUE CM unit ball is
 sqrt(delta)K(Ball_H(1)), hence PRIMARY Friz-Hairer Theorem11.6 would give
 P(D(X)>r)<=barPhi(Phi^-1(mu(A))+r/sqrt(delta))
                         <=exp(-r^2/(2delta)).             (BT1a)
Do not replace exact raw geometry by its embedding upper bound and lose
an extra constant in the action. Resolve the source measurability footnote
using compact ball images and the closed A, not an unproved outer measure.

For Borel F:B0->R and a Borel nondecreasing finite G:[0,infinity)->R with
 F(x)<=G(r) for EVERY r>=0 and EVERY x inT_r,
propose, allowing an infinite right side,
 E exp(F(X)/delta)
 <=int_0^infinity (r/delta) exp((G(r)-r^2/2)/delta)dr.        (BT1b)
D is stochastically DOMINATED BY a Rayleigh radius whose density is
(r/delta)exp(-r^2/(2delta)). Prove attainment at the least radius and
monotone expectation comparison, including possible jumps of G, zero law
and unused raw directions. No finite Gaussian density on H is used.

## BT2. Exact eligibility and wave functional on the ORIGINAL E block law

Keep ALL original Gamma/amplitudes, d=1,2,3,0<a<1,alpha+a<2,
0<alpha<d or alpha=d=1, and the accepted source/driver exponent ranges.
E=H1/2 x H-1/2 (real, inhomogeneous Bessel, unitary Fourier).
Fix integer B>=1, 0<delta<min(1,1/B), R=delta^-1+2, L=1/delta,
true lengths ell_m, s_m, N,n as in accepted C3. Choose
 1/2<theta<min(1-a/2,(3-a-alpha)/2), nu=1/theta,
 1/(1-theta)<r_t<2/a, nu<=p<2<r_t.
The physical noise mask is eta(x/R)^2 ONCE, after any source smoothing.

Use full noise, not a projected residual:
 X_m=g_delta M_R(W composed with T_(delta,m)),
 g_delta=delta^((1-a)/2), stopped at ell_m and constantly extended to B.
Let X_delta=(X_m) and the Banach norm be
 ||x||_(delta,p)=(delta sum_m||x_m||Ctheta(B(E))^p)^(1/p).
Use a separable little-Holder/closed span supporting this ACTUAL Gaussian
tuple, not all of the generally nonseparable Ctheta(B(E)). Its raw space
is the closed supported H_I, not a time-indicator quotient construction.
The actual completed mean map is
 (K_delta Phi)_m(u)=int_0^min(u,ell_m)
   S_E(-v)mathcalT_(R,E)Phi(s_m+delta v)S_E(v)dv.
Propose the exact identity
 E[X_delta W(Phi)]=sqrt(delta)K_delta Phi,
compactness of K_delta at each FIXEDdelta/R, its genuine CM/seen-space/AWS
realization, and all BT1 hypotheses. Use accepted C2/C3, U actual covariance,
SA moments and explicit E/F compression; no F constant-column norm budget.
Accepted SA gives b_delta=2E||X_delta||->0. The family is NOT assumed to be
sqrt(delta) times a fixed Banach Gaussian law; K_delta and the space vary.

Define on ALL tuple inputs the continuous Young product
 mathcalP_delta(x)=product_(m=N,...,0)[S_E(ell_m)U_(x_m)(ell_m,0)],
 F_delta(x)=2delta log max(1,||mathcalP_delta(x)||B(E)).
Propose that the ACTUAL full-noise tuple reproduces GC's global E endpoint
by noise-only raw restart (including both velocities and the true final
block), so SP gives F_delta(X_delta)=2delta log||P_delta||. No independent
blocks, new spectral flow or pathwise canonical point evaluation is used.

Let G_delta(r)=sup{F_delta(a+K_delta Phi):a inA_delta,||Phi||H_I<=r}.
Propose it is finite and nondecreasing (therefore Borel), and BT1b applies
EXACTLY to E||P_delta||^2. Generic Banach Young growth plus accepted uniform
E mean Lr budget should give, for fixed B,
  G_delta(r)<=C_B[1+b_delta^nu+r^nu], 1<nu<2,               (BT2c)
uniformly R>=1,delta small. Prove this using the ACTUAL delta-weighted
norm, p>=nu,r_t>nu,delta*n<=2/B, true partial/empty blocks, and the
uniform mean primitive r_t budget; no unproved spectral-rate envelope.
The inequality is coarse and is not called the sharp upper constant.

## BT3. Exact tail budget and preservation of the half action

If G(r)<=A+C r^nu with A real,C>=0,1<nu<2, M>0 and
4C<=M^(2-nu), propose the explicit Rayleigh tail bound
 int_M^infinity (r/delta)exp((G(r)-r^2/2)/delta)dr
                         <=4exp((A-M^2/4)/delta).          (BT3a)
Reuse COMPLETE old GaussianTail.cutoff_density_split at x=r>=M with its
actual guards, then analytically integrate r/delta exp(-r^2/(8delta)).
The front constant4 and exponent M^2/4 must both be checked. This is a new
application of an old scalar kernel, not a Gaussian/measure theorem in Lean.

For any finite J:H->R bounded above on each raw ball, propose the exact
extended supremum identity
 sup_(r>=0)[sup_(||Phi||<=r)J(Phi)-r^2/2]
              =sup_Phi[J(Phi)-||Phi||^2/2].                (BT3b)
No compactness, rank or Gaussian density is needed for this order identity.
Later choosing J=2Rate_R requires a NEW uniform deterministic spectral/
product envelope and its own tail/limit gate. It is NOT a premise proved
by BT1-BT3. Signed-positive score, source normalization and exactlimit stay
OPEN. No sourceL identity or actualp1 label comparison is assumed.

## Falsification and evidence boundary

Before proof: direct scalar Gaussian MGF and direct Rayleigh integrals at
two precisions, zero-slope normalization, wrong half-action/CM-scale guards;
finite degenerate Gaussian matrices with explicit seen projections and
unused directions; exact Gaussian-cell formulas for polynomial versus
exponential counts, showing when the required expectednorm premise fails.
These are genuine finite Gaussian tests, not PDE simulations or proofs of
the actual infinite-dimensional eligibility. No clipping or statistical
confidence intervals; floating agreement is not a certified enclosure.

Use held PRIMARY Friz-Hairer2020 Theorem11.6 printed190 with the actual
measurability footnote; no finite-dimensional-independent roughpath theorem
or generalized Fernique norm-only substitution. Freeze a source/statement/
oldfinite-application packet and obtain independent Opus5.5/HIGH feasibility
review BEFORE long proof; then FULL proof gate before adoption/successor.
No new Lean/compiler/count (74facts20seams/L0), companion, HPC, contact,
Skorohod, source repair, TeX/PDF/wiki/bib or public-release action. Retain
the original all-model sharp goal ACTIVE, not a Gaussian-only replacement.
