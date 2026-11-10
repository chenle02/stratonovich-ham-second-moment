# Current039–048: bounded complex phase, Fock and inventory closure

Author mathematics only, science af97. This checks the actual ten CURRENT OWN deductions, reusing exact complete clauses in `reused-complete-clauses.json` and the full current proofs pinned in `source-bindings.json`. It is not a model review, ancestor acceptance, MAIN/HIGH credit, source amendment or new theorem. No Hthree, angular density, later Rayleigh/occupation/intrinsic route or source moment bound is a premise.

Use a_t=alpha0 for temporal homogeneity, a_cp=alpha/2 for the abstract complex-phase exponent. They are DIFFERENT. Original covariance is nonnegative even PD homogeneous tempered Radon Gamma, unnormalized spectral Gamma=integral exp(i xi.x)mu(dxi), d=1,2,3 with actual amplitude/white/singular/zero cases. R=R_alpha=alpha*pi*mu(B1)/(2sin(pi alpha/2)). Static039–043 do not contain the fractional temporal covariance. Original temporal windows enter046–048 through nu=3−alpha>1,beta=4−alpha−a_t>2,p=2−a_t>1,beta/nu>1. Abstract039/041 have their standalone broader Hilbert-space scopes. As written the earlier covariance-dependent static040/042/043 statements use the section's d3 setup;044 separately proves the needed dimension-free contractions for047/048.

##0. Falsification controls before proof

These are finite operator/Gaussian/inventory checks, not new homogeneous-noise SPDE models.

- A centred Gaussian g acting on its VACUUM has norm||g||2=1. On occupied h1=g, ||g h1||2=sqrt3>1. With a genuinely fresh independent g2, ||g2 h1(g1)||2=1. Thus the fresh-colour bound cannot be used on occupied background.
- g²vac=h0+sqrt2 h2. Degree cutoffN1 instead gives h0 and loses squared norm2;N2 is exact. For two colours, global total-degree1 would kill g2g1vac, while separate colour cutoffs1,1 preserve it. The selected-word statement is per-colour prefix degree, not a complete fixed-cutoff propagator identity.
- At two overlapping unit intervals, the two ordered insertion simplices each have volume1/2 and sum to1. At disjoint chronologically ordered unit intervals only one ordering survives, still volume1. An extra2! or1/2! is wrong.
- The free zero-frequency phase [[1,h],[0,1]] in X_lambda has normalized off-diagonal lambda h. Applied backward to pure velocity it has norm sqrt(1+(lambda h)²)>1. Free backward evolution is bounded by exp(lambda h/2), not contractive.
- At total energy degree2k, Gamma→bGamma forces coefficient scaling b^k. A globalR^k in addition to localR^k would give b^(2k), wrong even as a dimensional/algebraic count; for smallb it cannot uniformly dominate a positive coefficient of orderb^k. Only one covariance factor per paired degree remains below.

`counterchecks.py/json` gives exact Gaussian/2colour/factor counts and a noncommuting bounded2×2 root example satisfying the all-rho hypothesis. It does not replace the analytic proof.

##1.039: all-rho sandwich to FOUR ordered root comparisons and scalar calculus

Let A0 be BOUNDED nonnegative selfadjoint on a complex Hilbert H, B bounded selfadjoint. Put A_rho=rho²+A0 and assume EVERYrho>0 satisfies ||A_rho^−½ B A_rho^−½||≤d rho^(a_cp−2), 0<a_cp<1. Set

    I_a=integral_0^infinity t^−½(1+t)^((a_cp−3)/2)dt
       =Beta(1/2,1−a_cp/2),
    delta_a=min(1/4,pi/(8I_a)),
    |z|d≤delta_a lambda^(2−a_cp), L=A0−zB,
    L_lambda=L+lambda².

