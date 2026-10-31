# GL1-GL3 pre-proof falsification and exact scopes

UNREVIEWED statements. Named obstructions: wrong head density/half action;
missing finite-J normalizer/entropy; unbounded-head local constants;
incorrect polynomial cutoff; residual-only restart; false original point
upper or raw Hilbert-valued Gaussian. Original goal not narrowed.

Executed check-gaussian-head-v1.py locally via uv/mpmath:
18finite radial tails at40/70digits (J1/2/4,delta1/.25,nu1.5, weightC0/M1
orC1/M16,32), precision-relative differences<1e-25. The SAME evaluator at
C0 has6independent chi-square survival calibrations, including J2 exact
logtail=-M²/(2delta). It uses full radial density, endpoint-shifted exponent
and derivative-scaled integration variable to resolve tiny tails; no
clipping or omitted tail. Quadrature to infinity is noncertified, no
rigorous enclosure/operator/CM/SPDE computation. Tests compare the proposed
logmajorant Jlog2-M²/(8delta) only when the cutoff condition holds.

4residual Gaussian NORMALIZER integrals, J1/2/4/8 at40/70digits, independently
recover2^J from c_J int_0^infinity r^(J-1)exp(-r²/8)dr. This is the remaining
Gaussian quadratic after the density split, NOT an admissible nu2 SPDE
case. No factor2^J may be dropped without accounting for deltaJlog2.
4exact entropy examples delta1/n,Jn retain normalizedlogfactorlog2; they
refute discarding this bound along an arbitrary rank diagonal, not the
underlying operator theorem along every such diagonal.

9exact HALF-ACTION algebra rows compare maxima of2bphi-gamma phi² for
b.5/1/2,gamma.5/1/.25. Only gamma.5 gives the variance-delta Gaussian MGF
rate2b². This compares exact algebra with the elementary Gaussian formula;
it is NOT a separate numerical MGF integral. The actual density calibration
is the C0 radial evaluator above. Positive-action density divergence is
analytic, not a hard-coded integration result.

Exact wrong-cutoff witness M=x=C1,nu1.5 gives lhs1/2>rhs-1/4 for the
planned finite density split.8exact polynomial threshold rows use nu5/3,
C1=1,M0=512: cutoff ratio=2B^((m-15)/3). m18 grows, wrongm12 decreases.
These coefficients are calibration examples, not actual T_R norms. Empty
head J0 tail0/bulkprefactor1 is a convention, not a radial integral test.

The proposed finite tail lemma is fenced, not proved/compiled yet. All
actual source/restart, cutoff derivation, Gaussian integration, conditional
law and iterated limits remain full proof obligations. Root caught and
corrected a provisional M0-label mismatch BEFORE packet freeze; current
script/table consistently use512, not8. No independent-run count inflated.
No original POINT/sourceconstant inference from scalar controls; strict
r<2/a and the white fixed-smooth-projection uniformR guard remain.
