# Review Result
Category: proof-readability-equivalence
Model: deepseek/deepseek-v4-pro
Verdict: PASS_WITH_NOTES
Confidence: high

The assigned block was read in full. Both OLD (LF 5658–7101) and NEW (LF 6324–7941) were compared proof-by-proof, including unchanged prose. The rewrite adds per-proof roadmap sentences and `\textit{Step n.}` headings but I found no deleted displayed equation, no weakened hypothesis, no strengthened conclusion, and no introduced arithmetic or logical defect. The caveats are external: several proofs' coefficient rates are imported from Chen–Hu (5.1)/(5.15) and Chen's variational finiteness theorem, and proof 50's fidelity to the source's (2.13)/(2.22)/(3.1)/(2.16) conventions is asserted with a self-contained Bochner/pathwise identification but cannot be checked against the cited article here; these are pre-existing imports, unchanged between OLD and NEW.

---

## L:static-holder-input
- Global main ordinal: 41
- Old reading: COMPLETE
- New reading: COMPLETE
- Public reconstruction: COMPLETE
- Original-step coverage: OLD proof has two logical stages: (i) static-input/paring identification; (ii) conversion of an upper coefficient rate into an all-order constant. NEW splits these into Step 1 and Step 2 with a two-sentence roadmap. All facts are retained.
- Argument preservation: PRESERVED
- New explanations: JUSTIFIED
- Evidence: Let `B_k(t)=Σ_{m=0}^{2k}E[U_mU_{2k-m}]` with `U_0=1`. The proof imports three external facts and checks their hypotheses: `γ_χ` has degree `1<χ<2<d`, hence Dalang's condition; Chen–Hu Thm 3.8(i) gives fixed-order `L²` existence; (2.17)+(2.19) identify `B_k` as the complete nonnegative sum over `2k+1` splits and all pairings (self-pairs included). Then (5.1) and (5.15) at `p=2` are quoted:
  `B_k(t)=t^{(4-χ)k}B_k(1)`, `limsup_{k→∞}(1/k)log((k!)^{3-χ}B_k(1))<∞`.
  The local deduction: choose `R` above the limsup; for `k≥k_0`, `B_k(1)≤e^{Rk}/(k!)^{3-χ}`; set `C_st=max(e^R, max_{1≤k<k_0}((k!)^{3-χ}B_k(1))^{1/k})`. Then `B_k(1)≤C_st^k/(k!)^{3-χ}` for all `k≥1`, and homogeneity gives `B_k(t)≤C_st^k t^{(4-χ)k}/(k!)^{3-χ}`. The finite-order `L²` property guarantees the finitely many pre-`k_0` values are finite.
- Lost steps/qualifiers: none. The `B_0=1` normalization and the "only finite upper rate used, no sharp constant" qualifier survive.
- Pre-existing concerns: the coefficient rate is imported, not proved here.

---

