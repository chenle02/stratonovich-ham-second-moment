# Adjudication: complete-reading Codex GPT-6.1-Sol review of the Lean ledger

- **Object:** `docs/statement-ledger.md`, companion commit
  `1a8c419de2195e0446a6d0dd0af41503f8161024`, against manuscript
  `669ccc9b07241ae94f365f4a2e17c04da66870ca`.
- **Reviewer:** `subscription-review-cli run codex --model gpt-6.1-sol --effort
  high`; receipt `model_actual` gpt-6.1-sol, `effort_actual` high; read-only
  sandbox, `CODEX_HOME` workaround as before (`codex-home-listing.txt`).
- **Contract:** the previous Codex contract with the commit id, totals (38/50)
  and a binding COMPLETE-READING section added (`contract-diff-from-v2.txt`):
  18 named manuscript files that contain every cited label must be read
  completely in consecutive ranges; all 50 no-label rows need searches over
  all files, including equivalent forms, with every match read in context;
  any gap makes affected rows INCONCLUSIVE and confidence below high.
  `contract-check` observable on contract and dispatched prompt; dry run clean.
- **Frozen packet:** `packet.tar.gz` (68 files + `PROVENANCE.json`);
  `candidate_hashes_unchanged` true; no auth tokens in the evidence.

## Transport, validity, coverage, acceptance

| Layer | Result |
|---|---|
| Transport | completed, exit 0, 612 s |
| Report validity | valid (`review-complete`) |
| Verdict | **FAIL**, confidence **medium**; 88 checks: 33 PASS, 1 FAIL, 54 INCONCLUSIVE; 1 fatal, 1 required repair |
| Source coverage vs the 18 required files | **17 complete** (every `integrated_*` file with a cited label, lines 1–end); **main file partial**: complete ranges 1–180, 1910–2170, 2480–2550, 2660–2735, 3890–3975, 4860–5360, 7230–7706 of 7,706 lines; gaps 181–1909, 2171–2479, 2551–2659, 2736–3889, 3976–4859, 5361–7229 stated by the reviewer |
| Consequence (as contracted) | 49 no-label rows and the 5 labelled rows whose labels sit in the main file (ClockFilter ×3, HermiteWord ×2) INCONCLUSIVE; the 33 labelled rows in fully read files PASS; no fidelity defect found in any of the 88 rows |
| Acceptance | not accepted (`blocking-finding`) |

## Findings (adjudicator: Claude Opus 5.5, #22)

| ID | Sev | Disposition | Evidence checked | Change (companion 0eb9403) |
|---|---|---|---|---|
| K1 | FATAL | **ACCEPTED (reverses the previous adjudication's "equivalent, not the same computation")** | `integrated_covariance_foundation.tex` l.347–375: the proof of `L:masked-trig-products` expands the two trigonometric factors into four complex exponential modes, frequencies `σr+τρ`, coefficients of absolute value 1/4. For the cosine-cosine case pairing conjugate modes gives exactly `PhaseResponse.lean:42-44` with x=rt, y=ρt. This is the same step in real form, the contract's own equivalent-form criterion, and the same special-case treatment already used for the box rows. | Row → `L:masked-trig-products` (cosine-cosine case, real form); module prose names the exception; complex form, sine cases and the bound stated as not checked; index; coverage row (`conclusion: special-case`) |

Counts: **39 labelled, 49 unlabelled** (script: index equals tables; 55 cited
labels exist at 669ccc9). coverage.yaml: 26 rows (22 inputs-supplied, 4
outside). Companion `0eb9403` is a docs-only descendant of `38d16163ab89`.

## Status and recommendation

- Gate **not closed**. The remaining obstacle is coverage, not a known
  defect: one reviewer pass cannot read the 7,706-line main file completely
  together with everything else.
- Recommended next review design: split by source, then compose
  (`subscription-review-cli compose` exists for split reviews):
  (1) a main-file pass that reads `notes_stratonovich_ham_second_moment.tex`
  completely, in chunks if needed, and decides the 49 no-label rows plus the
  5 main-file labelled rows; (2) reuse of this attempt's complete coverage of
  the 17 module files for the 33 PASS rows, or a fresh module-only pass.
  A human statement read (work package A1) remains recommended.
- Downstream: the board needs a Group B row for `L:masked-trig-products`
  (new inputs-supplied row); its level is the owner's decision.
