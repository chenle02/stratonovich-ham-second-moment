# Research program: Gaussian wave growth and intermittency

Discussion record: 2026-11-01. This is an internal research assessment,
not a manuscript, a proof-adoption record, or a claim of publication readiness.
[Progress.md](../Progress.md) remains the workflow authority and
[PROJECT-GOAL.md](../PROJECT-GOAL.md) remains the completion contract.

## Le's directions and the unchanged objective

Le asked us to derive the constants produced by the model, rather than force
agreement with Chen's guessed constants. He then asked whether the long notes
could become a gradual series of papers, encouraged a higher-level assessment
of a possible new theory, and asked what we actually contribute relative to
the cited literature. He requested that these discussions be documented here.

The original Stratonovich second-moment objective remains intact: all original
admissible dimensions, covariances and amplitudes, data (1,0), fixed spatial
point, the correct growth scale, and a fully specified actual constant. A new
research program does not turn an unfinished part of that objective into a
completed result. No Skorohod development or sibling-repository edits are included.

## Why the notes became long

The current scientific PDF has 257 pages. It accumulated discovery history,
conditional and alternative routes, finite-order diagnostics, separately
expanded technical foundations, repeated setup, and internal status prose.
The author should have separated the research archive from the focused
manuscript earlier. Page count is not evidence of correctness or completion.

The dependency audit reaches 143 of 213 proof blocks from the main model/upper/
intrinsic theorem roots, and 158 when the derived bounds and Jensen are included.
The 55 not explicitly reached are candidates for manual disposition, not proved
redundant: unlabelled setup and implicit dependencies must still be checked.
See the [reading guide and dependency audit](../reviews/2026-11-01-manuscript-dependency-audit/main-reading-guide-v1.md).
No proof has been deleted or manuscript split performed on this basis.

## The proposed organizing idea

A possible common principle is:

> Rare Gaussian environments produce spectral wave growth; annealed moment
> growth balances that gain against the original Gaussian variance-half cost.

The wave-specific difficulties are substantial: displacement and velocity must
both be propagated; the actual regularized and canonical solutions must agree;
long products need quantitative control; and constants must remain usable as
the spatial localization grows. Growth of an operator norm is not automatically
growth of the displacement observed from the prescribed initial data.

Our physical-time route uses the original Gaussian noise, operator-valued
interaction paths and Young phase evolutions. We have not constructed a
complex-time stochastic integral. Chen's held author-version representation and
Remark6.3 supply an important comparison, but the precise construction mentioned
in his talk has not been identified from a transcript. This methodological
difference alone proves neither novelty nor that complex time is unnecessary
for every related problem.

## A gradual paper structure

| Candidate | Central question | Present material and additional requirement |
|---|---|---|
| I. Gaussian-driven wave evolutions and uniform spectral growth | Can the physical-time construction and long-time growth estimates be expressed as reusable theorems? | Current weak-phase construction, source convergence, spectral estimates, Gaussian tubes and uniform products are ingredients. The theorem must be independent of the final C2 result and useful in another meaningful class. |
| II. Exact second-moment asymptotics for the time-dependent Stratonovich hyperbolic Anderson model | What is the actual original-model logarithmic limit and its complete variational constant? | Current full upper, actual raw lower, signed-positive optimized comparison, cutoff removal and derived bounds belong here. Consolidated verification remains open. |
| III. Universality and higher moments | Which noise features govern growth beyond the current homogeneous p2 model? | Contingent on genuinely new theorems. Higher moments, mixtures and changed temporal memory are research targets, not extracted existing papers. |

The recommendation is two coherent paper candidates, with a third conditional
on new results. If candidateI is only a repackaging of standard theory or has no
useful second application, its methods should remain inside candidateII.
A separate nonsharp p2 paper followed by an exact p2 paper needs an independent
scientific reason; it should not be chosen just to increase the paper count.
Historical failed routes belong in a research archive. Technical appendices
must preserve necessary arguments and their exact interfaces.

## What we currently contribute, and what we borrow

1. **Correct-scale full p2 upper bound.** The current result bounds the logarithm
   of the original second moment at scale T^kappa, with
   kappa=(4-alpha-alpha0)/(3-alpha), throughout the original model class.
   The comparison is with the crude exp(C T²) p2 bound in the held Chen author
   version, not an obsolete arXiv statement.
