# Review Result
Category: proof-readability-equivalence
Model: deepseek-v4-pro
Verdict: PASS_WITH_NOTES
Confidence: high

Scope note. I compared the seven assigned OLD/NEW proof pairs in
`notes/integrated_raw_block_lower.tex` against the supplied unassigned baseline
contexts (`integrated_constant_phase_young`, `integrated_compact_mean_family`,
`integrated_masked_moments`, `integrated_exact_scaling`,
`integrated_source_convergence`, `integrated_actual_operator_driver`,
`notes_stratonovich_ham_second_moment` excerpts). Upstream proposition *proofs*
are not re-audited here; I checked only that target consumers invoke them under
their stated hypotheses and that every target deduction reconstructs from them.
The rewrite is a step-numbered reorganization with added motivation and
citations. I found no quantitative change and no dropped qualifier in any of the
seven proofs. The notes below record the reconstructed working and the
justification of the added sentences.

---

## L:raw-block-inputs
Old reading: COMPLETE
New reading: COMPLETE
Public reconstruction: COMPLETE
Argument preservation: PRESERVED
New explanations: JUSTIFIED

Original-step coverage and working.

1. Pullback isometry. For the covariance of `W(F)=∫F(t,x)W` with temporal
   kernel `|t-s|^{-a}` and spatial form `Γ`, the test `T_{δ,m}f =
   δ^{a/2-1}f((s-s_m)/δ,x)` gives, under `s=s_m+δu`, `t=s_m+δr`:
   ```
   ds dt = δ^2 du dr,  |s-t|^{-a} = δ^{-a}|u-r|^{-a},
   (δ^{a/2-1})^2 = δ^{a-2},
   ```
   total factor `δ^{a-2}δ^2δ^{-a}=1`. Hence `T_{δ,m}` is an isometry of the
   original test completion and annihilates covariance-null tests
   (`E:raw-block-pullback`). The common-space identity `W_{δ,m}(f)=
   W_fast(f(·-mB,·))` follows since `s_m=mδB`.
2. Separable path space `B_0`. Finite-rank rational matrices are norm-dense in
   `K(F)` via `P_nTP_n→T`; polygonal rational paths with the interpolation
   bound `[f]_θ ≤ (2‖f‖_∞)^{1-θ}Lip(f)^θ` give `C^θ`-separability. Finite
   coefficient paths `iA_jL_ψ` are Lipschitz compact-valued; their Gaussian
   sums converge in `L^pC^θ`.
3. Joint Gaussianity and moment bound (`E:raw-block-moments`). For finite
   coordinate lists including `Z`, Gaussianity is retained through `L^2` limits
   via convergence of variances and characteristic functions. `(X,Z)` is the
   asserted Banach Gaussian variable; `E‖XZ‖≤‖X‖_2√v<∞` gives the Bochner
   covariance.
4. Covariance direction. The test pullback and the mean pairing of
   `L:compact-raw-profile` give
   ```
   E[W_{δ,m}(f)Z] = δ^{a/2}∫ f(u,x) h_{s_m+δu}(x) dx du
   ```
   (`E:raw-block-mean-jacobian`): the time-substitution Jacobian `δ` converts
   `δ^{a/2-1}` into `δ^{a/2}`. Multiplying by `g_δ=δ^{(1-a)/2}` gives
   `g_δδ^{a/2}=√δ`, so the operator-path cross-covariance with `Z` is
   `√δ H_m`, i.e. `b=√δ H` (`E:raw-block-covariance`). The extension from
   matrix-entry tests on `E` to all of `F` uses `E:driver-covariance-row`, the
   indicator approximation with `|u-r|^{-a}Γ` domination, both constant
   columns and density of `E⊕R^2` in `F`.

Added explanations in NEW are justified:
- Step 2’s claim that `W_{δ,m}` has the same Gaussian law as `W` and therefore
  `P:constant-phase-driver` supplies the same `C_{R,B}√p` norm bound: correct,
  because the bound depends only on the law/moment structure of the noise and
  the pullback is an isometry; the `g_δ` factor is then pulled out.
