# Scripts behind Appendix E, "The AI work in numbers"

Every number, table row and the timeline figure in Appendix E are generated
from the files in this folder and the repository's git history.

| Path | What it is |
|---|---|
| `make_appendix.py` | Writes `notes/ai-statistics-data.tex` (macros, table rows, figure). |
| `milestones.json` | The project's milestones: tag name, recorded date, UTC time, original commit, label and source record. At release the same names become annotated tags in the public repository, through the commit map. |
| `infrastructure.json` | Start dates of the parts of the system that are older than the book (bibliography, paper library, source collection, wiki, skills), each with the first commit that is the evidence. Used for the paragraph before the timeline figure. |
| `commits-per-day.json` | Commits per UTC day in the working repository up to the counted commit (written by `make_appendix.py`). |
| `reviews/` | `count_reviews.py` counts review runs from `reviews/`; outputs `runs.tsv`, `review-stats.json`, `unclassified.txt`. |
| `tokens/` | `token_totals.py` reads local model logs; `token-totals.json` is the recorded snapshot. |
| `no-go/` | `nogo-counts.json`: kind and status of each recorded no-go (see its README). |
| `timeline.json`, `commits-per-day-timeline.json` | The commit up to which commits per day are counted for the opening numbers and the line in the figure, and the counts. This can be later than the commit of the review census. |
| `selection.json` | Names, by path and SHA-256, the dated inputs that `make_appendix.py` must read: the token and no-go snapshots, `timeline.json` with its counts, and the later-attempts snapshot. The generator stops if one is missing or differs; it has no fallback, and it does not replace a missing usage field by zero. |
| `reviews/later-attempts-2026-11-15.json` | Per-day counts of review attempts recovered from retained records for November 12 to 15, with their limits. Counts only, no identifiers. These are the grey bars of the figure; they are not runs of the census and are not added to it. |

Rebuild from the repository root:

    python3 scripts/ai-statistics/reviews/count_reviews.py . scripts/ai-statistics/reviews
    python3 scripts/ai-statistics/make_appendix.py
    latexmk -pdf -outdir=notes notes/notes_stratonovich_ham_second_moment.tex

`count_reviews.py` takes about 45 s and 4.3 GB of memory.
`token_totals.py` only works on the machine that holds the model logs
(set `CODEX_SESSIONS` and `OPENCODE_DB` if they are not in the default
places); everyone else uses the committed snapshots. Set `TOKEN_TOTALS_OUT`
to write a new dated snapshot (for example `token-totals-2026-11-15.json`)
without overwriting an earlier one, and then name it in `selection.json`.

## Two dates

The review census (`reviews/`) ends at the commit named in
`reviews/review-stats.json`; its last day is November 12, 2026, and the bars
of the figure stop there. The commits per day, the milestones, the token
totals and the no-go record are dated snapshots that can be later
(`timeline.json`, `selection.json`). The first snapshots
(`commits-per-day.json`, `tokens/token-totals.json` of November 11 and
`no-go/nogo-counts.json` of November 10) stay in the repository unchanged.
The snapshots of November 15 (`tokens/token-totals-2026-11-15.json`,
`no-go/nogo-counts-2026-11-15.json`) also stay. The current ones are dated
November 16, 2026: the token snapshot was taken again from the same machine's
logs, the commits are counted at the commit named in `timeline.json`, and the
no-go record was re-affirmed without change. The token snapshot of November 16
contains the recorded usage of that day's re-read calls, so the figure in the
re-read section is part of it and is not added to it.
Reviews done after the census are not added to its bars or its table. The
figure shows a separate grey count of recovered attempts, beside the census bar
on a day that has both, and the closeout ledger described below reports the
closeout reviews. In the token snapshot, the Claude Code field `api_calls`
is a legacy name: it counts logged assistant usage records, including
synthetic ones (which carry no tokens), not verified API calls.

## Every number and its source

| Number in Appendix E | Source |
|---|---|
| days, first and last day, commits (UTC days) | `git log` up to the commit named in `timeline.json`, `TZ=UTC`, recorded in `commits-per-day-timeline.json` (the first snapshot, counted at the commit named in `reviews/review-stats.json`, stays in `commits-per-day.json`). The public repository's history is filtered (commit ids rewritten, private-only commits dropped), so there the script reads this file. |
| review folders, folders with a run, runs, follow-ups, runs dated by folder name | `reviews/review-stats.json`, `reviews/runs.tsv` |
| review table: runs, completed, not completed, met the bar, FAIL, MEDIUM, hours and their coverage | `reviews/runs.tsv` (rules in `make_appendix.py`) |
| GPT FAIL count | `reviews/runs.tsv`, family GPT/Codex |
| worker sessions and tokens; Claude calls and tokens; DeepSeek sessions, tokens and cost; snapshot time; worker/DeepSeek ratio | the token snapshot named in `selection.json` |
| no-go totals by kind and status | the no-go snapshot named in `selection.json`; the first-snapshot counts quoted in the text come from `no-go/nogo-counts.json` |
| timeline figure | `reviews/runs.tsv` (bars), `git log` (line), `milestones.json` (numbered markers and key) |

Definitions: a *run* is one review task sent to one reviewer model; *met the
bar* is a completed run graded PASS or PASS WITH NOTES at HIGH confidence.
Meeting the bar is not acceptance: recorded acceptance exists only for the
Claude and GPT runs (see `reviews/README.md`).

## Final review synchronization gate

Appendix E's historical census remains separate from its later closeout ledger. The default selected committed ledger is now `experiment/ledger-updates/2026-11-15-cold-closeout/run-ledger-v4.json`. That additive snapshot preserves the29 historical rows and adds six later cold checks. `python3 scripts/ai-statistics/make_appendix.py --check` verifies generated data without writing files; `--ledger PATH` selects a different explicitly committed snapshot. Token sums are separated by actual model, original field signature and accounting scope; reported costs are also separated by currency. Partial final-step objects never certify whole-run usage.

Le required this consistency work as a final publishing gate on 2026-11-15. Run `python3 scripts/ai-statistics/check_review_sync.py` to verify the captured snapshot. The final release owner must run the release mode against a detached checkout of the exact release SHA with an external attestation bound to that SHA and the REVIEW-SYNC manifest hash, after reconciling all final review decisions, including private evidence. Later reviews, decisions or artifact changes require renewed synchronization. The check does not grant scientific acceptance or public release; release-wrapper integration and rehearsal belong to its owner.


## Additive chronology and policy evidence

Step B selects review_evidence and review_inventory explicitly in
selection.json. The generator verifies their hashes, original-ledger binding,
118/25/93/4 inventory counts, clock kinds, day bounds and unchanged-grade policy
before producing the chronology macros. The original 35-row ledger is not
rewritten. The inventory does not enter completion, met-bar, token or cost sums;
the historical quality table remains tied to its own census.

The release consistency checker now requires the archival combined edition as
well as the book and reader. Every selected input must be present, match its
declared hash and be included in the final review-sync seal. The source code
change belongs to B; the manifest-only reseal remains D, after combined
regeneration and all authorized source changes. No final owner attestation or
scientific/release acceptance is manufactured by snapshot checks.
