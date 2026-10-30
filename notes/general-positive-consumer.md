# Actual general-positive-test event and variational lower bound

CANDIDATE PROOF, not adopted. Preproof statement/object audit passed
Opus5.5/HIGH with no required repairs at source14fe727. Full independent
scientific analytic/type/application review is REQUIRED. Original sharp
source constants, intended normalization and all dimensions remain open.

## 1. Exact fixed objects and scoped imports

Work with the original real d1 Stratonovich model,0<a<1,0<alpha<=1,
alpha+a<2, and its nonzero positive Riesz/white Radon covariance Gamma,
including its amplitude. Put kappa=(4-alpha-a)/(3-alpha)>0. Define
C_pos as all nonnegative nonzero real psi in C_c^infinity((0,1)xR).
Fix ONE such psi throughout Sections1-4, before delta tends to0. Set

 h_sigma(x)=int_0^1 |sigma-u|^-a (Gamma*psi(u,.))(x)du,
 q_avg(x)=int_0^1 psi(u,x)du, Z=W(psi),v=E Z^2,
 H_sigma=-d2-h_sigma on H2(R),0<=sigma<=1.                 (1)

Use the actual real F from local-causal-young-flow.md Section4: closure
of compact smooth phases PLUS both constants in uniformly local
H1/2 x H-1/2. Let e0=(1,0). Fix nonnegative smooth compact phi with
integral1. J(v,w)=<v,phi> is the UNSQUARED real bounded displacement
functional constructed in nonseparable-profile-family.md (13). The
phase remains (v,w); all projections below retain velocity.

Imported accepted inputs, with exact scope:
- nonseparable-profile-family.md S1-S3, (4),(8),(11)-(14),(19), with
  its scientific-adjudication-v1.md: the actual H_sigma has simple
  positive L2-normalized ground p_sigma, rate lambda_sigma>=l>0,
  and actual frozen physical wave P_sigma on F. Write
  e_sigma=(p_sigma,lambda_sigma p_sigma),
  ell_sigma(v,w)=(<p_sigma,v>+<p_sigma,w>/lambda_sigma)/2,
  Pi_sigma=e_sigma ell_sigma, Q_sigma=I-Pi_sigma. Then

 ell_sigma(e_sigma)=1,
 P_sigma(t)Pi_sigma=Pi_sigma P_sigma(t)=exp(lambda_sigma t)Pi_sigma,
 ||exp(-lambda_sigma t)P_sigma(t)Q_sigma||<=C_R exp(-eta t), (2)

  for ALL sigma in[0,1],t>=0, with C_R>=1,eta>0 uniform. The e,ell,Pi
  are norm-continuous and bounded in F,F*,B(F); lambda is Lipschitz
  and bounded above. Also a_*=inf_sigma ell_sigma(e0)>0 and
  j_*=inf_sigma J(e_sigma)>0. Uniform finite-horizon bounds follow
  from (2) and bounded Pi,lambda. Sigma is an INDEX, not coupling;
  lambda_0>0 although psi(0,.)=0. No bU theorem is invoked at b=0.
- joint-gaussian-tilt.md (5)-(6): (1) is its ACTUAL general-psi raw
  mean profile, by Tonelli, not psi(sigma,.). It is Lipschitz in sigma
  into C_b^1, bounded there, with uniform vanishing C1 spatial tails.
- local-causal-young-flow.md (4.4),(5.2)-(5.6),(7.1)-(7.3): actual
  masked B(F) driver reduction, physical Young flow/composition,
  bounded deterministic base and local stability, and uniform unit
  maximum. These are analytic inputs, not scalar Lean deductions.
- joint-gaussian-tilt.md (1),(7),(9),(12), Section5 unit identification,
  (13)-(14): actual common Gaussian/driver law, measurable physical
  shifted flow and signed average, SAME-Z identity for its square,
  and exact original-point consumer. Its class is GENERAL real psi;
  Banach separability in its driver construction is not tensor psi.
