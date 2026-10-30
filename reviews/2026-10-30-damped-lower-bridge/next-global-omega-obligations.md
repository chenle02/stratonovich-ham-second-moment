# Next original-range target: global Omega via a one-variable Gamma bound

UNREVIEWED planning/recon only, OUTSIDErunningfullproofpacket. Candidate
reduction to audit/falsify/freeze before longproof, not an acceptedlemma.
The currentgeneralOmega/whitepoint proof doesNOTsettle globalOmega>=1.

A potentially useful refinement preserves more of exp(-u lambda):
P4(z)=1-z+z²/2-z³/6+z⁴/24 >=exp(-z)>0,z>=0,by Taylorremainder.
Use it only as an UPPERbound inside K_star. TermwiseGaussianintegration
would give R_star(a,d)<=B4(a,d), where

 B4(a,d)=sum_(j=0..4) (-1)^j Gamma((a+j)/2)/Gamma(a)
                         *2^a d^((a+j)/2)/[j!(j+2-a)].

Because P4>=0, the integral defining this bound is increasing in d;
actuald=q-2a<=4-2a. Delta(q,a) is decreasing inq onq>=3, since
itsqderivative is (1/2)log[q(q-2a)/(q-a)²]<0. Hence a sufficient SINGLE
VARIABLE inequality for the originalALLd1range would be

 M_a^-1 >= B4(a,4-2a) exp(Delta(3,a)), ALL0<a<1.           (G4)

The envelopeq4 doesnotassert an alpha0SPDE; it is only a bound onkerneld.
Prove everyreduction/domain/termconstant first. No theoremfromsamplegrid.

Eight50digitcases a=.001,.01,.1,.25,.5,.75,.9,.99 all havepositive
logmargins in next-global-taylor4-probe.py/json. Smallest is~1.8948e-5 at
.001,largest~3.753 at.99. Direct9parameterrowprobe hadpositiveOmega but
(G4) is a STRICTERsufficientcriterion, still UNPROVED. Its fullrange proof
would move toward originald1dampedlowerendpoint, not just extendonepoint.

Near0 the capacity's formal logseries has linear coefficient log4 and
positivehigher coefficients (derive/justify beforeusing). The B4row has
a smaller first-order coefficient at d4, unlike the weakerP2bound; this
motivates choosingP4. Do not import a claimedseriesinequality unverified.
A possible proof can split smalla andlargea with explicitGamma bounds,
or show a global monotonicity/positivecoefficient property. No numerical
intervalcertificate or endpointuniformestimate has been proved here.

Even a successfulglobalOmega proof wouldnot provide sharpUPPERconstant,
originald2/d3lower, allpossibleprintedAd/sourcefix or exactlimit. Retain
alloriginalgoal/decision boundaries, no sourceauthorcontact/HPC/companion.
