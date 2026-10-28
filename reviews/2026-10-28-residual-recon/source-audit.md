# Residual d2 Riesz source audit

[held back: collaborators' unpublished work]

## Exact target and inherited boundary

For the Stratonovich HAM with initial data (1,0), covariance
|s-r|^(-alpha0) c|x-y|^(-alpha), c>0, d=2,
0<alpha0<1/2 and 3/2<=alpha<2-alpha0, obtain a finite C such that
E u(t,x)^2 <= exp(C t^kappa), kappa=(4-alpha-alpha0)/(3-alpha)
(at least for sufficiently large t). Constants may depend on fixed parameters.
This does not ask for a sharp constant. No Skorohod theorem is developed.

Read authority: Progress.md; notes Section6; the Round3 source crosswalk and
Round4 literature gate. The one-wave spatial supremum is infinite in this range
by the recorded P:higher-obstructions. This is a failure of that route, not of
moment growth. The G0 common-Laplace-parameter majorant is already ruled out;
its unchanged reuse is not a new route.

## Candidate 1: retain Chen's integrated pair norms before uniformization

**Source:** pinned X. Chen author version, pp14–15, definitions (3.3)–(3.5)
and Theorem3.1 (3.6); Appendix LemmaA.1, pp60–62, (A.1)–(A.2).
The theorem accepts two separately ordered chains, all pair partitions, and
arbitrary nonnegative vertex kernels G_l. Edge spectral measures are finite,
nonnegative covariance functions; temporal edge kernels are Laplace mixtures
restricted to measurable sets A_(j,k). General homogeneous kernels require the
source's regularization/limit passage.

For H_theta(s,x)=exp(-theta s)G_s(x), its squared type-2 norm contains the
joint integral

  integral_(s,t>0) exp(-theta(s+t)) |s-t|^(-alpha0)
    integral G_s(dx) G_t(dy) gamma(x-y) ds dt.

LemmaA.1 proves finiteness under source (1.5), which covers the present
alpha+alpha0<2 regime. Its resolvent representation integrates both wave
increments and their relative time before any fixed-translation supremum.
Consequently the divergent pointwise spatial maximum does not prohibit this
source input. Formula constants must follow definitions (3.2)–(3.5), including
the Gamma(alpha0) normalization; this audit does not certify every printed
prefactor of the appendix.

**Exact missing transfer:** an order-aware/grouped use of (3.6) must retain
sufficient temporal structure to recover the factorial denominator
(k!)^(3-alpha), rather than the G0 denominator (k!)^(3-alpha-alpha0).
Theorem3.1 supplies a product of norms with a pairing-dependent partition
Q0,Q1,Q2; it does not state that the resulting bound is a symmetric time
integrand to which the successful Wick-sum simplex argument can be applied.
The required map cannot simply use the same theta at every vertex and sum
all pairings: that is exactly the recorded no-go. No such improved map is
proved or claimed here.

**Smallest falsification test:** keep distinct vertex Laplace weights at total
order four and test all three pairings for splits (0,4),(1,3),(2,2), including
empty-chain and exchange cases. Check that the proposed order-aware estimate
actually differs from the common-theta G0 envelope and that any claimed
symmetry survives the pairing-dependent Q partition. Reject before all-order
work if symmetrization has already been lost. Scaling/factorial accounting is
a necessary test, not a proof of the target bound.

## Candidate 2: deterministic two-wave time smoothing before contraction loss

**Exact primary input:** Bolaños Guerrero–Nualart–Zheng,
*Averaging 2d stochastic wave equation*, arXiv:2003.10346v2,
Lemma4.3 (4.7), p20; proof pp29–31. With the usual two-dimensional wave kernel
G_h(x)=1_(|x|<h)/(2 pi sqrt(h^2-|x|^2)), for q in (1/2,1),
delta in [1,1/q], s<t,

  integral_s^t [(G_(t-r)^(2q) * G_(r-s)^(2q))(z)]^delta dr
    <= C_q (t-s)^(1-delta(2q-1))
         G_(t-s)(z)^(delta(2q-1)).

This is an integrated-time deterministic estimate, not a fixed-r bound and
not a stochastic moment theorem. Source:
[arXiv v2](https://arxiv.org/abs/2003.10346v2).

**Stratonovich consumer already in print:** Balan (2022), AppendixC,
LemmaC.1, p2687, is the delta=1/q case. The proof of LemmaC.2, p2688,
retains the intermediate bound

  integral_r^t (G_(t-s) * G_(s-r))(x-z) ds
    <= C_(t,q)^2 (t-r)^(2(1-q)) A_q^q
         G_(t-r)(x-z)^(2q-1),
  C_(t,q)=(2 pi t)^(2q-1).

It then weakens the fractional kernel power back to G_(t-r), yielding its
stated Ct^2 G_(t-r) bound. The weaker conclusion alone leaves the present
wave-front singularity problem unchanged. The intermediate displayed proof
contains t/s/r subscript and differential typographical slips in the published
PDF; its endpoint and intended convolution are clear from LemmaC.1, but this
report does not silently certify the typo-containing chain as literal algebra.
A future use should state the clean deduction from C.1 with its correct clocks.

Balan's Theorem3.2 proof, Step3(a), p2659, uses C.2 to remove indices J that
carry no internal trace factor in an L1 estimate. Section6.1, pp2679–2680,
groups Stratonovich orders n into fixed Wiener-chaos projections K_m with
n-m even. These are published mechanisms, not new methodology. However, the
subsequent norm estimates use condition (C),
K_mu=integral (1+|xi|^2)^(-1/2) mu(dxi)<infinity (p2645), which fails for
Riesz alpha>=1. The source noise is also time-independent. Thus its complete
trace estimate does not cover the residual target.

**Exact missing transfer:** preserve the sharper fractional-power convolution
while integrating vertices in the *actual* fractional-time pairing integral.
Every full pairing vertex carries a covariance edge. A supposedly removable
vertex can have both spatial and temporal factors involving a remote vertex;
C.1 has no such weights. Nor is Balan's trace L1 removal automatically valid
inside the later squared norm, where remaining chaos vertices acquire cross
edges. Establishing a suitable weighted bound and a contraction/grouping
algorithm with correct time/factorial powers is new work. The lemma does not
justify replacing the two chains by a semigroup or discarding these factors.

**Smallest falsification test:** use total order four with one ordered chain
and crossing pairs (1,3),(2,4), and the split (1,3) with pairs (1,3),(2,4).
Attempt the proposed two-step merge symbolically while keeping the exact
covariance factor at its intermediate vertex. If a remote-dependent factor
has been pulled outside the integral without a bound, the proposed application
fails already in that example. Independently test the retained fractional-power
kernel at a shift on the wave front and under unequal gap lengths, with t
rescaled rather than treating C_(t,q) as time-independent. These tests are
proposed, not executed numerical evidence.

## Other checked source and exclusions

Chen–Hu (2025), Theorem3.3 (3.10), pp2157–2158, gives an almost-sure
Laplace/Brownian-potential representation of each Stratonovich order under
Dalang's condition for time-independent noise. It is a genuine integrated
representation and a static calibration. It does not supply the missing
fractional-time two-chain clock map. It is not added as a third ready estimate.

No source inspected here directly implies the stated residual theorem.
This is bounded implication evidence, not a claim that none exists. The most
concrete next experiment is Candidate2's weighted order-four merge test;
Candidate1 should advance only with a specific order-preserving ingredient
that escapes the already established common-theta no-go.

## Coverage and limitations

- Current author Chen: extracted pp14–15 and60–62 read, including definitions,
  theorem/base cases and appendix identities; not a new complete proof audit.
- Balan publisher PDF: condition(C), selected Theorem3.2 proof consumer,
  contraction grouping and AppendixC read; pp2687–2688 rendered and inspected.
  Matching local TeX was used for readable formulas; publisher PDF governs.
- BNZ v2: definition of G, Lemma4.3 statement and proof pp29–31 read in extracted
  text; original Lemma1.6 proof was not independently audited in full.
  Bibliographic landing page confirms the cited v2 and EJP26(102),2021;
  no publisher-version statement comparison was made.
- Chen–Hu publisher PDF: Theorem3.3 statement and surrounding proof on
  pp2157–2158 read; not the full Brownian moment/LDP proof.
- The previous local wiki/refdb crosswalk is reused, not represented as a fresh
  exhaustive search. No fresh MathSciNet/zbMATH or complete citation-chain audit.
  Novelty stays UNVERIFIED. A full literature gate remains required before
  claiming a new theorem or investing in a large proof wave.
- All formulas above are source inputs or explicitly marked missing transfers;
  no new accepted mathematics, numerical result, Lean certificate or reviewer
  verdict is asserted. Existing source bytes are unchanged.
