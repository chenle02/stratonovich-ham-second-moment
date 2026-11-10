# Review Result — deepseek

- category: paper-review-deepseek
- model: deepseek/deepseek-v4-pro
- verdict: PASS_WITH_NOTES
- confidence: HIGH

## Critical findings

None. I found no mathematical error in the lemma statement or proof, no sign error, no incorrect constant, and no false identity in its application to the source's Case 2. The insertion plan is coherent and correctly scoped.

## Noncritical findings

- N1. **Raw `.tex` line numbers not independently verifiable in this run.** The plan cites frozen-base line numbers (671, 673, 213–221, 294–310, 576–581, 912–938, 989–1040, 1058–1116, 1320–1347, 379–509, 6397–6618, 1378, 7671, 217, 296, 457). The supplied bounded-context excerpt carries the review-file numbering (offset), not the `.tex` line numbering, and I am forbidden from opening the file. Semantic adjacency is verified: the embedded manuscript shows `L:damped-homogeneous-norms` proof ending immediately before the joint-regularization setup, so the claimed insertion point is correct. The plan itself already requires re-resolving labels/line numbers at integration.
- N2. **"All 213 original proof bodies byte-identical" cannot be byte-checked read-only.** The plan correctly conditions this on recording any changed proof-body delta explicitly, so this is a production-gate verification step, not a defect.
- N3. **Source-image verification of printed pages 14/21 is not performed here** (only held text extraction). This is outside the current text-only mathematics scope and remains a separate gate; I do not award raster/image credit.
- N4. Minor remarks only: everything read-only; no build executed; no integration claimed as done.

## Checked derivations