This is a RELATIVE ORDERED INVERSE-root calculation, not an absolute square-root-difference integral or an assumed unbounded square-root-domain theorem. For kappa=sqrt(lambda²+t),

    L_lambda+t=A_kappa^½(I−zK_kappa)A_kappa^½,
    K_kappa=A_kappa^−½ B A_kappa^−½,
    ||zK_kappa||≤delta_a.

The positive spectral functions of A0 commute with each other. The resolvent difference in its actual order is

 A_lambda^½[(L_lambda+t)^−1−A_kappa^−1]
  =A_lambda^½ A_kappa^−½ (I−zK_kappa)^−1 zK_kappa A_kappa^−½.

The four norms are≤1,(1−delta_a)^−1,|z|d kappa^(a_cp−2),kappa^−1. Multiplying byt^−½/pi and integrating gives

    Q=A_lambda^½ L_lambda^−½,
    ||Q−I||≤|z|d lambda^(a_cp−2)I_a/[pi(1−delta_a)]≤1/6.

The substitutiont=lambda²s gives EXACTlambda^(a_cp−2), not an extra lambda power or a divergent Beta. Bounded holomorphic calculus/its norm-convergent resolvent representation is on the strict right half-plane. Q^−1=L_lambda^½ A_lambda^−½ has norm≤6/5 and Q≤7/6. Apply the same argument toL*=A0−conjugate(z)B; the inverse-root integral commutes with taking adjoints. This gives L_lambda^−½ A_lambda^½ and its inverse A_lambda^−½ L_lambda^½, also≤2. These are the FOUR ordered factors. No A_lambda/L commutation is used.

For a unit u put s=||A0^½u||. The all-rho form bound at rho=s gives |<Bu,u>|≤2d s^a_cp; when s0 use rho↓0. The SEPARATEbound at rho=lambda gives |z<Bu,u>|≤delta_a(s²+lambda²). Thus, for w=x+iy=<Lu,u>,

    x+lambda²≥(1−delta_a)(s²+lambda²), x≥−lambda²/4,
    |y|≤2delta_a lambda^(2−a_cp)s^a_cp,
    y²≤lambda²(x+lambda²)/3.

Use lambda^(2−2a_cp)s^(2a_cp)≤s²+lambda². Squaring shows |w|≤x+2lambda², hence |Im sqrt(w)|≤lambda. The three auxiliary functions are

    C_h(w)=cos(h sqrtw),
    F_h(w)=sqrt(w+lambda²)sin(h sqrtw)/sqrtw,
    H_h(w)=w sin(h sqrtw)/[sqrt(w+lambda²)sqrtw].

Cos and sin/sqrt are entire; their0 values are removable. The only needed principal branch is w+lambda², with real part≥3lambda²/4 on closed numerical range, so all three are holomorphic on a neighbourhood. Scalar estimates are e^(lambda h),2(1+lambda h)e^(lambda h),2e^(lambda h). For F split |w|≤lambda²/2 versus>lambda²/2; use the integral identitysin(h sqrtw)/sqrtw=integral_0^h cos(r sqrtw)dr in the small region. For H use |w|/|w+lambda²|≤1+(1−delta_a)^−1≤7/3.

The EXACTexternal input is Crouzeix–Palencia authorpreprintv1(3),p1/Theorem6,pp5–6, for BOUNDED operators on a complex Hilbert space and functions holomorphic near the closed numerical range, constant1+sqrt2<3. All8 provided pages were read. No journal-version equivalence, finite spatial dimension or optional unbounded extension is imported. It gives function norms3e,6(1+lambda h)e,6e. Under(u,v)→(u,A_lambda^−½v), the phase blocks are, IN ORDER,

    C_h(L),
    F_h(L)L_lambda^−½ A_lambda^½,
    −A_lambda^−½ L_lambda^½ H_h(L),
    A_lambda^−½ L_lambda^½ C_h(L)L_lambda^−½ A_lambda^½.

