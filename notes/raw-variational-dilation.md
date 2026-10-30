# Raw variational dilation of the accepted second-moment lower bound

CANDIDATE, not independently accepted. The proposed statement passed its
preproof class/fidelity/feasibility audit at6203ab7,12groups/HIGH; this is
not proof acceptance. V_c below is an auxiliary raw variational label.
No first-mean, source-constant, optimizer or sharp upper identification is
claimed. Original full upper/sharp and dimensional goal remains active.

## 1. Class, representation independence, and exact imported bounds

Fix d1,0<a<1,0<alpha<=1,alpha+a<2 and the original nonzero positive
Riesz/white covariance Gamma, including its fixed amplitude. Its Radon
homogeneity is Gamma(sA)=s^(1-alpha)Gamma(A),s>0. Write C_sep for the
SET OF FUNCTIONS psi(t,x)=f(t)q(x), where EACH factor is nonnegative,
nonzero and smooth compact, supp f contained in(0,1), q on R.
The class is nonempty: take the standard smooth bump
b(x)=exp(-1/(1-x^2)) for |x|<1 and0 otherwise, then f(t)=b(4t-2),q=b.
All derivatives at its boundary vanish because they are finite sums of
rational powers times this exponential, so these are legitimate tests.

Use the raw covariance and actual spectral objects of the accepted
notes/actual-shifted-event.md and notes/spectral-ground-family.md:

 k_f(t)=integral_0^1 |t-u|^-a f(u)du, U_q=Gamma*q,
 H_(b,q)=-d2-bU_q on domain H2(R),
 E1(b,q)=inf spectrum H_(b,q)<0,
 lambda_(b,q)=sqrt(-E1(b,q))>0,
 I_psi=integral_0^1 lambda_(k_f(t),q)dt, v_psi=E W(psi)^2.    (1)

All spaces/noises are real; spectral statements use complexification of
the accepted real-potential self-adjoint operators, with real restriction
as appropriate. For each fixed test, k_f has a positive compact range
contained in one K_par, and the accepted ground rates are positive,
continuous and bounded there. Hence I_psi is finite and positive.

I_psi depends only on psi, not its factorization. Indeed if f q=F Q,
choose t0,x0 with f(t0)q(x0)>0. Then F(t0)>0,Q(x0)>0. Evaluating at t0
gives Q=q/l with l=F(t0)/f(t0)>0, and evaluating at x0 then gives F=l f.
Thus k_F=l k_f,U_Q=U_q/l and the ACTUAL potential k_F(t)U_Q equals
k_f(t)U_q. Its operator and lowest rate, hence I_psi, are unchanged.
v_psi is already intrinsic by W(psi). Equivalently the potential is the
raw covariance convolution of psi, so it is determined by that function.

The raw variance factors exactly as

 v_psi=A_f B_q,
 A_f=integral_0^1 f(t)k_f(t)dt,
 B_q=integral_R q(x)U_q(x)dx.                              (2)

This follows directly from the covariance bilinear form and Tonelli, with
nonnegative factors; it contains no Fourier normalization. A_f is finite
because k_f is bounded, and positive because k_f>=integral f>0.
B_q is finite since U_q is bounded and q compact. In the white case
Gamma=c_Gamma delta_0 it equals c_Gamma integral q^2>0. For Riesz,
c_Gamma|x-y|^-alpha is positive and locally integrable; since q is positive
on an interval, its double integral against q(x)q(y) is positive. Thus

 0<I_psi<infinity, 0<v_psi<infinity.                        (3)

Two INPUTS are scoped accepted, not proved again:
- Actual shifted-event(4) gives, for EACH fixed psi in this class,
  Q2>=2I_psi-v_psi/2, where
  Q2=liminf_(t->infinity)t^-kappa log E|u(t,0)|^2.
- Canonical T:full-upper gives a finite limsup for the SAME canonical
  original point solution and kappa=(4-alpha-a)/(3-alpha).

The explicit upper dictionary is alpha_0=a. Its canonical expansion/mild
solution is the same original canonical u used by the accepted lower
consumer, not an arbitrary pathwise mild version. Exact H:homog, theorem
excerpt, current/source-at6203ab7 hash check and dependency paragraph are
in reviews/2026-10-30-raw-variational-dilation/accepted-upper-context.txt,
accepted-full-upper-statement.txt and upper-input-verification-v2.json.
Only finiteness is imported. The prefactor log(e(t+2)^d)/t^kappa tends
to0 because kappa>0. No first-mean or numerical static constant is used.
Therefore one number C_up<infinity, independent of the test, satisfies

 2I_psi-v_psi/2<=Q2<=C_up for all psi.                      (4)

