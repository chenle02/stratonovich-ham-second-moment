# Review Result
Category: proof-readability-equivalence
Model: deepseek-v4-pro
Verdict: PASS_WITH_NOTES
Confidence: high

The ten assigned proofs (global main ordinals 31–40) are read completely in both revisions. In every case the NEW revision differs from the OLD only by added roadmap sentences and "Step n" headings; the declarations, hypotheses, displayed formulas, and the mathematical deductions are byte-for-byte the same in the ten proof bodies (the two corollary proofs, 36 and 39, receive no restructuring at all). All ten proofs reconstruct publicly with checkable arithmetic; the only reason for NOTES is that the proofs lean on unassigned baseline inputs (Wick expansion, P:mixed, L:joint-fixed-order, the Chen wave-kernel Fourier formulas), which I can check for hypothesis fit but whose own proofs are outside the assigned set.

I reconstruct each proof below independently, not treating OLD as an oracle. Constants are verified numerically where possible.

## L:d1-spatial
- Global main ordinal: 31
- Old reading: COMPLETE
- New reading: COMPLETE
- Public reconstruction: COMPLETE
- Original-step coverage: (1) convolution bounds for the two covariances; (2) descending-label integration with the opening/closing invariant; (3) weighted AM-GM. The NEW adds a roadmap and Steps 1–3 with no mathematical change.

**Step 1 (convolution bound, Riesz).** G(h,y) = ½1_{|y|<h}. The supremum over z of ∫G(h,y)c_α|y+z|^{-α}dy = ½c_α sup_z ∫_{z-h}^{z+h}|u|^{-α}du. The even decreasing integrand makes the interval centered at 0 the maximizer, giving ½c_α·2h^{1−α}/(1−α) = c_αh^{1−α}/(1−α). Replacing γ by γ_ε = p_ε*γ and writing γ_ε(y+z) = ∫p_ε(w)γ(y+z−w)dw, the same supremum still bounds the mass-one average (Tonelli). So sup_z ∫G(h,y)γ_ε(y+z)dy ≤ c_αh^{1−α}/(1−α), uniform in ε.

**Step 1 (white).** γ_ε = c_δp_ε, so ∫G(h,y)γ_ε(y+z)dy = ½c_δ∫_{z−h}^{z+h}p_ε(u)du ≤ c_δ/2.

**Step 2 (descending integration).** The change x_l → y_l = x_l − x_{p(l)} is triangular with unit diagonal, determinant one. Processing labels in order 2k,…,1: at a closing label l∈C_D the pair is (i,l) with i<l, x_l−x_i = y_l+z where z uses only earlier-processed increments; no other surviving pair touches y_l, so the one-factor convolution bound removes it. At an opening label the partner's factor was already removed; the only remaining y_l factor is G(h_l,y_l) with ∫ = h_l. There are k of each type, yielding (c_α/(1−α))^k ∏_{O}h_i∏_{C}h_j^{1−α} (Riesz) and (c_δ/2)^k∏_{O}h_i (white).

**Step 3 (AM-GM).** Maximize ∏_{O}h_i∏_{C}h_j^{1−α} under ∑h_l ≤ 2t. Lagrange: h_i = 2t/(bk) at openings (weight 1), h_j = (1−α)2t/(bk) at closings (weight 1−α), total weight k+k(1−α) = kb. The value is (2t/(bk))^{k+k(1−α)}(1−α)^{(1−α)k} = (2t/(bk))^{bk}(1−α)^{(1−α)k}. Multiplying by (c_α/(1−α))^k gives c_α^k(1−α)^{−αk}2^{(2−α)k}(2−α)^{−(2−α)k}t^{bk}k^{−bk} = K_sp^k t^{bk}/k^{bk}, exactly with K_sp = c_α2^{2−α}(1−α)^{−α}/(2−α)^{2−α}. White: ∏_{O}h_i ≤ (2t/k)^k, times (c_δ/2)^k = (c_δ)^k t^k/k^k = K_sp^k t^{bk}/k^{bk} with b=1, K_sp = c_δ.

