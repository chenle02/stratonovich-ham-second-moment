# Review Result — deepseek

- category: paper-review-deepseek
- model: deepseek/deepseek-v4-pro
- verdict: PASS_WITH_NOTES
- confidence: HIGH

## Critical findings

None invalidating the conditional deduction. The statement is a hypothesis-to-conclusion sufficiency claim (U1–U6 ⇒ proposed conclusion). With the exact quantifiers written in `candidate.json`, the radial/tail/bulk argument closes without a hidden lower bound, without assuming an optimizer, and without a diagonal B(δ) limit. The two genuine gate risks — (i) whether the Gaussian scaling legitimately invokes classical Borell enlargement and (ii) whether the growing cutoff error `e_B → 0` is the correct requirement — are both handled correctly by the frozen text.

## Noncritical findings

1. **Tightness is implicit.** U1 says only "strongly measurable centered Gaussian … finite second norm moment." The Borell application actually needs a tight Radon law and the support = closure of the Cameron image. This follows from separable range plus finite second moment via the inlined `P:tube-wiener-realization`, but if U1 is read in isolation the hypothesis hiding the realization theorem is invisible. Recommend a one-line cross-reference rather than a stronger hypothesis.

2. **Wording of the parameter line.** Line 6 says "Constants listed here do not depend on delta or B," yet `eta_B`, `C*B^s`, and `R_B` are visibly B-dependent. The correct reading is "A0,C,c0,c1,p,nu,s are fixed; eta_B is fixed once B is fixed." This is a spelling issue, not a logic error, but it invites misreading.

3. **Model-specific U5/U6 are external content.** The abstract deduction is nearly tautological once U5/U6 are granted; the scientific load is carried by the wave-specific deterministic envelope and the uniform residual bound. The inlined contexts support `s = 3ν` and a sup-over-R envelope, but the full proof of `P:uniform-arbitrary-residual` is not inlined, so U6's `e_B → 0` for the wave model remains an input from outside this packet. This is acknowledged in the target and is not a completeness defect of the conditional statement itself.

4. **`nu = 1` and `nu = 2` are excluded for good reason, but the text never flags why `nu = 2` would break only the tail.** At `nu = 2` the condition `4C B^s ≤ R_B^{2−nu}` degenerates independent of k, and the boundary `nu = 1` is excluded to make the weighted power means used in the envelope clean. Worth one sentence of documentation.

## Checked derivations

**H01 — Gaussian/Cameron scaling and Borel envelope.** With `E[X W(h)] = sqrt(δ) M h`, the Cameron ball is `K = C(B_H(1)) = sqrt(δ) M(B_H(1))`, so the tube `A + M(B_H(r)) = A + (r/sqrt(δ))K`. Borell with `t = r/sqrt(δ)`, `â = Φ_N^{-1}(μ(A)) ≥ 0` (because `b = 2E||X||` forces `μ(A) ≥ 1/2`), gives `P(d(X)>r) ≤ Φ_N(â+t) ≤ e^{-t²/2} = e^{-r²/(2δ)}`. The Rayleigh dominator has density `(r/δ)e^{-r²/(2δ)}` and survival `e^{-r²/(2δ)}`. The transferred exponent is exactly `(G(r) − r²/2)/δ`. Signs and scales check; no lost constant.

**H02 — Upper moment finiteness without assumed finiteness.** U3 explicitly forbids assuming `E exp(F/δ) < ∞`, and the proof does not. On `[0,R_B]` the integral is `(R_B²/(2δ)) e^{(S+E)/δ}`, finite because U6 makes `E_{δ,B}` finite. On `[R_B,∞)` the U5 bound `G(r) ≤ A0 + C B^s r^ν + η_B b^ν` with `ν < 2` makes the exponent `−r²/(2δ)(1+o(1))`, hence integrable; the explicit tail gives a finite bound. So finiteness is deduced, not assumed.

**H03 — Zero-law ordered `e_B` condition.** For a zero law (`M=0`, `b=0`, `J≥0`, `J(0)=0`, `H={0}`), U6 collapses to `E_{δ,B} = max(0,F(0))`. The clause correctly requires only `e_B = limsup_δ max(0,F(0))` finite with `e_B → 0`, not `e_B = 0` at every fixed B. The sanity family `F(0)=1/B, Z=1, A0=1, C=η=0, p=1, s=0` satisfies U1–U6 with `e_B = 1/B`, and the conclusion reduces to `0 ≤ 0`. It is correctly preserved.

