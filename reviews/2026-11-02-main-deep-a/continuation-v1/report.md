# Review Result — deepseek

- category: paper-review-deepseek
- model: deepseek/deepseek-v4-pro
- verdict: PASS_WITH_NOTES
- confidence: HIGH

**Scope note (read with the verdict).** This is the bounded UnitA audit of PROOF037–041 and A01–A08 only, from the frozen embedded material. It does **not** clear: source-image/render verification, the full 213-proof/44-section/63-check main goal, the independent cold-read gate, or any legacy/composition credit. All five target proofs were checked by hand below; the residual items are scoped limitations, not proof defects.

---

## Critical findings

None in the five target proofs themselves. I computed every asserted constant, sign, factor ordering, endpoint, and integral; no false identity, wrong sign, wrong constant, or invalid limiting step was found.

---

## Noncritical findings

1. **Crouzeix–Palencia import is textual, not image-verified.** Statement (3) of the preprint and Theorem 6 (pp. 5–6, C_Ω ≤ 1+√2) are present in the embedded `crouzeix-v1.txt` excerpt and match the imported form `‖F(T)‖ ≤ (1+√2)sup_{W(T)}|F(w)|` for bounded T and F holomorphic on a neighborhood of the closure of W(T). This is the correct specialization, but no rendered page was inspected in this run (no image supplied).
2. **Root-comparison adjoint step is compressed.** The derivation of `L_λ^{-1/2}A_λ^{1/2}` and `A_λ^{-1/2}L_λ^{1/2}` bounds via “apply to L^* and take adjoints” is one sentence; I verified it explicitly (see PROOF039) but it is the most terse step in the five proofs.
3. **Hermite creation/annihilation row-norm facts are stated tersely.** “Row map norm √(k+1)” and annihilation adjointness in PROOF040 are standard second-quantization facts; they are asserted in one line each. I verified the underlying inequalities (see PROOF040), but an auditable expansion would help.
4. **Review-status meta-claims are unverifiable in this blind run.** The abstract and `\myCmts` comments state that component proofs “passed scoped independent reviews.” Those claims can only be checked against Progress/Review artifacts, which were deliberately excluded here. Recorded as limitation, not as an overclaim in the mathematics.
5. **Dimension scope.** PROOF037–038 (and hence 040–041) are stated in R³ with 0<α<2. The downstream interval section handles d∈{1,2,3} through a separate dimension-free re-derivation (L:interval-contractions), which was checked only for correct use of the targets, not given full downstream-proof clearance.

---

## Checked derivations

### PROOF037 — L:phase-contractions (lines 52–106)

- **Spectral homogeneity / no atom.** From Γ(cA)=c^{3−α}Γ(A) with Γ = ∫e^{iξx}μ(dξ), Fourier scaling gives μ(cξ)=c^{α−3}μ(ξ), hence μ(B_r)=r^α V with V=μ(B_1); α>0 gives μ({0})=0. Verified (the radial factor involves `c^α`, correct).
- **Resolvent comparison.** The Gaussian pairing ∫e^{−s|q+ξ|²}μ(dξ)=∫p_{2s}(x)e^{iqx}Γ(dx) uses p̂_{2s}=e^{−s|ξ|²}; evenness makes the middle integral real, nonnegativity of Γ gives ≤∫p_{2s}dΓ=∫e^{−s|ξ|²}μ(dξ). Multiplying by e^{−λ²s} and Tonelli gives ∫μ(dξ)/(λ²+|q+ξ|²) ≤ value at q=0. At q=0, layer-cake on μ(B_r)=Vr^α gives αV∫_0^∞r^{α−1}/(λ²+r²)dr. With ∫_0^∞ρ^{α−1}/(1+ρ²)dρ = π/(2 sin(πα/2)), this equals R_αλ^{α−2}, R_α=απV/(2sin(πα/2)). ✔
- **T_ε identity.** Fubini: T_ε(a,q) = ∫Γ_ε(x)e^{iqx}G_a(dx) = ∫μ(dξ)e^{−ε|ξ|²}Ĝ_a(q+ξ). ✔
- **Trace bound.** |T_ε(a,q)|≤T_ε(a,0) since Γ_εG_a is a finite nonnegative measure. Radial distribution Γ(B_r)=Mr^{3−α} (homogeneity only, no isotropy needed) plus layer-cake gives, for radial Schwartz F, ∫F dΓ=(3−α)M∫F(r)r^{2−α}dr = c_Γ∫F(x)|x|^{−α}dx with c_Γ=(3−α)M/(4π) (spherical factor 4π). With F=G_a*p_{2ε} radial: T_ε(a,0)≤c_Γ sup_z(G_a*|·|^{−α})(z).
- **Spherical convolution.** Direct polar integration with G_a=(4πa)^{−1}σ_a (mass a): (G_a*|·|^{−α})(z)=[(a+r)^{2−α}−|a−r|^{2−α}]/(2r(2−α)), r=|z|>0 — reproduced exactly. Region bounds r<a/2→2^α a^{1−α}, r>2a→a^{1−α}, a/2≤r≤2a→3^{2−α}a^{1−α}/(2−α); endpoints by continuity. Combining gives D_Γ=c_Γ(2^α+3^{2−α}/(2−α)). ✔

