# Wave L9 correspondence reviews: summary

Companion eb253a5 (eb253a5022fa, branch wave-l9/int: L8 + L9 modules and the L9 docs merge; prior 5ec3c11), manuscript a284420; reviewer Codex gpt-6.1-sol, effort high, min-confidence high, --source-revision eb253a5. Packets built by scratchpad/build-l9-review.py. Every finding below is verbatim from report.json.

Groups (as split before dispatch): g1 WaveGreenFourier+LowAlphaConvolution; g2 PhaseContractions+L9Completed (+Scope/Index/Not-in-Lean changes, totals); g3 RawOccupationEnergy+OccupationCeilingExact; g4 ComplexPhaseScalar; g5a GaussianHermite; g5b HermiteFock; g6a FockForm+HermiteWordFock; g6b the reworded P:static-phase-all-orders and P:interval-coefficients rows and passages. A retry happens only when an attempt is not review-complete (tool failure), recorded in the driver log.

## g1-wave-green-fourier-low-alpha

Preflight: contract-check CONTRACT-OBSERVABLE (14 required field(s), 0 dispatch input(s); no provider call); dry run exit 0 (dryrun/); contract-check with --dispatch-input dryrun/prompt.txt CONTRACT-OBSERVABLE (14 required field(s), 1 dispatch input(s); no provider call)

