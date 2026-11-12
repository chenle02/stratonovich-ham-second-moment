# Appendix G: how far each result has been checked

Appendix G of the book counts, by proof group, how far the numbered results
have been checked: by AI review, by Lean and by people. It is generated from
the verification ledger (`VERIFICATION.md` at the root of the repository),
not typed by hand.

| File | What it is |
|---|---|
| `pin_verification.py` | Copies the ledger's results table, unchanged, into `verification.md`, with the ledger's commit date and the coverage commit of its Lean column. |
| `verification.md` | The pinned results table. The book reads only this copy. |
| `make_appendix_g.py` | Writes `notes/verification-status-data.tex` from the pinned table. |

To refresh after the ledger changes:

```bash
python3 -I scripts/verification-status/pin_verification.py VERIFICATION.md
uv run --with pyyaml python -I scripts/verification-status/make_appendix_g.py
latexmk -pdf -interaction=nonstopmode -halt-on-error -outdir=notes notes/notes_stratonovich_ham_second_moment.tex
```

`make_appendix_g.py` stops, instead of writing a wrong table, when

- the ledger's labels are not exactly the book's numbered theorems,
  propositions, lemmas, corollaries and no-go results (read from the `.aux`
  file);
- a result's group in the ledger is not the group of the chapter that
  contains it;
- a result's Lean entry, or its number of Lean claims, differs from the
  coverage file pinned for Appendix F (`scripts/lean-coverage/coverage.yaml`);
- the AI review column starts to differ between rows (the appendix then needs
  a row for it), or a Human entry is not `unchecked`, `checked by ...` or
  `disputed ...`.