FULLY_CHECKED. No unresolved gap; no isotropy/density/translation-monotonicity assumption smuggled in.

### PROOF038 — P:static-phase-variance (lines 158–240)

- **Bochner/Fubini justification.** E|W_ε(x)W_ε(y)|²=E[W_ε(x)²W_ε(y)²]=Var_x·Var_y+2Cov² ≤3Γ_ε(0)² (Γ_ε(0) finite by temperedness); G_t has mass t, C_t is an L² contraction. Justifies the Gaussian/Fourier exchanges for Schwartz data, then extension by uniformity. ✔
- **Initial-coordinate factor.** a_s(η)=cos(sq)f̂+(sin(sq)/q)ĝ; Cauchy–Schwarz against (1,√(λ²+q²)/q) gives |a_s|²≤[cos²(sq)+(1+λ²/q²)sin²(sq)]e_λ=...[1+λ²sin²/q²]e_λ≤(1+λ²s²)e_λ. ✔
- **Output multiplier.** k_τ(r)=(sin(τr)/r, cos(τr)/√(λ²+r²)); |k_τ|²=(1+λ²sin²(τr)/r²)/(λ²+r²)≤(1+λ²h²)/(λ²+r²). ✔
- **Exact second moment.** Plancherel with cancellation δ(η+ξ−η′−ξ′): E‖Z_1(h)‖_λ²=(2π)^{−3}∫dη∫μ_ε(dξ)|∫_0^h k_{h−s}(|η+ξ|)a_s(η)ds|². ✔
- **Time Cauchy–Schwarz.** (∫|k|²ds)(∫|a_s|²ds) ≤ h(1+λ²h²)/(λ²+|η+ξ|²)·h(1+λ²h²)e_λ = h²(1+λ²h²)²e_λ/(λ²+|η+ξ|²). Using μ_ε≤μ and PROOF037 and (2π)^{−3}∫e_λ=N² gives **E:phase-born** R_αh²λ^{α−2}(1+λ²h²)²N². ✔
- **Mean of Z_2.** E[W_εW_ε]=Γ_ε so the contracted kernel is G_{s−r}(·)Γ_ε(·) with multiplier T_ε(s−r,η), L²-norm ≤D_Γ(s−r)^{1−α} (correct exponent). Under the isometry, ‖k_τ(|D|)‖≤√(1+λ²h²)/λ and ‖w_0(r)‖₂≤√(1+λ²h²)N. Minkowski plus ∫_0^h∫_0^s(s−r)^{1−α}drds=h^{3−α}/((2−α)(3−α)) gives **E:phase-mean**. ✔
- **Free-phase Gronwall.** d/dt‖Z_0‖²: the −Δ terms cancel exactly, leaving 2λ²Re⟨A_λ^{-1}ẇ_0,w_0⟩, bounded in absolute value by λ‖Z_0‖²; hence ‖Z_0(h)‖≤e^{λh/2}N. ✔
- **K_ε coefficient.** K_ε=E‖Z_1‖²+2Re⟨Z_0,EZ_2⟩ (E Z_1=0). At λ=h^{-1}: first term ≤4R_αh^{4−α}N²; cross term ≤2·√eN·2D_Γh^{4−α}N/((2−α)(3−α))=4√eD_Γh^{4−α}N²/((2−α)(3−α)). Both terms retained; no covariance monotonicity used. **E:phase-variance** ✔.

