# Review Result
Category: proof-readability-equivalence
Model: deepseek/deepseek-v4-pro
Verdict: PASS
Confidence: high

All ten assigned proofs were read in both revisions in full. The NEW revision is a readability rewrite: it adds numbered step headings and short explanatory sentences, and in a few places supplies a one-line justification that was previously implicit. I found no introduced mathematical change and no lost step or qualifier. The derivations below are checked with public equations; where a target invokes an UNASSIGNED lemma I state the dependency and check its hypotheses, without counting that lemma's own proof as assigned completion.

Throughout, the standing parameters are `ν=3-α>1`, `β=4-α-α0>2`, `p=2-α0>1`, `κ=β/ν=(4-α-α0)/(3-α)`, so `β-ν=1-α0>0`.

## L:interval-complex
- Global main ordinal: 21
- Old reading: COMPLETE
- New reading: COMPLETE
- Public reconstruction: COMPLETE
- Original-step coverage:
  1. Adjoint sandwich: `Aρ^{-1/2}V^*Aρ^{-1/2}=(Aρ^{-1/2}VAρ^{-1/2})^*`, immediate since `Aρ` is selfadjoint.
  2. Resolvent identity. With `L=A0-V`, `L+Λ²+t=Aκ-V`, `Kκ=Aκ^{-1/2}VAκ^{-1/2}`,
     `(L+Λ²+t)^{-1}-Aκ^{-1}=Aκ^{-1/2}(1-Kκ)^{-1}Kκ Aκ^{-1/2}`.
     Left-multiplying by `AΛ^{1/2}` gives norm `≤ ∥AΛ^{1/2}Aκ^{-1/2}∥∥(1-Kκ)^{-1}∥∥Kκ∥∥Aκ^{-1/2}∥ ≤ Dκ^{a-3}/(1-δa)`, using `∥AΛ^{1/2}Aκ^{-1/2}∥≤1` (`Λ≤κ`), `∥Kκ∥≤Dκ^{a-2}≤δa`, `∥Aκ^{-1/2}∥≤κ^{-1}`.
  3. Root comparisons: `Q=AΛ^{1/2}LΛ^{-1/2}` satisfies `∥Q-I∥≤1/6`, then `∥Q∥≤7/6`, `∥Q^{-1}∥≤6/5`; the same applied to `L^*=A0-V^*` gives the four ordered comparisons, each at most `2`.
  4. Numerical range: for unit `u`, `s=∥A0^{1/2}u∥`, `⟨Lu,u⟩=x+iy`; evaluating the sandwich at `ρ=Λ` and `ρ=s` gives `|⟨Vu,u⟩|≤DΛ^{a-2}(s²+Λ²)` and `|⟨Vu,u⟩|≤2Ds^a`, hence `x+Λ²≥(1-δa)(s²+Λ²)` and `|y|≤2δaΛ^{2-a}s^a`. These feed the imported numerical-range parabola of `L:complex-phase`, yielding block norms `3e^{Λh}`, `12(1+Λh)e^{Λh}`, `12e^{Λh}`, `12e^{Λh}`, sum `≤100e^{2Λh}`.
  5. Metric count: for the phase norm, `∥z∥_{ρnew}≤max{1,ρold/ρnew}∥z∥_{ρold}`; at a cut with ending fields `E`, starting fields `S`, remaining `R`,
     `(λ+Σ_R ω+Σ_E ω)/(λ+Σ_R ω+Σ_S ω)≤1+Σ_E ω/λ≤∏_E(1+ω_i/λ)`.
     Each connected interval ends once, giving `E:interval-metric`.
- Argument preservation: PRESERVED. NEW only adds steps 1–3 heads and an introductory sentence.
- New explanations: JUSTIFIED. No added claim is incorrect.
- Evidence: the four inequalities above; the metric bound holds whether the weight increases (`≤1`) or decreases (`=old/new`), because the displayed product is `≥1`.
- Lost steps/qualifiers: none. The phrase "`Q^{-1}=LΛ^{1/2}AΛ^{-1/2}`" in the OLD/NEW text is mildly abbreviated relative to the ordered list in `E:phase-root-comparisons`, but all four comparisons are bounded by `2`, which is all that is used. Pre-existing wording, not introduced.

