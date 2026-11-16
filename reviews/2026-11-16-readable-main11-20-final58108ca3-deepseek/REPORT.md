# Review Result
Category: proof-readability-equivalence
Model: deepseek-v4-pro
Verdict: PASS
Confidence: high

Scope: the ten assigned global main-file proof ordinals 11–20 of `notes_stratonovich_ham_second_moment.tex`, OLD revision `cdde711c…` vs NEW revision `58108ca3…`. The rewrite is presentational: it inserts proof roadmaps and `Step k` headings, splits paragraphs, and adds four small clarifying sentences. All statements, equation labels, hypotheses and the mathematical argument bodies are otherwise byte-identical. I reconstructed every deduction independently below, including unchanged portions, and verified each added sentence against the surrounding definitions. No introduced defects were found; all added explanations are correct and anchored. Boundary/upstream results (e.g. `L:vertex-crude`, `L:joint-fixed-order`, `L:damped-homogeneous-norms`, `L:pairing-product-envelope`) are UNASSIGNED and were only checked for hypothesis compatibility at their use sites, not re-proved.

---

## P:mild-construction (ordinal 11)
- Global main ordinal: 11
- Old reading: COMPLETE. New reading: COMPLETE. Public reconstruction: COMPLETE.
- Original-step coverage (OLD 1988–2123; NEW 2171–2340, statement 2151–2165 vs 1968–1982 byte-identical):

1. *Gaussian polynomial degree space.* Define `\mathscr{P}_{≤n}` as closed degree-≤n space. Regularized terminal integrals and their `L^2` limits `X_n` lie there (imported Bochner construction).
2. *Multiplication bound* `E:occupied-multiplication`: for centered Gaussian `H`, `F∈\mathscr{P}_{≤n}`, `‖HF‖_2 ≤ 2√(n+1)‖H‖_2‖F‖_2`. Public check: take `H/‖H‖_2` as first coordinate of an ONB; creation/annihilation on total degree ≤ n have squared-coefficient weights `a_1+1 ≤ n+1` and `a_1 ≤ n`; sum of norms ≤ `√(n+1)+√n ≤ 2√(n+1)`. Approximation in the degree-closed space closes multiplication (explicitly restated).
3. *Measurability and spatial mean-square continuity.* `L:vertex-crude` gives absolute `L^2` summability of the series; joint strong measurability in `(s,y)` follows from Bochner domination (finite Green masses, bounded Gaussian moments). Joint spatial stationarity gives `‖Y_n^b(s,y)−X_n(s,y)‖_2 = ‖Y_n^b(s,0)−X_n(s,0)‖_2`, hence uniform convergence in `y` and continuous representatives. NEW adds an explanatory rescaling: at `t>0`, divide ordered times/spatial Green increments by `t`, using `G_{tr}(t dz)=tG_r(dz)` (mass check: `∫G(ct,c dz)=∫G(ct,dw)=ct=c∫G(t,dz)`), giving `t^{2n}` from the `n` time Jacobians and `n` Green rescalings; `t=0` is trivial. This only supports measurability at fixed `t>0`.
4. *Partially regularized terminal integral.* `I_{n,a}(t,x)=∫_0^t∫_{ℝ^d}G(t−s,x−dy)W_a(s,y)X_{n−1}(s,y)ds`; existence by `E:fixed-external-domination` `‖W_a X_{n−1}‖_2 ≤ 2√n √V_a q_{n−1}(T)` (degree ≤ n−1) with Green mass `t−s`.
5. *Inner-width limit.* `E:partial-vertex-limit` `I_{n,a}=lim_{b↓0}Y_n^{(b,a)}` in `L^2` (terminal-kernel Fubini at positive widths; `n=1` exact). `E:mixed-vertex-bound` `sup_{a>0}‖I_{n,a}‖_2 ≤ q_n(t)` passes `E:vertex-crude` to the inner limit.
6. *Dimension-3 Green-first convention.* `W_a X_{n−1}` is `L^2`-continuous in `y` (two applications of `E:occupied-multiplication`); convolution against `p_η*G_{t−s}` converges in `L^2` to convolution against `G_{t−s}` via partition of unity, scalar weak convergence, tightness, and the uniform `E:fixed-external-domination` bound; dominated time integration; no interchange of Green and noise limits (explicit).
7. *External width limit.* `E:external-vertex-limit` `lim_{a↓0}I_{n,a}=X_n` from `L:joint-fixed-order`: choose `r` with `‖Y_n^{(b,a)}−X_n‖_2<ζ` below `r`, then `‖I_{n,a}−X_n‖_2≤ζ`; arbitrary relative rates, no partial-limit theorem assumed.
8. *Full product.* `∑_n‖W_a X_{n−1}‖_2 ≤ 2√V_a ∑√n q_{n−1}(T)<∞` by `L:vertex-summability`; multiplication closed by a subsequence argument; `I_a=∑_n I_{n,a}` in `L^2`.
9. *Two-stage tail.* `‖I_a−(u−1)‖_2 ≤ ∑_{n=1}^N‖I_{n,a}−X_n‖_2 + 2∑_{n>N}q_n(t)`; `a↓0` then `N→∞`. Source (5.3)–(5.4)/§5(ii) not used.

