# The technical companion as a book

The long document is now a book-style technical companion. The short reader
remains an article and the entry point. Both retain their existing filenames.
The book has **293 pages, 11 chapters and four appendices**; the reader has
**27 pages**. The full pair therefore contains 320 pages.

The main proof runs continuously through the numbered chapters. The appendices
retain finite-order calculations, direct bounds with additional hypotheses,
covariance comparisons and the unsuccessful clock representation. None of the
mathematical record was deleted to make the structure appear shorter.

| Chapter | Topic | Printed pages |
|---|---|---|
| 1 | Setting and strategy | 1–12 |
| 2 | Construction and two-chain estimates | 13–35 |
| 3 | An independent upper bound | 36–66 |
| 4 | Covariance estimates and Gaussian approximation | 67–90 |
| 5 | The original noise and operator paths | 91–108 |
| 6 | Fixed masks and wave evolution | 109–128 |
| 7 | Scaling and the point lower bound | 129–145 |
| 8 | Spatial controls and Gaussian means | 146–161 |
| 9 | Bounds as the spatial radius grows | 162–176 |
| 10 | Gaussian estimates for the point upper bound | 177–206 |
| 11 | The constant and its consequences | 207–224 |
| A | Finite-order calculations | 225–230 |
| B | Direct upper bounds and static interpolation | 231–248 |
| C | Covariance comparisons in higher dimensions | 249–270 |
| D | Static comparisons and the clock obstruction | 271–283 |

The front matter has an overview, a guide to the argument, a multilevel contents
page and a short list of illustrations. The cover has its own PDF page label;
front matter uses Roman pages and the text uses Arabic pages. Chapter headings,
running headers, restrained colors and Latin Modern fonts provide a consistent
layout. Body size and text width remain 12pt and 6.2in. Chapters may start on any
page, so no blank odd-page openings are inserted merely for book conventions.

The construction chapter promotes its seven original subsections into sections.
The independent upper-bound chapter also has more descriptive subsections. The
benchmark goals now appear with the setting; the summary and open comparisons
close the main argument before the appendices.

Existing labels are retained. Numbering now includes chapter and section, and
figure counters restart by chapter. `S:G0` names the construction chapter;
its two old prose references were corrected from Section to Chapter.
[The numbering map](book-numbering-map.json) records all 44 original section
identities and the old reader's 71 landmarks. Source-paper theorem and page
pinpoints retain the source paper's numbering; they were not renumbered.

All 215 technical proofs retain their mathematical expressions, checked by
proof owner. The 27 mathematical modules retain their proof text; one now includes an
additional explanatory figure. The literature section is a separate input. This is a
structural and typographic revision, not a new mathematical result or an
upgrade of the independent review status. The previous 275-page article-style
companion is preserved at commit 669ccc9.

The reader's literal section-number references were replaced by links to stable
labels and its external map refreshed: 80 mapped labels and 246 remote PDF links
resolve. Its figures remain fixed beside their explanations. The book contains
19 illustrations and the reader contains nine.

Build from the repository root, using the recorded frozen bibliography if the
external refdb is unavailable:

```sh
latexmk -pdf -bibtex- -interaction=nonstopmode -halt-on-error -outdir=notes notes/notes_stratonovich_ham_second_moment.tex
latexmk -pdf -bibtex- -interaction=nonstopmode -halt-on-error -outdir=notes notes/notes_stratonovich_ham_second_moment_reader.tex
```

The book typography is in `book-layout.tex`. Current source/PDF pins and check
results are in [figures/VALIDATION.json](figures/VALIDATION.json); the prior
illustration/style record is retained separately under `figures/history/`.

The November 10 comparison adds separate discussions of Skorohod and
Stratonovich products, temporal noise regimes, and methodological tradeoffs.
Five additional diagrams explain endpoint elimination, degree allocation,
interval-end charges, chronological regions and subset optimization; two
book literature maps and one compact reader map distinguish model and result
classes. These changes preserve all 215 existing proof bodies.
