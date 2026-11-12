# Wave L9 re-review round 7 (pointer Index): summary

Companion 434a7e2 (wave-l9/repair; pointer Index and section-table repairs, docs only; reviewed commit a723987), manuscript a284420; reviewer Codex gpt-6.1-sol, effort high, min-confidence high, --source-revision 434a7e2. Packets built by scratchpad/build-l9-reconfirm7.py. Checkers at 434a7e2: index_category_check.py: Index rows: 177; labels: 176; manuscript labels at a284420: 879; problems: 0; index_check_pointer.py: 0 problems (pairs without a table row 0; bad []). Every finding below is verbatim from report.json.

Packets: p1 the pointer Index (177 rows, two checks), the Scope description and the FORMALIZATION wording; p2 the 25 changed section-table rows and the 13 rows flagged in round 6 that the agent judged correct (confirm or refute); p3 no new overclaim over the diff a723987..434a7e2 and classification consistency. Retry only on tool failure, recorded in the driver log.

## p1-pointer-index

Preflight: contract-check CONTRACT-OBSERVABLE (14 required field(s), 0 dispatch input(s); no provider call); dry run exit 0 (dryrun/); contract-check with --dispatch-input dryrun/prompt.txt CONTRACT-OBSERVABLE (14 required field(s), 1 dispatch input(s); no provider call)