- Step 3’s inserted matrix-entry substitution (`ζ_R1_{(0,u)}v_zG_w`) and the
  constant-column identity “free displacement from `(c_1ψ,c_2ψ)` equals
  `c_1+t c_2` on `B_{2R}` for `t≤B`”: justified by `L:constant-phase-free`
  (constant block `(c_1,c_2)↦(c_1+tc_2,c_2)`), `ψ=1` on `B_{2R+B+1}⊃B_{2R}`,
  finite propagation, and the fact `S_F(-r)i=iS(-r)`.

No step or qualifier is lost. No independent audit-worthy defect identified.

---

## P:raw-block-gaussian-law
Old reading: COMPLETE
New reading: COMPLETE
Public reconstruction: COMPLETE
Argument preservation: PRESERVED
New explanations: JUSTIFIED

Original-step coverage and working.

1. Finite-coordinate shift. For real `s`, the density `e^{-sZ-s²v/2}` is an
   equivalent probability `Q_s` (complete the square in the `N(0,v)` density:
   `e^{-sZ-s²v/2}e^{-Z²/(2v)}=e^{-(Z+sv)²/(2v)}`). For finite continuous
   coordinates `ℓ`, `(ℓ(X),Z)` is equal in law to `(TG,z·G)` with a positive
   covariance square root (no inverse is needed when the covariance is
   singular), `Tz=ℓ(b)`, `|z|²=v`. Substituting `G'=G+sz` gives
   `E_{Q_s} f(ℓ(X+sb)) = E f(ℓ(X))`.
2. Norm-Borel passage. Matrix entries at rational times plus `0,B` generate
   the norm-Borel σ-field; for a dense set `D` of unit vectors,
   `‖T‖=sup_{u,w∈D}|⟨Tu,w⟩|`; suprema over rational times dominate the
   sup/Hölder norms; separability makes open sets countable unions of balls;
   cylinders form a ∩-stable generator. Uniqueness extends the finite equality;
   simple-function/monotone convergence gives the nonnegative identity.
3. Choose `s=δ^{-1/2}`; then `sb = δ^{-1/2}(√δ H)=H` using
   `E:raw-block-covariance`.

The only NEW change is cosmetic step headings. The sign algebra is reproduced
correctly: `E j(X)=E[e^{-Z/√δ-v/(2δ)}j(X+H)]`, consistent with the `Q_s` shift
and with `s²v/2=v/(2δ)`. The two No-go remarks and the “no translated
exceptional-domain assumption” clause are retained verbatim.

---

## L:raw-block-uniform-error
Old reading: COMPLETE
New reading: COMPLETE
Public reconstruction: COMPLETE
Argument preservation: PRESERVED
New explanations: JUSTIFIED

Original-step coverage and working.

1. Moment bound of the maximum. For finite families the `p`-power of a maximum
   is bounded by the sum of the `p`-powers, so, with `N+1≤2/δ`,
   ```
   ‖M_δ‖_p ≤ (N+1)^{1/p}C√p g_δ ≤ C'√p δ^{(1-a)/2-1/p}.
   ```
   For fixed `q` take `p>max(q,2/(1-a))`, giving `M_δ→0` in `L^q`.
2. Exponential square moment. For `n≥n_0` with `n_0(1-a)≥1`,
   ```
   E M_δ^{2n} ≤ 2C^{2n}(2n)^n δ^{n(1-a)-1} ≤ 2C^{2n}(2n)^n.
   ```
   `n!≥(n/e)^n` gives `(2n)^n/n!≤(2e)^n`, so the tail of the exponential series
   is at most `2∑_{n≥n_0}(2ecC²)^n`, geometric for small `c`
   (`E:raw-block-maximum-exponential`).
3. Deterministic comparison. `H_m^stat` is the constant-potential primitive;
   `P_{s_m}(u)=S_F(u)U_{H_m^stat}(u,0)`. The coefficient `V_s` is Lipschitz in
   `L^∞` and `L^2` with `|V_{s_m+δr}-V_{s_m}|≤CδB`; integrating the bounded
   free groups bounds the primitive difference by `C_Bδ` in `C^θ` (the two `B`
   factors are absorbed into `C_B`). On `{M_δ≤1}`, local Young stability on the
   ball of radius `H_0+1` gives `E_{op,δ}≤C(M_δ+δ)`, hence convergence in
   probability.