Only functions of L commute. Their norms sum to(39+12lambda h)e^(lambda h)≤100e^(2lambda h). The actual phase is the entire exponential of the BOUNDED block generator; the auxiliary roots estimate it, not define a branch-dependent solution. Full source0395066–5228 supplies the scalar bounds/details; exact existing support§1.2 is reused.

##2.040/044: actual Fock sandwiches, BOTH variances and general dimensions

The only spatial input needed is the translated resolvent bound

    sup_eta integral mu(dxi)/(rho²+|eta+xi|²)≤R rho^(alpha−2).

It follows from physical Gamma≥0, evenness, Gaussian Fourier pairing and the radial ball law; no angular density, finite original mu-total or Hthree. Source037 proves the static input;044 rederives it for every original dimension, so no d3 trace assertion is passed to d1/d2.

At fixedepsilon>0 take real e_i(x)=E[W_epsilon(x)g_i], sum_i e_i(x)²=v_epsilon<infinity. Let H_i=A_rho^−½ M_ei A_rho^−½. They are bounded SELFADJOINT. The correct covariance identity is

 sum_i||H_i f||²
 =(2pi)^−d integral |fhat(eta)|²/(rho²+|eta|²)
          [integral e^(−epsilon|xi|²)mu(dxi)/(rho²+|eta+xi|²)]deta
 ≤R rho^(alpha−4)||f||².

The INPUT half-weight A_rho^−½ is essential; dropping it produces a false LHS. Row and column sums agree because H_i are selfadjoint. Finite mode subsums preserve the positive bound. For Fourier projection S_b, (S_bH_iS_b)²≤S_bH_i²S_b; this uses a positive missing term, not commutation of H_i/S_b. A_rho itself commutes withS_b.

On Gaussian degreej, the CREATION ROW(v_i)→sum a_i* v_i has norm sqrt(j+1), because its product with its adjoint is sum a_i*a_i=(j+1)I on degreej+1. Compose with the deterministic spatial column(H_i) and use distinct output degrees' orthogonality. The annihilation part is the adjoint AFTERcutoff; both parts remain. On Hermite degree≤N this gives

    ||A_rho^−½ B_N,m,b A_rho^−½||
      ≤d_N rho^(alpha/2−2), d_N=2sqrt(N+1)sqrtR.

This is a bounded selfadjoint Fock/spatial compression; A0=−Delta is bounded on S_b even though its band Hilbert space is infinite-dimensional. CP applies here, NOT to the eventual unbounded sample multiplication operator. Unweighted finite-degree multiplication also has norm≤2sqrt(N+1)sqrt(v_epsilon); v_epsilon is allowed ONLY for fixed-width existence/cutoff identification.

The unsandwiched column bound is sum_i||A_rho^−½(e_i f)||²≤R rho^(alpha−2)||f||². A NEW independent colour on its vacuum therefore has insertion norm sigma_i sqrtR rho^((alpha−2)/2), tensored with ANYother Hilbert factor. Occupied colour must instead use its Fock bound. Full exactA1–A4 clauses and source040/044 are reused; this is not a one-variance shortcut or pointwise order of compressed covariances.

##3.041/042/043: selected words, static orders and the actual local inputs

After any selected word prefix, colouri's degree≤its insertion count so far. Free/spatial deterministic factors do not alter Gaussian degree. N_i≥theTOTALselected occurrences makes P act identically before/after every insertion. Lowering/self-contractions are retained. This proves equality of selected vectors, finite sums and existing Bochner word integrals. It does NOT identify a complete fixed-cutoff propagator with the uncut full flow.

For static042 ordern, chooseN=n. Apply039/040 Cauchy VECTOR coefficient extraction on a COMPLEXcircle, then lambda=n/h. Output comparison costs n, input contracts, d_n≤2sqrt(2n)sqrtR. The coefficient is bounded by

    100n(2sqrt2 e²/delta_(alpha/2))^n
       R^(n/2)h^((4−alpha)n/2)n^(−(3−alpha)n/2)||v||_(1/h).

