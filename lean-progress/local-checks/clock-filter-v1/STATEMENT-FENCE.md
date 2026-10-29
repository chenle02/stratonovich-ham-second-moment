# Isolated Lean filter audit: statement fence

User2026-10-29: "You may use Lean verification to alleviate the review burden."
This authorizes local verification. The audit needs no new repository/package,
lease,registration,shared-package edit or cluster job. Companion creation
remains a separate PROJECT-GOAL decision4;this is a standalone local pilot.

Lean4.35.0/Mathlib56a005855ea17e0b0958f73ec801ae140b0a1679,matching Agent8's
existing packages. Official GitHub release API checked today:Lean and Mathlib
latest stable tags are v4.35.0. No toolchain/dependency source is modified.

These are the only three target statements. Objects/hypotheses are fixed.
They specialize the already independently reviewed mathematical proof at
sourcee68310f,C1c/C3;source/model correspondence remains separate.

(1) Real resolvent algebra
For theta>0,lambda>0,r real:
(2theta+lambda)/[2theta(theta^2+r^2)((theta+lambda)^2+r^2)]
 = [1/(theta^2+r^2)-1/((theta+lambda)^2+r^2)]/(2theta*lambda).

(2) Pointwise filter
For theta>0,lambda>0:
0 < 2theta/(2theta+lambda) < 1.

(3) Actual conditional measure-theory consumer
sigma is ANYnonzero Borel measure on Real (NOT assumed finite),
supported almost everywhere on positive lambda.
w:Real->Real is integrable against sigma and positive sigma-almost everywhere.
theta>0.
Conclude:the filtered function [2theta/(2theta+lambda)]*w(lambda)
is integrable against sigma,and its integral is STRICTLY below integralw.
Filtered integrability must be DERIVED,not assumed. No desired strict
comparison is an input. Zero/oscillating-density exceptions are handled by
the explicit positivity/nonzero hypotheses,not silently excluded.

Actual paper correspondence:
sigma = volume restricted to Ioi0,not the spatial spectral measuremu.
w=w_thetafrom E:cross-clock-lambda-weight;C1proves its positivity/integrability.
The generic theorem permits this infinite measure. K and J1representation,
Brownian/Gaussian limits,spatial homogeneity and SPDE facts remain outsideLean.
A separate correspondence check must discharge these actual model inputs.

Local source/pin API search found and will REUSE:
Integrable.mono_nonneg,integral_mono_ae,integral_eq_iff_of_ae_le,ae_neBot,
and measurable arithmetic at the EXACTMathlibpin. Registry queries were
partial (earlier Agent8coordination);no global absence claim or new library.
Private goals are not sent to external semantic search services.

Acceptance for this pilot:
capped local Lean elaboration from frozen owned bytes;exact printed public
types;live transitive axioms subset{propext,Classical.choice,Quot.sound};
semantic wrong-filter/normalization controls;fresh OWNEDsource replay using
unchanged pinned dependency cache. No official lean-pkg/full-package/whole-
paper/formal-SPDE claim. Preserve every failed attempt and exact inputs.
