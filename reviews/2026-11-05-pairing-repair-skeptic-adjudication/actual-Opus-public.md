# Actual Opus primary-skeptic report

Verdict: PASS_WITH_NOTES. Confidence: medium. Driver accepted: false at the unchanged HIGH threshold.

This is a faithful readable rendering of the public JSON. Raw and parsed originals remain preserved.

## R01 Exact normalized hypotheses and the norm convention

Verdict: PASS_WITH_NOTES.

Candidate §0 (LF7-30) assumes, for each edge e: a finite positive mu_e with gamma_e(x)=∫e^{iξx}mu_e(dξ)>=0. Since gamma_e is real, mu_e is symmetric and gamma_e is even, bounded, continuous and positive definite. The Laplace domain A_e⊂(0,∞) is measurable, nu_e=1_{A_e}λ^{a-1}dλ/Γ_E(a), and kappa_e=∫e^{-λ|t|}nu_e. With A_e=(0,∞) this gives exactly |t|^{-a}, matching source (3.2) with α0=a and OWN004 E:damped-norm-definitions. Kernels are nonnegative and L1 on (0,∞)×R^d, and every cross-label N0, N1_e and N2_e is assumed finite, matching the p14 hypothesis 'all ‖G_l‖^{(0)},‖G_l‖^{(1)}_{j,k},‖G_l‖^{(2)}_{j,k}<∞'. I checked the p14 image: the inner absolute bars in (3.4) are printed, and (3.5) literally prints G(s,x)G(t,x) with dy. The candidate states its theorem for the independent-variable form G(s,x)G(t,y). That is the form p20 and OWN214/OWN004 use, and it is a positive semidefinite quadratic form. The candidate says explicitly that the literal repeated-x print is not certified (LF3, LF18). The literal print is a source typo. Under it the y-integral merely multiplies by ∫gamma, which diverges for constant gamma (independent-fusion-controls LF172-177). The candidate never feeds an infinite original mu to the theorem: §8 applies heat-weighted finite mu_e first. Note: the theorem is proved for the declared y-norm, which is a qualification of literal (3.5), not of the intended source norm.

## R02 Endpoint extraction with predecessor phase, cap finiteness, coefficient 1 and adjacent mass

Verdict: PASS.

Candidate §3 (LF105-116). Let v be a chain endpoint with predecessor p (or the root) and partner a. On a region R with s_a<=s_p<s_v we have |s_v−s_a|>=|s_v−s_p|. Since kappa is a positive mixture of e^{-λ|r|}, it is nonincreasing in |r|, so kappa(s_v−s_a)<=kappa(s_v−s_p) pointwise. Before this replacement, R's indicator must not involve s_v or x_v. Because v is terminal, no other kernel or covariance involves (s_v,x_v), and the only constraint is s_v>s_p. Put u=s_v−s_p and z=x_v−x_p. At a finite cap nu_e(A∩(0,L]) is finite: near 0, ∫_0 λ^{a-1}<∞ because a>0. mu_e is finite and G_v is L1, so Fubini gives ∫G_v(u,z)kappa(u)gamma(z+x_p−x_a)=∫∫e^{iξ(x_p−x_a)}L_{G_v}(λ,ξ)nu(dλ)mu(dξ). Its modulus is at most ∫|L_{G_v}|dnu dmu=N1_e(G_v), with coefficient 1 and uniformly in the offset. This needs the inner bars, which the p14 image confirms; it is the p17 step. If a becomes terminal after v is removed, integrating (s_a,x_a) over s_a>s_{a-1} gives exactly N0(G_a), because no other factor involves a. This gives (H): I_R<=N1N0P_rest=(1/2)N0[2N1]P_rest. Domestic Case 1 has s_a<=s_{v-1} on the whole domain because a<v in the same chain. No division is used.

## R03 Fusion eligibility and mass norm

Verdict: PASS.

