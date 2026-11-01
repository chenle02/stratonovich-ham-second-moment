# Launching the Codex run

Le revised the constant target on2026-10-31: derive the actual value from
the computation; matching Chen's guessed constants is not required.
`PROJECT-GOAL.md` and active `Progress.md` control current work. The G0
launch text below is historical and must not reopen completed rounds.

> Superseded for the current hand-off by `HANDOFF.md` (agent #30, 2026-10-26),
> which adds the lean-pkg track. This prompt remains valid for a fresh session.

Run from the repository root (example; adjust model/effort to Le's current
routing):

```bash
cd <HOME>/workspace/svn/Article-Stratonovich-HAM-Second-Moment
codex   # interactive; paste the prompt below as the first message
```

## First prompt

```text
You are the research worker for Article-Stratonovich-HAM-Second-Moment.

Before anything else, read in this order: AGENTS.md, PROJECT-GOAL.md,
Progress.md, sources/SOURCE-MANIFEST.md, and
notes/notes_stratonovich_ham_second_moment.tex (build it once to confirm the
toolchain). Then read the source pages the manifest marks in bold, from the
rendered author-version PDF (pdftoppm), not from the text layer.

Your task is Round 1 = Gate G0 in Progress.md:
 (a) justify E u^2 = sum over (m,n), m+n even, of E[S_m(g_m) S_n(g_n)] from
     (2.13), (2.18), (2.21) and Theorem 1.1, and write each term as a
     two-chain pairing integral in the form of (3.6);
 (b) reproduce Remark 5.1's bound E u^2 <= exp(C t^2) and locate exactly
     where the exponent 2 enters instead of kappa = (4-alpha-alpha_0)/(3-alpha);
 (c) decide, with a counting argument, whether Theorem 3.1 with the
     Laplace-weighted kernels of Lemma A.1 can give the scale t^kappa.

[held back: collaborators' unpublished work]

## Before launching

- `git fetch && git status -sb` must show the branch level with `origin`.
- Confirm the wiki project page
  `../SPDEs-wiki/content/projects/stratonovich-ham-second-moment.md` exists.
- The run must not start Round 2 without Le reading the Round 1 report.
