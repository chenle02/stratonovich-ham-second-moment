# Wave L8 correspondence reviews: summary

Companion 3518233 (35182337601a), manuscript a284420; reviewer Codex gpt-6.1-sol, effort high, min-confidence high.

Groups g1-g6 are under l8rev/; the reruns g5b (packet adds the StratonovichHAMAudit step modules, missing from g5) and g6a/g6b/g6c (g6 split after it could not complete its reading) are under l8rev-b/. g5 and g6 attempt-01 are packet-gap/size INCONCLUSIVE results (not tool failures), kept as record.

## g1-spectral-damped

Driver log:
```
2026-11-12T13:40:34Z start attempt-01
2026-11-12T13:47:19Z attempt-01 exit=2 Status: review-complete
2026-11-12T13:47:19Z done
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
Check verdicts: PASS 43, PARTIAL 2, FAIL 4 (of 49)

Checks not PASS/PASS_WITH_NOTES:
- StratonovichHAMSecondMoment.DampedMultiplier.damped_homogeneous_norms_full_wave: L:damped-homogeneous-norms: PARTIAL: Ledger:1477 and claims.yaml:12476-12482 accurately paraphrase DampedMultiplier.lean:547-585, whose hypothesis is H:homog alone. However, the ledger labels it 'whole result with nothing supplied'. TeX notes_stratonovich_ham_second_moment.tex:845-846 asserts Green smoothing gives a multiplier for the wave norms in all permitted dimensions; the declaration concludes only an equality between N2GreenSq expressions, not their identification with N2onSq. That identification is separate at DampedMultiplier.lean:594-606 and restricted to d = 1. See W2.
- PARA-SpectralMassIdentity: PARTIAL: The main correspondence, constants, open-ball discussion, Γ = 0 allowance, used fields and alternative proof route at ledger:5397-5475 are accurate. But ledger:5485-5486 says the alpha-zero controls give R_0 = 0 'under any reading of the quotient'. SpectralMassIdentity.lean:80-81 evaluates 0/0 using Lean's totalized division; TeX notes_stratonovich_ham_second_moment.tex:531 has no such convention. This is materially inaccurate; see W3.
- PARA-DampedMultiplier: FAIL: Most detailed descriptions at ledger:1328-1435 correctly disclose supplied GreenFourier, dimension-one identification and the omitted covariance-smoothing identity. Nevertheless ledger:1323-1326 asserts 'every assertion of the lemma is a Lean conclusion' of full_wave. DampedMultiplier.lean:582-585 supplies only the generic transform-norm equality, whereas the wave-norm identification is dimension one at 594-606. The acknowledged reading does not make the stronger summary correct. See W2.
- COVERAGE-ROWS: FAIL: The spatial-bound row at coverage.yaml:528-547 correctly records same-assumptions/full and the R_alpha theorem. The damped row correctly uses conclusion: weaker and its note at 207-209 accurately describes membership-only covariance smoothing. However its conclusion_scope at 165 contradicts that limitation by saying 'spatial Gaussian smoothing ... [is] proved in every dimension'. Only Gaussian-factor membership is proved; the spectral measure of p_eps * Γ is not identified. All listed claim IDs exist. See W1.
- REFUTATIONS: FAIL: All eight files prove the displayed formal negations or counterexamples. Six have the claimed genuine finite/integrable witnesses. AlphaPositive.lean:9-12,35-46 and FourierBoundAlphaZero.lean:15-16,57-67 rely on evaluating the quotient at alpha = 0 as Lean's 0/0 = 0. The ledger's claim at 5485-5486 that this works 'under any reading' is false: ordinary division is undefined there, and the continuous extension of alpha*pi/(2*sin(pi*alpha/2)) is 1. See W3.
- CROSS-REFERENCES: FAIL: The R_alpha cross-references and the explicit omissions at ledger:7407-7414 are accurate. But Scope:192-197, Index:630, and WaveGreen prose:6986-6988 call full_wave the full lemma despite the dimension-one-only wave-norm identification and the membership-only covariance-smoothing reading. These summaries must retain the narrower scope rather than override it. See W2.

Findings, fatal (1):
- W1 — COVERAGE-ROWS: lean/coverage.yaml:165 and docs/coverage-scope-tex.yaml:14-15 say 'spatial Gaussian smoothing ... [is] proved in every dimension'. Lean DampedMultiplier.lean:223-228 proves only '0 ≤ η → IsMultiplier (gaussMult η)'; ledger:1391-1395 explicitly says the spectral identity for p_eps * Γ 'is not stated'. TeX notes_stratonovich_ham_second_moment.tex:845-846 says spatial Gaussian smoothing gives a multiplier, which identifies an operation, not merely membership of an unrelated factor. Fix both scope sentences to say explicitly that covariance smoothing is represented only by Gaussian-factor membership and that its spectral identity is not formalized. Retain conclusion: weaker.

Findings, major (2):
- W2 — PARA-DampedMultiplier, full_wave row and CROSS-REFERENCES: ledger:1323-1326 says 'every assertion of the lemma is a Lean conclusion' of full_wave; ledger:1477,192-197,630,6986-6988 repeats whole/full-result language. Lean DampedMultiplier.lean:582-585 concludes N2GreenSq(p*G, μ) = N2GreenSq(G, mμ), not equality with the waveHat-defined N2onSq. The latter is proved without a supplied Fourier identity only for d = 1 at DampedMultiplier.lean:594-606. TeX notes_stratonovich_ham_second_moment.tex:226,845-846 applies the smoothing assertion in d = 1,2,3. Fix these summaries and the row/index qualifiers to describe the extended spectral and mass conclusions, explicitly retaining the dimension-one limitation and membership-only covariance-smoothing reading. Merely citing the later limitations does not justify calling full_wave the full lemma.
- W3 — PARA-SpectralMassIdentity and REFUTATIONS: ledger:5485-5486, AlphaPositive.lean:10-12 and FourierBoundAlphaZero.lean:15-16 claim R_0 = 0 'under any reading' because its numerator is zero. Lean SpectralMassIdentity.lean:80-81 and AlphaPositive.lean:44-46 instead evaluate 0/0 using totalized division. TeX notes_stratonovich_ham_second_moment.tex:531 gives the quotient under the positive-alpha domain of H:homog at 240 and supplies no alpha-zero convention. Ordinary division is undefined at the witness; the continuous extension of the coefficient alpha*pi/(2*sin(pi*alpha/2)) equals 1, not 0. Fix the ledger and refutation comments to identify these as controls of the Lean-totalized extension outside the manuscript domain, remove the quotient-independent claim, and do not present them as convention-independent numerical counterexamples.

Findings, minor (1):
- W4 — Scope attribution: ledger:189-192 attributes 'R_Gamma(1) = R_alpha' to spatial_fourier_bound_ralpha_paper. Lean SpectralMassIdentity.lean:272-285 uses that identity but does not conclude it; resolvent_eq_ralpha_paper at 228-236 does. TeX integrated_spatial_occupation.tex:153-154 states the identity separately. Optional clarification: name resolvent_eq_ralpha_paper for the identity and spatial_fourier_bound_ralpha_paper for its bound consequence.

Required repairs (3):
- Correct the damped conclusion_scope and its ASCII/TeX copies as specified in W1, explicitly distinguishing Gaussian-factor membership from the unformalized covariance-smoothing spectral identity.
- Replace the full/whole-result assertions about damped_homogeneous_norms_full_wave in the target prose, row qualifier, Scope, Index and WaveGreen cross-reference with the narrower scope specified in W2.
- Correct the alpha-zero refutation descriptions and comments as specified in W3: disclose dependence on Lean's totalized division and remove the assertion that 0/0 is zero under any reading.

Limitations (5):
- The complete-reading requirement A was completed for its scoped sections, declarations, entries, audit/refutation files, excerpts and cited authoritative TeX ranges. Context modules and unrelated ledger sections were inspected selectively, as reflected in source_coverage.
- PROVENANCE.json outside the reported ranges and manuscript-anchor.json outside the reported ranges were not read completely; these were contextual metadata inspections, not a byte-binding or historical-revision audit.
- Compilation and standard-axiom status were accepted as supplied. The audit files contain #check/#print commands, not captured elaboration output; no build was launched.
- The external source's Gaussian normalization was not independently checked; that source is not included in the frozen packet.
- This is an AI correspondence review, not human verification or a novelty audit.

## g2-spacetime-ceiling

Driver log:
```
2026-11-12T13:40:34Z start attempt-01
2026-11-12T13:50:18Z attempt-01 exit=0 Status: review-complete
2026-11-12T13:50:18Z done
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
Check verdicts: PASS 81, PASS_WITH_NOTES 3 (of 84)

