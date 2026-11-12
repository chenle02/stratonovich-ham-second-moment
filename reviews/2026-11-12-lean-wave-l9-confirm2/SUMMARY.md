# Wave L9 re-confirmation reviews: summary

Companion ba6c565 (wave-l9/repair; confirmation-round repairs, docs only; reviewed commit 338cdba), manuscript a284420; reviewer Codex gpt-6.1-sol, effort high, min-confidence high, --source-revision ba6c565. Packets built by scratchpad/build-l9-reconfirm.py. Every finding below is verbatim from report.json.

Packets: r1 the c1-c4 confirmation findings, the nine renamed headings, the Scope bullet, no new overclaim, L8 repairs kept; r2 one check per remaining (whole result) heading (56) plus classification consistency (split from r1 for size). Retry only on tool failure, recorded in the driver log.

## r1-findings-renames

Preflight: contract-check CONTRACT-OBSERVABLE (14 required field(s), 0 dispatch input(s); no provider call); dry run exit 0 (dryrun/); contract-check with --dispatch-input dryrun/prompt.txt CONTRACT-OBSERVABLE (14 required field(s), 1 dispatch input(s); no provider call)

Driver log:
```
2026-11-12T15:53:58Z start attempt-01
2026-11-12T15:59:15Z attempt-01 exit=2 Status: review-complete
2026-11-12T15:59:15Z done
```
### attempt-01
```
# CLI review attempt

Status: review-complete

Scientific verdict: FAIL

Accepted: False

See receipt.json, input-manifest.json, prompt.txt, and retained transport.
```
Verdict: **FAIL**, confidence: **high** (attempt-01)
Check verdicts: PASS 6, PASS_WITH_NOTES 1, PARTIAL 1, FAIL 2 (of 10)

Checks not PASS/PASS_WITH_NOTES:
- c3-C1: PARTIAL: The originally identified IntervalScalar and StaticPhaseCauchy headings and their Index references are repaired at ledger:3196,6887,702-712,784-788. Their supplied hypotheses match IntervalScalar.lean:1167-1173 and StaticPhaseCauchy.lean:577-582. However, the expanded partial-module classification still conflicts with the surviving RemoveMask 'whole result' Index row at ledger:761; see R1.
- RENAMED-HEADINGS: FAIL: The nine new section headings accurately describe their wrappers, supplied inputs and complete subclaims, including IntervalScalar.lean:642-654 and WaveTwoVariances.lean:822-861. The required Index cleanup is incomplete: ledger:761 still calls P:variational-remove-mask a 'whole result', although RemoveMask.lean:697-705 expressly retains a narrower abstract-function conclusion. This is neither an input-free definition nor an input-free complete bound.
- SCOPE-BULLET: FAIL: Ledger:54-80 names the same ten modules and audit exception as FORMALIZATION.md:82, and the fifty-two-result sentences are qualified. Nevertheless, the requirement that nothing calls these partial modules whole results fails at ledger:761. That row contradicts the corrected RemoveMask heading at:5538 and coverage.yaml:1618-1621.

Findings, fatal (0):

Findings, major (1):
- R1 — Residual RemoveMask whole-result classification. candidate/statement-ledger.md:761 says 'P:variational-remove-mask (whole result; rate part with nothing supplied, the point display over the named input RawBlockOriginalLower)'. Lean instead explicitly says 'the canonical solution u and its moment are not defined in Lean' at lean/StratonovichHAMSecondMoment/RemoveMask.lean:697-700, and its wrapper takes '{L : ℝ → ℝ}' and 'hRB : RawBlockOriginalLower ... L' at:702-705. TeX asserts the display 'For the original canonical solution and any fixed x' at manuscript/notes/integrated_unmasked_variational.tex:173-177. Thus this row is not an input-free complete definition or bound and contradicts the repaired heading, Scope and inputs-supplied/weaker coverage row. Exact fix: replace 'whole result' at ledger:761 with 'part of a result', retaining the supplied-input disclosure and specifying Rayleigh-form rates and a real function in place of the point moment.

