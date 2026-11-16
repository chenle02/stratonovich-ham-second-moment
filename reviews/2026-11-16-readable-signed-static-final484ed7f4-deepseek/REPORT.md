# Review Result
Category: proof-readability-equivalence
Model: deepseek/deepseek-v4-pro
Verdict: PASS_WITH_NOTES
Confidence: high

Scope: the four assigned target proofs in `notes/integrated_signed_static.tex`, OLD revision `cdde711` vs NEW `484ed7f4`. All four statements are textually invariant (only local LF placement shifts). The NEW revision restructures three proofs into labelled steps and adds two clarifying computations; no constant, hypothesis, domain, normalization, or limiting convention changed. All four targets were read completely, and all original steps were reconstructed publicly. The signed setting is maintained throughout: no positivity of the potential, no ground state, and no spectral gap are imported; potential bounds use `|v_V(u,u)|` and AM–GM, and the upper bottom bound uses translation/dilation of a bump, not positivity of `V`.

---

## L:signed-limiting-multiplier

- Old reading: COMPLETE
- New reading: COMPLETE
- Public reconstruction: COMPLETE
- Original-step coverage:
  1. **Cauchy extraction of `V`.** Choose `L_{q_n} -> L` in `K(F)`. The constant-displacement state `(0,0,1,0)` has `F`-norm `1`, and
     `L_{q_n}(0,0,1,0) = (0,V_{q_n},0,0)`.
     Since the second `E`-coordinate of `(0,V_{q_n},0,0)` has norm `||V_{q_n}||_{H^{-1/2}}`,
     `||V_{q_n}-V_{q_j}||_{H^{-1/2}} = ||(L_{q_n}-L_{q_j})(0,0,1,0)||_F <= ||L_{q_n}-L_{q_j}||_{B(F)} -> 0`,
     so `V_{q_n}` is Cauchy and converges to a unique `V in H^{-1/2}`.
  2. **Support and zero columns.** Each `V_{q_n}` is supported in `supp m_R`; testing against smooth functions disjoint from `supp m_R` shows the limit is supported there. The first `E`-column and the two constant columns of `L_{q_n}` are zero; operator-norm convergence preserves each zero column.
  3. **Multiplier convergence.** For `(u,0,0,0)` with norm `||u||_{H^{1/2}}`,
     `||L_q(u,0,0,0)||_F = ||V_q u||_{H^{-1/2}}`, so `||M_{V_q}||_{B(H^{1/2},H^{-1/2})} <= ||L_q||_{B(F)}`.
     Therefore `||M_{V_{q_n}}-M_{V_{q_j}}|| <= ||L_{q_n}-L_{q_j}|| -> 0`; the multipliers converge in `B(H^{1/2},H^{-1/2})` to a limit `M` with `||M|| <= lim inf ||L_{q_n}|| = k`.
  4. **Identification on tests.** Smooth compact `u` multiplies `H^{-1/2}` boundedly (upstream `Lemma L:cutoff-factorization`), so `V_{q_n}u -> Vu` in `H^{-1/2}`; hence `Mu = Vu` on tests, and density of tests in `H^{1/2}` uniquely extends `M` to multiplication by `V` on `H^{1/2}`. The constant column recovers `V`, giving `L(u,v,c_1,c_2)=(0,Vu+c_1V,0,0)` and uniqueness.
  5. **Pairing bound.** For compact smooth `u,w`,
     `v_V(u,w)=<Vu,w>_{H^{-1/2},H^{1/2}} = <V,uw>`,
     so `|v_V(u,w)| <= ||Vu||_{H^{-1/2}}||w||_{H^{1/2}} <= k||u||_{H^{1/2}}||w||_{H^{1/2}}`,
     symmetric in `u,w`; bounded-bilinear extension to `H^{1/2}×H^{1/2}` follows by density.
  6. **Complexification.** A real-linear bounded operator extends complex-linearly with preserved norm: for `z=u+iv`,
     `||Tz||² = ||Tu||²+||Tv||² <= ||T||²(||u||²+||v||²)`.
     The Hermitian extension of `v_V` has diagonal `v_V(a+ib,a+ib)=v_V(a,a)+v_V(b,b)` since the real form is symmetric.