- Argument preservation: PRESERVED. New explanations: JUSTIFIED (the `t^{2n}` sentence is correct as an amplitude-level remark; note it does not state full homogeneous rescaling of the covariance, which is irrelevant to the measurability purpose).
- Evidence: equations `E:occupied-multiplication`, `E:fixed-external-domination`, `E:partial-vertex-limit`, `E:mixed-vertex-bound`, `E:external-vertex-limit` are identical in both revisions; the only added prose is the `t>0` rescaling sentence in NEW Step 2 and the roadmap. The weight computation `a_1+1≤n+1`, `a_1≤n` is public.
- Lost steps/qualifiers: none. Pre-existing dependencies all satisfied: `L:vertex-crude` supplies `q_n` with `E:vertex-summability`; `L:joint-fixed-order` supplies joint convergence at arbitrary relative rates.

## P:envelope (ordinal 12)
- Global main ordinal: 12
- Old reading: COMPLETE. New reading: COMPLETE. Public reconstruction: COMPLETE.
- Original-step coverage (OLD 2158–2205; NEW 2375–2433; statement 2135–2156 vs 2352–2373 identical):

1. *Homogeneous norm scaling* `E:homogeneous-norms` from `L:damped-homogeneous-norms`: `N_0=θ^{−2}`, `N_1(θ)=N_1(1)θ^{α+α_0−2}`, `N_2(θ)^2=N_2(1)^2θ^{−β}`. Public: `N_0·N_1` has degree `−2+(α+α_0−2)=−β`, and `N_2^2` has degree `−β`. Pick `K≥max{2N_1(1), N_2(1)^2}`.
2. *Pairing majorant.* Each admissible `L:pairing-product-envelope` product uses `q_0` mass slots, `q_1=q_0` first-norm slots (factor 2 each), `q_2` second-norm slots with `q_0+q_2/2=k`. The combined `θ`-degree is `−2q_0+(α+α_0−2)q_0−(β/2)q_2=−β(q_0+q_2/2)=−βk`, so each product `≤K^kθ^{−βk}`, times horizon `e^{2θt}` and `P_k` pairings. Regulator limits: `d=3` Green then noise with Cauchy–Schwarz (`‖Y_mY_n−X_mX_n‖_1≤‖Y_m−X_m‖_2‖Y_n‖_2+‖X_m‖_2‖Y_n−X_n‖_2`); `d=1,2` noise only; uniform via `L:crude-corrected`. Hence `E:homogeneous-envelope`.
3. *Majorant.* `P:mixed` gives `E u^2 = ∑_k∑_m∑_D J`, so `E u^2 ≤ B_K(t)` with `2k+1` `m`-values per total order.
4. *Infimum.* Minimize `e^{2θt}θ^{−βk}`: derivative gives `θ=βk/(2t)`, value `e^{βk}(2t/(βk))^{βk}`. Public check by differentiation.
5. *Series sandwich.* Using `k!≤P_k≤2^kk!`, `(k/e)^k≤k!≤k^k`, `2k+1≤3^k`: `∑(at^β)^k/(k!)^q ≤ B_K ≤ ∑(bt^β)^k/(k!)^q` with `q=β−1`. The residual factor is `(k!)^{q+1}/k^{βk}=(k!)^β/k^{βk}∈[e^{−βk},1]`, absorbed into `a^k,b^k`. Upper bound by `(∑z^{k/q}/k!)^q=e^{qz^{1/q}}` (`ℓ^q⊂ℓ^1` for `q>1`). Lower: `k=⌊z^{1/q}/2⌋`, `1/(k!)^q ≥ 1/k^{qk}`, giving single summand `≥(z/k^q)^k≥2^{qk}`.
6. *Growth.* `log B_K≍t^{β/q}=t^ρ`, `ρ=β/(β−1)`; `ρ>κ` since `β−1=3−α−α_0<3−α`. The statement explicitly restricts the lower bound to the numerical majorant `B_K`, not the second moment.

- Argument preservation: PRESERVED. New explanations: JUSTIFIED (roadmap + two-step split only; no new mathematics).
- Evidence: exponents verified explicitly: `−2q_0+(α+α_0−2)q_0−(β/2)q_2=−β(q_0+q_2/2)`; `∫`-infimum differentiation; `(k!)^{\beta}/k^{\beta k}∈[e^{−βk},1]`; Hensel-type lower `z/k^q≥2^q`. Equation labels `E:homogeneous-norms`, `E:homogeneous-envelope`, `E:B-envelope`, `E:envelope-growth` unchanged.
- Lost steps/qualifiers: none. The non-identification of the lower bound with the second moment is preserved verbatim.

## L:phase-contractions (ordinal 13)
- Global main ordinal: 13
- Old reading: COMPLETE. New reading: COMPLETE. Public reconstruction: COMPLETE.
- Original-step coverage (OLD 2297–2347; NEW 2525–2586; statement 2281–2295 vs 2509–2523 identical):

