# Joint tilt: four finite algebra consumers only

Pinned latest stable Lean4.35.0 and Mathlib tagv4.35.0, commit
56a005855ea17e0b0958f73ec801ae140b0a1679. Official release/tag queries are
retained in reviews/2026-10-30-joint-gaussian-tilt/lean-release-preflight.json.
The public web tool refused with token_revoked; direct public official
GitHub API reads verified the releases. No auth/runtime change was made.

No generic Gaussian/Young library is built. Existing direct-event and
interaction-driver real-power consumers were inspected; the actual present
amplitude quotient and tilt covariance/cost polynomial were not in those
finite types. Use Mathlib ring and Real.rpow_add/sqrt_eq_rpow directly;
no nontrivial new definition or library API is needed. Donor dependencies
were read-only, namespace guards checked, output isolated, no new package,
lease, registry transaction, companion or cluster. Latest-release Mathlib
pin equals the existing reviewed donor pin; no migration was required.

Four kernel deductions:
- tilt_exponent: cancellation with covariance c, variance parameters v,w
  and r,s real. It is a polynomial identity, NOT a Gaussian MGF theorem.
- wrong_sign_error: the incorrect plus-density polynomial leaves 2rsc.
- wrong_cost_error: the incorrect full-cost polynomial leaves -s^2v/2.
- shifted_amplitude: for delta>0 and any real a, the actual real-power
  quotient g delta^(a/2)/sqrt(delta)=1. No target scaling is an assumption.

All compile cleanly, show exact public types and the standard three axioms,
and replay from fresh owned source/output directories. All five owned
output hashes agree. Three numerical altered-statement controls reduce to
actual unsolved False goals; no unknown APIs or setup errors. Raw41member
archive retained and hash/member verified. These are local development
checks, not native package/Comparator or formal Gaussian/SPDE acceptance.
Independent statement/type/application review remains PENDING.

Analytic boundary: Gaussian closure/laws, Banach Borel measurability,
raw profile convolution/clock/covariance identity, Young assembly/flow,
source limits, canonical average/point transfer, and every spectral/event/
constant issue remain outside these finite Lean deductions. See the
candidate notes/joint-gaussian-tilt.md Sections1-6.
