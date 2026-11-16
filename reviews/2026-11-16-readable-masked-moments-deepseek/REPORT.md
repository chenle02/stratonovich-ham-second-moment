# Review Result
Category: proof-readability-equivalence
Model: deepseek-v4-pro
Verdict: PASS
Confidence: high

The three assigned proofs were read in full in both revisions (OLD/NEW as embedded).
Each old proof was read as COMPLETE, each new proof as COMPLETE. All three arguments
are preserved; the added sentences are explanatory/structuring, and each added
mathematical assertion I could check is justified under the unchanged hypotheses.
Statements and the module preamble (mask definition, chain-integral notation,
covariance `C_rho = K_eta(s-r) Gamma_{2epsilon}(z-w)`, bound `c_rho`, Green
measures with mass `r`) are byte-identical between revisions.

---

## L:masked-chain-comparison

- Old reading: COMPLETE
- New reading: COMPLETE
- Argument preservation: PRESERVED
- New explanations: JUSTIFIED
- Evidence:
  - Statement (OLD/NEW LF 23–37) is unchanged, including
    `E:masked-order-comparison` (`0 ≤ E[X^m_n X^m_k] ≤ E[X_n X_k]`), the odd
    vanish qualifier, and `E:masked-order-bound` with `q_n`.
  - The new proof inserts "Step 1/2/3" and an intro sentence; the underlying
    chain of implications is unchanged.
  - Chain mass: the recursion `f_n(t) = ∫_0^t (t-r) f_{n-1}(r) dr` with
    `f_0 = 1` and Green total mass `t-r` gives `t^{2n}/(2n)!`. Independent
    check: `f_1 = t^2/2 = t^2/2!`, `f_2 = ∫_0^t (t-r) r^2/2 dr =
    (1/2)(t^4/3 - t^4/4) = t^4/24 = t^4/4!`. The new sentence "Substituting
    `f_{n-1}(r) = r^{2n-2}/(2n-2)!`" is correct.
  - New Step 1 final paragraph ("This is the Bochner integrability condition…
    exchange expectation and the two chain integrals"): the absolute moment of a
    fixed number of source factors is bounded uniformly in the vertices by
    Hölder/scalar Gaussian moments; integrating a uniform bound against the
    finite measure `nu_n ⊗ nu_k` (mass `t^{2n}/(2n)! · t^{2k}/(2k)!`) is finite,
    so the interchange is valid. This is a faithful expansion of the OLD phrase
    "permits stochastic Fubini between two chains."
  - New Step 2 final paragraph: `E|X̄ - X|^2 = E X̄^2 + E X^2 - 2E[X̄ X]`; all
    three moments (two square, one cross) tend to the same unsmoothed Wick sum,
    so the combination → 0. This is exactly the OLD sentence "Square and cross
    moments between smoothed and unsmoothed integrals converge to the same
    diagram sum." Correct, and the clarifying "not just a limit of their
    variances" is accurate.
  - New Step 3 sentences: `C_rho ≥ 0` (since `K_eta > 0` and
    `Gamma_{2epsilon}(z-w) ≥ 0` for the nonnegative Radon measure `Gamma`), the
    product chain measure is positive, and `∏ m(z_i) ∈ [0,1]`; hence per-diagram
    finite nonnegative integrals only decrease. Correct.
- Lost steps/qualifiers: none. All retained items verified present in NEW:
  "including unequal and empty chains and every self-pairing"; "At n=k=0 both
  sides are one"; "no samplewise solution order or Gaussian covariance order is
  used"; the d=1,2 Green-smoothing qualifier; "No samplewise source bound on
  heat-kernel tails is needed"; "Consequently Lemma L:vertex-crude applies to
  the unmasked integrals"; and the application `k=n, y=x` for `E:masked-order-bound`.
- Pre-existing concerns: none identified within this read. The self-pairing and
  sphere-measure conventions are upstream declarations, not altered here.

---

## P:masked-source-moments

- Old reading: COMPLETE
- New reading: COMPLETE
- Argument preservation: PRESERVED
- New explanations: JUSTIFIED
- Evidence:
  - Statement identical (OLD LF 100–115, NEW LF 132–147), including the
    pre-existing grammatical slip "an Bochner" (unchanged, so not introduced).
  - `Q_T = Σ q_n(T) < ∞` by `E:vertex-summability`; the double-majorant bound is
    unchanged.
  - New Step 1 elaboration: the uniqueness bound `B M^n T^{2n}/(2n)!` → 0
    because `(2n)!` dominates every fixed power of `M T^2`; the existence of the
    constant `B` follows from continuity of the two solutions' difference on the
    compact cone. Both correct; the OLD "bounded by `B` on the larger compact
    cone" is what licenses `B`, and the note "applies separately on each fixed
    compact observation set and finite horizon" matches the OLD localization.
  - New Step 3 elaboration: `E|X^m_n X^m_k| ≤ ‖X^m_n‖_2 ‖X^m_k‖_2 ≤ q_n(t)q_k(t)`
    by Cauchy–Schwarz plus `E:masked-order-bound`; summing gives
    `(Σq_n)(Σq_k) = Q_t^2`, the absolute majorant. Correct.
  - Stationarity note: `E[u(x)u(y)] ≤ ‖u(x)‖_2 ‖u(y)‖_2`, and both second
    moments equal `E|u(0)|^2` under the unmasked law's stationarity (finite
    Picard integrals commute with translations; L² limits inherit it). Correct,
    and the explicit "Stationarity is not required of the masked solution" is
    retained. The new "geometric mean" phrasing duplicates Cauchy–Schwarz.
  - Step 4 unchanged: `L^2`-continuity of the Bochner term, `q_n` tails,
    Bochner average, absolute Fubini by `‖phi‖_1^2 Q_t^2`, and
    `phi ≥ 0` integration of the two-point inequality into
    `E:masked-average-source`.