- Argument preservation: PRESERVED (OLD/NEW lines 21–37 are identical).
- New explanations: JUSTIFIED (no new text; nothing to flag).
- Evidence: `F`-norm normalization and the restriction bound `||M_{V_q}|| <= ||L_q||` above; `E:signed-multiplier-form` reproduced with `k`.
- Lost steps/qualifiers, unresolved issues, pre-existing concerns: none identified within this read. The proof depends on the unassigned smooth-multiplication boundedness (`L:cutoff-factorization`), applied under its stated hypotheses.

---

## P:signed-closed-form

- Old reading: COMPLETE
- New reading: COMPLETE
- Public reconstruction: COMPLETE
- Original-step coverage:
  1. **Coercivity.** With `b=||u||_2`, `z=||u||_{H^1}`,
     `||u||²_{H^{1/2}} = ∫<ξ>|û|² <= (∫|û|²)^{1/2}(∫<ξ>²|û|²)^{1/2} = bz`,
     and `|v_V(u,u)| <= Kbz <= (z²+K²b²)/2` by weighted AM–GM. Since `q_V = z²-b²-v_V(u,u)`,
     `q_V+cb² >= z²-b²-(z²+K²b²)/2+(2+K²)b² = z²/2+(1+K²/2)b²`,
     and
     `q_V+cb² <= (3/2)z²+(1+3K²/2)b² <= L_K z²`, `L_K=3(1+K²)`,
     because `b²<=z²` gives `(3/2)z²+(1+3K²/2)b² <= (5/2+3K²/2)z² <= 3(1+K²)z²`.
     The lower bound dominates both `z²/2` and `b²`, making the shifted form closed and norm-equivalent to `H^1` (`E:signed-form-bounds`).
  2. **Self-adjointness and form domain.** Closedness in the Teschl p. 80 sense and `Theorem 2.14, p. 81, (2.63)` give a unique self-adjoint `H_V`, independent of the admissible shift. `Theorem 3.6, (3.51)–(3.53), p. 109` after shifting give `D(A^{1/2})=H^1` (`E:signed-form-domain`). The form lower bound `q_V+c||·||²>=||·||²` implies the spectral lower bound `A>=1`: any bounded spectral slice below `1` would contradict the form bound on a unit `D(A)` test.
  3. **Fractional-power comparison.** Set `B_0=1-Δ`; the same form inequalities give `(1/2)B_0 <= A <= L_K B_0` on the common form domain `H^1`. For `T_0,S_0>=1` with common form domain and `q_{T_0}<=q_{S_0}`, completing the square gives the variational identity
     `<f,(T_0+t)^{-1}f> = sup_u{2Re<f,u>-q_{T_0}(u)-t||u||²} >= <f,(S_0+t)^{-1}f>`, `t>0`.
     Hence `(T_0+t)^{-1} >= (S_0+t)^{-1}`, so `I-t(T_0+t)^{-1} = T_0/(T_0+t) <= S_0/(S_0+t)`.
     The scalar identity `sqrt x = π^{-1}∫_0^∞ t^{-1/2}x/(x+t)dt` (substitute `t=xv²`) and positive spectral integration/Tonelli give `T_0^{1/2}<=S_0^{1/2}` with domain inclusions.
  4. **Quarter powers and negative phase.** Applying this to `(B_0,2A)` and `(A,L_K B_0)` yields, for fourth roots,
     `2^{-1/4}||u||_{H^{1/2}} <= ||A^{1/4}u||_2 <= L_K^{1/4}||u||_{H^{1/2}}` with `D(A^{1/4})=H^{1/2}` (`E:signed-quarter-phase`). For `v∈L²`, the dual norm of `u-><v,u>` against `||A^{1/4}u||_2` is `||A^{-1/4}v||_2`: Cauchy–Schwarz gives the upper bound, and `u=A^{-1/2}v` (or its normalization) attains it, so duality/completion identify the negative phase as `H^{-1/2}`.