After R's indicator is dropped (LF114), the nonterminal unpaired a sits only in G_a(s_a−s_{a-1},·) and G_b(s_b−s_a,·), where b is a's successor in its own chain. Integrating s_a∈(s_{a-1},s_b) and x_a∈R^d gives F(s_b−s_{a-1},x_b−x_{a-1}) with F(t,x)=∫_0^t∫G_a(s,y)G_b(t−s,x−y). This matches the source p18 G̃ and equals the full convolution of the zero-extended kernels. By Tonelli F>=0, F is L1 and N0(F)=N0(G_a)N0(G_b) exactly. If a is the first vertex, its predecessor is its own chain root (0,0) under the p14 convention s_{n1}=0,x_{n1}=0 for G_{n1+1}, and the formula is unchanged. Every edge norm of F is finite by (E1)/(E2): N1_e(F)<=N0(G_a)N1_e(G_b) and N2_e(F)<=N0(G_a)N2_e(G_b) for every e, so the cross-label hypotheses of the n−1 induction hold for the fused family. Zero kernels or masses give F=0 and cause no division. Changing the L1 representative on a null set changes no Tonelli integral.

## R04 First-slot fusion retains the 2: N1_e(G*H)<=N0(G)N1_e(H), exact HALF

Verdict: PASS.

The Fourier–Laplace transform factors as L_F=L_{G_a}L_{G_b} by absolute Fubini, with λ>=0 and both kernels L1. Also |L_{G_a}(λ,ξ)|<=∫e^{-λt}G_a<=N0(G_a). Hence N1_e(F)=∫|L_{G_a}||L_{G_b}|<=N0(G_a)N1_e(G_b) for every e (E1). In case i=1 the induction supplies 2N1_{e1}(F), because F is in the reduced Q̃1. Source p18 (3.9) drops that 2; I confirmed this on the image, so it is a genuine source gap. With the 2 kept, the p19 conversion N1(F)<=N2N2 (itself a valid scalar inequality) yields only N1_{e0}(G_v)·2N2N2·B_rest, which is the FULL product and not the half Case 3 needs. Control: with mu=δ0, A=(0,1], a=1/2 and G=H=e^{-t}φ, the substitution λ=u² gives nu=(2/√π)du. Then N1(G*G)=(2/√π)∫_0^1(1+u²)^{-2}du=(2/√π)(2+π)/8 and N2(G)²=∫nu/(1+λ)=√π/2. So 2N1(G*G)/N2(G)²=1+2/π>1, and the 2 cannot be absorbed. The candidate instead bounds N1_{e0}(G_v)·2N1_{e1}(F)·B_rest<=(1/2)N0(G_a)[2N1_{e1}(G_b)][2N1_{e0}(G_v)]B_rest, which is the claimed exact half, with Q0=R0∪{a} and Q1=R1∪{b,v}. Counts: the reduced partition has |R0|=|R1|+1, so the new |Q0|=|R1|+2=|Q1|. This is one new mass and two new first slots, and no edge is turned into two second slots. I verified the derivation independently.

## R05 Second-slot fusion: N2_e(G*H)<=N0(G)N2_e(H)

Verdict: PASS.

Work at a finite cap. Take the feature map Φ(t,x)=h_λ(t,·)e^{iξx} in L²(nu⊗mu⊗dr) with h_λ(t,r)=√(2λ)e^{-λ(t−r)}1_{r<=t}. Then ∫h_λ(s,r)h_λ(t,r)dr=2λe^{-λ(s+t)}∫_{-∞}^{min}e^{2λr}dr=e^{-λ|s−t|}, which I checked. Thus <Φ(s,x),Φ(t,y)>=kappa(s−t)gamma(x−y), and ‖Φ‖²=nu(A_L)mu(R^d) is finite, so the integrals are Bochner integrals. N2_e(G)=‖∫GΦ‖. A spacetime translation acts as a unitary on the feature space: a shift in r and multiplication by e^{iξz}. Translation therefore preserves N2 for zero-extended kernels. F=∫G_a(r,z)τ_{(r,z)}G_b dr dz, and Minkowski gives N2(F)<=N0(G_a)N2(G_b) (E2). Monotone convergence in the cap carries this to the uncapped norms. This uses only the stationary covariance kernel. It does not need positive definiteness of an independently shifted kernel or a finite total original mu, since mu_e is the finite heat-weighted measure. The i=2 lift: the term N1_{e0}(G_v)N2_{e1}(F)B_rest is at most (1/2)N0(G_a)[2N1_{e0}(G_v)]N2_{e1}(G_b)B_rest. The source's p20 spectral proof is valid and gives the same bound; I checked it on the image.

