# Wave L8 confirmation reviews: summary

Companion bd1c439 (wave-l8/repair; reviewed commit 3518233), manuscript a284420; reviewer Codex gpt-6.1-sol, effort high, min-confidence high.

Packets: c1 (damped smoothing scope, R_0 controls, R_alpha attribution, narrower count: g1, g6a W1-W2, g6b, g6c), c2 (TerminalWick hK, FiniteWick integrability, mixed-moment scope, refutation lists: g4, g6a W3), c3 (minor findings of g2, g3, g5b). Built by build-l8-confirm.py from the detached worktree l8rev-conf/src at bd1c439.

## c1-damped-spectral-counts

Driver log:
```
2026-11-12T14:18:28Z start attempt-01
2026-11-12T14:27:26Z attempt-01 exit=2 Status: review-complete
2026-11-12T14:27:26Z done
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
Check verdicts: PASS 5, PASS_WITH_NOTES 4, FAIL 1 (of 10)

Checks not PASS/PASS_WITH_NOTES:
- NO-REGRESSION: FAIL: The edited Scope sentence still asserts integrability for each real-valued integral conclusion at candidate/statement-ledger.md:291-297, contradicting the correctly repaired totalized-F bridge description at :1927-1931 and FiniteWick.lean:578-591; see C1. The three Lean-file changes are comment-only by direct comparison. The inspected scope copies agree, contain no Lean declaration names or TeX line locators, and preserve the square-root Rayleigh-rate interpretation. C2 and C3 are additional minor wording points.

Findings, fatal (0):

Findings, major (1):
- C1 — NO-REGRESSION / Scope integrability guarantee. The edited sentence at candidate/statement-ledger.md:291-297 still says 'integrability is part of each real-valued integral conclusion'. Lean FiniteWick.lean:578-580 instead assumes only '(hF : Continuous F)' and concludes equality of two integrals, without asserting integrability; :586-591 gives a separate integrability equivalence. The newly repaired ledger itself correctly recognizes this exception at :1927-1931. TeX manuscript/notes/notes_stratonovich_ham_second_moment.tex:3657-3660 establishes 'Bochner integrability' for the actual Gaussian products, not arbitrary continuous F. Thus the global guarantee remains materially broader than the declarations. Exact fix: restrict the Scope guarantee to the manuscript integral assertions whose finiteness is formalized, and explicitly except totalized auxiliary identities, including the continuous-F Gaussian bridge.

Findings, minor (2):
- C2 — TerminalWick module-header wording. lean/StratonovichHAMSecondMoment/TerminalWick.lean:31-32 groups both wrappers under 'hypotheses plus the added restriction hK', although terminal_wick_mono_paper at :667-683 has no hK parameter; only terminal_wick_paper at :624 has it. TeX manuscript/notes/notes_stratonovich_ham_second_moment.tex:3601-3605 assumes bounded variance and cell-wise mean-square continuity, while :3640-3642 states comparison without global covariance measurability. Optional exact clarification: say that only terminal_wick_paper adds hK. The detailed ledger already distinguishes the wrappers correctly at :5950-5951.
- C3 — WaveGreen closing attribution. candidate/statement-ledger.md:7076-7080 places 'the smoothed Green norm identified ... only in d = 1' inside a sentence ending with full_wave. Lean DampedMultiplier.lean:582-585 concludes only an N2GreenSq-to-N2GreenSq identity; the N2onSq identification is at :594-606 in fourier_one. TeX manuscript/notes/notes_stratonovich_ham_second_moment.tex:845-847 contains the broader smoothing remark. Optional exact clarification: attribute the narrowed bundle to full_wave and the additional dimension-one identification separately to fourier_one. The preceding sentence and DampedMultiplier section already explain this distinction.

Required repairs (1):
- Qualify candidate/statement-ledger.md:291-297 so its global integrability guarantee explicitly excludes totalized auxiliary integral identities, consistently with the repaired FiniteWick description.

Limitations (4):
- Complete-reading requirement A was satisfied. Files marked partial have unreviewed portions outside the recorded ranges; no packet-wide mathematical audit is claimed.
- The packet omits the unrelated refutation sources newly inventoried for FiniteWick, OccupationCeilingFinite, SpaceTimePositivity and TerminalWick. Their mathematical descriptions were compared with included package statements, but their exact file-level implementations could not be confirmed.
- No build, external-source consultation, historical review certification or packet-wide hash verification was performed. Direct comparisons confirmed that the supplied changed Lean files differ only in comments.
- This is an AI correspondence review, not human verification, proof-correctness certification or a novelty audit.

## c2-wick

Driver log:
```
2026-11-12T14:18:28Z start attempt-01
2026-11-12T14:25:27Z attempt-01 exit=2 Status: review-complete
2026-11-12T14:25:27Z done
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
Check verdicts: PASS_WITH_NOTES 3, PASS 3, FAIL 1 (of 7)