Findings, minor (1):
- R2 — Deferred Archimedes proof-route comment. lean/refutations/wave-green-fourier/ArchimedesUnit.lean:8-9 says 'The proof uses the package law at a unit vector', whereas:39-40 uses 'Measure.toSphere_ne_zero' directly. The manuscript's 'direct integration over its normal coordinate' at manuscript/notes/notes_stratonovich_ham_second_moment.tex:2125-2130 is unaffected. Optional exact fix in a later comment-only wave: replace the proof-route sentence with 'The proof uses Measure.toSphere_ne_zero to establish nonzero sphere mass.' The documented deferral is acceptable.

Required repairs (1):
- Correct candidate/statement-ledger.md:761 from 'whole result' to an accurately scoped partial-result description, retaining its supplied input and disclosing the Rayleigh-rate and abstract-function substitutions.

Limitations (5):
- Requirement A was completed; truncated output was reread. Partial-file entries cover the specified passages, not unrelated contents of those files.
- Proof correctness, compilation and kernel replay were outside this correspondence review; no build was run.
- Provenance metadata was read only at lines1-42; remaining bindings, hashes and repository history were not independently authenticated.
- The complete claims inventory and unrelated ledger classifications were not independently recertified.
- This AI review is not human verification or a novelty audit.

## r2-whole-result-headings

Preflight: contract-check CONTRACT-OBSERVABLE (14 required field(s), 0 dispatch input(s); no provider call); dry run exit 0 (dryrun/); contract-check with --dispatch-input dryrun/prompt.txt CONTRACT-OBSERVABLE (14 required field(s), 1 dispatch input(s); no provider call)

Driver log:
```
2026-11-12T15:53:30Z start attempt-01
2026-11-12T16:05:06Z attempt-01 exit=2 Status: review-complete
2026-11-12T16:05:06Z done
```
### attempt-01
```
# CLI review attempt

Status: review-complete

Scientific verdict: FAIL

Accepted: False

See receipt.json, input-manifest.json, prompt.txt, and retained transport.
```
Verdict: **FAIL**, confidence: **medium** (attempt-01)
Check verdicts: PASS 29, FAIL 20, INCONCLUSIVE 8 (of 57)

