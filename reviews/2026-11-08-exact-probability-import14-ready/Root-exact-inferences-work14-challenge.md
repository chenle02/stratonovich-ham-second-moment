# Exact inference reconstructions for independent checking

Root's working derivations, not accepted theorems or independent review. These address the exact questions in diagnosis13 against the unchanged frozen candidate. The reviewer must check the derivations and actual complete sources independently. No new overall verdict/confidence is requested in the working task.

## 005: remaining-pair induction, then two-path absorption

Fix an ordered time vector 0<s1<...<s_(2j)<T and a pairing D of these labels. The invariant is: the remaining even label set R is a union of whole original pairs; its retained matching is D restricted to R; its path variables have the marginal Brownian law at exactly those times; removed steps contribute deterministic upper factors, with distinct selected right-end labels. Initially R is the full set and the deterministic product is1. The empty matching has product1.

For nonempty R, let v=max R, p be its partner, and q=max(R minus {v}). Thus p<=q<v. Conditional on all retained earlier path variables, only the pair involving v depends on B_(s_v). Brownian independent increments give

E[gamma_b(B_(s_v)-B_(s_p)) | B_(s_l), l in R minus {v}]
 = (p_(s_v-s_q)*gamma_b)(B_(s_q)-B_(s_p))
 <= A*(s_v-s_q)^(-alpha/2)
 <= A*(s_v-s_(v-1))^(-alpha/2).

The last predecessor v-1 is in the ORIGINAL time list; q<=v-1 gives the inequality in this direction. The remaining factors are nonnegative and measurable with respect to the conditioning sigma algebra, so conditional expectation and Tonelli justify multiplying the bound by them. Remove both p and v. Integrating the unused B_(s_p) leaves precisely the Brownian marginal at the new retained set; no conditional bridge law is substituted. This proves the invariant inductively. At every step the selected label is the largest of the current set and is removed, so no selected original adjacent gap is repeated. There are j steps and hence j distinct selected gaps.

For Delta_l=s_l-s_(l-1), the ordered time-simplex integral of the resulting upper product has j exponents -alpha/2 and the other j exponents0, with an additional terminal slack coordinate. The Dirichlet integral is

Gamma_E(1-alpha/2)^j * T^((2-alpha/2)*j) / Gamma_E((2-alpha/2)*j+1).

Since alpha<2, every exponent parameter is positive. Summing over at most(2j)! orders gives the printed moment bound, uniformly in b>0. Boundaries have zero time Lebesgue measure at this regularized calculation.

For the positive Laplace total mass, the wave-resolvent/heat identity changes each of the2k gaps to a Brownian gap with factor1/2. Insert the two terminal horizon integrals with factor1/4; the exponential factors combine to exp(-(a+b)/2). On fixed independent Brownian paths, enlarge each ordered chain domain to its full time cube. Every paired edge uses two distinct integration labels and every label is used once, so Tonelli factors the cube integral into S1^v1*S2^v2*A12^w. Spectral Cauchy-Schwarz gives0<=A12<=sqrt(S1*S2). For v1+v2+w=k, each exponent v_i+w/2 is in[0,k]. For any S>=0 and0<=r<=k, S^r<=(1+S)^k (including r=0). Consequently, pathwise,

S1^v1*S2^v2*A12^w <= (1+S1)^k*(1+S2)^k.

The constant is1 for EACH fixed split/pairing; there is no hidden sum over triples in the lemma's fixed-D assertion. If one sums finitely many pairings or splits later, their finite count can be retained explicitly. Independence of the two full Brownian paths separates the expectation. Expanding each(1+S)^k gives the finite majorant M_k(a)=sum_(j=0)^k binom(k,j)*C_j*a^((2-alpha/2)*j). Every integral int_0^infty exp(-a/2)*a^r da is finite for the displayed r>=0. The total mass is bounded by2^(-2k-2)*(int exp(-a/2)M_k(a)da)^2, independent of all smoothing widths. An empty chain has S=0 and horizon0; the auxiliary exponential integral still has its stated value. No time-covariance singular factor belongs in this spatial lemma.

The paired-gap formulation in diagnosis13 is false when p<q. With d1 white spatial covariance and positive smoothing b, choose original times1,1.5,2,2+delta and pairs(1,4),(2,3). Conditional on the earlier vertices the first pair has mean p_(b+delta)(B_2-B_1), which on a positive-probability neighborhood of B_2=B_1 exceeds A*(1+delta)^(-1/2) for small b,delta. The source uses the correct last-remaining-predecessor gap above.

