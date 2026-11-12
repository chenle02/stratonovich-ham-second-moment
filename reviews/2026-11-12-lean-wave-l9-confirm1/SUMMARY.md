# Wave L9 confirmation reviews: summary

Companion 338cdba (wave-l9/repair: 7bd4c62 merges main aff7409 = L8 with both review repair rounds; 338cdba repairs the L9 findings, docs only), reviewed commit eb253a5, manuscript a284420; reviewer Codex gpt-6.1-sol, effort high, min-confidence high, --source-revision 338cdba. Packets built by scratchpad/build-l9-confirm.py. Every finding below is verbatim from report.json.

Packets: c1 g1 findings + merge resolution and preservation of both L8 repair rounds + mirror completeness; c2 g2/g3/g4 findings; c3 g5a/g5b/g6a/g6b findings + reclassifications of L:finite-word-cutoff and L:damped-homogeneous-norms; c4 re-run of the two g2 INCONCLUSIVE checks (CROSS-REFERENCES, SCOPE-AND-NOT-IN-LEAN) plus totals. Retry only on tool failure (not review-complete), recorded in the driver log.

## c1-damped-green-merge

Preflight: contract-check CONTRACT-OBSERVABLE (14 required field(s), 0 dispatch input(s); no provider call); dry run exit 0 (dryrun/); contract-check with --dispatch-input dryrun/prompt.txt CONTRACT-OBSERVABLE (14 required field(s), 1 dispatch input(s); no provider call)

Driver log:
```
2026-11-12T15:02:51Z start attempt-01
2026-11-12T15:42:08Z attempt-01 exit=2 Status: review-complete
2026-11-12T15:42:08Z done
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
Check verdicts: PARTIAL 1, PASS 7, PASS_WITH_NOTES 1, FAIL 1 (of 10)

Checks not PASS/PASS_WITH_NOTES:
- g1-W1: PARTIAL: The substantive repair is correct: lean/coverage.yaml:236-238 restores same-assumptions/weaker; candidate/statement-ledger.md:1686-1698,1852,1915-1921,8396-8411 distinguish multiplier membership from covariance identification and credit the Fourier wrappers correctly. DampedMultiplier.lean:458-459 explicitly excludes covariance identification, while WaveGreenFourier.lean:753-766 supplies the Green identification in dimensions 1,2,3, consistently with main TeX:845-847. However, lean/README.md:24-25 still advertises the 'full conclusions of fifty-two labelled results', without qualifying the narrower conclusions included in that number; see C1.
- NO-REGRESSION: FAIL: The technical smoothing, integrability and radial-density repairs are correct, and the inspected Lean changes since eb253a5 are comments only: diffs/l9-repair-eb253a5-338cdba.diff:187-237,1458-1500. The scope mirrors remain plain-English statements with matching ASCII and correctly square-root-defined Rayleigh rates. However, diffs/findings-repair-7bd4c62-338cdba.diff:74-85 revises the README overview while retaining the unsupported 'full conclusions' claim for all52 results. C1 requires qualification.

Findings, fatal (0):

Findings, major (1):
- C1 — README overview retains an unqualified full-conclusion overclaim. lean/README.md:24-25 says the modules 'prove the full conclusions of fifty-two labelled results'. That total includes the17 narrower conclusions explicitly recorded at lean/FORMALIZATION.md:80. In particular, main TeX manuscript/notes/notes_stratonovich_ham_second_moment.tex:845-847 asserts 'Spatial Gaussian smoothing and Gaussian smoothing of the Green kernel give multipliers in this class', whereas lean/StratonovichHAMSecondMoment/DampedMultiplier.lean:458-459 says 'The spectral identity for spatial covariance smoothing p_ε * Γ is not stated (only the membership of its multiplier, item5)'. The detailed README bullet at87-96 correctly acknowledges this limitation, but does not make the overview's literal full-conclusion count true. Exact fix: replace README.md:24-25 with wording such as 'formalize fifty-two labelled results to the scopes specified below, some with narrower conclusions, and parts of further results'. Keep the corrected numerical counts and detailed limitations.

Findings, minor (1):
- C2 — Deferred Archimedes proof-route wording. lean/refutations/wave-green-fourier/ArchimedesUnit.lean:8-9 says 'The proof uses the package law at a unit vector', but its proof at39-40 invokes 'Measure.toSphere_ne_zero' directly. The manuscript's 'direct integration over its normal coordinate' at manuscript/notes/notes_stratonovich_ham_second_moment.tex:2125-2131 is unaffected. Optional exact fix in a later comment-only wave: replace that sentence with 'The proof uses Measure.toSphere_ne_zero to establish nonzero sphere mass.' The documented deferral does not block acceptance.

Required repairs (1):
- Qualify lean/README.md:24-25 so the52-result overview does not claim full conclusions for results recorded with narrower conclusions; retain the existing counts and detailed scope disclosures.

Limitations (5):
- The expressly required sections and repair passages were read completely. Files marked partial were inspected only at the listed textual ranges, apart from the stated whole-file YAML parsing; their unrelated contents were not reviewed.
- The complete historical documentation diff since eb253a5 was not reread line by line. Relevant documentation changes were examined through the complete repair, combined-merge and L8-repair diffs; all Lean-change hunks in that historical diff were read.
- Compilation, proof correctness, receipt validity and complete provenance byte binding were not independently audited; this is a statement-correspondence review.
- The disclosed dimension-three toSphere modelling choice was not independently identified with Hausdorff or Riemannian surface measure.
- This AI review is not human verification or a novelty audit.

## c2-phase-occupation-complex

Preflight: contract-check CONTRACT-OBSERVABLE (14 required field(s), 0 dispatch input(s); no provider call); dry run exit 0 (dryrun/); contract-check with --dispatch-input dryrun/prompt.txt CONTRACT-OBSERVABLE (14 required field(s), 1 dispatch input(s); no provider call)

Driver log:
```
2026-11-12T15:02:51Z start attempt-01
2026-11-12T15:42:53Z attempt-01 exit=0 Status: review-complete
2026-11-12T15:42:53Z done
```
### attempt-01
```
# CLI review attempt

