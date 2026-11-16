# Review Result
Category: proof-readability-equivalence
Model: deepseek-v4-pro
Verdict: PASS
Confidence: high

## L:exact-canonical-scaling

- Old reading: COMPLETE
- New reading: COMPLETE
- Public reconstruction: COMPLETE
- Argument preservation: PRESERVED
- New explanations: JUSTIFIED

### Statement comparison (OLD/NEW LF 10–30)

The lemma statement is byte-identical in content across the two revisions. Both carry: `a = α_0`, `κ = (4−α−a)/(3−α)`, `δ = T^{−κ}`, `r_T = Tδ = T^{(a−1)/(3−α)}`; the fast equation `δ²∂_t²V_δ = ΔV_δ + √δ·W·V_δ` (`E:exact-fast-equation`) with data `(1,0)`; the identity `T^{−κ}log E|u(T,0)|² = δ log E|V_δ(1,0)|²` (`E:exact-moment-scaling`); and the qualifier that the assertion is equality in law, assuming no pathwise uniqueness for a full rough solution. No statement text changed.

### Proof comparison (OLD proof LF 32–62; NEW proof LF 32–86)

Sentence-by-sentence, every OLD sentence survives verbatim in NEW, in order. The only changes are additions: (i) an orienting roadmap plus `Step 1.`/`Step 2.` headers; (ii) three explanatory sentences documented below; (iii) the concluding sentence “Finally, evaluate the law identity at `t=1,x=0` …” The byte delta (2925 → 4003) is fully accounted for by these additions; no deletion was detected. SHA256 change is expected from these insertions.

### Original-step coverage (with public working)

The target proof has seven logical steps. Each is reconstructed below; both revisions contain all seven, and the working is supplied here from first principles (not by quoting OLD).

**Step 0 — parameter consistency (statement, unchanged).**
From `(3−α)κ = 4−α−a` and `δ = T^{−κ}`:
```
r_T = Tδ = T^{1−κ} = T^{1−(4−α−a)/(3−α)} = T^{(3−α−4+α+a)/(3−α)} = T^{(a−1)/(3−α)}.
```
Hence the two displayed definitions of `r_T` agree. All powers below are positive real powers, valid since `T > 0`, `δ > 0`, `r_T > 0`, `α ∈ (0,d)`, `a ∈ (0,1)`.

**Step 1 — dilated source covariance amplitude `T^{−a}r_T^{−α}`.**
```
Cov(W(Tt,r_Tx), W(Ts,r_Ty))
  = |Tt−Ts|^{−a} γ(r_T x − r_T y)
  = T^{−a}|t−s|^{−a} · γ(r_T(x−y)).
```
Under Hypothesis `H:homog`, the Radon-measure homogeneity `Γ(cA) = c^{d−α}Γ(A)` is the distribution-level statement `γ(r_T z) = r_T^{−α}γ(z)`. For spatial white noise `Γ = δ_0` (admitted when `α = d = 1`), the same mass computation gives `δ_0(r_T z) = δ_0(z) = r_T^{0}·1`, matching `α = d`. Therefore the covariance amplitude of the dilated field is `T^{−a}r_T^{−α}`, and a single Gaussian factor carries the square root `T^{−a/2}r_T^{−α/2}`. This is the “covariance amplitude versus noise amplitude” distinction the task asks to verify: the proof correctly scales covariance by `T^{−a}r_T^{−α}` and the per-vertex field factor by its square root, never confusing them.