Findings, fatal (0):

Findings, major (0):

Findings, minor (3):
- W1 — PARA-SpaceTimePositivity: ledger:4371-4380 says 'Every field in the statements' is continuous compactly supported and 'Integrability of every integrand is a conclusion'. This is broader than the actual auxiliary types: SpaceTimePositivity.lean:143-145 assumes only support and pointwise bounds, and :804-806 assumes continuity but not compact support. TeX integrated_intrinsic_constant.tex:84-92 concerns the genuine integrals used in the main identities. Optional clarification: restrict these prose sentences to the principal space-time positivity and mean/variance statements, excluding the explicitly totalized auxiliary bounds. The table already states the exceptions correctly.
- W2 — CROSS-REFERENCES: ledger:2751-2752 calls integratedRate_sq_le and score_le_ceiling '(no manuscript label)', whereas ledger:3600-3601 and Index:643,646 map them to T:intrinsic-occupation-ceiling or its proof. Lean OccupationCeilingFinite.lean:836-840,893-897 supplies the larger-constant versions of TeX integrated_occupation_ceiling.tex:224-245. Optional clarification: replace the parenthetical with 'route lemmas, not separately labelled manuscript results'; their stated mathematical scope is already correct.
- W3 — REFUTATIONS: the controls are accurate for their advertised generic Lean types, but some formal witnesses lie outside the manuscript's standing ranges. WrongRowConstant.lean:25-33 uses p=0, corresponding to a=1 rather than TeX main file:226's 0<a<1; ZeroScoreMax.lean:23-33 uses alpha=0 rather than main TeX:240's positive alpha. CSConstant.lean:9-12 and VarianceFactor.lean:9-12 use Lebesgue spatial covariance, outside the positive-homogeneity-exponent model. Optional clarification: identify these explicitly as controls for the generalized auxiliary statements, or add manuscript-admissible witnesses. This does not invalidate the negative controls as currently typed or the reviewed correspondence conclusions.

Required repairs (0):

Limitations (4):
- This is an AI correspondence review, not human verification or a novelty audit.
- Compilation and absence of nonstandard axioms were stipulated; no compiler or proof-checking workflow was run. The supplied Audit files are source commands requesting checks, not captured elaboration transcripts.
- The two target modules, required ledger sections, claim entries, coverage rows, refutations, audits, excerpts and cited authoritative TeX ranges were read completely. Partial contextual files were inspected only in the ranges listed; their unrelated declarations and earlier-wave results were not independently re-reviewed.
- The ledger's historical statement about the pre-a284420 proof route cannot be independently reconstructed from older manuscript sources absent from this frozen packet; its present numerical consequence follows from the supplied revision.

## g3-bracket-mask-cauchy

Driver log:
```
2026-11-12T13:40:34Z start attempt-01
2026-11-12T13:52:45Z attempt-01 exit=0 Status: review-complete
2026-11-12T13:52:45Z done
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
Check verdicts: PASS 102, PASS_WITH_NOTES 2 (of 104)

Findings, fatal (0):

Findings, major (0):

Findings, minor (1):
- W1 — Optional standalone-row clarity for the Cauchy estimates. candidate/statement-ledger.md:5595-5596 abbreviates the side conditions, while Lean StaticPhaseCauchy.lean:193-194 explicitly requires '0 < rho' and :215-216 requires an entire map, '0 < c' and '0 <= d'. TeX notes_stratonovich_ham_second_moment.tex:2301, 2487, 2613-2623 supplies positive radii and c=delta*lambda^(2-alpha/2), d=d_n>=0; claims.yaml:14593, 14600 states the conditions explicitly. Thus the intended manuscript application is sound. Optional fix: repeat these conditions in the two ledger cells so they can be read independently.

Required repairs (0):

Limitations (4):
- This is an AI correspondence review, not human verification or a novelty audit.
- Lean compilation and axiom admissibility were accepted as stipulated; no build was launched. The audit files contain checking commands and consumers, not captured elaboration logs.
- Coverage statements concern the contract's required ranges and named declarations, not a fresh review of earlier waves or the entire manuscript. Other manuscript files were searched for label uniqueness; byte hashing was not treated as substantive mathematical reading.
- External operator, Gaussian, spectral-ground-rate and canonical-solution identifications remain external exactly as disclosed by the candidate.

## g4-wick

Driver log:
```
2026-11-12T13:40:34Z start attempt-01
2026-11-12T13:50:18Z attempt-01 exit=2 Status: review-complete
2026-11-12T13:50:18Z done
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
Check verdicts: PASS 85, FAIL 6, PASS_WITH_NOTES 1 (of 92)