Driver log:
```
2026-11-12T14:24:40Z start attempt-01
2026-11-12T14:37:25Z attempt-01 exit=2 Status: review-complete
2026-11-12T14:37:25Z done
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
Check verdicts: PASS 66, PARTIAL 2, PASS_WITH_NOTES 2, FAIL 5 (of 75)

Checks not PASS/PASS_WITH_NOTES:
- StratonovichHAMSecondMoment.LowAlphaConvolution.gammaEps: E:low-alpha-convolution: PARTIAL: The definition '∫ y, heatDens ε (x-y) ∂Γ' at LowAlphaConvolution.lean:148-149 matches TeX 'γ_ε=p_ε*γ', manuscript/notes/notes_stratonovich_ham_second_moment.tex:4515, and claims.yaml:15097-15103. However ledger:3646 additionally says integrability is a conclusion of 'every theorem that uses it'. gammaEps_nonneg at Lean:174-176 and gammaEps_spectral at 325-328 have no such conclusion. W2 requires narrowing that sentence to integrable_heatDens and the appropriate wrappers.
- PARA-LowAlphaConvolution: PARTIAL: The constants, closed-ball V, origin convention, εI normalization, supplied Fourier input, field usage and uniform quantifiers in ledger:3558-3641 are otherwise accurate. However ledger:3587-3589, 3618 and especially 3646 overgeneralize integrability conclusions: gammaEps_spectral (LowAlphaConvolution.lean:325-328) is an equality only, unlike smoothed_pairing_spectral:394-403 and the final wrappers. See W2.
- COVERAGE-ROWS: FAIL: All listed claim IDs exist. The low-alpha and phase-contractions same-assumptions/full rows are supported by L9Completed.lean:96-110, 150-184. The damped-norm row's 'conclusion: full' at lean/coverage.yaml:237 is not supported: its own note at 281-283 reduces covariance smoothing to factor membership, whereas TeX:845-846 asserts the actual smoothing operation gives that multiplier. WaveGreenFourier closes the d=2,3 Green gap, not this omitted covariance-identification conclusion among the cited declarations. W1.
- CROSS-REFERENCES: FAIL: The L9Completed and PhaseContractions cross-references correctly discharge the two Fourier/sphere inputs, and ledger:8742-8750 correctly distinguishes pointwise covariance representation from spectral-measure identification. Nevertheless the Scope, Index and earlier sections still call L:damped-homogeneous-norms full, or attribute the full lemma to full_wave alone, despite the narrower cited conclusions. Occurrences and repairs are enumerated in W1.
- L8-PATTERNS: FAIL: Patterns (a) and (d) remain: lean/coverage.yaml:237; candidate/statement-ledger.md:200-207, 247-248, 573, 696, 1639-1642, 1796, 1830-1831, 1855-1859, 1916-1918, 8112-8113, 8194-8196 overstate whole-lemma coverage or attribute it to insufficient wrappers. W2 additionally identifies an overly broad integrability summary at ledger:3587-3589, 3618, 3646. No undisclosed added manuscript restriction of pattern (b), or convention-free description of the totalized controls in pattern (c), was found.
- CHANGED-ROW L:damped-homogeneous-norms: FAIL: diffs/coverage.diff:130-156 changes weaker to full, deletes the scope and adds two WaveGreenFourier claims; diffs/coverage-scope-tex.diff:16-18 removes the companion scope entry. The added declarations at WaveGreenFourier.lean:736-766 genuinely close the Green-Fourier identification in d=2,3. They do not state covariance-smoothing spectral identification. The old covariance-membership limitation survives in coverage.yaml:281-283 and ledger:1709-1713, so deleting all narrowing is unjustified. W1.
- CHANGED-PASSAGE WaveGreen (whole result): FAIL: The Fourier-extension updates themselves are correct. However the revised paragraph, candidate/statement-ledger.md:8186-8196 (diffs/statement-ledger-changed-sections.diff:233-254), still concludes 'The full lemma with nothing supplied is ...damped_homogeneous_norms_full_wave'. That declaration at DampedMultiplier.lean:547-585 neither identifies its Green norm with N2onSq nor states the covariance-smoothing spectral identity. TeX:845-846 asserts both operations. The paragraph must describe the actual combination of results and remaining limitation. W1.

Findings, fatal (1):
- W1 — L:damped-homogeneous-norms is incorrectly classified and summarized as fully formalized. TeX manuscript/notes/notes_stratonovich_ham_second_moment.tex:845-846 says 'Spatial Gaussian smoothing and Gaussian smoothing of the Green kernel give multipliers in this class.' The cited Lean full wrapper concludes only '∀ η, 0 ≤ η → IsMultiplier (gaussMult η)' and Green-family smoothing identities (DampedMultiplier.lean:573-584); its documentation explicitly says the covariance spectral identity 'is not stated' (458-459). WaveGreenFourier.lean:753-766 correctly supplies the missing Green identification in d=2,3, but does not add covariance identification. LowAlphaConvolution.lean:325-328 now proves a useful pointwise representation; this is neither the claimed spectral-measure statement nor a conclusion of the damped-norm row's cited declarations. The limitation is disclosed at candidate/statement-ledger.md:1709-1713, 8742-8750 and lean/coverage.yaml:281-283, yet contradicted by coverage.yaml:237 and ledger:200-207, 247-248, 573, 696, 1639-1642, 1796, 1830-1831, 1855-1859, 1916-1918, 8112-8113, 8194-8196. Exact fix: retain same-assumptions but change the coverage conclusion to weaker, restore matching plain-English ASCII/TeX scope sentences describing the covariance-identification gap and successful three-dimensional Green extension, and qualify these whole-lemma/full_wave summaries. Alternatively, prove and cite the missing covariance-identification conclusion and cite the Fourier wrapper wherever its Green identification is claimed.

Findings, major (1):
- W2 — The LowAlphaConvolution ledger overstates integrability conclusions. candidate/statement-ledger.md:3646 says integrability is 'a conclusion of every theorem that uses' gammaEps; related blanket wording appears at 3587-3589 and 3618. In contrast, LowAlphaConvolution.lean:325-328 assumes only 'IsSpectralMeasure Γ μ', '0 < ε' and x and concludes an equality, with no Integrable conjunct; gammaEps_nonneg:174-176 also concludes only nonnegativity for arbitrary Γ. TeX manuscript/notes/notes_stratonovich_ham_second_moment.tex:4736-4738 explicitly justifies Fourier Fubini under the standing tempered/Radon assumptions. The final wrappers do supply genuine integrability, so the lemma's bound is not refuted. Exact fix: say that integrable_heatDens:311-319 supplies the inner integrability under tempered Γ and ε>0, that smoothed_pairing_spectral:394-403 and the final wrappers include the relevant integrabilities, and that gammaEps_spectral alone is an identity of Lean integrals without an integrability conclusion.

Findings, minor (2):
- W3 — candidate/statement-ledger.md:8300-8301 says radial2 s r vanishes for 'r >= s' without stating s>=0. The actual supporting theorem WaveGreen.lean:159 requires 'hs : 0 ≤ s' and 'hr : s ≤ r'; for negative s the unqualified assertion is false. TeX's density is used at positive h, manuscript/notes/notes_stratonovich_ham_second_moment.tex:4703, 5182-5183, so this does not affect the reviewed Fourier results. Optional fix: write 'for 0 <= s <= r' or explicitly restrict the sentence to positive time and radial r.
- W4 — lean/refutations/wave-green-fourier/ArchimedesUnit.lean:7-9 says the proof uses the package law at a unit vector to obtain nonzero sphere mass. The actual proof at 31-40 uses Measure.toSphere_ne_zero directly. TeX's normal-coordinate discussion at manuscript/notes/notes_stratonovich_ham_second_moment.tex:2125-2131 is unaffected, and the counterexample is valid. Optional fix: correct the proof-route comment; no theorem change is needed.

Required repairs (2):
- Repair W1: remove the unsupported full classification and whole-lemma/full_wave summaries, restoring an accurate covariance-smoothing limitation in lean/coverage.yaml and matching docs/coverage-scope-tex.yaml scope text; or add and cite the missing formal covariance-identification result. Preserve the correctly proved d=1,2,3 Green-smoothing extension.
- Repair W2: replace blanket integrability-conclusion assertions in the LowAlphaConvolution section, particularly candidate/statement-ledger.md:3646, with declaration-specific statements distinguishing gammaEps_spectral's equality from the integrability conclusions of integrable_heatDens, smoothed_pairing_spectral and the final wrappers.

Limitations (6):
- The contracted complete-reading requirement A was completed for the target modules, required ledger sections, module claim entries, coverage rows, relevant change hunks, audits, refutations and cited manuscript ranges. Partial contextual-file coverage above does not assert review of their unrelated declarations.
- PROVENANCE.json was inspected only partially; lines 76-1864 were not systematically read after the initial truncated display. manuscript-anchor.json was inspected at lines 1-85 and matching revision-history lines only. No complete byte-binding or provenance audit is claimed.
- Manuscript-wide searches established cited-label uniqueness; unrelated manuscript statements, earlier-wave results and external source literature were not re-reviewed.
- Compilation and standard-axiom status were supplied by the contract, not independently rerun. The audit files contain #check/#print directives rather than captured elaboration output.
- The d=3 identification with Hausdorff or Riemannian surface measure is not proved in the packet; the disclosed Euclidean cone-measure model has the correct 4π normalization and Fourier law.
- This AI correspondence review is not human verification or a novelty audit.

## g2-phase-contractions-l9completed

Preflight: contract-check CONTRACT-OBSERVABLE (14 required field(s), 0 dispatch input(s); no provider call); dry run exit 0 (dryrun/); contract-check with --dispatch-input dryrun/prompt.txt CONTRACT-OBSERVABLE (14 required field(s), 1 dispatch input(s); no provider call)

Driver log:
```
2026-11-12T14:24:40Z start attempt-01
2026-11-12T14:38:47Z attempt-01 exit=3 Status: review-complete
2026-11-12T14:38:47Z done
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
Check verdicts: PASS 56, PASS_WITH_NOTES 2, PARTIAL 1, FAIL 2, INCONCLUSIVE 2 (of 63)

