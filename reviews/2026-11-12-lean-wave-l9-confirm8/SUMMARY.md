# Wave L9 re-review round 8 (label assignments, pointer Index): summary

Companion 06ee849 (wave-l9/repair; every label in a label cell is an assignment, context labels moved, Index regenerated, docs only; reviewed commit 434a7e2), manuscript a284420; reviewer Codex gpt-6.1-sol, effort high, min-confidence high, --source-revision 06ee849. Packets built by scratchpad/build-l9-reconfirm8.py. Checkers at 06ee849: index_category_check.py: Index rows: 186; labels: 185; manuscript labels at a284420: 879; problems: 0; index_check_pointer.py: 0 pairs without a table row, bad []. Every finding below is verbatim from report.json.

Packets: q1a the 15 kept or new label assignments (ASSIGN) and the 7 other changed rows; q1b the 12 rows with labels moved to (Context: ...) and the 33 cleared no-direct-label cells; q2 the 186-row pointer Index and the Scope/FORMALIZATION rule text; q3 no new overclaim over 434a7e2..06ee849 and over lines 241-854 of the a723987..434a7e2 diff. Retry only on tool failure, recorded in the driver log.

## q1a-assignments

Preflight: contract-check CONTRACT-OBSERVABLE (14 required field(s), 0 dispatch input(s); no provider call); dry run exit 0 (dryrun/); contract-check with --dispatch-input dryrun/prompt.txt CONTRACT-OBSERVABLE (14 required field(s), 1 dispatch input(s); no provider call)

Driver log:
```
2026-11-12T19:58:10Z start attempt-01
2026-11-12T20:05:33Z attempt-01 exit=0 Status: review-complete
2026-11-12T20:05:33Z done
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
Check verdicts: PASS 21, PASS_WITH_NOTES 1 (of 22)

Findings, fatal (0):

Findings, major (0):

Findings, minor (1):
- P1 — CHANGED line 3016: the optional parenthetical described as Lean reads `K.Cg * exp(-(K.ηg t))` at candidate/statement-ledger.md:3016. The actual expression is `K.Cg * Real.exp (-(K.ηg * t))` at lean/StratonovichHAMSecondMoment/IndexedCone.lean:337; the manuscript states `C_{\mathrm{gap}}e^{-\eta_{\mathrm{gap}}t}` at manuscript/notes/integrated_raw_block_lower.tex:256. Replace that parenthetical expression with the actual Lean expression. The surrounding mathematical formula is already correct, so this is nonblocking typography.

Required repairs (0):

Limitations (5):
- All passages required by requirement A were read completely, including section/table headers, complete declaration statements and authoritative manuscript statements or proof passages. Partial-file coverage denotes material outside those required passages; those remaining ranges were not reviewed.
- The conclusions concern exactly the 22 requested documentation-correspondence checks, not a global certification of every ledger assignment.
- Checker source and recorded outputs were inspected, not executed; syntactic checker success was not treated as semantic evidence.
- No Lean build, proof-correctness audit or independent provenance-hash verification was performed.
- This AI review is neither human verification nor a novelty audit.

## q1b-context-cleared

Preflight: contract-check CONTRACT-OBSERVABLE (14 required field(s), 0 dispatch input(s); no provider call); dry run exit 0 (dryrun/); contract-check with --dispatch-input dryrun/prompt.txt CONTRACT-OBSERVABLE (14 required field(s), 1 dispatch input(s); no provider call)

Driver log:
```
2026-11-12T19:58:10Z start attempt-01
2026-11-12T20:02:10Z attempt-01 exit=0 Status: review-complete
2026-11-12T20:02:10Z done
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
Check verdicts: PASS 45 (of 45)

Findings, fatal (0):

Findings, major (0):

Findings, minor (0):

Required repairs (0):

Limitations (4):
- The review covers exactly the 45 requested documentation-correspondence checks, not every declaration or Index pointer in the packet.
- Files marked partial were read selectively; all reading units required by contract A were completed. Unlisted portions of those files were not systematically reviewed.
- Proof correctness, Lean compilation, provenance hashes and historical manuscript versions were not independently audited. Checker outputs and adjudication conclusions were not used as substitutes for source comparison.
- This AI review is neither human verification nor a novelty audit.

## q2-pointer-index

Preflight: contract-check CONTRACT-OBSERVABLE (14 required field(s), 0 dispatch input(s); no provider call); dry run exit 0 (dryrun/); contract-check with --dispatch-input dryrun/prompt.txt CONTRACT-OBSERVABLE (14 required field(s), 1 dispatch input(s); no provider call)

