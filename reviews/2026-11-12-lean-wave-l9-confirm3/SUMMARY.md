# Wave L9 re-confirmation-3 reviews (strict heading categories): summary

Companion d5667f5 (wave-l9/repair; strict three-category headings, docs only; reviewed commit ba6c565), manuscript a284420; reviewer Codex gpt-6.1-sol, effort high, min-confidence high, --source-revision d5667f5. Packets built by scratchpad/build-l9-reconfirm3.py. Every finding below is verbatim from report.json.

Packets: h1/h2/h3 every ledger section heading (66 library sections in three thirds; h3 also the 24 audit sections); h4 every Index-by-label first cell (394 rows, 4 checks); h5 r1 R1 (RemoveMask row), r2 findings, classification consistency of counts, no new overclaim in ba6c565..d5667f5, earlier repairs kept. Retry only on tool failure, recorded in the driver log.

## h1-headings-lib-a

Preflight: contract-check CONTRACT-OBSERVABLE (14 required field(s), 0 dispatch input(s); no provider call); dry run exit 0 (dryrun/); contract-check with --dispatch-input dryrun/prompt.txt CONTRACT-OBSERVABLE (14 required field(s), 1 dispatch input(s); no provider call)

Driver log:
```
2026-11-12T16:15:36Z start attempt-01
2026-11-12T16:23:55Z attempt-01 exit=2 Status: review-complete
2026-11-12T16:23:55Z done
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
Check verdicts: PASS 11, FAIL 11 (of 22)

Checks not PASS/PASS_WITH_NOTES:
- HEADING ComplexPhaseScalar: FAIL: Category B is correct, but the heading at statement-ledger.md:1519 does not explicitly name the missing propagator identification or interval-metric telescoping. Both are substantive omissions disclosed at 1581-1589. See finding H2.
- HEADING DriverParameters: FAIL: The numerical conclusion matches the manuscript, including its full-hypothesis wrapper, but the required coverage row has no conclusion: full field (coverage.yaml:130-136). Thus the heading does not satisfy the stipulated category-A metadata condition. See H1.
- HEADING FiniteGaussianMatrix: FAIL: The inspected wrappers match the trace and moment conclusions, but all three cited coverage rows omit conclusion: full (coverage.yaml:418-427, 1108-1123, 1699-1709). The strict category-A condition is therefore unmet. See H1.
- HEADING FockForm: FAIL: Category B is correct, but 'spatial column bounds supplied' does not name the further finite-coordinate and operator-identification restrictions or the missing self-adjointness conclusion for B_(N,m,b). These are disclosed at statement-ledger.md:2471-2479 but absent from the heading and Index cells 860-861. See H3.
- HEADING GaussianScalarPowers: FAIL: All four scalar conclusions match integrated_compact_gaussian.tex:13-27 and GaussianScalarPowers.lean:29-94, but coverage.yaml:407-416 lacks conclusion: full. See H1.
- HEADING GramScalarAlgebra: FAIL: GramScalarAlgebra.lean:82-91 matches all three manuscript conclusions, but coverage.yaml:428-434 omits conclusion: full, contrary to the required category-A convention. See H1.
- HEADING HomogHypothesis: FAIL: HomogCovariance faithfully states the listed hypothesis and its two numerical wrappers match the manuscript (HomogHypothesis.lean:64-103). However, neither cited numerical coverage row records conclusion: full (coverage.yaml:130-143). See H1.
- HEADING IndexedCone: FAIL: The conclusion is proved for an arbitrary GroundFamily, whose identification with the manuscript's physical family is documentation only (IndexedCone.lean:989-1012; statement-ledger.md:3150-3155). Under the explicit modelled-object rule this is category B, not A. Its coverage row also lacks a conclusion field. See H4.
- HEADING IntervalScalarCompleted: FAIL: Category B is correct, but the heading names supplied analytic inputs without naming the surviving positive-noise restriction and missing identification of scalar coefficients with the interval evolution. These remain after completion; see IntervalScalarCompleted.lean:158-189 and statement-ledger.md:3273-3280,3389-3392. See H5.
- HEADING KappaRange: FAIL: The exponent and strict range match manuscript main TeX:252-254 and HomogHypothesis.lean:91-95. Nevertheless, coverage.yaml:137-143 omits conclusion: full, so the strict category-A condition is unmet. See H1.
- HEADING L8Completed: FAIL: The narrower classification is warranted, but 'completions ... see the rows' does not name the substantive missing conclusions required of a B heading. Moreover, the whole-result exception for L:uniform-series-tail uses chain measures not identified with the manuscript's chains. See H6 and H7.

Findings, fatal (0):

Findings, major (7):
- H1 — Category-A coverage metadata is missing for DriverParameters, FiniteGaussianMatrix, GaussianScalarPowers, GramScalarAlgebra, HomogHypothesis and KappaRange. The relevant coverage.yaml rows at 130-143,407-434,1108-1123,1699-1709 omit 'conclusion: full', although statement-ledger.md:62-66 requires it. This is not evidence that their mathematical conclusions are false: for example Lean states 'kappa ... ∈ Set.Ioo 1 2' (lean/StratonovichHAMSecondMoment/HomogHypothesis.lean:91-95), matching TeX '\kappa:=...\in(1,2)' (manuscript/notes/notes_stratonovich_ham_second_moment.tex:252-254); the scalar wrappers likewise match their TeX statements. Exact fix: explicitly add conclusion: full to E:driver-parameters, E:kappa, L:gaussian-scalar-powers, L:gaussian-trace-bounds, L:gram-scalar-algebra, P:finite-gaussian-matrix and R:gaussian-one-variance-test after maintaining their verified scope. Do not infer the required field from a separate summary table.
- H2 — ComplexPhaseScalar's B heading does not name its missing conclusions. Lean concludes a bound for the displayed expression built from Cop, Fop, Hop and Q' (lean/StratonovichHAMSecondMoment/ComplexPhaseScalar.lean:1321-1331), whereas TeX concludes '\|\mathcal{M}_z(h)\|...\le100e^{2\lambda h}' (manuscript/notes/notes_stratonovich_ham_second_moment.tex:2302-2307). Lean's interval_metric_paper is a product inequality for given finite jump sets (ComplexPhaseScalar.lean:1392-1397), whereas TeX asserts total phase-norm loss along connected intervals (main TeX:2909-2916). Exact fix: amend the heading and corresponding Index scope to say that propagator/block-map identification and interval-norm telescoping are not formalized, while retaining disclosure of supplied functional-calculus inputs.
- H3 — FockForm's B heading and Index cells disclose supplied column bounds but omit independent narrower conclusions. Lean proves coefficient sums and symmetry of the sandwiched field on '(Fin m → ℕ) → X' (lean/StratonovichHAMSecondMoment/FockForm.lean:219-229). TeX works in the full Gaussian Hermite cutoff and asserts 'These are bounded selfadjoint operators' for B_(N,m,b) and A_rho (manuscript/notes/notes_stratonovich_ham_second_moment.tex:2475-2485). The ledger itself acknowledges unmodelled coordinates i>m and missing self-adjoint operator packaging at 2471-2479. Exact fix: add these restrictions and the unformalized spatial-operator identification to the heading and Index cells 860-861; supplied column bounds alone do not describe the narrowing.
- H4 — IndexedCone is incorrectly category A under the supplied modelled-object rule. Lean quantifies '(G : GroundFamily F)' and concludes a bound involving G.P, G.lam and G.obs (lean/StratonovichHAMSecondMoment/IndexedCone.lean:996-1012); its preceding disclosure says the link to Gamma is 'by documentation' (989-995). TeX concludes a bound for the physical P_sigma, lambda_sigma and O_phi (manuscript/notes/integrated_raw_block_lower.tex:232-247). Naming the abstract structure does not formalize that identification. Exact fix: classify the heading and Index row 531 as 'narrower result: abstract GroundFamily; identification with the physical wave family not formalized', and set the coverage row at coverage.yaml:749-787 to conclusion: weaker with that scope.
- H5 — IntervalScalarCompleted's B heading fails to name surviving restrictions. Lean retains '_hRpos : 0 < R' and '_hσpos : ∀ i, 0 < σ i', with real coef and Q as inputs (lean/StratonovichHAMSecondMoment/IntervalScalarCompleted.lean:171-189). TeX bounds coefficients of the actual evolution and explicitly reduces zero and signed noise in its proof (manuscript/notes/notes_stratonovich_ham_second_moment.tex:3402-3423). Exact fix: state in the heading and completion Index scope that only positive-noise scalar coefficient assembly is proved, with interval-evolution identification and zero/sign reduction not formalized; retain the named analytic-input disclosure.
- H6 — L8Completed's generic B heading does not name what is missing. Lean's bracket wrapper bounds 'sSup (scoreSet ... 2)' and uses 'energyValue ... (K0 ... * Rsp ...)' (lean/StratonovichHAMSecondMoment/L8Completed.lean:262-280). TeX bounds C_2 and compares the actual occupation energy E_(1/2)^O (manuscript/notes/integrated_occupation_ceiling.tex:252-264); its ceiling uses C_occ and includes C_2<=U_2 (205-218). Exact fix: replace 'completions ... see the rows' by explicit scope naming K_0 R_sp instead of C_occ, S_2^pos instead of C_2, the substituted occupation energy, and unformalized rate/cost identifications. Carry those qualifications into the associated completion Index cells.
- H7 — The L8Completed heading's whole-result exception for L:uniform-series-tail conflicts with the modelled-object rule. Lean takes arbitrary finite measures ν with only their mass and product-measurability properties specified (lean/StratonovichHAMSecondMoment/L8Completed.lean:318-323) and concludes bounds for 'TerminalWick.chainIntegral (ν ...)' (332-345). The source explicitly says the measures are not constructed (303-309). TeX instead takes the terminal-chain terms of L:terminal-wick (manuscript/notes/notes_stratonovich_ham_second_moment.tex:3704-3706). The abstract convergence conclusions, including the optional second-moment conclusion in UniformSeriesTail.lean:301-316, do not identify those chain measures. Exact fix: remove the whole-result exception from the L8Completed heading and classify this composition as narrower until that identification is formalized; update coverage.yaml:975-996 and the corresponding Index scope accordingly.

Findings, minor (0):

Required repairs (4):
- Add the explicit conclusion: full fields identified in H1 to the corresponding category-A coverage rows.
- Make the ComplexPhaseScalar, FockForm and IntervalScalarCompleted headings and associated Index cells explicitly name their surviving omissions and restrictions, as specified in H2, H3 and H5.
- Reclassify IndexedCone and its main coverage/Index entries as narrower because the physical-family identification is not formalized.
- Replace L8Completed's generic narrowing description with its actual missing conclusions and remove the unsupported whole-result exception for the un-identified terminal-chain composition.

Limitations (4):
- The mandatory section prose, qualification searches, relevant paper/completed wrapper types, named coverage rows and complete TeX excerpt file were examined. Files marked partial were otherwise read only at the listed ranges; unlisted proofs and unrelated ledger sections were not reviewed.
- The distinction between supplied facts about manuscript objects and un-identified modelled objects was applied literally, including to GroundFamily and the terminal-chain measures; merely documenting an intended identification was not treated as a Lean identification.
- No Lean build, kernel replay, provenance-hash verification or independent proof-correctness audit was performed.
- This is an AI correspondence review, not human verification or a novelty audit.

## h2-headings-lib-b

Preflight: contract-check CONTRACT-OBSERVABLE (14 required field(s), 0 dispatch input(s); no provider call); dry run exit 0 (dryrun/); contract-check with --dispatch-input dryrun/prompt.txt CONTRACT-OBSERVABLE (14 required field(s), 1 dispatch input(s); no provider call)

Driver log:
```
2026-11-12T16:15:36Z start attempt-01
2026-11-12T16:23:25Z attempt-01 exit=2 Status: review-complete
2026-11-12T16:23:25Z done
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
Check verdicts: FAIL 9, PASS 13 (of 22)