Checks not PASS/PASS_WITH_NOTES:
- PARA-PhaseContractions: PARTIAL: The objects, constants, source ranges, discharged inputs and principal conclusions at candidate/statement-ledger.md:4864-4921,4932-4954 match the sources. However, :4923-4925 asserts integrability of every integrand is a conclusion and excludes all junk-integral statements. PhaseContractions.lean:192-194,772-774,976-979 do not conclude integrability under their unrestricted hypotheses. This material scope error is W1.
- REFUTATIONS: FAIL: MiddleRegionExponent.lean:26-39 and NormalCoordinateConstant.lean:27-40 give genuine in-domain numerical contradictions with the stated perturbations. ShiftInvariance.lean:9-12,26-43 instead uses d=1, Gamma=Lebesgue and μ=δ0; this is outside TeX:2054-2057's d=3,0<alpha<2 class and corresponds to homogeneity alpha=0. It refutes the broader Lean-only equality variant, not equality under the manuscript's standing class. The ledger supplies no description making that distinction. See W2.
- CROSS-REFERENCES: INCONCLUSIVE: The checked references at candidate/statement-ledger.md:236-248,2299,2408,3556-3675,8232-8348,8742-8750 accurately distinguish completed contraction bounds from still-supplied spatial operator inputs. However, the complete correspondence of every other cross-wave passage and all declarations it invokes was not finished; the broad 'every other place' claim is therefore not certified.
- L8-PATTERNS: FAIL: The completed phase and low-alpha wrappers genuinely remove their supplied inputs, and no wrong constant or rate/supremum identification was found in them. Nevertheless, candidate/statement-ledger.md:4923-4925 overstates their integrability coverage as applying to every statement, although the unrestricted types at PhaseContractions.lean:192-194,772-774,976-979 omit it. This is a summary-conclusion overclaim of pattern (a), documented in W1.
- SCOPE-AND-NOT-IN-LEAN: INCONCLUSIVE: The complete changed-sections diff and Scope/Index/Not-in-Lean passages were read. The phase/low-alpha completion changes and the retained toSphere caveat are supported by the checked types; the Fock spatial input and occupation-class limitations are explicitly retained. However, not every declaration supporting all newly changed cross-wave summary passages was read completely, so the universal claim about all changed passages remains unverified.

Findings, fatal (0):

Findings, major (2):
- W1 — PARA-PhaseContractions, blanket integrability assurance. candidate/statement-ledger.md:4923-4925 says 'the integrability of every integrand (a conclusion, so no statement holds through the junk value of a non-integrable Bochner integral)'. In contrast, Lean PhaseContractions.lean:192-194 assumes only 'IsSpectralMeasure Γ μ' and s>0, :976-979 only that predicate and epsilon>0, and :772-774 allows any Gamma; none concludes integrability. TeX notes_stratonovich_ham_second_moment.tex:2054-2057 retains tempered Radon covariances and :2097 explicitly says 'The integrals are finite'. The distinction is substantive: the bare Lean spectral predicate, HomogHypothesis.lean:52-55, is an equality of totalized integrals and does not require temperedness or local finiteness. For example, infinite-mass atoms on both sides make all its Schwartz integral equalities zero without Gaussian integrability. Fix the ledger assurance by restricting it to the principal tempered-covariance estimates/wrappers, and explicitly describe unrestricted pairing identities and positivity statements as statements of Lean integrals; alternatively strengthen those auxiliary statements with genuine-integrability conclusions under appropriate hypotheses. The completed manuscript-domain bounds themselves were not found deficient.
- W2 — REFUTATIONS, manuscript-domain mismatch. ShiftInvariance.lean:9-12 describes the example 'd = 1, Γ = Lebesgue measure, μ = δ_0'; its theorem at :35-43 assumes only 'IsSpectralMeasure Γ μ'. TeX notes_stratonovich_ham_second_moment.tex:2054-2057 instead requires a covariance on R^3 with '0 < alpha < 2' and degree3-alpha scaling. Lebesgue covariance has alpha=0, so this example is outside that class, independently of its dimension. It uses genuine finite Gaussian integrals, not an explicitly identified totalized-arithmetic extension control. Neither candidate primary section describes the negative controls or this limitation. Fix the manuscript-control correspondence by adding or replacing it with a counterexample satisfying S:static-phase, and identify the existing example only as a control for the broader Lean generalization.

Findings, minor (1):
- W3 — L9Completed hypothesis-usage wording. candidate/statement-ledger.md:3531-3532,3554 and lean/claims.yaml:17377 call alpha0 'carried, unused'. Lean L9Completed.lean:184 calls PhaseCovariance.of_homog; PhaseContractions.lean:141-142 calls alpha_mem_Ioo_of_homog, whose proof at SpectralMassIdentity.lean:214 uses 'hH.threshold' and 'hH.alpha0_pos'. TeX notes_stratonovich_ham_second_moment.tex:226,238 supplies exactly these numerical hypotheses. No hypothesis is missing from the wrapper and its conclusion is independent of alpha0. Optional wording fix: say alpha0 does not occur in the conclusion, but its positivity and threshold hypotheses are used to obtain alpha<2.