4. Uniform integrability. The global Young growth bound
   `max_m sup_u‖D_m^+(u)‖≤C_B exp(C_B(1+H_0+M_δ)^{1/θ})`; since `θ>1/2`
   (`1/θ<2`), every finite power is dominated by a constant times
   `e^{cM_δ²}`, giving uniform higher moments and hence `L^q` convergence
   (`E:raw-block-operator-error`). Measurability uses dense unit states and
   rational times.

The NEW Step 2 citations to `P:constant-compact-base` (primitive/Lipschitz
bound for `V_{s_m+δr}`, `V_{s_m}`, and their difference) and to
`P:constant-young-linear` (local stability and growth) are exactly the
statement being used; the hypotheses (fixed compact support, continuous
derivatives, `g_δ` bounded) hold. No change in the estimates.

---

## L:raw-block-indexed-cone
Old reading: COMPLETE
New reading: COMPLETE
Public reconstruction: COMPLETE
Argument preservation: PRESERVED
New explanations: JUSTIFIED

Original-step coverage and working (the order of choices is the key check).

1. Margins chosen first: `a_*,j_*` positive by `E:compact-positive-margins`,
   `M_e,M_ℓ,M_P,M_Q=M_P+1,M_z=M_e+1,E_0=1,H_obs` finite; aperture
   `ϑ=min(1,j_*/(16H_obsC_gap))`; then `B` with
   `q_B=C_gap e^{-η_gapB}≤min(1/8, ϑa_*/(8M_QE_0))`; then `ν` with
   `νM_z≤min(ϱ/2,ϑ,1/4)`; then `ω` from uniform continuity of `ℓ_s,Π_s`; then
   the five smallness conditions on `ε_op`.
2. Entrance. `ℓ_sP_s(B)=e^{λ_sB}ℓ_s`, `Q_sP_s(B)=P_s(B)Q_s`
   (`E:compact-F-eigen`), so the normalized entrance amplitude is `ℓ_s(e_0)`
   and the unperturbed residual is `≤q_BM_QE_0` by
   `E:compact-normalized-complement`. With perturbation (using `e^{-λ_sB}≤1`)
   the normalized amplitude is `≥a_*/2` and the residual `≤ϑa_*/4`.
3. Rebase and propagate. For `z=Ae_b+r` and adjacent `c`, since
   `Q_c-Q_b=Π_b-Π_c`:
   ```
   ℓ_c(z) ≥ (1-νM_z)A,   ‖Q_cz‖ ≤ (ϑ+νM_z)A.
   ```
   For `D` near `P_c(B)`, `x=e^{-λ_cB}ℓ_c(Dz)`, `y=e^{-λ_cB}‖Q_cDz‖`:
   ```
   x ≥ (1-νM_z-M_ℓε_opM_z)A ≥ (1-ϱ)A > A/2,
   y ≤ [q_B(ϑ+νM_z)+M_Qε_opM_z]A ≤ (1/8·2ϑ+ϑ/4)A = ϑA/2,
   ```
   hence `y≤ϑx`. Each full block preserves the cone and multiplies the
   amplitude by `e^{λ_cB}(1-ϱ)`.
4. Terminal block. Rebase to `σ_N` gives `ℓ_c(z)≥3A/4`, `‖Q_cz‖≤2ϑA`; the
   normalized observable is `≥3j_*/4-2H_obsC_gapϑ-j_*/8≥j_*/2` using
   `16H_obsC_gapϑ≤j_*` and `H_obsε_opM_z≤j_*/8`. Combining entrance, `N-1`
   intermediate blocks and the terminal estimate gives `c_*=a_*j_*/4`
   (`E:raw-block-positive-product`), including `N=1` and `u=0`.

The NEW Step 1 attribution to `P:compact-F-projection`/`E:compact-positive-margins`
for positivity and uniform continuity is the exact stated input; Step 2’s use
of `E:compact-F-eigen` is correct. The added explanations of `Q_c-Q_b=Π_b-Π_c`,
the two rebasing errors, and the `u=0`/`N=1` cases all check. The determinant
argument is unchanged and holds for every `N≥1` with no independence,
positivity or composition hypotheses on the `D_m`.

---

