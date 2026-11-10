# Adjudication: correspondence review of the wave L1 whole-result rows

- **Object:** the five "whole result" ledger sections (19 rows), index, totals,
  scope prose and five coverage rows at companion `9d1c7c4`, manuscript
  `ba01d98`. Reviewer: Codex GPT-6.1-Sol, effort high, read-only sandbox,
  `CODEX_HOME` workaround; frozen packet (58 files), contract-check and dry run
  clean. Required reading (5 Lean modules, ledger, claims, coverage, four cited
  TeX modules, main TeX 150–200) reported complete.
- **Result:** valid, **FAIL**, confidence high; 28 checks: 15 PASS, 13 FAIL;
  4 fatal, 1 major; 3 required repairs. No proof or mathematics defect: every
  failure concerns the claim "same assumptions / complete".

| ID | Sev | Disposition | Verified | Repair (companion) |
|---|---|---|---|---|
| W1 | fatal | **ACCEPTED** | GramScalarAlgebra drops completeness of H and the section's `C_ij >= 0` (`integrated_positive_gram.tex` l.4–6) | wrapper `gram_scalar_algebra_paper` with exactly those hypotheses (`20f86b6`); coverage cites it (`828da24`) |
| W2 | fatal | **ACCEPTED** | KappaRange/DriverParameters assume only the numerical part of `H:homog` (main TeX l.169–186) | described as parameter-only generalizations in ledger, coverage note, README (`828da24`); the covariance part of H:homog is not modelled (a surrogate would be unfaithful) |
| W3 | fatal | **ACCEPTED** | RayleighTail drops the section's `0 < δ < 1` (`integrated_gaussian_tubes.tex` l.8–9); helper allows `M >= 0`; head lemma drops ν<2 and the cutoff | wrapper `rayleigh_tail_paper` with the manuscript's hypotheses incl. δ<1 (`20f86b6`); rows describe the generalizations |
| W4 | fatal | **ACCEPTED** | the lemma's "In particular" application (l.463–464, 477–479) is not formalized | excepted wherever completeness is claimed (ledger scope, coverage summary, README, FORMALIZATION) |
| W5 | major | **ACCEPTED** | ledger row for `rayleigh_head_integrable` omitted `Measurable G` | row states it, and that ν<2 and the cutoff are not needed |

Afterwards: 109 declarations (61 labelled, 48 unlabelled), lean-pkg receipt and
gate verified-private at `828da24`, claims synced at `f510681`. A confirmation
review of the repaired rows at `f510681` was launched the same day.

Tooling note for lean-ops: lean-pkg coverage has no class for "proved under
weaker hypotheses than the paper"; generalizations are recorded with a `note`.