Checks not PASS/PASS_WITH_NOTES:
- WHOLE DampedMultiplier: FAIL: The covariance-smoothing assertion remains absent, not merely supplied: candidate/statement-ledger.md:1692-1704; DampedMultiplier.lean:486 only proves multiplier membership, whereas manuscript/notes/notes_stratonovich_ham_second_moment.tex:845-846 identifies actual smoothing as producing that multiplier.
- WHOLE DampedNormsHomog: FAIL: The wrapper at DampedNormsHomog.lean:669-692 lacks the comparison lower bounds and smoothing assertions. Other modules add lower bounds, but the covariance-smoothing conclusion remains unformalized: candidate/statement-ledger.md:1917-1926 and lean/coverage.yaml:235-238.
- WHOLE FiniteWick: FAIL: This is a foundation for the finite-value Wick step, not the whole labelled terminal-chain lemma. FiniteWick.lean:690-710 concerns finite products; the TeX also concludes chain-integral existence, bounds and series convergence at main manuscript:3607-3644. The ledger itself distinguishes these at :2265-2273,2319-2320.
- WHOLE GaussianHermite: FAIL: GaussianHermite.lean:243-259,480-481 supplies orthogonality, recurrence and polynomial spanning. These are proof steps, not the whole Fock, cutoff or mild-construction results; see main manuscript:2472-2489,2531-2553 and candidate/statement-ledger.md:2671-2682.
- WHOLE H1Density: FAIL: H1Density.lean:86-91,575 proves density, a sentence inside the proof at manuscript/notes/integrated_spatial_occupation.tex:262-266. It does not prove either labelled proposition whose proof uses density; the section explicitly calls itself a foundation at ledger:2827-2840.
- WHOLE HermiteFock: FAIL: HermiteFock.lean:597-620 proves an abstract finite Fock bound conditional on a column inequality. That is the Fock half of the proof, not the full spatial/operator conclusion in main manuscript:2472-2489; ledger:2936-2944 expressly says so.
- WHOLE L8Completed: FAIL: Discharging inputs does not complete missing conclusions. L8Completed.lean:128-154 uses K0*Rsp, :262-280 brackets a score supremum rather than C2, and :312-345 does not include the final B1 conclusion of the uniform-tail lemma. Compare occupation-ceiling TeX:205-220,252-266 and main TeX:3725-3726.
- WHOLE MaskedAuxiliaryNorm: FAIL: MaskedAuxiliaryNorm.lean:932-950 handles complex H only. The real-H complexification clause at manuscript/notes/integrated_covariance_foundation.tex:99 is expressly unformalized at ledger:3867-3871.
- WHOLE OccupationCeilingExact: FAIL: OccupationCeilingExact.lean:748-757 proves the exact variational ceiling, but not the moment conclusion C2<=U2 at manuscript/notes/integrated_occupation_ceiling.tex:217. Its comparison :779-785 likewise concerns the score supremum, not C2.
- WHOLE OccupationCeilingFinite: FAIL: OccupationCeilingFinite.lean:938-968 gives a larger ceiling using K0*Rsp rather than Cocc; the energy form and moment conclusion are absent. L8Completed removes SpaceTimeCS, not these differences. Compare occupation-ceiling TeX:209-217.
- WHOLE OccupationPhysicalClass: INCONCLUSIVE: The quantitative conclusions and SquarePairingBounds discharge are present at OccupationPhysicalClass.lean:782-803 and SpatialOccupationL7Completed.lean:323-374. However, the bridge from strongly H1-measurable fields to IsOccField is unformalized; compare the latter's :154-158 with spatial-occupation TeX:381-414. I do not certify the whole-class correspondence from this packet alone.
- WHOLE RawOccupationEnergy: INCONCLUSIVE: RawOccupationEnergy.lean:703-720 contains every displayed algebraic and dilation conclusion over IsOccField. Equality of that modelled occupation class with the TeX class is not formalized, as ledger:5466-5474 records; this affects the meanings of both suprema.
- WHOLE RayleighTail: FAIL: RayleighTail.lean:178-185 proves the scalar tail estimate and finite head only. The labelled lemma additionally asserts finiteness of the operator-moment bound at manuscript/notes/integrated_gaussian_tubes.tex:466-467; ledger:5526-5528 confirms that application is absent.
- WHOLE SeriesType: FAIL: SeriesType.lean:89-91 is an elementary series estimate, not the coefficient/type equivalence of L:positive-series-type in main TeX:7222-7234. The latter is proved in TypeContinuity.lean:383-389. Ledger:5658-5662 identifies SeriesType as inline foundations.
- WHOLE SpaceTimePositivity: FAIL: SpaceTimePositivity.lean:1073-1085,1103-1108 proves integral identities for continuous compact fields. It does not construct Q, rho_g, J_G or the mean map required by occupation-ceiling TeX:23-42 and intrinsic-constant TeX:22-39.
- WHOLE SpatialBracket: FAIL: SpatialBracket.lean:481-495 brackets sSup(scoreSet ... 2), and uses energyValue(K0*Rsp). The TeX brackets C2 and compares the actual occupation energy at occupation-ceiling:257-264. Neither L8 completion nor the exact comparison supplies the missing C2 identification.
- WHOLE SpatialFourLinear: INCONCLUSIVE: Density is discharged and the square, four-linear, positivity and ratio conclusions appear at SpatialOccupationL7Completed.lean:122-276. Sequential continuity is mathematically appropriate for H1, but the whole energy-score correspondence still uses the unbridged rate/cost interpretation recorded at ledger:6167-6169.
- WHOLE SpatialOccupationCompleted: INCONCLUSIVE: The named floor and StaticControls inputs are genuinely discharged at SpatialOccupationCompleted.lean:73-81,109-124. The remaining correspondence boundary is the identification of the Rayleigh/integral quantities with the manuscript's rate and variance, explicitly left outside Lean at ledger:6320-6324.
- WHOLE SpatialOccupationL7Completed: INCONCLUSIVE: The density and square-pairing discharges are present, and manuscript constants are restored at :363-374. The occupation-class bridge and rate/cost identifications remain outside the formalization: ledger:6396-6405. Completion of named inputs alone does not settle those semantic correspondences.
- WHOLE SpatialSmoothRatio: INCONCLUSIVE: The ratio and score conclusions are present after the documented completions: SpatialSmoothRatio.lean:693-770; L8Completed.lean:189-203. Whether that proves the manuscript result rather than its integral/Rayleigh reformulation depends on the unformalized identifications at ledger:6498-6501.
- WHOLE SpatialStaticControls: INCONCLUSIVE: Both parts, including the supremum score form, are supplied by SpatialOccupationCompleted.lean:93-100 and L8Completed.lean:176-181. The rate/cost correspondence boundary at ledger:6600-6604,6772-6774 remains unbridged; I do not treat an equivalent-looking reformulation as verified correspondence without that identification.
- WHOLE VariationalDilation: INCONCLUSIVE: VariationalDilation.lean:412-420 proves the bijection and four identities for its definitions; :438-458 only transfers genuineness conditions. The spectral-rate and stochastic-variance identifications are not formalized or supplied as named hypotheses, as ledger:7807-7817,7846-7850 records.
- WHOLE VariationalFloor: FAIL: VariationalFloor.lean:466-472 proves a positivity floor for a Rayleigh set, not the operator, regularity and integrated-rate conclusions of P:variational-unmasked-rate at unmasked-variational TeX:98-111. Ledger:7951-7958 calls it a foundation with no labelled result of its own.
- WHOLE VariationalMean: FAIL: The heat-envelope lemma is complete, but VariationalMean.lean:679-711 proves bounds and Lipschitz properties only. The mixed-derivative conclusion at unmasked-variational TeX:66-67 is missing, explicitly acknowledged at ledger:8135-8141.
- WHOLE VariationalRate: FAIL: VariationalRate.lean:739-759 omits the operator half of P:variational-unmasked-rate; :781-823 and L8Completed.lean:163-168 omit Q2>=S2pos from P:variational-positive-scores. These are conclusions in unmasked-variational TeX:100-107,279, not undisclosed upstream inputs.
- WHOLE WaveGreen: FAIL: The Green-measure facts are proved, but the labelled damped-norm result remains incomplete even after its companion wrappers: ledger:8323-8329,8411-8417 records the absent covariance-smoothing identification. Green masses and scaling alone also do not prove L:higher-riesz.
- WHOLE WaveGreenFourier: FAIL: WaveGreenFourier.lean:721-727 proves the Fourier/mass display used in proofs; ledger:8455-8465,8491-8499 describes only the Green-smoothing part of the damped lemma. It does not itself prove the labelled contraction lemmas or the full damped result.
- CLASSIFICATION-CONSISTENCY: FAIL: The nine renamed headings agree with the explicit partial-module list, but the classification still calls 47 results 'Whole labelled result' while acknowledging seventeen narrower conclusions at FORMALIZATION.md:80. Proven omissions and proof-step foundations still retain whole headings; same-assumptions is not equivalent to every conclusion proved.

