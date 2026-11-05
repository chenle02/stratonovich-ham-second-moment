# CURRENT mixed002 and vertex008: author reconstruction

This is actual mathematics forP:mixed andL:vertex-crude, not a native review, source edit or acceptance claim. Exact CURRENT prerequisites and actual downstream uses are separated in prerequisite-and-consumer-table.md. OriginalH:homog remains: d=1,2,3;0<a<1;0<alpha<d oralpha=d=1;alpha+a<2;Gamma originalevennonnegativePDhomogeneous temperedRadon withitsactualamplitude,data(1,0). Allrandomsourcecutoffs belong toonefixedGaussianfamily retaininggivenW, allowingonefixedauxiliaryextensionifneeded. No width is resampled independently.

##0. Falsification first: zero/first orders and imbalance

X0=Y0=1 exactly. X1 is centered, soE X0X1=0 butE X1² is generallypositive. ForGamma=c delta0,d1, reuse current003’s exactc0=c/[(1−a)(2−a)(3−a)]:

 E X1²=c0 t^(3−a), E X0X2=E X2=c0 t^(3−a)/2,
 E X2X0=c0 t^(3−a)/2.

Thus totalorder2 is2c0t^(3−a), notthecross1+1termalone. The twoempty orientations are distinct splits.

There is also genuine NONEMPTY imbalance: E X1X3>0 in the sameoriginalwhite model. In initial-chaincoordinates takepairingD={(1,4),(2,3)}, withfirstchainlabel1 andsecondchain2,3,4. Restrict s1,s2 to[t/8,t/4],s3 to[3t/8,t/2],s4 to[3t/4,7t/8], andafterthetwoDiraccontractions take y1=y4,y2=y3 in[−t/64,t/64]. EachofthefourGreenfactors is1/2, since itsdisplacement isstrictlyinsideitspositivegapcone. Temporalpairfactors areboundedbelow by(3t/4)^(−a)(3t/8)^(−a). Timevolume is(t/8)^4 andremainingspatialvolume(t/32)^2. Hence theONEdiagram has thepositive lowerbound

 J_(1,3,D)(t)>=c² 2^(−26)(32/9)^a t^(6−2a)>0.

Itsfiniteness follows fromthefixed-orderconstruction006; no order4closedformula isneeded. Therefore unequalorders are NOTorthogonal as in a pure-Wickchaos expansion. A model-free logicalcontrol also matters: finiteL2 existence ofeachterm alone doesnot implysumconvergence(e.g.Xn=onefixednonzeroGaussian for alln). The all-order tail below must be derived, not attributed to005/006’s fixed-order result.

##1. Objects, regularized pairing law and actual finite-order inputs

Forpositivevertexwidths bolda=(a1,...,an),aj=(epsilon_j,delta_j), Y_n^bolda is the orderedTERMINALGaussian-polynomial integral withkernel

 product_(j=1)^n G_(s_(j+1)−s_j)(x_(j+1)−x_j),
 0<s1<...<sn<t, s_(n+1)=t,x_(n+1)=x.

It is an ordinary product ofGaussianfields, not a Wick-orderedproduct. TheterminalpositiveGreenmeasure hasmass t^(2n)/(2n)!. At fixedpositivewidths GaussianHolder bounds theL2product integrand bysqrt((2n−1)!!)V_*^(n/2), finiteuniformlyinvertexpositions. ThusBochner/time/spatialFubini forfixedm,n is legitimate; no all-orderestimate is used for this finite statement.

The actual mixedsourcecovariance is

 E[W_(epsilon,delta)(s,y)W_(epsilon',delta')(r,z)]
 =kappa_(delta∨delta')(s−r)gamma_(epsilon+epsilon')(y−z),
 kappa_delta(v)=Gamma_E(a)^(−1)integral_0^(1/delta)
                          exp(−lambda|v|)lambda^(a−1)dlambda,
 gamma_b=p_b*Gamma.