Checks not PASS/PASS_WITH_NOTES:
- HEADING L9Completed: FAIL: The completed wrappers discharge Fourier/Archimedes inputs, but retain waveGreen 3 (L9Completed.lean:96-108,150-183). Its surface-measure identification remains explicitly unformalized (WaveGreen.lean:26-34; ledger:3643-3647). Under the stipulated model-object rule this is category B, notwithstanding coverage.yaml:529,670.
- HEADING LowAlphaConvolution: FAIL: All numerical conclusions are present at LowAlphaConvolution.lean:575-587 and L9Completed.lean:96-108. However, the d=3 conclusion uses the toSphere model rather than a formalized identification with the manuscript's surface-measure kernel (WaveGreen.lean:26-34; manuscript main file:4697-4699,5184-5186). The unqualified category A heading is incompatible with the strict convention.
- HEADING OccupationCeilingExact: FAIL: Category B is correct, but its missing-part description is incomplete. Besides C2 and the O bridge, the score uses Rayleigh-defined rates and integral-defined cost (OccupationCeilingExact.lean:748-757; VariationalDilation.lean:236-247). Their spectral-rate/variance identifications are not formalized, although the manuscript uses those quantities (integrated_unmasked_variational.tex:100-109; integrated_compact_mean_family.tex:405-410).
- HEADING OccupationCeilingFinite: FAIL: The heading identifies the larger constant and missing moment sentence but omits the absent occupation-energy form and the rate/cost identification restrictions. Lean's wrappers only bound scores by ceilingValue with K0*Rsp (OccupationCeilingFinite.lean:938-968); the manuscript also concludes the E_zeta^O equality at integrated_occupation_ceiling.tex:214-215. Ledger:4651-4659 expressly records these additional omissions.
- HEADING PhaseContractions: FAIL: The bounds and Fourier identity are fully bundled and the named inputs discharged (PhaseContractions.lean:1070-1082; L9Completed.lean:150-183), but the physical trace remains defined using the toSphere Green model. Ledger:5024-5027 and WaveGreen.lean:26-34 disclose the missing surface-measure identification. The strict model-object rule therefore requires category B.
- HEADING QuotientObstruction: FAIL: QuotientObstruction.lean:991-996 concludes a statement about covW, not a noise variance. The definition explicitly says W is not constructed (:586-594), whereas the manuscript proposition asserts E W(zeta F)^2 <= C E W(F)^2 (integrated_covariance_foundation.tex:257-263). No variance-identification input appears in the wrapper. The declared D1 interpretation does not meet the contract's formalized-identification requirement.
- HEADING RadiusMeanAnchor: FAIL: The mathematical wrapper contains the stated bounds and limit with disclosed inputs (RadiusMeanAnchor.lean:442-486; manuscript/integrated_radius_anchor.tex:280-305). Nevertheless, its coverage row has no conclusion field (coverage.yaml:1386-1398). Category A explicitly requires conclusion full; the prose note cannot substitute for the missing classification.
- HEADING RemoveMask: FAIL: Category B is appropriate, but the heading does not explicitly identify the absent canonical-moment and integral-cost/variance identifications. Lean concludes a liminf bound for arbitrary L (RemoveMask.lean:702-739), not the manuscript's canonical solution (integrated_unmasked_variational.tex:174-177). Moreover, Index cell ledger:772 still says 'part of a result', contrary to Scope:75's same-category wording requirement.
- HEADING SpatialBracket: FAIL: Replacing C2 by S2 is not the only narrowing. SpatialBracket.lean:490-494 uses energyValue alpha (K0*Rsp), whereas manuscript/integrated_occupation_ceiling.tex:263-264 uses the exact E_(1/2)^O. Ledger:5884-5900 explicitly records this additional substitution and the Rayleigh/integral conventions. The heading and principal Index cell :769 do not name them.

