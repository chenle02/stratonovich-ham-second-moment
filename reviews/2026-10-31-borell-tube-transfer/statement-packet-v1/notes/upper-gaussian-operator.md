# Actual Gaussian operator upper on a fixed spatial mask

ACCEPTED at the scoped FULL analytic/source/type/actual-application gate:
scientific180bf1a,18groupedchecks/HIGH335.531seconds,no requiredrepairs.
Five optional clarity notes adjudicated in
reviews/2026-10-31-upper-gaussian-operator/scientific-adjudication-v1.md.
Frozen proof/report unchanged. One finite tail fact also passed its exact
FULL type/application gate. FixedR OPERATOR second-moment upper only;
original unmasked point/sharp-source goal remains ACTIVE/OPEN.

## 1. Objects, exact claim and direct accepted inputs

Use ALL original H:homog nonzero Gamma/amplitudes,d=1,2,3,
0<a=alpha_0<1,0<alpha<d or alpha=d=1,alpha+a<2. The zero covariance case
is treated separately below. Fix physical m_R=eta_R² ONCE, R>0. Use the
actual real phase F=E directsum R²,E=H1/2xH-1/2, both constant columns and
S_F from fixed-mask-young-constant-phase.md. Let H=H_I be the supported raw
Hilbert space onI=(0,1), W the GIVEN isonormal process. Choose fixed
 1/2<theta<min(1-a/2,(3-a-alpha)/2),
 1/(1-theta)<r<2/a, nu=1/theta<=p<2<r.

For0<delta<1, define W_fast(f)=W(T_(delta,0)f) using the accepted isometric
raw pullback, and g_delta=delta^((1-a)/2). On the global fast horizon
L=1/delta let D_delta=g_delta A_R(W_fast) be the ACTUAL interaction first
driver, and define
 P_delta^R=S_F(L)U_(D_delta)(L).
This definition involves neither auxiliary block lengthB nor rankJ.

Direct OWN accepted inputs, not broadly recertified:
- C3, upper-cameron-compactness.md: supported H, FIRST-J ONbasis e_j and
  projections P_J,Q_J, compact T:H->Lr(I;K(F)), actual covariance/head paths.
- D1, upper-residual-exponential.md: actual residual norm Y_delta,J and
  G_delta,J(B,eta)=E exp(eta Y_delta,J^nu/delta)<infinity, for every eta>0;
  this is a scalar expectation, distinct from E4's head vector G or G_B;
  lim_(J->infinity)limsup_(delta->0)delta log G_delta,J(B,eta)=0 at FIXEDB.
- E1-E4, upper-young-perturbation.md: physical fullhead+residual identity,
  joint Borel maps, Q_J/head independence, conditional ratio at q2 with
  R_delta,J(B,M)<infinity and its same iterated normalized log limit0.
- S1-S4, upper-signed-static.md: actual signed spectral rate lambda(L)>=0,
  lambda(L)<=max(1,||L||), Rate(Phi)=int lambda(T Phi(s))ds continuous.
- B1-B3, upper-mean-block-product.md: explicit crude C_theta B bound,
  C_B<=32B^(3-1/r), actual mean r-budget, polynomial-ball product upper.
- raw-block-event-lower.md Section7(19)-(23), source-operator-convergence.md
  Theorem1 and the fixed-mask phase: actual same-source/raw noise-only
  restart, not the Psi-dependent positive shift or ground-family argument.

Define the OWN score over ALL signed raw controls

 S_R_all=sup_(Phi in H)[2Rate(Phi)-||Phi||H²/2].              (1)

**Claim GL.** The actual endpoint norm is Borel,
 1<=E||P_delta^R||B(F)²<infinity for every delta in(0,1),
 0<=S_R_all<=2+2||T||²<infinity,

 0<=limsup_(delta->0)delta log E||P_delta^R||B(F)²<=S_R_all. (2)

No equality with a point moment, actual first mean, source L^* or a positive-
control score is asserted. ||T|| always means H->Lr(I;K(F)), with the actual
amplitude and covariance norm. No infinite-dimensional Gaussian density.

