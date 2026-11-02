# Cutoff overlap and horizon consistency: proof draft

AUTHOR DRAFT,2026-11-02. Not adopted or independently cleared. This fills
specific source-interface obligations from the cutoff-statement review;
it is not a new local-flow theorem, a novelty claim, or a replacement
for the original second-moment goal. The original scientific TeX/PDF
are unchanged.

## Objects and named construction inputs

Use the original admissible Stratonovich model and covariance amplitude.
Let E=H^(1/2)(Rd;R) x H^(-1/2)(Rd;R), with both phase components. S(t) is
the free wave group on E. We use its strong continuity, boundedness on
finite time intervals and speed-one finite propagation for distributional
phase data. Smooth compact multipliers D_f are bounded on E.
These are the free/multiplier facts used in L:constant-phase-free.

Fix zeta as in the frozen cutoff statement. Write m_R=zeta_R, chi_j=zeta_j
and psi_N=zeta_N. Observation support is contained in closed B_(2j).
All integer indices below are positive. The guard is R,N>=2j+T+3.
The physical coefficient has the ONE mask m_R, not its square by accident.

The named existing construction inputs are:

1. The actual raw Gaussian interaction path and its fixed-mask Young flow
   from P:actual-operator-driver, P:constant-phase-driver and
   P:constant-gaussian-flow. They are measurable with respect to the original W.
2. ONE retaining source field Y_n for rho_n=(1/n,1/n), on a common extension
   of the original probability space. It can depend on the independent
   completion noise J as well as W. It is not asserted W-measurable.
   In the construction Y_n(t,x)=I(v_(rho_n;t,x)), where the retaining
   isometry I and point-field vectors have no R,T index. Its restrictions
   to different masks/time horizons therefore use this same field.
   L:source-retaining-isometry and L:source-pointfield-regularity supply
   its construction/regularity. Only countably many n and integer compact
   horizons are used for common events.
3. For fixed R,T,n, b_R,n(r,x)=m_R(x)Y_n(r,x) is continuous in time and
   smooth/compact in space on a full-probability regularity event. Its
   spatial derivatives are bounded on the fixed horizon. The actual source
   interaction primitive on every E state is

     M_R^n(t)e = integral_0^t S(-r) B_R,n(r) S(r)e dr,
     B_R,n(r)(u,v)=(0,b_R,n(r)u).

   This is a statewise strong integral, not an operator-norm derivative
   assertion. Its all-state/time identity is P:source-ordinary-response.
4. For each R,T, physical source flows converge to the ACTUAL raw flow in
   every finite Lq uniform triangle operator norm, as supplied on F and
   restricted to E below. No uniformity as R,T grow is assumed.

These inputs are used as named existing analytic results, not re-proved
from the source papers here. The new deductions below are explicit.
The underlying extension has a measure-preserving projection onto the
original probability space; raw W-measurable objects are pulled back there.

## Lemma A: E restriction and all-state ordinary source identification

For fixed R,T, raw/source F flows preserve the closed isometric copy iE.
Their restrictions have the existing uniform triangle Lq convergence on E.
For fixed n, on one full-probability event for the countable integer data,
the source physical flow on E solves the ordinary phase Duhamel equation
for EVERY e in E and every0<=s<=t<=T, with initial phase e at time s.
It is the unique continuous E-valued solution for that initial phase.

Proof. The source and raw interaction paths satisfy A i=i M_E,
pi_C A=0, and the free groups satisfy S_F(t)i=i S(t).
The interaction flow preserves constant coordinates, so starting in iE
it remains in iE. Restrict its Young sums to this closed subspace to
obtain the E interaction flow. No density of E in F is used. Physical
conjugation preserves the restriction as well.

For invariant bounded operators Q,Q' on F,

  ||Q|E-Q'|E||_B(E) <= ||Q-Q'||_B(F).

Restriction is a bounded linear map on the closed invariant-operator
subspace, also for uniform triangle families. It preserves strong
measurability and transfers the stated source convergence and moments.
The raw flow here remains its original-W Young construction; it is not
redefined just to force a source limit.

Fix one regular source sample, n,R,T, and put
C(r)=S(-r)B_R,n(r)S(r). Multiplication satisfies
||B_R,n(r)||_B(E)<=||b_R,n(r)||_infinity, up to the fixed Sobolev norm
convention. Hence C is strongly continuous on each state and uniformly
bounded on[0,T]. Strong continuity, not norm continuity, of S suffices.
The source primitive increments are its statewise integrals by input3.

For the interaction state V(r)=U_M^n(r,s)S(-s)e, the left Young sums are

  sum_k integral_(r_k)^(r_(k+1)) C(r)V(r_k) dr.

Their difference from integral_s^t C(r)V(r)dr is bounded by
T*sup_r||C(r)|| times the modulus of continuity of V at the mesh size.
It tends to zero. Thus V satisfies the ordinary interaction equation.
Multiplying by S(t) gives, for Q(t,s)e=S(t)V(t),

  Q(t,s)e=S(t-s)e + integral_s^t S(t-r)B_R,n(r)Q(r,s)e dr.       (A1)

This argument is deterministic on the all-state primitive event and works
for every state and every initial time; it is not limited to e_0 or s=0.

For completeness, construct the ordinary phase directly. Put
Q_0(t,s)=S(t-s), and, statewise,

  Q_(k+1)(t,s)e=integral_s^t S(t-r)B_R,n(r)Q_k(r,s)e dr.

If C_T bounds S on[-T,T] and K bounds B_R,n on[0,T],

  ||Q_k(t,s)|| <= C_T^(k+1) K^k (t-s)^k/k!.

