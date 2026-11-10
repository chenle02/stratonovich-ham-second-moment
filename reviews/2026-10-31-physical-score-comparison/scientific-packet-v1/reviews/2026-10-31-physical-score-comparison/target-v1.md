# PB1-PB5 actual physical signed-to-positive score target

UNREVIEWED proposed statements,not a theorem/premise/noveltyclaim. Freeze
before external literature implication audit and newdiagnostics/proof.
Original authorL_*/L^* sharpconstants/intendednormalization remainrequired;
this ownscore target does NOT replace that contract. No actualp1identity.

## Original model and accepted inputs

ALL original H:homog even nonnegative positive-definite homogeneous tempered
Radon Gamma/amplitudes,d=1,2,3,0<a<1,0<alpha<d or alpha=d=1,alpha+a<2.
ZeroGamma treated directly. Rawreal H_I=H_t tensor H_sp with ORIGINAL
covariance K(s,t)Gamma(x-y),K=|s-t|^-a onI=(0,1),notrescalednoise/action.
Real E=Hhalf x Hminus-half,unitary Fourier,Lambda=(1-Delta)^(1/2).
Fixed smooth even plateau rooteta,0<=eta<=1,eta=1onB1,suppB2,
m_R=eta(x/R)^2 ONCE aftersmoothing,R>=1. Do notassumemonotonicityinR.

Fix admissible U/US s_sp,r,theta andotherauxiliaries ONCE,independentR/n;
C_mean>=0 is the accepted R-uniform completed E mean bound (choice-dependent).
mathcalT_R:H_I->Lr(I;K(E)) is the actualmean; Rate_R(Phi)=int_I lambda(
mathcalT_RPhi(s))ds uses US1 realH1Rayleigh form with FULL kineticgradient.
 S_R=sup_(Phi inH_I)[2Rate_R(Phi)-||Phi||HI^2/2].
Accepted UR states originalpoint limsup at kappa_scale is<=limsup_delta
S_(delta^-1+2). Accepted PG finite lemma gives active-setdual/positivecone
optimizer andoptimizedENTRYWISEGrammonotonicity,notphysicalcomparison.

Accepted unmasked-variational-lower61ac2a3 defines C_pos as ALLnonnegative
nonzero real C_c^infinity(I xR^d),includingNONSEPARABLEtests. For Psi inC_pos,
 h_Psi,s=int_I K(s,t)(Gamma*Psi(t,.))dt,
 v_Psi=||Psi||HI^2=E W(Psi)^2=int Psi h_Psi,
 I_Psi=int_I sqrt(-inf_spectrum(-Delta-h_Psi,s))ds.
Its Section3(11) is the exactREALunitH1Rayleigh formula,withoutrequiring an
unmaskedgroundeigenstate. Its originalpointliminf>=2I_Psi-v_Psi/2,and
 S_c^pos=sup_(Psi inC_pos)[c I_Psi-v_Psi/2]=c^m S_1^pos>0finite,
 m=(4-alpha)/(3-alpha),fornonzeroGamma. Finitenesswas obtainedusingtheOLD
canonicalupper,not the newcomparison. S_1^pos is auxiliary,NOTactualmean
or an identifiedauthorconstant. ForGamma0 defineS_c^pos=0,u=1 directly.

## PB1: actual normalized raw labels and positive Gram entries

For a finitepartition into nonempty intervals I_i,lengthell_i>0,sumell=1,
and REAL f_i inC_c^infinity(R^d),||f_i||2=1,put
 h_i=1_Ii/ell_i,b_i=||grad f_i||2^2,
 k_i^R=h_i tensor(m_R f_i^2), k_i^infty=h_i tensor f_i^2.
These are genuineH_Ilabels,notoperatorsmasking arbitraryrawPhi. ForEVERYPhi,
 <Phi,k_i^R>HI=(1/ell_i)int_Ii v_(mathcalT_RPhi(s))(f_i,f_i)ds,       (PB1a)
wherev isHminus/Hhalfdualpairing of the displacementmultiplier. Proveexact
normalization using U2's Erow z=(f_i,0),w=(0,Lambda f_i),whoseproductis
eta_R f_i*eta_R f_i=m_R f_i^2. No additionalGamma/convolution/c_d factor.
 C_ij^R=<k_i^R,k_j^R>, D_ij=<k_i^infty,k_j^infty>
areactualsymmetricPSDGrams with0<=C_ij^R<=D_ij ENTRYWISE. D-C neednotPSD.
Allspatialpairings usephysicalGamma measureandtimekernel,includingwhite.

## PB2: uniform optimizer norm and positive smooth approximation

Set M_*=4C_mean+4. For the UNMASKED finiteprofile objective
 J_D(Phi)=2sum_i ell_i sqrt((<Phi,k_i^infty>-b_i)_+)-||Phi||HI^2/2,