## L:raw-block-restart
Old reading: COMPLETE
New reading: COMPLETE
Public reconstruction: COMPLETE
Argument preservation: PRESERVED
New explanations: JUSTIFIED

Original-step coverage and working.

1. Coupled regularization. One regularized slow noise `Y_{ε,η}` on an extension
   preserving `W` defines `Y_fast(f)=Y_{ε,η}(T_{δ,0}f)`,
   `Y_m(f)=Y_{ε,η}(T_{δ,m}f)`. `E:source-two-dominations` gives source/residual
   variance bounds `≤‖f‖²_{H_W}`; residual tends to zero testwise; joint
   Gaussianity retained; `P:source-gaussian-transfer` gives `L^pC^θ`
   operator-path limits on `[0,L_ext]` and `[0,B]` including both constant
   columns.
2. Field/temporal identity. `Y_fast(u,x)=δ^{a/2}Y_{ε,η}(δu,x)` and
   `Y_m(u,x)=Y_fast(mB+u,x)` by change of variables in the test integrals.
   The temporal kernel check:
   ```
   δ^a K_η(δr) = δ^a Γ_E(a)^{-1}∫_0^{η^{-1}}e^{-λδr}λ^{a-1}dλ
               = Γ_E(a)^{-1}∫_0^{δ/η}e^{-μr}μ^{a-1}dμ = K_{η/δ}(r).
   ```
   The ordinary primitives identify with the Gaussian operator paths by the
   indicator approximation of `E:raw-block-mean-jacobian` plus the point-test
   integral identity.
3. Restart identity. Change of variables and composition of free groups give,
   on `F`,
   ```
   S_F(mB)[A_glob^src(mB+u)-A_glob^src(mB)]S_F(-mB)=X_m^src(u).
   ```
   Restriction/difference/conjugation are bounded on fixed-horizon `C^θ`
   spaces; the source limit passes the identity through. Conjugating the global
   Young equation on `[mB,mB+u]` gives the local equation driven by `X_m`;
   uniqueness identifies it with `U_{X_m}`, proving
   `E:raw-block-restart`. Using `iS(-r)=S_F(-r)i`, the deterministic primitive
   for `V_{δt}` satisfies the identical cocycle, so the shifted identity holds
   with `X_m+H_m`; composition identifies the full product with terminal `τ`.
4. Source limit of finite products. At fixed `δ,N`, with factor bound `C`
   and max factor difference `e_src`, the recurrence
   ```
   d(n+1) ≤ C d(n) + C^n e_src,  d(0)=0,
   ```
   comes from adding/subtracting a source factor at the next product; no
   commutativity of factors is used. It yields `d(N+1)≤(N+1)C^{N+1}e_src`
   (using `C≥1`); Hölder with exponents `4(N+1)` and `4` gives the `L²`
   limit:
   ```
   ‖d(N+1)‖_{L²} ≤ (N+1)‖C‖_{L^{4(N+1)}}^{N+1}‖e_src‖_{L^4} → 0.
   ```

The NEW Step 1 citation (`P:source-canonical-convergence` for the field-test
identity, `L:constant-source-response` for the primitive identification) is an
accurate localization of the two facts actually used; the Step 4 citations to
`P:constant-gaussian-flow` (unshifted factors) and `P:constant-compact-base`
with `g=g_δ` plus the fixed mean `V_{δt}` (shifted factors) are valid because
`g_δ≤1` and `V_{δτ}` has `δτ∈[0,2]`. The “no mask commuted through a wave
group” and “no finite-source Cameron mean is substituted” qualifiers are kept.

---

## P:raw-block-point-comparison
Old reading: COMPLETE
New reading: COMPLETE
Public reconstruction: COMPLETE
Argument preservation: PRESERVED
New explanations: JUSTIFIED

Original-step coverage and working.

1. Gaussian identity. With
   ```
   j_δ(x)=|O_φ D_{x_N}(τ)D_{x_{N-1}}(B)···D_{x_0}(B)e_0|²,
   ```
   which is continuous and nonnegative on all of `B_δ` (everywhere-defined
   Young map, fixed-time bounded free groups, finite products, bounded `O_φ`),
   `P:raw-block-gaussian-law` gives `E|U_{δ,B}|²=E[e^{-Z/√δ-v/(2δ)}Y_{δ,B}²]`
   (`E:raw-block-square-identity`) since `D_m^0=D_{X_m}`,
   `D_m^+=D_{X_m+H_m}`. Unweighted finite moments follow from Gaussian path
   bounds and Hölder at fixed `δ,N`.
