# Project goal and completion contract

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

[held back until the source author has been told]

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