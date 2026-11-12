# Wave L9 re-review round 4 (strict categories, split modelled-object rule): summary

Companion e2c50b5 (wave-l9/repair; round-3 repairs and the split modelled-object rule, docs only; reviewed commit d5667f5), manuscript a284420; reviewer Codex gpt-6.1-sol, effort high, min-confidence high, --source-revision e2c50b5. Packets built by scratchpad/build-l9-reconfirm4.py. Every finding below is verbatim from report.json.

Packets: h1/h2 the 17 changed ledger headings; h3 the three M1 whole-result sections, the register text and the missing-construction moves; h4a-h4d the Index-by-label table in pieces of 99 rows with only the named Lean declarations (numbered excerpts) and module headers; h5 round-3 findings, classification consistency of counts, no new overclaim in d5667f5..e2c50b5, earlier repairs kept. Retry only on tool failure, recorded in the driver log.

## h1-changed-headings-a

Preflight: contract-check CONTRACT-OBSERVABLE (14 required field(s), 0 dispatch input(s); no provider call); dry run exit 0 (dryrun/); contract-check with --dispatch-input dryrun/prompt.txt CONTRACT-OBSERVABLE (14 required field(s), 1 dispatch input(s); no provider call)

Driver log:
```
2026-11-12T16:40:47Z start attempt-01
2026-11-12T16:46:55Z attempt-01 exit=2 Status: review-complete
2026-11-12T16:46:55Z done
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
Check verdicts: PASS 8, FAIL 1 (of 9)

Checks not PASS/PASS_WITH_NOTES:
- HEADING L8Completed: FAIL: Category B is correct, and the substitutions and chain-measure boundary are repaired. However, the aggregate heading still does not name every missing conclusion: the occupation-energy form of the ceiling and Q_2 >= S_2^pos remain absent. Lean's completed ceiling and positive-score wrappers conclude only the surrogate ceiling and variational supremum facts (L8Completed.lean:128-168); TeX additionally concludes the occupation-energy equality and point-liminf inequality (manuscript/notes/integrated_occupation_ceiling.tex:214-215; manuscript/notes/integrated_unmasked_variational.tex:279). Both omissions are explicitly retained elsewhere in the candidate, including Index cells 827-828 and section lines 3584-3594,3622. See K1.

Findings, fatal (0):

Findings, major (1):
- K1 — L8Completed's aggregate narrower heading is still incomplete. Lean concludes 'sSup (scoreSet ...) ≤ ... ceilingValue ... (K0 ... * Rsp ...)' (lean/StratonovichHAMSecondMoment/L8Completed.lean:149-154) and positive, homogeneous variational suprema (:163-168). TeX additionally asserts '= c^m(2 zeta)^(alpha/(2k)) F_0(E_zeta^O)' (manuscript/notes/integrated_occupation_ceiling.tex:214-215) and 'Q_2 >= S_2^pos' (manuscript/notes/integrated_unmasked_variational.tex:279). Neither conclusion appears in those Lean wrappers. The heading at candidate/statement-ledger.md:3541 does not name these omissions, although its Index cells :827-828 and prose :3584-3594,3622 do. Substitution of energyValue for E_(1/2)^O in the bracket comparison does not describe the missing general-zeta ceiling equality. Exact fix: append 'the occupation-energy form of the ceiling and Q_2 >= S_2^pos not formalized' to the L8Completed heading, retaining its existing substitutions and identification qualifications.

Findings, minor (0):

Required repairs (1):
- Complete the L8Completed heading by explicitly naming the unformalized occupation-energy form of the ceiling and Q_2 >= S_2^pos, as specified in K1.

Limitations (6):
- Requirement A's required selections were read completely; partial-file entries omit unrelated material or proof bodies, not required wrapper signatures or scope passages. Truncated outputs were reread.
- The review covers the nine specified heading claims, not an exhaustive recertification of all Index cells, aggregate counts or other ledger sections.
- Proof correctness, compilation and kernel replay were outside scope; no build was run.
- Packet hashes, repository history and source-revision byte bindings were not independently authenticated.
- No incorrect numerical constant was identified in the checked correspondence. The blocking finding concerns completeness of the prescribed heading qualification.
- This AI correspondence review is not human verification or a novelty audit.

## h2-changed-headings-b

Preflight: contract-check CONTRACT-OBSERVABLE (14 required field(s), 0 dispatch input(s); no provider call); dry run exit 0 (dryrun/); contract-check with --dispatch-input dryrun/prompt.txt CONTRACT-OBSERVABLE (14 required field(s), 1 dispatch input(s); no provider call)

Driver log:
```
2026-11-12T16:40:47Z start attempt-01
2026-11-12T16:45:54Z attempt-01 exit=0 Status: review-complete
2026-11-12T16:45:54Z done
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
Check verdicts: PASS 8 (of 8)

Findings, fatal (0):

Findings, major (0):

Findings, minor (0):

Required repairs (0):

