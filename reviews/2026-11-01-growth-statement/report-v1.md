# Review Result — deepseek

- category: paper-review-deepseek
- model: deepseek/deepseek-v4-pro
- verdict: PASS_WITH_NOTES
- confidence: MEDIUM

## Critical findings

1. **Zero-law guard is only implicit inside U6, not stated as a guard (G02/G06).**
U2 explicitly allows the zero Gaussian law (`support={0}, M=0, b=0`). For `M=0, b=0`, the error in U6 collapses to `E = max(0, sup_{||h||<=R_B} (F(0) - pJ(h))) = max(0, F(0))`, since `J>=0` and `J(0)=0`. Thus `e_B->0` forces exactly `limsup max(0, F(0)) = 0`. This is sufficient for the conclusion, but the candidate never states this collapse. The supplied signed-context instead handles zero covariance by a separate direct argument (`0 <= δ log M_δ <= 2δ log[C(1+δ^{-1})] -> 0`), not by the tube skeleton. If the zero law is retained, the guard `max(0, F(0)) -> 0` must be explicit, otherwise the "zero Gaussian law is allowed" clause hides a hypothesis inside U6.

2. **U6 drops the radius-`R` uniformity present in the source error envelope (G08).**
The framed signed context defines
`E_{δ,B,M} = max(0, sup_{R>=1, ||Φ||<=M, ||x||<=b} [F(x + M_{δ,B,R}Φ) - 2Rate_R(Φ)])`,
i.e. the supremum runs over `R>=1`. The candidate U6 defines
`E = max(0, sup_{||a||<=b, ||h||<=R_B} [F(a+Mh) - pJ(h)])`
with no `R` variable. As an abstract U-theorem this is self-sufficient, but for the claimed paper-I application the actual mean `M_{δ,B,R}` and the stochastic radius `R_δ = δ^{-1}+2` vary with `R`, so U5/U6 must hold uniformly in `R` (and the `R>=1` sup must appear in U6) to be a faithful extraction. Without that, the abstract statement can be adopted but is not yet certified for the wave tuple.

These are not mathematical invalidations of the U1–U6 implication, but they are mandatory edits before the statement is used as a production-gate artifact.

## Noncritical findings

1. **F1 determinant labeling is ambiguous (G07).** With generator `A=[[0,1],[1,0]]`, `det A = -1`, not `1`; the identity `det = 1` holds for the propagator `e^{tA}` because `trace(A)=0`. The candidate writes "phase generator ... determinant1," so it should specify "propagator determinant 1" or correct the generator determinant to `-1`. The refutation itself (operator norm `e^t` vs. displacement `e^{-t}` on the `(1,-1)` eigenvector) is unaffected.

2. **F2's "error grows as B^14" is not derivable from the supplied text (G07/G10).** The exponents `ν=3/2`, `s=3ν=9/2`, `k=10`, and tail-dominance exponent `k(2-ν)-s = 1/2` check out; `fixed_ball_error M^ν/B -> 0` is consistent with the supplied envelopes. But the specific `B^14` growth of the fixed-B error is asserted only in `falsifications.json` ("local Sympy 1.14.0") and no derivation is inlined. Recorded as a limitation; it should be derived or relabeled as an unverified local computation.

3. **Borell input cannot be independently checked.** The set-enlargement bound `μ((A+tK)^c) <= \barΦ_N(â+t)` with `â = Φ_N^{-1}(μ(A))` and `\barΦ_N(y) <= e^{-y^2/2}` is imported from Friz–Hairer, and the primary PDF is not supplied. The application path (Cameron ball `K = √δ M_δ(B_H(1))`, tube `T_r = A + M_δ(B_H(r)) = A + (r/√δ)K`, tail `e^{-r^2/(2δ)}`) is internally consistent. This imported fact is treated as an input per scope, and the limitation is preserved.

4. **Finality claim is stated weaker than what is proved.** Under U5 the Rayleigh integral is finite for every `δ>0`, so `Z_δ` is finite for all `δ`, not only "for δ sufficiently small." Weakness is harmless, but the stronger statement is available and would remove the impression of an unproved small-δ condition.

## Checked derivations

**G01 — actual Gaussian/Cameron scaling and changing Banach spaces: PASS.**
U1 sets `E[X W(h)] = √δ M_{δ,B}h`, so the covariance image is `C = √δ M_{δ,B}` and the Cameron unit ball is `K = √δ M_{δ,B}(B_H(1))`. Then `T_ρ = A + M(B(ρ)) = A + (ρ/√δ)K`, giving `P(d(X) > ρ) <= e^{-ρ²/(2δ)}`. The `δ`-dependent scale is carried correctly; varying `V_{δ,B}` is fine at each fixed pair. No uniform-in-`(δ,B)` Cameron equivalence is required.

**G02 — Borel tube envelope and zero-law guards: PASS with note.**
`b = 2E||X||` gives `μ(A) >= 1/2` by Markov. Compact `M` maps the weakly compact Hilbert ball to a norm-compact closed set, so `T_ρ` is closed, `d` is lower semicontinuous/Borel, and `G(ρ)` is nondecreasing hence Borel; U5 makes each `G(ρ)` finite. Zero law is covered only through the implicit `E = max(0, F(0))` reduction (Critical 1).