Required repairs (2):
- Correct candidate/statement-ledger.md:4923-4925 so its genuine-integrability assurance applies only where integrability is actually proved; explicitly qualify the unrestricted Gaussian-pairing and positivity declarations, or strengthen their Lean statements appropriately.
- Provide a shift-equality negative control within S:static-phase and document its assumptions; do not present the existing d=1, alpha=0 example as a counterexample under the manuscript's standing class.

Limitations (6):
- The two primary Lean modules, their53 ledger rows and claims entries, both audit files, all three refutation files, the primary cited authoritative TeX ranges, the complete excerpts file, Scope, Index, Not in Lean and the changed-sections diff were read completely.
- The broader complete-reading obligation for every declaration invoked by all cross-wave changed summary passages was not completed. Checks CROSS-REFERENCES and SCOPE-AND-NOT-IN-LEAN are therefore INCONCLUSIVE; the overall verdict is INCONCLUSIVE rather than acceptance despite the identified mandatory repairs.
- Contextual coverage remains partial as listed: especially the full ledger diff, coverage.diff:76-566, prior-file substantive contents, and uncited portions of supporting modules. Structural parsing, label searching and hash verification are not substitutes for substantive correspondence reading.
- The audit files contain #check/#print commands, not captured elaboration output. No compiler was run; compilation and standard-axiom proof correctness were accepted as supplied by the contract.
- T_epsilon(a,q) is a complex scalar Fourier integral in both PhaseContractions.lean:750-751 and manuscript main TeX:2081-2084. No trace-class operator assertion about this T was present to verify.
- This is an AI correspondence review, not human verification or a novelty audit.

## g3-raw-energy-ceiling-exact

Preflight: contract-check CONTRACT-OBSERVABLE (14 required field(s), 0 dispatch input(s); no provider call); dry run exit 0 (dryrun/); contract-check with --dispatch-input dryrun/prompt.txt CONTRACT-OBSERVABLE (14 required field(s), 1 dispatch input(s); no provider call)

Driver log:
```
2026-11-12T14:24:40Z start attempt-01
2026-11-12T14:36:05Z attempt-01 exit=2 Status: review-complete
2026-11-12T14:36:05Z done
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
Check verdicts: PASS 41, PASS_WITH_NOTES 18, FAIL 1 (of 60)

Checks not PASS/PASS_WITH_NOTES:
- REFUTATIONS: FAIL: The six files prove their stated scalar or route counterexamples, and PenaltyPositive.lean:6-10 explicitly acknowledges totalized division at ζ=0. However, CellWidth.lean:2-9, 26-33 and TrapezoidLimit.lean:2-11, 26-34 refute properties of Lean-only constructions absent from the manuscript; the latter distinguishes endpoint values that do not change its time integrals. Neither target ledger section supplies the required account of these six controls. Thus the contract's assertion that every listed perturbation is a corresponding manuscript misstatement, accurately described in the ledger, is not met. See W1.

Findings, fatal (0):

Findings, major (1):
- W1 REFUTATIONS: The required manuscript-correspondence certification is not satisfied. CellWidth.lean:26-33 negates a bound for 'OccupationCeilingExact.idx'; TrapezoidLimit.lean:26-34 negates convergence of 'OccupationCeilingExact.trap' to a closed-interval indicator at s=0. TeX integrated_occupation_ceiling.tex:160-173 instead uses a countable first-index Borel selection and states neither construction; its integral conclusion is at :151-155. These are valid Lean-route unit controls, not refutations of corresponding manuscript assertions. Ledger sections :4375-4470 and :5257-5347 contain no descriptions of the six supplied controls, including the totalized ζ=0 limitation expressly stated in PenaltyPositive.lean:6-10. Fix: add a six-file control-correspondence account distinguishing manuscript scalar perturbations, Lean-route-only controls and the totalized-extension control. Do not certify the route-only files as manuscript negative controls; supplement them with actual manuscript-claim perturbations if that certification is retained.

Findings, minor (3):
- W2 idx_measurable notation: ledger:4456 and claims.yaml:15845 write 'min(floor((N+1)s),N)' on all R, whereas OccupationCeilingExact.lean:160-161 uses natural floor '⌊...⌋₊', clipped at zero for negative arguments. TeX integrated_occupation_ceiling.tex:169-173 has no such index. Optional clarification: write 'natural floor' or max(0,floor(...)) before taking the minimum; the intended time-domain construction is unaffected.
- W3 T finiteness wording: ledger:5293-5294 says A and T have finiteness as a conclusion. OccupationPhysicalClass.lean:154-158 already requires 'energy_lt_top : Tlin DG < ⊤', exactly as TeX integrated_spatial_occupation.tex:381-383 requires T(g)<∞ in the definition of O. Optional correction: say A finiteness is proved, while T finiteness is inherited from occupation membership and its real integral representation is proved.
- W4 Representative-class terminology: ledger:5310-5316 and :4438-4443 calls joint representatives 'narrower'. Lean OccupationPhysicalClass.lean:154-158 specifies jointly a.e.-strongly measurable function/gradient representatives with unit H1 slices and finite budget; TeX integrated_spatial_occupation.tex:381-383 specifies strongly H1-measurable occupations and :407-414 constructs representatives. These describe equivalent a.e. mathematical data, although the bridge is not formalized. Optional clarification: distinguish an unformalized representation equivalence from a genuinely smaller mathematical class. The existing explicit representation disclaimer should remain.

Required repairs (1):
- Resolve W1 before asserting that all six supplied refutation files satisfy REFUTATIONS: document each control's exact target and domain in the target ledger sections, expressly separate Lean-route-only controls from manuscript counterexamples, and supply genuine manuscript perturbation controls wherever the stronger manuscript-negative-control certification is retained.

Limitations (6):
- This is an AI correspondence review, not human verification, proof rechecking or a novelty audit. Compilation and standard-axiom status were accepted as stipulated.
- Audit.lean files contain commands and consumer proofs, not captured elaboration output; they were read but not executed.
- The complete target modules, target sections, four coverage rows, required changed passages, refutation files, audit files and excerpt file were read. Context library files were inspected in the reported ranges, not exhaustively.
- PROVENANCE.json was not completely read after an initially truncated display; the unnumbered remainder was not relied on. Only numbered ranges 1-55 and 1770-1837 were subsequently inspected. Its intervening manifest entries and byte bindings were not independently verified.
- lean/provenance/manuscript-anchor.json was read only at 1-32 and 1790-1825; the intervening metadata was not reviewed.
- Unrelated portions of coverage files and diffs, and earlier-wave ledger results outside the requested changed passages, were not reviewed. The full prior ledger and full statement-ledger.diff were not read; the supplied changed-section diff was read completely.

## g4-complex-phase-scalar

Preflight: contract-check CONTRACT-OBSERVABLE (14 required field(s), 0 dispatch input(s); no provider call); dry run exit 0 (dryrun/); contract-check with --dispatch-input dryrun/prompt.txt CONTRACT-OBSERVABLE (14 required field(s), 1 dispatch input(s); no provider call)

Driver log:
```
2026-11-12T14:24:40Z start attempt-01
2026-11-12T14:33:27Z attempt-01 exit=2 Status: review-complete
2026-11-12T14:33:27Z done
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
Check verdicts: PASS 77, PASS_WITH_NOTES 3, PARTIAL 2 (of 82)

