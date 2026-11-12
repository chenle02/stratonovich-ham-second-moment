# Wave L9 re-review round 5 (every-cell Index rule, split rule extended): summary

Companion 350d191 (wave-l9/repair; round-4 repairs, docs only; reviewed commit e2c50b5), manuscript a284420; reviewer Codex gpt-6.1-sol, effort high, min-confidence high, --source-revision 350d191. Packets built by scratchpad/build-l9-reconfirm5.py. Mechanical checker at 350d191: cells checked: 402; problems: 0. Every finding below is verbatim from report.json.

Packets: h1 the three changed headings and the three coverage rows moved to weaker; h2 round-4 findings, register text, classification consistency, no new overclaim in e2c50b5..350d191, earlier repairs kept; i1-i5 the Index table in pieces of at most 81 rows with only the named Lean declarations (statements up to :=, original line numbers, module headers; every named helper present). Retry only on tool failure, recorded in the driver log.

## h1-changed-headings-moved-rows

Preflight: contract-check CONTRACT-OBSERVABLE (14 required field(s), 0 dispatch input(s); no provider call); dry run exit 0 (dryrun/); contract-check with --dispatch-input dryrun/prompt.txt CONTRACT-OBSERVABLE (14 required field(s), 1 dispatch input(s); no provider call)

Driver log:
```
2026-11-12T18:18:41Z start attempt-01
2026-11-12T18:23:21Z attempt-01 exit=0 Status: review-complete
2026-11-12T18:23:21Z done
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
Check verdicts: PASS 2, PASS_WITH_NOTES 2 (of 4)

Findings, fatal (0):

Findings, major (0):

Findings, minor (1):
- K1 — TypeContinuity prose: candidate/statement-ledger.md:7700 retains 'No conclusion is narrower than the TeX.' Lean explicitly takes '(mom : ℕ → ℝ → ℝ → ℝ)' (lean/StratonovichHAMSecondMoment/TypeContinuity.lean:1109,1144), while TeX defines rates through 'log E[u^(a)(T,x)^p]' (manuscript/notes/notes_stratonovich_ham_second_moment.tex:7508-7511). The revised heading and coverage clearly disclose this distinction, so this is nonblocking shorthand, not an undisclosed overclaim. Optional exact replacement: 'Every conclusion formula is proved for the abstract moment function; its identification with the solution moments is not formalized.'

Required repairs (0):

Limitations (4):
- Requirement A's specified selections were completely read; truncated required passages were reread. Partial-file entries omit unrelated sections, coverage rows, diff hunks or proof bodies, not required wrapper signatures or scope passages.
- Review covers exactly the four contracted checks, not all 402 Index cells or a package-wide recount. Mechanical category presence was accepted as permitted.
- No Lean compilation or proof-correctness audit was performed. Packet hashes and revision byte bindings were not independently authenticated.
- This AI correspondence review is not human verification or a novelty audit.

## h2-register-consistency-diff

Preflight: contract-check CONTRACT-OBSERVABLE (14 required field(s), 0 dispatch input(s); no provider call); dry run exit 0 (dryrun/); contract-check with --dispatch-input dryrun/prompt.txt CONTRACT-OBSERVABLE (14 required field(s), 1 dispatch input(s); no provider call)

Driver log:
```
2026-11-12T18:18:41Z start attempt-01
2026-11-12T18:25:32Z attempt-01 exit=3 Status: review-complete
2026-11-12T18:25:32Z done
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
Check verdicts: INCONCLUSIVE 3, FAIL 2 (of 5)

