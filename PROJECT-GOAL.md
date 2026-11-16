# Project goal and completion contract


## Active publication goal — 2026-11-16

Set explicitly by Le: "Can you update your goal to complete these work".
The earlier bounded Appendix G goal is complete; the active goal now covers
the remaining publication process below. Progress.md remains the workflow
authority, and the exact owner decisions and source-bound receipts govern
execution.

1. Finish the authorized final-source rereads and mathematical adjudication,
   with at most three concurrent reviewer jobs. Keep superseded reports on
   their actual sources, and retain every failed, partial and conditional
   outcome. Build an exact final-source coverage inventory; returned reports
   alone are not accepted deductions or a publication-completion percentage.
2. Synchronize Appendix E, AI-use disclosures, dated review statistics and
   VERIFICATION provenance through the last adjudicated review. Preserve
   Le's honest-standing release choice and all recorded scientific grades;
   no local report, editorial aid or source-pixel check upgrades whole-book
   assurance. Unknown usage/cost remains unknown, without estimates or
   double-counting historical censuses.
3. Coordinate the final book, reader and combined editions, approved figures,
   Preface and editorial corrections with Agents 24, 16, 22 and 5. Verify
   the exact candidate's build/link/critical-path, Lean-label/correspondence,
   preservation, filter and export checks. Reconcile Progress, handoff and
   internal project status through their authorized owners/queue.
4. After the final review and disclosure/data synchronization, create one
   manifest-only REVIEW-SYNC reseal on Agent 16's exact verified candidate.
   Deliver its parent/SHA, source/PDF hashes and snapshot receipt. Early
   sealing or stale disclosure/statistics does not satisfy this gate.
5. Continue the remaining publication sequence as its actual human gates are
   satisfied: Le's typesetting pass; R; companion re-anchor/v0.10.0 and
   private-video handoffs; re-pin/rebuild/reseal and zero-shift checks; F;
   rehearsal/trial audit; Le's accept file; approved export/publication.
   Agent 16 retains integration/verification and named-push coordination;
   Le authorizes public release and submits to arXiv.

Do not mark this goal complete while required work remains. Approval-dependent
steps remain explicitly open until their evidence arrives. This goal does not
invent a new review allowance, confidence retry, fallback, push, release or
submission permission. It does not declare the historical mathematical
completion contract below satisfied or rewrite its assurance record.


Status: SET UP 2026-10-26 by Le Chen's instruction ("create a project for
the second moment, upper bound and exact constant; another agent (Codex)
will run it"). Handed to Codex agent #30 on 2026-10-26 with Le's instruction
"use paper-dev + lean-pkg workflow".

Revised by Le on 2026-10-31 in this thread:

> Chen's requested sharp constants might not be the right one, but he has his good intuition to guess those. But we should not force us to get those constants. We should derive the contants, whatever they come out of our computation.

This explicitly supersedes matching Chen's conjectured constants as a
completion requirement. Preserve the original model, exponent, all
admissible dimensions/covariances, and verification and scope requirements.
Chen's predictions and the documented normalization issues remain
literature comparisons; they do not constrain the constant we derive.

## Goal statement (set this as the run's goal)

> Develop Article-Stratonovich-HAM-Second-Moment with the paper-dev + lean-pkg
> workflow: prove an upper bound for E u^2(t,x) at the scale
> t^{(4-alpha-alpha_0)/(3-alpha)} for the Stratonovich hyperbolic Anderson model
> with time-fractional noise, prove the asymptotic limit and derive its
> actual p=2 constant from the model, whatever value or variational formula
> the proof gives. Simplify and bound that constant where justified; compare
> with Chen's prediction without forcing agreement. Use independent
> cross-family review and authorized local Lean checks for worthwhile
> finite/algebraic steps; creating a private companion still requires
> decision-point-4 approval. Record no-gos honestly and honor the remaining
> decision points and scope limits.

## Objective

For the Stratonovich hyperbolic Anderson model (1.1) with covariance
|s−t|^{−α₀}γ(x−y), 0<α₀<1, γ(cx)=c^{−α}γ(x), α₀+α<2 (0<α<d, or α=d=1),
d ∈ {1,2,3}, data (1,0), and κ = (4−α−α₀)/(3−α):