- Argument preservation: PRESERVED (NEW = OLD + headings).
- New explanations: JUSTIFIED (roadmap accurately names the three deductions).
- Evidence: OLD LF ≈4831–4878, NEW LF ≈5381–5442; the AGM constant identity and the white constant identity are recomputed above and match K_sp for both cases.

## P:d1-upper
- Global main ordinal: 32
- Old reading: COMPLETE
- New reading: COMPLETE
- Public reconstruction: COMPLETE

**Step 1 (common spatial bound, temporal pairing sum).** F_k(s) = ∑_{D∈Π_k}∏_{(i,j)∈D}|s_i−s_j|^{−α_0} is invariant under all (2k)! permutations because a permutation induces a bijection of pairings. The pairwise integral is ∫_{[0,t]²}|s−r|^{−α_0}ds dr = ∫_0^t[s^{1−α_0}+(t−s)^{1−α_0}]/(1−α_0)ds = 2t^{2−α_0}/((1−α_0)(2−α_0)) = Zt^{2−α_0}. Each pairing's k pairs are disjoint, so ∫_{[0,t]^{2k}}∏_{(i,j)∈D}|s_i−s_j|^{−α_0}ds = (Zt^{2−α_0})^k, and summing over P_k pairings gives P_k(Zt^{2−α_0})^k. The cell [0,t]^m_<×[0,t]^{n}_< is one of m!n! symmetric cells, giving the displayed E:d1-time-symmetry = P_k(Zt^{2−α_0})^k/(m!n!).

**Step 2 (counts).** Choosing the smallest label's partner gives P_k = (2k−1)P_{k−1}, so P_k = (2k)!/(2^k k!). Also Σ_{m=0}^{2k}1/(m!(2k−m)!) = 2^{2k}/(2k)!. Multiplying the spatial maximum K_sp^k t^{bk}/k^{bk} (valid because ∑h_l ≤ 2t) by the pairing/split counts:
K_sp^k t^{bk}/k^{bk} · 2^{2k}/(2k)! · (2k)!/(2^k k!)·(Zt^{2−α_0})^k = (2ZK_sp)^k t^{(2−α+2−α_0)k}/(k!k^{bk}) = (2ZK_sp)^k t^{βk}/(k!k^{bk}) since b+2−α_0 = 4−α−α_0 = β.

**Step 3 (limits and series).** Removal of regularization uses L:joint-fixed-order (hypothesis H:homog holds under E:d1-covariances); products pass to L^1 by the Cauchy–Schwarz product inequality ||YZ−Y′Z′||_1 ≤ ||Y−Y′||_2||Z||_2+||Y′||_2||Z−Z′||_2. The factorial step: k^{bk} = (k^k)^b ≥ (k!)^b, so k!k^{bk} ≥ (k!)^{b+1} = (k!)^q with q = 3−α. Finally Σ_k z^k/(k!)^q = Σ_k (z^{k/q}/k!)^q ≤ (Σ_k z^{k/q}/k!)^q = e^{qz^{1/q}} for q≥1 (here q ≥ 2 since α≤1); z = 2ZK_sp t^β gives κ = β/q = (4−α−α_0)/(3−α), C_dir = q(2ZK_sp)^{1/q}.

- Argument preservation: PRESERVED.
- New explanations: JUSTIFIED.
- Evidence: symmetry factor Z, the split sum 2^{2k}/(2k)!, P_k, and the (k!) exponent are all recomputed; the temporal-pairing symmetry factor is exactly m!(2k−m)! (checked above); no extra factor is lost.

## L:low-alpha-convolution
- Global main ordinal: 33
- Old reading: COMPLETE
- New reading: COMPLETE
- Public reconstruction: COMPLETE

**Step 1 (spectral ball masses).** Since γ(c·) has spectral measure the pushforward of μ under ξ→cξ, homogeneity γ(c·)=c^{−α}γ gives μ(A/c)=c^{−α}μ(A), i.e. μ(cA)=c^αμ(A) (consistent with the degree-α scaling of μ used in L:damped-homogeneous-norms). Hence μ(B_R) = VR^α, and by outer regularity μ({0}) = lim_{R↓0}VR^α = 0 since α>0. Layer cake: min(h,|ξ|^{−1}) = ∫_0^h 1_{|ξ|<u^{−1}}du, so ∫min(h,|ξ|^{−1})μ(dξ) = V∫_0^h u^{−α}du = Vh^{1−α}/(1−α).