Status: review-complete

Scientific verdict: PASS_WITH_NOTES

Accepted: True

See receipt.json, input-manifest.json, prompt.txt, and retained transport.
```
Verdict: **PASS_WITH_NOTES**, confidence: **high** (attempt-01)
Check verdicts: PASS 9, PASS_WITH_NOTES 4 (of 13)

Findings, fatal (0):

Findings, major (0):

Findings, minor (2):
- C1 — ComplexPhaseScalar control-target wording. Candidate/statement-ledger.md:1584-1588 abbreviates BlockExponent as replacing the exponential bound and PhaseWeight as making 'the loss factor unsquared'. BlockExponent.lean:21-26 actually refutes the scalar majorant '(39+12*x)*exp x <= 100*exp x', corresponding to main TeX:2458-2459, not an identified propagator bound. PhaseWeight.lean:23-29 refutes an unsquared factor in the multiplier inequality, whereas main TeX:2968-2969 correctly has an unsquared factor for norms. Optional exact clarification: say 'the scalar block-sum majorant' and 'the multiplier/squared-norm loss factor unsquared'. The existing detailed declaration rows supply the correct distinctions.
- C2 — Generic refutation terminology. Lean README.md:266-267, 325 and FORMALIZATION.md:87 use 'wrong variants of the whole results'. For example, CellWidth.lean:26-33 concerns 'OccupationCeilingExact.idx', while integrated_occupation_ceiling.tex:169-173 uses first-index Borel cells, not that index. The repaired ledger correctly classifies this at 4554-4560, so the generic wording need not be read as manuscript-counterexample certification. Optional exact replacement: 'proofs refuting specified declaration variants, including manuscript scalar steps, Lean-route-only constructions, and totalized or broader-generalization controls; see the ledger for their domains'.

Required repairs (0):

Limitations (5):
- Complete-reading requirement A was met. Contextual files outside its required passages were inspected only in the ranges reported; structural parsing and byte verification are not substantive correspondence review of their remaining contents.
- No compiler, kernel replay or independent proof-correctness audit was performed; proof correctness was outside this contract.
- The supplied diffs establish comment-only Lean changes within this packet; no external repository history was accessed.
- No in-domain shift-equality refutation is supplied, and the ImaginaryRoot witness does not settle the strengthened root bound under the manuscript's full hypotheses.
- This is an AI correspondence review, not human verification or a novelty audit.

## c3-hermite-fock-word

Preflight: contract-check CONTRACT-OBSERVABLE (14 required field(s), 0 dispatch input(s); no provider call); dry run exit 0 (dryrun/); contract-check with --dispatch-input dryrun/prompt.txt CONTRACT-OBSERVABLE (14 required field(s), 1 dispatch input(s); no provider call)

Driver log:
```
2026-11-12T15:02:51Z start attempt-01
2026-11-12T15:41:46Z attempt-01 exit=2 Status: review-complete
2026-11-12T15:41:46Z done
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
Check verdicts: PASS 10, FAIL 2 (of 12)