## R06 All three slot lifts: partition, counts, edge multiplicities, p19 union/count, nonincident labels

Verdict: PASS.

Reduced partition R0,R1,R2 together with F's slot. i=0: |R0|+1=|R1|. New Q0=R0∪{a,b} and Q1=R1∪{v}, so |Q0|=|R0|+2=|Q1|; Q2=R2 is even, and e0 is first once. i=1: |R0|=|R1|+1. New Q0=R0∪{a} and Q1=R1∪{b,v}, so the counts are equal. e1 was F's unique first occurrence and now sits on b; e0 sits on v; e0∉D' so the two differ; neither is in Q2. i=2: |R0|=|R1| and |R2| is odd. New Q2=R2∪{b} is even. e1 now has exactly two second occurrences and e0 is first once. In all three branches the labels are disjoint and cover {1..2n}, and every edge of D is used first once or second twice. Source p19 i=0 prints Q̃0∩{j0,j0+1}, which is empty; this is a typo and union is correct. Source p19 i=1 prints '#(Q̃1)−1' first labels in D'∖{(j1,k1)}. Counting gives |D'|−1=n−2=|Q̃1|+|Q̃2|/2, so the correct number is #(Q̃1); this is an off-by-one in the print. Nonincident labels: the p15 image's second example assigns ‖G3‖^{(1)}_{1,5} and ‖G5‖^{(1)}_{2,4}, so the source rule does not require incidence, and the i=1 relabeling of e1 onto G_b is admissible. No consumer I read (OWN006/007/008/010) uses incidence.

## R07 Base cases, empty or unequal chains, zeros, p16 swapped caption

Verdict: PASS_WITH_NOTES.

n=0: the integral and the product are both 1. n1=n2=1: the cross pairing at a common root is bounded by N2N2 via covariance CS, giving Q2={1,2}. A single chain of two, whichever chain is empty, factors exactly as N0(G_first)·∫G_last kappa gamma<=N0(G_first)N1(G_last)=(1/2)N0[2N1]. The general step also reproduces these from n=0. The p16 caption for n1=0,n2=2 prints ‖G1‖^{(1)}‖G2‖^{(0)}, which swaps the chronological labels. The candidate's control shows that the UNMULTIPLIED swap fails: arctan(1/2)/√π>√π/8, ratio about 1.18. I checked this, including tan(π/8)=√2−1<1/2. The swap also fails WITH the theorem's factor 2. In independent-fusion-controls the ratio is about 5.07>2, with an exact certificate 16(1+λ)/(16+λ)∈(4,32/5) on [4,9]. Alternatively, put G1 near time T: N1(G1)~T^{-1/2}→0 while N0(G1)N1(G2) stays fixed. So this is a source label typo, not a falsification of the existential (3.6), and the candidate uses the correct Q0={first}, Q1={last}. Empty chains in the induction step are handled because the nonempty chain's endpoint necessarily has a domestic partner. One-vertex chains use the root. Zero mu_e, A_e, kernels or norms make the corresponding factors 0 at finite caps, with no division and no 0×∞.

## R08 Case 2: predecessor time and space offsets; OWN214 coefficient-one CS

Verdict: PASS.