Findings, fatal (2):
- H1 L9Completed, LowAlphaConvolution and PhaseContractions: 'whole result' conflicts with the strict model-object rule. Lean defines 'waveGreen' using 'volume.toSphere' (lean/StratonovichHAMSecondMoment/WaveGreen.lean:106-111) and explicitly states that its surface-measure identification is not proved (:26-34). TeX uses 'sigma_h ... surface measure' (manuscript/notes/notes_stratonovich_ham_second_moment.tex:5184-5186). The completed conclusions still integrate against this model (lean/StratonovichHAMSecondMoment/L9Completed.lean:103-108,155-163). Fix: classify these three headings and corresponding Index cells as narrower results naming the unresolved d=3 Green-measure identification; align their coverage classifications and dependent classification summaries. Proving Fourier/Archimedes inputs alone does not remove this stated boundary.
- H4 QuotientObstruction: the whole-result claim suppresses an unformalized object identification. Lean concludes an inequality involving 'covW' (lean/StratonovichHAMSecondMoment/QuotientObstruction.lean:991-996), whose definition says 'W itself is not constructed' (:586-594). TeX concludes the obstruction for 'E W(zeta F)^2' (manuscript/notes/integrated_covariance_foundation.tex:261-262). Fix: use 'narrower result: covariance-functional obstruction; identification with noise variances not formalized' in the heading and principal Index cell, and align coverage and classification summaries.

