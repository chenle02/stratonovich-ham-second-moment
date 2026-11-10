# Unit H Independent Mathematical Audit (af97)

## 0. Scope, source identity, and operative rules

- **Manuscript audited:** af97ae4db921a660b0a4ed1ffbe9b6f53a487e2b.
- **Canonical H owner block:** 20 OWN deductions, `PROOF194`–`PROOF213`.
- **Canonical H declarations:** 23 = 20 OWN + 3 CONTEXT (`S067 Conj:allp`, `S069 G:sharp`, `S225 R:gram-controls`). `S064 H:homog` is a separate CONTEXT/logical-given model statement. The union used below is **24 = OWN20/CONTEXT4/EXTERNAL0**.
- **Guiding rule used:** a source location, stored status, author no-gap opinion, or a vote is **not** a proof. A scoped audit is **not** whole/image/cold acceptance. This report is an audit of the H20/24 scope only.

This is an analytical audit with no execution of Lean/HPC/numerical tools. All produced mathematics below is written work from the supplied current source modules; it does not claim to clear every upstream parent `A–G` chain.

---

## 1. Global model retention

The standing `H:homog` data is:

- `d ∈ {1,2,3}`, `0 < a = α₀ < 1`;
- `Γ` nonnegative, even, positive-definite, tempered Radon, homogeneous:
  `Γ(cA) = c^(d−α)Γ(A)`;
- allowed `0<α<d`, or `α=d=1` (spatial white noise), with `α+a<2`;
- data `(1,0)`;
- original covariance amplitude; no added angular density, no finite total spectral-mass assumption, no Hilbert-valued white vector, no `H³`-type extra hypothesis.

This is retained throughout. For `Γ=0`, `u≡1` and all positive-order terms/scores vanish; each relevant proof has a direct zero branch.

---

## 2. PROOF194 (S220): Gram scalar algebra

**Statement.** For `ℓ ∈ R`, `w>0`, `t≥0`:

```
2ℓ√t ≤ ℓ²/w + wt;
⟨Φ,z⟩ − ‖Φ‖²/2 = ‖z‖²/2 − ‖Φ−z‖²/2 ≤ ‖z‖²/2;
‖Σᵢ wᵢkᵢ‖² = Σᵢⱼ wᵢCᵢⱼwⱼ.
```

**WORK.** The first identity is the square

```
(ℓ/√w − √(wt))² = ℓ²/w + wt − 2ℓ√t ≥ 0,
```

valid at `t=0`. Equality for `ℓ,t>0` occurs at `w = ℓ/√t`.
The second is the Hilbert completion-of-square; the gradient form has the **half** `‖Φ‖²/2`, not `‖Φ‖²`.
The third is bilinearity. No covariance inverse, no compactness, no Hilbert-ball compactness used.

**Coverage:** WORKED; no defect found.

---

## 3. PROOF195 (S221): interior dual minimum

**Statement.** For nonempty eligible `A ⊆ J` (`Cᵢᵢ>0`), `D_A: wᵢ>0 → Σ ℓᵢ²/wᵢ − Σ bᵢwᵢ + ½Σ Cᵢⱼwᵢwⱼ` has a unique positive minimizer `w^A`, with stationarity

```
Σⱼ Cᵢⱼ wⱼ^A − bᵢ = ℓᵢ²/(wᵢ^A)² > 0.
```

**WORK.** Writing `cᵢ = Cᵢᵢ>0`, nonnegative entries give the **simultaneous** barrier/coercivity estimate

```
D_A(w) ≥ Σ ℓᵢ²/wᵢ + (1/4)Σ cᵢwᵢ² − Σ bᵢ²/cᵢ .
```

This blocks escape to any coordinate `0` **and** any coordinate `∞` from a single lower bound, so bounded sublevels lie in a compact box **strictly inside the positive orthant**. Continuity attains a minimizer.
The Hessian is

```
diag(2ℓᵢ²/wᵢ³) + C_A ,
```

strictly positive because its diagonal part is strictly positive and `C_A` is PSD — so the strict quadratic term survives **even if `C` is singular**. Differentiating at the interior minimum gives the stationarity display.

**Control.** The linear `−bᵢwᵢ` adds nothing to the Hessian; the strictness comes from the `ℓᵢ²/wᵢ` term, not from demanding an invertible Gram.

**Coverage:** WORKED; singular-Gram and zero-threshold behavior coherent.

---

## 4. PROOF196 (S223): positive conic optimizer

**Statement.**

```
𝒮(C) = max_{A⊆J} d_A^C .
```