## P:static-holder-upper
- Global main ordinal: 42
- Old reading: COMPLETE
- New reading: COMPLETE
- Public reconstruction: COMPLETE
- Original-step coverage: OLD had five implicit stages: parameter verification; common regularized measure; low-endpoint bound; ordered removal of Green and noise regularization; power combination and series summation. NEW makes these explicit Steps 1–5 with a roadmap. Statement unchanged.
- Argument preservation: PRESERVED
- New explanations: JUSTIFIED
- Evidence:
  1. Parameters: `χ-1=(α-1)/(1-ϑ)>0`, `2-χ=(2-α-ϑ)/(1-ϑ)>0`, hence `1<χ<2`; and `α=ϑ+(1-ϑ)χ`, `α_0=ϑb_0`.
  2. Since `γ_α=|x|^{-α}=|x|^{-ϑ}|x|^{-(1-ϑ)χ}`, and `c=c^ϑc^{1-ϑ}`, Gaussian Hölder with the probability measure `p_{2ε}(z-x)dx` gives
     `γ_{α,2ε}(z)≤γ_{1,2ε}(z)^ϑ γ_{χ,2ε}(z)^{1-ϑ}`.
     The truncated temporal product satisfies `Q_δ≤T_{α_0}=∏_e|s_i-s_j|^{-α_0}=(∏_e|s_i-s_j|^{-b_0})^ϑ=T_{b_0}^ϑ`.
     Hölder on the common positive measure `ν_{k,t,η}` gives
     `A_k^{reg}≤(L_k^{reg})^ϑ(B_k^{reg})^{1-ϑ}` with `L=∫T_{b_0}H_1 dν`, `B=∫H_χ dν`.
  3. Low bound. Lemma L:alpha-one-convolution gives closing mass `πV_1/2` per pair; `k` closings contribute `(πV_1/2)^k`, `k` openings contribute `∏_O h_i≤(2t/k)^k` by AM–GM, so spatial `≤(πV_1)^k t^k/k^k`. Temporal pairing-sum symmetry over the full cube gives `2^k(Z_{b_0}t^{2-b_0})^k/k!`. Hence
     `L≤(2Z_{b_0}πV_1)^k t^{(3-b_0)k}/(k!k^k)≤C_low^k t^{(3-b_0)k}/(k!)^2`.
  4. Limits: `η↓0` first (weak Green convergence, dominated by `∏h_l`), then noise widths via `L²` fixed-order limits; product `L¹` inequality `‖YZ-Y'Z'‖_1≤‖Y-Y'‖_2‖Z‖_2+‖Y'‖_2‖Z-Z'‖_2`; then apply the static lemma only after limits.
  5. Powers: `2ϑ+(1-ϑ)(3-χ)=3-α`, `ϑ(3-b_0)+(1-ϑ)(4-χ)=4-α-α_0`; `Σz^k/(k!)^q≤e^{qz^{1/q}}` with `q=3-α>1`, `z=Ct^{4-α-α_0}`, `β/q=κ`.
- Lost steps/qualifiers: none. The "no monotonicity in ε, no uniform large-time static bound" warning and the explicit note that `L_k` is only a deterministic integral (not a mixed-regularization stochastic object) are retained.
- Pre-existing concerns: the `L_k` bound is borrowed from the unassigned proof of P:low-alpha-upper/L:alpha-one-convolution; its hypothesis (degree one, temporal `b_0<1`) is checked.

---

## L:planar-endpoints
- Global main ordinal: 43
- Old reading: COMPLETE
- New reading: COMPLETE
- Public reconstruction: COMPLETE
- Original-step coverage: OLD stages: polar measure; low-endpoint positive definiteness; static positive definiteness; wave convolution bound; regularized Hölder. NEW gives these as Steps 1–5. Statement unchanged.
- Argument preservation: PRESERVED
- New explanations: JUSTIFIED
- Evidence:
  - Polar measure. `Γ({0})=0` since `d-α=2-α>0`; with `σ(E)=(2-α)Γ{0<|x|≤1,x/|x|∈E}`,
    `Γ{a<|x|≤b, x/|x|∈E}=(b^{2-α}-a^{2-α})/(2-α)σ(E)=∫_a^b r^{1-α}dr σ(E)`,
    so `Γ` polarizes to `r^{1-α}dr σ(dω)`. Endpoints become `dr σ(dω)` and `r^{1-χ}dr σ(dω)`; finiteness near `0` uses `χ<2`, temperedness uses Schwartz decay.
  - Low positive-definiteness: `Γ_low=(1/2)∫_{S¹}∫_R f(rω)drσ(dω)`; for `ψ=φ*φ̃`,
    `∫_R ψ(rω)dr=∫_{ω^⊥}|∫_R φ(sω+v)ds|²dv≥0`; the `1/2` compensates the two orientations.
  - Static positive-definiteness: `|x|^{-λ}=Γ(λ/2)^{-1}∫s^{λ/2-1}e^{-s|x|²}ds`, `λ=χ-α>0`; each `e^{-s|x|²}Γ` is PD and `∫|ψ||x|^{-λ}dΓ=∫|ψ|dΓ_st<∞`; Tonelli/Fubini justify the mixture.
  - Convolution: with the planar density `G_h(y)=1_{|y|<h}/(2π√(h²-|y|²))`, `∫_R G_h(z-rω)dr=1/2` exactly if `|z·ω^⊥|<h`, else `0`; hence `(G_h*Γ_low)(z)=(1/4)∫1_{|z·ω^⊥|<h}dσ≤S/4`; Gaussian averaging preserves the bound, giving the stated `≤S/4`.
  - Hölder: `ϑ(α-1)+(1-ϑ)(α-χ)=0` when `ϑ=(χ-α)/(χ-1)`, so
    `(p_ε*Γ)(z)=∫p_ε(z-x)|x|^{ϑ(α-1)}|x|^{(1-ϑ)(α-χ)}dΓ≤(p_ε*Γ_low)^ϑ(p_ε*Γ_st)^{1-ϑ}`.
