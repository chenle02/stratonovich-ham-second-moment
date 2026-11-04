# Fixed-order005/006: current author reconstruction

This reconstructs the two assigned current deductions at af97, not a review vote or source repair. The exposed004/214 and external3.1 clauses are separated in prerequisite-clauses.md. No infinite solution series, target upper bound, source4.1/L4.4/Section5, intrinsic constant or theorem of rough-PDE uniqueness is a premise.

Throughout0<a=alpha0<1,0<alpha<d oralpha=d=1,alpha+a<2,d=1,2,3. Gamma is the ORIGINAL nonnegative even PD homogeneous tempered Radon covariance, Gamma(cA)=c^(d−alpha)Gamma(A). Its unnormalized spectral pairing isGamma=integral exp(i xi·x)mu(dxi). Positive waveG_t has mass t and Fouriertransformsin(t|xi|)/|xi|, value t atzero; Brownianp_t hastransformexp(−t|xi|²/2). We never treat the d3 sphere as a density. Putc=alpha/2∈(0,1), V=mu(B1),gamma_b=p_b*Gamma. Original amplitude stays insideGamma/mu.

##0. Falsification controls and zero/empty cases

The unchanged exact white controls from the earlier foundation replay are reused, not rerun. ForGamma=cw delta0 in d1, the static cross1+1 spatialdiagram hasJ=cw min(r1,r2)/2 and dampedmasscw/4. The empty+length2 selfdiagram hasJ=cw r1/2 forpositivegaps and dampedmasscw/2. Therefore the limiting density need NOT vanish asr2→0, while its measure can have no atom there. “G0 has masszero”cannot replace a measure-face argument. For the emptychain ell_empty=0 identically: its zero-level face carries ALLmass; onlypositivehorizonfacesT>0 can be declared null without an emptychain exception.

At Brownianj1 white,A_heat=cw/sqrt(2pi), and the bound below is exact: E S0(T)=8cw T^(3/2)/(3sqrt(2pi)). Atj2 the threechronological integrals sequential/crossing/nested arecw²T³ times1/12,1/36,1/24, each occurring8times in the labeledcube; theirsum is11cw²T³/9, below the bound2cw²T³. Thus the factorial/Gamma constants are tested beyondj1. These are finiteoccupation controls, not an all-order solution assertion.

For unequal sourcewidths epsilon and4epsilon, their mixed spatialcovariance isgamma_(5epsilon), not a marginal covariance; temporalwidthseta and3eta useK_(3eta), since Laplaceprefixes intersect. Independent copies with the same nonzero limiting marginal variance would instead have crossmoment0 and squaredL2distance2Q, not0. This refutes a marginal-only Cauchy argument. Both-chainsempty is order0, unitmass on the emptytuple,Y0=X0=1. Gamma0 givesmu0 and everypositive-orderdiagram/term0 directly; none ofthepositive-order ornormdivisionarguments is invoked.

##1. Heat estimate and Brownianoccupation constants

Spectralhomogeneity givesmu(B_r)=Vr^alpha andmu({0})=0. Radial Stieltjes integration, not an angular density, yields

 A_heat=alpha V integral_0^infinity u^(alpha−1)exp(−u²/2)du
       =2^c V Gamma_E(1+c),
 0<=(p_t*gamma_b)(x)<=integral exp(−(t+b)|xi|²/2)mu(dxi)
       =A_heat(t+b)^(−c)<=A_heat t^(−c).

For standardBrownian motionB putS_b(T)=integral_[0,T]² gamma_b(B_s−B_t)dsdt. Atb>0 the integrand isbounded/nonnegative. Expand itsjthmoment and order its2j labeledtimes, ignoring null equalitydiagonals. There are(2j)!chronological simplices. On one, write0<u1<...<u_(2j)<T and retain its fixedmatchingD.

Among remaining observations choose the LARGESTtimeu_h and itspartneru_i. The previousremainingtimeu_v exists because an evennumber>=2 remains. Conditional on all OTHERremainingobservations, the lastincrementB_(u_h)−B_(u_v) is independent Gaussian withvarianceu_h−u_v. The heatbound therefore removes this edge at costA_heat(u_h−u_v)^(−c), uniformly in the partnerposition. All remainingedgefactors are measurable under that conditioning. Then REMOVEbothh andi: no remainingedge containsi, so integrating its nowunused observation leaves the ordinary Brownian law at the survivingtimes. Continuing to condition on removedfutureobservations would incorrectly create a Brownianbridge; we do not do that.