A maximizing nonempty `A` is attained by `Φ_A = Σ_{i∈A} wᵢ^A kᵢ`, strictly positive coefficients; empty branch is `Φ=0`.

**WORK.**

1. For any `Φ`, put `A(Φ) = {i : ⟨Φ,kᵢ⟩ > bᵢ}` (strictly active). If empty, the objective is `−‖Φ‖²/2 ≤ 0`.
2. For nonempty `A(Φ)`, set `tᵢ = ⟨Φ,kᵢ⟩−bᵢ>0`, `z = Σ_{i∈A} wᵢkᵢ`. Using PROOF194,

```
F(Φ) ≤ Σ ℓᵢ²/wᵢ − Σ bᵢwᵢ + ⟨Φ,z⟩ − ‖Φ‖²/2 ≤ D_A(w),
```

so `F(Φ) ≤ d_A`.
3. Conversely `Φ_A` from the dual minimizer is exactly active on `A` and both scalar inequalities are equal on `A`; omitted labels add **nonnegative** roots; hence `F(Φ_A) ≥ d_A`.

Maximization over all subsets (including empty) closes the identity. This needs **no** primal concavity, **no** global dual concavity, **no** inverse Gram, **no** assumption that omitted labels are inactive, and **no** claimed uniqueness of the primal optimizer.

**Coverage:** WORKED.

---

## 5. PROOF197 (S222): real Gram realization

**Statement.** Every finite real symmetric PSD matrix is a Gram in a finite-dimensional real Hilbert space.

**WORK.** The Schur-complement induction is valid:

- Zero diagonal exactly forces the whole row/column to vanish (test `eᵢ+te_j`).
- Otherwise, with the leading diagonal `c>0`, the complement `B = A − vvᵀ/c` is PSD because of the test `(−vᵀy/c, y)`, **regardless of signs** of its entries.
- Assemble `k₁=(√c,0)`, `kᵢ = (vᵢ/√c, uᵢ)`.

No nonnegative-coordinate factorization, no complete positivity, no inverse of `C` is required.

**Coverage:** WORKED. Realization independence is correctly scoped: the dual max depends only on `C`, `ℓ`, `b`, and the eligible set, which is characterization-of-the-matrix, not a blanket claim for arbitrary non-PSD matrices.

---

## 6. PROOF198 (S224): entrywise optimized-value comparison

**Statement.** If `0 ≤ Cᵢⱼ ≤ Dᵢⱼ`, both PSD, same `ℓ,b`, then `𝒮(C) ≤ 𝒮(D)`.

**WORK.**

```
D_A^D(w) − D_A^C(w) = ½ Σ_{i,j∈A} wᵢ(D−C)ᵢⱼ wⱼ ≥ 0,
```

termwise by `wᵢ>0`. Infima and then maximization over the finite eligible families give the result. The eligible family **may grow** under `C≤D` (new nonzero diagonals). `D−C` need not be PSD; no same-`Φ` pointwise comparison and no covariance/Loewner order is used.

**Control not to confuse.** The companion `S225` example `D−C = [[1,1/2],[1/2,1]] − I₂` has spectrum `±1/2`, yet the optimized scales are `3·2^{-4/3}` and `(9/2)·6^{-2/3}` with the latter larger — this is an **optimized-value** comparison, not a Loewner order.

**Coverage:** WORKED.

---

## 7. S225 (R:gram-controls, CONTEXT, no attached proof)

**Role check.** This is a remark, not an OWN theorem. Its numerical statements are checked, with one correction of interpretation:

- `D(4) = −3199/400` is a **test value**, not the dual infimum. Compute
  ```
  D(w)=1/(100w)−4w+w²/2,
  D'(w)=w−4−1/(100w²),
  D'(4)=−1/1600,
  D'(6401/1600)>0,
  ```
  with `D''(w)=1+1/(50w³)>0`. Hence the dual minimizer lies **above** `4`, and values fall **below** `D(4)`; the **empty/origin** value `0` is the true finite value for `C=1,ℓ=1/10,b=4`.
- `k=ℓ=b=1`: on `φ≤1` the score is `−φ²/2≤0`; on `φ>1` the score is `2√(φ−1)−φ²/2`, whose maximum is at `φ≈1.4656`, with value `≈0.302` — so “nonconcavity/infinite right slope” refers to the fact that the root term is not concave in `Φ‖²`, not to a missing maximum.
- `k=ℓ=1,b=0`: max `3/2` at `φ=1`.
- “Doubling the cost” changes the objective from `−φ²/2` to `−φ²`; for `b=0,ℓ=1,k=1` the positive critical point is `2^{-2/3}` with value `3·2^{-4/3}`.

