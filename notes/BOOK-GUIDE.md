# The technical companion as a book

The long document is now a book-style technical companion. The short reader
remains an article and the entry point. Both retain their existing filenames.
The book has **284 pages, 11 chapters and four appendices**; the reader has
**24 pages**. The full pair therefore contains 308 pages.

The main proof runs continuously through the numbered chapters. The appendices
retain finite-order calculations, direct bounds with additional hypotheses,
covariance comparisons and the unsuccessful clock representation. None of the
mathematical record was deleted to make the structure appear shorter.

| Chapter | Topic | Printed pages |
|---|---|---|
| 1 | Setting and strategy | 1–8 |
| 2 | Construction and two-chain estimates | 9–30 |
| 3 | An independent upper bound | 31–59 |
| 4 | Covariance estimates and Gaussian approximation | 60–83 |
| 5 | The original noise and operator paths | 84–101 |
| 6 | Fixed masks and wave evolution | 102–121 |
| 7 | Scaling and the point lower bound | 122–138 |
| 8 | Spatial controls and Gaussian means | 139–154 |
| 9 | Bounds as the spatial radius grows | 155–169 |
| 10 | Gaussian estimates for the point upper bound | 170–199 |
| 11 | The constant and its consequences | 200–216 |
| A | Finite-order calculations | 217–222 |
| B | Direct upper bounds and static interpolation | 223–240 |
| C | Covariance comparisons in higher dimensions | 241–262 |
| D | Static comparisons and the clock obstruction | 263–275 |

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
proof owner. The 27 included mathematical modules are unchanged. This is a
structural and typographic revision, not a new mathematical result or an
upgrade of the independent review status. The previous 275-page article-style
companion is preserved at commit 669ccc9.

The reader's literal section-number references were replaced by links to stable
labels and its external map refreshed: 78 mapped labels and 240 remote PDF links
resolve. Its figures remain fixed beside their explanations. The book retains
all 12 illustrations and the reader retains seven.

Build from the repository root, using the recorded frozen bibliography if the
external refdb is unavailable:

```sh
latexmk -pdf -bibtex- -interaction=nonstopmode -halt-on-error -outdir=notes notes/notes_stratonovich_ham_second_moment.tex
latexmk -pdf -bibtex- -interaction=nonstopmode -halt-on-error -outdir=notes notes/notes_stratonovich_ham_second_moment_reader.tex
```

The book typography is in `book-layout.tex`. Current source/PDF pins and check
results are in [figures/VALIDATION.json](figures/VALIDATION.json); the prior
illustration/style record is retained separately under `figures/history/`.