Checks not PASS/PASS_WITH_NOTES:
- ROUND4-FINDINGS: INCONCLUSIVE: The RadiusMeanAnchor and TypeContinuity reclassifications match their abstract Lean arguments (RadiusMeanAnchor.lean:458-469; TypeContinuity.lean:1106-1122,1141-1160), and the L8Completed heading contains the requested additions (candidate/statement-ledger.md:3553). However, the damped-norm heading still omits the general multiplier lower-bound limitation requested by h4b K4, and the final aggregate Index cell remains uncategorized (ledger:1909,907; findings K1 and K3). Exhaustive resolution of all prior findings was not established because required diff and committed-context reading remains incomplete.
- REGISTER-TEXT: FAIL: The three register descriptions consistently disclose M1 and its unproved surface-measure identification (ledger:80-95; README.md:107-118; FORMALIZATION.md:90-99), matching WaveGreen.lean:26-34,106-111. All three relevant sections name M1 (ledger:3648,3704,5045). But the whole-result Index cells at ledger:854,864,903 do not name M1, unlike :906. Thus the contracted requirement that dependent rows name the registered model is not consistently satisfied.
- CLASSIFICATION-CONSISTENCY: FAIL: Independent parsing reproduces COMPLETION's 25/18/0/30/3/144 = 220; library modules 27/0/31/18 plus 23 audit proof-step modules; headings 24/32/34; coverage classes 47/30/3, comprising 29 same-assumptions/full, 18 same-assumptions/weaker and 30 inputs-supplied/weaker. The declaration inventories reproduce 559/135, 943/199, 466/78 and 82/6, and 1303 labelled plus 1165 unlabelled declarations. All 48 conclusion_scope sentences have matching ASCII mirrors. The numerical disagreement is lean/coverage.yaml:2: it still says 1158 claims have no direct label, contradicting ledger:909-910 and README.md:449. Exhaustive semantic certification of every main-row correspondence was not completed.
- NO-NEW-OVERCLAIM: INCONCLUSIVE: Diff lines 1-365 and 930-1068 were read, but lines 366-929 and not every new-side passage in committed context were read. Therefore the universal hunk-by-hunk and every-declaration claim cannot be certified. The inspected repair also leaves an uncategorized aggregate cell visible in diff:969 and ledger:907, despite the every-cell assertion.
- L8-REPAIRS-KEPT: INCONCLUSIVE: The inspected Scope retains the integrability warning, continuous-F exception and TerminalWick added restriction (ledger:403-413); the single-word limitation remains in the heading at :1072; and the completed phase-contraction signatures remain three-dimensional (L9Completed.lean:150-184). Nevertheless, incomplete diff reading prevents certifying that no hunk weakens any listed earlier repair. The damped-norm heading limitation also remains incompletely stated, as detailed in K1.

Findings, fatal (0):

Findings, major (4):
- K1 — Unresolved DampedNormsHomog heading qualification. candidate/statement-ledger.md:1909 names only the missing covariance-smoothing identification, while :1940-1942 says the wave wrapper states the lemma except its smoothing remark. Lean explicitly says the general lower bounds are 'not conclusions here' (lean/StratonovichHAMSecondMoment/DampedNormsHomog.lean:667-668), and its comparison conclusion contains only upper inequalities (:686-692). TeX states '0\le N_{1,m,S}' and '0\le N_{2,m,S}^2' (manuscript/notes/notes_stratonovich_ham_second_moment.tex:838-839). Exact fix: add the absent general multiplier lower bounds to the DampedNormsHomog heading and qualify :1940-1942 accordingly, retaining the reference to their separate treatment in DampedMultiplier. This is the still-unresolved heading portion of prior h4b K4.
- K2 — Stale unlabelled-claim count. lean/coverage.yaml:2 says '1158 further claims', whereas the independently counted ledger has 1165 unlabelled and 1303 labelled declarations (candidate/statement-ledger.md:909-910). The seven reclassified integrability-transfer declarations are explicitly unlabelled at :549,7977,7986,7988,7990,7993,7997,8001. Lean calls them 'additional Lean-route statements, not steps of the TeX proof' (lean/StratonovichHAMSecondMoment/VariationalDilation.lean:60-62); TeX instead says 'Positive Tonelli applies this identity' (manuscript/notes/integrated_unmasked_variational.tex:249-250). Exact fix: replace 1158 by 1165 in the coverage header.
- K3 — The every-cell rule excludes an aggregate cell in practice. candidate/statement-ledger.md:907 has first cell 'no direct label' with no category. tools/index_category_check.py:63 explicitly skips this aggregate row, explaining why its output does not establish the universal claim. Its contents include Lean's synthetic '2*30^60 < 39^39*21^21' (lean/StratonovichHAMAudit/RawValueCeiling.lean:9), distinct from TeX's general logarithmic gap 'Delta ... > 0' (manuscript/notes/integrated_occupation_ceiling.tex:275-281). Exact fix: categorize the aggregate first cell as foundation/unlabelled audit facts, and remove the checker exemption or otherwise ensure this cell is included in the every-cell check.
- K4 — M1 is not named in all dependent whole-result Index cells. candidate/statement-ledger.md:854,864,903 retain whole-result classifications without naming M1, although :906 does name it. Lean defines the three-dimensional measure using 'volume.toSphere.map' (lean/StratonovichHAMSecondMoment/WaveGreen.lean:110-111) and disclaims its surface-measure identification (:26-34); TeX specifies 'sigma_h is surface measure' (manuscript/notes/notes_stratonovich_ham_second_moment.tex:5184-5186). Exact fix: explicitly name registered model choice M1 in those dependent whole-result cells and corresponding full-result detail rows, preserving their dimensions and supplied-input qualifications. No mathematical reclassification is required merely because M1 is used.

