# Actual two-variance deductions069/071/073/074

Author reconstruction of the four CURRENT written deductions, not a reviewer verdict, source edit or new theorem. Exposed CURRENT OWN input clauses are tabulated separately. The model is originalH:homog: d=1,2,3;0<a<1;0<alpha<d oralpha=d=1;alpha+a<2;Gamma is even,nonnegative,PD,homogeneous tempered Radon. Its spectral convention isGamma=integral exp(i xi·x)mu(dxi) distributionally, but spatial Fourier transforms below are UNITARY with c_d=(2pi)^(−d/2). This distinction fixes every Fourier constant. The original covariance amplitude is retained.

##0. Falsification controls before the general estimates

At frequencyzero, sin(tr)/r→t, not0 or infinity. The normalized phase kernel computed below is[[-t,−t²],[1,t]], so neitherphase entry disappears. In particularK21=1 has temporal norm SQUARED

 ||1_I||_Ha²=integral_I²|t−s|^(−a)dtds
 =2h^(2−a)/[(1−a)(2−a)].

Replacing a squared norm by its norm loses the requiredtime power. Forr=rho→infinity, cos(rt)cos(rho t)=(1+cos(2rt))/2 has a constant component. Since the integrable kernel1_(I×I)|t−s|^(−a) has a vanishing Fouriertransform atinfinitefrequency, its exact squarednorm tends to onequarter of||1_I||Ha². A bound using onlyr+rho, or multiplying independent single-frequency gains, would incorrectly force its temporal covariance tozero. The r−rho term is indispensable.

For whiteGamma=c delta0 in d1,mu=c dxi/(2pi). The auxiliarynu_R is exactly constant-density c L_zeta²/(4pi²) dxi. Atxi=0,

 Phi_h(0,−lambda)=2<hlambda>^(a−1)/<lambda>.

Forh<=1/2 and1<=|lambda|<=1/h this is bounded below by a positivea-dependent constant/|lambda|. Thus itsnu_R integral grows at least aslog(1/h); B1(h)=1+log(1/h) cannot be replaced by a uniformconstant in the general scalar row lemma. This is a kernel control, not a claim of a sharp lower asymptotic for every actual wave form.

The necessity of both gain directions is also visible without SPDE assumptions. In a two-dimensional Hilbert model let the weaker input norm be|z1|²+L^(−2gamma)|z2|², andA=|e1><e2|. For a scalar standardGaussianG andell(z,w)=G<Az,w>, the input-family variance is||A*z||²=|z1|² and has constant1 against the weaker norm. The output-family variance atz=e2 is||Az||²=1 and requiresconstant>=L^(2gamma). One direction alone cannot imply the other balanced-gain bound. This is a finite linear falsification, not a counterexample to the actual wave estimates proved below.

##1. Covariance and mask constants actually used

Let M_Gamma=integral exp(−|x|²/4)Gamma(dx) andC_Gamma=e M_Gamma/(2sqrt(pi))^d. Temperedness gives finiteness; nonzeroGamma gives positivity. Applying the distributional spectral identity to ONEGaussianSchwartz test gives exactly

 integral exp(−|xi−y|²/r²)mu(dxi)
 =(r/(2sqrt(pi)))^d integral exp(−r²|x|²/4)exp(−iy·x)Gamma(dx).

The absolute value removes the phase becauseGamma>=0. Radon homogeneity gives the remaining spatial integral r^(alpha−d)M_Gamma. OnB(y,r) the Gaussian is>=e^(−1), so

 mu(B(y,r))<=C_Gamma r^alpha, all y,r>0.

This is the061 clause used, not an angular density or a centered-ball-only assumption. A closed ball follows by applying the open-ball bound atr+epsilon andepsilon→0. Positivealpha implies no spectral atom; this does NOT forbid the physical origin atom of spatialwhiteGamma.

For the fixed real smooth maskshapezeta, zeta_R(x)=zeta(x/R),k_R=zeta_R-hat=R^d zeta-hat(R·),L_zeta=||zeta-hat||1=||k_R||1. Define the actual auxiliary measure

 nu_R(deta)=rho_R(eta)deta,
 rho_R(eta)=c_d² L_zeta integral |k_R(xi−eta)|mu(dxi).

