# Exact operator work15: complete report read, mathematical slips corrected

Root read all29319bytes/468lines: A1–A8, B1–B8, C1–C7, external-theorem match and final boundaries. Actual same-session DeepSeek V4 Pro completed391934input/26870output-plus-reasoning, below437117input bound and311296hard reserve. No overall verdict/confidence was requested or supplied. Native public bytes are preserved losslessly; neither the report's status prose nor its mathematics is silently rewritten. Original source remains unchanged. This report is new detailed verification evidence, not an error-free certificate or HIGH receipt.

The useful detailed derivations are: bounded block-exponential even/odd powers, ordered weighted-block identities, coefficient ODE and BOTH Duhamel components; selected-word cutoff induction; coupled background/spatial evolution tensored with identity on fresh cross factors; chronological used-color induction; fresh-column bound and shared-copy Cauchy; explicit creation/annihilation tails, strong product telescoping and actual fixed-word coefficient identification; entire-majorant separation. Compare these with the actual source formulas and the following corrections before reuse.

## 1. Negative numerical-range points are allowed; no square-root branch of w is needed

A2 falsely says W(L_z) avoids the negative real axis and the auxiliary functions require a branch of sqrt(w). The candidate explicitly permits negative real w. C_h and G_h are ENTIRE power series in w, with G_h(0)=h. The source definitions are F_h(w)=sqrt(w+lambda^2)*G_h(w) and H_h(w)=w*G_h(w)/sqrt(w+lambda^2). Only sqrt(w+lambda^2) requires a branch, on a right-half-plane containing W(L)+lambda^2. Source E:complex-phase gives Re(w)>=-lambda^2/4, hence Re(w+lambda^2)>=3lambda^2/4>0. These functions are therefore holomorphic on a neighborhood of the compact closed numerical range. The scalar sin/cos expressions are removable power-series expressions, not a principal-sqrt(w) domain restriction.

Legal countercheck to the report: A0=I,B=I,d=1 satisfies the ALL-rho form bound1/(rho^2+1)<=rho^(a-2),0<a<1. Let delta=delta_a>0, choose lambda=(2/delta)^(1/(2-a)), and z=2. This lies on the allowed coupling circle. L_z=-I, so W(L_z)={-1}, while L_z+lambda^2 remains strictly positive. The report's negative-axis exclusion is false under the actual abstract hypothesis. The source's shifted-root argument remains valid and accommodates precisely the negative spectrum relevant to wave growth. Do not add L>=0 as a new hypothesis.

## 2. Ordered blocks and ordinary Taylor normalization

A3's root cancellations use only functions of L and are correct. Its parenthetical suggesting L equals A_lambda when B commutes with A0 is not correct: commutation alone does not imply equality. Neither equality nor noncommutation is assumed by the source. Retain the printed ORDERED products.

A4's phrase no1/n! means no EXTRA factorial in the coefficient recursion. Precisely T_n=(1/n!)*partial_z^n M_z|0, M_z=sum z^nT_n, and T_n=integral exp((h-s)G0)K T_(n-1)(s)ds with coefficient1. The time-simplex volume already carries the usual factorial where applicable.

At finite Gaussian degree, B is P_N(sum_j M_gj tensor S_bM_ejS_b)P_N, not uncompressed Gaussian multiplication on the full Gaussian L2 space. Apply A4 first to this actual bounded B_N. The selected-prefix degree induction in A6 permits removal of P_N for the chosen nth word, at the finite-mode/band stage. Name that coefficient Z_n^(epsilon,m,b); it becomes the full Z_n^epsilon only AFTER the stated strong band/mode limits. No fixed-N full-flow identity follows.

A5 mixes normalized and unnormalized Hermites. With normalized h2=(g^2-1)/sqrt(2), g^2=1+sqrt(2)*h2. With the unnormalized probabilists He2=g^2-1, g^2=1+He2. Both retain the constant self-contraction1; do not use the report's coefficient1 on a normalized h2. The source creation/annihilation coefficients and d_N=2sqrt(N+1)sqrt(R_alpha) use the correct normalized convention. Root's separate finite check explicitly used unnormalized He_n with inner-product weights n!, not Euclidean-normalized coordinates.

## 3. Correct tensor spaces, with each background factor appearing once

B1/B2's coupled grouping is the needed one. B3/B4 then erroneously write H_A tensor X_rho tensor Z_S while defining Z_S to ALREADY contain H_A. This duplicates the background factor. Define instead

C_S=(tensor_(i in S)G_i^(1)) tensor (tensor_(i in C minus S)G_i^(0)),
Z_S=H_A tensor C_S.

The actual phase over Z_S is Z_S tensor X_rho, canonically isometric to(H_A tensor X_rho) tensor C_S. Background Gaussian factors occur ONCE. Use retained cross factors of degree<=2 at the cutoff, or restrict to C_S, where the global cross projection is identity. On that space the background generator is ONE coupled operator on H_A tensor X_rho, tensored with Id_cross. Its norm-convergent exponential has the same tensor identity, preserving C_S. Phase conversions preserve C_S; a fresh insertion maps C_S to C_(S union{i}). This gives the source's chronological prefix invariant without separate Gaussian-versus-spatial factorization or spatial commutations.

Our earlier Root working note also used the ambiguous shorthand cross subspace Z_S. The notation C_S above removes that ambiguity. The candidate itself defines Z_S correctly and never duplicates H_A.

B3's phase-conversion norm is AT MOST q_j=max(1,rho_old/rho_new); an exact equality is unnecessary and was not established. B5's squared fresh variance has exponent alpha-2; its norm has exponent(alpha-2)/2. The fully sandwiched Fock variance/norm exponents are alpha-4 and(alpha-4)/2, respectively. The Fock form is used inside the background CP bound. It is not by itself a direct uniform occupied-color phase-insertion norm estimate on arbitrary X_rho inputs. All these operator types must remain distinct.