## 2. Actual global restart, Borel norm and the finite head

Fix an integerB>=1 and0<delta<min(1,1/B). Use N=floor1/(delta B),n=N+1,
true lengths ell_m=B for m<N,ell_N=L-NB in[0,B),s_m=m delta B. Every local
path is stopped at ell_m and constantly extended on[0,B]. To recall the
exact accepted NOISE-ONLY source argument, use one retaining slow source
and its fast pullback on[0,(N+1)B]. Ordinary source responses satisfy

 S_F(mB)[D_glob^src(mB+u)-D_glob^src(mB)]S_F(-mB)
                                          =X_m^(full,src)(u).

It is just a change of integration variable in the interaction integral
and composition of free groups; no mask commutation. Actual Gaussian
transfer of the SAME sources gives global/local Ctheta convergence before
any delta limit, at this fixed finite horizon. Restriction, difference and
bounded fixed conjugation pass this to the RAW paths (raw-block(21)).
Young Riemann sums/uniqueness then give physical restart(22), hence

 P_delta^R=P_N^full(ell_N)...P_0^full(B)                    (3)

almost surely for this fixed delta,B. Its proof uses only the valid fixed
mask and noise-only source identities, not any positive Psi/eligible-ground
condition from the lower consumer. Current m_R=eta_R² satisfies those mask
conditions. The finite source horizon may depend on delta, but the source
limit is taken first; no uniform conjugation bound in delta is assumed.
Restricting to L gives the already defined global P_delta^R, regardless of
the auxiliary extension, B or J. No event for all uncountably many delta
or source parameters is needed for these expectation inequalities.

For FIRST J supported raw basis vectors put
 Phi_delta,J=sqrt(delta)sum_(j<=J)W(e_j)e_j.
Accepted E2(5) says, simultaneously for this finite tuple,

 X_m^full=H_m(Phi_delta,J)+X_m^res,                          (4)

on the SAMEW, including BOTH columns. Here X_m^res is the Q_J residual,
not the old lower-note full X_m. The scalar normalization is also the
unchanged old JointTilt.shifted_amplitude with delta>0,a=alpha_0:
g_delta delta^(a/2)=sqrt(delta). That kernel fact certifies scalar powers
only; the actual covariance/Bochner identity is the C3/E2 input.

The residual tuple is measurable in the completed Q_J Gaussian field and
independent of (W(e_j))_(j<=J), by E4; timeblocks can remain correlated.
For J>=1 the coordinates phi_j=sqrt(delta)W(e_j) have the EXACT density

 (2pi delta)^(-J/2) exp(-|phi|²/(2delta)) dphi,              (5)

and ||sum phi_j e_j||H=|phi|. This uses only finite independent standard
normal coordinates of an isonormal process, not an H-valued Gaussian.
The J0 head is0, with no density integration.

The global driver is a strongly measurable Gaussian compact-valued path
in a separable little-Holder/closed path span, by actual Gaussian transfer
and the F extension. The Young endpoint map is norm-continuous there.
Also U_D(L)-I is compact: its Young sums are finite sums of compact
increments times bounded operators, converging in operator norm, and K(F)
is closed. Thus P_delta^R lies in S_F(L)(I+K(F)), a separable affine image.
In particular its norm is Borel; equivalently evaluate it on a countable
dense unit set of F, not the largest matrix entry.

The driver values have range in closed iE, so applying pi_C to Young sums
gives pi_C U_D=pi_C (fixed-mask(8)). Therefore
 pi_C P_delta^R=tau(L)pi_C, tau(t)=[[1,t],[0,1]].
The unit constant-displacement input e_disp has output constant coordinate
(1,0), so ||P_delta^R||>=1. This is not positivity of the random potential.
Finiteness is proved in Section4, before asymptotic arguments.

## 3. Score coercivity and the finite scalar tail lemma

