# Review Result — deepseek

- category: paper-review-deepseek
- model: deepseek/deepseek-v4-pro
- verdict: PASS_WITH_NOTES
- confidence: MEDIUM

## Critical findings

None in the supplied excerpt that invalidates the deduction of a finite full-H1 spatial ratio. The imported-finitude-to-uniform-ratio argument is algebraically correct and avoids the circularities the draft claims to avoid. No proof-killing constant, sign, boundary, scaling, or asymptotic error was found within `candidate.md` lines 1–136.

## Noncritical findings

1. **Text-only source limitation (mandatory statement).** This review is TEXT-ONLY. No visual certification of the Chen 2023 pages is possible from the inlined `pdftotext` packet, which contains OCR artifacts (`FIXME!`, rotated column text, garbled spacing) exactly around Theorem 1.1 and (1.4)/(1.5). The Kimi source-image check is separately assigned and is **not assumed** here. All acceptance of the imported source formula is conditioned on that check.
2. **Unverifiable project claims.** "Citekey chen:23:exponential verified in read-only refdb" and "the main TeX, PDF, 213 proof bodies, 221 statements… remain UNCHANGED" cannot be audited from the excerpt. The unchanged bodies are not inlined, so their independence from this replacement is asserted, not demonstrated here.
3. **d1 white constant is imported, not re-derived.** Line 100 cites "already derived" `E=c^2/6`. My independent check is consistent (see below), but the derivation itself is not in this excerpt; treat as prior result.
4. **Fourier/2π convention.** The d3 plane spectral measure `c/(2π)dξ1 δ0(dξ2)δ0(dξ3)` is correct only under the no-2π-in-exponent convention `Γ=∫e^{iξ·x}μ(dξ)` (matches the source's Bochner convention). The `1/(2π)` factor and hence `Dalang = c/2` are convention-sensitive and cannot be visually re-certified from the extraction.
5. **Unreviewed cross-reference.** Lines 37–38, asserting the imported kinetic coefficient 1/2 "does not alter the actual wave kinetic one or the Gaussian variance-half action in the main limit theorem," is outside this excerpt and is not provable from the supplied text.

## Checked derivations

**FIN01 — Import and Dalang.** The claim `μ(B_R)=R^α μ(B_1)` is **correct**: a covariance homogeneous with exponent `d−α` has spectral measure homogeneous with exponent `α` (verified from `Γ(rx)=r^{−α}Γ(x)` giving `μ(B/r)=r^{−α}μ(B)`). The dyadic shell bound `≤ μ(B_1) 2^α Σ_{j≥0}2^{−j(2−α)}` is a valid majorant (shell mass `≤2^{(j+1)α}μ(B_1)`, weight `(1+|ξ|²)^{−1}≤2^{−2j}`). It converges iff `α<2`, which follows from the original threshold `α+α0<2`, `α0>0` together with `α>0`. Local finiteness of positive Radon `μ` controls `B_1`. So Dalang's condition holds, hence the imported finiteness legitimately applies. The `d−1` index artifacts in my initial scratch were resolved; the paper's factor accounting (`ℓ^{2d}·ℓ^{−d}·ℓ^{α−d}=ℓ^α`) is right.

**FIN02 — Compact vs full energy and normalization.** Restricting the source's full-domain supremum to real unit compact smooth tests gives `E≤E_full<∞`; valid. `A(f)` equals `⟨Γ,(f²)∗(f²)⟩` by translation `z=x−y` and evenness of `Γ`, so the source pairing `∫γ(x−y)g²(x)g²(y)` is correctly represented. Kinetic coefficient 1/2 is used consistently.

**FIN03 — Dilation and finite-supremum guards.** `U_b f(x)=b^{d/2}f(bx)` preserves `‖·‖₂`; `T(f_b)=b²T`; `A(f_b)=b^αA`. The optimizer `b=(αA/T)^{1/(2−α)}` is finite and positive since `A>0`, `T>0`, `0<α<2`. `T>0` is proved by the correct zero-set Fourier argument. Substitution gives `E≥((2−α)/2)α^{α/(2−α)}(A/T^{α/2})^{2/(2−α)}`, and the inversion gives `C_E=α^{−α/2}[2E/(2−α)]^{(2−α)/2}` — arithmetically correct, all bases/denominators strictly positive. The `A=0` branch is immediate and `E≥0` follows by `b↓0`.

**FIN04 — Physical shifted-a.e. Fatou extension.** Convergent `H¹` approximants have an a.e.-convergent subsequence; translated null sets stay null, and Tonelli over `dx⊗Γ(dz)` makes convergence hold at both `x` and `x−z` product-a.e. Fatou plus `T(f_n)→T(f)` gives `A(f)≤liminf A(f_n)≤C_E T(f)^{α/2}`. This is version-independent via the cited `L:spatial-physical-pair`, which uses no ratio/score finiteness. Valid, noncircular.

**FIN05 — Amplitudes/zero/white/plane tests.** (a) `Γ=0`: `A=0`, `R_sp=0`, and dilation-spread tests make the energy zero; consistent. (b) d1 white `cδ0`: `α=1`; independent soliton check (`f=√(1/2)sech`, `∫f⁴=1/3`, `∫(f′)²=1/3`) gives `E=1/6`, `R=1/√3`, so `C_E=√(2E)=c/√3` matches. (c) d3 plane `cδ0(dx1)dx2dx3`: `α=1`; projected spectral measure gives `Dalang=c/2`; product-test argument and transverse spreading are sound and correctly avoid a false high-dimensional white conclusion.

**FIN06 — Independence from old upper/scores.** The derivation uses only the imported `E<∞` (restricted to compact smooth) and the Fatou transfer; it does not invoke the old full wave upper, positive score, rough stochastic evolution, or a ground state. Confirmed.

**FIN07 — Exact limited scope.** The draft states it establishes only `R_sp` finiteness and explicitly does not replace `P:spatial-smooth-ratio`'s lower-score comparison, `S_c` finiteness, or other full-upper consumers. Honest. The scaling identity `E(cΓ)=c^{2/(2−α)}E(Γ)` via the dilation bijection is correct, and `C_E` scales linearly.

**FIN08 — Completeness of supplied TEXT and ambiguities.** The excerpt is internally complete for the finiteness deduction. Remaining unresolvable ambiguities: the visual source certification (Kimi-assigned), the `2π` convention, the unprovided "already derived" white constant derivation, and the unprovided unchanged main bodies. All are recorded rather than resolved.

## Required fixes before production gate

1. Obtain and independently confirm the visual/certified Chen pages 1–3 (Kimi check) for Theorem 1.1/(1.5) and the Dalang condition, and declare convergence with this text-only review.
2. Re-verify the `c/(2π)` factor and the d1 `E=c²/6` value against the certified source convention before relying on the consistency checks.
3. Either supply the derivation of the d1 white `E=c²/6` or mark it as an external prior result.
4. Remove or constrain the unreviewed assertation that the imported kinetic coefficient 1/2 does not alter the main wave kinetic/Variance-half terms.
5. Enumerate the unchanged "full-upper consumers" (`S_c`, canonical moments, uniform integrability, cone transfers) and confirm none depends circularly on the replaced proof.

## One-line summary

The imported Dalang-condition spatial energy, combined with a correct compact-test dilation, optimization, and shifted-a.e. Fatou extension, does yield the finite ratio bound `R_sp ≤ C_E` with correct constants and no critical gap in the supplied excerpt — accepted with notes pending the assigned visual source certification.