These finite arithmetic checks are **not** a replacement for analytic attainment or physical application, exactly as the source states.

**Role coverage:** CONTEXT — numerically checked, correct finite scope; no invented proof; no analytic/physical exemption granted.

---

## 8. PROOF199 (S227): positive raw embedding

**Statement.** `J_G: L²(I;G)→H_t⊗G` with

```
‖J_GF‖² = ∫I² K(s,t)⟨F(s),F(t)⟩_G ds dt ≤ K₀‖F‖²_{L²(I;G)},
K₀=2ᵃ/(1−a),
```

and for a smooth positive spacetime `Ψ`: `‖Ψ‖²_{H_I}=v_Ψ` and `𝒯_RΨ(s)=B_E(m_R h_{Ψ,s})`.

**WORK.**

- The row integral of `K(s,t)=|s−t|^{-a}` is
  `(s^{1-a}+(1-s)^{1-a})/(1-a) ≤ 2ᵃ/(1-a)`. Schur then gives the inclusion **without** defining a literal `Φ_t` for general `Φ`.
- Local Radon mass gives `‖q‖²_{H_sp} ≤ |B|Γ(B−B)‖q‖²∞` for compact-support `q`; separated common-support smooth approximations identify `J_{H_sp}Ψ` with the **original** raw class.
- Covariance inverse/Tonelli on the fixed smooth `Ψ` yields `‖Ψ‖²=v_Ψ` and the actual masked mean version simultaneously for all `R,s` for this one fixed smooth control.

**Coverage:** WORKED at its stated generic/fixed-control scope. No claim of rough `Φ_t`, no surjectivity, no raw/feature-class equality is inferred.

---

## 9. PROOF200 (S228): physical Gram labels

**Statement.** For `hᵢ = 1_{Iᵢ}/ℓᵢ`, real unit `C_c∞` profiles `fᵢ`, threshold `bᵢ = ‖∇fᵢ‖²`,
the raw labels are

```
kᵢ^R = hᵢ ⊗ (m_R fᵢ²),   kᵢ^∞ = hᵢ ⊗ fᵢ²,
```

satisfying the completed row

```
⟨Φ,kᵢ^R⟩_{H_I} = ℓᵢ^{-1} ∫_{Iᵢ} v_{𝒯_RΦ(s)}(fᵢ,fᵢ) ds,
```

and `0 ≤ C^Rᵢⱼ ≤ Dᵢⱼ` entrywise.

**WORK.**

- `hᵢ` is the **normalized time cell label**; the spatial multiplier is separate, with **exactly one** mask `m_R fᵢ²`.
- The dual E-state `(0,Λfᵢ)` cancels `Λ^{-1}`, leaving `m_R fᵢ²`; no Fourier normalization remains.
- `ℓᵢ` stays **outside** the square root in the score.
- Nonnegativity of `K`, `Γ`, and `0≤m_R≤1` gives entrywise `C^Rᵢⱼ ≤ Dᵢⱼ`; both matrices are PSD as actual Grams.

**Coverage:** WORKED, with normalization explicitly verified (`Σ ℓᵢhᵢ = 1`, not `1/2`).

---

## 10. PROOF201 (S229): uniform optimizer norm

**Statement.** With `C=C_mean`, `M = 4C+4`, `𝒮_R` may be restricted to `‖Φ‖≤M`, uniformly in `R`; every unmasked finite optimizer `Φ_D` has `‖Φ_D‖≤M`; positive smoothing follows.

**WORK.**

- The E-spectral/mean bound is used **before** any time averaging:
  `Rate_R(Φ) ≤ 1 + C‖Φ‖`.
- Therefore

```
2 Rate_R(Φ) − ‖Φ‖²/2 ≤ 2 + 2Cq − q²/2 < 0   (q>M),
```

while the zero control gives `0`. No previous `e_n`, no Jensen reversal, and no trial-gradient budget appears here.
- For a fixed finite family with covering plateau `R'`, Bochner cell averages `Wᵢ` and the norm-of-average estimate give

```
F_D(Φ) ≤ 2 Σᵢ ℓᵢ λ(Wᵢ) − q²/2
       ≤ 2 + 2 Σᵢ ℓᵢ‖Wᵢ‖ − q²/2
       ≤ 2 + 2Cq − q²/2.
```

- A nonnegative attained conic optimizer shares the same `M` ball independent of partition, gradients, and `R'`.
- Positive smoothing: on a nonzero branch, mollify the time indicators/cut off inside `I`; finite-tensor inclusion and `C_mean`-independent local bounds give raw convergence and rate/cost continuity. The zero branch uses `S₂^pos ≥ 0`.

