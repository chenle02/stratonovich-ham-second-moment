# Assigned task: proof-readability reread of one frozen module

Review the OLD and NEW mathematical source below, with the assigned ten proofs.
This is an independent read of an editorial rewrite, not a whole-book or release
review. The requested model is DeepSeek V4 Pro, independent of the GPT author.
Do not infer correctness or acceptance from that description.

Read BOTH complete versions of EVERY assigned proof and its unchanged statement
and needed module definitions. Check that mathematics is unchanged, no step or
scope condition was lost, and the new explanations are justified under the old
hypotheses. Do not treat unchanged displays or a mechanical gate as mathematical
evidence. Do not use the OLD text as an oracle: distinguish a pre-existing concern
from a defect introduced by the rewrite. Report material new mathematical
justification or changed argument, even if you think it is correct. Do not repair
or silently strengthen the proofs.

Pay particular attention to endpoints/zero cases; noncommutative trace products
and rectangular factor two; Fourier normalization and negative Sobolev orders;
the cutoff-map density and series-limit passages; rank/index estimates; left and
right variance congruences; scalar eigenvalue order versus operator powers;
finite compression, measurability and the two Fatou passages; nonlocal Bessel
transforms versus physical test-function support; and translation noncompactness.

Two previously flagged passages require an explicit disposition from your own
read: (C1) dense cores and extension/identification in the mixed counting/Lebesgue
Schur argument; (C2) recovery from periodic Fourier partial sums through the
extended cutoff map, for every real Sobolev order. The NEW source has no AUDIT
comments. List any unresolved AUDIT-worthy issue honestly, including a new one.

The full module is supplied as mathematical context; its unproved remark and
comments are not additional assigned proofs. No prior review verdict, author QA
report or acceptance record is supplied. No source PDF/image review is assigned.
Do not browse, run tools, delegate, read files, edit or contact anyone. All inputs
you may use are embedded in this message. If more context or time is needed,
mark the affected proof PARTIAL/NOT_READ and state the precise remaining issue.
Do not invent missing work or give an unearned PASS/HIGH.

# Output contract

Return a self-contained Markdown report. Begin exactly with:
# Review Result
Category: proof-readability-equivalence
Model: <your actual model identity, if known>
Verdict: PASS | PASS_WITH_NOTES | FAIL | INCONCLUSIVE
Confidence: high | medium | low

Use your own unforced verdict and confidence. Then provide exactly one section
headed '## <proof label>' for each of the ten labels in the assignment, in order.
Each section must contain:
- Old reading: COMPLETE | PARTIAL | NOT_READ
- New reading: COMPLETE | PARTIAL | NOT_READ
- Argument preservation: PRESERVED | CHANGED | UNCERTAIN
- New explanations: JUSTIFIED | CONCERN | UNCERTAIN
- Evidence: concrete mathematical working or checks, with the relevant equation
  labels or OLD/NEW local line ranges. Do more than restate the mechanical facts.
- Lost steps or qualifiers, unresolved issues, and any pre-existing concern;
  'none identified within this read' is permitted when justified.

After all ten, give '## AUDIT dispositions' for C1/C2 and any new flagged issue,
then '## Findings and limits' with actionable distinctions between new defects,
pre-existing concerns, harmless wording and unread/context-limited work.
If a proof is only partially read, do not claim full ten-proof completion.
Keep the public report to roughly 6000 words or less; spend the available budget
on actual reasoning, not copies of the source. No whole-book, Lean-correspondence,
render/image, human-verification or publication acceptance is requested.