No density ofmu is assumed. Schwartz decay against a temperedmeasure makesrho_R finite/continuous oncompacts; evenness ofmu and|k_R| givesnu_R even. Tonelli gives

 nu_R(B(y,r))=c_d² L_zeta integral |k_R(u)|mu(B(y+u,r))du
 <=C_nu r^alpha, C_nu=c_d² L_zeta² C_Gamma,

uniformly inR>0. The centered-ballbound gives temperedness ofnu_R. For Hilbert-valuedSchwartzF, Fourier convolution and weightedCauchy–Schwarz give

 ||(zeta_RF)-hat(xi)||H²
 <=c_d² L_zeta integral |k_R(xi−eta)| ||F-hat(eta)||H²deta.

Integratingmu andTonelli gives the062 auxiliary contraction. Originalnoise covariance, with the UNITARY spatialtransform, is

 E|W_C(F)|²=(2pi)^d integral ||F-hat(xi)||_(HaC)² mu(dxi).

Hence masked noise is bounded by the sameright side withF-hat andnu_R. Theauxiliary measure is a bound for actualmaskednoise, not a claim that masking preserves stationarity or the originalnoise quotient.

As a normalization check on the Riesz/resolvent constants, V=mu(B1) impliesmu(B_r)=V r^alpha, so radial Stieltjesintegration gives

 integral mu(dxi)/(rho²+|xi|²)
 =alpha V integral_0^infinity r^(alpha−1)/(rho²+r²)dr
 =R_alpha rho^(alpha−2), R_alpha=alpha*pi*V/[2sin(pi alpha/2)].

Also C_Gamma=e Gamma_E(1+alpha/2)V by the centered Gaussian identity. For any translated-growthmeasure withconstantC (includingnu_R), layercake gives the nonhomogeneous BOUND

 integral nu(dlambda)/(rho²+|lambda−y|²)
 <=2C integral_0^infinity r^(alpha+1)/(rho²+r²)²dr
 =C[alpha*pi/(2sin(pi alpha/2))]rho^(alpha−2).

Only for actualhomogeneousmu atcenter0 is the previous exactR_alpha formula asserted. ForwhiteGamma=c delta0 it yieldsR1=c/2. These checks keep amplitude and Fourier factors; the row proof uses its explicit shell estimates, not an assumed isotropic covariance identity.

##2. Temporal squared-kernel estimate, including zero frequencies

The real temporalcompletionHa has kernel|t−s|^(−a); its complexification uses conjugation in the second slot. The063 Schur bound is

 ||f||Ha²<=2T^(1−a)/(1−a)||f||L2(0,T)².

This admits bounded interval amplitudes and supplies separableHa. ForA inC1(I),M=sup|A|,D=sup|A'|, let c(v)=integral_(t0)^(t0+h−v) A(u+v)conj(A(u))du. Then c(h)=0,|c(v)|<=hM² and|c'(v)|<=M²+hMD, including the moving-endpoint term. The squared temporalnorm of1_I A exp(iomega t) is

 2h^(2−a) Re integral_0^1 y^(−a)exp(iomega h y) f(y)dy,
 f(y)=c(hy)/h, |f|,|f'|<=(M+hD)², f(1)=0.

For|omega h|<=1, absoluteintegration suffices. Fork=|omega h|>1 split at1/k; the low part is<=(M+hD)² k^(a−1)/(1−a). Integrationby parts on[1/k,1] has no endpointat1; its other endpoint is<=(M+hD)²k^(a−1), and its derivative integral is<=(M+hD)²k^(a−1)(1+1/(1−a)). Since k^(a−1)<=sqrt2<k>^(a−1), the constant C0(a)=16/(1−a) suffices:

 ||1_I A exp(iomega t)||Ha²
 <=C0 h^(2−a)(M+hD)²<homega>^(a−1).

Expanding a product of sine/cosine factors atfrequenciesr,rho producesfour coefficients ofmodulus1/4 at±r±rho. WeightedHilbertCauchy–Schwarz, not orthogonality or independence, bounds its squarednorm by C0 h^(2−a)(M+hD)² Q_h(r,rho), where

 Q_h(r,rho)=<h(r−rho)>^(a−1)+<h(r+rho)>^(a−1).