Findings, minor (0):

Required repairs (4):
- K1: Complete the DampedNormsHomog heading and wave-wrapper summary with the missing general multiplier lower-bound limitation.
- K2: Correct the coverage.yaml header's unlabelled-claim count to 1165.
- K3: Categorize the final aggregate Index cell and include it in enforcement of the every-cell rule.
- K4: Name M1 explicitly in the dependent whole-result Index cells and corresponding full-result detail rows.

Limitations (6):
- Requirement A was not completed: diff lines 366-929 were not read, and not every diff hunk's committed passage was read in context. The affected universal checks are consequently INCONCLUSIVE.
- The entire Index was not semantically checked declaration by declaration against Lean and authoritative TeX. The findings are established counterexamples, not an exhaustive defect list.
- Counts and ASCII-mirror equality were independently parsed across complete files; such parsing is not complete semantic reading or verification of every category qualifier.
- The three moved wrapper signatures were read completely, but their proof bodies and all upstream constructions were not audited.
- No proof checking, compilation, network access, file modification, delegation or provenance-hash authentication was performed.
- This AI correspondence review is not human verification or a novelty audit.

## i1-index-505-585

Preflight: contract-check CONTRACT-OBSERVABLE (14 required field(s), 0 dispatch input(s); no provider call); dry run exit 0 (dryrun/); contract-check with --dispatch-input dryrun/prompt.txt CONTRACT-OBSERVABLE (14 required field(s), 1 dispatch input(s); no provider call)

Driver log:
```
2026-11-12T18:18:41Z start attempt-01
2026-11-12T18:24:46Z attempt-01 exit=2 Status: review-complete
2026-11-12T18:24:46Z done
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
Check verdicts: FAIL 1, PASS 1 (of 2)

Checks not PASS/PASS_WITH_NOTES:
- INDEX-CELLS lines 505-585: FAIL: Line 542 remains a mixed input-status row: its qualifier 'whole result; no supplied input via masked_trig_products_completed_paper' covers the concrete completion theorem, abstract wrappers retaining supplied inputs, and input-free helpers. MaskedTrigProducts.lean.excerpt.txt:262-265 explicitly retains hmem and hmod; MaskedModulation.lean.excerpt.txt:166-169 retains hmem and hnorm. Only the concrete theorem in TimeCompletion.lean.excerpt.txt:117-129 has neither. Completion elsewhere does not make that qualifier true of every listed declaration. Other reviewed classifications, including the abstract-path and ground-family restrictions, agree with the registered split rule.

Findings, fatal (0):

Findings, major (1):
- K1 — Mixed input-status classification at candidate/statement-ledger.md:542. The cell says 'whole result; no supplied input via masked_trig_products_completed_paper', but includes abstract declarations with explicit supplied inputs: '(hmem : ∀ ω ... ∈ V)' and '(hmod : ∀ ω ... ≤ ...)' in lean-excerpts/StratonovichHAMSecondMoment/MaskedTrigProducts.lean.excerpt.txt:262-265 (original Lean:347-350), and '(hnorm : ∀ f : V ...)' in lean-excerpts/StratonovichHAMSecondMoment/MaskedModulation.lean.excerpt.txt:166-169 (original Lean:1120-1123). The TeX fixes the actual completion norm—'Norms below are those of the complexified temporal completion'—at manuscript/notes/integrated_covariance_foundation.tex:296-298 and states the bound at :347-360. The concrete completed theorem does prove this without supplied inputs (lean-excerpts/StratonovichHAMSecondMoment/TimeCompletion.lean.excerpt.txt:117-129), so the aggregate mathematical result is not disputed. Nevertheless, 'via' does not remove the abstract declarations' binders, and the row violates the binding every-declaration qualifier rule. Exact fix: split line 542, retaining 'whole result; no supplied input' only for TimeCompletion.masked_trig_products_completed_paper; classify the abstract reductions and remaining helpers as proof steps, explicitly distinguishing hmem/hmod, hmem/hnorm, and input-free helpers.

Findings, minor (0):

Required repairs (1):
- Split candidate/statement-ledger.md:542 so the input-free whole-result qualifier applies only to TimeCompletion.masked_trig_products_completed_paper; put the abstract reductions and helpers in appropriately qualified proof-step rows.

Limitations (4):
- All material required by complete-reading requirement A was read completely. Unread portions of the partial ledger and manuscript files lie outside the selected ranges and heading list.
- The review concerns documentation correspondence for Index lines 505-585, not other Index rows or package-wide counts.
- Lean ground truth was reviewed through the supplied frozen excerpts; compilation and proof correctness were not audited.
- This AI review is neither human verification nor a novelty audit.

## i2-index-586-666

Preflight: contract-check CONTRACT-OBSERVABLE (14 required field(s), 0 dispatch input(s); no provider call); dry run exit 0 (dryrun/); contract-check with --dispatch-input dryrun/prompt.txt CONTRACT-OBSERVABLE (14 required field(s), 1 dispatch input(s); no provider call)

Driver log:
```
2026-11-12T18:18:41Z start attempt-01
2026-11-12T18:25:13Z attempt-01 exit=2 Status: review-complete
2026-11-12T18:25:13Z done
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
Check verdicts: FAIL 2 (of 2)