## L:inventory-product
- Global main ordinal: 22
- Old reading: COMPLETE
- New reading: COMPLETE
- Public reconstruction: COMPLETE
- Original-step coverage:
  1. Evaluation radius: at `z=θk^ν`, `θ=1/4`, with `P_i=θk^νi^{-β}`, `Q_i=θki^{-p}`. Since `ν+α-2=1`, the third singleton term is exactly `Q_i`; `1+A+B≤(1+A)(1+B)` separates the `1+Q_i` factors. For `p>1`, `Σ_{i≥1}log(1+Ai^{-p})≤∫0∞log(1+Ax^{-p})dx=A^{1/p}∫0∞log(1+x^{-p})dx≤Ck^{1/p}≤Ck`. NEW explicitly records the near-zero and infinity estimates: `log(1+x^{-p})≲C+p|log x|` at `0`, `≤x^{-p}` at `∞`.
  2. Coarse factors: for `i≤k` the second singleton term `θk^{ν-1}i^{-(β-1)}≤P_i` because `i/k≤1`, so the factor is dominated by `Sν(4P_i)=Σ_{l≥0}(4P_i)^l/(l!)^ν` using `(1+li/k)²≤(1+l)²≤4^l`. Then `Σ_{i≤k}log Sν(4P_i)≤ν(4θ)^{1/ν}kΣ_i i^{-β/ν}≤Ck` since `β/ν>1`. The bound `Σ x^l/(l!)^ν≤e^{νx^{1/ν}}` is the `ℓν`-vs-`ℓ1` inequality `(Σa_l)^ν≥Σa_l^ν`.
  3. Fine factors: for `i>k`, `P_i≤θ`, the singleton tail is
     `θ k^νΣ_{i>k}i^{-β}+θ k^{ν-1}Σ_{i>k}i^{-(β-1)}≤θ(1/(β-1)+1/(β-2))k^{ν+1-β}=Ck^{α0}`.
     The higher-degree sum obeys `Σ_{l≥2}P^l(1+ly)²/(l!)^ν≤CP²(1+y²)`, justified by `(1+ly)²≤2l²(1+y²)` and `P^l≤P²4^{-(l-2)}`. With `y=i/k`,
     `Ck^{2ν}(Σ_{i>k}i^{-2β}+k^{-2}Σ_{i>k}i^{2-2β}) = Ck^{2ν}(k^{1-2β}/(2β-1)+k^{-2}k^{3-2β}/(2β-3)) = Ck^{2α0-1}≤Ck`.
  4. Coefficient extraction: the product is `≤e^{Ck}`, so
     `[z^k]P≤P(θk^ν)/(θk^ν)^k≤θ^{-k}k^{-νk}e^{Ck}≤C^k/(k!)^ν`, using `k!≤k^k`, hence `k^{-νk}≤1/(k!)^ν`.
- Argument preservation: PRESERVED.
- New explanations: JUSTIFIED. The two derivation sentences added are correct.
- Evidence: the three clean estimates above; all exponents rely only on `β>2`, `β/ν>1`, `p>1`, `α0∈(0,1)`.
- Lost steps/qualifiers: none.

