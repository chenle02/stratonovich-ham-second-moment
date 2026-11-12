# Wave L9 re-review round 6 (Index regenerated per declaration): summary

Companion a723987 (wave-l9/repair; round-5 repairs, Index regenerated per declaration, docs only; reviewed commit 350d191), manuscript a284420; reviewer Codex gpt-6.1-sol, effort high, min-confidence high, --source-revision a723987. Packets built by scratchpad/build-l9-reconfirm6.py. Mechanical checker at a723987: cells checked: 657; problems: 0. Every finding below is verbatim from report.json.

Packets: i1-i8 the Index table (657 rows) in pieces of at most 83 rows with every named Lean declaration (statements, original line numbers, module headers); h2a/h2b the round-5 findings (i1-i3; h1, h2, i4, i5) and NO-NEW-OVERCLAIM over the two halves of the ledger diff 350d191..a723987 (h2b also the other files); h3 classification consistency of counts and L8 repairs kept. Retry only on tool failure, recorded in the driver log.

## h2a-r5-findings-diff-first-half

Preflight: contract-check CONTRACT-OBSERVABLE (14 required field(s), 0 dispatch input(s); no provider call); dry run exit 0 (dryrun/); contract-check with --dispatch-input dryrun/prompt.txt CONTRACT-OBSERVABLE (14 required field(s), 1 dispatch input(s); no provider call)

Driver log:
```
2026-11-12T18:36:49Z start attempt-01
2026-11-12T18:45:27Z attempt-01 exit=3 Status: review-complete
2026-11-12T18:45:27Z done
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
Check verdicts: PASS 8, INCONCLUSIVE 1 (of 9)

Checks not PASS/PASS_WITH_NOTES:
- NO-NEW-OVERCLAIM-HALF: INCONCLUSIVE: The complete diff was read, and confirmed counterexamples remain in its changed rows: GaussianIBP's integration-by-parts helper is classified as the whole matrix proposition (diffs/ledger-half.diff:147; ledger:622); a resolvent proof-step theorem is classified as the whole spatial-energy lemma (:590; ledger:941); and individual lower-bound helpers retain the qualifier 'both bounds' (:606; ledger:950). See K1-K3. However, the required declaration-by-declaration and coverage-row reading for every changed row was not completed, so this check is INCONCLUSIVE under requirement A rather than an exhaustive verdict.

Findings, fatal (0):

Findings, major (3):
- K1 — Whole-result classification still covers an integration-by-parts helper. candidate/statement-ledger.md:622, introduced in diffs/ledger-half.diff:147, classifies GaussianIBP.integral_coord_mul_eq_of_growth_paper as 'P:finite-gaussian-matrix (whole result)'. Its conclusion is integrability and '∫ ω, g k ω * f ... ∂P = ∫ ω, f′ ... ∂P' (lean/StratonovichHAMSecondMoment/GaussianIBP.lean:306-315), not either matrix-moment inequality. The TeX proposition states the Schatten average and maximum bounds (manuscript/notes/integrated_compact_gaussian.tex:98-118); integration by parts occurs only in its proof at :123-126. Exact fix: remove this declaration from the whole-result row and give it a separate 'P:finite-gaussian-matrix (proof steps: Gaussian integration by parts on the original probability space)' row. Retain whole-result status only for declarations actually concluding the proposition.
- K2 — The regenerated spatial-Fourier whole-result row still contains a proof-only wrapper. candidate/statement-ledger.md:941 and diffs/ledger-half.diff:590 include SpectralMassIdentity.resolvent_eq_ralpha_paper under 'L:spatial-fourier-bound (whole result ...)'. Lean concludes 'resolvent μ 1 = ralpha μ alpha' and the general resolvent identity (lean/StratonovichHAMSecondMoment/SpectralMassIdentity.lean:228-232), whereas the labelled lemma concludes 'b > 0' and '0 ≤ A_sp(g) ≤ 2^(1+alpha) R_alpha b^(alpha/2)' (manuscript/notes/integrated_spatial_occupation.tex:101-111). The resolvent identity occurs only in its proof at :149-155. Exact fix: retain spatial_fourier_bound_ralpha_paper in the whole-result row and move resolvent_eq_ralpha_paper to a separate proof-step row explicitly identifying that resolvent calculation.
- K3 — A changed comparison row still has a false every-declaration qualifier. candidate/statement-ledger.md:950 and diffs/ledger-half.diff:606 describe damped_multiplier_comparison, N1on_nonneg and N2onSq_nonneg together as 'both bounds'. The latter declarations conclude only '0 ≤ N1on ...' and '0 ≤ N2onSq ...' respectively (lean/StratonovichHAMSecondMoment/DampedMultiplier.lean:146-147,159-162); only the assembly concludes both lower and upper comparisons (:175-184). TeX E:damped-multiplier-comparison contains both two-sided inequalities (manuscript/notes/notes_stratonovich_ham_second_moment.tex:836-841). Exact fix: separate the general comparison assembly from the two individual lower-bound helpers, classify those helpers as proof steps naming their respective inequality, and remove 'both bounds' from their cells.

Findings, minor (0):

Required repairs (3):
- Split candidate/statement-ledger.md:622 so GaussianIBP.integral_coord_mul_eq_of_growth_paper is classified as an integration-by-parts proof step, not the whole matrix proposition.
- Split candidate/statement-ledger.md:941 so SpectralMassIdentity.resolvent_eq_ralpha_paper is classified as the resolvent proof step, not the whole spatial-Fourier lemma.
- Split and accurately scope candidate/statement-ledger.md:950; individual nonnegativity helpers must not inherit the 'both bounds' qualifier.

Limitations (5):
- Requirement A is incomplete for NO-NEW-OVERCLAIM-HALF: although all prior reports, adjudication, diff hunks, supplied TeX excerpts and checker output were read, Lean statements and coverage rows for every changed Index row were not all read. Unread modules and partially read sources are explicitly identified in source_coverage.
- The overall INCONCLUSIVE verdict reflects this mandatory coverage gap; it does not retract the three confirmed material documentation defects or permit acceptance without their repair.
- The eight finding-specific checks address the specified repairs, not the correctness of unrelated rows in those modules.
- Package-wide declaration counts and PROVENANCE byte bindings were not independently verified. The checker was inspected but not executed; its suffix-based wrapper classification does not establish semantic completeness.
- Proof correctness and compilation were outside scope. This AI review is neither human verification nor a novelty audit.

## h2b-r5-findings-diff-second-half

Preflight: contract-check CONTRACT-OBSERVABLE (14 required field(s), 0 dispatch input(s); no provider call); dry run exit 0 (dryrun/); contract-check with --dispatch-input dryrun/prompt.txt CONTRACT-OBSERVABLE (14 required field(s), 1 dispatch input(s); no provider call)

Driver log:
```
2026-11-12T18:36:49Z start attempt-01
2026-11-12T18:45:24Z attempt-01 exit=3 Status: review-complete
2026-11-12T18:45:24Z done
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
Check verdicts: PASS 10, FAIL 1, INCONCLUSIVE 1 (of 12)

Checks not PASS/PASS_WITH_NOTES:
- i4-K3: FAIL: Definitions and several input groups were correctly separated, but the split remains semantically incorrect. Ledger:1022 puts mixed_moment_mono in a 'no named analytic input' row despite its supplied hmeas₁ and hmeas₂ (TerminalWick.lean:523-530). Ledger:1026 repeats that false qualifier over terminal_wick_mono_paper, whose measurability inputs are explicit at :679-680, and retains irrelevant real-r/Wick-formula qualifications. See K1.
- NO-NEW-OVERCLAIM-HALF: INCONCLUSIVE: Both diffs were completely read, but not every changed row's Lean statements, coverage row and section context were read, so requirement A is incomplete. The inspected material already establishes counterexamples: TerminalWick input scopes at ledger:1022,1026 (K1), and theorem rows incorrectly described as the definition of T_eps at :1085,1087 (K2). Thus the universal claim cannot be accepted independently of the remaining reading gaps.

Findings, fatal (0):

