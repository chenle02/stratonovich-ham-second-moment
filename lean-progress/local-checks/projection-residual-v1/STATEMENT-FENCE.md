# Projection-residual scalar fence

Standalone local verification under Le's existing authorization; no new
companion, package, lease, registry, donor write, cluster or Comparator gate.
Reuse the current exact Lean4.35.0 / Mathlib56a005855ea17e0b0958f73ec801ae140b0a1679
pins and read-only dependency cache, with owned outputs.

Two paper-specific scalar facts: the ACTUALbound
20000/1932951+1/96 < 101/(3200*sqrt(2)), and its affine tilted-coefficient
consumer for arbitrary real q,p with p at least that lower bound. The desired
gap is not assumed. Existing Mathlib real sqrt/order/rational tactics suffice;
this is not a new generic library theorem. No custom axiom or sorry.

Outside Lean: the original Gaussian field and test-profile projection,
Hilbert/Loewner positivity, cone profile bound and actual first-coefficient
integral, Gaussian density, Stratonovich tail/remainder and full means,
finite-rank asymptotic lower bridge. Independent type/application review
must match the scalar constants to these analytic reductions. No full sharp
or all-tilts impossibility claim. Finiteness under q tilt requires1<q<2,
although the scalar affine identity itself is valid for all real q.
