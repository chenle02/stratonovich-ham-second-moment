# Reading edition with the current technical companion

Read [the 20-page reader](notes_stratonovich_ham_second_moment_reader.pdf)
with [the 269-page technical companion](notes_stratonovich_ham_second_moment.pdf).
The reader introduces the model, proposed result and variational constant,
explains how the main steps fit together, and links to the detailed proofs.
It is a guided route through the work, not a standalone 20-page proof.
The combined record is 289 pages; no total-proof-length reduction is claimed.

This November 9 revision matches the current **unadopted mathematical candidate**.
It updates the literature and contribution discussion, mentions the three
ongoing Skorohod projects, and refreshes the technical page map. The technical
proofs and statements are unchanged modulo whitespace; the exposition and
bibliography have been revised. Its scope remains215 OWN proofs,241 declarations,
13 joins and nine global checks. Independent scientific and final clearance
remain open; the reader does not change those acceptance states.

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

[Current validation](../reviews/2026-11-09-literature-review/README.md)
records 69 matched labels, 209 valid external PDF links and clean builds.
The original November 5 V4 reader at commit 9895781 was paired with the old
263-page companion. Its original source/PDF and validation remain in Git and
[the historical review directory](../reviews/2026-11-05-reader-v4-paired-revision/).