- Lost steps/qualifiers: none. The "no angular density or isotropy" clause survives.
- Pre-existing concerns: none material; `Γ` itself is assumed PD/even/tempered (a hypothesis of the lemma, not derived).

---

## L:planar-static-input
- Global main ordinal: 44
- Old reading: COMPLETE
- New reading: COMPLETE
- Public reconstruction: COMPLETE
- Original-step coverage: OLD: zero-covariance case; Dalang verification; imported finiteness input; rate-to-constant. NEW labels these Step 1–3 (Step 1 covers zero case and Dalang, Step 2 the imported finiteness, Step 3 the constant). Statement unchanged.
- Argument preservation: PRESERVED
- New explanations: JUSTIFIED
- Evidence: `Ξ(rA)=r^{2-χ}Ξ(A)` with `1<χ<2` gives spectral homogeneity `μ_Ξ(rA)=r^χμ_Ξ(A)`. With `B_R` balls,
  `∫(1+|ξ|²)^{-1}dμ_Ξ≤μ(B_1)+2^χ μ(B_1)Σ_{j≥0}2^{j(χ-2)}<∞`,
  since `χ<2`; this is Dalang. The proof then imports Thm 3.8(i) and (2.17)/(2.19) for finite nonnegative pairing sums, imports finiteness of the variational constant `M` (identifying `2^{χ/(4-χ)}M` with a Chen–Hu square-root quantity), and imports (5.1)+(5.15). The all-order constant is obtained exactly as in ordinal 41:
  `B_k(t)=t^{(4-χ)k}B_k(1)`, choose `R` above the limsup, enlarge `e^R` over the finitely many smaller `k`-th roots.
- Lost steps/qualifiers: none. The zero case (`Ξ=0 ⇒ B_k=0`, `C_st=1`) and the "general homogeneous covariance, not a Riesz specialization" qualification are retained.
- Pre-existing concerns: external coefficient rate imported.

---

## P:planar-upper
- Global main ordinal: 45
- Old reading: COMPLETE
- New reading: COMPLETE
- Public reconstruction: COMPLETE
- Original-step coverage: OLD: parameter/spectral verification; common measure + Hölder; low-endpoint estimate with explicit temporal count; noise limits; power combination and summation. NEW: identical content as Steps 1–5. Statement unchanged.
- Argument preservation: PRESERVED
- New explanations: JUSTIFIED
- Evidence:
  - Step 1: `χ-α=ϑ(α-1)/(1-ϑ)>0`, `2-χ=(2-α-ϑ)/(1-ϑ)>0`, so L:planar-endpoints applies with its interpolation weight equal to `ϑ`. The spectral condition for the time-dependent source follows from the dyadic sum with weight `(1+|ξ|²)^{-(2-α_0)/2}` because `α<2-α_0`.
  - Step 2: the common finite measure `ν_{k,t}` is defined over splits and `D∈Π_k` with spatial mass `∏h_l`; `H_Γ≤H_{Γ_low}^ϑ H_{Γ_st}^{1-ϑ}` from the planar lemma; Hölder gives `A_k^{ε,δ}≤(L_k^ε)^ϑ(B_k^ε)^{1-ϑ}`.
  - Step 3: closing bound `S/4` per pair and `∏_O h_i≤(2t/k)^k` give the spatial bound `(S/4)^k(2t/k)^k=(S/2)^k t^k/k^k`. The temporal sum is displayed explicitly:
    `Σ_{m,D}∫_{[0,t]^m_<×[0,t]^{2k-m}_<}T_{b_0}ds=(2k)!/(2^k k!)(Z_{b_0}t^{2-b_0})^k Σ_m 1/(m!(2k-m)!)`
    `=(2^k/k!)(Z_{b_0}t^{2-b_0})^k`.
    Multiplying: `L_k^ε≤(Z_{b_0}S)^k t^{(3-b_0)k}/(k!k^k)≤C_low^k t^{(3-b_0)k}/(k!)^2`.
  - Step 4: `L²` fixed-order limits (L:joint-fixed-order for target, Chen–Hu for static), product `L¹` convergence; limits passed.
  - Step 5: the standard two identities give the factorial exponent `3-α` and time exponent `4-α-α_0`; scalar `ℓ^q≤ℓ^1` series gives the exponential.
