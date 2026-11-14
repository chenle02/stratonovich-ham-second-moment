# Dated ledger correction, 2026-11-14

This is an additive correction to the [unchanged v2 snapshot](../../run-ledger.json), internally committed at3422eca5. It does not replace or edit that historical file. The [v3 ledger](run-ledger-v3.json) retains the same29 process records, scientific outcomes, reported token objects/lists and numeric cost fields. It is still only the instrumented closeout subset of the repository-wide mathematics experiment, not a lifetime census or a whole-book acceptance claim.

[CORRECTIONS.json](CORRECTIONS.json) records the exact changes:

- Actual native assistant metadata and a matching public final establish `deepseek-v4-pro` for P1-deepseek, P1-cold and P2-cold. The [committed identity evidence](../../report-supplement-v1/PANEL-MODEL-EVIDENCE.json) supplies the source. P2-deepseek remains unknown; no requested-model fallback is used.
- The prior numerical-eligibility rule unnecessarily excluded four provider attempts with reported usage merely because their actual model was unknown. V3 includes reported figures under “Model not recorded” when identity remains unknown. It does not impute a model or any missing figure.
- Numerical aggregation has18 records with actual reported usage. Denominator eligibility separately retains all19 original provider-attempt records, including the running record with no reported usage, so missing data can be shown honestly as n-of-N rather than silently dropped or filled with zero. Group by actual model **and** `token_format_signature`; the running missing-format record must remain a visible missing-data category.
- Derived recoveries, parser refusals, preflights and audit addenda remain excluded. Both format continuations have `usage_nonoverlap_verified: false`; their accounting is not added to parents. No recovery or continuation is another independent vote.
- The four historical panel token objects are explicitly header/final-step usage, not verified session totals. Their raw field structures are unchanged and must not be merged with a different accounting format as lifetime spending.

Every row still has `WHOLE_BOOK_ACCEPTED: false`. Costs retain their reported numeric values and `cost_currency: null`; currency was not established by an explicit checked receipt. Do not relabel them USD or estimate missing currency/tokens. `provider_calls: null` means the exact count is not recorded, not zero.

The original provider outcomes remain anchored to v2's `snapshot_utc`; this update does not pretend to refresh a live review. `correction_recorded_utc` dates only these metadata corrections. `publication_state_as_of_correction` distinguishes recorded internal commits from an unverified filtered external release. The former DRAFT_NOT_RELEASED value remains preserved in the original snapshot; a historical snapshot label is not a current-release control switch.

This correction requires a new Agent16 exact-file filter approval before commit. Its contents are data/provenance only; no new raw provider report, private reasoning, primary-source attachment or held criticism is added. Appendix E belongs to Agent24 and should regenerate only from the eventual committed correction after approval.