1. *Radial spectral mass.* `μ(B_r)=Vr^α` by homogeneity + Fourier uniqueness; no origin atom.
2. *Heat comparison.* `∫e^{−s|q+ξ|²}μ(dξ)=∫p_{2s}(x)e^{iqx}Γ(dx)≤∫p_{2s}(x)Γ(dx)=∫e^{−s|ξ|²}μ(dξ)`. Public: `e^{−s|ξ|²}=Fourier(p_{2s})`; the middle equality is the Fourier transform of `p_{2s}Γ` at `−q`; evenness makes it real, nonnegativity of `Γ` gives the inequality.
3. *Resolvent.* Multiply by `e^{−λ²s}`, integrate `ds≥0` (Tonelli): `∫μ(dξ)/(λ²+|q+ξ|²) ≤ ∫μ(dξ)/(λ²+|ξ|²)`; at `q=0`, radial `dμ=αV r^{α−1}dr` gives `αV∫_0^∞r^{α−1}/(λ²+r²)dr=R_α λ^{α−2}`, using `∫_0^∞u^{α−1}/(1+u²)du=π/(2sin(πα/2))`.
4. *Trace.* `T_ε` identity by Fourier Fubini (`Γ_ε=p_{2ε}*Γ`). Nonnegative measure `Γ_ε(x)G_a(dx)` gives `|T_ε(a,q)|≤T_ε(a,0)`.
5. *Radial integral formula.* `Γ(B_r)=Mr^{3−α}`, so `dΓ_{rad}=(3−α)Mr^{2−α}dr`; `c_Γ=(3−α)M/(4π)` makes `∫F dΓ=c_Γ∫_{ℝ³}F(x)|x|^{−α}dx` for radial Schwartz `F` (spherical factor `4π` absorbed).
6. *Spherical convolution.* For `F=G_a*p_{2ε}`: `T_ε(a,0)=c_Γ[p_{2ε}*(G_a*|·|^{−α})](0)≤c_Γ sup_z(G_a*|·|^{−α})(z)`.
7. *Exact kernel.* With `r=|z|`, `(G_a*|·|^{−α})(z)=[(a+r)^{2−α}−|a−r|^{2−α}]/(2r(2−α))`. I verified this publicly: `G_a` has mass `a`, i.e. surface density `1/(4πa)`; the surface integral `∫_{S(0,a)}|re_3−y|^{−α}dσ` equals `(2πa/r)[(a+r)^{2−α}−|a−r|^{2−α}]/(2−α)` via the substitution `u=cosθ`; dividing by `4πa` yields the displayed formula.
8. *Piecewise bounds.* `r<a/2`: minimum distance `≥a/2`, bound `2^α a^{1−α}`; `r>2a`: bound `a^{1−α}`; `a/2≤r≤2a`: numerator `≤(3a)^{2−α}`, denominator `2r(2−α)≥a(2−α)`, giving `3^{2−α}a^{1−α}/(2−α)`; endpoints by continuity (`r→0` limit is `a^{1−α}`). Sum into `b_α=2^α+3^{2−α}/(2−α)`, concluding `E:phase-trace`.
- Argument preservation: PRESERVED. New explanations: JUSTIFIED (roadmap + two-step split).
- Evidence: the resolvent constant uses the spectral mass `V=μ(B_1)`, the trace constant `D_Γ` uses the physical mass `M=Γ(B_1)`, kept distinct (statement: “physical mass M and spectral mass V are not identified”). Spherical formula verified by direct integration.
- Lost steps/qualifiers: none.

## P:static-phase-variance (ordinal 14)
- Global main ordinal: 14
- Old reading: COMPLETE. New reading: COMPLETE. Public reconstruction: COMPLETE.
- Original-step coverage (OLD 2396–2469; NEW 2635–2722; statement 2373–2394 vs 2612–2633 identical):

1. *Setup.* Unnormalized Plancherel `(2π)^{−3}dη`; integrability of `E:phase-duhamel` via `G_t` mass `t`, `C_t` `L²` contraction, and `E|W_ε(x)W_ε(y)|² ≤ 3Γ_ε(0)²`.
2. *Free Fourier coefficient.* `a_s(η)=ŵ_0(s,η)` and `e_λ(η)=|f̂|²+|ĝ|²/(λ²+|η|²)`; Cauchy–Schwarz over the two initial coordinates gives `|a_s(η)|²≤(1+λ²s²)e_λ(η)` since the coefficient-vector squared norm is `cos²(sq)+(1+λ²/q²)sin²(sq)≤1+λ²s²`.
3. *Output multiplier.* `k_τ(r)=(sin(τr)/r, cos(τr)/√(λ²+r²))` with `|k_τ(r)|²=(1+λ²sin²(τr)/r²)/(λ²+r²)≤(1+λ²h²)/(λ²+r²)`.
4. *Covariance–Plancherel.* `E‖Z_1(h)‖_λ²=(2π)^{−3}∫dη∫μ_ε(dξ)|∫_0^h k_{h−s}(|η+ξ|)a_s(η)ds|²`; Cauchy–Schwarz in time gives the squared norm `≤ h²(1+λ²h²)²e_λ(η)/(λ²+|η+ξ|²)`. Then `μ_ε≤μ` and `L:phase-contractions` give `E:phase-born` `R_α h²λ^{α−2}(1+λ²h²)²N²`, closing via `(2π)^{−3}∫e_λ dη = ‖f‖²+‖A_λ^{−1/2}g‖²=N²`.
5. *Mean.* The contraction in `E Z_2` is the convolution with kernel `G_{s−r}(dx)Γ_ε(x)`; Fourier multiplier `T_ε(s−r,η)`; operator norm `≤D_Γ(s−r)^{1−α}`. Under the isometry `(u,v)↦(u,A_λ^{−1/2}v)`, `‖k_τ(|D|)‖≤√(1+λ²h²)/λ` and `‖w_0(r)‖_2≤√(1+λ²h²)N`. Minkowski and `∫_0^h∫_0^s(s−r)^{1−α}dr ds=h^{3−α}/((2−α)(3−α))` give `E:phase-mean`.
6. *Free energy.* Differentiating squared phase norm, the `−Δ` terms cancel leaving `2λ² Re⟨A_λ^{−1}ẇ_0,w_0⟩`; by `A_λ≥λ²`, `|⟨A_λ^{−1}ẇ_0,w_0⟩|≤(2λ)^{−1}E`, so Gronwall gives `‖Z_0(h)‖_λ ≤ e^{λh/2}N`.
7. *Coefficient.* `K_ε=E‖Z_1(h)‖_λ²+2Re⟨Z_0(h), E Z_2(h)⟩_λ` (σ²-coefficient; the σ¹ cross with `Z_1` vanishes). With `λ=h^{−1}`: first term `4R_αh^{4−α}N²`; second `≤2·e^{1/2}N·(2D_Γh^{4−α}/((2−α)(3−α)))·N`, matching `E:phase-variance`.
- Argument preservation: PRESERVED. New explanations: JUSTIFIED (roadmap + three-step split).
- Evidence: all arithmetic on `h²λ^{α−2}(1+λ²h²)²` at `λ=h^{−1}`, the double time integral, and the derivative cancellation of `E` verified. The second term (second-order mean) is explicitly retained, matching `P:nogo-15`.
- Lost steps/qualifiers: none (the “first variance order only” scope restriction is preserved in both).