- Argument preservation: PRESERVED. The NEW proof adds only an introductory sentence and `Step 1`/`Step 2` headings; all displayed mathematics and citations are unchanged (OLD 65–115 vs NEW 65–126, with the line increase attributable to headings/whitespace).
- New explanations: JUSTIFIED. The added summaries (“bound the signed potential form …”, “compare fractional powers through resolvent order”) accurately describe the unchanged content.
- Evidence: the explicit `b,z` computation, `L_K` verification, resolvent sup identity, and `sqrt x` scalar identity above reproduce all constants `c=2+K²`, `L_K=3(1+K²)`, `2^{-1/4}`, `L_K^{1/4}`.
- Lost steps/qualifiers, unresolved issues, pre-existing concerns: one pre-existing expository compression (identical in both revisions): the text derives only the `α=1/2` monotonicity identity, then says “Apply this to `(B_0,2A)` and `(A,L_K B_0)`” to get fourth-root comparisons. Reaching fourth roots needs the `α=1/4` analogue of the same resolvent-integral argument,
  `x^{1/4}=c_{1/4}∫_0^∞ t^{-3/4}x/(x+t)dt`, `c_{1/4}=1/(π√2)`,
  or the standard Löwner–Heinz conclusion. The conclusion is valid and the method is the one just proved; this is a terseness, not a new defect. Upstream Teschl citations remain imported inputs.

---

## L:signed-spectral-wave

- Old reading: COMPLETE
- New reading: COMPLETE
- Public reconstruction: COMPLETE
- Original-step coverage:
  1. **Lower bottom bound.** For unit `u`, `z=||u||_{H^1}>=1`, and
     `q_V(u) >= z²-1-(z²+K²)/2 = z²/2-1-K²/2 >= -(1+K²)/2 >= -K²`.
     Hence `β(V) >= -K²`.
  2. **Upper bottom bound without positivity.** Dilate a unit compact smooth bump (spreading it lowers `||∇u||_2 -> 0`) and translate its support off `supp m_R`. Then `v_V(u,u)=0` while the kinetic energy tends to zero, so `β(V)<=0`. Real and complex infima agree since a complex diagonal splits into two real diagonals.
  3. **Form/spectral bottom equality.** Teschl `(3.52)–(3.53)` identifies the form infimum with the spectral bottom; the two-sided slice argument (a spectral slice below the form bound would contradict a unit form test; the form integral is bounded below by the spectral infimum) gives `β(V)=inf spec H_V`.
  4. **Spectrum = PVM support.** For `z∉Σ` (closed support of the PVM), `(h-z)^{-1}` set to zero off `Σ` is a bounded Borel function whose calculus is the two-sided resolvent inverse; for `z∈Σ`, normalized projections on shrinking neighborhoods give approximate eigenvectors, so `z∈σ(H_V)`. Hence `λ=sqrt(-β)<=K`, and every spectral `h` satisfies `h+c>=2` because `h>=β>=-K²`, `c=2+K²`.
  5. **Phase norm and condition number.** `E_A` norm `||A^{1/4}u||²+||A^{-1/4}v||²`, with `M_K=L_K^{1/4}`, is equivalent to `E` with cost
     `M_K² = sqrt(3(1+K²)) <= 2(1+K)`.
  6. **Matrix and entry bounds.** In the `E_A` isometry the matrix is
     `[[C_t, sqrt(h+c)S_t],[-hS_t/sqrt(h+c), C_t]]`.
     For `h>=0`: `|C_t|<=1`, `sqrt(h+c)|S_t| <= 1+sqrt c t` (since `sqrt(h+c)min(t,h^{-1/2}) <= sqrt(1+ct²) <= 1+sqrt c t`), and
     `|hS_t|/sqrt(h+c) = |sqrt h sin(t sqrt h)|/sqrt(h+c) <= 1`; at zero the off-diagonals are `sqrt c t, 0`.
     For `β<=h<0`: `|C_t|<=e^{λt}`, `|S_t|<=t e^{λt}`, `sqrt(h+c)|S_t| <= sqrt c t e^{λt}`,
     and `|hS_t|/sqrt(h+c) = sqrt(-h)sinh(t sqrt(-h))/sqrt(h+c) <= K e^{λt}`, with no division by `λ`.
  7. **Total bound.** With `sqrt c <= 2K`, each entry is bounded by `2(1+K)(1+t)e^{λt}`; the `2×2` norm is at most twice an entry bound, and the condition-number cost gives
     `||P_V^E(t)|| <= 2(1+K)·2·2(1+K)(1+t)e^{λt} = 8(1+K)²(1+t)e^{λt}` (`E:signed-E-wave`).
     Bounded Borel calculus (Teschl `Theorem 3.1, (3.18)–(3.21)`) licenses the spectral estimate; dominated convergence gives strong continuity; scalar addition identities give the group property; the same bounds hold on the weighted graph levels via spectral cutoffs.
