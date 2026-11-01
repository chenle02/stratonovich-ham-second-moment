# The damped lower comparison on the entire original parameter range

ACCEPTED at the scoped FULL analytic/source/type/application gate:
Opus5.5/HIGH,10checks PASS/PASS_WITH_NOTES,318.460s, no required repairs,
scientific sourceed2e5f5. Two new scalar facts have local clean compile,
complete type/axiom audit, replay/controls and accepted actual applications.
Seven optional clarifications are in the scientific adjudication. Frozen
proof/report unchanged. Original full sharp/source goal remains ACTIVE.

## 1. Exact scalar definitions and accepted inputs

Fix 0<a<1, the TEMPORAL exponent; alpha below is the SPATIAL exponent. For a SCALAR damping D>0 put

 R(a,D)=2/Gamma_E(a) int_(s=0)^(1/2) int_(lambda=0)^infinity
                  lambda^(a-1)exp[-s(lambda+lambda²/(2D))]dlambda ds,
 Delta(q,a)=[qlogq+(q-2a)log(q-2a)]/2-(q-a)log(q-a), q>2a,
 J_a(q)=R(a,q-2a)exp(Delta(q,a)).                              (1)

Gamma_E is Euler's Gamma function, not the SPATIAL covariance Gamma.
J_a(q) is a scalar function, not the occupation interaction J(g) or the
energy map F_a(z). We will prove

 d_q log J_a(q)>=a²/[2(D+4a)(D+2a)]>0, D=q-2a,                (2)

and, for 0<alpha<2-a, q=4-alpha, k=3-alpha=q-1>1,

 M_a=Gamma_E((1+a)/2)/[Gamma_E(1+a)Gamma_E((1-a)/2)],
 Omega=[M_a J_a(q)]^(-1/k),
 0<M_a J_a(q)<=V(a/2)<1,
                 Omega>=V(a/2)^(-1/k)>1.                    (3)

No physical dimension is assigned to D. For the POINT consequence retain
ALL original H:homog hypotheses: d=1,2,3, nonzero original Gamma with
its amplitude, 0<alpha<d or alpha=d=1, alpha+a<2. The scalar range in(3)
is broader than any single dimension's model; it does not enlarge that
model. The accepted point input is OWN all-dimensional-static-occupation-
bridge.md(26), scientific249e2c4/adoptionaa4a016:

 Q2>=2^m Omega F_a(E_star^O), m=q/k,
 Q2=liminf_(T->infinity)T^(-kappa)log E|u(T,0)|²,
 kappa=(4-alpha-a)/(3-alpha).                                (4)

It uses the FULL strong-H1/a.e.unit/finite-integrated-gradient occupation
class and literal half-gradient energy, and proves its positive finiteness.
Its M_a, R_star, Delta and Omega agree with(1),(3): positive Tonelli in its
kernel/row definition gives R_star=R(a,q-2a). No old d1 X/HS flow or
firstmean theorem is imported as an all-dimensional stochastic premise.

Other OWN accepted scalar inputs, EXACT pinpoints:
- global-d1-damped-lower.md(3): R(a,D)<=B4(a,D), B4>0 for0<a<1,D>0,
  B4=sum_(j=0..4)(-1)^j Gamma_E((a+j)/2)/Gamma_E(a)
                     *2^a D^((a+j)/2)/[j!(j+2-a)].
  Positivity is through its positive Taylor integral, not alternating terms.
- That note(13) defines the literal rational V; (14) gives
  0<M_a B4(a,4-2a)expDelta(3,a)<=V(a/2), for0<a<1.
  These are PURE scalar results with no remaining spatial-alpha/dimension
  variable. Their old d1 stochastic consumer is NOT used.
- That note(17), and the unchanged GlobalOmega.rational_lt_one with COMPLETE
  definitions/public types, prove V(r)<1 for0<r<=1/2. Its exact new
  application r_a=a/2 is below. No certificate is changed or re-proved.

The new local AllAlphaMoment.moment_lower and rational_gap have exact
fenced types; their actual analytic guards are supplied in Sections2-3.
Equation numbers introduced by old/that note refer to that named input;
unqualified equation numbers below refer to this note.
They are only scalar deductions, not formal Gaussian/integral theorems.

## 2. Normalization, finite moments and the actual derivative

Let Z_mass(a,D) be the positive double integral in R BEFORE multiplying
by2/Gamma_E(a). It is a deterministic normalizing mass, not a Gaussian
variable from a prior noise tilt. The integrand is positive on an open
rectangle, so Z_mass>0. We prove finiteness and all needed domination.
For s>0,j>=0, the substitution v=s lambda²/(2D) gives

 int_0^infinity lambda^(a+j-1)e^(-s lambda²/(2D))dlambda
       =(1/2)(2D/s)^((a+j)/2)Gamma_E((a+j)/2).                (5)

