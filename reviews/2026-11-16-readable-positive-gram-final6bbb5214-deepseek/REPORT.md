# Review Result
Category: proof-readability-equivalence
Model: deepseek-v4-pro
Verdict: PASS
Confidence: high

The five assigned proof pairs were read completely in both the OLD
(`cdde711c...`) and NEW (`6bbb5214...`) modules. The NEW revision adds
roadmaps/step headings to two proofs and one explicit inner-product
verification sentence to `L:gram-realization`. All added explanatory assertions
are mathematically justified. No target step, hypothesis qualifier, limiting
order, or constant is lost in any assigned proof. Statements are
content-identical in all five labels (the later ones only shift line numbers).

Assigned proofs and line ranges used below follow the inventory convention:
raw-module local LF ranges. Context sources (`notes_stratonovich_ham_second_
moment.tex`) and No-go `P:nogo-29` are unassigned and were not counted as
additional proofs; their hypotheses were checked only insofar as they are not
invoked in a way that changes the assigned arguments.

---

## L:gram-scalar-algebra

- Old reading: COMPLETE
- New reading: COMPLETE
- Public reconstruction: COMPLETE
- Original-step coverage: COMPLETE (no omissions identified)
- Argument preservation: PRESERVED
- New explanations: JUSTIFIED (no new explanatory assertion was introduced;
  the proof is byte-identical in mathematical content)

**Statement** (LF 27–38 in both): unchanged. It claims
`2ℓ√t ≤ ℓ²/w + wt` for real `ℓ`, `w>0`, `t≥0`; the Hilbert identity
`⟨Φ,z⟩ − ‖Φ‖²/2 = ‖z‖²/2 − ‖Φ−z‖²/2 ≤ ‖z‖²/2`; and the finite Gram
identity `‖∑_i w_i k_i‖² = ∑_{i,j} w_i C_{ij} w_j`.

**Working:**

1. Scalar inequality. Since `w>0` and `t≥0`, `√(wt) = √w√t`. The square
   identity is
   \[
   0\le(\ell/\sqrt w-\sqrt{wt})^2
   =\ell^2/w+wt-2\ell(\sqrt{wt})/\sqrt w
   =\ell^2/w+wt-2\ell\sqrt t.
   \]
   Rearranged this is exactly `E:gram-sqrt-dual`.

2. Equality case. Equality requires `ℓ/√w = √(wt)`, i.e.
   `ℓ²/w = wt`, hence `w² = ℓ²/t`. With `ℓ,t>0` and `w>0` this is
   `w=ℓ/√t`, verifying the stated equality condition.

3. Hilbert square. Expand
   `‖Φ−z‖² = ‖Φ‖² − 2⟨Φ,z⟩ + ‖z‖²`; hence
   `‖z‖²/2 − ‖Φ−z‖²/2 = ⟨Φ,z⟩ − ‖Φ‖²/2`, and the bound follows from
   `‖Φ−z‖² ≥ 0`.

4. Gram identity. `‖∑ w_i k_i‖² = ∑_{i,j} w_i w_j ⟨k_i,k_j⟩
   = ∑_{i,j} w_i C_{ij} w_j` by bilinearity over the real inner product,
   valid for finite real `w_i`.

The final clause — that these identities need neither Hilbert-ball compactness
nor an inverse covariance matrix — is retained in both versions and is merely a
scope observation, not a further assertion needing proof.

**Evidence:** OLD LF 40–51 and NEW LF 40–51 are mathematically identical;
equations `E:gram-sqrt-dual` and `E:gram-hilbert-square` are unchanged in both.
No cancellation hidden: the square completion is exact, and the `t=0` case is
covered since `√0=0`.

---

## L:gram-dual-minimum

- Old reading: COMPLETE
- New reading: COMPLETE
- Public reconstruction: COMPLETE
- Original-step coverage: COMPLETE (no omissions identified)
- Argument preservation: PRESERVED
- New explanations: JUSTIFIED
- Evidence: OLD proof LF 62–100; NEW proof LF 62–112. The NEW text adds a
  three-sentence roadmap and `Step 1`/`Step 2` headings; every mathematical
  sentence of the OLD proof is retained verbatim, and each new sentence is
  checkable below.

**Statement** (unchanged, LF 53–60): each nonempty `A⊂J` has a unique positive
minimizer `w^A` of `D_A^C`, and stationarity
`∑_j C_{ij} w_j^A − b_i = ℓ_i²/(w_i^A)² > 0` holds.

