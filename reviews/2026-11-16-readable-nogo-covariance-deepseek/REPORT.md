# Review Result
Category: proof-readability-equivalence
Model: deepseek/deepseek-v4-pro
Verdict: PASS_WITH_NOTES
Confidence: high

All six assigned scientific statements and proofs are present in both scientific views; the only changes are added `Step 1./Step 2./Step 3.` headings and short roadmap sentences inside `proof` environments. No displayed hypothesis, constant, normalization, strictness, limiting order, or conclusion changed. One assigned proof, P:nogo-11, carries a substantial pre-existing mathematical defect that is identical in both revisions (the claimed power-series identity for `F(A)` does not follow from the stated ODE and appears inconsistent with `\cosh^2\sqrt z`). That defect does not arise from the rewrite, so readability preservation still passes, with notes.

---

## P:nogo-08
Old reading: COMPLETE. New reading: COMPLETE. Argument preservation: PRESERVED. New explanations: JUSTIFIED. Public reconstruction: COMPLETE.

Original-step coverage:

1.  Statement retained exactly: Riesz failure for `3/2 ≤ α < 2`; product-covariance failure for every `1 < α < 2` in dimensions two and three; admissibility `α+α0 < 2` possible.
2.  Riesz step. For `y = e1 + ρ(cosφ,sinφ)`,
    `|y|² = 1 + 2ρcosφ + ρ²`, so on `2π/3 ≤ φ ≤ 4π/3`
    `1−|y|² = −2ρcosφ − ρ² ≤ 2ρ`, and
    `1−|y|² ≥ ρ − ρ² = ρ(1−ρ) > 0` for `ρ < 1/2`. The disk density obeys
    `(2π√(1−|y|²))^{-1} ≥ (2π√(2ρ))^{-1}`. With polar Jacobian `ρ dρ dφ`,
    the angular sector length `2π/3`, and `|y−e1|^{−α} = ρ^{−α}`, the constant is
    `(2π)^{-1}·(2ρ)^{-1/2}·(2π/3) = 1/(3√2)`, giving
    `(c/(3√2))∫_0^{1/2} ρ^{1/2−α}dρ = ∞` since `1/2−α ≤ −1`; logarithmic at `α = 3/2`.
3.  Product step. With `a1 = (1+max{2−α, α−1})/2` and `a2 = α−a1`: for `α ≤ 3/2`, `a1=(3−α)/2`, `a2=3(α−1)/2`, giving `a1+a2/2=(3+α)/4>1`; for `α ≥ 3/2`, `a1=a2=α/2`, giving `a1+a2/2=3α/4>1`. In both cases `0<a1,a2<1`. `γ(x)=c|x1|^{−a1}|x2|^{−a2}` has degree `−(a1+a2)=−α`, is locally integrable, and each coordinate factor is a positive Gaussian mixture (third coordinate constant one in `d=3`), so the product is positive definite.
4.  Substitution `u=1−y1`, `y2=√(2u−u²)w` gives `1−|y|²=(2u−u²)(1−w²)`; the disk density becomes
    `(2π)^{-1}(1−w²)^{-1/2}du dw`, and `γ(y−e1)=c u^{−a1}(2u−u²)^{−a2/2}|w|^{−a2}`. Integrating `|w|^{−a2}(1−w²)^{-1/2}` over `[−1,1]` gives `B((1−a2)/2,1/2)`. Near `u=0` the `u`-integrand is `~ u^{−(a1+a2/2)}`, divergent since `a1+a2/2>1`. This matches the displayed formula.
5.  Projection `G_1^{(3)} → G_1^{(2)}`: the two sphere graphs each contribute surface Jacobian `(1−|y|²)^{-1/2}`, divided by `4π`, i.e. exactly `G_1^{(2)}`; hence the three-dimensional divergence follows.
6.  Smoothing: Gaussian smoothing converges to the unsmoothed kernel off the singular sets, whose translated wave measure is zero, so Fatou forces lower-limit divergence; `α0 < 2−α` yields `α+α0<2`.

Lost steps/qualifiers: none. The exact ranges `3/2 ≤ α < 2` and `1 < α < 2`, the admissibility qualifier, and the logarithmic endpoint are preserved. New roadmap text (“We test … the smoothing limit shows why neither example admits the proposed uniform spatial maximum”) accurately summarizes the proof. The Riesz smoothing passage is ultimately supported by the cited `P:higher-obstructions`/`L:higher-riesz` material (unassigned context, read here only for application), not re-derived in this proof body; this is unchanged in both views.

