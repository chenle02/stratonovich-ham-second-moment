# Author-only cold-clean editorial v2

Status: exact external candidate for root inspection; no adoption or dispatch.
Base science is `53bf01b7585b8815ec92b56b5ba1590550c3e93f`. ACTIVE was observed at
review-only `ee91bcdba865679226f7dd2ea045d36c0430714a`; all28 TeX files were byte-equal
to science53bf at snapshot. No ACTIVE/source/Git-ref/global/bibliography change
or provider call was made.

## Exact artifacts

- `proposed-editorial.patch`: complete patch from science53bf, SHA256
  `5a5c470073bbbec8bda8a451b244e131a8baaf8619be66220f512fc48c972fe5`.
- `v1-to-v2-protected-editorial.patch`: ONLY the four specifically approved
  protected-body wording changes, SHA256
  `ba7bac3e2f9d9340b74c849d60c8480dd35e726c4ff34f9e745623f03aea2a40`.
- `base/` and `proposed/`: exact28-source snapshots plus unchanged extra.bib.
- `editorial-change-manifest.json`: exact hashes, stable proof IDs, 240 formal
  statements, 515 display bodies, exact approved old/new wording and v1 changes.
- `proposed/notes/notes_stratonovich_ham_second_moment.pdf`: rebuilt candidate,
  SHA256 `bdb63e76e10c2861bd150f70087719bfc592aebb54fdf1c631d3fbe56132829f`.
- `build-render-receipt.json`: clean-build and author render/text inventories.

Both complete and incremental patches pass `git apply --check` against their
respective exact baselines. All four changed source files pass format-tex--check.

## Deliberately acknowledged protected-body changes

The four changes are exactly root's authorization:

1. PROOF034: remove the comparison with an earlier candidate proposition;
   retain the endpoint hypothesis conclusion and Proposition reference.
2. PROOF189: delete only the adjective `accepted` before `fixed-order`.
3. PROOF193: `The Jensen and lower bounds remain valid.` replaces the
   acceptance/status sentence.
4. R:static-holder-scope: `No novelty is asserted here.` replaces the
   novelty/formal-verification process sentence.

**Exactly3/214 proof-body hashes change; the other211 are byte-identical.**
**Exactly1/240 formal statement bodies changes (the remark); the other239,
including hypotheses, definitions, goals, theorem statements and other remarks,
are byte-identical.** Stable proof IDs and labels are retained.
The v1-only assertion that ALL214/240 bodies are identical is historical and
is explicitly NOT asserted for v2.

| Proof | Base/v1 raw body SHA256 | V2 raw body SHA256 |
|---|---|---|
| PROOF034 | 143054ceed344de11dd276f1c4c585863074be1c5959d2faa14e108539862eaf | 69dc5ff9df6bcb84ccd2d5a74e99d848553c516e739e846a51d75b37a4f8d61e |
| PROOF189 | 7f228b02d9715d7822a628b797d06c21737a9483b76e2510e7e0a81edd62fd49 | ae457ae3b6b342a37ecd8f1884bfcb4df3ba1aa1d7eb72b31d742a7e6fee07e0 |
| PROOF193 | b490e32d9ceaf08bede40076aaa2fa3cd42326424fc9360a211e3049b0eafff2 | fc76ecdd1c6901ae5725944a1807cfbb73a33dcf281f2178eece6d20487b48f9 |

The remark body changes from `db368f1b685cc6cfe1b1104ec272a8333098ccbdd65ee40c0cb0b28a8fa138b7` to
`c54d2473d42652629a23d3ce28ad76a675b9e4d6e18c7bb3481b5288f0420a17`. All515 display-environment bodies, every authored
inline/display-delimiter math span, all label sequences and all citekeys remain
verbatim. No mathematical scope guard, formula, parameter condition, theorem
claim or no-go boundary is changed. The raw-body differences are acknowledged
editorial differences; this proposal makes no automatic review-credit transfer.

Relative to53bf, four TeX files change: main, integrated_point_transfer,
integrated_signed_moment_upper and integrated_intrinsic_constant. The other24
scientific TeX files and the bibliography are unchanged. Relative tov1, ONLY
main/point-transfer/signed-upper have the four exact approved changes.

## Build and author layout check

Mandated root latexmk command with read-only canonical refdb through BIBINPUTS
completes at259pages: zero errors, undefined references/citations and overfull
boxes. The log, aux, bbl and stdout are retained. The fresh v2 changed pages
50,68,237,241 and continuation238 were rendered and author-inspected; no
clipping or collision was observed. They display the exact authorized wording.
The previous v1 image inspection is not transferred as final-v2 visual evidence.
This is not full259-page visual inspection or independent source/image credit.

## Residual wording and packet leakage limits

The all28-source scan now finds no previous project-review outcome/model name,
no `accepted` adjective, and no pending-cold/whole-review process prose.
`residual-keyword-scan.json` retains the exact remaining hits:

- `PrintReviews`/`review` in the amsrefs preamble is ordinary bibliography logic;
  generated `review={MR...}` fields are Mathematical Reviews identifiers.
- The separate verification of the mild equation is a mathematical construction
  assertion, not a reviewer endorsement.
- GateG0/GateG1/G2 labels, the `G0 verdict` and `What this gate tests` remark
  titles, and the separate Chen--Hu `source audit` wording remain from v1.
  These are development-route/source-fidelity terminology, not independent
  review votes; their mathematical limitation/no-go content remains intact.
- Remaining `high` occurrences are high/low-frequency, inverse-power and norm
  estimates, not confidence labels.

The manuscript is still not author-anonymous: Le Chen's name, date, exact title,
source/citation identities, edition pinpoints, author-manuscript hash/retrieval
metadata and source discrepancies remain. Exact source fidelity is retained.
A future genuinely prior-review-blind packet must also exclude outcome-bearing
Progress/HANDOFF/review/ledger/governance prose and irrelevant All.bib/pipeline
metadata from its CONTEXT, not just remove those files from its tree. Primary
source texts and publication metadata are separate from previous project votes.
These decisions and actual final packet verification remain root obligations;
this source-edit preparation alone does not certify packet blindness.

No source-image, mathematical whole-review, fresh cold-read, publication,
correspondence, Lean/HPC or full-project acceptance is claimed. Root must inspect
and decide adoption before any source merge or provider dispatch.
