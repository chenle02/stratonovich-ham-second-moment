# Scripts behind Appendix F, "What Lean checks"

Appendix F lists, for each numbered result of the book that the Lean
companion covers, how much of it Lean checks, and reports the companion's
build and statement checks. Everything in it is generated from the files in
this folder.

| File | What it is |
|---|---|
| `coverage.yaml` | The companion's coverage file (schema coverage/1), pinned. |
| `coverage-scope-tex.yaml` | LaTeX versions of the three narrower-conclusion sentences; each row repeats the ASCII sentence so drift is detected. |
| `coverage-commit.txt` | The verified commit the book quotes, its date, and the commit the coverage files were read from. |
| `lean-receipt-summary.json` | Numbers from the companion's receipts and claims ledger at the verified commit (no host names or paths). |
| `pin_companion.py` | Writes the four files above from a clone of the companion (`python3 pin_companion.py COMPANION VERIFIED_COMMIT [COVERAGE_COMMIT]`; needs `lean-pkg` on the PATH). |
| `make_appendix_f.py` | Writes `notes/lean-coverage-data.tex` (`python3 scripts/lean-coverage/make_appendix_f.py`). |

Current pin: verified commit d40f394 (receipts and claims ledger bound to
it), coverage files read from 31441aa (later commits change only
documentation). lean-pkg 0.29.0.

Checks built in:
- `pin_companion.py` refuses receipts or a claims ledger that are not bound to
  the verified commit, a ledger that is not complete, and a coverage commit
  whose changes after the verified commit touch any build input.
- `make_appendix_f.py` refuses a label missing from the book, an unknown
  category, a scope sentence whose LaTeX version has drifted from
  `coverage.yaml`, and receipts that show an unproved step or a non-standard
  axiom (the appendix would then say something false).

The table's wording for the five categories follows the companion's README.
The correspondence between the Lean statements and the book is reviewed by AI
models of a different family from the ledger's author; it is not human
verification.