## L:fixed-split
- Global main ordinal: 23
- Old reading: COMPLETE
- New reading: COMPLETE
- Public reconstruction: COMPLETE
- Original-step coverage:
  1. Active sets. `I={i:k_i>0}`, `C={i:k_i=1,r_i=q_i=1}`, `B=I∖C`, `ℓ_i=1_{r_i>0}+1_{q_i>0}`. After discarding zero-length intersections, every active interval is `I_i^T=(a_i,b_i)` with positive length.
  2. Background radii: `a=α/2`, `ω_i=k_i/h_i`, `d_i=2√(2k_i+1)√Rα`, `ϱ_i=δaω_i^{2-a}/(σ_i d_i)`.
  3. Background sandwich: for `|z_i|=ϱ_i` on the background set `A`,
     `D(t)=Σ_{i∈A}|z_i|σ_i d_i 1_{I_i^T}(t)=δaΣ_{i∈A}ω_i^{2-a}1_{I_i^T}(t)≤δaΛ(t)^{2-a}`,
     using `Σx_i^{2-a}≤(Σx_i)^{2-a}` for `2-a>1`. This is the `L:interval-contractions` sandwich with identity on Gaussian factors.
  4. Segment product: the common partition has `M≤2|A|+m+1≤3k+1`. With `Λ_j` constant on each cell,
     `∏_j∥P_j∥_{H_{Λ_j}}≤100^Mexp(2Σ_jΛ_jΔt_j)≤100^{3k+1}e^{4k}=:M_k`,
     because `λT=k` and `ω_i(b_i-a_i)≤k_i`.
  5. Phase-metric product: `q_j=max{1,Λ_j/Λ_{j+1}}` bounds the identity norm by the spectral inequality `A_{Λ_{j+1}}^{-1}≤q_j²A_{Λ_j}^{-1}`. Each interval ends once, so
     `∏_{j=0}^M q_j≤D_A=∏_{i∈A}(1+k_i/(λh_i))`.
  6. Cross-color insertion: for `i∈C`, `J_i(u,w)=(0,σ_iB_iu)` maps `Z_S→Z_{S∪{i}}` (first Gaussian degree only). Orthonormality of `g_{ij}` and `E:interval-column` give
     `∥J_i(1_i⊗(u,w))∥²_{Hρ}=σ_i²Σ_j∥Aρ^{-1/2}S_bM_{e_{ij}}S_bu∥²≤σ_i²Rαρ^{α-2}∥u∥²≤σ_i²Rαρ^{α-2}∥1_i⊗(u,w)∥²`,
     so `∥J_i∥≤σ_i√Rα Λ(t_i)^{(α-2)/2}≤c_i=σ_i√Rαλ^{(α-2)/2}`, valid since `Λ≥λ` and `α-2<0`.
  7. Word bound: `∥W_A(z,t)v∥_λ≤(∏_j∥P_j∥)(∏_jq_j)(∏_{i∈C}c_i)∥v∥_λ≤M_kD_A∥v∥_λ∏_Cc_i`.
  8. Cube/Dyson: `Φ_A(z):=[∏_{i∈C}y_i]M^cut_{(z,y,0)}v=Σ_π∫_{D_π}W_A(z,t)v dt`, `Σ_π|D_π|=∏|I_i^T|≤∏h_i`; hence `∥Φ_A(z)∥_λ≤M_kD_A∥v∥_λ∏_Cc_ih_i`, with no `m!` factor.
  9. Vector Cauchy: normalized torus integral extracts
     `U_rv=(∏_{i∈A_r}ϱ_i^{-r_i})∫_{[0,2π]^{A_r}}e^{-iΣr_iθ_i}Φ_{A_r}((ϱ_ie^{iθ_i}))∏dθ_i/(2π)`;
     the angular measure has mass one, so `∥U_rv∥_λ≤∏_{A_r}ϱ_i^{-r_i}M_kD_{A_r}∥v∥∏_Cc_ih_i`.
  10. Pairing and constants: `∥w∥_{1/T}≤k∥w∥_λ`, `∥v∥_λ≤∥v∥_{1/T}`; Cauchy–Schwarz gives `E:split-before-absorption` with `r_i+q_i=2k_i` and `D_{A_r}D_{A_q}=∏_{i∈B}(1+k_i/(λh_i))^{ℓ_i}`. The radius factorial:
      `ϱ_i^{-2k_i}=(σ_i²d_i²/δa²)^{k_i}(h_i/k_i)^{(4-α)k_i}≤(12δa^{-2})^{k_i}(Rασ_i²h_i^{4-α})^{k_i}k_i^{-(3-α)k_i}≤(12δa^{-2})^{k_i}(Rασ_i²h_i^{4-α})^{k_i}/(k_i!)^{3-α}`,
      with `d_i²≤12k_iRα`. Finally `M_k²=100^{6k+2}e^{8k}≤(100^8e^8)^k` for `k≥1`, giving
      `C_split=100^8e^8 max{1,12δ_{α/2}^{-2}}`.
