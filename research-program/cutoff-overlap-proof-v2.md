# Cutoff overlap and horizon consistency: revised proof candidate

AUTHOR REVISED CANDIDATE, 2026-11-02. Pending scoped production
verification; not adopted. This successor addresses the seven production
requests in the HIGH cutoff-proof review without changing the frozen
O1/O2/O3 target in `research-program/cutoff-overlap-statement-v1.json`.
The reviewed v1 draft and report remain unchanged. This is not a full local
flow theorem, a novelty claim, or a replacement for the original second-
moment goal. The original scientific TeX/PDF are unchanged.

## Objects and named construction inputs

Use the original admissible Stratonovich model and covariance amplitude.
Let E=H^(1/2)(Rd;R) x H^(-1/2)(Rd;R), with both phase components. S(t) is
the free wave group on E. We use its strong continuity, boundedness on
finite time intervals and speed-one finite propagation for distributional
phase data. Smooth compact multipliers D_f are bounded on E.
These are the free/multiplier facts of L:constant-phase-free in
`notes/integrated_constant_phase_young.tex` and the strong free-wave
bounds of L:driver-gain-localization in
`notes/integrated_actual_operator_driver.tex`. Write D_f(u,v)=(fu,fv).
Use the inhomogeneous Bessel norms and the Hilbert product norm on E.
Choose the fixed exponents of E:driver-parameters, in particular
1/2<theta<beta<min(1-alpha0/2,(3-alpha0-alpha)/2).

Fix the real even zeta from the frozen cutoff statement: zeta is smooth
and compactly supported, 0<=zeta<=1, equals one on a neighbourhood of
closed B_1 and is zero off B_2. Set zeta_k(x)=zeta(x/k).
Write m_R=zeta_R, chi_j=zeta_j
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
   every finite Lq uniform triangle operator norm, by
   P:constant-gaussian-flow and E:constant-flow-limit/
   E:constant-physical-flow in `notes/integrated_constant_phase_young.tex`,
   supplied on F and restricted to E below. No uniformity as R,T grow is
   assumed.

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
C(r)=S(-r)B_R,n(r)S(r). For the chosen Bessel/product norms,

  ||B_R,n(r)(u,v)||_E
    = ||b_R,n(r)u||_HminusHalf
    <= ||b_R,n(r)u||_L2
    <= ||b_R,n(r)||_infinity ||u||_L2
    <= ||b_R,n(r)||_infinity ||(u,v)||_E.

Thus K=sup_(0<=r<=T)||b_R,n(r)||_infinity is a finite bound for
||B_R,n(r)||. With equivalent Sobolev norm conventions one instead
multiplies K by the fixed embedding constants for Hhalf->L2 and
L2->HminusHalf. No spatial derivative norm is needed for this E->E
estimate. The smoothness from input 3 remains available for distributional
multiplication and propagation. Time continuity in L-infinity makes B
operator-norm continuous, while strong continuity of S and its finite-
horizon bound C_T make C strongly continuous on every state, with
sup_r||C(r)||<=C_T^2 K. Norm continuity of S or C is not asserted.

Input 3, P:source-ordinary-response in
`notes/integrated_source_convergence.tex`, identifies the increments of
M_R^n with the statewise integral of C. It also gives operator-norm
Lipschitz increments, hence C^theta regularity of M_R^n on this horizon.
P:constant-young-linear gives C^theta regularity of
V(r)=U_M^n(r,s)S(-s)e in r, since theta>1/2. These are the primitive and
state regularities used in E:constant-young-estimate: the Young integrator
is M_R^n, not C. No C^theta assertion about C is needed or imported.

The left Young sums for this interaction state are

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
For each integer triple (n,R,T), let Omega_A(n,R,T) be the intersection
of the source regularity, all-state primitive, restriction and Young-flow
construction events used above. Each has probability one on the retaining
extension. Set

  Omega_A = intersection_(n,R,T>=1) Omega_A(n,R,T).

This is a countable probability-one event. On it, the all-state ordinary
identification, Picard series and uniqueness just proved hold for every
integer triple. There is no common event over all positive source widths.
This proves Lemma A.

## Lemma B: ordinary-source overlap and horizon restriction

For fixed n, both-component observed source phases agree for all initial
E states and all times whenever R1,R2,N1,N2>=2j+T+3. Ordinary source
phases with fixed R also agree when a longer horizon is restricted to a
shorter one.

Proof. Fix a sample in Omega_A from Lemma A. In particular, it belongs
to both Omega_A(n,R1,T) and Omega_A(n,R2,T); both ordinary Picard series
and their uniqueness statements hold on this same sample. Fix
0<=s<=t<=T and use the open inflated backward balls
K_r=B_(2j+1+t-r), s<=r<=t. The guard makes both physical masks and both
initial cutoffs equal one on a neighbourhood of the closures of every
required ball. For e in E, the initial phase difference
(D_psi_N1-D_psi_N2)e vanishes on K_s as a pair of distributions.
L:constant-phase-free, with the free-group identification and Sobolev
support extension in L:driver-gain-localization, shows that its free
propagation to r vanishes on K_r. This is the order-zero Picard comparison
for both displacement and velocity.

Let q_i,k(r)=Q_i,k(r,s)D_psi_Ni e be the k-th ordinary Picard term
for coefficient B_i(r)=B_Ri,n(r). Suppose q_1,k(r)-q_2,k(r) vanishes
on K_r for every intermediate r. The forcing difference is exactly

  B_1(r)q_1,k(r)-B_2(r)q_2,k(r)
    = B_1(r)(q_1,k(r)-q_2,k(r))
      + (B_1(r)-B_2(r))q_2,k(r).