- Canonical T:full-upper, with alpha_0=a, gives a finite upper rate
  for this SAME original canonical solution. The exact model,
  expansion, mild-construction and theorem excerpts/custody are in
  reviews/2026-10-30-general-positive-consumer/canonical-*.

These imports do not contain this note's general-test event or lower
bound. Old moving-block, actual-event and variational notes motivate the
arguments below; their narrower separable/bU conclusions are not used
as general-test theorems. Define I=int_0^1 lambda_sigma dsigma.

## 2. Re-establish the indexed-family cone argument

For theta>0 define C_sigma(theta) as z=A e_sigma+r, where
A=ell_sigma(z)>0,ell_sigma(r)=0,||r||<=theta A. Fix0<rho<1/2.
All norms below are actual F,F*,B(F) norms. Choose finite constants

 M_e=max(1,sup||e_sigma||), M_l=max(1,sup||ell_sigma||),
 M_P=max(1,sup||Pi_sigma||), M_Q=1+M_P, M_z=M_e+1,
 E0=||e0||>0, H=max(1,||J||).

Choose FIRST theta=min(1,j_*/(16 H C_R))>0. Next choose INTEGER B>=1
so that q_B=C_R exp(-eta B)<=min(1/8,theta a_*/(8 M_Q E0)).
Next choose nu>0 with nu M_z<=min(rho/2,theta,1/4). Uniform continuity
on compact[0,1] supplies omega>0 so that |b-c|<=omega implies
||ell_b-ell_c||<=nu and ||Pi_b-Pi_c||<=nu. Halve a strict modulus
radius if needed. Finally choose epsilon_op>0 satisfying ALL

 M_l epsilon_op M_z<=rho/2, M_Q epsilon_op M_z<=theta/4,
 M_l epsilon_op E0<=a_*/2, M_Q epsilon_op E0<=theta a_*/8,
 H epsilon_op M_z<=j_*/8.                                (3)

Every right side is positive and every coefficient finite positive,
so the minimum of their five ratios works. These choices depend on the
fixed psi,phi,rho, never on the following N,s or index sequence. Theta
was selected BEFORE B; no exp(CB) terminal bound enters its choice.

Take ANY N>=1,indices sigma_0,...,sigma_N with adjacent gaps<=omega,
and real bounded operators D_m(t) on F,m=0,...,N,0<=t<=B, such that

 sup_(m,0<=t<=B)||D_m(t)-P_(sigma_m)(t)||<=epsilon_op.       (4)

No composition, positivity, independence or continuity of D is assumed.
Set z0=e0,z_(m+1)=D_m(B)z_m for0<=m<N. We prove

 J(D_N(s)z_N)>=c_*(1-rho)^(N-1)
 exp(B sum_(m<N)lambda_(sigma_m)+s lambda_(sigma_N)),
 0<=s<=B, c_*=a_*j_*/4>0.                                (5)

For entrance put b=sigma_0,E=(D_0(B)-P_b(B))e0. Then ||E||<=epsilon_op E0.
Commutation in (2),ell_b Q_b=0 and lambda_b>=l>0 give

 exp(-lambda_b B)ell_b(z1)>=a_*-M_l epsilon_op E0>=a_*/2,
 exp(-lambda_b B)||Q_b z1||
 <=q_B M_Q E0+M_Q epsilon_op E0<=theta a_*/4.              (6)

The ratio is <=theta/2, so z1 lies in C_b(theta), with amplitude at
least exp(lambda_b B)a_*/2. Constants were not put in global L2.

For any z=A e_b+r in C_b(theta),||z||<=M_z A. If |b-c|<=omega,
rebase BEFORE applying (2):

 ell_c(z)>=(1-nu M_z)A,
 ||Q_c z||=||Q_b z+(Pi_b-Pi_c)z||<=(theta+nu M_z)A.        (7)