**Coverage:** WORKED. This is a **physical** uniform budget, not an abstract Gram bound with a frozen `C_mean`.

---

## 11. PROOF202 (S230): signed score positive ceiling

**Statement.** `𝒮_R ≤ S₂^pos` for every `R`.

**WORK (order is essential).**

1. First, on the **whole** M-ball, `e_n→0` uniformly in `R` from scalar compactness of `C_t:H_t→L^r` plus the tensor norm bound (not tensor compactness).
2. Fix `n,R,Φ`; choose one near-Rayleigh real compact unit trial per cell with square-root error `ε`; weighted error is `2ε` because `Σℓᵢ=1`.
3. Compare **optimized** finite Gram values entrywise:

```
2 Rate_R(Φ) − ‖Φ‖²/2 ≤ 𝒮(C^R) + 2e_n + 2ε
                    ≤ 𝒮(D) + 2e_n + 2ε
                    = F_D(Φ_D) + 2e_n + 2ε.
```

4. Only now apply the **same** `e_n` estimate to `Φ_D`, whose norm is first bounded by `M` (PROOF201) and whose trial supports are covered by one `R'`.
5. Positive smoothing yields, on the positive branch,

```
F_D(Φ_D) ≤ 2 Rate_{R'}(Φ_D) − ‖Φ_D‖²/2 + 2e_n ≤ S₂^pos + 2e_n .
```

The form-order step `Rate_{R'}(Ψ)≤I_Ψ` is legitimate **only for the nonnegative smooth approximants**, not for arbitrary signed controls.

Hence the total error is `S₂^pos + 4e_n + 2ε`; send `ε→0`, then raw-ball supremum, then `n→∞`.

**Coverage:** WORKED in its exact limit order; the comparison remains a comparison of suprema, not a class identification.

---

## 12. PROOF203 (S231): cutoff removal for the possibly nonmonotone score family

**Statement.** `lim_{R→∞} 𝒮_R = S₂^pos`.

**WORK.**

- Fix one smooth positive `Ψ` **before** taking `R→∞`.
- For each fixed compact real unit `f`, `m_R=1` on its support for all large `R`; hence

```
liminf_R λ_R(s)² ≥ ∫ h_{Ψ,s}f² − ‖∇f‖² .
```

Compact-trial density and the unmasked Rayleigh identity give `λ_R(s)→λ_{Ψ,s}` pointwise.
- `sup_{s}h_{Ψ,s}<∞` gives domination; dominated convergence gives `Rate_R(Ψ)→I_Ψ`; cost `v_Ψ` is independent of `R`. Hence `liminf_R 𝒮_R ≥ 2I_Ψ−v_Ψ/2`.
- Choose a fixed near-optimizer before the liminf and use the PROOF202 ceiling for the reverse limsup.

No monotonicity of the **upper** mask family, no unmasked ground eigenfunction, no noisy unmasked limit, no R-dependent maximizing control is required.

**Coverage:** WORKED for the upper-family limit. The earlier monotone **lower** family in `P:variational-remove-mask` is a distinct numerical use and is not needed for this lemma.

---

## 13. PROOF204 (S226): intrinsic second-moment theorem

**Statement.**

```
lim_{T→∞} T^{-(4−α−a)/(3−α)} log E|u(T,x)|²
  = C₂(Γ,a) = S₂^pos = 2^{(4−α)/(3−α)}S₁^pos,
```

with the displayed full positive-control formula, kinetic coefficient one, and variance-half action.

**WORK (the source’s actual chain).**

- **Finiteness/gap structure.** The finiteness of `S₂^pos` is supplied by the independent full upper (051)-driven score construction `130/131/132`, **not** by `203/204`. The forward-source presentations of `051` are navigation, not premises.
- **Upper.** `193` gives the original point limsup in terms of the moving signed score `𝒮_{δ^{-1}+2}`; `203` shows the all-R limit exists, so the limsup equals `S₂^pos` without a `B(δ)` diagonal.
- **Lower.** `132` gives the point liminf lower bound `S₂^pos` for the **same canonical Stratonovich solution**.
- Both bounds concern exactly `Γ`, `a`, `u(T,x)`, self/unequal/empty chains, both phase entries, original amplitude, kinetic one, and `v_Ψ/2`.

**Zero covariance.** `H_I={0}`, all means/costs/rates/scores are zero, `u≡1`, `C₂=0`. No nondegenerate-Gaussian argument is needed.