Findings, major (2):
- K1 — TerminalWick supplied-input splitting remains incorrect. candidate/statement-ledger.md:1022 says 'no named analytic input' over mixed_moment_mono alongside declarations without the supplied product-measurability input. Lean explicitly requires '(hmeas₁ : ∀ n, AEStronglyMeasurable ...)' and '(hmeas₂ : ∀ n, AEStronglyMeasurable ...)' (lean/StratonovichHAMSecondMoment/TerminalWick.lean:523-530). The same inputs occur in terminal_wick_mono_paper at :679-680, contradicting ledger:1026's 'no named analytic input'. That wrapper concludes only the mixed-moment comparison (:681-683), not a real-r convergence statement or a Wick formula requiring hK. TeX distinguishes comparison from real-or-complex-r convergence (manuscript/notes/notes_stratonovich_ham_second_moment.tex:3640-3644) and derives product measurability separately (:3657-3659). Exact fix: move mixed_moment_mono into its own proof-step row naming hmeas₁ and hmeas₂; retain pairing_integral_nonneg and chainIntegral_zero in the row without that supplied input. Rewrite the mono-wrapper cell as a narrower per-mixed-moment comparison for unconstructed chain measures, naming hmeas₁ and hmeas₂, noting the carried unused _hmass premise, and removing the real-r, Wick-formula and 'no named analytic input' clauses. Keep the real-r and hK disclosures on the main Wick wrapper where they apply.
- K2 — Regeneration misstates the roles of PhaseContractions theorems. candidate/statement-ledger.md:1085 describes lintegral_waveGreen_three, sphere_convolution, three_regions and kernel_le_bAlpha as 'the definition of T_eps'; :1087 repeats that description for traceT_fourier. Lean instead proves a normal-coordinate integral identity (lean/StratonovichHAMSecondMoment/PhaseContractions.lean:485-488), a sphere-convolution formula (:590-594), regional and uniform bounds (:694-702,720-723), and an integrability/Fourier identity (:1007-1012). The actual definition is traceT at :750-751, already separately indexed at ledger:1086. TeX likewise separates the definition/Fourier identity (manuscript/notes/notes_stratonovich_ham_second_moment.tex:2081-2084) from the convolution and regional proof steps (:2125-2136). Exact fix: describe row 1085 as the normal-coordinate/sphere-convolution identities and regional/uniform kernel bounds, retaining ArchimedesLaw; describe row 1087 as the integrability and Fourier representation of T_eps, retaining WaveFourierThree. Remove the definition claim from the theorem-only row 1084 as well.

Findings, minor (0):

Required repairs (2):
- K1: Correct the TerminalWick rows' actual supplied-input sets and restrict each wrapper's qualifications to its own conclusions.
- K2: Replace the PhaseContractions theorem rows' definition descriptions with their actual integral-identity and bound roles.

Limitations (5):
- Requirement A is incomplete for NO-NEW-OVERCLAIM-HALF. In particular, changed-row statements in StaticPhaseCauchy, L8Completed, RawOccupationEnergy, ComplexPhaseScalar, GaussianHermite and HermiteFock were not read; portions of other changed-row modules and their coverage/section contexts also remain unchecked. The overall INCONCLUSIVE verdict reflects this incomplete universal audit, not uncertainty about the established defects.
- The distinct-name recount verifies the reported labelled/unlabelled totals but is not a semantic review of the entire Index. Adjudication's intermediate 2431/37 explanation was not used as evidence for those totals.
- The mechanical checker's exact-name input whitelist does not establish semantic input completeness; it misses the subscripted measurability inputs identified in K1.
- Proof correctness and Lean compilation were outside scope. Provenance hashes were not independently authenticated.
- This AI correspondence review is neither human verification nor a novelty audit.

## h3-consistency-l8

Preflight: contract-check CONTRACT-OBSERVABLE (14 required field(s), 0 dispatch input(s); no provider call); dry run exit 0 (dryrun/); contract-check with --dispatch-input dryrun/prompt.txt CONTRACT-OBSERVABLE (14 required field(s), 1 dispatch input(s); no provider call)

Driver log:
```
2026-11-12T18:36:49Z start attempt-01
2026-11-12T18:43:49Z attempt-01 exit=3 Status: review-complete
2026-11-12T18:43:49Z done
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
Check verdicts: FAIL 1, INCONCLUSIVE 1 (of 2)

Checks not PASS/PASS_WITH_NOTES:
- CLASSIFICATION-CONSISTENCY: FAIL: Independent parsing reproduces 2468 declarations: 1300 labelled and 1168 unlabelled; 2050 theorems and 418 definitions. COMPLETION reproduces 25/18/0/30/3/144 = 220; coverage has 47 same-assumptions, 30 inputs-supplied and 3 outside rows, with 29 full and 18 weaker same-assumptions conclusions. All 48 conclusion_scope sentences equal their 48 ASCII mirrors. Module counts reproduce 27/0/31/18, plus 23 audit proof-step modules; heading counts are 24 whole, 32 narrower and 34 foundation/proof-step headings. The category inventories reproduce 559/135, 943/199, 466/78 and 82/6 theorem/definition counts. There are 657 Index rows. Thus no numerical disagreement was found in the requested summaries (ledger:44-112,1163-1164; FORMALIZATION:80-86; README:21-38,449; COMPLETION:35-56; coverage.yaml:2,10-13). Nevertheless, category and qualifier consistency fails: ledger:941 calls a resolvent-only theorem the whole spatial Fourier-bound result; :946 and :950 retain mixed mathematical roles; :1022 and :1026 incorrectly disclaim named analytic inputs. See K1-K4.
- L8-REPAIRS-KEPT: INCONCLUSIVE: The inspected passages preserve the covariance-smoothing limitation and add the missing general lower-bound limitation (ledger:1983-2006,2163,2192-2197); retain the totalized-division warning (7167-7181), monomial/continuous-F distinction (2593-2600), Scope integrability warning (403-413), one-mode/single-word restriction (1326-1364,1156), three-dimensional phase signatures (L9Completed.lean:150-184), refutation-domain wording (ledger:5403-5415), and M1 register and dependent whole-result cells (80-95,1095,1157,1160). The main TerminalWick row still records hK as an added restriction (1025,7550-7590). However, regeneration introduces false input-free qualifications for comparison declarations (diff:722,726; K3), so preservation is not clean. Complete universal certification is unavailable because the full diff and all regenerated Index qualifiers were not exhaustively read against their declarations.

Findings, fatal (0):

Findings, major (4):
- K1 — Residual false whole-result classification in the SpectralMassIdentity Index row. candidate/statement-ledger.md:941 labels both declarations 'whole result with the manuscript's constant R_alpha'. But resolvent_eq_ralpha_paper concludes only 'resolvent μ 1 = ralpha μ alpha' and the scaled resolvent identity (lean/StratonovichHAMSecondMoment/SpectralMassIdentity.lean:228-232). TeX L:spatial-fourier-bound additionally requires 'b>0' and '0 <= A_sp(g) <= 2^(1+alpha) R_alpha b^(alpha/2)' (manuscript/notes/integrated_spatial_occupation.tex:101-111); the resolvent identity appears only in its proof (:149-155). Exact fix: retain whole-result status for spatial_fourier_bound_ralpha_paper alone and put resolvent_eq_ralpha_paper in a separate proof-steps row describing the resolvent identity and integrability.
- K2 — DampedMultiplier still combines wrappers and supporting fragments under false shared qualifiers. candidate/statement-ledger.md:946 says 'narrower result ... wrappers with nothing supplied' over, among others, IsMultiplier.mul, whose entire conclusion is 'IsMultiplier (g * h)' (lean/StratonovichHAMSecondMoment/DampedMultiplier.lean:199-202), and N2GreenSq_gauss, a general-family smoothing identity (:370-374). Neither is a wrapper for the labelled lemma. Likewise ledger:950 says 'both bounds' over N1on_nonneg and N2onSq_nonneg, which individually conclude only '0 <= N1on ...' and '0 <= N2onSq ...' (DampedMultiplier.lean:146-162). TeX states both lower and upper inequalities in E:damped-multiplier-comparison and separate smoothing assertions (manuscript/notes/notes_stratonovich_ham_second_moment.tex:836-847). Exact fix: separate the lemma wrappers from supporting proof steps, qualify the dimension-one Fourier wrapper by its actual scope, and give the comparison assembly and each individual lower-bound theorem distinct, accurate qualifiers.
- K3 — Regeneration incorrectly marks TerminalWick comparison declarations input-free. candidate/statement-ledger.md:1022 places mixed_moment_mono under 'no named analytic input', although Lean explicitly takes 'hmeas₁' and 'hmeas₂' as AEStronglyMeasurable hypotheses (lean/StratonovichHAMSecondMoment/TerminalWick.lean:523-530). Ledger:1026 repeats that disclaimer for terminal_wick_mono_paper, which takes the same supplied measurability inputs and '_hmass' (:669-683). The manuscript asserts existence of the Bochner integrals and covariance comparison (manuscript/notes/notes_stratonovich_ham_second_moment.tex:3610,3640-3642); the ledger itself identifies strong measurability as supplied, not discharged (candidate/statement-ledger.md:7557-7562). These disclaimers are introduced at diffs/docs-350d191-a723987.diff:722,726. Exact fix: isolate mixed_moment_mono from the input-free helpers and explicitly disclose hmeas₁/hmeas₂; rewrite the comparison-wrapper cell for its comparison-only conclusion, supplied measurability and mass premises, without implying that it asserts a Wick formula or takes hK.
- K4 — A copied DampedNormsHomog qualifier no longer describes its declarations. candidate/statement-ledger.md:703 retains 'N_0; N_1, N_2 as the full-domain case' after N0 was split into :702. The remaining Lean declarations conclude only 'N2onSq ... univ ... = N2sq ...' and 'N1on ... univ ... = N1 ...' (lean/StratonovichHAMSecondMoment/DampedNormsHomog.lean:439-448). TeX defines N_0 separately from N_1 and N_2 (manuscript/notes/notes_stratonovich_ham_second_moment.tex:782-793). Exact fix: remove the N_0 qualification from :703 and classify these supporting full-domain identities as proof steps, distinguishing the first- and second-norm identities rather than assigning both scopes to every declaration.

Findings, minor (0):

Required repairs (4):
- K1: Split the spatial Fourier-bound wrapper from the resolvent-only proof theorem and correct its category.
- K2: Split the remaining DampedMultiplier wrapper/supporting-fragment rows and make every qualifier accurate for each declaration.
- K3: Restore explicit supplied-measurability qualifications on both TerminalWick comparison declarations and correct their comparison-only scope.
- K4: Remove the stale N_0 qualification and correctly classify the full-domain norm identities.

Limitations (6):
- This is not an acceptance verdict: established classification errors require repair independently of the incomplete universal review.
- The entire 657-row Index was counted but not exhaustively checked declaration by declaration against Lean and authoritative TeX. The findings are counterexamples, not an exhaustive defect inventory.
- The diff was not completely read: gaps are lines 101-135,171-249,296-487,508-561,641-696,736-774,817-889. Consequently the strict complete-reading requirement and universal L8-REPAIRS-KEPT certification are not claimed satisfied.
- Coverage class/conclusion fields were read for every row; intervening claim lists and notes were not all semantically read. Complete machine parsing established counts and ASCII equality, not complete semantic source reading.
- Lean proof correctness, compilation, provenance hashes and unavailable refutation files were not independently verified.
- No files were edited, no network was used, and no work was delegated. This AI review is not human verification or a novelty audit.

## i1-index-505-587

Preflight: contract-check CONTRACT-OBSERVABLE (14 required field(s), 0 dispatch input(s); no provider call); dry run exit 0 (dryrun/); contract-check with --dispatch-input dryrun/prompt.txt CONTRACT-OBSERVABLE (14 required field(s), 1 dispatch input(s); no provider call)

Driver log:
```
2026-11-12T18:36:49Z start attempt-01
2026-11-12T18:41:21Z attempt-01 exit=2 Status: review-complete
2026-11-12T18:41:21Z done
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
- INDEX-CELLS lines 505-587: FAIL: The required reading is complete, but the per-declaration correctness rule fails. Line 551 incorrectly puts a theorem with supplied path-moment and measurability inputs in a 'no named analytic input' group. Lines 530 and 534 apply 'whole result' to declarations proving only individual parts. Lines 574 and 581 classify supporting facts as narrower results without an applicable missing conclusion. See K1-K3. The completed/abstract split at lines 554-558 is supported by TimeCompletion's original lines 1056-1068 and the abstract wrappers' binders.