- Lost steps/qualifiers: none. The "symmetry used only for the pairing sum, not for an individual diagram" and "no interpolation of different temporal cutoff kernels" qualifications survive.
- Pre-existing concerns: the temporal binomial identity assumes ties have measure zero, stated.

---

## C:planar-range
- Global main ordinal: 46
- Old reading: COMPLETE
- New reading: COMPLETE
- Public reconstruction: COMPLETE
- Original-step coverage: a three-case corollary proof. Unchanged.
- Argument preservation: PRESERVED
- New explanations: JUSTIFIED (no substantive additions)
- Evidence: for `0<α≤1` use P:low-alpha-upper; for `1<α<2-α_0` use P:planar-upper; for vanishing covariance `u=1` with `C_dir=0`. Consumers at `α=1` are routed to the low-α proposition, avoiding overlap.
- Lost steps/qualifiers: none.

---

## L:product-endpoints
- Global main ordinal: 47
- Old reading: COMPLETE
- New reading: COMPLETE
- Public reconstruction: COMPLETE
- Original-step coverage: OLD: endpoint-interval construction; covariance properties; Gaussian Hölder. NEW labels these Steps 1–3. Statement unchanged.
- Argument preservation: PRESERVED
- New explanations: JUSTIFIED
- Evidence:
  - Endpoints: for a zero coordinate `L_j=U_j=0`. For `a_j>0`, `L_j<U_j` in both cases `a_j≥ϑ` and `a_j<ϑ`. With `I={j:L_j>0}`, `r=|I|`, `Σ L_j=(Σ_{I}a_j-r+rϑ)/ϑ<1`; for `r≥2`, `Σ_I a_j≤α<2-ϑ≤r-(r-1)ϑ` since `(r-2)(1-ϑ)≥0`. Also `Σ U_j>1` (either some `a_j≥ϑ` giving `U_j=1` plus another positive coordinate, or `ΣU_j=α/ϑ>1`). Hence `0<Λ<1` and `Σb_j=1`. The bounds `b_j<U_j≤a_j/ϑ` and `b_j>L_j≥(a_j-1+ϑ)/ϑ` give `0<v_j<1`; `Σv_j=(α-ϑ)/(1-ϑ)=χ`; `χ-α=ϑ(α-1)/(1-ϑ)>0`, `2-χ=(2-α-ϑ)/(1-ϑ)>0`.
  - Covariance: each active coordinate `0<e_j<1` gives local integrability `∫|u|^{-e_j}du<∞` and temperedness `∫|u|^{-e_j}(1+|u|)^{-N}du<∞` for `N>1`; the Gaussian-mixture `|u|^{-e_j}=Γ(e_j/2)^{-1}∫s^{e_j/2-1}e^{-su²}ds` proves positive definiteness (constant factor one at zero exponents).
  - Hölder: coordinatewise `a_j=ϑb_j+(1-ϑ)v_j` and common amplitude imply `γ_a=γ_b^ϑγ_v^{1-ϑ}` a.e.; Gaussian-probability Hölder gives the comparison; amplitude `c^ϑc^{1-ϑ}=c`.