Limitations (4):
- Requirement A was completed; truncated required passages were reread. Partial-file coverage excludes unrelated sections or proof bodies, not required selections.
- Acceptance concerns exactly the eight contracted headings and their relevant correspondence evidence. Aggregate counts, the entire Index, claims.yaml and unrelated classifications were not independently recertified.
- No Lean build, proof-correctness audit, provenance-hash verification or complete-diff certification was performed.
- This AI correspondence review is not human verification or a novelty audit.

## h3-m1-register

Preflight: contract-check CONTRACT-OBSERVABLE (14 required field(s), 0 dispatch input(s); no provider call); dry run exit 0 (dryrun/); contract-check with --dispatch-input dryrun/prompt.txt CONTRACT-OBSERVABLE (14 required field(s), 1 dispatch input(s); no provider call)

Driver log:
```
2026-11-12T16:40:47Z start attempt-01
2026-11-12T16:46:24Z attempt-01 exit=2 Status: review-complete
2026-11-12T16:46:24Z done
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
Check verdicts: PASS 3, FAIL 2 (of 5)

Checks not PASS/PASS_WITH_NOTES:
- REGISTER-TEXT: FAIL: The ledger register at candidate/statement-ledger.md:62-93 accurately describes WaveGreen.lean:26-34,106-111, and its three M1 sections name the model. However, the required counterparts are incomplete: lean/README.md:106-117 merely takes Mathlib's sphere measure as surface measure, without identifying M1, disclosing the unproved identification, or stating the split rule. lean/FORMALIZATION.md:90-105 references the register and summarizes the distinction, but omits the requirement that the exceptional model be named. See K1.
- MISSING-CONSTRUCTIONS: FAIL: The specified repairs are present: narrower headings at candidate/statement-ledger.md:3115,3541,5199,7739; narrower principal Index cells at :555,641,712,835; weaker coverage with matching scope mirrors at lean/coverage.yaml:756-795,984-1006,1263-1300 and docs/coverage-scope-tex.yaml:50-52,71-73,98-100. Nevertheless, the mandated whole-section search exposes further unregistered missing constructions. RadiusMeanAnchor explicitly leaves M_R and residual noises unconstructed (:5385-5413), while its wrapper takes arbitrary M (RadiusMeanAnchor.lean:458-469). TypeContinuity uses arbitrary mom rather than constructed solution moments (TypeContinuity.lean:957-976,1106-1110,1141-1145). Their whole headings and full coverage remain inconsistent with the split rule. See K2-K3.

Findings, fatal (0):

Findings, major (3):
- K1 REGISTER-TEXT — The required register counterparts are incomplete. Lean defines waveGreen 3 using 'ENNReal.ofReal (s / (4 * π))' and 'volume.toSphere.map' (lean/StratonovichHAMSecondMoment/WaveGreen.lean:106-111), explicitly saying that neither surface-measure identification is proved (:26-34). TeX uses 'sigma_h is surface measure on the sphere of radius h' (manuscript/notes/notes_stratonovich_ham_second_moment.tex:5184-5186). lean/README.md:106-117 omits this unproved-identification boundary and the registered-choice/missing-construction split; lean/FORMALIZATION.md:90-105 omits the named-model requirement. Exact fix: add an explicit M1 description or explicit M1-register reference with the surface-measure disclaimer in README, and state in both counterparts that registered standard choices preserve whole status only with the model named, whereas missing constructions require narrower status.
- K2 RadiusMeanAnchor — An additional missing construction remains classified whole. Lean takes '(M : ℕ → Ω → ℝ → E)' and moment/measurability hypotheses, then bounds expressions formed from M (lean/StratonovichHAMSecondMoment/RadiusMeanAnchor.lean:458-485); its module explicitly abstracts 'M_R, Y_m, W' to arbitrary paths (:17-19). TeX instead defines 'X_m(u)=g_delta M_R(Y_m)(min(u,ell_m))' for the specific residual noises (manuscript/notes/integrated_radius_anchor.tex:280-304). candidate/statement-ledger.md:5411-5413 expressly says the operator-path and residual-noise constructions are not formalized, yet :5362 and Index :537 say whole, and lean/coverage.yaml:1402-1411 says full. M1 does not cover these objects. Exact fix: classify this result as narrower for arbitrary random paths, naming the missing M_R(Y_m)/residual-noise construction and identification; update the heading, principal Index cell, coverage conclusion to weaker, scope sentence and TeX mirror, retaining the named moment inputs.
- K3 TypeContinuity — The two stochastic moment results retain an unregistered abstract-object substitution. Lean quantifies '(mom : ℕ → ℝ → ℝ → ℝ)' with TypeContinuityInputs and concludes growth properties of mom (lean/StratonovichHAMSecondMoment/TypeContinuity.lean:957-976,1106-1122,1141-1160); its modelling disclosure calls the moment an 'abstract real function' (:46-49). TeX defines the rates through 'log E[u^(a)(T,x)^p]' and states the proposition and corollary for those rates (manuscript/notes/notes_stratonovich_ham_second_moment.tex:7505-7528,7574-7593). The supplied coefficient, interpolation and asymptotic facts do not construct the solution moments or formalize their identification with mom. Nevertheless candidate/statement-ledger.md:7603,7634-7638 and Index :696-697 classify them whole, with full coverage at lean/coverage.yaml:99-100,1346-1347. Exact fix: classify these two results as narrower for abstract moment functions, naming the missing solution-moment construction/identification; update their Index and coverage entries with weaker conclusions and matching scope mirrors. Retain the independent whole classification of L:positive-series-type.

Findings, minor (0):

Required repairs (4):
- Complete the README and FORMALIZATION register counterparts as specified in K1.
- Reclassify P:radius-mean-anchor consistently as the narrower arbitrary-path result, with the missing physical construction disclosed in its heading, Index, coverage scope and TeX mirror.
- Reclassify P:moment-growth-logconvex and C:static-moment-constant-continuity consistently as narrower abstract-moment results, preserving L:positive-series-type as whole.
- Synchronize the affected Scope, README, FORMALIZATION, COMPLETION and coverage summaries and module/result counts after those reclassifications.

Limitations (5):
- Requirement A was completed; partial-file coverage outside its required selections is identified above. Other whole-result sections were searched for the stipulated phrases, not exhaustively re-reviewed declaration by declaration.
- The observed heading tally is 26 whole, 30 narrower and 34 foundation/proof-step sections. Aggregate theorem/definition inventory counts were not independently recertified.
- Proof correctness, compilation and kernel replay were outside scope. No build was run.
- PROVENANCE byte bindings, repository history and the complete documentation diff were not independently authenticated.
- This is an AI correspondence review, not human verification or a novelty audit.

## h4a-index-501-599

Preflight: contract-check CONTRACT-OBSERVABLE (14 required field(s), 0 dispatch input(s); no provider call); dry run exit 0 (dryrun/); contract-check with --dispatch-input dryrun/prompt.txt CONTRACT-OBSERVABLE (14 required field(s), 1 dispatch input(s); no provider call)

Driver log:
```
2026-11-12T16:40:47Z start attempt-01
2026-11-12T16:46:35Z attempt-01 exit=2 Status: review-complete
2026-11-12T16:46:35Z done
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
- INDEX-CELLS lines 501-599: FAIL: Thirty-seven first cells omit every prescribed category term, contrary to candidate/statement-ledger.md:62-79 and lean/FORMALIZATION.md:95-105. Examples include the explicitly incomplete cost and Rayleigh identifications at ledger:549-550. The repaired IndexedCone cell at ledger:555 correctly retains the abstract-family limitation, consistent with coverage.yaml:755-796 and IndexedCone.lean.excerpt.txt, original lines 989-1011; the M1 exception does not excuse the uncategorized cells.
- INDEX-MAPPING lines 501-599: FAIL: Ledger:545 assigns L:variational-control-dilation to seven integrability-transfer auxiliaries while expressly admitting they are not stated in TeX. The authoritative statement and proof, manuscript/notes/integrated_unmasked_variational.tex:225-268, contain dilation identities and a positive-Tonelli argument, not these conditional integrability equivalences. VariationalDilation.lean.excerpt.txt, original lines 60-62 and 428-458, independently confirms this distinction. Under the requested correspondence criterion, this row needs 'no direct label'.

