# Adjudication: Codex GPT-6.1-Sol correspondence review of the Lean statement ledger

- **Object:** `docs/statement-ledger.md`, companion commit
  `5e0d122fd3f8efd6b4dc758f431818df912eff05` (after both Kimi-K3 fix rounds),
  against manuscript `669ccc9b07241ae94f365f4a2e17c04da66870ca` (41 TeX inputs).
- **Reviewer:** `subscription-review-cli run codex --model gpt-6.1-sol --effort
  high` (lab default GPT setting), codex-cli 0.167.0, ChatGPT subscription
  login, no API key. Receipt: `model_actual` gpt-6.1-sol, `effort_actual` high.
- **Family independence:** the ledger was written by Claude; the original Lean
  seams were written by the Codex/GPT worker. The object under review is the
  ledger, so the reviewer family differs from the ledger's author. No earlier
  report was in the packet.
- **Read-only:** `codex exec --sandbox read-only`, `approval_policy="never"`, web
  search, hooks, apps, plugins, browser, computer use and multi-agent disabled,
  user config ignored (`attempt-01/execution.json`, `codex-profile.toml`).
- **Launch deviation (recorded):** the default launch was refused
  (`blocked-auth-or-launch`): the tool's skill-disable override for 1,432
  skills in `~/.codex/skills` exceeds the 126,976-byte single-argument limit.
  The run used `CODEX_HOME` = a dedicated directory holding only a symlink to
  the real `auth.json` (`codex-home-listing.txt`), so the reviewer had no
  skills and no user config. The lab tool itself was not changed.
- **Frozen packet / preflight:** `packet.tar.gz` (68 files + `PROVENANCE.json`,
  byte-compared to git blobs); `candidate_hashes_unchanged` true. Contract =
  the Kimi v2 contract with the commit id updated; `contract-check` observable
  on the contract and the dispatched prompt (`contract-check.json`); dry run
  clean (`dryrun/`). Evidence scanned for auth tokens: none.

## Transport, validity, acceptance

| Layer | Result |
|---|---|
| Transport | completed, exit 0, 821 s |
| Report validity | **valid** (`review-complete`), first valid high-confidence report of this ledger |
| Scientific verdict | **FAIL**, confidence high: 88 checks (81 PASS, 3 PARTIAL, 4 FAIL); 1 fatal, 2 major, 0 minor; 4 required repairs |
| Acceptance | not accepted (`blocking-finding`): correct, the ledger at 5e0d122 had real defects |

## Findings (adjudicator: Claude Opus 5.5, #22)

| ID | Sev | Disposition | Evidence checked at 669ccc9 / Lean | Change (companion c9e28af) |
|---|---|---|---|---|
| K1 | FATAL | **ACCEPTED, with a modification** | `integrated_wave_variance.tex`: `P:actual-wave-form` (l.212) states `<S(-t)B(b(t))S(t)z,w>` (`E:variance-physical-adjoint`) and the kernel `(-b_r c_ρ, -b_r b_ρ; c_r c_ρ, c_r b_ρ)/sqrt(<ξ><η>)` (`E:variance-normalized-kernel`), derived at l.317–329; `S(-t)(0,f)=(-sin(t|D|)f/|D|, cos(t|D|)f)` at l.310. Lean `full_interaction` (`DimensionalMatrix.lean:15–17`) is exactly this kernel with `c_r=cp`, `b_r=sp/p`, `c_ρ=cq`, `b_ρ=sq/q`, coefficient `H`. `forward`=`S(t)`, `backward`=`S(-t)`, `coupling`=`B(b)(u,v)=(0,bu)` (`integrated_symplectic_phase.tex:41`, in `L:symplectic-free`). The reviewer mapped the definitions to `L:symplectic-free`/`L:complex-phase`; this adjudication maps all four rows to `P:actual-wave-form`, where they are the factors of the displayed composition, and records the other two labels in prose. | Four rows and index → `P:actual-wave-form`; module prose rewritten (weight, Fourier interpretation and zero-frequency sine quotient outside Lean); coverage row added |
| K2 | MAJOR | **ACCEPTED** | `HermiteWord.lean:26,39` `(hv₀ : Good (fun _ => 0) v₀)`; without it `raw_support` fails already for the empty word. Manuscript starts from `1⊗v`, "an induction starting from degree zero" (main l.5270–5287). claims.yaml had it. | Both rows and the module paragraph state the zero-count condition |
| K3 | MAJOR | **ACCEPTED** | `tilt_exponent` is not displayed; the proof of `P:raw-block-gaussian-law` substitutes `G'=G+sz` (`integrated_raw_block_lower.tex:124–132`). Under the ledger's own definition, an undisplayed computation carries no label. Consistent with the manuscript owner's 2026-11-09 ruling ("not a literal displayed source equation"). | Row → no direct label (auxiliary); index entry removed; coverage row `P:raw-block-gaussian-law` removed (no claim left) |
| Repair 4 | — | **ACCEPTED** | Totals: 36 labelled, 52 unlabelled (script: index equals per-module tables; all 51 cited labels exist at 669ccc9) | Totals and coverage header updated |

## Significance

K1 overturns an "absent" classification that three earlier reviews accepted:
DeepSeek V4 Pro, Kimi-K3 v1 and Kimi-K3 v2 (v2 even found the free matrix
under `L:complex-phase` but missed `P:actual-wave-form`). The manuscript
owner's target triage had also treated DimensionalMatrix as a development
calculation. That triage should be updated. K2 is a real fidelity omission
that all three earlier reviews passed. This review was the first to find a
correspondence defect.

## Status

- All accepted repairs applied at companion `c9e28af`, a docs-only descendant
  of `38d16163ab89` (gate check confirms). Coverage: 24 rows (20
  inputs-supplied, 4 outside).
- **Correspondence gate: NOT closed.** This valid review returned FAIL on
  5e0d122. Closing the gate needs a successor review of the repaired ledger
  at c9e28af with an accepted receipt (same contract; Codex route works).