- Lost steps/qualifiers: none. The per-`rho` identification via an a.s.
  convergent subsequence and "no common event over uncountably many widths is
  needed" are both retained in Step 2.
- Pre-existing concerns: none substantive; "an Bochner" is cosmetic and common
  to both revisions.

---

## P:masked-canonical-transfer

- Old reading: COMPLETE
- New reading: COMPLETE
- Argument preservation: PRESERVED
- New explanations: JUSTIFIED
- Evidence:
  - Statement identical (OLD LF 161–175, NEW LF 221–235): the fixed-`t` limit
    at arbitrary relative width rates and the explicitly conditional
    masked-limit premise (`E:masked-conditional-transfer`) are unchanged.
  - Step 1 reversal unchanged: `s'_j = t - s_{n+1-j}`, `z'_j = -z_{n+1-j}`.
    Evenness is what is needed: `K_eta` is even in `v` (integrates
    `e^{-lambda|v|}`), and `Gamma_{2epsilon}` is even by Hypothesis H:homog; so
    the covariance products are preserved under reversal and relabeling, giving
    the `P:mixed` initial-chain convention (also for an empty chain).
  - Step 2 elaboration: `|E|u_rho|^2 - E|u|^2| ≤ (finite-square error) + (two
    omitted tails)`; each tail is dominated by `q_n q_k` outside the square,
    summable via `Q_t^2`, and `δ → 0` yields whole-double-sum convergence. This
    is the OLD δ-argument made explicit; `2δ` vs `δ` is immaterial since δ is
    arbitrary.
  - Step 3 elaboration: `|E|B|^2 - E|A|^2| = |E(|B|-|A|)(|B|+|A|)| ≤
    ‖B-A‖_2 (‖B‖_2 + ‖A‖_2)`, using reverse triangle and Cauchy–Schwarz
    ("factoring the difference of squared norms"). Correct for real `A,B`
    (here real-valued). L² convergence bounds both norms on the right. The
    conditional premise sentence ("Existence of the masked limit remains an
    explicit premise here; the next section constructs it…") is retained.
- Lost steps/qualifiers: none. "arbitrary relative noise-width rates", "odd
  mixed moments stay zero", "Green-width identification removes Green smoothing
  first", "single-width diagram laws … without assigning a new pathwise
  realization" are all present.
- Pre-existing concerns: none identified within this read.

---

## AUDIT dispositions

No `AUDIT` markers exist in the new module (or the old). I found no
AUDIT-worthy defect introduced by the rewrite. One item worth dispositioning as
an observation, not a defect: the module never spells out the `Gamma = 0`
reduction. The upstream source construction (Proposition
`P:source-canonical-convergence`) is stated under "assume `Gamma ≠ 0` in the
construction". At `Gamma = 0`, `C_rho = 0`, so every diagram of total order
`≥ 2` vanishes, `u_rho = u = 1`, the comparison collapses to `0 ≤ 0 ≤ 0`
(and `1 ≤ 1` at `n = k = 0`), the order bounds hold since `1 ≤ q_0(t) =
e^{theta_0 t}`, and both moment limits equal `1`. Hence the conclusions remain
valid there, and Hypothesis H:homog's allowance of `Gamma = 0` is not broken;
the case is simply implicit. Identical in both revisions.

## Findings and limits

- Scope: exactly the three assigned proofs were reviewed; the unchanged
  statements/definitions/preamble were compared. Upstream lemmas
  (`L:vertex-crude`, `L:joint-fixed-order`, `P:mixed`,
  `L:source-pointfield-regularity`, `P:source-canonical-convergence`) were
  checked only for consistency of use against their stated conditions, not for
  internal validity (their proofs are not assigned).
- Usage-respect checks passed: `q_n` bounds apply to fixed positive widths
  (vertexwise); `L:joint-fixed-order` is invoked only after the Green-width
  identification, at arbitrary relative rates, including unequal/empty chains;
  `P:mixed` is used to identify the canonical sum of diagram limits; the
  covariance `K_eta Γ_{2epsilon}` matches the declared equal-width joint source
  covariance; `L:source-pointfield-regularity` supplies the per-`rho`
  continuous/smooth field version used for measurability, continuity, and
  spatial testing.
- Focus points confirmed: positive Green measures with mass `r` (sphere measure
  in d=3; the mass `r` is correct for the displacement Green measure in all
  d ∈ {1,2,3}); finite chain mass `t^{2n}/(2n)!`; Green smoothing before noise
  removal; all Wick pairings incl. self/unequal/empty; mask factors in `[0,1]`
  at expected-diagram level with the samplewise/arbitrary-phase-order use
  explicitly excluded; local-cone Picard existence/uniqueness; same-source
  pointwise versions per fixed `rho`; `Q_t^2` mixed-order majorant; stationarity
  only for the unmasked law; Bochner spatial testing; fixed-order canonical
  limits at arbitrary relative widths with an explicit conditional masked-limit
  premise; zero/order-zero and `Gamma = 0` cases (see AUDIT dispositions). No
  unitary Fourier inversion kernels are used in this module, so no
  distribution-scalar issue arises here.
- No primary source PDF/image or render was reviewed, and no Lean quotation
  correspondence, rendered pages, or release are certified. This PASS concerns
  scope preservation and justification of new explanations in this module only,
  not whole-book truth or the unassigned upstream proofs.
- Pre-existing cosmetic issue retained in both revisions: "an Bochner `L^2`
  integral" (P:masked-source-moments statement).