For any full D with ||D-P_c(B)||<=epsilon_op, normalized amplitude
A'=exp(-lambda_c B)ell_c(Dz) is at least
(1-nu M_z-M_l epsilon_op M_z)A>=(1-rho)A>A/2. Its normalized residual
obeys

 exp(-lambda_c B)||Q_c Dz||
 <=[q_B(theta+nu M_z)+M_Q epsilon_op M_z]A<=theta A/2.     (8)

Indeed q_B<=1/8,nu M_z<=theta and the second (3) give
(1/8)(2theta)+theta/4=theta/2. The projection Q_c has range ker ell_c,
so (8) and A'>A/2 imply Dz in C_c(theta), with amplitude factor at
least exp(lambda_c B)(1-rho). This holds for every full block.

For the terminal time0<=s<=B, (7) gives ell_c(z)>=3A/4,
||Q_c z||<=2theta A. Equation (2), j_* positivity and the FIRST choice
of theta give

 exp(-lambda_c s)J(P_c(s)z)
 >=(3j_*/4-2H C_R theta)A>=5j_* A/8.

The normalized terminal perturbation is at most
H epsilon_op M_z A<=j_* A/8, since exp(-lambda_c s)<=1. Therefore

 J(D_N(s)z)>=(j_*/2)exp(lambda_c s)A,                     (9)

when c=sigma_N and z is in the previous cone. This proves a positive
average, not merely a norm-growth estimate. Inducting (8) from (6)
gives the amplitude of z_N at least
(a_*/2)(1-rho)^(N-1)exp(B sum_(m<N)lambda_(sigma_m)). Apply (9).
For N=1 the induction is empty. Times s=0 and indices sigma=0 are
included; (4) suffices even without D_N(0)=I. This proves (5).

The three unchanged MovingCone finite lemmas match exactly: residual_budget
has q=q_B,d=nu M_z,e=M_Q epsilon_op M_z and (8)'s bracket;
cone_conversion takes x=A',y=the normalized residual,a=A;
terminal_margin takes j=j_*,K=H C_R,e=H epsilon_op M_z. Each scalar
hypothesis follows above; their kernels do not supply (2),(4) or (7).

## 3. Discharge the premise for the actual retained noisy flow

Fix c_obs>=1+support-radius(phi),delta in(0,1],L=1/delta,
r=c_obs/delta,g=delta^((1-a)/2). Use the SAME jointly defined W^delta,Z
from the tilt, and actual physical evolution mathcalP_delta(t,s) for

 g zeta_r W^delta(u,x)+zeta_r h_(delta u)(x),0<=u<=L.       (10)

Define Y_delta=J(mathcalP_delta(L,0)e0), a signed measurable real variable.
Measurability follows from the accepted continuous Young map and scalar
pairing before squaring, not from point evaluation. No residual is
removed or resampled.

Uniform tails and derivatives of h in Section1 imply

 d_r=sup_(sigma in[0,1])||(zeta_r-1)h_sigma||W1infinity ->0. (11)

The function term and the term (zeta_r-1)h'_sigma are bounded by their
uniform exterior tails on |x|>=r, and zeta'_r h_sigma by
C sup_sigma||h_sigma||infinity/r. In the white case h_sigma has common
compact spatial support, but compactness is not required for Riesz.
For auxiliary padded units cap h_bar(t)=h_(min(t,1)),t>=0. This is
Lipschitz in C_b^1 with common bound K and uniform tails. The profiles

 h_(delta,j)(u)=zeta_r h_bar(delta(j+u)),0<=u<=1,
 j=0,...,ceil(L),                                        (12)

satisfy local-flow(5.6) with zero constant part and one common W1infinity
bound, independent of r>=1,j,delta. Frozen h_sigma satisfy it as well.
Multiplication by the smooth bounded mask preserves these properties.

For a FIXED integer B selected by Section2, let N=floor(L/B),s=L-NB
and sigma_m=delta mB,m=0,...,N. These are in[0,1], with adjacent gaps
delta B. For every used unit piece of block m, slow Lipschitz variation
and (11) give

 sup_used ||h_(delta,j)(u)-h_(sigma_m)||W1infinity
 <=C_h delta B+d_r=:a_delta(B)->0.                        (13)

