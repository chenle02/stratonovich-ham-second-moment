# U1-U5 falsification/calibration report

Target frozen before execution, then exact block-factor v2 clarification.
The evaluator uses the ACTUAL d1 white spatial covariance H_sp=L2 with
Gamma=delta0,alpha1 (e.g.a1/4,s3/8,beta1/8). This is a lawful original
model, but only spatial rows for selected states are measured.

white-row-controls-v1.json:24physical masked rows over R1/2/4/8,centers
0,R,1.5R and two physical/Fourier resolutions. Real Gaussian states are
normalized by the WHOLE-SPACE H1/2 Fourier integral evaluated at35/65digits.
Physical mask is compact smooth eta_R^2 ONCE, not a mask on noise labels.
There are12resolution pairs and2unmasked exact Gaussian calibrations.
Max unmasked cutoff-tail relative error decreases .00364174 ->.00071284;
max masked tail absolute resolution change .000126456. Free Parseval
and heat-difference Gaussian identities agree within stated floating
assertion tolerances; these are floating calibrations, not enclosures.

Tail integrals use partially weighted frequency boundary cells; no periodic
state problem replaces R. Finite Nyquist and spatial discretization errors
are not rigorously enclosed. The tested scaled tail ratios remain bounded
(max frequency .437961,heat .357424); no operator supremum, all-Gamma or
Gaussian exponential conclusion follows. No clipping/singular sampling.
The experiment does not prove U2; it found no counterexample in this family.

hilbert-extension-controls-v1.json:24EXACT rational r4 tensor cases with
rank-one/diagonal/rotated diagonal time operators and1/2/5/11Hilbert
coordinates, including aligned equality cases. Three Gaussian fourth-
moment formulas are exact algebra, not Monte Carlo integration. Three
orthogonal-spatial input/output separations are computed through the
same evaluator (not hard-coded outputs) and remain unchanged with dimension.
The separation section was corrected before final retention to actually
compute the advertised distances; the code was rerun for that new check.
No full infinite-dimensional theorem or fractional C_t simulation follows.
A sqrt(dimension) upper may be true but is too loose; the experiment does
not falsely label that upper mathematically refuted. Scalar compactness
tensor infinite identity still must NOT be called compact.

No new Lean declarations or source/model narrowing. Gate decision:
SURVIVES THESE TESTS ONLY. Proceed to a complete UNREVIEWED analytic
candidate from existing accepted inputs; freeze for independent review
before adoption or a substantial successor. GC/SP review gates unchanged.