Checks not PASS/PASS_WITH_NOTES:
- INDEX-CELLS lines 586-666: FAIL: The repaired completed-wave row 614 correctly separates the input-free theorem from the abstract wrapper at 615, and the quotient-obstruction restriction at 646 correctly follows the split rule. Nevertheless, row 594 assigns whole-result status to definitions alone; other whole-result cells still mix complete results with proof-only declarations. Several automatically assigned narrower-result references identify an unrelated omission rather than the limitation of their declarations. See K1-K3, against the rules at candidate/statement-ledger.md:62-95.
- INDEX-MAPPING lines 586-666: FAIL: Row 633 includes variational_global_mean_lipschitz_paper under L:variational-global-mean while expressly acknowledging that it is not a TeX statement. The joint space-time Lipschitz conclusion is neither the displayed time-only bound nor a statement made in that lemma's proof (manuscript/notes/integrated_unmasked_variational.tex:64-96). Under the contract's statement-or-proof containment rule, this complement needs a separate no-direct-label row. See K4.

Findings, fatal (0):

Findings, major (4):
- K1 — Row 594 incorrectly says 'L:masked-time-completion (whole result: the form and its kernel)'. Lean supplies only 'def kern ... := |x| ^ (-a)' and 'def timeForm ... := ∫ ...' (lean-excerpts/StratonovichHAMSecondMoment/TimeSchur.lean.excerpt.txt:57-59,146-147; original Lean lines 57-59,298-299). TeX additionally asserts 'positive semidefinite', a separable null-quotient completion, continuous extension, and interval-amplitude membership (manuscript/notes/integrated_covariance_foundation.tex:147-155). Definitions do not conclude these assertions. Exact fix: change this cell to 'proof steps: definitions of the temporal form and kernel only'; retain whole-result status for the completed theorem at row 610.
- K2 — Whole-result cells still contain proof-only declarations, contrary to the every-declaration split requirement. For example, row 596 includes FrequencyRow.frequencyPair_le_two, whose entire conclusion is 'frequencyPair a h r ρ ≤ 2' (lean-excerpts/StratonovichHAMSecondMoment/FrequencyRow.lean.excerpt.txt:121-124), whereas P:frequency-row concludes 'sup J_h ≤ K C B_alpha(h)' (manuscript/notes/integrated_wave_variance.tex:47-54). Row 637 includes IsOrthonormalL2 and separate one-direction Bessel theorems; phase_bessel concludes only the unconjugated inequality (lean-excerpts/StratonovichHAMSecondMoment/PhaseBessel.lean.excerpt.txt:129-133), while TeX also requires 'the same bound ... with conjugate u' (manuscript/notes/integrated_wave_variance.tex:346-355). Row 631 similarly includes heat_envelope explicitly 'without its positivity clause' (lean-excerpts/StratonovichHAMSecondMoment/VariationalMean.lean.excerpt.txt:147-158), although TeX says 'The value at zero is strictly positive' (manuscript/notes/integrated_unmasked_variational.tex:34). Analogous mixed full-result/supporting-declaration groupings occur at rows 593, 595, 597, 603, 605, 610 and 611. Exact fix: split complete-result declarations from definitions, constituent clauses and proof helpers, placing the latter in accurately scoped proof-steps/foundation cells; do not transfer a wrapper's whole-result category to every supporting declaration.
- K3 — Rows 621, 632 and 635 refer to omissions unrelated to their own declarations. At 621, mu_closedBall_le concludes 'μ (closedBall y r) ≤ ... CGamma Γ * r ^ alpha' (lean-excerpts/StratonovichHAMSecondMoment/MaskedAuxiliaryNorm.lean.excerpt.txt:315-319); its restriction is to the closed-ball mass portion of E:masked-translated-ball (manuscript/notes/integrated_covariance_foundation.tex:46-51), not the real-H complexification omission named by section MaskedAuxiliaryNorm. At 632, heat_identity concludes only the Fourier identity (lean-excerpts/StratonovichHAMSecondMoment/VariationalMean.lean.excerpt.txt:137-144); E:variational-heat-envelope also contains the nonnegative upper bound and finiteness (manuscript/notes/integrated_unmasked_variational.tex:27-33), unrelated to the section heading's missing mixed derivatives. At 635, the conclusion is merely 'IsRayleighTrial ... ↔ MemLp ... ∧ HasWeakGradient ... ∧ ∫ f² = 1' (same excerpt:443-448), not the rate identity 'lambda² = sup ...' (same TeX file:104-108). Exact fix: classify these as proof steps respectively describing the closed-ball bound, the heat spectral integrand/identity only, and the Rayleigh admissibility side-condition equivalence; remove the irrelevant narrower-result section references.
- K4 — Row 633 mixes a manuscript result with an additional consequence not stated there. Lean explicitly calls variational_global_mean_lipschitz_paper 'a first-order complement ... (not a TeX statement)' and concludes a bound involving arbitrary x and x' (lean-excerpts/StratonovichHAMSecondMoment/VariationalMean.lean.excerpt.txt:428-436). TeX states '||h_s-h_t||_infinity ≤ C_Psi |s-t|' and its proof discusses bounded derivatives and the time Lipschitz estimate, not the joint metric inequality (manuscript/notes/integrated_unmasked_variational.tex:64-96). The joint inequality is a valid consequence of bounded first derivatives, but implication is not statement-or-proof containment. Exact fix: move this declaration to a separate 'no direct label (foundation: first-order joint-Lipschitz complement to L:variational-global-mean)' row, retaining its explanatory cross-reference.