Findings, fatal (0):

Findings, major (2):
- K1 — Missing Index categories. At candidate/statement-ledger.md:527,531-533,536,540-541,543,545-552,554,556-564,568-570,572-573,580,584-585,590,594,598, the first cells contain none of 'whole result', 'narrower result', 'foundation', or 'proof steps' (37 cells). This violates the explicit rule at ledger:79. For example, original Lean lines 239-240 in lean-excerpts/StratonovichHAMSecondMoment/VariationalDilation.lean.excerpt.txt define 'rawCost' solely by an integral, whereas manuscript/notes/integrated_compact_mean_family.tex:409-410, reproduced in excerpts/tex-excerpts.txt, states 'v_Psi := E Z^2 = [integral]'. Ledger:549 acknowledges the missing stochastic identification but omits category B. Fix: give every listed cell an explicit applicable category; specifically make :549 'narrower result: integral-form cost only; identification with E W(Psi)^2 not formalized' and :550 'narrower result: Rayleigh-form rate only; spectral-bottom identification not formalized'. Use category C for unlabelled auxiliaries and supplied-field foundations, and split mixed rows where necessary.
- K2 — Incorrect direct label for Lean-only integrability transfers. Candidate/statement-ledger.md:545 labels the auxiliaries L:variational-control-dilation. Lean explicitly says 'integrability transfers are additional Lean-route statements, not steps of the TeX proof' (lean-excerpts/StratonovichHAMSecondMoment/VariationalDilation.lean.excerpt.txt, original lines 60-62); the companion theorem states conditional 'Integrable ... ↔ Integrable ...' conclusions at original lines 438-458. In contrast, authoritative TeX says 'Positive Tonelli applies this identity inside the temporal convolution' (manuscript/notes/integrated_unmasked_variational.tex:249-250), and its complete statement/proof at :225-268 does not state these equivalences. Fix the first cell to 'no direct label (foundation: Lean-route integrability-transfer auxiliaries supporting L:variational-control-dilation; conditional transfers only)'. The supporting-result reference may remain, but not as the direct manuscript label.