FULLY_CHECKED. Both variance and mean terms correct; the honesty paragraph correctly refuses to clear higher orders or G:upper.

### PROOF039 — L:complex-phase (lines 295–457)

- **Factorization.** L_λ+t=A_κ^{1/2}(1−zK_κ)A_κ^{1/2}, κ=(λ²+t)^{1/2}, K_κ=A_κ^{-1/2}BA_κ^{-1/2}; ‖zK_κ‖≤|z|dκ^{a−2}≤δλ^{2−a}κ^{a−2}≤δ (κ≥λ, a−2<0). ✔
- **Resolvent bound.** A_κ^{1/2}(L_λ+t)^{-1}=(1−zK_κ)^{-1}A_κ^{-1/2}, norm ≤1/((1−δ)κ). ✔
- **Form bound.** Re⟨L_λu,u⟩≥(1−δ)⟨A_λu,u⟩ since |⟨Bu,u⟩|≤dλ^{a−2}⟨A_λu,u⟩ and |z|d≤δλ^{2−a}. ✔
- **Inverse-root integral.** w^{−1/2}=π^{−1}∫t^{−1/2}(w+t)^{−1}dt gives Q_z−1=π^{−1}∫t^{−1/2}A_λ^{1/2}[(L_λ+t)^{−1}−A_κ^{-1}]dt (note A_λ+t=A_κ). Resolvent identity and the ordered four-factor decomposition A_λ^{1/2}A_κ^{-1/2}(1−zK_κ)^{-1}zK_κA_κ^{-1/2} give integrand ≤|z|d/(1−δ)·κ^{a−3}; scaling t=λ²u gives ‖Q_z−1‖≤|z|dλ^{a−2}I_a/(π(1−δ))≤δI_a/(π(1−δ)). With δ∈{1/4, π/(8I_a)}: δI_a/(π(1−δ))≤(1/8)·(4/3)=1/6. ✔ (t→0 integrable by t^{−1/2}; t→∞ integrable since (a−4)/2<−3/2 for 0<a<1.)
- **Four root comparisons.** Q_z=A_λ^{1/2}L_λ^{-1/2} and Q_z^{-1}=L_λ^{1/2}A_λ^{-1/2} both ≤2. Applying the same argument to L^*=A_0−z̄B: Q̃=A_λ^{1/2}(L_λ^*)^{-1/2}, Q̃^{-1}≤2; adjoints give L_λ^{-1/2}A_λ^{1/2}=Q̃^* and A_λ^{-1/2}L_λ^{1/2}=(Q̃^{-1})^*, both ≤2. All four ✔; explicitly not an assumed square-root domain identity.
- **Numerical range.** Optimized at ρ=s: |⟨Bu,u⟩|≤2ds^a (s=0 via ρ↓0). At ρ=λ: |z⟨Bu,u⟩|≤δ(s²+λ²). Hence for w=x+iy: x+λ²≥(1−δ)(s²+λ²), |y|≤2δλ^{2−a}s^a. From s^{2a}λ^{2−2a}≤s²+λ²: y²≤[4δ²/(1−δ)]λ²(x+λ²)≤(1/3)λ²(x+λ²), x≥−λ²/4. Then |w|≤x+2λ² (verified by squaring: difference (11/3)λ²(x+λ²)≥0) and |Im√w|≤λ (verified: forcing |v|>λ implies 4u²λ²≤(1/3)λ²u², contradiction). Only the w+λ² branch is needed (Re(w+λ²)≥(3/4)λ²>0); C_h,F_h,H_h are entire in w except the positive-real-part √(w+λ²); w=0 removable. ✔
- **Scalar bounds.** |C_h|≤e^{λh}; sin/√w=∫_0^hcos(r√w)dr gives ≤he^{λh}; |F_h|≤2(1+λh)e^{λh} (splits |w|≤λ²/2 → √(3/2)λhe^{λh}, |w|>λ²/2 → √3e^{λh}); |H_h|≤√(|w|/|w+λ²|)e^{λh}≤√(7/3)e^{λh}≤2e^{λh} using |w|/|w+λ²|≤1+(1−δ)^{-1}≤7/3. ✔
- **Crouzeix application.** (1+√2) times these gives 3e^{λh}, 6(1+λh)e^{λh}, 6e^{λh}. ✔
- **Four weighted blocks.** Top-left C_h(L); top-right F_h(L)L_λ^{-1/2}A_λ^{1/2}=G_h(L)A_λ^{1/2} (F_h(L)=L_λ^{1/2}G_h(L), functions of L commute); bottom-left −A_λ^{-1/2}L_λ^{1/2}H_h(L)=−A_λ^{-1/2}LG_h(L); bottom-right A_λ^{-1/2}L_λ^{1/2}C_h(L)L_λ^{-1/2}A_λ^{1/2}=A_λ^{-1/2}C_h(L)A_λ^{1/2}. Block norms 3, 12(1+λh), 12, 12 (times e^{λh}); no commutation with A_λ used. Sum 39+12λh≤39(1+λh)≤100e^{2λh}. ✔
- **Entireness.** M_z(h)=e^{h[[0,1],[−L,0]]} is entire in z; roots are auxiliary only. Constant independent of H,‖A_0‖,‖B‖. ✔