**Coverage:** WORKED while explicitly conditioned on the actual `193/132/203` consumers being present, and on the point-transfer/source/upper-node identifications that feed them. This report **does not** independently re-derive that full source-to-point chain; it verifies the closure algebra and the consistency of the objects.

---

## 14. PROOF205 (S233): occupation raw square

**Statement.** A continuous map `Q:H¹(ℝᵈ)→H_sp` exists with `⟨Q(f),Q(h)⟩=B_Γ(f²,h²)`; for strongly-H¹ unit profiles `g_s`, `ρ_g = J_{H_sp}(s→Q(g_s))` satisfies `‖ρ_g‖²=A(g)` and `⟨Ψ,ρ_g⟩=∫h_{Ψ,s}g_s²`.

**WORK.**

- Approximate `f,h` by compact smooth and use the absolute four-linear estimate. The `H_sp` product is defined by completing those smooth pairings, not by multiplying distribution classes.
- `∫‖Q(g_s)‖²ds ≤ R_sp T(g)^{α/2}` uses concavity `∫b_s^{α/2} ≤ T(g)^{α/2}` and the smooth-ratio bound; hence `J_{H_sp}` is applicable.
- The `⟨Ψ,ρ_g⟩` identity is Tonelli on the **positive** physical integrand, with Lebesgue `x` integrated first for each displacement `z`. The raw-Hilbert Cauchy bound follows from `‖Ψ‖²=v_Ψ`.

**Coverage:** WORKED. No Gamma-null transfer from Lebesgue-null and no rough occupation inside a stochastic flow is asserted.

---

## 15. PROOF206 (S235): raw occupation energy and dilation

**Statement.** `0<C_occ≤K₀R_sp<∞`, and

```
ℰ_ζ^O = D_ζ C_occ^{2/(2−α)},
C_occ = ((2ℰ_ζ^O)/(2−α))^{(2−α)/2} (2ζ/α)^{α/2},
ℰ_ζ^O = ζ^{-α/(2−α)}ℰ₁^O.
```

**WORK.**

- Unit strong-H¹ profiles have `T(g)>0`; the raw (un-damped) kernel `K(s,t)=|s−t|^{-a}` is distinct from `K_*`.
- Unit-L²/`H¹`-invariant dilation `U_ℓ` gives exactly

```
A(U_ℓ g)=ℓ^α A(g),   T(U_ℓ g)=ℓ²T(g),
```

with **Radon** `ℓ^{α−d}` and **Lebesgue** `ℓ^{d}⋅ℓ^{-d}` factors kept separate.
- Differentiating `Aℓ^α − ζTℓ²` gives the explicit global maximum

```
D_ζ = ((2−α)/2)(α/(2ζ))^{α/(2−α)}.
```

No optimizer/minimax swap is used.

**Coverage:** WORKED.

---

## 16. PROOF207 (S234): countable Rayleigh near-occupation

**Statement.** For fixed smooth positive `Ψ` and `ε>0`, there is `g_ε ∈ O` with

```
I_Ψ² + T(g_ε) ≤ √(v_Ψ A(g_ε)) + ε.
```

**WORK.**

- Real separable `H¹` gives a countable dense **normalized** family. The `FIRST-index` Borel cells `A_j = U_j ∖ ∪_{i<j}Uᵢ` produce a strongly measurable selection without a continuum eigenstate selector or an optimizer.
- The pointwise bound `b(g_ε(s)) < ∫h_{Ψ,s}g_ε(s)² − λ_{Ψ,s}² + ε ≤ H_Ψ+ε` gives finite kinetic budget.
- Integrating the near-Rayleigh inequality and using PROOF205 gives the display; time Cauchy–Schwarz on unit `I` gives `I_Ψ²≤∫λ²`.

**Coverage:** WORKED. First-index measurability and finite kinetic budget are explicit; no selection theorem is hidden.

---

## 17. PROOF208 (S232): computed occupation ceiling

**Statement.**

```
S_c^pos ≤ c^m k [ α^{α/2}C_occ /(8 q^{q/2}) ]^{1/k}
       = c^m(2ζ)^{α/(2k)}F₀(ℰ_ζ^O),
k=3−α, q=4−α, m=q/k.
```

**WORK.**

- From PROOF207, with `v=v_Ψ`, `C=C_occ`, `β=α/4`:

```
I_Ψ² ≤ √(vC)T^β − T + ε   (some T>0).
```

Optimizing the scalar `√(vC)T^β − T` over `T≥0` and then `cDv^{1/q}−v/2` over `v≥0` gives exactly

