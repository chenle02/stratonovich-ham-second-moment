# The technical companion as a book

The long document is now a book-style technical companion. The short reader
remains an article and the entry point. Both retain their existing filenames.
The book has **326 pages, 11 chapters and four appendices**; the reader has
**29 pages**. The full pair therefore contains 355 pages.

The main proof runs continuously through the numbered chapters. The appendices
retain finite-order calculations, direct bounds with additional hypotheses,
covariance comparisons and the unsuccessful clock representation. None of the
mathematical record was deleted to make the structure appear shorter.

| Chapter | Topic | Printed pages |
|---|---|---|
| 1 | Introduction | 1–22 |
| 2 | Construction and two-chain estimates | 23–45 |
| 3 | An independent upper bound | 46–77 |
| 4 | Covariance estimates and Gaussian approximation | 78–102 |
| 5 | The original noise and operator paths | 103–121 |
| 6 | Fixed masks and wave evolution | 122–141 |
| 7 | Scaling and the point lower bound | 142–158 |
| 8 | Spatial controls and Gaussian means | 159–174 |
| 9 | Bounds as the spatial radius grows | 175–189 |
| 10 | Gaussian estimates for the point upper bound | 190–219 |
| 11 | The constant and its consequences | 220–237 |
| A | Finite-order calculations | 238–244 |
| B | Direct upper bounds and static interpolation | 245–263 |
| C | Covariance comparisons in higher dimensions | 264–285 |
| D | Static comparisons and the clock obstruction | 286–299 |

The front matter has a Preface, Abstract, multilevel contents, illustrations,
a six-page notation list and a guide to the argument. A five-page subject
index follows the bibliography. The cover has its own PDF page label;
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
labels and its external map refreshed: 95 mapped labels and 264 remote PDF links
resolve. Its figures remain fixed beside their explanations. The book contains
21 illustrations and the reader contains ten.

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

## Entering a chapter directly

All eleven chapters and four appendices now open with a motivating question,
linked prerequisites and a short outline. These openings explain what each
chapter establishes and where its conclusions stop. They distinguish fixed
spatial cutoffs from growing radii, signed upper controls from nonnegative
lower controls, and auxiliary comparisons from the main proof. The front
guide explains how to use these entry points. The forty-year SWE introductions
and the shared guitar illustration appear in both editions.

The chapter openings change exposition and pagination only. The 215 proof
bodies are unchanged up to whitespace against the preceding committed edition.
All fifteen opening pages were inspected, and the reader's external label map
was refreshed. This does not transfer earlier independent review acceptance.

Section 1.6 discusses higher even moments, the proposed constant and the
spatial-regularity obstacle. These are future questions, not additional proved
results of this edition.

Section 1.6 now has five subsections, ending with a sourced outlook on
logarithmic wavefields and possible scaling limits. Rytov prior art and
formal mechanisms are distinguished from conjectures and established results.

The proof map now links its nodes to chapters, sections and results. A separate
roadmap covers all eleven chapters and four appendices. Refresh the page table
with `uv run --with pymupdf python scripts/refresh-book-guide.py`; the helper
uses numbered chapter labels, so the front-matter guide is not an appendix.
Refresh reader links with `python3 scripts/refresh-reader-labels.py`.

## Reference tools

The notation list has 85 recurring symbols in seven groups, with definition
links and explicit local scope. The subject index has 167 headings including
synonyms, built from 281 curated mappings and 360 page references at 230
existing labels. All eleven chapters, four appendices and 27 included
mathematical modules have subject coverage. The kernel label hook adds index
entries without editing statements or proofs. See `index/README.md` for
maintenance, generation and page-verification commands.

The opening chapter is titled Introduction. The Preface explains audience,
prerequisites and reading routes; the Abstract retains the mathematical
summary; the Guide to the proof explains dependencies. Acknowledgments and
publication-specific matter are left for actual authorial/publication decisions.