FULLY_CHECKED (with note 2 on the compressed adjoint step).

### PROOF040 — L:fock-form (lines 480–524)

- **ONB representation.** e_i(x)=E[W_ε(x)g_i], Σ_ie_i(x)²=Γ_ε(0)=v_ε, |e_i(x)|≤√v_ε ⇒ M_{e_i} bounded, selfadjoint. ✔
- **Plancherel identity.** With H_i=A_ρ^{-1/2}M_{e_i}A_ρ^{-1/2}, Gaussian isometry and spatial Plancherel give Σ_i‖H_if‖²=(2π)^{−3}∫|f̂(η)|²(ρ²+|η|²)^{−1}J_{ρ,ε}(η)dη with J_{ρ,ε}(η)=∫e^{−ε|ξ|²}μ(dξ)/(ρ²+|η+ξ|²). Verified by Σ_ie_i(x)e_i(y)=Γ_ε(x−y)=∫e^{iξ(x−y)}μ_ε(dξ) and the η→η+ξ shift. ✔
- **Column sum.** J≤R_αρ^{α−2} (μ_ε≤μ, PROOF037); then 1/(ρ²+|η|²)≤1/ρ² gives Σ_iH_i²≤R_αρ^{α−4}I in quadratic forms. Finite sub-sums inherit it; compression (S_bH_iS_b)²≤S_bH_i²S_b for selfadjoint H_i; row=column because H_i selfadjoint. ✔
- **Creation/annihilation.** g_i=a_i^*+a_i with normalized g_ih_k=√(k_i+1)h_{k+e_i}+√k_ih_{k−e_i}. Creation row: ‖Σ_iv_ia_i^*‖≤√(k+1)‖v‖ (since ⟨u,Σ_{i,j}v_iv_ja_ia_j^*u⟩≤‖v‖²(k+1)‖u‖²); composed with the spatial column √(Σ_i(S_bH_iS_b)²)≤√R_αρ^{(α−4)/2} gives creation part ≤√(k+1)√R_αρ^{(α−4)/2}. Annihilation is the adjoint, ≤√k·√R_αρ^{(α−4)/2}, **retained** (self-contractions included). Outputs at different degrees are orthogonal; sum over degrees ≤N gives ≤(√(N+1)+√N)S≤2√(N+1)√R_αρ^{α/2−2}=d_Nρ^{α/2−2}. Uniform in ε,m,b. ✔

