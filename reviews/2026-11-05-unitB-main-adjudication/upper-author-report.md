# Author adjudication of B's energy/terminal/tail/independent-upper working

I read the ENTIRE actual public report:27557B/SHA019633b4c3789ff65c0f0797fb2295358593d583a830a7f5c39e92fbc9348743,228 logical lines,227LF and no terminalLF. I checked WORK036/049/050/051 and their joined applications against actual af97 source, the frozen full upper working407bbd41… and its precise prerequisite/countercheck/route records. This is author mathematical/source adjudication, not an independent review, source repair, confidence conversion or acceptance. No private reasoning, new model call, source/Git/runtime/configuration edit or supplemental-call proposal is involved.

**Concrete result:** public WORK051 contains a false finite-J covariance inequality. The manuscript and held full working use the correct infinite numerical majorant followed by positive finite-order monotone convergence, so this counterexample does not refute their upper proof. The other assigned source calculations match their stated hypotheses. The report also has explicit reconstruction-boundary ambiguities that must stay visible rather than being cleared from the availability of source text.

## 1. False finite-J inequality, with an original-model counterexample

Native logical line101/§2.6 WORK051 says

 gamma_delta^0 Gamma_epsilon <= K_J Gamma_epsilon <= K_infinity Gamma_epsilon

at fixed widths/finite order. The first comparison is FALSE for an arbitrary finite J. K_J<=K_infinity is correct. Nothing in source051 asserts the first comparison.

Take the admissible original model d=1,alpha=1,Gamma=delta0,a=1/2,T=1, with any positive spatial heat width. Choose H0=6,J=0,s=1/4,r=1/4+1/100 and delta=1/100. All three coarsest grid cells containing the times are(0,6),(-4,2),(-2,4), away from their boundaries. Each has variance weight6^(1/2)*6^(−1/2)=1, hence K0(s,r)=3. But

 gamma_delta^0(1/100)
 =1/sqrt(pi) * integral_0^100 exp(−q/100) q^(−1/2)dq
 >=20/(e*sqrt(pi)) >10/3 >3.

The last strict bound uses e<3,sqrt(pi)<2. The spatial heat covariance at zero is positive, so multiplication by Gamma_epsilon(0) preserves the failure. Continuity and the fact that K0 is constant inside these cells make this an open-neighborhood failure, not an irrelevant diagonal or grid-endpoint value. This falsifies the quoted pointwise premise; I do NOT infer that some full finite-partial moment must violate the eventual uniform upper bound.

More generally, for each fixed finite J,

 K_J(s,r)<=3(6/H0)^a sum_(j=0)^J 2^(ja)<infinity,
 gamma_delta^0(tau)>=exp(−1)delta^(−a)/(a Gamma_E(a)) if0<tau<=delta.

Small positive delta defeats universal domination by that fixed J. This does not claim that no specially selected J(delta) could ever dominate a given regularization. Such a selection is neither proved nor needed by source051.

The exact source replacement is at main LF6705–6744: gamma_delta^0(tau)<=|tau|^(−a)<=K_infinity(s,r) off the diagonal; K_J increases to K_infinity. At FIXED partial order N, every terminal-chain pairing has positive Green measures, nonnegative covariance factors and coefficient1. Nonnegative Tonelli/MCT therefore gives

 E|U_N^(epsilon,delta)|²
 <=lim_(J→infinity) E|V_(N,J)^epsilon|²
 <=sup_J E|u_(J,epsilon)|² <=B(T).

Only then does049 send N→infinity at fixed positive widths. No infinite-depth Gaussian field is constructed. The frozen upper working LF226–233 and243–250 prints precisely this chain, not domination by each K_J. Native§4.1's prelimit-chain summary is compatible with the correct source route, but does not erase the explicit false premise in WORK051. Keep both pieces of the actual public record unchanged.

## 2. Actual036: correct seed, two Cauchy steps and singular-measure extension

