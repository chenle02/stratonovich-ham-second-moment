# Assigned task: seven rewritten compact-mean-family proofs

Independently compare BOTH OLD and NEW complete proofs and their unchanged
statements/definitions in the assigned module. Check that each argument is
preserved, no step or qualifier is lost, and every new explanatory assertion
is justified under the same hypotheses. Mechanical byte retention is not
mathematical evidence. Distinguish a defect introduced by the rewrite from a
pre-existing concern. Do not use OLD as an oracle, silently repair a proof,
or certify a whole book.

The assignment is exactly the seven proof labels in the inventory, in order.
Read every complete OLD and NEW proof, including unchanged portions. The
baseline context sources supply explicitly UNASSIGNED upstream statements
and definitions. Their proofs are NOT assigned for a new review and must not
be counted as extra proofs read. You may use those named upstream statements
under checked hypotheses, but may not invoke an assigned target conclusion
or its counterpart to skip reconstructing that target's own deduction.

Reconstruct the assigned deductions with checkable public equations and
estimates, rather than label assertions. Check every inserted mathematical
explanation against the actual OLD argument and the supplied hypotheses.
In particular check the following, without treating this list as a substitute
for the complete seven-proof read:
- The real nonnegative compact smooth potential family on one fixed compact
  support, continuous in the stated topology, with a single unit H1 negative
  trial of margin epsilon. Distinguish family parameter sigma from propagation
  time. Check the closed form domain and H2 operator domain; spectral bottom
  below the essential threshold before invoking the imported simple-positive-
  ground-state theorem; max-min at the essential threshold; uniform energy
  and rate gaps; normalized positive ground-state L2 and H2 continuity.
- Resolvent variational order and the square-root integral, quarter-power
  domains, uniform phase-norm equivalence and the negative completion by
  duality. Do not replace scalar/eigenvalue comparisons with an unsupported
  rule for arbitrary noncommuting operator powers.
- Every weighted wave-matrix entry on positive, zero and negative spectrum;
  include the mu=0 case. Removing the growing ground phase branch leaves the
  decaying branch. Preserve both ground copies and all uniform projection
  bounds. Check the graph-level derivative, spectral cutoffs, Duhamel/Picard
  identification and strong versus operator-norm topologies; E is not dense
  in F.
- The full F=E plus two constant coordinates, both constant-data columns and
  their coupling into E. Derive the variation-of-constants block formula and
  its E-valued Fubini justification; compute the constant dual using both
  exponential integrals and the shifted tail. Verify eigenprojection identities,
  continuity and strictly positive integral margins without assuming the
  ground state is L1 or using a point trace.
- The exact complementary F forcing, including its subtraction/tail term,
  polynomial contribution of constant velocity, cubic convolution bound and
  strict eta<d0 normalization. Check finite-horizon potential dependence from
  statewise Duhamel differences and measurable operator norms, without an
  operator-norm derivative of the free group.
- Original nonnegative nonzero smooth compact spacetime control Psi, with no
  separability assumption; original noise variable and covariance amplitude.
  Derive the mean, finite strictly positive covariance cost and time-uniform
  mean floor using positive Radon pairings/homogeneity. Distinguish a
  nonnegative nonzero lower spatial profile from a strictly positive covariance
  cost: do not assert global pointwise positivity of that profile. Obtain
  regularity by differentiating the compact test, not the singular time kernel.
- The dilated unit trial, exact Radon versus Lebesgue scaling factors, compact
  mask plateau, L^(-alpha) potential lower bound versus L^(-2) kinetic energy,
  fixed finite radius before applying the family results, rate Lipschitz
  denominator and positivity at sigma=0. Preserve the original Psi, W(Psi)
  and variance when the trial/mask grow. Do not turn this into all-strength
  binding for one fixed compact potential, uniform growing-radius path bounds,
  or an exchange of source and time-asymptotic limits.

The module retains its explicit imported source statements/references. This
is rewrite-preservation review, not a new verification of primary Teschl or
Young-source PDFs, source images, Lean correspondence, rendered pages or
human sign-offs. Check target application hypotheses against the supplied
stated inputs and identify any missing context honestly. Fourier/Bessel and
Sobolev conventions are supplied in the raw context; do not silently change
normalizations or domains.

List any AUDIT-worthy issue found. No prior reviewer verdict, worker QA,
grade or acceptance record is supplied. Do not browse, run tools, delegate,
read other files, edit, contact anyone or launch an authoring workflow.
Everything allowed is embedded. Mark PARTIAL/NOT_READ and precise missing
work rather than inventing a completed read or an unsupported mathematical
claim. Honest failure or inconclusiveness is permitted.

# Public reconstruction requirement

For every assigned proof, enumerate its original logical steps (including unchanged portions) and provide checkable public working for each. A target statement or a bound established inside that same target proof is not an unassigned input. Named UNASSIGNED upstream statements may be used after checking their hypotheses; their own proofs remain unassigned. Reading and reconstruction are distinct: if any required target step is not reconstructed publicly, say so and mark Public reconstruction: PARTIAL or NOT_RECONSTRUCTED, even if Old/New reading is COMPLETE. Do not replace a derivation by saying it is unchanged.

# Output contract

Begin with:
# Review Result
Category: proof-readability-equivalence
Model: <your actual model identity if known>
Verdict: PASS | PASS_WITH_NOTES | FAIL | INCONCLUSIVE
Confidence: high | medium | low

Verdict/confidence are unforced. Then exactly one '## <proof label>' section
for each assigned label, in inventory order. Each must give:
- Old reading: COMPLETE | PARTIAL | NOT_READ
- New reading: COMPLETE | PARTIAL | NOT_READ
- Public reconstruction: COMPLETE | PARTIAL | NOT_RECONSTRUCTED
- Original-step coverage: <steps and working, with omissions explicit>
- Argument preservation: PRESERVED | CHANGED | UNCERTAIN
- New explanations: JUSTIFIED | CONCERN | UNCERTAIN
- Evidence: concrete mathematical checks/working using equation labels or
  OLD/NEW module-local LF ranges, not merely byte-retention facts.
- Lost steps/qualifiers, unresolved issues and pre-existing concerns; 'none
  identified within this read' is allowed when justified.

End with '## AUDIT dispositions' and '## Findings and limits'. A partially
read proof prohibits a claim of full assignment completion. Distinguish target
argument preservation from proving all upstream analysis or whole-book truth.
Keep the public report roughly 5000 words. Do not certify primary
source PDFs/images, Lean quotation correspondence, rendered pages, human
verification or release.

The word target is approximate; do not sacrifice a required derivation for brevity.