- Lost steps/qualifiers: none.
- Pre-existing concern: values on coordinate planes are ignored via a.e. equality for locally integrable densities; legitimate because `e_j<1`.

---

## L:plane-endpoints
- Global main ordinal: 48
- Old reading: COMPLETE
- New reading: COMPLETE
- Public reconstruction: COMPLETE
- Original-step coverage: OLD: scaling check; positivity including normal Dirac; Hölder on the plane; spectral normalization. NEW labels these Steps 1–4. Statement unchanged.
- Argument preservation: PRESERVED
- New explanations: JUSTIFIED
- Evidence:
  - Scaling: `s=a_1+a_2=α-1∈(0,1)`; `0≤a_j<1`, `v_j<1`, `v_1+v_2=s/(1-ϑ)=χ-1<1`. A plane measure `f_e(y)dy δ_0(dz)` scales as `r^{2-e_1-e_2}`, so the three measures have exponents `3-α`, `2`, `3-χ`.
  - Positivity: the tangential density is a positive Gaussian mixture; for fixed `z` the quadratic form `∫∫f_e(y-y')φ(y,z)overline(φ(y',z))dydy'` is nonnegative by tangential Fourier positivity. Absolute Fubini via `A(u)≤C_N∏(1+|u_j|)^{-N}` and `N>1`.
  - Hölder: on the finite measure `p_ε(w-(y,z))m(dy,dz)` of mass `p_ε^{(1)}(w_3)`, `cf=c^ϑ(cf^{1/(1-ϑ)})^{1-ϑ}` with `f^{1/(1-ϑ)}=∏|y_j|^{-v_j}`.
  - Spectral mass: `μ_low=(c/2π)δ_0(ξ_1)δ_0(ξ_2)dξ_3` gives `V_low=c/π`, hence the closing bound `πV_low/2=c/2`.
- Lost steps/qualifiers: none. The "zero coordinate powers mean one" convention is preserved so the low endpoint `cm` is covered by the same positivity argument.
- Pre-existing concern: the `1/2π` normalization is tied to the stated spectral convention; consistent with the `d=1` white normalization in the embedded Remark R:low-alpha-scope.

---

## L:endpoint-closure
- Global main ordinal: 49
- Old reading: COMPLETE
- New reading: COMPLETE
- Public reconstruction: COMPLETE
- Original-step coverage: OLD: Gaussian-kernel extension; pushforward; finite sums. NEW labels these Steps 1–3.
- Argument preservation: PRESERVED
- New explanations: JUSTIFIED
- Evidence:
  - Gaussian extension: take `a<λ_min(Σ)`, `q_Σ=p_a*q_{Σ-aI}`; if `F_J=p_a*J`, then
    `q_Σ*Γ≤q_{Σ-aI}*(F_low^ϑ F_st^{1-ϑ})≤(q_Σ*Γ_low)^ϑ(q_Σ*Γ_st)^{1-ϑ}`
    by pointwise comparison (ε=a) and Gaussian-probability Hölder. Finiteness uses `|F_J(x)|≤F_J(0)<∞`.
  - Pushforward: `J_T=T_#J`, `d_T=|det T|`; `(φ*φ̃)(Ty)=d_T(ψ*ψ̃)(y)` with `ψ(y)=φ(Ty)`, so positive definiteness persists. With `Σ=εT^{-1}(T^{-1})^T`, `(p_ε*J_T)(x)=d_T^{-1}(q_Σ*J)(T^{-1}x)`; the two endpoint factors contribute `d_T^{-ϑ}d_T^{-(1-ϑ)}=d_T^{-1}`, exactly the target factor.
  - Finite sums: with `l_i=(p_ε*L_i)(x)`, `s_i=(p_ε*S_i)(x)`, discrete Hölder gives
    `p_ε*(Σw_iΓ_i)≤Σ(w_il_i)^ϑ(w_is_i)^{1-ϑ}≤(p_ε*Σw_iL_i)^ϑ(p_ε*Σw_iS_i)^{1-ϑ}`.
- Lost steps/qualifiers: none. The warning that pushforward does not preserve spectral/variational quantities under nonorthogonal maps is immediately after the lemma and unchanged.
- Pre-existing concerns: none.