Findings, minor (0):

Required repairs (4):
- Reclassify row 594 as definitions/proof steps, not a whole temporal-completion result.
- Split the mixed whole-result cells identified in K2 so every declaration receives a category appropriate to its own scope.
- Replace the misleading narrower-result references at rows 621, 632 and 635 with the declaration-specific proof-step descriptions in K3.
- Separate variational_global_mean_lipschitz_paper from row 633 and give it the no-direct-label foundation mapping specified in K4.

Limitations (4):
- Requirement A was completed. Partial coverage entries concern additional context sources, not gaps in mandatory reading.
- Unlisted portions of the ledger and manuscript were not reviewed; conclusions concern the specified 81 Index rows.
- Lean ground truth was the supplied excerpts, including their marked omissions. Proof correctness and compilation were outside this review.
- This AI review is neither human verification nor a novelty audit.

## i3-index-667-747

Preflight: contract-check CONTRACT-OBSERVABLE (14 required field(s), 0 dispatch input(s); no provider call); dry run exit 0 (dryrun/); contract-check with --dispatch-input dryrun/prompt.txt CONTRACT-OBSERVABLE (14 required field(s), 1 dispatch input(s); no provider call)

Driver log:
```
2026-11-12T18:18:41Z start attempt-01
2026-11-12T18:24:40Z attempt-01 exit=2 Status: review-complete
2026-11-12T18:24:40Z done
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
Check verdicts: FAIL 1, PASS 1 (of 2)

Checks not PASS/PASS_WITH_NOTES:
- INDEX-CELLS lines 667-747: FAIL: The required reading is complete. The narrower classifications for the abstract moment and terminal-series families respect the split rule, but several first-cell qualifiers remain incorrect: line 742 denies inputs actually present in its helpers; line 717 applies the L2/TerminalWickInput description to arbitrary-Hilbert-space general forms; lines 735-736 omit an essential sign condition, and line 736 abbreviates away the occupation-energy multiplier. See K1-K3.

Findings, fatal (0):

Findings, major (3):
- K1 — False input-free qualifier at candidate/statement-ledger.md:742. The cell says its scalar helpers 'take no input' and assigns supplied inputs only to subsequent rows. However, IntervalScalar.lean.excerpt.txt, original Lean lines 202-207, requires hY, hodd and hfirst for static_interaction_assembly; lines 346-351 require hborn and hmean for first_coefficient_le; lines 566-567 require the per-block hypothesis hstep for independent_blocks_scalar. These are precisely the order/parity/variance and iteration facts used in manuscript/notes/notes_stratonovich_ham_second_moment.tex:2737-2752,2788-2793, not consequences established by these helpers. Fix: split the input-free definitions/scalar estimates from these conditional helpers, and explicitly disclose the latter's order, parity, first-variance and per-block premises. Do not retain 'take no input' over the mixed row.
- K2 — Mixed scope and input packaging at candidate/statement-ledger.md:717. The cell describes all four declarations as an abstract 'L^2 family' with the two facts 'supplied as TerminalWickInput'. Only the paper wrappers take that structure: UniformSeriesTail.lean.excerpt.txt, original Lean lines 261-267,301-307, contain hTW. The general forms instead quantify over an arbitrary index/filter and real inner-product space, with eventual hypotheses hsum and hpos (original Lean lines 164-169,195-200). The TeX states positive regularization pairs and L2 terminal terms (manuscript/notes/notes_stratonovich_ham_second_moment.tex:3704-3714), and cites the two facts in its proof at 3730-3731. Fix: separate the paper wrappers from the arbitrary-Hilbert-space/filter general forms; identify TerminalWickInput only for the wrappers and disclose the general forms' eventual summability/nonnegative-inner-product hypotheses.
- K3 — Incomplete general-bound qualifiers at candidate/statement-ledger.md:735-736. 'Any constant R with SquarePairingBounds' omits the explicit hypothesis 'hR : 0 ≤ R' in OccupationPhysicalClass.lean.excerpt.txt, original Lean lines 378-380,530-532,743-746. This is not implied by the predicate in general: its homogeneous field uses ENNReal.ofReal (R * Nnorm ... ^ 4) (original Lean lines 133-139), so Gamma = 0 permits negative R, whereas the advertised real physical bound would then have a negative right side. Additionally, line 736 says 'bound spEnergyVal alpha R'; the actual conclusion is 'EstarO ... ≤ Rstar a D ^ (2 / (2 - alpha)) * spEnergyVal alpha R' (original Lean lines 747-749). The TeX retains this multiplier in manuscript/notes/integrated_spatial_occupation.tex:399-402. Fix: state R ≥ 0 explicitly in both general-form cells and give the complete energy bound, including Rstar^(2/(2-alpha)); distinguish the parameter-free energy definitions from the conditional theorem.

Findings, minor (0):

Required repairs (3):
- Repair line 742 by separating input-free declarations from conditional helpers and disclosing the latter's supplied premises.
- Split line 717's paper wrappers from its arbitrary-Hilbert-space/filter general forms and accurately describe their different input packaging and quantifiers.
- Correct lines 735-736 to require R ≥ 0 and state the full occupation-energy bound with its Rstar multiplier.

Limitations (4):
- All selections required by requirement A were read completely; unselected portions of larger documentation and manuscript files were not reviewed.
- Lean citations in findings use original line numbers printed inside the excerpts; source_coverage uses packet-file line numbers.
- This is a documentation-correspondence review, not proof checking, human verification, or a novelty audit. Omitted Lean bodies and completion-module implementations were not independently kernel-verified.
- The mechanical category-presence check was accepted as supplied, not rerun.

## i4-index-748-828

Preflight: contract-check CONTRACT-OBSERVABLE (14 required field(s), 0 dispatch input(s); no provider call); dry run exit 0 (dryrun/); contract-check with --dispatch-input dryrun/prompt.txt CONTRACT-OBSERVABLE (14 required field(s), 1 dispatch input(s); no provider call)

Driver log:
```
2026-11-12T18:18:41Z start attempt-01
2026-11-12T18:25:36Z attempt-01 exit=2 Status: review-complete
2026-11-12T18:25:36Z done
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
Check verdicts: FAIL 2 (of 2)

