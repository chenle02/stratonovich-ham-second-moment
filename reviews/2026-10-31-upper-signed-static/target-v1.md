# S1-S4 signed static wave upper and actual mean-field interface

FROZEN UNREVIEWED STATEMENTS ONLY. Prior goal turn PROGRESS: actual fixedR/M
nonlinear E1-E4 accepted scientificcdf2056/adoptionb480aca,24HIGH388.122s;
current149b0e2 clean. Full original all-Gamma sharp/source objective ACTIVE.
These new static/form/freezing-interface claims are not yet proved/adopted.

## Exact potential class and phase

Use original H:homog Gamma/amplitude,d=1,2,3 and physical m_R=eta_R² ONCE,
R fixed. Actual phase E=H^(1/2)xH^(-1/2), F=E directsum R² with its real
Hilbert norm, same free S_F. Lambda=(1-Delta)^1/2, unitary Fourier convention.
For q real C_c^infinity define V_q=m_R(Gamma*q), real smooth compact,
B(V_q)(u,v,c1,c2)=(0,V_q(u+c1),0,0). This is the compact F operator in
accepted C3 Section3, including its constant-displacement column; the
instant constant-velocity column is0 but its evolved response is not0.
Let mathcalV_R be the OPERATOR-NORM closure of these B(V_q) in K(F).
An element L is to be identified with the distribution V from its constant
column. Set k=||L||, K>=max(1,k). No pointwise boundedness or positivity
of this limiting V is assumed. A vanishing covariance is trivial.

## S1. Actual multiplier, closed form and self-adjoint realization

Propose: every L in mathcalV_R determines a unique real distribution V
in H^(-1/2), supported in supp m_R; on smooth tests L has exactly the
multiplier action B(V), and its first column extends H^(1/2)->H^(-1/2).
The real symmetric pairing v_V(u,w)=<Vu,w> extends continuously there,
with |v_V(u,w)|<=k||u||H1/2||w||H1/2. Complexification is Hermitian.
On H1, q_V(u)=||grad u||2²-v_V(u,u). With c=2+K² propose

 A_V=H_V+c >=1 self-adjoint on L2,
 D(A_V^(1/2))=H1,
 (1/2)||u||H1²<=q_V(u)+c||u||2²<=3(1+K²)||u||H1²,           (S1a)
 D(A_V^(1/4))=H1/2, negative dual completion H-1/2.          (S1b)

No H2 domain asserted for the ROUGH operator. Proposed construction:
coercive Hilbert form/Riesz resolvent followed by the bounded positive
self-adjoint spectral theorem; identify completions from cores. Do not
invoke KLMN or a rough Schrodinger theorem without actual primary hypotheses.
Quarter-power comparison may use the resolvent/sqrt argument already proved
in compact-mean-ground-family.md Section3 with the NEW form bounds.

## S2. Sharp exponential rate, polynomial norm budget, actual F flow

Define beta(V)=inf_(u in H1,||u||2=1)q_V(u) and
lambda(V)=sqrt(max(0,-beta(V))). Propose
 -K²<=beta(V)<=0, lambda(V)<=K,

 ||P_V(t)||B(F)<=C(1+K)^4(1+t)^3 exp(lambda(V)t), t>=0,      (S2)

where C is universal for these phase conventions (uniform d<=3), independent
of R,Gamma,V,K,t. Polynomial exponents sufficient, not claimed optimal;
the exponential rate is EXACTLY lambda(V), no added fixed positive rate.

P_V must be the ACTUAL physical F evolution: the zero-started interaction
primitive D_V(t)=int_0^t S_F(-s)L S_F(s)ds and its Young solution, equivalently
the ordinary bounded-perturbation Duhamel flow on every finite horizon.
The integral is operator-norm continuous via compact L and strong group/
adjoint. Need all-time consistency/real subspaces and BOTH constant columns.
The spectral H_V wave on E must be identified with THIS flow. Smooth
operator-norm approximation must justify the rough limit, not a false H2
identity for rough V or constants in L2. Lambda0/continuous spectrum/no
ground eigenstate or gap are all allowed. No positivity of V is required.

## S3. Quantitative bottom and rate continuity

For L_V,L_W in mathcalV_R with norms<=K,K>=1, propose

 |beta(V)-beta(W)|<=(K+2)||L_V-L_W||,
 |lambda(V)-lambda(W)|<=sqrt((K+2)||L_V-L_W||).              (S3)

Use normalized approximate form minimizers, not eigenstates. The support
condition supplies beta<=0 via translated/dilated tests. A Lipschitz lambda
at beta0 is NOT claimed. A pure C exp(lambda t) norm bound at lambda0 is
NOT claimed; free velocity already grows linearly.

## S4. Actual compact mean family and block-averaging rate interface

Use accepted C3 T=T_sp U:H_I->Lr(I;K(F)), supported raw H_I and r>2.
Propose T Phi(s) belongs to mathcalV_R for a.e.s, and
 F(Phi)=int_I lambda(T Phi(s))ds
is finite and continuous on H_I. On ||Phi||<=M, T-images have compact
closure in Lr. For the actual partition I_m with mesh<=delta B, let
barT_delta Phi be the Bochner average of T Phi on each positive-length
I_m (an empty last interval has no contribution). Propose

 sup_(||Phi||<=M)||barT_delta Phi-T Phi||Lr ->0,
 sup_(||Phi||<=M)int_I
       |lambda(barT_delta Phi(s))-lambda(T Phi(s))|ds ->0.   (S4)

All averaged operators must remain in the SAME closed linear multiplier
class. The rate function is evaluated pointwise on this operator class,
not on an instantaneous Gaussian field. Uniform-integrability/positive-
length last interval and measurability required; no division by empty length.
This is a RATE-INTERFACE convergence only, not yet a deterministic product
upper, nonlinear replacement or original point asymptotic.

## Falsification, reuse and remaining scope

Before proof: exercise full spectral wave matrix for signed/zero h,
including h0 and lambda0; free constant-velocity polynomial growth; scalar
sqrt non-Lipschitz at0; normalization and fractional shifted-phase weights;
prove finite diagnostics' scope, no actual CM/eigenstate claim from them.
Existing C3/D1/E1-E4 do not supply these S1-S4 claims. Existing positive-
family compact-mean-ground Sections3-4 are METHOD comparators only.
Search/reuse finite real AMGM/square-root/kernel inequalities; no new Lean
foundation needed just to wrap spectral or form analysis.73facts19seams/L0
unchanged until any new meaningful separately reviewed finite seam.

Known-method application, no theorem/method novelty or publication claim.
Need local wiki search/cite+syntheses and exact held-primary crosswalk
before long proof. Required independent statement THEN FULL analytic/
source/type/actual application review. No automatic KLMN/generalized
Schrodinger import without hypotheses, no positive-gap argument promoted.

Original mean-action tails/M-infinity, actual global restart, deterministic
product/time-freezing/variational optimization, growing original cone/
localization/entropy, original POINT upper/source constants/normalization/
conditional exact limit remain OPEN. The accepted white uniformR guard
for fixed finite smooth projections stands. No F3reverse/pointtrace/rawL2
Gaussian/timeblock or heaterror independence/Skorohod/contact/HPC/sourcefix/
companion/TeX/PDF/wiki/bib/publication/fullgoalcompletion.