Use100n≤200^n and n!≤n^n; A_alpha=400sqrt2 e²/delta_(alpha/2) is alpha-only. The static norm factorial exponent is nu/2; energy/043 uses nu, notnu/2. At fixedepsilon, remove band then modes on EACHfinite degree/word using strong convergence and the uniform finite-degree multiplication bound. For an omitted Gaussian mode acting on a finite-coordinate vector, annihilation is0; creation tail tends to0 by sum_tail e_i(x)²≤v_epsilon and dominated spatial integration. Density extends it. The locally entire v_epsilon-dependent majorant constructs the full actual series separately; no zero-smoothing phase limit is claimed.

The elementary sumS_b(x)=sum x^n/(n!)^b≤2exp(3x^(1/b)) for b=nu/2 in(1/2,3/2) uses l^b/l1 whenb≥1. Forb<1 apply Holder to((2x^(1/b))^n/n!)^b times2^(−bn); the geometric companion is≤2 becauseb/(1−b)>1. This preserves the Holder POWERSb and1−b. It gives the source042 full static sum, not an interval-overlap representation.

043 retains the complete general-lambda FIRSTenergy coefficient: Born term AND2Re<Z0,EZ2>. It consumes source038's general-lambda bounds and the free-energy ABSOLUTEderivative estimate valid forward/backward, not only lambda h=1 or a false free contraction. Hence ||S0(−h)||lambda≤sqrt(e) forlambda h≤1. For Yn=S0(−h)Zn,

 ||Yn||L2Xlambda≤sqrt(e)/(lambda h)
      (A_alpha sqrtR)^n h^((4−alpha)n/2)/(n!)^(nu/2)||v||lambda.

Parity removes oddtotalr+s. Forr+s=2k, r!s!≥(k!)², including empty factors, gives e(2k+1)(A_alpha²R)^k h^((4−alpha)k)/[(lambda h)²(k!)^nu]. For k≥2 absorb e(2k+1)≤(3e)^k; keep the sharper Born+mean separately. Thus B_alpha=3eA_alpha² is alpha-only. Dyadich_j=2^(−j)/lambda,sigma_j²=h_j^(−a_t) yields, afterT/h_j, powersh_j^(1−a_t),h_j^(2−alpha−a_t),h_j^(2beta−3), allPOSITIVE. The independent NEXT-field block extension is a Hilbert tensor argument, not arbitrary dependence/reuse. Summing errors across dyadic levels is NOT a product/evolution for overlapping fields. The finite interval chain below uses044/045/041/046/047 instead, not043's independent partition.

##4.045: complex SUM and every ending metric charge

For bounded V, not necessarily selfadjoint, assume ||A_rho^−½ V A_rho^−½||≤D rho^(a_cp−2) for EVERYrho>0 and D≤delta_a Lambda^(2−a_cp). V* has the same bound. Repeat the ORDERED inverse-root calculation withK_kappa=A_kappa^−½ V A_kappa^−½. Q,Q^−1 and the V* adjoint pair give all four comparisons≤2; the numerical-range form estimates at rho=Lambda andrho=s give the same parabola. No selfadjointness or commutation of V/A0 is needed. This separately proves the complex-SUM use; it is not a silent application of039's selfadjoint-B statement to V.

For backgroundcomplexamplitudes |z_i|=varrho_i, omega_i=k_i/h_i,d_i=2sqrt(2k_i+1)sqrtR, choose

    varrho_i=delta_a omega_i^(2−a_cp)/(sigma_i d_i).

On one copy, backgroundA consists onlyofused noncrosscolours. D(t)=sum_A |zi|sigma_i d_i 1_Ii ≤delta_a sum omega_i^(2−a_cp)≤delta_a Lambda(t)^(2−a_cp), Lambda=lambda+sum_Aomega_i1_Ii. These are deterministic norm estimates on the JOINT Gaussian Hilbert space; input may already depend on background fields.

