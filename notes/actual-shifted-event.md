# Actual shifted-flow growth event and raw-cost second-moment lower bound

ACCEPTED at the scoped scientific analytic/type/application gate: actual
Opus5.5/HIGH,18PASS/PASS_WITH_NOTES groups,379.671seconds,no required
repairs; scientific sourced5dcd46. Evidence and six optional adjudications
in reviews/2026-10-30-actual-shifted-event/scientific-adjudication-v1.md.
Actual residual is retained; positive average event and raw-cost original
point lower bound are for each FIXED positive separable test only.
Original sharp constants, optimizer identification and dimensions remain open.

## 1. Objects, scoped inputs and claims

Work in d1,0<a<1,0<alpha<=1,alpha+a<2, with the ORIGINAL positive
nonzero Riesz/white covariance Gamma including its amplitude. All spaces,
noises and operators below are REAL. Fix EACH of f and q to be nonzero,
nonnegative and smooth compact, with supp f contained in(0,1) and q on R.
Set psi(t,x)=f(t)q(x), Z=W(psi), v=E Z^2, and

 U=Gamma*q, k(t)=integral_0^1 |t-s|^-a f(s)ds,0<=t<=1.

Fix a nonnegative smooth compact phi of integral1, support radius M_phi,
and c>=1+M_phi. Define delta in(0,1], L=1/delta, r=c/delta,
g=delta^((1-a)/2). Use exactly the common W^delta,Z and physical Young
flow on F from notes/joint-gaussian-tilt.md. The shifted potential is

 g zeta_r W^delta(u,x)+zeta_r k(delta u)U(x),0<=u<=L.        (1)

Let P_delta^h(t,s) denote that actual physical evolution and J the bounded
displacement average against phi. Thus e0=(1,0) belongs to actual F and

 Y_delta=J(P_delta^h(L,0)e0)                                (2)

is a SIGNED measurable real variable. Measurability follows exactly as in
the accepted tilt (12): before squaring, J applied to the continuous
Young-map/driver reconstruction is already a continuous scalar function.
No point evaluation or global stationary operator is used.

Imported scoped accepted inputs, not re-proved here:
- local-causal-young-flow.md Sections4-7: F includes compact phases PLUS
  constants, physical Young flow and composition, admissible deterministic
  profiles, and actual all-unit-block maximum/stability (7.2)-(7.3).
- joint-gaussian-tilt.md Sections3-5: raw covariance/profile regularity,
  same-residual shifted-flow Gaussian identity (13), with raw half cost,
  and original point-moment consumer (14).
- spectral-ground-family.md, spectral-weighted-projection.md and
  spectral-complement-transfer.md: actual frozen family H_b=-d2-bU,
  positive normalized p_b, rate lambda_b and projections on F.
- moving-block-cone.md: accepted deterministic integer-block cone,
  constant entrance and positive terminal-average estimate UNDER its
  explicit perturbation premise. That premise is proved below.

Define K_par and I_psi as in Section2. Claims (candidate): for every e>0,

 P{Y_delta>=exp((I_psi-e)/delta)} ->1, delta down0,           (3)

and for the ORIGINAL canonical stationary Stratonovich solution,

 liminf_(t->infinity) t^(-kappa) log E|u(t,0)|^2
        >=2 I_psi-v/2, kappa=(4-alpha-a)/(3-alpha).          (4)

These are for each FIXED positive separable test before delta tends to0.
There is no assertion that its value is the original sharp constant.

## 2. Actual time profile and uniform mask/freezing defect

Extend f by0 outside(0,1). The accepted raw convolution formula gives
h(t,x)=k(t)U(x). Since a<1 and |t-s|<=1 for t,s in[0,1],

 0<m_f=integral_0^1 f(s)ds <=k(t)<=2||f||infinity/(1-a).    (5)

For the lower bound use |t-s|^-a>=1 except on its harmless integrable
diagonal. Differentiate the convolution by moving the derivative onto
the smooth zero extension of f, as justified in tilt Section3. Thus k'
is bounded by 2||f'||infinity/(1-a), and k is Lipschitz on[0,1]. Fix
ONE compact interval K_par subset(0,infinity) containing its range,
for example [m_f/2,1+2||f||infinity/(1-a)]. All spectral/cone constants
below are selected for this ONE family, not uniformly across tests.
The accepted lambda_b is positive and continuous on K_par. Hence

 F_psi(t)=lambda_(k(t)) is continuous on[0,1],
 I_psi=integral_0^1 F_psi(t)dt is finite and positive.         (6)