## L:complex-phase (ordinal 15)
- Global main ordinal: 15
- Old reading: COMPLETE. New reading: COMPLETE. Public reconstruction: COMPLETE.
- Original-step coverage (OLD 2522–2675; NEW 2775–2952; statement 2498–2520 vs 2751–2773 identical):

1. *Factorization and invertibility.* `L_λ+t=A_κ^{1/2}(1−zK_κ)A_κ^{1/2}`, `κ=√(λ²+t)`, `K_κ=A_κ^{−1/2}BA_κ^{−1/2}`. Since `a−2<0`, `‖zK_κ‖≤|z|dκ^{a−2}≤δ_a(κ/λ)^{a−2}≤δ<1`, so `‖A_κ^{1/2}(L_λ+t)^{−1}‖≤1/((1−δ)κ)` and `Re⟨L_λu,u⟩≥(1−δ)‖A_λ^{1/2}u‖²` (using `|z|≤δ_aλ^{2−a}/d` twice).
2. *Square-root comparison.* `w^{−1/2}=π^{−1}∫_0^∞t^{−1/2}(w+t)^{−1}dt` (Re w>0) gives `Q_z−1=π^{−1}∫t^{−1/2}A_λ^{1/2}[(L_λ+t)^{−1}−(A_λ+t)^{−1}]dt`. The resolvent identity and ordered factorization `A_λ^{1/2}A_κ^{−1/2}(1−zK_κ)^{−1}(zK_κ)A_κ^{−1/2}` have factor norms `1`, `1/(1−δ)`, `|z|dκ^{a−2}`, `κ^{−1}`, so the integrand is `≤(|z|d/(1−δ))κ^{a−3}`. Substituting `t=λ²s` yields `κ^{a−3}` integration `=λ^{a−2}I_a`, so `‖Q_z−1‖≤|z|dλ^{a−2}I_a/(π(1−δ))≤δ_a I_a/(π(1−δ))≤1/6` (since δ_a≤π/(8I_a), δ≤1/4). Hence `Q_z,Q_z^{−1}≤2`; applying to `L^*=A_0−z̄B` and taking adjoints gives all four `E:phase-root-comparisons` norms ≤2. (Comparison at bounded cutoffs, not a square-root domain identity.)
3. *Numerical range.* With `s=‖A_0^{1/2}u‖`: optimizing the sandwich at `ρ=s` gives `|⟨Bu,u⟩|≤2ds^a`; at `ρ=λ` gives `|⟨Bu,u⟩|≤dλ^{a−2}(s²+λ²)`, hence `|z⟨Bu,u⟩|≤δ(s²+λ²)`. For `w=x+iy`: `x+λ²≥(1−δ)(s²+λ²)`, `|y|≤2δλ^{2−a}s^a`. Then `s^{2a}λ^{2−2a}≤s²+λ²` (Young, `0<a<1`) gives `y²≤(4δ²/(1−δ))λ²(x+λ²)≤(1/3)λ²(x+λ²)` and `x≥−λ²/4`. The NEW addition: `|w|≤x+2λ²` reduces to `y²≤4λ²(x+λ²)` (verified: `x²+y²≤(x+2λ²)² ⇔ y²≤4λ²x+4λ⁴`), and `|Im√w|²=(|w|−x)/2` (verified: `√w=u+iv ⇒ w=u²−v²+2iuv ⇒ x=u²−v², |w|=u²+v²`), so `|Im√w|≤λ`.
4. *Scalar bounds.* On `W(L)`: `|cos(h√w)|,|sin(h√w)|≤e^{λh}` via `|Im√w|≤λ`; `sin(h√w)/√w=∫_0^h cos(r√w)dr ≤ he^{λh}` (entire, value `h` at `0`). For `F_h=√(w+λ²)sin(h√w)/√w`: if `|w|≤λ²/2`, `≤√(3/2)λh e^{λh}`; if `|w|>λ²/2`, `|w+λ²|≤3|w|` so `≤√3 e^{λh}`; hence `≤2(1+λh)e^{λh}`. For `H_h=√w sin(h√w)/√(w+λ²)`: `|w|/|w+λ²|≤1+λ²/|w+λ²|≤1+(1−δ)^{−1}≤7/3` (using `|w+λ²|≥x+λ²≥(1−δ)λ²`), so `|H_h|≤√(7/3)e^{λh}<2e^{λh}`. Applying `E:cp-input` (`1+√2<3`) gives operator bounds `3e^{λh}`, `6(1+λh)e^{λh}`, `6e^{λh}`. (Minor exposition note: the text writes the `7/3` ratio for `|w|/|w+λ²|`; the bound `2` follows after the square root `√(7/3)<2`, which is valid but not spelled out.)
5. *Phase blocks in noncommuting order.* Weighted blocks `C_h(L)`, `F_h(L)L_λ^{−1/2}A_λ^{1/2}`, `−A_λ^{−1/2}L_λ^{1/2}H_h(L)`, `A_λ^{−1/2}L_λ^{1/2}C_h(L)L_λ^{−1/2}A_λ^{1/2}` correspond to the matrix `(C_h, G_h; −LG_h, C_h)`, `G_h=sin(h√L)/√L`. Only functions of `L` commute; no commutation with `A_λ` is used. Block norms `3`, `12(1+λh)`, `12`, `12` times `e^{λh}`; sum `(39+12λh)e^{λh}≤39(1+λh)e^{λh}≤100e^{2λh}` (`max_{x≥0}(1+x)e^{−x}=1`, `39≤100`). The propagator is the exponential of the bounded block generator, entire in `z`; square roots are estimation devices only.
- Argument preservation: PRESERVED. New explanations: JUSTIFIED (the added `|w|≤x+2λ² ⇔ y²≤4λ²(x+λ²)` and `|Im√w|²=(|w|−x)/2` identities, plus `x≥−λ²/4`, are all correct and fill the one previously implicit step inside Step 2).
- Evidence: all numerical constants checked: `1/6` from `(π/(8I_a))·I_a/(π(3/4))=1/6`; `4δ²/(1−δ)≤1/3`; `1+(1−δ)^{−1}≤7/3`; CP factor `1+√2<3`; final `39≤100`. `E:abstract-sandwich`, `E:phase-root-comparisons`, `E:complex-phase-bound` unchanged.
- Lost steps/qualifiers: none. The self-adjointness of `A_0,B` and boundedness hypotheses are preserved; the `a∈(0,1)` hypothesis is used for `I_a<∞` (verified: exponent `(a−4)/2<−1`) and Young’s inequality.

