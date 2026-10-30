# Preproof matrix/temporal/radial checks and limitations

Sympy exactFULL2x2 phase product has lower-left H cp cq, top-left
-H sp cq/p,matching S(-u)B(H)S(u) and BOTHphaseentries. This control is
not scalar solution-value propagation or gauge replacement.

Temporaltests useactualrawa1/2 andcompletedGaussianC1test
f=t²(1-t)² on[0,1],zeroelse. Its temporalpotential is EXACTformula
k(u)=16/15[u^(5/2)+(1-u)^(5/2)]-64/35[u^(7/2)+(1-u)^(7/2)]
     +256/315[u^(9/2)+(1-u)^(9/2)],
by Beta integration. J0=64/693, fmass1/30,uniformboundk<=1/4,|k'|<=2
fromf<=1/16,|f'|<=1/2. IBP constant9/4 andthreshold6237/64; r128,256,512
withdifferences0,1/4,1/2,1 give12positiveactualtimecosproducts>=J0/8.
Momentformula viahyp1f1 iscrosschecked by2literalquadratures atfrequencies
1/2and4 (50digits,relative1e-40). No row claimedtoevaluate Hhat or an
actualnoisyoperator norm. Hhatlowfrequency positivity is analyticobligation.

SevenEXACTdyadicshells of radialr^(d-3) show d1decay,d2log2 eachshell,
d3doublingmass; actualnear-frequency-diagonal domain/Jacobian/Esweights
muststillbeproved. This is whole-spacepolarcalibration,not a periodic
Fourierlattice substitutedforcovariance. Script/JSONscope limits explicit.
No deterministicN orGaussianC proof from controls. No uniformgain/source
constant/d2moment orreplacementtopology theorem adopted beforepropergates.