Findings, fatal (0):

Findings, major (3):
- K1 — Undisclosed supplied inputs in candidate/statement-ledger.md:551. The cell says 'no named analytic input, premises as stated' while including mean_anchor_bound_blocks. In lean-excerpts/StratonovichHAMSecondMoment/RadiusMeanAnchor.lean.excerpt.txt, original lines 330-338 explicitly mark a 'supplied input' and bind hMC, hMint, hMmom and hXmeas; hMmom assumes '(∫ ω, holderNorm θ B (M m ω) ^ p ∂μ) ^ (1 / p) ≤ C * Real.sqrt p * R ^ e'. The manuscript uses the residual paths 'Y_m as in Corollary C:radius-covariance-residuals' at manuscript/notes/integrated_radius_anchor.tex:284-285 and their moment estimate at 311-317. The section table itself discloses these inputs at candidate/statement-ledger.md:5711. Exact fix: remove mean_anchor_bound_blocks from line 551 and give it a separate proof-steps row explicitly naming hMC, hMint, hMmom and hXmeas. The scanner's RadiusMeanAnchor binder list at tools/decltable.py:21 omits all four, explaining why mechanical homogeneity did not detect this.
- K2 — Partial conclusions marked whole per declaration at candidate/statement-ledger.md:530,534. DriverParameters.gamma_interval_nonempty concludes only '∃ γ ...', and theta_beta_interval_nonempty only '∃ θ β ...' (lean-excerpts/StratonovichHAMSecondMoment/DriverParameters.lean.excerpt.txt, original lines 25-34), whereas manuscript/notes/integrated_actual_operator_driver.tex:18-23 specifies both intervals and says 'The strict intervals are nonempty.' Likewise GaussianScalarPowers.weighted_power concludes only 'u ^ θ * v ^ (1 - θ) ≤ θ * u + (1 - θ) * v' (its excerpt, original lines 29-31); the other declarations separately prove the integer-power, Hölder and expectation conclusions. The labelled TeX lemma contains all four at manuscript/notes/integrated_compact_gaussian.tex:13-27. Collective completeness of a module does not satisfy the stipulated requirement that 'whole result' be true of every declaration in a row. Exact fix: keep parameters_nonempty in a whole-result row, move its two component lemmas to proof-steps rows, and classify the four GaussianScalarPowers declarations as proof steps proving the respective parts; retain the module-level statement that together they formalize the whole lemma.
- K3 — Inapplicable narrower-result classifications at candidate/statement-ledger.md:574,581. CPos_nonempty proves '(CPos d).Nonempty' (lean-excerpts/StratonovichHAMSecondMoment/VariationalDilation.lean.excerpt.txt, original line 106), matching 'It is nonempty' at manuscript/notes/integrated_unmasked_variational.tex:13-15. There is no missing rate or variance identification in that claim. setScaling_of_homog concludes only 'SetScaling alpha Γ' from HomogCovariance (same excerpt, original lines 400-402), extracting the already-assumed clause 'Γ(cA) = c^{d-α} Γ(A)' at manuscript/notes/notes_stratonovich_ham_second_moment.tex:235-236. Neither theorem is the narrower dilation result named by the referenced section. Exact fix: change line 574 to 'proof steps: nonemptiness of the control class' and line 581 to 'proof steps: extraction of the scaling clause of H:homog'; remove their narrower-result cross-references.

Findings, minor (0):

Required repairs (3):
- Split mean_anchor_bound_blocks from line 551 and disclose its four supplied inputs as specified in K1.
- Correct the per-declaration whole-result classifications at lines 530 and 534 as specified in K2.
- Replace the narrower-result classifications at lines 574 and 581 with accurately scoped proof-steps classifications as specified in K3.

Limitations (5):
- All selections required by requirement A were read completely. Other ledger, coverage and manuscript content was read selectively; unlisted ranges were not reviewed.
- Source-coverage ranges for excerpt files are physical packet-file lines; findings identify their embedded original Lean line numbers.
- The packet supplies Lean statement excerpts, not complete Lean modules. Proof correctness, global counts, byte bindings and material outside the selected Index rows were not independently audited.
- The supplied checker output says 'cells checked: 657; problems: 0'; the checklist's reference to 402 is inconsistent with that artifact. Category presence was not rechecked.
- This AI correspondence review is neither human verification nor a novelty audit.

## i2-index-588-670

Preflight: contract-check CONTRACT-OBSERVABLE (14 required field(s), 0 dispatch input(s); no provider call); dry run exit 0 (dryrun/); contract-check with --dispatch-input dryrun/prompt.txt CONTRACT-OBSERVABLE (14 required field(s), 1 dispatch input(s); no provider call)