Findings, major (5):
- H2 OccupationCeilingExact: category B is correct but incomplete. Lean bounds 'c * integratedRate ... - rawCost ... / 2' (lean/StratonovichHAMSecondMoment/OccupationCeilingExact.lean:752-757); 'rate' is defined by the Rayleigh supremum and 'rawCost' by an integral, with identifications explicitly unformalized (lean/StratonovichHAMSecondMoment/VariationalDilation.lean:236-247). TeX uses 'lambda = sqrt(-E_s)' (manuscript/notes/integrated_unmasked_variational.tex:100-109) and 'v_Psi := E Z^2' (manuscript/notes/integrated_compact_mean_family.tex:405-410). Fix: add the unformalized rate/cost identifications to the heading and corresponding principal Index qualifier, alongside the existing C2 and O omissions.
- H3 OccupationCeilingFinite: the missing-part description omits a conclusion, not merely a proof route. Lean concludes only ceilings with 'K0 alpha0 * Rsp' (lean/StratonovichHAMSecondMoment/OccupationCeilingFinite.lean:938-968); TeX also asserts '= c^m (2 zeta)^(alpha/(2k)) F_0(E_zeta^O)' (manuscript/notes/integrated_occupation_ceiling.tex:214-215). Ledger:4654-4659 acknowledges that this energy form is absent. Fix: explicitly name the missing occupation-energy form and the unformalized rate/cost identifications in the narrower heading and principal Index qualifier.
- H5 RadiusMeanAnchor: category A's mandatory coverage metadata is absent. Lean contains the mean bound and decay limit (lean/StratonovichHAMSecondMoment/RadiusMeanAnchor.lean:470-486), matching TeX's 'E Z_delta' bound and 'delta^e_anchor -> 0' (manuscript/notes/integrated_radius_anchor.tex:294-302), with supplied inputs disclosed. However, lean/coverage.yaml:1386-1398 has 'class: inputs-supplied' but no 'conclusion: full'. Fix: add that conclusion classification to this row; otherwise the whole-result heading fails the adopted convention.
- H6 RemoveMask: the heading's qualifier and Index terminology remain incomplete. Lean's point conclusion is 'liminf ... L(T)' for an arbitrary real function L (lean/StratonovichHAMSecondMoment/RemoveMask.lean:702-739), while TeX names the 'original canonical solution' and its second moment (manuscript/notes/integrated_unmasked_variational.tex:174-177). Its integral cost also lacks the variance identification (lean/StratonovichHAMSecondMoment/VariationalDilation.lean:236-240 versus manuscript/notes/integrated_compact_mean_family.tex:409-410). Fix: name these missing identifications in the heading, retain RawBlockOriginalLower as the supplied transfer input, and replace 'part of a result' in candidate/statement-ledger.md:772 with the prescribed 'narrower result' terminology.
- H7 SpatialBracket: 'for S_2^pos, not C_2' does not describe all missing conclusions. Lean compares 'F0 alpha (energyValue alpha (K0 alpha0 * Rsp ...))' with Fb at the same surrogate energy (lean/StratonovichHAMSecondMoment/SpatialBracket.lean:490-494). TeX compares F0 and Fa at the exact 'E_(1/2)^O' (manuscript/notes/integrated_occupation_ceiling.tex:263-264). Fix: name this energy substitution, and the unformalized rate/cost identifications, in the heading and principal Index qualifier; do not imply that substituting S2 alone reproduces the corollary.

Findings, minor (0):

Required repairs (7):
- H1: Reclassify the three Green-measure-dependent headings and corresponding Index/coverage entries to disclose the unresolved d=3 object identification; synchronize classification summaries.
- H4: Reclassify QuotientObstruction as the narrower covariance-functional result and disclose the absent noise-variance identification consistently.
- H2: Complete OccupationCeilingExact's heading and principal Index qualifier with the rate/cost identification restrictions.
- H3: Complete OccupationCeilingFinite's heading and principal Index qualifier with the missing occupation-energy form and rate/cost identification restrictions.
- H5: Add conclusion: full to the P:radius-mean-anchor coverage row.
- H6: Complete RemoveMask's missing-identification qualifier and replace the nonconforming 'part of a result' Index classification.
- H7: Complete SpatialBracket's heading and principal Index qualifier with the surrogate-energy substitution and rate/cost identification restrictions.

Limitations (5):
- Requirement A's mandated prose, wrapper signatures, coverage rows and complete TeX excerpt file were read. Partial-file entries omit unrelated sections or proof bodies, not required correspondence material.
- This review applies the contract's strict model-object rule to the expressly disclosed toSphere and covariance-functional boundaries; author-approved definitional readings are not treated as formalized identifications.
- No mathematical inequivalence of those models is asserted. The findings concern documentation scope and absent formal correspondence.
- Lean proofs were not rerun or audited for correctness. Packet hashes and repository history were not independently verified.
- This AI review is neither human verification nor a novelty audit.

## h3-headings-lib-c-audit

