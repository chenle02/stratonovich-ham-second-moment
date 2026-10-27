# HANDOFF

**Last updated**: 2026-10-27 14:28 UTC
**Project**: Article-Stratonovich-HAM-Second-Moment — reviewed partial upper bound
**Wiki page (authoritative strategy)**: `../SPDEs-wiki/content/projects/stratonovich-ham-second-moment.md`

## ⏭ Next session: where to stand and what to do

Stand at this repository root on `master`. Read `Progress.md` and the
accepted Section5 result, especially Proposition 5.5 on PDF p.21.
**Stop for Le at decision point 5:** the target-scale upper bound has now
been proved and cross-family reviewed for 0<alpha<=1 in d=1,2,3. The
original full goal is not complete. Do not open another proof wave until
Le responds to this checkpoint. Point1 was passed earlier and must not be
reimposed; this is the new proof checkpoint.

The private companion proposal is also pending the explicit decision point 4
answer. No repository, remote, package registration or lease has been created.
Approval to continue mathematics is not automatically approval to create it.

## Pre-flight checks

1. `git fetch origin && git status -sb`; audit local/origin/<HUB> and
   preserve new foreign WIP. Expected ancestry and provenance are below.
2. Author PDF SHA-256:
   `5f7385ca451e643a1f3ff31835e4ee52b2708b5d2e3652eec3fb5d3958b97b6c`.
3. Read `AGENTS.md`, `PROJECT-GOAL.md`, `Progress.md`, source manifest,
   Section5 and `lean-progress/CREATION-PROPOSAL.md` before acting.
4. Canonical notes have 25 pages. Build with the root latexmk command;
   require 0 errors, 0 undefined references/citations and 0 overfull boxes.
5. Final TeX SHA-256:
   `1ca13d491918d96126e70aef6229a80805ce5043a676f0a55c34c0858238e686`.
   PDF SHA-256:
   `461da80cee71c1b651ed63500c8ce9687c92dbeb8bcfc555979321690d6dc8bd`.
6. Verify actual live handles before waiting on any job. All current agents
   and native mathematical reviews are terminal; no cluster job was launched.

## Concrete deliverables for the next session

- Obtain Le's decision after the reviewed partial G:upper result.
- If mathematics continuation is authorized, choose the remaining
  1<alpha<2-alpha0 range in d2/d3 or the sharp-constant work according to
  that direction. Preserve the full goal, including the inherited constant gap.
- A tentative high-alpha spatial-maximum/Holder lead is recorded in
  `reviews/2026-10-27-round3/recon/high-alpha-transfer-note.md`; it is
  UNREVIEWED, not a theorem. Its maximum hypothesis is not available for
  arbitrary anisotropic homogeneous covariance. Revalidate before use.
- If companion creation is approved, reuse the exact-compatible Physlib
  matching count, review the actual statement interface and verify the new
  coefficient-count/algebra consumers locally through lean-pkg. The package
  must remain private; no public release is authorized.

## Success criteria for the immediate next step

Le has made the next-wave decision. The successor must keep the accepted
proof unchanged unless a concrete defect is found, preserve the distinction
between proved alpha<=1 coverage and open higher-alpha cases, and obtain
independent review for any new proof. Formal verification must reach actual
consumers, not merely re-define the desired numerical recurrence.

## Anti-success criteria

[held back: collaborators' unpublished work]

## What the previous sessions produced

- G0: `4ff2bca60e666482480596cc1e53b9be06750ea7`, reviewed mixed expansion,
  corrected crude bound, intermediate rho upper bound and scoped no-go.
- G1: `8358d58c40591922a971790827f10ebe576932e0`, all 15 white order-four terms,
  exact static coefficient11/540, Riesz coefficients/representation.
- G2 scientific checkpoint: `53e2817eafd9ed4de30f3acda6427629b61c71e0`. Spatial endpoint elimination
  retains k^(-(2-alpha)k); the full temporal Wick sum is then symmetrized,
  yielding denominator(k!)^(3-alpha). Spectral ball masses handle alpha<1;
  a separate degree-one polar/Gaussian Fourier identity handles alpha=1.
- Result: E u²<=exp(C2 t^kappa), kappa=(4-alpha-alpha0)/(3-alpha), for
  0<alpha<=1 in all three dimensions, with explicit nonsharp constants.
  This covers the full stated d1 range and includes its white endpoint.
- Opus final upper review: PASS_WITH_NOTES/high, all 12 checks PASS, accepted,
  complete source delivery, no required repairs. Earlier FAIL/medium screen,
  repaired screen, below-threshold d1 review and preflight refusal are preserved.
- Status-only promotion changed no mathematics: root compared all 14 proof
  environments, all 27 statement bodies and equation blocks byte-for-byte.
- Exact scopes/hashes/archives: `reviews/2026-10-27-round3/README.md` and
  `upper-review-summary.json`, `upper-promotion-binding.json`.
- Known reusable count: Physlib pin3bfc7af8dbd43b439d761e09ce365a3759b5c2f5,
  matching Lean 4.35.0 / Mathlib 56a005855ea17e0b0958f73ec801ae140b0a1679.
  Read-only source findings are in `lean-progress/recon/`; no build was run.

## Repo & git state at handoff

- Article pre-handoff HEAD: `0982ca48c65b8a55878019f2dcf0fb7b4ecddc9c` on `master`.
- Accepted scientific checkpoint: `53e2817eafd9ed4de30f3acda6427629b61c71e0`.
- Wiki proof-status commit: `a1aab66454bfefa4c5823684b9a9635fcc152539`, published after the full push gate
  and final origin race check. Its rebase onto unrelated upstream work was
  patch-identical. The provenance loop is recorded in Progress.md.
- This handoff is a separate commit. Final push/parity and clean-tree checks
  follow this write. The clean isolated wiki clone contains no external WIP.

## Operating notes

The full goal remains unfinished; the goal service is stopped at the user's
proof checkpoint, not marked complete. Higher-alpha G:upper, G:sharp, private
formal verification and final cold-reader/circulation clearance remain open.
The Lean track is still L0. The pending creation question was not answered;
elapsed time is not approval. No emails, fleet messages or Telegram notices
were sent. No public paper or Lean package was released.

## Risks to monitor

1. The successful theorem requires nonnegative covariance as well as positive
   definiteness; neither requirement may be silently removed.
2. Temporal symmetry is used only AFTER taking a common spatial bound and
   SUMMING pairings. It is false for a general individual diagram.
3. The alpha=1 endpoint retains the oscillation and uses a polar measure;
   the divergent absolute Fourier envelope cannot be used there.
4. In d3, take the Green eta limit at fixed noise smoothing before the noise
   limit. The accepted proof writes the L2/L1 transfer explicitly.
5. Higher-alpha maximum bounds may fail for anisotropic covariance; the
   unreviewed conditional lead is not the full remaining theorem.
6. Static endpoint tests constrain uniformity near the endpoint, not an
   arbitrary separately chosen constant at fixed positive alpha0.
7. Imported source results remain imports; no whole-source, novelty, human
   referee or Lean certification is inferred from the Opus report.
