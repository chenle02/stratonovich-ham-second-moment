# Review Result — deepseek

- category: paper-review-deepseek
- model: deepseek/deepseek-v4-pro
- verdict: PASS_WITH_NOTES
- confidence: MEDIUM

## Critical findings

No blocking mathematical defect found in the three assigned proofs (PROOF101 `L:masked-chain-comparison`, PROOF102 `P:masked-source-moments`, PROOF103 `P:masked-canonical-transfer`). Signs, boundary terms, ordering conventions, and the final coefficients were checked and found consistent. The main caveat is not a fault in the three proofs themselves: they lean on two substantial supplied lemmas (`L:joint-fixed-order`, `L:vertex-crude`) and on the imported source pairing bound (Chen Theorem 3.1). Those lemma bodies are supplied in `constructor-model.tex` and were read and spot-checked at each use, but I did not re-derive every estimate line-by-line, so my verdict treats those as verified interfaces rather than as independent reconstructions.

## Noncritical findings

1. **PROOF101, Green smoothing with masks (LF 70–84).** The Green-width identification cites `L:joint-fixed-order`, whose proof handles the unmasked/smoothed cross-moment convergence. The deterministic factor `∏m(z_i)` must be carried through that weak-convergence passage; this is harmless because `m∈C_c^∞([0,1])` is bounded continuous, but it is left implicit rather than stated as an addendum to the cited lemma.
2. **PROOF102, uniqueness cone (LF 127–138).** The Picard majorant `M^n T^{2n}/(2n)!` and the difference-iteration bound `B M^n T^{2n}/(2n)!` are correct, but the nested-cone enlargement and the compact-exhaustion of `R^d` are compressed. The argument is standard and valid; it is not a defect, only a terseness.
3. **PROOF102, products of partial sums (LF 148–154).** The `L^1` convergence is asserted; the justification (Cauchy–Schwarz with `‖U−u‖₂‖U_M‖₂` plus the `Q_t²` double-sum budget) is straightforward but not spelled out.
4. **PROOF103, reversal bijection (LF 189–194).** The pairing relabeling `{i,j}↦{r(i),r(j)}` and the verification that the reversed chains land in the `P:mixed` initial-root convention are stated correctly but tersely; for cross-pairings between the two chains the notation obscures a routine bookkeeping step.
5. **External dependency not fully re-derived.** Chen `(2.19)` Wick formula, `(2.13)–(2.16)`/Theorem 4.1, and Theorem 3.1 `(3.6)` are quoted imports; they were checked against the embedded `chen-author.txt` excerpts (PDF text layer, formulas possibly garbled per `source-manifest.md`) but not visually certified from page images. This is recorded as a tracking limitation, not a suspected error.

## Checked derivations

**PROOF101 — CHECKED.** Chain measure `ν_n^{t,x}` with backward spatial factors `G_d(s_{j+1}−s_j,dz_j)`, `s_{n+1}=t`; recursion `f_n(t)=∫_0^t(t−r)f_{n−1}(r)dr` gives `ν_n^{t,x}(1)=t^{2n}/(2n)!` (verified `n=1,2`). Covariance upper bound `c_ρ=K_η(0)Γ_{2ε}(0)<∞` for `ρ=(ε,η)>0`, with `K_η(v)` a Laplace mixture and `Γ_{2ε}(x−y)=∫e^{iξ·(x−y)}e^{−ε|ξ|²}μ(dξ)` nonnegative. Bochner integrability follows from Gaussian/Wick moment bounds and continuity of `Y_ρ`. The pair-partition comparison is exact: a fixed pairing `D` contributes `∫∏_{pairs}C_ρ d(ν⊗ν)`, and the masked version multiplies by `∏_{i=1}^{2l}m(z_i)∈[0,1]` with each vertex counted once, hence `0≤masked≤unmasked` termwise. Odd total order vanishes by Wick centering; `n=k=0` gives both sides 1. Setting `k=n, y=x` and using `L:vertex-crude` (width-uniform `q_n`) yields both `L²` bounds. No wrong constant found.

