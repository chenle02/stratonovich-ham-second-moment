# Adjudication: wave-L4 correspondence review of the MaskedModulation section

- **Object:** the "MaskedModulation (whole result)" section of the Lean companion ledger, its index rows, coverage rows and cross-references, at companion `efec88b`, manuscript `3920258`. Reviewer: Codex GPT-6.1-Sol, effort high, read-only, `CODEX_HOME` workaround; frozen packet; contract-check (schema), dry run and contract-check on the dispatched prompt clean.
- **Result:** valid, **FAIL**, confidence high; 61 checks {'PASS': 59, 'FAIL': 1, 'PASS_WITH_NOTES': 1}; findings {fatal: 0, major: 1, minor: 1}.
- **Adjudication:** every finding checked by the integrator against the Lean source and the TeX at `3920258` (the file:line evidence quoted in each finding was confirmed); all accepted, none rejected; all documentation (ledger rows, index, wording); no Lean statement change. Repairs at companion `7afcd23`.

| ID | Sev | Disposition | Finding (as reported) | Repair (companion `7afcd23`) |
|---|---|---|---|---|
| W1 | major | **ACCEPTED** | W1 — LEDGER-INDEX is incomplete. candidate/statement-ledger.md:130-238 indexes only 17 distinct target declarations, although :1465-1521 contains 57. Missing are all nine TimeSchur auxiliaries at :1473-1481 and all 31 MaskedModulation auxiliaries at :1489,1492-1521. For example, Lean TimeSchur.lean:236-237 defines 'integrand', and MaskedModulation.lean:332-338 states the shift theorem with 'phase ω δ = -1'; neither is indexed. TeX integrated_covariance_foundation.tex:331-342 instead says 'integrate the exponential by parts', supporting the ledger's 'no direct label' classification rather than … | applied as the finding's exact fix |
| W2 | minor | **ACCEPTED** | W2 — CROSS-REFERENCES wording: candidate/statement-ledger.md:1742 says the modulation bound 'is not proved; it is the supplied hypothesis hmod'. That is true locally for MaskedTrigProducts.lean:349-350, but MaskedModulation.lean:1081-1094 now proves the integral bound corresponding to TeX integrated_covariance_foundation.tex:303-308, including 'C0(a)=16/(1-a)'. Optional clarification: say 'not proved in MaskedTrigProducts; the integral bound is proved in MaskedModulation and transferred by the bridged wrapper'. | applied as the finding's exact fix |

Next: narrow confirmation review of the wave-L4 repairs (`2026-11-11-lean-wave-l4-confirm`).