## 033: read the printed coefficient, including its gradient units

The published Chen–Hu PDF is SHA25658b152d78cd0d54d82b991933b3eaece86e1ed2b44fe09882c14eba921e97e22, identical in the local library and pinned source repository. Root actually viewed physical page4/printed2147 and physical page37/printed2180. This is Root source inspection, not extra independent pixel credit or a model image-read claim. The whole textF126 is separately supplied to the reviewer.

Printed(1.11) defines M=sup_(||g||2=1){Q(g)^(1/2)-||grad g||2^2}. It has UNIT gradient penalty. The physical Radon energy in E:three-static-variational is the same Q by the already proved physical/spectral identity. For clarity about C23's half-gradient convention, write M_c=sup{sqrt(Q)-cE}. Under g_l(x)=l^(d/2)g(lx), sqrt(Q(g_l))=l^(chi/2)sqrt(Q(g)) and E(g_l)=l^2 E(g). Set l=c^(-2/(4-chi)). Both terms then have common factor c^(-chi/(4-chi)), and the dilation is a bijection. Thus M_c=c^(-chi/(4-chi))*M_1, in particular M_(1/2)=2^(chi/(4-chi))*M_1. This is a finiteness/normalization crosswalk, not replacement of the functional printed in(1.11).

For fixed integer p, source(5.15) concerns the ENTIRE coefficient sum B_(n,p)=sum_(l1+...+lp=2n) E product S_(lj)(g_(lj)(.,1,0)). With Q=3-chi and nu=4-chi, its coefficient-rate product is

2^(-Q) * p^nu * (2*sqrt(M_1)/nu)^nu.

The logarithm is of this full rate product. This grouping can be independently derived from the preceding unambiguous(5.13): B_(n,p) is bounded by a fixed constant times binom(n+p-1,p-1)^2 * n!*p^(nu*n)/Gamma_E(1+nu*n) * [2*(1+delta)*M_1^(nu/2)]^n. Multiplying by(n!)^Q, taking the n-th root, using the polynomial factor's root limit1 and Stirling ratio ((n!)^nu/Gamma_E(1+nu*n))^(1/n)->nu^(-nu), and then delta down to0 gives2*p^nu*M_1^(nu/2)/nu^nu. This equals the displayed(5.15) product because nu-Q=1. No disputed white-noise Corollary1.4 specialization is used.

At p=2, B_(n,2) is exactly the candidate B_n(1), including both empty-chain orientations and every self/cross pairing. Its rate is Lambda_st=2*(2*sqrt(M_st)/(4-chi))^(4-chi). No extra factorial or chain-copy factor is introduced. Source(5.1), or directly static wave/field scaling at fixed total order2n, gives B_n(t)=t^((4-chi)*n)B_n(1). The candidate's r>0 enlargement handles high n; the exact finite remaining coefficients remain a finite power sum. That asymptotic rate is never substituted as the all-time coefficient constant. C23 supplies finiteness under Dalang, not the stated p2 coefficient bound by itself.

## 042: bounded matrix functions and both Taylor recursion components

At finite mode, band and Hermite cutoffs, work on the resulting Hilbert space H. Let L_z=A0-zB and G_z=[[0,I],[-L_z,0]]=G0+zK, with K=[[0,0],[B,0]]. All operators are bounded. The norm-convergent exponential exp(hG_z) is entire in z, locally uniformly with its h derivative. Direct multiplication gives G_z^(2m)=diag((-L_z)^m,(-L_z)^m) and G_z^(2m+1)=[[0,(-L_z)^m],[(-L_z)^(m+1),0]]. Summing even and odd powers yields exactly

M_z(h)=[[C_h(L_z),G_h(L_z)],[-L_z G_h(L_z),C_h(L_z)]],
C_h(w)=sum_m(-1)^m*h^(2m)*w^m/(2m)!,
G_h(w)=sum_m(-1)^m*h^(2m+1)*w^m/(2m+1)!.

These entries are entire in the coupling. The auxiliary F_h,H_h used for CP bounds are only asserted holomorphic on the required neighborhood, not globally entire. With L_lambda=L_z+lambda^2, the SOURCE definitions F_h(L)=L_lambda^(1/2)G_h(L), H_h(L)=L*L_lambda^(-1/2)G_h(L) give the weighted blocks in their printed order:

F_h(L)L_lambda^(-1/2)A_lambda^(1/2)=G_h(L)A_lambda^(1/2),
-A_lambda^(-1/2)L_lambda^(1/2)H_h(L)=-A_lambda^(-1/2)L G_h(L),
A_lambda^(-1/2)L_lambda^(1/2)C_h(L)L_lambda^(-1/2)A_lambda^(1/2)=A_lambda^(-1/2)C_h(L)A_lambda^(1/2).

Only functions of L commute in these cancellations. No A_lambda factor is commuted across L. The weighting D_lambda=diag(I,A_lambda^(-1/2)) is fixed in z.

Writing M_z=sum_n z^n T_n and comparing coefficients in M_z'=G_zM_z gives T0(h)=exp(hG0), T_n(0)=0 for n>=1, and T_n'=G0T_n+K T_(n-1). Variation of constants therefore gives T_n(h)=int_0^h exp((h-s)G0)K T_(n-1)(s)ds. On a vacuum initial phase v, if Z_(n-1,u) is the position component, the two entries of this integral are G_(h-s)(A0)B Z_(n-1,u) and C_(h-s)(A0)B Z_(n-1,u). This is precisely BOTH components of E:phase-duhamel, including velocity forcing. The ordinary coefficient is derivative/n!, not a renormalized chaos coefficient.

Each order-n selected Dyson word has exactly n noise insertions. Every prefix has Gaussian degree at most its number of insertions, hence at most n. The projection at N=n is the identity before AND after each such insertion; no prefix reaches n+1. Free propagators preserve these degrees. This proves termwise equality by induction, and bounded Bochner time integrals preserve it. It does not identify an entire fixed-N propagator with the uncut propagator. Lowering branches remain: at order2, a single coordinate gives g^2, whose constant Hermite part is the self-contraction. Weighting by D_lambda preserves these coefficient equalities.

## 047: correct coupled tensor grouping and chronological prefix induction

Let H_A be the finite-degree Hilbert space of background colors, H_C the tensor product of retained cross-color factors, and X_rho the spatial two-component phase. Reorder factors unitarily as (H_A tensor X_rho) tensor H_C. This is an isometry because the rho-weight acts only spatially. On each fixed cross subspace Z_S, every background generator is a bounded operator on the COUPLED H_A tensor spatial phase, tensored with Id on the cross factors. Gaussian multiplication of background color i acts on H_A; its spatial multiplication and Laplacian act in the same coupled operator. The full background generator is generally not a sum of separately factorable evolutions on background and space.

The exponential power series of G_A tensor Id_C is exp(tG_A) tensor Id_C, since each power is G_A^n tensor Id_C and convergence is in operator norm. Thus every background segment preserves the fixed vacuum/first-degree choice of EACH cross factor and acts as identity on those factors. Phase-norm conversions are identities on the underlying phase coordinates and all Gaussian factors, hence have the same cross-factor invariance and the printed norm bound q_j.

Induct on the factors of the chronological word, rightmost first. Initially all cross colors are in vacuum. A background segment or phase conversion leaves the used-cross set S unchanged. At the unique insertion of a new cross color i notin S, the incoming vector lies in its vacuum tensored with R_i tensor X_rho. Independence and orthogonality of the new coordinates give squared insertion norm sigma_i^2*sum_j||A_rho^(-1/2)S_b M_(eij)S_b u||^2, bounded by sigma_i^2 R_alpha rho^(alpha-2)||u||^2. The identity is tensored with all other factors; arbitrary dependence on earlier cross colors/background is allowed. The outgoing vector has i in first degree, so the used set becomes S union{i}. No later factor reuses i as noise. This closes the prefix invariant for the entire word.

No spatial operator or insertion is commuted. Tensor invariance on the fresh factors is sufficient. The already proved segment/metric/fresh-insertion norms therefore multiply in their existing chronological order, giving M_k D_A product(c_i). Summing the exactly once-permutation simplices fills the insertion cube with total volume product |I_i^T|, then normalized vector Cauchy acts on background amplitudes. Empty cross sets and empty background sets reduce respectively to a background propagator and a free propagator with fresh insertions. Nothing requires the false factorization suggested in diagnosis13.

## 048: explicit strong mode/band convergence and fixed-word dominators