**PROOF102 — CHECKED.** `Q_T=Σq_n(T)<∞` from `L:vertex-crude` ratio summability. `M^nT^{2n}/(2n)!` matches the chain mass recursion (factor `2n` in the factorial is correct for a `G`-convolution iterate). Continuity of Picard terms via unit-time Green representation; summing the Volterra recursion gives the ordinary mild equation with data `(1,0)`. Uniqueness among locally continuous ordinary mild solutions uses the homogeneous difference iteration with `(2n)!` decay; no weak/rough-SPDE uniqueness is claimed. Bochner term = pathwise chain integral at fixed terminal via ordinary Fubini and integrable source products; an a.s. subsequence of `L²` partial sums matches the continuous Picard version. The two-point inequality passes through `L^1` product convergence, backed by `Σ_{n,k}E|X_nX_k|≤Q_t²`. Unmasked spatial stationarity (finite Picard integrals commute with translations; `L²` limits inherit it) plus Cauchy–Schwarz gives `E[u_ρ(t,x)u_ρ(t,y)]≤E|u_ρ(t,0)|²` *without* masked stationarity. The Bochner average uses `L²` spatial continuity, a separable image, and the `‖φ‖₁²Q_t²` Fubini budget with `φ≥0`; integrating the two-point bound against `φ(x)φ(y)` gives the `‖φ‖₁²E|u_ρ(t,0)|²` budget (coefficient `‖φ‖₁²`, not a pointwise trace).

**PROOF103 — CHECKED.** The common-width source law at fixed order is exactly the `L:joint-fixed-order` vertexwise law. Reversing both chains at terminal `(t,0)` by `s'_j=t−s_{n+1−j}`, `z'_j=−z_{n+1−j}` preserves Green increments (even in space) and covariance differences (even `K_η`, `Γ_{2ε}`); relabeling maps pairings to the `P:mixed` initial-root convention, including empty/unequal chains. Termwise `E[X_{ρ,n}X_{ρ,k}]→E[X_nX_k]` at fixed `n,k`. The double tail is dominated by `q_n(t)q_k(t)` (summable to `Q_t²`), giving the finite-square/δ argument; `P:mixed` identifies the canonical sum, proving the unmasked point-moment limit at arbitrary relative width rates. The conditional transfer uses `|E|B|²−E|A|²|≤‖B−A‖₂(‖B‖₂+‖A‖₂)` and the limit of `E|u_ρ(t,0)|²`; masked-average `L²` convergence is kept as an explicit premise. No circular final-constant use, no operator-path/Skorohod import, no new pathwise realization.

**Proof statuses:** PROOF101 = CHECKED; PROOF102 = CHECKED; PROOF103 = CHECKED (each with the minor cautions above).

## Required fixes before production gate

None blocking. Recommended non-gating clarifications: (a) state explicitly that the deterministic mask factor passes through the `L:joint-fixed-order` Green-smoothing convergence; (b) spell out the nested-cone/exhaustion step in PROOF102’s uniqueness; (c) one line of justification for `L^1` convergence of products of partial sums; (d) spell out the pairing bijection for cross-pairings in PROOF103’s reversal. These improve auditability but do not affect correctness of the three scoped proofs.

**MASK01 — PASS.** `H:homog` (nonnegative, even, PD tempered Radon `Γ`, `d∈{1,2,3}`, `α₀+α<2`, `α∈(0,d)` or `α=d=1` incl. white), data `(1,0)`, `m∈C_c^∞`, `0≤m≤1` after regularization; `ρ=(ε,η)`, `C_ρ=K_η·Γ_{2ε}`, `c_ρ` finite nonnegative; widths `ε+ε′` and Laplace *prefix* (not convolution) verified; retaining `J` not asserted `W`-measurable; no Gaussian-nonlinear-solution assumption.

