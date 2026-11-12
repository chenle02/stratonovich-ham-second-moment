# Wave L9 final confirmation (round 9): summary

Companion 6d108c0 (wave-l9/repair; convention text, step_Q, 55 rows repaired after the lost-disclosure check, docs only; reviewed commit 06ee849), manuscript a284420; reviewer Codex gpt-6.1-sol, effort high, min-confidence high, --source-revision 6d108c0. Packets built by scratchpad/build-l9-reconfirm9.py. Lost-disclosure check re-run at 6d108c0 (identical output): 657 removed Index rows, 376 checks, 291 row, 85 section, 0 lost. Pointer checker: Index rows 186, problems 0; table checker totals 2468/1300/1168. Section-level sample: seed 20261112, stratified by module (packet f4, tools/section-sample.txt). Every finding below is verbatim from report.json.

Packets: f1 convention text and the step_Q row; f2/f3 the 55 repaired section-table rows (28 + 27) with full Lean modules and TeX with proofs; f4 25 sampled section-level matches and no new overclaim over 06ee849..6d108c0. Retry only on tool failure, recorded in the driver log.

## f1-convention-stepq

Preflight: contract-check CONTRACT-OBSERVABLE (14 required field(s), 0 dispatch input(s); no provider call); dry run exit 0 (dryrun/); contract-check with --dispatch-input dryrun/prompt.txt CONTRACT-OBSERVABLE (14 required field(s), 1 dispatch input(s); no provider call)

Driver log:
```
2026-11-12T20:11:27Z start attempt-01
2026-11-12T20:12:51Z attempt-01 exit=0 Status: review-complete
2026-11-12T20:12:51Z done
```
### attempt-01
```
# CLI review attempt

Status: review-complete

Scientific verdict: PASS

Accepted: True

See receipt.json, input-manifest.json, prompt.txt, and retained transport.
```
Verdict: **PASS**, confidence: **high** (attempt-01)
Check verdicts: PASS 2 (of 2)

Findings, fatal (0):

Findings, major (0):

Findings, minor (0):

Required repairs (0):

Limitations (3):
- Requirement A was completed without gaps; unread portions of partially covered files lie outside its required passages.
- Acceptance concerns only the two requested documentation checks, not an exhaustive audit of label assignments, lost disclosures, proof correctness, or packet byte bindings.
- This AI review is neither human verification nor a novelty audit.

## f2-repaired-rows-a

Preflight: contract-check CONTRACT-OBSERVABLE (14 required field(s), 0 dispatch input(s); no provider call); dry run exit 0 (dryrun/); contract-check with --dispatch-input dryrun/prompt.txt CONTRACT-OBSERVABLE (14 required field(s), 1 dispatch input(s); no provider call)