**G03 — moment finiteness deduced before assumption: PASS.**
U5 gives `G(ρ) <= A0 + C B^s ρ^ν + η_B b^ν` with `1<ν<2`; hence `∫_0^∞ (ρ/δ) e^{(G(ρ)-ρ²/2)/δ} dρ < ∞` by the subquadratic tail, before any finiteness of `E e^{F/δ}` is assumed. The Rayleigh transfer then bounds the moment; no circularity.

**G04 — one growing cutoff vs. subquadratic tail: PASS.**
With `r>=M`, `1<ν<2`, `C>=0`, `4C <= M^{2-ν}`, the cutoff `Cr^ν - r²/2 <= -M²/8 - r²/8` is correct; `-d/dr[4e^{-r²/(8δ)}] = (r/δ)e^{-r²/(8δ)}` yields the front factor `4` and exponent `A0 - M²/4`. The candidate guard `4 C B^s <= R_B^{2-ν}` from `R_B = c B^k`, `k > s/(2-ν)`, is exactly right; the `F2` caution concerns verifying `e_B->0`, not this algebra.

**G05 — SAME Z_δ and correct δ-first/B-second limits: PASS.**
U3 fixes `Z_δ` independent of `B`. At fixed `B`, `δ log(R_B²/(2δ)) -> 0`; limsup subadditivity gives `limsup_δ δ log Z_δ <= max(V_up + e_B, A0 - R_B²/4)`. Letting `B->∞` with `e_B->0` and `R_B²/4->∞` collapses the max to `V_up = limsup S_δ`. No diagonal `B(δ)` is used; `M_δ>=1` gives the lower bound `0`.

**G06 — no tautological hypothesis or hidden selector: PASS.**
U6 is a deterministic remainder `F - pJ`, not the conclusion restated; U4 expressly assumes no optimizer; the error is an ordinary supremum (finite by U5) with no measurable selecting argument; `G` needs only monotone Borel measurability, not attainment.

**G07 — scalar nonzero sanity model and four falsification boundaries: PASS with note.**
Sanity model checks: `b_δ = 2√(2δ/π)`, `E e^{a|W|/√δ} = 2 e^{a²/(2δ)} Φ(a/√δ)`, normalized limit `a²/2 = S_δ`. F1's operator-vs-displacement counterexample is directionally correct (determinant label caveat above). F2's exponents are consistent, but `B^14` is unverified (limitation). F3: `Γ(4)-4^{-1/2}Γ(1) = (√2-1)/2 > 0` is correct. F4: `J_n(h)=max(0,1-2||h-e_n||)` satisfies `J_n<=1, J_n(0)=0`, converges pointwise to `0`, yet `S_n>=1/2` at `h=e_n`; this correctly refutes naive sup-limit interchange with escaping `l²` directions.

**G08 — faithful extraction, independent of C2/positive-score theorem: PASS with note.**
The U1–U6 skeleton matches the source bulk/tail and same-endpoint ordered-limit architecture; `S_δ` is the own signed score and is never identified with a variational limit or a positive constant; no C2/positive-score theorem enters. The sole infidelity is the dropped `R>=1` sup in U6 (Critical 2).

**G09 — honest mixture/observable/variational exclusions: PASS.**
Scope lines 5 and 65–69 correctly exclude lower observable bounds, exact moving-score limits, unmasked/noisy wave groups, and novelty; `mixture_scope_probe.not_established` is disclosed; F1/F3 are scoped as falsifications of overgeneralized claims, not original-data theorems.

**G10 — complete supplied text and remaining qualifications: PASS.**
All listed qualifications (zero law, imported Borell, no novelty claim, local Sympy scope, Kimi quota) appear; the Bolt/Borell input is treated as imported, not source-certified. No missing external identity claim was found in the inlined material.

## Required fixes before production gate

1. **U6 radius uniformity:** add the `sup_{R>=1}` (or explicit radius-mask uniformity at `R_δ`) to U5/U6, matching `P:signed-moment-bulk-tail`, or formally restrict the abstract statement to a fixed-radius model.
2. **Zero-law guard:** state that for `M=0`, U6 reduces to `E = max(0, F_{δ,B}(0))` and require `limsup_{δ->0} max(0, F_{δ,B}(0)) = 0` (or invoke the separate zero-covariance direct bound).
3. **F1 metadata:** change "determinant1" to `det(generator) = -1`, or explicitly say "propagator determinant 1".
4. **F2:** derive or remove the `B^14` error-growth figure if it is not verifiable from inlined sources; keep the fixed-ball insufficiency warning.
5. **Optional:** strengthen the finiteness conclusion to "all `δ>0`" and cite the exact tail constants (`4`, `-M²/4`) in the skeleton line.

## One-line summary

The frozen abstract U1–U6 transfer is internally sound for both nonzero and zero Gaussian laws and correctly isolates the own signed score, contingent on two production edits: an explicit radius-`R` uniformity clause in U6 and an explicit zero-law `max(0,F(0))->0` guard; verdict PASS_WITH_NOTES.