Endpoints u,v are paired with each other, with predecessor origins (A,z) and (B,w); root (0,0) for a one-vertex chain. The inner integral is ∫G_u(t−A,x−z)G_v(s−B,y−w)kappa(t−s)gamma(x−y)=Q(T_{A,z}G_u^0,T_{B,w}G_v^0). By OWN214 L:translated-covariance-CS (LF33-127, read completely), this is at most N2(G_u)N2(G_v) with coefficient 1, in all dimensions, after zero extension. Each self pairing is translated separately. The image confirms that p21 displays γ^0(s−r) after the change of variables while keeping the spatial offsets, so it drops A−B. This is a false equality in general: the control with G=4·1_(0,1/4)φ and offset 1 gives |u−v+1|>=3/4>|u−v|. The resulting inequality is still true via (D). Removing u, v and e0 leaves a valid (n−1)-diagram. Under the full induction, adding u,v to Q2 with e0 used twice keeps |Q0|=|Q1| and Q2 even. Case 2 needs no half, and the candidate claims none. The equality-versus-inequality issue is a source error, and the candidate's repair matches OWN214.

## R09 Case 3 regions: last-gap comparison, independent indicators, drop after extraction, own-chain successor

Verdict: PASS.

Case 3: a=partner(v)∈chain1 with a<u, and b=partner(u)∈chain2 with b<v; let p=u−1 and q=v−1. Split into R_A={s_a<=s_q} and R_B={s_a>s_q}; ties have measure 0 and are assigned to R_A. On R_A, s_a<=s_q<s_v, so kappa(s_v−s_a)<=kappa(s_v−s_q). The indicator involves only s_a and s_q, and q≠v. On R_B, chain order gives s_p>=s_a (a<=p) and s_q>=s_b (b<=q), so s_p>=s_a>s_q>=s_b and therefore kappa(s_u−s_b)<=kappa(s_u−s_p). The indicator involves only s_a and s_q, both different from u. In each region the endpoint is extracted first, then the indicator is dropped by positivity, then the partner is fused with its own-chain successor: a+1<=u in chain 1, and b+1<=v in chain 2. The cases a+1=u and b+1=v are allowed. In global indexing the first vertex of chain 2 has root predecessor and successor n1+2 in its own chain (the 'k=b+1⇒b+2' item). The candidate defines successors by chain, so this is handled. No restriction survives into the reduced full diagram before the n−1 hypothesis is applied. This matches the p21 split, with a correct fusion step.

## R10 Regional HALF from FULL n−1 induction; half-sum<=max; exhaustiveness

Verdict: PASS.

Each region applies only the n−1 FULL bound to its reduced diagram, then the branch algebra of R02/R04/R05/R06, giving I(R_A)<=P_A/2 and I(R_B)<=P_B/2. No half is assumed inductively, so the argument is not circular (dependency-order JSON consistent). Then I_D=I(R_A)+I(R_B)<=(P_A+P_B)/2<=max(P_A,P_B). That is an admissible product with exact constants; there is no slotwise maximum and no extra factor. Without the halves, P_A+P_B can exceed the max. Exhaustiveness, which I derived independently: if a∈chain2 or b∈chain1 we are in Case 1. Otherwise a∈chain1 and b∈chain2. If a=u then b=v (Case 2). If a≠u then b≠v, because partner(v)=a≠u, so a<u and b<v (Case 3). In Case 3 both chains have length at least 2. One-vertex chains fall into Case 1 or Case 2, and empty chains into Case 1. Induction is on n, with n=0 as the base.

## R11 Caps to measurable domains, finite admissible set, zeros

Verdict: PASS_WITH_NOTES.

At cap L the theorem holds with nu_e^L finite: for each L there is an admissible (Q_L,ℓ_L) with I^L<=P^L(Q_L). For fixed n and D the set of (partition, edge-label map) pairs is finite, so some pair recurs along a subsequence L_m→∞. Since every norm is monotone in L (N1's integrand is nonnegative; N2²'s kappa^L increases with gamma>=0 and G>=0), P^L(Q)<=P(Q). The capped diagram integrand increases pointwise to the uncapped one (defined as that limit, possibly +∞ on diagonals), so by monotone convergence I=lim I^{L_m}<=P(Q). Only the upper bound P^L<=P is needed; candidate LF194 also states convergence of the product, which is true but unnecessary. The domestic and regional halves pass the same way. Amplitude: N1 is linear in c·mu_e and N2 is linear in √c, with each edge used first once or second twice, so every product has degree c^1 per edge (checked). Zero edges give finite-cap diagrams equal to 0, so the limit is 0 and no 0×∞ arises. No uniform-in-order claim is made. Note: the chosen Q may depend on the caps, mu_e and A_e, not only on the kernels; the candidate's subsequence argument handles this.