Fix positive spatial smoothing and a finite color inventory. For one color write W_epsilon(x)=sum_j g_j e_j(x), with sum_j e_j(x)^2=v_epsilon<infinity. A finite-coordinate vector F of Gaussian degree<=N depends only on coordinates j<=M. For m>=M the omitted annihilation tail vanishes. The fresh creation coordinates j>m are mutually orthogonal and independent of F, so exactly

|| (W-W_m)F ||_(L2(Omega,x))^2 = int sum_(j>m)e_j(x)^2 * E||F(x)||^2 dx.

Pointwise tail variance tends to0 and is bounded by v_epsilon, giving convergence by dominated convergence. The uniform multiplication norm between fixed degree levels is at most2*sqrt(N+1)*sqrt(v_epsilon). Approximate an arbitrary degree<=N vector by finite-coordinate vectors; the uniform bounds extend strong convergence to the whole degree space. Actual multiplication by the measurable smoothed field is a closed multiplication operator, so the closed limit agrees with that operator, not an abstract substitute.

The phase insertion (u,w)->(0,Wu) is bounded between the required degree levels in X_lambda by the preceding constant/lambda. Band projections P_b=diag(S_b,S_b) are contractions in X_lambda, tend strongly to Id, and commute with free evolution. Consequently P_b K_m P_b tends strongly to K_m; the same finite-degree bounds are uniform in m,b. A finite product of strongly convergent uniformly bounded factors converges strongly, by telescoping A_m B_m-AB=A_m(B_m-B)+(A_m-A)B on each fixed vector.

For a fixed length-n word, free phase factors contribute at most exp(lambda*T/2). The n insertions each have a bound using2*sqrt(n+1), fixed positive widths, the finite inventory amplitudes and lambda^(-1). This is a finite constant independent of mode/band cutoffs and integrable on the time simplex of volume T^n/n!. Dominated Bochner time integration gives strong L2 phase convergence of each word. A selected multicoefficient has only finitely many color words, so its convergence follows. The local Hermite cutoffs N_i=2k_i already preserve those words exactly; no global fixed-N propagator limit is asserted.

Thus the finite-cutoff uniform coefficient bound transfers to the ACTUAL fixed-word coefficient. For a pair of coefficients the inner products converge by the L2 Cauchy-Schwarz difference estimate. The separate entire majorant, uniform in mode/band at fixed smoothing and finite family, is exp(lambda*T/2)*(2*z_*sqrt(n+1)*sqrt(v_max)*T/lambda)^n/n! times ||v||_lambda; its n-th root tends to0. It identifies the full actual analytic series locally uniformly on compact amplitude sets, or equivalently permits vector Cauchy extraction of the limiting coefficients. v_max may depend on smoothing and family and is used only for identification. The uniform coefficient bound contains R_alpha^k and parameter/inventory constants, not v_max. No zero-smoothing phase limit is asserted here.

[held back: collaborators' unpublished work]

Read-only F209 sets delta0=4-alpha-beta, kappa_den=3-alpha, covariance |s-r|^(-beta)|x-y|^(-alpha), unit wave speed and data(1,0), and noise amplitude sqrt(theta). Its domain has strict Riesz alpha<d,0<beta<1,alpha+beta<3; the original Stratonovich common Riesz domain alpha+alpha0<2 lies inside it when beta=alpha0. Its kappa_den is the denominator of our TIME exponent, not our symbol kappa. The time exponent delta0/kappa_den is exactly(4-alpha-alpha0)/(3-alpha) on that intersection.

[held back: collaborators' unpublished work]

The formal beta up to1 comparison in F209 explicitly requires normalized temporal covariance(1-beta)|s-r|^(-beta)/2 to approximate a time delta. It is not substitution of beta=1 into a colored-time theorem. The d1 spatial-white endpoint alpha=d=1 is outside the strict Riesz domain alpha<d of that note; the candidate's white note explicitly retains that boundary and does not import an endpoint theorem by continuity.

[held back: collaborators' unpublished work]

## Lean scope suggested by the user's question

The existing ledger records80accepted finite facts/22local checks, not a whole-SPDE formalization. Potential additions are the remaining-pair finite invariant, selected-word degree/cutoff induction, and exact static factor-two/exponent bookkeeping. They should expose Brownian conditional expectation, operator/field analytic realizations, Stirling/source-rate input and convergence as named boundaries. This note opens no companion repository or Lean proof wave, claims no fresh compilation or package gate, and does not substitute formal arithmetic for the actual independent source/application checks above.