**Step 2 — cutoff/width transforms (unchanged sentence).**
Temporal Laplace prefix: with `K_η(v) = (1/Γ_E(a))∫_0^{η^{-1}} e^{−λ|v|} λ^{a−1} dλ` (context `P:source-canonical-convergence`),
```
K_η(Ts) = (1/Γ_E(a))∫_0^{η^{-1}} e^{−λT|s|} λ^{a−1} dλ
        = (1/Γ_E(a))∫_0^{T/η} e^{−λ'|s|} (λ'/T)^{a−1} dλ'/T   (λ' = λT)
        = T^{−a} K_{η/T}(s).
```
Spatial heat width: `p_ε(r_T z) = (2πε)^{−d/2}e^{−r_T²|z|²/(2ε)} = r_T^{−d} p_{ε/r_T²}(z)`, so the width becomes `ε ↦ ε/r_T²`. Summed-space width: writing `Γ_e = p_e * Γ` and using measure homogeneity `Γ(r_T dy') = r_T^{d−α}Γ(dy')`,
```
Γ_{ε+ε'}(r_T z) = ∫ p_{ε+ε'}(r_T z − y)Γ(dy)
                = ∫ r_T^{−d} p_{(ε+ε')/r_T²}(z − y') r_T^{d−α} Γ(dy')
                = r_T^{−α} Γ_{(ε+ε')/r_T²}(z).
```
Hence the joint maximum-time width (`η,η' ↦ max(η,η')/T`) and summed-space width (`ε+ε' ↦ (ε+ε')/r_T²`) laws are preserved at every vertex, as claimed.

**Step 3 — Green measure scaling.**
The claimed identity `G_d(Tτ, r_T dz) = r_T G_d(τ/δ, dz)` is equivalent (λ = T, μ = r_T, λ/μ = T/r_T = 1/δ) to `G_d(λt, μ dz) = μ G_d((λ/μ)t, dz)`. This follows from the function-level degree `1−d` homogeneity `G_d(t, μx) = μ^{1−d}G_d(t/μ, x)` after accounting for the measure pushforward under `z ↦ μz`, which contributes `μ^d`. Direct verification in all three dimensions:
- d = 1: `G_1(t,dz) = ½ 1_{|z|≤t} dz`; `G_1(λt, μdz) = μ·½ 1_{|z|≤λt/μ} dz = μ G_1((λ/μ)t, dz)`.
- d = 2: `G_2(t,dz) = (2π)^{-1}(t²−|z|²)_+^{-1/2} dz`; `G_2(λt, μdz) = μ²(2π)^{-1}[(λt)²−μ²|z|²]_+^{-1/2} μ^{-1} dz = μ G_2((λ/μ)t, dz)`; mass `λt` is preserved.
- d = 3: `G_3(t,dz) = (4πt)^{-1} σ_t(dz)`, `σ_t` surface measure on the radius-`t` sphere. `σ_{λt}(μB) = μ² σ_{λt/μ}(B)`, so `G_3(λt, μdz)(B) = σ_{λt}(μB)/(4πλt) = μ²σ_{λt/μ}(B)/(4πλt) = μ G_3((λ/μ)t, dz)(B)`. The sphere measure in `d = 3` is thereby included, as claimed.

**Step 4 — per-vertex factor and the two power identities.**
Each of the `n` vertices contributes one time Jacobian `T`, one Green scaling `r_T`, and one noise square root `T^{−a/2}r_T^{−α/2}`, so the vertex coefficient is `T^{1−a/2}r_T^{1−α/2}`. Then:
```
T^{1−a/2} r_T^{1−α/2} = T^{1−a/2}(Tδ)^{1−α/2} = T^{2−(a+α)/2} δ^{1−α/2}.
```
Setting this equal to `δ^{−1/2}` requires `T^{2−(a+α)/2} δ^{3/2−α/2} = 1`, i.e., with `δ = T^{−κ}`, `2−(a+α)/2 = κ(3/2−α/2) ⟺ 4−a−α = κ(3−α)`, which is exactly the definition of `κ`. Hence `T^{1−a/2}r_T^{1−α/2} = δ^{−1/2}`. Multiplying by `δ = r_T/T`:
```
δ · T^{1−a/2}r_T^{1−α/2} = T^{−a/2} r_T^{2−α/2} = δ^{1/2} = √δ.
```
Both identities displayed in the proof are confirmed; the second is the per-vertex (Green-propagator) factor, the first is the companion noise-amplitude identity.

