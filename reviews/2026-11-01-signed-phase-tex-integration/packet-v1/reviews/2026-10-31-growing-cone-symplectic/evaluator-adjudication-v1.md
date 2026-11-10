# Bessel evaluator repair

V1 exact matrices are Hamiltonian and the reported rational defects are
valid for those matrices, but their lower force used Lambda^-1 V Lambda^-1,
rather than the stated Bessel-coordinate Lambda^-1/2 V Lambda^-1/2.
V1 therefore does not calibrate the intended physical coordinate map.
Preserve script/results; no PDE/actual-application claim based on v1.

V2 sets the RATIONAL square root of Lambda to diag(1,5/4,5/3), defines
Lambda as its square and K=Lambda^2-I. Thus physical free frequencies
squared K>=0 match Lambda=(I+K)^1/2 EXACTLY, and the lower potential is
Lambda^-1/2 V Lambda^-1/2 with rational entries. Same-weight false guard
uses physical conjugation by Lambda^1/2 on BOTH coordinates. This is a
substantive corrected actual-coordinate evaluator, not a rerun to obtain
more favorable diagnostics. No spectral/PDE approximation is claimed.
