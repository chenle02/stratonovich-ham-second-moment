# Project goal and completion contract

Status: SET UP 2026-10-26 by Le Chen's instruction ("create a project for
the second moment, upper bound and exact constant; another agent (Codex)
will run it"). Not yet started.

## Objective

For the Stratonovich hyperbolic Anderson model (1.1) with covariance
|s−t|^{−α₀}γ(x−y), 0<α₀<1, γ(cx)=c^{−α}γ(x), α₀+α<2 (0<α<d, or α=d=1),
d ∈ {1,2,3}, data (1,0), and κ = (4−α−α₀)/(3−α):

- **Goal G:upper.** Prove limsup_{t→∞} t^{−κ} log 𝔼u²(t,x) < ∞, with an
  explicit constant if possible.
- **Goal G:sharp.** Prove
  2^{(4−α)/(3−α)} L_* ≤ liminf t^{−κ} log 𝔼u² ≤ limsup t^{−κ} log 𝔼u² ≤ 2^{(4−α)/(3−α)} L^*,
  where L_* = L(𝓔_*), L^* = L(𝓔) are the constants in X. Chen's Theorem 1.2
  (1.10) (author version, p. 3). The exact limit 2^{(4−α)/(3−α)}L^* is a
  conditional target, contingent on closing Chen's 𝓔_* < 𝓔 gap.

Partial outcomes count and must be recorded honestly, for example:
G:upper alone; G:upper plus a lower bound strictly above the Jensen bound
2L_*; G:sharp in d = 1 only; or a proved obstruction showing that a named
route cannot reach the scale t^κ.

## Completion contract (for any claimed result)

1. Every new statement has a complete written proof in the notes, with all
   imported inputs labeled and pinpointed to the author-version PDF.
2. The statement passes the calibrations in AGENTS.md (α₀→0; p=1;
   Jensen; comparison with the Skorohod p=2 result).
3. An adversarial review by a model family different from the author
   (Claude Opus 5.5 skeptic), every finding adjudicated in Progress.md, and
   a final DeepSeek cold read for any result Le may circulate.
4. Clean build: 0 errors, 0 undefined references/citations, 0 overfull
   boxes; PDF committed with the source.
5. Progress.md, the wiki project page status line, and a handoff updated;
   commits pushed and <HUB> in sync.

## Scope limits

[held back: collaborators' unpublished work]