Checks not PASS/PASS_WITH_NOTES:
- StratonovichHAMSecondMoment.ComplexPhaseScalar.phase_block_of_inputs: no direct label: PARTIAL: Ledger:1623 matches Lean:1250-1270, including 'c * lam^(a-2) ≤ deltaA a', parameter signs and measurable domination. TeX:2301,2357-2359 makes coupling essential to 1/6. However claims.yaml:16448 omits that coupling and the parameter/measurability premises from its conditional summary. Mere domination does not imply 1/6; W1.
- REFUTATIONS: PARTIAL: All five files prove their stated negations with ordinary, defined arithmetic. BlockExponent, NeumannInverse, ParabolaQuarter and PhaseWeight correctly test their stated scalar steps. ImaginaryRoot.lean:7-10,21-31 instead uses lambda=1,w=-1, which violates the manuscript's x≥-lambda²/4 at TeX:2393. It tests the generalized reduced-premise implication, not the manuscript numerical-range domain; W2. The target ledger section contains no individual refutation descriptions.

Findings, fatal (0):

Findings, major (2):
- W1 — phase_block_of_inputs summary omits an essential smallness hypothesis. lean/claims.yaml:16448 says 'If PhaseRangeBounds ... and Qʹ - 1 = (1/pi) int J with ||J t|| dominated, then ... ||Qʹ - 1|| <= 1/6'. The actual Lean declaration at lean/StratonovichHAMSecondMoment/ComplexPhaseScalar.lean:1250-1259 additionally requires '0<a<1', '0<lam', '0≤h', 'c * lam^(a-2) ≤ deltaA a', a.e.-strong measurability and a specific domination. The manuscript at manuscript/notes/notes_stratonovich_ham_second_moment.tex:2301,2357-2359 uses the coupling condition to obtain the final 1/6. Arbitrary dominated integrals need not have that small norm. Fix claims.yaml:16448 by including these antecedents, particularly the coupling condition and explicit domination; the ledger row at candidate/statement-ledger.md:1623 already states them correctly.
- W2 — ImaginaryRoot does not provide an in-domain manuscript negative control. lean/refutations/complex-phase-scalar/ImaginaryRoot.lean:7-10,21-31 refutes the lambda/2 variant using 'lambda=1, w=-1, r=i' under only '||w||≤Re w+2lambda²'. The manuscript numerical range additionally satisfies 'x≥-lambda²/4' at manuscript/notes/notes_stratonovich_ham_second_moment.tex:2391-2393, so this point is excluded. The file correctly refutes the generalized Lean implication at ComplexPhaseScalar.lean:515-516, but does not establish failure of the strengthened root bound under the manuscript hypotheses. Fix the control documentation by explicitly reclassifying it as a reduced-premise auxiliary control outside the manuscript numerical-range domain, or replace it with a counterexample satisfying the manuscript hypotheses. Add that distinction to the ledger if these refutations are cited as correspondence controls.

Findings, minor (2):
- W3 — Incorrect implementation wording in candidate/statement-ledger.md:1509: 'phaseG, phaseH are if branches'. Lean defines an if-branch only for phaseG at lean/StratonovichHAMSecondMoment/ComplexPhaseScalar.lean:549-550; phaseH at 561 is a product using phaseG. The removable value required by manuscript/notes/notes_stratonovich_ham_second_moment.tex:2405-2406,2429 is nevertheless correct. Optional fix: say 'phaseG explicitly supplies the removable sine-quotient value, and phaseH consequently has value zero'.
- W4 — Unit-vector qualification in candidate/statement-ledger.md:1619. The row correctly states the identity for every u, matching lean/StratonovichHAMSecondMoment/ComplexPhaseScalar.lean:1161-1163, but then calls it 'a point of W(A_0-T)'. The manuscript at manuscript/notes/notes_stratonovich_ham_second_moment.tex:2373,2384 requires '||u||=1' for numerical-range membership. Optional fix: append 'when ||u||=1' to that interpretation; do not restrict the valid general identity.