Rate(0)=0 because lambda(0)=0, so S_R_all>=0. On the unit slow interval,
L1<=Lr and S4's growth bound (from S2's lambda<=K) give
 Rate(Phi)<=1+||T Phi||L1<=1+||T||||Phi||H.
For q=||Phi||H and t0=||T||,
 2Rate(Phi)-q²/2<=2+2t0q-q²/2
                =2+2t0²-(q-2t0)²/2<=2+2t0².              (6)
This proves finiteness in(1) with the EXACT half action from(5).

The following finite inequality is locally kernel-checked in
lean-progress/local-checks/gaussian-tail-v1/, with exact frozen public type:
if M>0,x>=M,C>=0,1<nu<2 and4C<=M^(2-nu), then

 Cx^nu-x²/2<=-M²/8-x²/8.                                  (7)

For a self-contained scalar proof, 2-nu>0 gives
4C<=M^(2-nu)<=x^(2-nu). Multiplying by x^nu>=0 and using positive-base
power addition gives4Cx^nu<=x². Consequently the left side<=-x²/4,
which is<=-M²/8-x²/8 because x>=M>0. This proves(7), including C0.
The local Lean source verifies exactly this finite implication; Gaussian
integration, the eventual cutoff and all analytic applications remain
separate obligations, checked below and by the pending FULL gate.

## 4. A coarse bound valid on the ENTIRE unbounded head

For arbitrary Phi in H and zero-started operator Ctheta paths x_m define
 P_m(Phi,x_m)=S_F(ell_m)U_(H_m(Phi)+x_m)(ell_m),
 v_m=||x_m||theta,y=(delta sum v_m^p)^(1/p),
 a_m=C_B delta^(-1/r)||T Phi||Lr(I_m).
No additional 'compatibility' property is needed for the coarse estimate;
actual residuals also satisfy pi_C x_m=0. B1 and the two-entry power mean
with exponent nu>=1 give

 delta log product_m||P_m(Phi,x_m)||²
 <=2C_theta B[delta n+2^(nu-1)delta sum_m(a_m^nu+v_m^nu)].   (8)

All factors are positive: Young evolutions and S_F are invertible. Use the
same COMPLETE existing Mathlib finite powermean type for this two-entry
step, and for the finite Holder steps below. Exponent r/nu>1 on a_m^nu
and exponent p/nu>=1 on v_m^nu give

 delta sum a_m^nu
 <=(2/B)^(1-nu/r) C_B^nu||T||^nu||Phi||^nu,
 delta sum v_m^nu<=(2/B)^(1-nu/p)y^nu.                      (9)

Values nonnegative, n>=1,delta>0, and every reciprocal power is positive;
zero values are safe and nu=p is equality in the second inequality. This
is an exact actual application of the retained general finite type, not
new kernel probability content. Since delta n<=2/B and C_B<=32B^(3-1/r),
(8)-(9) give

 delta log product_m||P_m(Phi,x_m)||²
 <=A0+A1 B^(3nu)||Phi||^nu+eta_B y^nu,
 A0=4C_theta,
 A1=2^(nu+1-nu/r)C_theta32^nu||T||^nu,
 eta_B=2^(nu+1-nu/p)C_theta B^(nu/p).                       (10)

These A0,A1 are target GL2's C0,C1; they are DISTINCT from D1's CM
coefficient C0. In particular A1>=0 (possibly0) and eta_B>0, and none of
these coefficients depends on J,delta or an unbounded head realization.
Only the crude global B1 bound was used, not local E1 constants.

Take B=1, J=0 and Phi=0. Then (3)-(4),(10), submultiplicativity and D1 imply
 E||P_delta^R||²<=exp(A0/delta)G_delta,0(1,eta_1)<infinity
for EVERY delta in(0,1). Combined with Section2 this completes GL1.

## 5. Bulk head: actual conditioning and finite-dimensional integration

For B,M fixed let Err_delta(B,M) (target E_delta(B,M)) be the positive part of the deterministic
supremum of delta sum log||P_m^0(Phi)||-Rate(Phi) over||Phi||<=M. It is
finite by the B1/mean budgets. The underlying functions are continuous in
Phi (bounded primitives, continuous Young maps, baseline norms>=1 and S4
Rate), so the supremum is deterministic, also representable over a countable
dense ball. No random supremum is moved across expectation.