Here j=mB+nu,nu integer,0<=nu<B; for the last block use only physical
times through L. The same bound holds on the capped padding if needed.
Every constant here is fixed before delta tends to0.

Let x_delta be g times the accepted maximum of local HS Ctheta driver
norms over relevant spatial cells and integer unit starts j<=ceil(L).
Choose a fixed p>4/(1-a). By local-flow(4.4),(7.1)-(7.3),

 ||x_delta||Lp<=C_p delta^((1-a)/2-2/p)->0.                (14)

This is a measurable finite maximum of separable path norms; it uses no
independence. It includes FULL units ending at ceil(L)+1<L+2. This
already accepted less-than-two-unit padding is cited openly, with (12)
defining its deterministic base. The physical observable only uses the
prefix through L. No new B-long stochastic extension will be used.

On {x_delta<=1}, accepted unit stability bounds the actual unit flow's
operator difference from its deterministic (12) flow by C_1 x_delta,
uniformly in all local endpoints. The difference of interaction
primitives for deterministic (12) and frozen h_(sigma_m) is bounded
in Ctheta B(F) by C a_delta(B), by local-flow(5.5). Then (5.3) gives
the physical flow difference <=C_2 a_delta(B). Thus every USED actual
unit piece differs from its corresponding frozen piece by at most

 e_delta=C_1 x_delta+C_2 a_delta(B).                       (15)

Both piece norms are <=A for one deterministic A>=1 on this event.
Use deterministic (5.2), bounded free physical conjugations on[0,1],
common K, and add C_1 x_delta<=C_1. Unit reset is essential: by accepted
tilt Section5 and local-flow Section7, the field at fast time j+u is
exactly W_j^delta(u) on the same common Gaussian space. The phase is
(V,partial_u V); no norm of the large-time free group S(j) enters.

For completeness the required finite ordered-product estimate is

 A_(n-1)...A_0-B_(n-1)...B_0
 =sum_(k<n) B_(n-1)...B_(k+1)(A_k-B_k)A_(k-1)...A_0.       (16)

For n=1 it is immediate. To pass n to n+1, split the difference as
B_n times the old difference plus (A_n-B_n) times the old A product;
substitution gives exactly (16). Empty products are identity. With
factor norms<=A and differences<=e_delta, (16) bounds the difference
by n A^(n-1)e_delta<=n A^n e_delta. Both finite factor sequences can
be extended by IDENTITIES, so ALL-index norm bounds and differences
remain valid. The prefix difference d_n then satisfies d_0=0 and
d_(n+1)<=A d_n+A^n e_delta using the alternative split with A_n.
This discharges all hypotheses of unchanged finite_error_accumulation;
it proves only the scalar bound d_n<=n A^n e_delta, not the operator
recurrence. The latter was proved here by norm inequalities.

Since B and mB are integers, [mB,mB+t] has at most B unit pieces for
0<=t<=B, including a possible final partial piece. Actual composition
and frozen autonomy identify their products, with identity at t=0.
Equations (15)-(16) imply, on {x_delta<=1},

 sup_(m,used t)||mathcalP_delta(mB+t,mB)-P_(sigma_m)(t)||
 <=B A^B e_delta.                                        (17)

Used t is all[0,B] for m<N and only[0,s] for m=N. This estimates fixed
B products, never the full long product. For m<N define the actual
D_m(t)=mathcalP_delta(mB+t,mB),0<=t<=B. Define D_N the same way up to
s, and for s<t<=B put

 D_N(t)=P_(sigma_N)(t-s)D_N(s).                            (18)