- **Exponential-kernel factorization (B6).** For `h_λ(t,r)=√(2λ)e^{-λ(t-r)}1_{r≤t}`, I recompute ∫h_λ(t,r)h_λ(s,r)dr = 2λe^{-λ(t+s)}(1/(2λ))e^{2λ min(t,s)} = e^{-λ|t−s|}, and ∫h_λ²dr=1. Correct signs and constants.
- **Feature inner product (B7).** On `H_L=L²((0,L]×R^d×R, ν⊗μ⊗dr)` with inner product linear in the first entry, `‖Φ_L(t,x)‖² = ν((0,L])·μ(R^d)=m_L` and `<Φ_L(t,x),Φ_L(s,y)> = κ_L(t−s)γ(x−y) = C_L((t,x),(s,y))`. Both verified directly.
- **Norm-continuity/measurability/Bochner.** `‖Φ(t,x)−Φ(s,y)‖² = 2m_L − 2Re C_L(·,·)→0`; continuity of `C_L` follows by dominated convergence; separable range and boundedness hold; Bochner integrability of `∫fΦ` with `‖F_L(f)‖ ≤ √m_L‖f‖₁`; Bochner Fubini is justified by the scalar majorant `m_L‖f‖₁‖h‖₁`. No finite-matrix-to-infinite jump remains.
- **PSD and CS.** `Q_L(f,h)=<F_L(f),F_L(h)>` gives `Q_L ≥0` and `|Q_L(f,h)| ≤ Q_L(f,f)^{1/2}Q_L(h,h)^{1/2}`. Constant one is exact.
- **Common-translation invariance (B9).** Changing both integration variables on the full time line, with `γ(X+a−(Y+a))=γ(X−Y)` and `κ_L(u−v)`, gives `Q_L(Tf,Th)=Q_L(f,h)`. No `exp(A+B)` factor arises.
- **Truncation and cap limit.** `G_{i,M}=min(G_i,M)1_{0<t≤M,|x|≤M}` increases to `G_i`; nonnegativity of `C_L` and of the integrands gives monotone convergence for both self and cross pairings; self-limits `Q_L(Gᵢ⁰,Gᵢ⁰)↑N_C(Gᵢ)²` control the cross limit. Zero norms/caps need no division. Verified.
- **Boundedness/nonnegativity of the kernel.** `|Q_L(f,h)| ≤ ν((0,L])μ(R^d)‖f‖₁‖h‖₁`; `κ_L,γ≥0` gives `C_L≥0` pointwise, so the translated cross pairing is nonnegative (it does not require the shifted cross kernel to be PSD).
- **Case-2 identity (B10).** With origins `(A,a)=(s_{n₁−1},x_{n₁−1})`, `(B,b)=(s_{2n−1},x_{2n−1})`, the original final-pair integral equals `Q(T_{A,a}G₁⁰,T_{B,b}G₂⁰)`: the first factor is `G₁(t−A,x−a)`, the second `G₂(s−B,y−b)`, with `κ(t−s)` (evenness removes the orientation issue). Verified against held page 21.
- **Origins/false-equality diagnosis.** The held page 21 displays `γ⁰(s−r)` after relative-time change, omitting `A−B = s_{2n−1}−s_{n₁−1}`; the bridge supplies the correct bound without using that offset-free identity. Verified.
- **Regularized-input constants.** `μ_e(R^d)= α V b^{-α/2}∫_0^∞ u^{α−1}e^{-u²/2}du` (radial ball-mass integration, not a density); `ν_e` finite on every cap for `α₀>0`; `N₀(e^{-θt}G_t)=θ^{-2}`. Verified.
- **Falsification controls rechecked.**
  - Shifted cross matrix at `μ=δ₀,ν=δ₁`, indices `{0,1}`: `L=[[e^{-1},1],[e^{-2},e^{-1}]]`; `vᵀLv=2e^{-1}−1−e^{-2}=−(1−e^{-1})²<0`; Laplace-mixture on `[1,2]` is `−∫(1−e^{-λ})²λ^{α₀−1}dλ/Γ_E<0`.
  - Unit-box self/cross: `A(λ)=2(λ−1+e^{-λ})/λ²`, `B(λ)=(1−e^{-λ})²/λ²`, `H(λ)=2λ−3+4e^{-λ}−e^{-2λ}`, `H(0)=0`, `H'(λ)=2(1−e^{-λ})²>0`, so `A>B`. Verified.
  - Full fractional measure: `N_C(G)²=2/[(1−α₀)(2−α₀)]` and `N₁=1/(1−α₀)` verified by integration; `ν=δ₁` box gives `N_C²=2/e`. Constant-one attained at coincident origins `G₁=G₂`, `N_C>0`.
  - Spatial smoothing non-monotone: `γ_b(0)=1+e^{-b/2}`, `γ_b(π)=1−e^{-b/2}`, opposite monotonicities in `b`.

## Required fixes before production gate

- **No mathematical repairs are required** for the lemma, its proof, or its application.
- Production-only gates (already correctly kept open by the plan):
  1. Re-resolve exact frozen-base `.tex` line numbers and labels at integration (N1); verify no proof-body delta, or record one explicitly (N2).
  2. Run the repository's LaTeX build to 0 errors / 0 undefined refs / 0 overfull boxes; rebuild and refresh the PDF/render inventory.
  3. Retain independent rendered source-image verification of physical pages 14 and 21 (N3); text extraction is not image credit.
  4. Final whole-argument cold read and FND production closure remain open and are not certified by this audit.

## BR01–BR12 determinations