---

## P:three-transfer
- Global main ordinal: 50
- Old reading: COMPLETE
- New reading: COMPLETE
- Public reconstruction: COMPLETE
- Original-step coverage: OLD: static input and coefficient bound; target hypotheses and common measure; deterministic low endpoint; static zero-Green-width identification; both inner Green limits; noise widths and all-time bound; precise asymptotic constant. NEW maps this to Steps 1–7. Statement unchanged.
- Argument preservation: PRESERVED
- New explanations: JUSTIFIED
- Evidence:
  1. Static input. `μ_Ξ(rA)=r^χμ_Ξ(A)`; the dyadic estimate gives `∫(1+|ξ|²)^{-1}dμ_Ξ<∞`; generalized covariances are covered by the source's (2.18) convention. Then (5.1)+(5.15) give `B_k(t)=t^{(4-χ)k}B_k(1)` and a finite rate; all-order constant `C_st` as in ordinal 41, stated as (E:three-static-coefficient).
  2. Target/common measure. Target spectral scaling exponent α and `α<2-α_0` give the time-dependent spectral condition; `H_Γ≤H_low^ϑ H_st^{1-ϑ}` and `Q_δ≤T_{b_0}^ϑ` imply `A_k^{ε,δ,η}≤(L_k^{ε,η})^ϑ(B_k^{ε,η})^{1-ϑ}` on `ν_{k,t,η}`.
  3. Low endpoint: `L≤C_low^k t^{(3-b_0)k}/(k!k^k)≤C_low^k t^{(3-b_0)k}/(k!)^2`, with `P_k=(2k)!/(2^k k!)` and `P_kΣ_m1/(m!(2k-m)!)=2^k/k!`.
  4. Static Green inner limit. `W_ε(x)=W^st(p_ε(x-·))` has covariance `p_{2ε}*Γ_st`, bounded continuous. The displayed increment bound
     `E|W_ε(x+h)-W_ε(x)|²≤|h|²∫|ξ|²e^{-ε|ξ|²}dμ_st`
     plus Gaussian moments and Kolmogorov in dimension three give a continuous modification. For `Φ_n(x)=∏W_ε(x_j)`, `‖Φ_n‖₂²≤P_n v_ε^n`. For the ordered Green measure `𝔤^0` with mass `ρ(1)<∞`, the pathwise vs Bochner agreement uses
     `∫E|Φ_n|dρ≤M_nρ(1)<∞`, `‖J_n‖₂≤∫‖Φ_n‖₂dρ≤M_nρ(1)`,
     and `E[YJ_n]=∫E[YΦ_n]dρ` for pathwise and Bochner integrals; taking `Y=J_n-U_n^{ε,0}` gives a.s. equality. This is identified with the source's `S_{n,ε}` under its (2.22)/(3.1) convention.
  5. Inner limits. Second and mixed `η/0` moments converge by weak Green-measure convergence against bounded continuous Gaussian-moment functions with dominating `const·∏h_l`; subtracting gives `L²` convergence in `η`. The target field `γ_δ^0(u)=Γ(α_0)^{-1}∫_0^{1/δ}e^{-λ|u|}λ^{α_0-1}dλ` has `γ_δ^0(0)=δ^{-α_0}/(α_0Γ(α_0))` and `γ_δ^0(0)-γ_δ^0(h)≤C_δ|h|`; joint increment variance bounded by `C(|h_0|+|h'|²)`, Gaussian 12th moment `≤C|h|^6`, Kolmogorov in dimension four; the Bochner/pathwise agreement for `X_n^{ε,δ,0}` is the same duality argument.
  6. Noise removal and sum. Fixed-order `L²` limits (L:joint-fixed-order and Chen–Hu Thm 3.8(i)); product `L¹` inequality; coefficient bound
     `A_k≤(C_low^k t^{(3-b_0)k}/(k!)^2)^ϑ·(C_st^k t^{(4-χ)k}/(k!)^{3-χ})^{1-ϑ}=C^k t^{βk}/(k!)^q`,
     using `2ϑ+(1-ϑ)(3-χ)=3-α` and `ϑ(3-b_0)+(1-ϑ)(4-χ)=4-α-α_0`; scalar series gives `E u²≤exp(qC^{1/q}t^κ)`.
  7. Precise asymptotic constant. The imported (5.15) rate reads
     `limsup_k((k!)^Q B_k(1))^{1/k}≤2^{-Q}2^{ν}(2√M_st/ν)^ν=Λ_st`
     with `Q=3-χ`, `ν=4-χ`, i.e. `Λ_st=2(2√M_st/(4-χ))^{4-χ}`. For `r>0` there is `N_r` with `B_k(1)≤(Λ_st+r)^k/(k!)^Q` for `k≥N_r`; homogeneity makes `N_r` independent of `t`. Inserting into the coefficient Hölder inequality gives `A_k(t)≤D_r^k t^{βk}/(k!)^q` for `k≥N_r`, `D_r=C_low^ϑ(Λ_st+r)^{1-ϑ}`. Low orders `k<N_r` are kept with `d_k=C_low^{ϑk}B_k(1)^{1-ϑ}/(k!)^{2ϑ}<∞`; `P_r(t)=1+Σ_{k<N_r}d_k t^{βk}` has `log P_r(t)/t^κ→0`. Hence `limsup t^{-κ}log E u²≤log2/t^κ+max(0,qD_r^{1/q})→qD_r^{1/q}`; let `r↓0`.