Let M_B=max(1,sup_(sigma,0<=t<=B)||P_sigma(t)||)<infinity, as follows
from (2) and bounded lambda,Pi. Autonomy shows
D_N(t)-P_(sigma_N)(t)=P_(sigma_N)(t-s)[D_N(s)-P_(sigma_N)(s)].
Thus the FULL premise (4) has error at most the scalar

 xi_delta=M_B B A^B e_delta ->0 in probability,            (19)

on {x_delta<=1}. For s=0, D_N(0)=I and extension (18) is exactly the
frozen flow. No new noise past L is needed by (18); observed D_N(s)
is unchanged. Strong continuity suffices; all time bounds are suprema
of differences. For fixed delta the finitely many blocks are on accepted
simultaneous versions; no uncountable parameter exceptional-set exchange
is made.

Now fix a desired e>0. Choose rho in(0,1/2) with log(1-rho)>-e/3.
Choose theta,B,nu,omega,epsilon_op,c_* in Section2 in that order. Then
take delta sufficiently small that N>=1 and delta B<=omega. All these
constants depend on the fixed psi,phi,e; no across-test uniformity is
claimed. Define the MEASURABLE event

 E_delta={x_delta<=1,xi_delta<=epsilon_op},                 (20)

where xi_delta is the scalar expression (19) with (15) even off the
event. By (11),(13)-(14),P(E_delta)->1. On it, the actual (17)-(19)
DISCHARGE (4). Actual evolution composition gives exactly

 Y_delta=J(D_N(s)D_(N-1)(B)...D_0(B)e0).

Equation (5) applies with sigma_m=delta mB. Its normalized rate is
R_delta=delta[B sum_(m<N)lambda_(delta mB)+s lambda_(delta NB)].
The nonnegative weights sum to1. Integrating the left-endpoint error
on each slow interval of length at most delta B bounds
|R_delta-I| by the modulus of continuity of lambda at delta B, hence
it tends to0. Also0<=delta(N-1)<=1/B<=1, so

 delta(N-1)log(1-rho)>=log(1-rho)>-e/3,
 delta log c_* ->0.

For small delta these losses plus R_delta-I imply, on E_delta,
Y_delta>=exp((I-e)/delta)>0. Consequently

 P{Y_delta>=exp((I-e)/delta)} ->1 for every e>0.            (21)

This proves the general-positive-test actual growth event.

## 4. Same-Z raw cost and the original point lower rate

Let U_delta be the accepted canonical NOISE-ONLY signed average on the
same common Gaussian/driver space, and M_delta=E U_delta^2. The exact
general-psi identity, tilt(13), is

 M_delta=E[exp(-Z/sqrt(delta)-v/(2delta))Y_delta^2].          (22)

This is a MINUS density, with the SAME Z and raw half-variance cost.
Section5 below proves0<v<infinity directly; it also follows from the
accepted Gaussian construction. Chebyshev gives
P{|Z|>delta^(-1/4)}<=v delta^(1/2)->0. Intersect its complement with
(21)'s event, denoting its probability by p_delta. The union bound
implies p_delta->1, with no independence. Nonnegativity of the SQUARE
integrand permits restriction in (22), yielding

 M_delta>=p_delta exp((2I-2e-v/2)/delta-delta^(-3/4)).       (23)

For small delta,p_delta>=1/2, so delta log p_delta->0. The normalized
moderate penalty is delta*(delta^(-1/4)/sqrt(delta))=delta^(1/4)->0,
exactly the unchanged moderate_penalty scalar lemma for delta>0.
Taking lower limits in (23) and then e down0 gives
liminf_(delta down0)delta log M_delta>=2I-v/2.

Tilt(14) with delta=t^-kappa and physical R=t delta identifies this
NOISE-ONLY average with its original canonical consumer, and gives
M_delta<=E|u(t,0)|^2. Its phi has unit mass; no R^d loss occurs. The
bijection t=delta^(-1/kappa) carries all sufficiently small delta to
large t. Therefore for the SAME original canonical Stratonovich u,

 Q2:=liminf_(t->infinity)t^-kappa log E|u(t,0)|^2
      >=2I_psi-v_psi/2 for EACH fixed psi in C_pos.         (24)