Repeatjtimes. Selectedrightendpoints h are distinct and their currentgaps are>=the ORIGINALadjacentgapsDelta_h=u_h−u_(h−1); negativepower then bounds the product byA_heat^j timesj DISTINCToriginalgaps to power−c. On the ordered simplex the2j gapvariables plusresidualT−u_(2j) havej Dirichletparameters1−c andj+1parameters1. Hence its exactintegral is

 Gamma_E(1−c)^j T^((2−c)j)/Gamma_E((2−c)j+1).

Summing the(2j)!orderings proves, withzerothmoment1,

 E S_b(T)^j<=D_j T^((2−c)j),
 D_j=(2j)![A_heat Gamma_E(1−c)]^j/Gamma_E((2−c)j+1).

The bound is uniformb>0. Its only singular-gap condition isc<1, exactlyalpha<2. It is finite at each fixedj; no uniform-in-j analytic radius is inferred.

##2. Positive spatialWick measures and explicittotalmass

Fixm+n=2k>=2, a labeledpairpartitionD, and two chains each with its OWNroot(0,0). Gapcoordinatesr_l>0 andspatialincrementsz_l givecumulative s_l,x_l withinthat chain. Forvertexwidthsepsilon_l>0 define

 J_(epsilon,D)(r)=integral product_lG_(r_l)(dz_l)
                 product_(e={j,h})gamma_(epsilon_j+epsilon_h)(x_j−x_h),
 rho_epsilon(dr)=J_(epsilon,D)(r)dr,
 nu_epsilon(dr)=exp(−sum_l r_l)rho_epsilon(dr).

They are positive; localfiniteness follows fromboundedheatcovariances andGreenmassesr_l. Initiallyextend byzero tocoordinatefaces of[0,infinity)^(2k). For e letb_e=epsilon_j+epsilon_h. Its actual finite spectralmeasure ismu_e=exp(−b_e|xi|²/2)mu, with

 mu_e(Rd)=A_heat b_e^(−c)=V Gamma_E(1+c)(2/b_e)^c.

Orient eachpair j<h andleteta_l(xi) be the coefficient ofz_l in sum_e xi_e·(x_j−x_h). Finiteedge spectralmasses and finite dampedGreenmasses justify ABSOLUTE Fourier/LaplaceFubini. Forlambda_l>=0,

 L_epsilon(lambda)=integral exp(−sum lambda_l r_l)dnu_epsilon
 =integral exp(−sum_e b_e|xi_e|²/2)
   product_(l=1)^(2k)[(1+lambda_l)²+|eta_l(xi)|²]^(−1)
   product_e mu(dxi_e).

The integrand AFTERLaplace is nonnegative. It increases whenheatwidthsdecrease. At anyvector it is<=the commonvertexwidth epsilon_*=min epsilon_l. This is transformmonotonicity only; physicalgamma_b neednot be pointwise monotone inb.

The finite positive wave/heat measures satisfy

 integral_0^infinity exp(−qt)G_t(dx)dt
 =(1/2)integral_0^infinity exp(−q²u/2)p_u(x)du dx,

because their Fouriertransforms are both(q²+|xi|²)^(−1). Their masses are bothq^(−2), so no measure at infinity is hidden. Applying this to each of2k Greenfactors atq1 changes to2 independent AUXILIARY Brownianchains with gapweights exp(−sum u_l/2), and prefactor2^(−2k). They are not independent copies of the actualGaussian drivingnoise.

If tau_i is the last Browniantime inchaini, setit0 foremptychain. Insert the exactidentity

 1=(1/4)integral_(A>=tau1,B>=tau2)
          exp(−((A−tau1)+(B−tau2))/2)dA dB.