```
cI − v/2 ≤ c^m k[ α^{α/2} C /(8 q^{q/2})]^{1/k}.
```

The `k+α=3` identity and the half-action/double-maximum chain are retained; the `(2ζ)^{α/(2k)}` factor cancels the raw-energy penalty scaling. `C₂=S₂^pos` is then identified **via PROOF204**, after which the ceiling is a bound on the actual moment constant.

**Coverage:** WORKED as a scalar double-maximization; **not** a numerical evaluation of `C₂`.

---

## 18. PROOF209 (S236): common spatial-energy bracket

**Statement.**

```
2^m M_a^{-1/k}F₀(ℰ_sp) ≤ C₂(Γ,a) ≤ 2^m K₀^{1/k}F₀(ℰ_sp),
```

and, for non-degenerate `Γ`,

```
C₂ ≤ 2^mF₀(ℰ_{1/2}^O) < 2^mF_a(ℰ_{1/2}^O).
```

**WORK.**

- Lower bracket is `S_c` lower score with the spatial energy; upper uses `C_occ≤K₀R_sp` and the algebraic conversion between `R_sp` and `ℰ_sp`.
- Strict log-gap uses

```
q−2a = (q−a)−a > 2−a > 1,
```

not `q≥3`.
- The `Δ = ½[q log q+(q−2a)log(q−2a)]−(q−a)log(q−a)>0` computation is elementary strict midpoint convexity of `x log x` for positive arguments.
- The `ζ=1/2` comparison and the `ζ=1` unfavorable example are **bound comparisons**; the exact finite control

```
α=5/4, a=1/2:  8[Δ−(α/2)log2] = log(11^11·7^7/(2^5·9^18)) < 0
```

is a comparison of own computed bounds, explicitly not an actual moment/source refutation.

**Coverage:** WORKED with that explicitly delimited interpretation.

---

## 19. PROOF210 (S238): full-profile CDF square

**Statement.** For every real unit `f∈H¹(ℝ)`, `A=∫f⁴<∞`; with `F(x)=∫_{-∞}^xρ`, for all real `z`,

```
∫[f'− zf(1−2F)]² = b −2zA + z²/3.
```

**WORK.**

- Local absolute continuity of the weak derivative, `ρ=f²`, `ρ'=2ff'∈L¹`, zero tail limits, and `∫ρ=1` give a locally AC, limits-zero representative.
- `F'=ρ`, endpoints `0,1`, integration by parts gives `∫f'f(1−2F)=A` and `∫f²(1−2F)²=1/3` via `P(y)=y−2y²+(4/3)y³` with `P(1)−P(0)=1/3`.
- Expanding the display gives the polynomial `b−2zA+z²/3`.

No positivity of `f` and no strict increase of `F` is needed; profiles with sign changes are included. Substitution `z=3A` gives `3A²≤b`.

**Coverage:** WORKED for all real `H¹` profiles.

---

## 20. PROOF211 (S239): exact white spatial energy

**Statement.** For `Γ=cδ₀`, `R_sp=c/√3`, `ℰ_sp=c²/6`; both zero at `c=0`.

**WORK.**

- From `3A²≤b`, Cauchy gives `(cA−b/2) ≤ c²/6 − (3/2)(A−c/3)²`, hence upper bound.
- The normalized sech profile `f_ℓ=√(ℓ/2)sech(ℓx)` has `‖f_ℓ‖₂²=1`, `A=ℓ/3`, `b=ℓ²/3`; choosing `ℓ=c` (or taking `ℓ↓0` for `c=0` with a dilated unit profile, never a zero unit vector) attains `c²/6`.
- The sech is an **energy profile**; compactness is supplied by density through `P:spatial-four-linear`, not by claiming the noncompact sech is itself a compact spacetime control.

**Coverage:** WORKED.

---

## 21. PROOF212 (S237): white moment bounds

**Statement.**

```
(2/3)√(c/M_a) ≤ C₂(c,a) ≤ (2/3)√(c K₀(a)),
K₀(a)=2ᵃ/(1−a),
M_a=Γ_E((1+a)/2)/[Γ_E(1+a)Γ_E((1−a)/2)].
```

**WORK.**

- Here `q=3,k=2,m=3/2`; `F₀(z)=2[(2z)^{1/2}/(8·3^{3/2})]^{1/2}`.
- `√(2ℰ_sp)=c/√3`, so `F₀(ℰ_sp)=√c/(3√2)` and `2^mF₀=(2/3)√c`.
- Substituting the PROOF209 bracket yields the display with `√c`; the exponent is `(3−a)/2`.
- These are **bounds**, not a numerical evaluation of the intrinsic supremum.

