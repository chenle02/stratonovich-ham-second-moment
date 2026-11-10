# Working 267-page draft checkpoint — 2026-11-09

Le requested an atomic commit and push of the working TeX/PDF, then a detailed
AI development history for human study. This checkpoint stores the current
candidate at the normal notes paths. Storage is not mathematical adoption.

The main TeX is byte-identical to the frozen November 5 integration candidate:
`516d6a650bdac7d3da68672f37836afd084b651c39553b43d5135d0512e39d14`.
All 28 TeX files match the prior independent verification input pins. The 27
included modules and extra.bib have not changed from the preceding checkout.

The fresh root build used the exact reviewed bibliography and visible date:

```sh
SOURCE_DATE_EPOCH=1793912362 FORCE_SOURCE_DATE=1 latexmk -pdf -bibtex- -interaction=nonstopmode -halt-on-error -outdir=notes notes/notes_stratonovich_ham_second_moment.tex
```

The frozen .bbl is deliberately tracked despite the generic ignore rule.
All.bib remains a read-only external symlink; its availability is unnecessary
for this frozen-bibliography build. Bibliography regeneration is a separate task.
The build passes with 267 pages, zero errors, undefined references/citations,
and overfull boxes. Its PDF is byte-identical to the independently verified
November 7 rebuild, hash `a2aea80bd73cad92db7e2fe70bff7aa6c70f6142d5be460a2710d3f88667f434`.

The original reviewed PDF hash is
`26f9f4a5ee65b08449cedc41dc34e688d15147f0ab4e3b9d23e4ee3f9a8624f8`.
Prior verification established identical extracted layout text and identical
RGB rasters on all 267 pages at scale 1600 between that original and rebuild.
The three `prior-verification-*.json` files preserve that earlier evidence;
this checkpoint does not claim a new raster audit. The fresh PDF's byte identity
with that verified rebuild is checked in `build-receipt.json`.
Producer build logs are preserved in `build-logs.tar.gz`; their machine paths
are diagnostic records, not repository dependencies.

Existing mathematical and visual reviews keep their original byte bindings,
confidence, limitations and acceptance states. No review receipt is rewritten
or transferred to claim new mathematical, visual, cold-read or final clearance.
The previous tracked 263-page TeX/PDF remain recoverable from commit
`11e009aac6fcc9fdeddb00cdd7063dc56c457aad` at the same notes paths.

See [the human development history](../../AI-DEV-HISTORY.md),
[the working-draft status](../../notes/WORKING-DRAFT-STATUS.md), and the
[complete pre-checkpoint Git chronology](../../history/git-history.tsv).

The local pre-commit TeX formatter initially altered indentation. Before push,
the exact frozen TeX bytes were restored and the unpushed checkpoint amended
with `GIT_TEX_HOOK=/dev/null` for that invocation only. No hook configuration
was changed. The explicit source pins, tab check and build checks above retain
the reviewed source/PDF binding; no mathematical source edit was introduced.
