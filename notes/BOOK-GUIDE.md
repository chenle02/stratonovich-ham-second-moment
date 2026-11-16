# The technical companion as a book

The long document is now a book-style technical companion. The short reader
remains an article and the entry point. Both retain their existing filenames.
The book has **472 pages, 12 chapters and seven appendices**: four proof
appendices, Appendix E on the AI work, Appendix F on Lean coverage and
Appendix G on how far each result has been checked.
Chapter 12 presents numbered obstructions and failed approaches. The reader has **28 pages**. The full pair therefore contains 500 pages.

The main proof runs continuously through the numbered chapters. The appendices
retain finite-order calculations, direct bounds with additional hypotheses,
covariance comparisons and the unsuccessful clock representation. None of the
mathematical record was deleted to make the structure appear shorter.

| Chapter | Topic | Printed pages |
|---|---|---|
| 1 | Introduction | 1–29 |
| 2 | Construction and two-chain estimates | 30–56 |
| 3 | An independent upper bound | 57–92 |
| 4 | Covariance estimates and Gaussian approximation | 93–125 |
| 5 | The original noise and operator paths | 126–148 |
| 6 | Fixed masks and wave evolution | 149–173 |
| 7 | Scaling and the point lower bound | 174–195 |
| 8 | Spatial controls and Gaussian means | 196–216 |
| 9 | Bounds as the spatial radius grows | 217–234 |
| 10 | Gaussian estimates for the point upper bound | 235–269 |
| 11 | The constant and its consequences | 270–290 |
| 12 | Obstructions and failed approaches | 291–331 |
| A | Finite-order calculations | 332–338 |
| B | Direct upper bounds and static interpolation | 339–358 |
| C | Covariance comparisons in higher dimensions | 359–381 |
| D | Static comparisons and the clock obstruction | 382–396 |
| E | The AI work in numbers | 397–404 |
| F | What Lean checks | 405–423 |
| G | How far each result has been checked | 424–433 |

The front matter has a Preface, Abstract, multilevel contents, illustrations
and a guide to the argument. After the bibliography, the six-page List of
notation immediately precedes the six-page Subject index. The cover has its own PDF page label;
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

In the original book-format conversion, all 215 technical proofs retained
their mathematical expressions, checked by proof owner. The 27 mathematical modules retained their proof text; one received an
additional explanatory figure. The literature section became a separate input.
That conversion was structural and typographic, without upgrading the
independent mathematical review status. The previous 275-page article-style
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

All twelve chapters and four mathematical appendices now open with a motivating question,
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
roadmap covers all twelve chapters and four mathematical appendices. Refresh the page table
with `uv run --with pymupdf python scripts/refresh-book-guide.py`; the helper
uses numbered chapter labels, so the front-matter guide is not an appendix.
Refresh reader links with `python3 scripts/refresh-reader-labels.py`.

## Reference tools

The notation list has 85 recurring symbols in seven groups, with definition
links and explicit local scope. The subject index has 167 headings including
synonyms, built from 281 curated mappings and 360 page references at 230
existing labels. All twelve chapters, four mathematical appendices and 27 included
mathematical modules have subject coverage. The kernel label hook adds index
entries without editing statements or proofs. See `index/README.md` for
maintenance, generation and page-verification commands.

The opening chapter is titled Introduction. The Preface explains audience,
prerequisites and reading routes; the Abstract retains the mathematical
summary; the Guide to the proof explains dependencies. Acknowledgments and
publication-specific matter are left for actual authorial/publication decisions.

The November 11 deterministic update adds Lemma `L:spatial-fourier-bound` and
revises the proofs of `P:spatial-smooth-ratio` and
`L:damped-homogeneous-norms`. The current book has 216 proofs, with 213 unchanged
from its immediate baseline. That scoped mathematical review is recorded in
`../reviews/2026-11-11-deterministic-spatial-multiplier/`; it is separate from
the historical formatting checks and the open whole-paper gates.