Checks not PASS/PASS_WITH_NOTES:
- StratonovichHAMSecondMoment.TerminalWick.mixed_moment_eq_sum_pairings: E:terminal-wick-formula: FAIL: Fidelity passes: TerminalWick.lean:389-396, ledger:5935 and claims.yaml:13975 all include supplied hmeas, finite ν and 'hK : Measurable ... K'. Mapping fails as an exact-hypothesis specialization: TeX:3601-3605 requires bounded variance and mean-square continuity only on open cells, not globally Borel-measurable covariance. Cut-time values need not be Borel measurable. The section incorrectly treats this additional hypothesis as merely implicit; see W1.
- StratonovichHAMSecondMoment.TerminalWick.terminal_wick_paper: L:terminal-wick: FAIL: TerminalWick.lean:610-634 has the nine conjuncts, correct factorial majorant, odd case and real-r quantifier described by ledger:5953 and claims.yaml:14101. However its hypothesis 'hK : Measurable ... K' at 618 is stronger than TeX:3601-3605's cell-wise mean-square continuity. Ledger:5953 calls this an 'Exact-hypothesis wrapper' and calls hK implicit, which is false without an additional convention or modification argument. See W1.
- PARA-FiniteWick: FAIL: The pairing representation, Gaussian-law abstraction, constants and Stein-versus-generating-function route are accurately described at ledger:1877-1913. But ledger:1902-1903 says every integral identity has integrability 'as a conjunct', and 1914-1915 says every Bochner integral has proved integrability. FiniteWick.lean:578-589 only assumes Continuous F and states a totalized integral equality plus a separate integrability equivalence. This is a false universal guarantee; see W2.
- PARA-TerminalWick: FAIL: Ledger:5840-5912 correctly records the unconstructed measures, supplied hmeas, factorial masses, real-r restriction, per-mixed-moment comparison, unused hypotheses and omitted identification paragraphs. Its classification of global covariance measurability as implicit at 5875-5879,5953 is not justified by TeX:3601-3605 and fails at unrestricted cut-time values. See W1.
- COVERAGE-ROWS: FAIL: coverage.yaml:635-671 correctly uses inputs-supplied/weaker and discloses real r, arbitrary mass-normalized measures and mixed-moment-only comparison. All listed claim IDs exist. Nevertheless the two-item inputs list omits the genuinely additional global covariance-measurability assumption used by the formula wrapper; merely calling it explicit in the note does not explain the stronger scope. See W1. The uniform-tail row at 682-704 correctly has full conditional conclusions: TerminalWickInput is exactly discharged, and the composition at L8Completed.lean:312-357 does not require hK.
- CROSS-REFERENCES: FAIL: The uniform-tail references at ledger:233-241,580-584,2783-2812,6282-6298,6351-6354 and the exclusions at 7485-7494 are substantively accurate. However the Scope summary at 269-273 says 'every conclusion for real r' without the independently acknowledged restriction at 5893-5895: the comparison is stated only for individual mixed moments, not finite-partial-sum second moments. Scope:281-283 also incorrectly subsumes the global hK requirement under implicit measurability. See W1 and W3.

Findings, fatal (1):
- W1 — TerminalWick covariance measurability is an additional hypothesis, not an implicit consequence of the stated TeX assumptions. Lean TerminalWick.lean:618 requires 'hK : Measurable fun q => K q.1 q.2'; the formula theorem has the same requirement at 392. TeX manuscript/notes/notes_stratonovich_ham_second_moment.tex:3601-3605 assumes a centered real Gaussian field, bounded variance, and joint mean-square continuity only 'on each open cell' of a finite time partition. Those conditions leave cut-time values unrestricted. For example, take a standard Gaussian Z, an interior cut time c, a non-Borel set A in R^d, and W(t,y)=1_{t=c}1_A(y)Z. This is a bounded-variance centered Gaussian field, identically zero and mean-square continuous on every open cell; its actual-chain product maps are a.e. zero for positive order, satisfying the supplied hmeas. But its covariance is not globally Borel measurable, as a cut-time section recovers 1_A. Therefore ledger:5875-5879,5953 cannot describe hK as merely implicit or the wrapper as exact-hypothesis. Fix: either weaken the Lean requirement to suitable chain-measure-a.e. measurability and establish its manuscript applicability, or explicitly describe global covariance measurability as an additional restriction/supplied assumption in the ledger and coverage.yaml:661-671, updating the terminal conclusion-scope ASCII and TeX sentences consistently. Do not claim the original TeX hypotheses alone imply this hK.

Findings, major (2):
- W2 — PARA-FiniteWick overstates integrability and absence of junk values. Ledger:1902-1903 says every integral identity has integrability 'as a conjunct'; 1914-1915 says 'every Bochner integral appears with a proof of integrability'. Lean FiniteWick.lean:578-580 assumes only 'Continuous F' and equates two Bochner integrals; 586-589 proves an Integrable equivalence, not Integrable F. A continuous F such as exp(x_0^4) under a nondegenerate one-dimensional standard Gaussian is not integrable, so the bridge identity can equate totalized zero values. TeX manuscript/notes/notes_stratonovich_ham_second_moment.tex:3662-3673 concerns finite Gaussian monomials, whose integrability is indeed established by the Lean development. Fix the ledger paragraph to restrict its genuine-integral assurance to Gaussian monomials and explain that the arbitrary-continuous-function bridge is a totalized identity, with integrability transferred only conditionally. No change to the correctly paraphrased bridge rows is necessary.
- W3 — Scope omits one expressly acknowledged conclusion narrowing. Ledger:269-273 advertises L:terminal-wick as 'every conclusion for real r'. Lean TerminalWick.lean:674-675 concludes only 'E[Y1_m Y1_n] ≤ E[Y2_m Y2_n]' for each m,n, whereas TeX manuscript/notes/notes_stratonovich_ham_second_moment.tex:3641-3642 states comparison of 'all finite partial-order second moments'. Ledger:5893-5895 itself says second moments of finite partial sums are not stated as such. Although summing mixed-moment comparisons gives the mathematical implication, the review contract requires stated coverage to distinguish it. Fix Scope:269-273 to repeat the mixed-moment-only restriction, or add the finite-partial-sum comparison statement and adjust the narrower-scope descriptions consistently.

Findings, minor (1):
- W4 — Negative-control documentation is absent from the two target sections. Ledger:1875-1968,5838-5954 contains no description of the seven supplied refutations. The files themselves accurately document and prove their perturbations; for example PairingCount.lean:7-10,30-37 refutes '(2k)!/k!' against the unordered-pair convention of TeX manuscript/notes/notes_stratonovich_ham_second_moment.tex:3671-3673. Optionally add a short cross-reference list distinguishing combinatorial controls from actual Gaussian-field examples; NonnegDropped.lean:23-37 tests arbitrary weights rather than presenting a covariance matrix.

Required repairs (3):
- W1: Correct the treatment of global covariance measurability in the TerminalWick ledger prose, formula/wrapper correspondence and terminal coverage inputs/scope. Either supply a manuscript-valid a.e./modification bridge in Lean or explicitly classify global Borel measurability as an additional restriction, not an implicit TeX hypothesis. Keep the ASCII and TeX scope descriptions synchronized.
- W2: Remove the false blanket assertion that every FiniteWick integral identity includes or proves integrability. Explicitly distinguish proved monomial integrability from the totalized arbitrary-continuous-F bridge and its conditional integrability equivalence.
- W3: Make the Scope summary disclose that covariance comparison is stated per mixed moment rather than for second moments of finite partial sums, unless that latter conclusion is added as a Lean statement.

