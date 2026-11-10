# Review Result — deepseek

- category: paper-review-deepseek
- model: deepseek/deepseek-v4-pro
- verdict: PASS_WITH_NOTES
- confidence: HIGH

## Critical findings

None. No proof gap, false identity, hidden hypothesis, incorrect constant, or invalid sign found in either targeted production change.

The two audited deltas are:

1. **PRODUCTION214** — `L:translated-covariance-CS` (lemma + proof) and `R:source-case2-time-shift`, inserted after the proof of `L:damped-homogeneous-norms` in `production-main-context.tex` (candidate excerpt lines 685–909). The lemma is a self-contained covariance Cauchy–Schwarz for two differently translated test kernels in one stationary form. I verified every algebraic step independently.

2. **PRODUCTION182** — the changed multi-line baseline in the proof of `P:uniform-mean-product` in `production-uniform-products.tex` (candidate excerpt lines 2071–2078). The change replaces an incorrect shortcut ("its norm bound is at most `K/B ≤ K`") with the correct spectral baseline `‖S_E(B)U_{\bar H_m}(B,0)‖ ≤ 8(1+K)²(1+B)e^{Bλ(\bar M_m)}`. The old sentence conflatably treated the instantaneous multiplier bound `‖\bar M_m‖ ≤ K/B` as a bound on the physical wave norm; the new text separates the three distinct objects (`\bar M_m`, `\bar H_m`, endpoint wave). This is a real corrected error, not a cosmetic edit.

## Noncritical findings

- **N1 (scope boundary, not a defect).** The surrounding manuscript prose ("component proofs have passed scoped independent reviews", the quoted first-moment `L_*` normalization, etc.) is explicitly historical/prose and is not used as a mathematical premise by either target. I did not rely on it.
- **N2 (PRD13 limitation).** Image/layout evidence is author-only. `build-evidence.json` reports `images_delivered_to_reviewer: false`, `full260_page_visual_inspection: false`, and `source14_21_independent_image_gate: OPEN`. I do not certify raster/source-image/260-page rendering/global/cold. Future production credit is bound to exact candidate HEAD `36c0fec8f0abf1584c4ca1abe5ec553c2c4ea2d7` only.
- **N3 (PRD12 limitation).** The mechanical-identity evidence is machine-generated SHA256; I did not hand-recompute hashes (and am not required to). Its internal consistency is confirmed: among proofs, only `PROOF182` differs base-vs-candidate and `PROOF214` is newly added; candidate `integrated_uniform_products.tex` hash equals `proposed_source_sha256`; candidate main-file hash matches `build-evidence.json`. This is a binding/identity audit, not an independent 213-proof validity vote.
- **N4 (harmless).** The trivial bound `0 ≤ γ(z) ≤ μ(ℝᵈ)` used in the absolute estimate silently uses the explicitly assumed pointwise nonnegativity `γ ≥ 0`. Correct, because `γ` is real and nonnegative by hypothesis and `|γ(z)| ≤ μ(ℝᵈ)` trivially.
- **N5.** Held primary p14–21 is text-only; its p21 transcript (excerpt lines 5763–5785) independently confirms the source drops the temporal offset (`κ(s−r)` written for relative times) while **retaining** the spatial origins in the two Green tests. No independent raster credit is claimed from it.

## Checked derivations

Independently re-derived (candidate line/equation references):

1. **Kernel feature identity** (lines 734–743, = author B6): `∫h_λ(t,r)h_λ(s,r)dr = 2λe^{−λ(t+s)}∫_{−∞}^{min(t,s)}e^{2λr}dr = e^{−λ|t−s|}`. ✔
2. **L² normalization** (line 744): `∫h_λ(t,r)²dr = 1` — uses squared L² (not L¹); matches the diagnostics note that the L¹ norm is `√(2/λ) ≠ 1`. ✔
3. **`m_L`** (line 754): `‖Φ_L(t,x)‖² = ν((0,L])μ(ℝᵈ) = m_L`. ✔
4. **Reproducing kernel** (line 755): `⟨Φ_L(t,x),Φ_L(s,y)⟩ = γ(x−y)∫_{(0,L]}e^{−λ|t−s|}dν = C_L((t,x),(s,y))`. ✔
5. **Bochner + Fubini → CS** (lines 766–770): `Q_L(f,h)=⟨F_L(f),F_L(h)⟩`, giving `|Q_L| ≤ (Q_L(f,f)Q_L(h,h))^{1/2}` with constant exactly 1; no shifted cross-kernel PSD is invoked. ✔
6. **Common-translation invariance** (lines 776–783): `Q_L(T_{A,a}f,T_{A,a}h)=Q_L(f,h)`; full-line + Lebesgue translation. ✔
7. **Truncation/cap limiting passages** (lines 787–808): monotone on nonnegative integrands only; finite cross limit bounded by `N_C(G₁)N_C(G₂)`; no division by norms (zero measures/norms included). ✔
8. **Edge spectral mass** (lines 874–879): `μ_e(ℝᵈ) = ∫e^{−b|ξ|²/2}μ(dξ) = αV b^{−α/2}∫_0^∞ u^{α−1}e^{−u²/2}du` with `b=ε_j+ε_h`. Verified by Stieltjes integration against ball mass `m(r)=μ(B_r)=V r^α` (radial homogeneity; no radial density needed). ✔
9. **`N_0`** = `θ⁻²` for `G=e^{−θt}G_t` (`mass G_t(ℝᵈ)=t`). ✔
10. **Offset sign** (lines 843–851, diagnostics): with `t=u+A`, `s=v+B`, `κ(t−s)=κ(u−v+A−B)`; test `A=2,B=5,u=1,v=0` gives `t−s = −2` (= `u−v+A−B`), refuting the reversed-origin value 4. ✔
11. **Spatial shift** (line 857): `x=X+a`, `y=Y+b` ⇒ `γ(x−y)=γ(X−Y+a−b)`. ✔
12. **Falsification independent checks** (author-falsification.md, re-derived):
    - Shifted cross kernel `κ(s−r+1)` on `{0,1}`: `vᵀLv = 2e^{−1}−1−e^{−2} = −(1−e^{−1})² < 0` (not PSD). ✔
    - `A(λ)=2(λ−1+e^{−λ})/λ²` vs `B(λ)=(1−e^{−λ})²/λ²`; `H(λ)=2λ−3+4e^{−λ}−e^{−2λ}`, `H(0)=0`, `H'=2(1−e^{−λ})²>0`, so `A>B` (independent translation fails). ✔
    - Constant 1 is attained at coincident origins (`N_C>0`); coefficient sharp. ✔