**Step 2 (smoothed convolution).** With |sin s| ≤ min(s,1), |ŴG_h(ξ)| = |sin(h|ξ|)|/|ξ| ≤ min(h,|ξ|^{−1}). The Gaussian multipliers of p_ε and p_η are bounded by 1 (equals 1 when η=0). Fourier Fubini is justified by the Gaussian-weighted finite measure (polynomial ball growth). So |∫G_{h,η}(dy)γ_ε(y+z)| ≤ ∫min(h,|ξ|^{−1})μ(dξ) = Vh^{1−α}/(1−α). Nonnegativity of γ_ε (Gaussian translates of a nonnegative distribution) and of G_{h,η} gives the lower bound 0. Uniform in ε>0, η≥0, z.

- Argument preservation: PRESERVED.
- New explanations: JUSTIFIED.
- Evidence: the layer-cake identity and ball-mass computation are fully public; the bound uses ball masses, not a radial density (the text's qualification is accurate).

## L:alpha-one-convolution
- Global main ordinal: 34
- Old reading: COMPLETE
- New reading: COMPLETE
- Public reconstruction: COMPLETE

**Step 1 (polar decomposition).** μ({0}) = 0. σ(E) = μ{0<|ξ|≤1, ξ/|ξ|∈E} with σ(S^{d−1}) = V. Homogeneity μ(cA)=cμ(A) gives sector mass Rσ(E); subtracting sectors yields mass (r_2−r_1)σ(E) on polar rectangles (r_1,r_2]×E, and uniqueness of measures on the generated σ-algebra gives μ = dr⊗σ. Evenness of the real covariance transfers to μ, hence to σ.

**Step 2 (radial integral).** The combined multiplier is e^{−(ε+η)r²/2} = e^{−ar²}, a = (ε+η)/2 > 0. Pairing against e^{iξ·z}, evenness kills the sine part, giving ∫G_{h,η}(dy)γ_ε(y+z) = ∫_{S^{d−1}}I_a(h,θ·z)σ(dθ) with I_a(h,v) = ∫_0^∞e^{−ar²}sin(hr)r^{−1}cos(rv)dr. The angular integral already runs over both antipodes, so no factor 2 appears.

**Step 3 (one-dimensional convolution bound).** For g_h = ½1_{|v|<h} and p_{2a}^{(1)} = (4πa)^{−1/2}e^{−v²/(4a)}: ĝ_h = sin(hr)/r and p̂_{2a}^{(1)} = e^{−ar²}. Then (g_h*p_{2a}^{(1)})(v) = (2π)^{−1}∫e^{irv}e^{−ar²}sin(hr)r^{−1}dr = π^{−1}I_a(h,v) (the odd part vanishes by evenness). Since 0 ≤ g_h ≤ ½ and p has mass 1, 0 ≤ g_h*p ≤ ½, so 0 ≤ I_a ≤ π/2. Integrating against σ gives the upper bound (π/2)V = πV/2. The osciallatory integral is evaluated exactly at the α=1 endpoint; the divergent absolute envelope (∫|ξ|^{−1}μ) is not invoked.

- Argument preservation: PRESERVED.
- New explanations: JUSTIFIED.
- Evidence: the convention check (γ = ∫e^{ix·ξ}μ with no (2π)^{−d}) makes the polar display constant-free; the 1/π ∈ [0,½] identification is exact.

## P:low-alpha-upper
- Global main ordinal: 35
- Old reading: COMPLETE
- New reading: COMPLETE
- Public reconstruction: COMPLETE

**Step 1 (spatial bound in all dimensions).** The descending-label invariant of 31 is dimension-independent (it only uses which increment enters which position), so the vector-increment argument in d∈{1,2,3} gives S_D ≤ M^k∏_{O}h_i∏_{C}h_j^{1−α} for 0<α<1 (M = V/(1−α), from 33) and M^k∏_{O}h_i at α=1 (M = πV/2, from 34). Weighted AM-GM as in 31 converts this to (K_sp^gen)^k t^{bk}/k^{bk}: for α<1, M^k = V^k(1−α)^{−k} times the AM-GM value gives V^k2^{(2−α)k}(1−α)^{−αk}(2−α)^{−(2−α)k}; at α=1, M^k∏_Oh_i ≤ (πV/2)^k(2t/k)^k = (πV)^k t^k/k^k.

**Step 2 (temporal).** The pairing-sum symmetry, cube integral and split counts of 32 are spatial-dimension-free, so the identical product of counts gives A_k ≤ (2ZK_sp^gen)^k t^{βk}/(k!k^{bk}).

**Step 3 (limits).** In d=3: fix noise smoothing, η↓0 first (products of Green measures converge weakly with masses ∏h_l; dominated convergence on bounded simplices; the mixed-η covariance gives the L² Cauchy property), then noise smoothing via L:joint-fixed-order; in d=1,2 only the latter. Products pass in L¹ by Cauchy–Schwarz, bounds are uniform. The factorial and series bounds are 32's verbatim, with K_sp^gen replacing K_sp. The endpoint α=1 is reached by the separate Lemma 34, not by letting α↑1 in K_sp^gen (stated and preserved).

- Argument preservation: PRESERVED.
- New explanations: JUSTIFIED.
- Evidence: the M → K_sp^gen conversion is recomputed for both cases; the d=1 white agreement K_sp^gen = πV = c_δ (V = c_δ/π) is the remark's check, consistent.

## C:d1-first-calibration
- Global main ordinal: 36
- Old reading: COMPLETE
- New reading: COMPLETE
- Public reconstruction: COMPLETE

Single chain of length 2k: increments sum to t, so apply the spatial bound 31 (or the spatial part of 35) with t/2 replacing t, giving K_*^k(t/2)^{bk}/k^{bk}. The temporal pairing sum on [0,t]^{2k}_< is P_k(Zt^{2−α_0})^k/(2k)! (one ordered cell out of (2k)! symmetric cells). Hence
E X_{2k} ≤ K_*^k 2^{−bk}t^{bk}k^{−bk} · (2k)!/(2^k k!) · (Zt^{2−α_0})^k/(2k)! = (ZK_*/2^{b+1})^k t^{βk}/(k!k^{bk}).
Since b+1 = 3−α and k!k^{bk} ≥ (k!)^q, this is ≤ (ZK_*/2^{3−α})^k t^{βk}/(k!)^q. Odd terms vanish (Wick); the L² expansion permits summing expectations of partial sums; the scalar series bound of 32 then gives E u ≤ exp(q(ZK_*/2^{3−α})^{1/q}t^{β/q}) = exp(C_{1,*}t^κ), with C_{1,*} = q(ZK_*/2^{3−α})^{1/q}. The ratio C_{1,*}/C_{2,*} = (ZK_*/2^{3−α}·(2ZK_*)^{-1})^{1/q} = 2^{−(4−α)/(3−α)}, so C_{1,*} = C_{2,*}/2^{(4−α)/(3−α)}. Since (4−α)/(3−α) > 1, 2C_{1,*} < C_{2,*}. The first-moment lower-rate statement is conditional ("if the intended first-moment lower bound holds"), and the conclusion 2L_* ≤ 2C_{1,*} < C_{2,*} is a consistency check against P:Jensen, not a claimed inequality free of that premise. The nonzero qualification (K_* > 0, hence C_{1,*} > 0) is explicit.

- Argument preservation: PRESERVED (no restructuring in NEW).
- New explanations: JUSTIFIED (none added; conditional claim unchanged).
- Evidence: the t/2 substitution, the (2k)! cell factor, and the 2^{3−α} = 2^{b+1} identity are recomputed; the Jensen conditioning and nonzero-source qualification are preserved in both versions.

## P:higher-transfer
- Global main ordinal: 37
- Old reading: COMPLETE
- New reading: COMPLETE
- Public reconstruction: COMPLETE

**Step 1 (parameters and spatial elimination).** δ = α−1, and δ+α_0 < 1 (from α < 2−α_0) makes (1/(1−α_0), 1/δ) nonempty. From r > 1/(1−α_0): r(1−α_0) > 1 ⇒ (r−1)/r > α_0 ⇒ θ = α_0r′ < 1; δr < 1 from r < 1/δ, hence a = 1−δr/2 ∈ (½,1). The edge covariance combines endpoint widths as p_{ε_e}*p_{ε′_e} = p_{ε_e+ε′_e}, covered by H:spatial-maximum. Descending integration (same invariant as 31) gives S_D ≤ M^k∏_{O}h_i∏_{C}h_j^{−δ}, and the opening increments sum to ≤ 2t, so ∏_{O}h_i ≤ (2t/k)^k, i.e. S_D ≤ M^k(2t/k)^kH_D, H_D = ∏_{C}h_j^{−δ}. Note: this is a spatial bound for a fixed pairing, not the common maximum of 31.

**Step 2 (Hölder).** With T_D = ∏|s_i−s_j|^{−α_0}, Hölder on (counting × Lebesgue) with conjugates r,r′ gives ∑_D∫H_DT_D ≤ (∑_D∫H_D^r)^{1/r}(∑_D∫T_D^{r′})^{1/r′}. Dirichlet on Ω_{m,n}, with k_1,k_2 closing labels in the two chains (k_1+k_2 = k): closing increments have parameter 1−δr, the rest and the terminal gap parameter 1, so
∫_{Ω_{m,n}}H_D^r ds = Γ(1−δr)^k t^{(2−δr)k}/(Γ(1+m−δrk_1)Γ(1+n−δrk_2)).
The two Γ-arguments are positive with average 1+(2k−δrk)/2 = 1+ak. Log-convexity of Γ gives the product ≥ Γ(1+ak)², and Γ(1+ak) ≥ ∫_{ak}^{ak+1}x^{ak}e^{−x}dx ≥ e^{−1}(a/e)^{ak}k^{ak} ≥ e^{−1}(a/e)^{ak}(k!)^a, so the square ≥ D_a^{−k}(k!)^{2−δr} with D_a = e²(e/a)^{2a}. Thus ∑_D∫H_D^r ≤ P_k[Γ(1−δr)D_a]^k t^{(2−δr)k}/(k!)^{2−δr}. The sum ∑_DT_D^{r′} is symmetric (θ = α_0r′), so on Ω_{m,n} it equals P_k(Z_θt^{2−θ})^k/(m!n!) ≤ P_k(Z_θt^{2−θ})^k/(k!)² (m!n! ≥ (k!)² for m+n = 2k, maximum of the binomial coefficient at the middle). P_k = ∏_{j≤k}(2j−1) ≤ 2^kk!, and k^k ≥ k!.

Combining: the constant comes from 2^k (opening) × 2^k (P_k bound) × M^k, and the factorial exponent 1 (from k^k ≥ k!) plus (2−δr)/r + 2/r′ minus 1 (from the k! in P_k) equals (2−δr)/r + 2/r′ = 2−δ = q. So
∑_D∫_{Ω_{m,n}}S_DT_D ds ≤ {4M[Γ(1−δr)D_a]^{1/r}Z_θ^{1/r′}}^k t^{βk}/(k!)^q,
with time power 1+(2−δr)/r+(2−θ)/r′ = 3−δ−α_0 = β. There are 2k+1 ≤ 3^k splits, giving K = 12M[Γ(1−δr)D_a]^{1/r}Z_θ^{1/r′}.

**Step 3–4 (limits and series).** The limit passage mirrors 35 (d=3: η↓0 then noise widths; d=2: noise widths only), using L:joint-fixed-order under H:homog; the L¹ product bound is the displayed two-term Cauchy–Schwarz estimate. Then Σ_k z^k/(k!)^q ≤ e^{qz^{1/q}} with q = 2−δ = 3−α > 1, z = Kt^β, κ = β/q.

- Argument preservation: PRESERVED.
- New explanations: JUSTIFIED.
- Evidence: all four constants are recomputed: the Dirichlet normalization, log-convexity plus the explicit Γ lower bound yielding D_a, the symmetric-pairing cell factor, and the 4→12 constant chain including the 3^k split count. The "no low-α conclusion used" qualification (Lemma 31 is explicitly not applied) is preserved.

## L:higher-riesz
- Global main ordinal: 38
- Old reading: COMPLETE
- New reading: COMPLETE
- Public reconstruction: COMPLETE

**Step 1 (d=3).** G_h^{(3)} = σ_h/(4πh), mass h, G_h(hA) = hG_1(A). The unsmoothed convolution is ch^{1−α}F_3(z/h) with F_3(w) = ∫G_1^{(3)}(dy)|y+w|^{−α}. Spherical average: |y+w|² = 1+ρ²+2ρu, and F_3(w) = ((1+ρ)^v−|1−ρ|^v)/(2vρ), v = 2−α ∈ (0,1). For ρ<1, F_3 = (2ρ)^{−1}∫_{−ρ}^{ρ}(1+s)^{v−1}ds with f(s) = (1+s)^{v−1}; f is convex, so ρ[f(ρ)+f(−ρ)]−∫_{−ρ}^{ρ}f ≥ 0, i.e. F_3 is nondecreasing. For ρ>1, distance √(1+ρ²+2ρu) has derivative (ρ+u)/√(1+ρ²+2ρu) > 0, so the negative power decreases. Maximum at ρ=1: F_3(e_1) = 2^v/(2v) = 2^{1−α}/(2−α). So the uniform bound is ch^{1−α}2^{1−α}/(2−α) = (c2^{1−α}/(2−α))h^{−δ} = M_3h^{−δ}.

**Step 2 (d=2).** Claim G_1(B(w,R)) ≤ 2R^{3/2} for 0<R≤1/4. If |w|<1/2, the ball lies in |y|<3/4 where density ≤ 2/(π√7), mass ≤ 2πR²/(π√7)·… = 2R²/√7 ≤ R^{3/2}. If |w|≥1/2, slice in x: for |v|≤R, x≥1/4, L=√(1−v²), 1−|y|² = (L−x)(L+x) with L+x>1; integrating (L−x)^{−1/2} over a slice of length ≤2R gives ≤ 2√(2R), and the v-range of length ≤2R gives (2√2/π)R^{3/2} < 2R^{3/2}. Layer cake |y+w|^{−α} = α∫_0^∞R^{−α−1}1_{|y+w|<R}dR splits at R = 1/4: the tail gives 4^α (G_1 mass 1 times ∫_{1/4}^∞αR^{−α−1}dR = 4^α) and the head gives 2α∫_0^{1/4}R^{1/2−α}dR = 2α(α−3/2)^{-1}·(−)… = (2α/(3/2−α))4^{α−3/2}. Hence F_2 ≤ M_2/c with M_2 = c{4^α+2α(3/2−α)^{-1}4^{α−3/2}}.

**Step 3 (smoothing and optimality).** Tonelli + Gaussian convolution rules give ∫G_{h,η}(dy)γ_ε(y+z) = ∫p_{ε+η}(w)(G_h*γ)(z−w)dw (both widths combine into their sum, and γ_ε = p_ε*γ is even), so mass-one averaging preserves the supremum bounds for all independent widths — this is exactly the uniformity demanded by H:spatial-maximum. For optimality in d=3: the approximate-identity argument (neighborhood continuity; integrable singular ball with Gaussian tail ε^{−j/2}e^{−|x|²/(8ε)}; bounded far region) gives p_ε*|x|^{−λ}(x) → |x|^{−λ} for x≠0; Fatou at the maximizing shift (ρ=1, η=0) recovers the unsmoothed value M_3 since the single singular point has zero surface measure, so no smaller M can be uniform. This optimality is proved, not asserted; the d=2 constant is presented only as an admissible bound.

- Argument preservation: PRESERVED
- New explanations: JUSTIFIED
- Evidence: spherical and layer-cake formulas recomputed; the combined-width Gaussian identity is the explicit "independent regularization widths" check requested.

## C:higher-riesz
- Global main ordinal: 39
- Old reading: COMPLETE
- New reading: COMPLETE
- Public reconstruction: COMPLETE

The mixture |x|^{−α} = Γ(α/2)^{−1}∫_0^∞s^{α/2−1}e^{−s|x|²}ds (substitute u = s|x|²) represents c|x|^{−α} as a positive mixture of positive-definite Gaussians. Distributional positivity: for ψ = φ*φ̃ (Schwartz), local integrability (α<d) plus rapid decay give ∫|x|^{−α}|ψ|dx < ∞; Tonelli/Fubini on the mixture against ψ, with each Gaussian's integral against ψ = positive factor × |φ̂|² ≥ 0, proves nonnegative definiteness. The ranges α+α_0<2 are exactly the corollary's stated caps, and L:higher-riesz supplies H:spatial-maximum with all width uniformities; P:higher-transfer then applies with M = M_d.

- Argument preservation: PRESERVED (unchanged).
- New explanations: JUSTIFIED (none added).
- Evidence: the mixture formula and the positivity/quadratic-form justification are public; the corollary is a legitimate consumer of 37–38 at their stated hypotheses (Riesz admissible ranges and width uniformity).

## P:higher-obstructions
- Global main ordinal: 40
- Old reading: COMPLETE
- New reading: COMPLETE
- Public reconstruction: COMPLETE

**Step 1 (planar Riesz divergence).** h=1, z=−e_1, y = e_1+ρ(cosφ,sinφ), wedge 0<ρ<1/2, 2π/3≤φ≤4π/3. Then 1−|y|² = −2ρcosφ−ρ² satisfies 0<1−|y|²≤2ρ (since cosφ ≤ −1/2 and ρ<1/2). Since |y−e_1| = ρ and the G_1^{(2)} density is (2π√(1−|y|²))^{−1} ≥ (2π√(2ρ))^{−1}, area element ρdρdφ:
∫G_1^{(2)}(dy)c|y−e_1|^{−α} ≥ c(2π√2)^{−1}·(2π/3)∫_0^{1/2}ρ·ρ^{−α}·ρ^{−1/2}dρ = (c/(3√2))∫_0^{1/2}ρ^{1/2−α}dρ = ∞ for α ≥ 3/2 (logarithmic at α = 3/2).

**Step 1 (product counterexample).** a_1 = (1+max{2−α,α−1})/2, a_2 = α−a_1. For 1<α<2: a_1<1, a_2∈(0,1) (both verified from max{2−α,α−1}<1 and <2α−1), and a_1+a_2/2 = (1+max{…}+2α)/4 ≥ (2+α+2α)/4 = (2+3α)/4 > 1 since α>1. γ = c|x_1|^{−a_1}|x_2|^{−a_2} is homogeneous of degree −α, locally integrable (each exponent <1 in its coordinate), tempered, and the per-coordinate Gaussian mixtures make it nonnegative definite with the bound |ψ| ≤ C_N∏(1+|x_j|)^{−N} (N>1) justifying Tonelli/Fubini.

**Step 2 (explicit divergence).** u = 1−y_1, y_2 = √(2u−u²)w, with dy_2 = √(2u−u²)dw and 1−|y|² = (2u−u²)(1−w²):
∫G_1^{(2)}(dy)γ(y−e_1) = c(2π)^{−1}B((1−a_2)/2,1/2)∫_0^2u^{−a_1}(2u−u²)^{−a_2/2}du,
after ∫_{−1}^1|w|^{−a_2}(1−w²)^{−1/2}dw = B((1−a_2)/2,1/2) (finite since a_2<1). Near u=0 the integrand behaves like u^{−a_1−a_2/2} with a_1+a_2/2>1, so the integral diverges.

**Step 2 (transfer to d=3 and smoothing).** The projection of G_1^{(3)} = σ_1/(4π) onto (y_1,y_2) is the two graphs with Jacobian (1−|y|²)^{−1/2} each over the disk, i.e. 2/(4π√(1−|y|²))dy = G_1^{(2)}; since γ is y_3-free, the d=3 integral equals the divergent planar one. For the widths: p_ε*γ factorizes as c∏_{j=1,2}(p_ε^{(1)}*|·|^{−a_j})(x_j) (third coordinate integrates to 1); each 1-D factor converges to |x_j|^{−a_j} at x_j≠0 (a_j<1). The singular coordinate axes have zero shifted Green measure, so Fatou (with η=0) gives liminf_{ε↓0}∫G_1(dy)γ_ε(y−e_1) ≥ ∫G_1(dy)γ(y−e_1) = ∞. If both widths must be positive, take η=ε and use the combined-width Gaussian identity of 38: ∫G_{1,ε}(dy)γ_ε(y+z) = ∫p_{2ε}(w)(G_1*γ)(z−w)dw, and G_1*γ is lower semicontinuous at z = −e_1 (Fatou since γ is continuous off the zero-G_1-measure hyperplanes through −e_1), so its Gaussian average also tends to +∞. Hence no uniform M exists.

- Argument preservation: PRESERVED.
- New explanations: JUSTIFIED (the two-step split and the sentence in Step 2 describing the transfer are accurate).
- Evidence: the divergence formulas (both the wedge bound and the B-function integral) are recomputed; the a_1,a_2 feasibility and the a_1+a_2/2>1 condition are verified; the obstruction concerns only the spatial supremum H:spatial-maximum, as the closing remark states.

## Findings and limits

**Reading.** All ten assigned proofs were read in full in both revisions; no hash or statement-byte shortcut was used. Reading is COMPLETE for both OLD and NEW in every case, and public reconstruction is COMPLETE for all ten: each displayed estimate, symmetry factor, Dirichlet/Gamma constant, Hölder exponent, and final κ was re-derived above.

**Fidelity of the change.** The NEW revision's only edits inside the ten proofs are additive roadmap sentences and "Step n" headings in eight proofs (31–35, 37, 38, 40); the corollary proofs 36 and 39 are untouched. I detected no changed formula, no changed hypothesis, no suppressed qualifier, and no newly introduced defect. Headings accurately reflect the content (verified item by item), so New explanations are JUSTIFIED throughout.

**Requested checklist (all verified in the reconstructions).** Determinant-one triangular chain-increment change (31, 35, 37); opening/closing label sets and the descending-label invariant (31, 35, 37); white versus Riesz convolution constants and the white case b=1 (31, 32); independent edge covariance widths and combined-width Gaussian identity (37, 38); spectral ball masses μ(B_R)=VR^α (33); translated-Gaussian Fourier bound I_a = π(g_h*p_{2a}^{(1)}) with antipodal factor (34); endpoint α=1 via the oscillatory 1-D integral, not a limit in K_sp^gen (34, 35); temporal-pairing symmetry factor m!(2k−m)! (32, 35, 37); conjugate Hölder exponents r,r′ (37); Gamma/factorial constants Γ(1−δr), D_a and the factorial power q (37); exact κ = (4−α−α_0)/(3−α) in 32, 35, 37; d=1 sharp constants versus d=2,3 spectral bounds (31/32 vs 33–35); the additional spatial-maximum hypothesis as a genuine assumption (37); zero/nonzero covariance boundary and V>0 (35, 36); the small/large parameter distinctions (a=(ε+η)/2>0 in 34; ρ<1 vs ρ>1 and the planar 3/2 boundary in 38/40); source-dependent/Jensen calibration conditioning in 36; no limit interchange claimed in the assigned arguments; and no asserted (unproved) sharp constants, the only optimality claim being M_3 in 38, which is proved by approximate identity plus Fatou.

**Notes/limits.** (i) Each proof rests on unassigned baseline inputs: the Stratonovich/Wick expansion, P:mixed, L:joint-fixed-order, L:damped-homogeneous-norms, and the Chen wave-kernel formulas ŴG_h = sin(h|ξ|)/|ξ| and the d=2,3 G_h measures. I checked that each consumer invokes these at their stated hypotheses (H:homog, the d∈{1,2,3} and α ranges), but their own deductions are outside the assigned set and were not re-proved here. (ii) The convergence passages in 32, 35, 37 assert the fixed-order L² behavior of L:joint-fixed-order; that is an accepted unassigned input, not re-derived. (iii) 38's d=2 constant M_2 is an admissible but not claimed-optimal bound; optimality is claimed only for M_3. These points are pre-existing and identical in both revisions; they do not affect the argument-preservation verdict for the assigned proofs.
