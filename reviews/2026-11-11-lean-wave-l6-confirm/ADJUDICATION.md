# Adjudication: confirmation review of the wave-L6 repairs

- **Object:** the repairs at companion `4486c57` (manuscript `975feb3`) of the
  16 findings of the eight wave-L6 reviews at `250cf39`
  (`2026-11-11-lean-wave-l6-*`), a rescan of every row of the fourteen
  sections, the totals and the whole-ledger index, and regressions.
  Reviewer: Codex GPT-6.1-Sol, effort high, read-only, `CODEX_HOME`
  workaround; frozen packet with the eight prior reports, every library
  module, claims.yaml, coverage.yaml, docs/coverage-scope-tex.yaml and all 78
  TeX inputs at `975feb3`; contract-check, dry run and contract-check on the
  dispatched prompt clean.
- **Result:** valid, **FAIL**, confidence high; 26 checks: 25 PASS, 1 FAIL
  (a-WaveGreen-W3); 0 fatal, 0 major, 1 minor; one required repair. Every
  other prior finding confirmed resolved; the eight rescans, the totals
  (1463; 737 labelled, 726 unlabelled), the whole-ledger index and the
  regression check pass.

| ID | Sev | Disposition | Verified | Repair (companion) |
|---|---|---|---|---|
| C1 | minor | **ACCEPTED** | `DampedNormsHomog.lean:123-126` (the `GreenMass` doc comment) still said the wave Green measures are ones "which this package does not define", although `WaveGreen` defines them and `waveGreen_greenMass` discharges `GreenMass`; the same stale package-wide claim was found in `DampedNorms.lean:18-19` and fixed with it | `4b09ee6` (branch `l6-confirm-fix`; comment-only, comment-stripped sources identical) |

Because this confirmation is not a clean PASS, Le's conditional acceptance
of the L6 gate does not apply to it. Next: merge `4b09ee6`, rerun the
comparator generators and CheckFidelity, receipts of both tiers at the new
commit, regate, a narrow re-confirmation of C1, and Le's decision.