A single test supplies a finite lower bound on Q2, so Q2 is a finite real
number. Every inequality here concerns one fixed canonical model/covariance;
changing the test does NOT change that model or the upper bound.

## 2. Intrinsic class dilation and Radon covariance calculation

For fixed s>0 define

 (D_s psi)(t,x)=s^(3-alpha)psi(t,sx),
 q_s(x)=s^(3-alpha)q(sx), so D_s psi=f tensor q_s.           (5)

q_s stays smooth, compact, nonnegative and nonzero, with support scaled
by1/s. Positive real-power multiplication gives D_r D_s=D_(rs), so
D_(1/s) is the inverse on C_sep. This is intrinsic to psi and compatible
with all its factorizations. The time profile k_f is unchanged.

Let T_s(y)=s y. Its pushforward measure is, for every Borel A,

 ((T_s)_#Gamma)(A)=Gamma(A/s)=s^(alpha-1)Gamma(A).            (6)

Thus integration of nonnegative Borel functions against this measure
gives the change of variables below, legitimate for compact smooth q:

 U_(q_s)(x)
   =s^(3-alpha)integral q(sx-sy)Gamma(dy)
   =s^(3-alpha)s^(alpha-1)integral q(sx-z)Gamma(dz)
   =s^2 U_q(sx).                                         (7)

This handles the white Radon endpoint directly: alpha=1 makes the
pushforward factor1 and U_(q_s)=c_Gamma s^2 q(sx). No Lebesgue-density
Jacobian has been incorrectly applied to delta_0, and the actual covariance
amplitude is retained. Riesz U is not made compact by this calculation.

## 3. Unitary spectral dilation and raw quadratic variance

Define the L2 unitary T_s g(x)=sqrt(s)g(sx); an ordinary Lebesgue change
of variables gives ||T_s g||2=||g||2 and inverse T_(1/s). Its weak derivatives
satisfy (T_s g)'=s T_s(g') and (T_s g)''=s^2 T_s(g''). For example these
follow by testing against compact smooth functions and changing variables;
applying the same argument to the inverse shows H2 is mapped bijectively.
For every g in the WHOLE domain H2, (7) therefore yields

 H_(b,q_s) T_s g=s^2 T_s H_(b,q)g,
 H_(b,q_s)=s^2 T_s H_(b,q) T_s^(-1).                        (8)

Both are the accepted self-adjoint operators on H2, so unitary conjugation
and multiplication by the positive scalar s^2 scale the full spectrum,
including its bottom. Thus E1(b,q_s)=s^2 E1(b,q), and

 lambda_(b,q_s)=s lambda_(b,q).                            (9)

The positive normalized eigenfunction is T_s p_(b,q): positivity and L2
normalization are preserved, and simplicity fixes this choice. This is an
L2 spectral calculation, not an assumed isometry of the actual F phases
or a claim of scale-uniform physical error constants.

Since k_f is unchanged, integration of (9) gives

 I_(D_s psi)=s I_psi.                                     (10)

Also (2),(7) and the ordinary dx change of variables give

 v_(D_s psi)
  =A_f integral s^(3-alpha)q(sx) s^2 U_q(sx)dx
  =s^(4-alpha) v_psi.                                    (11)

This scales the RAW VARIANCE, not its square root. At white alpha=1 it
is s^3. Gamma itself and the underlying point-moment problem stay fixed.
For every fixed s, D_s psi is a permitted fixed test for the lower input;
its own ground-family/event constants may depend on s. No substitution
s=s(delta) or uniform event estimate over s is used anywhere.

## 4. Well-defined real suprema and a positive value

For c>0 let S_c be the set of real scores cI_psi-v_psi/2, psi in C_sep.
Each S_c is nonempty by the explicit bump example. Equations (3)-(4)
show S_2 is bounded above. Also each I_psi-v_psi/2 is <=2I_psi-v_psi/2,
so S_1 is bounded above by the same C_up. Define the real supremum
V_1=sup S_1; the real completeness theorem applies to a NONEMPTY bounded
set, and no optimizer is assumed.

V_1>0. Choose any fixed test with I=I_psi>0,v=v_psi>0 and put

 k=3-alpha>0, m=(4-alpha)/(3-alpha)=(k+1)/k,
 s0=(I/v)^(1/k)>0.                                       (12)