No signed first-moment restriction is made. This proves the actual
raw-cost original-point lower bound for the enlarged positive class.

## 5. Intrinsic variance, fixed dilation and real suprema

The function q_avg is smooth compact nonnegative and nonzero: a positive
value of the continuous psi has a space-time open neighborhood of
positivity, so its time integral is positive on an interval. Since
|sigma-u|^-a>=1 almost everywhere on[0,1]^2, Tonelli gives
h_sigma>=Gamma*q_avg for every sigma. The covariance bilinear form and
Tonelli give the intrinsic RAW variance

 v_psi=int_0^1 int_R psi(sigma,x)h_sigma(x)dx dsigma.        (25)

It is finite because h is bounded and psi integrable, and
v_psi>=int_R q_avg(x)(Gamma*q_avg)(x)dx>0. For white Gamma=c_Gamma delta_0
this last integral is c_Gamma int q_avg^2>0; for Riesz, local
integrability gives finiteness and positivity on the product of an
interval where q_avg>0 gives strict positivity. Also
0<I_psi=int_0^1 lambda_sigma dsigma<infinity by Section1.

For each fixed s>0 define the intrinsic test dilation

 (D_s psi)(t,x)=s^(3-alpha)psi(t,sx).                       (26)

It maps C_pos bijectively to itself: compact support rescales, positivity
and smoothness persist, and D_r D_s=D_(rs),inverse D_(1/s). With Gamma
fixed, its pushforward under y->sy is s^(alpha-1)Gamma, since
Gamma(A/s)=s^(alpha-1)Gamma(A). Thus, for every sigma, Tonelli and the
Radon change of variables give

 h_(D_s psi),sigma(x)
 =s^(3-alpha)int_0^1 |sigma-u|^-a int psi(u,sx-sy)Gamma(dy)du
 =s^2 h_psi,sigma(sx).                                    (27)

This includes white alpha=1 directly, without a false Lebesgue Jacobian
for a Dirac measure; the covariance amplitude is unchanged. The L2
unitary T_s f(x)=sqrt(s)f(sx) has inverse T_(1/s) and maps H2 onto H2.
Weak differentiation tested against compact smooth functions gives
(T_s f)''=s^2 T_s(f''). Hence on the ENTIRE H2 domain, (27) gives
H_(D_s psi),sigma=s^2 T_s H_psi,sigma T_s^(-1). Unitary conjugation
scales the full spectrum and its bottom, so
lambda_(D_s psi),sigma=s lambda_psi,sigma. Integrating and using (25)
with the ordinary dx Jacobian proves

 I_(D_s psi)=s I_psi, v_(D_s psi)=s^(4-alpha)v_psi.         (28)

This is an L2 spectral/class calculation, not an F isometry or a new
noise law. Every s/test is fixed before the time limit in (24), with
its own admissible flow constants. No s(delta) or uniform test estimate
is used. The unchanged dilation_factors lemma needs only s>0 and
checks the two exponents in (27)-(28), not these analytic identities.

For c>0 let S_c^pos={cI_psi-v_psi/2:psi in C_pos}. These are nonempty
sets of real numbers, since products of nonzero nonnegative smooth
compact bumps in time and space give elements of C_pos. The accepted
canonical full upper rate supplies a finite C_up independent of psi.
Together with (24), it implies

 2I_psi-v_psi/2<=Q2<=C_up for every psi.                    (29)

A single test gives a finite lower bound for Q2, so Q2 is a finite real
number. In particular S_2^pos is bounded ABOVE, and S_1^pos is also
bounded above since I_psi>0. Define V_1^pos=sup S_1^pos as a real
supremum of a nonempty bounded-above set; no optimizer is assumed.