**MASK02 — PASS.** Backwards terminal chain measure, mass `t^{2n}/(2n)!`, unit-time dilation measurability, sphere-vs-density in `d=3`, strong measurability/separability, Gaussian moment/Fubini bounds, empty-chain conventions all present; no illegal stationarity/coupling identity.

**MASK03 — PASS.** All pair partitions incl. self-pairings and unequal/empty orders; coefficient per pairing exactly 1; odd-zero; mask factor once per vertex; termwise comparison at same `t`, arbitrary `x,y`; positive Green approximate-identity and Green-before-noise convention matched to `L:joint-fixed-order`; `q_n` matched to `L:vertex-crude`.

**MASK04 — PASS.** Local bound `M` on compact backward cone, explicit `M^nT^{2n}/(2n)!` majorant, term continuity, local continuity/spatially-unbounded-source allowed, uniqueness only among locally continuous ordinary mild solutions, data `(1,0)` both entries; no weak/rough uniqueness claim. (Nested-cone detail compressed but sound.)

**MASK05 — PASS.** Ordinary Fubini vs Bochner terms; integrable source products; pointwise identification by `L²` subsequence at each terminal point; continuous version via dense-point patching; one event per fixed `ρ`; width-uniform estimates are not promoted to an all-`ρ` path event.

**MASK06 — PASS.** Double mixed sum `≤Q_t²`; products `L¹`-convergent; unmasked stationarity after Picard limit; Cauchy–Schwarz offdiagonal bound without masked stationarity; Bochner average via `L²` spatial continuity + separable image; budget `‖φ‖₁²Q_t²`; `φ≥0` prerequisite; zero-order/zero-`Γ`/zero-mask/`φ=0` cases consistent; no Sobolev phase point trace.

**MASK07 — PASS.** Same terminal `(t,0)` reversal on both chains; pairing relabel exact; no unequal-terminal unshifted covariance; Green-first and arbitrary relative width rates; `q_nq_k` summable majorant and finite-square tail; no false same-space `L²` convergence of the whole family or new pathwise realization.

**MASK08 — PASS.** Masked-average `L²` limit is an honest premise; second-moment convergence inequality verified; same-width/sequence limits matched to the unmasked point-moment limit; `P:constant-raw-average` uses the genuine `L^p` tested limit and identifies Bochner/ordinary averages at fixed mask/horizon; fast-source/cone consumers use fixed `δ`, correct amplitude `g=δ^{(1−a)/2}` and `τ/δ` temporal-width normalization; no improper uniformity or smuggled global-flow conclusion.

**MASK09 — PASS.** By-hand checks: `n=k=0` (=1), `n+k` odd (=0), `n=k=1` masked comparison, `n=0,k=2` self-pairing, `m=0`/`m≡1` comparator, `φ` nonnegative/zero scope, `Γ=0`, `d=3` sphere, `d=1` white; `c_ρ→∞` as widths vanish is separated from width-uniform `q_n`; `Q_T` finite; local `M` sample-dependent; two distinct spatial terminals at the same `t` need no single-root reversal (two chain measures), and unequal terminal *times* would need a shifted covariance, which the target never asserts.

**MASK10 — PASS.** All three proofs reconstructed from the supplied text; scalar-source/constructor path is honored and operator-path conclusions (`P:source-gaussian-transfer`, driver paths) are not consumed by 101–103; downstream conditional use is sound; no circular final-constant premise, no source correction, no Skorohod result; full-213/global/source-image/cold gates remain unclaimed.

## One-line summary

The three fixed-mask displacement-moment proofs are logically sound with correct constants and ordering conventions, relying legitimately on the supplied `L:joint-fixed-order`/`L:vertex-crude` interfaces; only minor compression of standard cone/uniqueness/smoothing details remains, and nothing blocks the production gate.