**Step 5 — match with the fast equation.**
For `δ²∂_t²V = ΔV + F`, the Green kernel is `K(τ,·) = δ^{−1}G_d(τ/δ,·)`. Verify at measure level: `δ²∂_τ²K − ΔK = δ^{−1}(G_d'' − ΔG_d)(τ/δ,·) = δ^{−1}δ_{(τ/δ,·)}`; since the measure `δ_{(τ/δ)}` has mass `δ` (i.e. `= δ·δ_{(τ)}`), this equals `δ_{(τ,·)}`. Therefore `K` is the correct fundamental kernel. With noise `√δ·W`, each vertex contributes `δ^{−1}·√δ = δ^{−1/2}`, exactly matching the dilated original vertex factor. Hence the fixed-order coefficient laws coincide at every vertex.

**Step 6 — fixed-order joint laws and passage to the canonical series.**
Since the vertex factors and the vertexwise width laws match, every finite list of fixed-order coefficients has the same joint law under the dilation (self-pairings, unequal orders, empty chains all included: the two-chain pairing convention `P:mixed` admits `m ≠ n` and `n = 0`, and `L:joint-fixed-order` covers unequal and empty chains). Passing to the full series uses `L:joint-fixed-order` (joint `L²` limits, Green smoothing removed before noise smoothing, width divided by `r_T²` on the scaled side in `d = 3`) together with the absolute `L²` summability of `L:vertex-crude`. Publicly: equality in law of every finite sub-vector of coefficients plus `L²`/in-probability convergence of partial sums implies equality in law of the infinite-series limits; and for the second moment, `E|ΣX_n|² = Σ_{m,n}E[X_mX_n]` by the Cauchy–Schwarz cross-term majorant `q_m q_n` and the summable tail `Σ√(n+1)q_n < ∞`, identically on both sides. The fast-equation coefficients inherit finite `L²` bounds because their fixed-order laws equal those of the dilated original coefficients, whose `L²` norms are bounded at fixed geometric scale by `q_n` of `L:vertex-crude`. No large-time/source limit exchange occurs: everything is at fixed finite `T` and fixed `δ > 0`, and the sentence “No large-time and source limit are interchanged” is retained verbatim.

**Step 7 — logarithmic moment identity.**
Evaluating the law identity `u(Tt,r_Tx) =_d V_δ(t,x)` at `t = 1`, `x = 0` gives `u(T,0) =_d V_δ(1,0)`, hence `E|u(T,0)|² = E|V_δ(1,0)|²` and `log E|u(T,0)|² = log E|V_δ(1,0)|²` (both moments ≥ 1, since the order-zero term is `1` and all other terms are centered, so the logs are finite). Multiplying by `δ` and using `δ = T^{−κ}` gives `T^{−κ}log E|u(T,0)|² = δ log E|V_δ(1,0)|²`, i.e. `E:exact-moment-scaling`.

### Justification of the three new explanatory assertions

1. NEW “substituting `r_T = Tδ` and `(3−α)κ = 4−α−a` with `δ = T^{−κ}` gives `T^{1−a/2}r_T^{1−α/2} = δ^{−1/2}`; multiplying by `δ` gives the companion identity.” Verified in Step 4 above: the substitution is the rearrangement of the statement’s own definitions, and `δ·δ^{−1/2} = √δ` together with `δ·T^{1−a/2}r_T^{1−α/2} = T^{−a/2}r_T^{2−α/2}` recovers `T^{−a/2}r_T^{2−α/2} = √δ` exactly. Correct.
2. NEW “At each vertex the time substitution contributes the Jacobian `T`, the Green-measure scaling contributes `r_T`, and the single Gaussian source factor contributes the square root `T^{−a/2}r_T^{−α/2}` of its covariance amplitude.” This is a word-for-word factorization of the unchanged vertex factor `T·r_T·T^{−a/2}r_T^{−α/2}`, and “single … factor” is correct because each vertex carries exactly one noise evaluation. Correct.
3. NEW “Finally, evaluate the law identity at `t = 1, x = 0` and use `T^{−κ} = δ`.” Verified in Step 7 above. Correct, and it merely makes explicit what OLD compressed into “This proves the law assertion and `E:exact-moment-scaling`.”