Multiply by s^ell and integrate s over(0,1/2). This is finite whenever
ell-(a+j)/2>-1. We need only (j,ell)=(0,0),(1,1),(2,1); all satisfy this
because0<a<1. The additional E_D[s] used in Cauchy-Schwarz is trivially
finite and <=1/2 on its support. Dropping e^(-s lambda)<=1 bounds Z_mass and the
two first-moment integrals below by finite constants. On any compact
D interval [D_-,D_+] contained in(0,infinity), the SAME bounds with D_+
dominate uniformly. Euler Gamma's positive-argument integral is finite
and positive, so 0<R(a,D)<infinity.

Normalize the ACTUAL joint density
 lambda^(a-1)e^[-s(lambda+lambda²/(2D))]/Z_mass on(0,1/2)x(0,infinity).
It defines a probability, not a product law. Write its expectation E_D,

              m1=E_D[s lambda], m2=E_D[s lambda²]/D.         (6)

Both are finite nonnegative by(5). For each FIXED s>0 integrate the
derivative of lambda^a exp[-s(lambda+lambda²/(2D))] from0 to infinity.
The endpoint at0 is0 since a>0; the endpoint at infinity is0 by Gaussian
decay for this s>0. Its three terms integrate to

 int [a lambda^(a-1)-s lambda^a-(s/D)lambda^(a+1)]
                  exp[-s(lambda+lambda²/(2D))]dlambda=0.

Every term has finite joint absolute integral by(5). Thus integrating
this identity in s and using Fubini is justified separately for each
term, with no cancellation of infinities and no assumption at the excluded
null endpoint s=0. Division by Z_mass gives

                            m1+m2=a.                       (7)

Cauchy-Schwarz on the SAME probability, with factors sqrt(s) and
sqrt(s)lambda, gives m1²<=E_D[s]E_D[s lambda²]<=D m2/2 because s<1/2.
No independence is asserted. Apply the locally kernel-checked
AllAlphaMoment.moment_lower with x=m1,y=m2 and the ACTUAL guards a>0,D>0,
(7),m1²<=D m2/2. We obtain

                        m2>=2a²/(D+4a).                    (8)

For differentiation, the D-derivative of the density's unnormalized
exponential factor is s lambda²/(2D²) times itself. On [D_-,D_+] its
full unnormalized integrand derivative (including lambda^(a-1)) is
bounded in absolute value by D_-^(-2)/2 times
s lambda^(a+1)exp(-s lambda²/(2D_+)). This is integrable by(5).
Dominated differentiation and continuity therefore prove R is C1 in D,
with

                 partial_D log R=m2/(2D)
                              >=a²/[D(D+4a)].              (9)

The normalization itself was differentiated as an integral R, not silently
held fixed inside an expectation. Equations(7)-(9), including all
probabilistic/IBP/differentiation premises, are ANALYTIC; the finite lemma
only establishes the scalar implication from their explicitly listed guards.

## 3. Entropy derivative and monotonicity on ALL q>2a

For q>2a, D=q-2a>0 and q-a>0. Direct differentiation gives

 partial_q Delta=(1/2)log[q(q-2a)/(q-a)²]
               =-(1/2)log(1+a²/[D(D+2a)]).                 (10)

The identity uses (q-a)²=qD+a² and q=D+2a. For z>=0,
log(1+z)=int_0^z(1+t)^(-1)dt<=z. Hence(9)-(10) and the chain rule give

 d_q log J_a(q)>=a²/[D(D+4a)]-a²/[2D(D+2a)]
                 =a²/[2(D+4a)(D+2a)]>0.                    (11)

The equality and strict positive last expression are exactly the locally
kernel-checked AllAlphaMoment.rational_gap at its ACTUAL a>0,D>0 guards.
All denominators are positive. The preceding derivative identity and
integral/chain-rule inputs remain analytic. J is positive C1 and the
mean-value theorem applied to log J on any compact subinterval of(2a,infinity)
shows it is strictly increasing. This proves(2) over the entire stated
scalar domain, not just the physically admissible subinterval.

## 4. Exact old rational envelope and the new alpha>1 region

For clarity the literal V from the OLD definition(13) is

 P(r)=1-r²+r^4/2, g(r)=1-3r/5, L(r)=(177/100)(1-7r/5),
 C(r)=1/(3-2r)+(2r+1)(1-r)/[3(5-2r)],
 E(r)=1/[2(1-r)]+r(1-r)/(2-r)+r(r+1)(1-r)²/[3(3-r)],
 V(r)=2P(r)(1-4r²)/g(r)*[E(r)-2g(r)C(r)rL(r)]
                                *(3-4r)/(3-4r-2r²).        (12)