**Working:**

1. Reduction to the diagonal plus dropped nonnegative cross terms. Since
   `C_{ij}≥0` and `w_i>0`, and `c_i=C_{ii}>0` for `i∈A⊂J`,
   \[
   D_A^C(w)= \sum_i ℓ_i²/w_i −\sum_i b_i w_i
   +\frac12\sum_{i,j}w_iC_{ij}w_j
   \ge \sum_i\left(ℓ_i²/w_i-b_iw_i+\frac12 c_i w_i²\right),
   \]
   where all off-diagonal contributions `w_iC_{ij}w_j` (`i≠j`) are dropped,
   not cancelled.

2. Completion of the square without cancellation. Split
   `c_i w_i²/2 = c_i w_i²/4 + c_i w_i²/4`. Then
   \[
   \frac{c_i}{4}w_i²-b_iw_i
   =\frac{c_i}{4}\Big(w_i-\frac{2b_i}{c_i}\Big)²-\frac{b_i²}{c_i}.
   \]
   Thus
   \[
   D_A^C(w)\ge \sum_i ℓ_i²/w_i + \frac14\sum_i c_i w_i² - K_A,
   \qquad K_A=\sum_i b_i²/c_i,
   \]
   which is exactly `E:gram-dual-coercivity`. The remaining term
   `(1/4)c_i w_i²` forces growth to `+∞`; no finite term can hide it.

3. Positive compact box. Take `w⁰=(1,…,1)`, `d_0=D_A^C(w⁰)`,
   `L_A=d_0+K_A`. Coercivity at `w⁰` gives
   `L_A ≥ ∑ℓ_i² + ∑c_i/4 > 0`. For any `w` with `D_A^C(w)≤d_0`,
   `E:gram-dual-coercivity` gives `∑ℓ_i²/w_i ≤ L_A` and
   `∑c_i w_i²/4 ≤ L_A`, hence per coordinate
   \[
   ℓ_i²/L_A \le w_i \le \sqrt{4L_A/c_i}.
   \]
   The sublevel is nonempty (`w⁰` is in it) and, as the preimage of
   `(−∞,d_0]` under the continuous `D_A^C` inside the closed box
   `∏[ℓ_i²/L_A, √(4L_A/c_i)]` (which lies in the open positive orthant), it is
   closed and compact.

4. Attainment and globality. A continuous function on a nonempty compact set
   attains its minimum. Outside the sublevel, values exceed `d_0`, while the
   sublevel contains a point of value `d_0`; hence the attained minimum is a
   global minimum on the whole positive orthant. (The proof phrases this via a
   "minimizing sequence chosen in the sublevel"; continuity plus compactness
   provides the same conclusion. This is a pre-existing mild imprecision, not a
   NEW modification; see Findings.)

5. Strict convexity and uniqueness. On a nonzero vector `ξ`, the Hessian of the
   smooth function `D_A^C` satisfies
   \[
   \sum_i \frac{2ℓ_i²}{w_i³}ξ_i² + \sum_{i,j}ξ_i C_{ij} ξ_j >0,
   \]
   since `ℓ_i>0`,`w_i>0` make the first sum strictly positive, and
   `∑ξ_iC_{ij}ξ_j = ‖∑ξ_ik_i‖² ≥0`. Hence the Hessian is positive definite on
   the convex open orthant, so the restriction to every nonconstant segment has
   positive second derivative; strict convexity gives uniqueness.

6. Exact stationarity. The minimum is interior, so each coordinate admits both
   sign perturbations. Differentiating,
   \[
   ∂_{w_i}D_A^C = -ℓ_i²/w_i² - b_i + \sum_{j∈A}C_{ij}w_j =0,
   \]
   which is `E:gram-dual-stationarity`. The right side
   `ℓ_i²/(w_i^A)²>0` because `w_i^A>0`.

**New explanations check.** The roadmap claims (i) coordinates are bounded away
from both zero and infinity, (ii) this attains an interior minimum, (iii)
strict Hessian positivity gives uniqueness and the stationarity equations.
Items (i)–(iii) are precisely steps 3–6 above, all valid under the stated
hypotheses. `Step 1`/`Step 2` headings match the content. No qualifier
(`ℓ_i>0`, `c_i=C_{ii}>0`, nonempty `A⊂J`) was dropped.

---

## P:gram-positive-optimizer

