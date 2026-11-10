# Reader prototype V3: bounded CP application fidelity

The two requested clarifications are complete in the editorial worktree. The reader is now **20 pages**, with unchanged typography. The technical companion remains **263 pages**, so the complete supplied package is **283 pages**. No effort was made to force the additional explanation onto 19 pages.

## Current TeX/PDF pair

Under `<HOME>/.local/state/Le-AI-Lab/stratonovich-reading-notes-20261105`:

- `notes/notes_stratonovich_ham_second_moment_reader.tex`: 58,679 bytes, SHA-256 `8cc07385b349eea82a68d83484dc2112bb2187981899ce797e469c331a749885`.
- `notes/notes_stratonovich_ham_second_moment_reader.pdf`: 342,909 bytes, SHA-256 `17e647586c5335d789f553c6aa41ab6c77c88b12046b226f1901b5f277254d2b`.

## Exact bounded change

Only the opening of reader §3.1 changed. `v2-v3-full-source.diff` is the complete diff.

The text now explains that finite Gaussian modes do not bound Gaussian multiplication. Each selected word receives a sufficient finite Hermite degree cutoff, with N_i at least its number r_i of insertions. Starting from the vacuum, every prefix stays within that degree cutoff, including creation followed by annihilation. This proves the selected-word identity; it does not identify full propagators at one fixed truncation. These cutoffs, together with the spatial band cutoff, supply bounded operators for the existing ordered-root CP application. Mode/frequency cutoffs are removed at fixed selected word and positive noise widths. Full evolution is constructed separately by summation.

The CP import now states its bounded complex-Hilbert operator and holomorphic-neighborhood hypothesis and cites the same held author-preprint v1, **Theorem 6, pp. 5–6, and (3), p. 1**. This agrees with the full technical source at main LF5031–5041. The prefix argument agrees with `L:finite-word-cutoff`, main LF5296–5344; the coefficient/source identification is the fixed-positive-width passage near LF6387–6411. No unbounded-operator extension or full truncated-flow identity is used. No new theorem, covariance restriction or proof route was introduced.

Everything outside this one source-diff hunk, including all definitions, the complete C2 formula, the V2 five clarifications, theorem statements and technical correspondence map, remains unchanged.

## Preservation and validation

Before editing, the exact V2 pair and report seals were copied into `v2-preimages/`; `v2-preservation.json` records their identities. The old V1 and V2 report directories remain held and unchanged. The full V2 report manifest was rehashed before and after this revision.

The rebuilt pair passes the prescribed process-local BIBINPUTS/latexmk build: zero errors, undefined references/citations, overfull boxes and tabs. The style check passes. There are still 68 exact technical labels and 205 external links; all targets resolve in the supplied technical PDF. The source/body/formal correspondence is retained in `statement-proof-correspondence.json`.

All 28 original TeX files and the 263-page technical PDF remain byte-identical and match the original scientific inventory. The full PDF SHA is still `096cb3cd4610c91d7dc8718bd56526e777cdd06ebca41651a8955bc230eb2f35`. Sample final renders of pages 6, 7, 8, 19 and 20 are saved; author visual checks inspected the changed paragraphs, formula placement and final bibliography. These are author checks, not independent review credit.

No staging, commit, push, review/model call or global setup change occurred. The actual pair is ready for Root's inspection and atomic paired commit; this report is not scientific acceptance or project completion. All producer writes stop at the seal.