Consequently everyevenGaussianproduct has exactlyonecontributionper labeledpairpartition, withP_k=(2k)!/(2^k k!) partitions attotaldegree2k; oddtotaldegree giveszero. Eachvertex belongs toexactlyoneedge. This is finiteGaussianWickformula(source(2.19),physicalp12) applied to ONEcoupledfamily, retaining self/cross/empty possibilities. No n!or m!n! isintroduced by theorderedkernel; if symmetrized, itsaveraging factorcancels thepermutationmultiplicity.

In d3, Greenheat smoothing is removed FIRST atfixedpositive NOISEwidths, in bothsquareandCROSSmoments. Boundedcontinuousspatialcovarianceproducts, weakconvergenceofpositiveGreenmeasuresandunchangedgapmasses give a commonmomentlimit andactualL2Greenlimit. Then005/006 supplyuniquejointL2limitsX_n andfiniteindividualdiagramlimits at ALLrelativevertexwidthrates. They establish fixedorders only. Their proof usesexplicitspatialmeasure/markedtail bounds plus004/214/external3.1, not002/008/009or aninfiniteSPDEseries.

##2.008: uniform vertexwise norm inequality, allconstants explicit

Putbeta_time=4−alpha−a>2. The exposed004normclauses give, for theta>=1,

 N0(theta)=theta^(−2),
 N1(theta)=A theta^(alpha+a−2)<=A,
 N2(theta)=B theta^(−beta_time/2)<=B theta^(−1).

TakeC0=max(1,A,B),D=max(1,2C0),C1=D². These arefinite model/parameter constants independentofn,t,x andEVERYvertexwidth. This LARGEtheta restriction isretained; itwouldnotjustifytheta=n/t whenn/t<1.

For thesquare ofY_n^bolda, copyitswidthvector to theotherchain andapplyfiniteWickformula. Reverseeachterminalchain at SAME(t,x):s'_j=t−s_(n+1−j),y'_j=x−y_(n+1−j). This preservesLebesguetimeJacobian andGreenpushforwards, permutesthewidthlabels andnegatescovariancedifferences, absorbedbyevenness. The twochains getOWNinitialroots(0,0), notoneconcatenatedroot.

For each oftheP_npairings applyheldauthorTheorem3.1 to dampedkernels exp(−theta r)G_r, withpositiveGreenheat ifneeded. At e={j,l}, itsfinitepositivespectralmeasure isexp(−(epsilon_j+epsilon_l)|xi|²/2)mu(dxi), anditsLaplaceprefixdomain is[0,(delta_j∨delta_l)^(−1)]. Itsinverse is gamma_(epsilon_j+epsilon_l)>=0. Hence theexactfinite-edge hypotheses hold evenwhenallvertexwidthsdiffer.004bounds allnorms bythevaluesabove: firstFourier–Laplaceinnertransform isnonnegative; secondnorms arecovariancequadraticforms andthe positiveGaussianmultipliers canberemoved AFTERtimeintegration. Temporalprefixes canonlydecreasethesenorms.214supplies theindependent-predecessor Case2 coefficient1, without droppingorigindifferences. No unregularizedinfinite-mu orfinite-Fouriermode shortcut isused.

Letq_i=|Q_i| in theuniversalpartition. It satisfiesq0=q1 andq0+q2/2=n. Productweights telescopewithin EACHchain:

 product_l exp(−theta(s_l−s_prev(l)))
 =exp(−theta(s_n+s_(2n)))>=exp(−2theta t).

Theundamped finitehorizon diagram istherefore<=exp(2theta t) times itsdamped infinite-simplex bound. The latter isatmost

 theta^(−2q0)(2C0)^q1(C0 theta^(−1))^q2
 <=D^(q1+q2)theta^(−2n)<=C1^n theta^(−2n).

Thus, forALLpositivevertexwidths andtheta>=1,

 ||Y_n^bolda(t,x)||2²<=P_n exp(2theta t)C1^n theta^(−2n).

