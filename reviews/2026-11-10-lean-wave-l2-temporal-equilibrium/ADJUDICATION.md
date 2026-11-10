# Adjudication: correspondence review of the TemporalEquilibrium rows (wave L2)

- **Object:** the "TemporalEquilibrium (whole result)" section (43 rows),
  its index rows, the coverage rows for `L:equilibrium-gamma-beta` and
  `L:temporal-equilibrium`, and the cross-references to it. Reviewer: Codex GPT-6.1-Sol, effort high, read-only sandbox, `CODEX_HOME`
  workaround; frozen packet (one Lean module, ledger, claims, coverage, all
  manuscript inputs at `ba01d98`), contract-check (schema) and dry run clean,
  contract-check on the dispatched prompt clean. Object: companion `c4e0620`.
- **Required reading:** Lean module, `integrated_temporal_equilibrium.tex`
  (1-90), coverage reported complete; ledger and claims complete for the
  required sections.
- **Result:** valid, **FAIL**, confidence high; 47 checks: 44 PASS, 1
  PASS_WITH_NOTES, 2 FAIL; 0 fatal, 2 major, 1 minor; 2 required repairs.
  Both wrappers (`gamma_beta_paper`, `temporal_equilibrium_paper`) and
  both same-assumptions coverage rows passed.

| ID | Sev | Disposition | Verified | Repair (companion) |
|---|---|---|---|---|
| W1 | major | **ACCEPTED** | `lintegral_affine_beta` is an auxiliary of the Lean (Möbius) proof route; the TeX proof (l.56-64) keeps the factor `(1-su)^(-r)` and never states the general affine Beta integral | row relabelled "no direct label (auxiliary to the Lean proof route)", index moved (`17f0490`) |
| W2 | major | **ACCEPTED** | `lintegral_mobius` computes a convolution with exponent `-2r` that the TeX series proof (l.56-70) does not use | as W1 (`17f0490`) |
| W3 | minor | **ACCEPTED** | "every integral conclusion includes integrability" was too broad: the auxiliary `lintegral` identities state finite values instead | sentence restricted to the manuscript's integral evaluations (`17f0490`) |

Afterwards: totals 223 (142 labelled, 81 unlabelled). The gate is not
closed by this receipt; a narrow confirmation review of the repairs at
`17f0490` follows (`2026-11-10-lean-wave-l2-confirm`).