Checks not PASS/PASS_WITH_NOTES:
- NO-REGRESSION: FAIL: The changed smoothing scopes correctly disclose both gaps (DampedMultiplier.lean:71-76,515-527,594-606 versus manuscript notes_stratonovich_ham_second_moment.tex:845-847). The numerical convention corrections, Cauchy hypotheses, node-list abstraction and Not-in-Lean clarification are supported. All Lean changes in diffs/repair-3518233-bd1c439.diff:35-83,603-645 are confined to comments. However, the contract's universal ASCII/TeX mirroring requirement is not satisfied: lean/coverage.yaml contains 35 conclusion_scope fields, while docs/coverage-scope-tex.yaml:7-69 provides only 21 matching entries. Fourteen scopes have no ASCII/TeX counterpart; see C1. This omission predates the repair but still fails the explicitly requested universal check.

Findings, fatal (0):

Findings, major (1):
- C1 — NO-REGRESSION scope-mirror completeness. Fourteen conclusion_scope fields lack entries in docs/coverage-scope-tex.yaml:1-69: L:driver-holder-limit, L:driver-interval-limit, L:exact-canonical-scaling, L:finite-word-cutoff, L:higher-riesz, L:raw-block-inputs, L:raw-block-restart, P:actual-wave-form, P:gram-entrywise-comparison, P:gram-positive-optimizer, P:masked-noise-completion, P:raw-block-original-lower, P:wave-two-variances and P:white-spatial-energy. For example, lean/coverage.yaml:307-309 says 'Lean checks only the facts about the wave Green measures'; the corresponding Lean fact is 'waveGreen d s univ = ENNReal.ofReal s' at lean/StratonovichHAMSecondMoment/WaveGreen.lean:250-251, and the TeX says 'mass h and satisfy G_h(hA) = hG_1(A)' at manuscript/notes/notes_stratonovich_ham_second_moment.tex:5186-5187. The mathematical limitation is disclosed, but its required mirror is absent. This is pre-existing metadata incompleteness, not a newly introduced mathematical regression. Fix: add entries for all fourteen labels, each with ASCII equal to its conclusion_scope and equivalent TeX.

Findings, minor (2):
- C2 — FiniteWick integrability packaging. candidate/statement-ledger.md:1924-1926 says every Gaussian-monomial identity includes integrability 'as a conjunct'. Yet lean/StratonovichHAMSecondMoment/FiniteWick.lean:513-515 states wick_stdPi as an equality alone; integrability is separately proved at :493-496. The substantive assurance is correct, and the TeX's application concerns monomials ('the m+n Gaussian variables at their labelled vertices', manuscript/notes/notes_stratonovich_ham_second_moment.tex:3663). Optional exact wording improvement: replace 'as a conjunct' with 'either as a conjunct or in a separate theorem'.
- C3 — TerminalWick module-comment scope. lean/StratonovichHAMSecondMoment/TerminalWick.lean:31-32 collectively describes both wrappers as having 'the added restriction hK', although :667-683 shows terminal_wick_mono_paper takes no hK; the ledger correctly states this at candidate/statement-ledger.md:5949-5951. The TeX's comparison sentence at manuscript/notes/notes_stratonovich_ham_second_moment.tex:3641-3642 likewise adds no global measurability hypothesis. Optional exact clarification: say 'terminal_wick_paper additionally requires hK; both wrappers retain the supplied inputs below'.

Required repairs (1):
- Complete docs/coverage-scope-tex.yaml for the fourteen labels listed in C1, with an ASCII mirror equal to each lean/coverage.yaml conclusion_scope and a mathematically equivalent TeX version.