Eachone-dimensional integral is2, even foremptychain. Combinedweight isexp(−(A+B)/2). Tonelli allowsenlarging eachBrownian orderedtime simplex toits fullcube; this is an inequality introducing NO extra m!,n!or(2k)!factor. Atfixedpaths, disjointpair endpoints then factor thecubeintegral asS1(A)^v1 S2(B)^v2 C12(A,B)^w, v1+v2+w=k. Finiteheatweightedmu and FourieroccupationfunctionsF_i(xi)=integral exp(i xi·B_i(s))ds give

 0<=C12=integral F1 conj(F2)mu_(2epsilon_*)
 <=sqrt(S1 S2).

Physicalnonnegativity gives the firstinequality, spectralCauchy–Schwarz the second. Thus theproduct<=S1^(v1+w/2)S2^(v2+w/2)<=(1+S1)^k(1+S2)^k, withzeropower1. Define

 M_k(t)=sum_(j=0)^k binom(k,j)D_j t^((2−c)j).

The Brownianbound and independence ofthese TWOauxiliarypaths nowgive

 sup_epsilon L_epsilon(0)
 <=U_k=2^(−2k−2)[integral_0^infinity exp(−t/2)M_k(t)dt]²
 =2^(−2k)[sum_(j=0)^k binom(k,j)(2j)!
               (2^(2−c)A_heat Gamma_E(1−c))^j]²<infinity.

Here integralexp(−t/2)t^((2−c)j)dt cancels theGamma denominator and supplies2^((2−c)j+1). Everyfactor2 is explicit. Forwhitecw1,k1,U1=25/4, consistent with actualcross1/4,self1/2. U_k maygrowveryfast withk and is not amplitudehomogeneous because of the loose(1+S)^k bound; each ACTUALdiagram still hasdegreek in the original covarianceamplitude. Only fixed-k finiteness isused.

##3.005: Laplace compactification, uniqueness and no lostmass

For commonvertexwidthh decreasingtozero, the positive spectralintegrand atlambda0 increases toF0=product_l[1+|eta_l|²]^(−1). TheuniformU_k bound andmonotoneconvergence proveF0 integrable againstproductmu. For ANYvertexwidthsequence tendingtozero, itsGaussianweight tends to1 andisboundedby1. Hence dominatedconvergence gives

 L_epsilon(lambda)→L_D(lambda)=integral product_l[(1+lambda_l)²+|eta_l|²]^(−1)product_e mu,

at everylambda_l>=0 and arbitraryrelativewidthrates. DominationbyF0 also givescontinuityofL_D atzero. No coordinatewise monotonicity oftheactualwidthsequence isrequired.

Pushnu_epsilon to[0,1]^(2k) byy_l=exp(−r_l), temporarilyaddingtheboundary. UniformmassU_k givescompactweakclustermeasures. Theirinteger monomialmoments are L_D(n1,...,n_(2k)), including theconstantmomentL_D(0). These moments uniquelydetermine a finite measure: for continuousf use multivariateBernsteinpolynomialB_Nf(y)=E f(K1/N,...,K_(2k)/N), Ki independentBinomial(N,y_i). Uniformcontinuity/Chebyshev yield

 sup_y|B_Nf(y)−f(y)|<=omega_f(d)+2||f||infty*(2k)/(4N d²).

FirstN→infinity atfixedd>0, thend→0 provesuniformpolynomialdensity. Equalmonomialmoments implyequalintegrals ofallcontinuousf andthus equalfiniteBorelmeasures. Call theuniquecompactlimitbar_nu_D. The boundedpositive-measure compactness usedhere is only the standardfinite-measure weakcompactness on a compactmetriccube, not a sourceSPDE construction.

We mustexclude infinityfaces r_l=infinity, i.e.y_l=0. Forq>0 the functionproduct_l y_l^q iscontinuous onthecube,zero onanysuchface, anditslimitintegral isL_D(q,...,q). Asq decreases tozero it increases to1_{all y_l>0}. ContinuityofL_D atzero gives

 bar_nu_D{all y_l>0}=lim_(q→0)L_D(q,...,q)=L_D(0)=bar_nu_D(total).

