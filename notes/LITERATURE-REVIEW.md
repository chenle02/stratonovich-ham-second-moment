# Literature review and contribution crosswalk — November 9, 2026

This is the bounded literature goal requested by Le after the reader merge.
It integrates relevant earlier SWE work, explains the present contribution,
and distinguishes three ongoing Skorohod projects. It does not replace the
original scientific completion contract or independently certify the proof.

## Goal and acceptance criteria

1. Check source editions and the model/result boundaries for Chen–Dalang (2015),
   Balan–Le Chen–Xia Chen (2022), Chen–Eisenberg (2023), and Chen–Guo–Song (2024).
2. Place them alongside the direct Stratonovich predecessors and relevant
   colored-noise Skorohod bounds. Explain why none is a direct substitution
   yielding the present claimed second-moment identification.
3. Put the current contribution near the start of the technical manuscript;
   keep the reader concise and align its technical links with the rebuilt notes.
4. Identify the three ongoing projects as ongoing, without invented titles,
   public-preprint status, theorem claims or use as proof inputs.
5. Preserve all theorem statements/proof bodies, validate both builds and
   external reader links, record the development history and deliver through Git.

The final counts, hashes and verification results are recorded in
[the validation record](../reviews/2026-11-09-literature-review/VALIDATION.json).
The main theorem's independent acceptance remains open.

## Retrieval and edition discipline

The local wiki search and cite commands were run in a disposable clone, because
ranked search can rebuild its ignored index. The shared wiki was not modified.
Queries included `wave` with author `Chen, Le`, `moments` with author `Guo`, and
`Stratonovich hyperbolic`; exact cite lookups included the four principal papers
and Chen–Hu. Their synthesized pages and the Skorohod-versus-Stratonovich concept
page were read before primary-source comparisons. The initial system Python
lacked frontmatter; the existing wiki virtual environment supplied the tool.

BibTeX identities were checked against the read-only All.bib. The published
Guo–Chen–Song record is `chen.guo.ea:24:moments`, not the retained 2022 preprint
identity. The local Publications/31 PDF is arXiv v1; it was not passed off as the
journal article. The published PDF was retrieved from Le's author website and
matches the previously recorded published hash b39465dc… in the wiki.
The first three principal PDFs were copied from the existing publication
symlinks, after checking the actual title pages and journal identities.

Full retained primary PDFs and two flattened reading sources are pinned under
[sources/literature-20261109](../sources/literature-20261109/source-pins.json).
The flattened sources are stored as lossless gzip to preserve their original
bytes (including upstream indentation); they are not published PDF artifacts.
Xia Chen's existing 64-page author manuscript remains pinned by the original
[source manifest](../sources/SOURCE-MANIFEST.md), not replaced by arXiv v1.

Read coverage is selected model/assumption passages, main result statements,
relevant remarks and method descriptions. For CGS, the rendered published
pages 4257 and 4259 were also inspected directly. This is a statement/attribution
crosswalk, not a full independent proof audit of each source. No MathSciNet
citation-chain search or exhaustive novelty verdict is claimed.

## Principal source/result crosswalk

| Source | Model, interpretation and data | Supported result and pinpoint | Role here and non-transfer boundary |
|---|---|---|---|
| Chen–Dalang (2015), DOI 10.1016/j.spa.2014.11.009 | One-dimensional SWE, space-time white noise, Itô–Walsh random field; rough deterministic displacement and measure velocity under its stated assumptions | Theorem 2.3, published pp. 1610–1611, gives moment bounds and the solvable second-moment identity; Corollary 1.1, pp. 1607–1608, specializes constant data; Theorem 2.7, p. 1612, gives the second Lyapunov rate and intermittency bounds | Foundational SWE second-moment and rough-data context. White temporal noise and its stochastic integral do not identify the correlated-time Stratonovich solution. |
| Balan–Le Chen–Xia Chen (2022), DOI 10.1214/21-AIHP1207 | Static Gaussian noise, Skorohod wave solution, data (1,0); homogeneous covariance functions in dimensions at most three and spatial-white cases in dimensions one and two | Theorem 1.6, pp. 1592–1593, gives exact large-time/high-moment asymptotics with a variational constant. The separate three-dimensional spatial-white case is critical, not a global large-time case covered by that claim. | Closest of Le's papers for sharp hyperbolic asymptotics. Static versus colored time and Wick versus ordinary multiplication both matter; no constant or solution identity is imported. |
| Chen–Eisenberg (2023), DOI 10.1007/s40072-022-00258-6 | Fractional differential operators, static Gaussian noise, Skorohod interpretation, constant displacement/zero velocity where required; fractional temporal derivative order strictly below two | Theorems 1.6–1.7, pp. 1207–1209, give solvability and exact moment asymptotics under their covariance, parameter and nonnegative-kernel assumptions | Broader fractional-equation development of the static moment program. Fractional differentiation is not fractional temporal noise. The ordinary wave endpoint is not silently included in a theorem stated for time order below two. |
| Chen–Guo–Song (2024), DOI 10.1090/tran/9138 | Fractional SPDE family with space-time white noise, Itô–Skorohod interpretation and constant data. The matching lower bound requires positive displacement and nonnegative velocity, plus its kernel hypotheses | Theorem 1.1(a), pp. 4259–4260, gives exact second-moment formulas and rate; Proposition 5.10, pp. 4284–4286, specializes the wave growth orders. Equations (1.10a,b)–(1.11), pp. 4257–4258, give matching p^(3/2) orders with explicitly nonoptimal constants | Central wave moment-growth predecessor. Exact second moments and matching higher-moment orders are different conclusions; the latter do not identify a sharp higher-moment constant or prove general higher-moment limit existence. |