Preflight: contract-check CONTRACT-OBSERVABLE (14 required field(s), 0 dispatch input(s); no provider call); dry run exit 0 (dryrun/); contract-check with --dispatch-input dryrun/prompt.txt CONTRACT-OBSERVABLE (14 required field(s), 1 dispatch input(s); no provider call)

Driver log:
```
2026-11-12T16:15:36Z start attempt-01
2026-11-12T16:28:59Z attempt-01 exit=2 Status: review-complete
2026-11-12T16:28:59Z done
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
Check verdicts: FAIL 10, PASS 36 (of 46)

Checks not PASS/PASS_WITH_NOTES:
- HEADING SpatialFourLinear: FAIL: The heading at candidate/statement-ledger.md:6078 correctly names sequential continuity and the rate/cost bridges. However, its main-result Index cell at:700 names the proved energy fragment rather than the missing score identifications required by the strict convention. Compare SpatialFourLinear.lean:1698-1738 and coverage.yaml:1450-1478. See H8.
- HEADING SpatialOccupationCompleted: FAIL: The category-B heading at candidate/statement-ledger.md:6297 is accurate, but Index cells:661-662 merely say completed wrappers and omit the retained category-B boundary. SpatialOccupationCompleted.lean:133-177 still uses integral costs and Rayleigh rates; ledger:6330-6334 explicitly preserves that narrowing. See H8.
- HEADING SpatialOccupationL7Completed: FAIL: Category B is correct, but the heading omits sequential-only continuity, retained explicitly at candidate/statement-ledger.md:6406-6414. SpatialOccupationL7Completed.lean:182-194 proves a sequence-limit statement, whereas manuscript/notes/integrated_spatial_occupation.tex:229-230 asserts joint continuity. Completion does not remove this boundary. See H1.
- HEADING SpatialSmoothRatio: FAIL: The heading at candidate/statement-ledger.md:6438 correctly names the rate/cost identification gap. Its main-wrapper Index cell at:655 instead says both claims without that category-B qualification. SpatialSmoothRatio.lean:763-772 and coverage.yaml:1511-1513 retain the modelled-score boundary. See H8.
- HEADING SymplecticFree: FAIL: Category B is correct, but supplied free-group/Young inputs do not describe the missing conclusions. SymplecticFree.lean:723-754 omits J_E and preservation of the form on E, asserted at manuscript/notes/integrated_symplectic_phase.tex:32-41. Ledger:7095-7103 acknowledges these omissions, absent from heading:7023 and its Index repetitions:789-793. See H2.
- HEADING TemporalEquilibrium: FAIL: The mathematical conclusions are complete in TemporalEquilibrium.lean:470-474,633-645 and match manuscript/notes/integrated_temporal_equilibrium.tex:13-22,37-51. Nevertheless, neither required coverage row contains conclusion: full: coverage.yaml:312-318,916-922. Thus heading:7169 and Index:510-511 do not meet the explicitly required category-A metadata condition. See H3.
- HEADING TerminalWick: FAIL: The heading at candidate/statement-ledger.md:7251 correctly identifies category B and added measurability, but omits real-only coupling, unconstructed terminal-chain identification and mixed-moment-only comparison. These are explicit in TerminalWick.lean:623-640,669-683 and ledger:7264-7277,7316-7334, versus main manuscript:3607-3608,3641-3644. See H4.
- HEADING VariationalRate: FAIL: The heading correctly names the operator half and Q_2 inequality as missing, but omits the stochastic-cost identification. VariationalRate.lean:779-780 expressly uses rawCost, not E W(Psi)^2; ledger:8270-8276 confirms the additional gap. Index:634 overstates the scope as everything except Q_2. See H5.
- HEADING WaveTwoVariances: FAIL: The spectral core is accurately called full, but named inputs do not name the remaining abstraction gap. WaveTwoVariances.lean:908-916 takes abstract P, J, normSG and var; the manuscript bounds E|ell_R|^2 on its actual phase spaces at integrated_wave_variance.tex:368-383. Ledger:8675-8683 admits the missing construction/identification. See H6.
- HEADING HermiteWordFock: FAIL: Category B is correct, but the heading names only the one-mode restriction. HermiteWordFock.lean:43-48 proves a single List word, and its:21-23 explicitly excludes finite sums and Bochner integrals. Main manuscript:2551-2552 includes those conclusions. Ledger:1064-1068 acknowledges the omission absent from heading:1034. See H7.

Findings, fatal (0):

Findings, major (8):
- H1 SpatialOccupationL7Completed: incomplete category-B heading. Lean states 'Tendsto (fun n => C4 ...) atTop' at lean/StratonovichHAMSecondMoment/SpatialOccupationL7Completed.lean:182-192; TeX states 'jointly continuous on (H^1)^4' at manuscript/notes/integrated_spatial_occupation.tex:229-230. candidate/statement-ledger.md:6407-6408 explicitly retains the sequential-only boundary, omitted from heading:6349. Exact fix: append 'joint continuity only in sequential form' to that heading, retaining the class-O and rate/cost gaps; qualify Index:728 and:734 as narrower completion wrappers with their respective retained boundaries.
- H2 SymplecticFree: supplied inputs are not a complete description of missing conclusions. Lean explicitly says 'the operator J_E ... and the preservation of omega by S_E on all of E ... are not formalized' at lean/StratonovichHAMSecondMoment/SymplecticFree.lean:723-725, whereas TeX asserts 'There is a bounded isometric skew-adjoint J_E' and 'The free group preserves omega' at manuscript/notes/integrated_symplectic_phase.tex:32-40. The force wrapper concludes only the omegaL2 identity at SymplecticFree.lean:707-714. Exact fix: replace the qualifier at candidate/statement-ledger.md:7023 and its Index repetitions:789-793 with 'narrower result: J_E, the duality-form identification and symplectic preservation on E not formalized; force skewness only at L2 level; free-group data and Young convergence supplied'.
- H3 TemporalEquilibrium: category-A coverage prerequisite is absent. Lean concludes 'MemLp (density a) 1 ...' and 'MemLp (density a) 2 ...', the endpoint potential and exact positive mass at lean/StratonovichHAMSecondMoment/TemporalEquilibrium.lean:633-645, matching TeX 'belongs to L^1(0,1) intersect L^2(0,1)' and its displayed identities at manuscript/notes/integrated_temporal_equilibrium.tex:42-48; gamma_beta_paper:470-474 likewise matches TeX:13-22. But lean/coverage.yaml:312-318 and:916-922 contain no conclusion field. The strict rule at candidate/statement-ledger.md:62-66 requires conclusion full, not merely same-assumptions. Exact fix: add 'conclusion: full' to both coverage rows; the mathematical evidence supports retaining the whole-result heading and Index cells.
- H4 TerminalWick: the category-B heading omits additional substantive boundaries. Lean quantifies 'forall r : real' at lean/StratonovichHAMSecondMoment/TerminalWick.lean:640, takes arbitrary nu with a mass hypothesis at:623-624, and compares individual mixed moments at:681-683. TeX asserts convergence for 'every real or complex r' and comparison of 'all finite partial-order second moments' at manuscript/notes/notes_stratonovich_ham_second_moment.tex:3641-3644, using the actual terminal-chain measure at:3607-3608. Exact fix: extend candidate/statement-ledger.md:7251 and classify its main Index cell:785 to disclose real coupling only, mixed-moment comparison only, and the unformalized actual-chain construction/mass identification, while retaining supplied-input and added-measurability disclosures.
- H5 VariationalRate: missing stochastic-cost identification is omitted from the heading and contradicted by the Index's exhaustive wording. Lean says 'rawCost ... not E W(Psi)^2' at lean/StratonovichHAMSecondMoment/VariationalRate.lean:779-780; TeX defines the 'original variance v_Psi = E W(Psi)^2' at manuscript/notes/integrated_unmasked_variational.tex:17-18 and uses it in the score set at:272-279. candidate/statement-ledger.md:8275-8276 acknowledges this gap, but heading:8212 omits it and Index:634 says 'everything except Q_2 >= S_2^pos'. Exact fix: add the missing cost identification to the heading and replace that Index qualifier with 'narrower result: Rayleigh-form rates and integral-form costs, their spectral/stochastic identification and Q_2 >= S_2^pos not formalized', retaining the S1Bdd disclosure.
- H6 WaveTwoVariances: the category-B heading does not identify its modelled-object boundary. Lean takes '(var : ... P -> P -> real)' and only an upper-bound hypothesis hlink at lean/StratonovichHAMSecondMoment/WaveTwoVariances.lean:908-916. TeX concludes bounds on the actual 'E|ell_R(I;e_k,z)|^2' and reversed variance at manuscript/notes/integrated_wave_variance.tex:371-382. Neither actual ell_R nor its phase-space identification is constructed, as candidate/statement-ledger.md:8675-8683 records. Exact fix: replace heading:8580 and Index qualifier:624 with a category-B description explicitly naming abstract variance/phase spaces and the unformalized identification with the manuscript objects, while preserving the named inputs and full spectral-core statement.
- H7 HermiteWordFock: one-mode wording is not the complete narrowing. Lean proves a single '(w : List (Fin m × B))' equality at lean/StratonovichHAMAudit/HermiteWordFock.lean:43-48 and explicitly excludes sums/integrals at:21-23. TeX additionally says 'The equality holds for finite sums and for Bochner integrals of such words' at manuscript/notes/notes_stratonovich_ham_second_moment.tex:2551-2552. Exact fix: change candidate/statement-ledger.md:1034 to 'narrower result: L:finite-word-cutoff for one Gaussian mode per color and single finite words; finite sums and Bochner integrals not formalized'; give Index:865 the same category-B qualification.
- H8 SpatialFourLinear, SpatialOccupationCompleted and SpatialSmoothRatio: retained Index qualifiers do not implement the strict category-B convention. Lean's shared definitions are explicitly 'rawCost' in integral form and a 'rate' whose identification is not formalized at lean/StratonovichHAMSecondMoment/VariationalDilation.lean:236-247. TeX uses the original variance 'v_Psi = E W(Psi)^2' at manuscript/notes/integrated_unmasked_variational.tex:17 and the corresponding score conclusions at manuscript/notes/integrated_spatial_occupation.tex:50-53,171-176,316-322. Their headings disclose these gaps, but candidate/statement-ledger.md:700 names only the proved energy fragment, :655 says 'both claims', and :661-662 say only 'completed wrappers'. Exact fix: add 'narrower result: rate and cost identification not formalized' to these main-result Index cells, retaining their existing fragment, completion and supplied-input information. Completion alone must not erase the category.

Findings, minor (0):

Required repairs (8):
- H1: Add the retained sequential-continuity boundary to the SpatialOccupationL7Completed heading and accurately classify its principal completion Index cells.
- H2: Make the SymplecticFree heading and repeated Index qualifiers name the missing J_E, duality and full-E symplectic conclusions, not merely supplied inputs.
- H3: Add conclusion: full to the L:equilibrium-gamma-beta and L:temporal-equilibrium coverage rows.
- H4: Complete the TerminalWick heading and principal Index classification with the real-only, mixed-moment-only and unconstructed actual-chain boundaries.
- H5: Add the stochastic-cost identification gap to VariationalRate and remove the Index claim that only the Q_2 inequality is missing.
- H6: Identify the abstract variance/phase-space substitution in the WaveTwoVariances heading and principal Index cell.
- H7: Add the single-word restriction and missing finite-sum/Bochner-integral conclusions to the HermiteWordFock heading and Index qualification.
- H8: Apply explicit, accurately scoped category-B qualifiers to the SpatialFourLinear, SpatialOccupationCompleted and SpatialSmoothRatio main-result Index cells identified above.

Limitations (6):
- Requirement A was completed. Partial-file coverage entries omit material outside the required selections; required passages and wrappers were read without remaining gaps.
- Proof correctness, compilation and kernel replay were outside scope; no build was run.
- Packet hashes, repository history and the documentation-only nature of the revision were not independently authenticated. PROVENANCE.json, claims.yaml and the complete diff were not audited.
- Unrelated ledger classifications, aggregate module/result counts and the full claims inventory were not recertified.
- No incorrect numerical constant was identified in the checked correspondence; the blocking findings concern scope descriptions, Index classifications and required coverage metadata.
- This AI correspondence review is not human verification or a novelty audit.

## h4-index-cells

Preflight: contract-check CONTRACT-OBSERVABLE (14 required field(s), 0 dispatch input(s); no provider call); dry run exit 0 (dryrun/); contract-check with --dispatch-input dryrun/prompt.txt CONTRACT-OBSERVABLE (14 required field(s), 1 dispatch input(s); no provider call)

Driver log:
```
2026-11-12T16:15:36Z start attempt-01
2026-11-12T16:21:32Z attempt-01 exit=3 Status: review-complete
2026-11-12T16:21:32Z done
```
### attempt-01
```
# CLI review attempt