Findings, minor (0):

Required repairs (2):
- Add explicit, substantively correct category wording to all 37 first cells identified in K1, retaining missing-identification and supplied-input qualifications.
- Replace the direct manuscript-label assignment at candidate/statement-ledger.md:545 with the unlabelled-foundation wording specified in K2.

Limitations (4):
- Requirement A was completely read. Full-file coverage was not required for the ledger, coverage.yaml, or authoritative manuscripts; their unread portions lie outside the reported ranges.
- Complete reading of the supplied Lean excerpts does not supply omitted source text. In particular, the displayed types of DampedNorms.damped_norms_finite_paper, ClockCopyHomog.damped_norms_finite_paper, and VariationalDilation.variational_control_dilation_paper stop before their complete conclusions. This limits exhaustive positive certification, but does not affect the demonstrated failures.
- Lean citations above use the original source numbers printed inside excerpt files; source_coverage uses physical packet-file line numbers.
- This is a documentation-correspondence review, not proof checking, human verification, or a novelty audit.

## h4b-index-600-698

Preflight: contract-check CONTRACT-OBSERVABLE (14 required field(s), 0 dispatch input(s); no provider call); dry run exit 0 (dryrun/); contract-check with --dispatch-input dryrun/prompt.txt CONTRACT-OBSERVABLE (14 required field(s), 1 dispatch input(s); no provider call)

Driver log:
```
2026-11-12T16:40:47Z start attempt-01
2026-11-12T16:48:30Z attempt-01 exit=2 Status: review-complete
2026-11-12T16:48:30Z done
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
- INDEX-CELLS lines 600-698: FAIL: All 99 rows and the required category rules were read. Sixty-six first cells lack an explicit category required by candidate/statement-ledger.md:62-79. Row 610 incorrectly applies 'no supplied input' to an abstract theorem retaining hmem and hnorm (MaskedContinuousWave.lean.excerpt.txt:253-266). Several whole-result cells disagree with their narrower section headings, and the damped-norm wrappers omit more than the stated smoothing qualification. M1 was treated as the registered standard construction, not as a missing construction.
- INDEX-MAPPING lines 600-698: INCONCLUSIVE: The visible principal mappings agree with the manuscript statements and proofs, including the explicitly restricted covariance-functional and spectral-side readings. However, the packet does not expose every listed declaration's statement. In particular, the six internal helpers named at candidate/statement-ledger.md:602 are absent from the completely read OccupationKernelRow.lean.excerpt.txt:1-173. Some supplied signatures also stop before their conclusions finish, for example DampedNormsHomog.lean.excerpt.txt:414-418. Their hypotheses and exact correspondence cannot be independently certified from this packet.

Findings, fatal (1):
- K1 — False input-free qualifier at candidate/statement-ledger.md:610. The row combines the completed theorem with masked_continuous_wave_paper under 'whole result; no supplied input'. Lean explicitly retains '(hmem : ...)' and '(hnorm : ...)' in lean-excerpts/StratonovichHAMSecondMoment/MaskedContinuousWave.lean.excerpt.txt:253-266 (embedded Lean lines 395-408). The manuscript instead uses the concrete completion: 'Lemma ... makes it continuous in H_a' and 'the averages are Bochner integrals' at manuscript/notes/integrated_covariance_foundation.tex:404-407. Fix: separate the completed input-free theorem from the abstract wrapper, and disclose hmem, hnorm and the abstract E/V/emb boundary for the latter; completion must not retroactively remove its hypotheses.

Findings, major (3):
- K2 — Missing explicit Index categories. The 66 affected rows are candidate/statement-ledger.md:600,602-605,607-609,611,616-619,621,623-625,627,629-631,633-640,642-645,649-651,653,655-656,659-664,666-678,681-684,689,692,694,698. Descriptions such as 'auxiliary', 'definition' and 'finite Gaussian comparison only' do not use the required category words. For example, Lean defines 'nu ... := volume.withDensity (rho ...)' at lean-excerpts/StratonovichHAMSecondMoment/MaskedAuxiliaryNorm.lean.excerpt.txt:259-261, corresponding to 'nu_R(d eta) = rho_R(eta) d eta' at manuscript/notes/integrated_covariance_foundation.tex:83-86; its auxiliary setup is distinct from the proposition. Fix: explicitly classify every affected first cell as whole result, narrower result with its missing content, or foundation/proof steps with its precise scope, consistently with the holding section.
- K3 — Unqualified whole-result cells conflict with narrower holding sections. candidate/statement-ledger.md:613-614,622,646-647,652 say 'whole result', whereas their sections at 3822,1897,8612 are narrower and do not name these as separate whole results. For example, Lean's 'def rho' and 'def nu' at lean-excerpts/StratonovichHAMSecondMoment/MaskedAuxiliaryNorm.lean.excerpt.txt:256-261 correctly encode the measure display at manuscript/notes/integrated_covariance_foundation.tex:83-86, but that does not make them the whole auxiliary-norm proposition, whose real-H clause is at line 99. Fix: classify these cells as proof steps specifying the fully covered displays, or explicitly separate whole-result sections and corresponding full coverage entries; do not leave the category disagreement unresolved.
- K4 — Incomplete damped-norm narrowing at candidate/statement-ledger.md:620,639 and heading 1897. The heading names only the covariance-smoothing identification; row 639 excludes only the smoothing remark. Yet Lean's conclusions are only 'N2onSq ... <= N2onSq ...' and 'N1on ... <= N1on ...' at lean-excerpts/StratonovichHAMSecondMoment/DampedNormsHomog.lean.excerpt.txt:341-347,356-362. The TeX also states '0 <= N_{1,m,S}' and '0 <= N_{2,m,S}^2' at manuscript/notes/notes_stratonovich_ham_second_moment.tex:838-839. The excerpt expressly records these lower bounds as absent from the wrapper at physical lines 406-413. Fix: state explicitly that these particular wrappers omit the general multiplier lower bounds as well as the relevant smoothing identification, classify row 620 as narrower rather than merely mentioning proof steps, and remove row 639's implication that smoothing is the only missing conclusion.

Findings, minor (0):

Required repairs (4):
- Separate the completed and abstract declarations in Index row 610 and disclose the abstract wrapper's retained hmem and hnorm inputs.
- Add explicit, section-consistent categories to all 66 first cells identified in K2, naming or explicitly referencing missing content for every narrower-result cell.
- Resolve the whole-result versus narrower-section disagreements in rows 613-614,622,646-647,652 without overstating the covered displays.
- Correct the damped-norm heading and Index qualifications to disclose the general multiplier lower bounds absent from the listed wrappers.

Limitations (3):
- Requirement A was completed for the supplied files and required ranges. Partial-file entries outside those ranges are intentional contextual reads, not gaps in the required reading.
- The frozen Lean excerpts omit six internal helper statements listed in row 602 and portions of several other signatures. Complete file reading cannot recover omitted source text; the universal mapping check therefore remains inconclusive.
- No proof checking, repository-wide count audit, human verification or novelty audit was performed. No incorrect numerical constant was identified in the visible correspondence examined.

## h4c-index-699-797

Preflight: contract-check CONTRACT-OBSERVABLE (14 required field(s), 0 dispatch input(s); no provider call); dry run exit 0 (dryrun/); contract-check with --dispatch-input dryrun/prompt.txt CONTRACT-OBSERVABLE (14 required field(s), 1 dispatch input(s); no provider call)

Driver log:
```
2026-11-12T16:40:47Z start attempt-01
2026-11-12T16:46:41Z attempt-01 exit=2 Status: review-complete
2026-11-12T16:46:41Z done
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
- INDEX-CELLS lines 699-797: FAIL: 57 first cells lack the required category words; others disagree with their section category. Row 764 also applies 'nothing supplied' to declarations explicitly taking GreenMass or GreenFourier inputs. Rows 730-731 describe R_0-specialized bounds although the listed theorems have an arbitrary supplied bound constant R. See K1-K4. The split rule itself supports keeping row 712 narrower: its abstract terminal-chain identification is not registered model choice M1 (Scope:80-93; coverage.yaml:983-1006).