FULLY_CHECKED (with note 3 on the terse standard Fock facts, which I verified).

### PROOF041 — L:finite-word-cutoff (lines 552–572)

Each M_{g_{ij}} changes color-i degree by exactly ±1 (annihilation term zero when a_{ij}=0), and I⊗F_l leaves all Gaussian degrees unchanged. Starting from the vacuum (degree 0 in every color), after l insertions the uncompressed word has color-i degree ≤ r_i(l)=#{j≤l: i_j=i} ≤ r_i ≤ N_i. Hence P is the identity both before and after every insertion along that fixed word; induction over l proves the displayed equality. The lowering (annihilation) term and creation-followed-by-annihilation self-contractions are retained. Bochner integrals follow by pointwise equality of vector integrands and linearity. The statement is correctly scoped to selected finite words from the vacuum, not full propagators at a fixed cutoff. ✔

FULLY_CHECKED.

---

## A01–A08 determinations

- **A01 — FULLY_CHECKED.** Fourier pairing, even/nonnegative Radon Γ, homogeneity ⇒ μ(B_r)=Vr^α with no atom, Tonelli, radial mass/R_α, sphere trace and radial convolution bound all verified; no isotropy/density/translation-monotonicity used (layer-cake, not radiality of Γ, gives Γ(B_r)=Mr^{3−α}).
- **A02 — FULLY_CHECKED.** Exact smoothed covariance/Fourier factors, both phase entries, Bochner/Fubini, time C–S constants, mean-contraction simplex integral h^{3−α}/((2−α)(3−α)), free Gronwall e^{λh/2}, and both K_ε terms (including the cross term) verified.
- **A03 — FULLY_CHECKED.** Ordered resolvent factor, norm-convergent holomorphic integral, t=0/∞ integrability for all 0<a<1, I_a scaling λ^{a−2}I_a, δ_a ⇒ 1/6, and all four root comparisons (including the L^*/adjoint route). No unbounded extension; no assumed square-root domain identity.
- **A04 — FULLY_CHECKED.** Numerical-range parabola, optimized s=0 (ρ↓0) case, |Im√w|≤λ, w=0 removable (functions entire in w except √(w+λ²) with Re>0), scalar bounds C/F/H = 1, 2(1+λh), 2 times e^{λh}, Crouzeix hypotheses (bounded T, holomorphic neighborhood of closure of W(T)) and prefactor (1+√2) matched to the embedded source (3) and Theorem 6.
- **A05 — FULLY_CHECKED.** All four weighted blocks verified with correct noncommuting factor order; only functions of L commute, never A_λ with L; block norms 3, 12(1+λh), 12, 12 ⇒ 39+12λh ≤ 39(1+λh) ≤ 100e^{2λh}; entire in z; downstream a=α/2∈(0,1) for α∈(0,2) and A_0=−Δ bounded on the spatial band.
- **A06 — FULLY_CHECKED.** Gaussian isometry/Plancherel identity, compression inequality, normalized creation **and** annihilation with degrees/adjoints (self-contractions retained; annihilation not omitted), selfadjoint boundedness, d_N=2√(N+1)√R_α uniform in ε,m,b. Row/column equality justified by selfadjointness; the underlying Fock row-norm inequality verified.
- **A07 — FULLY_CHECKED.** Prefix color-degree induction, deterministic F_l ordering, P identity before/after each insertion, normalized lowering/self-contractions retained, Bochner vector-integral equality; correctly limited to selected finite words from vacuum.
- **A08 — CHECKED / CONSISTENT (scoped).** Downstream uses a=α/2 (∈(0,1)), bounded A_0 on band, d_N as required; R_α=0 ⇒ μ=0 ⇒ all positive orders vanish (handled); h=0/zero-coupling trivial (M_z(0)=1≤100); scalar A_0=I,B=I admits d=sup_ρρ^{2−a}/(ρ²+1)<∞ (e.g. a=1/2, d=3^{3/4}/4); one-color two-insertion Hermite word reproduces creation+lowering within degree ≤2 with P identity. Suspect endpoints: a→0,1 keep I_a finite. The text explicitly disclaims zero-smoothing phase limits, uniform-noise, and full-propagator claims (lines 247, 989, 1135–1139) — no premature overclaim found.

