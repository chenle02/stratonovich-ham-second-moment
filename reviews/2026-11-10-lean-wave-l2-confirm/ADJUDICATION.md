# Adjudication: narrow confirmation review of the wave-L2 repairs

- **Object:** the repairs at companion `17f0490` (manuscript `ba01d98`) of
  the six findings of the three wave-L2 reviews at `c4e0620`
  (`2026-11-10-lean-wave-l2-{temporal-equilibrium,radius-mean-anchor,
  masked-trig-products}`), a rescan of every labelled TemporalEquilibrium
  row for further route-auxiliary mislabels, the totals, and regressions.
  Reviewer: Codex GPT-6.1-Sol, effort high, read-only, `CODEX_HOME`
  workaround; frozen packet with the three prior reports; contract-check and
  dry run clean (a first dry run was blocked by a glob in the contract,
  `prior/*-report.json`, read as a file name; the contract then named the
  files).
- **Result:** valid, **PASS_WITH_NOTES**, confidence high, accepted; 11
  checks: 9 PASS, 2 PASS_WITH_NOTES; 0 fatal, 0 major, 1 minor; no required
  repairs. W1, W2, W3 (TemporalEquilibrium), W1, W2 (RadiusMeanAnchor) and
  W1 (MaskedTrigProducts) are confirmed resolved; the rescan found no other
  mislabelled row; totals 223 (142/81) confirmed.

| ID | Sev | Disposition | Verified | Repair (companion) |
|---|---|---|---|---|
| C1 | minor | **ACCEPTED** | the general reflection and splitting `lintegral` identities (Lean l.147-148, 160-161) take arbitrary `F` and do not assert finiteness; the paragraph's "auxiliary lintegral identities establish finite values" read too broadly | wording restricted to the evaluated auxiliary integrals (`79afdde`) |

Afterwards: lean-pkg receipt at `79afdde` (fresh build, 0 sorry, standard
axioms, 223 claim axioms; `--memory-max 12G`, peak 6.5 GiB), package
re-gated verified-private `9033c4e -> 79afdde`, claims synced at `a2e9625`.