Norm conversion fromoldrho tonewrho costsmax(1,rho_old/rho_new). At a cut withendingE,startingS,remainingR,

    ratio≤[lambda+sum_Romega+sum_Eomega]/[lambda+sum_Romega+sum_Somega]
          ≤1+sum_Eomega/lambda≤product_E(1+omega_i/lambda).

An initial increase costs1; insertion-only cuts do not changeheight. Count final return toX_lambda asendingatT. Every CONNECTED interval ends once, so productconversion≤D_A=product_A(1+k_i/(lambda h_i)). No second copy ofD_A appears at insertion or start. Disconnected support of a reused colour would need additional ending charges and is NOT asserted by this count.

##5.047: occupied background, fresh cross and one-copy versus two-copy

Fixr_i+q_i=2k_i,sum k_i=k≥1,lambda=k/T,N_i=2k_i. Colourreflection removes oddtotals, but the two vectors in the energy use the SAME Gaussianfields. SetC={k_i1,r_i=q_i1}; B=remainingactivecolours. Cross colours are fresh ON EACHcopy; singleton(2,0)/(0,2) belongsB, so a vacuum estimate must not be applied to it.

After choosing allcrossinsertiontimes andbackgroundendpoints, there are≤3k+1 segments. The backgroundCPweights satisfy

    integral_0^T Lambda(t)dt=lambda T+sum_Aomega_i |I_i∩[0,T]|
                              ≤k+sum_Ak_i≤2k.

Thus ONEcopy segment-product costs M_k=100^(3k+1)e^(4k). Refining by insertiontimes does not repeat the integral. Only AFTER vector estimates and Cauchy–Schwarz between the two same-field vectors is M_k SQUARED: M_k²=100^(6k+2)e^(8k)≤(100^8e^8)^k. The earlier two-copy-e4k caption is false; source/complete reuse correctly uses onecopye4k/twocopye8k.

The precise fresh-colour argument uses tensor spacesZ_S: usedcrosscoloursS are in firstdegree, unusedC\S in vacuum, backgroundcolours in their retainedlevels. Backgroundsegments/spatialfree factors preserve these spaces because they neveract oncrossGaussianfactors. At owninsertioni∉S the input is1_i tensor(u,w), witharbitrary dependence onothercolours. Gaussian orthogonality and the unsandwiched column inequality tensored withthat otherHilbertspace give

    ||J_i||≤sigma_i sqrtR Lambda(t_i)^((alpha−2)/2)
             ≤sigma_i sqrtR lambda^((alpha−2)/2)=c_i.

N_i2 preservesvacuum→firstdegree. Each crosscolour is inserted exactlyonce, so it is fresh whenused; no occupied annihilation is assigned this bound. The current vector can depend onbackground andpreviouscrosscolours. No conditional independence of successive TIMEcells is invoked.

The Dyson coefficient linear in EVERYcrossamplitude is the sum over permutation simplices of product_i(I_i∩[0,T]). They partitionthefullcube up tonulldiagonals; totalvolume≤product h_i. There is no m! or1/m!. Boundeach chronologicalword with allsegment/identity/insertionfactors inactualorder to obtain ||Phi_A(z)||lambda≤M_k D_A ||v||lambda product_C(c_i h_i). Normalized angular VECTORCauchy extraction costs product_Avarrho_i^(−r_i) on onecopy and productvarrho_i^(−q_i) on theother. Never apply a holomorphic formula to a squared norm.

Output X_lambda→X_(1/T) costs k on each vector; input X_lambda norm contracts. The actual preabsorption bound is

 k²M_k² D_Ar D_Aq ||v||_(1/T)²
       product_B varrho_i^(−2k_i)
       product_C(R sigma_i² h_i² lambda^(alpha−2)).

