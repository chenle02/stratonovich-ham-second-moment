# Semantic controls

WrongHolderThreshold uses H3/4,theta5/8,p12. It satisfies the weaker1/(H-theta)<p
but the ACTUALmidpoint gamma gives negative dyadic margin. This tests this
midpoint selection, not a necessary moment condition for every Holder proof.
MissingSpatialCount uses a1/2,p6 and forgets one of the two box-index factors;
it rejects the claimed positive sufficient union-bound exponent. It does
not say the actual Gaussian maximum fails to shrink at p6.
WrongGaussianExponent uses u=v1,z1/2 and replaces the harmonic Gaussian
parameter by the arithmetic sum. It resolves the actual mixC definition.
MissingGaussianNormalization uses the generic positive-Pprefactor at P4,u=v1
and omits1/sqrt(P), giving2ratherthan1. P=pi is the analytic specialization;
this is an abstract prefactor identity control, not a physical pi sample.
NegativeLogFactor uses L=-2 in the variance identity after dropping L>=0.
It is an abstract domain control; the actual L(h)=1+|log h|is nonnegative.

All five resolve imports/names and fail on False. The failed redundant tactic
and duplicate setup preflight are not mathematical controls or reviews.