Define c_r(t)=cos(rt), b_r(t)=<r>sin(rt)/r forr>0 andb0(t)=t. Forr>=1,b_r is a sine withcoefficient<=sqrt2. For0<=r<=1,

 b_r(t)=t<r> integral_0^1cos(vrt)dv.

Thus any productF_rG_rho, F/G∈{c,b}, is coefficient<=2 times a probabilityaverage of t^j times a trigproduct, j=0,1,2, with each frequencychangedbyatmost1. The average is Bochner inHa by L2continuity andSchur. ForA=t^j,(M+hD)²<=(1+T)^4. Each altered h(r±rho) differsbyatmost2; bracketcomparisons andnegative exponenta−1 cost<=3^(1−a). Jensen andthe squaredcoefficient bound4 give

 ||1_I F_rG_rho||Ha²
 <=C1(a)(1+T)^4 h^(2−a)Q_h(r,rho),
 C1(a)=4*3^(1−a)*C0(a).

This derivation coversr0,rho0 andresonancer=rho explicitly; no division byzero or productofindependenttemporalnorms is used.

##3.069: complete scalar row for a measure

Supposenu(B(y,r))<=C r^alpha, C>=0; noevenness or density is needed HERE. Let

 Phi_h(xi,eta)=Q_h(|xi|,|eta|)/(<xi><eta>),
 J_h(xi)=<xi>^(2gamma) integral Phi_h(xi,xi−lambda)nu(dlambda),
 0<gamma<min(1/2,(2−alpha)/2).

IfC=0, coveringRd bycountablymanyfiniteballs givesnu0. ForC>0 fixxi andpushnu forward toeta=xi−lambda. Writeq=max(1,|xi|),epsilon=1−2gamma>0. Thepushedmeasure hasmass<=Cr^alpha oncenteredballs. ForN=ceil(log2(5q)), unitballplusannuli gives

 A_xi(q)=integral_(|eta|<=5q)<eta>^(−1)nu_xi(deta)
 <=C[1+2^alpha sum_(j=0)^(N−1)2^(j(alpha−1))].

Since5q<=2^N<10q, this is<=K_alpha C times1 ifalpha<1,1+logq ifalpha1,andq^(alpha−1) ifalpha>1.

On|lambda|<=4q,|eta|<=5q andbothQ brackets<=1, so the near contribution is<=2q^(−epsilon)A_xi(q). Foralpha<1 this is bounded. Foralpha1 use exp(−epsilon u)(1+u)<=1+1/(e epsilon),u=logq. Foralpha>1 its power isq^(alpha+2gamma−2)<=1 by the strictgaincondition. Hence thenearpart<=K_(alpha,gamma)C.

Onr=|lambda|>4q, |eta|>=3r/4, ||eta|−|xi||>=r/2, |eta|+|xi|>=r/2. Therefore each oscillatorybracket is>=<hr>/2. Usingnegative exponent and<eta>^(−1)<=4/(3r),<xi>^(−epsilon)<=1, thefarpart isatmost

 (4/3)2^(2−a) integral_(|lambda|>4q) r^(−1)<hr>^(a−1)nu(dlambda)
 <=K_(alpha,a) C S(h),
 S(h)=sum_(j>=0)2^(j(alpha−1))<h2^j>^(a−1).

ForL=floor(log2(1/h)), splitj<=L andj>=L+1. Lowj usesbracketpower<=1. Highj uses(h2^j)^(a−1); sincealpha+a−2<0, its sum is

 h^(a−1)2^((L+1)(alpha+a−2))/(1−2^(alpha+a−2))
 <=h^(1−alpha)/(1−2^(alpha+a−2)).

Thelow sum is<=1/(1−2^(alpha−1)) ifalpha<1, L+1 ifalpha1, and2^(alpha−1)h^(1−alpha)/(2^(alpha−1)−1) ifalpha>1. Thus

 sup_xi J_h(xi)<=K(alpha,a,gamma) C B_alpha(h),
 B_alpha(h)=1 (alpha<1),1+log(1/h) (alpha1),h^(1−alpha) (alpha>1).

