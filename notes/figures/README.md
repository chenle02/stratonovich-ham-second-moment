# Illustrations for the reader and technical companion

The same TikZ sources are used by both documents. The technical companion
contains 26 figures; the reader uses ten selected illustrations.
Captions state the mathematical meaning and the limits of each schematic.
They do not replace the proofs.

| Source | What it explains | Reader |
|---|---|---|
| `nogo-chain-geometry.tex` | Chronological merging can violate the original wave-support geometry | Chapter 12 |
| `nogo-phase-blocks.tex` | Velocity passes across a block boundary | Chapter 12 |
| `nogo-projection-escape.tex` | A fixed projection cannot follow translated controls as the radius grows | Chapter 12 |
| `nogo-feature-range.tex` | A finite-cutoff point feature can lie outside the closed image of the original noise | Chapter 12 |
| `proof-map.tex` | The independent upper bound and the fixed-control lower bound establish finiteness before the sharp comparison | Yes |
| `nonseparable-controls.tex` | Nonnegative smooth controls need not be one temporal function times one spatial function | Yes |
| `two-chain-pairings.tex` | Self-pairs, cross-pairs and unequal chain lengths; ordering is only within each chain | Yes |
| `order-of-limits.tex` + `order-of-limits-drawing.tex` | Numbered Green-before-noise construction; joint width approaches and the separate summable-tail passage | Technical detail |
| `common-noise.tex` + `common-noise-drawing.tex` | One fixed Gaussian extension; the auxiliary channel may contribute at a cutoff and vanishes on the original range | Yes |
| `light-cone.tex` + `light-cone-drawing.tex` | The backward domain of dependence lies inside the cutoff plateau; both displacement and velocity matter | Yes |
| `global-control-blocks.tex` | Correlated blocks, the true final shortened interval, and one global Gaussian cost | Yes |
| `hermite-cutoff.tex` | The degree bound for every prefix of a selected Gaussian word, including lowering steps | Technical detail |
| `dyadic-cover.tex` | Three shifted interval grids and the infinite covariance majorant | Technical detail |
| `white-strip.tex` | The rectangle/strip intersection behind the fourth-order spatial-white calculation | Technical detail |
| `positive-gram.tex` | Positive combinations without inverse Gram matrices; singular and zero cases remain allowed | Yes |
| `gaussian-enlargement.tex` + `gaussian-enlargement-drawing.tex` | An image of a Hilbert ball enlarging a Gaussian event; the control norm is not Euclidean distance | Technical detail |

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

## Linked proof destinations and chapter roadmap

The shared proof map now gives chapter/section/result destinations inside
its nodes. The report also includes `chapter-roadmap.tex`, covering all eleven
chapters and four appendices, with auxiliary comparisons shown separately.
The node links are local in the report and external in the reading edition.
Both report figures and the reader proof map were inspected after integration.

## Combined iceberg and memory candidate — HELD

One combined-source build includes the exact approved icebergc81b81cd and
placed-memory2bf48696 sources. MemoryFigure3.2 is on printed64 inside3.2;
icebergFigure12.1 is on printed250 inside12.1. Candidate396book/28reader,
29numberedbook figures; earlier Figure7.2/guitar-wrap sources unchanged. All99reader
technical labels and271external named links checked. Bounded source/PDFpins:
`VALIDATION-iceberg-memory-combined-held.json`; detailed current-origin impact,
final page images, source-equality and real-filter checks:
`private/audit/2026-11-15-iceberg-memory-combined-held/`.
This is not yet the adopted set;16checks and Leapproves this combined SHA
before push. Car remains separate in the Preface replay; existing adopted
validation/count statements above retain their historical scopes.

## HELD drawing asset: kappa fan

`kappa-fan-drawing.tex` plots the exponent against the temporal parameter for
three supplied spatial exponents. The3/2line stops at its excluded half-time
cutoff; the same line's continuation is faint/dashed and explicitly outside
the hypothesis. Open endpoints, spatial-white label, static-limit note and
longer-memory arrow retain the requested scope. Content9.61×5.03cm,12ptprose.
Standalone0/0/0/0/exact-fraction evidence:
`private/audit/2026-11-15-kappa-fan-drawing-held/`; current bounded pins:
`VALIDATION-kappa-fan-held.json`.24owns caption/placement,3checks caption,
16andLeapprove. No current book/reader insertion, figure counts or adopted
PDF pins are changed by this drawing-only HELD unit.

The kappa-fan HELD successor to56114300uses true ytick7/5instead of4/3;
4/3nowlabels only the gold open cutoff. The memory arrow is under the actual
axis and title, away from the legend. Curves/endpoints/palette/legend/type/
scales are unchanged. Final0/0/0/0and exact-Fraction regression pass. Content
9.598×5.160cm versus9.608×5.028cm: height+1.32mm explicitly disclosed to keep
3.20ptannotation clearance without smaller type or clipping.24checks actual
book-page impact; no adoption or size waiver. Evidence:
`private/audit/2026-11-15-kappa-axis-clarity-held/`; latest pins in
`VALIDATION-kappa-fan-held.json`.

## HELD drawing asset: physical-mask window (2026-11-15)

`mask-window-drawing.tex` stacks a smoothed toy potential, a smooth squared-root
mask and their verified product over one spatial axis. The 11.8 cm by 6 cm drawing
uses 12 pt prose. It is not inserted in the book or reader; #24 owns caption and
placement, #3 checks the draft caption, and #16/Le approve. No covariance claim is
made by this asset. Standalone 0/0/0/0 and product/plateau/support evidence:
`VALIDATION-mask-window-held.json` and
`private/audit/2026-11-15-mask-window-drawing-held/`. Existing adopted figure
counts/pins are unchanged; no integration/scientific gate is advanced.

## HELD drawing asset: control, mean and wave

`control-mean-wave-drawing.tex` is the supplied Chapter8construction-order
row: Gaussian control, deterministic mean and wave evolution, two labelled
arrows, and a fixed-spatial-radius bracket. No equations or other claims.
Content14.55×2.89cm; matched12pttitle baselines and uniform11ptbody/edge/note
hierarchy retain clear margins and a two-line middle description. Scoped
0/0/0/0preview, exact wording/baseline checks and hashes:
`private/audit/2026-11-15-control-mean-wave-drawing-held/` and
`VALIDATION-control-mean-wave-held.json`.24owns caption/placement,3checks
caption,16andLeapprove. No book/reader insertion or adopted pins changed.

The Chapter8control/mean/wave HELD successor to8025ccd6retains its main row,
adds live-overridable section macros on the arrow labels, and two lighter
secondaryinputs8.1→8.2with only8.2feeding the mean box. The thin fixed-radius
bracket spans both rows below them, avoiding a path/label crossing. Content
14.550×4.201cm; preservedmain12/11pthierarchy, secondary11pt; both default and
override previews0/0/0/0. Evidence:
`private/audit/2026-11-15-control-mean-wave-inputs-held/`; current bounded pins
`VALIDATION-control-mean-wave-held.json`.24caption/placement and3scientific
captioncheck precede16/Leapproval. No book/reader/caption or public/master change.

Latest Chapter8flow HELD successor toa33fd95cmoves only the two main-arrow
lines fromy=.80to.60, preserving xextents and every other drawing byte. Final
standalone0/0/0/0, text/dimensions unchanged; arrows meet straight sides below
rounded top corners. Evidence/two-line diff:
`private/audit/2026-11-15-control-mean-wave-lower-arrows-held/`.24typesets
and seeks Le/3/16checks; no book edit or push/adoption in this source unit.