## L:fock-form (ordinal 16)
- Global main ordinal: 16
- Old reading: COMPLETE. New reading: COMPLETE. Public reconstruction: COMPLETE.
- Original-step coverage (OLD 2702–2738; NEW 2979–3028; statement 2683–2700 vs 2960–2977 identical):

1. *Coordinates.* Orthonormal Gaussian basis, `e_i(x)=E[W_ε(x)g_i]`; `∑_ie_i(x)²=Γ_ε(0)=v_ε`, `|e_i(x)|≤√v_ε`; each `M_{e_i}` bounded selfadjoint. `H_i=A_ρ^{−1/2}M_{e_i}A_ρ^{−1/2}`.
2. *Column variance.* Gaussian isometry + Plancherel: `∑_i‖H_if‖²=(2π)^{−3}∫(|f̂(η)|²/(ρ²+|η|²))J_{ρ,ε}(η)dη` with `J_{ρ,ε}(η)=∫e^{−ε|ξ|²}μ(dξ)/(ρ²+|η+ξ|²)≤R_αρ^{α−2}` by `L:phase-contractions`. Hence `∑_iH_i²≤R_αρ^{α−4}I` in quadratic forms.
3. *Band compression.* For selfadjoint `H_i`, `(S_bH_iS_b)²≤S_bH_i²S_b`; the NEW addition makes this explicit: the difference `S_bH_i²S_b−(S_bH_iS_b)²=S_bH_i(I−S_b)H_iS_b=((I−S_b)H_iS_b)^*((I−S_b)H_iS_b)≥0`. Correct (verified by expanding `S_bH_iS_bH_iS_b`). Row and column variances agree by self-adjointness.
4. *Creation/annihilation.* `g_i=a_i^*+a_i`; normalized Hermite action `√(k_i+1)h_{k+e_i}+√(k_i)h_{k−e_i}`; creation row `v↦∑a_i^*v_i` has norm `√(k+1)` (since `RR^*=∑a_i^*a_i=(k+1)I` on degree `k+1`); annihilation is its adjoint. Composing with the spatial column (`≤√R_αρ^{(α−4)/2}`) and adding creation + annihilation on degree ≤N gives `2√(N+1)√R_αρ^{α/2−2}`, i.e. `E:fock-sandwich`. Boundedness of `−Δ` on `S_b` is explicit (multiplier `≤b²`).
- Argument preservation: PRESERVED. New explanations: JUSTIFIED (the compression-difference identity is correct and sourced to self-adjointness + `S_b`).
- Evidence: quadratic-form bound `R_αρ^{α−2}·∫|f̂|²/(ρ²+|η|²)/(2π)³=R_αρ^{α−4}‖f‖²`; `(α−4)/2=α/2−2`; `d_N` formula unchanged. Imported Janson used only for the Hermite normalization as stated.
- Lost steps/qualifiers: none.

