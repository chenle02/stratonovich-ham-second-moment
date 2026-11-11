# Review-run counts for Appendix E

`count_reviews.py` counts AI review runs from `reviews/` only (loose files and
the archives inside it, read in memory), so anyone with the repository can
rebuild the numbers:

    python3 scripts/ai-statistics/reviews/count_reviews.py . scripts/ai-statistics/reviews

It takes about 45 s and 4.3 GB of memory. Outputs: `review-stats.json`
(aggregates, every run, follow-ups, folder categories; `generated_from_commit`
names the commit counted), `runs.tsv` (one row per run) and `unclassified.txt`
(folders and records not counted, with the reason).
File and folder names in all three outputs are written as they appear in
the public release, whose filter renames the private hub host to `hub`.

Definitions (from the script; first written by a read-only subagent,
2026-11-10): a run is one dispatch of one review task to one reviewer model,
with or without a report. Copies of the same run merge on the session
identifier. Compactions, probes, preflight-only sessions, dry runs and
preflight refusals are not runs; same-session corrections and resumes are
counted separately as follow-ups.

Result at b80217b: 498 runs (Claude 244, DeepSeek 143, Kimi 93, GPT/Codex 18)
and 40 follow-ups. Cross-check: of 221 distinct review sessions in the local
receipt store on the worker machine, 216 are counted here; the other 5 review
documents outside this book.

Caution on "accepted": the receipt's `accepted` field exists only for Claude
and GPT/Codex runs. For DeepSeek and Kimi the script's `accepted_effective`
column is inferred (completed, PASS or PASS_WITH_NOTES, HIGH confidence), and
a spot check found a Kimi page check counted this way whose own record says
`accepted: false` (accepted as image evidence only). The appendix therefore
reports "met the bar" (PASS or PASS_WITH_NOTES at HIGH) for every family and
recorded acceptance only where a receipt records it.

Known limits: Kimi tokens and per-run time are not recorded; DeepSeek hours
are an undercount (some runs record only their last dispatch); 113 run dates
come from folder names; 156 folders with report-like files but no run record
were sampled (5), not checked one by one.