Required repairs (2):
- Repair lean/claims.yaml:16448 so phase_block_of_inputs explicitly retains its essential coupling, parameter and measurable-domination hypotheses.
- Correct the manuscript-domain characterization of ImaginaryRoot: either provide an admissible manuscript-domain negative control or explicitly classify the existing theorem as a control only of the generalized reduced-premise scalar implication.

Limitations (6):
- Complete-reading requirement A was met for the target section, Scope, entire Index, own Lean module, required imported declarations, claim entries, coverage entries, audit, refutations, excerpts and cited authoritative TeX passages.
- Basenames used in check reasons resolve to the exact paths listed in source_coverage; unqualified Lean line references refer to ComplexPhaseScalar.lean, and TeX references to notes_stratonovich_ham_second_moment.tex.
- Ancillary provenance history, prior versions and diffs were read only in the contextual ranges recorded above; their remaining ranges were not reviewed. These are not gaps in requirement A.
- The supplied compilation premise was accepted; no build or independent proof re-elaboration was performed. Audit.lean contains audit commands, not captured elaborator output.
- No claim is made that the manuscript's lambda/2 root bound is true or false under its full hypotheses; the supplied counterexample does not settle that question.
- This is an AI correspondence review, not human verification or a novelty audit.

## g5a-gaussian-hermite

Preflight: contract-check CONTRACT-OBSERVABLE (14 required field(s), 0 dispatch input(s); no provider call); dry run exit 0 (dryrun/); contract-check with --dispatch-input dryrun/prompt.txt CONTRACT-OBSERVABLE (14 required field(s), 1 dispatch input(s); no provider call)

Driver log:
```
2026-11-12T14:24:40Z start attempt-01
2026-11-12T14:32:36Z attempt-01 exit=0 Status: review-complete
2026-11-12T14:32:36Z done
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
Check verdicts: PASS 61, PASS_WITH_NOTES 2 (of 63)

Findings, fatal (0):

Findings, major (0):

Findings, minor (1):
- W1 — PARA-GaussianHermite, candidate/statement-ledger.md:2623-2625: the phrase '(or n - 1) only appears multiplied by ... sqrt(n)' is too literal for the unnormalized formulas. GaussianHermite.lean:124-132 has 'n * hermR (n - 1)', whereas the normalized manuscript recurrence at manuscript/notes/notes_stratonovich_ham_second_moment.tex:2516-2517 has 'sqrt(k_i) h_(k-e_i)'. Both coefficients vanish at zero, so the asserted absence of junk-value dependence remains correct. Optional exact wording fix: say that truncated lowering indices carry a coefficient n or sqrt(n), as appropriate, which vanishes at zero.

Required repairs (0):

Limitations (6):
- All complete-reading requirement A ranges for this target were read. Partial-file entries above denote deliberately scoped reading of larger files, not gaps in those required ranges.
- The remainder of manuscript-anchor.json, prior files, diffs, unrelated ledger sections, and unrelated library modules was not substantively reviewed. Searches and byte-binding checks are not claimed as complete semantic reading.
- The supplied audit file contains #check/#print commands, not captured elaboration output. Compilation, absence of sorry, and the standard-axiom restriction were accepted as stipulated; no build was run.
- Creation-row, number-order, and vacuum-square-of-sum refutation files are not included in this GaussianHermite packet. Their mathematical perturbations are consistent with the inspected foundation identities, but their separate Lean files were not verified.
- External Janson content and claims about what is absent from Mathlib were not independently audited. The local proofs establish the Hermite identities without supplying Janson's algebra as a hypothesis.
- This is an AI correspondence review, not human verification or a novelty audit.

## g5b-hermite-fock

Preflight: contract-check CONTRACT-OBSERVABLE (14 required field(s), 0 dispatch input(s); no provider call); dry run exit 0 (dryrun/); contract-check with --dispatch-input dryrun/prompt.txt CONTRACT-OBSERVABLE (14 required field(s), 1 dispatch input(s); no provider call)

Driver log:
```
2026-11-12T14:24:40Z start attempt-01
2026-11-12T14:36:11Z attempt-01 exit=0 Status: review-complete
2026-11-12T14:36:11Z done
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
Check verdicts: PASS 49, PASS_WITH_NOTES 5 (of 54)

Findings, fatal (0):

Findings, major (0):