The declared parameter windows are nonempty. For example, the one-dimensional
space-time-white wave model with constant displacement 1 and velocity 0 is an
admissible comparison in CD/CGS. In BCC a one-dimensional Riesz covariance of
homogeneity 1/2 lies in its homogeneous range; white noise in dimension one is
also a separately stated case. For CE one may take spatial fractional order 2,
time order 1, smoothing order 0, dimension 1 and Riesz degree 1/2: the strict
solvability inequality reads 1/2 < min(2,4,1). These are source examples, not
parameter maps converting those equations into the current Stratonovich model.

Only the existence and qualitative form of these earlier results are used in
the new exposition. Their constants, normalized diffusion speeds and noise
strengths are not transplanted. The present equation has Laplacian coefficient
one and its original covariance amplitude; earlier displayed coefficients may
use a wave speed or a half-diffusion convention. An equality of constants would
require a separate normalization and functional-domain comparison.

## Direct Stratonovich and colored-noise context

- Balan (2022), `balan:22:stratonovich`: static Stratonovich construction in
  dimensions one and two under a spectral condition stronger than Dalang's.
  The retained flattened source's model, main construction statement were
  consulted. This is construction context, not a claim
  of the present exact colored-time constant.
- Xia Chen–Hu (2025), `chen.hu:25:hyperbolic`: static Stratonovich solvability
  and homogeneous moment asymptotics. The published main statements provide
  direct background. Existing qualifications concerning printed constants and
  separate audits are retained; this review does not adopt a correction or a
  numerical identification with the present variational constant.
- Xia Chen–Deya–Jian Song–Tindel (2023), `chen.deya.ea:23:hyperbolic`:
  Strichartz/Young-type well-posedness in dimensions one and two, under its own
  noise and data hypotheses. The retained source is the edition identified in
  the source manifest. No universal construction theorem or flat-data application
  is imported from this citation.
- Xia Chen's pinned author manuscript: Theorem 1.2 is a two-sided first-moment
  result, not the exact first-moment limit stated in arXiv v1. Remark 5.1 gives
  the coarse second-moment growth bound. Both retain their original source
  qualifications in the notes. No normalization correction is adopted.
- Balan–Conus (2016): fractional-temporal-noise Skorohod moment bounds under
  their stated covariance assumptions; the existing source and comparisons
  remain in place.
- Hu–Wang (2024), `hu.wang:24:matching`: general colored-noise Skorohod moment
  bounds, especially Theorem 3.7 in the retained flattened source. Its covariance
  and Green-kernel hypotheses remain explicit. Matching orders alone are not a
  sharp constant or exact-limit theorem. The new citation describes this scope,
  not a fresh proof/application verification.

## Present contribution to emphasize

The draft's contribution is a second-moment result in the original correlated-
time Stratonovich model, retaining the homogeneous covariance class in dimensions
one through three. The contribution paragraph highlights:

1. An independent finite upper bound on the correct time scale, improving the
   source's coarse quadratic exponential estimate in the target parameter range.
2. A limiting constant specified intrinsically over the full nonnegative smooth
   compact spacetime-control class, including nonseparable controls, with original
   covariance amplitude, unit kinetic coefficient and Gaussian half-action.
3. Identification of upper and lower rates for the same canonical solution,
   with the zero covariance case treated directly.
4. Derived occupation/spatial-energy bounds and the exact white spatial energy,
   distinguished from a numerical evaluation of the entire moment supremum.

These are the written candidate's claims, not new independent clearance.
No “first ever” claim, general new-method priority, numerical closed form,
identification of the auxiliary label-one score with an actual first moment,
or equivalence with a Skorohod constant is asserted. The current paper's
self-pairings and unequal-order terms prevent literal reuse of orthogonal-chaos
arguments. No automatic continuity conclusion is asserted at a noise endpoint.

## Three ongoing joint projects: scope, not unpublished theorem imports

Le supplied the following distinctions explicitly in this session:

[held back: collaborators' unpublished work]

[held back: collaborators' unpublished work]

The manuscript uses descriptive prose, not fabricated manuscript titles or
bibliographic entries. No source-author/coauthor message, email, publication,
wiki edit, registry operation or further Skorohod proof work is performed.

## Remaining limits

This completes a focused attribution and positioning task once its build and
Git delivery checks pass. It does not complete the original research project,
its whole-mathematical reviews, source/application gate, final visual/cold review
or acceptance. Earlier receipts remain bound to their original source/PDF bytes;
pagination changes in the new edition do not transfer old visual-page credit.

## November 10 expansion: both stochastic interpretations

The book now has a dedicated comparison in `literature_review.tex`, organized
by white-in-time, static and fractional temporal noise. It explains Skorohod
orthogonality, Stratonovich traces, the dependence of smooth-noise limits on
the approximation, and practical advantages and limitations of each model.
The source comparison distinguishes construction, growth-order bounds and
exact asymptotic limits. In particular, the CDST2025 data restrictions and the
BS2019 Riesz-limit specialization are retained. This is a bounded survey;
it is not an exhaustive novelty verdict or a new scientific review gate.

The pinned author edition remains the authority for the source first-moment
statement. Catalogue presence alone does not establish edition fidelity.