ForB, d_i²≤12k_iR andk_i!≤k_i^k_i give

 varrho_i^(−2k_i)≤(12delta_a^−2)^k_i
       (R sigma_i² h_i^(4−alpha))^k_i/(k_i!)^nu.

D_Ar D_Aq=product_B(1+k_i/(lambda h_i))^ell_i,ell_i=1_(r_i>0)+1_(q_i>0). A singletonmean has EXACTLYONEcharge; highercolour atmosttwo. Since |C|+sum_Bk_i=k, the product contains R^k ONCE. Equivalently source047 factorsR^k outside and leavesNO R inlocalweights. Mixing these conventions doubles covariance dependence. The explicit sourceC_split=100^8e^8 max(1,12delta_a^−2) is alpha-only. Original sorted labels are retained; no inventory-size/permutation/Gaussianmode factor is hidden.

##6.046/048: all coefficient allocations and factorialnu

At fixedsmoothing/inventory the actual finite-model vector series is entire by

    exp(lambda T/2)[2z_*sqrt(n+1)sqrt(v_max)T/lambda]^n/n! ||v||lambda,

on max_i|z_i|≤z_*. Complexcoefficients have bothcreation/annihilation norms bounded bytheirl2 coefficientnorm; no extra#colours entersv_max=sup_t sum sigma_i²1_Ii Gamma_epsilon(0). This majorant is nonuniforminsmoothing/inventory, usedONLYidentification. VectorCauchy at twice thepolydisc gives sum z_*^|r| ||U_rv||≤2^|F|K; its finitefactor establishesabsoluteenergyseries, nottheuniformcoefficientconstant.

Forrealcommoncouplings, [s^(2k)]energy=sum_(|r|+|q|2k)<U_rv,U_qv>. Colourreflection forcesr_i+q_i=2k_i; atmostkactivecolours, andproduct_i(2k_i+1)≤3^k split choices. LocalHermiteN_i=2k_i preservesbothselectedvectors by041, despite fullbackgroundpropagators atthatcutoff notbeing theuncutflow. Ordinarycoefficients containnofactorialnormalization. Allword-order counts are alreadyinsideU_r.

After sigma_i²≤c h_i^(−a_t), localweights apartfromcommonconstants are

 mean singleton: R h_i^beta(1+1/(lambda h_i)),
 cross singleton: R lambda^(alpha−2)h_i^p,
 higherl≥2: R^l h_i^(beta l)(1+l/(lambda h_i))²/(l!)^nu.

Substituteh_i≤LT/i onlyintheWHOLEweight. Expandedpowersbeta l,beta l−1,beta l−2 arepositive;meanpowersbeta,beta−1 andcrosspowerp arepositive. L may be enlarged tomax(1,L). Withlambda=k/T, extractC^k R^k T^(beta k), leaving

    v_i=i^−beta+k^−1 i^−(beta−1)+k^(alpha−2)i^−p,
    b_i,l=i^(−beta l)(1+li/k)²/(l!)^nu.

In particular crossT-power is(2−alpha)+p=beta. Positive ordinary product multiplication counts allocations sumk_i=k exactlyONCE:

    sum_(sum k_i=k) product_i w_i,ki
       =[z^k]product_i sum_(l≥0)w_i,l z^l.

There is NOnew multinomial. Combining two singleton alternatives in v_i bounds every one ofits3splits; the alreadycounted3^k is charged once, notagain inallocations. k²≤4^k andsigma c^k/L powers are absorbed asallowedconstants.