Driver log:
```
2026-11-12T19:43:00Z start attempt-01
2026-11-12T19:47:26Z attempt-01 exit=2 Status: review-complete
2026-11-12T19:47:26Z done
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
Check verdicts: FAIL 2, PASS 1, PASS_WITH_NOTES 1 (of 4)

Checks not PASS/PASS_WITH_NOTES:
- POINTERS lines 512-600: FAIL: All 89 first cells are existing, uniquely located manuscript labels; all listed section categories match their headings. All section sets match if only the leading label in each table cell is counted. However, the contract requires label-column uses, not merely leading labels: line 564 omits ClockCopy and MaskedSpectralGrowth despite explicit 'also L:low-alpha-convolution' at candidate/statement-ledger.md:1266,4206-4208. Literal label-column searches also find unlisted sections for lines 525 and 536. The supplied checker's anchored extraction at tools/index_category_check.py:53-54 ignores these non-leading references.
- POINTERS lines 601-688: FAIL: All 87 manuscript labels exist uniquely, the single no-direct-label row matches its 71 sections, and every listed category matches its heading. Leading-label assignments match throughout. But line 667 omits FockForm, whose label column explicitly identifies E:fock-sandwich at candidate/statement-ledger.md:2322; line 686 omits HermiteWordFock, whose label column explicitly identifies E:finite-word-cutoff at :891. Literal label-column searches additionally expose omissions at lines 605 and 610. Thus the claimed exact section correspondence is false under the supplied contract.

Findings, fatal (0):

Findings, major (3):
- P1 — First-slice pointer omissions. candidate/statement-ledger.md:564 lists only L9Completed, LowAlphaConvolution and WaveGreenFourier. Yet the label column for Lean declarations SpectralHomog.SpectralHomogeneous and MaskedSpectralGrowth.map_smul_of_scaling/spectralHomogeneous_of_scaling/spectralHomogeneous_of_homog explicitly says 'also `L:low-alpha-convolution`' at :1266,4206-4208. The authoritative TeX labels that lemma at manuscript/notes/notes_stratonovich_ham_second_moment.tex:4702 and gives precisely the spectral-homogeneity step at :4719-4722. Fix: add `ClockCopy` (whole result) and `MaskedSpectralGrowth` (whole result) to Index row 564. The checker cannot establish the broader contract because tools/index_category_check.py:53-54 extracts only the first label.
- P2 — Second-slice pointer omissions. candidate/statement-ledger.md:2322 labels Lean FockForm.fock_form with '`E:fock-sandwich`, main TeX lines 2484-2488', but Index row :667 omits FockForm. The TeX explicitly labels the sandwich bound at manuscript/notes/notes_stratonovich_ham_second_moment.tex:2484-2488. Likewise, ledger :891 labels Lean HermiteWordFock.cut_eq_raw_fock with '`E:finite-word-cutoff` for the Fock model', but Index row :686 omits HermiteWordFock; the TeX labels the word equality at :2543-2550. Fix: add `FockForm` (narrower result) to row 667 and `HermiteWordFock` (narrower result) to row 686.
- P3 — Undisclosed leading-label-only mapping convention. The supplied contract says sections whose tables use a label 'in their label column'; candidate/statement-ledger.md:79-84 does not restrict that rule to the first backticked label. Exhaustive searches reveal further missing label/section pairs: L:temporal-equilibrium→WhiteRelativeWidth (:8699); H:homog→L9Completed, PhaseContractions, QuotientObstruction, SpectralMassIdentity (:3482,4947,5120,6718,6720); L:spatial-fourier-bound→SpatialSmoothRatio (:6400,6411); E:spatial-static-score→SpatialSmoothRatio (:6402). For example, Lean SpatialSmoothRatio.StaticControls is described as '`E:spatial-static-score` in existential form' at :6402, while the TeX labels that score at manuscript/notes/integrated_spatial_occupation.tex:50-53. Some other references are contextual hypotheses rather than result attributions. Fix: distinguish those contextual references from label assignments, moving them outside the label column where appropriate, and make every remaining label assignment participate in pointer generation and checking. Do not treat a first-label-only match as proof of the present contract.

Findings, minor (1):
- P4 — Audit-category wording. lean/FORMALIZATION.md:110-112 says the '`StratonovichHAMAudit` step modules are all of this kind' after defining category C. The ledger instead explicitly excepts HermiteWordFock at candidate/statement-ledger.md:76-78 and categorizes its Lean cut_eq_raw_fock as a narrower result at :853,891. The TeX permits multiple modes per color and Bochner integrals at manuscript/notes/notes_stratonovich_ham_second_moment.tex:2532-2538,2551-2552, explaining that exception. Because FORMALIZATION.md:82,84 already acknowledges it, this is a local wording issue. Suggested exact clarification: replace 'are all of this kind' with 'are of this kind except HermiteWordFock, a narrower result'.

Required repairs (3):
- Add the missing ClockCopy and MaskedSpectralGrowth pointers to L:low-alpha-convolution, with their whole-result heading categories.
- Add FockForm (narrower result) to E:fock-sandwich and HermiteWordFock (narrower result) to E:finite-word-cutoff.
- Resolve the label-column mapping discrepancy: separate contextual references from actual label assignments, include every actual assignment in the Index, and check non-leading assignments rather than extracting only the first label.

Limitations (4):
- Requirement A was completed. Full mathematical reading of the manuscript and all declaration statements was not required and was not performed; manuscript coverage outside the reported matches and contexts remains partial.
- The additional non-leading references include contextual hypotheses and explicitly no-direct-label annotations; these must not automatically be interpreted as formalizations merely because a label string occurs there.
- Proof correctness, build receipts, historical revision comparisons and provenance hashes were not independently verified.
- This AI review is neither human verification nor a novelty audit.

## p2-section-rows

Preflight: contract-check CONTRACT-OBSERVABLE (14 required field(s), 0 dispatch input(s); no provider call); dry run exit 0 (dryrun/); contract-check with --dispatch-input dryrun/prompt.txt CONTRACT-OBSERVABLE (14 required field(s), 1 dispatch input(s); no provider call)

Driver log:
```
2026-11-12T19:43:00Z start attempt-01
2026-11-12T19:50:34Z attempt-01 exit=0 Status: review-complete
2026-11-12T19:50:34Z done
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
Check verdicts: PASS 36, PASS_WITH_NOTES 2 (of 38)

Findings, fatal (0):

Findings, major (0):

Findings, minor (2):
- P1 — ConeConstants.step_Q notation: candidate/statement-ledger.md:3007 uses an unexplained shorthand 'q'. Lean spells this factor as 'K.Cg * Real.exp (-(K.ηg * t))' (lean/StratonovichHAMSecondMoment/IndexedCone.lean:337); the manuscript uses 'q_B' for its full-block specialization (manuscript/notes/integrated_raw_block_lower.tex:268,310). Optional exact clarification: write 'q(t) = C_gap exp(-eta_gap t)' in the row. The stated inequality and supplied inputs are otherwise correct.
- P2 — ClockCopy.degree_one specialization: candidate/statement-ledger.md:1334 correctly states 'SpectralHomogeneous mu 1' in its statement cell but uses the generic phrase 'SpectralHomogeneous mu alpha' in its inputs cell. Lean takes '(hI : SpectralHomogeneous μ 1)' (lean/StratonovichHAMSecondMoment/ClockCopy.lean:671), matching the manuscript's 'When alpha=1' specialization (manuscript/notes/notes_stratonovich_ham_second_moment.tex:7774-7776). Optional exact clarification: replace 'mu alpha' by 'mu 1' in that inputs cell.

