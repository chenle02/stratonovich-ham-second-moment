# Ground state and uniform gap for the actual profile family

ACCEPTED at the scoped analytic/source gate: actual Opus5.5/HIGH,
11PASS,126.626seconds, no required repairs, scientific source45e1b13.
Evidence and seven optional clarifications are in
reviews/2026-10-30-spectral-phase/ground-adjudication-v1.md.
This is standard spectral groundwork, not novelty or an F-wave bound.
Full original upper/sharp goal remains active.

## Inputs and scope

Use the exact target family in
reviews/2026-10-30-spectral-phase/target-v2.md: real d1, original nonzero
Riesz/white Gamma, nonzero nonnegative smooth compact q, U=Gamma*q,
b in fixed K=[b0,b1] with0<b0<=b1<infinity, and H_b=-d^2/dx^2-bU.
The accepted Gaussian-tilt note Section3 gives U smooth, bounded, nonnegative,
nonzero and tending to0 at infinity. In the white case U=c_Gamma q;
in the Riesz case its tail is retained. Write M=||U||_infinity>0.

Imported, not proved here, from Teschl2014 SECOND edition:
- Theorem10.2,p258: for the bounded vanishing potential -bU,
  H_b is self-adjoint on H2, bounded below, essential spectrum[0,infinity),
  and compact smooth functions form a core. This exact source/definition
  map was statement-reviewed; original images/custody are retained.
- Theorem10.13,p273: if the bottom of such an operator is an eigenvalue,
  it is simple and has a strictly positive eigenfunction.
- Theorem4.12,p141: max-min characterization of eigenvalues counted with
  multiplicity below essential spectrum, setting later variational levels
  to the essential threshold once discrete eigenvalues run out. Its formula
  also holds on the quadratic form domain, as stated immediately afterward.

The following deductions do not assume existence, a uniform gap, a
complement estimate or a desired moment lower rate.

## 1. A single trial gives a uniform negative bottom

Choose D>0 with m=integral_[-D,D] U(x)dx>0; boundedness makes it finite,
and nonzero continuity/nonnegativity makes such a D exist. Choose a nonzero
smooth compact chi,0<=chi<=1,chi=1 on[-1,1], and set
A=integral |chi'|^2, B=integral chi^2>0.
Take one fixed L>=max(1,D,2A/(b0 m)). For w_L(x)=chi(x/L), a change of
variables gives ||w_L||_2^2=LB and ||w_L'||_2^2=A/L. Since w_L=1 on[-D,D],

    <w_L,H_b w_L> <= A/L-b0 m <= -b0 m/2.

The Rayleigh quotient therefore implies, uniformly over b in K,

    E1(b)=inf spectrum(H_b) <= -epsilon,
    epsilon=b0 m/(2LB)>0.                                  (1)

Also H_b>=-b1 M, since the kinetic form is nonnegative and U<=M.
Thus -b1M<=E1(b)<=-epsilon. The bottom belongs to the spectrum of this
self-adjoint lower-bounded operator (equivalently use its spectral measure).
It is below essential threshold0. By the definition of essential spectrum
used in the source, it is an isolated eigenvalue of finite multiplicity.
Theorem10.13 now applies and supplies simplicity and an L2-normalized positive
real eigenfunction p_b. No theorem conditional on an eigenvalue has been
used to prove that eigenvalue exists.

Set lambda_b=sqrt(-E1(b)); then

    sqrt(epsilon)<=lambda_b<=sqrt(b1 M).                    (2)

Strict positivity can be read a.e. from the imported theorem. It is also
pointwise for the continuous representative: p_b in H2 has a C1 representative
in d1, and p_b''=(lambda_b^2-bU)p_b is continuous, so p_b is C2. If a
nonnegative p_b vanished at a point, its derivative there would be0;
uniqueness for this continuous-coefficient linear ODE would force it to
vanish identically, contradicting normalization.

## 2. Two variational levels and uniform energy separation

Define E2(b) by the source's second max-min level, using the common domain
H2 (or common form domain H1) and normalized vectors. If a second negative
eigenvalue exists it is that eigenvalue; otherwise E2(b)=0. This convention
covers infinitely many Riesz bound states as well as a single bound state.
Because E1(b) is simple and isolated,

    E1(b)<E2(b)<=0.                                        (3)

For any unit form vector z,

    |<z,H_b z>-<z,H_c z>| <= M |b-c|.

The same comparison survives an infimum over unit vectors in the orthogonal
complement of any fixed finite list, and then a supremum over those lists.
Theorem4.12 therefore gives, for j=1,2,

    |Ej(b)-Ej(c)|<=M|b-c|.                                 (4)

This uses the SAME test classes at b,c, not continuity of already-selected
eigenvectors. In particular E2 is continuous through the threshold where
a second eigenvalue appears or disappears. It is not incorrectly defined
only when a second bound state exists.

The positive continuous function E2-E1 on compact K has a positive minimum
Delta>0. Thus the energy separation is uniform, derived from (3)-(4) and
compactness rather than assumed as a spectral premise.

## 3. Growing rates are uniformly separated

Let mu_b=sqrt(-E2(b))>=0; E2<=0 includes the threshold case mu_b=0.
Both rates are continuous,0<=mu_b<lambda_b, and

    lambda_b-mu_b
       =(E2(b)-E1(b))/(lambda_b+mu_b)
       >=Delta/(2sqrt(b1 M))>0.                            (5)

The denominator is positive by (2), and each rate is at most sqrt(b1 M).
Choose eta0 as half the minimum of sqrt(epsilon) and
Delta/(2sqrt(b1 M)). Then0<eta0<inf_b lambda_b and
mu_b<=lambda_b-2eta0. This is separation of the frozen L2 spectral rates,
NOT yet an operator norm estimate on E or F.

## 4. Falsification, formal boundary and remaining work

A white-family trial diagnostic can use any smooth unit-mass q supported
inside[-1,1], covariance amplitude1 and the H1 trapezoid chi equal1 on[-1,1]
and linear to0 at±2. It has A=2,B=8/3. At b0=1/4,L=16 the exact trial
energy is2/16-1/4=-1/8, and its Rayleigh quotient is-3/1024. This diagnostic
has the correct attractive sign and does not use integrability of a Riesz
tail. The written proof above uses smooth chi; the H1 diagnostic is allowed
by the source's form-domain formulation. It is not a growth-rate computation.

Lean triage: the new content is analytic variational/spectral reasoning,
not an unverified finite combinatorial calculation. Existing real-number
positivity/algebra can check margins, but cannot certify max-min, spectrum,
compactness or eigenfunction conclusions without substantial new foundations.
No such library/package expansion is undertaken here; finite margins will
be paired with the eventual actual wave consumer if they become load-bearing.
This note is NOT a Lean spectral theorem or official package/companion gate.

Still open: uniform weighted eigenfunction/derivative/duality bounds on F,
continuity/normalization of the actual wave projections, global fractional
Sobolev wave calculus and the genuine F-complement estimate. Individual
Simon decay does not automatically make its constants uniform. Product/
cone/initial-transient/terminal-observable and event/variational/sharp
constants, original higher dimensions and source normalization remain open.