Limitations (4):
- Requirement A was completed. Unlisted portions of supporting files were not semantically reviewed.
- The blocking finding concerns the contract's requirement to mirror every conclusion_scope; the fourteen omissions also occur in the prior scope file and are not regressions introduced by this repair.
- Occupation-ceiling and space-time-positivity refutation files named by added prose are not supplied as standalone files. Their range distinctions were checked against the available general declarations and elementary mathematical witnesses, not against those omitted artifacts.
- No compilation, proof-correctness certification, provenance hash reproduction, historical build verification, human verification or novelty audit was performed.

## c3-minors

Driver log:
```
2026-11-12T14:18:28Z start attempt-01
2026-11-12T14:27:42Z attempt-01 exit=2 Status: review-complete
2026-11-12T14:27:42Z done
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
Check verdicts: PASS 9, FAIL 1 (of 10)

Checks not PASS/PASS_WITH_NOTES:
- NO-REGRESSION: FAIL: The changed Scope passage still promises integrability for 'each real-valued integral conclusion' at ledger:295-297, although FiniteWick.lean:578-580 and SymplecticFree.lean:300-307 include totalized integral identities without integrability guarantees (C1). Otherwise the inspected smoothing and constant repairs agree with DampedMultiplier.lean:434-608 and SpectralMassIdentity.lean:77-81,228-285; the count is 28 same/full, 15 same/weaker, 5 supplied/full, 20 supplied/weaker and 3 outside. The required and changed scope/ASCII/TeX sentences agree. All Lean hunks in the complete diff are comment-only; direct TerminalWick comparison confirms this. Its new plural-wrapper parenthetical has the optional wording issue C2.

Findings, fatal (0):

Findings, major (1):
- C1 — Scope integrability guarantee remains materially overbroad. candidate/statement-ledger.md:295-297 says 'integrability is part of each real-valued integral conclusion'. But lean/StratonovichHAMSecondMoment/FiniteWick.lean:578-580 assumes only 'hF : Continuous F' and concludes equality of two integrals, not their integrability; its separate integrability equivalence is at :586-589. Likewise SymplecticFree.lean:300-307 proves the integral cancellation for arbitrary functions, while the manuscript explicitly calls its L2 application an 'absolutely integrable cancellation' at manuscript/notes/integrated_symplectic_phase.tex:88-90. The detailed ledger exceptions at :1926-1931 and :5798 are accurate but contradict the blanket Scope guarantee. Exact fix: replace the guarantee with 'Integrability is proved where explicitly stated; totalized integral identities and auxiliary bounds do not themselves guarantee integrability.'

Findings, minor (1):
- C2 — TerminalWick comment parenthetical has ambiguous distributive scope. lean/StratonovichHAMSecondMoment/TerminalWick.lean:31-32 groups both wrappers before 'hypotheses plus the added restriction hK'. Only terminal_wick_paper has hK (:616-624); terminal_wick_mono_paper's complete inputs at :667-679 do not. The TeX comparison says 'entrywise comparison ... compares all finite partial-order second moments' without this restriction (manuscript/notes/notes_stratonovich_ham_second_moment.tex:3640-3642). The ledger correctly distinguishes the wrappers at :5950-5951 and :6044. Optional exact clarification: 'Both wrappers use the supplied inputs below; terminal_wick_paper additionally requires hK, whereas terminal_wick_mono_paper does not.'

Required repairs (1):
- Narrow or remove the universal integrability guarantee in candidate/statement-ledger.md:295-297 as specified in C1. Do not imply that totalized integral identities certify integrability.

Limitations (5):
- Requirement A was completed. Files marked partial contain contextual or unrelated material outside the required ranges that was not independently reviewed.
- This is an AI correspondence review, not human verification or a novelty audit. No compilation, proof-correctness audit, network access or file modification was performed.
- Provenance revisions were inspected, but packet hashes were not independently recomputed.
- The two current spectral-mass refutation files are represented by their complete repair hunks and supplied prior versions, rather than standalone current files. Unchanged finite-wick and terminal-wick refutation scripts are not supplied; their added numerical summaries were assessed against the displayed formulas, not by inspecting those scripts.
- The FAIL concerns the residual Scope guarantee, not the validity of the eight specifically repaired findings or the Lean proofs.