## L:finite-word-cutoff (ordinal 17)
- Global main ordinal: 17
- Old reading: COMPLETE. New reading: COMPLETE. Public reconstruction: COMPLETE (this proof is byte-identical, no added material).
- Original-step coverage (OLD 2770–2786; NEW 3060–3076):

1. Hermite action of `M_{g_{ij}}` changes color-`i` total degree by exactly one (`±1`), leaving other colors unchanged; `I⊗F_l` preserves Gaussian degree.
2. After the first `l` insertions, color-`i` degree is `≤r_i(l)=|{j≤l:i_j=i}|≤r_i≤N_i`; induction from degree zero.
3. Hence the projection `P` acts as the identity before and after every insertion along the word, giving `E:finite-word-cutoff` by induction on `l`. The annihilation (lowering) term is retained, so creation-then-annihilation self-contractions are included.
4. Bochner-integral extension: equality of the vector integrands + linearity.
- Argument preservation: PRESERVED. New explanations: none (fully unchanged).
- Evidence: the combinatorial induction is self-contained and public; the statement’s qualifier “equality of selected finite words, not of full propagators at a fixed cutoff” is preserved.
- Lost steps/qualifiers: none.

## P:static-phase-all-orders (ordinal 18)
- Global main ordinal: 18
- Old reading: COMPLETE. New reading: COMPLETE. Public reconstruction: COMPLETE.
- Original-step coverage (OLD 2827–2903; NEW 3117–3211; statement 2797–2825 vs 3087–3115 identical):

1. *Zero case.* `R_α=0 ⇒ μ=0` ⇒ positive orders vanish.
2. *Cutoffs.* Finite `m` (modes), `N` (degree), `b` (band); `L:fock-form` + `L:complex-phase` with `a=α/2` give bound `100e^{2λh}` on the coupling circle of radius `δ_{α/2}λ^{2−α/2}/d_N`. Entries entire in coupling; Cauchy bounds the `n`-th coefficient by `100e^{2λh}(d_N/(δ_{α/2}λ^{2−α/2}))^n‖S_b(f,g)‖_λ`. The coefficient is the `n`-th Duhamel phase from the vacuum; `L:finite-word-cutoff` (one color, `N=n`, free waves as `F_l`) identifies cutoff and uncompressed words exactly (self-contractions included); dominated time integration preserves this.
3. *Scale choice.* `λ=n/h`; `‖z‖_{1/h}≤n‖z‖_{n/h}` (verified: `n²A_{1/h}−A_{n/h}=(n²−1)(−Δ)≥0 ⇒ A_{n/h}≤n²A_{1/h}`) and `‖(f,g)‖_{n/h}≤‖(f,g)‖_{1/h}`; `d_n≤2√(2n)√R_α`. `e^{2λh}=e^{2n}`, `λ^{−(2−α/2)n}=(h/n)^{(2−α/2)n}`, so `n^{−n(3−α)/2}` appears. With `100n≤200^n` and `n!≤n^n ⇒ n^{−(3−α)n/2}≤(n!)^{−(3−α)/2}`, get `E:all-static-phase-orders` with `A_α=400√2e²/δ_{α/2}` (factors verified: `200·2√2=400√2`).
4. *Cutoff removal.* Unweighted field multiplication on degree ≤N has norm `≤2√(N+1)√v_ε` uniformly in `m`; noise phase insertion bounded by that over `λ`; free evolution bounded by `e^{λh/2}`. `S_b→I` strongly, commutes with the free propagator ⇒ each word converges as `b→∞`; `m→∞` via finite-coordinate vectors (annihilation tail zero, creation tail `≤(∫∑_{i>m}e_i²‖F‖²dx)^{1/2}→0` by dominated convergence with `∑_ie_i²≤v_ε`), uniform bound extends strong convergence ⇒ limit is `Z_n^ε`, estimate survives. No zero-smoothing limit asserted.
5. *Summation.* `β=(3−α)/2∈(1/2,3/2)`. `∑x^n/(n!)^β≤2e^{3x^{1/β}}`: for `β≥1`, `∑(x^{n/β}/n!)^β≤(∑x^{n/β}/n!)^β=e^{βx^{1/β}}≤e^{3x^{1/β}}`; for `β<1`, Hölder factorizes `x^n/(n!)^β=((2x^{1/β})^n/n!)^β·(2^{−βn/(1−β)})^{1−β}` into factors with sums `e^{2x^{1/β}}` and `≤2` (since `β>1/2`). With `‖Z_0‖_{1/h}≤√e‖(f,g)‖_{1/h}`, absolute summation + squaring gives `E:all-static-phase-sum` (exponent `6A_α^{2/(3−α)}(|σ|²R_α)^{1/(3−α)}h^{(4−α)/(3−α)}`, since `1/β=2/(3−α)` and `x=A_α|σ|√R_αh^{(4−α)/2}`).
- Argument preservation: PRESERVED. New explanations: JUSTIFIED (roadmap + four-step split).
- Evidence: verified `n²A_{1/h}≥A_{n/h}`, `n^{−(3−α)n/2}≤(n!)^{−(3−α)/2}`, both Hölder branches, and the final exponent arithmetic. `A_α` unchanged between revisions; the `R_α>0` hypothesis is stated before `L:complex-phase` is invoked (so `d_n>0`).
- Lost steps/qualifiers: none; the explicit disclaimer “no zero-smoothing phase limit” is preserved.