Driver log:
```
2026-11-12T18:36:49Z start attempt-01
2026-11-12T18:44:09Z attempt-01 exit=2 Status: review-complete
2026-11-12T18:44:09Z done
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
- INDEX-CELLS lines 588-670: FAIL: Residual category and input-disclosure errors remain at candidate/statement-ledger.md:588,600,603,605-606,611,615,622,635,655; see K1-K6. In particular, an integration-by-parts foundation is grouped with a whole proposition, partial display lemmas retain whole-result status, and supplied spectral homogeneity is omitted from input classification. The checker output at tools/index_category_check.out:1 does not establish semantic correctness: tools/decltable.py:6-23 omits SpectralHomogeneous, and its binder scan at 33-45 does not recover inherited section-variable inputs. The complete required readings were performed. The principal frequency and occupation wrappers and the displayed numerical constants otherwise match their cited statements.
- INDEX-MAPPING lines 588-670: FAIL: candidate/statement-ledger.md:655 assigns FrequencyRow.one_le_scaleProfile to the defining equation E:variance-scale-profile. Its conclusion is instead the bound used in the proof of P:frequency-row: manuscript/notes/integrated_wave_variance.tex:136-138, versus the definition at 12-20. See K4. Other examined mappings are supported by the labelled statements, their proofs, or the explicitly disclosed abstract-family correspondence.

Findings, fatal (0):

Findings, major (6):
- K1 — Mixed whole-result row at candidate/statement-ledger.md:622. GaussianIBP.integral_coord_mul_eq_of_growth_paper concludes Gaussian integration by parts, namely '∫ ω, g k ω * f (...) ∂P = ∫ ω, f′ (...) ∂P', with derivative, continuity and polynomial-growth premises (GaussianIBP.lean:303-315, original numbering in the supplied excerpt). TeX uses this only as a proof step at manuscript/notes/integrated_compact_gaussian.tex:121-126; the proposition itself asserts the two Schatten bounds at 98-118. FiniteGaussianMatrix.finite_gaussian_matrix_paper does state those bounds (FiniteGaussianMatrix.lean:1299-1321). Exact fix: remove the GaussianIBP declaration from the whole-result row and give it a separate 'proof steps: Gaussian integration by parts' row, retaining P:finite-gaussian-matrix as its proof label. Keep the matrix wrapper in the whole-result row.
- K2 — Partial clock-display lemmas labelled whole at candidate/statement-ledger.md:605. K_eq_integral_weight concludes only 'N2sq ... = ∫ ... weight'; J_one_eq concludes integrability and the filtered-integral identity; J_rho_props concludes integrability and '0 < J ... ∧ J ... ≤ J ... 1' (ClockCopy.lean:434-437,556-560,603-607, original numbering in the supplied excerpt). None concludes the strict inequality 'J_{Γ,1}(θ) < K_Γ(θ)' required by manuscript/notes/notes_stratonovich_ham_second_moment.tex:7764-7773; even their listed conclusions collectively omit it. Exact fix: classify these declarations as proof steps with their individual scopes, not as the whole display. Point readers seeking the full display to the complete obstruction wrappers already indexed at lines 603 and 638.
- K3 — Partial translated-mass lemmas labelled whole at candidate/statement-ledger.md:635. translated_gauss_le concludes only the Gaussian upper bound (MaskedSpectralGrowth.lean:383-386); closedBall_le concludes only 'μ (closedBall y r) ≤ ...' and assumes Gaussian integrability as hint (MaskedSpectralGrowth.lean:421-424; original numbering in the supplied excerpt). TeX E:masked-translated-ball contains both the nonnegative Gaussian bound and the ball bound, allowing open or closed balls (manuscript/notes/integrated_covariance_foundation.tex:46-51). The whole-result category is therefore not true of each declaration. Exact fix: use separate proof-step rows describing the Gaussian upper bound and the closed-ball mass bound, including the latter's integrability premise; retain the complete proposition wrapper at ledger line 631 as whole.
- K4 — Wrong category and direct label at candidate/statement-ledger.md:655. FrequencyRow.one_le_scaleProfile concludes only '1 ≤ scaleProfile α h' for 0 < h ≤ 1 (FrequencyRow.lean:222-224, original numbering in the supplied excerpt). TeX E:variance-scale-profile defines the three cases '1', '1+log(1/h)', and 'h^{1−α}' at manuscript/notes/integrated_wave_variance.tex:12-20; it does not state this inequality. The inequality appears as 'using B_α(h) ≥ 1' in the proof of P:frequency-row at 136-138. Exact fix: change this cell to 'P:frequency-row (proof steps: B_α(h) ≥ 1 used in the proof)'. The definition remains correctly indexed separately at line 654.
- K5 — False input-free qualifiers at candidate/statement-ledger.md:588,600. These cells say 'no named analytic input', although the GroundFamily lemmas depend on the supplied abstract family G, and the ConeConstants lemmas additionally use K's recorded bounds. Lean defines 'structure GroundFamily' with eigenrelations, complementary decay, continuity and positive margins (IndexedCone.lean:83-126), and 'structure ConeConstants (G : GroundFamily F)' with the assumed gap and smallness bounds (238-287); positive_product_of_constants uses those data at 683-692. TeX obtains precisely these analytic bounds before the induction at manuscript/notes/integrated_raw_block_lower.tex:254-280. Exact fix: split the GroundFamily and ConeConstants groups at line 588, explicitly naming their respective supplied structures, and replace the input-free qualifier at line 600 with the corresponding GroundFamily/ConeConstants disclosure. Preserve their proof-step categories.
- K6 — Spectral-homogeneity input omitted from the regenerated classification. candidate/statement-ledger.md:603,606 does not name hI; rows 611 and 615 also group declarations retaining spectral homogeneity with declarations not retaining it. ClockCopy.clock_copy_obstruction_paper explicitly takes '(hI : SpectralHomogeneous μ alpha)' (ClockCopy.lean:722-724), degree_one takes 'SpectralHomogeneous μ 1' (669-672), and DampedNorms.damped_norms_finite_paper retains hI (DampedNorms.lean:359-365). SpectralHomog's scaling consequences likewise retain hI, including resolvent_homog and heat_homog (SpectralHomog.lean:225-245; original numbering in the supplied excerpts). TeX derives this input, 'μ(cA) = c^α μ(A)', in manuscript/notes/notes_stratonovich_ham_second_moment.tex:851-852. Its later discharge does not remove it from the older declarations. Exact fix: name SpectralHomogeneous explicitly in the affected first cells and split rows 611 and 615 by actual supplied-input set. Rows 603 and 606 may retain whole-result status with the named input disclosed and its completion identified; do not describe the older declarations as input-free.

Findings, minor (0):

Required repairs (5):
- K1: Separate the GaussianIBP proof step from the whole-result matrix wrapper at ledger line 622.
- K2-K3: Replace whole-result tags on partial display lemmas at lines 605 and 635 with accurately scoped proof-step cells, split where their scopes or inputs differ.
- K4: Reclassify and remap one_le_scaleProfile at line 655 to the proof of P:frequency-row.
- K5: Correct the GroundFamily/ConeConstants input disclosures and grouping at lines 588 and 600.
- K6: Disclose retained SpectralHomogeneous inputs and split the affected rows by their actual input sets.

Limitations (4):
- All portions required by complete-reading requirement A were read completely. For files marked partial, lines outside the explicitly listed ranges were not reviewed; the broader ledger, unrelated coverage records and other manuscript sections are outside these two checks.
- Lean citations in findings use the original source-line numbers embedded in the supplied excerpts. Every excerpt file was read completely, but its intentionally omitted proof/source ranges were unavailable.
- This reviews documentation correspondence, not Lean proof correctness, package compilation, global declaration counts or cryptographic provenance.
- An AI review is not human verification or a novelty audit.

## i3-index-671-753

Preflight: contract-check CONTRACT-OBSERVABLE (14 required field(s), 0 dispatch input(s); no provider call); dry run exit 0 (dryrun/); contract-check with --dispatch-input dryrun/prompt.txt CONTRACT-OBSERVABLE (14 required field(s), 1 dispatch input(s); no provider call)

Driver log:
```
2026-11-12T18:36:49Z start attempt-01
2026-11-12T18:42:04Z attempt-01 exit=2 Status: review-complete
2026-11-12T18:42:04Z done
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
Check verdicts: FAIL 1, INCONCLUSIVE 1 (of 2)

Checks not PASS/PASS_WITH_NOTES:
- INDEX-CELLS lines 671-753: FAIL: Residual category/qualifier errors occur at candidate/statement-ledger.md:691,703,718,749. In particular, the core theorems at lean-excerpts/StratonovichHAMSecondMoment/WaveTwoVariances.lean.excerpt.txt:315-340 have neither abstract phase-space data nor the supplied inputs attributed by row 749. Other rows still conflate comparison with finiteness, or distinct partial conclusions. The completed temporal and continuous-wave whole-result classifications are supported by their Lean statements and full coverage rows; the registered M1 exception was applied as written, not treated as a missing construction.
- INDEX-MAPPING lines 671-753: INCONCLUSIVE: The available declarations have appropriate statement/proof anchors, including Gaussian comparison in manuscript/notes/integrated_covariance_foundation.tex:239-246 and the spectral variance core in manuscript/notes/integrated_wave_variance.tex:385-458. However, row 708 names DampedNormsHomog.KS_univ, whose declaration is absent from the completely read lean-excerpts/StratonovichHAMSecondMoment/DampedNormsHomog.lean.excerpt.txt:1-439. The paraphrase at candidate/statement-ledger.md:2315 cannot independently verify its type or the no-direct-label mapping.

