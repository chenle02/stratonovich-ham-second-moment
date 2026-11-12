# Pairings mathematical review adjudication — DeepSeek attempt 01

Scope: the ten stable no-go IDs in candidate-v1/pairings.tex, not a whole-book
or rendered-page/source-image gate. The author is GPT; the independent reviewer
was the actual configured DeepSeek V4 Pro route.

Native report: PASS_WITH_NOTES, confidence high. Twelve checks PASS, including
one individually named check for each of NG-01,02,03,04,05,06,07,10,17,18,
plus source/application and scope. No fatal or major finding, and no mandatory
repair. The native exported session verifies provider deepseek, model
deepseek-v4-pro, finish stop, and no tool use. See collection.json and the
unaltered private native export and explicitly derived public metadata/text view; the report is not a supervisor-authored judgment.

## Minor findings

1. **Unprovided homogeneous-norm lemma.** Agree with the limitation. NG-01
   itself proves a numerical-majorant statement for an arbitrary K>0, so its
   obstruction does not require reconstructing that upstream lemma. The
   surrounding model majorant remains the existing P:envelope result supplied
   in full. The report also mentions NG-06 here; NG-06 instead follows directly
   from spatial-box counting and temporal integrals, with no N1/N2 input.
   No target change is required.
2. **Unprovided cross-reference targets and upstream construction.** Retain
   this limitation. The new no-gos consume the existing convergent expansion
   and named book results at their stated scope; the report does not become
   a fresh proof of every upstream dependency. Source and visual gates remain
   separate. No new mathematical defect or mandatory repair was reported.
3. **The bound 0<=S_{A,s}(w)<=1 is stated without a separate derivation.**
   The reviewer independently verified it. Directly, e^{-s(w-t)}<=1 in the
   displayed positive integral, so S<=e^{-Aw}+integral_0^w A e^{-At}dt=1;
   nonnegativity is immediate, including A=0. This is an optional expansion,
   not a missing hypothesis or an alteration needed to make the claim true.
   Preserve the reviewed source unchanged pending the second review.

## Custody and limits

The target and figure match the frozen hashes. Concurrent main-book changes
added backward references and changed chapter placement; no supplied proof
was changed. A finite-chapter excerpt diff is retained separately. This is
mathematical component evidence only; it does not promote historical grades
or certify source images, full argument closure, or rendered typography.