## C:static-interaction (ordinal 19)
- Global main ordinal: 19
- Old reading: COMPLETE. New reading: COMPLETE. Public reconstruction: COMPLETE.
- Original-step coverage (OLD 2956–3019; NEW 3264–3341; statement 2908–2954 vs 3216–3262 identical):

1. *First variance coefficient.* `Y_n=S_0(−h)Z_n^ε`; `‖S_0(−h)‖_λ≤√e` (two-sided free estimate), `Y_0=(f,g)`. By `P:static-phase-variance`, the complete first coefficient is `≤L_α(h,λ)N²`: first random term `≤e·E:phase-born`, second mean term `≤2N√e·E:phase-mean`. At `λh≤1`, `(1+λ²h²)²≤4`, giving exactly `L_α=4eR_αh²λ^{α−2}+(4√eD_Γ/((2−α)(3−α)))h^{3−α}/λ`.
2. *Higher orders.* `‖Y_n‖_{L²(Ω;X_λ)}≤(√e/(λh))(A_α√R_α)^nh^{(4−α)n/2}/(n!)^{γ/2}·N`, `γ=3−α`. Verified comparison `‖z‖_λ≤(λh)^{−1}‖z‖_{1/h}` for `λh≤1` (from `A_λ≥(λh)²A_{1/h} ⇔ (1−λ²h²)(−Δ)≥0`) and `‖(f,g)‖_{1/h}≤‖(f,g)‖_λ=N`. Gaussian symmetry kills odd `r+s`; absolute convergence of double series. For `r+s=2k`, `r!s!≥(k!)²` gives diagonal sums `≤(e(2k+1)/(λh)²)(A_α²R_α)^kh^{(4−α)k}/(k!)^γ N²`, including edges `r=0` or `s=0` (`√e/(λh)≤e/(λh)²` since `λh≤1`, and `(2k)!≥(k!)²`). `e(2k+1)≤(3e)^k` controls `k≥2` by `(λh)^{−2}∑_{k≥2}x^k/(k!)^γ ≤ (λh)^{−2}x²e^{γx^{1/γ}}`, with `x=B_ασ²R_αh^{4−α}`, `B_α=3eA_α²`, and `∑x^j/(j!)^γ≤e^{γx^{1/γ}}` (`ℓ^γ⊂ℓ^1`). Keeping `k=1` separate proves `E:static-interaction`.
3. *Dyadic summability.* `β=4−α−α_0>2`. After `×T/h_j`: first term `c·Tλ^{α−2}h_j^{1−α_0}`; mean term `c·(T/λ)h_j^{2−α−α_0}`; higher `(T(B_αR_α)²/λ²)h_j^{2β−3}exp{γ(B_αR_α)^{1/γ}h_j^{β/γ}}` (using `x_j=B_αR_αh_j^β`). All powers positive (`1−α_0>0`, `2−α−α_0>0`, `2β−3>0`); exponential bounded at `h_0`; geometric in `2^{−j}` ⇒ `E:static-block-series`.
4. *Independent blocks.* `M_j(h_j)=S_0(h_j)I_j(h_j)`; `E:static-interaction` + `‖S_0(h_j)‖²≤e^{λh_j}` give bounded maps; tensoring with past space + density extends to independent random initial phases; iteration yields `∏e^{λh_j}(1+E_j)≤exp{λ∑h_j+∑E_j}` via `1+y≤e^y` ⇒ `E:independent-static-blocks`. Only the single-partition, independent-successive-block setting is claimed.
- Argument preservation: PRESERVED. New explanations: JUSTIFIED (roadmap + three-step split).
- Evidence: `L_α` assembled from `E:phase-born`/`E:phase-mean` with explicit factors `e,2N√e`; the `1/λh` comparison operator inequality verified; dyadic exponents verified; `γ>1` needed for `ℓ^γ⊂ℓ^1`.
- Lost steps/qualifiers: none; the non-identification with overlapping/repeated fields, and the `P:nogo-11` log-convexity disclaimer, are preserved.

## L:interval-contractions (ordinal 20)
- Global main ordinal: 20
- Old reading: COMPLETE. New reading: COMPLETE. Public reconstruction: COMPLETE.
- Original-step coverage (OLD 3084–3131; NEW 3406–3470; statement 3062–3082 vs 3384–3404 identical):