Findings, fatal (0):

Findings, major (4):
- K1 — WaveTwoVariances core row, candidate/statement-ledger.md:749: the qualifier attributes 'abstract variance and phase spaces' and 'the proposition with the named inputs hlink, hJL2/hJ, hnormSG' to two concrete spectral-core declarations. Lean concludes 'InputBound ... ∧ OutputBound ...' without P, J, var or those inputs (lean-excerpts/StratonovichHAMSecondMoment/WaveTwoVariances.lean.excerpt.txt:315-340; original Lean 822-853). Those binders occur only in the proposition wrapper at excerpt lines 360-373. TeX distinguishes the noise variance 'sum_k E|ell_R(I;e_k,z)|^2' at manuscript/notes/integrated_wave_variance.tex:374-375 from its spectral proof at lines 413-451. Fix row 749 to 'proof steps: spectral core for nu_R, with no supplied analytic input; noise/phase identification not established here'; retain the abstract-object and named-input qualifications only on row 750.
- K2 — Auxiliary Fourier row, candidate/statement-ledger.md:691: a finiteness-only supporting lemma is presented alongside comparison theorems as a narrower labelled result. Lean's lintegral_paperHat_nu_lt_top concludes only '∫⁻ η, ‖paperHat ... η‖ₑ ^ 2 ∂nu ... < ⊤' (lean-excerpts/StratonovichHAMSecondMoment/MaskedAuxiliaryNorm.lean.excerpt.txt:458-460; original Lean 802-804). It does not conclude the comparison '∫ ‖hat(zeta_R F)‖² dmu ≤ ∫ ‖hat F‖² dnu_R' of manuscript/notes/integrated_covariance_foundation.tex:95-98; finiteness appears in that proof at lines 134-135. Fix by moving the finiteness-only declaration to a separate 'proof steps: finiteness of the right-hand side only' row, leaving the comparison declarations accurately scoped separately.
- K3 — Damped full-domain row, candidate/statement-ledger.md:703: the retained qualifier includes 'N_0', although neither listed declaration mentions N_0. Lean states 'N1on a theta univ mu = N1 a theta mu' and 'N2onSq a theta univ mu = N2sq a theta mu' (lean-excerpts/StratonovichHAMSecondMoment/DampedNormsHomog.lean.excerpt.txt:284-289; original Lean 439-447). TeX defines N_0 separately at manuscript/notes/notes_stratonovich_ham_second_moment.tex:784 and N_1,N_2 at lines 785-791. Fix by removing N_0 and splitting into proof-step rows naming respectively the unrestricted N_1 identity and unrestricted N_2-squared identity; keep N_0 on row 702.
- K4 — Mean-bound row, candidate/statement-ledger.md:718: 'the upper bound and the Lipschitz bound' does not describe every declaration in the row, and the section reference does not identify the missing conclusions of this equation. Lean mean_le concludes only 'mean ... ≤ B * exp ... * gMass ... * (2 / (1-a))', whereas mean_lip concludes only a joint difference bound (lean-excerpts/StratonovichHAMSecondMoment/VariationalMean.lean.excerpt.txt:332-349; original Lean 558-582). TeX E:variational-global-mean contains '0 ≤ h_s(x) ≤ M' and the time sup-norm Lipschitz estimate (manuscript/notes/integrated_unmasked_variational.tex:69-73); the unformalized mixed-derivative sentence is outside that display, at line 66. Fix by splitting into 'proof steps: upper bound only' and 'proof steps: joint Lipschitz estimate, yielding the displayed time estimate at x=x′' rows.

Findings, minor (0):

Required repairs (5):
- Correct row 749 to describe only the input-free spectral core, separating it from row 750's abstract proposition and supplied inputs.
- Separate the finiteness-only declaration from the Fourier comparison declarations in row 691.
- Remove the unsupported N_0 qualifier from row 703 and give the two full-domain identities their own accurately scoped proof-step rows.
- Split row 718 into separately qualified upper-bound and Lipschitz proof-step rows.
- Supply the frozen KS_univ declaration and necessary context so row 708 can be independently checked.

Limitations (5):
- Requirement A's specified files and ranges were read completely, including all supplied Lean excerpts. Nevertheless, the packet omits the Lean declaration KS_univ named by row 708.
- For sources marked partial, portions outside the listed ranges were not reviewed; unrelated ledger entries, coverage rows and manuscript passages are outside this report.
- Category-word presence was not rechecked. The supplied checker output reads 'cells checked: 657; problems: 0', rather than the stale 402 count in the check description.
- Proof correctness, compilation, provenance byte hashes and package-wide counts were not independently audited.
- This AI review is neither human verification nor a novelty audit.

## i4-index-754-836

Preflight: contract-check CONTRACT-OBSERVABLE (14 required field(s), 0 dispatch input(s); no provider call); dry run exit 0 (dryrun/); contract-check with --dispatch-input dryrun/prompt.txt CONTRACT-OBSERVABLE (14 required field(s), 1 dispatch input(s); no provider call)

Driver log:
```
2026-11-12T18:36:49Z start attempt-01
2026-11-12T18:42:21Z attempt-01 exit=2 Status: review-complete
2026-11-12T18:42:21Z done
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
- INDEX-CELLS lines 754-836: FAIL: The required reading is complete, but some inherited qualifiers remain collective rather than declaration-specific: candidate/statement-ledger.md:770,811-812,815 confuse input-free/existential statements with supplied-input supremum statements. Line 786 incorrectly transfers the enclosing proposition's narrower status to a fully proved deterministic display. Lines 804 and 814 omit the important restriction that their wrappers prove only part (i), not the score inequality. See K1-K3.

Findings, fatal (0):

Findings, major (3):
- K1 — Residual collective form/input qualifiers at candidate/statement-ledger.md:770,811-812,815. The qualifier 'supremum forms on the named input S1Bdd' at line 770 covers only variational_positive_scores_paper, whose Lean statement has no S1Bdd binder and concludes nonemptiness, positivity, scaling and a boundedness equivalence, not the supremum assertions (lean-excerpts/StratonovichHAMSecondMoment/VariationalRate.lean.excerpt.txt, original lines 781-802). Those supremum assertions occur in the separate S1Bdd-taking theorem at original lines 817-823. Likewise, line 811's theorem concludes '∀ y ... ∃ Ψ' without S1Bdd, whereas line 812's theorem concludes an inequality with S1pos under S1Bdd (lean-excerpts/StratonovichHAMSecondMoment/SpatialStaticControls.lean.excerpt.txt, original lines 1127-1137 and 1151-1155). Both declarations at ledger line 815 have existential score conclusions and no S1Bdd binder (lean-excerpts/StratonovichHAMSecondMoment/SpatialOccupationCompleted.lean.excerpt.txt, original lines 133-137 and 169-176). TeX distinguishes finite supremum assertions from these existential reformulations: manuscript/notes/integrated_unmasked_variational.tex:272-279 says 'bounded above' and defines the finite supremum, while manuscript/notes/integrated_spatial_occupation.tex:50-53,171-176 displays S1pos inequalities. Fix: make line 770 explicitly the input-free, non-supremum part; make line 811 existential with no named analytic input; make line 812 the sSup form with S1Bdd; make line 815 existential completed wrappers with no supplied input. Any discussion of other forms must explicitly identify them as declarations outside that row.
- K2 — Incorrect narrower-result category for E:spatial-dilation at candidate/statement-ledger.md:786. Lean concludes both 'spatialEnergy Γ (dilL2 ℓ g) = ℓ ^ alpha * spatialEnergy Γ g' and 'gradEnergy (dilL2 ℓ g) = ℓ ^ 2 * gradEnergy g', under the section hypotheses and with no supplied analytic input (lean-excerpts/StratonovichHAMSecondMoment/SpatialSmoothRatio.lean.excerpt.txt, original lines 673-677). These are exactly both identities in manuscript/notes/integrated_spatial_occupation.tex:189-195: 'A_sp(U_ell g)=ell^alpha A' and 'b(U_ell g)=ell^2 b(g)'. Neither identity involves the unconstructed spectral rate or stochastic cost named by the referenced section heading. Thus the reference does not identify anything missing from this display. Fix line 786 to 'proof steps: the display in full, nothing supplied; the enclosing proposition and module remain narrower', preserving E:spatial-dilation as the anchor.
- K3 — Missing part-(i)-only restriction at candidate/statement-ledger.md:804,814. Both cells describe 'Rayleigh-form rate and integral-form cost', but their sole declarations assert integrability of U_z, positivity/finiteness of its Rayleigh supremum and local Lipschitz continuity; neither concludes a cost or score inequality (lean-excerpts/StratonovichHAMSecondMoment/SpatialStaticControls.lean.excerpt.txt, original lines 1098-1105; lean-excerpts/StratonovichHAMSecondMoment/SpatialOccupationCompleted.lean.excerpt.txt, original lines 93-100). The labelled TeX lemma additionally asserts 'S_1^{pos} >= lambda_z(1) - M_a B_Gamma(z,z)/2' at manuscript/notes/integrated_spatial_occupation.tex:50-53, after the rate assertions at lines 40-49. Merely naming unformalized rate/cost identifications does not disclose that this entire second conclusion is absent from these wrappers. Fix both cells to state 'part (i) only: positivity, finiteness and local Lipschitz continuity; E:spatial-static-score is not a conclusion of this declaration'. Retain RayleighFloor on line 804 and 'nothing supplied' on line 814.

Findings, minor (0):

Required repairs (3):
- Replace the collective form/input qualifiers at ledger lines 770, 811-812 and 815 with the declaration-specific descriptions specified in K1.
- Reclassify ledger line 786 as proof steps proving E:spatial-dilation in full, as specified in K2.
- Disclose the part-(i)-only scope and absent score conclusion at ledger lines 804 and 814, as specified in K3.

Limitations (5):
- Requirement A was completed. Other ledger, coverage and manuscript passages were read selectively; this is not a review of the remaining ledger rows or the full manuscript.
- Lean citations in findings use the original line numbers printed inside the supplied excerpt files. Complete excerpt coverage does not mean complete original-module coverage.
- The packet does not supply Lean excerpts for L8Completed or SpectralMassIdentity. Their asserted input discharges and constant-identification proofs were not independently inspected.
- The supplied checker output says 'cells checked: 657; problems: 0', not the 402 stated in one check description. Category presence was not rechecked, and the mechanical result was not treated as evidence of semantic correctness.
- Proof correctness, package-wide counts and provenance hashes were not independently verified. This AI review is neither human verification nor a novelty audit.

## i5-index-837-919

Preflight: contract-check CONTRACT-OBSERVABLE (14 required field(s), 0 dispatch input(s); no provider call); dry run exit 0 (dryrun/); contract-check with --dispatch-input dryrun/prompt.txt CONTRACT-OBSERVABLE (14 required field(s), 1 dispatch input(s); no provider call)

Driver log:
```
2026-11-12T18:36:49Z start attempt-01
2026-11-12T18:41:48Z attempt-01 exit=2 Status: review-complete
2026-11-12T18:41:48Z done
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
Check verdicts: FAIL 1, PASS 1 (of 2)

