# An experiment in a new way of doing mathematics

The experiment is the way of doing mathematics described in the [Preface](../notes/preface.tex). The dataset is the **entire released repository and its retained public history**: how the problem and goals were chosen, proof iterations, successful and failed approaches, numbered no-gos, human decisions, AI drafting, source verification, independent criticism and responses, and the precise scope of Lean checks. The experiment is not merely a record of publication closeout, and a favorable review is not proof of mathematical correctness.

Start with the [repository guide](../README.md), the Preface, and the [public-history index](history-index/README.md). The latter is presently a labelled placeholder; the actual all-history inventory will be generated only from the release-day filtered checkout. Disclosure restrictions and removals must remain explicit rather than being mistaken for absence of failed work.

## Current instrumented subset: publication closeout

The [machine-readable ledger](run-ledger.json) is **one bounded subset**, not a lifetime experiment census. It currently contains 29 process records: all 11 entries in the captured closeout registry; eight role attempts from two scoped Chapter12 panels; two same-session format continuations; three canonical derived-recovery events; one refused recovery; one delivery-audit addendum; and three native preflights. [Completeness and exclusions](COMPLETENESS.md) records the boundary.

Each row has an explicit outcome: `accepted-at-scope`, `not-accepted`, `invalid`, `refused`, `recovered`, `preflight`, `continuation`, or `timeout`. `not-accepted` can mean pending or no established gate acceptance; it is not automatically a negative mathematical verdict. A recovered representation is not a new independent vote, and a recovered report can still fail its confidence threshold. Every row has `WHOLE_BOOK_ACCEPTED: false`.

The files in [reports/](reports/) are **author-written process summaries**. The separate [report supplement](report-supplement-v1/README.md) retains four unchanged provider final responses and one derived B002 recovery. Its [dated availability map](report-supplement-v1/AVAILABILITY-2026-11-14.json) identifies the files, hashes, scopes and recorded approval. A provider final response is distinct from private model reasoning; retaining it at an exportable path does not mean the repository has been released publicly. Complete native evidence and unsuccessful attempts remain preserved privately. Private reasoning, credentials and runtime details, third-party source texts and images, held source criticisms and private correspondence remain under their disclosure rules.

## Telemetry for later analysis

Only verified **actual model identifiers and families** are reported; unknown actual identities are `null`, without requested-model fallback. Stable record IDs may retain an old purpose-role label; only `actual_model` and `actual_family` identify the model. Token objects and per-request lists retain their reported field names and formats. Missing values are `null`; no token totals, costs, model identities or estimates are fabricated. Numeric reasoning-token counts are telemetry, not reasoning content.

Appendix E may aggregate only actual reported fields, grouped by **actual model and original field format**, with the contributing count `n` out of eligible count `N` stated. Do not mix incompatible token formats or accounting levels. Derived recoveries, preflights and audit addenda are excluded; continuation usage must not be added to parent usage until nonoverlap is verified. `cost_currency` is populated only from an explicit recorded receipt currency; otherwise it is `null` and labelled “currency not recorded.” A numeric cost without a recorded currency is not a dollar estimate.

Registry, receipt and result snapshot hashes preserve provenance. Each ledger records what was known at its stated date; a historical “running” or “pending” field is not a current process-status claim. Later records do not overwrite those snapshots. The [C003 correction](ledger-updates/2026-11-14-c003-provenance/CORRECTIONS.json) distinguishes the raw B001 response from its parsed serialization. The supplement availability map records which full report versions are now retained, separately from the old ledger flags. No lifetime totals or whole-book acceptance are inferred from this subset.

## Release boundary and history indexing

The existing ledger and supplement artifacts were committed internally after their exact-file checks. That is distinct from an external public release, which remains held. New exports or further changes still require the applicable release approval; source, correspondence and other disclosure holds remain in force. Source snapshot IDs are provenance strings, not links into unfiltered private history.

The [inventory generator](tools/index_filtered_reviews.py) scans every reachable tree in an approved filtered checkout, recording each retained review/report/telemetry path/blob version and its SHA256. It generates relative current-file links, identifies historical versions by Git object IDs, and does not re-export content or turn artifacts into review votes. [Synthetic tests](tools/test_index_filtered_reviews.py) check historical versions and rejection of private/runtime paths; they are not a release audit.

After the release-day filtered checkout and filter receipt exist, the coordinator can run:

```sh
python experiment/tools/index_filtered_reviews.py \
  --filtered-root /path/to/filtered-checkout \
  --output /path/to/filtered-checkout/experiment/history-index \
  --filter-receipt /path/to/approved-filter-receipt.json \
  --ack-filtered
```

These are illustrative placeholders, not private host paths. The generated files require their own exact release/filter review. No absent historical data is silently counted as zero.