This is EXACTLY the current unchanged GlobalOmega.envelopeRational,
with exact rational constants. Its complete printed definitions and public
types and the prior/current byte binding are supplied. The old polynomial
and denominator certificates are reused, not renamed to the new damping D.

Now0<alpha<2-a gives q=4-alpha in(2+a,4), k=q-1>1 and q>2a.
By(11), J_a(q)<=J_a(4). Also(10) shows Delta decreases strictly in q;
since3>2a for0<a<1, Delta(4,a)<=Delta(3,a). Therefore the old scalar
R<=B4 input at D=4-2a>0 gives

 J_a(q)<=R(a,4-2a)expDelta(4,a)
       <=B4(a,4-2a)expDelta(3,a).

Multiplying by M_a>0, the EXACT accepted old(14) yields

                  0<M_a J_a(q)<=V(r_a), r_a=a/2.            (13)

Finally r_a>0 and r_a<1/2 discharge GlobalOmega.rational_lt_one's FULL
guards 0<r_a and r_a<=1/2, giving V(r_a)<1. Positivity of V(r_a) comes
from the positive chain(13), not from an unproved positivity conclusion
of that finite theorem. This handles q<3 when alpha>1: we used monotonicity
of J up to4, and compared Delta at4 and3. We NEVER asserted q>=3 or
Delta(q,a)<=Delta(3,a) at such a q.

Since t->t^(-1/k) decreases for t>0 and k>0, (13) gives precisely(3),
including V(r_a)^(-1/k)>1 because0<V(r_a)<1. The literal V(0)=1,
so no certificate gain uniformly separated from1 as a tends to0 is claimed.
This does not assert a limit of the exact Omega or the energies. This proves D2.

## 5. Actual original point consequence in the SAME own energy

Return to the original physical hypotheses in Section1. Input(4) has
D=q-2a, M_a and Omega from(1),(3), and the SAME explicitly defined positive
finite E_star^O and F_a(E_star^O)>0. Combining it with(3) yields

 Q2>=2^m V(a/2)^(-1/k)F_a(E_star^O)>2^m F_a(E_star^O).        (14)

This is an ORIGINAL canonical Stratonovich point-moment bound in every
admissible dimension/covariance, including alpha>1 where admissible.
All noise amplitudes stay in the SAME energy; none was normalized away.
It is not an extension of the old d1 stochastic proof. The new all-Gamma
full-H1 occupation theorem is the accepted stochastic/energy input.
No actual firstmean or author label is identified by this inequality.

## 6. Verification boundary and remaining full goal

The TWO new finite scalar facts preserve the independently gated headers.
They have local clean compile, separate full pp.all types/standard-axiom
audits,5matching artifacts in fresh owned replay and4semantic False controls.
The first compiled attempt failed the WARNING gate on a redundant tactic;
its22native files are preserved. The clean successor has41native files,
changes proof body only and disables no linter. The FULL gate checked statement fidelity and actual applications;
there are now73accepted finitefacts in19local seams, still L0 PROPOSED.
The frozen pre-compilation input-bindings/fence and original local receipt
retain their historical pending language; the current application summary
and Lean ledger record their later acceptance.
No formal integral/probability/derivative/SPDE theorem is claimed.

The unchanged old V kernel is not recompiled or re-proved; actual formula,
complete public types and r_a guards are audited as reuse. Normalized
mass, IBP, dominated differentiation, Cauchy-Schwarz expectations, real
powers, Gamma bound and point consumer are explicit ANALYTIC inputs/steps.
No official package/companion/lease/registry/HPC gate is opened.

Old diagnostic field log_F_q_derivative means dlogJ_a/dq, while
E_u_lambda_squared equals D*m2, not m2. Only5of20 derivative cases have
q in the model interval(2+a,4);15are scalar cases outside it. Nine further
alpha>1 cases satisfy the parameter threshold for d2/3; they are not d1
model cases. Working45digits is not an error certificate. No numerical
V(a/2),J_a(4),M_aJ<=V comparison, occupation energy or actual SPDE moment
was evaluated. Exact finite fixtures have a reproducible separate generator.
None of these numerical controls substitutes for Sections2-5.

As recorded in Progress.md, the original correct-scale upper is retained;
this is a status citation and not a premise of(14). Kappa's static exponent
limit is unchanged. Separate valid Jensen bounds may be combined with(14)
by a maximum; (14) itself does not identify a firstmean rate or source L_*.
The strict gain is in our own full-H1 finite-energy half-gradient domain.
Intended source-domain/normalization correspondence, matching sharp upper
constant and conditional exact limit remain OPEN. No source repair/contact/
Skorohod/HPC/TeX/PDF/wiki/privatecompanion/publication or whole-paper/
novelty/human/circulation clearance. Full original goal stays ACTIVE.