Findings, fatal (0):

Findings, major (4):
- K1 — Missing Index categories. candidate/statement-ledger.md:700-797 contains 57 cells without 'whole result', 'narrower result', 'foundation' or 'proof steps': 700-702,706-707,709-711,713-716,718,720-723,725-727,732-736,741-744,748-750,752,754-759,762-769,773,776,787,790-794,796-797. For example, row 714 is only 'E:uniform-series-tail'. Lean's term_bound explicitly takes 'hsum : Summable ...' and 'hpos : ∀ m n, 0 ≤ inner ...' (lean-excerpts/StratonovichHAMSecondMoment/UniformSeriesTail.lean.excerpt.txt:77-81), whereas TeX states the terminal-family estimates '≤ B_r^{1/2}r^{-n}' (manuscript/notes/notes_stratonovich_ham_second_moment.tex:3718-3723). Fix every listed cell by adding its applicable category or explicit categorized-section reference, preserving the supplied-input and missing-identification qualifications; '(proof)' and 'completion' alone do not satisfy Scope:62-79.
- K2 — Category disagreement with the containing section. Row 788 says 'whole result', but SpatialBracket is headed 'narrower result' at candidate/statement-ledger.md:5875. The listed Lean facts are the scalar 'Fb alpha b 0 = 0' and 'Fb alpha 0 z = F0 alpha z' (lean-excerpts/StratonovichHAMSecondMoment/SpatialBracket.lean.excerpt.txt:143,153), corresponding to TeX's 'define F_b(0) = 0' and 'At b = 0 this is exactly the map' (manuscript/notes/integrated_occupation_ceiling.tex:195-203). Likewise, rows 771,772,774 use 'narrower result' inside the foundation section at ledger:5752; their integral-form identities do not construct the Hilbert-space objects in TeX's '||rho_g||² = A(g)' or '||Psi||² = v_Psi' (integrated_occupation_ceiling.tex:33-37; integrated_intrinsic_constant.tex:33-35). Fix row 788 by explicitly referring to SpatialBracket's narrower-result category while retaining that the scalar map is complete. Reword rows 771,772,774 as foundation/proof-step cells, retaining their integral-form restrictions rather than presenting them as labelled results.
- K3 — 'Nothing supplied' is false for all declarations bundled in row 764. candidate/statement-ledger.md:764 includes damped_homogeneous_norms_full_paper and damped_homogeneous_norms_fourier_paper under that qualifier. Their Lean types explicitly contain '(hG : GreenMass G)' and '(hF : GreenFourier G)' (lean-excerpts/StratonovichHAMSecondMoment/DampedMultiplier.lean.excerpt.txt:375-376,389-390). These are the mass and Fourier identities used in TeX: 'G_s(R^d) = s' and 'Ghat_s(xi) = sin(s|xi|)/|xi|' (manuscript/notes/notes_stratonovich_ham_second_moment.tex:881,777-778). Row 780 similarly calls pair_unit_le 'nothing supplied', although it takes the smooth homogeneous-bound hypothesis 'hR : ∀ g, IsUnitTest g → spatialEnergy Γ g ≤ R * gradEnergy g ^ (alpha / 2)' (OccupationCeilingFinite.lean.excerpt.txt:224-229), corresponding to an inequality used in integrated_occupation_ceiling.tex:117-118. Fix by separating conditional general helpers from discharged wrappers, or explicitly restricting 'nothing supplied' to the latter and naming the retained hypotheses for the former.
- K4 — Incorrect constant specialization in rows 730-731. The cells say 'with R_0 for R_sp' and 'spEnergyVal alpha R_0', but occupation_physical_bound, Jlin_le and occupation_own_energy quantify an arbitrary R and take 'SquarePairingBounds Γ alpha R'; their conclusions contain 'Rstar a D * R' and 'spEnergyVal alpha R' (lean-excerpts/StratonovichHAMSecondMoment/OccupationPhysicalClass.lean.excerpt.txt:295-306,357-363; original Lean:378-382 for Jlin_le). TeX uses 'R_star R_sp' and 'R_star^{2/(2-alpha)} E_sp' (manuscript/notes/integrated_spatial_occupation.tex:395-402). Fix rows 730-731 to describe the general supplied constant R, explain that the paper wrapper specializes R = R_0, and retain the modelled-class qualification and subsequent R_sp/E_sp identification.