Limitations (6):
- The binding reading requirement A was completed. Partial-file entries above reflect the expressly scoped review, not gaps in required declarations, sections, registry entries or cited TeX ranges.
- In check reasons, FiniteWick.lean, TerminalWick.lean, UniformSeriesTail.lean and L8Completed.lean refer to their exact paths under lean/StratonovichHAMSecondMoment/ listed in source_coverage; ledger means candidate/statement-ledger.md; TeX means manuscript/notes/notes_stratonovich_ham_second_moment.tex.
- Lean compilation and standard-axiom status were accepted as stipulated. The supplied Audit files contain checking commands and consumer proofs, not captured elaborator output; no build or recompilation was performed.
- Historical recompilation claims and provenance hashes were read but not independently reproduced. No external Mathlib source, network material or earlier manuscript revision was consulted.
- The non-Borel cut-time example in W1 is a mathematical correspondence counterexample, not an additional machine-checked artifact.
- This AI correspondence review is neither human verification nor a novelty audit.

## g5-symplectic

Driver log:
```
2026-11-12T13:40:34Z start attempt-01
2026-11-12T13:46:13Z attempt-01 exit=3 Status: review-complete
2026-11-12T13:46:13Z done
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
Check verdicts: PASS 62, INCONCLUSIVE 2, PASS_WITH_NOTES 2 (of 66)

Checks not PASS/PASS_WITH_NOTES:
- StratonovichHAMSecondMoment.SymplecticFree.freeMatrix_eq_forward: L:symplectic-free: INCONCLUSIVE: Lean:177-180 assumes 'k ≠ 0' and 'br ≠ 0' and equates freeMatrix with the imported DimensionalMatrix.forward at q=k/br. TeX:74-76 displays the expected quotient matrix. Ledger:5709 and claims.yaml:14214 match the visible theorem type, but the required imported forward declaration is absent from the packet, preventing complete verification of its advertised expansion.
- PARA-SymplecticFree: INCONCLUSIVE: Ledger:5616-5692 correctly locates the TeX statement/proof, distinguishes frequency algebra from the abstract supplied group, describes the filter proof route and lists the omitted Sobolev/Young constructions. Full confirmation of the DimensionalMatrix comparison at 5633-5634 is blocked by its absent source. Minor wording issues remain concerning 'partitions' and the statement that T>0 is carried in both wrappers (W1,W2).

Findings, fatal (0):

Findings, major (0):

Findings, minor (3):
- W1 — LeftYoungSumsConverge terminology. Ledger:5657-5660,5743 says 'filter of partitions'; SymplecticFree.lean:545-547 requires only a nontrivial filter on (n,p), eventual node membership in [s,t], and convergence. It requires neither p(0)=s, p(n)=t, ordering, nor mesh tending to zero. TeX integrated_symplectic_phase.tex:94-98 uses genuine partition sums. The weaker condition is sufficient and is implied by the TeX, so this does not invalidate the baseline deduction. Optional clarification: call these 'finite node lists' and explicitly state the omitted partition/mesh conditions.
- W2 — Unused-hypothesis prose. Ledger:5669-5671 says 'T > 0 ... in both baseline wrappers'. SymplecticFree.lean:661 has '_hT : 0 < T', whereas the product wrapper at 681-689 has B and no positive-horizon hypothesis. TeX integrated_symplectic_phase.tex:43-51 likewise distinguishes [0,T] from the product horizon [0,B]. Optional fix: restrict the T>0 statement to the single-path wrapper.
- W3 — Not in Lean parenthetical scope. Ledger:7345-7349 groups the free group, J_E and preservation of omega before saying 'supplied ... as FreeWaveData'. SymplecticFree.lean:522-535 supplies only the group, reversal and translation data; TeX integrated_symplectic_phase.tex:32-40,63-84 separately constructs J_E and proves preservation. Optional fix: attach the supplied-input parenthesis only to the free-group data, and separately say that J_E and preservation are omitted.

Required repairs (1):
- Supply the frozen source declaration StratonovichHAMAudit.DimensionalMatrix.forward, including its namespace and relevant assumptions, so check 15 and the corresponding prose comparison can satisfy the mandatory declaration-reading requirement.

Limitations (5):
- Requirement A is incomplete for the explicitly named imported declaration DimensionalMatrix.forward: its module is not included in the packet. The visible equality theorem and its proof reference do not replace reading that declaration.
- The partial reads of WaveKernel.lean and L8Completed.lean include the complete additional declarations required for this review; unrelated declarations in those modules were not reviewed.
- PROVENANCE.json and manuscript-anchor.json were consulted selectively for revision/context metadata. Their remaining contents and all packet byte bindings were not independently audited.
- The audit file contains #check/#print-axioms commands, not captured elaboration output. No Lean build was run; compilation and absence of sorry/nonstandard axioms were accepted as stipulated.
- Earlier ledger waves and unrelated manuscript mathematics were not re-reviewed. This AI correspondence review is neither human verification nor a novelty audit.

## g6-l8completed-changes

Driver log:
```
2026-11-12T13:40:34Z start attempt-01
2026-11-12T13:54:04Z attempt-01 exit=3 Status: review-complete
2026-11-12T13:54:04Z done
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
Check verdicts: PASS 21, PASS_WITH_NOTES 2, INCONCLUSIVE 19, FAIL 7 (of 49)