## R12 Quantifier: ∀G∃Q (candidate) versus ∃Q∀G (strong literal p15 reading)

Verdict: PASS_WITH_NOTES.

The p15 image reads: 'There is a partition {Q0,Q1,Q2}..., possibly depending on n1, n2 and D, such that...'. Read strictly, this lists the only permitted dependencies, so Q would be independent of G, mu_e and A_e. But the printed proof ends at p21 by 'choosing the one that produces the larger product', which depends on norm values. So the printed proof establishes at most ∀G∃Q, and the strong reading is unproved by the source. The candidate proves exactly ∀(G,mu,A)∃(Q,ℓ) (LF30, map LF7-14) and explicitly disclaims ∃Q∀G. I did not determine whether ∃Q∀G is true or false, and it is not needed. The candidate is therefore a precise qualification of the strongest literal statement, not a reproduction of it. Because the admissible set is finite, I_D<=max_Q P_Q. The consumers I read (R14) need only a scalar bound that holds for every admissible product, followed by scalar operations: infimum in θ and sums over pairings. No consumer selects, integrates, differentiates or passes a limit through a fixed partition, and no measurable selector is needed because everything is deterministic. The qualification is sufficient for these consumers and must be cited in per-family form.

## R13 Original-model application (d=1,2,3, all admissible Gamma)

Verdict: PASS_WITH_NOTES.

Hypothesis H:homog: d∈{1,2,3}, 0<α0<1, Gamma nonnegative even PD tempered Radon with Γ(cA)=c^{d−α}Γ(A), 0<α<d or α=d=1, and α+α0<2. OWN004 gives mu(B_r)=Vr^α, so mu_e=e^{−b|ξ|²/2}mu (b=ε_j+ε_h) is finite: αVb^{−α/2}∫u^{α−1}e^{−u²/2}du, using ball masses only and no angular density. gamma_e=p_b*Γ>=0. Temporal domains (0,(δ_j∨δ_h)^{−1}] and tails (M,L] carry the Γ_E(α0) normalization. The kernel e^{−θt}(p_η*G_t) is a nonnegative L1 function in d=1,2,3, using η>0 first in d=3. Its N0 is θ^{−2} and its Fourier–Laplace transform is e^{−η|ξ|²/2}/((θ+λ)²+|ξ|²)>=0, so the inner modulus in (3.4) is harmless (checked against OWN004). The cross-label norms of every kernel against every edge are bounded by the full OWN004 norms: the N1 integrand is positive; for N2 the per-ξ temporal form is nonnegative (kappa PD), so heat multipliers<=1 and restriction of the Laplace domain decrease it. White noise (α=d=1) and Gamma=0 are covered. The OWN004 scalings N1∝θ^{α+α0−2} and N2²∝θ^{−β} make 2N0N1 and N2² both of degree θ^{−β}, which I checked. Remaining current-OWN premises, not reproved here: removal of Green smoothing before noise smoothing (OWN006/007/010 proofs); identification of the source's temporal regularization γ^0_δ in (2.11)/(2.24) with the Laplace truncation; OWN005's weak spatial limit. All three are used at their stated clauses only.

## R14 Direct consumers OWN004/214/006/007008/010; indirect 002/009/051

Verdict: PASS_WITH_NOTES.