All extendedintegrals are nowfinite. K comesonlyfromthese numericalshellbounds andisindependentofd,nu,C,R,h,xi. It is not uniform at the excludedgain/time endpoints.

For070 choose1/2<beta_H<min(1−a/2,(3−a−alpha)/2). Then h^(2−a)B_alpha(h)<=K_beta h^(2beta_H): alpha<1 uses2−a>2beta_H; alpha>1 uses3−a−alpha>2beta_H; alpha1 usesdelta0=2−a−2beta_H>0 andh^delta0(1+log(1/h))<=1+1/(e delta0). Strictness absorbs the white logarithm.

##4.071: actual raw test, Sobolev adjoint and normalized kernel

Set s=1/2,E_r=H^r×H^(r−1),Lambda=(1−Delta)^(1/2), inner products linear in the FIRSTslot. The unitary phase normalization is

 Jz(xi)=(<xi>^(1/2)z1-hat(xi),<xi>^(−1/2)z2-hat(xi)).

The free matrix isS(t,xi)=[[cos(tr),sin(tr)/r],[−r sin(tr),cos(tr)]],r=|xi|, withsin(tr)/r=t atr0. AfterJ it becomes[[c_r,b_r],[−r sin(tr)/<r>,c_r]], uniformly bounded for|t|<=T and strongly continuous by dominated convergence on Fourier vectors. No operator-norm continuity or E-unitarity is claimed.

Letv_z(t)=[S(t)z]1 and

 G_w(t)=−[sin(t|D|)/|D|]Lambda w1+cos(t|D|)Lambda^(−1)w2.

ForB(b)(u,v)=(0,bu), S(−t)(0,f)=(-sin(t|D|)f/|D|,cos(t|D|)f). The two E-inner-product weights areLambda andLambda^(−1). Moving these real selfadjoint Fourier multipliers onto w yields exactly

 <S(−t)B(b)S(t)z,w>_E=integral b(t,x)v_z(t,x)conj(G_w(t,x))dx.

Thus the output dualwave has the minus sign and DIFFERENT Sobolev weights shown above; it is not the position component ofS(t)w. For a real compact smoothchi multiplying BOTHphysicalphaseentries, weighted duality gives

 D_chi^(star,E)w=(Lambda^(−1)chi Lambda w1,
                    Lambda chi Lambda^(−1)w2).

Inserting an output observation cutoff therefore usesG_(D_chi^star w), notG_(chi w); chi need not be selfadjoint onE. Smooth multiplication is bounded on every required Sobolevspace by Fourierconvolution and<xi>^r<eta>^(−r)<=2^(|r|/2)<xi−eta>^|r|, followed byweightedSchwartzL1*L2. This gives all deterministic identities on states. The raw form itself has NOobservation cutoff:

 F_(z,w)(t,x)=1_I(t)v_z(t,x)conj(G_w(t,x)),
 ell_R(I;z,w)=W_C(zeta_R F_(z,w)).

For Schwartzz,w the free/Bessel multipliers give Schwartz functions with seminorms continuous/bounded ont∈[0,T]. The maskedtest has one compact supportK. Its absolute raw spatial bilinear pairing is bounded by|K|Gamma(K−K)||F(t)||infty||H(u)||infty. TimeSchur then admits smooth temporal approximations of1_I and the continuous temporal profile, including endpoints0,T, in the ORIGINAL noise completion. Constants in this admission may depend onR; no final uniform variancebound is inferred from them.

To identify the auxiliary spectral extension with that original limit, approximateF by finite temporal tensorsF_n converging inL2time in every Schwartzseminorm. Integrationbyparts inx gives

 ||(F_n−F)-hat(xi)||_(L2time)<=epsilon_n<xi>^(−N),epsilon_n→0.

ChooseN large enough for the squareweight to be integrable against BOTHtemperedmeasuresmu,nu_R. Schur supplies convergence in their spectralHa norms. Fixedzeta_R multiplication preserves the seminorm convergence, giving actual maskedraw andmu-spectral convergence too. Thus the two completed objects coincide on the specific products used here. This does not assert multiplication byzeta_R is bounded on the original raw-null quotient; the065 obstruction excludes that shortcut in general.