Checks not PASS/PASS_WITH_NOTES:
- LEDGER-INDEX: INCONCLUSIVE: The structural scan found each of the seventeen declarations exactly once in the index, at ledger:693-703, under the requested labels; all seventeen distinct manuscript labels extracted from this section occurred exactly once. However, the complete Index-by-label reading required by A was not finished, so the full check cannot receive PASS.
- COVERAGE-ROWS: INCONCLUSIVE: All twelve requested coverage rows were read, and every coverage claim identifier exists in claims.yaml. The L8 completed wrappers support the advertised discharges. W1 identifies an established overstatement in the damped-norm scope sentence. Substantive verification of every other cited declaration, particularly the physical-class and static-phase rows, remains incomplete.
- CROSS-REFERENCES: FAIL: W2: ledger:192-197 calls L:damped-homogeneous-norms 'stated in full', and :6986-6988 again says 'The full lemma'. This conflicts with its undisclosed spatial-covariance smoothing gap and its acknowledged dimension-one-only identification of Green smoothing; see DampedMultiplier.lean:456-459,515-527,594-606 and TeX:845-847.
- CHANGED-ROW C:intrinsic-spatial-bracket: INCONCLUSIVE: Coverage.yaml:28-54 correctly discloses S_2 instead of C_2 and the substituted energy. The completed wrapper at L8Completed.lean:262-281 removes the ceiling input under H:homog and Gamma != 0. However, all scalar declarations added to this row were not read, and the prior file was not independently read.
- CHANGED-ROW L:damped-homogeneous-norms: FAIL: W1: coverage.yaml:165 and docs/coverage-scope-tex.yaml:14-15 say everything except the higher-dimensional Green-smoothing identification is proved, including spatial Gaussian smoothing in every dimension. DampedMultiplier.lean:458-459 explicitly excludes the spectral identity for p_epsilon * Gamma; ledger:1391-1395 and :7411-7414 retain that exclusion. Gaussian multiplier membership alone is not that object-identification assertion of TeX:845-846.
- CHANGED-ROW L:spatial-fourier-bound: INCONCLUSIVE: The manuscript bound and its exact constant were read at integrated_spatial_occupation.tex:101-164. The change to full coverage depends on SpectralMassIdentity declarations that were not substantively read; the identifier-existence scan does not verify their types.
- CHANGED-ROW L:spatial-static-controls: INCONCLUSIVE: The new supremum wrapper at L8Completed.lean:176-183 agrees with TeX integrated_spatial_occupation.tex:40-53 and removes S1Bdd. Verification of the complete coverage claim list, including the original positivity and Lipschitz wrappers, was not completed.
- CHANGED-ROW P:occupation-physical-class: INCONCLUSIVE: The wording change from line numbers to 'a simple-function approximation' agrees with TeX integrated_spatial_occupation.tex:409-414. The source physical-class and completion declarations needed to certify the entire changed row were not read.
- CHANGED-ROW P:spatial-energy-map: INCONCLUSIVE: The added completed supremum claim agrees with L8Completed.lean:210-215 and TeX integrated_spatial_occupation.tex:316-322. The underlying full energy-map theorem and every declaration cited by coverage.yaml:1104-1118 were not checked.
- CHANGED-ROW P:spatial-smooth-ratio: INCONCLUSIVE: The new completed score and quantitative R_0 wrappers agree with L8Completed.lean:189-204. The TeX's current Fourier proof and former score-based route are distinguished correctly. Full checking of the original module wrappers and the complete changed section was not finished.
- CHANGED-ROW P:static-phase-all-orders: INCONCLUSIVE: The coverage row and supplied-input list at coverage.yaml:1184-1224 were read, but the StaticPhaseCauchy source declarations and authoritative TeX ranges for their constants and cutoff hypotheses were not read.
- CHANGED-ROW P:variational-positive-scores: INCONCLUSIVE: The principal promotion to same-assumptions/weaker is supported by L8Completed.lean:140-170 versus integrated_unmasked_variational.tex:270-337. The complete set of older scalar/helper declarations cited by the changed row was not read, so the entire row check remains incomplete.
- CHANGED-ROW T:intrinsic-occupation-ceiling: INCONCLUSIVE: The same-assumptions/weaker classification itself is supported, as detailed in CLASS-OCCUPATION-CEILING. The complete added list of auxiliary ceiling declarations and prior-row comparison was not substantively checked.
- CHANGED-PASSAGE RawValueCeiling: INCONCLUSIVE: Ledger:1041-1052 and the authoritative corollary proof at integrated_occupation_ceiling.tex:275-299 were read. The added completion reference agrees with L8Completed.lean:262-281, but the packet supplies no RawValueCeiling Lean module for independently checking the earlier scalar declaration's type.
- CHANGED-PASSAGE DampedNormsHomog (whole result): FAIL: W1/W2: the changed sentences at ledger:1535-1540 and :1597-1601 broadly say the closing Gaussian spatial/Green smoothing remarks are proved. TeX:845-847 concerns actual smoothing of those objects. DampedMultiplier.lean:458-459 excludes the spatial-covariance spectral identity, and :515-527 requires GreenFourier for the norm identification, discharged only in dimension one at :594-606. These cross-references require the same qualifications as the coverage row.
- CHANGED-PASSAGE SpatialFourierBound (whole result): INCONCLUSIVE: The required whole ledger section, its changed hunks and the SpectralMassIdentity declarations supporting the new exact-constant statement were not completely read.
- CHANGED-PASSAGE SpatialFourLinear (whole result): INCONCLUSIVE: The required whole ledger section and its changed hunks were not completely read. The completed static-energy supremum wrapper itself was checked, but that does not establish this broader passage check.
- CHANGED-PASSAGE SpatialOccupationCompleted (whole result): INCONCLUSIVE: The whole ledger section at :4906-4956 was read, and its new claim that S1Bdd is discharged agrees with L8Completed.lean:140-170. The source completion declarations and required changed hunks were not completely read.
- CHANGED-PASSAGE SpatialOccupationL7Completed (whole result): INCONCLUSIVE: The whole ledger section at :4958-5045 was read. Its added completed supremum reference agrees with L8Completed.lean:210-215, but the corresponding source completion declarations and changed hunks were not completely checked.
- CHANGED-PASSAGE SpatialSmoothRatio (whole result): INCONCLUSIVE: The required whole ledger section :5047-5198 and its changed hunks were not completely read; only the relevant definitions and L8 completed wrappers were checked.
- CHANGED-PASSAGE SpatialStaticControls (whole result): INCONCLUSIVE: The required whole ledger section :5200-5393 and its changed hunks were not completely read. Checking the completed static-score wrapper does not establish all changed cross-references in this section.
- CHANGED-PASSAGE VariationalRate (whole result): INCONCLUSIVE: Ledger:6782-6899 and the changed hunks :1360-1389 were read. The added S1Bdd-discharge claim is supported by L8Completed.lean:140-170. Complete reading of the other declarations named by this section was not achieved.
- CHANGED-PASSAGE WaveGreen (whole result): FAIL: W2: the changed paragraph at ledger:6978-6988 correctly says the Gaussian-smoothed Green norm is identified with N_{2,m,S} only in dimension one, then incorrectly calls damped_homogeneous_norms_full_wave 'The full lemma'. TeX:845-847 asserts the smoothing remarks without that restriction; DampedMultiplier.lean:547-585 does not discharge the missing identification.
- CLASS-DAMPED-NORMS: FAIL: The weaker classification is correct, but the scope does not state all gaps exactly. The dimension-one limitation is real: DampedMultiplier.lean:515-527 takes GreenFourier G, and :594-606 discharges it only for d = 1. Additionally, :458-459 expressly says the spectral identity for spatial covariance smoothing p_epsilon * Gamma is not stated, whereas coverage.yaml:165 and docs/coverage-scope-tex.yaml:14-15 claim spatial Gaussian smoothing is proved in every dimension. TeX:845-846 concerns actual smoothing, not merely membership of exp(-eta|xi|^2) in a multiplier class. W1 requires correcting this scope assertion.
- LEDGER-TOTALS: FAIL: The structural counts agree for 2108 unique ledger declarations, 1747 theorem and 361 definition claims, exactly one row per claims.yaml declaration, 66 whole-result modules, and 986 no-direct-label rows. Coverage has 43 same-assumptions results, five inputs-supplied results with full/default-full conclusions, 20 inputs-supplied/weaker rows and three outside main theorems. However, there are FIFTEEN same-assumptions/weaker rows, not the FOURTEEN stated at coverage.yaml:10-11. W3: the narrower-result subtotal is wrong.
- SCOPE-AND-NOT-IN-LEAN: FAIL: The L8 discharges and remaining occupation/moment limitations at ledger:198-241,7352-7397 agree with the checked wrappers. However, W2 applies to the Scope's 'stated in full' claim at :192-197. The Not-in-Lean exclusion of the smoothed-covariance spectral identity at :7411-7414 further contradicts the coverage sentence claiming spatial Gaussian smoothing proved. The complete remaining changed-passage audit was not finished.

