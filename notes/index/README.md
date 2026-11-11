# Subject index and notation list

These files provide the technical book's two complementary lookup tools.
They do not add mathematical hypotheses or alter statement/proof text.

- `entries.json` is the curated subject-index catalogue. Entries point to
  definitions, result statements and substantive discussions through existing
  labels. Main topics have selected subentries; synonyms lead to the canonical
  heading. Conjectural and conditional material is identified in the entry.
- `notation.json` groups recurring notation by role and states its local scope.
  Each row links to a definition or principal use. It explicitly distinguishes
  covariance Gamma from Euler Gamma, the equilibrium mass from the mean-growth
  rate, the phase space F from the scalar map F_0, and shrinking spatial scales
  from growing cutoff radii. Generic calculation letters are not listed merely
  because they occur.
- `generate.py` validates every referenced label, checks subject cross-references
  and duplicate entry/anchor pairs, and generates `anchors.tex` and
  `list-of-notation.tex`. `notation-locations.json` records the source crosswalk.
- `setup.tex` loads standard `imakeidx` with automatic shell execution disabled,
  plus `longtable`, `array` and `needspace` for the notation tables. It uses the LaTeX kernel's
  `label` hook and never redefines `\label`. The installed TeX Live 2026 format
  provides this hook. Only selected labels emit entries, once per label.

The catalogue covers all 27 integrated modules, the main-source construction
and upper-bound arguments, all four appendices, and selected explanatory
figures and future-work discussions. Its purpose is useful retrieval, not a
concordance or a count of every word. Index page numbers come from the actual
label encounter during typesetting. No broad chapter ranges are manufactured.
Standard MakeIndex may compress genuinely consecutive selected page numbers.

## Integration

Load `notes/index/setup` in the technical main preamble **before hyperref**.
Insert `notes/index/list-of-notation` after the contents and illustrations;
the proof guide may follow it before `\mainmatter`. It appears as a
front-matter chapter in the contents.
Print `\printindex` after the bibliography. The reader does not load the setup
or indexing hook. The integration patch also ignores standard `.idx`, `.ind`
and `.ilg` build artifacts; generated index files need not be committed.

## Updating and building

After editing either catalogue or moving source definitions:

```sh
python3 notes/index/generate.py --write
```

The regular book build runs MakeIndex through latexmk's dependency handling:

```sh
latexmk -pdf -interaction=nonstopmode -halt-on-error -outdir=notes notes/notes_stratonovich_ham_second_moment.tex
```

For an explicit manual index pass, use:

```sh
makeindex -o notes/notes_stratonovich_ham_second_moment.ind notes/notes_stratonovich_ham_second_moment.idx
latexmk -pdf -interaction=nonstopmode -halt-on-error -outdir=notes notes/notes_stratonovich_ham_second_moment.tex
```

Then verify that every emitted index record has the page recorded for its
intended label:

```sh
python3 notes/index/generate.py --verify-index notes/notes_stratonovich_ham_second_moment.idx --aux notes/notes_stratonovich_ham_second_moment.aux
```

Rebuild the reader's label map after the book build as usual. Inspect the
notation tables, index column breaks and links in the PDF; mechanical label
coverage cannot decide whether an entry is editorially useful.

## Editorial and technical checks

The initial catalogue has 281 mappings, 360 emitted records at 230 existing
anchors, and 167 top-level headings including synonyms. The notation list
contains 85 rows in seven groups. Every integrated mathematical module and
each appendix has substantive index coverage. No proof or definition was
rewritten to insert index commands. The chapter roadmap also has an entry.

A complete scratch build produced a six-page notation list and five-page
subject index. All 360 index records matched their compiled label pages;
MakeIndex accepted all entries with zero rejections and zero warnings. The
book build had zero errors, undefined references/citations and overfull boxes.
All notation pages and all index pages were visually inspected. Paragraph
headings are kept with the first table rows; a local index layout guard keeps
main entries with following lines. The full root build should repeat these
checks after inserting the preface and choosing the final front-matter order.

Intentional exceptions: generated index entries use required command-argument
braces; notation source references deliberately repeat their target labels;
protected mathematical subscripts and local parameter conventions are kept.
The Hölder entry uses an explicit ASCII sort key with an accented display name.
The index is a reading aid and does not change the manuscript's proof status.