Native logical line67/WORK036 matches the actual standalone R3 claim at source LF4644–4768. C23 Theorem1.1 closing finiteness for QUARTIC(1.5), under the homogeneous Dalang condition chi<2, is used only on real unit-L2 Schwartz profiles. It is distinct from square-root(1.4) used by static027/033. The printed Q(f)<=0.5||grad f||²+C0 is read at the native paragraph's stated unit-profile normalization. For a general f the source explicitly rescales to

 Q(f)<=0.5||f||2²||grad f||2²+C0||f||2^4.

The two calculations have different roles: spectral Cauchy bounds the mixed square-product P(f,h), while physical Cauchy on dy Xi(dz) bounds the quadratic product energy E(fh), not the quartic Q(fh). They give the actual Lipschitz-to-H1 estimates for A_f(y,z)=f(y+z)f(y) and B_f=hat(f²). Sigma-finite Fubini with Lebesgue y FIRST identifies A_g and representative independence even for singular Xi; no Lebesgue-null=>Xi-null inference is used. L1 convergence of squares gives uniform Fourier convergence, identifying the singular-mu strong L2 limit with hat(g²). The source passes equality and the quartic inequality to H1 correctly.

The native paragraph is a condensed account: it names the strong L2 estimates instead of printing their full inequalities. The complete source/author working supplies and permits author checking of those inequalities; that availability is not an invented longer native deduction or a new review grade. No assigned source gap was located. Its Xi-dependent C0 is an energy-identification constant; it is not inserted as the parameter-only constant financing051. No temporal Hhomog restriction, rough-potential theorem, Teschl or later Rayleigh route is a prerequisite of036.

## 3. Actual049/050 and the cutoff/limit order in051

WORK049(native line97) accurately identifies the finite Gaussian product argument, exact mass T^(2n)/(2n)!, coefficient1 from labelled MGF differentiation, self/unequal/empty chains, symmetrization without extra factorial, and Green-first convention. At n=0 the empty term is1; n=1 mass is T²/2 and n=2 mass T⁴/24. The successive term majorant ratio is |r|sqrt(V)T²/((2n+2)sqrt(2n+1)), tending to0. Thus fixed-positive-width entire L2 convergence is valid, but it gives no width-uniform Br. The public record explicitly preserves that last distinction. Entrywise positivity comparison applies to nonnegative covariance/positive position kernels, not arbitrary Gaussian covariance PSD order or arbitrary phase data.

WORK050(native line99) correctly states a conditional lemma. The enlarged-noise-amplitude second moment at r>1 contains r^(2n)E|Y_n|² as a nonnegative mixed-series term; it gives sqrt(Br)r^(−n) and a geometric norm tail. Canonical full-series convergence is then a conclusion after actual fixed-n L2 source convergence, not an assumption. At r=2, covariance and R_alpha become4Gamma and4R_alpha; the tail after N is sqrt(B(T;2))*2^(−N). The final moment bound is passed from B(T;1), not the larger tail bound.

Apart from the finite-J sentence above, the source route and native ingredients respect these distinctions:

*044–048 prove the actual finite interval/Fock bounds. Mode/band limits identify actual ordinary finite-family coefficients before positivity/locality is invoked. A width/family-dependent v_max entire majorant is for identification only, not the uniform moment constant. The Hermite cutoff preserves each selected word, rather than supplying a full-flow cutoff theorem.
*The three nested shifted grids give L=78,c=6^a and K_infinity as a NUMERIC positive majorant. K_J is not stationary in time; source LF6695 expressly compares its actual TERMINAL kernels before any time reversal. No colored fields are asserted to converge to the original noise. The report does not otherwise claim such a field convergence, but its shorthand must be read with this exact source restriction.
*Flat data(f_T,0) agree causally with(1,0) on B1 at the terminal time. The position estimate uses ||f_T||2²<=|B_(T+2)| and spatial stationarity of the unmasked finite interval field; division by|B1| yields e(T+2)^d. No derivative or F-lift norm enters the estimate. Both phase entries were carried by the preceding finite phase estimates; the final observable here is position.
*Fix positive original noise widths and finite N; remove the source Green width FIRST, including d3. Gaussian product integrability, tested Fubini/Bochner duality and mixed Green moments identify the actual source terms. At this finite N take J→infinity only in positive Wick integrals; then at fixed noise widths send N→infinity by049. Use actual006 at each fixed n and050's width-uniform B(T;2) tail to remove source widths and the order cutoff. Pass B(T;1), and only thereafter send T→infinity.