Checks not PASS/PASS_WITH_NOTES:
- RESCAN: FAIL: C1: 'IntervalScalar (whole result)' and 'StaticPhaseCauchy (whole result)' remain at candidate/statement-ledger.md:3190,6881, despite their immediately stated inputs-supplied/weaker scope (:3192-3201,6883-6892). IntervalScalar.lean:1157-1175 assumes hsplits and hfixed, and StaticPhaseCauchy.lean:568-586 assumes the circle bound and identifications. The manuscript asserts bounds for actual evolutions and Duhamel phases (main TeX:3402-3414,2577-2605). This is the same completeness-language mismatch accepted as g6a-W2. The reviewed formulas, controls and numerical coverage totals otherwise support their disclosed scopes.
- NO-REGRESSION: FAIL: C1 also affects edited Scope and Index sentences: diffs/findings-repair-7bd4c62-338cdba.diff:223-226,288-289 retain whole-result terminology for partial consumers while correcting only the FockForm exception. The other scoped mathematical repairs are supported. Independently parsed scope data have 42 mirrors and no ASCII mismatches; the seven required TeX mirrors preserve their content. The complete changed-file inventory and Lean hunks in diffs/l9-repair-eb253a5-338cdba.diff:187-237,1458-1500 show comment-only Lean changes, not declaration or proof changes.

Findings, fatal (0):

Findings, major (1):
- C1 — Residual completeness-language mismatch in IntervalScalar and StaticPhaseCauchy. candidate/statement-ledger.md:3190,6881 still calls these sections '(whole result)', repeated for StaticPhaseCauchy at :780-784; the revised Scope at :62-64 singles out only FockForm as the exception. Lean instead assumes 'hsplits : coef = ...' and 'hfixed : ...' in lean/StratonovichHAMSecondMoment/IntervalScalar.lean:1168-1173, and 'hcircle : ...' plus coefficient and convergence inputs in lean/StratonovichHAMSecondMoment/StaticPhaseCauchy.lean:578-582. TeX asserts the actual evolution coefficient '[s^{2k}] E||U_F^epsilon(T;s)v||^2' at manuscript/notes/notes_stratonovich_ham_second_moment.tex:3405-3407 and the actual Duhamel-phase bound '||Z_n^epsilon(h)||' at :2589-2594. The detailed limitations are accurate but do not cure the prohibited headings, just as for accepted g6a-W2. Fix: rename both headings to identify proof steps/parts of results with supplied analytic inputs, update their Index references, and revise Scope:62-64 so 'whole result' is not the classification of these partial consumers. Retain the genuinely complete E:static-block-series subclaim.

Findings, minor (0):

