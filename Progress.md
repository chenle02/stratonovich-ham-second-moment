# Progress.md — Article-Stratonovich-HAM-Second-Moment

> **AUTHORITY.** This file is the sole source of truth for the workflow state
> (per `progress-md-authority-paper-dev`). Start every session here. Update it
> at the end of every round, before committing.

## Current state

- **Phase:** Round 2 = Gate G1 complete (2026-10-27), after Le authorized continuation. Main targets remain open; G2 preparatory screens are active and companion creation awaits decision point 4.
- **Proved in this project:** P:Jensen (§2); reviewed G0 P:mixed, L:white-test,
  L:crude-corrected and P:envelope (§3); reviewed G1 P:white-four, L:static-four and P:riesz-small (§4). Intermediate upper exponent rho>kappa; principal goals open.
- **Open targets:** Goal G:upper, Goal G:sharp (see PROJECT-GOAL.md).
- **Blocking human decisions:** decision point 1 passed by Le's explicit reactivation/continuation. Decision point 4 still applies before companion creation; registry/reuse reconnaissance only until that proposal is ready.
- **Worker:** Codex agent #30 (<MACHINE>, `n30-stratonovich-ham-second`), handed over
  2026-10-26; workflow paper-dev + lean-pkg (Lean track: `lean-progress/PROGRESS.md`).

## Round plan

Each round: one bounded question, a frozen claim boundary, a written result
in the notes (or a recorded no-go), a cross-family review for any new proof,
then the round-close protocol (`paper-dev-round-close-protocol`).

| Round | Gate | Question | Exit criterion |
|---|---|---|---|
| 1 | **G0 diagnosis** | (a) Justify 𝔼u² = Σ_{m,n} 𝔼[S_m(g_m)S_n(g_n)] (m+n even) from (2.13), (2.18), (2.21) and Theorem 1.1, and write each term as a two-chain pairing integral in the form of (3.6). (b) Reproduce Remark 5.1's e^{Ct²} from (2.13), (4.4) and locate exactly where the exponent 2 enters instead of κ. (c) Decide whether Theorem 3.1 with Laplace-weighted kernels (Lemma A.1) can give the scale t^κ. | A written section in the notes: the cross-term formula with proof; the diagnosis; a verdict "Theorem 3.1 route viable / not viable" with the counting argument. |
| 2 | **G1 calibration and small cases** | Compute the n = 1, 2 (chaos orders 2 and 4) contributions to 𝔼u² explicitly (d = 1, α = 1 white space first; then Riesz) and compare their growth with t^κ scaling; check the α₀→0 limit against Chen–Hu (2025). | Explicit low-order formulas plus a calibration table in the notes. |
| 3 | **G2 upper bound** | Prove Goal G:upper by the route chosen in G0 (Laplace transform, two-chain bound, scaling, Tauberian/Mittag-Leffler conversion). | Complete proof plus Opus skeptic review, findings adjudicated. |
| 4+ | **G3 sharp constant** | Two-clock analogue of Chen's Theorem 6.1 for two ordered chains, and the matching large deviations (Theorem 7.1 analogue); lower bound beyond Jensen first. | Per sub-goal; record partial results honestly. |

## Decisions log

