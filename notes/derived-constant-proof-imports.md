# Proof imports for derived-constant integration

This is an audit of import interfaces, not a new proof, a whole-paper
review or a certificate that the dependency closure is complete. It refines
the earlier19-source starting inventory. The current user target remains
the actual all-model asymptotic constant; agreement with Chen is optional.
The accepted PB/OC/WS result set remains frozen.

## Findings that change integration

1. The Gaussian upper proof uses SA through an alias rather than a literal
   filename. SA is `radius-stochastic-driver-anchor.md`, scientific8cf62b0.
   The starting inventory omitted it. Its radius-explicit first-driver
   moment is necessary for the typical Gaussian ball to shrink at growing
   mask radius. Fixed-radius driver estimates alone do not supply that step.
2. The spatial product foundation B uses the already established independent
   canonical full upper bound for finiteness. UL likewise uses that old
   upper bound. They must precede the new signed-score upper UR and the
   exact-limit assembly PB. Using PB to justify their finiteness would make
   the integration circular. The declared graph respects this order.
3. A filename mention can denote a narrow calculation rather than an entire
   model theorem. TE imports only the temporal equilibrium identity through
   its equation(4); GI imports only Gamma duplication and its scalar inputs.
   Their historical d1 stochastic consumers are not imported into d2/3.
4. S describes compact positive ground-family arguments as method comparators,
   but its actual full-F forcing calculation invokes CG Section5(14). This
   bounded-operator Fubini step belongs in the integrated proof. It does not
   require positivity or a ground eigenstate for a signed potential.
5. GC invokes the old fixed-mask Gaussian theorem for fixed-parameter
   finiteness, not its fixed-mask rate on a growing diagonal. The manifest
   conservatively retains that branch (GLF). FY Section4 already states
   all-finite-moment Young bounds under square-exponential Gaussian driver
   tails. A direct local finiteness argument could avoid importing the old
   fixed-mask upper machinery. That compression has NOT been adopted or
   certified here; verify the actual same driver and phase correspondence
   before removing the branch.
6. The final upper proof also needs the noise-only restart from GL Section2,
   retained as GR independently of GLF. It uses one common source and then
   the raw limit. Temporal block independence is neither stated nor needed.

## Proposed proof order and selected scopes

The following order is topologically valid for the declared scoped imports.
Acyclicity checks bookkeeping only. Complete selected proof bodies, external
pinpoints and actual application hypotheses still need integration checks.
Duplicate paths have intentionally different scopes (E1/EA and GR/GLF).