The first term vanishes on K_r because multiplication by a smooth function
preserves distributional vanishing: pairing b w against a test phi
supported there is pairing w against b phi, with the same support.
The second vanishes there because
b_R1,n-b_R2,n=(m_R1-m_R2)Y_n is zero on a neighbourhood of K_r.
Each B term has zero displacement component and the stated vanishing
velocity component, so the whole forcing phase vanishes on K_r.

For r<=v, enlarging K_v by the free propagation distance v-r gives K_r.
Apply L:constant-phase-free (and the Sobolev support argument of
L:driver-gain-localization) to the forcing phase: its free propagation
S(v-r) vanishes on K_v in both components. Compactly supported tests in
K_v have a positive margin inside this open ball, so their translated
compact wave kernels test only inside K_r. Testing the statewise strong
integral against these tests preserves zero. This proves the induction
step and agreement of every Picard term.

The operator-norm convergence of the two series implies convergence as
phase distributions. Hence their sums agree on K_t=B_(2j+1), an open
neighbourhood of supp chi_j. Multiplication by D_chi_j gives the zero
observed phase difference. This includes velocity, not only displacement.
The argument applies to every E state and every s,t on the fixed regular
sample, giving the whole observed operator-triangle identity.

For horizon restriction, the same sample in Omega_A belongs to
Omega_A(n,R,T1) and Omega_A(n,R,T2). The coefficient b_R,n uses the
same retaining time field on both horizons. The longer solution restricted
to the shorter interval solves (A1) with
the same initial phase. Ordinary uniqueness in Lemma A identifies it with
the shorter-horizon flow. No compatibility of raw driver versions was
assumed. This proves Lemma B.

## Proposition C: raw overlap and horizon consistency

The O1/O2 identities in the frozen statement hold on one ORIGINAL
probability-one event, for all their integer tuples, E states and times.

Proof. For each fixed tuple define the nonnegative random variable

  D= sup_triangle ||D_chi_j(P_R1,T D_psi_N1-P_R2,T D_psi_N2)||_B(E).

We make its measurability explicit. For each raw construction sample,
P_R,T(t,s)=S(t)U_M(t,s)S(-s) on E. P:constant-young-linear gives
joint operator-norm continuity of U_M; L:constant-phase-free gives strong
continuity and finite-horizon boundedness of S. Therefore, for every
fixed e, P_R,T(t,s)e is jointly continuous in (s,t). Indeed, if
(s_l,t_l)->(s,t), first S(-s_l)e->S(-s)e; multiplication by the
uniformly bounded and norm-convergent U_M(t_l,s_l) preserves convergence;
then the strongly continuous, locally bounded S(t_l) preserves it.
The same holds after fixed left and right cutoff multiplication.
This proves joint strong continuity without assuming norm continuity
of the physical free group.

Choose a countable dense subset {e_l} of the unit sphere of E and put
Delta_T^Q={(s,t): s,t rational, 0<=s<=t<=T}. If
A(t,s)=D_chi_j(P_R1,T(t,s)D_psi_N1-P_R2,T(t,s)D_psi_N2), then

  D = sup_((s,t) in Delta_T^Q) sup_(l>=1) ||A(t,s)e_l||_E.

For each fixed time pair, density of {e_l} gives the operator norm.
For each fixed e_l, joint strong continuity and density of the rational
triangle give the supremum over all time pairs. Taking the two suprema
in either order proves the display. Every term is W-measurable by the
actual raw construction. Intersect the countably many raw construction
events. On their W-measurable null complement define D=0 if needed;
this only specifies the diagnostic random variable there and does not
redefine the raw flows. Thus D is a W-measurable nonnegative random
variable. This also
agrees with the uniform-triangle strong-measurability statement of
P:constant-gaussian-flow. All cutoff multiplier norms below are finite
for this fixed tuple; none is assumed uniform in j or N.

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

Let z belong to E_local=Hhalf_loc x HminusHalf_loc. Here, H^sigma_loc
means distributions w for which eta w belongs to H^sigma(Rd) for every
eta in C_c^infinity(Rd), at sigma=1/2 and -1/2. Thus a compact smooth
cutoff sends each local component into the indicated global Sobolev
space by this definition. Subsequent compact multiplications are bounded
there by the weighted Fourier argument in L:constant-phase-free.
For one O1 tuple choose an integer M>2max(N1,N2), so psi_M=1 on
neighbourhoods of BOTH supports of the data cutoffs. Then
e=D_psi_M z belongs to E, and
D_psi_Ni e=D_psi_Ni z. Apply Proposition C to this global e on its universal
operator event. This proves the tested local cut-off identity O3, without
feeding z directly into a global E operator. It is not a point trace and
does not yet prove assembly/composition of the full local Fréchet flow.

## Remaining gates

This revised candidate requires scoped production verification before
adoption. The v1 HIGH report applies to its original frozen bytes; it is
not silently transferred to this successor. The present proof imports
the named fixed-mask Gaussian/source construction and deterministic free
support facts; it does not independently verify their full source-paper
proofs. The v1 reviewer reported that the PaperDev-Tailored-Workflow.md
excerpt was unavailable in its snapshot. That limitation remains recorded;
no full-workflow or source-image certificate is inferred from that review.
No asymptotic C2,
new covariance regime, global unmasked norm, publication novelty, arbitrary
weak-solution uniqueness or new Lean certification is claimed.
