# Round 4 status accuracy update

STATUS: DONE — status-only correction; configured high-confidence acceptance remains pending.

Updated only the Section 6 banner and the final status sentence of `R:higher-calibrations`. Both now state that Opus reviewed the section with PASS_WITH_NOTES/medium confidence and that configured high-confidence acceptance remains pending. Neither says UNREVIEWED or implies an unrun review. No running review remains, per root.

Root reports that v2 completed with all nine checks PASS, no mandatory repairs and verified full source delivery, but driver accepted=false because medium confidence does not meet the configured high gate. This update does not promote mathematical acceptance, abstract/accepted coverage, or full-goal status. No confidence retry or proof repair was made. Optional v2 suggestions remain for root's record and decision; none were applied.

## Exact preservation

The pre-edit source hash matches frozen v2. Byte comparisons verified all proof, theorem, hypothesis, proposition, lemma and corollary environment bodies throughout the entire manuscript: {'proof': 18, 'theorem': 2, 'hypothesis': 2, 'proposition': 9, 'lemma': 7, 'corollary': 2}. All were exactly unchanged. The entire prefix before Section 6 and suffix beginning at Targets are also byte-identical. The only differences are the two status passages below. Abstract and previously accepted scope are unchanged.

Root is archiving raw packets/attempts byte-exact in `reviews/2026-10-27-round4/review-evidence.tar.xz`, with member hashes; the v2 source member is `packet-v2/candidate.tex`. Compact reports remain `opus-v1-report.json` and `opus-v2-report.json` in the round directory. This worker used its saved hash-matching v2 baseline for preservation and did not modify or claim to verify that archive.

## Build

Ran from the repository root:

```text
latexmk -pdf -interaction=nonstopmode -halt-on-error -outdir=notes notes/notes_stratonovich_ham_second_moment.tex
```

Exit 0; 31 pages. Final log: zero errors, zero undefined references/citations and zero overfull boxes. Source tabs: 0. This is not a claim of zero nonfatal warnings or independent mathematical validation.

- Frozen v2 TeX SHA-256: `86ea2cf65a8eeff0a2bfb79fe045fcf9709d1e10ae7117b4d9472a7e2bd8a1da`
- Status-updated TeX SHA-256: `81bd89bdd2cbbd10e4973953db3794a47aa596c65d7e5e0ad33e7a41531e473a`
- Rebuilt PDF SHA-256: `d3c9179fa2466126bc77e2340536a05bf6ab1ab48aa6397bfc307321dbcc7099`

## Complete source diff

```diff
--- v2/candidate.tex
+++ notes/notes_stratonovich_ham_second_moment.tex
@@ -1546,10 +1546,11 @@
 \section{Higher spatial exponents under a convolution bound}
 \label{S:higher-alpha}
 
-\myCmts{UNREVIEWED candidate: all new statements in this section await
-  independent Opus review. The convolution assumption below is additional
-  to homogeneity. The concrete applications cover only the stated Riesz
-  ranges; the full general upper-bound goal and sharp constants remain open.}
+\myCmts{Reviewed by Opus with PASS\_WITH\_NOTES/medium confidence;
+  configured high-confidence acceptance remains pending. The convolution
+  assumption below is additional to homogeneity. The concrete applications
+  cover only the stated Riesz ranges; the full general upper-bound goal
+  and sharp constants remain open.}
 
 We retain the standing covariance assumptions and take $d\in\{2,3\}$ and
 $1<\alpha<2-\alpha_0$. Put $\delta=\alpha-1$, $q=3-\alpha$, and
@@ -1928,8 +1929,9 @@
   obstructions above concern only the spatial supremum, not existence,
   moment finiteness, or failure of the target time scale. In particular,
   arbitrary homogeneous covariances remain outside this conditional
-  argument, even when $\alpha+\alpha_0<2$. All statements in this
-  section remain candidates pending independent review.
+  argument, even when $\alpha+\alpha_0<2$. Opus reviewed this section
+  with PASS\_WITH\_NOTES/medium confidence; configured high-confidence
+  acceptance remains pending.
 \end{remark}
 
 \section{Targets}\label{S:targets}
```

Only the authorized source status passages, build artifacts and this report were written. No Git command, proof repair, review dispatch, message, sibling edit or Lean work was performed.

STATUS: DONE — review status accurate; high-confidence acceptance pending user/root decision.
