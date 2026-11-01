# Draft independent spatial-ratio finiteness deduction

STATUS: AUTHOR DRAFT v2, NOT independently reviewed or adopted.
The v1 draft is retained. v2 explicitly distinguishes E_full from its
compact-test energy E; the finiteness target and all original cases stay. This does not
replace any frozen proof or satisfy the full wave/constant goal. The old
full upper remains retained. No new Skorohod result or feature/raw bridge.

## Exact imported input and original-model hypotheses

From Xia Chen, Exponential asymptotics for Brownian self-intersection local
times under Dalang's condition, EJP28(2023),119, Theorem1.1,(1.5),p2:
under integral (1+|xi|²)^(-1) mu(dxi)<infinity the spatial energy

  E_full = sup{ A(f) - T(f)/2 : real f in H1(Rd), ||f||2=1 }

is finite. Denote that source full-domain value by E_full. To avoid
assuming a generalized-covariance pairing identification on rough H1
profiles, use E below for the SAME physical energy supremum restricted
to real unit compact smooth tests. This subclass gives E<=E_full<infinity.
Only smooth source pairings are used before the independent Fatou
extension. Here T(f)=||gradient f||2² and, on compact smooth f,

  A(f)=integral Gamma(dz) integral f(x)² f(x-z)² dx.

Source p1 explicitly permits generalized covariance functions, and p2
explicitly discusses the Dirac case. Its nonnegative positive-definite
tempered covariance hypothesis includes our nonnegative even positive-
definite tempered Radon measures. No density or convolution-square-root
hypothesis is introduced. Read exact retained primary pages1-3, source
PDF SHA2569ed4b0ae633cc79eb1b985ecf00b2ae67db83061fd0d8a73628704b5b664a5da.
Citekey chen:23:exponential verified in read-only refdb; source theorem is
IMPORTED, not re-proved here. This is an auxiliary spatial-energy input, not an identification of the
source full-domain value with an unverified rough pairing, Chen2026's
printed time-dependent endpoints or our wave C2.
Its kinetic coefficient1/2 does not alter the actual wave kinetic one or
the Gaussian variance-half action in the main limit theorem.

Our original threshold alpha+a<2, a>0, implies0<alpha<2. Spatial homogeneity
gives mu(B_R)=R^alpha mu(B_1). Local finiteness bounds the integral on B_1.
On dyadic shells2^j<=|xi|<2^(j+1), the remaining integral is at most

  mu(B_1) 2^alpha sum(j>=0) 2^(-j(2-alpha)) < infinity.

This uses radial ball mass only, not a spectral density or angular
regularity. Zero covariance gives zero measure and is treated directly.
Thus the published finiteness input applies at every original amplitude
and in every admitted dimension/white case. For compact smooth f the
physical pairing is unambiguous as the action of the covariance on the
compact smooth autocorrelation, so only that subclass of the imported
variational bound is needed for the following deduction.

## Complete author deduction before any finite supremum is assumed

For real unit compact smooth f, let A=A(f)>=0 and T=T(f)>0. The gradient
cannot vanish for a nonzero L2 function on Rd: its L2 Fourier transform
would otherwise be supported on the null set{0} and hence vanish. Set f_b(x)=b^(d/2)f(bx), b>0.
The physical Radon change of variables gives

  ||f_b||2=1,   A(f_b)=b^alpha A,   T(f_b)=b² T.

For A>0, the finite imported E therefore bounds, for EVERY b>0,

  b^alpha A - b² T/2 <= E.

Choose b=(alpha A/T)^(1/(2-alpha)). Direct substitution gives

  E >= ((2-alpha)/2) alpha^(alpha/(2-alpha))
           [ A / T^(alpha/2) ]^(2/(2-alpha)).

All powers and divisions have positive bases/denominators. Consequently

  A / T^(alpha/2)
    <= alpha^(-alpha/2) [2E/(2-alpha)]^((2-alpha)/2) =: C_E < infinity.

If A=0 this same bound is immediate. E>=0 follows by taking b down to0
in the individual energy tests. This does not assume that R0 or R_sp is
a finite real number before obtaining a uniform bound on its test set.

For a real unit f in full H1, approximate in H1 by real normalized compact
smooth f_n. Then T(f_n) tends to T(f) and, after a subsequence, f_n tends
to f Lebesgue-a.e. The positive measure dx Gamma(dz) is sigma-finite.
For every fixed z a translated Lebesgue null set remains null; Tonelli
therefore gives convergence at BOTH positions x and x-z almost everywhere
for this product measure. This is precisely the version-independent
physical pairing argument of existing L:spatial-physical-pair, whose proof
uses no ratio or score finiteness. Fatou yields

  A(f) <= liminf A(f_n) <= C_E T(f)^(alpha/2).

Thus every physical pairing is finite and the entire full-H1 ratio set
is bounded by C_E. Its supremum R_sp is finite without the old full wave
upper, the positive score, a rough stochastic evolution or a supposed
unmasked ground state. No maximizer is asserted. If Gamma=0, A=0 and
R_sp=0 directly; the imported energy supremum is0 by spreading tests.

## Falsification and normalization checks

- Spatial white covariance c*delta0 in d1 has alpha1. Using the already
  derived auxiliary spatial value E=c²/6, approximated by compact tests, C_E=sqrt(2E)=c/sqrt3, matching
  the existing sharp spatial-ratio value. This is a consistency check,
  not a new numerical evaluation of the time-colored wave constant.
- A d3 homogeneous covariance supported on a coordinate plane,
  Gamma(dx)=c*delta0(dx1)dx2dx3, has alpha1 and physical characteristic
  spectral measure c/(2pi) dxi1*delta0(dxi2)*delta0(dxi3). Its Dalang
  integral is c/2. The source thus covers a genuinely singular original
  measure case. For unit product tests f=g(x1)h(x2,x3),
  A(f)=c integral g^4 and T(f)=T(g)+T(h). Spreading h preserves its L2
  norm and makes T(h) vanish; the ratio tends to the finite d1 ratio,
  not a false high-dimensional-white or unmasked-eigenstate assumption.
- Multiplying Gamma by a finite c>0 preserves Dalang finiteness; A and
  the ratio scale linearly in c. Spatial dilation gives auxiliary
  E(cGamma)=c^(2/(2-alpha))E(Gamma): choose b=c^(1/(2-alpha));
  the dilation f to f_b is a bijection on unit compact smooth tests, and
  c A(f_b)-T(f_b)/2=c^(2/(2-alpha))[A(f)-T(f)/2].
  Taking suprema over the bijected compact smooth test class proves the
  displayed identity. No source/full-H1 pairing identification is used. Thus C_E scales linearly too. At c0
  the direct zero identities apply. No unit-covariance normalization.

## What remains before a shorter main argument exists

This establishes an author draft route for R_sp finiteness only. The
finiteness of all S_c and all other T:full-upper consumers must be audited
separately. In particular, canonical source/point moments, uniform source
integrability and growing-cone transfers cannot be discarded by citing a
spatial energy result. Existing mean/occupation inequalities might yield
an independent score bound once their hypotheses and order are arranged;
that has not been adopted here. Current P:spatial-smooth-ratio additionally
states a lower-score comparison, whose proof is not replaced by the present
finite-ratio argument. Every original asserted result must remain justified.

Before any main-source change, check this imported application and author
deduction independently, inspect every remaining old-upper consumer, and
write the complete replacement. Retain/validate the reviewed full-upper
result as required. The main TeX, PDF,213proof bodies,221statements and
frozen common-v2 review obligations remain UNCHANGED by this draft.
