# Actual driver falsification controls and boundary cases

21 actual C_infinitycompact time-test convolutions with f supported[1,2]
insidepositive time (flat endpoints), a.1/.5/.9,t0/.5/1/1.25/1.5/2/2.5.
Derivative moved ontof' compared with symmetricdifference step1e-5, absolute
tolerance1e-5. Singular lag removed analytically by v=ell z^(1/(1-a)).
40digitworking is not certifiedaccuracy. These tests check smooth CMtime
means, not all highderivatives or originaloperator/timepath norms.

Actualallowed d2Gamma=delta_x1 tensorLeb_x2,alpha1: compact q=chi(x1)chi(x2),
radialactualmask zeta(x)=chi(|x|),R1. Gamma*q=chi(x1)*intchi. Correct
zeta*(Gamma*q) depends onx2 and vanishes outsideB2; wrongGamma*(zeta q)
is independentx2 andnonzero at(0,3). Three closedform spatialcomparisons
use numerical1D integralsofchi; no fullcovariance/timeoperator computed.
Spatialtest covariancefactor positive. A translated test atx1shift5 has
nonzero rawvariance but zero maskedCMmean: don't assume eachbasisdirection
active aftermask. Nulltests can exist for invariantdirections.

Four finite diagonal tail controls in dimension256, B_j=j^-2,N0/4/16/64,
operatornorm andS2 powers decrease. Finite model is not originalnoise and
proves no infinitecompact-tail theorem. Analytical boundarycounterexample
uses actualwhole-space disjointcompactstate ONsequence: rankoneprojections
weakto0,norm1,dominatedbyI(noncompact). IndependentGaussian diagonals on it
have uniformlyboundedvariance but no bounded limiting operator since
P(sup_j|g_j|<=M)=lim p_M^N=0. This tests the necessity of compactdomination,
NOT a no-go for actualphysicallymaskednoise with its compactenvelopes.

No numerical Gaussianpath/sourcecutoff/Young/u-moment/calibrationconstant
claimed. New infiniteGaussian/operator/path assertions need analytic proof
and full review after statement gate. No newLeanmodule proposed; previous
71facts/18seams do not formalize these steps. No cutoff-mollifier replacement.