Findings, minor (0):

Required repairs (4):
- Supply valid category wording or explicit categorized-section references for all 57 cells identified in K1.
- Resolve the section-category disagreements identified in K2 without upgrading narrower or foundation modules.
- Restrict the 'nothing supplied' qualifiers in rows 764 and 780 to declarations that actually discharge the relevant inputs; disclose the conditional helpers separately.
- Correct rows 730-731 to distinguish their arbitrary supplied constant R from the R_0 specialization and subsequent manuscript-constant identifications.

Limitations (4):
- Requirement A was completed. Files marked partial were read only in the exact ranges listed; unrelated ledger bodies, coverage rows and manuscript passages were not reviewed.
- The supplied Lean excerpts omit material by construction. No compilation or proof-correctness audit was performed; the review concerns documentation correspondence.
- Package-wide counts, documentation outside the two requested checks, and provenance hashes were not independently audited.
- This AI review is neither human verification nor a novelty audit.

## h4d-index-798-895

Preflight: contract-check CONTRACT-OBSERVABLE (14 required field(s), 0 dispatch input(s); no provider call); dry run exit 0 (dryrun/); contract-check with --dispatch-input dryrun/prompt.txt CONTRACT-OBSERVABLE (14 required field(s), 1 dispatch input(s); no provider call)

