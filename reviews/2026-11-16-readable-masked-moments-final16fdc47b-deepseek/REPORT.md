# Review Result
Category: proof-readability-equivalence
Model: deepseek-v4-pro
Verdict: PASS_WITH_NOTES
Confidence: high

Scope: exactly the three assigned labels in
`notes/integrated_masked_moments.tex`. Baseline context sources are used only
as unassigned inputs; their proofs were not re-reviewed. The three assigned
statements and their complete proofs were read in both OLD and NEW forms.

---

## L:masked-chain-comparison

- Old reading: COMPLETE (statement OLD 23–37, proof OLD 39–98)
- New reading: COMPLETE (statement NEW 23–37, proof NEW 39–127)
- Public reconstruction: COMPLETE
- Argument preservation: PRESERVED
- New explanations: JUSTIFIED

**Statement comparison.** The lemma statement is word-for-word identical in the
two revisions, including all quantifiers (`n,k ≥ 0`, fixed `t,x,y`, positive
`ρ`), the odd-`n+k` vanishing clause, and the two `q_n`-bounds. No declaration
or scientific-setup change occurs in this item; the preceding module setup
(OLD/NEW lines up to 22) is also unchanged, including `0 ≤ m ≤ 1`, positive
Green measures of mass `r` with support in `B_r`, the `d=3` sphere-measure
remark, and the sentence about using all pair partitions including
self-pairings.

**Original-step coverage and public working.**

1. *Chain measure and mass.* The proof introduces `ν_n^{t,x}` on
   `0 < s_1 < ⋯ < s_n < t` with spatial factors
   `G_d(s_{j+1}-s_j, dz_j)`, `s_{n+1}=t`, recovering positions backward from
   `x`, and declares the order-zero mass to be one. The recursion is
   `f_n(t)=∫_0^t(t-r)f_{n-1}(r)dr`. This is checkable by induction from
   `f_0=1`:
   \[
   f_n(t)=\int_0^t(t-r)\frac{r^{2n-2}}{(2n-2)!}\,dr
   =\frac{t^{2n}}{(2n-2)!}\int_0^1(1-u)u^{2n-2}\,du
   =\frac{t^{2n}}{(2n-2)!}B(2,2n-1)
   =\frac{t^{2n}}{(2n)!}.
   \]
   This gives exactly `E:masked-chain-mass`, and the new explanation spelling
   out `f_{n-1}(r)=r^{2n-2}/(2n-2)!` is correct, not merely paraphrase.

2. *Measurability.* The assertion that `G_d(r)` is `r` times the dilation of a
   unit-time probability measure is retained and used only for measurability of
   the chain measure; the new text adds only "In particular, the measure is
   finite at each fixed order," which follows from Step 1.

3. *Covariance bound.* The proof sets
   `C_ρ(s,z;r,w)=K_η(s-r)Γ_{2ε}(z-w)` and
   `0 ≤ C_ρ ≤ c_ρ := K_η(0)Γ_{2ε}(0) < ∞`. This matches
   `E:source-joint-covariance` specialized to equal widths:
   `K_η(t-s)Γ_{ε+ε}(x-y)`, with `K_η` even and `Γ_{2ε}(·)` positive because
   `Γ` is a nonnegative Radon measure and `p_e` is positive. The second bound
   follows from `Γ_{2ε}(z-w)≤Γ_{2ε}(0)` by Cauchy–Schwarz in `L^2(μ)` and
   `K_η(·)≤K_η(0)`. Finiteness holds since `a>0` gives `K_η(0)<∞` and
   `Γ_{2ε}(0)=∫e^{-ε|ξ|²}μ(dξ)` is finite for tempered `μ`. Both revisions
   state this identically.

4. *Gaussian moment integrability.* Using the Wick expansion for a fixed number
   of jointly Gaussian source factors,
   \[
   \Big|\mathbb E\prod_{i=1}^{2n}Y_ρ(s_i,z_i)\Big|
   ≤(2n-1)!!\,c_ρ^n,
   \]
   uniformly in the vertices, since each pairing contributes at most `c_ρ^n`.
   Taking the square of an `n`-fold product gives `2n` source factors, so
   `‖∏_{i=1}^n Y_ρ(·)‖_2 ≤ (2n)!...`-type constant at fixed `(ρ,n)`. The new
   Step 1 sentence "the bound ... is uniform over the integration variables at
   fixed `ρ,n`; its integral against the finite chain measure is therefore
   finite" is exactly this uniformity plus `ν_n^{t,x}(1)<∞`, and is the
   Bochner-condition check. Applying the same argument jointly to two products
   gives the absolute integrability needed for stochastic Fubini, also as
   stated.