| ID | Source in notes/ | Own inputs | Selected scope |
| --- | --- | --- | --- |
| MAIN | `notes_stratonovich_ham_second_moment.tex` | base | Existing canonical mixed-order construction, crude vertex summability and independent T:full-upper; retain full existing proofs. |
| SF | `spectral-mask-covariance-foundation.md` | base | Sections1-4: actual covariance, translated spectral growth and temporal PSD/Schur. |
| FG | `finite-gaussian-schatten.md` | base | Theorem1 and complete finite proof; finite matrix statement, both variances. |
| TE | `damped-lower-endpoint-bridge.md` | base | Section2 through equation(4) ONLY: self-contained temporal equilibrium identity and its L1/L2 mass. No old d1 stochastic or rough-control consumer. |
| PG | `positive-gram-variational-comparison.md` | base | PG1-PG2 full finite analytic optimization; positive conic maximizer and ENTRYWISE Gram comparison, not just finite Lean algebra. |
| FR | `scalar-frequency-row-bound.md` | SF | Proposition1 and Corollary2, all original exponents; spectral measure has uniform translated growth. |
| TP | `temporal-phase-bound.md` | SF | Sections1-3: admitted indicators, temporal modulation and wave factors. |
| CC | `compact-sobolev-cutoff.md` | FG | Whole-space compact cutoffs, actual adjoints, finite Gaussian operator upgrade; no periodic replacement of states. |
| DS | `direct-event-calibration.md` | MAIN | Section1(S)-(M) ONLY: canonical law scaling, all original measures; later scalar calibration is not imported. |
| GI | `global-d1-damped-lower.md` | TE | Section3 equation(5) and named Gamma inputs ONLY: duplication from positive Beta integral, recurrence and Gamma(1/2). No d1 SPDE consumer or global Omega argument. |
| AV | `actual-two-variance-forms.md` | SF, FR, TP | Propositions1-2 and basis construction: actual forms and BOTH variance directions, not a random bounded operator. |
| AD | `actual-operator-driver.md` | AV, CC, FG, SF | Sections1-10: same-W compact-operator Holder driver, both tails and Gaussian moments, fixed mask/horizon. |
| SC | `source-operator-convergence.md` | AD | Theorems1-2, Gaussian contraction and given-W-retaining sources; ordinary first response. |
| FM | `fixed-mask-moment-transfer.md` | SC, MAIN | F1-F3: all mixed/unequal/empty chains; source-point limit and conditional raw average transfer. |
| FY | `fixed-mask-young-constant-phase.md` | AD, SC, FM | Y1-Y4: exact E plus two constants, Young growth/stability, source identity and closes F3 premise. |
| CG | `compact-mean-ground-family.md` | FY | Sections1-8: full-dimensional positive compact-family ground/gap, fractional phase, complementary full wave and common trial. |
| E1 | `upper-young-perturbation.md` | FY | Sections1-3 ONLY: dimension-free multiplicative Young perturbation, any bounded left factor. |
| RB | `raw-block-event-lower.md` | CG, AD, SC, FY, FM, DS | Sections1-9: actual common noise, raw half-cost, all full blocks/remainder and original point lower. |
| UL | `unmasked-variational-lower.md` | CG, RB, MAIN | Sections1-6: all positive nonseparable smooth controls, unmasked H1 rate and intrinsic score scaling; finiteness from independent MAIN upper. |
| GR | `upper-gaussian-operator.md` | RB, SC, FY | Section2(3) noise-only restart ONLY; does not use its fixed-mask upper rate. |
| B | `all-dimensional-static-occupation-bridge.md` | UL, TE | Sections2-5: smooth controls, positive finite R_sp, physical H1 four-linear extension and occupation class; temporal identity has no spatial restriction. |
| C3 | `upper-cameron-compactness.md` | B, CC, AD, SC, FY, RB | Sections2-7: actual fractional product and compact mean, tensor identification and raw supported-row covariance. RB use is its Section2 isometry only. |
| U | `uniform-e-cameron-regulator.md` | C3, SC, RB | Uniform-R spatial E means, temporal tensor bound and regulator tails; raw pullback only from RB Section2. |
| D1 | `upper-residual-exponential.md` | C3, AD, SC, FY | Fixed-mask residual exponential estimate and actual first-chaos realization. Retained conservatively for existing GL finiteness dependency. |
| S | `upper-signed-static.md` | C3, FY, CG | Sections2-5 rough signed form/spectrum/physical-wave identity. CG Section5(14) supplies bounded full-F forcing/Fubini calculation, not ground-state positivity. |
| SP | `e-phase-symplectic-baseline.md` | AD, SC, FY, C3, RB | Sections2-7, especially pure-mean and actual raw E norm baseline. RB Section2 pullback; no independent blocks. |
| SA | `radius-stochastic-driver-anchor.md` | CC, AV, AD, SC, RB, C3 | Sections2-6: radius-explicit compact envelopes and actual FIRST-driver norm tending to zero on the growing-mask scale. |
| EA | `upper-young-perturbation.md` | FY, C3, D1, SC | Sections4-7: fixed-mask nonlinear residual and conditioning consumers used in GL; distinct from E1-only scope. |
| BT | `borell-tube-rayleigh-transfer.md` | SA, C3, U, FY, SC, GR, SP | Full E-law realization, compact mean, closed control tubes, Rayleigh comparison, actual endpoint product and coarse bound. D1 method is explicitly rechecked in Section5. |
| US | `uniform-e-spectral-products.md` | C3, U, S, E1, SP | Sections2-8: actual rough signed E rate, uniform averaging, polynomial-radius mean product and arbitrary small residual. |
| MB | `upper-mean-block-product.md` | C3, S, E1, FY, EA | Fixed-mask mean-product proof used by original GL; not the later uniform-R E theorem. |
| GLF | `upper-gaussian-operator.md` | C3, D1, EA, S, MB, GR | Fixed-delta finite-mask moment finiteness portion of GL as invoked by GC. A direct FY Gaussian/Young deduction may remove this branch after correspondence check. |
| GC | `growing-cone-point-upper-transfer.md` | FM, FY, SC, RB, DS, GLF | Original canonical point/source-first/all-chain identity to actual E flow, polynomial data cost, fixed-delta finiteness and stationarity. |
| UR | `rayleigh-signed-moment-upper.md` | US, BT, GC, SA | Original point limsup bounded by growing-mask signed raw score; order delta then B, same endpoint at every B. |
| PB | `physical-signed-positive-score-comparison.md` | U, US, PG, UR, UL | PB0-PB5: actual raw labels, uniform optimizer norm BEFORE averaging, positive smoothing, signed score comparison and original exact point limit. |
| OC | `all-model-occupation-ceiling.md` | B, U, PB, UL, TE | Full occupation/H1 embedding and intrinsic constant ceiling; common spatial-energy bracket. Optional source-shaped strict gap algebra is separate. |
| WS | `white-spatial-evaluation.md` | PB, OC, B, GI | Full real unit H1 CDF-square proof, exact white spatial energy, Gamma-function bound evaluations and ratio; only d1 alpha1 for this example. |