Theboundholds beforeGreenremoval andpasses toitsactualL2limit atfixednoisewidths. Thisderivation isuniforminwidths andorders; itdoesnot useany002mixed-infinite-series assertion orsource(5.3)–(5.4)all-timeconstant.

For n>=1,t>0 choose theta=1+n/t. Thenexp(2theta t)=exp(2t+2n),theta^(−2n)<=(t/n)^(2n). Since(2n)!<=(2n)^(2n),

 P_n n^(−2n)<=(2^n)/n!.

WithC=2e² C1 onegets

 ||Y_n^bolda(t,x)||2²<=exp(2t)C^n t^(2n)/n!,
 ||Y_n^bolda(t,x)||2<=q_n(t)=exp(t)C^(n/2)t^n/sqrt(n!).

006L2convergence passes thisboundtoX_n. Putq0(t)=exp(t)>=1 toboundtheemptyterm separately. At t0 allpositiveordersvanish andq0=1 directly; the n/tchoice isnotmade there. The covarianceamplitude remainsinsideA,B(andthereforeC);Cisnonsharp andnotclaimedamplitudehomogeneous. Actualdegree-nterms stillhave noise-amplitudedegreen.

Theoldsourceall-t estimateC^n t^(2n)/n! withouttheexp(2t)repairwouldfail alreadyatn1white: c0t^(3−a)/(Ct²)→infinity. Thecurrent extraexp(2t)andtheta>=1restriction avoidthat falseuniformity. This isconstruction-scalecrudecontrol, not the sharp t^kappa upper rate.

##3.008: weighted summability andexplicit usable tails

For fixedT>0 setz=sqrt(C)T andr_n=sqrt(n+1)q_n(T). Then

 r_(n+1)/r_n=z sqrt(n+2)/(n+1)→0.

Hence sum_n sqrt(n+1)q_n(T)<infinity. Morequantitatively, rratio<=z sqrt(2/(n+1)). Given0<rho<1, chooseintegerNwithN+1>=2z²/rho². For n>=N theweightedratios are<=rho, yielding

 sum_(n>N)sqrt(n+1)q_n(T)
 <=sqrt(N+2)q_(N+1)(T)/(1−rho).

Theplainratio isz/sqrt(n+1), so theunweightedtail hasthesameboundwithsqrt(N+2)removed wheneverthatplainratio<=rho. Allconstants arefixedbeforethewidthlimits. Sinceq_n(s)<=q_n(T) for0<=s<=T, thesetailboundsareuniform intimeuptoT, inspatialx, andallactualpositivevertexwidths. This isnot a normofaspatialsupremumor a samplewiseuniformspacetimeconvergence assertion.

Inparticular Q_T=sum q_n(T)<infinity. Minkowski constructsu_series=sum X_n inL2 withoutP:mixed. TheelementaryCauchy–Schwarzseriesbound

 (sum_(n>=0) z^n/sqrt(n!))²
 <=(sum2^(−n))(sum(2z²)^n/n!)=2exp(2z²)

also givesE|u_series(t,x)|²<=2exp(2t+2Ct²). ThisisderivedAFTERnormsummability, notassumedfromthetargetmoment. The constantsarethecurrentfixedmodelones; n0/zeroGammacasesaredirect.

##4.002: thefinite unequal-chain identity ontheSAMEfamily

Fixm,n,t,x. Atpositivevertexwidths, finiteGaussianWickformula givesE[Y_m^bolda Y_n^boldb]=0 ifm+n isodd. Ifm+n=2k itis aFINITE sumoverD∈Pi_k, eachcoefficient1, withtheactualmixed max-time/summed-space covariance from§1. A zero-orderfactor remains1. TheGreenwidthlimits comeFIRST atfixedpositive externalwidths.

For aterm's initial-chain convention, in thefirstterminalchain set

 s'_j=t−s_(m+1−j), y'_j=x−y_(m+1−j),1<=j<=m,