- Old reading: COMPLETE
- New reading: COMPLETE
- Public reconstruction: COMPLETE
- Original-step coverage: COMPLETE (no omissions identified)
- Argument preservation: PRESERVED
- New explanations: JUSTIFIED
- Evidence: OLD statement LF 103–112 / proof LF 114–145; NEW statement
  LF 115–124 / proof LF 126–170. Statement content is identical; the NEW proof
  adds a roadmap and two step headings only.

**Statement:** `E:gram-active-duality`, `𝓢(C)=max_{A⊂J} d_A^C`, with `Φ=0`
attaining for an empty maximizing subset and the positive conic
`Φ_A=∑_{i∈A} w_i^A k_i` attaining for a nonempty maximizing `A`; no primal or
subset uniqueness is asserted.

**Working (Step 1, upper bound).**

1. Active set. For arbitrary `Φ`, set
   `A(Φ)={i:⟨Φ,k_i⟩>b_i}`. If `k_i=0` then `⟨Φ,k_i⟩−b_i=−b_i≤0` (because
   `b_i≥0`), so `A(Φ)⊂J`. With `t_+=max(t,0)`, only strictly active indices
   contribute; indices with `⟨Φ,k_i⟩=b_i` are at the threshold and contribute
   zero.

2. Empty active set. If `A(Φ)=∅`, then every squared-root term vanishes and
   `𝔉_C(Φ)=−‖Φ‖²/2 ≤ 0 = d_∅^C`.

3. Nonempty active set. Fix any positive `w` on `A=A(Φ)`, put
   `t_i=⟨Φ,k_i⟩−b_i>0` and `z=∑_{i∈A}w_ik_i`. `L:gram-scalar-algebra`
   (`E:gram-sqrt-dual`) gives
   `2ℓ_i√t_i ≤ ℓ_i²/w_i + w_i t_i`, so summing over `A`
   \[
   𝔉_C(Φ)=2\sum_{i∈A}ℓ_i\sqrt{t_i}-\frac12‖Φ‖²
   \le\sum_{i∈A}\big(ℓ_i²/w_i + w_i(⟨Φ,k_i⟩-b_i)\big)-\frac12‖Φ‖²
   \]
   \[
   =\sum_iℓ_i²/w_i-\sum_i b_iw_i
   +\Big(⟨Φ,z⟩-\frac12‖Φ‖²\Big)
   \le\sum_iℓ_i²/w_i-\sum_ib_iw_i+\frac12‖z‖²
   =D_A^C(w),
   \]
   using `E:gram-hilbert-square` and the Gram identity in the last equality.
   Infimizing over `w>0` gives `𝔉_C(Φ)≤d_A^C`. Since `A(Φ)` ranges over the
   finitely many subsets of `J`, and `d_A^C` is finite by
   `L:gram-dual-minimum`, taking the supremum gives
   `𝓢(C) ≤ max_{A⊂J}d_A^C`. The exact order is: primal value → its own
   active-set dual value → max over subsets.

**Working (Step 2, attained converse).**

4. Empty case. `𝔉_C(0)=0` (all `(·)_+=0`, `‖0‖=0`) equals `d_∅^C=0`.

5. Nonempty case. For `A≠∅`, let `w^A` be the unique positive dual minimizer
   and put `Φ_A=∑_{i∈A}w_i^Ak_i`. By `E:gram-dual-stationarity`,
   \[
   ⟨Φ_A,k_i⟩-b_i=\sum_{j∈A}C_{ij}w_j^A-b_i
   =\frac{ℓ_i²}{(w_i^A)²}>0,
   \]
   so every `i∈A` is strictly active and
   `√(⟨Φ_A,k_i⟩−b_i)=ℓ_i/w_i^A`.

6. Both bounds are exact on the active sum. The scalar inequality is saturated
   because `w_i^A=ℓ_i/√t_i` with `t_i=ℓ_i²/(w_i^A)²`. The Hilbert inequality
   is saturated because `z=Φ_A` and `⟨Φ_A,z⟩−‖Φ_A‖²/2=‖z‖²/2`. Therefore the
   objective restricted to active terms equals
   \[
   \sum_{i∈A}\frac{ℓ_i²}{w_i^A}-\sum_{i∈A}b_iw_i^A+\frac12‖Φ_A‖²
   =D_A^C(w^A)=d_A^C,
   \]
   since `‖Φ_A‖²=∑_{i,j∈A}w_i^AC_{ij}w_j^A`.

