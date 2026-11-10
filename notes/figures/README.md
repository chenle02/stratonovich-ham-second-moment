# Illustrations for the reader and technical companion

The same TikZ sources are used by both documents. The technical companion
contains all twelve figures; the reader uses seven central illustrations.
Captions state the mathematical meaning and the limits of each schematic.
They do not replace the proofs.

| Source | What it explains | Reader |
|---|---|---|
| `proof-map.tex` | The independent upper bound and the fixed-control lower bound establish finiteness before the sharp comparison | Yes |
| `nonseparable-controls.tex` | Nonnegative smooth controls need not be one temporal function times one spatial function | Yes |
| `two-chain-pairings.tex` | Self-pairs, cross-pairs and unequal chain lengths; ordering is only within each chain | Yes |
| `order-of-limits.tex` | Green smoothing is removed before external noise widths, followed by the summable-order passage | Technical detail |
| `common-noise.tex` | Every cutoff uses the given Gaussian noise and one fixed auxiliary noise; the limit retains the original noise | Yes |
| `light-cone.tex` | The backward domain of dependence lies inside the cutoff plateau; both displacement and velocity matter | Yes |
| `global-control-blocks.tex` | Correlated blocks, the true final shortened interval, and one global Gaussian cost | Yes |
| `hermite-cutoff.tex` | The degree bound for every prefix of a selected Gaussian word, including lowering steps | Technical detail |
| `dyadic-cover.tex` | Three shifted interval grids and the infinite covariance majorant | Technical detail |
| `white-strip.tex` | The rectangle/strip intersection behind the fourth-order spatial-white calculation | Technical detail |
| `positive-gram.tex` | Positive combinations without inverse Gram matrices; singular and zero cases remain allowed | Yes |
| `gaussian-enlargement.tex` | An image of a Hilbert ball enlarging a Gaussian event; the control norm is not Euclidean distance | Technical detail |

The reader figures stay at their explanatory locations. Technical figures use
normal floats. Blue arrows and dashed covariance pairs provide distinct cues
without relying solely on color. The figures use normal readable labels, not
reduced document typography.

Both documents load TikZ and `styles.tex`. The shared `ProofRef` command points
to local technical labels in the companion and to external technical references
in the reader. Refresh the reader's embedded label map whenever technical pages
change. All figure captions and their reference targets are part of the build.

[VALIDATION.json](VALIDATION.json) pins the sources and PDFs and records the
build, reference, style and preservation checks. A separate subagent reviewed
every source/caption body; all twelve technical figure pages and all seven
reader figure pages were inspected. Required geometric and placement errors
were corrected before the final check. This is illustration and editorial
review, not independent acceptance of the mathematical proof or the entire PDF.

The style revision also replaces private terminology with ordinary descriptions,
retains the original labels for verification links, and preserves mathematical
expressions up to whitespace and explicit single-symbol font/accent arguments.
Generated label entries, necessary command arguments and distinct labels on
separately numbered aligned equations are retained intentionally. The technical
companion retains its technical-report organization; the reader supplies the
front-facing result statements and guide.

## November 10 additions

The book now contains 19 figures and the reader nine. Added endpoint elimination,
interval degree allocation, phase-norm changes, chronological cross-color
regions and active-subset optimization. The latter also appears in the reader.
Two book literature figures and a compact reader map distinguish the stochastic
products and selected source-qualified results. All eight new sources/captions
received separate semantic review and their integrated pages were inspected.
The previous validation is retained in history/dbbd9c8-validation.json; current
hashes, counts and link checks are in VALIDATION.json. This does not establish
whole-PDF or scientific acceptance.

## Chapter-opening and history edition

The current pair has 301 technical pages and 28 reader pages, with 20 and ten
figures respectively. The shared `walsh-guitar.tex` uses the credited artwork
in `media/guitar-sandstorm/`. The 81-label map and all 248 remote PDF links
resolve. Current pins are in VALIDATION.json; the preceding validation is
preserved in `private/audit/2026-11-10-chapter-guides/prior-validation.json`
from the repository root. Chapter-opening inspection covers fifteen opening
pages; it does not certify the whole document visually or mathematically.

## Reader/report figure parity

Both literature maps now use `literature-results-drawing.tex`, with their own
captions and stable labels. The reader matches the report's fonts and colors.
The positive-Gram diagram separates the singular-case heading from the vector
label. All ten reader figures and the affected report figures were inspected.
The guitar caption's source indentation now survives the repaired formatter.
This resolves the previously pending caption-style correction.
