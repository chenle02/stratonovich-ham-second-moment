# Statement on the use of AI

## Who did what

This work was carried out by the author with **Amy**, the author's AI research
system. Amy is not a model. She is a model-agnostic research operating system:
a set of workflows and standing rules (how a research round is run, how
reviews are dispatched, what counts as evidence, when to stop), a research
knowledge base (bibliography, reference library, curated arXiv sources and an
SPDE wiki), and interfaces through which any capable language model can work
within her. In this project, models from four families worked within Amy:
Anthropic Claude, OpenAI GPT (through Codex), DeepSeek and Kimi.

Amy developed the mathematics: the models working within her drafted the
proofs, the LaTeX source and the bookkeeping. The author's role was to drive
the work: choosing the problem, setting and revising the goals, deciding which
approaches to pursue or abandon, choosing the reviewers and deciding which
results to keep. The author takes full responsibility for the entire content. **AI systems are not authors
of this paper.** The preface is signed "Le Chen, with Amy", recording that it
was written with her.

## How the work was checked

- **Cross-family review.** A review counts only when the reviewing model
  belongs to a different family from the model that wrote the work under
  review. The reviewers were DeepSeek V4 Pro (main reviewer), Kimi-K3 and
  Claude, and Codex (GPT) for the Lean statement ledger.
- **Whole-paper review.** The latest review of the complete technical notes
  (DeepSeek V4 Pro) returned *pass with notes* at **medium** confidence, with
  no required repair, on an earlier edition. The project's own standard
  requires high confidence, so this review is **not accepted**, and no grade
  is carried over to the current edition.
- **Lean.** A companion Lean package checks parts of the work. Its coverage
  file at commit `d9ded8f` (documentation changes only after the verified
  commit `aff7409`; to be re-pinned to the companion's release tag) records:
  - thirty-nine numbered results, three displayed equations and one remark
    formalized under the manuscript's own hypotheses (fifteen of the results
    with a narrower conclusion);
  - five further results have every conclusion proved, with named analytic
    inputs supplied as hypotheses;
  - for twenty more, Lean checks steps or parts of the proof.

  All of it is kernel-checked, using only Lean's standard axioms. Every
  module of the Lean library was also checked a second time by Lean's
  separate kernel checker. Analytic and probabilistic inputs that enter as
  hypotheses are **not** verified by Lean. Most of the main theorems are outside Lean: three of the four. For
  the fourth, `T:intrinsic-occupation-ceiling`, Lean proves a narrower
  conclusion under the manuscript's own hypotheses. The correspondence
  between the Lean statements and the manuscript's statements was reviewed
  by AI and accepted by the author on 2026-11-12. This is AI-checked
  correspondence only, not human verification. The verification ledger
  lists, result by result, what Lean covers.
- **Human checking.** Part I (the reading edition) has not yet been checked
  line by line by a human reader. The technical notes have not yet been
  checked line by line by a human reader. Independent checks by readers are
  recorded result by result in the public verification ledger,
  https://github.com/chenle02/stratonovich-ham-second-moment/blob/v1.0.0/VERIFICATION.md.

**No AI review grade in this statement is a proof.**

## The record

The complete development history (every step, every review with its model
family and grade, and the routes that failed) is public at
https://github.com/chenle02/stratonovich-ham-second-moment (release tag
`v1.0.0`),
with a small number of documented redactions (other authors' copyrighted
texts, private infrastructure, collaborators' unpublished work and private
planning notes).

## Disclosure of support

The author was supported in part by the U.S. National Science Foundation
under Grant DMS-2246850 and CAREER Grant DMS-2443823, and by Simons
Foundation Collaboration Grant for Mathematicians 959981. OpenAI provided
access to its AI tools through the ChatGPT for Academic Researchers program.
These acknowledgements are the same as in the book's preface.
