# Semantic controls

WrongEndpoint places s at the upper trace endpoint for b=3/2, so the
claimed strict2s+b<3 is false. This is the boundary choice, not phaseIndex.
WrongEnergy uses original WHITEalpha1,a1/2, for which the energy phase fails.
MissingHalf uses zero phases in the ACTUALcosine-product identity and omits
its factor1/2. All three are exact normalization/regime controls.

WrongWindow is an ABSTRACTerror-budget control: J0,A=B=t=r1,a1/2 satisfies
the displayed error bound and weak threshold B/(At)<=r, but not the actual
2B/(At)<=r. The inferred positive lower window is false. This is not a
claim that J0 is the actual temporal covariance norm at that point.

All four current source files resolve imports/names and fail on False.
The first successful compilation's unused-hypothesis-name warning is not
an additional mathematical test. Only hB was renamed _hB, not removed.