For complexF=f+ig withreal temporal/spatial tensors, E|W_C(F)|²=EW(f)²+EW(g)². IfA(xi)=<f-hat(xi),g-hat(xi)>_(HaC), reality givesA(−xi)=conj(A(xi)). Evenmu ornu_R cancels the imaginary cross term of||f-hat+i g-hat||² afterintegration. Approximation extends this identity to the present complexproducts. Consequently

 E|ell_R|²=(2pi)^d integral ||(zeta_RF)-hat(xi)||Ha²mu(dxi)
 <=(2pi)^d integral ||F-hat(lambda)||Ha²nu_R(dlambda).

This is actualnoise on the sameW, with complexificationW_C(F)=W(ReF)+iW(ImF). It is linear inz and conjugate-linear inw. No independent real/imaginary or new stationarymaskednoise is introduced.

PutU=Jz,V=Jw,xi=eta+lambda,r=|xi|,rho=|eta|. Direct substitution gives

 v_z-hat(t,eta)=<eta>^(−1/2)(c_rho U1+b_rho U2),
 G_w-hat(t,xi)=<xi>^(−1/2)(−b_r V1+c_r V2).

Therefore the literal two-by-two normalizedkernel is

 K(t;xi,eta)=1/sqrt(<xi><eta>)
              [[−b_r c_rho,−b_r b_rho],
               [ c_r c_rho, c_r b_rho]].

Atxi=eta=0 this is[[-t,−t²],[1,t]], as tested. Fourier multiplication with conjugation gives

 F-hat(t,−lambda)=c_d integral sum_(i,j)1_I K_ij(t;eta+lambda,eta)
                               U_j(eta)conj(V_i(eta+lambda))deta.

Schwartzdecay and the finite-horizon wavebounds give absolute frequencyintegration uniformly intime, hence a genuine BochnerHa integral bySchur. Reflectlambda usingevennu_R in the previous spectralbound; (2pi)^d c_d²=1 EXACTLY. We obtain the actual071 covariancebound

 E|ell_R(I;z,w)|²<=integral nu_R(dlambda)
   ||integral sum_(i,j)1_I K_ij(·;eta+lambda,eta)
               U_j(eta)conj(V_i(eta+lambda))deta||Ha².

There is no leftover Fourierfactor. Using§2 entrywise now gives the normalizedtimekernel SQUARED estimate

 ||1_I K_ij(·;xi,eta)||Ha²
 <=A_T h^(2−a) Phi_h(xi,eta), A_T=C1(a)(1+T)^4.

The denominatorssqrt(<xi><eta>) inK become<xi><eta> after squaring. This is where replacing a squared temporalnorm by a norm would give the wrongfrequency andtime budget.

##5.072 and073: BOTH Bessel variance orientations, with balancedgain

For separablecomplexHilbertH, finiteorthonormal{u_k}⊂L2(Rd;C²) andg∈L2(Rd;H²), expandg in an orthonormalH-basis. On every scalarcoefficient apply scalarBessel to{conj(u_k)} for integrals sum_j u_(k,j)g_j, or to{u_k} for conjugatedcoefficients. Summing the nonnegative scalar inequalities withParseval gives

 sum_k||integral sum_j u_(k,j)(eta)g_j(eta)deta||H²
 <=integral sum_j||g_j(eta)||H²deta,

and the analogous version withconj(u_(k,j)). Each Bochnerintegral exists byL2Cauchy–Schwarz. Independence of the resulting random coefficients is irrelevant; this is a deterministic Hilbert inequality.

HereH=HaC. For eachfixedlambda the kernels below are stronglymeasurable and in the assertedL2space: c_r,b_r are uniformly bounded onfiniteT, theK entries are continuous inL2time includingzero frequencies, Schur transfers continuity intoHa, and shiftedSchwartzcomponents supply spatialL2 integrability. No nu_R integral is presumedfinite yet; those will be nonnegativeTonelli integrals whosefiniteness is proved by the rowbound.

