# Narrow confirmation of the repaired ledger rows, and closing record

## The confirmation review

- **Object:** `docs/statement-ledger.md` at companion
  `48ce162955b28b752bb9a62a8c61b9f561f75295`, manuscript
  `ba01d9857383292da5359299983fe2d594c4c8f6` (50 TeX inputs).
- **Reviewer:** `subscription-review-cli run codex --model gpt-6.1-sol --effort
  high`, read-only sandbox, `CODEX_HOME` workaround (`codex-home-listing.txt`).
  Contract, schema, `contract-check` (observable on contract and dispatched
  prompt), dry run and frozen packet (77 files, byte-compared) in this
  directory. No auth tokens in the evidence.
- **Scope (six checks):** `DirectEvent.kappa_gt_one` → `E:kappa (lower
  inequality)`; `LocalFlow.noise_order` → `L:temporal-equilibrium`; the
  DirectEvent and LocalFlow module paragraphs; LEDGER-INDEX (all 88 rows, all
  cited labels in all 50 files, the three affected coverage rows);
  LEDGER-TOTALS (88 = 82 + 6; 40 labelled, 48 unlabelled).
- **Required reading, all reported complete:** ledger, claims.yaml,
  coverage.yaml, DirectEvent.lean, LocalFlow.lean,
  integrated_exact_scaling.tex, integrated_point_transfer.tex,
  integrated_temporal_equilibrium.tex, main TeX lines 160–200. Label commands
  of all 50 files searched; 57 cited labels found.

| Layer | Result |
|---|---|
| Transport | completed, exit 0, 158 s; gpt-6.1-sol / high; inputs unchanged |
| Report | valid; **PASS**, confidence **high**; 6/6 checks PASS; 0 fatal, 0 major, 0 minor; no required repairs |
| Acceptance | **accepted: true** (runner-written) |

No finding to adjudicate; no ledger change.

## Closing record for the ledger correspondence gate

The ledger at companion `48ce162` is covered as follows:

1. **The 86 unchanged rows** passed at companion `0eb9403` in the split
   review (`../2026-11-10-lean-ledger-codex-split/JOIN.md`): component M read
   the main TeX completely (1–7706, gapless) and S read the 17 module files
   completely, both at high confidence. `ledger-delta-0eb9403-to-48ce162.json`
   (script) shows these 86 rows and all other module paragraphs are
   byte-identical between `0eb9403` and `48ce162`. The manuscript moved
   669ccc9 → ba01d98 with every cited label present and the mathematics of
   every cited statement and proof unchanged (script check, recorded in the
   companion's `provenance/manuscript-anchor.json`).
2. **Everything that changed** (the two repaired rows, the two module
   paragraphs, the index, the totals) is covered by this **accepted** receipt
   at `48ce162` over `ba01d98`.
3. The opening revision sentence of the ledger changed with the re-anchor; it
   states the supervisor's script check and is outside every review's scope.

**Status:** every one of the 88 rows has a high-confidence, complete-reading
Codex review with no open finding, and every repair since then has an
accepted receipt. This is a documented conjunction, not a `compose`
certificate (compose takes only Claude receipts; see the split JOIN.md).
Only the final narrow review is itself an accepted receipt. **Whether this
combination satisfies the project's correspondence acceptance rule is Le's
decision.** It certifies statement-to-manuscript correspondence of the ledger
as reviewed by an AI. It is not human verification (work package A1 remains
recommended), and it does not verify the analytic inputs outside Lean.
