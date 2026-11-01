# Unmasked Rayleigh rates and an intrinsic all-dimensional lower functional

ACCEPTED at the scoped full analytic/source/type/application gate:
Opus5.5/HIGH,11checks PASS/PASS_WITH_NOTES,303.405seconds, no required
repairs, scientific source61ac2a3. Seven optional clarifications are recorded
in reviews/2026-10-31-unmasked-variational-target/scientific-adjudication-v1.md.
Frozen proof/report bytes remain unchanged. The earlier statement gate was
separate. Original sharp/source goal remains ACTIVE.

## 1. Exact class, conclusions and accepted inputs

All objects are real unless a self-adjoint operator is complexified. Fix
one nonzero original H:homog covariance Gamma in d=1,2,3, temporal a in(0,1),
0<alpha<d or alpha=d=1, and alpha+a<2. Keep its actual amplitude. Its even
positive tempered Radon spectral measure has convention

 Gamma=int exp(i xi.x)mu(dxi) as tempered distributions.             (1)

Let C_pos be ALL nonnegative nonzero real C_c^infinity((0,1)xR^d) tests,
including nonseparable tests. It is nonempty: with b(z)=exp(-1/(1-z²))
for |z|<1 and0 otherwise, b(4s-2) product_(j=1..d)b(x_j) belongs to C_pos.
Every derivative at a boundary is zero by exponential decay against any
power of (1-z²)^-1, so this is a legitimate smooth compact test.
For each Psi in C_pos put

 h_s(x)=int_0^1 |s-t|^-a (Gamma*Psi(t,.))(x)dt,
 v_Psi=int_0^1 int_Rd Psi(s,x)h_s(x)dx ds.                         (2)

The SAME raw variance E W(Psi)² equals v_Psi. No covariance or test is
changed by a spatial noise mask. The proposed conclusions are:

 - h is globally bounded and smooth in x, with every mixed derivative
   bounded uniformly on compact time intervals. H_s=-Delta-h_s on H2
   is self-adjoint; E_s=inf spectrum H_s is negative with a common floor
   away from0 on I=[0,1]. lambda_s=sqrt(-E_s) is positive Lipschitz on I.
 - For increasing smooth masks m_R, the accepted compact ground rates
   lambda_(R,s) increase uniformly on I to lambda_s. With
   I_Psi=int_I lambda_s ds, the ORIGINAL canonical point rate satisfies

                  Q2>=2 I_Psi-v_Psi/2.                           (3)

 - For every auxiliary c>0 the intrinsic scores

   S_c=sup_(Psi in C_pos)(c I_Psi-v_Psi/2)
       =c^m S_1 are positive finite real numbers,
   Q2>=S_2=2^m S_1, m=(4-alpha)/(3-alpha).                        (4)

S_1 is an auxiliary variational value, NOT an actual first moment, author
L_*, L^* or printed energy. No sharp upper or conditional exact limit is
claimed. In particular (4) is not an identified source-constant theorem.

OWN accepted inputs, at their EXACT scopes:
A. compact-mean-ground-family.md Sections1-2,7-8, scientificbfbd472/
   adoptionab6596f: real bounded COMPACT smooth potentials with a common
   negative H1 trial have actual positive ground rates/minmax values;
   for EVERY original Psi, one finite plateau/mask gives a common trial
   without changing Psi or v_Psi. Section7 mean smoothness is LOCAL only.
B. raw-block-event-lower.md(1), scientificd4d876e/adoptionc426e5a:
   for EACH original Psi and eligible fixed mask R, same original canonical
   Q2>=2int_I lambda_(R,s)ds-v_Psi/2, in ALL original covariance classes.
   Its source/Young/point identification, fixed-mask moment inequality and
   same-Z half-cost are accepted analytic inputs, not proved again here.
C. Canonical T:full-upper, its exact statement/context/custody in the
   packet: SAME H:homog canonical expansion solution, alpha_0=a and
   kappa=(4-alpha-a)/(3-alpha)>0. It gives

 E|u(T,0)|²<=e(T+2)^d exp(C_up T^kappa), T>=1, C_up<infinity.       (5)

   log(e(T+2)^d)/T^kappa->0: choose epsilon=kappa/2>0 and integrate
   x^(epsilon-1) to get log T<=(T^epsilon-1)/epsilon, T>=1.
   Also log(T+2)<=log T+log3. Division by T^kappa gives the claimed
   limit. Thus limsup of
   T^-kappa log E|u(T,0)|²<=C_up. This is the SAME original canonical
   solution as B, not the old d1 consumer mentioned in historical context.
   Exact all-dimensional identity pointers are upper-custody-v1.json
   and raw-block-event-lower.md Sections1,8, not the old d1 historical
   context consumer. Only finiteness is imported; no first-mean/static
   numeric constant.
