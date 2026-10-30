# Damped lower-endpoint bridge: proposed actual theorem

PROPOSED, unproved/unreviewed. Target the ORIGINALpoint second moment,
not a replacement functional. General comparison for ALLactuald1parameters,
then an exact strict lower-endpoint closure atwhitealpha1,a1/2. The GLOBAL
scalar comparison remains OPEN; no full sharp/all-dimensional completion.
No source correction or actual first-moment theorem used.

## Exact model, accepted objects and notation

Actualreal d1 RieszGamma=c_Gamma|x|^-alpha dx for0<alpha<1,orwhite
Gamma=c_Gamma delta_0 atalpha1; positiveamplitude retained.0<a<1,
alpha+a<2. Put q=4-alpha,k=3-alpha,m=q/k,d=q-2a>0.
Use actualX_pos,C_pos,B_Gamma,v_psi,wholeH1RayleighrateI_psi andREAL
V_c^pos from accepted occupation approximation/general-positive consumer:
Q2=liminf t^-kappa log E|u(t,0)|²>=V2=2^m V1,
kappa=(4-alpha-a)/k, SAMEcanonicalu, no roughstochasticflow needed.

Let Fsp={realg inH1(R):||g||2=1}, b(g)=int|g'|²,
A_sp(g)=int g²(Gamma*g²), E_sp=sup_Fsp[A_sp(g)-b(g)/2].
These are NEWpurely spatial RAWenergies, no temporal kernel/staticnumericM.
Let O be the accepted strongH1-measurable normalizeda.e finiteintegrated-
energy occupation class; let T(g)=int b(g_t)dt. Define ACTUALdampedkernel

 K_star(u)=Gamma(a)^(-1)int_0^infinity
      exp[-(lambda+lambda²/(2d))|u|]lambda^(a-1)dlambda,
 R_star=2int_0^(1/2)K_star(u)du,
 E_star^O=sup_(g inO)[int int K_star(s-t)
           int g_s²(Gamma*g_t²) dx dsdt-T(g)/2].           (D)

This uses sourceauthorp4(1.13)kernel andp4(1.12)penalty1/2, but domainO is
EXPLICITmeaningfulfiniteenergy, not allpossibleprintedAd readings. Source
normalizationUNKNOWN; no E_star^O=value under an unspecifiedintendedfix.
Keep the source-shaped algebraicmap from acceptedrawvalueceiling:

 F_b(z)=k[(q-2b)^((q-2b)/2)/(8(q-b)^(q-b))
                     *(2z/(2-alpha))^((2-alpha)/2)]^(1/k),
 Delta=[qlogq+(q-2a)log(q-2a)]/2-(q-a)log(q-a)>0,
 F_a(z)=exp(Delta/k)F_0(z),z>0.                            (M)

F0changes DISPLAYparameter only; E_sp contains NOtimekernel bydefinition.
F_a as firstmean source MAP doesnot assert p1 theorem. c2 consumer ourlabel.

## T1: exact temporal potential and legal rough controls

For r=(1-a)/2 in(0,1/2), define
 f_a(t)=[t(1-t)]^-r/[Gamma(r)Gamma(1-r)],t in(0,1).
Prove nonnegative f_a inL1intersectL2(time),nonzero, and EXACT
 int_0^1|s-t|^-a f_a(t)dt=1 for EVERYs in[0,1].
Mass M_a=int f_a=Gamma((1+a)/2)/[Gamma(1+a)Gamma((1-a)/2)]>0.
Use a self-contained Beta/binomial/incompleteBeta derivation, not a
d>=2Riesz theorem applied without its dimension restriction. Endpoint
values, singular integrals, Tonelli and L2threshold must be justified.
No massrenormalization. For EVERYpositive nonzero phi inspatialB=L1intL2,
psi=f_a tensorphi belongs toactualX_pos. Match actualq/h sigma a.e.:
h_sigma=Gamma*phi is TIME-CONSTANT, v_psi=M_a intphiGamma*phi,
I_psi equals the actual wholeH1Rayleigh rate of that potential, no Gaussian
pointvalue or rough H2/eigenfunction/Youngflow theorem claimed.