Let R_delta,J(B,M) denote E3 at q2, with supremum OUTSIDE expectation. From
(3)-(4), the actual norm is bounded by max(1,z) times the product of mean
physical norms. Apply E4's Borel freezing/conditional inequality given the
finite head. On its ball, the square of that mean product is at most
exp((2Rate(Phi)+2Err_delta)/delta). Thus for J>=1, with b_J(M) the ordinary
Euclidean ball volume,

 Bulk_delta,J(B,M):=E[1_(||Phi_delta,J||<=M)||P_delta^R||²]
 <=R_delta,J(B,M)(2pi delta)^(-J/2)
   int_(|phi|<=M) exp((2Rate(sum phi_j e_j)-|phi|²/2
                                      +2Err_delta(B,M))/delta)dphi
 <=R_delta,J(B,M)(2pi delta)^(-J/2)b_J(M)
                       exp((S_R_all+2Err_delta(B,M))/delta). (11)

The joint integrand is Borel by E4 and the mean flow continuity, and the
conditional version is its one Borel integral against the independent
residual law. No intersection of uncountably many head-null sets is used.
The subset span{e_1,..,e_J} lies in H, so its score is bounded by(1). This
is a finite integral upper bound, not an infinite-dimensional/unbounded
Laplace principle or an exchange with a pointwise delta limit.
For J0 use prefactor1 and Phi0; (11) remains an upper bound because S>=0.

## 6. Tail head: actual cutoff, density split and normalization

Choose ANY fixed M0>0 and m>3nu/(2-nu), let M_B=M0B^m. For every integerB
satisfying
 4A1 B^(3nu)<=M_B^(2-nu),                                  (12)
and every0<delta<min(1,1/B), we claim the finite tail bound below. If A1=0,
(12) holds for everyB without division. If A1>0, its ratio is a positive
constant times B^(m(2-nu)-3nu), so (12) holds for ALL sufficiently largeB.
The exponent is positive by the strict m choice.

By(10) and actual head/residual independence,

 Tail_delta,J(B):=E[1_(||Phi_delta,J||>M_B)||P_delta^R||²]
 <=exp(A0/delta)G_delta,J(B,eta_B)
 E[1_(||Phi_delta,J||>M_B)
                         exp(A1 B^(3nu)||Phi_delta,J||^nu/delta)].

For J>=1 insert the density(5), and apply the EXACT finite lemma(7) with
 C=A1 B^(3nu), M=M_B, x=|phi|.
Here M>0, x>M, C>=0,1<nu<2 and the cutoff(12) are the actual public
hypotheses; none is the desired conclusion. Division by delta>0 and
monotonicity of exp give the scalar density split. Extending the remaining
integral to ALL R^J yields

 HeadTail<=exp(-M_B²/(8delta))(2pi delta)^(-J/2)
                             int_RJ exp(-|phi|²/(8delta))dphi
         =2^J exp(-M_B²/(8delta)).

The equality is the product of one-dimensional Gaussian integrals; the
normalizer ratio is (8pi delta)^(J/2)/(2pi delta)^(J/2)=2^J. Therefore

 Tail_delta,J(B)<=2^J exp((A0-M_B²/8)/delta)
                                      G_delta,J(B,eta_B). (13)

Keep the rank-dependent factor until the delta limit at FIXEDJ. The J0
tail is empty and equal0; its logarithm can be read as -infinity. D1 gives
the finite residual expectation at every fixed eta_B, including zero-law
cases; no source-error or physical-block independence was asserted.
This proves both GL2 bounds and the exact actual use of the finite kernel.

## 7. The three limits on ONE actual operator moment

Let L_R=limsup_(delta->0)delta log E||P_delta^R||² in[0,infinity]. For each
fixed largeB choose the radius M_B above and a threshold s satisfying
s>r(3+m)/(r-nu), as required by B3. The quantitative B2 bound with K_B=B^s
provides nonnegative epsilon_B->0 such that
 limsup_(delta->0)Err_delta(B,M_B)<=epsilon_B.                 (14)