- Argument preservation: PRESERVED. NEW adds only step heads and an introductory roadmap sentence.
- New explanations: JUSTIFIED.
- Evidence: the ten displayed estimates above, all reproduce `E:fixed-split-bound`.
- Lost steps/qualifiers: none introduced. This proof is the heaviest; its use of `L:finite-word-cutoff`, `L:interval-complex`, and `L:interval-contractions` is stated at the correct hypotheses. The `c_i` bound intentionally charges the smaller `λ` rather than `Λ(t_i)`, which is a valid upper bound.

## P:interval-coefficients
- Global main ordinal: 24
- Old reading: COMPLETE
- New reading: COMPLETE
- Public reconstruction: COMPLETE
- Original-step coverage:
  1. Normalizations: null `σ_i` removed; `L≥1`; `σ_i>0` after `(σ_i,W_i)→(|σ_i|,sgn(σ_i)W_i)`, a law-preserving real Gaussian transformation.
  2. Entire majorant: with `v_max=sup_tΣ_iσ_i²1_{I_i}(t)Γε(0)`, multiplication on degrees `≤n` has norm `≤2√(n+1)√v_max`, free phase `≤e^{λh/2}`, insertion into `Xλ` costs `≤2√(n+1)√v_max/λ`, so order `n` is bounded by `e^{λT/2}(2z_*√(n+1)√v_maxT/λ)^n/n!∥v∥_λ`, an entire series. Vector Cauchy on the larger polydisc gives `∥U_rv∥≤K_{2z_*}(2z_*)^{-|r|}` and absolute-summable coefficient norms with finite factor `4^{|F|}K_{2z_*}^2`.
  3. Color splits: with `Q_{r,q}=⟨U_rv,U_qv⟩`, `E:interval-energy-splits` holds; reflection of color `i` multiplies by `(-1)^{r_i}`, so `Q_{r,q}=0` unless `r_i+q_i=2k_i`; number of splits `∏(2k_i+1)≤3^k`.
  4. Exact Hermite cutoff: `N_i=2k_i` preserves each selected word coefficient exactly by `L:finite-word-cutoff`, including creation-then-annihilation.
  5. Local weights from `L:fixed-split` after `σ_i²≤c h_i^{-α0}` and `λ=k/T`:
     `(2,0)/(0,2): Rαh^β(1+1/(λh))`; `(1,1): Rαλ^{α-2}h^{2-α0}`; `k_i=l≥2: Rα^lh^{βl}(1+l/(λh))²/(l!)^ν`.
     The monotonicity in `h` follows from the expansion
     `h^{βl}(1+l/(λh))²=h^{βl}+(2l/λ)h^{βl-1}+(l²/λ²)h^{βl-2}`, all powers positive since `β>2`. At `h=LT/i`, `1+l/(λh)=1+li/(kL)≤1+li/k` and `L`-powers are absorbed into `C`. Substitution extracts `C^kRα^kT^{βk}` and the inventory `v_i` at `k_i=1` and `b_{i,l}` at `k_i=l`.
  6. Summation identity `Σ_{Σk_i=k}∏w_{i,k_i}=[z^k]∏_i(Σ_lw_{i,l}z^l)` removes any multinomial factor; `L:inventory-product` gives `≤C^kRα^kT^{βk}/(k!)^ν`.
  7. Cutoff limits: mode/band limits and closed graph identification recover the smoothed model; the majorant is used only for identification, not as a uniform bound. The summation `Σ_kx^k/(k!)^ν≤e^{νx^{1/ν}}` (`ν>1`) gives `E:interval-phase-bound`.
- Argument preservation: PRESERVED. NEW adds a closed-graph sentence and renumbers into six steps.
- New explanations: JUSTIFIED.
- Evidence: the local-weight table and the length-substitution expansion above.
- Lost steps/qualifiers: none. The dependence of `v_max` on family and smoothing is explicitly quarantined from the uniform constant.