**Coverage:** WORKED.

---

## 22. PROOF213 (S240): white relative width

**Statement.** For `c>0`, the ratio of upper/lower bound formulas is `√(K₀(a)M_a) ≤ [√π/(2Γ_E(5/4)²)]^{1/2}`, equality at `a=1/2`.

**WORK.**

- Gamma duplication handles the denominator exactly;
- with `x=1+a/2`, `y=(3−a)/2`, `x+y=5/2`, Euler’s integral Cauchy–Schwarz bounds `Γ_E(x)Γ_E(y) ≥ Γ_E(5/4)²`.
- Only the **ratio of the two bound formulas** is symmetric under `a↔1−a`, not the moment constant, not C2, not the clock.

**Coverage:** WORKED.

---

## 23. Declaration-role audit (24 roles)

| Role | Kind | Attached proof | Audit disposition |
|---|---:|---|---|
| `PROOF194`–`PROOF213` (S220–S240 with irregular formal order) | OWN | yes | Audited above; no invented context proof |
| `S067 Conj:allp` (main) | CONTEXT/conjecture | none | **Ratified as conjecture/comparison**; not a proved all-p or actual-`p1` result; no forced Chen target |
| `S069 G:sharp` (main) | CONTEXT/goal | none | **Ratified as full-domain/amplitude/kinetic/action original goal**; presence does **not** accept `204` or shut whole/cold gates |
| `S225 R:gram-controls` (positive_gram) | CONTEXT/remark | none | **Finite arithmetic and conditional-certificate boundaries** checked; `D(4)` interpreted only as a test value; no fabricated proof |
| `S064 H:homog` (main, external owner A) | CONTEXT/hypothesis, logical given | none | Original model retained as **given**; not a “24th canonical H declaration”; no proof needed |

Each context receives only its actual role; no cross-file proof was invented.

---

## 24. JOIN-POSITIVE-INTRINSIC

**Consumed chain to verify.**

- **Finite Gram layer (`194–198`).** Real nonnegative PSD Gram, empty/singular branches, exact `‖Φ‖²/2`, active-set dual; optimized-value entrywise comparison. **Present and verified at the finite layer.**
- **Continuum labels (`199–200`).** A fixed smooth control joins the original raw class with cost `v`; physical finite families yield normalized cell row `m_R fᵢ²` and entrywise Gram order. **Present and verified.**
- **Uniform budget/positive smoothing (`201–202`).** `M=4C_mean+4` before a second averaging; fixed finite near-trials; optimized Gram comparison; positive smoothing **only** for nonnegative means; `4e_n+2ε` in the stated order. **Present and verified.**
- **Cutoff limit (`203`).** Fixed positive near-test before `R`, compact-trial plateau convergence, DCT; reverse ceiling from `202`. **Present and verified.**
- **Final point equality (`204`) consumes independent `193` and `132`.** The closure algebra is acyclic, but the join inherits those consumers.

**Honest limitation.** The join is algebraically closed **iff** the input applications `193` (original point upper/point transfer) and `132` (independent lower/finiteness via `051`) are themselves established with actual current clauses. This audit verifies the join’s internal composition and the same-object matching, but not the unworked source-to-point/tube/lower parent construction in full. Therefore the join is **not weakened by finite Gram certificates alone**, and it is **not cleared by those certificates either**.

---

## 25. JOIN-DERIVED-BOUNDS-WHITE

**Consumed chain to verify.**

- **Occupation ceiling uses exact kinetic-half/penalty/raw-half-action and full domains (`205–208`).** Verified above: `RAW` kernel not damped `K_*`, `T(g)>0` but infimum `0` by spreading, `(2ζ)^{α/(2k)}` retained, ceiling precedes moment interpretation.
- **Spatial bracket uses one common kinetic-HALF own energy, correct `M_a/K₀`, full `H¹` (`209`).** Verified; the strict log-gap uses `q−2a>2−a>1`.
- **White evaluation (`210–213`).** All real unit `H¹`, `3A²≤b`, sech energy profile, `c²/6`; gamma relative width; **bounds only**, explicit comparison comparisons.
- **Source-primary fidelity.** BC strict-Riesz comparisons remain comparisons; the direct white case(iv) of BC’s theorem is available for white comparison and is **not** excluded by the strict-Riesz caveat. CH raw moment vs `L^p`-root normalization and the same-canonical Jensen are retained as qualifications, not forced identities.