Findings, fatal (0):

Findings, major (3):
- W1 — L:damped-homogeneous-norms scope overstates spatial covariance smoothing. Coverage.yaml:165 and docs/coverage-scope-tex.yaml:14-15 say 'Everything is proved ... except one remark' and 'spatial Gaussian smoothing ... [is] proved in every dimension'. TeX notes_stratonovich_ham_second_moment.tex:845-846 says actual spatial Gaussian smoothing gives a multiplier. The cited Lean source instead states 'The spectral identity for spatial covariance smoothing p_epsilon * Gamma is not stated (only the membership of its multiplier)' at DampedMultiplier.lean:458-459; the same limitation remains in ledger:1391-1395,7411-7414. Exact fix: retain same-assumptions/weaker, but revise both scope versions to distinguish proved Gaussian multiplier membership from the unformalized covariance-smoothing identification, alongside the dimension-one Green-norm identification limitation.
- W2 — Unqualified full-lemma cross-references are inaccurate. Ledger:192-197 says L:damped-homogeneous-norms is 'stated in full'; :6986-6988 says 'The full lemma'; :1535-1540,1597-1601 broadly claim its smoothing remarks are proved. TeX notes_stratonovich_ham_second_moment.tex:845-847 has no dimension-one restriction. Lean DampedMultiplier.lean:515-527 requires 'hF : GreenFourier G' for the relevant norm identification, discharged only in dimension one at :594-606; the full_wave type at :547-585 does not supply it in dimensions two and three. Exact fix: replace those full/complete-smoothing assertions with explicit references to the proved spectral conclusions and the two remaining smoothing-identification limitations.
- W3 — The narrower-result subtotal is incorrect. Coverage.yaml:10-11 says 'fourteen with a narrower conclusion', but a structural count of its rows gives fifteen same-assumptions/weaker results, including L:positive-raw-embedding at :428-431 and T:intrinsic-occupation-ceiling at :1359-1362. The TeX/Lean comparison independently confirms that the latter's C_occ ceiling, TeX integrated_occupation_ceiling.tex:209-215, is replaced by K_0 R_sp in L8Completed.lean:128-155. Exact fix: change the subtotal to fifteen, consistently describing 28 full and 15 narrower same-assumptions results.

Findings, minor (1):
- W4 — Misnamed dropped hypothesis in the terminal-Wick composition row. Ledger:2812 calls hK 'the covariance formula'. Lean TerminalWick.lean:618 actually has 'hK : Measurable ... K ...'; covariance identification remains in the centered-Gaussian-field hypothesis at L8Completed.lean:316, matching the field-with-covariance assumption in TeX notes_stratonovich_ham_second_moment.tex:3601-3603. Suggested wording fix: replace 'the covariance formula hK' with 'measurability of the covariance hK'.

Required repairs (3):
- Correct the L:damped-homogeneous-norms conclusion_scope in lean/coverage.yaml and both corresponding versions in docs/coverage-scope-tex.yaml to disclose the spatial covariance-smoothing identification gap as well as the dimension-one-only Green-norm identification.
- Qualify the ledger's full-lemma and complete-smoothing cross-references in Scope, DampedNormsHomog and WaveGreen so they do not claim the unformalized smoothing identifications.
- Correct the coverage summary's narrower-result subtotal from fourteen to fifteen.

Limitations (8):
- Complete-reading requirement A was not met. Consequently this is not an acceptance report; the overall verdict is INCONCLUSIVE despite established mandatory documentation repairs.
- The complete Index-by-label section, several required changed ledger sections, most of diffs/statement-ledger-earlier-sections.diff, diffs/statement-ledger.diff, and excerpts/tex-excerpts.txt were not completely read. Their gaps are recorded in source_coverage.
- The prior files were not independently read. Old/new coverage wording was compared through the supplied complete coverage diffs, not independently reconstructed from those prior files.
- Not every declaration cited by the twelve coverage rows or earlier-wave tables was substantively read. Identifier existence and numerical counts were checked by read-only structural scans; those scans do not establish mathematical correspondence.
- The packet contains Audit.lean commands, not captured elaborated-type output. Types were inspected in source; no build or proof-correctness audit was attempted.
- The RawValueCeiling step-module source is not included in the supplied file index, limiting independent checking of that earlier scalar declaration.
- Provenance metadata was only partially read, and packet hashes were not independently verified.
- No network access, file modification, delegation, installation or publication was performed. This AI review is neither human verification nor a novelty audit.

## g5b-symplectic

Driver log:
```
2026-11-12T13:55:59Z start attempt-01
2026-11-12T14:03:13Z attempt-01 exit=0 Status: review-complete
2026-11-12T14:03:13Z done
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
Check verdicts: PASS 61, PASS_WITH_NOTES 5 (of 66)

Findings, fatal (0):

Findings, major (0):

Findings, minor (4):
- W1 — LeftYoungSumsConverge terminology: candidate/statement-ledger.md:5657-5661,5743 and lean/coverage.yaml:623-624 call the indexing objects 'partitions'. SymplecticFree.lean:545-547 requires only an existential nontrivial filter and eventual 'p j ∈ Set.Icc s t'; it requires neither ordered nodes, prescribed endpoints nor shrinking mesh. In contrast, integrated_symplectic_phase.tex:94-98 uses genuine left Young sums converging to U_X(t,s)-I. This is a harmless weakening for the compactness deduction, and the ledger already says U is an arbitrary family with the supplied property. Optional clarification: call these finite node lists and explicitly note that the condition does not characterize Young evolution.
- W2 — Not in Lean parenthetical scope: candidate/statement-ledger.md:7345-7348 groups 'the free wave group', 'the operator J_E' and 'the preservation of omega' before '(supplied ... as FreeWaveData)'. SymplecticFree.lean:522-535 supplies only group, reversal and translation properties, whereas integrated_symplectic_phase.tex:32-40,63-84 additionally constructs J_E and proves preservation. The detailed ledger section at 5682-5689 correctly distinguishes them. Optional clarification: attach the supplied-input parenthetical only to the group/reversal/translation properties, and state separately that J_E and preservation are neither proved nor assumed.
- W3 — Unused-hypothesis prose: candidate/statement-ledger.md:5669-5671 says 'T > 0 ... in both baseline wrappers'. SymplecticFree.lean:661 has '_hT : 0 < T', but the product wrapper at 681-689 has B and lengths in [0,B], with no T>0 argument; integrated_symplectic_phase.tex:43-51 likewise distinguishes [0,T] and [0,B]. Optional clarification: attribute T>0 only to the single-path wrapper.
- W4 — Generic matrix zero-value wording: candidate/statement-ledger.md:5706 says the value at k=0 is the TeX's matrix at zero. SymplecticFree.lean:187 gives '[[1, br*t],[0,1]]', while integrated_symplectic_phase.tex:78 gives '[[1,t],[0,1]]'. The ledger immediately states the general formula at 5710 and physical specialization at 5711, so the intended reading is clear. Optional clarification: add 'after setting br=<0>=1' to the generic definition row.

Required repairs (0):

Limitations (5):
- All reading required by requirement A was completed. Whole-file portions marked partial are outside the requested sections or declarations and were not reviewed; earlier-wave correspondence was not re-audited.
- The audit file contains #check/#print directives, not captured elaboration output. No compilation was run; proof correctness and successful compilation were accepted as stipulated.
- Provenance metadata was read, but file hashes were not independently recomputed and historical revisions were not accessed.
- The non-vacuity witness establishes consistency of the supplied fields, not their realization by the manuscript's physical free wave group. At d=0 the cocompact filter is trivial; the baseline applications require d≥1.
- This AI correspondence review is not human verification or a novelty audit.

## g6a-l8completed

Driver log:
```
2026-11-12T13:55:59Z start attempt-01
2026-11-12T14:04:34Z attempt-01 exit=2 Status: review-complete
2026-11-12T14:04:34Z done
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
Check verdicts: PASS 20, PASS_WITH_NOTES 2, FAIL 5 (of 27)