7. Omitted vectors. For `i∉A`, the term
   `2ℓ_i√((⟨Φ_A,k_i⟩−b_i)_+)` is nonnegative (this uses `ℓ_i>0` and the
   nonnegativity of the square root; no outside inactivity is assumed). Hence
   `𝔉_C(Φ_A) ≥ d_A^C`, including the case `d_A^C<0`. Maximizing over `A⊂J`
   (including `∅`) yields `max_A d_A^C ≤ 𝓢(C)`. Combined with Step 1 this
   proves `E:gram-active-duality` and attainment. No concavity, invertibility,
   primal uniqueness, or outside inactivity is invoked anywhere.

**New explanations check.** The roadmap correctly summarizes both steps, and
the two headings match the actual content. The phrase "nonnegative conic
control" is accurate: `Φ_A` has strictly positive coefficients `w_i^A>0`.

---

## L:gram-realization

- Old reading: COMPLETE
- New reading: COMPLETE
- Public reconstruction: COMPLETE
- Original-step coverage: COMPLETE (no omissions identified)
- Argument preservation: PRESERVED
- New explanations: JUSTIFIED
- Evidence: OLD statement LF 157–161 / proof LF 163–181; NEW statement
  LF 182–186 / proof LF 188–208. NEW inserts the verification sentence
  "The inner products are `⟨k_1,k_i⟩=v_i` and
  `⟨k_i,k_j⟩=v_iv_j/c+B_{ij}=A_{ij}`, while `‖k_1‖²=c`," and is otherwise
  unchanged.

**Statement:** every finite real symmetric PSD matrix is a Gram matrix of
vectors in a finite-dimensional real Hilbert space; when its entries are
nonnegative, `𝓢(C)` is realization-independent.

**Working:**

1. Base and zero case. Induct on size; empty matrix realized in `{0}`. PSD
   gives each diagonal `C_{ii}=e_i^{⊤}Ce_i≥0`. If all diagonal entries vanish,
   evaluate the form on `e_i+t e_j`:
   \[
   (e_i+te_j)^{⊤}C(e_i+te_j)=2tC_{ij}\ge0\quad\forall t∈\mathbb R,
   \]
   forcing `C_{ij}=0`; hence `C=0`, realized by zero vectors.

2. Schur-complement step. Otherwise permute a positive diagonal entry `c` to the
   first position and write
   `C=[[c, v^T],[v, A]]`. Set `B=A-vv^T/c`. For any `y`, choose
   `x=(-v^Ty/c, y)`; then
   \[
   x^{⊤}Cx = c\left(\frac{v^Ty}{c}\right)^2
   -2\frac{v^Ty}{c}v^Ty+y^{⊤}Ay
   =\frac{(v^Ty)^2}{c}-2\frac{(v^Ty)^2}{c}+y^{⊤}Ay
   =y^{⊤}\Big(A-\frac{vv^T}{c}\Big)y
   =y^{⊤}By.
   \]
   Since `x^⊤Cx≥0`, `B` is PSD. By induction, realize `B` by vectors `u_i`.

3. Construction. Define `k_1=(√c,0)` and
   `k_i=(v_i/√c,u_i)` for the remaining indices. Then the NEW sentence's
   computation is exact:
   \[
   ‖k_1‖²=c,\qquad ⟨k_1,k_i⟩=√c·(v_i/√c)=v_i,
   \]
   and for `i,j≠1`,
   \[
   ⟨k_i,k_j⟩=\frac{v_iv_j}{c}+B_{ij}
   =\frac{v_iv_j}{c}+A_{ij}-\frac{v_iv_j}{c}=A_{ij}.
   \]
   Undoing the permutation finishes the realization. The remark that `B` need
   not have nonnegative entries is correct: only symmetric-PSD is required for
   the induction, and the construction imposes neither nonnegative coordinates
   nor complete positivity. This is precisely the possibly-signed
   Schur-complement case required by the task.

4. Realization independence. In any realization, `C_{ii}=0` means
   `‖k_i‖²=0`, so `k_i=0`, and the whole row
   `C_{ij}=⟨k_i,k_j⟩=0` vanishes. Since `E:gram-active-duality` expresses
   `𝓢(C)` through `C,ℓ,b` and the eligible set
   `J={i:C_{ii}>0}`, the value does not depend on the particular Hilbert space
   or vectors. This is asserted only in the nonnegative-entry scope, matching
   the scope of `P:gram-positive-optimizer`; the NEW text preserves this
   qualification.

**New explanations check.** The added inner-product verification is correct
term-by-term (computed above) and closes a previously implicit step, so it is
JUSTIFIED.

---