Consequently sum_k Q_k converges uniformly in triangle operator norm.
For each Picard term and state, dominated convergence in the strong
integral, including its moving endpoints, gives joint strong continuity
in(s,t). The uniform series passes that property to the sum, which
satisfies(A1) and is bounded. If two continuous state solutions differ, iterating their
homogeneous difference equation bounds it by a finite supremum times
(C_T K T)^k/k! for every k, hence by zero. This proves uniqueness and
identifies the source physical flow with this ordinary phase for every s,e.
The regularity and primitive events may be intersected over countably many
(n,R,T); no common event over all positive source widths is claimed.
This proves Lemma A.

## Lemma B: ordinary-source overlap and horizon restriction

For fixed n, both-component observed source phases agree for all initial
E states and all times whenever R1,R2,N1,N2>=2j+T+3. Ordinary source
phases with fixed R also agree when a longer horizon is restricted to a
shorter one.

Proof. Fix a regular source sample and0<=s<=t<=T. Use the inflated backward
balls K_r=B_(2j+1+t-r), s<=r<=t. The guard makes both physical masks and
both initial cutoffs equal one on a neighbourhood of every required ball.
Their initial phase difference vanishes on K_s. The free evolutions of
that difference vanish on K_r by speed-one propagation.

Use the ordinary Picard series from Lemma A for both coefficients and
both cut initial phases. Suppose their k-th terms agree on K_r at every
intermediate time. On K_r the coefficients agree, since both equal the
same Y_n there. Their forcing difference therefore vanishes on K_r.
For r<=v, the backward enlargement of K_v by v-r is exactly K_r.
Free propagation shows that this forcing difference, transported to v,
vanishes on K_v. Testing the strong integral against compact tests in
K_v preserves zero. Induction proves agreement of every Picard term.

The operator-norm convergence of the two series implies convergence as
phase distributions. Hence their sums agree on K_t=B_(2j+1), an open
neighbourhood of supp chi_j. Multiplication by D_chi_j gives the zero
observed phase difference. This includes velocity, not only displacement.
The argument applies to every E state and every s,t on the fixed regular
sample, giving the whole observed operator-triangle identity.

For horizon restriction, b_R,n uses the same time field on both horizons.
The longer solution restricted to the shorter interval solves(A1) with
the same initial phase. Ordinary uniqueness in Lemma A identifies it with
the shorter-horizon flow. No compatibility of raw driver versions was
assumed. This proves Lemma B.

## Proposition C: raw overlap and horizon consistency

The O1/O2 identities in the frozen statement hold on one ORIGINAL
probability-one event, for all their integer tuples, E states and times.

Proof. For each fixed tuple define the nonnegative random variable

  D= sup_triangle ||D_chi_j(P_R1,T D_psi_N1-P_R2,T D_psi_N2)||_B(E).

It is measurable in the original W sigma algebra by the actual raw-flow
measurability and bounded left/right multiplication. Its triangle norm
measurability is supplied by the construction; alternatively, strong
state continuity and a countable dense unit sphere/rational time pairs
give the same supremum. All cutoff multiplier norms below are finite for
this fixed tuple; none is assumed uniform in j or N.

Lift D to the retaining extension. Lemma B makes the observed ordinary
source difference zero there for each n. Triangle inequality gives

  E_original D = E_extension D
    <= ||D_chi_j|| ||D_psi_N1|| E_extension sup_triangle||P_R1,T-P_R1,T^n||
     + ||D_chi_j|| ||D_psi_N2|| E_extension sup_triangle||P_R2,T-P_R2,T^n||.

Both terms tend to zero by Lemma A/input4. Thus E_original D=0, and D=0
almost surely on the original space. Source events themselves were not
claimed W-measurable; D is. This is why the retaining completion noise
causes no change in the raw event. A same-law but differently coupled
source would not make the middle term zero.

For horizon consistency, use the supremum on the shorter triangle of
||P_R,T2-P_R,T1||. Its source middle term is zero by Lemma B. Bound the two
errors by the longer/shorter uniform triangle convergence. The same
expectation argument proves the raw horizon identity. This characterizes
compatibility of the already constructed raw versions through their
unique Lq source limits; it does not presume a raw-driver gluing theorem.

There are only countably many integer tuples, including horizon tuples.
Intersect their W-measurable probability-one events and the countably
many raw construction events. A zero operator-triangle norm already
covers every state and real time pair on its triangle. No uncountable
intersection over states, times or source widths is introduced.
For Gamma=0 the noises are zero and all flows are free; these arguments
reduce to deterministic free propagation and horizon uniqueness, without
nondegenerate Gaussian or Cameron assumptions. This proves Proposition C.

## Local cut-off data consequence, not a local-flow theorem

Let z belong to E_local=Hhalf_loc x HminusHalf_loc. For one O1 tuple choose
an integer M>2max(N1,N2), so psi_M=1 on neighbourhoods of BOTH supports of
the data cutoffs. Then e=D_psi_M z belongs to E, and
D_psi_Ni e=D_psi_Ni z. Apply Proposition C to this global e on its universal
operator event. This proves the tested local cut-off identity O3, without
feeding z directly into a global E operator. It is not a point trace and
does not yet prove assembly/composition of the full local Fréchet flow.

## Remaining gates

This proof draft requires independent review of the new lemmas and exact
existing interfaces before adoption. It imports the stated fixed-mask
Gaussian/source construction and deterministic free support facts; it does
not independently verify their full source-paper proofs. No asymptotic C2,
new covariance regime, global unmasked norm, publication novelty, arbitrary
weak-solution uniqueness or new Lean certification is claimed.