D. RawVariational.label_score,positive_score,strict_label_factor, with
   COMPLETE public types in the packet, are OLD scalar finite facts.
   Their exact new guards/consumers are in Section7. No new kernel run.

The older raw-variational-dilation.md is ONLY a method comparator for
positive SEPARABLE tests and d1 Riesz/white Gamma. Its stochastic/spectral
consumer and the older d1 rough occupation X theorem are NOT imported here.
No compact-potential essential-spectrum or positivity theorem is applied
to the UNMASKED H_s. Its bottom need not be an eigenvalue.

## 2. The Gaussian-convolution bound and global smoothness

Write p_e(x)=(2pi e)^(-d/2)exp(-|x|²/(2e)), e>0. Positivity and temperedness
of each Radon measure imply integrability of a sufficiently fast decreasing
polynomial weight: choose a nonnegative smooth cutoff equal1 on B1.
Temperedness bounds its dilation seminorms by C R^N for R>=1, hence
measure(B_R)<=C R^N by positivity. Summing dyadic annuli then makes
(1+|x|)^(-L) integrable for L>N. Apply this separately to Gamma and mu.
Hence Gaussian weights are integrable against both measures. For fixed x, the convolution int p_e(x-y)Gamma(dy) is finite,
and is smooth locally in x by dominated differentiation (Gaussian
translations/derivatives are bounded by such a polynomial weight locally).
We claim the exact convention-(1) identity

 (Gamma*p_e)(x)=int exp(i xi.x)exp(-e|xi|²/2)mu(dxi),
       0<=(Gamma*p_e)(x)<=(Gamma*p_e)(0)<infinity.                (6)

To justify it, pair the classical convolution with a Schwartz test phi.
Fubini is absolutely justified by the Gaussian and polynomial weights;
(1) applied to p_e*phi gives the right-hand distributional pairing, because
int p_e(y)exp(-i xi.y)dy=exp(-e|xi|²/2). Thus there is no extra Fourier
normalization factor: p_e is even, so its integrals against exp(+i xi.y)
and exp(-i xi.y) coincide, and int p_e(x-y)phi(x)dx=(p_e*phi)(y).
The mu Gaussian integral is absolutely finite and
its Fourier integral is continuous by dominated convergence. The classical
convolution is also continuous, so distributional equality gives equality
at EVERY x. The left side is nonnegative because Gamma is. Evenness of
mu makes the right side real, and its absolute value is at most the total
Gaussian spectral integral, its value at0. That value is strictly positive
because Gamma is nonzero and p_e is strictly positive. This proves (6).

Fix Psi and any mixed time/spatial derivative D Psi of its zero extension.
The extension is smooth because the time support lies inside(0,1).
For one fixed e>0, compactness of the common spatial support and boundedness
of D Psi give a constant C_D with

            |D Psi(t,x)|<=C_D p_e(x) for ALL t,x.              (7)

Indeed p_e has a positive minimum on that compact support. From(6)-(7),
Gamma*|D Psi(t,.)| is bounded uniformly in t,x. Ordinary local dominated
differentiation against the Radon measure gives Gamma*D Psi as the actual
corresponding spatial/time derivative. For the singular temporal integral,
change to r=s-t after zero extension:

 h_s(x)=int_R |r|^-a (Gamma*Psi(s-r,.))(x)dr.                   (8)

On each compact s interval the relevant r lie in a fixed bounded interval.
The bound from(7) times |r|^-a is integrable since a<1. Thus every time
or spatial derivative falls on the smooth TEST and passes through (8)
by dominated convergence. All such derivatives are globally bounded in x,
uniformly on that compact time interval. Nonnegativity follows from(2).
In particular M=sup_(s in I,x)h_s(x)<infinity, and bounded partial_s h gives

              ||h_s-h_t||infinity<=C_Psi |s-t| on I.          (9)

No decay of h at spatial infinity or nonnegative spectral eigenfunction
for the unmasked operator has been inferred. This proves the global mean
assertions of U1.

## 3. Unmasked operator, exact form domain and the negative rate

Let A=-Delta on complex L2(R^d), domain H2. Fourier transformation gives
self-adjointness and nonnegative spectrum directly: it is multiplication
by |xi|² with its maximal domain. B_s=-h_s is bounded self-adjoint, with
norm<=M. H_s=A+B_s on H2 is densely defined, closed and symmetric;
closedness follows from the graph norm equivalence under a bounded B_s.
For any real b>M,

 H_s-ib=(I+B_s(A-ib)^(-1))(A-ib)