U has bounded spatial C1 norm and vanishing C1 tails by the accepted tilt
profile calculation. The mask zeta_r=1 on[-r,r], with derivative bounded
by C/r, therefore satisfies

 d_r=||(zeta_r-1)U||W1infinity ->0 as r->infinity.            (7)

Explicitly bound the function and its U' term by the suprema of |U|,|U'|
on |x|>=r, and the remaining derivative term by C||U||infinity/r. No
Riesz L1 assumption is imposed. For white noise U=c_Gamma q is compact,
so d_r=0 for all sufficiently large r, retaining the actual amplitude.

For padded unit intervals only, put k_bar(t)=k(min(t,1)), t>=0.
It is Lipschitz, keeps the same range K_par, and equals k for t<=1.
Define deterministic unit profiles on local u in[0,1] by

 h_(delta,j)(u,x)=zeta_r(x)k_bar(delta(j+u))U(x),
                     j=0,...,ceil(L).                     (8)

They satisfy local-flow (5.6) with zero constant part and a common bounded
W1infinity norm K_base independent of j,delta,r>=1. They are strongly
measurable into C_b^1 (in fact Lipschitz). Time smoothness at the cap is
not needed by that admissibility statement. Frozen profiles bU for b in
K_par obey the same hypotheses with a common enlarged K_base.

For a fixed positive INTEGER block length B, put b_m=k(delta mB) for
m=0,...,N, where N=floor(L/B). These parameters lie in K_par. For a unit
j=mB+nu used inside block m, 0<=nu<B, and any of its used times u,

 ||h_(delta,j)(u)-b_m U||W1infinity
       <=C[delta B+d_r]=:a_delta(B) ->0, fixed B.           (9)

Indeed Lipschitz k_bar changes by at most Lip(k)delta B, and the mask
term is bounded by sup k times d_r. Also consecutive b_m differ by at
most Lip(k)delta B, including the final b_N. Every constant here is
fixed by the test/family and, in (9), by B, before delta tends to0.

## 3. Actual unit errors on one measurable event

Use exactly the jointly defined raw unit fields and physical mask from
local-flow (7.1)-(7.3). They are reset at integer fast time j and use
W^delta(j+u), equivalently the source-compatible field there. The phase
is (V,partial_u V). The accepted identification of these physical unit
flows with restrictions of P_delta^h follows at positive source widths
from the ordinary time-shifted equation and then by the accepted common
raw limits and composition. Re-centering uses S(u)U_j(u,v)S(-v), not a
bound on S(j). Thus constants do not grow with the start time j.

Let x_delta=g times the accepted maximum of local HS unit-driver
Ctheta norms over the spatial cells and unit starts j<=ceil(L). This is
a nonnegative measurable scalar (finite maximum of separable path norms).
For any fixed p>4/(1-a), accepted (7.2) gives

 ||x_delta||Lp <=C_p delta^((1-a)/2-2/p) ->0.               (10)

No independence of units, cells, or x_delta and Z is needed. The accepted
maximum includes FULL units through ceil(L), so its driver event involves
noise cells up to ceil(L)+1, less than two fast-time units beyond L.
We cite that already accepted padding OPENLY. Profiles (8) define the
auxiliary deterministic base there without changing its range or bound.
The actual observable and all used physical operators depend only on the
prefix up to L. No new B-long stochastic extension will be invoked.

On {x_delta<=1}, the accepted unit stability against profiles (8) gives
maximum physical operator difference <=C_1 x_delta from its deterministic
unit flow, uniformly in both local endpoints 0<=v<=u<=1. The deterministic
flow against (8) differs from the frozen physical P_(b_m)(u-v) by at most
C_2 a_delta(B). To see the latter application explicitly, local-flow (5.5)
bounds the interaction primitive difference in Ctheta B(F) by the uniform
W1infinity difference (9); (5.3) on the common bounded driver set and the
fixed-horizon physical conjugation then give the difference bound. Thus
for every used unit piece in block m the ACTUAL error is at most

 e_delta=C_1 x_delta+C_2 a_delta(B),                         (11)

on {x_delta<=1}. Both actual and frozen unit-piece norms are <=A with
one deterministic A>=1 on this event: deterministic bounds follow from
(5.2), fixed free-group bounds and K_base, and actual bounds follow by
adding C_1 x_delta<=C_1. Strong continuity of physical paths is enough;
only the uniform norm of operator DIFFERENCES has been used.

## 4. Fixed-B composition and final partial extension