- **BR01 — FULLY_CHECKED.** Hypotheses are consistent and integrable; finite positive Borel `μ`, real nonneg `γ`, cap-finite `ν` with `λ>0`-positive domains, `N₀+N_C` finite, zero extension and full-line translations, temporal singularity handled by positive caps. No unregularized spatial distribution theorem is invoked; imported theorem's `N₁` hypothesis is not waived for the parts that remain imported.
- **BR02 — FULLY_CHECKED.** Factorization, `ℓ¹` norm 1, inner product `exp(−λ|t−s|)`, product feature measure, phase `exp(iξ·x)`, Fourier convention, `m_L=ν_cap·μ_mass` all verified. No stochastic field or probability space is constructed (correctly, and explicitly stated).
- **BR03 — FULLY_CHECKED.** Strong measurability, norm continuity, separable/bounded range, Bochner integrability, absolute scalar/Bochner Fubini bound, linear-first inner product, positivity of `Q_L`, and no division by zero all verified; zero-mass cases handled.
- **BR04 — FULLY_CHECKED.** Common-translation invariance and the two different-origin cross bound verified; separate self-norm invariance and retained cross offsets are correct; every sign checked; no cross-kernel PSD claim.
- **BR05 — FULLY_CHECKED.** Bounded compact truncations, monotone convergence before/after translation, nonnegativity of `γ` driving integrand monotonicity, finite `N_C` controlling the cross limit, and survival of both invariance and the inequality through `L→∞` all verified. No pointwise spatial-mollifier monotonicity is asserted.
- **BR06 — FULLY_CHECKED.** Predecessors in their own chains (one-vertex second chain uses its own root `(0,0)`, not the first chain's terminal vertex); empty chain has no interchain Case-2 pair; the original final-pair integral matches the translated tests; printed page 21 retains `a,b` in the spatial test arguments and drops only the prior-time difference. Verified against held page 21 text.
- **BR07 — FULLY_CHECKED.** Source (3.1)–(3.5) p.14, Theorem 3.1/(3.6) p.15, and Case 2 p.21 read in context; independent-`y` (B12) is explicitly distinguished from the printed repeated-`x`, not falsely quoted; the bridge supplies exactly the needed `Q₂` covariance estimate, leaving other induction steps imported, not newly certified.
- **BR08 — FULLY_CHECKED.** `μ_e=exp(−(ε_j+ε_h)|ξ|²/2)μ_original` with radial-ball finite mass and `b^{-α/2}` factor; `γ_e=p_{(ε_j+ε_h)}*Γ≥0`; `ν_e` normalized and cap-finite; damped Green `N₀=θ^{-2}`, `N₂` finite via `L:damped-homogeneous-norms`; Green smoothing initially in d=3. No new unregularized or random-operator-norm claim.
- **BR09 — FULLY_CHECKED.** The listed consumers (`L:joint-fixed-order`, `L:crude-corrected`, `L:vertex-crude`, `P:envelope`) do use Theorem 3.1 and get exactly the Case-2 step supplied; constant one adds no `Q₂`/origin factor; the `Q₁` factor 2 and existing constants/`θ` choices are preserved; cap/Green/spatial removal order retained; transitive Jensen/mixed/full-upper use is not circular and no first-moment or intrinsic constant is used to prove the bridge.
- **BR10 — FULLY_CHECKED.** All three falsification mechanisms recomputed and correct (negative shifted cross kernel, non-invariance under independent translation, non-monotone spatial smoothing), plus constant-one attainment and smallest independent-root Case 2. Controls test mechanisms and do not replace the proof.
- **BR11 — FULLY_CHECKED (semantic).** Proposed placement immediately after `L:damped-homogeneous-norms` and before the joint setup is semantically correct; proposed labels do not collide with anything in the supplied excerpt; direct consumers and scope are correctly identified; plan explicitly keeps integration/build unclaimed and preserves old obligations while adding the new proof (214 total). Exact raw line numbers and byte-identity remain integration-time re-checks (N1/N2), not plan defects.
- **BR12 — FULLY_CHECKED.** No required mathematical repair or missing hypothesis for the new proof/application/plan. Mathematics is distinguished from source-image/final-cold/global and future transcription/build gates; GPT-authored new material is not a novelty claim; a favorable audit is not production integration or FND closure.

## BRIDGE statuses

- **BRIDGE-LEMMA: FULLY_CHECKED**
- **BRIDGE-APPLICATION: FULLY_CHECKED**
- **BRIDGE-INSERTION-PLAN: FULLY_CHECKED** (plan correctness; completed integration/build remains a separate gate)

## One-line summary

The GPT-authored translated-covariance Cauchy–Schwarz bridge is mathematically correct with constant exactly one, applies faithfully to the source's Case 2 (correcting the dropped prior-time difference without the false equality), and its insertion plan is coherent; no mathematical fix is required, while line-number re-resolution, rebuild/render, source-image, and final cold/FND gates remain open.