is onto and has a bounded inverse, since ||B_s(A-ib)^(-1)||<=M/b<1
and the first factor has its convergent Neumann inverse. The same holds
with +ib. For completeness this proves self-adjointness without a compact
potential theorem: if u belongs to D(H_s*), solve
(H_s-ib)v=(H_s*-ib)u with v in D(H_s). Then u-v lies in
ker(H_s*-ib)=Ran(H_s+ib)^perp={0}; hence u=v and D(H_s*)=D(H_s).

On H2, the quadratic expression is
 q_s(f)=||grad f||2²-int h_s|f|², bounded below by -M||f||2².
Here is the whole H1 form-domain check, using the ordinary spectral theorem
as in accepted compact-family Section2, with no compactness assumption.
Set c_shift=1+M and J_s=H_s+c_shift>=1. For f in H2, integration by parts gives

 ||J_s^(1/2)f||2²=q_s(f)+c_shift||f||2²,
 ||f||H1²<=q_s(f)+c_shift||f||2²<=c_shift||f||H1².                       (10)

For f in D(J_s^(1/2)), spectral cutoffs 1_[1,n](J_s)f belong to H2
and converge in the half-power norm. Thus H2=D(J_s) is a core for the
J_s half-power norm, by spectral dominated convergence. H2 is dense in
H1 by Fourier cutoffs. Their completions in the equivalent norms (10)
therefore identify D(J_s^(1/2)) with H1 as ACTUAL L2 subspaces; both
completion norms dominate the L2 norm. Thus q_s is exactly the H1 form.

Its infimum over complex unit H1 tests equals E_s=inf spectrum H_s.
One direction follows from the spectral lower bound. For the reverse,
nonzero spectral projections in [E_s,E_s+epsilon] provide unit H2 vectors
with Rayleigh value<=E_s+epsilon; boundedness below ensures E_s is a finite
spectral point. Let epsilon down0. Real unit tests give the same infimum:
q_s(u+iv)=q_s(u)+q_s(v), and the quotient is the norm-weighted average of
the real quotients for nonzero u,v. The same real/complex observation holds
for compact masks. Accordingly write the positive rate using REAL tests:

 lambda_s²=sup_(f in H1 real,||f||2=1)
                     (int h_s f²-||grad f||2²)=-E_s.          (11)

Choose the accepted common negative trial from A for this ORIGINAL Psi:
one real unit compactly supported w in H1, epsilon0>0 and a finite
plateau mask m_(R0) obey
||grad w||2²-int m_(R0)h_s w²<=-epsilon0 for every s in I.
Here the cited trial has support in B_(2L); choose R0>=2L. Any plateau
mask equal1 on B_(R0), including the radial family defined in Section4,
agrees with the unmasked potential on supp w. Also 0<=m_(R0)<=1 and
h_s>=0, so the unmasked form on the same w is no larger.
Thus -M<=E_s<=-epsilon0<0 uniformly. In particular M>=epsilon0>0 and
lambda_s lies in[sqrt(epsilon0),sqrt(M)]. Taking the same unit infima in
|q_s(f)-q_t(f)|<=||h_s-h_t||infinity gives

 |E_s-E_t|<=||h_s-h_t||infinity,
 |lambda_s-lambda_t|<=C_Psi |s-t|/(2sqrt(epsilon0)).           (12)

Hence I_Psi is positive finite. No unmasked eigenvalue/isolation/essential
spectrum claim is used. This proves the remaining assertions of U1.

## 4. Monotone masks and the ORIGINAL point lower bound

Choose a smooth nonincreasing radial profile chi equal1 for r<=1 and0
for r>=2, with values in[0,1], and put m_R(x)=chi(|x|/R), R>0. Such a
profile is obtained from F(t)=exp(-1/t) for t>0 and0 otherwise by
chi(r)=F(2-r)/(F(2-r)+F(r-1)); its denominator is positive and the quotient
is nonincreasing. It is constant near0, so m_R is smooth at the origin.
These masks are even, compact and increase pointwise to1 as R increases.

Enlarge R0 if necessary so the accepted trial w from Section3 is supported
inside its plateau, as supplied by compact-family Section8. All R>=R0
then have the same negative trial/epsilon0, by monotonicity. The smooth
compact families m_R h_s satisfy accepted input A, with supports fixed
per R and s in I. Their actual ground rates satisfy the real H1 version
of(11) with h_s replaced by m_R h_s. Call them lambda_(R,s). They are
continuous and positive, bounded above by sqrt(M), and monotone in R.