OWN006 (LF38-63): at θ=1, N0=1. Every unmarked edge contributes either 2N1<=2A or N2²<=B² to the product, hence <=H=max(1,2A,B²). The marked tail edge contributes 2A_M or B_M², whichever mode it receives. So every admissible product is <=H^{k−1}(2A_M+B_M²), and with the k difference-of-products terms and e^{T1+T2} this matches E:joint-temporal-tail, uniformly in widths and caps. OWN007/008: products are <=(θ^{−2})^{q0}(2C0)^{q1}(C0θ^{−1})^{q2}<=D^{q1+q2}θ^{−(2q0+q2)}<=(D²)^nθ^{−2n}, using q0=q1 and 2q0+q2=2n, and the choice θ0+n/t is made after Q has disappeared (checked). OWN010: exponent −2q0+(α+α0−2)q1−βq2/2=−β(q0+q2/2)=−βk and constant<=K^k with K>=max(2N1(1),N2(1)²), for every θ>0 (checked). OWN214 supplies Case 2 and is consistent with (D). OWN005 is an independent Brownian/Laplace proof that does not use Theorem 3.1 (read completely). A Grep of the main source for Theorem~3.1 citations found only LF214, 293, 457, 807, 898, 1141, 1222, 1231, 1300, 1324, 1563, 1607 and 7877. I read 205-309, 445-469 and 1600-1635, and none needs ∃Q∀G. Indirect 002/009/051 were not reviewed as whole parents and remain current-OWN conditions.

## R15 Attribution, constants and limits

Verdict: PASS_WITH_NOTES.

Constants preserved exactly: 2 per first norm, coefficient 1 for N2N2, the domestic and regional 1/2, q0=q1, even q2, and every edge first once or second twice. No C^n is added, and nonincident labels are permitted by the source rule. Printed-source defects confirmed against the images: (3.5) repeated x (typo; intended y); p16 swapped caption labels (fails even with the factor 2); p18 (3.9) missing 2 in the i=1 fused factor (genuine proof gap in the print); p19 ∩ for ∪ and the #(Q̃1)−1 off-by-one; p21 Case 2 dropped time offset A−B (false equality, true inequality); p21 Case 3 subscript naming. None of the repairs is attributed to Chen; the candidate keeps SOURCE-INTERNAL-DISCREPANCY. The finite controls are abstract finite-theorem inputs (mu=δ0 or a Gaussian mu, α-free) and are explicitly labelled as not homogeneous-SPDE examples. Key ratios hand-checked: 1+2/π; arctan(1/2)/√π versus √π/8; Gaussian c1=1/√2, c2=1/√3 and ratio √(2/3)(1+2/π)>1. I found no ancillary arithmetic error. Outcome: a per-family exact-constant reconstruction of intended (3.6) with the y-norm. It is not the strongest literal ∃Q∀G reading and not the literal x-norm. It does not narrow the whole-paper C2, the 214/240/13 obligations or any acceptance gate.

## Fatal findings

None.

## Major findings

None.

## Minor findings

- Candidate §1 LF49-54: the candidate's own p16 control shows only that the UNMULTIPLIED swapped caption fails (ratio ≈1.18<2). Stronger and supportable: the printed swapped product with the theorem's factor 2 also fails. Examples: independent-fusion-controls with A=[4,9], ratio ≈5.07>2; or G1 concentrated near a large time T, where N1(G1)→0. Optional wording strengthening only.
- Further print typos not itemized in the ledger, none consequential to the reconstruction: p16 'In summary' display writes |s1−s2|^{−α0}γ(x−y) instead of γ^0_{1,2}γ_{1,2}; p19 displays γ^0(s+t)γ(x−y)G(s,x)G(t,x), repeating the (3.5) x typo; p17 uses μ(dξ) without the edge subscript; p18 has x_{j0 1}; p21 has 'k1∈I2' for k0 and 'Q'_1,Q'_2,Q'_3' for Q'_0,Q'_1,Q'_2.
- Quantifier bookkeeping: the per-family Q may depend on G, mu_e, A_e, the finite caps, θ and the vertex widths, not only on n1, n2 and D. Any adopted citation should state Theorem 3.1 in the ∀(G,mu,A)∃(Q,ℓ) form with the y-norm, and should not quote p15's 'possibly depending on n1,n2 and D' as if a kernel-independent Q were proved.
- OWN008 LF108 writes the temporal domain as [0,(δ_j∨δ_l)^{−1}], whereas the candidate uses (0,·]. The difference is Lebesgue-null and harmless.
- Candidate LF194: 'its product converges to the corresponding ORIGINAL product' is true but unnecessary; only the monotone bound P^L(Q)<=P(Q) is needed.
- The current OWN006/007/008/010 text still cites the printed Theorem 3.1 (3.6). Adopting the candidate means re-pointing those citations to the reconstructed per-family statement with the independent-y norm. This is editorial and outside this focused scope.