Checks not PASS/PASS_WITH_NOTES:
- INDEX-CELLS lines 748-828: FAIL: Required reading A is complete. The whole-result classification at candidate/statement-ledger.md:766 agrees with lean/coverage.yaml:824-843 and the Fourier-bound statement. Several repairs correctly separate supplied-input helpers, including cells 757, 759, 770 and 822. Nevertheless, cell 756 applies a positive-noise restriction to a general theorem lacking that restriction; cells 760-763 classify fully proved physical displays as narrower using unrelated module-level omissions; and cell 817 mixes definitions and theorems with different measurability and mass assumptions. These violate the every-declaration qualifier rule.
- INDEX-MAPPING lines 748-828: FAIL: Cell 767 correctly maps ralpha to E:intro-spectral-mass, but also maps hRdef_iff_resolvent and hRdef_iff_resolvent_paper there. manuscript/notes/notes_stratonovich_ham_second_moment.tex:530-532 only defines R_alpha; it contains neither the resolvent identity nor these interface equivalences. The requisite identity instead appears in manuscript/notes/integrated_spatial_occupation.tex:149-155. The bridge declarations should have a separate auxiliary mapping.

Findings, fatal (0):

Findings, major (4):
- K1 — Cell 756 has a mixed positive-noise qualifier. candidate/statement-ledger.md:756 says 'positive noise only' for both completed assembly declarations. Lean's general interval_coefficient_assembly_completed assumes 'hR : 0 ≤ R' and 'σ i ^ 2 ≤ c * h i ^ (-alpha0)', without σ_i > 0 (lean-excerpts/StratonovichHAMSecondMoment/IntervalScalarCompleted.lean.excerpt.txt:127-141, original Lean 140-154). Only the paper wrapper carries '_hRpos : 0 < R' and '_hσpos : ∀ i, 0 < σ i' (same excerpt:157-175). TeX explicitly performs the reduction: 'Zero noise is trivial; omit any zero σ_i' and 'Thus, we may assume σ_i > 0' (manuscript/notes/notes_stratonovich_ham_second_moment.tex:3417-3423). Fix: split the cell into a general proof-step row, disclosing hsplits and hfixed, and a narrower paper-wrapper row retaining the positive-noise and unformalized-identification qualifications.
- K2 — Cells 760-763 import narrowing that their declarations do not have. Cell 760 expressly cites missing 'rate and cost and class O identifications'; cells 761-763 refer to the same qualified section. These objects do not occur in the physical square-pairing, homogeneous-bound, four-linear-bound or spatial-energy-map statements. Lean proves, for example, '0 ≤ ...pairing... ≤ Real.sqrt (...)' under HomogCovariance, Γ ≠ 0 and H¹-pair hypotheses (lean-excerpts/StratonovichHAMSecondMoment/SpatialOccupationL7Completed.lean.excerpt.txt:124-131), exactly the TeX display '0 ≤ B_Gamma(f²,h²) ≤ sqrt(A_sp(f)A_sp(h))' (manuscript/notes/integrated_spatial_occupation.tex:225-227). Likewise the energy theorem concludes 'Esp Γ = energyValue alpha (Rsp Γ alpha) ∧ 0 < Esp Γ' (original Lean 273-276), matching TeX:309-314. No rate, cost or occupation-class identification is needed for these displays. Fix: classify cells 760-763 as 'proof steps: the display in full, nothing supplied; enclosing result/module remains narrower', rather than asserting a nonexistent narrowing of each display.
- K3 — Cell 817 still combines incompatible input scopes. Its blanket qualifications include 'chain measures specified by their masses, hmeas supplied', but prodL2 is a definition depending only on the Gaussian-field evidence and a tuple (lean-excerpts/StratonovichHAMSecondMoment/TerminalWick.lean.excerpt.txt:158-161). pairing_integral_nonneg assumes covariance nonnegativity, not hmeas or prescribed masses (same excerpt:289-293), while summable_norm_smul_chainIntegral assumes hmass but not hmeas (same excerpt:311-314). Other listed mixed-moment theorems require hmeas but not prescribed masses. TeX distinguishes the field-product definition, mass calculation and measurability argument: 'Y_n ... = integral product W ... g_n', 'M_n(T) = T^(2n)/(2n)!', and 'the product is strongly measurable in L²' (manuscript/notes/notes_stratonovich_ham_second_moment.tex:3607-3608, 3648-3659). Fix: split definitions into foundation rows and separate the theorem groups by their actual mass and measurability inputs; retain the full real-r, mixed-moment, missing-chain-construction and added-hK qualifications on the appropriate narrower wrappers.
- K4 — Cell 767 misattributes the resolvent-interface bridges. Lean states 'R = alpha * π * ... / (...) ↔ R = resolvent μ 1' (lean-excerpts/StratonovichHAMSecondMoment/SpectralMassIdentity.lean.excerpt.txt:145-159). E:intro-spectral-mass states only 'R_alpha = alpha π μ(B_1)/(2 sin(πα/2))' (manuscript/notes/notes_stratonovich_ham_second_moment.tex:530-532). The additional identity 'R_Gamma(q) = q^(alpha-2) R_alpha' belongs to the proof of L:spatial-fourier-bound (manuscript/notes/integrated_spatial_occupation.tex:149-155), not to a proof attached to E:intro-spectral-mass. Fix: keep ralpha under E:intro-spectral-mass and move both hRdef_iff_resolvent declarations to 'no direct label (foundation: Lean-interface equivalences)', with cross-references to the definition and resolvent calculation.