- **Goal G:upper.** Prove limsup_{t→∞} t^{−κ} log 𝔼u²(t,x) < ∞, with an
  explicit constant if possible.
- **Goal G:sharp.** Derive an intrinsically defined constant C₂(γ,α₀)
  and prove lim_{t→∞} t^{−κ} log 𝔼u²(t,x) = C₂(γ,α₀) for every fixed x
  and every original admissible model. Specify its complete variational
  domain, covariance amplitude, kinetic coefficient and Gaussian action.
  An exact, fully specified variational characterization is a derived
  constant; distinguish it from a nonsharp bound or a claimed closed form.
  Further simplification, evaluation and rigorous bounds must follow the
  computation rather than a prescribed guess. Treat zero covariance directly.

Historical comparison, not a required answer: the original setup sought
2^{(4−α)/(3−α)}L_* ≤ liminf ≤ limsup ≤ 2^{(4−α)/(3−α)}L^* and an exact
limit at the upper endpoint conditional on the source gap. Retain that
conjecture and its source qualifications in the comparison record. We may
derive a different constant or show that a proposed identification fails.
No source correction or equality of energy domains is silently adopted.

Partial outcomes count and must be recorded honestly, for example:
G:upper alone; improved bounds consistent with actual Jensen;
G:sharp in d = 1 only; or a proved obstruction showing that a named
route cannot reach the scale t^κ.

## Completion contract (for any claimed result)

1. Every new statement has a complete written proof in the notes, with all
   imported inputs labeled and pinpointed to the author-version PDF.
2. The statement passes the calibrations in AGENTS.md (α₀→0; p=1;
   Jensen; comparison with the Skorohod p=2 result).
3. Independent cross-family review using DeepSeek V4 Pro + Kimi-K3,
   per Le's directive in AGENTS.md, with DeepSeek V4 Pro explicitly the
   main reviewer (2026-11-02), HIGH confidence and
   verified actual route, source, application and visual coverage. Every
   finding is adjudicated in Progress.md. Any result Le may circulate also
   requires a final cold read in a fresh session, independent of material
   proof authors and the skeptic as required by the review protocol.
   Preserve earlier reviews under their original identities and scopes.
4. Clean build: 0 errors, 0 undefined references/citations, 0 overfull
   boxes; PDF committed with the source.
5. Progress.md, the wiki project page status line, and a handoff updated;
   commits pushed and <HUB> in sync.

Current internal mathematical checkpoint: scientific40ec9a9, adopted at
d52d1d8, proves the all-model intrinsic limit C₂=S₂^pos=2^{(4−α)/(3−α)}S₁^pos
with the explicit positive raw-control class in
`notes/physical-signed-positive-score-comparison.md`. This is not actual p1
or an identification with Chen's L. Integration, final whole-paper/cold-read
checks and synchronization remain separate; this checkpoint alone does not
declare this completion contract satisfied. This intrinsic theorem is now
integrated in `notes/integrated_intrinsic_constant.tex`, scientifica880288,
with its own full actualOpus5.5/HIGH30-check application review and no
required repairs. Occupation/white-example integration is now scoped-gated
at scientific d041546 (packet 691f413), with 31 HIGH checks and no required
repairs. Final presentation, whole-paper/cold-read, calibration/source and
delivery gates remain OPEN. The older tracked
TeX goal/summary paragraphs have now been reconciled in a consolidated
working candidate. Its changed proof text still requires the fresh
whole-argument and final cold reviews; no component receipt is silently
transferred to those new bytes. The first whole-argument attempt timed out;
its supported continuation returned INCONCLUSIVE/medium with incomplete
image/source coverage and is not accepted. The coverage-recovery target
retains all sections, proofs and primary/render obligations. Its editorial
successor changes scope/status prose only; the full mathematical and final
independent cold gates remain open.

## Scope limits

[held back: collaborators' unpublished work]

## Decision points: stop and report to Le

[held back: collaborators' unpublished work]