Checks not PASS/PASS_WITH_NOTES:
- INDEX-CELLS lines 837-919: FAIL: Residual section-level qualifiers do not accurately describe every listed declaration at candidate/statement-ledger.md:873-874, and four complete display wrappers retain an unjustified narrower-result category at lines 877, 879, 881 and 885. See K1-K2. The inspected white-transform constants, inventory coefficient bound, uniform-tail hypotheses and occupation-energy factor otherwise match their supplied statements.

Findings, fatal (0):

Findings, major (2):
- K1 — Residual mixed scope at candidate/statement-ledger.md:873-874. Both cells say 'narrower result: joint continuity of C_4 in sequential form', but this does not describe every declaration. For example, Lean spatial_Asp_pos_paper concludes only '0 < pairing ...' (lean-excerpts/StratonovichHAMSecondMoment/SpatialFourLinear.lean.excerpt.txt:847-850, original Lean 1565-1568); spatial_ratio_H1_paper concludes 'Rsp Γ alpha = R0 Γ alpha' (same excerpt:830-842); squarePairingBounds_paper supplies the homogeneous and squared-CS bounds (same excerpt:903-921). TeX separately asserts 'jointly continuous' and positivity at manuscript/notes/integrated_spatial_occupation.tex:229-236. Exact fix: retain the sequential-continuity qualification on the bundled result and continuity declaration only; give multilinearity, ratio equality, pairing bounds and positivity their own proof-step descriptions, retaining hdense only where actually present.
- K2 — Complete displays incorrectly inherit narrower-result status at candidate/statement-ledger.md:877,879,881,885. Lean states the homogeneous bound, square-CS bound, four-linear integral bound and energy identity in full, with the disclosed density input: lean-excerpts/StratonovichHAMSecondMoment/SpatialFourLinear.lean.excerpt.txt:727-778,928-937, including 'Esp Γ = energyValue alpha (Rsp Γ alpha) ∧ 0 < Esp Γ'. These match manuscript/notes/integrated_spatial_occupation.tex:224-234,309-314. Neither sequential continuity nor rate/cost identification is part of these displays. Thus referring to the narrower enclosing section does not identify a missing conclusion of these labels. Exact fix: classify these four cells as 'proof steps: the display in full, with the named density input hdense; the enclosing proposition remains narrower', consistent with the distinction already applied to their completed counterparts.

Findings, minor (0):

Required repairs (2):
- Replace the inherited continuity qualifiers at lines 873-874 with declaration-appropriate scopes, splitting the row where necessary and preserving the actual density-input distinctions.
- Reclassify lines 877, 879, 881 and 885 as full-display proof steps with hdense supplied, rather than narrower displays justified by unrelated section-level omissions.

Limitations (3):
- Requirement A was read completely. Partial-file coverage above concerns material outside its required ranges; the remaining manuscript and ledger bodies were not reviewed globally.
- TerminalWick and completion-module Lean sources are not supplied among the excerpts, so their discharge cross-references could not be independently inspected.
- Proof correctness, package-wide counts, provenance hashes and novelty were not audited. This AI review is not human verification.

## i6-index-920-1002

Preflight: contract-check CONTRACT-OBSERVABLE (14 required field(s), 0 dispatch input(s); no provider call); dry run exit 0 (dryrun/); contract-check with --dispatch-input dryrun/prompt.txt CONTRACT-OBSERVABLE (14 required field(s), 1 dispatch input(s); no provider call)