## T2: staticcontrol lower with ALLconstants and no optimizer

Prove E_sp finitepositiveREAL and its sharpspatialratio relation by
actualspatialCS/Sobolev/scaling, not disputed publishedMvalues. For each
realunitH1g, use phi=theta(S_ellg)^2,theta,ell>0. Occupationdilation
S_ellg=sqrt(ell)g(ellx) is DISTINCT from raw D_sGaussian dilation.
Rayleigh gives lambda²>=theta ell^alpha A_sp(g)-ell²b(g) whenpositive;
rawcost=M_a theta²ell^alpha A_sp(g). Optimize ACTUALtheta andell, or
positive kinetic/interaction/rate variables, retaining square-root/half-
cost and domain b,A>0, to prove

 V1^pos>=M_a^(-1/k) F_0(E_sp).                            (L)

Use the accepted roughX score approximation/consumer, not unprovedstatic
SPDE asymptotic or optimizer attainment. Each test/scale fixed beforetime.

## T3: dampedenergy upper and general explicit comparison

Prove K_star positive/even/decreasing,locallyintegrable,K_star<=|.|^-a,
so its time row max is EXACT R_star at1/2. Prove spatialcovarianceCS for
positiveBinputs from actualpositive-definiteGamma (or accepted Xcovariance
CS with onecommonpositive smoothtimefactor). With SHARPspatialratio,
Schur and spatial dilation derive finitepositiveREAL E_star^O and

 E_star^O<=R_star^(2/(2-alpha)) E_sp.                     (S)

Then for ALLoriginald1parameters derive the ACTUALpoint lower comparison

 Q2>=2^m Omega(alpha,a) F_a(E_star^O),
 Omega=[M_a^(-1)/(R_star expDelta)]^(1/k)>0.               (C)

This is unconditional with explicitOmega, NOTthe unprovedclaimOmega>=1
onfullrange. Gammaamplitudes cancel fromOmega. Allsource-domain/rate/cost
and labelmatching must hold before invoking C. No sup/time interchange.

## T4: rigorous closure atwhitealpha1,a1/2

At alpha1,a1/2,d2,k2,prove by dropping ONLYexp(-u lambda) inK_star and
integrating the remaining GaussianLaplaceintegral that
 R_star<=B_star=(4/3)2^(-1/4)Gamma(1/4)/sqrt(pi).
Here M_a^-1=(sqrt(pi)/2)Gamma(1/4)/Gamma(3/4).
Gamma logconvexity viaHolder gives Gamma(3/4)<=pi^(1/4). Consequently
 M_a^-1/B_star >=W:=3 pi^(3/4)2^(1/4)/8.
At this point expDelta=2*3^(3/2)/(5/2)^(5/2),and
 [W/expDelta]^4=pi³*5^10/(9*2^25).
Use pi>157/50 plus EXACTcertificate157^3*5^4>9*2^28 to prove
 Omega>zeta:=(2418683125/2415919104)^(1/8)>1.
Thus obtain the direct ORIGINALpoint result (kappa5/4)

 liminf t^(-5/4)log E|u(t,0)|²
      >=zeta*2^(3/2) F_(1/2)(E_star^O).                  (P)

The strictfactor is optional-strengthening, not requiredsourcecorrection.
This covers one actualwhite/timeparameter point for ALLnoiseamplitudes;
full originala/alpha/d2/d3 target remains open. No actualJensen comparison:
F_a(E_star^O) not identified with actualmean or sourceL withoutdictionary.
No sourceupper/sharp-exactlimit/firstmean theorem/Skorohod development.

## Controls, review and unresolved original goal

15singularity-resolved50digit temporalpotential cases and massformula,
plus pointGamma/coarse-bound/exactinteger controls are executeddiagnostics,
not proofs. Initialnumericalendpointcancellation producedinfinity at a.1,
s1 and is PRESERVED; factorizedproduct/expm1 successor passes without
changing claimedidentity/tolerance. Global9pointOmega-positive probe is
priorrecon only, not globalscalarproof. No importedhigher-dimensionRiesz
source theorem, no newcompanion/HPC/source/wiki/sibling/contact/publication.
Independentpreproof then fullscientific/type/application review mandatory.