## Review-input custody and exclusions

`reviews/2026-10-31-derived-constant-integration/review-input-custody-v1.json`
checks56 note-input hashes from six existing FULL review receipts against
their exact scientific Git revisions. All56 match. Fifty also match current
adopted files byte-for-byte; six reflect later adoption edits. Those six
are not silently certified by the frozen hash: retain and consult their
existing finding-by-finding adjudications and later accepted consumers.
This check neither reruns the reviewers nor creates new acceptance.

The PB receipt also contains `occupation-control-approximation.md` and
`raw-positive-value-ceiling.md`; OC includes `all-alpha-damped-lower.md`
and the latter ceiling note. These provide older d1 calibration/comparison
context and finite scalar provenance. They are not new all-dimensional
premises of PB0-PB5 or OC's common-spatial-energy bracket. Keep their
reviewed claims and boundaries available for the final calibration audit.
Do not erase them or promote them to unrestricted model statements.

Likewise, old d1 ODE, weighted-projection and spectral-complement notes are
method comparisons for the current compact-family proof. They do not
replace its full-dimensional proof. The same distinction applies to the
old separable raw-score construction versus the full nonseparable class.

The conditional finite Lean capsules retain their existing source, public
types, axioms, replay and application records. No new kernel run or theorem
is needed for this audit. Eighty finite facts across22 seams do not measure
coverage of the analytic argument and do not create an official companion.

## Concrete next work

Start the actual TeX integration with the covariance/variance/compact-driver
foundation and explicit source/Young identification, keeping the independent
canonical full upper available. Then integrate the lower event and UL,
spatial foundation and growing-mask Gaussian upper, finite Gram comparison,
and PB/OC/WS. All own imported statements need internal statements and
complete proofs; Markdown filenames are not substitutes for those proofs.

Use the existing110-page TeX/PDF as the build baseline. Define stable labels
for each integrated claim and bind them to these selected source scopes.
Inspect source/PDF correspondence and preserve analytic/formal boundaries.
Final whole-argument skeptic and independent cold reader remain mandatory;
this inventory does not clear publication, novelty, circulation or delivery.


## 2026-11-01 integration audit: fixed-parameter GC finiteness candidate

The conservative declared graph above is unchanged. The current C1-C3/E1
integration is accepted at scientific5e36bcb. A precise UNREVIEWED direct
application is frozen in
reviews/2026-11-01-uniform-e-mean-tex-integration/gc-finiteness-audit-v1.md.
GCSection2 uses GL only for finite moments at each fixed delta,R, while
the accepted F Gaussian Young-flow theorem and GC's exact isometric E
restriction appear to supply that property and source Lp differences.
The future GC gate must verify SAME driver/noise/mask/horizon and all
restriction/source guards before removing GLF. BTSection5 explicitly
rechecks D1Sections2-3 generic first-chaos/Wiener realization on actual E;
no norm-only concentration or finite-head consumer is silently imported
through that method reference. No pruning, new upper rate or proof-closure
certificate is adopted here. Current next U remains within the graph.


## 2026-11-01 BT checkpoint and direct GC interface candidate

Thedeclaredconservativegraphisunchanged. BT'sactualWienerrealizationand
noise-onlyrestartnowhavecompleteinternalTeXproofs,scientific37f322f,
actualOpus5.5HIGH26PASS511.526seconds. D1genericmethodiswrittenhere,
not itsnormexponentialtheorem; thealreadyinternalL:raw-block-restart
sufficesforGRinterfacewithoutGLrate. A futureGCapplicationcoulduseBT
coarseoperatorsecondmomentfiniteness atB1 forSAMEdelta,Rdelta,Wfast/gdelta,
replacingONLYGLfinitenessparagraph. Exactcandidate/guards in
reviews/2026-11-01-tube-transfer-tex-integration/gc-finiteness-audit-v2.md.
ThisisUNREVIEWEDasGCapplication, notanadoptedpruningorclosurecertificate.
Keepallhistoricalproofs/reviews andvalidatewholeGCsourcebeforeanyremoval.
