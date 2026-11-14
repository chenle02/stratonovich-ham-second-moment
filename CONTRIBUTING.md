# Contributing

Thank you for helping. This project asks mathematicians to check, question
and interpret results that were developed with AI systems. The rules for
credit are written here **before** anyone contributes, so that credit never
depends on who asks or when. If these rules change, the change applies only
to later contributions.

## What you can contribute

- **A verification.** Check one result in [VERIFICATION.md](VERIFICATION.md)
  and open a pull request that changes that row. Say exactly what you
  checked: the statement, the proof, the cited inputs, and anything you did
  not check.
- **A correction or a gap.** Open an issue naming the result's label (for
  example `L:masked-trig-products`) and what fails. A proposed repair is
  welcome as a pull request.
- **An interpretation or a question.** Use GitHub Discussions.
- **A formalization.** See the Lean companion's contributor guide.

## Credit

Mathematics treats coauthors as equal contributors, listed alphabetically.
Open contributions also need explicit criteria. The test below adapts the
four-part authorship criteria used in medical publishing (ICMJE), chiefly the
requirement to take responsibility, which matters most for text developed
with AI.

| Tier | Who qualifies | Credit |
|---|---|---|
| **Acknowledgment** (automatic) | Any merged pull request: a verification sign-off, a correction, an interpretation | Named in the Acknowledgments of the next arXiv version and in `VERIFICATION.md`, with a link to the pull request |
| **Coauthorship** (all three required) | (a) A substantial contribution to the mathematics: a missing proof, a repaired gap that a stated theorem depends on, a new result included in the paper, or a complete independent line-by-line check of one of the paper's five groups (defined by chapter in [VERIFICATION.md](VERIFICATION.md#proof-groups): I. setting, construction and the independent upper bound; II. Gaussian approximation and the lower bound; III. matching upper bound and the constant; IV. the appendices; V. the obstructions of Chapter 12); to the Lean verification: a stated result formalized in full that is outside Lean or formalized only with a narrower conclusion, merged into the Lean companion; or to the tools behind the book: a tool or generator that the book's build or checks depend on, merged into this repository. (b) You read and approve the version you sign. (c) You accept responsibility for the parts you contributed | Coauthor of the next arXiv version, in alphabetical order, with each person's role listed using the CRediT contributor roles |
| **Verification report** (optional) | Contributors whose checks fall short of a complete proof group, or who prefer not to be coauthors of the paper | Coauthors of a separate short report on what they verified |

A complete, independent line-by-line check of one of the five groups
counts toward coauthorship, provided (b) and (c) also hold. Here the check is
the contribution: in a paper developed with AI, careful human verification is
part of what makes the result mathematics. A check of individual results,
short of a whole group, earns an acknowledgment or a place in the
verification report.

## How authorship is decided

- Anyone may propose authorship, for themselves or for someone else, in a
  GitHub Discussion.
- Le Chen decides as principal investigator within about one month and
  posts the reasons in the same Discussion.
- Disputes go to Raluca Balan (University of Ottawa).
- arXiv allows authors to be added in later versions, so you can join after
  the first version.
- Authorship changes take effect at the next MAJOR version, which is a new
  arXiv version; see [VERSIONING.md](VERSIONING.md).
- **AI systems are never authors.** Their role is disclosed in the paper's
  AI-use statement.
- Credit does not depend on the tools you use. A check done by hand counts
  the same as one done with an AI assistant, and you remain responsible for
  what you sign.

## How contributions are recorded

Every contribution is recorded at the level of results, so that anyone can
see who did what and check it.

- **By label.** Each result has a stable LaTeX label (for example
  `L:masked-trig-products`). A contribution names the labels it concerns.
  Labels do not change between versions; numbers may.
- **By record.** Each claimed contribution links to the merged pull
  request, issue or commit that shows the work. `VERIFICATION.md` records
  sign-offs row by row.
- **By role.** Each coauthor's roles are named with the
  [CRediT](https://credit.niso.org/) contributor roles. Those most used
  here:

  | CRediT role | In this project |
  |---|---|
  | Conceptualization | the question, the route or a key idea |
  | Methodology | a technique or reduction used in a proof |
  | Formal analysis | writing a proof, or repairing a gap |
  | Validation | an independent line-by-line check |
  | Software | Lean formalization, numerical or symbolic checks |
  | Writing – original draft | drafting text of the paper |
  | Writing – review & editing | corrections and revisions of the text |
  | Supervision, Project administration | direction of the project |

The paper's contributions statement is built from these records. Template
(one line per person, alphabetical):

```text
Author contributions.
<Name>: <CRediT roles>. <What, by label>: e.g. checked Section 4,
  results L:a–P:b, line by line (PR #12); supplied the proof of L:c (PR #15);
  repaired the gap in P:d (issue #9, PR #18).
Le Chen: Conceptualization, Formal analysis, Supervision, Writing – original
  draft. Directed the project and its AI system; checked Part I (the
  reading edition).
AI systems: not authors; their use is described in the AI-use statement.
```

Each coauthor approves their own line before a version is posted. The
record shows what was done; how much a contribution weighs is decided by
the coauthorship test above, not by counting lines.

## Ground rules

- Be precise about what you checked and what you did not.
- Quote the label of every result you discuss.
- Do not post other people's unpublished work or copyrighted texts.
- Be kind. Disagreement about mathematics is welcome; disrespect is not.
