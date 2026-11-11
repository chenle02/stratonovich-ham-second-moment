# Scripts behind Appendix E, "The AI work in numbers"

Every number, table row and the timeline figure in Appendix E are generated
from the files in this folder and the repository's git history.

| Path | What it is |
|---|---|
| `make_appendix.py` | Writes `notes/ai-statistics-data.tex` (macros, table rows, figure). |
| `milestones.json` | The project's milestones: tag name, recorded date, UTC time, original commit, label and source record. At release the same names become annotated tags in the public repository, through the commit map. |
| `commits-per-day.json` | Commits per UTC day in the working repository up to the counted commit (written by `make_appendix.py`). |
| `reviews/` | `count_reviews.py` counts review runs from `reviews/`; outputs `runs.tsv`, `review-stats.json`, `unclassified.txt`. |
| `tokens/` | `token_totals.py` reads local model logs; `token-totals.json` is the recorded snapshot. |
| `no-go/` | `nogo-counts.json`: kind and status of each recorded no-go (see its README). |

Rebuild from the repository root:

    python3 scripts/ai-statistics/reviews/count_reviews.py . scripts/ai-statistics/reviews
    python3 scripts/ai-statistics/make_appendix.py
    latexmk -pdf -outdir=notes notes/notes_stratonovich_ham_second_moment.tex

`count_reviews.py` takes about 45 s and 4.3 GB of memory.
`token_totals.py` only works on the machine that holds the model logs
(set `CODEX_SESSIONS` and `OPENCODE_DB` if they are not in the default
places); everyone else uses the committed `token-totals.json`.

## Every number and its source

| Number in Appendix E | Source |
|---|---|
| days, first and last day, commits (UTC days) | `git log` up to the commit named in `reviews/review-stats.json`, `TZ=UTC`, recorded in `commits-per-day.json`. The public repository's history is filtered (commit ids rewritten, private-only commits dropped), so there the script reads this file. |
| review folders, folders with a run, runs, follow-ups, runs dated by folder name | `reviews/review-stats.json`, `reviews/runs.tsv` |
| review table: runs, completed, not completed, met the bar, FAIL, MEDIUM, hours and their coverage | `reviews/runs.tsv` (rules in `make_appendix.py`) |
| GPT FAIL count | `reviews/runs.tsv`, family GPT/Codex |
| worker sessions and tokens; Claude calls and tokens; DeepSeek sessions, tokens and cost; snapshot time; worker/DeepSeek ratio | `tokens/token-totals.json` |
| no-go totals by kind and status | `no-go/nogo-counts.json` |
| timeline figure | `reviews/runs.tsv` (bars), `git log` (line), `milestones.json` (numbered markers and key) |

Definitions: a *run* is one review task sent to one reviewer model; *met the
bar* is a completed run graded PASS or PASS WITH NOTES at HIGH confidence.
Meeting the bar is not acceptance: recorded acceptance exists only for the
Claude and GPT runs (see `reviews/README.md`).