2. Amplitude rescaling. `Γ_δ=g_δ²Γ`, `W'=g_δW_fast`, same admissible class
   (degree `α`, temporal `a` unchanged); linearity in noise makes the `n`-th
   source chain carry `g_δ^n`.
3. Source-limit premise. Factors `F_m=D_m^0(B)` (`m<N`), `F_N=D_N^0(τ)`, and
   ordinary source factors `F_{m,ρ}`. `L:raw-block-restart` and
   `P:constant-gaussian-flow` give factor `L^q` convergence and uniform norm
   moments. With `n=N+1`, `C_ρ`, `e_ρ`, telescoping gives
   `‖F_{N,ρ}···F_{0,ρ}-F_N···F_0‖≤nC_ρ^n e_ρ` (each telescoped term has one
   factor error and at most `n-1` factors bounded by `C_ρ`). Hölder:
   ```
   ‖·‖_{L²} ≤ n‖C_ρ‖_{L^{4n}}^n‖e_ρ‖_{L^4} → 0.
   ```
   `L:constant-source-solution` (same `m_R`, `e_0`) identifies the source
   product with the ordinary masked solution at `L=1/δ`; hence `U_{δ,B}` is its
   `L²` limit.
4. Masked comparison. `P:masked-source-moments` (mask factor `0≤m_R≤1` per
   vertex, positive Green measures, unequal/self/empty chains) plus the
   discharged premise of `P:masked-canonical-transfer` give
   `E U_{δ,B}²≤E|u_{Γ_δ}(L,0)|²`. Only the unshifted source product is needed.
5. Scaling identity. `g_δY_fast(u)=√δ Y_{ε,η}(δu)`; the fast→slow change
   `t=δu` with phase `(V,δV_t)` transforms the unmasked equation into the
   regularized form of `E:exact-fast-equation`. `L:exact-canonical-scaling`
   gives `E|V_δ(1,0)|²=E|u(T,0)|²` with `δ=T^{-κ}`
   (`E:raw-block-original-comparison`).

The NEW Step 3 explanation of the telescoping bound (“one factor error, at most
`n-1` factors `≤C_ρ`, `C_ρ≥1`”) correctly justifies `≤nC_ρ^n e_ρ`. The
physical-scale/mask-radius distinction and “mask need not contain the growing
backward cone” qualifier are retained.

---

## P:raw-block-original-lower
Old reading: COMPLETE
New reading: COMPLETE
Public reconstruction: COMPLETE
Argument preservation: PRESERVED
New explanations: JUSTIFIED

Original-step coverage and working.

1. Cone constants fixed before `δ↓0`. Choose `ϱ<1/2` with
   `log(1-ϱ)>-e_rate/3`, then `B=B(e_rate)` from `L:raw-block-indexed-cone`.
2. Union bound without independence. For `p>2/(1-a)`, `γ_p=p(1-a)/2-1>0`:
   ```
   P(M_δ>η) ≤ η^{-p} Σ_{m=0}^N E‖X_m‖_{C^θ}^p
             ≤ η^{-p}(N+1)(C_{R,B}√p)^p δ^{p(1-a)/2}
             ≤ A_pη^{-p}δ^{γ_p},  A_p=2(C_{R,B}√p)^p.
   ```
3. Deterministic tolerance. The primitive bounds of
   `L:raw-block-uniform-error` give `max_m max(‖H_m‖,‖H_m^stat‖)≤H_0` and
   `max_m‖H_m-H_m^stat‖≤C_Bδ`; `P:constant-young-linear` on the ball of radius
   `H_0+1` gives `E_{op,δ}≤L_B(M_δ+δ)` on `{M_δ≤1}`. With
   `η=min(1,ε_op/(2L_B))` and `δ≤ε_op/(2L_B)`, `M_δ≤η` implies
   `E_{op,δ}≤ε_op`.
