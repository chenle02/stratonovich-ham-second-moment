# Review Result — deepseek

- category: paper-review-deepseek
- model: deepseek/deepseek-v4-pro
- verdict: PASS_WITH_NOTES
- confidence: MEDIUM

## Critical findings

None. I found no false identity, wrong sign, broken boundary term, or incorrect final coefficient among PROOF112–118. The seven proofs are internally coherent and the referenced external statements (Teschl 10.2/10.13/4.12/4.13; Friz–Hairer Young (4.3)) match the embedded text carriers within OCR limits.

One load-bearing point was checked most carefully and survives: the full-phase complement identity in PROOF116 (the subtraction of the growing constant-response via the tail integral) is exact — the `(1+t−r)(1+r)` integral is `t + t² + t³/6`, and the rate-gap normalization `e^{-λt}e^{μt} = e^{-(λ−μ)t}` uses `λ−μ ≥ d₀` with no division by `μ`.

## Noncritical findings

1. **PROOF113 dual-norm wording.** The dual of the norm `‖A_σ^{1/4}u‖` is stated for `z ∈ L²`. Strictly, the dual space is the completion `D(A_σ^{-1/4}) = H^{-1/2}`, and `‖A_σ^{-1/4}z‖` is infinite for general `z ∈ L²`. The argument is correct after completion (Cauchy–Schwarz gives the upper bound on `D(A^{-1/4})`; `u = A_σ^{-1/2}z` attains it for `z` in the completing class), but the sentence as printed is imprecise.

2. **PROOF114 graph-level bookkeeping is terse.** The claim that the spectral matrix gives continuous `H²×H¹` solutions is correct but the displayed step is compressed. The key bound is that `h ↦ √(h+c)·sin(t√h)/√h` (i.e. `A_σ^{1/2}S_t(H_σ)`) is bounded uniformly in `h ≥ −M` by `C(1+t)`, which makes `S_t(H_σ)` map `H¹ → H²`; this is not written out in the manuscript.

3. **Primary-image certification absent.** Teschl and Friz–Hairer pinpoints were verified against the OCR text carriers only (pp. 140–141 max–min, p. 258 Thm 10.2, p. 273 Thm 10.13; Friz–Hairer (4.3) on p. 62). No rendered page images are in this snapshot, so typography-level pinpoints remain uncertified. This is a custody/evidence limitation, not a mathematical defect.

4. **PROOF117/118 rely on the raw covariance completion.** The identities `E W(Ψ)W(F₀) = ∫F₀(s,x)h_s(x) dx ds` and `v_Ψ = E Z²` are quoted from the covariance/raw-no