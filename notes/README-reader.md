# Compact reading edition — editorial prototype

Read [the 20-page reader](notes_stratonovich_ham_second_moment_reader.pdf)
with [the 263-page technical companion](notes_stratonovich_ham_second_moment.pdf).
The complete supplied package has 283 pages. This makes the main reading route
shorter; it does not claim a reduction in the total technical record.

The reader states the original model, complete variational constant and
principal intermediate results, explains the connecting deductions, and links
to the actual technical statements and full proofs. All28 original TeX files
and the technical PDF are unchanged. All214 proofs,240 declaration roles,
13 joined obligations and the full model remain in the verification scope.
This prototype does not establish final independent or circulation clearance.

Build from the repository root:

```bash
latexmk -pdf -interaction=nonstopmode -halt-on-error -outdir=notes notes/notes_stratonovich_ham_second_moment_reader.tex
```

In an isolated worktree without an adjacent refdb checkout, supply the existing
read-only refdb directory through `BIBINPUTS`. The bibliography symlink and
database are not edited. The portable technical-label map is embedded in the
reader source; both PDFs must travel together for its external proof links.

Every reader TeX edit is committed with its rebuilt PDF after the zero-error,
undefined-reference/citation and overfull-box checks. Current source/PDF pair
is version V4 of the editorial prototype; detailed author validation and Root
source/visual readback are retained separately from scientific review gates.
Version V4 names the positive spectral shift and the temporal source cutoff,
and states the inherited positive-radius parameter conditions explicitly.