1. *Resolvent comparison in every d.* `μ(B_r)=r^αμ(B_1)`; the heat-comparison chain from `L:phase-contractions` uses no dimension-specific identity: `∫e^{−s|η+ξ|²}μ(dξ)=∫p_{2s}^{(d)}(x)e^{iηx}Γ(dx)≤∫e^{−s|ξ|²}μ(dξ)`. Integrating against `e^{−ρ²s}ds` and using radial homogeneity: `sup_η∫μ(dξ)/(ρ²+|η+ξ|²)≤R_αρ^{α−2}`. Dimension independence is real: `dμ_{rad}=αμ(B_1)r^{α−1}dr` and `∫_0^∞u^{α−1}/(1+u²)du=π/(2sin(πα/2))` carry no surface-area factor, so the same `R_α=απμ(B_1)/(2sin(πα/2))` holds for all `d`. No exclusion of a physical origin atom is used (the statement relaxes the “no origin atom” remark of `L:phase-contractions`).
2. *Column bound.* `Σ_m‖A_ρ^{−1/2}M_{e_m}f‖²=(2π)^{−d}∫|f̂(η)|²(∫e^{−ε|ξ|²}μ(dξ)/(ρ²+|η+ξ|²))dη ≤ R_αρ^{α−2}‖f‖²` ⇒ `E:interval-column`. Finite mode sums are positive sub-sums; `S_b` commutes with `A_ρ` and `S_bA_ρ^{−1}S_b≤A_ρ^{−1}` gives the same for `S_bM_{e_m}S_b`. New-color vacuum insertion: `‖Σ_mg_m(0,M_{e_m}u)‖²_{L²(Ω;X_ρ)} = Σ_m‖A_ρ^{−1/2}M_{e_m}u‖² ≤ R_αρ^{α−2}‖u‖² ≤ R_αρ^{α−2}‖(u,v)‖_ρ²`, hence insertion norm `≤√R_αρ^{(α−2)/2}`; input independent of this color.
3. *Finite-degree bound.* Substituting `A_ρ^{−1/2}f`: `Σ_m(A_ρ^{−1/2}M_{e_m}A_ρ^{−1/2})²≤R_αρ^{α−4}I`. Self-adjoint sandwiches: row/column variances equal. Creation row from degree `j→j+1` has norm `√(j+1)`; annihilation is its adjoint (as in `L:fock-form`); composing with the spatial column and adding both parts gives `2√(N+1)√R_αρ^{α/2−2}` ⇒ `E:interval-fock`. Positive operator identities tensor with any other Hilbert factor. Only `μ(B_1)`, homogeneity, nonnegativity used; no angular bound or unsmoothed multiplication norm absorbed.
- Argument preservation: PRESERVED. New explanations: JUSTIFIED (roadmap + three-step split).
- Evidence: dimension independence of `R_α` checked via radial `dμ`; `S_bA_ρ^{−1}S_b≤A_ρ^{−1}` checked as a form inequality; `(α−4)/2=α/2−2`; the `δ_0` white-noise case (`d=α=1`) is allowed by the section setup.
- Lost steps/qualifiers: none.

---

## Findings and limits

**Overall.** The NEW revision is a faithful readability rewrite of the ten assigned proofs. Statements, equation labels, hypotheses, and the mathematical deductions are unchanged; the transformations are (i) proof roadmaps, (ii) `Step k` headings and paragraph splits, and (iii) at most one added explanatory sentence per proof, in exactly three places: the `t^{2n}` measurability rescale in `P:mild-construction` (Step 2), the `|w|≤x+2λ² ⇔ y²≤4λ²(x+λ²)` and `|Im√w|²=(|w|−x)/2` derivation in `L:complex-phase` (Step 2), and the compression-difference identity in `L:fock-form` (Step 1). All three additions are mathematically correct.

**Reconstructed facts checked publicly.** In addition to the per-proof work above, the following cross-cutting items were verified and found intact: physical/spectral mass separation (`M=Γ(B_1)` vs `V=μ(B_1)`); the dimension-independent constant `R_α` coming from radial spectral mass with no surface factor; the noncommuting ordered root factors in `L:complex-phase` (only functions of `L` commute); the exact Hermite creation/annihilation pair `√(k_i+1),√(k_i)` with the lowering term retained for self-contractions; the full CP/Janson imports used only as quoted (CP with constant `1+√2<3`, Janson for the creation/annihilation normalization); and all factorial/exponent identities (`P_k`, `k!≤P_k≤2^kk!`, `(k/e)^k≤k!≤k^k`, `2k+1≤3^k`, `n!≤n^n`, the ℓ^β/ℓ^1 and Hölder series bounds, `β−ν=1−α_0>0`, `2β−3>0`).

**Boundary hypotheses.** The UNASSIGNED inputs were checked at their stated use sites only: `L:vertex-crude` supplies `q_n`/`E:vertex-summability` to `P:mild-construction`; `L:joint-fixed-order` supplies joint, arbitrary-relative-rate `L²` convergence; `L:damped-homogeneous-norms` supplies the three homogeneous norm scalings to `P:envelope`; `L:pairing-product-envelope` supplies the admissible product bound with `q_0+q_2/2=k`. Their internal proofs remain unassigned and are not counted here. `P:mixed` is cited for the majorant and the `L²` summability used in `P:envelope`; its hypothesis (Hypothesis `H:homog`) is respected.

**Minor non-defect notes (pre-existing, not introduced).** (1) In `L:complex-phase` Step 3, the bound `|H_h|≤2e^{λh}` follows from the stated `|w|/|w+λ²|≤7/3` only after the square root `√(7/3)<2`; the conclusion is valid but the intermediate step is implicit in both revisions. (2) In `P:mild-construction` Step 2 the phrase “time Jacobians and Green masses contribute `t^{2n}`” is a measured-scaling remark; a complete homogeneity identity would also involve spatial-measure and covariance factors, which are irrelevant to its measurability purpose. (3) The `L:complex-phase` statement restricts `A_0,B` to bounded operators; the application in `P:static-phase-all-orders` uses the band/mode/degree cutoffs to secure boundedness before the cutoff-removal step, as stated.

**Limitation.** This is a bounded readability/argument-preservation review of the ten assigned ordinals only. Full-book consistency, LaTeX rendering, Lean quotation, primary-source/PDF fidelity, and the proofs of the UNASSIGNED upstream lemmas are outside scope, as required. No step of the ten target proofs required material absent from the embedded context; no PARTIAL/UNCERTAIN reading was forced.

Final verdict: **PASS**, confidence **high**.