Pre-existing vs new: none introduced; the proof is identical in substance.

---

## P:nogo-09
Old reading: COMPLETE. New reading: COMPLETE. Argument preservation: PRESERVED. New explanations: JUSTIFIED. Public reconstruction: COMPLETE.

Original-step coverage:

1.  `Γ(x)=|x1|^{−9/10}|x2|^{−3/5}` in `d=3`: exponents `9/10, 3/5 ∈ (0,1)`, sum `α=3/2`; `α0=1/4` gives `α+α0=7/4<2`. The third coordinate factor is the constant covariance one. Each one-dimensional factor is a positive Gaussian mixture, hence `Γ` is positive definite, locally integrable, and tempered.
2.  `F=|x|^{1/2}Γ` is locally integrable: split `|x|^{1/2} ≤ |x1|^{1/2}+|x2|^{1/2}+|x3|^{1/2}`, producing integrals like `∫|x1|^{−2/5}|x2|^{−3/5}` over bounded boxes, finite since both exponents `<1`. Multiplied by a rapidly decaying Schwartz test the same bounds give temperedness.
3.  `p_σ*F(0)` is finite: `p_σ` is bounded, and local integrability plus polynomial growth justifies the integral.
4.  Lower bound at `Le3`. On `1≤y1≤2, 1≤y2≤2, |y3−L|≤1`, the Gaussian factor is `≥ c_σ>0`; `|y1|^{−9/10}≥2^{−9/10}`, `|y2|^{−3/5}≥2^{−3/5}`; and `|y|^{1/2}≥(L−1)^{1/2}`. Since the box has positive volume, `(p_σ*F)(Le3) ≥ c_σ√L`.
5.  If `F` were positive definite as a distribution, the Hermitian form `Q(g,h)=⟨F, g*h̃⟩` gives `|Q(g, τ_xg)|² ≤ Q(g,g)Q(τ_xg,τ_xg)`. For a centered Gaussian `g` with `g*g̃=p_σ`, the diagonal is `(p_σ*F)(0)` and the cross term is `(p_σ*F)(x)`, hence `|(p_σ*F)(x)|≤(p_σ*F)(0)`. This contradicts the `√L` growth.

Lost steps/qualifiers: none; the statement still says `F` is “locally integrable tempered” and “not positive definite as a distribution.” Added headings only describe the two stages (“verify the original covariance”, “obtain the contradiction after Gaussian convolution”).

Pre-existing vs new: none. Proof mathematics identical.

---

## P:nogo-11
Old reading: COMPLETE. New reading: COMPLETE. Argument preservation: PRESERVED. New explanations: JUSTIFIED (descriptive of the proof, though the proof has a pre-existing defect). Public reconstruction: PARTIAL.

Original-step coverage:

1.  Stated problem: `y''=Zy`, `y(0)=1, y'(0)=0`, `Z` centered Gaussian with variance `A`, `F(A)=E[y(1)^2]`; claim `F(100)^2 > F(99)F(101)`.
2.  Step 1 of the proof asserts
    `F(A)=1+∑_{k≥1} t_k(A)`, `t_k(A) = 2^{3k−1}(2k)!A^k/(k!(4k)!)`.

    This identity does not reconstruct. Since `y(1) = cosh√Z` (entire in `Z`), we have
    `y(1)^2 = cosh²(√Z) = (1+cosh(2√Z))/2`. Expanding,
    `cosh(2√Z)=∑_{n≥0} 2^{2n}Z^n/(2n)!`; for a centered Gaussian of variance `A`, `E[Z^n]=(2n)!/(2^n n!)A^n`, so `E cosh(2√Z)=e^{2A}` and
    `F(A)=(1+e^{2A})/2 = 1+∑_{k≥1} 2^{k−1}A^k/k!`. The correct `t_k` is `2^{k−1}/k!`, not the displayed one (`t_1=1`, not `A/3`). With the correct `F`, `log F` is convex (`2e^{2A}/(1+e^{2A})` is increasing), so `F(100)^2 < F(99)F(101)`, the opposite of the asserted inequality. Consequently the stated no-go appears false as written.