Findings, minor (0):

Required repairs (4):
- K1: Split cell 756 so the positive-noise qualification applies only to the paper wrapper.
- K2: Reclassify cells 760-763 as complete-display proof steps within the narrower module, removing unrelated narrowing explanations.
- K3: Split cell 817 by declaration role and actual mass/measurability assumptions.
- K4: Separate the two resolvent-interface bridges from the E:intro-spectral-mass definition mapping.

Limitations (4):
- All mandatory reading-A portions were completed; partial-file coverage above concerns additional contextual sources or material outside those required portions.
- Full Lean types for externally referenced completion declarations, including the WaveGreenFourier wrapper and L8Completed discharges, are not supplied among these excerpts; those references have documentary rather than independent type-level corroboration here.
- Proof correctness, package-wide counts and Index rows outside lines 748-828 were not audited.
- This AI correspondence review is neither human verification nor a novelty audit.

## i5-index-829-907

Preflight: contract-check CONTRACT-OBSERVABLE (14 required field(s), 0 dispatch input(s); no provider call); dry run exit 0 (dryrun/); contract-check with --dispatch-input dryrun/prompt.txt CONTRACT-OBSERVABLE (14 required field(s), 1 dispatch input(s); no provider call)

Driver log:
```
2026-11-12T18:18:41Z start attempt-01
2026-11-12T18:24:21Z attempt-01 exit=2 Status: review-complete
2026-11-12T18:24:21Z done
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
Check verdicts: FAIL 1, PASS 1 (of 2)

Checks not PASS/PASS_WITH_NOTES:
- INDEX-CELLS lines 829-907: FAIL: Two residual per-declaration classification problems remain: line 876 applies the qualifier 'both forms' to a theorem proving only the individual-control inequality, and line 900 classifies degree-support hypotheses and proof steps as a narrower labelled result. See K1-K2. The M1 exception itself is correctly applicable: the relevant sections explicitly name the model at candidate/statement-ledger.md:3648,3704,5045, and the completed Lean statements retain the required conclusions.

Findings, fatal (0):

Findings, major (2):
- K1 — Mixed scope at candidate/statement-ledger.md:876. The cell says 'both forms of E:occupation-score-ceiling' for both listed declarations. However, lean-excerpts/StratonovichHAMSecondMoment/OccupationCeilingExact.lean.excerpt.txt:225-229 (original Lean lines 699-703) concludes only 'c * integratedRate ... - rawCost ... / 2 ≤ SpatialBracket.ceilingValue ...'. It contains neither the supremum conclusion nor the occupation-energy identity. Those appear in intrinsic_occupation_ceiling_paper, original Lean lines 748-757. The TeX explicitly distinguishes the supremum inequality and energy form at manuscript/notes/integrated_occupation_ceiling.tex:209-215, with the individual-control argument at :235-245. Fix: split the row; classify score_le_ceiling_Cocc as proof steps establishing the individual-control ceiling only, retaining the model/identification disclaimers, and reserve 'both forms' for intrinsic_occupation_ceiling_paper.
- K2 — Wrong result category at candidate/statement-ledger.md:900. This row contains the hypotheses and supporting definitions of the finite-word proof, not a narrower instance of its conclusion. lean-excerpts/StratonovichHAMSecondMoment/FockForm.lean.excerpt.txt:338-371 (original Lean lines 495-537) defines GoodDeg and truncC and proves statements such as 'GoodDeg ... (vac ... u)' and 'truncC Nc v = v' under a degree-bound hypothesis. The TeX places precisely these degree-preservation and cutoff-fixing steps in the proof at manuscript/notes/notes_stratonovich_ham_second_moment.tex:2556-2565; the labelled conclusion is the word equality at :2543-2548. Its actual one-mode formalization is cut_eq_raw_fock, separately indexed at ledger line 902. Fix: change line 900 to 'proof steps: degree-support definitions and hypotheses of the finite-word induction, one mode per color; nothing supplied', preserving its label and section reference.

Findings, minor (0):

Required repairs (2):
- Split ledger line 876 so that 'both forms' applies only to intrinsic_occupation_ceiling_paper; describe score_le_ceiling_Cocc as the individual-control proof step.
- Reclassify ledger line 900 as proof steps rather than a narrower labelled result.

Limitations (4):
- All mandatory reading in requirement A was completed. Partial-file entries identify portions outside the required scope, not unread gaps in the required excerpts or Index slice.
- The remaining ledger rows, package-wide counts, provenance hashes, and proof correctness were not independently audited.
- Lean citations in findings distinguish physical excerpt lines from the original Lean numbering embedded in those excerpts. Material omitted from the supplied excerpts was not reconstructed.
- This AI review is neither human verification nor a novelty audit.