## L:terminal-wick
- Global main ordinal: 25
- Old reading: COMPLETE
- New reading: COMPLETE
- Public reconstruction: COMPLETE
- Original-step coverage:
  1. Chain mass: `M_0=1`, `M_n(T)=∫0^T(T-s)M_{n-1}(s)ds`, inducing `M_n(T)=T^{2n}/(2n)!`.
  2. Gaussian integrability: Hölder gives `∥∏_{j=1}^nW_j∥_2≤∏_j∥W_j∥_{2n}≤√((2n-1)!!)V^{n/2}`; with finite kernel mass this is Bochner integrability and `E:terminal-term-majorant`.
  3. Wick formula: expectation passes through the two finite kernel measures; differentiating the Gaussian MGF once per coordinate at zero gives a sum over unordered pair partitions with coefficient one per pairing. The `(2^kk!)` denominator cancels orientations/orderings. This yields `E:terminal-wick-formula` and `E:terminal-pairing-integral`.
  4. Symmetrization: averaging the `n!` pushforwards with weight `1/n!` leaves the symmetric field product unchanged, so there is no `n!` normalization factor and no `m!n!` in the two-chain product.
  5. Dimension-three Green limit: `p_η*G` has the same mass and weak limit; dominated convergence of bounded continuous finite Gaussian moments gives the same `L²` limit, the fixed-noise Green convention.
  6. Positivity/monotonicity: `K≥0` makes each covariance product nonnegative, so positive diagrams and moments compare entrywise. The ratio of successive majorants with `|r|^n` is `|r|√V T²/((2n+2)√(2n+1))→0`, giving absolute convergence for all complex `r`.
- Argument preservation: PRESERVED. NEW adds four step heads.
- New explanations: JUSTIFIED.
- Evidence: the recurrence and its closed form, plus the ratio test, are directly checkable.
- Lost steps/qualifiers: none. Both chain splits, self-pairings, unequal chains, and empty chain conventions are retained.

## L:uniform-series-tail
- Global main ordinal: 26
- Old reading: COMPLETE
- New reading: COMPLETE
- Public reconstruction: COMPLETE
- Original-step coverage:
  1. Nonnegative mixed moments imply the diagonal dominates: `E|u(r)|²≥r^{2n}E|Y_n|²`, so `r^{2n}E|Y_n|²≤B_r`.
  2. Fixed-order `L²` limit `Y_n→X_n` transfers `∥X_n∥₂≤B_r^{1/2}r^{-n}`.
  3. Geometric tails and triangle inequality give `E:uniform-series-tail`.
  4. Double limit: the distance between the two full series is at most
     `2B_r^{1/2}r^{-(N+1)}/(1-r^{-1})+∥Σ_{n=0}^N(Y_n-X_n)∥₂`;
     let `ε,δ↓0` at fixed `N`, then `N→∞`. This constructs the full regularized limit rather than assuming it.
  5. `L²`-norm continuity passes `B_1` to `u`.
- Argument preservation: PRESERVED (NEW is textually unchanged aside from the proof heading being identical; no new steps). 
- New explanations: JUSTIFIED (none added beyond the unchanged text).
- Evidence: the two displayed inequalities above.
- Lost steps/qualifiers: none.

