# What the main theorems rest on (Appendix G, last section)

`make_critical_path.py` writes `notes/critical-path-data.tex`: the tables and
the list of the section "What the main theorems rest on".

    latexmk -pdf -outdir=notes notes/notes_stratonovich_ham_second_moment.tex   # the .aux gives the numbers
    uv run --with pyyaml python scripts/critical-path/make_critical_path.py
    uv run --with pyyaml python scripts/critical-path/make_critical_path.py --check

## What a link is

Result R rests directly on result S when the statement or the proof of R cites
S by `\ref`, or cites an equation labelled inside the statement or the proof
of S, or when the proof of R says "the preceding lemma" (and the like) and S
is the result just before R. A main theorem rests on every result reached by
following links. The four main theorems are named in `ROOTS` in the script.

Results cited only in the sentences that introduce R (after the previous
result, proof or heading and before the statement of R) are printed in
parentheses. They are not links: such a sentence often cites a result to
contrast with it.

## Links read by hand

A citation by label does not show every use. `link-corrections.json` records
the links added (`add`), removed (`remove`) and deliberately left out
(`not_added`) after reading statements and proofs, each with the file and the
words that justify it. The reading covered the 26 results that most others
depended on and the 26 proved results of Chapters 2 to 11 that the script had
not reached. The other results were not read in this way; their list of
direct links may be incomplete. The generator stops if a correction names an
unknown result or removes a link that is not there.

## What the list is not

It shows which results a proof cites or uses. It does not say that a proof is
correct, and it is not a review. The Lean class of a result comes from
`scripts/lean-coverage/coverage.yaml`, the file Appendix F is generated from.