Thus no mass hasescaped toinfinity. Moreexplicitly, theclosedsetsF_d={min y_l<=d} decrease tothe nullzero-faceunion. Portmanteau giveslimsup_epsilon bar_nu_epsilon(F_d)<=bar_nu_D(F_d)→0. For boundedcontinuousg(r) multiplyg(−log y) byacontinuouscutoff awayfromF_d; itextendscontinuouslybyzero tothecube. Itsintegralsconverge, whiletheomittedparts arebounded by||g||infty timesF_(2d) masses. This proves finite-measure weakconvergence ofnu_epsilon on[0,infinity)^(2k) withfullmass, notmerely vagueconvergence. Everywidthsequence hasthesamelimit; that is thejointmultivariable spatiallimit.

For a coordinateface r_l=0, holdallotherlambda0 andsendONLYlambda_l→infinity inthepositive spectralformula. Itsone resolventfactor tends tozero andF0 dominates. On themeasureside exp(−lambda_l r_l) tends to1_{r_l=0}. Therefore

 nu_D{r_l=0}=lim L_D(0,...,lambda_l,...,0)=0.

This is an atom/face statement, not a limiting-density argument.

##4.005: UNDAMPED homogeneity andpositivehorizonfaces

Define rho_D=exp(sum r_l)nu_D; it is Radon andlocallyfinite. Wave/heat scaling gives

 G_(cr)(c dz)=cG_r(dz),
 gamma_b(cx)=c^(−alpha)gamma_(b/c²)(x),
 rho_epsilon(cA)=c^((4−alpha)k)rho_(epsilon/c²)(A).

The exponent counts2k Greenfactors+2k timeJacobians−alpha*k. Pass this identity oncompactcontinuous tests byvagueconvergence, yieldingrho_D(cA)=c^((4−alpha)k)rho_D(A) forBorelA. OnlytheUNDAMPEDmeasure ishomogeneous; nu_D isnot.

Letell_i be sumofgapsinthe NONEMPTYchaini, andell_empty=0. If a compactK⊂{ell_i=T}, T>0, hadpositivemass, then cK atcountablymanydistinctc∈[1,2] wouldbedisjoint, eachwitha commonpositive lowerbound onmass, andallinside thecompact image[1,2]K. This contradictslocalfiniteness. Exhaustingthefacebycompacts provesrho_D{ell_i=T}=0. For anemptychain thepositive-Tface isempty. Itsell=0pushforward, however, hasfullmass; for anonemptychain theell=0face issubsetofthecoordinatezero facesandisnull.

ForT1,T2>0, Omega={r>0:ell1<T1,ell2<T2} isbounded: everyactualcoordinate belongs toanonemptychain. Itsboundary liesintheproved coordinatezero/positivehorizonfaces. Acompactcutoff bounds exp(sum r_l) byexp(T1+T2) onthisregion. Weakconvergence andthezero-boundarymass therefore give, forboundedcontinuousphi,

 integral_Omega phi drho_epsilon→integral_Omega phi drho_D.

Ifphi isstatedonlyontheopenpositiveorthant, firstcutoffnearthecoordinatefaces; theirvanishingmass controls theerror. Noextensionof an oscillatinginteriorphi throughazero face isassumed. This finishes every assertionof005, independentlyoftheuniversaltemporalpairinginequality.

##5. Exact004/214 norm clauses andexternal3.1 eligibility

UseunitdampingG_l(r,x)=exp(−r)(p_(zeta_l)*G_r)(x), positiveGreenheatzeta_l>0 whenafunction isneeded(d3). Its massnormN0 is1. At edgee={j,h}, spatialmu_e=exp(−(epsilon_j+epsilon_h)|xi|²/2)mu isFINITE ascomputedin§2, withinversegamma_e=p_(epsilon_j+epsilon_h)*Gamma>=0. Thetemporaledgemeasure is1_(A_e)(lambda)lambda^(a−1)dlambda/Gamma_E(a), finiteoneachcap(0,L] becausea>0. EachA_e may bea prefix/full/marked-tail domain. These are theactualfinite-edge andnonnegativekernel hypotheses oftheheldauthorTheorem3.1(3.6),physicalpp14–15, not an extension ofit toinfiniteunregularizedmu.