---

## Target ledger (PROOF037–041)

| Target | Determination | Checked steps | Unresolved gaps / limit / constant notes |
|---|---|---|---|
| PROOF037 L:phase-contractions | FULLY_CHECKED | Homogeneity ⇒ μ(B_r)=Vr^α, no atom; Gaussian pairing + Tonelli ⇒ resolvent bound; q=0 exact R_α=απV/(2sin(πα/2)); T_ε identity via Fubini; layer-cake radial identity with c_Γ=(3−α)M/(4π); sphere convolution formula [(a+r)^{2−α}−|a−r|^{2−α}]/(2r(2−α)); region bounds ⇒ D_Γ=c_Γ(2^α+3^{2−α}/(2−α)) | None. α∈(0,2) required for finiteness of R_α and (2−α) denominators. |
| PROOF038 P:static-phase-variance | FULLY_CHECKED | Factor |a_s|²≤(1+λ²s²)e_λ; |k_τ|²≤(1+λ²h²)/(λ²+r²); exact second-moment Plancherel; time C–S; mean-contraction kernel T_ε(s−r,η) with ∫∫(s−r)^{1−α}=h^{3−α}/((2−α)(3−α)); Gronwall e^{λh/2}; K_ε both terms (variance **and** cross) ⇒ [4R_α+4√eD_Γ/((2−α)(3−α))]h^{4−α} | None. Bochner justified by E|WW|²≤3Γ_ε(0)². |
| PROOF039 L:complex-phase | FULLY_CHECKED | L_λ+t=A_κ^{1/2}(1−zK_κ)A_κ^{1/2}; ‖zK_κ‖≤δ; resolvent/ordered-factor integrand |z|dκ^{a−3}/(1−δ); Q_z−1 ≤δI_a/(π(1−δ))≤1/6; **all four** root comparisons ≤2 (Q_z real + L^*/adjoint); numerical-range parabola; scalar bounds 1, 2(1+λh), 2; Crouzeix ×(1+√2); four blocks 3, 12(1+λh), 12, 12 ⇒ 100e^{2λh} | Compressed adjoint step (verified by hand). Import is textual, not rendered. |
| PROOF040 L:fock-form | FULLY_CHECKED | ONB e_i(x)=E[W_εg_i], Σe_i²=v_ε; Σ_i‖H_if‖² Plancherel identity with J≤R_αρ^{α−2}; ΣH_i²≤R_αρ^{α−4}; compression; creation √(k+1), annihilation √k (retained); d_N=2√(N+1)√R_α | Standard Hermite row/column facts stated tersely (verified by hand). |
| PROOF041 L:finite-word-cutoff | FULLY_CHECKED | Prefix color-degree ≤r_i(l)≤r_i≤N_i induction; P identity before/after; lowering/self-contractions retained; Bochner via integrand equality | None. Correctly scoped to finite words from vacuum. |

---

## Required fixes before production gate

**For the five target proofs: none blocking.** The mathematics of PROOF037–041 is correct as verified by hand.

**Residual items that belong to the non-UnitA gates (recorded, not waived):**
1. Rendered-page/image verification of the Crouzeix–Palencia pages (1, 5–6) and Chen pages 7–8 remains open; this run is text-only and no image was supplied.
2. Reconciliation of the in-notes “passed scoped independent reviews” meta-claims against Progress/Review artifacts (excluded here).
3. Full 213-proof/44-section/63-check and final cold-read gates remain open; a favorable UnitA verdict must not be promoted to whole-project clearance.

---

## One-line summary

All five UnitA target proofs (PROOF037–041) and all eight risk checks (A01–A08) are mathematically correct under hand verification — no false identity, sign error, incorrect constant, or invalid limit found — but this is a scoped, text-only audit that does not clear source-image/whole-project/cold gates; verdict PASS_WITH_NOTES, confidence HIGH.