Driver log:
```
2026-11-12T19:58:10Z start attempt-01
2026-11-12T20:00:55Z attempt-01 exit=2 Status: review-complete
2026-11-12T20:00:55Z done
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
Check verdicts: PASS 2, FAIL 1 (of 3)

Checks not PASS/PASS_WITH_NOTES:
- SCOPE-AND-FORMALIZATION: FAIL: The audit-category exception is correct: candidate/statement-ledger.md:77-78 and lean/FORMALIZATION.md:110-113 exclude HermiteWordFock from category C, consistently with its narrower-result heading at candidate/statement-ledger.md:862. However, neither the complete Scope nor the complete FORMALIZATION states the required label-cell assignment/context convention. Candidate/statement-ledger.md:79-84 and lean/FORMALIZATION.md:90-92 describe pointers only generically; candidate/statement-ledger.md:462-467 explains no-direct-label semantically but does not prohibit manuscript labels in those cells. The explicit rule appears in adjudication/round7-434a7e2.md:5,19,21, not in the two required reader-facing descriptions.

Findings, fatal (0):

Findings, major (1):
- P1 — Missing assignment convention in Scope and FORMALIZATION. The Lean-companion Scope says labels point to sections 'whose tables formalize it' (candidate/statement-ledger.md:79-84), while FORMALIZATION says the Index 'points from each label to those sections with their category' (lean/FORMALIZATION.md:90-92). Neither specifies that every backticked manuscript label anywhere in a label cell is an assignment, that context-only labels belong in the statement cell as '(Context: ...)', or that no-direct-label cells contain no manuscript label. This matters for nested co-labels such as 'L:finite-word-cutoff' and 'E:finite-word-cutoff' in candidate/statement-ledger.md:900, corresponding to TeX '\label{L:finite-word-cutoff}' and '\label{E:finite-word-cutoff}' at manuscript/notes/notes_stratonovich_ham_second_moment.tex:2531,2543. Exact fix: add all three convention clauses explicitly to both the ledger Scope and lean/FORMALIZATION.md. This is a documentation-rule omission, not a mathematical statement discrepancy.

Findings, minor (0):

Required repairs (1):
- Add to both candidate/statement-ledger.md Scope and lean/FORMALIZATION.md: every backticked manuscript label anywhere in a section-table label cell is an assignment and creates an Index pointer; context-only label mentions belong in the statement cell as '(Context: ...)'; no-direct-label cells carry no manuscript label.

Limitations (3):
- Requirement A was completed. Outside its required portions, ledger prose and manuscript files were searched selectively rather than read completely; coverage entries identify those partial readings.
- The review checks documentation correspondence only. Lean proof correctness, package builds, provenance hashes, and historical revision equivalence were not verified.
- This AI review is neither human verification nor a novelty audit.

## q3-diffs

Preflight: contract-check CONTRACT-OBSERVABLE (14 required field(s), 0 dispatch input(s); no provider call); dry run exit 0 (dryrun/); contract-check with --dispatch-input dryrun/prompt.txt CONTRACT-OBSERVABLE (14 required field(s), 1 dispatch input(s); no provider call)

Driver log:
```
2026-11-12T19:58:10Z start attempt-01
2026-11-12T20:01:30Z attempt-01 exit=3 Status: review-complete
2026-11-12T20:01:30Z done
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
Check verdicts: PASS 1, INCONCLUSIVE 1 (of 2)

Checks not PASS/PASS_WITH_NOTES:
- NO-NEW-OVERCLAIM-a723987-434a7e2-lines-241-854: INCONCLUSIVE: The entire requested diff range, diffs/docs-a723987-434a7e2.diff:241-854, was read. However, requirement A additionally demands complete reading of every corresponding section-table row for the removed per-declaration Index entries. That correspondence reading remains incomplete, particularly for the extensive declaration groups removed at lines 241-699. Selected retained limitations were verified, including the Fock column inputs at candidate/statement-ledger.md:2325-2334, abstract GroundFamily status at 2918-2975, and M1 at 3439,3474-3478,3487-3491. These samples and pointer-set equality do not establish universal preservation of supplied inputs and narrower scopes.

Findings, fatal (0):

Findings, major (0):

Findings, minor (0):

Required repairs (0):

Limitations (6):
- Complete-reading requirement A was not fully met: most section-table rows corresponding to the removed Index entries in the previous diff were not textually reviewed. The second check and overall acceptance therefore remain INCONCLUSIVE.
- Whole-file structural parsing verifies pointer correspondence, not semantic preservation of every removed qualifier or supplied hypothesis.
- Lean source files and elaborated types are absent from the packet. Selected declaration descriptions were corroborated against claims.yaml; this was not independent verification of Lean types or proofs.
- PROVENANCE.json was read, but its byte bindings were not independently verified.
- No mandatory documentation repair was established; an empty required_repairs list does not constitute acceptance.
- This AI review is neither human verification nor a novelty audit.