Then s0^k=I/v. By (10)-(11), the score at its fixed dilate is

 I_(D_s0 psi)-v_(D_s0 psi)/2
    =s0 I-s0^(k+1)v/2=s0 I/2>0.                           (13)

This one positive score forces the real supremum to be positive. Scale
s0 is fixed by this test before any time limit; no maximizing sequence
is used in the stochastic estimate.

## 5. Label homogeneity, lower consumer and strict auxiliary comparison

Fix c>0 and put s=c^(1/k)>0. Elementary positive-base real-power identities
and m in (12) give c s=s^(k+1)=c^m. Consequently, for EVERY test psi,

 c I_(D_s psi)-v_(D_s psi)/2
      =c^m (I_psi-v_psi/2).                               (14)

Because D_s is a bijection of C_sep, S_c is EXACTLY the positive scalar
multiple c^m S_1. In particular every element of S_c is <=c^m V_1,
so this nonempty set is bounded and has a well-defined real supremum V_c.
This argument establishes finiteness before using any properties of V_c.
It also gives V_c<=c^m V_1. Conversely (14) and the upper-bound property
of V_c imply I_psi-v_psi/2<=V_c/c^m for every psi. Leastness of V_1
as an upper bound gives V_1<=V_c/c^m, hence the reverse inequality.
Therefore

 V_c=c^((4-alpha)/(3-alpha)) V_1, c>0.                     (15)

This also proves V_c>0 for every positive label c. Since m=1+1/k>1,
2^m>2, and positivity of V_1 gives

 V_2=2^((4-alpha)/(3-alpha))V_1>2V_1.                      (16)

Finally the fixed-test input in (4) gives Q2>=V_2. One may see this without
any interchange of a supremum and a time limit: for every e>0, the defining
property of the finite supremum supplies a fixed test with score at c2
larger than V_2-e. Its accepted lower bound implies Q2>=V_2-e; let e down0.
Together with the independent upper input,

 0<V_2<=liminf t^-kappa log E|u(t,0)|^2
       <=limsup t^-kappa log E|u(t,0)|^2<infinity.           (17)

This is the raw positive-separable variational lower bound for the original
d1 Stratonovich model, not the requested source sharp-constant theorem.

## 6. Source, calibration and formal boundaries

c in (15) is a VARIATIONAL LABEL. V_1 has not been identified with actual
first-moment growth, source L_*, E or E_star. The strict comparison (16)
is NOT an improvement over actual Jensen. It isolates the expected factor
inside this raw test-class functional only. The signed first-moment
restriction needed for an analogous stochastic c1 proof is not asserted.

At alpha=1, (5),(7),(11) give q_s=s^2q(sx), U_s=s^2U(sx), raw variance
s^3 and exponent3/2. The exponent in (15) is independent of a, matching
the expected static moment-power exponent as a calibration; no a->0
limit interchange or numeric static white constant is imported.
The construction uses the accepted Stratonovich/ordinary-product actual
flow and its point-moment consumer. No Skorohod asymptotic is deduced or
assumed equal. Original higher dimensions remain open.

Pinned source p4 E has raw time kernel and gradient penalty1, while
E_star has a damped kernel and penalty1/2. The retained HIGH audit's
literal discrepancy and UNKNOWN intended normalization remain unchanged.
No numerical value, correction or equality with either source object
has been adopted. Exact current upper-context and source dictionaries
use only accepted finite-rate input, not a printed first-mean upper value.

The finite rational diagnostics verify six exponent/normalization cases
only; they do not prove Radon transformations, unitary equivalence or
supremum arguments. Four local real-power deductions (dilation factors, label score, positive
score and strict label factor) now compile/replay cleanly on the pinned
latest stable Lean/Mathlib4.35.0, with complete public types/live standard
three axioms, five matching owned outputs and three numerical False
controls. Evidence/fences in lean-progress/local-checks/raw-variational-v1/.
A prior warning-bearing server-hash refusal is preserved separately; only
two tactic sequencing tokens changed, no public types. These are scalar
checks, not measure/spectral/class/supremum proofs. Full independent
scientific analytic/type/application review remains REQUIRED before
adopting this note.
No general/nonseparable optimizer approximation, source constant match,
sharp upper theorem, whole-paper/novelty/circulation or companion claim.
Canonical TeX/PDF unchanged; this is an internal candidate proof.
