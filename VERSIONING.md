# Versions

Every release of this book has a version number `MAJOR.MINOR.PATCH`, for
example `1.2.3`. The first public release is `1.0.0`; earlier private states
count as `0.x`. The rule below is the same for everyone who contributes, and it
decides each number from what changed, not from who made the change.

## What each number means

| Number | It goes up when | The release brings |
|---|---|---|
| **MAJOR** (`1.4.2` → `2.0.0`) | A reader of the arXiv version must see the change: a main theorem is added or its statement changes; an error that affects a stated result is corrected; the proof becomes substantially simpler; or enough smaller changes have accumulated to justify a new arXiv version. | A new arXiv version. Changes of authorship take effect here (see [CONTRIBUTING.md](CONTRIBUTING.md)). |
| **MINOR** (`1.4.2` → `1.5.0`) | The mathematics changes, but every main theorem keeps its statement: a gap is filled; a proof is repaired or replaced; a lemma, remark or entry in the list of approaches that do not work is added; a result is newly checked by Lean; or the check status of a result goes up, for example after a complete line-by-line check by a person. | No arXiv update. |
| **PATCH** (`1.4.2` → `1.4.3`) | The mathematics does not change: typos, wording, references, figures, layout, metadata, or a documentation-only change to the Lean records. | No arXiv update. |

When a number goes up, the numbers after it return to zero.

Every release, at every level, is a Git tag `vMAJOR.MINOR.PATCH`, a GitHub
release and a Zenodo record with its own DOI. Patches may be collected into one
release.

## How a contribution is graded

1. Every pull request carries one label: `patch`, `minor` or `major`, chosen by
   what it changes. The reviewer who merges it confirms the label.
2. The next release takes the highest label merged since the last release.
3. An error is graded by its effect. A wrong statement of a main theorem makes
   the next release MAJOR and comes with an erratum note. An error that leaves
   every main theorem unchanged is MINOR.
4. When in doubt between two levels, choose the higher one.

## What each release records

Each release adds an entry to the changelog with

- the version and the date;
- what changed, by result label (labels do not change between versions;
  numbers may);
- who contributed, with links to the merged pull requests;
- which entries of the public verification table changed their status.

## The Lean companion

The Lean companion has its own version numbers. Each release of the book names
the companion version and commit it was checked against; the appendix "What
Lean checks" records them.
