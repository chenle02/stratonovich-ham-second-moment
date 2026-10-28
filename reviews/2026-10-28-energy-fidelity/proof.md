# Physical and spectral quartic energy: Sobolev identification

Status: new local proof, independent review pending. This is a statement-fidelity
lemma for the general static endpoint, not a proof of the full moment theorem
or arbitrary-covariance factorization. No earlier medium report is promoted.

## Falsification and normalization first

For d3 take g(x)=pi^(-3/4)exp(-|x|²/2). It has unit L2 norm,
g²=pi^(-3/2)exp(-|x|²), its unnormalized Fourier transform is
exp(-|xi|²/4), and its autocorrelation is p_1(z). Thus BOTH proposed energies
must equal (p_1*Xi)(0), with no extra2pi factor.

For Xi=c dy delta0(dz), the physical value is c/sqrt(2pi). Its spectral
measure is c delta0(dxi1)delta0(dxi2)dxi3/(2pi), giving the same value.
For Xi=c/|x| in R3, the value is c sqrt(2/pi), and the spectral density
c |xi|^(-2)/(2pi²) gives exactly that value. For constant covariance c dx,
the spectral measure c delta0 gives energy c. These tests cover singular
physical measures, noncompact covariance and an atomic spectral measure.
They are normalization checks, not a continuous proof or Lean certificate.

## Statement and sole analytic input

Let Xi be a nonnegative even positive-definite tempered Radon covariance in
R^d, with source convention Xi=int exp(i xi.x)mu(dxi). mu is a positive even
tempered spectral measure. Write hat h(xi)=int exp(-i xi.x)h(x)dx.

On real Schwartz functions, define

 E(h)=int |hat h|² dmu,       Q(f)=E(f²).

Assume the following bound for real Schwartz f, with a fixed C0>=0:

 (F) Q(f) <= (1/2)||f||_2²||grad f||_2² + C0||f||_2^4.

In the actual endpoint application, (F) follows from the FINITENESS assertion
in Chen2023 Theorem1.1(1.5), pinned PDF p2, restricted first to unit-L2 real
Schwartz functions and then normalized. This import does not require any
unproved identification on nonsmooth Sobolev profiles. The exact source PDF
has DOI10.1214/23-EJP985 and SHA256
9ed4b0ae633cc79eb1b985ecf00b2ae67db83061fd0d8a73628704b5b664a5da.
Its Dalang hypothesis is verified for the static endpoint by beta<2.

Then for every real g in H1(R^d), both expressions below are finite and equal:

 Q_phys(g)=int Xi(dz)int g(y+z)²g(y)²dy
         =int |hat(g²)(xi)|²mu(dxi)=Q_spec(g).

The physical expression is independent of the Borel representative of g.
Bound(F) also holds for g, with Q_phys=Q_spec. Consequently the physical
positive-measure variational functional in the notes matches the actual
spectral/generalized-function functional, including singular endpoint measures.

## Proof on Schwartz functions

For real Schwartz f,h, Fourier pairing gives

 P(f,h):=int Xi(dz)int f(y+z)²h(y)²dy
       =int hat(f²) conjugate(hat(h²)) dmu.

Evenness ensures the sign/conjugation convention is immaterial to this real
quantity. All pairings are absolutely convergent Schwartz pairings. Since
both Xi and mu are nonnegative, there are TWO different Cauchy bounds:

 (1) 0<=P(f,h)<=sqrt(Q(f)Q(h)),             by spectral Cauchy;
 (2) E(fh)<=sqrt(Q(f)Q(h)),                 by physical Cauchy.

For(2), the physical expression for E(fh) is the integral of
[f(y+z)f(y)] [h(y+z)h(y)] on dy Xi(dz). Its square factors have norms
Q(f) and Q(h). In particular E(fh) here is NOT the quartic expression Q(fh).

Set N(f)²=||f||_2²+||grad f||_2². From(F) there is finite D such that

 sqrt(Q(f)) <= D N(f)².

Let M be the positive sigma-finite measure dy Xi(dz), and define

 A_f(y,z)=f(y+z)f(y),        B_f(xi)=hat(f²)(xi).

For real Schwartz f,h, decompose

 A_f-A_h=(f-h)(y+z)f(y)+h(y+z)(f-h)(y).

Bound(1) gives

 ||A_f-A_h||_L2(M) <= D [N(f)+N(h)]N(f-h).

Also B_f-B_h=hat((f-h)(f+h)). Bound(2) gives

 ||B_f-B_h||_L2(mu) <= D N(f-h)N(f+h)
                    <= D [N(f)+N(h)]N(f-h).

These estimates distinguish the physical tensor product from the spectral
transform of the square; neither is silently assumed continuous on H1.

## Density and identification of the limits

Choose real Schwartz f_n->g in H1. The two estimates make A_(f_n) and
B_(f_n) Cauchy in their respective L2 spaces. After a subsequence,
f_n->g Lebesgue-almost everywhere. Translation invariance of Lebesgue
measure and positive sigma-finite Fubini imply

 f_n(y+z)f_n(y)->g(y+z)g(y), M-almost everywhere.

Thus the strong L2(M) limit is A_g. The same Fubini reasoning shows that
changing the Lebesgue representative of g does not change A_g in L2(M).

Further,

 ||f_n²-g²||_1 <= ||f_n-g||_2 (||f_n||_2+||g||_2)->0.

Hence hat(f_n²)->hat(g²) uniformly on all frequencies. A subsequence of
the strong L2(mu) limit converges mu-almost everywhere; it must equal that
uniform Fourier limit. Thus the strong limit is B_g=hat(g²).

For each n, ||A_(f_n)||²=Q(f_n)=||B_(f_n)||². Passing to the two strong
limits proves Q_phys(g)=Q_spec(g)<infinity. Passing(F) to the limit proves
the stated bound on H1. This proves the lemma, conditional only on the
explicit Schwartz bound(F), whose source application was specified above.

## Application and scope

Apply this to Xi=Gamma_st in the notes. The source's variational finite
supremum in(1.5) supplies(F) on Schwartz before the extension. The identities
then justify using the ordinary positive-measure energy for every real H1
profile in M_st. For unit-L2 profiles, Q<=B/2+C0 with B=||grad g||², so
sqrt(Q)-B is uniformly bounded above. This independently supplies finiteness
of that functional without guessing a sharp value. Its equality with the
source spectral functional is profile-by-profile, not only an inequality
between two suprema. No target moment or source-normalization correction is
asserted by this lemma.