- Argument preservation: PRESERVED. Step 1/Step 2 reorganization is purely additive; all original estimates are retained.
- New explanations: JUSTIFIED. The added closing computation of `|hS_t|/sqrt(h+c)` for `h<0` is correct: `sqrt(-h)<=K`, `h+c>=2`, `sinh(t sqrt(-h))<=e^{λt}` give `<=K e^{λt}` (the implicit `sqrt 2` only improves the bound); the claim that it remains meaningful at `λ=0` is correct.
- Evidence: all matrix-entry bounds and the final `8(1+K)²` constant are reproduced above; `M_K²=sqrt(3(1+K²))<=2(1+K)` verified by squaring.
- Lost steps/qualifiers, unresolved issues, pre-existing concerns: none new. The `σ(H_V)=Σ` argument is condensed but standard and valid.

---

## P:signed-physical-wave

- Old reading: COMPLETE
- New reading: COMPLETE
- Public reconstruction: COMPLETE
- Original-step coverage:
  1. **Distributional equation and graph embedding.** Test the form representation (Teschl `Theorem 2.14, (2.63)`) against compact smooth functions to get `H_Vu=-Δu-Vu` for `u∈D(H_V)`. Then `u∈H^1` and `Vu∈H^{-1/2}`, so
     `(1-Δ)u = u-Δu = Hu+Vu+u = Au+Vu+(1-c)u ∈H^{-1/2}`,
     hence `u∈H^{3/2}` by Bessel invertibility. Graph continuity: `||u||²_{H^1}<=2<Au,u> <=||Au||²+||u||²` from `E:signed-form-bounds`, and
     `||u||_{H^{3/2}} ≍ ||(1-Δ)u||_{H^{-1/2}} <= ||Au|| + ||Vu||_{H^{-1/2}} + |1-c|||u|| <= C(||Au||+||u||_{H^1})`,
     which is controlled by the graph norm `||Au||+||u||`. So `D(H_V)↪H^{3/2}` graph-continuously.
  2. **Free generator.** `A_0(u,v)=(v,Δu)` on `H^{3/2}×H^{1/2}` by differentiating the Fourier matrix after a frequency cutoff and removing it; strong-generator derivatives force `v∈H^{1/2}` and `Δu∈H^{-1/2}`, i.e. `u∈H^{3/2}`. No operator-norm derivative of the group is used.
  3. **Graph trajectories and Duhamel.** Starting from `D(A)×D(A^{1/2})=D(H_V)×H^1`, spectral cutoffs and dominated convergence give continuous graph trajectories and `C^1` trajectories in `H^1×L²` with `u_t=v`, `v_t=-H_Vu`; projections `1_{[1,n]}(A)` approximate graph data and the weighted matrix bounds control tails. Since `z_t=A_0z+L_Ez`, the strong-group chain rule on `D(A_0)` gives
     `S_E(-t)z(t)=z(0)+∫_0^t S_E(-s)L_Ez(s)ds`.
     `D(H_V)×H^1` is dense in `E` (`D(A)` dense in `D(A^{1/2})=H^1`; `H^1` dense in `H^{1/2}` and `H^{-1/2}`), and finite-horizon boundedness extends the identity to all `E`; Volterra/Picard uniqueness identifies the physical wave. No `D(A^{3/4})=H^{3/2}` identity is asserted.
  4. **Young flow on F.** Bounded `L∈K(F)` and strongly continuous `S_F` define a unique Duhamel flow with `n`-th Volterra term bounded by `C_T^{n+1}||L||^nT^n/n!`. Compactness of `L` and strong continuity of `S_F` and `S_F^*` give norm continuity of `S_F(-s)LS_F(s)` (as in upstream `P:cameron-actual-embedding`), so the interaction primitive is Lipschitz and its ordinary equation is exactly the Young equation.
  5. **Constant columns and final bound.** For initial `(e,c_1,c_2)` the constant coordinates are `(c_1+tc_2,c_2)`, and the `E` component is
     `P_V^E(t)e+∫_0^t P_V^E(t-s)(0,V(c_1+sc_2))ds`;
     the finite-time Fubini/triangle argument from `E:compact-F-block` verifies it solves the full system, so uniqueness identifies it; no ground positivity or gap is used. The forcing has norm `<=K(1+s)|(c_1,c_2)|`. Since `λ>=0` and `∫_0^t(1+t-s)(1+s)ds = t+t²+t³/6 <= (1+t)^3`, the total is at most
     `(1+t)^3e^{λt}{8(1+K)²||e||+[8K(1+K)²+1]|(c_1,c_2)|}`,
     where the `+1` covers the constant-coordinate block. Then `8(1+K)²<=8(1+K)^3` and `8K(1+K)²+1<=9(1+K)^3`, so Cauchy–Schwarz on the two components gives factor `sqrt(8²+9²)<13`, hence
     `13(1+K)^3(1+t)^3e^{λt}||(e,c_1,c_2)||_F`,
     which implies the stated sufficient bound `16(1+K)^4(1+t)^3e^{λt}` (`E:signed-F-wave`) since `13 <=16(1+K)` for `K>=1`.