5. *Green-before-noise removal.* The Step 2 content is an accurate
   restatement, including the positive heat approximate identity, weak
   convergence preserving masses, continuity via
   `L:source-pointfield-regularity`, the integrable time majorant from
   `E:masked-chain-mass`, and identification with the Green-before-noise limit
   of `L:joint-fixed-order`. The added sentence
   "The unmasked `X_{ρ,n}(t,x)` is `Y_n^{\mathbf a}(t,x)` from
   `L:vertex-crude` with every vertexwise noise width in `\mathbf a` set equal
   to `ρ`, so its bound is `q_n(t)`" is a valid specialization: setting all
   vertexwise widths to the common `ρ` recovers a common-width source, and
   `L:vertex-crude` is stated under `H:homog` with no restriction on the
   individual widths. The same argument covers the masked summand because
   `0≤m≤1` reduces the coefficient moments.

6. *Diagram comparison.* For `n+k=2l`, the joint moment has the Wick form
   \[
   \mathbb E[X_{ρ,n}(t,x)X_{ρ,k}(t,y)]
   =\sum_{D\in\Pi_{2l}}\int\prod_{\{i,j\}\in D}
   C_ρ(s_i,z_i;s_j,z_j)\,d(ν_n^{t,x}⊗ν_k^{t,y}),
   \]
   with `Π_{2l}` the set of all pair partitions of the `2l` vertices. The
   masked moment inserts `∏_{i=1}^{2l}m(z_i)∈[0,1]`. Since each diagram
   integrand is nonnegative, the masked diagram is pointwise ≤ the unmasked
   diagram, and summing preserves the inequality. The statement explicitly
   retains "unequal and empty chains and every self-pairing"; for `n=k=0` there
   is a single empty partition contributing `1`, giving equality. For `k=n`,
   `y=x`, the comparison becomes `E|X_{ρ,n}^m|²≤E|X_{ρ,n}|²`, and the unmasked
   `q_n` bound gives `E:masked-order-bound`.

**Gamma = 0 / order-zero checks.** If `Γ=0`, then `c_ρ=0`, every diagram with
at least one covariance factor vanishes, and only the `n=k=0→1` term remains;
all inequalities and bounds still hold, with `q_n` remaining valid as an upper
bound. The proof does not require `Γ≠0`.

**Lost steps/qualifiers.** None identified. The final sentence that these are
"expected displacement diagrams; no samplewise solution order or Gaussian
covariance order is used" is preserved verbatim; the same applies to the
Green-before-noise ordering.

**Pre-existing concern (not introduced).** The step needs the cited Green
measures to be symmetric under `z ↦ -z` when used in the later time/space
reversal; this is plausible from the source-declared sphere/radial kernels but
is not an explicit declaration in this module. This is an upstream-source
reliance, unchanged by the rewrite.

---

## P:masked-source-moments

- Old reading: COMPLETE (statement OLD 100–115, proof OLD 117–159)
- New reading: COMPLETE (statement NEW 129–144, proof NEW 146–210)
- Public reconstruction: COMPLETE
- Argument preservation: PRESERVED
- New explanations: JUSTIFIED

**Statement comparison.** Only grammatical change: "an Bochner" (OLD 115)
becomes "a Bochner" (NEW 144). All mathematical content, including the
conditional clause "For every nonnegative `φ∈C_c^∞(ℝ^d)`", is unchanged.

**Original-step coverage and public working.**

1. *Absolute `L²` convergence.* Put `Q_T = ∑_{n≥0}q_n(T)<∞` by
   `E:vertex-summability`. Since `E:masked-order-bound` gives
   `‖X_{ρ,n}^{(m)}(t,x)‖_2 ≤ q_n(t)` uniformly in `x` and widths, one has
   `∑_n‖X_{ρ,n}^{(m)}(t,x)‖_2 ≤ Q_t <∞`. Hence both masked and unmasked sums
   converge absolutely in `L²`. (`E:vertex-summability` is stronger,
   `∑√{n+1}q_n(T)<∞`, so `∑q_n(T)<∞` follows.)

2. *Pathwise Picard identification.* For fixed `ρ`, a compact observation set,
   and horizon `T`, the boundedness of the smooth coefficient on the enlarged
   backward cone by a sample-dependent `M` plus finite propagation and
   `E:masked-chain-mass` give the `n`th Picard term bound
   `M^n T^{2n}/(2n)!`. The sum of these converges (cosh-like), term continuity
   comes from the unit-time Green representation, and summing the Volterra
   recursion gives the ordinary mild equation with data `(1,0)`. The uniqueness
   estimate is `B M^n T^{2n}/(2n)!→0`. Both versions contain exactly the same
   argument.