Let{e_k} be a finite complexE_s-orthonormal Schwartzfamily and putU_k=Je_k.

FIRST fixV=Jz in the output slot and sum INPUTphasebasis. For eachlambda define

 g_j^lambda(eta)=sum_i 1_I K_ij(·;eta+lambda,eta)conj(V_i(eta+lambda)).

ApplyBessel inUk to071 and Cauchy–Schwarz only over the TWOoutputcomponents. Then

 sum_j||g_j^lambda(eta)||Ha²
 <=2 sum_(i,j)|V_i(eta+lambda)|²||1_IK_ij||Ha²
 <=4A_T h^(2−a)Phi_h(eta+lambda,eta)sum_i|V_i(eta+lambda)|².

Changingthe Lebesgue variablexi=eta+lambda atfixedlambda andthenTonelli gives

 sum_k E|ell_R(I;e_k,z)|²
 <=4A_T h^(2−a) integral |V(xi)|²
                  [integral Phi_h(xi,xi−lambda)nu_R(dlambda)]dxi
 <=4A_T K C_nu h^(2−a)B_alpha(h)
                 integral <xi>^(−2gamma)|Jz(xi)|²dxi.

The last integral is EXACTLY||z||_(E_(s−gamma))²: bothphasecoordinates lose the SAMEgamma. The orthonormalfamily remained normalized inE_s, not inE_(s−gamma). This proves the first variance orientation.

SECOND fixU=Jz in the inputslot and sum OUTPUTphasebasisV_k=Je_k. Rewrite071 withxi=eta+lambda and define

 f_i^lambda(xi)=sum_j1_I K_ij(·;xi,xi−lambda)U_j(xi−lambda).

Use the CONJUGATED Bessel version onV_k. Cauchy–Schwarz over the TWOinputcomponents gives

 sum_k E|ell_R(I;z,e_k)|²
 <=4A_T h^(2−a) integral nu_R(dlambda) integral
           Phi_h(xi,xi−lambda)sum_j|U_j(xi−lambda)|²dxi.

Aftereta=xi−lambda, the fixedeta row is integralPhi_h(eta+lambda,eta)nu_R(dlambda). Reflectlambda→−lambda using the ACTUALevenness ofnu_R, then usePhi_h symmetry:

 integralPhi_h(eta+lambda,eta)nu_R(dlambda)
 =integralPhi_h(eta−lambda,eta)nu_R(dlambda)
 =integralPhi_h(eta,eta−lambda)nu_R(dlambda)
 <=K C_nu B_alpha(h)<eta>^(−2gamma).

This proves the second inequality with the SAMEconstant

 C_T=4 C1(a)(1+T)^4 K(alpha,a,gamma)c_d² L_zeta² C_Gamma.

It depends on the originalmodel/amplitude,d,maskSHAPE,exponents,T, butNOTonR,I,h,orthonormalfamilysize or a chosen spectral density. The scalarrow069 itself didnotneed evenness; the reflected secondwaveorientation DOES. No nonnegative physical inversecovariance fornu_R or arbitrary-phasecovariance monotonicity was used. Applying070 at the two row integrals replacesh^(2−a)B_alpha(h) by C_beta h^(2beta_H), withstrictbeta_H window andwhite logarithm absorption.

This calculation exposes the two gain/adjoint substitutions: the literalG_w already carriesLambda versusLambda^(-1) in its two entries; afternormalization each variance direction places<frequency>^(-2gamma) on the FIXEDphasez at its own frequency. It doesnot put that weight on the orthonormalfamily or identify the two row operators before reflection.

##6.074: original-W columns and adjointcolumns, without independence

Choose a countable realSchwartz orthonormalbasis{e_k} ofE_s. To obtain it, first approximate realphase Fouriercoordinates by compact smooth ones and replace eachg(xi) by(g(xi)+conj(g(−xi)))/2. InverseBessel/Fourier maps give realSchwartz phases, dense in the weightedL2norm. Gram–Schmidt on a countabledensefamily, discardingzero residuals, preserves realSchwartz and yields the basis. The sameclass is dense inE_(s−gamma).

