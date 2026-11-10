# Local phase evolution: selected source comparison

Author reconnaissance,2026-11-02. This compares specific displayed statements,
not complete source proofs. It is not a novelty or publishability clearance.
The proposed local evolution remains unproved. Original p2 goals and all final
verification requirements remain intact.

## What the closest statements already provide

The published CDST paper, DOI10.1093/imrn/rnad039, has the following interfaces
in its typeset advance-access PDF (printed1-54):

- Theorem1.1,pp2-3, and Corollary5.7,p47: dimensions1/2 and, under spatial
  homogeneity, alpha0+alpha_cov<rho_d, with rho1=1,rho2=1/2.
- Definition4.2,p27: a time-Hölder displacement path in weighted Besov spaces,
  with time-dependent weights. This is not our unweighted local phase topology.
- Proposition4.4/(4.4),p28: explicit inequalities among noise Besov loss,
  solution regularity, time regularities and integrability.
- Notation4.7/Theorem4.8,p36: initial data in global H^(1+kappa_s)xH^kappa_s.
  CDST's kappa_s is a spatial regularity parameter, not our time-growth exponent.
  Its alpha_B is a Besov noise loss, not the covariance order alpha_cov.
- Equations5.3-5.7,p42: an integrated fractional Gaussian field and a coupled
  dyadic spatial spectral truncation, not our heat/Laplace approximation as written.

Chen's retained current author version, SHA5f7385ca...b97b6c, sets data(1,0)
and literal covariance |t-s|^(-alpha0)Gamma on p2. Theorem1.1,pp2-3, gives
canonical random-field existence under its spectral condition; Definition2.1,
p10, specifies its mild solution. This is already existence at the full
original homogeneous range alpha+alpha0<2. Its necessity statement concerns
square-integrable solutions admitting the stated Stratonovich expansion;
it is not a necessity theorem for every possible local distributional flow.

## A concrete source-range test

Take d1, spatial Gamma=c delta0 with c>0, and alpha0=1/2. The covariance
order is alpha_cov=1. Our original range admits it because1+1/2<2.
The CDST homogeneous Gaussian corollary requires1+1/2<1, which fails.
Its Theorem1.1 spectral criterion also fails: the spectral measure is a
positive multiple of Lebesgue measure, while its decay power is
rho1-alpha0-eta=1/2-eta, insufficient for integrability at infinity.

Therefore the displayed CDST hypotheses do not directly cover this test
case. This does not prove that our prospective theorem is new among all
literature, or that no adaptation of an existing proof can cover it.
The old source's smoother global data assumptions also do not directly
contain all local Hhalf x HminusHalf data, but improved initial-data estimates
and standard local patching may already be available in the overlap range.
We must not sell an easy localization corollary as a new theory.

## The exact possible residual

Known canonical existence is not our contribution. A candidate additional
object is a common-original-W continuous linear evolution for all local
phase data, with fixed-compact/horizon random seminorm bounds, cutoff
overlap consistency, composition and a precise regularization class.

The first analytical input is the actual Gaussian interaction operator
construction in weak phase at the original roughness range. Generic Young
machinery can be applied once that input exists. A nonanalytic wave group
prevents a direct analytic-semigroup substitution, but does not rule out
an interaction-picture reformulation inside standard Young theory.
Thus the new content must lie in the rough-Gaussian driver and its
correspondence/uniform estimates, not in calling an equation a Young equation.

No unmasked bounded operator on global Hhalf x HminusHalf is proposed.
No local Hhalf point trace or automatic point-moment equality is available.
Local flow agreement with the canonical solution must first be stated after
compact smooth testing. Define finite propagation by the exact initial-data
and same-W cutoff-overlap statement needed; do not silently assume a universal
noise-locality theorem for arbitrary unrelated realizations.

## A normalization bridge which cannot be skipped

CDST's displayed integrated covariance is

  R_a(t,s) gamma_CDST,
  R_a(t,s)=(|t|^(2-a)+|s|^(2-a)-|t-s|^(2-a))/2.

Off the diagonal its mixed derivative is

  c_a |t-s|^(-a) gamma_CDST,   c_a=(1-a/2)(1-a).

For0<a<1 this coefficient is positive. To match our literal physical
covariance |t-s|^(-a)Gamma, the displayed convention requires

  gamma_CDST=Gamma/c_a,

or a factor c_a^(-1/2) on the integrated input when keeping gamma_CDST=Gamma.
At a=1/2, c_a=3/8. Local Sympy verifies this off-diagonal coefficient only;
distributional derivatives, boundary behavior and actual same-W identification
are still analytic obligations. This is a comparison of conventions, not a
proposed correction to a source theorem, and changes no current manuscript
normalization, original Gaussian cost or derived constant.

The CDST spectral approximation and our retaining sources must also be
coupled correctly. Matching Hurst parameters or marginal laws is not enough
for pathwise same-noise convergence. Spatial spectral truncation may destroy
physical covariance nonnegativity, so positive-diagram arguments must not be
transferred without checking their actual hypotheses. That issue need not
prevent a Gaussian operator-convergence argument, but such an argument is
still to be supplied.

## Dependency and next-step boundary

Actual explicit-reference traversals from P:actual-operator-driver,
P:source-ordinary-response and P:constant-gaussian-flow reach respectively
26,34,36proofs and no T:full-upper, P:variational-positive-scores or final
T:intrinsic-second-moment. Their source files match original science887fbfbe.
This supports independence from the final asymptotic theorem, but is only
syntactic evidence; unlabelled setup remains to be audited.

A useful next bounded target is cutoff-overlap consistency: prove equality
for the SAME ordinary source on a fixed backward cone, then pass it through
fixed-mask operator convergence before any local gluing. Countability,
physical strong continuity, both phase components and the exact solution/
approximation class must be handled. No overlap lemma or local evolution
is declared proved by this comparison.

Decision: REFRAME candidateI around actual local wave construction and
correspondence. Continue bounded statement/interface checking, while full
source/novelty review remains open. Do not open an expensive proof wave,
create a new companion, or promise a separate paper on this evidence alone.

## Edition repair and evidence

The exact identity repair ticket
`tk-20261101-190012-codex-stratonovich-reference-identity` is terminal PARTIAL.
On <HUB>, All_PDFs and Papis now both have the correct54-page published
PDF SHA13be3be8...ea5bf0. Partial status is from inherited wiki digest checks
(verify-digest MAJOR), not a failed PDF identity repair. Old wrong/preprint
bytes were preserved by the writer. Local canonical copies still carried
the old hashes at our observation; correct external project source copies
remain available. No direct corpus overwrite or false local sync claimed.

[Exact crosswalk, selected source images, archive and repair receipt](../reviews/2026-11-02-local-phase-source-crosswalk/crosswalk.json)
and the [symbolic normalization check](local-phase-flow-normalization-check-v1.json)
retain pinpoints, hashes and scope. Seven primary images were displayed by
the author. This is not independent source review or full-paper reading.
