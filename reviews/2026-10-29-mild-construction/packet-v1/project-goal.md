# Project goal and completion contract

Status: SET UP 2026-10-26 by Le Chen's instruction ("create a project for
the second moment, upper bound and exact constant; another agent (Codex)
will run it"). Handed to Codex agent #30 on 2026-10-26 with Le's instruction
"use paper-dev + lean-pkg workflow".

## Goal statement (set this as the run's goal)

> Develop Article-Stratonovich-HAM-Second-Moment with the paper-dev + lean-pkg
> workflow: prove an upper bound for E u^2(t,x) at the scale
> t^{(4-alpha-alpha_0)/(3-alpha)} for the Stratonovich hyperbolic Anderson model
> with time-fractional noise, then pursue the sharp p=2 constant, round by
> round from Gate G0, with every new proof cross-family reviewed and its finite
> and algebraic parts verified in a private lean-pkg companion; record no-gos
> honestly; stop for Le at each decision point listed below.

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

[held back until the source author has been told]

## Scope limits

[held back: collaborators' unpublished work]

## Decision points: stop and report to Le

[held back: collaborators' unpublished work]