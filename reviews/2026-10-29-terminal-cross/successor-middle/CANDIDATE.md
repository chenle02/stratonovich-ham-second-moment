# Unreviewed middle-cross successor

This is independent research beyond the accepted terminal-cross note. No
claim of13controlled diagrams or a full comparison is adopted. White1Donly,
theta1,split13:02|13,crosslambda on02,selfnu on13. Mirror31:02|13swaps
canonical pair parameters. All original full covariance/sharp goals persist.

## Candidate actual reduction

Physical gap variables:u singleton;v,w,z long-chain gaps. Pairspacepositions
X=cross,Y=self giveG_u(X)G_v(Y)G_w(X-Y)G_z(Y-X). Selfspanw+z;crossspan
abs(u-v-w). WriteC=min(w,z),R=u+v,q=u-v. IntegratingRwithJac1/2and
area/16gives (1/16)*int_0^C exp(-max(abs(q),t))dt. Forabsq>=Cthisis
C exp(-absq)/16;forabsq<Cit is[(absq+1)exp(-absq)-exp(-C)]/16.

Setb=1+nu,c=1+lambda. Swapthepositiveintegral:t>=0,w,z>=t,thenw=t+x.
Integratez,xandt/qcones. Candidate closed actual formula:
I_mid=(2b^2+4bc+2c^2-c+1)/[8bc(b+1)(2b+1)(b+c-1)(2b+2c-1)].
The threepositivecone contributions are:
(1/c+1/(2b+lambda+1))/[16b(b+lambda)(2b+2lambda+1)],
1/[16b(b+lambda)(2b+1)(2b+1+lambda)],
(1/(b+lambda)+1/c)/[16b(2b+1)(b+1)].
Their sum simplifies to the closed formula. Atlambda0it matches the exact
charged-in-one-chain anchor (b+1)/[4b^2(2b+1)^2]. These derivations still
need independent review/model correspondence,not only symbolic simplification.

## Candidate enlargedclock and a failed further shortcut

Drop only the positive clockoverlap to defineJdag>=J. Withr=w+z andR=u+v,
spatialCovdet=r[R+w(r-w)/r]. Thusdensityh(r)h(R+w(r-w)/r). LetA=lambda+
lambda^2/2,bridge=w(r-w)/r. Rootqkernel afterLaplace mixture has
K_As(w)=int_R exp(-s absq)exp(-A abs(q-w))dq
=2/(s+A)*S_As(w),
S_As(w)=[s exp(-Aw)-A exp(-sw)]/(s-A),s>1/2.
The mixture weight is m(s)/s withm=1/[pi sqrt2 sqrt(s-1/2)]times
exp(-(s-1/2)bridge). OverallJdagprefactor is1/32.

ReplacingK_As(w)byK_As(0)gives an integratedUPPERcandidate
U_zero=(1+c+2b)/[4b^2 c(c+1)(c+2b)(2b+1)]. Thisshortcut is too weak:
atb1,c11/10,closedI545/11616,U_zero1025/21483,
I-U_zero=-6005/7562016. This is a PROVISIONALexactformula-based obstruction
toROOTSHIFT ERASURE,not a refutation ofJdag<=Ior the SPDEconjecture.
Check the underlying integralidentities independently before certifying it.
The evenK component has zero initialhazard,so the terminalcase's positive
pureexponentialdecayrate cannot simply be reused.

## Stronger survival envelope and scalar route

S_As(w)=exp(-Aw)+int_0^w A exp(-At)exp(-s(w-t))dt.
Since s>=1/2,thisis<=S_A,h(w)withh1/2. This is an elementary positive
integrand comparison,not a new probabilistic model. Preserve thewdependence.

DefineM_b(a;A)as the same enlargedclockintegral withK_As(w)replaced by
[2/(s+A)]exp(-a w). Putrho=sqrt(b^2+2a). PositiveGamma integration,
int_0^1[b^2+2a t+2d t(1-t)]^(-3/2)dt
=2(rho+b)/[b rho((rho+b)^2+2d)],d=s-1/2,
and the tripleLorentzianintegral give
M_b(a;A)=(1+c+rho+b)/[4b rho c(c+1)(c+rho+b)(1+rho+b)].
Check all factors againstM_b(0;0)=I_mid(0,nu).

Candidate boundJdag<=U_surv=[h M_b(A;A)-A M_b(h;A)]/(h-A)forA!=h.
AtA=hit isM_b(h;A)-h*partial_aM_b(h;A). Bothtermsfinite;combinationis
the positive integral ofS_A,h. There is a nonsingular rational reformulation.
LetD=sqrt(b^2+c^2-1),E=sqrt(b^2+1),B=b+c,C=b+1,K=1/[4bc(c+1)],
M(r)=K[1/(r(r+C))+1/(r(r+B)(r+C))]. Then
U_surv=M(E)+K*(F1+F2)/(D+E),where
F1=(D+E+C)/[DE(D+C)(E+C)],
F2=[D^2+DE+E^2+(B+C)(D+E)+BC]/[DE(D+B)(E+B)(D+C)(E+C)].
This is the divided-difference cancellation ofE-D,valid continuously atD=E.
It was only screened algebraically/numerically here,not independently proved.

## Exact positive-coefficient screen (not yet Lean)

SetZ=b+E,T=(D+c)/(b+1). Foractualb>=1,c>1,Z>2,T>1.
b=(Z-Z^-1)/2,E=(Z+Z^-1)/2,
c=[(b+1)T-(b-1)/T]/2,D=[(b+1)T+(b-1)/T]/2.
This satisfies the two root identities and positivity;verify every inverse
and endpoint in the actual consumer before formalization.

algebra-screen.pyclears the ORIGINALpositive denominators ofI_mid-U_surv,
substitutes this rationalparametrization,and shiftsZ=2+x,T=1+y. Its numerator
has300positiveINTEGERcoefficients,allterms divisible byy,minx0,maxdegrees
x19,y15. The exact monomials,denominators and sourceSHAare initsJSON.
This is promising for a localLeanACTUALrootconsumer,not merely polynomial
positivity. No desiredcomparison should become a hypothesis. Alsoverify
the positiveheat-bridge/Gamma/triple-resolvent analytic reductions separately.

A16point floating gridb1,1.1,2,11andc1.01,1.1,2,11foundU_surv/I_mid<1.
This is only a diagnostic,not a theorem or certified enclosure. The raw
algebra driver has no runtime kernel certificate or source-familyreview.
Do not call13or15terms controlled from this working candidate.