Driver log:
```
2026-11-12T18:36:49Z start attempt-01
2026-11-12T18:43:24Z attempt-01 exit=2 Status: review-complete
2026-11-12T18:43:24Z done
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
- INDEX-CELLS lines 920-1002: FAIL: The required reading is complete, but semantic homogeneity is not. For example, candidate/statement-ledger.md:941 assigns whole-result status to a resolvent proof lemma; :938 describes an input-free existential theorem as an S1Bdd-dependent sSup theorem; :994-996 each claim both bracket halves although their declarations prove separate halves. Additional copied qualifiers and mixed roles occur at :931, :946, :950, :971-972, :977, :984-990 and :1002. These violate Scope :62-79 and lean/FORMALIZATION.md:100-110. The mechanical output tools/index_category_check.out:1 does not establish semantic correctness.

Findings, fatal (1):
- K1 — Whole-result overclaim at candidate/statement-ledger.md:941. SpectralMassIdentity.resolvent_eq_ralpha_paper concludes only 'resolvent μ 1 = ralpha μ alpha ∧ ∀ q ... resolvent μ q = q ^ (alpha - 2) * ralpha μ alpha' (lean-excerpts/StratonovichHAMSecondMoment/SpectralMassIdentity.lean.excerpt.txt:134-138, original Lean 228-232). The labelled lemma instead concludes 'b>0' and '0≤A_sp(g)≤2^(1+alpha) R_alpha b^(alpha/2)' (manuscript/notes/integrated_spatial_occupation.tex:101-111); the resolvent identity appears only in its proof at :149-155. A reader cannot cite this declaration as the whole lemma. Exact fix: retain whole-result status only for spatial_fourier_bound_ralpha_paper and move resolvent_eq_ralpha_paper to a proof-steps row explicitly describing the resolvent calculation.

Findings, major (7):
- K2 — Mixed conclusion scopes at candidate/statement-ledger.md:931. The cell describes every listed declaration as the narrower joint-continuity result. However, spatial_four_linear_multilinear_paper_completed concludes four linearity equations, spatial_ratio_H1_paper_completed concludes 'Rsp Γ alpha = R0 Γ alpha', and squarePairingBounds_paper_completed supplies two pairing inequalities; only the continuity and assembled wrappers contain sequential continuity (lean-excerpts/StratonovichHAMSecondMoment/SpatialOccupationL7Completed.lean.excerpt.txt:151-255). TeX separately states joint continuity and the ratio identity and proves multilinearity (manuscript/notes/integrated_spatial_occupation.tex:229-236, 277-290). Exact fix: separate the assembled proposition, sequential-continuity clause, multilinearity, ratio identity and pairing bounds; classify supporting components as proof steps and give each its actual conclusion.
- K3 — Wrong conclusion and supplied input at candidate/statement-ledger.md:938. spatial_static_energy_score_paper_completed concludes '∀ y < ... F0 alpha (Esp Γ), ∃ Ψ ... y < integratedRate ... - rawCost ... / 2', without S1Bdd (lean-excerpts/StratonovichHAMSecondMoment/SpatialOccupationL7Completed.lean.excerpt.txt:268-279). The sSup version with '(hB1 : VariationalRate.S1Bdd ...)' is the different declaration at :281-290, already indexed at ledger :939. TeX states 'S_1^pos ≥ M_a^(-1/k) F_0(E_sp)' (manuscript/notes/integrated_spatial_occupation.tex:316-322). Exact fix: change :938 to the existential near-score form with nothing supplied, retaining the disclosed rate/cost identification limitation; reserve the sSup/S1Bdd qualifier for :939.
- K4 — DampedMultiplier rows remain semantically mixed at candidate/statement-ledger.md:946 and :950. At :946, declarations called 'wrappers with nothing supplied' include IsMultiplier.mul, whose conclusion is merely 'IsMultiplier (g * h)', and N2GreenSq_gauss, a conditional identity for an arbitrary family with 'hfin : ∀ s, 0 < s → IsFiniteMeasure (G s)' (lean-excerpts/StratonovichHAMSecondMoment/DampedMultiplier.lean.excerpt.txt:163-171, 295-306). Neither states the narrower labelled lemma. At :950, N1on_nonneg and N2onSq_nonneg conclude only individual nonnegativity bounds, whereas damped_multiplier_comparison also concludes the upper comparisons (:125-161). TeX distinguishes the two-sided display from the smoothing assertions (manuscript/notes/notes_stratonovich_ham_second_moment.tex:836-847). Exact fix: separate the genuine result wrappers from supporting smoothing lemmas, and separate the full comparison from each lower-bound component; use proof-steps categories and conclusion-specific hypotheses for the supporting rows.
- K5 — Copied occupation-assembly qualifiers at candidate/statement-ledger.md:971-972 and :977. young_quarter, young_q and ceilingValue_eq are scalar inequalities/algebra with no SpaceTimeCS premise; integratedRate_sq_le alone carries '(hST : SpaceTimeCS alpha0 Γ)' and concludes an integrated-rate square bound (lean-excerpts/StratonovichHAMSecondMoment/OccupationCeilingFinite.lean.excerpt.txt:116-150, 303-316). TeX likewise separates the scalar maxima from the occupation estimate (manuscript/notes/integrated_occupation_ceiling.tex:222-245). Also, s1Bdd_paper concludes only 'S1Bdd alpha0 Γ', while the other declaration at ledger :977 states positivity and general supremum homogeneity (excerpt :350-384; TeX manuscript/notes/integrated_unmasked_variational.tex:272-279). Exact fix: remove the rate-bound/SpaceTimeCS claims from the scalar row, describe only the square estimate at :972, and split :977 into the coefficient-one boundedness component and the supremum-result wrapper.
- K6 — Scalar-component scope overstatements at candidate/statement-ledger.md:984, :986, :988 and :990. Fb_zero proves only 'Fb alpha b 0 = 0', and Fb_zero_eq_F0 proves only the b=0 identification; neither gives the scalar map 'in full'. Dzeta_half proves only 'Dzeta alpha (1 / 2) * C ^ ... = energyValue alpha C'. The ceiling identities distinguish the special penalty 1/2 from arbitrary positive zeta (lean-excerpts/StratonovichHAMSecondMoment/SpatialBracket.lean.excerpt.txt:141-153, 192-223). TeX defines the full map for z>0 at manuscript/notes/integrated_occupation_ceiling.tex:195-203 and gives the arbitrary-zeta energy/ceiling formulas at :99-104, :209-215. The heterogeneous list at ledger :986 also does not make every declaration a proof of every listed scalar claim. Exact fix: replace the inherited collective descriptions with declaration-specific proof-step descriptions: zero value, b=0 identification, individual corollary-proof calculations, the zeta=1/2 coefficient identity, and the separate special/general ceiling identities. Do not classify Dzeta_half as an occupation-energy result.
- K7 — Both-halves qualifier is false for each separated bracket row at candidate/statement-ledger.md:994-996. spatial_bracket_lower_paper concludes an existential lower approximation and takes neither S1Bdd nor OccupationCeilingK0; spatial_bracket_lower_sSup_paper proves only the lower sSup inequality using S1Bdd; spatial_bracket_upper_paper proves boundedness and only the upper inequality using OccupationCeilingK0 (lean-excerpts/StratonovichHAMSecondMoment/SpatialBracket.lean.excerpt.txt:265-298). TeX's display contains both inequalities (manuscript/notes/integrated_occupation_ceiling.tex:256-260). Exact fix: label :994 'lower half, existential form, nothing supplied', :995 'lower half, sSup form on S1Bdd', and :996 'upper half and boundedness on OccupationCeilingK0', retaining the relevant narrowing references.
- K8 — Point-moment claim attached to a rates-only declaration at candidate/statement-ledger.md:1002. variational_remove_mask_rates_paper has only HomogCovariance, nonzero covariance and control-membership premises; its conclusion contains masks and rate convergence, not a liminf or RawBlockOriginalLower input (lean-excerpts/StratonovichHAMSecondMoment/RemoveMask.lean.excerpt.txt:357-418, original Lean 623-682). TeX states rate convergence and the point lower bound as distinct clauses (manuscript/notes/integrated_unmasked_variational.tex:170-177), with the latter proved separately at :214-218. Exact fix: remove the point-display/RawBlockOriginalLower qualifier from :1002 and explicitly restrict that cell to the Rayleigh-form mask/rate clauses with nothing supplied; leave the point clause with its separate declaration.

Findings, minor (0):

Required repairs (8):
- K1: Split the whole Fourier-bound wrapper from the resolvent proof lemma at ledger line 941.
- K2: Give the declarations at line 931 conclusion-specific categories and scopes.
- K3: Correct line 938 to the input-free existential score form.
- K4: Separate DampedMultiplier result wrappers, general smoothing steps, full comparisons and individual lower bounds.
- K5: Correct the scalar-versus-SpaceTimeCS scopes at lines 971-972 and split boundedness from supremum conclusions at line 977.
- K6: Replace the scalar rows' collective/full-result descriptions with accurate component descriptions.
- K7: State the actual individual bracket half and input at each of lines 994-996.
- K8: Restrict line 1002 to its rates-only conclusion.

Limitations (5):
- Requirement A is complete. Ledger body and coverage rows outside the recorded ranges were not reviewed.
- The contract quotes both 402 and 657 mechanically checked cells; the frozen output actually states 657. Category presence was not rechecked.
- This review checks documentation correspondence, not Lean proof correctness, compilation, package-wide counts or cryptographic byte bindings.
- The supplied Lean files are excerpts with omitted proof bodies and imports. M1 was applied as the registered documentary exception, not independently identified with surface measure.
- This AI review is not human verification or a novelty audit.

## i7-index-1003-1085

Preflight: contract-check CONTRACT-OBSERVABLE (14 required field(s), 0 dispatch input(s); no provider call); dry run exit 0 (dryrun/); contract-check with --dispatch-input dryrun/prompt.txt CONTRACT-OBSERVABLE (14 required field(s), 1 dispatch input(s); no provider call)

Driver log:
```
2026-11-12T18:36:49Z start attempt-01
2026-11-12T18:44:04Z attempt-01 exit=2 Status: review-complete
2026-11-12T18:44:04Z done
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
- INDEX-CELLS lines 1003-1085: FAIL: The required reading is complete. The principal whole/narrower distinctions, including registered model choice M1 at candidate/statement-ledger.md:1076, are generally supported. However, false input and scope qualifiers remain at lines 1022, 1026, 1048 and 1074, with additional stale declaration-role descriptions identified in K4. The mechanical result at tools/index_category_check.out:1 does not establish semantic correctness: tools/decltable.py:17,44-45 recognizes the exact binder name hmeas but misses hmeas₁ and hmeas₂, which appear in the TerminalWick declarations.

Findings, fatal (0):