PG yields anattainednonnegative maximum,withoptimizerPhi_D=0 or a positive
sum of eligible unmaskedlabels. ChoosefiniteR' containingALLf_i supports,
so m_R'=1there. For EVERYrawPhi (notjustoptimizer),
 J_D(Phi)<=2sum_i ell_i lambda(average_Ii mathcalT_R'Phi)-||Phi||HI^2/2
          <=2+2C_mean||Phi||HI-||Phi||HI^2/2.                (PB2a)
Use frozenRayleigh and averagedL1budget/JensenforNORM,not timeapproximation
or concavityofsqrtpositivepart. Thereforea nonnegative maximizingvalue
has anoptimizerwith||Phi_D||HI<=M_* uniformlypartition/profiles. Thisnorm
bound MUST be established BEFORE invoking US2 forPhi_Dvaryingwithgrid.
S_R likewise restrictstosignedcontrols||Phi||<=M_* sinceoutsideboundnegative.

Forfixedgrid/profiles/nonemptymaximizingbranch,positive time smoothing
h_i,j inC_c^infinity(I),h_i,j>=0,h_i,j->h_i inL2 gives
 Psi_j=sum w_i h_i,j tensor f_i^2 inC_pos,
                Psi_j->Phi_D strongly inH_I.              (PB2b)
KhasboundedrowsK0=2^a/(1-a),so||h||Ht^2<=K0||h||2^2; spatiallabelsC∞
lieH_sp. Atfixedgrid allweights/profile-norms finite; no uniformL2bound
onPhi_Dor smoothingderivatives isassumed. Rawaction andRate_R'(Psi_j)
converge; rateerror canbecontrolleduniformR' viaUS15/U17 onboundedH_Iballs.
Ifmaxbranchisempty,usevalue0<=S_2^pos without requiring0inC_pos.

## PB3: actual signed raw score versus accepted positive lower score

For EVERY R>=1,
                              S_R<=S_2^pos.              (PB3)
Proposedroute: equal partitions mesh1/n (US2 atB1,delta1/n,emptylastomitted),
realunitH1Rayleighdensity viarealcompactC∞profiles,PGentryGramcomparison/
positiveoptimizer,PB2NONCIRCULARnormbound,US2uniformtimeavg onboundedPhi_D,
thenPB2smoothpositiveapprox andmasked<=unmaskedpositivepotentialFORMorder.
Alltime/rawlabel/cost normalizations anderrorquantifiers mustbe proved.
No wrongJensenfor sqrt((.)_+),no measurablecontinuumoptimizer,no unmasked
randomoperatororH_IvaluedwhiteGaussian,nocovarianceorder ofarbitrarywaves.
For eachsmoothpositivePsi,Rate_R'(Psi)<=I_Psi,by0<=m_R'<=1/h_Psi>=0 and
realH1forms. LowerclassALREADYincludesPsi; no d1roughXinput usedasallGamma.

## PB4: actual moving-mask score limit,without monotone cutoff family

For everyFIXED Psi inC_pos,Rate_R(Psi)->I_Psi asR->infinity,usingcompact
realH1trialprofiles,eventualplateau1andtheunmaskedboundedpotential. No
unmaskedgroundeigenstate/differencePSD/noisecovariancemonotonicityassumed.
Consequently
                         lim_(R->infty)S_R=S_2^pos.        (PB4)
PB3givesupper,positivePsi fixed inS_R giveslower,then takeC_possup. All
controlsarefixedbeforeanymomentlimit; nodiagonaltestsequenceinlower theorem.

## PB5: original all-model p2 own variational limit

Withkappa_scale=(4-alpha-a)/(3-alpha),everyfixedx,
 lim_(T->infty)T^-kappa_scale log E|u_Gamma(T,x)|^2
              =S_2^pos=2^m S_1^pos.                      (PB5)
Thisproposedownscorelimit wouldfollowURupper+PB3or4+acceptedpositiveLOWER.
Sourcefirst/self/mixed/emptychains/canonicalstationarity/calibrationsretained.
No claimS_1^pos=actualp1/authorL_*orL^*,andno printedenergyrepair/closing
sourcegap isbeingassumed. Intendedsourceconstantcomparisonstillseparate.
Gamma0giveslimit0directly. Formal a->0kappa matchesstaticexponent; no
uniformaendpointclaim or staticwhiteconstantrepair. No Skorohodresult.

## Required pre-proof screens and scope

Runlocalwiki search/cite/syntheses andclosestprimary/version/implication
crosswalk beforeproofinvestment. Fieldindexes/citationchains attempted,
readcoverageandnoveltylimits honest. No theorem/paperpromotiononmissing
sources. Freezebefore newdiagnostics. Actuald1white control/labelrowtest
mustexerciseamp!=1,unequalell,onephysicalmask andmasked/unmaskedGram.
ActualRiesznonlocalpositiveprofiles canrefuteanunneededLoewnerdifference
assumption. Scalarpositiveparts mustrefutewrongJensendirections. No
finitecalibration/PDEsimulation/enclosure/globalconfidence claim. Preserve
precision-specificresiduals/maximizingcases. ExistingPGkernelreusedatnew
actualH_Iguardfit,notrecompiledunchanged or creditedaswholePDEformalization.

EveryNEWanalyticlinkneedsitsOWNsource/statementFITandFULL independent
proof/application gate. Originalsharp/sourceobjectiveACTIVE; no correspondence,
publicrelease,HPC,companion/source/TeX/PDF/wiki/bib/siblingedits. Helpful
missingreferencesqueuedcanonicallywithverifiedmetadata/receiptswhenfound.