Checks not PASS/PASS_WITH_NOTES:
- COVERAGE-ROWS: FAIL: The occupation, bracket and score classifications correctly reflect the completed wrappers; the symplectic and uniform-tail rows retain supplied inputs honestly. Every listed claim id exists in claims.yaml. However, the damped-norm conclusion_scope at coverage.yaml:165 overstates spatial covariance smoothing: only multiplier membership is proved, not its identification with smoothing the covariance. See W1.
- CROSS-REFERENCES: FAIL: Cross-references to the three discharged inputs and the retained S2pos/integral-form limitations are consistent. The global statement at ledger:192-197 that damped-homogeneous-norms is 'stated in full' is not consistent with the actual unproved smoothing identifications, despite qualifications elsewhere. See W1.
- CLASS-DAMPED-NORMS: FAIL: same-assumptions/weaker, rather than full, is correct, and the d = 2,3 Green-Fourier gap is real: DampedMultiplier.lean:515-527 requires GreenFourier, discharged unconditionally only in dimension one at :594-606. But coverage.yaml:165 does not state the entire gap exactly. TeX main file:845-846 also identifies spatial covariance smoothing with a multiplier; DampedMultiplier.lean:71-76,458-459 expressly says that spectral identity is not stated. Membership of exp(-eta|xi|^2) alone does not establish it. See W1.
- LEDGER-TOTALS: FAIL: The per-module tables contain exactly 2108 unique declarations: 1747 theorems and 361 definitions, with one row per claims.yaml declaration, 1122 labelled and 986 no-direct-label rows. The coverage rows give 43 same-assumptions results, five inputs-supplied/full results, twenty inputs-supplied/weaker results and three outside results. However, fifteen—not fourteen—of the 43 same-assumptions rows have conclusion: weaker. The summary at coverage.yaml:10 is incorrect. See W2.
- SCOPE-AND-NOT-IN-LEAN: FAIL: The updated S1Bdd, SpaceTimeCS and OccupationCeilingK0 discharge descriptions, remaining supplied inputs, variational/moment distinction and new Not-in-Lean exclusions are accurate. The wave-L8 Scope assertion 'stated in full' for damped norms at ledger:192-197 is an overclaim; the Not-in-Lean passage at :7407-7414 itself acknowledges the missing covariance-smoothing spectral identity. See W1.

Findings, fatal (0):

Findings, major (2):
- W1 — CLASS-DAMPED-NORMS / coverage scope and ledger cross-references. coverage.yaml:165 and docs/coverage-scope-tex.yaml:14-15 say 'Everything is proved ... except one remark' and 'spatial Gaussian smoothing ... [is] proved in every dimension'; ledger:192-197 says the lemma is 'stated in full'. TeX notes_stratonovich_ham_second_moment.tex:845-846 says 'Spatial Gaussian smoothing and Gaussian smoothing of the Green kernel give multipliers in this class.' Lean DampedMultiplier.lean:223-228 proves only 'IsMultiplier (gaussMult ... eta)', while :71-76 and :458-459 explicitly acknowledge that the spectral identity for p_eps * Gamma is not stated. Separately, :515-527 needs GreenFourier for the Green-norm identification, discharged only in d = 1 at :594-606. Fix the coverage ASCII/TeX scope to disclose both gaps, and remove or qualify the ledger's full-coverage assertions. Retain same-assumptions/weaker; no change to Lean is necessary if these omissions are accurately reported.
- W2 — LEDGER-TOTALS / coverage summary. lean/coverage.yaml:10 says 'fourteen with a narrower conclusion', but its rows contain fifteen same-assumptions/weaker entries, including L:damped-homogeneous-norms at :163-165 and T:intrinsic-occupation-ceiling at :1360-1362. This is a metadata count, not a Lean-versus-TeX hypothesis issue. Change fourteen to fifteen. The 2108/1747/361 declaration totals, 1122/986 label split and other classification counts are correct.

Findings, minor (1):
- W3 — L8Completed uniform-tail row. candidate/statement-ledger.md:2812 calls hK 'the covariance formula'. Lean TerminalWick.lean:618 instead states 'hK : Measurable fun q ... => K q.1 q.2'; the covariance relationship remains in CenteredGaussianField, retained by L8Completed.lean:316. TeX notes_stratonovich_ham_second_moment.tex:3601-3604 assumes a centered Gaussian field with covariance K and cell-wise mean-square continuity. Optional wording fix: replace 'the covariance formula hK' with 'measurability of the covariance K (hK)'. The theorem and the rest of the row already retain the covariance relationship correctly.

Required repairs (3):
- Correct the damped-norm conclusion_scope in lean/coverage.yaml and both matching versions in docs/coverage-scope-tex.yaml: disclose that spatial covariance smoothing is represented only by Gaussian multiplier membership, without the covariance-smoothing spectral identity, as well as the d = 2,3 Green-Fourier identification gap.
- Qualify the ledger's damped-norm full-coverage assertions, particularly candidate/statement-ledger.md:192-197 and :1323-1326, consistently with those omissions and the same-assumptions/weaker classification.
- Change the narrower-conclusion count in lean/coverage.yaml:10 from fourteen to fifteen.