For any n>=1 bounded operators A_i,B_i, the exact ordered identity is

 A_(n-1)...A_0-B_(n-1)...B_0
 =sum_(k=0,...,n-1) B_(n-1)...B_(k+1)(A_k-B_k)A_(k-1)...A_0. (12)

Empty products are identity. For n=1 this is immediate. If it holds for
n, subtract B_n B_(n-1)...B_0 from A_n A_(n-1)...A_0, split as
B_n times the old difference plus (A_n-B_n) times the old A product,
and substitute the induction hypothesis. This proves (12) for all n,
without commutation. Submultiplicativity and the triangle inequality
therefore imply error <=n A^(n-1)e_delta whenever all factor norms are
<=A and all factor differences <=e_delta.

The looser bound n A^n e_delta used below also has a local arithmetic
Lean check: extend BOTH finite factor sequences by identities after the
last piece, so their bounds <=A and difference bound <=e_delta still
hold for ALL indices. Let d_n be the norm difference of their n-prefix
products. The frozen-prefix norm is <=A^n by induction from identity.
The identity A_n(P_n-Q_n)+(A_n-B_n)Q_n for the next difference gives
d_(n+1)<=A d_n+A^n e_delta and d_0=0. The checked scalar theorem
finite_error_accumulation yields d_n<=n A^n e_delta for every n.
Only this arithmetic deduction is kernel-checked; the norm recurrence
and the operator interpretation remain the analytic argument just given.

Every interval [mB,mB+t] with 0<=t<=B consists of at most B unit pieces,
including its possibly partial last piece, because B and mB are integers.
The actual evolution composition law and the frozen autonomous identity
P_b(u+v)=P_b(u)P_b(v) identify the respective ordered products. At t=0
both are identity. Equations (11)-(12) give, on {x_delta<=1},

 max_m sup_(used t<=B)
 ||P_delta^h(mB+t,mB)-P_(b_m)(t)|| <=B A^B e_delta.          (13)

Here used t includes all of[0,B] for m<N and only[0,s] for m=N,
s=L-NB in[0,B). No entire long-horizon product difference is claimed.
Constants A,B are fixed; B never grows with 1/delta.

For m<N set D_m(t)=P_delta^h(mB+t,mB) on[0,B]. For m=N use the same
physical family up to s, and for s<t<=B define

 D_N(t)=P_(b_N)(t-s)D_N(s).                                (14)

The spectral/Young accepted bounds imply a uniform finite
M_B=max(1,sup_(b in K_par,0<=u<=B)||P_b(u)||). It also follows directly
by adding growing projection and complementary bounds with lambda bounded
above. Autonomy gives

 D_N(t)-P_(b_N)(t)=P_(b_N)(t-s)[D_N(s)-P_(b_N)(s)].

Thus the FULL cone-premise error of these families, on {x_delta<=1}, is
at most

 xi_delta=M_B B A^B e_delta ->0 in probability.             (15)

For s=0 the actual D_N(0)=I, so (14) is exactly P_(b_N)(t).
This extension uses NO new noise beyond L. Its value at the observed
s is unchanged. All comparisons and prefix identifications use the actual
retained residual, not a re-sampled or discarded field. For fixed delta
there are finitely many blocks; the accepted simultaneous versions suffice.
There is no pathwise supremum over uncountably many delta or source widths.

## 5. Apply the cone, pay all losses and obtain the event

Fix desired e>0. Choose 0<rho<1/2 so small that log(1-rho)>-e/3, using
continuity of log at1. Apply the accepted moving-block theorem for this
rho and the fixed actual family/test; it supplies integer B, a parameter
tolerance omega, an operator-error tolerance epsilon_cone and c_*>0.
All are independent of delta and N. For sufficiently small delta,
N>=1 and Lip(k)delta B<=omega. Define the measurable event

 E_delta={x_delta<=1, xi_delta<=epsilon_cone}.               (16)

Here xi_delta in (15) is the scalar expression from (11), whether or not
x_delta<=1; (10) and (9) imply P(E_delta)->1. On this event (13)-(15)
DISCHARGE the actual operator-error premise for every required D_m(t).
Composition up to the observed horizon gives exactly

 Y_delta=J(D_N(s)D_(N-1)(B)...D_0(B)e0).

Consequently the accepted cone/terminal estimate implies on E_delta

 Y_delta>=c_*(1-rho)^(N-1)
          exp(B*sum_(m=0,...,N-1)lambda_(b_m)+s lambda_(b_N))>0. (17)

Consider the normalized deterministic rate

 R_delta=delta[B*sum_(m<N) F_psi(delta mB)+s F_psi(delta NB)]. (18)