- Lost steps/qualifiers: none. Key preserved qualifications: `M_st` needs only finiteness for the all-time bound; the variational constant is not asserted sharp and is not substituted into the all-time exponential; low orders are retained so the asymptotic constant does not replace the all-time constant; zero static rate causes no division.
- Pre-existing concerns:
  (a) The coefficient-rate formula with exact constant `Λ_st` is imported from Chen–Hu (5.15) together with the variational finiteness of Chen Thm 1.1; only the local conversion to `A_k` and the limsup is derived here.
  (b) The identification of `𝔤_{n,t,x}^0` with the source's `μ_n^{t,x}` and of the integral with `S_{n,ε}` (step 4) depends on citations (2.13)/(2.22)/(3.1). The Bochner/pathwise equality is demonstrated, but the external numbering/conventions themselves are not embedded, so this alignment is a stated import.

---

## Findings and limits
All ten assigned proofs were read in complete OLD and NEW form, not by hash. The NEW revision is a readability rewrite: it introduces top-level roadmap paragraphs and `\textit{Step n.}` headings, and in proof 50 it partitions four previously continuous passages into Steps 4–7. Every displayed equation in the OLD block appears in the NEW block with the same labels and content; the parameter identities, temporal/symmetry counts, Hölder exponents, Green/Bochner limit identifications, and the asymptotic `Λ_st` argument are all retained. I reconstructed the substantive deductions publicly above: parameter inequalities; the `2ϑ+(1-ϑ)(3-χ)=3-α` and `ϑ(3-b_0)+(1-ϑ)(4-χ)=4-α-α_0` power balancing; the `(S/4)^k(2t/k)^k=(S/2)^kt^k/k^k` spatial bound and `P_kΣ_m1/(m!(2k-m)!)=2^k/k!` temporal count; the polar/line-integral and Gaussian-mixture positive-definiteness arguments; the pushforward determinant reconciliation `d_T^{-ϑ}d_T^{-(1-ϑ)}=d_T^{-1}`; and the `Λ_st` limsup conversion with retained low-order polynomial remainder.

No introduced defects were found in the added roadmap/headings. The verdict is PASS_WITH_NOTES only because the static coefficient rates and Chen's variational finiteness are external imports whose hypothesis checks are verified here but whose proofs are not embedded, and because proof 50's alignment with the source's internal approximations depends on cited definitions not provided in the context block. These are pre-existing aspects of the original proof, not changes introduced by the rewrite. Each target proof is judged argument-preserving under its stated hypotheses; the unassigned boundary energy lemma L:physical-spectral-energy is used only as supplied, at `χ<2` with Dalang's condition, and its proof is not counted as assigned completion.