13. **PROOF182 baseline derivation**: `\bar H_m(u)=∫_0^u S_E(−v)\bar M_m S_E(v)dv` is exactly the interaction primitive of the constant potential `L=\bar M_m`; hence `S_E(B)U_{\bar H_m}(B,0) = P_V^E(B)` and the spectral bound `8(1+K)²(1+B)e^{λ(\bar M_m)B}` applies (constant re-derived from entry bound `≤2(1+K)(1+t)e^{λt}`, 2×2 norm ≤ twice, condition cost `≤2(1+K)` ⇒ 8). ✔
14. **Zero-potential regression test** (diagnostics): `\bar M_m=\bar H_m=0`, baseline `=S_E(B)` with `‖S_E(B)‖ ≥ 1`; `B=2,K=1` refutes any `‖wave‖ ≤ K/B = 0.5`. The corrected line passes; the old line fails. ✔
15. **Log-prefactor enlargement** (lines 2080–2086): `log(8(1+K)²(1+B)) ≤ log16 + 4log(1+K) + 3log(1+B) = L_{B,K}`, and `L_{B,K}/B → 0` in the corollary (PROOF183 unchanged). ✔

## PRD status audit

Distinction used throughout: **source-correctness** (is the imported/compared source display correctly characterized) vs **transcription/application** (is the candidate TeX faithful and correctly applied).