## Required repairs

None.

## Limitations

- This is an AI review, not human verification, a novelty audit, whole-paper acceptance, or acceptance of the 214/240/13 obligations, the final cold review, or Kimi/source-visual clearance.
- The full 263-page technical PDF and the 64-page primary outside pp14-21 were not read. The source's temporal regularization γ^0_δ in (2.11)/(2.24), which OWN006/008 identify with the Laplace truncation (0,(δ_j∨δ_h)^{−1}], was not checked against the primary pages.
- The indirect consumers 002/009/051 were checked only through a Grep for Theorem~3.1 citations and spot reads of main LF205-309, 445-469 and 1600-1635; their full proofs were not reviewed. Green-before-noise removal and OWN005's weak limit were accepted as current-OWN premises at their stated clauses, not reproved.
- The page images were the reduced-resolution review carriers (max 1000px). They were legible enough to confirm the inner bars in (3.4), the repeated x in (3.5), the missing 2 in (3.9), ∩ on p19, the dropped offset on p21 and the nonincident labels on p15.
- No code was executed. The finite-control numbers were checked by hand only for the key exact ratios. The combinatorial enumerations up to n=4 in the control JSONs were not re-run and were not used as evidence of the general induction, which I verified analytically.
- Whether the strong ∃Q∀G version of Theorem 3.1 is true or false was not determined. It is not needed by the consumers reviewed.

## Actual reported source coverage

- .review/required-sources.json lines 1-126 (read plan; complete)
- application-and-quantifier-map.md lines 1-40 (complete)
- science/candidate-full-proof.md lines 1-226 (complete)
- science/source-correction-ledger.md lines 1-20 (complete)
- science/partition-consumer-qualification.md lines 1-77 (complete)
- adversarial-checklist.md lines 1-22 (complete)
- review-request.md lines 1-24 (complete)
- primary/pages/page-14.layout.txt lines 1-70 (complete)
- primary/pages/page-15.layout.txt lines 1-61 (complete)
- primary/pages/page-16.layout.txt lines 1-59 (complete)
- primary/pages/page-17.layout.txt lines 1-74 (complete)
- primary/pages/page-18.layout.txt lines 1-72 (complete)
- primary/pages/page-19.layout.txt lines 1-55 (complete)
- primary/pages/page-20.layout.txt lines 1-60 (complete)
- primary/pages/page-21.layout.txt lines 1-64 (complete)
- primary/review-pages/page-14.png through page-21.png (all eight images viewed in full)
- current-source/model-and-result-context.tex.txt lines 1-34 (complete)
- current-source/damped-norm-definitions-and-OWN004.tex.txt lines 1-121 (complete)
- current-source/translated-CS-OWN214-and-source-qualification.tex.txt lines 1-243 (complete)
- current-source/OWN005-independent-spatial-measure-context.tex.txt lines 1-183 (complete)
- current-source/OWN006-application.tex.txt lines 1-97 (complete)
- current-source/OWN007008-crude-application.tex.txt lines 1-147 (complete)
- current-source/OWN010-homogeneous-envelope-application.tex.txt lines 1-77 (complete)
- science/original-complete-repair-proposal.md lines 1-131 (complete)
- science/original-dependency-order.json lines 1-102 (complete)
- science/candidate-finite-controls.json lines 1-177 (complete)
- science/independent-fusion-controls.json lines 1-196 (complete)
- SUPPLEMENTARY (not required; partial by design): reference/current-source/notes/notes_stratonovich_ham_second_moment.tex lines 205-309, 445-469, 1600-1635, plus a Grep with no truncation for 'Theorem~3.1' citations across reference/current-source/notes/