Precisely the004 clauses neededarefiniteA=N1(1),B=N2(1), tailsA_M=N1^(M)(1)→0,B_M=N2^(M)(1)→0, andtheuniformsmoothing/capbounds. Theirconstants canbeexposed as

 R_alpha=alpha*pi*V/[2sin(pi alpha/2)],
 A=R_alpha Gamma_E(2−alpha−a)/Gamma_E(2−alpha),
 B²<=V Gamma_E(1−a)[(2−a)/2+alpha/(2−alpha)],
 A_M=R_alpha/Gamma_E(a) integral_M^infinity
                       lambda^(a−1)(1+lambda)^(alpha−2)dlambda.

Theconditionsa>0,alpha+a<2 makethefirstintegral finite;0<alpha<2 and a<1 givetheBbound bysplittinglow/highspectralfrequencies. Namely integralexp(−(s+t))|s−t|^(−a)dsdt=Gamma_E(1−a), andtheversionwithst equals(2−a)Gamma_E(1−a)/2. ForB_M² replace|s−t|^(−a) byK_M(s−t)=Gamma_E(a)^(−1)integral_M^infinity exp(−lambda|s−t|)lambda^(a−1)dlambda. Itisnonnegative asatemporalPDquadraticform, andthe004absolutespectralmajorant plusoffdiagonalK_M→0 provesB_M²→0. Anexplicit scalarbound is

 B_M²<=V/Gamma_E(a) integral_M^infinity lambda^(a−1)
 [(1/2+alpha/(2−alpha))/(1+lambda)+1/(2(1+lambda)²)]dlambda→0.

No tailrate isrequired. InN1 the actualFourier–Laplaceintegral ofdampedGreenheat isexp(−zeta_l|xi|²/2)/[(1+lambda)²+|xi|²]>=0. Thus theABSOLUTEVALUE inheldsource(3.4),whichpdftotext canomit,doesnotchangetheformula. Spatialedge/Greenheat multipliers liein[0,1]. InN2 integrate thepositive timeQUADRATICFORM at eachxi BEFORE removingthosemultipliers; sin-waveproducts neednotbenonnegativepointwiseintime. Prefixrestriction/capremoval andmarkedtailrestriction then give fullnorms<=A,B andmarkednorms<=A_M,B_M uniformlyinallregularizations. This is not physicalcovariancepointwisemonotonicity.

The214 clause handles the sourceCase2's independentpredecessors. Withfixedfiniteedge mu_e andfinite temporalcap, writeC_L((t,x),(s,y))=kappa_L(t−s)gamma_e(x−y). Thefeatureidentity integral_R h_lambda(t,r)h_lambda(s,r)dr=exp(−lambda|t−s|), h_lambda=sqrt(2lambda)exp(−lambda(t−r))1_(r<=t), gives a positiveHilbertcovarianceformQ_L. Cauchy–Schwarzand simultaneoustranslation ofboth variablesgive

 0<=Q_L(T_(A,b)G1^0,T_(B,c)G2^0)<=N_C,L(G1)N_C,L(G2).

Boundedcompactkerneltruncation andpositivecaplimits pass this to thefullpairing with EXACTcoefficient1. TimeoriginA−B andspatialoriginb−c remain ifvariablesarerelativized: kappa(u−v+A−B)gamma(X−Y+b−c). Eachlength1chain hasitsOWNroot; anemptychain hasnointerchainCase2pair. Theprintedsourcep21 offset-freeequality isnotused. Theprinted(3.5)secondGreenvariable isindependentlyy, not repeatedx. No origin/massfactor isadded, andno positive-definitenessofaseparatelyshiftedcrosskernel isclaimed. Remaining3.1induction/firstnormfacts stay importedaftertheiractualhypothesesarechecked; nofullsourceproofispretendedhere.

The externaltheorem distributes2klabels intoQ0,Q1,Q2 with|Q0|=|Q1| and|Q2|even, bounding thedampeddiagram by

 product_(l∈Q0)N0(G_l) * product_(l∈Q1)2N1,e(l)(G_l)
                         * product_(l∈Q2)N2,e(l)(G_l).