| PRD | Status | Candidate evidence |
|---|---|---|
| PRD01 | FULLY_CHECKED | Lemmas/stmt lines 686–728; hypotheses exactly as required (finite positive `μ`, real nonnegative `γ`, locally-finite capped `ν`, full-line zero extension `G⁰`, `N₀,N_C<∞`). No missing hypothesis; no unauthorized added conclusion (only B4/B5 + coefficient-one). |
| PRD02 | FULLY_CHECKED | Lines 730–771: feature factorization, squared-L² normalization, complex phase `e^{iξ·x}` with linear-first inner product, `m_L`, norm continuity/separable range, Bochner/Fubini, CS constant 1. |
| PRD03 | FULLY_CHECKED | Lines 776–810: common-translation identity; differing-translation cross bound; zero measure/norm handled without division; spatial covariance fixed. |
| PRD04 | FULLY_CHECKED | Lines 787–808 (truncations/caps, monotone only for nonnegative integrands); remark (iii) 901–908: no pointwise spatial-Gaussian monotonicity, no unregularized spatial-distribution claim. |
| PRD05 | FULLY_CHECKED | Remark (i) 813–859; own-chain predecessors with `(0,0)` at one-vertex chains, empty chain excluded; exact Case-2 integral = `Q(T_{A,a}G₁⁰,T_{B,b}G₂⁰)`; `u−v+A−B` sign; spatial origins kept in tests, later `γ(X−Y+a−b)`; matches held p21. |
| PRD06 | FULLY_CHECKED | Remark (ii) 861–866; held p14 (3.5) repeats `x`; candidate uses independent `y` (`E:damped-norm-definitions` 579–582); source (3.6) cardinalities/norm placement (`2‖G‖^{(1)}` for `Q₁`, no factor for `Q₂`) untouched; no full Theorem 3.1 reproof. |
| PRD07 | FULLY_CHECKED | Remark (iii) 868–908: `b^{−α/2}` mass, `γ_e=p_b*Γ≥0`, `ν_e` with `Γ_E(α₀)` normalization and cap finiteness (`α₀>0`), `N₀=θ⁻²`, `N_C` finite from `L:damped-homogeneous-norms`, positive Green width in d3; first-norm hypotheses explicitly not waived. |
| PRD08 | FULLY_CHECKED | Bridge compatible at all four direct consumers: `L:joint-fixed-order` (1149–1151), `L:crude-corrected` (1230–1233), `L:vertex-crude` (1309–1312), `P:envelope` (1572–1573); uniform in predecessor origins, coefficient 1, no `Q₂` loss, no `exp(A+B)`, `Q₁` factor 2 untouched; cap/Green/spatial limit order preserved (deferred to `L:joint-fixed-order`/`L:spatial-wick-measures`). Imported Case 1/Case 3 arithmetic remains imported (out of change scope). |
| PRD09 | FULLY_CHECKED | Patch adds exactly three setup-reference insertions (hunks at 216/304/578) plus the lemma/remark block after `L:damped-homogeneous-norms` (hunk at 670), before joint regularisation; self-contained, no circular moment/first-constant input, no scope inflation. |
| PRD10 | FULLY_CHECKED | Candidate 2071–2084 equals proposal patch/binding; `‖\bar M_m‖ ≤ K/B ≤ K`, `‖\bar H_m‖_θ ≤ a_m ≤ K`, spectral endpoint prefactor; zero-potential test passes; `K≥1`, `B≥1` used as separate hypotheses; Young perturbation use is the pre-existing `P:young-upper-multiplicative`. |
| PRD11 | FULLY_CHECKED | Re-derived all signs/constants against falsification + diagnostics (items 10–12 above); no copied paraphrase. |
| PRD12 | FULLY_CHECKED (as identity audit) | Evidence internally consistent: only PROOF182 body differs (base `eb71…` → candidate `b1b2…`), PROOF214 added (`8a18…`, base null), 212 others `same:true`, old IDs/labels preserved, candidate hash equals proposed-source hash. Method: bytes strictly between `begin{proof}`/`end{proof}`, SHA256. Independent-review limit: no hand hash recomputation; not a validity vote. |
| PRD13 | FULLY_CHECKED (as limitation record) | `images_delivered=false`, full-260 render unverified, `source14_21_independent_image_gate=OPEN`, candidate PDF SHA author-only. Not certified by reviewer. |
| PRD14 | FULLY_CHECKED → SATISFIED_FOR_EXACT_CANDIDATE | See below. |

## Required fixes before production gate

- **None** for the mathematics, transcription, application, or signs/constants of PRODUCTION214 and PRODUCTION182 at the exact candidate HEAD `36c0fec8f0abf1584c4ca1abe5ec553c2c4ea2d7`.
- Remaining non-mathematical obligations are **retained, not adopted**: source-image/raster verification, full-260-page visual inspection, all-213 proof-validity clearance, and global/cold gates. These stay with root adjudication.

## Production statuses

- **PRODUCTION214: PASS** — Lemma `L:translated-covariance-CS` and `R:source-case2-time-shift` are present, correctly transcribed from the author proof, internally correct, and correctly positioned/connected.
- **PRODUCTION182: PASS** — The corrected static-wave baseline is mathematically correct, exactly matches the author proposal, and repairs a genuine error in the prior sentence.
- **FND_CASE2_PRODUCTION: SATISFIED_FOR_EXACT_CANDIDATE.**

**Reason:** The specifically identified Case-2 premise — a coefficient-one covariance Cauchy–Schwarz for the source Theorem 3.1 Case-2 step with the predecessor time-offset retained — is now supplied by the actual integrated candidate bytes. The lemma statement and its complete proof are embedded in the candidate (`production-main-context.tex`, excerpt lines 717–811), the application/qualification remark is embedded (lines 813–909), and the three setup references wire the lemma/remark into the actual consumers (`L:joint-fixed-order`, `L:crude-corrected`, `L:vertex-crude`, `P:envelope`, plus the transitive `P:Jensen`/`P:mixed` constructor chain). All signs (`u−v+A−B`, `γ(X−Y+a−b)`), constants (coefficient one; `μ_e(ℝᵈ)=αV b^{−α/2}∫u^{α−1}e^{−u²/2}du`), and hypotheses (finite `μ_e`, locally-finite capped `ν_e`, `N₀,N_C<∞`, Green smoothing in d=3) were independently verified. This covers only the Case-2 premise; the remaining parts of the source Theorem 3.1 and the source's first-norm hypotheses remain imported, and no FND/global/cold/full-goal adoption is made by this reviewer.

## One-line summary

Both production changes — the inserted translated-covariance Case-2 Cauchy–Schwarz bridge (PROOF214) and the corrected static-wave baseline bound in the uniform mean-product proof (PROOF182) — are mathematically correct, faithfully transcribed/applied, and the identified FND Case-2 premise is satisfied for the exact candidate HEAD `36c0fec8f0abf1584c4ca1abe5ec553c2c4ea2d7`, with no critical defects found.