4. Single good event and bound.
   ```
   E_δ={E_{op,δ}≤ε_op}∩{|Z|≤δ^{-1/4}},  p_δ:=P(E_δ)
   p_δ ≥ 1-A_pη^{-p}δ^{γ_p}-vδ^{1/2} → 1.
   ```
5. Riemann sum and cone lower bound. On `E_δ`:
   ```
   δlogY_{δ,B} ≥ δlogc_* + δ(N-1)log(1-ϱ) + δBΣ_{m<N}λ_{s_m} + δτλ_{s_N}.
   ```
   Since `s_N+δτ=1`, the last two terms are the left Riemann sum for `I_R` on
   `[0,1]` with mesh `≤δB`; error `≤C_λδB`. Also
   `0≤δ(N-1)≤1/B≤1`, so `δ(N-1)log(1-ϱ)≥log(1-ϱ)>-e_rate/3`. Combined with the
   two other losses `≤e_rate/3` each:
   `Y_{δ,B}≥exp((I_R-e_rate)/δ)` on `E_δ`, including `N=1` and `τ=0`.
6. Shifted second-moment identity. On `E_δ`, `-Z/√δ≥-δ^{-3/4}`:
   ```
   E|u(T,0)|² ≥ E U_{δ,B}² ≥ p_δ exp(2(I_R-e_rate)/δ - v/(2δ) - δ^{-3/4}).
   ```
   Taking `δlog`:
   ```
   δlogE|u(T,0)|² ≥ 2I_R-2e_rate-v/2 -δ^{1/4}+δlogp_δ.
   ```
   `δ^{1/4}→0` and `δlogp_δ→0`. Since `κ>0`, `δ=T^{-κ}` bijects large `T` with
   small `δ`, giving `Q_2≥2I_R-2e_rate-v/2`; `e_rate↓0` only after `δ↓0` for
   each fixed `B(e_rate)`. Final step: translation invariance of the noise law,
   Green kernels and constant initial data replaces `0` by any fixed `x`.

The NEW Step structure reproduces exactly these estimates; Step 4’s phrase “the
quadratic Gaussian cost is precisely half the original variance `v`” records the
`-v/2` term correctly. No block independence and no product of block
probabilities is used; the single `Z=W(Ψ)` Chebyshev term `vδ^{1/2}` is
retained.

---

## AUDIT dispositions
No AUDIT-comment markers remain in either the OLD or NEW module. I found no
audit-worthy issue introduced by the rewrite: no deterministically substituted
tilted mean, no scalar displacement-moment multiplication, no unauthorised mask
commutation, no dropped prefactor (`√δ`, `g_δ`, `δ^{(1-a)/2}`, `v/2`,
`δ^{-3/4}`), and no altered quantifier (`N≥1`, `τ∈[0,B)`, `B=B(e_rate)` before
`δ↓0`, then `e_rate↓0`).

## Findings and limits
All seven assigned proofs are argument-preserving; the NEW text adds only step
headings and locally checkable explanations, all of which are justified under
the same hypotheses. Two scope limitations are worth stating honestly.

1. The target proofs consume several unassigned upstream results
   (`P:constant-phase-driver`, `P:constant-young-linear`,
   `P:constant-compact-base`, `P:constant-gaussian-flow`,
   `P:compact-F-projection`/`E:compact-F-eigen`/`E:compact-normalized-complement`/
   `E:compact-positive-margins`, `P:source-gaussian-transfer`/
   `P:source-canonical-convergence`, `P:masked-source-moments`/
   `P:masked-canonical-transfer`, `L:constant-source-solution`,
   `L:exact-canonical-scaling`). I verified the conditions under which they are
   invoked, but did not re-prove their internal arguments (they are explicitly
   unassigned).
2. A few quantitative constants absorb the fixed horizon/block length `B`
   (e.g. `‖H_m-H_m^stat‖_{C^θ}≤C_Bδ` from a coefficient difference `≤CδB`).
   This is legitimate because `B` is fixed before the `δ↓0` limit and the
   constants may depend on `R,B,Ψ`; I flag it only to make the dependency
   explicit, not as a defect.

No lost step, lost qualifier, or rewritten-mathematics defect was identified in
the seven assigned proof pairs.