Itsphysicalp15 explicitmultiplicityrule isessential: eachedge occursonceinthefirstnormproduct ORtwiceinthe secondnormproduct, neverboth. Thus|Q1|+|Q2|/2=k. PutH=max(1,2A,B²). A singleMARKEDedgewithtemporalK_M contributesatmost2A_M H^(k−1) inthefirstcase,orB_M² H^(k−1) inthe secondcase. Theuniformsinglemarkedbound isthereforeH^(k−1)(2A_M+B_M²), not a loneB_M. No pairingcount appears forONElabeleddiagram.

##6.006: uniformmarkedtail, caps andGreen order

Onell1<T1,ell2<T2 undampingcosts atmostexp(T1+T2), sincesum r_l=ell1+ell2. LetF_(epsilon,0,D) be thefulltemporaldiagram andF_(epsilon,eta,D) thecommonprefixwidtheta. Atpositive spatialwidthsthefulltemporal integralisfinite: bound eachspatialcovariance byitsfinite supremumandGreenmassesbyH_T=max(T1,T2). Thedisjointpairtimefactors onthefulltimecube haveexactintegral

 [integral_[0,H_T]²|s−t|^(−a)dsdt]^k
 =[2H_T^(2−a)/((1−a)(2−a))]^k.

Differenceofproducts ofnonnegativeboundedprefix factors boundsF0−Feta byksinglemarkededge integrals. Applying§5 gives

 0<=F_(epsilon,0,D)−F_(epsilon,eta,D)<=E_k(eta),
 E_k(eta)=k exp(T1+T2)H^(k−1)
                      [2A_(1/eta)+B_(1/eta)²]→0.

ItisuniforminALLpositivevertexspatialwidths, allauxiliarytemporaluppercaps andGreenwidths; constants maydepend onfixedk,T1,T2,Gamma andparameters. Thecoefficient1 of214 addsnoexp(A+B)predecessorcost.

Tojustifyusingfulltemporaldomains, firstcapallLaplaceintervals aboveL, using(M,L] forthemarkededge. PositivitypassesL→infinity. Then atFIXEDpositive spatialwidths removeGreenheat: productsandlinearpushforwards ofpositive finiteGreenmeasures convergeweakly againstboundedcontinuous spatialcovarianceproducts. Their masses areunchanged; thejustdisplayed timecubeintegral timesfixedspatial-supremumandH_T^(2k) dominatesthetimeintegral, includingmarkedtails<=fulltimefactors. Thus dominatedconvergence removestheGreenwidthandpreservesE_k. This deterministicfulltemporaldiagram argumentdoesnotconstructanunregularizedpointfield. TheACTUALrandomsource terms below takeGreenFIRST atbothpositive noise widths, before anynoise limit. No finiteFouriermode truncationwithpossiblynegativephysicalcovariance isused.

##7.006: jointarbitraryrelative spatial/temporal limit

Atfixedeta>0 the multiplier product_e kappa_eta(s_j(r)−s_h(r)) isboundedcontinuous, evenonequal-timehyperplanes.005therefore gives theuniquespatiallimitb_D(eta). Itisfinite sincekappa_eta(0)^kexp(T1+T2)U_k boundsit. Aseta decreases, b_D(eta) increases. For0<eta1<eta2 theuniformmarkedbound gives

 0<=b_D(eta1)−b_D(eta2)<=E_k(eta2).

Afiniteanchorb_D(eta0)+E_k(eta0) boundsallsmallereta; theestimate makes themCauchy. Hencefiniteb_D=lim_(eta→0)b_D(eta), with0<=b_D−b_D(eta)<=E_k(eta).

If EVERY temporalvertexwidthdelta_l<eta, itsedgeprefixwidthdelta_j∨delta_h<eta. Therefore

 F_(epsilon,eta,D)<=F_(epsilon,bold_delta,D)
 <=F_(epsilon,0,D)<=F_(epsilon,eta,D)+E_k(eta).

Both theunknownF andlimitb_D lieinintervals oflengthE_k(eta) basedatF_epsilon,eta andb_D(eta), so

 |F_(epsilon,bold_delta,D)−b_D|
 <=|F_(epsilon,eta,D)−b_D(eta)|+E_k(eta).