## T:full-upper
- Global main ordinal: 27
- Old reading: COMPLETE
- New reading: COMPLETE
- Public reconstruction: COMPLETE
- Original-step coverage:
  1. Dyadic majorant. Three grids `h_j(n+(-1)^jt)`, `t=0,1/3,2/3`, `h_j=H_0 2^{-j}`, `6T≤H_0<12T`. Nesting: `m=2n+3(-1)^jt∈Z` since `3t∈Z`. For `s≠r` choose `3|s-r|<h_j≤6|s-r|`; boundary spacing `h_j/3>|s-r|` puts both points in one grid interval, so
     `|s-r|^{-α0}≤6^{α0}Σ_{three grids,|I|≤H_0}|I|^{-α0}1_I(s)1_I(r)=:K∞(s,r)`.
  2. Length inventory. At length `h_j`, at most `3(T/h_j+2)` intervals; the cumulative count through level `j` is bounded by `6T/h_j+6(j+1)≤6T/h_j+6·2^j≤78T/h_j`, giving `h_i≤78T/i`, so `L=78`, `c=6^{α0}`.
  3. Initial-data localization. For `f_T=1` on `B_{T+1}`, `supp f_T⊂B_{T+2}`, velocity zero, every chain point `(s,y)` ending at `x∈B_1` has `|y|+s≤|x|+T<T+1`, so the free initial-data factor is one. Termwise identification gives the constant-data model on `B_1`. NEW adds explicit definitions `W_{J,ε}`, `u_{J,ε}`, `u_{f_T,J,ε}` and the justification of the final inequality: `∥(f_T,0)∥_{1/T}²=∥f_T∥₂²≤|B_{T+2}|`. Stationarity gives `|B_1|E|u_{J,ε}(T,0)|²≤E∥u_{f_T,J,ε}(T)∥₂²≤e|B_{T+2}|exp{CRα^{1/ν}T^{β/ν}}`.
  4. Interval Wick sums. `E[W_{J,ε}(s,y)W_{J,ε}(r,z)]=K_J(s,r)Γε(y-z)`; `L:terminal-wick` applies and every covariance factor is `K_J(s_j,s_l)Γε(y_j-y_l)`, coefficient one, nonnegative diagrams.
  5. Positive diagram comparison. Source time covariance `γ_δ^0≤|s-r|^{-α0}≤K∞` pointwise; `K_J↑K∞` and nonnegative Tonelli at fixed `N` give
     `E|U_N^{ε,δ}(T,x)|²≤lim_J E|V_{N,J}^ε(T,x)|²≤sup_J E|u_{J,ε}(T,x)|²≤B(T)`.
     The text explicitly forbids reading this as covariance order for arbitrary initial phases: it is entrywise comparison of positive Wick integrals, and no Gaussian field of covariance `K∞Γε` is constructed.
  6. Scaled source bound. Amplitude `a>0` replaces `Γ` by `a²Γ`, `Rα` by `a²Rα`, giving `E|u^{ε,δ}(a;T,x)|²≤B(T;a)`.
  7. Regularization removal. `L:joint-fixed-order` gives `Y_n^{ε,δ}→X_n=S_n(g_n)` in `L²` at arbitrary rates; `L:uniform-series-tail` with `r=2`, `B_r=B(T;2)` gives absolute convergence of `u=ΣX_n` and `u^{ε,δ}(1)→u`; the limit at `a=1` proves `E:full-upper-bound`. The proof explicitly separates this from `P:mixed`, `L:crude-corrected`, the source's Section 5 proof, and any first-moment normalization; `P:mild-construction` only identifies the series as a mild solution and does not feed constants.
  8. Order of limits (NEW headings only renumber; content unchanged): coefficients uniform in cutoffs; mode/band limits at fixed smoothing; Green-width limit first, then `J→∞`, then `N→∞` by `L:terminal-wick`, then the uniform tail limit; no infinite-depth field and no simultaneous mode-depth limit; final bound uses `B(T;1)`, not `B(T;2)`.
- Argument preservation: PRESERVED.
- New explanations: JUSTIFIED. In particular the NEW Step 2 additions make the phase-bound-to-constant-data transfer explicit.
- Evidence: the nesting arithmetic, the `78T/h_j` inventory, the `K_J↑K∞` comparison, and the `r=2` tail application are all checkable as written.
- Lost steps/qualifiers: none introduced. Uses UNASSIGNED `L:joint-fixed-order`, `P:mild-construction`, `P:interval-coefficients`, `L:terminal-wick`, `L:uniform-series-tail` at their stated hypotheses. The theorem is genuinely independent-interval-field and positive-diagram comparison, not arbitrary-phase covariance order, matching the assignment's requirement.

