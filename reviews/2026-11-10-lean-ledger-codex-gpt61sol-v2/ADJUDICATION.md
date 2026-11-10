# Adjudication: successor Codex GPT-6.1-Sol review of the Lean statement ledger

- **Object:** `docs/statement-ledger.md`, companion commit
  `c9e28af1b12826c66849a67373890f81e3943485` (after the first Codex repair),
  against manuscript `669ccc9b07241ae94f365f4a2e17c04da66870ca`.
- **Reviewer:** `subscription-review-cli run codex --model gpt-6.1-sol --effort
  high`; receipt `model_actual` gpt-6.1-sol, `effort_actual` high. Same
  read-only sandbox and `CODEX_HOME` workaround as the first Codex run
  (`codex-home-listing.txt`). No earlier report in the packet.
- **Contract:** the first Codex contract with the commit id and the two
  hard-coded totals updated to the repaired values (36 labelled, 52
  unlabelled) so the reviewer would not check stale numbers
  (`contract-diff-from-v1.txt`). `contract-check` observable on the contract
  and the dispatched prompt; dry run clean.
- **Frozen packet:** `packet.tar.gz` (68 files + `PROVENANCE.json`);
  `candidate_hashes_unchanged` true. Evidence scanned for auth tokens: none.

## Transport, validity, acceptance

| Layer | Result |
|---|---|
| Transport | completed, exit 0, 675 s |
| Report validity | valid (`review-complete`) |
| Scientific verdict | **FAIL**, confidence **medium**: 88 checks (84 PASS, 3 FAIL, 1 INCONCLUSIVE); 2 fatal, 2 required repairs |
| Confidence reason (reviewer) | some manuscript files read only partially; keyword searches there; "not an exhaustive list of possible ledger defects" |
| Acceptance | not accepted (`blocking-finding`) |

## Findings (adjudicator: Claude Opus 5.5, #22)

| ID | Sev | Disposition | Evidence checked at 669ccc9 / Lean | Change (companion 1a8c419) |
|---|---|---|---|---|
| K1 | FATAL | **ACCEPTED** | `L:masked-continuous-wave` (`integrated_covariance_foundation.tex` ~l.379–382) defines `b_r(t) = <r> sin(rt)/r`; the first repair had set `b_r = sp/p`, dropping `<r>`. `E:variance-normalized-kernel` follows from `v_z`, `G_w` with individual `<eta>^{-1/2}`, `<xi>^{-1/2}` factors (`integrated_wave_variance.tex` l.317–326). Lean `backward`/`forward` are `S(-t)`, `S(t)` in unweighted coordinates, so `full_interaction` is the unweighted product. This was an error in the adjudicator's own previous repair. | Prose and row: unweighted product `S(-t)B(b)S(t)` supporting `E:variance-physical-adjoint`; the Bessel-weighted coordinate change and the weight that give the normalized kernel are outside Lean. Mapping to `P:actual-wave-form` kept. |
| K2 | FATAL | **ACCEPTED (overrides the 2026-11-09 manuscript-owner triage)** | Proof of `P:radius-mean-anchor` (`integrated_radius_anchor.tex` l.323–325): "`Q(1-a) > 2d`. Dividing by `2Q` gives `e_anchor > 0`", then substitutes `R_delta <= 3/delta` into the `g_delta R^{d/Q}` bound. At `d = 2` with Lean `p := Q`: `box_margin` (`4/(1-a) < p ⟹ 0 < (1-a)/2 - 2/p`) is that division, `box_scale` the power bookkeeping. The ledger's "a different fact, not an instance of it" was false. The manuscript owner had ruled to keep these rows unmapped as a d=2 numerical coincidence; under the ledger's own criterion (a computation that appears inside a labelled proof) the d=2 case is a genuine instance, and the ledger now says exactly that and no more. | Both rows → `P:radius-mean-anchor (case d = 2, p = Q)`; d = 1, 3 and the general margin `(1-a)/2 - d/Q` stated as not checked; Lean `p` distinguished from the manuscript's averaging `p`; coverage row added with `conclusion: special-case` |
| INC | — | **Keep no label; note added** | `L:masked-trig-products` expands cosine products into four complex exponential modes; the real identity `cos x cos y = (cos(x-y)+cos(x+y))/2` is not displayed. Equivalent, not the same computation. | Row note names the label and the exponential expansion |

Counts: 38 labelled, 50 unlabelled (script: index equals per-module tables;
all 54 cited labels exist at 669ccc9). coverage.yaml: 25 rows (21
inputs-supplied, 4 outside). Companion `1a8c419` is a docs-only descendant of
`38d16163ab89` (gate check confirms).

## Status

- Gate **not closed**: this review is FAIL at medium confidence; both defects
  are repaired. A further successor review of `1a8c419`, with complete reading
  of the cited manuscript files (not keyword search alone), is needed for an
  accepted receipt.
- Pattern across the five ledger reviews: each new reviewer has found a real
  mapping or fidelity defect the earlier ones passed (DimensionalMatrix,
  HermiteWord, the `<r>` factor, the box rows). A human statement read
  (work package A1) is strongly indicated in addition to the next AI pass.
- Downstream: the work-package board needs a Group B row for
  `P:radius-mean-anchor` (new inputs-supplied row); the manuscript owner's
  target triage should be updated for the box rows.