3. *Bochner term/pathwise identification.* Ordinary Fubini plus absolute
   product integrability from the lemma identifies each Bochner term with the
   pathwise chain integral at fixed terminal point; an a.s. convergent
   subsequence of the `L²` partial sums identifies the limit with the
   continuous Picard version. The qualifier that this is "at this fixed `ρ`;
   no common event over uncountably many widths is needed" is retained.

4. *Passing the mixed-order comparison through the series.* Cauchy–Schwarz
   gives:
   \[
   \sum_{n,k≥0}\mathbb E|X_{ρ,n}^{(m)}(t,x)X_{ρ,k}^{(m)}(t,y)|
   ≤\sum_{n,k}‖X_{ρ,n}^{(m)}(t,x)‖_2‖X_{ρ,k}^{(m)}(t,y)‖_2
   ≤ Q_t^2<∞.
   \]
   So products of partial sums are Cauchy in `L¹`, `E:masked-order-comparison`
   passes termwise, and `E:masked-two-point` follows. The added sentence
   "For the unmasked stationary field, Cauchy–Schwarz bounds its two-point
   expectation by the geometric mean of two equal point second moments" is
   correct: if the law is stationary then the two point second moments coincide,
   and
   `E[u(t,x)u(t,y)] ≤ ‖u(t,x)‖_2‖u(t,y)‖_2 = E|u(t,0)|²`.
   The subsequent claim that stationarity is not required of the masked
   solution (only of the unmasked majorant) is retained.

5. *Bochner spatial average.* The Step 4 added sentence that translating each
   recovered vertex position by `x` identifies `ν_n^{t,x}` with a translate of
   `ν_n^{t,0}` and changes only the arguments of the source factors (and of
   `m` in the masked case) is a correct explanation of the established
   `L²`-continuity in `x`. With the uniform `q_n` tail, the full sum is
   `L²`-continuous in `x`; separability of `L²` and the `Q_t` bound give the
   Bochner average. Fubini majorant is
   `∬φ(x)φ(y)E|u_ρ^m(t,x)u_ρ^m(t,y)|dxdy ≤ ‖φ‖₁² Q_t² <∞`.
   Therefore
   \[
   \mathbb E\Big|\int φ(x)u_ρ^m(t,x)\,dx\Big|²
   =∬φ(x)φ(y)\mathbb E[u_ρ^m(t,x)u_ρ^m(t,y)]\,dx\,dy
   ≤‖φ‖₁²\,\mathbb E|u_ρ(t,0)|²,
   \]
   which is `E:masked-average-source`.

**Lost steps/qualifiers.** None. The steps are reorganized into four labeled
steps, with none of the old assertions removed. In particular, the
"stationarity is not required of the masked solution" caveat and the
"no common event over uncountably many widths" caveat both survive.

**Pre-existing concern.** For `n=0` the sentence "Each term is continuous by
the unit-time Green representation" is technically about `n≥1`; the order-zero
term is the constant `1` and is trivially continuous. This is harmless and
pre-existing.

---

## P:masked-canonical-transfer

- Old reading: COMPLETE (statement OLD 161–175, proof OLD 177–212)
- New reading: COMPLETE (statement NEW 212–226, proof NEW 228–283)
- Public reconstruction: COMPLETE
- Argument preservation: PRESERVED
- New explanations: JUSTIFIED

**Statement comparison.** Identical in both revisions, including the
"arbitrary relative rates of the two widths" hypothesis for
`E:masked-unmasked-moment-limit` and the explicitly conditional premise for
`E:masked-conditional-transfer`. The identity `E|u(t,0)|²` with real `u`
matches `P:mixed`'s `E u²(t,x)`.

**Original-step coverage and public working.**

