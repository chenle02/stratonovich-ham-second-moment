# Local clock-filter verification

Three conditional statements in StratonovichHAMAudit/ClockFilter.lean compile
with Lean4.35.0 and Mathlib56a005855ea17e0b0958f73ec801ae140b0a1679.
No new package or repo was created. Dependencies are reused read-only from
the existing coefficient-convolution package coordinated with Agent8.

The exact statement fence precedes development. Attempts1/2 failed respectively
on a reserved binder and the orientation of the final proof term. Neither
failure changed any hypothesis or conclusion;all snapshots are retained.
Attempt3 and a fresh owned-source replay pass. Audit prints the public types
and their transitive axioms,exactly the standard three. Three intentionally
false normalization/filter/zero-measure claims fail with an unsolved False,
not import/setup failures. The third confirms why the nonzero-measure premise
matters for strictness. No extra finite-measure premise was introduced.

Evidence files map only filesystem prefixes to explicit LEAN_BIN and
DEPENDENCY_ROOT parameters;original/portable SHA pairs are retained. The raw
local execution records remain outside the committed portable evidence.
No dependency source or compiled dependency artifact is changed. This is
local verification,not an official package trust gate or Comparator replay.
The mathematical model's representation and density hypotheses remain outside
Lean. Independent exact-type/application correspondence is pending.
