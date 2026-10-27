# HANDOFF

**Last updated**: 2026-10-27 04:38 UTC
**Project**: Article-Stratonovich-HAM-Second-Moment — Stratonovich second-moment growth
**Wiki page (authoritative strategy)**: `../SPDEs-wiki/content/projects/stratonovich-ham-second-moment.md`

## ⏭ Next session: where to stand and what to do

Stand at this repository root on `master`. Read the Round 1 disposition in
`Progress.md` and the review reports in `reviews/2026-10-27-round1/`.
The immediate step is **Le's decision at decision point 1**, before any
Round 2 or Lean L1 work. Do not treat a resumed session as approval to pass
this gate. The uniform pairing estimate cannot reach the target scale;
its no-go is scoped to that estimate, not all uses of Theorem 3.1.

## Pre-flight checks

1. `git fetch origin && git status -sb`: verify the expected branch, parity,
   and ownership of any new dirt before edits; perform the <HUB> audit.
2. Verify the author PDF SHA-256 is
   `5f7385ca451e643a1f3ff31835e4ee52b2708b5d2e3652eec3fb5d3958b97b6c`.
3. Read `AGENTS.md`, `PROJECT-GOAL.md`, `Progress.md`, source manifest,
   notes and `lean-progress/PROGRESS.md`. The author PDF remains authority.
4. Build with the repository's latexmk command; require zero errors,
   undefined references/citations and overfull boxes.
5. `lean-pkg doctor` is diagnostic only. Lean remains at L0; no companion
   repository exists, and decision point 4 still applies before creation.

## Concrete deliverables for the next session

- Record Le's decision about proceeding after the G0 no-go.
- Only after authorization, open the next bounded round in `Progress.md`.
  The missing factorial power alpha0 is a diagnostic constraint on any
  successor estimate; it is not itself a proved route to the target.
- Keep private Lean triage separate from companion creation. No package,
  registration or publication is authorized by this handoff.

## Success criteria for the immediate next step

Le has read the Round 1 report and explicitly chosen the next action. The
next worker must preserve the reviewed scope, source correction, and
Stratonovich-only boundary. No target constant or exponent is changed to
fit the intermediate bound.

## Anti-success criteria

[held back: collaborators' unpublished work]

## What the previous sessions produced

- Setup and Lean L0 planning: `b11a8d9` and its ancestors.
- Round 1 scientific checkpoint: `4ff2bca60e666482480596cc1e53b9be06750ea7`. The notes contain the full
  mixed expansion, individual-diagram convergence proof via independent
  noise colors, exact spatial-white first-order test, repaired crude bound,
  and the homogeneous upper exponent rho=(4-alpha-alpha0)/(3-alpha-alpha0).
  It satisfies kappa<rho<2. Both principal goals remain open.
- Frozen review packets and complete native evidence archives are retained
  in `reviews/2026-10-27-round1/`. V1's medium-confidence report is preserved
  separately from the substantive v2 successor; see the exact dispositions
  in `Progress.md` and the review summaries.
- Final Opus disposition: PASS_WITH_NOTES/high, accepted with complete source
  delivery and all eight checks passed. Optional exposition limitations remain
  in Progress.md; no whole-paper/circulation clearance is claimed.
- Source manifest records the scoped time-uniformity discrepancy.
- Wiki provenance checkpoint: `ae3ebd08c971f6f04f66cdef9da8344395b08722`. Lean files remain at L0 unchanged.

## Repo & git state at handoff

- Article pre-handoff HEAD: `0a76d146daeda18cb6c69999896b519883f33d17` on `master`.
- Round 1 checkpoint: `4ff2bca60e666482480596cc1e53b9be06750ea7`.
- Wiki checkpoint: `ae3ebd08c971f6f04f66cdef9da8344395b08722` on `v4`.
- Wiki final gated/published tip: `b413045eb74c4d61988e0178b8ade96c1def9ae9`.
  The full pre-push gate passed; local canonical and <HUB> match this tip
  with clean trees. The project and dashboard targeted lint also pass.
- This handoff is committed separately. Final push/parity verification is
  performed after this file is written; inspect current refs on resume.

## Operating notes

`Progress.md` is the workflow authority. Retain all prior report bytes and
read-coverage limits. Imported analytic results remain imported; formal
verification has not begun. Every future new proof requires the prescribed
cross-family review. Final DeepSeek cold reading remains required before
circulation or whole-project clearance. No emails or fleet messages were sent.

## Risks to monitor

[held back: collaborators' unpublished work]