For EVERY fixed real unit f in H1, dominated convergence gives
int m_R h_s f²->int h_s f² at each s, since h_s<=M and f² is integrable.
Thus lambda_(R,s)²<=lambda_s² and

 sup_(R>=R0)lambda_(R,s)²
  =sup_(R>=R0) sup_(unit real H1 f)(int m_R h_s f²-||grad f||2²)
  =sup_(unit real H1 f) sup_(R>=R0)(int m_R h_s f²-||grad f||2²)
  =lambda_s².                                                (13)

Only TWO suprema of real numbers have been interchanged. Positivity gives
lambda_(R,s) increasing to lambda_s. This convergence is uniform on I:
for integers n use R_n=R0+n. For epsilon>0 the open sets
{s:lambda_s-lambda_(R_n,s)<epsilon} are increasing and cover compact I;
a finite subcover is contained in the largest one. This proves uniform
convergence, and monotonicity extends it to all real R tending to infinity.
Consequently I_R=int_I lambda_(R,s)ds increases to I_Psi.

Apply accepted input B at EACH FIXED R>=R0 with the ORIGINAL Psi and
v_Psi. For the SAME number Q2 it gives Q2>=2I_R-v_Psi/2. Taking the
supremum of these numerical lower bounds AFTER their individual time
liminf gives (3). This is not a limit of stochastic solutions or events:
there is no R(delta), uniform-in-mask Gaussian estimate, source/time limit
exchange or unmasked noisy wave construction. Only compact operators
were asked to have a ground/gap/cone. This proves U2.

## 5. Exact all-dimensional Radon and Rayleigh dilation

For r>0 let (D_r Psi)(s,x)=r^(d+2-alpha)Psi(s,r x). It belongs to the SAME
C_pos class; D_(1/r) is its inverse, by multiplying the positive amplitude
powers. Homogeneity Gamma(r A)=r^(d-alpha)Gamma(A) gives the pushforward
identity for EVERY nonnegative measurable F,

 int F(r y)Gamma(dy)=r^(alpha-d)int F(z)Gamma(dz).              (14)

Indeed the left pushforward measure of a Borel A equals Gamma(A/r).
This measure argument includes singular/invariant Gamma and white noise;
it does not substitute a density or introduce a spurious Lebesgue factor.
Positive Tonelli, then(14), give

 h_(D_r Psi,s)(x)
 =r^(d+2-alpha)int_0^1 |s-t|^-a int Psi(t,r x-r y)Gamma(dy)dt
 =r² h_(Psi,s)(r x).                                         (15)

No temporal variable was rescaled. Using the actual raw pairing (2) and
now the LEBESGUE spatial substitution z=r x yields

 v_(D_r Psi)=r^(d+2-alpha)r²r^(-d)v_Psi=r^(4-alpha)v_Psi.       (16)

All equalities are between finite nonnegative integrals from Sections2-3
and input A. For a real unit H1 test f put U_r f(x)=r^(d/2)f(r x).
This is a unitary bijection of real L2 and preserves H1/H2 as sets under
inverse dilation. Differentiating its weak derivatives gives
||grad U_r f||2²=r²||grad f||2² and, by(15),
int h_(D_r Psi,s)(U_r f)²=r²int h_(Psi,s)f². The variational bijection
in(11) therefore gives

 lambda_(D_r Psi,s)=r lambda_(Psi,s), I_(D_r Psi)=r I_Psi.      (17)

Square roots are positive, so no sign ambiguity occurs. At the operator
level H_(D_r Psi,s)U_r=r²U_r H_(Psi,s) on H2, consistent with(17).
For compact masks the matching identity is
m_(R/r)(x)h_(D_r Psi,s)(x)=r²(m_R h_(Psi,s))(r x),
using m_R(r x)=m_(R/r)(x). A fixed R is NOT invariant under dilation.
This proves U3 without invoking the old d1 dilation_factors theorem.

## 6. Positive finite auxiliary scores and the p2 factor

From the original threshold, alpha<2<3, k=3-alpha>0, q=4-alpha=k+1>1,
and m=q/k>1. Fix any Psi0 in C_pos from Section1. Its I0=I_Psi0 and
v0=v_Psi0 are positive finite, the latter by accepted compact-family raw
variance assertion. Choose the EXACT positive radius

 r0=(I0/v0)^(1/k)>0.

It is not assumed less than1. The unchanged RawVariational.positive_score
with hI:I0>0,hv:v0>0,ha:alpha<3 gives

 I_(D_r0 Psi0)-v_(D_r0 Psi0)/2=r0 I0-r0^q v0/2>0.              (18)

