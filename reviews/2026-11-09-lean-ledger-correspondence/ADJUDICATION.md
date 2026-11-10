# Adjudication: DeepSeek V4 Pro correspondence review of the Lean statement ledger

- **Object:** `docs/statement-ledger.md` of `stratonovich-ham-second-moment-lean`
  at companion commit `38d16163ab8979dadb63766e41e59e9a84339d68` (lean-pkg
  verified-private), against manuscript revision
  `cf979d698a6ee7769e8c1316f43bc69948fa224b` (main TeX + 27 inputs).
- **Reviewer:** route `paper-review-deepseek`, model `deepseek/deepseek-v4-pro`
  (requested; `opencode run --pure`, session `ses_e3c60472fffeYisfgJxQG8MYuj`).
  OpenCode has no `reviewer` agent and fell back to its default agent;
  `OPENCODE_PERMISSION={"*":"deny"}` and the raw log has one step and no tool
  call, so the run was read-only with the inline frozen payload only.
- **Frozen inputs:** `prompt.md` (1,009,788 bytes, SHA-256 in
  `packet-manifest.json`): ledger, claims.yaml, 24 Lean files, 28 TeX files,
  each hashed. No prior review supplied. Not a cold read.
- **Run:** exit 0, 315,581 input / 5,139 output / 39,686 reasoning tokens.
  Report `report.md` (extracted text of `raw.jsonl`).
- **Coverage:** Section A has all 88 rows. Verdict PASS_WITH_CONCERNS,
  CRITICAL 0, MAJOR 1, MINOR 6, confidence **MEDIUM** (the reviewer's own
  reason: the 53 no-label confirmations were done by reading, without
  tool-assisted search). This is below the project's HIGH bar; see Status.
- **Adjudicator:** Claude Opus 5.5 (#22), the ledger's commissioning author.
  Every finding was checked against the TeX at cf979d6 and the Lean sources
  before a disposition. Manuscript-owner input from #3 (private audit
  `private/audit/2026-11-09-companion-target-triage.md`, commit 4288421)
  is applied where it overlaps.

## Findings

| ID | Sev | Declaration(s) | Disposition | Evidence checked | Change (companion a78c5d0) |
|---|---|---|---|---|---|
| F1 | MAJOR | JointTilt.wrong_sign_error, wrong_cost_error | **ACCEPTED** | `integrated_raw_block_lower.tex`: no sign-reversal or doubled-cost computation; #3 independently: "controls, not extra change-of-law theorems" | Both now "no direct label (diagnostic)"; tilt_exponent reworded as an auxiliary exponent-consistency check (#3 item 3) |
| F2 | MINOR | WhiteCDF.cdf_square_bound | **ACCEPTED** | `integrated_white_evaluation.tex` l.71–72: "Substitution z=3A into (E:white-cdf-square) gives 3A²≤b" inside proof of P:white-spatial-energy | Relabelled to P:white-spatial-energy; L:white-cdf-square is the supplied hypothesis; coverage row L:white-cdf-square removed (no Lean claim left) |
| F3 | MINOR | InteractionDriver.temporal_range | **ACCEPTED** | E:driver-parameters (l.19–22) also needs (3-a-α)/2, γ range, θ<β | Row states only the 1-a/2 endpoint is checked |
| F4 | MINOR | InteractionDriver.holder_parameters, dyadic_ratio | **ACCEPTED (partly pre-disclosed)** | Module text already named the midpoint choice; L:driver-holder-limit takes an arbitrary interior η | Module paragraph states the rows check the midpoint instance only |
| F5 | MINOR | DirectEvent.kappa_gt_one | **ACCEPTED** | E:kappa (main l.141–142) asserts κ∈(1,2); Lean `1 < kappa` only | Row states κ<2 is not checked |
| F6 | MINOR | 37 auxiliary definitions | **ACCEPTED** | Inventory: 43 public defs, 6 with rows | Scope bullet: the other 37 only name quantities and have no rows |
| F7 | MINOR | InteractionDriver.box_margin, box_scale | **NO CHANGE NEEDED** (confirms existing assignment) | Lean 2/p vs manuscript d/Q with separate Q; #3 item 2 agrees | Added #3's d/Q note so the resemblance is not read as a mapping |

No finding was rejected. No finding is a Lean or manuscript defect: all
are ledger mapping/scope precision. No manuscript edit is required; the
manuscript owner (#3) confirmed no source defect.

## Resulting counts

Labelled rows 35 → **33**; no direct label 53 → **55**. coverage.yaml:
24 rows (20 inputs-supplied, 4 outside). claims.yaml is unchanged (88
claims; the two diagnostics keep status `reusable`, a build input, so not
changed without a new receipt; recorded here as a known imprecision).
Companion `a78c5d0` is a docs-only descendant of `38d16163ab89`; the
lean-pkg receipt stays bound (gate check output confirms).

## Status

- Accepted repairs: applied. Re-review of the edited rows: **not run**.
- The review is MEDIUM confidence, below the HIGH requirement for an
  acceptance-grade correspondence gate, and a single family. It does not
  establish correspondence acceptance for the 33 mapped rows. Per AGENTS.md,
  the next step toward a gate is a second-family review (Kimi-K3, the other
  designated reviewer) of the post-repair ledger at a78c5d0 with
  tool-assisted label search, or a human statement-fidelity read (community
  work package A1).