anduse thelength-n version onthesecondchain. TheterminalfactorG(t−s_m,x−y_m) becomesG(s'_1,y'_1); theothers become successiveGreenincrements. Thevertexinvolution isrho(j)=m+1−j andrho(m+j)=m+n+1−j. Itpreserves absolute timeJacobian1 andbijectionsofGreenpushforwards. Time/spatialcovariance differences changeSIGN; evenness absorbsthesesigns. Thepairingbijection isD→{{rho(a),rho(b)}:{a,b}∈D}. Thewidthlabels arepermutedwiththeirvertices, neverdiscarded. EachfirstvertexusesitsOWNroot(0,0); thesecondchain doesNOTcontinue thefirst. Emptychains have noverticesandfactor1.

Thus thefinite diagramlimit isprecisely thecurrentinitial-chainJ_(m,n,D)(t):integrateproductsof successiveG over[0,t]^m_<×[0,t]^n_<, timesone fulltime/spatialcovariance factorperpair. For generalRadonGamma/white/d3, thatnotation denotes the actualjointlimit ofthese positive regularizedintegrals suppliedby005/006, NOT pointwise multiplicationofmeasure/distribution densities. Thetransformation isvalid BEFOREnoise removalandonlyidentifiesmoments attheSAMEterminal(t,x). Itdoesnotassert pathwise equalitywithaforwardnoiseintegral. Differentterminaltimes wouldretaintheirtime-origin offset.

006gives Y_m→X_m,Y_n→X_n inL2 andtheindividualdiagramlimits. Theproductpassage isEXPLICIT:

 ||Y_mY_n−X_mX_n||1
 <=||Y_m−X_m||2 ||Y_n||2+||X_m||2 ||Y_n−X_n||2→0.

ThefiniteYn normsareboundedalongthelimit(evenuniformlyby008). Hence

 E[X_mX_n]=sum_(D∈Pi_k)J_(m,n,D)(t)>=0 ifm+n=2k,
 E[X_mX_n]=0 ifm+n odd.

For m=n0 thevalueis1, withunitmassontheemptytuple. Thefinitepairingcount isP_k, notP_mP_n, andincludes selfpairsandallunequalsplits. No independencebetweenX_m,X_n wasintroduced. Inparticular§0’spositive1+3term survives.

##5.002: fullseries/expectation/Fubini with anactual all-order bound

By008, forfixed(t,x),sum||X_n||2<=Q_t<infinity. Thisalreadyconstructsu_series inL2 withoutusing002. Moreover

 E sum_n|X_n|<=sum_n||X_n||2<=Q_t,
 sum_(m,n)E|X_mX_n|<=sum_(m,n)q_m(t)q_n(t)=Q_t²<infinity.

Tonelli impliessum|X_n|<infinity almostsurely ATTHISfixedpoint; thea.s.sum equals theL2sum byuniquenessinprobability. Its absolutelyconvergent productseries is u_series². AbsoluteFubini now gives

 E u_series²=sum_(m,n>=0)E[X_mX_n].

Alternatively, U_N=sum_(n<=N)X_n satisfies

 |E U_N²−E u_series²|
 <=||U_N−u_series||2(||U_N||2+||u_series||2)
 <=2Q_t sum_(n>N)q_n(t)→0.

These areindependent justifications; neither assumes themomentidentity itisproving. Sinceeachfinite mixedexpectation in§4 isnonnegative, E U_N² increases NUMERICALLY withN, though U_N² neednotincrease samplewise. Thedoubleexpectationseries isabsolute andnonnegative, soeveryenumerationagrees. Grouping bytotalorder2k gives

 E u_series(t,x)²
 =sum_(k>=0) sum_(m=0)^(2k) sum_(D∈Pi_k)J_(m,2k−m,D)(t).