[held back: collaborators' unpublished work]

## Verified facts (setup reading, 2026-10-26)

- Theorem 1.2 (p. 3) gives two-sided first-moment bounds L_* ≤ liminf ≤
  limsup ≤ L^*, with L(𝓔) as in the notes; 𝓔_* < 𝓔 ((1.11)–(1.13), p. 4).
- Remark 5.1 (p. 37): 𝔼u²(t,x) ≤ e^{Ct²} for large t, "from (2.13) and (4.4)".
- Remark 6.3 (p. 42): single-chain monotone ordering is why the method
  stops at p = 1.
- Theorem 3.1 (p. 15): universal two-chain pairing bound, including
  cross-pairings, over a partition {Q₀,Q₁,Q₂} with #Q₀ = #Q₁, #Q₂ even.
- Theorem 4.1 (4.3) (p. 22): exact two-chain formula for 𝔼[S_n(g_n)]².
- Conjecture (1.22) (p. 6): constant p^{(4−α)/(3−α)} L^* for p = 1, 2, …

## Failed routes / no-gos

- **G0 uniform pairing estimate — NOT VIABLE for G:upper.** With beta=4-alpha-alpha0,
  Theorem 3.1 and exact homogeneous norm scaling give the optimized numerical
  majorant B_K with log B_K(t) of order t^rho, rho=beta/(beta-1)>kappa.
  Its order coefficient has denominator (k!)^(3-alpha-alpha0), losing the
  factor (k!)^alpha0 needed at the target scale. This rules out that specific
  common-theta uniform-per-pairing estimate, not all uses of Theorem 3.1.
  Refined order-retaining/grouped estimates remain unexamined. Do not infer a
  moment lower bound from the lower bound on B_K.
- **Unrestricted use of source (5.4) — invalid uniformity.** The n=1 spatial-
  white-noise test grows as t^(3-alpha0), not O(t²). Restricting the Laplace
  parameter to theta>=theta0 recovers the large-time exponential conclusion.

## Round log

| Round | Date | Outcome | Commit |
|---|---|---|---|
| 0 | 2026-10-26 | Setup: repo, notes scaffold (5 pp, clean build), source manifest, wiki project page | see git log |
| 1 | 2026-10-27 | G0 complete: mixed expansion, corrected crude bound, intermediate rho upper bound and scoped no-go; Opus PASS_WITH_NOTES/high | 4ff2bca60e666482480596cc1e53b9be06750ea7 |
| 2 | 2026-10-27 | G1 complete: all fifteen white order-four terms, exact static11/540, Riesz coefficients/representation; Opus PASS_WITH_NOTES/high | 8358d58c40591922a971790827f10ebe576932e0 |

## Round 1 — Gate G0 (2026-10-27)

### Scope and preflight

Local, origin and <HUB> were clean and aligned at `b11a8d9` before edits.
The author PDF hash matches the manifest. `lean-pkg doctor` exited zero;
Lean remains at L0, with no companion package. The workspace-wide sync
inventory timed out without output; the mandatory focused repository checks
passed. No emails or fleet messages were sent.

### Reviewed findings

- `P:mixed`: full convergent nonnegative mixed-term expectation series,
  including zero chains and all self/cross pairings.
- `L:white-test`: exact white-space total-order-two check. At alpha0=1/2,
  E[X1²]=(8/15)t^(5/2), E[X2]=(4/15)t^(5/2).
- `L:crude-corrected`: recovers exp(Ct²) for large t using
  theta=theta0+n/t, retaining the large-theta restriction in Lemma A.1.
- `P:envelope`: homogeneous upper bound with beta=4-alpha-alpha0 and
  rho=beta/(beta-1), strictly between kappa and 2. The explicit numerical
  majorant has log-growth of order t^rho, so that uniform pairing estimate
  cannot reach G:upper. This is not a no-go for every use of Theorem 3.1.
- The author-version (5.4) cannot have its printed constant uniform in t;
  (4.4), cited by Remark 5.1, is a smoothing limit. The discrepancy does
  not refute the repaired final exp(Ct²) bound or the existence theorem.

### Falsification and honesty

The exact first-order white-space calculation preceded the general estimates.
Finite enumeration checks pairings and every split through total order eight:
pair counts 1,3,15,105 and all-split totals 3,15,105,945. These checks are not
an all-order proof. Worker honesty and source correspondence are retained in
`reviews/2026-10-27-round1/work/worker-report.md`; independent root source
inspection is in `reviews/2026-10-27-round1/root-source-check.md`.

Review-sensitive points: generalized-kernel/white-noise limiting conventions;
source hypotheses for Theorem 3.1; the distinction between a majorant lower
bound and an actual moment lower bound; precise scope of the no-go.
No G:upper/G:sharp proof, novelty claim, or Lean certificate is asserted.

### Review record

Frozen candidate: `reviews/2026-10-27-round1/packet-v1/candidate.tex`,
SHA-256 `feac983bd37b77f3edd1758ee9353b8a4a9d84cfb72871e10f7afbf0ce142a74`.
Native Claude Opus 5.5 high skeptic launched on this packet, with high
acceptance threshold and mandatory source-read coverage. Account selected
from configured subscriptions by `claude-acct best`, with identity recorded
in the doctor and attempt receipts. A retained official Claude 2.1.304
runtime is scoped to this launch because the current 2.1.311 is not supported
by the frozen read-ledger parser. No global runtime/configuration was changed.

**V1 disposition:** native transport completed; actual model Claude Opus 5.5;
PASS_WITH_NOTES / medium; all C1–C8 PASS, no fatal/major findings or required
repairs. Driver exit 3, accepted=false: below the configured high threshold.
The original report is preserved, not upgraded or resumed for confidence.

A substantive successor adds an independently identified proof of individual
unequal-chain diagram limits (independent noise colors, source Lemma 4.4),
clarifies the two-step d=3 regularization, and addresses the report's optional
source/summary points. The root raised the individual-diagram issue before the
first terminal report. Expanded source coverage is supplied for the successor;
this is not a confidence-only retry.

### Stop boundary

Finish the reviewed G0 record and round-close provenance, then stop for Le at
decision point 1 (and the scoped no-go decision point 2). Round 2 and Lean L1
are not authorized to start in this run. Companion creation remains separately
blocked by decision point 4.

### Finding-by-finding adjudication

The v1 report contains nine optional findings, all preserved verbatim.

| V1 finding | Disposition |
|---|---|
| 1. Fixed-time summability relies on disputed (5.4) | Addressed in v2: independent corrected diagonal estimate; explicit noncircular forward reference. |
| 2. Name N1 nonuniformity as well as N2 restriction | Addressed in v2 source-fidelity remark. |
| 3. Generalize the counterexample beyond white noise | Not adopted: the exact nonzero white-noise witness already disproves the printed uniform assertion; no unnecessary extension. |
| 4. Abstract omits genuine intermediate bound | Addressed in v2: rho upper bound and corrected crude derivation stated. |
| 5. Section 2.2 omits finite-measure/truncation hypotheses | Addressed in v2 summary and application; Gaussian domination uses (1.5), no radial-density assumption. |
| 6. Generalized-kernel limit order is compressed | Addressed in v2: eta first at fixed noise smoothing, then noise limit; additionally independent colored-noise proof of individual diagrams. |
| 7. Alpha0-to-zero is only a formal calibration | Addressed in v2: explicitly formal, not distinguishing rho/kappa and not uniform-constant evidence. |
| 8. Display/explain p=1 loss | Addressed in v2: single-chain theta optimization stated. |
| 9. Source typographical defects | Recorded in root source check; not used as mathematical inputs and not silently repaired in the source PDF. |

V2 returned all eight checks PASS, PASS_WITH_NOTES / high, with no required
repairs, but surrounded its JSON with prose. Its original raw report and
invalid-format receipt remain immutable. A same-session format-only continuation
is requested through the native driver. Any outside-JSON qualifications must
remain in the final limitations; this is not another independent review.

| V2 optional finding | Disposition for this G0 checkpoint |
|---|---|
| 1. Specify the smoothing of independent colored copies more explicitly | Retained as optional exposition: the construction uses the source's common-field smoothing, checked against (2.9)–(2.11) in C1. No change to the frozen candidate. |
| 2. Colored d=3 eta limit is a routine analogue, not a literal source theorem | Retained explicitly as an exposition/import limitation. C1/C4 approve the step using bounded continuous smoothed covariances and weak Green-kernel approximation. Do not call this human-verified or Lean-certified; revisit before circulation. |
| 3. Move the noncircular summability lemma earlier | Deferred editorial preference; C2 verifies no circularity and the forward reference is explicit. |
| 4. Generalize the counterexample | Not adopted for the same reason as V1-3. |
| 5. Narrow the abstract's no-go wording further | The precise common-theta scope is fixed in the statement/remark and confirmed by C8; retain exact review binding. Use the narrow wording in every status report. |
| 6. Explain compact-time summability and solution identification | Imported solution identification remains a source input; corrected bound is compact-time summable. Reviewer records no blocking issue. Not a re-verification of the source's complete existence proof. |
| 7. Whole-source word 'only' in the setup description | Historical source-use summary is not independently audited across all 64 pages; no theorem or no-go relies on it. |
| 8. Additional source typos/monotonicity step | Not used; direct telescoping avoids that step. Source PDF remains unchanged. |

No substantive Opus-authored repair was inserted: the colored-noise argument
was GPT-authored in response to the root's pre-report concern. All new v2
mathematics is reviewed in v2; unchanged v1 judgments are retained as history.

### V2 format and account recovery

The v2 raw scientific report is PASS_WITH_NOTES/high, C1–C8 all PASS, no
required repairs, complete source coverage. Driver accepted=false because
introductory/closing prose makes the response invalid JSON. The exact raw
response is retained in `reviews/2026-10-27-round1/review-v2-original.txt`.
The same-session format-only continuation hit a subscription session limit;
that failure is not a review. A fresh unchanged-v2 attempt is launched using
an already-configured first-party subscription account after identity and
READY checks. No model, billing route, mathematical candidate or confidence
threshold changed; only the output-format instructions were reinforced.
See `reviews/2026-10-27-round1/account-recovery-log.md`.

### Final recovery disposition and additional findings

`opus-v2-recovery` completed normally on the unchanged v2 candidate:
**PASS_WITH_NOTES / high; accepted=true; driver exit 0; C1–C8 all PASS;
no fatal/major findings or required repairs.** Actual model is Claude Opus
5.5. The source-read ledger verifies complete required text/image delivery.
The final report and exact hashes are in `review-v2-report.json` and
`review-v2-summary.json` under the Round 1 review directory. Complete native
attempts, including the rejected format and quota failure, are archived
without rewriting them. Archive readback confirms the bound bytes.

The recovery report has seven optional findings, all adjudicated here:

| Recovery finding | Disposition |
|---|---|
| 1. Spell out translation/reversal before identifying colored covariance diagrams | C1 explicitly checks both transformations; retained as a future exposition improvement, not a changed hypothesis or blocking gap. |
| 2. Write the elementary colored d=3 eta-limit justification | Same limitation as V2-2; C1/C4 accept it using bounded continuous fixed-smoothing covariances and weak Green convergence. No claim of human/Lean verification. |
| 3. Emphasize the joint per-vertex limit | Candidate already says finite joint limit independent of relative rates; source Lemma 4.4 and C1 supply the exact hypothesis. |
| 4. Explain the regularized delta evaluation in the white-space test | The delta is integrated against Green kernels, not assigned a pointwise value. C3 checks the approximate-identity limit; a prose sentence may improve presentation before circulation. |
| 5. Broaden the counterexample beyond white noise | Not needed; retain the exact nonzero witness and avoid an unnecessary generalization. |
| 6. Name Section 5 in the historical source-use summary | Editorial suggestion; actual Section 5 application is explicitly audited in the G0 section. |
| 7. Old planned-route item still cites (4.4) | Preserved as the setup plan, superseded by the reviewed G0 source diagnosis and this workflow authority. Future work must use the corrected pinpoints and cannot revive the failed estimate. |

The scope is a reviewed diagnostic proof note, **not** whole-paper or
circulation clearance. External analytic theorems remain imported inputs;
no claim is made to have re-proved Chen's existence theorem or Lemma 4.4.
Final DeepSeek cold reading remains required before circulation/whole-goal
clearance. No Skorohod result was developed and no Lean package was created.

### Round 1 evaluation and close

- Worker status: DONE_WITH_CONCERNS (optional exposition limitations retained).
- G0 completeness: 8/10; instantiation score: 1.0 (new deductions proved,
  external source inputs identified); advance_delta: 1.0 for this bounded subaim.
- Notes: 11 pages; final build 0 errors, 0 undefined references/citations,
  0 overfull boxes; exact finite count checks pass through total order eight.
- Final candidate TeX SHA-256:
  `2c052ae4f6564b7f6a682ceb9830805ace7dca44fc74cce50f5e7664ac117761`.
- Final PDF SHA-256:
  `177b04f39f41ea9255e2e42b83c691efcfa5e47b363a3cf1d10735be3c24c49e`.
- Article round-close commit: 4ff2bca60e666482480596cc1e53b9be06750ea7.
- Wiki sync commit: ae3ebd08c971f6f04f66cdef9da8344395b08722.
- Next action: Le reads this report and chooses whether/how to proceed.
  Round 2, Lean L1 and companion creation remain unopened.

## Review readiness

| Layer | Runs | Status | Scope |
|---|---:|---|---|
| Root checks / instantiation | 2 candidates | PASS | Build, finite controls, source/application checks; not independent review |
| Worker honesty | 2 | Recorded | Exact concern and import boundaries |
| Fresh replay | 0 | Not due at Round 1 | Every-third-round cadence |
| Opus skeptic | 3 scientific attempts | Final PASS_WITH_NOTES/high, accepted | V1 medium below threshold; original v2 format rejected; recovery accepted; format-only quota attempt is not a review |
| Final cold reader | 0 | Not run; required before circulation | No whole-paper clearance claimed |
| Lean | 0 | L0 unchanged | No formal-verification claim |

### Wiki propagation verification

The project page and dashboard pass targeted lint; project relations and
contract validation pass. Index and dashboard generators were run in an
isolated clone. Timestamp-only index changes and unrelated machine-dependent
idle-time churn were removed; the project's missing cohort/dashboard entries
were retained. Existing companion and all five anchor-paper backlinks resolve.
The historical global log has pre-existing render/citekey warnings outside the
new log line; no such warning is introduced by this round. Full push-gate and
remote parity are verified at final close. Dashboard propagation commit:
`b413045eb74c4d61988e0178b8ade96c1def9ae9` (separate from the project Timeline commit above).

### Wiki pre-push race reconciliation

Three unrelated upstream wiki commits arrived before publication. The two
local documentation commits were rebased; range-diff reports both patches
identical (`=`). No Article source, review candidate or scientific report was
rewritten. The preliminary unpublished wiki identifiers in the earlier
provenance commit are superseded by the current hashes above.

```text
1:  e55a9f041 = 1:  ae3ebd08c project: record reviewed Stratonovich second-moment G0 verdict
2:  3e5c17975 = 2:  b413045eb propagate: include Stratonovich HAM project in cohort dashboard
```

## Resumption and Round 2 opening (2026-10-27)

Le reactivated the full goal after reading the G0 report and the explanation
of the checkpoint, then instructed continued work under replacement AGENTS
instructions. This authorizes proceeding beyond decision point 1; the old
handoff's stop is historical, not a fresh request to stop again. The broader
goal remains unchanged and active. The previous substantial goal turn was
progress: reviewed G0 results, source correction, committed evidence and parity.

Preflight: clean local/origin/<HUB> at `2e2ce0e`. Round 2 is the existing
G1 calibration subaim, not a novelty claim or a large new all-order proof wave.
Its finite-order identities are specializations of the reviewed G0 expansion;
retain the exact common field, covariance normalization and all self-pairings.
The G0 uniform-pairing no-go is not reopened.

Round 2 tasks:
- [x] Explicit total-order-four white-space terms, including all five splits.
- [x] Riesz order-two formula and useful reduced order-four representation.
- [x] Static-noise boundary calibration, homogeneity and source comparison.
- [x] Frozen packet, Opus skeptic, adjudication and clean notes build.
- [ ] Round close and successor-route decision within the full goal.

Lean reconnaissance found existing finite-matching interfaces in the private
SWE companion registry. These are reuse candidates only; no sibling edits,
new package, registration or verification claim has been made. A concrete
creation proposal remains subject to decision point 4.

### G1 candidate and verification status

Candidate frozen at TeX SHA-256
`1d1646e5b45ce8a80a5ccbde83bc944b8a0b1027620fc5ba6429be57c6c75560`.
The new section gives nine distinct white-space rows, with chain exchange
covering all fifteen order-four diagrams. Static total-order-four coefficient
is 11/540; Riesz order-two and explicit order-four representations are included.
These are fixed-order calculations, not proofs of either principal goal.

The exact polynomial-sector integration is the written proof mechanism.
Worker Sobol checks and the root's separate bounded-indicator Monte Carlo
agree with the exact static values but are diagnostics only. The latter uses
1,048,576 IID samples per split; the nine distinct entries are within 1.67
reported Monte Carlo standard errors of their proposed exact values.
Native Opus 5.5/high review is running on the frozen candidate, with mandatory
source delivery and JSON-only reporting. No acceptance is claimed yet.

Lean creation proposal: `lean-progress/CREATION-PROPOSAL.md`; Le was asked
asynchronously at the explicit decision point 4. Creation remains pending;
mathematics work is independent of that unanswered decision.

### G1 final review and adjudication

Native Opus 5.5/high returned **PASS_WITH_NOTES / high**, accepted=true,
all C1–C8 PASS, no fatal/major findings or required repairs. Complete text
and source-image delivery passed the read ledger. Root verified that the
entire G0 section is byte-identical to its previous committed version;
only title/abstract navigation and the new G1 section changed. This is a
scoped G1 review, not a re-audit of G0 or of imported analytic theorems.

| Optional finding | Adjudication |
|---|---|
| 1. Chain exchange also relabels pairings | Confirmed: between splits (1,3) and (3,1), A and C exchange and B stays B. For (0,4)/(4,0) the labels are unchanged. The theorem says exchange chains, not keep pairing labels fixed; the summed coefficient formula is correct. This explicit reading is retained here. |
| 2. Approximate-identity and time-truncation passage is terse | C2 checks continuity of the reduced area off null boundaries, a uniform 1/4 bound, and the monotone time truncations. Accepted as complete in substance; preserve the optional exposition limitation. |
| 3. G0 order-two white calculation could cite the same approximation | Existing G0 proof unchanged; the same elementary argument applies. No claim that a delta has a pointwise value. |
| 4. Fixed dominating exponent wording in Riesz static remark | Read as choosing a fixed upper exponent before decreasing alpha0, exactly as in the preceding lemma. Deferred prose clarification; no limit-order change. |
| 5. Riesz regularized-to-Lebesgue identification is implicit | C6 accepts the elementary domination at fixed alpha<1 and bounded wave supports; imported G0 convention remains explicit. No stronger covariance class is claimed. |
| 6. Static rows could say coefficient limits instead of alpha0=0 | The lemma and scope remark explicitly define this meaning; no endpoint SPDE or interchanged large-time/static limit is claimed. |
| 7. Abstract 'computes' can overstate Riesz order four | Actual proposition and scope table explicitly give an unevaluated but fully specified integral representation, not a closed form. Status reports retain that distinction. |
| 8. Symmetry-related Monte Carlo rows fluctuate more | Root's earlier 1.67-SE statement concerned the nine distinct rows only. The full fifteen include deviations up to about 2.4 SE, consistent with the preserved raw sample. No acceptance or proof uses Monte Carlo accuracy. |

Exact static white-space totals: M2(t)=t³/3 and M4(t)=11t⁶/540.
For fractional time, M2(t)=2c0 t^(3-alpha0), and all M4 terms are the
explicit time integrals in the nine-row table with chain exchange. The
Riesz order-two formulas are explicit; its order-four result is a finite,
fully specified unit-domain integral, not a closed-form evaluation.
The published static exponent is source-checked; disputed white constants
are not used. Both G:upper and G:sharp remain open.

### Round 2 evaluation and close

- Status: DONE_WITH_CONCERNS (optional exposition findings retained).
- G1 completeness: 8/10; instantiation: 1.0; advance_delta: 1.0 for G1.
- Clean notes build: 17 pages, 0 errors/undefined references/citations/
  overfull boxes. No Lean verification is claimed.
- TeX SHA-256: `1d1646e5b45ce8a80a5ccbde83bc944b8a0b1027620fc5ba6429be57c6c75560`.
- PDF SHA-256: `bfa0b11fb4f85a9c26a7a09fe021766170900eb2dfe5efd1194965aa99e8b0cb`.
- Review: `reviews/2026-10-27-round2/review-report.json`; exact bindings in
  `review-summary.json`, full native evidence in `review-evidence.tar.xz`.
- Article Round 2 commit: 8358d58c40591922a971790827f10ebe576932e0.
- Wiki Round 2 commit: 7c61911c772834f7d26f0809466102434e1cb0ab.
- Decision point 4: creation proposal prepared and asked; no answer received
  yet. No repository, remote or registry entry has been created.
- Next formal work: reviewed G0 finite/algebraic seams in the proposed private
  companion, once approved. Next mathematical work: falsification/reconnaissance
  of an all-order estimate that retains more than the failed uniform bound.

The Round 2 wiki clone helper initially refused its own overwritten tracked
page-health cache. The failed clone was removed by the helper. A fresh manual
isolated clone preserves the tracked cache and provisions read-only adapters;
no canonical wiki WIP or tool installation was modified to bypass the refusal.

### Parallel continuation authorized (2026-10-27)

Le explicitly authorized multiple subagents for parallel/independent work.
Three read-only tasks produced a mathematical route screen, an independent
primary-source crosswalk, and an exact-pinned Lean reuse memo. These are
reconnaissance, not new accepted manuscript proofs or Lean certificates.

[held back: collaborators' unpublished work]

Round 2 publication verification: project lint and relation checks pass;
index/dashboard generators ran, with unrelated idle-time churn discarded.
No project-status/DAG change required a separate generated propagation commit.
The exact wiki commit passed the full pre-push gate and the final origin race
check before publication. G1 is complete; G2 remains reconnaissance only.