## P:white-four
- Global main ordinal: 28
- Old reading: COMPLETE
- New reading: COMPLETE
- Public reconstruction: COMPLETE
- Original-step coverage:
  1. The area function `F(a,b,c)=4ab-(a+b-c)_+²+(|a-b|-c)_+²` is the area of `{|x|<a,|y|<b,|x-y|<c}`; spot-check `a=2,b=1,c=1` gives `F=4` and direct rectangle-minus-two-corners gives `8-4=4`.
  2. Spatial factors. The two white-noise deltas leave two free positions and an area divided by `16`. Position lists give:
     - `(0,4)`: `A:(x,x,y,y)` area `4ac`; `B:(x,y,x,y)` area `4a min(b,c,d)` (the `d` enters through the required increment to vertex 4); `C:(x,y,y,x)` area `4a min(b,d)`.
     - `(1,3)` with single vertex time `r` and long-chain gaps `a,b,c`: `A:(x,x,y,y)` area `4min(r,a)b`; `B:(x,y,x,y)` area `F(r,a,min(b,c))`; `C:(x,y,y,x)` area `F(r,a,c)`.
     - `(2,2)`: `A:(x,x),(y,y)` area `4ac`; `B:(x,y),(x,y)` area `4min(a,c)min(b,d)`; `C:(x,y),(y,x)` area `F(a,c,min(b,d))`.
  3. Time gaps read from the paired vertex times give the `q_1,q_2` columns exactly (e.g. `(0,4),B: q1=b+c`, `q2=c+d`).
  4. Delta integrations are justified by spatial approximate identity: each smoothed delta has mass one, so its paired-coordinate integral on `[-1,1]^2` is `≤2`; the four Green factors give spatial bound `2²/16=1/4`; time weights are integrable by the disjoint-pair bound used in `L:static-four`.
  5. Multiplicities: `J_{4,0,D}=J_{0,4,D}`, `J_{3,1,D}=J_{1,3,D}`, so the total order-four contribution is `2ΣJ_{0,4,D}+2ΣJ_{1,3,D}+ΣJ_{2,2,D}`.
  6. Scaling: `t^4` (time measure) `× t²` (area) `× t^{-2α0}` (two covariance factors) `=t^{6-2α0}`.
- Argument preservation: PRESERVED. NEW adds two step heads.
- New explanations: JUSTIFIED.
- Evidence: the per-row area computations and time-gap readings above.
- Lost steps/qualifiers: none.

## L:static-four
- Global main ordinal: 29
- Old reading: COMPLETE
- New reading: COMPLETE
- Public reconstruction: COMPLETE
- Original-step coverage:
  1. Dominated convergence: spatial factor `≤1/4`; for `0≤α0≤ā<1` the time factor is dominated by exponent `ā`, whose full-cube integral is
     `(∫0^1∫0^1|s-r|^{-ā}dsdr)²=(2/((1-ā)(2-ā)))²<∞`,
     since the two pairs use disjoint labels. So `α0=0` may be substituted.
  2. Time-slack reduction: for fixed free positions, integrating the time slacks first gives
     `J_{m,n,D}(1)|_{α0=0}=1/(16m!n!)∫(1-L1)_+^m(1-L2)_+^n dxdy`,
     where `L1,L2` are the chain lengths. The `(m,n)` length-pair table is verified (e.g. `(0,4),A: (0,|x|+w)`, `w=|x-y|`).
  3. Sector map: `(u,u+v)`, `(u+v,u)`, `(u,-v)` are determinant-one; the sector table entries follow from `∫_{u,v≥0}(1-pu-qv)_+^4dudv=1/(30pq)`. Spot-checks: `(0,4),B` in `0≤x≤y` is `∫(1-u-3v)_+^4=1/90`; `(1,3),A` is `∫(1-u)(1-u-3v)_+^3=1/24`.
  4. Summation: with factors `2/(16m!n!)` the row sums are `11/17280`, `143/34560`, `187/17280`; applying `E:total-four` gives `(2·11+2·143/2? )` precisely `11/540`, so static order-four is `11t^6/540`. Static order-two is `t³/3` by `L:white-test` at `α0=0`.
- Argument preservation: PRESERVED. NEW adds three step heads and splits the length-pair table into Step 2.
- New explanations: JUSTIFIED.
- Evidence: the three sector spot-checks and row-sum arithmetic above.
- Lost steps/qualifiers: none.