This proves theassertedfullnonnegativeexpansion.009 separately proves thattheSAMEcanonicalseries satisfies thesourceDefinition2.1Stratonovichmildequation; itdoesnot supplynormsummability or themixedidentity andneedsno002infinite expansion. Thus namingthisseriesu as theactualconstructedmildsolutiondoesnotmakea002↔009cycle or invoke auniqueness theorem.

Everymixedmoment, regularizedorcanonical, obeys |E Y_mY_n|,|E X_mX_n|<=q_m q_n. Since itsWickdiagramtermsarenonnegative, eachindividualdiagram isalso<=thatfinitebound. Thetotalorder2kcoefficient istherefore boundedby

 e^(2t) C^k t^(2k) sum_(m=0)^(2k)1/sqrt(m!(2k−m)!)
 <=e^(2t) C^k t^(2k) 2^k sqrt(2k+1)/sqrt((2k)!).

Thelastinequality isfiniteCauchy–Schwarzonsqrt(binomial(2k,m)). This is avalidcrudemajorant, not anidentification ofeachdiagram orasharpconstant. TheRAWdiagramcardinality is(2k+1)P_k(3,15,105atk1,2,3); itisnotanormalizedtimecoefficient. Factorslike2^k/k! ariseonlyaftertheirparticulartimeintegration/orderingcalculation, notfromreplacingeveryactualJbyoneidenticalintegral.

##6. Actual downstream use: source limits and uniformintegrability

Letu_rho=sum_nY_n^rho atCOMMONpositive noisewidthrho, afteritsinnerGreenlimit.008givesabsoluteL2series andtheUNIFORMtailbound sum_(n>N)q_n(t). ForfixedN,006gives itsfiniteprefixconvergence tosum_(n<=N)X_n. Hence

 ||u_rho−u_series||2
 <=sum_(n<=N)||Y_n^rho−X_n||2+2sum_(n>N)q_n(t)→0

byFIRSTwidths→0 atfixedN, THENN→infinity. Theratesofthetwonoisewidthsarearbitrary. Consequently

 E|u_rho²−u_series²|<=2Q_t||u_rho−u_series||2→0.

This supplies actualpointmomentconvergence anduniformintegrabilityofthesquaresALONGthewidthlimit. AuniformL2boundalone wouldNOT implyUIofsquares; thefiniteprefixplusuniformtail convergenceisessential. ItdoesnotassertglobalspatialL2control ofconstantdata, randomspacetimesuprema, operatornormUI, allLp-momentboundsor uniformityincovariancemodels. Thoseclaimswouldneedtheirowninputs.

Themaskedsource consumers101–103canusetheexacttails: atpositivewidths,onevertexmask0<=m<=1 preservespositivityofeachGaussianWickdiagram, soE|Y_(rho,n)^m|²<=E|Y_(rho,n)|²<=q_n². Testingbycompactnonnegativephi costs||phi||1, notapointtrace. Forunmaskedmomentlimits eachm,ntermconvergesby006andisdominatedbyq_mq_n, summableonN². Thusfiniteorderlimitsplus008uniformtails justifythecanonicalpoint-momentpassage in103; anL2limitofactualmaskedaverages isstillanADDITIONALconditionalpremise, notcreatedbytheq_nbound. NoPSDorderbetweennonlinearwavesisasserted.

##7. Whytheextra sqrt(n+1)weight isreally consumed

Atfixedexternalwidthrho putH=W_rho(s,y), sigma²=E H²=V_rho<infinity. IfRisin theclosedGaussianpolynomialspaceoftotaldegree<=n, then

 ||H R||2<=(sqrt(n+1)+sqrt(n))sigma||R||2
 <=2sqrt(n+1)sigma||R||2.