- Argument preservation: PRESERVED. The NEW proof restructures into Steps 1–4 and inserts explanatory sentences; all substantive estimates are unchanged.
- New explanations: JUSTIFIED. The added coefficient bounds in Step 4 are correct as computed above; the step headings accurately describe the unchanged arguments.
- Evidence: the `(1-Δ)u=Au+Vu+(1-c)u` identity, graph-norm bound, chain-rule Duhamel, forcing triangle `t+t²+t³/6<= (1+t)^3`, and `13(1+K)^3 -> 16(1+K)^4` step are all reproduced.
- Lost steps/qualifiers, unresolved issues, pre-existing concerns: none new. The compact-conjugation continuity and free-group facts are unassigned upstream inputs used under their stated hypotheses; `E` is not treated as dense in `F` (only density within `E` is used, and constants are handled separately).

---

## AUDIT dispositions

| label | Old reading | New reading | Reconstruction | Preservation | New explanations |
|---|---|---|---|---|---|
| L:signed-limiting-multiplier | COMPLETE | COMPLETE | COMPLETE | PRESERVED (identical) | JUSTIFIED (no new text) |
| P:signed-closed-form | COMPLETE | COMPLETE | COMPLETE | PRESERVED (additive headings only) | JUSTIFIED |
| L:signed-spectral-wave | COMPLETE | COMPLETE | COMPLETE | PRESERVED (restructured; one correct addition) | JUSTIFIED |
| P:signed-physical-wave | COMPLETE | COMPLETE | COMPLETE | PRESERVED (restructured; one correct addition) | JUSTIFIED |

All four target proofs were read completely in both revisions, and each original logical step was reconstructed publicly, including the unchanged limiting-multiplier proof.

---

## Findings and limits

**Preservation.** The NEW revision makes no mathematical change: statements are textually invariant, and the only proof deltas are step headings/introductory summaries plus two clarifying computations (the `h<0` lower off-diagonal spectral entry and the final coefficient Cauchy–Schwarz). Both additions are correct under the unchanged constants and normalizations. No constant, domain, shift `c=2+K²`, `A>=1`, `L_K`, phase norm, or limiting convention changed.

**Signed setting maintained.** Potential bounds use `|v_V(u,u)|<=Kbz` and AM–GM; the upper bottom bound `β(V)<=0` comes from translating/dilating a bump off `supp m_R`, not from positivity of `V`. No ground state, gap, or nonnegative potential property is imported from the unassigned compact-family context. The proofs assert only `D(H_V)↪H^{3/2}` (not an `H²` operator domain), and explicitly avoid `D(A^{3/4})=H^{3/2}`.

**Pre-existing concerns noted.** (i) In `P:signed-closed-form` the quarter-power comparison is terse: the text writes only the `α=1/2` scalar identity and then applies the method to get fourth roots; the `α=1/4` analogue (`x^{1/4}=c∫t^{-3/4}x/(x+t)dt`) or Löwner–Heinz completes it. This is identical in both revisions and is an expository compression, not a new defect. (ii) Several inputs are imported and unassigned (Teschl form/spectral theorems, `L:cutoff-factorization`, `L:constant-phase-free`, `P:cameron-actual-embedding`); their application hypotheses were checked in the target deductions, but their own proofs were not reviewed or counted.

**Limits.** This review certifies rewrite-preservation of the four assigned target proofs only. It does not certify upstream analytic results, primary-source PDF/image correctness, Lean correspondence, rendered pages, human sign-off, or whole-book/release status. All reading was from the embedded OLD/NEW module and the supplied UNASSIGNED context statements.