## P:gram-entrywise-comparison

- Old reading: COMPLETE
- New reading: COMPLETE
- Public reconstruction: COMPLETE
- Original-step coverage: COMPLETE (no omissions identified)
- Argument preservation: PRESERVED
- New explanations: JUSTIFIED (no new explanatory assertion was introduced;
  the proof is mathematically identical)

**Statement** (OLD LF 187–195, NEW LF 214–222): for symmetric PSD `C,D` on the
same finite index set with `0≤C_{ij}≤D_{ij}`, and the same `ℓ_i>0`,`b_i≥0`,
one has `𝓢(C)≤𝓢(D)`, with no PSD order on `D−C` required.

**Working:**

1. Well-definedness. `L:gram-realization` fixes each value because the entries
   `C_{ij},D_{ij}` are nonnegative. Eligible sets satisfy `J_C⊂J_D` since
   `C_{ii}≤D_{ii}` and `C_{ii}>0⟹D_{ii}>0`.

2. Pointwise dual comparison. For nonempty `A⊂J_C` and positive weights, the
   `ℓ` and `b` terms cancel:
   \[
   D_A^D(w)-D_A^C(w)
   =\frac12\sum_{i,j∈A}w_i(D_{ij}-C_{ij})w_j\ge0,
   \]
   because `D_{ij}−C_{ij}≥0` entrywise and `w_i>0`. This needs only entrywise
   order, not `D−C⪰0`.

3. Infimum monotonicity. Pointwise `D_A^D≥D_A^C` over the same positive orthant
   gives `d_A^C=inf D_A^C ≤ inf D_A^D=d_A^D` (all infima are attained/finite by
   `L:gram-dual-minimum`).

4. Global comparison. The empty values are both `0=d_∅^C=d_∅^D`. Since
   `J_C⊂J_D`, every maximization subset of the `C`-problem is available in the
   `D`-problem with a larger dual value:
   \[
   𝓢(C)=\max_{A⊂J_C}d_A^C
   \le \max_{A⊂J_D}d_A^D=𝓢(D),
   \]
   by `P:gram-positive-optimizer`. This includes eligible indices newly present
   for `D` (previously zero vectors for `C`). No PSD order is invoked anywhere.

**Evidence:** OLD LF 197–210 and NEW LF 224–237 are mathematically identical;
the difference formula and the two maxima are unchanged.

---

## AUDIT dispositions

No AUDIT-worthy issue is introduced by revision
`6bbb521412da88058c7ce4a9086a8117f9d1b6c8` in any of the five assigned proofs.

One pre-existing, non-blocking observation in `L:gram-dual-minimum` (present
identically in OLD): the sentence "A minimizing sequence chosen in the sublevel
has a convergent subsequence there" compresses the compactness argument. The
fully explicit conclusion follows from continuity of `D_A^C` on the nonempty
closed sublevel inside the positive compact box derived in
`E:gram-dual-coercivity`. This requires no repair of mathematics and is not a
defect introduced by the rewrite, so it does not change the verdict.

## Findings and limits

All five assigned proofs preserve their mathematics, hypotheses, constants, and
limiting structure. The NEW revision's only substantive additions are the
roadmaps/step headings in `L:gram-dual-minimum` and
`P:gram-positive-optimizer`, and the inner-product verification in
`L:gram-realization`; each new assertion was independently checked above.

Specific checks requested and completed: scalar square/completion identities
and the dual coercivity/coordinate bounds are reconstructed without
cancellation; compact positive sublevel attainment, interior minimizer, and
strict-Hessian uniqueness are explicit; stationarity yields strict activeness
and exact primal/dual equality at the positive conic candidate; nonnegative
omitted rewards and the empty active set are both handled; the exact sup/inf
order is preserved; no global primal concavity, primal uniqueness, outside
inactivity, or invertible Gram is assumed; real Gram realization is verified
through a possibly signed Schur complement with realization independence
scoped to nonnegative entries; entrywise comparison uses positive weights only,
never PSD order of `D−C`.

Limits: this review certifies only the assigned proof-pair comparison and
readability/argument preservation, not whole-book truth, not the unassigned
No-go `P:nogo-29`, and not the referenced local Lean certificates. The
unassigned model context (`H:homog`, Fourier covariance conventions) is not
used by these five proofs; no Fourier normalization or distributional kernel
appears in the assigned module, so no such normalization needed checking here.
Empty index sets, singular Grams, `H={0}`, and zero vectors are handled in the
assigned arguments as noted.