A directderivation permitsfullcorrelation. Forsigma>0 chooseGaussianbasisfirstcoordinateG1=H/sigma. Expandafinitedegreepolynomial innormalizedHermitesofG1 withcoefficientsintheorthogonalGaussiancoordinates. TheidentityG1 h_j=sqrt(j+1)h_(j+1)+sqrt(j)h_(j−1) gives creationnorm²<=n+1 andannihilationnorm²<=n ondegree<=n. Addtheirnorms. Finitepolynomialapproximation extends theinequality tocloseddegree<=n; theproductsareL2Cauchy, and an a.s.subsequenceidentifies theirlimitwiththeACTUALproductHR. Sigma0 isdirect. NoindependenceofH andR isassumed.

EachY_n is anL2integral ofordinarydegree-nGaussianproducts, andX_nitsL2limit, hence liesinthatcloseddegree<=nspace, withlower self-contractionchaosesretained. Atfixedexternalrho,

 ||W_rho(s,y)X_n(s,y)||2
 <=2sqrt(n+1)sqrt(V_rho)q_n(T),0<=s<=T,
 sum_n||W_rho X_n||2<=2sqrt(V_rho)sum_nsqrt(n+1)q_n(T)<infinity.

DO NOT applythefinite-degreeinequalitydirectlytotheinfinite-degreeu. Insteadpartialproductseriesconverges inL2 bytheweightedtail; an a.s.subsequenceofpartialsumsofu identifiesitslimit asW_rho u. Thisgives theactualfixed-rho productbound usedby009. V_rho mayblowup asrho→0; no uniformrho boundisclaimedorneededforitsGreen-FIRSTstep.

For009’spartial-vertexconsumer,theadditionalactualGreen/productargument proves atfixedexternalrho thatI_(n,rho)=integralG W_rho X_(n−1) istheinner-widthlimitofY_n^(inner,rho).008passes throughTHATlimitto ||I_(n,rho)||2<=q_n(t), uniformintheexternalrho;thisisnotobtainedfromtheblowing-upV_rho bound.006jointness thenremovestheexternalwidth, fixednfirst. Thefullmildsourceintegral usesitsfiniteprefixplus2sum_(n>N)q_n(t) remainder. ActualGreenaveraging requiresarandomfactorfixedintheGreenwidth,L2continuityoncompactspatialsets andfiniteGreenmass; itisprovedin009/theexistingGreenworking, notimpliedbyweightednormsummabilityalone. Thisnoteidentifiestheprecisepremiseandusewithoutreprovingall009.

##8. Dependence, zero branch andtrue-gap boundary

Theacycliclogicalspine is004+214+finite-edgeexternal3.1and005/006fixedorders →008all-ordernormtail →canonicalL2series.002’sFINITEidentity uses006/Wick; itsINFINITEidentity thenuses008.009consumesthesame008tail/006jointlimitsandoccupiedproducts to identifythatseriesasmild.001Jensen,010numericalmajorant,103sourcepointmomentand119scaling canthenconsumetheiractualclauses.051’sindependenttarget-scaleproof isnotfinancedbythiscrudeexp(Ct²)constructionestimate anddoesnotneed002’sinfiniteidentity asitsratepremise.

ForGamma0,allpositive-ordercutofftermsandX_nare0,u1;bothassignedstatementsfollowdirectly. Nonzeroamplitude,white/singularspectraandd1/2/3arepreservedwithoutdensity/finiteoriginalmu-total assumptions. ConstantsC0,D,C andq_narefixedmodelconstants, independentofn,t,x,sourcewidthsandGreenwidths, withtheexplicitgrowthintimealreadyshown. No convergenceuniformintheentiremodelclass or covariance-shapesisclaimed.

Noactualgapwaslocatedintheassigned002/008calculationsundertheexposedfixed-order/norm/sourcehypotheses. All-ordertailcontrolwasDERIVEDusingthen-uniformuniversalbound, notborrowedfromfixed-nexistence. Thisisauthorworking,notindependentreview,ancestoracceptance,whole214/240/13HIGH,sourcepixel/Kimi/visual/coldorcompletioncredit. NoArticle/source/Git/model/CLI/network/private-reasoning/frameworkactionoccurred.