## P:riesz-small
- Global main ordinal: 30
- Old reading: COMPLETE
- New reading: COMPLETE
- Public reconstruction: COMPLETE
- Original-step coverage:
  1. Spatial two-point integral: for `d=1`, `G(s,y)=1/2 1_{|y|<s}`,
     `∫_{R²}G(s,y)G(r,z)cα|y-z|^{-α}dydz=cα((s+r)^{2-α}-|s-r|^{2-α})/(2(1-α)(2-α))`.
     This is checked at `α=0` (`=sr`) and is the one-dimensional form of the classical indicator-vs-`|·|^{-α}` integral `∫_{-s}^s∫_{-r}^r|y-z|^{-α}=2((s+r)^{2-α}-|s-r|^{2-α})/((1-α)(2-α))`.
  2. `E X1²`: integrate on `s>r`, double, set `v=s-r`; with `s+r=2r+v`,
     `E X1²=cα/((1-α)(2-α))∫0^t v^{-α0}[(2t-v)^{3-α}-v^{3-α}/(2(3-α))-(t-v)v^{2-α}]dv`,
     reproducing `E:riesz-two`.
  3. `E X2`: in initial-chain variables, increments `r,v` give spatial factor `cαrv^{1-α}/(1-α)`; the remaining integral is `cα/(1-α)∫_{r+v<t}rv^{1-α-α0}drdv`, and two elementary integrations give the displayed `cαt^β/((1-α)(2-α-α0)(3-α-α0)(4-α-α0))`.
  4. Order-four unit-domain formula: each spatial increment `h_lU_l` turns the Green factor `1/2 1_{[-h_l,h_l]}` into `h_l×` the uniform law; the triangular increment-to-position map has determinant one; hence `E:riesz-four`. Scaling all time and space by `t` gives `t^8` from eight integrations and `t^{-2α-2α0}` from two time plus two spatial covariance factors, i.e. `t^{2β}`.
  5. Finiteness: on `[0,1]^4×[-1,1]^4` with Green indicators dropped, the two time factors use disjoint label pairs and integrate since `α0<1`; the two spatial factors likewise use disjoint pairs and integrate since `α<1`; Tonelli gives a finite bound without numerical evaluation.
- Argument preservation: PRESERVED. NEW adds three step heads.
- New explanations: JUSTIFIED.
- Evidence: the direct integrals in items 1–3 and the scaling count in item 4.
- Lost steps/qualifiers: none.

## Findings and limits
- No introduced defect was found in any of the ten NEW proofs. The revision is a faithful step-labelling/explanation pass; every added sentence is mathematically correct and no qualifier has been dropped.
- The substantial reconstructions required by the task were performed: changing phase weights (21), the coefficient inventory product with the fine/coarse index split (22), the full fixed degree-split estimate including the cross-color subspace/Fock norm and radius factorial (23), the interval-coefficient weight conversion and no-multinomial summation (24), the terminal-chain Wick formula with coefficient-one pairings and mass `T^{2n}/(2n)!` (25), the scaled-moment remaining-tail double limit (26), the full all-model upper scale with genuine independent interval fields, positive-diagram domination, and explicit order of Green/time/cutoff limits (27), the three finite-order white/static/Riesz calculations (28–30).
- Imported facts used but not reproved (all UNASSIGNED, hypotheses checked): Crouzeix–Palencia in `L:complex-phase`, `L:finite-word-cutoff`, `L:interval-contractions`, `L:joint-fixed-order`, `P:mild-construction`, `L:white-test` for the static order-two value, and the `L:interval-contractions` column bound. Their own proofs are not part of the assigned completion and I did not use their conclusions as replacement for target deductions; the target steps above were independently reconstructed.
- Pre-existing minor wording, not introduced and not mathematically harmful: the ordering shorthand around `Q` and its inverse in (21), and the qualitative statement `G_s*f_T=s ⇒ C_sf_T=1` in (27), which is correct at its stated hypotheses via the wave propagator evaluated on a constant ball.
- No limitation prevented a complete public reconstruction of the ten assigned targets.