Given anerror, FIRSTchooseeta forthemarkedtail; THENchooseallspatialwidthssmall fortheonefixedboundedcontinuoustest. Oncealltemporalwidthsare<eta theymayshrinkatANYratesrelative toeachotherandthespatialwidths. This provesthe jointlimit, notjustaniteratedone. Empty/unequalchains stayinthemeasureandthebound; no uniformconvergencerateink,TorGammashapeisclaimed.

##8.006: onecommonGaussianfamily retaining thegivenW

To make“SAMEW”precise, thegivenrealrawtestcompletionH_W canbeembedded isometrically in a deterministicfeatureHilbertspace. LetH_Gamma be thespatialcovariance-null completionandput

 G=L2((0,infinity)_lambda×R_r,
                  lambda^(a−1)dlambda dr/Gamma_E(a);H_Gamma),
 (Phi F)(lambda,r)=sqrt(2lambda)integral_(t>0,t>=r)
                                exp(−lambda(t−r))F(t,·)dt.

Thefeatureidentity from§5 andabsoluteFubini forcompacttests give||Phi F||G=||F||H_W. Complete toan isometrywithclosedrangeP. Retain the GIVENW byonefixed extension

 I(g)=W(Phi^(−1)Pg)+J((I−P)g),

whereJ isonescalarisonormalprocess ontheorthogonalcomplement, independentonceifneeded. This is NOTaG-valuedGaussianwhitevector. Theauxiliaryr rangesoverR butdefinesnonegative-time valueofrawW. CountabledensecompacttestsandthelocalRadoncovariancebound makethespacesseparable.

HeatC_epsilon isapositive contractiononH_Gamma withspectralmultipliere^(−epsilon|xi|²/2), andLaplaceprefixP_delta isamultiplicationprojection onG. Theycommuteandconvergestronglytoidentity. Thesmoothpositive-widthfield isI(v_(epsilon,delta;t,x)) with

 v=1_(lambda<=1/delta)h_lambda(t,r)p_epsilon(x−·).

Itsvarianceiskappa_delta(0)gamma_(2epsilon)(0)<infinity. Pairingtwofeatures gives EXACTLY

 E[W_(epsilon,delta)(t,x)W_(epsilon',delta')(s,y)]
 =kappa_(delta∨delta')(t−s)gamma_(epsilon+epsilon')(x−y).

Herekappa_delta(0)=delta^(−a)/Gamma_E(a+1), andgamma_(2epsilon)(0)=A_heat(2epsilon)^(−c). Testintegration givesI(P_delta C_epsilon Phi F)→I(Phi F)=W(F); onefixedextension thusretainsoriginalWliterally andallwidths simultaneously, withoutresampling. Positive-widthfields mayusefixedauxiliaryJ; astronger sigma(W)-measurability assertionisnotneeded orclaimed. Themaximum/summedwidthrule, notjustmatchingmarginal laws, istheactualcommon-sourceinput usednext.

##9.006: actualBochner terms, GreenFIRST andmixedL2Cauchy

Fixn,t,x andPOSITIVEvertexwidthvectors. Theterminalorderedchainmeasure hasmassM_n(t)=t^(2n)/(2n)!, fromM0=1 andM_n(t)=integral_0^t(t−s)M_(n−1)(s)ds. Thisincludes theflatdata(1,0), withorderzero1. LetV_* bound thefinitelymanypointvariances. GaussianHolderwithexponentn gives

 ||product_(j=1)^n W_(a_j)(s_j,y_j)||L2
 <=sqrt((2n−1)!!)V_*^(n/2).

Continuouspositive-widthcovariances implycontinuousfiniteGaussianLpvariablesandL2products; theirseparableparameterimage isstronglymeasurable. FiniteGreenmass thereforegivesanactualGaussian-polynomialBochnerintegralY_n^bold_a inL2. Constantsmaydependonitspositivewidths; this boundisNOTusedasuniformnoise-control.

Atfixednoisewidths, allGaussianproducts/Wickmoments areboundedbyfixedpowersofV_* andcontinuousinspatialvariables. ThusproductGreenheatmeasures andtheirlinearvertexpushforwards convergeagainstthem, withtimeboundproductofgapmasses integrablebyt^(2n)/(2n)!. Thisappliesto aSQUARE, aCROSSmomentwithanotherGreenwidth, andthecrossmomentwiththedirectGreenmeasureBochnerterm. AllconvergetothesamefiniteWicksum. ExpandingthesquaredL2difference provesactualGreenheat→actualwaveL2convergenceBEFOREanynoisewidthremoval. Noheat-tail sampleboundorpointwisedensityofthed3wavewasassumed.

