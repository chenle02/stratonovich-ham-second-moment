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
results to keep. The present author, Le Chen, set up and ran the work and is
responsible for what it reports: every objection will be looked into, and any
claim that does not hold up will be corrected, qualified or withdrawn, with each
change recorded in the public history. The technical chapters have not yet been
read in full by a human; the verification ledger records, result by result, what
was checked and how. **AI systems are not authors
of this paper.** The preface is signed "Le Chen, with Amy", recording that it
was written with her.

## How the work was checked

- **Cross-family review.** A review counts only when the reviewing model
  belongs to a different family from the model that wrote the work under
  review. The reviewers were DeepSeek V4 Pro (main reviewer), Kimi-K3 and
  Claude, and Codex (GPT) for the Lean statement ledger.
- **Whole-paper review.** Earlier complete-note reviews remain at **medium**
  confidence and are **not accepted** under the project's high-confidence
  standard. Six further review invocations are recorded separately. A blind
  whole-source call returned *inconclusive* at **medium** confidence; all 253
  proof rows were marked `NOT_READ`, meaning the proof bodies were not
  independently audited in that session, although the full scientific source
  was supplied. A focused call returned *pass with notes* at **high**
  confidence, with required core reconstruction incomplete. Four local calls
  returned three passes and one pass with notes, all at **high** confidence.
  Two were accepted as scoped mathematical evidence with notes and two were
  partial. The author accepted a bounded exception for one automatic native
  retry in the uniform-product check, with the incident disclosed. Its
  abandoned-stream usage/cost and whole-run usage/cost and aggregate cap
  compliance remain unknown. These are scoped observations, not
  whole-book or release acceptance; no earlier grade is upgraded.
  The separate Chapter 12 skeptic synthesis was **not obtained**; the scoped
  HIGH honesty synthesis does not replace it.
- **Lean.** A companion Lean package checks parts of the work. The state
  described here is its release v0.10.0 (DOI 10.5281/zenodo.24295453), cut
  from the wave-L14 gate: its checks are recorded for commit
  <!--s:lean.verified-->`c8d8e07`<!--/s--> of the public companion repository,
  with the coverage record at commit
  <!--s:lean.coverage-->`6e83b60`<!--/s--> of that repository. Under the registered
  modelling choices and scope qualifications described in Appendix F, the
  coverage record lists:
  - <!--s:lean.full_words-->sixty<!--/s--> numbered results, three displayed
    equations and one remark under the manuscript's hypotheses
    (<!--s:lean.narrow_words-->sixteen<!--/s--> of the results with a narrower
    conclusion);
  - for <!--s:lean.inputs_words-->thirty-five<!--/s--> more, analytic inputs are
    supplied as hypotheses or left outside Lean: one of them has every
    conclusion proved from two supplied inputs, and the others are checks of
    steps, parts or narrower forms. The entries distinguish supplied
    hypotheses, where present, from analytic work left outside Lean. Eight
    entries concern elementary checks without an additional analytic
    hypothesis; their surrounding analytic arguments are not formalized.

  These Lean statements are kernel-checked using only Lean's standard axioms.
  The private development verification record for `8f51004` also records a
  separate `leanchecker --fresh` replay of all 141 library modules and the
  umbrella, with all 142 targets passing both fresh and default replay.
  The three comparator-tier libraries were excluded from this replay.
  Analytic and probabilistic facts supplied as hypotheses are **not** proved
  merely by using them in Lean. Of the <!--s:main.count_words-->four<!--/s-->
  main theorems, <!--s:lean.outside_main_words-->two<!--/s--> are outside Lean.
  For `T:intrinsic-occupation-ceiling`, the original-moment sentence remains
  unformalized. For `T:white-moment-bounds`, the formalized bounds concern
  the variational value in place of the original moment constant, with the
  white spatial energy supplied. No main stochastic moment theorem is
  verified end to end. The correspondence between the Lean statements and
  the manuscript was reviewed by AI and accepted by the author through
  wave L14; this is not human verification. Appendix F states each result's
  scope, modelling choices and assumptions.
- **Readability pass and re-reads.** After the reviews above, the proofs were
  rewritten so that their steps are easier to follow. A GPT model working
  within Amy did the rewriting under written rules: inside a proof, sentences
  could be added, removed or reordered, while statements, displayed formulas,
  labels and references were kept. Separately, at the author's decision, the
  wording of three statements was corrected, a few damaged sentences of the
  original text were repaired, and one unused setup paragraph was removed. A
  Claude model listed the places where a reader would have to stop; it was an
  editorial aid, not a review. Every one of the 249 proofs of the technical
  files was then re-read by DeepSeek V4 Pro, with the old and the new text side
  by side: 59 calls and 58 reports (44 pass and 14 pass with notes, each at
  high confidence for the call), of which 38 cover the final text. These are
  scoped checks that the arguments were preserved. They do not upgrade the
  inconclusive whole-book cold read, replace the missing Chapter 12 skeptic
  synthesis, or accept the book. In four calls the client program restarted an
  interrupted answer, so part of their usage is unknown. Appendix E gives the
  counts and their limits.
- **Human checking.** Part I (the reading edition) has not yet been checked
  line by line by a human reader. The technical notes have not yet been
  checked line by line by a human reader. Independent checks by readers are
  recorded result by result in the public verification ledger,
  https://github.com/chenle02/stratonovich-ham-second-moment/blob/v1.0.3/VERIFICATION.md.

**No AI review grade in this statement is a proof.**

## The record

A filtered development history (the proof revisions, the review runs with
their model families and grades, selected reports, and the routes that failed)
is public at
https://github.com/chenle02/stratonovich-ham-second-moment (release tag
`v1.0.3`),
with documented redactions. [REDACTIONS.md](REDACTIONS.md) lists every class of
removal with its reasons and counts, including review records held back until a
source author has been told and evidence archives that were not deposited.

## Disclosure of support

The author was supported in part by the U.S. National Science Foundation
under Grant DMS-2246850 and CAREER Grant DMS-2443823, and by Simons
Foundation Collaboration Grant for Mathematicians 959981. OpenAI provided
access to its AI tools through the ChatGPT for Academic Researchers program.
These acknowledgements are the same as in the book's preface.