Its weights sum to delta(NB+s)=1. On each slow interval its sample is the
left endpoint, with interval length at most delta B. If w_F is a modulus
of continuity of F_psi on[0,1], integration interval by interval gives
|R_delta-I_psi|<=w_F(delta B)->0. This includes the last partial interval.
Also 0<=delta(N-1)<=1/B<=1, so the negative logarithm satisfies

 delta(N-1)log(1-rho)>=log(1-rho)>-e/3.

Finally delta log c_* tends to0. For small delta, taking logarithms in
(17) yields delta log Y_delta>=I_psi-e on E_delta. Since its probability
tends to1, (3) follows. This proves the candidate actual growth event.

## 6. Same-Z moderate event, exact half cost and original point moment

Let U_delta be the canonical NOISE-ONLY signed average from the accepted
tilt construction and M_delta=E U_delta^2. By its identity (13),

 M_delta=E[exp(-Z/sqrt(delta)-v/(2delta))Y_delta^2].           (19)

Here the residual in Y_delta is fully retained and Z is the SAME raw
Gaussian variable. In particular v=E Z^2 is finite and fixed. Chebyshev
implies P{|Z|>delta^(-1/4)}<=v delta^(1/2)->0. Intersect its complement
with the event in (3), for any fixed e>0, and call the probability p_delta.
The union bound gives p_delta->1; no independence is asserted. On this
intersection, the MINUS density is bounded below by
exp(-delta^(-3/4)-v/(2delta)), and Y_delta^2>=exp(2(I_psi-e)/delta).
The integrand in (19) is nonnegative everywhere, so restriction gives

 M_delta>=p_delta exp((2I_psi-2e-v/2)/delta-delta^(-3/4)).    (20)

For small delta,p_delta>=1/2; hence delta log p_delta tends to0. Also
delta*delta^(-3/4)=delta^(1/4)->0. The locally checked identity
moderate_penalty verifies the same normalized penalty directly as
delta*(delta^(-1/4)/sqrt(delta))=delta^(1/4), for delta>0. Taking lower limits in (20), then
letting e down0, proves

 liminf_(delta down0) delta log M_delta>=2I_psi-v/2.          (21)

This uses the SQUARED nonnegative observable in (19); no analogous signed
first-moment restriction is being asserted. The Gaussian identity is an
accepted analytic input, not a formally verified Gaussian theorem.

Accepted tilt (14), with delta=t^(-kappa) and physical spatial scale
R=t delta, identifies U_delta with the noise-only canonical average and
gives M_delta<=E|u(t,0)|^2. This input is the exact direct-event scaling
and phase-response averaged-to-point consumer; it has no R^d loss.
Every delta near0 corresponds to t=delta^(-1/kappa) tending to infinity,
so (21) gives (4). This proves the candidate raw-cost lower bound.

## 7. Calibration, formal boundary and remaining goal

All lower bounds here are for the ORIGINAL point second moment, with a
test average used only as a consumer. The existing Jensen lower comparison
remains available independently; (4) is an additional lower bound, not a
claim that every test beats Jensen. No first-moment source normalization
or L_* is assumed, and no correction to the source is adopted. This result
does not claim a sharp constant or a uniform a->0 interchange.

The finite controls from the frozen target have full reproducible code.
Their floor/remainder, ordered-product and density scalings are witnesses,
not proofs of the analytic input estimates or the all-length identity(12),
which is proved above. The telescope witness has identity B factors and
is explicitly weaker than a full noncommutative mutation test.

Lean triage: two new local arithmetic deductions compile/replay cleanly
at Lean/Mathlib4.35.0 with complete public types/live standard-three axioms,
five matching owned outputs and two numerical False controls. Their exact
applications are the extended-prefix recurrence in Section4 and normalized
moderate penalty in Section6; independent type/application review remains
required. Evidence/fences: lean-progress/local-checks/actual-event-v1/.
Exact scaling and finite margins inside the imported cone are reused at
their accepted scope. Gaussian tilting, probability limits,
operator/source stability, raw-field identifications, Riemann sums and
this assembly are not formalized by them. No new foundational library,
companion/package or cluster job is created. Source-level arithmetic
power checks do not certify a stochastic or variational theorem.

Full independent scientific proof/application review is REQUIRED before
adoption. Next is the actual variational optimization/optimizer class and
its exact relation, if any, to intended source constants. The original
sharp upper/lower constants, higher dimensions, source normalization and
whole-paper/novelty/circulation gates remain open. The canonical TeX/PDF
is unchanged; this is an internal candidate, not a completed full round.