Findings, fatal (0):

Findings, major (8):
- R1 Damped-family headings overstate completion. Lean DampedMultiplier.lean:486 states 'IsMultiplier (gaussMult ...)', whereas main manuscript:845-846 says 'Spatial Gaussian smoothing ... give multipliers in this class'. Ledger:1703-1704 explicitly leaves the spectral identification unformalized. Rename DampedMultiplier and DampedNormsHomog as scoped/partial results, and WaveGreen/WaveGreenFourier as foundations or specified partial results; do not present their combination as the whole labelled lemma without the missing conclusion.
- R2 MaskedAuxiliaryNorm omits a stated case. Lean MaskedAuxiliaryNorm.lean:934 requires 'InnerProductSpace ℂ H'; covariance-foundation TeX:99 additionally states 'For a real H, the same assertion holds after complexification'. Rename the heading to identify the complex-H case only, or supply the missing case before retaining 'whole result'.
- R3 Occupation ceilings and bracket are not whole manuscript results. Lean OccupationCeilingExact.lean:754 bounds 'sSup (scoreSet ...)' and L8Completed.lean:153-154 uses 'K0 ... * Rsp'; occupation-ceiling TeX:212 uses C_occ and :217 additionally concludes 'C_2 ... <= U_2'. The bracket similarly uses C_2 at TeX:257-264, not just the score supremum. Rename OccupationCeilingExact, OccupationCeilingFinite, SpatialBracket and the mixed L8Completed heading to their actual scopes. A complete uniform-tail component does not make L8Completed's other results whole.
- R4 SpaceTimePositivity is a partial integral-form foundation. Lean SpaceTimePositivity.lean:1106-1108 concludes integrability and 'stForm ... = rawCost ...'; intrinsic-constant TeX:24-35 additionally constructs J_G and identifies the uniform mean, while occupation-ceiling TeX:25-36 constructs Q and rho_g. Rename its heading as integral-form parts/foundations, not a whole result.
- R5 VariationalMean and VariationalRate omit explicit conclusions. Lean VariationalMean.lean:682-691 gives bounds, continuity and integrability, not 'Every mixed time and space derivative' in unmasked-variational TeX:66-67. Lean VariationalRate.lean:742-759 concerns a Rayleigh supremum, omitting the self-adjoint operator assertion at TeX:100-102; its score wrappers omit 'Q_2 >= S_2^pos' at TeX:279. Rename both headings to identify these partial results, and classify them accordingly.
- R6 RayleighTail omits the labelled lemma's application. Lean RayleighTail.lean:182-185 states scalar tail and head integrability; gaussian-tubes TeX:466-467 additionally asserts that the operator-moment bound is finite. Rename the heading to 'scalar estimate, application not formalized', or formalize that application.
- R7 Foundations retain misleading whole-labelled-result headings. FiniteWick.lean:690-694 proves a finite-product Wick identity, whereas main TeX:3607-3644 includes chain integrals and convergence. GaussianHermite.lean:258-259 proves a recurrence used in main TeX:2515-2524; HermiteFock.lean:614-620 proves its abstract Fock step. H1Density.lean:575 proves the density sentence inside spatial-occupation TeX:262-266. SeriesType.lean:89-91 is not the type equivalence at main TeX:7222-7234. VariationalFloor.lean:466-472 is not the full proposition at unmasked-variational TeX:98-111. Rename these six headings as foundations/proof steps, retaining precise statements of the facts actually proved.
- R8 Classification conflates assumptions with conclusion coverage. FORMALIZATION.md:80 says 'Whole labelled result, nothing supplied' while enumerating omitted conclusions; its :122,134 also counts foundations there. For example, Lean OccupationCeilingExact.lean:748-757 lacks the moment sentence in occupation-ceiling TeX:217. Split full conclusions, narrower/partial conclusions and foundations into distinct categories, update the ledger Scope and affected headings, and reconcile the summary wording with coverage.yaml's weaker rows. The existing nine-heading repair is insufficient.