## 4. Critical word-versus-integrated-coefficient distinction: h enters only after integration

B7's displayed WORD bound wrongly includes product(h_i). The source E:split-word-product is

||W_A(z,t)v||_lambda <= M_k*D_A*||v||_lambda*product_(i in C)c_i.

There is NO interval-length factor in this pointwise-in-insertion-times bound. The source E:interval-cross-vector for the INTEGRATED coefficient Phi_A is

||Phi_A(z)||_lambda <= M_k*D_A*||v||_lambda*product_(i in C)(c_i*h_i),

because the permutation simplices fill the insertion cube and their volumes sum to product |I_i^T|<=product h_i. This is where h_i enters exactly once per copy. Squaring the two-copy vector bounds gives the correct cross-singleton h_i^2. No h_i^4 is introduced.

Countercheck to the report's stronger word claim: take one nonzero fresh cross insertion, no background, k=T=lambda=1, and a fixed insertion time t0 in(0,1). Shrink I_h around t0 with lengthh down to0, leaving sigma, the positive spatial smoothing, finite Gaussian mode and spatial band fixed. Choose deterministic v so the incoming position at t0 is f with S_bM_eS_b f nonzero. Such a legal choice exists for d1white covariance: take a positive test coordinate, so e=p_epsilon*psi/||psi|| is nonnegative/nonzero, and a band vector f with positive integral e|f|^2. Free evolution is invertible. The pointwise word E0(1-t0)J E0(t0)v is the SAME nonzero vector for everyh. A bound by a fixed constant timesh tends to0 and is false. The true source word bound has no h; its time integral has the one correct factorh. The inventory assumptions allow fixed sigma at sufficiently smallh, so this is not excluded by the actual model.

This is a report error in B7, not a manuscript error. The source's explicit cube and vector-Cauchy formulas preserve the distinction. The corrected tensor prefix invariant plus ordinary norm multiplication proves the proper pointwise word bound; Minkowski and cube volume prove the integrated one. Same-copy singleton ending charge remains one; initial/final phase conversions and the common partition are all retained as in the source.

## 5. Strong limits use global L2, not an assumed finite spatial region

C1's exact tail identity is correct for finite-coordinate vectors:

||(W-W_m)F||^2 = integral_Rd sum_(j>m)e_j(x)^2 * E||F(x)||^2 dx.

Its sentence integrable on the finite spatial region is unnecessary and generally false as a support assumption. Band projections do not preserve compact support. The dominator is globally integrable because F belongs to L2(Omega tensor R^d) and sum_j e_j(x)^2=v_epsilon<infinity. No finite spatial-volume hypothesis is used by the candidate. For a phase insertion F is the POSITION component; the velocity need not be unweighted L2 after the band limit.

Use actual measurable multiplication closedness on the ambient L2 product space, the uniform finite-degree bound, density only within the generated Gaussian degree subspace, and then the common-space strong band/mode product telescoping. S_b commutes with FREE evolution, not with field multiplication. Each fixed color word has a time domain SUBSET of the ordered simplex, with volume AT MOST T^n/n!.

C4's loose e^(n*lambda*T/2) free-factor bound is justified for n>=1 only after using that the actual free time gaps sum toT. The uniform correct bound for the product of free factors is e^(lambda*T/2) for ALL n, including n=0. Multiplying this by the n fixed-degree insertion bounds gives the source's integrable per-word dominator. The empty word is handled by the free bound, not by setting that exponential to1. The source entire majorant already uses the correct e^(lambda*T/2) and does not inherit this report shortcut.

Fixed finite-color coefficient sums and same-Gaussian inner products then converge by the stated strong limits and Cauchy-Schwarz. The independent entire majorant identifies the actual finite-interval model locally uniformly in amplitudes. Its v_max is smoothing/family dependent and used only for identification; the uniform R_alpha coefficient bound has no v_max. No zero-smoothing phase theorem is asserted.

## 6. Imported theorem and actual boundaries

Crouzeix–Palencia is used on bounded operators on complex Hilbert spaces, first at every mode/degree/band cutoff. C_h,G_h are entire, F_h,H_h use only the shifted-root domain established above. One may take bounded convex neighborhoods of the compact closed numerical range inside that analytic domain and pass to the numerical-range supremum; no unbounded-operator extension or positivity of L is required. The published theorem remains imported with the candidate's exact pinpoints.

The Fock/column bounds, actual field realization, fixed-positive-smoothing measurable version and finite-degree multiplication/free bounds remain supplied parent arguments with the actual hypotheses. They are not restated as conclusions assumed to prove themselves. Source L:fixed-split explicitly assumes R_alpha>0 and sigma_i>0; zero noise is handled before calling it in P:interval-coefficients. Zero interval intersections give zero selected coefficients. All branches preserve the two-component phase and shared Gaussian copies.

No candidate-source failure was located, but the report's final phrase complete as written cannot be credited literally because of the explicit errors above. Use the actual source, these full corrections and the new exact-inference evidence in the next independent WHOLE scientific judgment. No component-grade conjunction, confidence upgrade, fixed-source patch, narrowed completion or new Lean/kernel credit is made. Both prior MAINLOW, latestMAINMEDIUM and KimiMEDIUM outcomes remain unchanged. Original full215OWN/241roles/13joins/allmodels,83fresh sources after the next actual compaction, source/application/fullvisual/freshcold/adoption/build/wiki/private-delivery gates all remain open.