Driver log:
```
2026-11-12T20:11:27Z start attempt-01
2026-11-12T20:17:53Z attempt-01 exit=2 Status: review-complete
2026-11-12T20:17:53Z done
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
Check verdicts: FAIL 1, PASS 27 (of 28)

Checks not PASS/PASS_WITH_NOTES:
- ROW line 1458: FAIL: The appended hJ and hJm are correct, and the original text is unchanged (diffs/docs-06ee849-6d108c0.diff:39-41). However, the norm-convergence interpretation omits completeness: lean/StratonovichHAMSecondMoment/ComplexPhaseScalar.lean:251-256 assumes only a normed real space and concludes IntegrableOn plus an integral inequality. The TeX's operator-norm convergence is in a Hilbert-space setting (manuscript/notes/notes_stratonovich_ham_second_moment.tex:2289-2290,2338). See P1.

Findings, fatal (0):

Findings, major (1):
- P1 — ROW line 1458 overextends norm convergence to incomplete spaces. The row says 'For a real normed space E' and calls its conclusion 'norm convergence'. Lean instead assumes '[NormedAddCommGroup E] [NormedSpace ℝ E]' and concludes 'IntegrableOn J (Ioi 0) ∧ ...' without completeness or a convergence conclusion (lean/StratonovichHAMSecondMoment/ComplexPhaseScalar.lean:251-256). The TeX assumes 'a complex Hilbert space' and states 'The integrals converge in operator norm' (manuscript/notes/notes_stratonovich_ham_second_moment.tex:2289,2338). Absolute norm integrability does not ensure an E-valued integral in an incomplete space: in c00 with the ℓ1 norm, let J equal e_n on successive subintervals of (1,2) of lengths 2^(-n), and zero elsewhere. It satisfies the row's domination with a=0, lambda=1, c=8, but its integral in the completion is the infinitely supported vector (2^(-n)), outside E. Exact fix: qualify the norm-convergence interpretation by completeness of E, and explicitly distinguish the unrestricted Lean IntegrableOn-plus-inequality statement from that Banach-space interpretation.

Findings, minor (0):

Required repairs (1):
- Amend candidate/statement-ledger.md:1458 to restrict the norm-convergence interpretation to complete E and disclose that the unrestricted Lean declaration itself states IntegrableOn and an integral norm inequality, not convergence in an arbitrary incomplete E.

Limitations (3):
- All reading required for the 28 checks was completed. Unlisted ranges of files marked partial were not reviewed; the verdict does not cover the remaining ledger rows or declarations.
- Lean compilation, proof correctness, packet-wide byte binding and the mechanical checker totals were not independently audited.
- This is an AI documentation-correspondence review, not human verification or a novelty audit.

## f3-repaired-rows-b

Preflight: contract-check CONTRACT-OBSERVABLE (14 required field(s), 0 dispatch input(s); no provider call); dry run exit 0 (dryrun/); contract-check with --dispatch-input dryrun/prompt.txt CONTRACT-OBSERVABLE (14 required field(s), 1 dispatch input(s); no provider call)

Driver log:
```
2026-11-12T20:11:27Z start attempt-01
2026-11-12T20:15:50Z attempt-01 exit=0 Status: review-complete
2026-11-12T20:15:50Z done
```
### attempt-01
```
# CLI review attempt

Status: review-complete

Scientific verdict: PASS

Accepted: True

See receipt.json, input-manifest.json, prompt.txt, and retained transport.
```
Verdict: **PASS**, confidence: **high** (attempt-01)
Check verdicts: PASS 27 (of 27)

Findings, fatal (0):

Findings, major (0):

Findings, minor (0):

Required repairs (0):

Limitations (4):
- Acceptance is confined to the 27 specified row checks. Other ledger rows and the global checker claims were not independently audited.
- Files marked partial were read only in the listed ranges, plus declaration-location searches. Unlisted portions of those files remain outside this review; no required row, repair hunk, declaration statement or relevant labelled TeX statement/proof remains unread.
- Proof correctness, recompilation, provenance-hash verification and historical claims of prior recompilation were not independently tested.
- This AI correspondence review is not human verification or a novelty audit.

## f4-section-sample-diff

Preflight: contract-check CONTRACT-OBSERVABLE (14 required field(s), 0 dispatch input(s); no provider call); dry run exit 0 (dryrun/); contract-check with --dispatch-input dryrun/prompt.txt CONTRACT-OBSERVABLE (14 required field(s), 1 dispatch input(s); no provider call)

Driver log:
```
2026-11-12T20:11:27Z start attempt-01
2026-11-12T20:18:56Z attempt-01 exit=0 Status: review-complete
2026-11-12T20:18:56Z done
```
### attempt-01
```
# CLI review attempt

Status: review-complete

Scientific verdict: PASS

Accepted: True

See receipt.json, input-manifest.json, prompt.txt, and retained transport.
```
Verdict: **PASS**, confidence: **high** (attempt-01)
Check verdicts: PASS 26 (of 26)

Findings, fatal (0):

Findings, major (0):

Findings, minor (0):

Required repairs (0):

Limitations (5):
- All mandatory requirement-A material was read completely, including recovery of truncated output. Files marked partial were consulted only in the listed ranges; their unlisted portions were not reviewed.
- Acceptance is confined to the specified 25 disclosure matches and the documentation repair diff; it does not certify unsampled section-level matches or the entire ledger.
- The mechanical checker's word-overlap criterion is not semantic verification; the sampled disclosures were compared independently with their removed rows, current section text and Lean statements.
- Lean proofs were not rebuilt or audited. Historical revisions and packet byte bindings were not independently authenticated.
- This AI correspondence review is neither human verification nor a novelty audit.