3.  Internal arithmetic (from the displayed series, regardless of its invalid link to `F`) is checkable. The ratio is
    `t_{k+1}/t_k = 16A(2k+1)/((4k+1)(4k+2)(4k+3)(4k+4)) ≤ 16A/(4k+1)^3`. For `k≥20`, `4k+1≥81`, so the tail from `k=21` is dominated by `t_{21}/(1−q_A)`, `q_A=16A/81^3<1` for `A=99,100,101`. Thus `S_20 ≤ F ≤ S_20 + t_{21}/(1−q_A)` is a valid enclosure for the displayed series.
4.  The final rational comparison from the table is arithmetically consistent:
    `L100² = 212332413² = 45,085,053,610,402,569`,
    `U99·U101 = 207442590·217304019 = 45,078,108,518,769,210`,
    difference `= 6,945,091,633,359`, i.e. `6945091633359/10^12 > 0`. So the table would imply the claimed sign if the series were the `F` of the statement.

Omissions explicit: I did not recompute all 21 partial sums that produce the table entries; the table is accepted as a stated finite rational computation, and the final difference identity and the ratio/tail bounds are checked.

Lost steps/qualifiers: none between Old and New; the added headings only relabel the two parts (“obtain the series and a controlled tail”, “compare the rigorous rational enclosures”).

Pre-existing vs new: the series/`F` mismatch is pre-existing, byte-identical in both views. It is a mathematical concern about the no-go itself, not a readability change. A bounded correction would replace `t_k` by `2^{k−1}/k!`, but then the claimed inequality reverses, so no silent repair is appropriate here.

---

## P:nogo-12
Old reading: COMPLETE. New reading: COMPLETE. Argument preservation: PRESERVED. New explanations: just no additions inside this proof. Public reconstruction: COMPLETE.

Original-step coverage:

1.  Parameters: `d=3`, `α=11/10`, `α0=1/4`, `Γ=|x1|^{−9/10}|x2|^{−1/5}`; exponents sum to `11/10=α`, both in `(0,1)`, so `Γ` is admissible as in P:nogo-09.
2.  Exponent check: `β=9/5`, `(2α−β)/2−1 = (22/10−18/10)/2−1 = (4/10)/2−1 = −4/5`, so `H(x)=∫_0^∞ s^{−4/5} F_s(x)^2 ds`.
3.  First-coordinate lower bound. For `0<s<1/16`, `|x1|≤√s`, restrict the 1D Gaussian convolution to `√s≤y1≤2√s`. Then `|x1−y1|≤3√s`, so the Gaussian is `≥ (2πs)^{-1/2}e^{-9/2}`, and `|y1|^{−9/10} ≥ 2^{−9/10}s^{−9/20}`. The interval length `√s` cancels `s^{−1/2}`, giving `(p_s^{(1)}*|·|^{−9/10})(x1) ≥ c s^{−9/20}`.
4.  Second-coordinate lower bound. For `1/2≤x2≤1`, restrict to `x2≤y2≤x2+√s`. The Gaussian is `≥ (2πs)^{-1/2}e^{-1/2}`, `|y2|^{−1/5}` is bounded below, so the `√s` interval length against `s^{-1/2}` gives a positive constant independent of `s`. The third coordinate contributes one.
5.  On `B=[−1,1]×[1/2,1]×[−1,1]`, the strip `|x1|≤√s` gives
    `∫_B F_s(x)^2 dx ≥ c s^{−2·(9/20)+1/2} = c s^{−2/5}`.
6.  Tonelli then gives `∫_B H dx ≥ c∫_0^{1/16} s^{−4/5}s^{−2/5}ds = c∫_0^{1/16}s^{−6/5}ds = ∞`.

Lost steps/qualifiers: none; “does not define a locally finite measure,” the specific box, and the restricted smoothing-scale integral are all preserved. The New view’s proof body for P:nogo-12 is unchanged (no step headings were added).

Pre-existing vs new: none.

---

## P:nogo-13
Old reading: COMPLETE. New reading: COMPLETE. Argument preservation: PRESERVED. New explanations: JUSTIFIED. Public reconstruction: COMPLETE.

Original-step coverage:

1.  `Γ(dy,dz)=(2π)^{-1}|y|^{-1/2}dy⊗δ_0(dz)` in `R^3=R^2×R`. The planar Riesz factor `|y|^{-1/2}` on `R^2` is locally integrable and positive definite via Gaussian mixtures; `δ_0(dz)` is positive definite because its quadratic form leaves two equal normal coordinates, producing a nonnegative tangential integral. Hence the product is positive definite.
2.  Homogeneity: for `y=ry'`, `ry` substitution gives `|y|^{-1/2}=r^{-1/2}|y'|^{-1/2}`, `dy=r²dy'`, and `δ_0` keeps unit mass at `0`, so `Γ(rA)=r^{3/2}Γ(A)`; thus `d−α=3/2`, `α=3/2`. The `α0=1/4` condition gives `α+α0=7/4<2`. Mass on a radius-`R` ball is `∝R^{3/2}`, giving temperedness.
3.  Suppose `C_n≤C` on a subsequence. For `f∈C_c^+`, vague convergence gives
    `∫f dΓ = lim ∫f dΓ_n ≤ C∫f(x)|x|^{-3/2}dx`.
    Since `|x|^{-3/2}` is locally integrable in `R^3`, this extends to domination of measures, so `Γ` would be absolutely continuous with respect to 3D Lebesgue measure.
4.  Contradiction: the compact planar annulus `{(y,0): 1≤|y|≤2}` has `Γ`-mass
    `(2π)^{-1}·2π·∫_1^2 r r^{-1/2}dr = ∫_1^2 r^{1/2}dr > 0`,
    but zero 3D Lebesgue measure. Hence every bounded subsequence of `C_n` is excluded, and `C_n→∞`.

Lost steps/qualifiers: none; “vague convergence,” “nonnegative measures,” the exact bound `C_n|x|^{-3/2}dx`, and the conclusion `C_n→∞` are all preserved. Added headings only separate “verify the singular covariance” from “contradict bounded envelope constants by singular support.”

Pre-existing vs new: none.

---

## P:nogo-19
Old reading: COMPLETE. New reading: COMPLETE. Argument preservation: PRESERVED. New explanations: JUSTIFIED. Public reconstruction: COMPLETE.

Original-step coverage:

1.  Parent covariance. `a=99/100`, `C((s,x),(t,y))=(1−a)|s−t|^{-a}|x−y|^{-1/2}` on `d=1`. Spatial degree `α=1/2`; temporal degree `α0=a`, and `α+a=0.5+0.99=1.49<2`. Both power kernels are positive definite and locally integrable via Gaussian mixtures.
2.  Projection. With `ψ=1_{[0,1]}⊗1_{[-1,1]}` and `V=E W(ψ)^2`, `0<V<∞` by positivity and local integrability. `Z=W(ψ)/√V` is unit Gaussian; the profile
    `m(s,x) = V^{-1/2}∫∫ C((s,x),(r,y))dy dr`
    satisfies `⟨m,f⟩=E[W(f)Z]` by Fubini, so `m` is the covariance of the generalized field with `Z`. Writing `W=Zm+W^⊥` with `W^⊥⟂Z` gives `P=m⊗m` and covariance `C−P`; positivity of `C−P` is automatic by Gaussian projection, not assumed.
3.  Explicit profile. `E_t=∫∫_{[0,1]²}|s−r|^{-a}drds=2/[(2−a)(1−a)]` and
    `E_φ=∫_{[-1,1]²}|x−y|^{-1/2}dxdy = ∫_{−2}^2(2−|u|)|u|^{-1/2}du = 16√2/3`.
    Hence `V=(1−a)E_tE_φ=2E_φ/(2−a)`. Also `∫_0^1|s−r|^{-a}dr=(s^{1−a}+(1−s)^{1−a})/(1−a)`, so `m(s,x)=B_a(s)F(x)/√V` with `B_a(s)=s^{1−a}+(1−s)^{1−a}≥1` and `F(x)=∫_{−1}^1|x−y|^{-1/2}dy`. `F≤4` with maximum at `x=0`, and for `|x|≤1`, `F(x)=2(√(1+x)+√(1−x))≥2√2`. On the backward cone of `(1,0)`, the wave supports give `|y|<1−t<1` and `|z|≤|y|+|y−z|<1−t+t−s=1−s<1`, so both spatial coordinates satisfy `|·|≤1`; hence `m(s,z)m(t,y)≥(2√2)²/V=8/V`.
