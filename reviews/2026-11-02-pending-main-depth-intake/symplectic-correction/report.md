# Review Result — deepseek

- category: paper-review-deepseek
- model: deepseek/deepseek-v4-pro
- verdict: PASS_WITH_NOTES
- confidence: HIGH

**SAME-SESSION CORRECTION** — this output corrects concrete inaccuracies and input-use attestations in my immediately prior report from this same session. It is not a new independent vote, not a confidence retry, not a cold read, and does not retroactively improve the prior report, which remains preserved unchanged.

## Critical findings

First, a retraction of my own prior attestation, not a manuscript finding:

**RETRACTED — false input-delivery attestation.** My prior report's Noncritical finding 3 and SYM08 claimed the Friz–Hairer excerpt, the completed mean `P:cameron-full-mean` and its parameter package were “not supplied”/“outside the bounded target excerpt.” That was factually wrong. All of these were delivered in the original packet and are re-inlined now:
- Full `integrated_cameron_mean.tex` at packet 13391–13906 (`P:cameron-full-mean` statement/proof at 13656–13727, parameter package at 13738–13747);
- Full `integrated_constant_phase_young.tex` at 10681–11179;
- Full `integrated_source_convergence.tex` at 9963–10453;
- Full `integrated_symplectic_phase.tex` at 15150–15537;
- All four source carriers at 21357–21704 (Friz), 21708–22210 (Teschl), 22214–22636 (Crouzeix), and the chen-author carrier.

The honest classification is **(b) delivered but not fully checked by me**, never (a) absent. This mislabeling is my error and I retract it.

No new proof gap, false identity, hidden hypothesis, incorrect constant, or invalid asymptotic was introduced or discovered in the manuscript by this correction. The five proofs remain sound.

## Noncritical findings

1. **The smoothness hypothesis in `L:symplectic-free` is stronger than needed, but this must not be read as a repair.** The skewness proof uses only `‖b‖_∞<∞` (I originally flagged “smooth” as over-formulated). Per this correction task, the stated stronger assumption is allowed and no broader theorem is claimed. I withdraw my prior “recommended fix #1” as a *necessary* repair; it was a cosmetic remark, not a defect.

