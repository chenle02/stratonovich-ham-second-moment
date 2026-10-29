# Bounded internal lower-comparison wave: REFRAME

Date2026-10-29. Previous goal turn:PROGRESS (fresh cold7collected/adjudicated,
published pinpoints checked,exact critical-path binding and proof map saved).
No live reviewer remains. Original full G:upper has been reported at its
primary gates;the continuing user goal explicitly includes pursuit of G:sharp.
This wave addresses a bounded internal corollary toward that unchanged goal.
It is not paper promotion,novelty certification,Lean creation or circulation.

## Exact candidate statements

Fix any NONZERO covariance in the original H:homog class,d1--3 and alpha<2.
Put nu=3-alpha,kappa_st=(4-alpha)/nu,a_max=min(1,2-alpha). For0<a<a_max,
let u^(a) be the canonical fractional-time solution;let U=u^(0) be the
canonical static solution with the SAME spatial covariance,data(1,0).
L0 is the ACTUAL static first-mean growth rate,without a numerical formula.

A. Candidate all-a partial lower bound:
liminf T^[-(4-alpha-a)/nu] log E[u^(a)(T,x)^2] >= 2^kappa_st*L0.
This does NOT replace the original2^kappa_st*L_*(a)target.
B. Candidate near-static strict gap from the actual Jensen rate:
for each fixed b in(0,a_max),there is a_star in(0,b] such that for0<a<a_star,
liminf T^-kappa(a)log E[u^(a)^2] > 2limsup T^-kappa(a)log E[u^(a)].
No E|u| first-moment or full-p intermittency theorem is claimed.
C. Auxiliaries:positive Wick comparison,raw-time coefficient Holder and an
elementary positive-entire-series type lemma. Treat these as classical
inequality consequences,not independently novel theorems.

## Exact source/implication crosswalk

| Candidate | Closest checked input | Map and residual | Disposition |
| --- | --- | --- | --- |
| A | Published Chen--Hu2025Th1.2(1.9)p2147 | Source time exponent isZERO;sourcep=1,2 gives ratio2^kappa_st. Positive temporal-minimum comparison and exact static amplitude/time scaling are the remaining bridge for a>0. | Internal corollary candidate;not direct same-parameter subsumption or novelty claim. |
| B | A + current full upper + static sourcep1law | Mean coefficients at0,a,b share the SAME spatial positive pairing measure. Holder with exact raw powers and series-type control may give continuity at0strong enough for a strict gap. | Bounded consequence candidate;missing analytic steps must be proved/reviewed. |
| Finite-order limits | Our L:spatial-wick-measures/L:joint-fixed-order;static Chen--HuTh3.8(i)p2165 | All original Radon covariances,unequal/empty chains,Green before noise. No source2026Th4.1black box needed. | Existing independently reviewed construction input. |
| Source2026first moment | Current authorTh1.2p3,not arXivv1 | Bracketed first-mean law;printed normalization unresolved. No constant from it enters A/B. | Context only;does not directly prove p2gap. |
| Balan--Conus/Hu--Wang | Existing corpus identifies Skorohod setting | Their kernels omit the Stratonovich self-contractions. No target theorem substitution or adaptation is developed here. | Comparison only;no sibling development. |

Static source convention/class directly checked in prior scoped source audits:
p2145standing class;p2152Eq2.18generalized covariance;p2165fixed order;p2150
Eq2.10series and p2171L2convergence;p2147Eq1.9moment law. Original numerical white constants are NOT
adopted. L0>0 follows from the nonzero-covariance Gaussian variational test
and scaling;L0<infinity and the structural p-law are the labeled source input.

## Recon coverage and limits

Local wiki/project/source crosswalks and published static theorem passages
have been checked. A fresh supplemental web pass used exact Stratonovich/
hyperbolic/strict-intermittency/static-comparison queries plus MathSciNet and
zbMATH domain queries. It returned the same published Chen--Hu primary PDF
and adjacent metadata;NO authenticated MathSciNet/zbMATH citation-chain access
or exhaustive citing-paper audit was obtained. Novelty remains UNVERIFIED.
Primary landing link:https://web.math.utk.edu/~xchen3/aop1758.pdf.
No new useful absent paper was authenticated;existing nine future-reference
requests persist,no duplicate intake. No messages/contact/publication.

Decision:REFRAME narrowly as the above INTERNAL corollary/inequality wave.
This is the existing near-static reconnaissance made exact,not a new paper
investment. Freeze a small source-bound proof packet and obtain the required
cross-family HIGH review. The skeptic should test whether the published
inputs already imply it and retain that possible subsumption. No polished
paper,formalization or novelty claim is opened. If the comparison/Holder
limit fails,record the exact failure and stop that shortcut.

## Falsification and scope traps

Existing exact controls:20clock scalings,84white order2Holder cases,40gap
windows. New white order4mean check uses all THREE one-chain pairings with
spatial weights r1*r3/4,r1*min(r2,r4)/4,r1*min(r2,r3,r4)/4. The static sum must
be11/17280. Test raw-power Holder numerically without exponent-dependent
Laplace-cutoff normalizations. These are diagnostics,not analytic proofs.

The static covariance minimum is a VARIANCE scale T^-a,hence NOISE amplitude
T^(-a/2). Gaussian coupling/PSD order of a difference is not assumed;use
entrywise positive Wick integrals at common spatial smoothing. Define the
a=0endpoint by the static model,never Gamma_E(0). Entire-series reasoning
uses coefficient LIMSUP,not an unproved coefficient limit. The new p1/p2gap
concerns Eu,not E|u|,and is only near-static. Original full G:sharp remains open.