For fixed realSchwartzz define on the SAMEoriginalW

 m_Nz=sum_(k<=N)ell_R(I;z,e_k)e_k,
 n_Nz=sum_(k<=N)ell_R(I;e_k,z)e_k.

These finite sums have correlated centeredGaussian coefficients. Orthogonality of the PHASEbasis, not independence of coefficients, gives

 ||m_Mz−m_Nz||_(L2(Omega;E_s))²
 =sum_(N<k<=M)E|ell_R(I;z,e_k)|²,

and the identical formula for n withtheotherorientation.073 bounds the full nonnegative sum byC_T h^(2−a)B_alpha(h)||z||_(E_(s−gamma))², so its tails vanish. Thusm_Nz,n_Nz converge inL2(Omega;E_s), stronglymeasurable byseparableE_s, and obey that squaredbound. Real linearity anddensity extend uniquely to bounded deterministic linear maps

 m_(R,I),n_(R,I):E_(s−gamma)^real→L2(Omega;E_s^real).

They are maps INTO random-vectorL2spaces, not an asserted common samplewise bounded operator.

For a realSchwartzw, letw_N be itsE_sorthogonalprojection. Then<m_Nz,w>_E=ell_R(I;z,w_N). Applying the OUTPUTsingleton073 bound to the normalized residual gives

 E|ell_R(I;z,w−w_N)|²
 <=C_T h^(2−a)B_alpha(h)||z||_(E_(s−gamma))²||w−w_N||_(E_s)²→0.

The zero residual needs no normalization. Takinglimits yields<mz,w>_E=ell_R(I;z,w) inL2. For the other identity projectz instead and use the INPUTsingletonbound

 E|ell_R(I;z−z_N,w)|²
 <=C_T h^(2−a)B_alpha(h)||w||_(E_(s−gamma))²||z−z_N||_(E_s)²→0.

Hence ell_R(I;z,w)=<z,nw>_E for every FIXEDrealSchwartzpair. The limits are basis-independent: pair them against a fixedcountableSchwartzbasis, use these identities andParseval; extension toE_(s−gamma) then follows from boundedinputcontinuity. No illegalE_sinnerproduct on two arbitrary roughE_(s−gamma) inputs is asserted.

Eachfinite scalarfunctional ofm_Nz,n_Nw is a finite linearcombination of evaluations of the originalW, hence centeredGaussian. L2convergence gives convergence ofvariances andcharacteristicfunctions. The same argument for finite linearcombinations of several vectorfunctionals proves jointGaussianity for every fixedfinitefamily, including afterboundedinputextension. No Gaussianindependence ofphasecolumns orH-valued realization of the originalnoise is used.

##7. Scope, constants, limits and result of the author check

Allfrequencyintegrals were measurepushforwards/Tonelli or absolutelyconvergent Schwartz pairings, not integrals against an inventedmu density. Admission/approximation constants may depend onR, whereas finalvariance C_T depends onfixedmaskshape throughL_zeta only. The role ofa+alpha<2 is explicit in the far-shelltail and the nonemptytime-exponentwindow; the strictgamma range handles the nearrow power/log. None oftheseconstants is declareduniform at excludedparameterendpoints.

ForGamma0 takeell,m,n,nu_R allzero directly; the puretemporalcompletion still exists. Originalwhite, singularnonradial andlower-dimensional spectral cases satisfy the same translatedball argument byphysicalGamma positivity andPD, with actual amplitude insideC_Gamma. Physicalatoms were not excluded by the absenceofspectralatoms. No spatial-angular density or finite totalmu/Gamma mass enters.

No concrete sourcegap was located in069/071/073/074 under the exposed CURRENT OWN covariance/time clauses. The calculations prove only the stated finite-interval forms and fixed-input L2columns. They doNOT create a common uncountable almost-sure operator version, randomHilbert–Schmidt realization, Ctheta-Schatten path, source convergence or nonlinear solutionmoment bound. Those remain separate061–093/driver/source seams; no whole214/240/13/HIGH/Kimi/visual/cold credit is claimed. No manuscript/source/Git/CLI/network/provider/privateReasoning action was taken.