For completeness the positiveinventory estimate is an actualsum, notan appeal touniformity. Evaluateat z=theta k^nu,theta1/4. PutP_i=theta k^nu i^−beta,Q_i=theta k i^−p (because nu+alpha−2=1). Separate(1+Q_i). Itslogsum≤(theta k)^(1/p)J_p≤Ck,J_p=integral log(1+x^−p)dx=pi/sin(pi/p),p>1. Fori≤k remainingfactor≤S_nu(4P_i),S_nu(x)≤exp(nu x^(1/nu)), soitslogsum≤nu k zeta(beta/nu) sincebeta/nu>1. Fori>k,P_i≤1/4; singletonsum≤C k^a_t andhigher sum≤C k^(2a_t−1)≤Ck. The explicit inequality sum_(l≥2)P^l(1+ly)²/(l!)^nu≤16P²(1+y²) followsfromgeometric sums4/3 and212/27. Thus product≤exp(D_inv k), coefficient≤theta^−k k^(-nu k)e^(D_inv k)≤C_inv^k/(k!)^nu. The exact finiteD_inv/C_inv formulas are REUSED fromcomplete§1.4(A12); theydependonlyalpha,a_t, notinventorysize.

This gives source048 |energycoefficient2k|≤C(alpha,a_t,L,c)^k R^k T^(beta k)/(k!)^nu. Phaseenergy coefficients are not assumednonnegative; thisisabsolute-majorant counting. Removeband/modes atfixedpositiveepsilon/family/selecteddegree bystrongfinite-degree multiplication andchronologicaldomination, thenidentifytheactualentirevectorseries usingthe separatev_maxmajorant. Finitemode/band covariances maychangephysicalsign, so do NOTusepositive-Wickcomparison herebeforethosecutoffsareremoved. No zero-smoothing orcanonicalnoise limit isasserted in039–048.

At orderzero freeenergy≤e||v||_(1/T)². WithY=exp(nu(CRT^beta)^(1/nu))≥1,absolute summation gives(e+Y−1)≤eY. Thisis thefiniteintervalphase estimate. The laterpositiveposition comparison049–051, enlarged-amplitude tail and canonical limit are separate CURRENTproofs, notpremises of this chain. No Rayleigh/mean route, Chenconstant, actualp1 or Hthree enters.

##7. Cases, constants, reuse and gap status

Gamma0 meansR0/mu0; allpositiveorders vanish DIRECTLYbeforedividingbyd_N orvarrho_i. Negative real sigma may be absorbed into the signof itsindependentrealcolour;sigma0isomitted. Intervalswithzerointersectionlength contribute0whenitsamplitudehaspositivepower. Sourceformulas using1/h or1/(lambda h) applyh>0; at h0 takeactualidentity/zerohighercoefficientsdirectly, not0^−1times0. At T0 useidentitydirectly; source047lambda=k/TassumesT>0,k≥1. At k0 usefreeenergy, notdegreeoptimization. Longintervalshi>Tareallowed via|I_i∩[0,T]|≤h_i; neverboundinverse-lengthfactorsseparately. Statica_t0 orendpointwindows are notobtainedbyGamma_E(0)substitutionoruniformparameterconstants.

R scaleslinearlywithcovarianceamplitude; vectororder n scalesasb^(n/2) andenergy2k asb^k. d_N has sqrtR; A_alpha/B_alpha arealpha-only, while043'sfirstcoefficient also containsactualD_Gamma fromthe3dtrace input. v_epsilon/v_max and2^|F|K controlonlyfixed-widthidentification andneverenter theuniform C_split/C_inv orcoefficientconstant. C_split isalpha-only; C_inv alpha/a_t-only; finalfinite-inventory C alsoallowsL,c. Fixedbackgroundintegral andpartition counts dependonTOTALdegree, notsizeofthefullinventory.

The exact existingcompleteclausesA1–A15/B1 areincludedwithhash/LF sourcepins inreused-complete-clauses.json. Full current039–048source isreadandbound, includingdetailedtensor/cube/metricword construction. Thisreconstructionmakes thecriticalomission-pronesteps explicit withoutrewriting unrelatedsource/canonical arguments orusing anyoldgrade. No actualgapwasidentifiedinthetenassigneddeductionsunder theexposedinputcontracts. That isauthorworkingonly; allownparentsremainCURRENTnotexternalaxioms andno MAIN/HIGH/sourcevisual/cold/project gate iscleared.