Findings, minor (3):
- W1 — creOp_bound input-cell wording. candidate/statement-ledger.md:2946 says the column bound 'and the symmetry of the H_i are hypotheses'. Lean actually assumes only 'hc : ∀ u, ∑ i, ‖H i u‖² ≤ c * ‖u‖²' at lean/StratonovichHAMSecondMoment/HermiteFock.lean:293-296; lean/claims.yaml:17080 correctly reflects that. TeX's spatial H_i are selfadjoint at manuscript/notes/notes_stratonovich_ham_second_moment.tex:2495-2496, so the manuscript application remains valid. Optional fix: remove symmetry from this declaration's input cell and identify it as a hypothesis needed by the annihilation/combined bounds, not this creation bound.
- W2 — annihilation cutoff comparison. candidate/statement-ledger.md:2892-2897,2947 compares '(N+1)c' with TeX's 'Nc'. Lean's theorem bounds input degrees ≤ N+1 into output degrees ≤ N (lean/StratonovichHAMSecondMoment/HermiteFock.lean:307-311), whereas the explicit TeX 'sqrt n' concerns input degrees ≤ n (manuscript/notes/notes_stratonovich_ham_second_moment.tex:1806-1809); the cited Fock proof itself says 'the same bound after truncation' at :2522-2523. The ledger's application with Supp N is sound. Optional fix: say that applying the N+1-to-N theorem to an input already supported through N leaves an unused degree of slack; do not compare the differently indexed operator domains without this qualification.
- W3 — inner-product convention. The target prose does not mention that Lean uses conjugate-linearity in the first slot, visible in lean/StratonovichHAMSecondMoment/HermiteFock.lean:487-494, while the manuscript explicitly says 'linear in the first slot' at manuscript/notes/notes_stratonovich_ham_second_moment.tex:2824. All reviewed adjoint identities survive conjugation, and norm-square/real-part identities are unchanged. Optional fix: add this convention translation to candidate/statement-ledger.md:2860-2873; no theorem or constant needs alteration.

Required repairs (0):

Limitations (5):
- Requirement A was completed. Files marked partial were read only in the required sections/declarations or as optional context; unrelated earlier-wave rows, historical metadata, and remaining diff contents were not comprehensively reviewed.
- Manuscript-wide searches establish uniqueness of the target labels, not a full review of every manuscript input.
- Compilation and standard-axiom status were accepted as stipulated; no build was launched. The audit packet contains #check/#print commands rather than their captured output.
- The unavailable GaussianHermite negative-control files mentioned in neighboring prose were not audited; check REFUTATIONS concerns the three supplied HermiteFock controls.
- This AI correspondence review is neither human verification nor a novelty audit.

## g6a-fock-form-word

Preflight: contract-check CONTRACT-OBSERVABLE (14 required field(s), 0 dispatch input(s); no provider call); dry run exit 0 (dryrun/); contract-check with --dispatch-input dryrun/prompt.txt CONTRACT-OBSERVABLE (14 required field(s), 1 dispatch input(s); no provider call)