Driver log:
```
2026-11-12T16:40:47Z start attempt-01
2026-11-12T16:48:27Z attempt-01 exit=2 Status: review-complete
2026-11-12T16:48:27Z done
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
- INDEX-CELLS lines 798-895: FAIL: All 98 rows were read. Sixty-four first cells lack the prescribed category wording; several narrower-result cells state their contents without naming the missing identification. Most decisively, candidate/statement-ledger.md:894 applies 'whole result' to traceT_fourier_completed, which concludes only the Fourier identity, not both contraction bounds (L9Completed excerpt, original Lean lines 134-139 versus 150-183). M1 legitimately preserves the whole-result status of the actual completed wrappers; it does not supply missing conclusions.

Findings, fatal (1):
- K1 — Whole-result overclaim at candidate/statement-ledger.md:894. The first cell says 'whole result with nothing supplied' for all three declarations. However, lean-excerpts/StratonovichHAMSecondMoment/L9Completed.lean.excerpt.txt, original Lean lines 134-139, concludes only 'Integrable ... ∧ traceT ... = ∫ ...'. The labelled TeX lemma also concludes the resolvent and trace bounds: manuscript/notes/notes_stratonovich_ham_second_moment.tex:2075-2079, '≤ R_alpha lambda^(alpha-2)' and '≤ D_Gamma a^(1-alpha)'. Exact fix: separate traceT_fourier_completed into a proof-steps row explicitly limited to the Fourier identity; retain 'whole result with nothing supplied' only for phase_contractions_paper_completed and phase_contractions_homog_completed.

Findings, major (3):
- K2 — Missing prescribed categories in 64 first cells at candidate/statement-ledger.md:799-810,812-814,820,826,829-832,836-842,844-845,847-849,851-855,857,862-863,868-885,888-890,893,895. For example, line 801 says only 'E:terminal-wick-formula (FiniteWick)', although the section heading at 2299 is 'foundation: the finite Wick formula'. Lean defines 'wickSum ... := ∑ p ∈ pairings S, pairWeight ...' (FiniteWick excerpt, original lines 81-83), whereas TeX:3619-3621 states the terminal-chain expectation formula. Likewise, line 875 describes narrower block-map wrappers without saying 'narrower result': Lean's complex_phase_paper bounds a weighted block expression (ComplexPhaseScalar excerpt, original lines 1326-1331), while TeX:2303-2307 bounds the propagator in X_lambda. Exact fix: give every listed cell an explicit whole-result, narrower-result, foundation or proof-steps category, with the applicable restriction or section reference; do not treat 'completion wrapper', 'proof', 'steps of the proof' or 'no direct label' as category substitutes.
- K3 — Narrower-result cells do not consistently name what is missing. At candidate/statement-ledger.md:859-860, the cells describe a general bound and positivity/dilation/scalar steps but omit the unformalized occupation-class bridge and do not explicitly refer to the qualified section heading. Lean quantifies over 'IsOccField G DG' (RawOccupationEnergy excerpt, original lines 137-140,266-270,430-433); TeX uses the 'full strongly H^1-measurable unit-profile class' (manuscript/notes/integrated_occupation_ceiling.tex:7-8). Line 865 similarly says only 'the first scalar maximum' without naming or referring to the section's missing class/rate/cost identifications: Lean concludes an integratedRate inequality (OccupationCeilingExact excerpt, original lines 666-669), while TeX:209-217 states the ceiling and its moment consequence. Exact fix: explicitly reference the corresponding fully qualified section heading in these cells, or state the missing identifications locally.
- K4 — Mixed rows attach supplied-input qualifiers to declarations that do not take those inputs. At candidate/statement-ledger.md:886, 'inputs supplied: ... FockColumn' covers FockColumn itself and fock_const_eq as well as the consumer theorems. Lean's fock_const_eq assumes only 'hR : 0 ≤ R' and 'hρ : 0 < ρ' (FockForm excerpt, original lines 147-149), proving the scalar normalization of TeX's 'd_N=2 sqrt(N+1) sqrt(R_alpha)' at main TeX:2487; it does not assume FockColumn. The row at 816 similarly includes the input-free orderedProd definition under an unqualified 'inputs supplied' description; Lean original lines 383-385 merely define the ordered product appearing in manuscript/notes/integrated_symplectic_phase.tex:53-58. Exact fix: split definitions and input-free scalar helpers from supplied-input consumer theorems, or explicitly scope each input qualifier to the declarations that actually assume it.

Findings, minor (0):

Required repairs (4):
- Split ledger line 894 so that the Fourier-identity declaration is not classified as the whole contraction lemma.
- Add the prescribed explicit categories to the 64 first cells enumerated in K2, preserving each declaration's actual scope.
- Make the missing occupation-class and other applicable identifications explicit, or explicitly reference the qualified section headings, in the cells identified in K3.
- Separate or individually qualify the mixed declaration groups identified in K4 so supplied-input claims are true declaration by declaration.

Limitations (4):
- Requirement A was completed. The ledger and coverage file were read in the required selections rather than in full; unrelated ledger sections, coverage rows and manuscript passages were not comprehensively reviewed.
- Lean citations in findings use the original Lean line numbers printed inside the excerpts; source_coverage gives physical excerpt-file ranges.
- The frozen excerpts intentionally omit portions of the original modules. This review concerns documented correspondence, not proof correctness or a fresh Lean build.
- This AI review is neither human verification nor a novelty audit.

## h5-consistency-diff

Preflight: contract-check CONTRACT-OBSERVABLE (14 required field(s), 0 dispatch input(s); no provider call); dry run exit 0 (dryrun/); contract-check with --dispatch-input dryrun/prompt.txt CONTRACT-OBSERVABLE (14 required field(s), 1 dispatch input(s); no provider call)

Driver log:
```
2026-11-12T16:40:47Z start attempt-01
2026-11-12T16:48:45Z attempt-01 exit=2 Status: review-complete
2026-11-12T16:48:45Z done
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
Check verdicts: PARTIAL 1, PASS 2, FAIL 1 (of 4)