4.  Degree-two coefficient. For covariance `D`,
    `A_D=∫_{0<s<t<1}∫_{R²}G_{1−t}(−y)G_{t−s}(y−z)D((s,z),(t,y))dz dy ds dt`,
    the single self-pair term (no factorial). With `G_r(x)=1_{|x|<r}/2`, covariance one gives
    `∫∫G_{1−t}(−y)G_{t−s}(y−z)dzdy=(1−t)(t−s)`, and
    `∫∫(1−t)(t−s)dsdt=1/24`.
5.  Parent coefficient. The inner spatial integral of `|z−y|^{-1/2}` against `G_{t−s}` is `(1/2)·4√(t−s)=2√(t−s)`, then `∫G_{1−t}=1−t`, so
    `A_C=2(1−a)∫_0^1(1−t)t^{3/2−a}dt/(3/2−a) = 2(1−a)/[(3/2−a)(5/2−a)(7/2−a)]`
    `=20000/1932951 < 1/96`.
6.  Projected coefficient. `A_P≥(8/V)(1/24)=1/(3V)=101/(3200√2)>1/48`.
7.  Mean passage (parent). `u_C(h)=∑h^n X_n`; `E[X_n²]≤r^{-2n}B_r` by nonnegativity of mixed moments, so the `L²` tail from `n=4` is `≤√B_r(|h|/r)^4/(1−|h|/r)`. Odd means vanish by Gaussian sign symmetry, giving `E u_C(h)=1+h²A_C+O(h^4)`.
8.  Mean passage (projected). The potential is `Zm(s,x)` with `M=sup|m|`; deterministic Picard coefficients are `≤M^n/(2n)!`, the absolute series is bounded by `E cosh√{M|Z|}<∞`, odd terms vanish by symmetry, and factoring `h^4` from the tail gives `E u_P(h)=1+h²A_P+O(h^4)`.
9.  Strict gap `A_P−A_C>1/48−1/96>0` makes `E u_P(h)>E u_C(h)` for all sufficiently small positive `h`, i.e. `E u_C< E u_P`.

The reconstruction compares the two concrete means directly and never invokes “arbitrary-phase covariance monotonicity.” The statement’s final sentence “The projection `P` is not asserted to be stationary or homogeneous” is retained verbatim; rank-one `P=m⊗m` is only positive semidefinite residual covariance, not homogeneous.

Lost steps/qualifiers: none. Added headings only organize the three stages.

Pre-existing vs new: none.

---

## Findings and limits

Preservation: all six proof bodies are preserved. The New view adds only `\medskip\noindent\textit{Step k.~}` headings plus short orienting sentences; no hypothesis, domain, constant, strictness, limiting order, normalization, or equation changed. P:nogo-12 is untouched. The roadmap sentences accurately describe their proofs. The inventory’s claim of byte-exact scientific statements/proofs is consistent with the supplied text.

Witness checks performed as directed: boundary divergence and the anisotropic homogeneous examples versus admissibility (P:nogo-08); radial repair breaking positive definiteness (P:nogo-09); scalar log-convexity arithmetic (P:nogo-11); heat–Mellin local finiteness and the actual covariance calculation (P:nogo-12); vague-limit obstruction for envelope constants (P:nogo-13); and the small-coupling parent-versus-projection comparison without assuming monotonicity, preserving the explicit non-homogeneity disclaimer (P:nogo-19).

Pre-existing concern: P:nogo-11’s displayed coefficient `t_k=2^{3k−1}(2k)!A^k/(k!(4k)!)` is inconsistent with the stated `F(A)=E[y(1)^2]`; the direct expansion gives `t_k=2^{k−1}A^k/k!`, `F(A)=(1+e^{2A})/2`, for which `log F` is convex and the asserted inequality is reversed. This appears to make the no-go statement false as written, and it is identical in both revisions, so it is not a rewrite defect. Because the key Step-1 equality cannot be reconstructed as valid, Public reconstruction for P:nogo-11 is PARTIAL even though both readings are complete.

Limitations: I verified the long numerical enclosure table in P:nogo-11 only structurally (ratio/tail bound and the final difference identity `6945091633359/10^12`), not every one of the 21 partial sums. LF positions inside each view are taken from the supplied inventory; I did not independently number source lines. Unassigned baseline material was used only for applied hypotheses (H:homog, P:mixed) and referenced smoothing/passage statements, not as reconstructed proofs. No tools, files, or network were used. These notes do not constitute correctness release for P:nogo-11, whose pre-existing series error warrants upstream attention independent of the readability-preservation question.