Driver log:
```
2026-11-12T14:24:40Z start attempt-01
2026-11-12T14:35:50Z attempt-01 exit=2 Status: review-complete
2026-11-12T14:35:50Z done
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
Check verdicts: PASS 23, PARTIAL 3, FAIL 3 (of 29)

Checks not PASS/PASS_WITH_NOTES:
- PARA-FockForm: PARTIAL: The mathematical body accurately identifies the supplied columns, operator abstractions, constants, unused covariance hypotheses, proof route and omitted closure/model construction (ledger:2296-2397; FockForm.lean:105-544; main TeX:1773-1814, 2472-2527, 2828-2897). However, the 'whole result' heading at ledger:2289 contradicts the explicitly partial correspondence under the contract's completeness-language rule (W2). The symmetry/self-adjointness wording also merits clarification (W3).
- PARA-HermiteWordFock: PARTIAL: The body correctly describes the one-mode coefficient model, insertion, frames, vacuum, four discharged hypotheses and omitted finite-sum/Bochner-integral statement (ledger:994-1026; HermiteWordFock.lean:43-51; main TeX:2531-2571). 'Nothing supplied' is true for that special case. Calling the section 'whole result' at ledger:992 nevertheless conflicts with its restricted scope (W2).
- COVERAGE-ROWS: FAIL: W1: coverage.yaml:337 says 'same-assumptions', although HermiteWordFock.lean:43-48 accepts one K_i and one Gaussian mode per color, whereas main TeX:2532-2538 allows arbitrary m_i and K_ij. The scope correctly discloses this restriction, but 'weaker' does not make the assumption-class claim true. The other three rows honestly describe supplied inputs and narrower conclusions. All listed claim IDs were located in claims.yaml.
- CROSS-REFERENCES: PARTIAL: The substantive references correctly distinguish the one-mode word theorem, supplied spatial columns, unformalized multi-mode applications and mild-construction remainder (ledger:263-266, 327-334, 3173-3176, 6743-6754, 8659-8678; main TeX:2625-2630, 3257-3262, 3490-3497). References at ledger:60, 755 and 2345 repeat the problematic 'whole result' section names and should follow the qualification repair in W2.
- L8-PATTERNS: FAIL: Pattern (d) occurs in the target headings at candidate/statement-ledger.md:992 and 2289 and their references at :60, :755 and :2345: 'whole result' is used despite one-mode-only coverage or supplied inputs (W2). The scoped 'nothing supplied' statements concern genuinely proved special cases and are not themselves false. No unsupported implicit side condition or totalized-arithmetic counterexample was found in the reviewed material.
- CHANGED-ROW L:finite-word-cutoff: FAIL: The merge replaces 'inputs-supplied' by 'same-assumptions' (prior/coverage-5ec3c11.yaml:263; diffs/coverage.diff:164-188; coverage.yaml:337). The added concrete theorem discharges the realization only for m_i = 1, not the arbitrary grouped modes of main TeX:2532-2538. Thus the concrete progress and new scope sentence are accurate, but the promoted assumption class is not (W1). The new TeX scope entry accurately mirrors the restricted scope.

Findings, fatal (1):
- W1 — False assumption-class promotion for L:finite-word-cutoff. lean/coverage.yaml:337 says 'class: same-assumptions'. Lean instead has 'K : Fin m → X →L[ℂ] X' and insertion 'gmul i (fun l => K i (v l))' (lean/StratonovichHAMAudit/HermiteWordFock.lean:43-48), while the TeX allows arbitrary grouped modes and 'J_i = sum_{j=1}^{m_i} M_{g_ij} tensor K_ij' (manuscript/notes/notes_stratonovich_ham_second_moment.tex:2532-2538). This is a restriction of admissible operator data, not an implicit side condition or merely an omitted concluding sentence. Fix: remove the same-assumptions promotion for the manuscript lemma; retain an accurately classified one-mode special case and identify the remaining multi-mode realization as unformalized, or formalize arbitrary m_i before retaining that class. Qualify coverage.yaml:355's 'Nothing supplied' explicitly as applying only to the one-mode special case.

Findings, major (1):
- W2 — Completeness-language mismatch. candidate/statement-ledger.md:992 and :2289 call the consumers 'whole result', repeated at :60, :755 and :2345. Lean's word theorem has only one mode per color (lean/StratonovichHAMAudit/HermiteWordFock.lean:43-48), versus arbitrary m_i and sums/integrals in the TeX (manuscript/notes/notes_stratonovich_ham_second_moment.tex:2532-2552); the Fock theorem assumes 'hcol : FockColumn H ...' (lean/StratonovichHAMSecondMoment/FockForm.lean:217), whereas the TeX proves that column bound (main TeX:2492-2511). The detailed disclosures are useful, but the headings retain the contract's prohibited whole-result language for narrower/supplied-input correspondence. Fix: rename these headings to identify partial consumers and the one-mode finite-word special case, and update their references.

Findings, minor (1):
- W3 — Symmetry terminology. candidate/statement-ledger.md:2380 says 'self-adjointness is proved', while Lean concludes the finite coefficient pairing identity 'sum inner (fieldOp ... v) w = sum inner v (fieldOp ... w)' (lean/StratonovichHAMSecondMoment/FockForm.lean:227-229); the TeX says 'bounded selfadjoint operators' (manuscript/notes/notes_stratonovich_ham_second_moment.tex:2483). Bounded symmetry has the intended self-adjoint interpretation on the complete finite coefficient space, but no such operator-space packaging is stated here. Optional clarification: use 'symmetry is proved' consistently, as the row and coverage scope already do.

Required repairs (2):
- Resolve W1: withdraw the same-assumptions classification for the full multi-mode manuscript lemma, explicitly distinguish the no-input one-mode theorem from the remaining multi-mode realization, and update any affected coverage totals; alternatively supply a formal arbitrary-m_i realization.
- Resolve W2: replace the two target 'whole result' headings with accurately scoped descriptions and update their occurrences at candidate/statement-ledger.md:60, 755 and 2345.

Limitations (4):
- All complete-reading requirement A sections, entries, declarations and cited TeX ranges were read. Files marked partial contain additional out-of-scope material that was not reviewed.
- PROVENANCE.json:41-1810 and lean/provenance/manuscript-anchor.json:61-1825 were not read; provenance was consulted only for revision metadata, not cryptographically audited.
- Compilation and standard-axiom status were accepted as stipulated; no build or proof-correctness audit was performed. The audit files contain check/print commands rather than captured elaborator output.
- This is an AI correspondence review, not human verification or a novelty audit.

## g6b-static-interval-reworded

Preflight: contract-check CONTRACT-OBSERVABLE (14 required field(s), 0 dispatch input(s); no provider call); dry run exit 0 (dryrun/); contract-check with --dispatch-input dryrun/prompt.txt CONTRACT-OBSERVABLE (14 required field(s), 1 dispatch input(s); no provider call)

Driver log:
```
2026-11-12T14:24:40Z start attempt-01
2026-11-12T14:33:34Z attempt-01 exit=0 Status: review-complete
2026-11-12T14:33:34Z done
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
Check verdicts: PASS 4, PASS_WITH_NOTES 2 (of 6)

Findings, fatal (0):

Findings, major (0):

Findings, minor (1):
- W1 — Cross-reference shorthand in candidate/statement-ledger.md:6794 ('L:complex-phase is formalized only with analytic inputs supplied') and :6787,6804 ('L:fock-form itself is in FockForm' / 'L:fock-form is FockForm.fock_form_paper') could identify the proved portions more precisely. ComplexPhaseScalar.lean:1326–1331 concludes a weighted-block-map inequality, whereas manuscript/notes/notes_stratonovich_ham_second_moment.tex:2302–2307 states the actual propagator inequality. FockForm.lean:206–232 gives the coefficient-model sandwich conclusions, whereas manuscript:2472–2489 also asserts self-adjointness of the unsandwiched operator on the larger Gaussian space. These differences are explicitly disclosed at ledger:6747–6750,6780–6788,1535–1537,2377–2385, so the cross-references are acceptable in context. Optional wording fix: replace the shorthand with 'the scalar and weighted-block-map deductions' and 'the coefficient-model sandwich estimate', respectively.

Required repairs (0):

Limitations (4):
- All ranges required by complete-reading requirement A were read completely. Partial-file entries identify contextual sources whose unlisted portions were not reviewed; no conclusion is offered about those portions or unchanged earlier-wave assertions.
- The manuscript-anchor historical remainder and PROVENANCE.json beyond the listed ranges were not reviewed. Packet hashes and repository ancestry were not independently recomputed.
- Lean compilation and proof correctness were accepted as stipulated, not independently rerun.
- This is an AI correspondence review, not human verification or a novelty audit.