Status: review-complete

Scientific verdict: INCONCLUSIVE

Accepted: False

See receipt.json, input-manifest.json, prompt.txt, and retained transport.
```
Verdict: **INCONCLUSIVE**, confidence: **low** (attempt-01)
Check verdicts: INCONCLUSIVE 4 (of 4)

Checks not PASS/PASS_WITH_NOTES:
- INDEX-CELLS lines 475-574: INCONCLUSIVE: The entire Index range and heading list were read, but the required declaration-level reading was not completed. A definite convention mismatch remains: line 477 gives the unqualified labelled corollary for RawValueCeiling.strict_log_gap, although its section at line 1249 is category C and its Lean conclusion is only the scalar logarithmic inequality (RawValueCeiling.lean:12-14), not the corollary's moment bracket (integrated_occupation_ceiling.tex:252-266). See H1.
- INDEX-CELLS lines 575-673: INCONCLUSIVE: Required declaration-level reading was incomplete. Independently, cells 661-662 do not carry or accurately reference their section's category-B limitation at line 6297: completion removes named inputs but leaves Rayleigh-rate/integral-cost modelling. The completed score conclusion explicitly uses integratedRate and rawCost (SpatialOccupationCompleted.lean:169-176). See H2.
- INDEX-CELLS lines 674-772: INCONCLUSIVE: Required declaration-level reading was incomplete. Examined counterexamples include the undisclosed class-O limitation in cell 734, the blanket 'nothing supplied' qualifiers in cells 728-729 despite retained analytic hypotheses, and the category-B wording for mere foundation definitions in cell 744. Evidence: SpatialOccupationL7Completed.lean:85-116,323-374; OccupationPhysicalClass.lean:154-158; SpaceTimePositivity.lean:329-341,1120-1122. See H2-H4.
- INDEX-CELLS lines 773-869: INCONCLUSIVE: Required declaration-level reading was incomplete. Cell 785 still says only 'L:terminal-wick (TerminalWick)' rather than stating or accurately referencing its narrower scope. The listed wrapper assumes supplied measurability, arbitrary measures specified by their masses, and an added covariance-measurability hypothesis, and concludes convergence only for real r (TerminalWick.lean:618-642), whereas the manuscript uses the constructed terminal-chain measures and states real or complex r (main TeX:3585-3598,3643-3644). See H5.

Findings, fatal (0):

Findings, major (5):
- H1 — Category-C audit cells remain unqualified labelled results. candidate/statement-ledger.md:477 reads only '`C:intrinsic-spatial-bracket`', whereas its section at 1249 says '(proof steps)'. Lean proves '0 < (q*Real.log q+(q-2*a)*Real.log (q-2*a))/2 -(q-a)*Real.log (q-a)' (lean/StratonovichHAMAudit/RawValueCeiling.lean:12-14). The labelled TeX corollary instead asserts bounds on C_2 and an energy comparison (manuscript/notes/integrated_occupation_ceiling.tex:252-266); the logarithmic inequality appears in its proof at 275-283. Exact fix: change this cell to '`C:intrinsic-spatial-bracket` (proof steps: scalar logarithmic gap only)' and apply the required proof-step classification to the other unqualified audit mappings rather than leaving bare result labels.
- H2 — Completion cells omit the surviving category-B limitations. Cells 661-662 and 734 of candidate/statement-ledger.md say 'completed wrappers' without stating or explicitly referencing the relevant narrowing; their sections at 6297 and 6349 do state it. Lean's completed score conclusion is '∃ Ψ ∈ CPos d, y < integratedRate ... - rawCost ... / 2' (lean/StratonovichHAMSecondMoment/SpatialOccupationCompleted.lean:169-176). The occupation wrappers quantify over 'OccupationPhysicalClass.IsOccField G DG' (SpatialOccupationL7Completed.lean:323-325,363-365), whose fields require joint a.e. strong measurability (OccupationPhysicalClass.lean:154-158). TeX defines O through strong H^1-measurability and claims the energy over 'exactly this full class' (manuscript/notes/integrated_spatial_occupation.tex:381-403). coverage.yaml:1364-1367 explicitly records the missing identification. Exact fix: mark cells 661-662 as narrower results for the Rayleigh-rate/integral-cost conclusions, retaining their existing supplied-input qualifications; mark cell 734 'narrower result: class O modelled by joint representatives; bridge not formalized; SquarePairingBounds discharged'.
- H3 — 'Nothing supplied' incorrectly covers conditional general helper theorems. candidate/statement-ledger.md:728 includes squareBound_of_smooth_completed under that qualifier, but Lean retains 'hsm : ∀ φ ψ, ... pairing ... ≤ ...' (lean/StratonovichHAMSecondMoment/SpatialOccupationL7Completed.lean:85-90). Cell 729 similarly includes C4_square_CS_completed and square_pairing_CS_completed, both retaining 'hB : SquareBound Γ alpha R' (same file:97-109). SquareBound is itself the analytic pairing estimate (SpatialFourLinear.lean:461-464). TeX derives that estimate by Fatou before using it for Cauchy-Schwarz (manuscript/notes/integrated_spatial_occupation.tex:270-285). Only the density input has been discharged in these general helpers. Exact fix: split or qualify these cells: the exact-hypothesis paper wrappers have nothing supplied; squareBound_of_smooth_completed retains hsm, and the two general Cauchy-Schwarz helpers retain SquareBound.
- H4 — Foundation definitions are classified as a narrower labelled result. candidate/statement-ledger.md:744 calls the SpaceTimePositivity declarations a 'narrower result' of E:positive-bochner-inclusion, contrary to the category-C heading at 5720 and Scope at 72-75. Lean's 'def stPair', 'def stForm', and 'def stFormIter' only define physical integral expressions (lean/StratonovichHAMSecondMoment/SpaceTimePositivity.lean:329-341,1120-1122). TeX's display asserts a bounded map J_G, its covariance-space norm identity, and its bound (manuscript/notes/integrated_intrinsic_constant.tex:24-30). Exact fix: classify cell 744 as 'foundation: definitions of the physical space-time integral forms only; J_G and its covariance-space norm identity not formalized', not as a labelled narrower result.
- H5 — TerminalWick's principal Index cell does not disclose its category-B scope. candidate/statement-ledger.md:785 gives only '`L:terminal-wick` (TerminalWick)', despite the narrower-result heading at 7251. Lean assumes 'hmass', 'hmeas', and 'hK : Measurable ... K ...' and concludes '(∀ r : ℝ, Summable ...)' (lean/StratonovichHAMSecondMoment/TerminalWick.lean:623-640). TeX constructs the actual chain measure (manuscript/notes/notes_stratonovich_ham_second_moment.tex:3585-3598), assumes cellwise mean-square continuity rather than global covariance measurability (3600-3605), and states convergence for 'every real or complex r' (3643-3644). Exact fix: replace the qualifier with 'narrower result: real r only; chain measures specified by masses, hmeas supplied; Wick formula additionally assumes hK', or explicitly reference a section qualification containing those limitations.

Findings, minor (0):

Required repairs (5):
- Apply category-C proof-step wording to the unqualified audit Index mappings, including line 477 (H1).
- Disclose or explicitly reference the surviving category-B modelling limitations in completion cells 661-662 and 734 (H2).
- Restrict 'nothing supplied' in cells 728-729 to the appropriate paper wrappers and disclose the general helpers' retained hsm/SquareBound hypotheses (H3).
- Reclassify cell 744 as foundation definitions, distinguishing them from the labelled inclusion assertion (H4).
- Add the narrower-result scope and restrictions to TerminalWick's principal Index cell 785 (H5).

Limitations (5):
- Requirement A was not completed: although the category definitions, complete Index, complete heading list, coverage.yaml and excerpts were read, most required Lean declaration statements were not examined. All four checks therefore remain INCONCLUSIVE; the findings are established examples, not an exhaustive inventory.
- Partial Lean files were read only at the ranges listed; unlisted declaration signatures and their surrounding parameter contexts remain unchecked.
- Authoritative manuscript passages were inspected for the reported findings, not for every Index mapping.
- Packet hashes and source-revision byte bindings were not independently verified.
- Proof correctness was outside scope. This AI review is neither human verification nor a novelty audit.

## h5-consistency-r1-diff

Preflight: contract-check CONTRACT-OBSERVABLE (14 required field(s), 0 dispatch input(s); no provider call); dry run exit 0 (dryrun/); contract-check with --dispatch-input dryrun/prompt.txt CONTRACT-OBSERVABLE (14 required field(s), 1 dispatch input(s); no provider call)

Driver log:
```
2026-11-12T16:15:36Z start attempt-01
2026-11-12T16:23:15Z attempt-01 exit=0 Status: review-complete
2026-11-12T16:23:15Z done
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
Check verdicts: PASS 5 (of 5)

Findings, fatal (0):

Findings, major (0):

Findings, minor (0):

Required repairs (0):

Limitations (5):
- Requirement A is complete; truncated outputs were reread. Partial-file coverage outside those required selections is explicitly identified above.
- This is a narrow documentation-correspondence review, not a fresh certification of every unchanged ledger declaration. The claims inventory was parsed for counting, not reviewed semantically in full.
- Proof correctness, compilation and kernel replay were outside scope; no build was run.
- Provenance metadata was inspected only at lines 1-46. File hashes and repository history were not independently authenticated.
- This AI review is not human verification or a novelty audit.