1. *Fixed-order canonical limit.* At fixed `(n,k)`, the common-width source law
   is the vertexwise law of `L:joint-fixed-order`. At terminal `(t,0)`, reverse
   each chain by `s'_j=t-s_{n+1-j}`, `z'_j=-z_{n+1-j}`. Temporal reversal
   changes each difference only in sign, and `K_η` is a function of `|t-s|`, so
   it is preserved; `Γ_{2ε}` is even, so spatial differences are preserved:
   \[
   K_η(s_i-s_j)=K_η(|s_i-s_j|)=K_η(|s'_i-s'_j|),\qquad
   Γ_{2ε}(z_i-z_j)=Γ_{2ε}(z'_j?).
   \]
   The relabeling `r` sends each pairing `{i,j}` to `{r(i),r(j)}`, giving the
   initial-chain convention of `P:mixed`. The added sentence "The relabelling
   `r` below reverses the vertex order separately within each chain" is an
   accurate gloss of the two displayed changes of variables; it does not
   enlarge the claim. Green smoothing is removed first, as in Step 2 of the
   lemma and in `L:joint-fixed-order`. Applying `L:joint-fixed-order` gives the
   canonical limit of each diagram at arbitrary relative noise-width rates, and
   odd `n+k` remain zero. Hence, for fixed `n,k`,
   \[
   \mathbb E[X_{ρ,n}(t,0)X_{ρ,k}(t,0)]\to\mathbb E[X_n(t,0)X_k(t,0)].
   \]

2. *Summable double majorant.* Before and after the limit,
   `|E[X_{ρ,n}X_{ρ,k}]|,|E[X_nX_k]|≤q_n(t)q_k(t)` by Cauchy–Schwarz and
   `E:masked-order-bound` (`L:vertex-crude` for the limiting `X_n`). Since
   `∑_{n,k}q_n(t)q_k(t)=Q_t²<∞`, for `δ>0` choose `N` with
   `∑_{(n,k)∉[0,N]²}q_nq_k<δ`. Then
   \[
   |S_ρ-S|≤\sum_{n,k≤N}|a_{n,k}(ρ)-b_{n,k}|+2δ,
   \]
   and the finitely many limits hold jointly, so `S_ρ→S=Σ_{n,k}b_{n,k}`.
   `P:mixed` (`E:full-second`) identifies `S` with `E|u(t,0)|²`, proving
   `E:masked-unmasked-moment-limit`. The proof's caveat that this uses
   single-width diagram laws without constructing a pathwise realization of the
   whole canonical family is unchanged.

3. *Conditional transfer.* With `A=∫φ(x)u_ρ^m(t,x)dx` and `B=Z_m(t,φ)`,
   `‖B-A‖₂→0` implies second-moment convergence by the displayed estimate
   \[
   |E|B|²-E|A|²|≤‖B-A‖₂(‖B‖₂+‖A‖₂),
   \]
   which is exactly the factorization `|B|²-|A|²=(B-A)(B+A)` (real case)
   plus Cauchy–Schwarz; `‖A‖₂→‖B‖₂` makes the right side tend to zero. The new
   explanatory sentence is therefore justified. Passing to the limit in
   `E:masked-average-source` and using `E:masked-unmasked-moment-limit` yields
   `E:masked-conditional-transfer`. The sentence that existence of the masked
   limit remains an explicit premise is retained.

**Lost steps/qualifiers.** None.

**Pre-existing concern.** `L:joint-fixed-order`'s limit sentence is stated for
`m+n=2k≥2`; the proof does not explicitly isolate the `n=k=0` case. This is
benign because both order-zero integrals are declared to equal `1` and
`P:mixed` states `m=n=0` equals one. This omission is pre-existing (identical
in OLD and NEW), not introduced by the rewrite.

---

## AUDIT dispositions

No AUDIT-marked comments or open audit flags appear in the supplied OLD or NEW
module text. I found no new AUDIT-worthy defect introduced by the rewrite. Two
non-blocking pre-existing points are recorded for completeness:

1. In `P:masked-canonical-transfer`, the `n=k=0` fixed-order limit is implicit
   rather than explicit; it is covered by the declared order-zero value `1` and
   `P:mixed`'s `m=n=0` case.
2. The reversal step relies on even/radial symmetry of the cited Green measures,
   which is source-declared via the `d=3` sphere measure and radial support but
   not independently restated in this module.

Neither affects the equivalence of OLD and NEW; neither was caused by the
rewrite.

## Findings and limits

The rewrite of all three assigned proofs is explanatory restructuring. No
substantive step, hypothesis, or qualifier was lost; no mathematical statement
changed except the grammatical "an/a Bochner" fix. The added sentences are
justified under the same hypotheses:

- the explicit induction for `E:masked-chain-mass` is correct;
- the Bochner-integrability uniform-bound sentence follows from `c_ρ^n` and the
  finite chain mass;
- the identification of `X_{ρ,n}` with `Y_n^{\mathbf a}` at all widths `ρ` is a
  valid specialization of `L:vertex-crude`;
- the geometric-mean explanation of stationary unmasked two-point domination is
  valid Cauchy–Schwarz;
- the translation-of-chain-measure explanation matches the `x`-continuity
  argument;
- the factorization proof of the second-moment convergence estimate is correct.

All required conditions for the consumed upstream statements
(`H:homog`, `ρ>0` fixed, common widths for fixed-order limits, Green smoothing
removed before noise smoothing) are used as stated. `Γ=0` and order-zero cases
remain consistent throughout. No oscillatory inversion kernel is used as a
scalar equality in these three deductions; only positivity of the heat/Laplace
kernels, the nonnegative Radon measure `Γ`, and Cauchy–Schwarz moment bounds
are invoked, so no Fourier normalization ambiguity enters the assigned proofs.

This review certifies scope preservation and mathematical equivalence of the
three assigned OLD/NEW proofs only. It does not certify whole-book truth, cited
source pages, rendered output, Lean correspondence, or any upstream analytic
result whose proof was not assigned.