Limitations (4):
- This is an AI correspondence review, not human verification, a novelty audit or an independent certification of Lean proof correctness. Compilation and standard-axiom status were accepted as stipulated; no build was run.
- Requirement A's target module, audit, seventeen claim entries, specified ledger sections, coverage rows, scope entries, complete excerpts and cited authoritative manuscript ranges were read completely. Partial supporting files are identified in source_coverage; their unlisted ranges were not semantically reviewed.
- PROVENANCE.json beyond the confirmed initial range, manuscript-anchor.json beyond line 55, most historical files and most diff content were not exhaustively read or byte-verified. No independent packet-integrity or historical-revision audit is claimed.
- Complete manuscript scans outside the substantive ranges were label-token searches only. Complete ledger/claims/coverage scans used for totals checked structure, identifiers and classifications, not the mathematics of previously reviewed waves.

## g6b-changed-rows

Driver log:
```
2026-11-12T13:55:59Z start attempt-01
2026-11-12T14:03:04Z attempt-01 exit=2 Status: review-complete
2026-11-12T14:03:04Z done
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
Check verdicts: PASS 10, PARTIAL 1 (of 11)

Checks not PASS/PASS_WITH_NOTES:
- CHANGED-ROW L:damped-homogeneous-norms: PARTIAL: The new lower bounds, multiplier comparison and smoothed N_0 identity are supported by DampedMultiplier.lean:146-189,262-289,547-585. However, coverage.yaml:165 and docs/coverage-scope-tex.yaml:14-15 overstate spatial covariance smoothing: the proved conclusion is only IsMultiplier(gaussMult eta), not identification of the spectral measure of the smoothed covariance. See W1.

Findings, fatal (0):

Findings, major (1):
- W1 — L:damped-homogeneous-norms: the new scope sentence says 'Everything is proved ... except one remark' and 'spatial Gaussian smoothing ... [is] proved in every dimension' (lean/coverage.yaml:165; docs/coverage-scope-tex.yaml:14-15). TeX asserts that 'Spatial Gaussian smoothing ... give[s] multipliers in this class' (manuscript/notes/notes_stratonovich_ham_second_moment.tex:845-846). Lean proves only 'IsMultiplier (gaussMult ... eta)' (lean/StratonovichHAMSecondMoment/DampedMultiplier.lean:223-228,573), without identifying the spectral measure of p_epsilon * Gamma; that omission is expressly acknowledged at DampedMultiplier.lean:458-459 and candidate/statement-ledger.md:1390-1395. Membership of a proposed multiplier does not establish its connection to covariance smoothing. Fix the coverage conclusion_scope and both ASCII/TeX scope sentences to disclose this additional omission, retaining the separate dimension-one limitation for the Green Fourier identification.

Findings, minor (0):

Required repairs (1):
- Correct lean/coverage.yaml:165 and docs/coverage-scope-tex.yaml:14-15: state that Gaussian multiplier membership is proved in every dimension but the spectral identification for spatial covariance smoothing is not formalized; retain the disclosed dimension-one Green identification and the proved N_0 mass identity.

Limitations (4):
- Requirement A was completed for all eleven checks. Partial-file entries contain the required rows, declarations or manuscript statements; unrelated earlier-wave content and unlisted helper proofs were not exhaustively reviewed.
- PROVENANCE.json was inspected only at lines 1-40; lines 41-1675 and packet-wide byte bindings were not independently checked.
- The audit file contains #check/#print commands, not captured elaborator output. Compilation and proof correctness were accepted as stipulated; no build was run.
- This AI correspondence review is neither human verification nor a novelty audit.

## g6c-changed-passages

Driver log:
```
2026-11-12T13:55:59Z start attempt-01
2026-11-12T14:03:53Z attempt-01 exit=2 Status: review-complete
2026-11-12T14:03:53Z done
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
Check verdicts: PASS 9, PARTIAL 2 (of 11)

Checks not PASS/PASS_WITH_NOTES:
- CHANGED-PASSAGE DampedNormsHomog (whole result): PARTIAL: The new lower bounds and mass-preservation references are correct, but candidate:1535-1540 and 1597-1599 overstate completion of the smoothing remarks. DampedMultiplier.lean:223-228 proves only membership of an explicitly defined Gaussian multiplier, not the spectral identity for smoothing Gamma. TeX main:845-847 asserts that actual spatial and Green smoothing give such multipliers. The associated coverage scope explicitly overclaims spatial smoothing; see W1.
- CHANGED-PASSAGE WaveGreen (whole result): PARTIAL: The dimension-one identification and higher-dimensional gap are correctly described, but candidate:6986-6988 then calls full_wave the 'full lemma'. DampedMultiplier.lean:515-518 requires the additional hypothesis 'hF : GreenFourier G' for identification with the smoothed wave norm; 594-606 discharges it only in dimension one. TeX main:805 and 845-847 assert the smoothing conclusion under H:homog. The unqualified completion claim needs narrowing; see W1.

Findings, fatal (0):

Findings, major (1):
- W1 — DampedNormsHomog/WaveGreen smoothing scope is materially overstated. Candidate/statement-ledger.md:1535-1540,1597-1599 says the smoothing remarks are proved, and 6986-6988 calls full_wave the 'full lemma'. lean/coverage.yaml:165 and docs/coverage-scope-tex.yaml:14-15 additionally say 'spatial Gaussian smoothing ... [is] proved in every dimension'. Lean DampedMultiplier.lean:223-228 concludes only 'IsMultiplier (gaussMult eta)'; it does not identify the spectral measure of p_eps * Gamma. For Green smoothing, the identification theorem explicitly assumes '(hF : GreenFourier G)' at 515-518, discharged only for d=1 at 594-606. TeX manuscript/notes/notes_stratonovich_ham_second_moment.tex:845-847 says 'Spatial Gaussian smoothing and Gaussian smoothing of the Green kernel give multipliers in this class' under H:homog at 805. Mere multiplier membership does not establish correspondence with the smoothed covariance, and the abstract transform identity does not supply the missing higher-dimensional wave identification. The narrower disclosures at candidate:1391-1399 and coverage:207-209 do not make the contradictory completion sentences accurate. Exact fix: narrow these ledger and coverage sentences to the proved multiplier-membership, mass and abstract-transform results; explicitly exclude the covariance-smoothing spectral identity and restrict the smoothed-wave identification to d=1 or supplied GreenFourier. Retain conclusion: weaker.

Findings, minor (0):

Required repairs (1):
- Correct the smoothing-completion claims in candidate/statement-ledger.md:1535-1540,1597-1599,6986-6988 and the L:damped-homogeneous-norms scope sentences in lean/coverage.yaml:165 and docs/coverage-scope-tex.yaml:14-15 as specified in W1. Do not describe the full manuscript lemma as completed unless the missing identifications are supplied by Lean conclusions.

Limitations (4):
- Requirement A was completed for the eleven scoped checks. Unlisted portions of files marked partial were not read; contextual metadata, prior files and coverage documents were sampled under requirement B.
- Unchanged earlier-wave assertions and new wave-L8 sections were not independently audited beyond the context needed for these checks.
- Compilation and standard-axiom correctness were accepted as stipulated; no Lean build or independent byte-hash verification was performed.
- This is an AI correspondence review, not human verification or a novelty audit.