All three respect the existing domains (`T > 0`, positive real powers) and the fixed-`T`, fixed-`δ` (no limit interchange) structure.

### Evidence summary

- Every OLD proof sentence is present verbatim in NEW; the `√δ`/`δ^{−1/2}` display, the `G_d(Tτ,r_T dz) = r_T G_d(τ/δ,dz)` display, the covariance-amplitude sentence, both cutoff transforms, the Green-before-noise and no-limit-interchange qualifiers are all retained.
- Independent algebra (Steps 0–7 above) reproduces every scalar identity asserted in the target proof from `H:homog` and the definitions of `κ,δ,r_T`; no hidden hypothesis was imported.
- Target consumer uses of `L:joint-fixed-order` and `L:vertex-crude` respect their hypotheses: both require only `H:homog`, which is in force; the `d = 3` Green-before-noise ordering is explicitly honored; the bound transfer to `V_δ` at fixed dilation is justified via fixed-order law identity and law-invariance of `L²` norms (see the pre-existing concern note below).

### Lost steps/qualifiers, unresolved issues, pre-existing concerns

No step or qualifier from OLD is lost; none identified within this read. The following are pre-existing (present identically in both revisions or in the underlying hypothesis), not introduced by the rewrite:

1. **Terse series-passage step.** The transfer of `L:vertex-crude` summability to the fast-equation series is only implicit. It is legitimate (fixed-order law identity makes `‖Y_n‖₂ = ‖X'_n‖₂` with `X'_n` a dilation of the original coefficient at time `T`, bounded by `q_n`-type bounds, and `Σ√(n+1)q_n(T) < ∞` at the fixed finite `T`), but not spelled out.
2. **Zero-covariance degeneracy.** If `Γ = 0`, the homogeneity `Γ(cA) = c^{d−α}Γ(A)` is `0 = 0` for every `α`, so the alpha-parameter entering `κ,δ,r_T` is not pinned by the hypothesis. The lemma nevertheless holds for any admissible `α`: `W = 0` forces `u ≡ 1` and, since `V_δ` with data `(1,0)` and zero noise is also `≡ 1`, the law identity is `1 = 1` and `E:exact-moment-scaling` is `0 = 0`. This is a property of the model hypothesis (`H:homog` allows `Γ = 0` by design), not a defect of the scaling argument.
3. **“Degree `1−d`” phrasing.** The Green-measure scaling hook is brief, but I verified it in `d = 1,2,3` (with the `d = 3` sphere measure explicitly), so no mathematical gap remains within this read.
4. **Fourier normalizations.** The unitary-Fourier caveat is not triggered: this proof invokes no Fourier inversion kernels or `(2π)^d` normalizations; it uses `γ(c·) = c^{−α}γ(·)` directly from `H:homog`, including the `δ_0` white-noise case.

## AUDIT dispositions

No `AUDIT` tokens occur in either revision of this module. No AUDIT-worthy defect is introduced by the rewrite: the three additions are correct and hypothesis-compatible, and no assertion or qualifier was dropped. The pre-existing items above are review notes on brevity/degeneracy, not blockers in the target proof.

## Findings and limits

The rewrite of `L:exact-canonical-scaling` is a faithful readability pass: it partitions the existing argument into numbered steps, adds an orienting sentence, makes the two scalar-power substitutions explicit, and spells out the final evaluation at `t=1, x=0`. All added mathematics was checked against the unchanged definitions of `κ, δ, r_T` and `H:homog` and found correct; the original argument is preserved with no lost steps or qualifiers; equality in law (not pathwise or samplewise identity) is consistently maintained, and no source/large-time limit is exchanged. Scope is limited to this one proof: I did not re-certify the upstream `H:homog`, `P:mixed`, `L:joint-fixed-order`, `L:vertex-crude`, or `P:source-canonical-convergence` arguments beyond verifying that their supplied stated hypotheses cover the uses made here. Context proofs were not counted as reviewed proofs. No primary-source PDF/image rendering, Lean quotation correspondence, or human verification is assessed; no tools, files, network, or delegation were used.
