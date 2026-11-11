# Adjudication: narrow confirmation review of the wave-L4 repairs

- **Object:** the repairs at companion `7afcd23` (manuscript `3920258`) of
  the 8 findings of the four wave-L4 reviews at `efec88b`
  (`2026-11-11-lean-wave-l4-{masked-spectral-growth,masked-modulation,
  frequency-row,occupation-kernel-row}`), a rescan of every row of the four
  sections, the totals and table format, and regressions. Reviewer: Codex
  GPT-6.1-Sol, effort high, read-only, `CODEX_HOME` workaround; frozen
  packet with the four prior reports and thirteen Lean modules;
  contract-check (schema), dry run and contract-check on the dispatched
  prompt clean (a first dry run was blocked by a contract line naming a
  file absent from the packet; the line was removed).
- **Result:** valid, **PASS_WITH_NOTES**, confidence high, accepted; 14
  checks: 13 PASS, 1 PASS_WITH_NOTES; 0 fatal, 0 major, 1 minor; no
  required repairs. All 8 prior findings confirmed resolved; the four
  rescans found nothing further; totals 724 (419 labelled, 305 not) and the
  four-cell table format confirmed.

| ID | Sev | Disposition | Verified | Repair (companion) |
|---|---|---|---|---|
| C1 | minor | **ACCEPTED** | ledger index row 240 (added in the repair) repeated the six OccupationKernelRow helpers already listed in row 236; checked by script: all six names present in 236 | duplicate row deleted (`ac6f767`) |

Afterwards: the wave-L4 correspondence review sequence (four reviews,
repairs at `7afcd23`, this confirmation, C1 at `ac6f767`) is complete; the
gate is Le's decision.