Atpositivewidths, finiteWickformula forY_mY_n is a sumoverALLpairpartitionsof2k=m+n, eachcoefficient1; oddtotaldegreegives0. Selfpairs, unequalchainsandY0=1 remain. For theL2CauchyproblemY_n^bold_a,Y_n^bold_b use thecommonfamily§8, notindependentcutoffs. At the SAMEterminal(t,x), reverseeachterminalchain bys'_j=t−s_(n+1−j),y'_j=x−y_(n+1−j), permutingvertexwidthlabels. Jacobianabsolute1, wavepushforwards,stationarity/evenness andabijectionofpairings giveexactlytheinitialchaindiagrams treatedin§7. EachchainretainsitsOWNroot. Thisisamomentchangeofvariables, notpathwiseequalitytoaforwardnoiseintegral. Ifdifferentphysicalterminaltimeswereused, thetime-originshiftwouldremain; itisnotdeletedbythisargument.

Everymixedmoment, includingdiagonals, thereforetendstotheSAMEfinitesumQ_n=sum_(D∈Pi_n)b_D. Thefullsquare+CROSScalculation is

 ||Y_n^bold_a−Y_n^bold_b||L2²
 =E(Y_n^bold_a)²+E(Y_n^bold_b)²−2E[Y_n^bold_aY_n^bold_b]
 →Q_n+Q_n−2Q_n=0.

Theactualmixedsourcecovariance withmax/summedwidths isindispensable. L2completeness givesauniquejointlimitX_n: chooseareferenceall-widths1/jsequence, thencompareanarbitrarysmallwidthvector toasmallmemberofthatsequence anditsL2limit. This provesuniquenessatALLrelativevertexwidthrates, notjustcommonwidths. Restrictingtocommonwidths givesexactlytheorderedmultipleStratonovichdefinitionS_n(g_n) withtheprescribedinnerGreenlimit. Noorder-summationorindependentupperboundhasbeenused.

Forunequalm,n atthesameterminalpoint, thefiniteGaussianpairingdescriptionand§7 applytoeveryevenmixedtotalorder; oddmixedexpectationsremain0. L2termconvergence passesproductstoL1 byCauchy–Schwarz. Anemptychain contributesY0=1anditsproperone-chainpairings. Finitefamiliesoffixed(t,x) points/termorders also convergejointlycomponentwise inproductL2; noneofthisdeclaresanuncountablecommonpathversion. Both-chainsempty andGamma0 werehandleddirectlyin§0.

##10. Scope, dependency and true-gap check

005is independentof3.1: itspositivespatialLaplace/Brownianmomentargument establishesU_k, uniquenessandfaces.006thenuses005plus004/214andtheexactexternal3.1application tomarkandremovetemporalwidths. Itsd3Greenlimit isatfixedpositiveexternalwidthsanditsL2Cauchyusesactualcross-widthcoupling. This graphhasno all-orderseries/sharpupper/variational-finiteness/source4.1/L4.4 premise.

Everyconstantcan dependonfixedorderk,horizonsT1,T2,originalcovarianceamplitude/shapeandallowedparameters, unlessanexplicitwidth/cap/Greenuniformitywasproved. NeitherU_k norE_k(eta) isadvertisedasall-order/asymptoticallysharp. Noangular/spectraldensity,finiteoriginalmu-total,finite-modepositivityorpointwiseheatmonotonicitywasassumed. Originald1/2/3,white/singular/zero,dataandStratonovichself/unequal/emptychains remainunchanged.

Noactualgapwaslocatedintheseassigned005/006stepsundertheexposed004/214andnamedexternalhypotheses. This iscompleteauthorworkingforthosesteps, notanindependentvote, ancestoracceptance,214wholeHIGH, source-pixel/Kimi/visual/coldclearanceorprojectcompletion. Alloriginalsourceandpriorfrozenfilesremainunchanged.
