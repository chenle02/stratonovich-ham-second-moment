# Root finite white/static calibration verification18

Working verification only; no review confidence, new Lean fact or asymptotic constant claim. Frozen candidate main SHA516d6a650bdac7d3da68672f37836afd084b651c39553b43d5135d0512e39d14, PROOF011/P:white-four and PROOF012/L:static-four. Unit spatial covariance delta0, unit time for numerical coefficients. Nonzero temporal exponent is retained only in the exact four-point table interpretation; the numerical integral replay is its fixed-order alpha0->0 calibration.

## Direct reconstruction of the white table geometry

Start each chain at0 and label the two paired spatial coordinates x,y. The three pairings give vertex lists A=(x,x,y,y), B=(x,y,x,y), C=(x,y,y,x). Reset the predecessor to0 at the split. Four Green indicators contribute1/16, and paired delta constraints have unit Jacobian. Their permitted areas follow directly from the chain increments, without temporal integration:

- Split(0,4), gaps(a,b,c,d): A area4ac; B area4a min(b,c,d); C area4a min(b,d).
- Split(1,3), gaps(r ; a,b,c): A area4min(r,a)b; B areaF(r,a,min(b,c)); C areaF(r,a,c).
- Split(2,2), gaps(a,b ; c,d): A area4ac; B area4min(a,c)min(b,d); C areaF(a,c,min(b,d)).

Here F(a,b,c) is the area of |x|<a, |y|<b, |x-y|<c. For c>=a+b it is4ab. For |a-b|<=c<a+b remove two corner triangles, whose combined area is(a+b-c)^2. For0<=c<|a-b| the retained strip has area4min(a,b)c; assuming a>=b, the claimed positive-part formula reduces to4ab-[(a-c+b)^2-(a-c-b)^2]=4bc, and symmetry handles b>=a. Thus the source's formula4ab-(a+b-c)_+^2+(|a-b|-c)_+^2 holds, including zero boundaries. Swapping x,y and the determinant-one map(x,y)->(x,x-y) give the full argument symmetry.

The actual time lists are(a,a+b,a+b+c,a+b+c+d), (r,a,a+b,a+b+c), and(a,a+b,c,c+d). Taking paired differences yields exactly the source's nine(q1,q2) rows: (b,d);(b+c,c+d);(b+c+d,c); (|r-a|,c);(|r-a-b|,b+c);(|r-a-b-c|,b); (b,d);(|a-c|,|a+b-c-d|);(|a-c-d|,|a+b-c|). This verifies the temporal factors too, without assuming individual-diagram permutation symmetry.

Each exchange of two chains preserves the sum over pairings and gives the two mirrored splits. The total multiplicity is therefore2*sum(0,4)+2*sum(1,3)+sum(2,2), not a diagonal-chaos sum. Time scaling contributes t^4, spatial area t^2, covariance time factors t^(-2alpha0), hence t^(6-2alpha0). These are finite coefficient identities, not large-time limits.

## Exact static integration replay

For a fixed free position, let L1,L2 be sums of absolute spatial increments in the two chains. Integrating time slacks produces (1-L1)_+^m/m! and (1-L2)_+^n/n!, with empty-chain factor1. The script derives L1,L2 directly from the vertex pairings and split, then uses the three sectors(x,y)=(u,u+v),(u+v,u),(u,-v), u,v>=0. Every Jacobian has absolute value1; reflection contributes2. It computes the intersections L1<=1,L2<=1 rather than entering their integration bounds from the source table. Each bound is linear, their exact rational crossing cuts partition u, and polynomial integration is exact.

All27 sector integrals and all9 coefficients match the source. Row sums are11/17280,143/34560,187/17280. With the full split multiplicities the result is11/540. Omitting reflection gives11/1080; omitting the mirrored splits gives539/34560. Both are rejected by the actual target, demonstrating that the two factors are essential. The JSON retains all derived lengths, limits, pieces and rational values so the computation can be inspected, not merely a PASS bit.

The fixed-order static passage requires separate domination: on the unit-time cube spatial factors are bounded by1/4 (each smoothed delta has unit mass and integrates to at most2 over its paired coordinates, then multiply by1/16). For0<=alpha0<=a_bar<1, time factors are bounded by their a_bar counterparts; disjoint pairing labels give the finite cube integral[2/((1-a_bar)(2-a_bar))]^2. Therefore dominated convergence at fixed order is valid. This does not exchange static and large-time limits. No disputed published white asymptotic constant is used.

The existing white CDF/energy/Gamma formulas and their accepted finite/algebraic application records are separate. This calculation resolves the concrete finite-table replay item named by Work16; it does not clear either whole scientific HIGH, cold or full-goal gate. No manuscript/PDF was changed.
