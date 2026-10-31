# Bounded private Lean reuse search

decision: reuse Mathlib at the exact established pin, with two small scalar
application lemmas; do not build any probability/integration library.

Two local registry/index queries: moment variance (22hits) and quadratic
inequality (8hits). All declarations/summaries inspected. Variance/moment
and quadratic-margin leads have different hypotheses/conclusions; none
is imported as this moment identity. Exact raw query output snapshots are
retained next to this record. Searches are INCOMPLETE: seven no-checkout
packages, and external Loogle/LeanSearch/Reservoir/Palomar/GitHub NOT queried.
No global or local absence claim. Do not expose unpublished formal goals
to external services. We found adequate DIRECT pinned Mathlib primitives,
so no competing foundational library/foreign package adoption is proposed.

At Mathlib56a005855ea17e0b0958f73ec801ae140b0a1679:
Algebra/Order/GroupWithZero/Basic.lean:1132 div_le_iff₀;
Algebra/Order/Ring/Unbundled/Basic.lean:608 sq_nonneg;
existing Mathlib.Tactic imports supply nlinarith,field_simp,ring,positivity.
Current package cache source pin checked; no dependency edit/upgrade/build.
Local existing scalar modules searched for sq_le_mul/mean-variance match:
no hit in those files. This does not establish absence in Mathlib/elsewhere.
The two proposed application headers/guards are in finite-fence-v1.md.

No registry/claims write, donor modification/build/lease/official package
or companion creation. Standalone local evidence only after statement gate.