Noise amplitude b replaces Gamma and R_alpha by b²Gamma and b²R_alpha, leaving alpha,a and all parameter-only constants unchanged. The final bound is C(alpha,a)R_alpha^[1/(3−alpha)]T^kappa with prefactor e(T+2)^d. There is no extra copy of the covariance amplitude and no actual sharp-C2 identification from this nonsharp upper. Gamma0 gives u=1 directly. The source argument remains for every original d1/2/3 model, including white and singular spectra;036's R3 auxiliary identity is not imposed as a restriction on044's independent all-dimensional contractions.

## 4. Native statuses, imports and genuine outside-OWN conditions

The actual header(native line7) says HIGH for internally valid B mathematics under stated inputs and MEDIUM for unconditional acceptance. It explicitly says the narrowed A clauses are assumed rather than rederived. WORK036/049/050/051 are literally CHECKED (050 conditional); no literal LIMITED row should be invented. Equally, internal HIGH cannot silently become unconditional or whole HIGH.

There are three necessary qualifications to the returned reasons:

1. **Named imports are allowed imports.** Failure to reprove author Theorem3.1, bounded CP, or C23 is not by itself unresolved OWN mathematical work. The obligations are exact edition/hypotheses/source fidelity and the owned application, including004/214/005/006 where used. Preserve the reviewer's actual confidence even when its explanation treats held source proofs as a reason for caution; do not reinterpret that explanation as a requirement to reprove the books or automatically increase its confidence.
2. **Outside current OWN is different.** Lines7 and223 say those A clauses are assumed valid, while line223 also says a checked narrow subclause is what was verified. This is an unresolved ambiguity of native reconstruction depth, not a source counterexample. In particular line211 calls006's own Theorem3.1 induction a named extern. The UNIVERSAL source theorem is external; the exact mixed-width/independent-origin/Green-first application producing OWN006 is owned mathematics. The supplied006 text/author capsule and matched endpoint signatures cannot supply missing native working or grant full-parent acceptance. Carry the real fixed-order clause as a condition wherever the public record actually leaves it assumed.
3. **009 is genuinely parallel.** WORK051(line101) and the upper join(line198) correctly name009 as a parallel mild-designation premise. The outside-A table/remaining-condition list omits009, so that list is not a complete dependency ledger for the PHYSICAL wording of source051. This is not a denial of009 in the report. Source LF6780–6787 explicitly distinguishes its actual multiplication/onefold Green/product construction, using006/008, from the numerical-rate estimate. Any adoption of the physical theorem must carry that actual application condition;009 is not downstream of051 and does not finance Br. No unsmoothed-solution uniqueness is claimed.

Finally native S064 coverage(line184) says Hhomog is consumed by EVERY B body. That is a scope overstatement:036 is standalone R3,039/045 are abstract bounded phase statements and046 is an inventory lemma, with their actual hypotheses. Native§5.4 itself recognizes the standalone static block. Similarly the introductory a=alpha0 convention does not turn the abstract root exponent a=alpha/2 in039/042 into temporal alpha0. These are report parameter/role qualifications, not manuscript gaps or permission to narrow standalone claims.

## Outcome boundary

One concrete false covariance premise in the public upper working is established analytically. The source and frozen upper working use the valid alternative already written, and no manuscript repair was located for036/049/050/051 under the exposed actual prerequisites. Actual native outside-OWN assumption/depth limitations and the physical009 condition remain separate from that source assessment. The false sentence, conditional HIGH/internal versus MEDIUM/unconditional wording and all original statuses remain immutable. No source availability, author verification or this batch creates additional native mathematical credit, changes confidence, closes a lineage or clears the full original-model/C2/214/240/13, Kimi, source-image, cold or delivery gates. Root alone adjudicates the actual bounded result; no further call is proposed.