**Honest limitation.** The join does **not** yield a numerical C2 evaluation, an actual C2 equality at either bound, a first-moment identification of `S₁^pos`, a long-time/white-time interchange, a Skorohod development, or a printed-source constant correction. All zero branches are direct.

---

## 26. Exact finite/scaling control that must persist (precision clause 12)

This is mandatory and is restated as an actual result:

```
V(cC,c^{2/3}b) = c^{1/3}V(C,b),  c>0,
V(cC,b)          = c^{1/3}V(C,c^{-2/3}b),  c>0,
V(cC,0)          = c^{1/3}V(C,0),  c>0,
V(0,b)           = 0,  b≥0.
```

Only the zero-threshold case is the simple `c^{1/3}` law. **The unqualified `V(cC,b)=c^{1/3}V(C,b)` is false for fixed general `b≥0`.**

**Explicit source-compatible countercontrol.**

- `C=1,k=1,ℓ=1/10,b=4`: for `φ≤4` the objective is `−φ²/2≤0`; for `φ>4`, with `y=φ−4`,

```
(1/5)√y − (y+4)²/2 ≤ −y²/2 −39y/10 −79/10 < 0.
```

so `V(1,4)=0` (empty/origin branch).
- Scale only covariance: `k'=16,C'=256`, same `b=4,ℓ=1/10`. At `φ=1`,

```
(1/5)√(16−4) − 1/2 = 2√3/5 − 1/2 > 0,
```

since `√3>5/4`. Thus `V(256,4)>0 = 256^{1/3}V(1,4)`.

This is a finite Gaussian-label control, not an original SPDE covariance counterexample. It neither invokes `D(4)` as an infimum nor claims an incorrect optimizer.

---

## 27. Dependency/cycle audit (bounded to Unit H)

- **Finite Gram (`194–198`)** is self-contained; no covariance/source/Hilbert input.
- **Intrinsic (`199–204`)** is acyclic **as stated**:
  - `051 → (130/131/132)` finiteness/gap;
  - `202` uses `132` only for a finite `S₂^pos`;
  - `203` uses `202` and fixed smooth tests;
  - `204` composes `132` with `193` **after** `203`.
  The presentation references to later theorems inside earlier sections are **navigation**, not proof premises.
- **Occupation/white (`205–213`)** depends on `R_sp`/spatial energy finiteness (`051→132→136→137→138`), but the H-owner deductions themselves do not feed their own finiteness.

Remaining conditions are **explicit pending consumers**: actual original point upper/lower, source-to-Bochner-average UI, source-first scaling/canonical closed restriction, and positive-smoothing/cutoff limit applications must be recognized as genuine unresolved premises if they are not established by their current owners. This audit does not clear them.

---

## 28. Findings

1. **No new mathematical defect found in the 20 own H-owner deductions.** Their internal derivations are reproduced above and are coherent at their stated hypotheses and limit orders.
2. **`S225` interpretation corrected without changing the source:** `D(4)` is a negative **test value**, not the dual infimum; the empty/origin value `0` is the actual finite optimizer/value in that example, and the minimizer of `D` lies above `4`.
3. **The finite-Gram covariance scaling law must retain the joint-threshold form.** This is a distinction between a correct special case and a false general law; it does not refute the source `194–198`, which never claims the false law.
4. **Literal coverage is complete** for the asked 20 proofs and 24 roles, with every role status stated.
5. **Both joins close only under their named current consumers.** The join algebra is verified; the whole-model `C2` claim is not accepted merely from the H-owner block.

---

## 29. Verdict and confidence

**Verdict (unforced).**
- For the **H20/24 scope in isolation**: the claims are **mathematically credible and internally consistent**; the majority of the deductions are verifiable, self-contained, or verified-with-explicit-inputs.
- For the **Unit-H whole intrinsic limit** (`C2=S₂^pos=2^mA1`): this is **conditionally established**; unqualified acceptance would silently reuse upper/lower/point-transfer parent clauses that are here only checked at their interfaces.

**Confidence (unforced categorical).**
- Finite Gram optimization (`194–198`): **high**.
- Occupation/white evaluations (`205–213`): **high** (at their stated energy/bounds scope).
- Intrinsic/signed positive closure (`199–204`): **medium**; the algebra and ordering are clean, but heavy current parent premises remain.
- Both canonical joins: **medium, conditionally on the actual consumed `D/E/F/G/C/A/B` clauses**; not high, not cleared by the finite certificates alone.

No source edit, new formal theorem, numerical-C2 claim, Skorohod development, Chen/actual-`p1` identification, whole-214/240/13, image/Kimi/cold, or build/private-delivery conclusion is implied by this audit.