Required repairs (0):

Limitations (4):
- Requirement A's selected rows, section/table headings, complete declaration statements, cited manuscript passages, prior reports and non-Index diff hunks were read. Files marked partial were not reviewed outside the recorded selections; these omissions are outside the required selections.
- Check 38's universal input-disclosure test was applied to ClockCopy, DampedNorms and SpectralHomog, as specified, not expanded to every module containing spectral-homogeneity notation.
- This is documentation-correspondence review, not proof verification, compilation, a complete pointer-Index audit, or independent authentication of provenance hashes. Mechanical checker outputs were not used as semantic evidence.
- An AI review is neither human verification nor a novelty audit.

## p3-diff-consistency

Preflight: contract-check CONTRACT-OBSERVABLE (14 required field(s), 0 dispatch input(s); no provider call); dry run exit 0 (dryrun/); contract-check with --dispatch-input dryrun/prompt.txt CONTRACT-OBSERVABLE (14 required field(s), 1 dispatch input(s); no provider call)

Driver log:
```
2026-11-12T19:43:00Z start attempt-01
2026-11-12T19:48:59Z attempt-01 exit=3 Status: review-complete
2026-11-12T19:48:59Z done
```
### attempt-01
```
# CLI review attempt

Status: review-complete

Scientific verdict: INCONCLUSIVE

Accepted: False

See receipt.json, input-manifest.json, prompt.txt, and retained transport.
```
Verdict: **INCONCLUSIVE**, confidence: **medium** (attempt-01)
Check verdicts: INCONCLUSIVE 1, PASS 1 (of 2)

Checks not PASS/PASS_WITH_NOTES:
- NO-NEW-OVERCLAIM: INCONCLUSIVE: A definite pointer-completeness defect is established: candidate/statement-ledger.md:2983 explicitly co-labels GroundFamily with P:compact-F-projection, P:compact-F-complement and P:compact-ground-family, but the complete Index at lines 506-688 contains only the first of these. The generator and both checkers extract only the initial label (tools/pointer_index.py:25-28; tools/index_category_check.py:53-54; tools/index_check_pointer.py:12-15,35), explaining their false-negative completeness checks. Scope lines 79-84 promise pointers for the labels used by section tables. However, diff lines 241-854 and most section-table rows corresponding to removed Index entries were not textually reviewed; requirement C therefore prevents a completed verdict on this compound claim.

Findings, fatal (0):

Findings, major (1):
- P1 — Missing co-label pointers. candidate/statement-ledger.md:2983 labels `StratonovichHAMSecondMoment.IndexedCone.GroundFamily` with `P:compact-F-projection`, `P:compact-F-complement`, and `P:compact-ground-family` as supplied outputs, but Index lines 506-688 omit the latter two labels entirely. The Lean declaration's supplied-output status is corroborated by lean/claims.yaml:2029-2031: 'Hypothesis structure of C16 outputs ... normalized complement ... positive margins.' The authoritative TeX contains `\label{P:compact-ground-family}` and `d_0:=\inf_I(\lambda_\sigma-\mu_\sigma)>0` (manuscript/notes/integrated_compact_mean_family.tex:34,48-52), and `\label{P:compact-F-complement}` with the normalized complement estimate (same file:338,344-347). Thus these are genuine explicit co-labels, not incidental references. Exact fix: add an Index row for each omitted label, both pointing to `IndexedCone` (narrower result); make the generator and both pointer checkers enumerate every explicit co-label in the first cell rather than only its initial label, and regenerate their outputs. This does not change the declaration or coverage-classification totals.

Findings, minor (0):

Required repairs (1):
- Add the missing P:compact-F-complement and P:compact-ground-family pointer rows to IndexedCone, correct explicit-co-label handling in the generator and both checkers, and regenerate the affected checker outputs.

Limitations (5):
- Complete-reading requirement A was not met: diffs/docs-a723987-434a7e2.diff:241-854 and most corresponding section-table rows remain textually unreviewed. NO-NEW-OVERCLAIM is therefore INCONCLUSIVE despite the verified mandatory repair.
- Whole-file machine parsing established counts and structural comparisons; it is not represented as complete semantic reading of the ledger or claims.
- Lean source files and elaborated types are not supplied in this packet. Selected declaration descriptions were compared with claims.yaml, not independently kernel-checked.
- PROVENANCE.json byte bindings were not independently verified.
- This AI review is neither human verification nor a novelty audit.