Required repairs (1):
- Resolve C1 by replacing the IntervalScalar and StaticPhaseCauchy whole-result headings and corresponding references with accurately scoped proof-step/partial-result descriptions, and make the Scope classification consistent.

Limitations (5):
- Complete-reading requirement A was satisfied. Partial-file entries identify scoped contextual reading, not gaps in the mandatory sections, rows or finding-specific declarations.
- The longer merge-plus-repair diff was not read throughout lines 661-1457. The repair-only diff was read completely, and all changed Lean-file hunks in the longer diff were inspected.
- Provenance metadata was consulted, but packet hashes, repository ancestry and historical verification claims were not independently authenticated.
- Proof correctness and compilation were outside this correspondence review; no build was launched. Unrelated modules and findings from other review groups were not comprehensively audited.
- This AI review is not human verification or a novelty audit.

## c4-scope-totals-rerun

Preflight: contract-check CONTRACT-OBSERVABLE (14 required field(s), 0 dispatch input(s); no provider call); dry run exit 0 (dryrun/); contract-check with --dispatch-input dryrun/prompt.txt CONTRACT-OBSERVABLE (14 required field(s), 1 dispatch input(s); no provider call)

Driver log:
```
2026-11-12T15:02:51Z start attempt-01
2026-11-12T15:48:13Z attempt-01 exit=2 Status: review-complete
2026-11-12T15:48:13Z done
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
Check verdicts: PASS 4, FAIL 1 (of 5)

Checks not PASS/PASS_WITH_NOTES:
- NO-REGRESSION: FAIL: The mathematical repair wording,42 ASCII/TeX mirrors and changed summaries check out; the complete Lean-file hunks in l9-repair diff:187-237,1458-1500 change comments only. However, the repaired COMPLETION row retains a dimension overclaim: COMPLETION.md:29 says 'low-alpha convolution and phase contractions with nothing supplied (d = 1, 2, 3)'. The full phase-contraction wrapper is exclusively three-dimensional (L9Completed.lean:150-163), as is the manuscript lemma (main TeX:2054-2057,2072-2084). See C1.

Findings, fatal (0):

Findings, major (1):
- C1 — COMPLETION wave-L9 dimension scope. lean/COMPLETION.md:29, reproduced on the added line of diffs/findings-repair-7bd4c62-338cdba.diff:10, states 'low-alpha convolution and phase contractions with nothing supplied (d = 1, 2, 3)'. This assigns the three-dimensional range to both results. Lean instead states 'phase_contractions_paper_completed ... {Γ μ : Measure (Rd 3)}' at lean/StratonovichHAMSecondMoment/L9Completed.lean:150-151, with its trace conclusion at :155-163; only the low-alpha wrapper is dimension-general under H:homog (:96-110). TeX explicitly assumes a covariance 'on R^3' at manuscript/notes/notes_stratonovich_ham_second_moment.tex:2054-2057 and q in R^3 at :2073. Exact fix: replace the clause with 'low-alpha convolution in d = 1, 2, 3 and phase contractions in d = 3, with nothing supplied'. This is retained wording within a changed row, not a newly changed Lean statement.

Findings, minor (0):

Required repairs (1):
- Correct lean/COMPLETION.md:29 to distinguish low-alpha convolution in dimensions1,2,3 from the full phase-contraction result in dimension3.

Limitations (5):
- Requirement A was completed for its specified sections, diffs, count fields, excerpts and declaration statements. Supporting Lean files were not read as complete proof files; their partial coverage is itemized above.
- Proof correctness, compilation and kernel replay were outside this correspondence review; no build was run.
- Refutation files are absent from the packet. Their proof contents were not independently recertified; domain disclaimers were assessed against the supplied declarations, manuscript and prior report.
- The full merge-plus-repair documentation diff was not substantively read throughout; its file headers and every Lean-file hunk were inspected for the requested no-code-change check.
- This is an AI correspondence review, not human verification or a novelty audit.