Findings, major (4):
- K1 — TerminalWick input-free claims are false. candidate/statement-ledger.md:1022 groups mixed_moment_mono with two other theorems under 'no named analytic input'; line 1026 repeats that assertion for terminal_wick_mono_paper, contradicting its own earlier measurability disclosure. Lean explicitly requires '(hmeas₁ : ∀ n, AEStronglyMeasurable ...)' and '(hmeas₂ : ∀ n, AEStronglyMeasurable ...)' in lean-excerpts/StratonovichHAMSecondMoment/TerminalWick.lean.excerpt.txt:330-337,450-451 (original Lean lines 523-530,679-680). The comparison wrapper also carries '_hmass' at excerpt line 449. TeX derives, rather than assumes, measurability: 'the product is strongly measurable in L²' at manuscript/notes/notes_stratonovich_ham_second_moment.tex:3657-3659, and states comparison at 3640-3642. Exact fix: split mixed_moment_mono out of row 1022 and name both supplied measurability premises; remove the input-free assertion from row 1026 and explicitly disclose both measurability premises and the carried, unused mass premise.
- K2 — Fixed-cutoff theorem incorrectly described as taking cutoff-removal inputs. candidate/statement-ledger.md:1048 says 'cutoff removals supplied' over static_phase_order_cutoff. Its complete Lean signature takes only the four relevant analytic premises 'hentire', 'hcircle', 'hz' and 'hv', and concludes a bound for z1: lean-excerpts/StratonovichHAMSecondMoment/StaticPhaseCauchy.lean.excerpt.txt:265-273 (original lines 401-409). The actual limit premises 'hband' and 'hgauss' occur in the later theorem at excerpt lines 285-296. TeX likewise first obtains the estimate 'at the cutoffs' at manuscript/notes/notes_stratonovich_ham_second_moment.tex:2640-2641, then removes them at 2643-2666. Exact fix: describe row 1048 as the fixed-cutoff estimate with hcircle, hentire, hz and hv supplied, without cutoff-removal assumptions; retain the removal qualifier on row 1049 only.
- K3 — Radial row still combines declarations with different conclusion scopes. candidate/statement-ledger.md:1074 says 'both displays, with V < infinity and integrability' over measure_closedBall_eq and integral_lowKernel. The former concludes only 'μ (closedBall 0 R) = ENNReal.ofReal (R ^ alpha) * specV μ', with no local-finiteness assumption or finiteness/integrability conclusion: lean-excerpts/StratonovichHAMSecondMoment/LowAlphaConvolution.lean.excerpt.txt:191-193. Only integral_lowKernel assumes local finiteness and alpha < 1 and concludes 'specV μ < ⊤ ∧ Integrable ...' at excerpt lines 219-222. TeX contains two separate identities at manuscript/notes/notes_stratonovich_ham_second_moment.tex:4704-4707. Exact fix: split row 1074 into a ball-mass-identity proof-step row and a layer-cake/integrability proof-step row, assigning the finiteness and integrability qualifiers only to the latter.
- K4 — Several inherited captions no longer describe the declarations remaining in their rows. candidate/statement-ledger.md:1035,1038 still say 'general form and exact-hypothesis wrapper', but each lists only its paper wrapper; Lean separates 'theorem compact_product_baseline' and 'theorem compact_young_baseline' from their paper wrappers in lean-excerpts/StratonovichHAMSecondMoment/SymplecticFree.lean.excerpt.txt:404-427,444-477. Their TeX targets are the two displays at manuscript/notes/integrated_symplectic_phase.tex:45-58. Similarly, ledger line 1081 describes Gaussian-density and smoothed-covariance notation over only PhaseCovariance.of_homog, whose conclusion is 'PhaseCovariance alpha Γ μ' at lean-excerpts/StratonovichHAMSecondMoment/PhaseContractions.lean.excerpt.txt:139-140. Lines 1084-1085 claim 'the definition of T_eps' over theorem-only lists; for example, 'theorem lintegral_waveGreen_three' proves a spherical integration identity at that excerpt's lines 209-212, whereas TeX defines T_eps as an oscillatory covariance integral at manuscript/notes/notes_stratonovich_ham_second_moment.tex:2081-2084. Exact fix: describe rows 1035 and 1038 as wrappers only; describe row 1081 solely as the implication from H:homog to the standing covariance class; replace the T_eps-definition captions at 1084-1085 with proof-step descriptions applicable to their actual theorem lists.

Findings, minor (0):

Required repairs (4):
- K1: Separate mixed_moment_mono from the input-free row and correct the comparison wrapper's supplied-input description.
- K2: Remove cutoff-removal assumptions from the fixed-cutoff theorem's Index caption.
- K3: Split the radial identity row and assign each declaration its actual conclusion scope.
- K4: Correct the stale wrapper, covariance-class and T_eps-definition captions at lines 1035, 1038, 1081, 1084 and 1085.

Limitations (5):
- Requirement A was completed; partial-file entries concern material outside the required ranges, not gaps in required reading.
- The supplied Lean excerpts contain intentional omissions of original source ranges. All supplied excerpt lines were read; omitted implementation and proof bodies were not independently inspected.
- This review concerns documentation correspondence for the specified 83 rows, not proof correctness, package-wide counts, or a complete documentation audit.
- No Lean build, generator execution, network access, or independent provenance-hash verification was performed.
- An AI review is not human verification or a novelty audit.

## i8-index-1086-1161

Preflight: contract-check CONTRACT-OBSERVABLE (14 required field(s), 0 dispatch input(s); no provider call); dry run exit 0 (dryrun/); contract-check with --dispatch-input dryrun/prompt.txt CONTRACT-OBSERVABLE (14 required field(s), 1 dispatch input(s); no provider call)

Driver log:
```
2026-11-12T18:36:49Z start attempt-01
2026-11-12T18:42:44Z attempt-01 exit=2 Status: review-complete
2026-11-12T18:42:44Z done
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
- INDEX-CELLS lines 1086-1161: FAIL: The principal whole/narrower classifications, M1 disclosures, occupation restrictions, and finite-word restriction agree with the supplied statements. However, the regenerated ComplexPhaseScalar cells retain qualifiers describing declarations no longer in their rows (1124-1127), and the supplied-input inventory at 1129 omits the essential hQ' identity. See K1-K2. The mechanical zero-problem output does not establish these semantic claims.

Findings, fatal (0):

Findings, major (2):
- K1 — ComplexPhaseScalar supplied-input inventory, candidate/statement-ledger.md:1129. The cell lists hCPC, hCPF, hCPH, hJ and hJm but omits hQ'. Lean explicitly requires '(hQ' : Q' - 1 = (1 / π) • ∫ t in Ioi (0 : ℝ), J t)' in lean-excerpts/StratonovichHAMSecondMoment/ComplexPhaseScalar.lean.excerpt.txt:635-638 (original Lean 1257-1260). This is the inverse-root representation corresponding to the TeX identity 'Q_z-1 = (1/π)∫ …' at manuscript/notes/notes_stratonovich_ham_second_moment.tex:2333-2336, not a dispensable side condition. Measurability and domination of J alone do not constrain the independently supplied Q'. Exact fix: add hQ' and its representation identity to row 1129's supplied hypotheses. The generator's binder inventory at tools/decltable.py:15 recognizes hQ but not hQ', explaining why the mechanical check misses this omission.
- K2 — ComplexPhaseScalar split rows retain an omnibus two-layer qualifier, candidate/statement-ledger.md:1124-1127. Each row still describes both 'the numerical-range layer with nothing supplied' and 'the propagator layer with the named inputs', although each now lists only one layer's declaration. In particular, complex_phase_range_paper concludes only '∀ w ∈ numRange …, PhaseRangeBounds …' (lean-excerpts/StratonovichHAMSecondMoment/ComplexPhaseScalar.lean.excerpt.txt:596-601), and interval_complex_range_paper concludes the adjoint sandwich bound and PhaseRangeBounds (611-617); neither concludes a weighted-block bound. The manuscript distinguishes the numerical-range calculations at manuscript/notes/notes_stratonovich_ham_second_moment.tex:2373-2429 and 2948-2958 from the block/propagator bounds at 2433-2464 and 2959-2964. Exact fix: describe rows 1124 and 1126 as numerical-range/scalar conclusions only, with nothing supplied and no block or propagator bound; describe rows 1125 and 1127 solely as supplied-input weighted-block conclusions, retaining the missing propagator identification and, where applicable, interval telescoping. The correct section-level explanation at candidate/statement-ledger.md:1854-1882 does not satisfy the contract's per-cell requirement.

Findings, minor (0):

Required repairs (2):
- Disclose the essential hQ' inverse-root representation hypothesis in Index row 1129.
- Replace the inherited two-layer qualifiers in Index rows 1124-1127 with declaration-specific conclusion and supplied-input descriptions.

Limitations (3):
- Requirement A was completed without gaps. Other ledger, coverage and manuscript material was read selectively; unlisted ranges of those partial files were not reviewed.
- Lean excerpts were read completely as supplied; their marked omissions were not available for inspection.
- This review concerns documentation correspondence, not proof correctness, a Lean rebuild, packet-wide count certification, human verification or novelty.