Checks not PASS/PASS_WITH_NOTES:
- ROUND3-FINDINGS: PARTIAL: The substantive heading repairs, explicit coverage conclusion fields, three missing-construction reclassifications, helper-input disclosures and audit-cell repairs are present. M1 justifies retaining the three Green-dependent whole-result headings: candidate/statement-ledger.md:80-93,3634-3636,3690-3692,5031-5033 agree with WaveGreen.lean:26-34,106-111 and L9Completed.lean:96-108,150-183. However, strict Index categorization remains incomplete. In particular, ComplexPhaseScalar's principal cells at ledger:875-876 still lack 'narrower result' or an explicit reference to its category-B heading; the interval cell does not itself name the telescoping omission. Thus adjudication:10's claimed section reference does not implement the stipulated convention. See K1.
- NO-NEW-OVERCLAIM: FAIL: All diff hunks and committed contexts were read. The revised mathematical qualifiers and counts are supported, and no incorrect numerical constant was identified. Nevertheless, the new split Index cells at candidate/statement-ledger.md:752,754-755 use 'completion helper'/'completion wrapper' without any required category words. Moreover, the retained cell:775 labels mere definitions a 'narrower result', contrary to the same foundation-versus-result distinction repaired at:770. These prevent acceptance of the claimed strict Index classification. See K1-K2. MovingCone also retains avoidable 'whole lemma' wording despite its newly narrower reference; see K3.

Findings, fatal (0):

Findings, major (2):
- K1 — Strict Index categories remain incomplete. candidate/statement-ledger.md:79 requires the same category words in Index first cells, but principal ComplexPhaseScalar cells:875-876 have neither 'narrower result' nor an explicit category-B section reference, and newly split cells:752,754-755 likewise have no category. This is not a failure of their displayed inequalities: Lean's interval_complex_paper concludes the weighted block inequality '100 * Real.exp (2 * (Λ * h))' (lean/StratonovichHAMSecondMoment/ComplexPhaseScalar.lean:1370-1375), whereas TeX names the propagator in X_Lambda and 'total loss from changing between these phase norms' (manuscript/notes/notes_stratonovich_ham_second_moment.tex:2909-2915). Lean's completion helper retains 'hsm' (SpatialOccupationL7Completed.lean:85-90), while TeX derives the corresponding Fatou bound inside the proposition's proof (manuscript/notes/integrated_spatial_occupation.tex:270-275). Exact fix: give cells875-876 explicit category-B wording, retaining the propagator gap and naming the interval telescoping gap or explicitly referencing that qualified heading; mark752 as proof steps of P:spatial-four-linear; explicitly categorize754-755 while retaining SquareBound as supplied for the general helpers and nothing supplied for the paper wrapper. Apply the promised category vocabulary consistently to remaining Index first cells rather than treating 'helper', 'wrapper' or a bare module name as a category.
- K2 — A remaining definition cell is incorrectly category B. candidate/statement-ledger.md:775 calls OccupationCeilingFinite.K0 and stForm a 'narrower result' of E:positive-bochner-inclusion, although they merely define the constant and integral form. Lean says 'def K0 ... := 2 ^ a / (1 - a)' (lean/StratonovichHAMSecondMoment/OccupationCeilingFinite.lean:97-99) and 'def stForm ... := ∫ s ... ∫ t ...' (:432-441). TeX instead asserts a bounded map J_G and its norm identity and bound (manuscript/notes/integrated_intrinsic_constant.tex:24-30: '\|J_GF\|^2 = ... \le K_0\|F\|^2'). This is the same foundation-versus-labelled-result distinction correctly repaired for SpaceTimePositivity at ledger:770. Exact fix: change cell775 to 'foundation: definition of K_0 and the iterated physical space-time form only; J_G and its covariance-space norm identity not formalized'.

Findings, minor (1):
- K3 — MovingCone retains contradictory shorthand. candidate/statement-ledger.md:1202-1203 says 'The whole lemma is formalized' immediately before its correctly qualified narrower-result reference;:1207 repeats 'the whole lemma'. Lean actually quantifies '(G : GroundFamily F)' (lean/StratonovichHAMSecondMoment/IndexedCone.lean:996-1009), whereas TeX uses the physical 'O_phi D_N ... e_0' (manuscript/notes/integrated_raw_block_lower.tex:243-247). Because the same passage explicitly discloses the abstraction gap, this is a wording issue. Optional fix: replace 'whole lemma' with 'abstract cone statement' in both places.

Required repairs (2):
- K1: Complete the Index's explicit three-category vocabulary, including the principal ComplexPhaseScalar cells and newly split completion-helper/wrapper cells, preserving their supplied inputs and missing conclusions.
- K2: Reclassify the OccupationCeilingFinite K0/stForm Index cell at candidate/statement-ledger.md:775 as foundation definitions, not a narrower labelled result.

Limitations (5):
- Requirement A was completed. Partial-file entries concern material outside its required selections; unchanged Lean declarations and manuscript statements were not exhaustively recertified.
- Proof correctness, compilation and kernel replay were outside scope and were not performed.
- The claims inventory was parsed for aggregate counts, not reviewed semantically in full.
- Packet hashes and source-revision byte bindings were not independently authenticated.
- This AI correspondence review is not human verification or a novelty audit.