2. **Intrinsic p2 variational characterization.** This is the strongest current
   candidate contribution: matching upper/lower values over nonnegative smooth
   spacetime controls, including nonseparable controls, with the actual covariance
   amplitude, wave kinetic coefficient1 and Gaussian cost v/2. The auxiliary
   label-one score is not identified with the signed first moment or Chen's
   printed endpoints. Component reviews do not complete whole-paper validation.
3. **Potential reusable method.** The candidate increment is the original-noise
   weak-phase construction together with uniform growing-domain product control
   and optimized signed-to-positive comparison. Its independent novelty is open.

Young integration, Gaussian large deviations, general rough-flow integrability,
and the imported spatial-energy finiteness theorem are known foundations.
The white spatial energy c²/6 is a calibration/prior result, not a new evaluation
of the wave constant or sufficient material for another paper. The current white
wave endpoints are bounds, not an exact numerical C2.

## Literature and actual holdings

| Source | Current full text | What the current comparison actually read |
|---|---|---|
| Chen-Deya-Song-Tindel, IMRN2023, DOI10.1093/imrn/rnad039 | Published 54-page PDF now held; correct older 34-page preprint also held | Selected theorem/introduction passages, especially Theorem 1.1 and 1.7-1.8; no complete proof comparison |
| Gubinelli-Tindel, AnnProb2010, DOI10.1214/08-AOP437 | 75-page PDF, refdb and Papis present | Selected analytic-semigroup setup/introduction |
| Friz-Victoir, AIHP2007, DOI10.1016/j.anihpb.2006.11.002 | 11-page published PDF acquired on <HUB> and copied to local external audit storage | Selected Gaussian LDP statements |
| Cass-Litterer-Lyons, AnnProb2013, DOI10.1214/12-AOP821 | 25-page PDF, refdb and Papis present | Abstract/metadata for this program assessment |

CDST already develops a Young-type Stratonovich wave theory in weighted Besov
spaces. Gubinelli-Tindel treats rough evolution equations with analytic semigroups.
Friz-Victoir gives Gaussian rough-path large deviations. Cass-Litterer-Lyons gives
Gaussian rough-flow integrability. Our different phase space or use of a wave
group does not by itself establish that these results fail to imply a proposed
claim; exact hypotheses, topology and uniformity must be compared.

The canonical PDF named chen_deya_ea-23-hyperbolic.pdf was checked on both machines
and actually contains Chen's different EJP2023 spatial-energy paper. The retained
project CDST TeX has the correct title/subject. A correct published CDST PDF was
obtained separately, and identity/edition repair was requested through the
canonical single-writer queue. Do not infer source identity from catalogue 5/5.

Exact receipts/editions/hashes are in the
[holdings and contributions record](2026-11-01-holdings-and-contributions-v1.json).
Reference intake tk-20261101-185423-codex-stratonovich-program now has an exact
GOLD receipt with digest PASS and clean lint; identity repair
tk-20261101-190012-codex-stratonovich-reference-identity remained CLAIMED at the
last observation. Completed ingestion is not a full mathematical proof audit.
No direct corpus edits were made.

The novelty gate is OPEN. Wiki search/cite and selected primary comparisons were
performed; MathSciNet returned only a JavaScript frontend. Full source reading,
implication maps and citation chains remain incomplete. We have not established
that a separate general-theory paper is publishable.

## The first precise theory candidate

The [current frozen upper-growth statement](uniform-gaussian-growth-statement-v2.json)
extracts a possible supporting proposition from the existing Gaussian tube and
signed bulk/tail arguments. It is a statement candidate awaiting independent audit.
Its six hypotheses specify:

- the actual raw isonormal noise and correctly scaled Cameron maps;
- small Gaussian path radii in separable spaces which may vary with delta/B;
- the same stochastic quantity for every block length B;
- finite, uniformly coercive moving control scores;
- a subquadratic radial growth envelope;
- a sharp deterministic comparison on a polynomial control ball large enough
  for the Gaussian tail cutoff, with delta first and B afterward.

Its proposed conclusion is only an upper bound by the moving control-score
limsup. It does not identify an exact limit, prove terminal displacement growth,
or establish mixture asymptotics. The Gaussian transfer may be a standard
supporting argument; novelty cannot be inferred from abstract notation.

The [falsification record](2026-11-01-theory-statement-falsification-v1.json)
retains local Sympy checks and their scope. The main boundaries are:

- The scalar wave u_second=u has operator growth exp(t), but initial phase
  (1,-1) gives displacement exp(-t). This refutes an arbitrary-phase lower
  theorem, not our original data(1,0) claim.
- Error M^(3/2)/B tends to zero for every fixed M but grows as B14 on a
  control ball of radius B10, even though that radius handles the stated
  coarse Gaussian tail. Fixed-ball convergence is insufficient.
- A sum of two homogeneous Riesz covariances does not inherit exact scaling
  at the larger order. At the explicit test, the discrepancy is
  (sqrt(2)-1)/2>0.
- On l2, rates J_n(h)=(1-2||h-e_n||)+ converge pointwise to zero, while their
  penalized suprema stay at least1/2. Bounded optimizing norms alone do not
  permit exchanging a supremum and a limit.

The last example is an analytical witness in the frozen statement; it is not a
Lean certificate. No new Lean declaration/package/run has been made for this
assessment. Existing finite-tail facts remain under their original scopes;
Gaussian geometry and uniform analytic limits are not replaced by assumptions
which restate the desired conclusion.

## New directions worth testing

The first broader construction test is a finite positive sum of admissible
homogeneous spatial covariances of different orders, at fixed mask and horizon.
Both wave-variance estimates and original-noise correspondence must survive.
No arbitrary independent decomposition of a given noise is assumed.

A later asymptotic question is whether the roughest component determines the
leading growth of that mixture. Exact self-similarity is lost, so this needs
new bounds. It is not a consequence of the homogeneous formula.

The first higher-moment target is the actual fourth moment. Score homogeneity
suggests a candidate scaling law, but proving it needs actual source/p-chain,
point-transfer and terminal-observable estimates. It does not solve the signed
first-moment problem.

A further direction separates short-time covariance singularity from long-time
memory, for example by comparing power-law with tempered power-law kernels.
No unchanged exponent or exact crossover law is asserted. Variational attainment
and sufficiency of separable controls also require a precise completed control
class and new arguments; neither follows from our present bounds.

## Review state and next decision

Le selected DeepSeek V4 Pro + Kimi-K3 as reviewers. Their exact routes and gates
are recorded in [AGENTS.md](../AGENTS.md). The recent DeepSeek report concerns
only the auxiliary spatial-ratio draft: PASS_WITH_NOTES/MEDIUM, below the HIGH
minimum, with source/normalization qualifications. Kimi hit monthly quota before
reading or returning a report. See the
[retained report](../reviews/2026-11-01-reviewer-switch/deepseek-report-v1.md) and
[adjudication](../reviews/2026-11-01-reviewer-switch/deepseek-adjudication-v1.md).
The abstract-growth v1 statement subsequently received a separate DeepSeek
PASS_WITH_NOTES/MEDIUM report, below HIGH. Its full report and
[adjudication](../reviews/2026-11-01-growth-statement/adjudication-v1.md) are retained.
v2 clarifies the radius indexing and the exact ordered zero-law reduction,
without adding the stronger fixed-block zero limit suggested by the reviewer.
Indeed, an all-zero Gaussian family with Z_delta=1 and F_delta,B(0)=1/B
satisfies the original hypotheses with e_B=1/B tending to zero. Requiring
the inner delta limit to vanish at every fixed B would exclude it needlessly.
v2 also spells out the propagator determinant and the B14 calculation.
No version has been adopted or received a passing HIGH gate.

The next decision is whether its assumptions are sufficient, noncircular and
independently verifiable in the original wave model, and what remains beyond
existing literature. Independent statement audit precedes proof adoption.
A useful second application and an exact source crosswalk determine whether
candidateI deserves its own paper. The original all-model p2 result and every
whole-proof/source/visual/final-cold gate remain required throughout.

## Detailed records

- [Paper bundles, proposed theorems and prior-art crosswalk](2026-11-01-series-assessment-v1.json)
- [Verified holdings, edition defect and contribution map](2026-11-01-holdings-and-contributions-v1.json)
- [Initial frozen upper-growth statement](uniform-gaussian-growth-statement-v1.json)
- [Clarified upper-growth statement and boundary examples](uniform-gaussian-growth-statement-v2.json)
- [Executed local symbolic falsification checks](2026-11-01-theory-statement-falsification-v1.json)