2. **The Friz import is bounded-bilinear Young, not a nonlinear vector-field theorem.** Verified against the supplied carrier: (4.3) at printed p. 62 gives the compensated estimate `∫_s^t Y dX − Y_s X_{s,t} ≤ C‖Y‖_β‖X‖_α|t−s|^{α+β}`, and p. 13 (Section 1.5) states the infinite-dimensional validity. The manuscript correctly *derives* its own linear left-composition solution/stability/uniqueness estimates from that scalar bilinear bound and does not invoke a bounded-vector-field RDE theorem. This is an imported statement (the full proof of Young's bound is upstream of the excerpt), not a gap.

3. **Upstream-of-target items that remain genuinely un-reaudited in this pass** (they are consumed by proofs I now audit, but they are not re-inlined and I do not re-derive them): `P:actual-operator-driver` (supplies the given-noise path `M_R` and its `√p`/square-exponential moments), and the Cameron-mean inputs `P:cutoff-singular-values` and the spatial occupation quantities `B_Γ`, `R_sp`, `L:spatial-physical-pair`. They were delivered in the original packet; they are **delivered** and **upstream prerequisites**, not absent. I name them so the exact target application stays qualified (see the ledger).

## Checked derivations

### A. Correction or defense of the three flagged statements

**Statement 1 — CONCEDED (my prior report was wrong).**
My SYM03 wrote that the physical flow `P=S_E(t)U(t,s)S_E(-s)` “inherits C¹ on all E.” The manuscript proves, and only claims, that **the interaction trajectory** `t↦U(t,s)e` is C¹ for each fixed state `e`, via the strong-integral difference quotient of `C_b(r)=S_E(-r)B(b^ρ(r))S_E(r)` (bounded, strongly continuous, so the Young/ordinary state equation makes `U` genuinely differentiable). It then uses:
- (a) interaction conservation: `d/dt ω(Ue,Uf)=0`, valid because `U` is C¹; and
- (b) **free invariance** `ω(S_E z,S_E w)=ω(z,w)`, already established in `L:symplectic-free`,
so that `ω(Pz,Pw)=ω(US_E(-s)z, US_E(-s)w)=ω(S_E(-s)z,S_E(-s)w)=ω(z,w)`. No differentiability of `S_E(t)` (which is only strongly continuous on rough `E` data) and no “C¹ inherited by P” is asserted or needed. The manuscript's own closing line “No … derivative of the free generator on a rough state was used” confirms this. **My sentence overclaimed; the manuscript is correct.**

**Statement 2 — CONCEDED on the variable, DEFENDED on the substance.**
Exact computation with `z=(u,v)`, `w=(f,g)`, `J_E(f,g)=(Λ^{-1}g,−Λf)`:
```
ω(z,w)=⟨z,J_E w⟩_E = ⟨u,g⟩_{1/2,−1/2} − ⟨f,v⟩_{1/2,−1/2},
ω(B(b)z,w)=ω((0,bu),(f,g)) = −⟨f,bu⟩ = −∫ f·b·u,
ω(z,B(b)w)=ω((u,v),(0,bf)) = ⟨u,bf⟩ =  ∫ u·b·f,
⇒ sum = −∫ f·b·u + ∫ u·b·f = 0.
```
The cancellation runs through the **displacement components `f` and `u`**, valid because `bu,bf∈L²` with `‖bu‖_{H^{-1/2}}≤‖bu‖₂≤‖b‖_∞‖u‖_{H^{1/2}}`. The velocity `g` appears in `ω` only through the dual pairing `⟨u,g⟩`, which cancels immediately in the first slot of both terms; `g` is **not** used as an L² multiplier of the force. My prior phrasing using `g` in that slot was wrong; the corrected pairing is `−∫f·b·u+∫u·b·f`.

**Statement 3 — CONCEDED (my prior zero-case summary conflated cases).**
Correct split:
- `c=0` (any fixed `Φ`): `D=D_Φ=E[W(Φ)M_R]` is a **deterministic covariance-mean** driver. The flow is deterministic; conservation `P*J P=J`, `‖P‖≥1`, and Young-invertibility hold. Not free unless `Φ=0` as well.
- `Φ=0` (any `c`): `D=cM_R`, a **centered stochastic** raw driver scaled by `c`. Conservation holds a.s.; the norm baseline and invertibility hold by the source-limit argument.
- `c=Φ=0` **or** `Γ=0`: `D=0`, the free group `S_E`. Trivial conservation; `‖S_E(t)‖≥1` follows from J-invariance.
The manuscript is careful (P:symplectic-raw: “For `c=0` … deterministic for every fixed `Φ`”; section end: “For zero covariance the drivers and covariance means vanish”). My report's “zero c/Φ → free” summary was the conflation; corrected here.

### B. Actual audit of the six consumed mean/Young clauses (now read)

All six are now checked against the re-inlined bodies; none fails.

1. **`P:cameron-full-mean`** — `TΦ(s)=T_sp(UΦ(s)):H→L^r(I;K(F))`, compact; for smooth `Φ` equals the actual multiplier `iB_F(m_R h_Φ(s))`. Domain is the completed `H=H_I`; `U=C_t⊗I` is bounded `H→L^r(I;H_sp)` (dimension-free); `T_sp:H_sp→K(F)` is compact at fixed `R` (via `T_sp Q_n` finite-rank limit). Compactness of `T` uses `T_n=T_sp Q_n U` (norm approximation by finite combination of compact `T_sp q_j` composed with precompact `C_t` coordinate extraction); `ε_J=‖T(I−P_J)‖→0` is the weak-null + compact-image argument. **Range in `iE`:** `T_sp q=iB_F(·)` has range ⊂ `iE` and annihilates constant columns; the operator-norm closure preserves this, so `TΦ(s)` has values with range in closed `iE`. This is exactly the clause PROOF169 compresses through `i`. ✓

2. **`E:cameron-block-parameters`** — `1/2<θ<min(1−a/2,(3−a−α)/2)`, `1/(1−θ)<r<2/a`, `1/θ≤p<2<r`. Window checks: `1/2<1−a/2` ⟺ `a<1`; `1/2<(3−a−α)/2` ⟺ `α+a<2`; `r`-window nonempty ⟺ `1/(1−θ)<2/a` ⟺ `θ<1−a/2`; `p<2` ⟺ `θ>1/2`; `2<r` from `r>1/(1−θ)>2`. All consistent under Hypothesis H:homog. ✓

3. **`E:cameron-actual-covariance` at rank zero** — `(L_{δ,J}Φ)_m(u)=√δ∫_0^{min(u,ℓ_m)}S_F(-v)T(Q_JΦ)(s_m+δv)S_F(v)dv`. At `Q_J=I`: `E[g_δ A_{F,m}(u)W(i_IΦ)]=√δ H_{m,F}(Φ)(u)`; compressing through `S_F i=iS_E` and `TΦ`'s range in `iE` gives `E[M_m(u)W(i_IΦ)]=δ^{a/2}H_{m,E}(Φ)(u)`, using `g_δδ^{a/2}=√δ` with `g_δ=δ^{(1−a)/2}`. The unscaled factor is `δ^{a/2}`, not `√δ`. ✓ All exponents verified.

4. **Compact-conjugation/Bochner + primitive** — `S_F(-v)T(Φ)(s_m+δv)S_F(v)` is Bochner-measurable via strong measurability of the mean field plus norm-continuity of conjugation on compact values; the primitive estimate exponent `1−1/r>θ` (from `r>1/(1−θ)`) yields the `C^θ` bound. ✓

5. **`P:constant-young-linear`** — the left equation `U_D(t,s)=I+∫_s^t dD(r)U_D(r,s)`; uniqueness by local contraction (`N_ℓ(I_D(V))≤c_θ[D]_θℓ^θN_ℓ(V)`) + patching; local Lipschitz in the triangle norm; growth `C_T exp(C_T(1+‖D‖_{C^θ})^{1/θ})`; **invertibility separate**, via `‖U−I‖_∞≤1/3` Neumann series on short pieces then products. This is precisely the “separate actual Young invertibility — not infinite-dimensional symplectic identity alone” requirement. ✓

6. **Fixed-shift/source flow convergence (used in 168)** — `P:constant-gaussian-flow` gives `U_{A^ρ}→U_A` in every finite `L^p(sup triangle norm)`: local Young Lipschitz + uniform Gaussian tails + `q=1/θ<2` + `pC(1+x)^q≤cx²+C_{p,c}` + square-exponential moment ⇒ uniform integrability. The shifted drivers `D=cM+D_Φ`, `D^ρ=cM^ρ+D_Φ^ρ` are “Gaussian paths plus deterministic shifts”; the `E/F` restriction `U_F i=iU_E` transfers it. ✓

### C. Delivery/consumption ledger

| Input | Delivered | Read now | Consumed by 165–169 | Remaining unverified upstream |
|---|---|---|---|---|
| `cameron-mean.tex` (P:cameron-full-mean, row, spatial map, temporal map, parameters, embedding) | yes | yes | PROOF169 (rank-zero mean; `δ^{a/2}`; `φ_m=δ^{-a/2}T_m^*i_IΦ`) | `P:cutoff-singular-values`, `R_sp`, `L:spatial-physical-pair` (delivered; upstream) |
| `young.tex` (P:constant-young-linear, P:constant-gaussian-flow, constant columns) | yes | yes | PROOF167/168/169 (uniqueness, separate invertibility, flow limit) | none load-bearing |
| `source.tex` (P:source-gaussian-transfer, P:source-canonical-convergence, retaining isometry, pointfield regularity, ordinary response) | yes | yes | PROOF166/168 (mean convergence, √p moments, source-limit) | `P:actual-operator-driver` (delivered; upstream) |
| `friz-hairer.txt` (bounded-bilinear Young, (4.3) p. 62, infinite-dim p. 13) | yes | yes | PROOF167/168/169 via `E:constant-young-estimate` | full proof of Young's bound imported as stated |
| `teschl-2014.txt` | yes | **not needed** for 165–169 | none (serves S:signed-static-wave, S:compact-mean-family) | n/a |
| `crouzeix-v1.txt` | yes | **not needed** for 165–169 | none (serves S:static-all-orders `L:complex-phase`) | n/a |
| `chen-author.txt` | yes | **not needed** as premise for 165–169 | none (contextual source-law matching only) | n/a |

### D. Corrected coverage ledger

- **PROOF165** `L:symplectic-free` (lines 49–85) — **CHECKED**. Balanced duality `J_E(f,g)=(Λ^{-1}g,−Λf)`, `J_E²=−I`, finite 2×2 Fourier det-one (incl. zero shear), L² displacement cancellation (correct variables `f,u`), no rough generator derivative.
- **PROOF166** `L:symplectic-source-mean` (106–146) — **CHECKED**. Bochner means, `C^θ` convergence bound, `h_Φ^ρ=⟨j_srcΦ,v_{ρ;t,x}⟩` regularity, primitive identity, noncentered/sign-changing combined source. Upstream: driver norm bound.
- **PROOF167** `P:symplectic-source` (157–186) — **CHECKED**. **C¹ scoped to the interaction `U` only**; physical conservation via free invariance + interaction conservation (not C¹ of P). Source event on fixed `c,Φ,R,T`.
- **PROOF168** `P:symplectic-raw` (200–274) — **CHECKED**. `D^ρ→D` in `L^pC^θ`, `1/θ<2`, square-exponential tails, countable Borel–Cantelli subgroup, `W`-measurable descent, `E` closed not dense in `F`, `‖P_D‖≥1` from `P*JP=J`, **separate** Young Neumann invertibility, `c=0` deterministic, `Φ=0` stochastic, both-zero/zero-Γ free; pointwise `δ`-growing-cone norm baseline only.
- **PROOF169** `P:symplectic-block-mean` (306–382) — **CHECKED**. True partition, `T_m` isometry, `φ_m=δ^{-a/2}T_m^*i_IΦ`, unscaled covariance `δ^{a/2}`, first-chaos orthogonality to `I−T_mT_m^*`, rank-zero completed identity compressed to `E`, stopped equality through `ℓ_m`, `ℓ=0` identity, pure-mean endpoint `‖S_E(ℓ_m)U_{H_m}(ℓ_m,0)‖≥1` via c=0 case of P:symplectic-raw.

- **SYM01** — PASS. **SYM02** — PASS. **SYM03** — PASS (C¹ correctly limited to `U`; conservation independent of free-generator differentiability). **SYM04** — PASS. **SYM05** — PASS. **SYM06** — PASS (inputs delivered and re-verified; `δ^{a/2}`, finite-2×2 vs infinite-invertibility, Bochner-not-pointwise mean all correct). **SYM07** — PASS (force cancellation on displacements `f,u`; zero-case split corrected: `c=0` deterministic mean, `Φ=0` centered stochastic, both-zero/zero-Γ free). **SYM08** — PASS (with the delivery attestation retracted and the delivered-vs-upstream distinction recorded).

## Required fixes before production gate

None for the manuscript's five proof bodies. Required actions concern only my prior report, which cannot be retroactively amended; they are recorded here:
1. Retract the “not supplied” classification of Friz/Cameron-mean/parameter-package/Teschl/Crouzeix (they were delivered; I had not fully checked them).
2. Retract the C¹-inheritance sentence for the physical flow (only the interaction `U` is C¹).
3. Correct the force-cancellation variable pairing to `−∫f·b·u+∫u·b·f`.
4. Replace the conflated zero-case summary with the three-way split above.

## One-line summary

Same-session correction: my prior report mis-attested delivered inputs as absent and made three imprecise/incorrect statements (C¹ inheritance, force-cancellation variables, zero-case conflation); after actually reading the re-inlined Cameron/Young/source/Friz bodies and re-auditing all six consumed clauses, PROOF165–169 remain CHECKED and SYM01–08 remain PASS, with the record now distinguishing delivered-unused (Teschl, Crouzeix, chen-author) from delivered-consumed (Friz) and delivered-upstream-unreaudited (driver construction, cutoff/singular-values, spatial-occupation quantities).