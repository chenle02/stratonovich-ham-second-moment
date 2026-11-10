# Documented join of the split ledger review (not a compose certificate)

**Why a documented join.** `subscription-review-cli compose` accepts only
Claude Opus 5.5 attempts with a hash-bound read ledger
(`review_report_contract.validate_correspondence_receipt`). The ledger under
review was written by Claude, and the project requires a reviewer from a
different family, so Le chose (2026-11-10) two Codex GPT-6.1-Sol components and
this documented join. It is not a `compose` certificate and carries no
machine-verified read ledger: reading coverage below is the reviewer's own
report, checked for gaps by the supervisor.

Machine-computed facts: `join-facts.json` (script over both receipts, reports
and `row-partition.json`).

## Candidate and partition

| Fact | Value |
|---|---|
| Candidate | companion `0eb9403dfb93cc223dbeb1571aa9d96cf0a157b8`, manuscript `669ccc9b07241ae94f365f4a2e17c04da66870ca` |
| Same `source_revision` in both receipts | yes |
| Row partition (`row-partition.json`) | M: 54 rows (49 no-label + 5 whose label is in the main TeX); S: 34 rows (labels in the 17 module files) |
| Disjoint | yes |
| Union equals all 88 ledger rows | yes |
| Each report's checks equal its assigned rows, in order | yes (S adds LEDGER-INDEX, LEDGER-TOTALS, LEDGER-SCOPE) |
| Ran concurrently | M 14:35:32–14:46:01 UTC, S 14:35:32–14:42:40 UTC |

## Components

| | M (main file) | S (modules) |
|---|---|---|
| Model / effort | gpt-6.1-sol / high | gpt-6.1-sol / high |
| Status | review-complete | review-complete |
| Inputs unchanged | yes | yes |
| Required reading | main TeX lines 1–7706 in 20 consecutive 400-line chunks, **gapless** (supervisor-checked); other TeX searched with matches read in context, as contracted | all 17 module files **complete** in consecutive ranges; main TeX only at referenced passages, as contracted |
| Confidence | high | high |
| Checks | 54: 53 PASS, 1 FAIL | 37: 35 PASS, 1 PARTIAL, 1 FAIL |
| Findings | 1 fatal (M1) | 1 fatal (S1) |
| Verdict / accepted | FAIL / false | FAIL / false |

## Joined result

- Coverage: for the first time every ledger row was reviewed under complete
  required reading at high confidence.
- 86 of 88 rows passed. The two failures (M1 `LocalFlow.noise_order`, S1
  `DirectEvent.kappa_gt_one`) and the LEDGER-SCOPE PARTIAL (the same
  `kappa_gt_one` prose) were accepted and repaired at companion `435fdb0`
  (see `ADJUDICATION.md`). LEDGER-INDEX and LEDGER-TOTALS passed.
- **The correspondence gate is NOT closed by this join.** Neither component
  receipt is accepted (each FAIL, correctly), and the repaired rows have not
  been re-reviewed.

## What would close it

A narrow successor confirmation of `435fdb0` covering the changed rows
(`DirectEvent.kappa_gt_one`, `LocalFlow.noise_order`, the DirectEvent and
LocalFlow module paragraphs, the index and totals), plus an accepted receipt;
the other 86 rows are unchanged from 0eb9403, where they passed under
complete reading. Whether that combination satisfies the project's
acceptance rule is Le's decision. A human statement read (work package A1)
remains recommended.