Thus the set of label1 scores contains a positive real value, supplied by
an ACTUAL smooth positive test, not a formal scaling parameter.

For each c>0 put r_c=c^(1/k)>0 and K_c=c^m>0. The unchanged scalar
RawVariational.label_score has ONLY guards c>0 and alpha<3; applying it
with the real I_Psi,v_Psi and(16)-(17) gives, for EVERY Psi,

 c I_(D_rc Psi)-v_(D_rc Psi)/2
                 =K_c (I_Psi-v_Psi/2).                       (19)

Consequently the ENTIRE set of c-label scores is K_c times the ENTIRE
set of label1 scores, because D_rc is a bijection of C_pos. This is not
merely an inequality for a convenient subclass of tests.

We verify boundedness before treating any supremum as a finite real.
From(3) every label2 score is <=Q2. One fixed mask/test bound from input B
bounds Q2 below by a finite number; input C bounds its limsup above by
C_up. Hence Q2 is a finite real number and ALL label2 scores are bounded
above by the SAME C_up, independent of Psi. Equation(19) at c=2 and
K_2>0 then bounds every label1 score above by C_up/K_2. Its nonempty set
has a finite real supremum S_1, strictly positive by(18).

For general c, the set equality after(19) shows the c-score set is
nonempty and bounded above, and its supremum equals K_c S_1. Explicitly
K_c S_1 is an upper bound, and any smaller number is exceeded by K_c
times a label1 score within the corresponding positive distance of S_1.
Thus S_c is positive finite, S_c=c^m S_1 and Q2>=S_2. This proves (4).
RawVariational.strict_label_factor with alpha<3 also gives 2^m>2;
since S_1>0, S_2>2S_1 is ONLY an auxiliary-score comparison. S_1 has
never been proved to equal an actual first-mean rate. There is no Jensen
improvement or author-constant identity in this comparison. This proves U4.

## 7. Exact old finite consumers, falsification and scope

The two unchanged RawVariational source/public-type byte bindings are in
lean-reuse-v1.json, matched to the old reviewed packet. Three OLD facts
are consumed here: positive_score in(18) with I,v>0 and alpha<3;
label_score in(19) with c>0 and alpha<3, and arbitrary REAL I,v;
strict_label_factor with alpha<3 after(19). All guards follow explicitly
from the original threshold, (11)-(12), compact-family (22)-(23)
for v_Psi>0, and c>0. In(18) the generic Lean I,v are instantiated
with I0=I_Psi0 and v0=v_Psi0; in(19) with I_Psi,v_Psi. No new Lean run,
replay or count:71facts18local seams/L0 PROPOSED unchanged. The d1-specific
dilation_factors is NOT an all-dimensional Radon/Jacobian proof; (14)-(17)
are analytic. Gaussian smoothing, spectral calculus, form domain/core,
uniform mask limits, canonical moment inequality and supremum arguments
also remain ANALYTIC, not formalized by those scalar facts.

The invariant-direction diagnostic in falsification-v0 is retained. Its
one-dimensional negative trial can be supplied explicitly: for b(x1)>=0
nonzero compact and smooth, take a real unit plateau w_L with w_L>=c L^-1/2
on supp b for large L. Then int b w_L²>=c² L^-1 int b, whereas
||w_L'||2²=D L^-2. For large L the Rayleigh form is negative. This is a
ONE-DIMENSIONAL argument, not all-strength binding of a compact potential
in arbitrary dimension. Its accepted compact spectral input then supplies
the 1d ground. Long x2 tubes approach the two-dimensional bottom, while a
bottom eigenfunction would have zero x2 derivative and cannot be nonzero
in L2. Thus no unmasked ground projection/decay was silently used here.
The arbitrary-d Radon factor is explicitly(14); d1 white and d2 invariant
costs both give r^3, matching(16) at alpha1. The moving-mask check rejects
fixed-R scaling. Replacement of S_1 by an actual firstmean is an EXCLUDED
logical inference, not a numerically falsified identity in this model.

The exponent kappa has the required static limit (4-alpha)/(3-alpha) as
a tends to0. No optimized static constant is asserted. Canonical P:Jensen
and its conditional numerical specialization remain separate valid inputs;
any independently established lower rate can be combined with(4) by a
maximum. We do not change a p1 statement or identify a Skorohod constant.
Variational occupation approximation, all-alpha damped comparison, intended
source-energy normalization/domain dictionary, sharp upper and conditional
exact limit remain OPEN. No source repair/contacts/Skorohod/HPC/companion/
TeX/PDF/wiki/publication or whole-paper clearance. Full goal remains ACTIVE.