Each radius is FIXED for that inner delta limit; no compactness on unbounded
balls or simultaneous B_delta limit is involved.

At fixedB,J>=1 split the finite expectation into(11) and(13), and use
 log(u+v)<=log2+max(log u,log v),
with the extended log0 convention when needed. In the INNER delta limit,
 delta log[(2pi delta)^(-J/2)b_J(M_B)]->0,
 delta Jlog2->0,
so the bounds imply

 L_R<=max(S_R_all+2epsilon_B+r_J(B), A0-M_B²/8+d_J(B)),
 r_J(B)=limsup_delta delta log R_delta,J(B,M_B),
 d_J(B)=limsup_delta delta log G_delta,J(B,eta_B).           (15)

Finiteness at each fixedJ follows from upper-young-perturbation.md
Section6(19) and D1(3)-(4). They are nonnegative upper rates, with limits0
as J->infinity by
E3 and D1. Crucially M_B,eta_B are fixed during that rank limit. P_delta^R,
and hence L_R, has no J or B in its definition. It is the SAME left side
for every bound in(15), not a family changed along an auxiliary sequence.
Thus let J->infinity in the right side to obtain
 L_R<=max(S_R_all+2epsilon_B,A0-M_B²/8).
This also proves finiteness of L_R. Finally integerB->infinity gives
M_B->infinity and epsilon_B->0, while S_R_all is finite. The right side
tends to S_R_all, proving(2). Its lower bound follows from norm>=1.
This proves GL3 for nonzero Gamma, with order delta, thenJ, thenB.

For Gamma0 the driver/H/T vanish, S_R_all=0 and P=S_F(1/delta). The
constant sector still gives norm>=1. Taking the integer ceil(1/delta) in
B1's FREE-GROUP estimate G_B<=4B bounds the norm by8/delta, hence normalized log second moment tends to0.
Only J0 is used, and (2) follows without a nontrivial Gaussian density.
This proves Claim GL in all stated cases.

## 8. Verification and original completion boundary

Finite tail source is locally compiled at the unchanged fenced header,
with complete type/std3axiom audit, two valid boundary examples,3false
numeric variants rejected and5fresh owned replay artifact pairs identical.
It proves ONLY(7). Actual cutoff derivation, half-action density, Gaussian
normalizer, conditioning, source restart, Bochner/operator/spectral limits
remain INFORMAL analytic arguments supplied above, pending FULL gate.
That exact application gate has passed:74acceptedfinitefacts20local seams,
including this one scalar inequality, with all analytic boundaries retained. No official companion/package/lease/HPC.

Falsification preceded proof:18radial tails40/70digits with6weightC=0 chi
calibrations (not coarseA0=4C_theta),4Gaussian normalizer integrals,9exact
half-action algebra rows against an analytic MGF formula,8polynomial
ratio restatements and4rank-entropy guards. These are not certified numerical
enclosures or actual CM/operator/SPDE simulations. Rank-diagonal examples
show why a prefactor cannot be dropped, not that every diagonal theorem is
false. The scalar sqrt/amplitude/finite types have their stated scopes.

This result is a fixedR OPERATOR second-moment upper with an own ALLSIGNED
control score. It neither identifies a source L^*/firstmean nor proves the
original unmasked point upper. Original growing cone/localization/entropy,
source stationarity/average-of-SQUARES/finite-propagation point transfer,
signed-to-positive-control optimization, intended normalization and exact
limit remainOPEN. F3 is not reversed, point Sobolev traces are not used,
and the white fixed-smooth-finite-projection uniformR obstruction stands.
No rawH/L2 Gaussian, independent timeblocks/heaterrors, Skorohod/contact/
sourcefix/companion/TeX/PDF/wiki/bib/publication or whole-goal certificate.
The growing-cone route document is UNREVIEWED, not a premise of this proof.