Findings, minor (0):

Required repairs (3):
- Replace the unsupported whole-result headings identified in R1-R7 with headings naming the precise partial result, special case or foundation actually proved, unless the missing conclusions are supplied by a verified, explicitly documented completion.
- Revise FORMALIZATION.md's classification and the ledger Scope so that narrower conclusions and proof-step foundations are not counted as whole labelled results; keep assumption coverage separate from conclusion coverage.
- Preserve the existing disclosures of omitted conclusions, supplied inputs and dimension restrictions when making those classification repairs.

Limitations (5):
- The required adjudication, heading inventory, whole-section opening/scope prose, classification paragraphs, relevant coverage rows, supplied-input paper wrappers and complete TeX excerpt file were read. Files marked partial contain unread material outside those required selections.
- Eight correspondence checks remain inconclusive because the packet records unformalized bridges between occupation-class representations or between integral/Rayleigh definitions and manuscript stochastic/spectral quantities. Equivalent mathematical representations should not automatically be called special cases, but their equivalence was not certified here.
- The FAIL verdict does not depend on those inconclusive checks: explicit omitted conclusions and proof-step-only headings independently block acceptance.
- Proof correctness was outside scope; no Lean build, kernel replay, network access or byte-hash verification was performed.
- This is an AI correspondence review, not human verification or a novelty audit.