Put k=3-alpha>0,m=(4-alpha)/(3-alpha)=(k+1)/k. For any fixed test
with I,v>0 choose s0=(I/v)^(1/k)>0. Then s0^k=I/v, and (28) gives
the score at D_s0 psi equal to s0 I-s0^(k+1)v/2=s0 I/2>0.
Thus V_1^pos>0. The unchanged positive_score lemma applies with these
actual I,v>0 and alpha<3. Now fix c>0 and s=c^(1/k). Positive real-power
identities give c s=s^(k+1)=c^m. For EVERY psi, (28) gives

 cI_(D_s psi)-v_(D_s psi)/2=c^m(I_psi-v_psi/2).             (30)

This is the unchanged label_score scalar identity with c>0,alpha<3.
Since D_s is a bijection, S_c^pos=c^m S_1^pos as sets. Hence S_c^pos
is nonempty and bounded above by c^m V_1^pos, so its REAL supremum
V_c^pos is well-defined BEFORE invoking any supremum algebra.
Every score in S_c^pos is <=c^m V_1^pos, proving V_c^pos<=c^m V_1^pos.
Conversely (30) and the upper-bound property of V_c^pos show every
score in S_1^pos is <=V_c^pos/c^m. Leastness of V_1^pos gives the
reverse inequality. Therefore

 0<V_c^pos=c^((4-alpha)/(3-alpha))V_1^pos<infinity,c>0.     (31)

Each fixed-test (24) implies Q2>=V_2^pos: alternatively choose for
every epsilon>0 a FIXED score larger than V_2^pos-epsilon, apply (24)
and let epsilon down0. No interchange of a time limit and supremum
is needed. Define C_sep as the positive product class in
raw-variational-dilation.md Section1, and V_2^sep as its score supremum.
If psi=f tensor q is in that class, (1) is EXACTLY
h_sigma=k_f(sigma)(Gamma*q), so its H_sigma and lowest rate are the
old H_(k_f(sigma),q) and lambda_(k_f(sigma),q). The new intrinsic I is
therefore the old integral of that rate; (25) factors as A_f B_q,
exactly its old raw variance. Thus the score functions agree on C_sep,
and C_sep subset C_pos gives V_2^pos>=V_2^sep. In all,

 0<V_2^sep<=V_2^pos<=liminf t^-kappa log E|u(t,0)|^2
 <=limsup t^-kappa log E|u(t,0)|^2<infinity.                (32)

This proves the enlarged positive-test variational lower. No strict
VALUE gap between the two classes is asserted.

## 6. Calibration and certification boundaries

c is an auxiliary VARIATIONAL LABEL, not a theorem for arbitrary moment
order. Equation (31) has exponent(4-alpha)/(3-alpha); white alpha=1
gives3/2 and variance degree3 in (28), and the moment-power exponent
matches the static calibration. No a->0 limit interchange is proved.
Since m>1, the unchanged strict_label_factor with alpha<3 also gives
V_2^pos>2V_1^pos. This concerns these raw scores only. V_1^pos has NOT
been identified with the actual first-mean growth or source L_*,E,E_star;
there is no claimed improvement over actual Jensen. Existing Jensen
remains available independently, regardless of this additional bound.
No source normalization repair or source constant is imported into (29).
The original source's intended correction remains UNKNOWN.

Nine generic finite Lean kernels (three MovingCone,two ActualEvent,
four RawVariational) are reused unchanged with complete public types
and prior local receipts bound in the review packet. Their NEW actual
application hypotheses have been proved above but still need independent
scientific review. The rate/variance/class/operator/Young/Gaussian/
probability/supremum arguments are analytic, not kernel-certified by
scalar arithmetic. No new package/companion, donor modification,
cluster job or full-goal/formal waiver is created.

General positive smooth controls remain distinct from signed Gaussian
controls and the source occupation-profile optimizer class. No optimizer
density, source equality, sharp upper constant, original higher-dimensional
extension, Skorohod result, novelty or whole-paper/circulation clearance
is claimed. Canonical TeX/PDF stay unchanged. Full independent scientific
proof/type/application review is required before adopting (21),(24),(31)-(32).
