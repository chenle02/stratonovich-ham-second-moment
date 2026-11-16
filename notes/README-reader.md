# Reading edition with the current technical companion

Read [the 28-page reader](notes_stratonovich_ham_second_moment_reader.pdf)
with [the 472-page technical companion](notes_stratonovich_ham_second_moment.pdf).
The reader introduces the model, proposed result and variational constant,
explains how the main steps fit together, and links to the detailed proofs.
It is a guided route through the work, not a standalone short proof.
The combined record is 500 pages; no total-proof-length reduction is claimed.

The reader follows the current **unadopted whole-paper mathematical candidate**.
The November 11 deterministic update adds a spatial Fourier bound and clarifies
spectral multiplier comparisons in the technical book. It preserves the main
moment theorems, revises two auxiliary proofs and adds one, giving 216 proof
bodies. The reader's technical references are refreshed. The scoped review of
that update is separate from the independent whole-paper and final clearance
gates, which remain open. Earlier dated editions retain their original scope.

Build from the repository root using the tracked frozen bibliography:

```sh
latexmk -pdf -bibtex- -interaction=nonstopmode -halt-on-error -outdir=notes notes/notes_stratonovich_ham_second_moment_reader.tex
```

The portable technical-label map is embedded in the reader source; both PDFs
must travel together in the same directory. Regenerating the bibliography
requires the read-only refdb database; it is not edited by this workflow.
For future technical edits, refresh the embedded map from the newly compiled
technical aux, rebuild the reader, and recheck its external destinations.
Every reader TeX edit travels with its cleanly rebuilt PDF.

[Current validation](figures/README.md)
records 96 matched labels, 266 valid external PDF links and clean builds.
The original November 5 V4 reader at commit 9895781 was paired with the old
263-page companion. Its original source/PDF and validation remain in Git and
[the historical review directory](../reviews/2026-11-05-reader-v4-paired-revision/).

The illustrated edition adds seven TikZ figures, selected from twelve shared
figure sources. It uses fixed reader placement so a diagram follows the full
statement or definition it explains. Both the figure sources/captions and all
rendered diagram pages were reviewed. The complete figure set appears in the
technical companion. See [the figure guide](figures/README.md). The earlier
20-page reading editions remain historical; the current reader has 28 pages.

The technical companion is now a book with 12 chapters and 7 appendices.
Chapter 12 develops the numbered no-go results; the final three appendices
give the AI work in numbers, what Lean checks and how far each result has
been checked. The
reader remains in article format. Its technical references use the book's
chapter/section numbering and printed pages, including explicit links to the
appendices. See [the book guide](BOOK-GUIDE.md) and its numbering map. The
earlier 275-page article-style companion remains in Git at 669ccc9.

The companion now opens every chapter and appendix with motivation, linked
prerequisites and an outline, so readers can enter at a topic of interest. Both
editions begin with a short history from Walsh's lectures to moment asymptotics.

The reader now uses the report's Latin Modern fonts and blue/teal palette.
Its literature comparison shares the report's vector drawing, including the
covariance sketches and separate contribution band. All ten figures were
inspected at their final page positions; the reading edition is 28 pages.

The proof-map nodes now link directly to chapters and key results in the
technical companion. Rebuild its external map with
`python3 scripts/refresh-reader-labels.py` after compiling the book.