**H04 — `R_delta` indexing vs. fixed-R estimates.** U6 requires *one* polynomial cutoff `R_B = c B^k` with `k > s/(2−ν)` and `e_B → 0`; fixed-ball convergence is explicitly marked insufficient. The `radius_application_clause` is mathematically correct: any `sup_{R≥1}` estimate with δ-independent constants is stronger and suffices by restriction to `R = R_δ`, while estimates proved only at each fixed R do not verify U5/U6 along a localization absorbed into `F,M,V`. The inlined `L:signed-score-envelope` supplies the uniform-in-R envelope, so the instantiation is consistent.

**H05 — Growing cutoff, subquadratic tail, ordered limits.** The cutoff condition `4C B^s ≤ R_B^{2−ν}` holds eventually because `k(2−ν) − s > 0`, and `R_B → ∞` since `k > 0`. The needed `ν∈(1,2)` is in the parameter block. The order is δ → 0 at fixed B, then B → ∞; B-independence of `Z_delta` (U3) is exactly what makes the left side B-free. The normalizers `δ log(R_B²/(2δ)) → 0` and `δ log 4 → 0` vanish; no diagonal B(δ) limit is used.

**H06 — Sanity model and the four falsification boundaries.** All four check out.
- Sanity model: `E e^{a|W|/√δ} = 2 e^{a²/(2δ)} Φ(a/√δ)`, normalized limit `a²/2`, and `S_δ = sup_h(a|h| − h²/2) = a²/2`; envelope and `e_B = 0` hold for δ small.
- F1: `A = [[0,1],[1,0]]` has `det A = −1` and `tr A = 0`, so `det P(t) = e^{t·tr A} = 1`; eigenvalues ±1 give `||exp(tA)|| = e^t`; the phase `(1,−1)` is the −1-eigenvector and decays as `e^{-t}`. Sign and determinants verify.
- F2: `E_B(M) = M^{3/2}/B → 0` at fixed M, but `E_B(B^{10}) = B^{15}/B = B^{14}`, while tail dominance `k(2−ν) − s = 1/2 > 0`. This exactly demonstrates why fixed-ball convergence is insufficient and why a growing cutoff is mandatory.
- F3: `Γ(4) − 4^{-1/2}Γ(1) = (√2 − 1)/2 > 0`; arithmetic correct, refuting largest-order homogeneous inheritance.
- F4: `J_n(e_n) = 1` gives `S_n ≥ 1/2` while the pointwise limit score is 0, with norm-bounded optima; correct failure of sup/limit interchange.

**H07 — Independence from positive scores / no hidden claims.** The bulk step uses only `F − ρ²/2 ≤ (F − pJ) + (pJ − ||h||²/2) ≤ E_{δ,B} + S_δ`. No optimizer, no attainment, no lower bound `Z ≥ 1`, no identification of `S_δ` with a variational limit, and no covariance-mixture step is required. The target explicitly disclaims lower terminal-observable and exact-score identification. The conclusion is a genuine upper bound only.

**H08 — Remaining defects and scope qualifications.** The target correctly lists what is not supplied: lower-displacement bound, identification of `limsup S_δ`, unmasked noisy wave group, mixture asymptotics, and novelty. The named Borell input is treated as a source-proof-cleared import; no in-project verification of its original edition exists in the packet, which is recorded as a limitation, not a reason to fail the conditional audit.

## Required fixes before production gate

1. Add one sentence under U1 cross-referencing the realization/tightness proposition (`P:tube-wiener-realization`) so the Radon-law and support hypotheses are not silently buried.
2. Rephrase the "constants do not depend on delta or B" line to state explicitly that `A0,C,c0,c1` are fixed while `eta_B`, `B^s`, and `R_B` are B-dependent with `eta_B` fixed per B.
3. State the existential B-link in the conclusion: finiteness holds for δ small enough after fixing any B with `4C B^s ≤ R_B^{2−ν}`; this is already true but understated.
4. Document that the wave-model instantiation with `p = 2, s = 3ν` and `e_B → 0` is model-specific content outside the abstract hypothesis half; do not present the abstract statement as proving wave p-moment for other p.
5. Add a note on why `ν=1` and `ν=2` are excluded (power-mean legality at `ν=1`; degenerate tail at `ν=2`).

## One-line summary

The conditional statement U1–U6 ⇒ proposed conclusion is mathematically sound under the frozen quantifiers, with correct Gaussian/Borell scaling, finiteness, zero-law ordering, growing-cutoff error, sanity/boundary checks, and an honest upper-bound-only scope; the sole caveat is that U5/U6 for the actual wave model are external deterministic inputs whose full proof is not inlined.