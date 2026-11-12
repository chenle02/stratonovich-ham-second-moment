# Scoped manuscript revision — accepted under the author-approved scope

This is a scoped adoption record, not whole-paper or human verification.
The source candidate is bound by candidate-v2/packet-manifest.json; its two
changed TeX files also match expanded-context-v3's binding. H:homog and all
existing labels are retained. One new lemma/proof is added; two existing
proofs are revised; the other213proof bodies are byte-identical to the baseline.

## Review lineages and disposition

1. Initial source: DeepSeek and Kimi both reached the900-second wall limit
   without a scientific verdict. Kimi's first dry run also rejected an
   unsupported per-call effort flag before dispatch. All attempts retained.
2. Candidate-v2 fixes a stale relative reference introduced by inserting the
   lemma. DeepSeek V4 Pro returned PASS_WITH_NOTES/high,10checks and no required
   repairs. Its check5 explanation incorrectly compared at theta with values
   at1 and incorrectly described an arbitrary positive Laplace domain as away
   from endpoints. The source itself was correct. A bounded same-session
   clarification rechecked this boundary, explicitly corrected the report-only
   errors and returned PASS_WITH_NOTES/high. A final serialization-only repair
   put the minor findings into the required string-list format. It preserved
   every other scientific field exactly and each original minor claim/reason
   verbatim. The final report passes the installed schema validator. These
   messages are ONE reviewer lineage; native exports preserve the original
   message prefixes and confirm deepseek/deepseek-v4-pro. See the format-repair
   content-preservation record, raw reports and native exports.
3. Candidate-v2 Kimi report text had PASS_WITH_NOTES/medium, no manuscript
   blockers, but unavailable input interfaces and invalid JSON/check tags.
   Its receipt is not accepted. It was not relabelled or resumed to obtain a
   higher confidence. The specific missing inputs were supplied in a new
   expanded-context assignment, with the mathematical candidate unchanged.
4. Expanded-context-v3 Kimi-K3: valid native receipt, PASS_WITH_NOTES/high,
   11checks, no required repairs. It read the complete expanded mathematical
   sources and the reader synchronization paragraph. Its source-image coverage
   is explicitly PARTIAL: the read-only profile lacked ReadMediaFile. Native
   accepted=true therefore closes only the text/mathematics part here, not
   image fidelity. Root does not reinterpret text extraction as image reading.

The mathematical scoped checks pass in both required families. Agent21 added
and tested the supported Kimi-only --allow-image-read flag in Le-AI-Lab8273447a.
The subsequent native image-fidelity review returned PASS/high,7checks, no
required repairs and accepted=true, with image_read_enabled=true and only
Read/ReadMediaFile observed. All nine requested images were inspected, with
additional source-page crops. Its minor notes concern OCR/layout artifacts
resolved against images and content outside that focused image assignment.
Those outside interfaces were covered by the expanded mathematics review;
no full-book or source-theorem acceptance is inferred. Root accepts the scoped
revision as a conjunction of these bound mathematical and image checks under
Le's prior approval. The text-only Kimi report is not relabelled as visual.

## Adjudication of optional findings and reviewer slips

- DeepSeek M1 / Kimi minor1 (radial integral and Euler evaluation): the ball
  mass law determines the radial pushforward alpha*V*r^(alpha-1)dr; integration
  against (q^2+r^2)^(-1) and the standard Euler integral give the displayed
  R_alpha exactly. No angular density is assumed. The calculation and its
  exact source location are present; adding another equation label is optional.
- DeepSeek M2 (positive definiteness): exp(-lambda*|s-t|) is standard; the
  following unchanged L:translated-covariance-CS proof also gives its explicit
  factorization, supplied in expanded context. The new comparison applies it
  after time integration, with absolute domination established first. No
  pointwise wave-product positivity is used.
- DeepSeek M3 (N2 squared notation) / Kimi minor2 (tail notation): the squared
  expression is explicitly defined, nonnegative, and reduces to the earlier
  full/tail definitions for the stated domains. No mathematical ambiguity or
  required repair was found; the existing notation is retained.
- DeepSeek M4 (standalone resolvent label): the reference names the precise
  lemma proof and the new proof displays the resolvent identity. Another
  numbered equation is not required for correctness.
- Kimi minor3: the initial context packet included the same unchanged consumer
  proof twice. Confirmed packet duplication, not manuscript duplication; keep
  the frozen inputs unchanged and avoid this in later packet generation.
- Kimi minor4: normalized Gaussian convolution has mass one; the independent
  image check includes the source heat-kernel definition and smoothing pages.
  This optional point does not assert homogeneity of a smoothed covariance.
- Kimi check3 includes a report-only phase-factor slip in an intermediate
  Fourier identity. The correct relation is F0(xi.grad Q)=i*|xi|^2*F0(Q).
  Taking moduli gives exactly the inequality used in the manuscript; the
  manuscript does not print the incorrect identity. DeepSeek independently
  verified the correct bound and constant. No source repair is needed.
- Kimi check9 calls the deterministic bound "strictly stronger." We adopt only
  its independence from S1 finiteness; no numerical ordering against the old
  S1-dependent upper constant has been proved or stated in the manuscript.
- The original R0 proof was a valid route through an independent stochastic
  upper estimate. The new route removes that dependency; it does not establish
  that the old proof was circular. Reviewer wording suggesting a repaired
  earlier cycle is not adopted.

No optional finding changes a mathematical formula or hypothesis. The reader
paragraph is a direct synchronization of the new finite-ratio dependency and
was explicitly checked in expanded-context-v3 check11. Whole-paper review,
source/image coverage outside this scope and Agent22's successor Lean
correspondence remain separate.

## Build and source checks

validate.py checks345book pages,28reader pages,216proofs with213unchanged,
96mapped labels,266valid reader links, H:homog byte identity, exact current
source hashes and zero errors/undefined references/overfull boxes. The subject
index has373records. Root inspected changed manuscript pages28--30 and165--167,
including the corrected reference on166; source pages3,5,13,14 were inspected
separately. This root inspection is not attributed to the text-only Kimi call.

Source images, extracted third-party page text and their native copied streams
are retained under private/audit/2026-11-11-deterministic-source-images/, covered
by the existing private/ public-export exclusion. The completed expanded
attempt was relocated byte-for-byte; its public reports/receipt remain here.
Raw native reports/receipts are preserved rather than rewritten to hide failed
attempts, lower confidence, runtime paths or unread image limitations.

## Integration after concurrent book updates

The final build includes the other owner's committed Appendix F/G and Preface
updates. The reviewed damped-norm section and spatial module match the frozen
candidate exactly. integration-page-comparison.json establishes pixel identity
of all five reviewed manuscript pages between the337-page review render and
the345-page final integration. This is reuse of exact selected pages, not a
transfer of whole-document visual clearance. The unreviewed concurrent Appendix
G is outside this scoped adoption. Agent22's successor correspondence check is
still required; no accepted companion re-anchor is claimed here.
