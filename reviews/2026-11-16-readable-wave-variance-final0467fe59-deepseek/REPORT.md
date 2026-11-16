# Review Result
Category: proof-readability-equivalence
Model: deepseek-v4-pro
Verdict: PASS_WITH_NOTES
Confidence: high

All six assigned proof pairs were read completely in both the OLD (`cdde711…`) and NEW (`0467fe5…`) modules, and all six were independently reconstructed from the embedded equations. The NEW text is a step-splitting, roadmap-adding expansion of the OLD proofs; no deduction, quantifier, case, constant, or uniformity qualifier was dropped. The added explanations are justified under the same hypotheses. The notes below are either pre-existing imprecisions (not introduced by the rewrite) or a phase-level-vs-scalar reading caveat on one added gloss; none invalidates the mathematics.

## P:frequency-row

- Old reading: COMPLETE (statement LFs 48–55; proof LFs 57–140)
- New reading: COMPLETE (statement LFs 48–55; proof LFs 57–165)
- Public reconstruction: COMPLETE

**Original-step coverage.**
1. Degenerate case. If `C = 0`, the ball-growth condition on every closed ball plus a countable cover by finite closed balls forces `ν = 0`; `J_h ≡ 0`. Identical in both.
2. Near-ball Bessel mass. For `C > 0`, `ν_ξ` is the pushforward of `ν` by `λ ↦ η = ξ − λ`; hence `ν_ξ(B(0,R)) ≤ C R^α`. Define `A_ξ(q) = ∫_{|η|≤5q} ⟨η⟩⁻¹ ν_ξ(dη)`. With `N = ⌈log₂(5q)⌉`, split into the unit ball and annuli `2^j < |η| ≤ 2^{j+1}`. Each annulus contributes at most `C·2^{(j+1)α}·2^{−j}` (unit ball contributes `≤ C`), giving
   `A_ξ(q) ≤ C(1 + 2^α Σ_{j=0}^{N−1} 2^{j(α−1)})`.
3. Geometric sum, three cases, yielding `E:frequency-inverse-bessel` with constant depending only on `α`; for `α > 1` the `q^{α−1}` case uses `2^N < 10q` to absorb `10^{α−1}`.
4. Near region `|λ| ≤ 4q`. Here `|η| ≤ 5q`, so `Q_h(·,·) ≤ 2` (each bracket is `⟨·⟩^{a−1} ≤ 1` because `a−1 < 0`). Since `J_h(ξ) = ⟨ξ⟩^{−ε}∫ Q_h ⟨η⟩⁻¹ dν_ξ` with `ε = 1−2γ`, the near contribution is `≤ 2⟨ξ⟩^{−ε}A_ξ(q) ≤ 2q^{−ε}A_ξ(q)`.
5. Case absorption. `α < 1`: bounded. `α = 1`: `q^{−ε}(1+log q) = e^{−εu}(1+u) ≤ 1+1/(eε)`. `α > 1`: remaining exponent `α−1−ε = α+2γ−2 < 0` by `E:variance-gamma-range`. So near part is `O_C(1)`.
6. Far region `r = |λ| > 4q ≥ 4`. With `|ξ| ≤ q < r/4`, the reverse triangle inequality gives `|η| ≥ 3r/4`, `||η|−|ξ|| ≥ r/2`, `|η|+|ξ| ≥ r/2`.
7. Bracket reduction. Each bracket `⟨hX⟩^{a−1}` with `X ≥ hr/2` obeys `⟨hX⟩^{a−1} ≤ ⟨hr/2⟩^{a−1}`; the inequality `⟨hr/2⟩ ≥ ⟨hr⟩/2` (squared: `1+(hr/2)² ≥ (1+(hr)²)/4`) with negative exponent gives `⟨hr/2⟩^{a−1} ≤ 2^{1−a}⟨hr⟩^{a−1}`. Two brackets: `2^{2−a}⟨hr⟩^{a−1}`. With `⟨η⟩⁻¹ ≤ 4/(3r)` and `⟨ξ⟩^{−ε} ≤ 1`, the far part is
   `(4/3)·2^{2−a} ∫_{|λ|>4q}|λ|⁻¹⟨h|λ|⟩^{a−1} ν(dλ)`,
   which is then enlarged to `|λ| > 1`.
8. Dyadic split giving `CS(h)` with `S(h)=Σ_{j≥0} 2^{j(α−1)}⟨h2^j⟩^{a−1}`; the `2^{j(α−1)}` comes from mass `C2^{(j+1)α}` times inverse radius `2^{−j}`.
9. Tail/finite split at `L = ⌊log₂(1/h)⌋`. Tail ratio `2^{α+a−2} < 1` and `2^{L+1} > 1/h` give `tail ≤ h^{1−α}/(1−2^{α+a−2})`. The finite part is `1/(1−2^{α−1})` (`α<1`), `1+log₂(1/h)` (`α=1`), and `2^{α−1}h^{1−α}/(2^{α−1}−1)` (`α>1`); the last uses `2^{L+1} ≤ 2/h`. Combining gives `S(h) ≤ K_{α,a}B_α(h)`, using `B_α(h) ≥ 1` and `h^{1−α} ≤ 1` in the `α<1` tail.

**Argument preservation.** PRESERVED. All cases (near/far, `α<1`, `α=1`, `α>1`) and the exact constants survive.

**New explanations.** JUSTIFIED. The added sentences verify the geometry (`|ξ| ≤ q < r/4`), justify `2^{1−a}` per bracket and `2^{2−a}` total, and spell out the dyadic mass `C2^{(j+1)α}`. Each follows from the stated hypotheses.

**Evidence.** Exponent ranges: `ε = 1−2γ > 0` because `γ < 1/2`; `α+2γ−2 < 0` because `γ < (2−α)/2`; `α+a−2 < 0` by `H:homog`. Constants `2^α`, `4/3`, `2^{2−a}`, `2^{α−1}/(2^{α−1}−1)`, `1/(1−2^{α+a−2})` are all explicit and `d`-independent; radius independence enters through `ν_ξ(B(0,R)) ≤ CR^α` used at every shell radius.

**Lost steps/qualifiers.** None identified. Pre-existing wording “Each oscillatory bracket is at least ⟨hr⟩/2” is imprecise (the *bracket argument* is ≥ hr/2, so the bracket is ≤ the 2^{1−a}-scaled quantity); the NEW text resolves this with the explicit “raising the lower bound … coefficient 2^{1−a}” clarification.

## C:frequency-time

- Old reading: COMPLETE (statement LFs 147–158; proof LFs 160–171)
- New reading: COMPLETE (statement LFs 172–183; proof LFs 185–199)
- Public reconstruction: COMPLETE

**Original-step coverage.**
1. Endpoint check. `1 − a/2 > 1/2` since `a < 1`; `(3−a−α)/2 > 1/2` since `α+a < 2`.
2. `α < 1`: `2β < 2−a`, so `J_h ≤ KC` and `h^{2−a} ≤ h^{2β}` (since `h ≤ 1`).
3. `α > 1`: from `P:frequency-row`, `J_h ≤ KC h^{1−α}`; multiplying by `h^{2−a}` gives `h^{3−a−α}`; the condition `3−a−α > 2β` gives the bound.
4. `α = 1`: `δ = 2−a−2β > 0`; `u = log(1/h) ≥ 0`; then `h^{2−a}(1+log(1/h)) = h^{2β} h^δ(1+u) = h^{2β} e^{−δu}(1+u) ≤ h^{2β}(1+1/(eδ))`.
5. No endpoint value of `β` is used (strict upper bounds throughout), so the interval `(1/2, min(...))` is covered.

**Argument preservation.** PRESERVED.

**New explanations.** JUSTIFIED. The added derivation `e^{−δu}(1+u) = e^{−δu} + ue^{−δu} ≤ 1 + 1/(eδ)` uses `d/du(ue^{−δu}) = e^{−δu}(1−δu)`, extremum `1/(eδ)` at `u = 1/δ`; correct.

**Evidence.** `δ > 0` follows from `β < 1−a/2`; `3−a−α−2β > 0` from `β < (3−a−α)/2`; the constant `1+1/(eδ)` absorbs the critical logarithm uniformly in `d,ν,C,h,ξ`.

**Lost steps/qualifiers.** None identified.

## P:actual-wave-form

- Old reading: COMPLETE (statement LFs 219–254; proof LFs 256–349)
- New reading: COMPLETE (statement LFs 247–282; proof LFs 284–416)
- Public reconstruction: COMPLETE

**Original-step coverage.**
1. Admission of `ζ_R F_{z,w}` in the original noise completion. The wave multipliers are smooth in frequency at zero through the continuous sine quotient (`S(t,ξ)` entry `sin(t|ξ|)/|ξ|` is `t` at zero); Bessel multipliers preserve Schwartz. Hence `v_z, G_w` and their product are continuous in all Schwartz seminorms on `[0,T]`. For tests supported in a fixed compact `K`, only `y ∈ K−K` contributes, so the spatial pairing is `≤ |K|Γ(K−K)‖F(t)‖∞‖H(u)‖∞` (`Γ(K−K)` finite for compact sets, including singular covariances). With the temporal Schur bound `E:masked-time-schur` and smooth interior approximations of `1_I` preserving the `ζ_R` support, the product lies in the original `H_a`-type completion in every allowed dimension.
2. Agreement of auxiliary and spectral limits. Time-step frozen values plus smooth smoothing of finitely many indicators give a diagonal sequence `F_n → F` in `L²(I)` in every Schwartz seminorm. Because each `F_n(t)−F(t)` is spatial Schwartz with locally integrable seminorms and convergence on the compact interval is uniform in each seminorm, Fourier integration by parts yields `‖\widehat{F_n−F}(ξ)‖_{L²(0,T)} ≤ ε_n⟨ξ⟩^{−N}` for each fixed `N` with `ε_n→0`. Choose `N` with `⟨ξ⟩^{−2N} ∈ L¹(μ) ∩ L¹(ν_R)` (temperedness); `L:masked-time-completion` transfers this to the spectral `H_a`-norm limits; multiplication by fixed `ζ_R` preserves them, and the compact-support bound gives convergence in the original completion. Hence the two limits agree (constants may depend on `R`, and are not the uniform variance constants).
3. Real-to-complex comparison. For real tensor tests, `A(−ξ)=‾A(ξ)`; integration against even `μ` (and even `ν_R`) cancels the imaginary mixed term, so the same squared-norm comparison holds for `f̂ + iĝ`. This produces `E:variance-complex-noise`, explicitly a bound, not a claim of stationarity.
4. Physical adjoint. Using `S(−t)(0,f) = (−sin(t|D|)f/|D|, cos(t|D|)f)` and the Sobolev pairings, with `⟨·,·⟩_{H^{1/2}} = ⟨Λ·,·⟩_{L²}` and `⟨·,·⟩_{H^{−1/2}} = ⟨Λ^{−1}·,·⟩_{L²}`:
   `⟨S(−t)B(b)S(t)z,w⟩_E = ⟨−sin(t|D|)/|D|·bv_z, w₁⟩_{H^{1/2}} + ⟨cos(t|D|)bv_z, w₂⟩_{H^{−1/2}}`
   `= ∫ bv_z \overline{−sin(t|D|)/|D|Λw₁} + ∫ bv_z \overline{cos(t|D|)Λ^{−1}w₂} = ∫ b(t,x)v_z\overline{G_w} dx`.
   This proves `E:variance-physical-adjoint`.
5. Cutoff adjoint. For `H^{1/2}`: `⟨χw₁,u₁⟩_{H^{1/2}} = ⟨χw₁,Λu₁⟩_{L²} = ⟨w₁,χΛu₁⟩_{L²} = ⟨w₁,Λ^{−1}χΛu₁⟩_{H^{1/2}}`, and similarly `⟨χw₂,u₂⟩_{H^{−1/2}} = ⟨w₂,ΛχΛ^{−1}u₂⟩_{H^{−1/2}}`. Hence `D_χ^{*,E}w = (Λ^{−1}χΛw₁, ΛχΛ^{−1}w₂)`; this is not `(χw₁,χw₂)` in general, so `D_χ` is not self-adjoint on `E`.
6. Normalized kernel. `v̂_z(t,η) = ⟨η⟩^{−1/2}[c_ρU₁ + b_ρU₂]` and `Ĝ_w(t,ξ) = ⟨ξ⟩^{−1/2}[−b_rV₁ + c_rV₂]`. The product `v̂_z(η)·‾(Ĝ_w(η−ω))` yields `Σ_{i,j}K_{ij}U_j\‾{V_i}` with the displayed 2×2 matrix; at `ξ=η=0` it is `[[−t,−t²],[1,t]]`. With `ω = −λ`, `ξ = η+λ`, and the Fourier constant `c_d` of the convention `c_d = (2π)^{−d/2}`:
   `\widehat{F}_{z,w}(t,−λ) = c_d 1_I(t)∫ Σ_{i,j}K_{ij}(t;η+λ,η)U_j(η)\‾{V_i(η+λ)} dη`.
7. Covariance bound. Substitute into `E:variance-complex-noise`, reflect `λ` by evenness of `ν_R`, use `(2π)^d c_d² = 1`, and use absolute convergence/Schur to regard the spatial integral as a Bochner `H_a^ℂ` integral; this gives `E:variance-normalized-covariance` with no residual Fourier factor.

**Argument preservation.** PRESERVED. The admission, the exact adjoints, the kernel at zero, and the normalization are all intact.

**New explanations.** JUSTIFIED, with one reading caveat. The added Step 4 sentence “applying `D_χ` to an output moves its phase adjoint onto the test vector `w`” is a phase-level gloss: computing `G_{D_χ^{*,E}w} = −sin(t|D|)/|D|·χΛw₁ + cos(t|D|)·χΛ^{−1}w₂`, which is **not** pointwise `χG_w` because `sin(t|D|)/|D|` and `χ` do not commute. The text only asserts the phase-adjoint statement (which is exactly `E:variance-cutoff-adjoint`), and it separately and correctly stresses that `D_χ` is not self-adjoint; no scalar commutation is claimed.

**Evidence.** The adjoint computations are checkable in Fourier/unbounded-operator form as above. The kernel factorization is a direct expansion of two linear combinations. No infinite oscillatory Fubini is invoked: the spatial Fourier product uses a single absolutely convergent Schwartz integral, and the auxiliary covariance bound comes from `P:masked-auxiliary-norm` (triangle inequality + Tonelli on `ν_R`), not from interchanging two infinite oscillatory measures.

**Lost steps/qualifiers.** None identified. Pre-existing brevity of the partition-approximation admission is compensated by the NEW explicit “fine time partition, frozen Schwartz values, diagonal over countable seminorms, Fourier integration by parts” explanation; the admission constants may depend on `R`, a qualifier retained verbatim.

## L:phase-bessel

- Old reading: COMPLETE (statement LFs 359–368; proof LFs 370–379)
- New reading: COMPLETE (statement LFs 426–435; proof LFs 437–449)
- Public reconstruction: COMPLETE

**Original-step coverage.**
1. Decompose `g` over an orthonormal basis `{h_n}` of `H`: the target vector has coefficients `a_{k,n} = ∫Σ_j u_{k,j}(η)⟨g_j(η),h_n⟩_H dη`.
2. Writing the scalar coefficient as `∫u_{k,j}φ_{n,j} = ⟨φ_{n,j},\overline{u_{k,j}}⟩_{L²}` (for the conjugation convention `⟨f,g⟩ = ∫f\‾g`), the vector coefficient is `⟨φ_n,\overline{v_k}⟩_{L²(ℂ²)}` with `v_k = (u_{k,1}, u_{k,2})`; complex conjugation preserves orthonormality.
3. Scalar finite Bessel on `{\overline{v_k}}` gives `Σ_k |a_{k,n}|² ≤ Σ_j∫|φ_{n,j}|²`; summing over `n` and using Parseval for `H` gives `Σ_j∫‖g_j‖_H²`.
4. The conjugated integrand applies the same argument with the family `{v_k}` itself; Bochner integrability follows from `L²` Cauchy–Schwarz. Finite-dimensional `H` and the zero space are immediate; no independence is involved.

**Argument preservation.** PRESERVED.

**New explanations.** JUSTIFIED. The added first sentence correctly pinpoints why the nonconjugated integrand needs `{\overline{u_k}}`: the scalar inner product conjugates its second argument.

**Evidence.** `∫u_kφ = ⟨φ,\overline{u_k}⟩` and `|⟨φ,\overline{u_k}⟩| = |⟨\overline{u_k},φ⟩|`, so Bessel on the conjugate family controls exactly the displayed coefficients. Both directions inherit the same constant.

**Lost steps/qualifiers.** None identified.

## P:wave-two-variances

- Old reading: COMPLETE (statement LFs 382–397; proof LFs 399–473)
- New reading: COMPLETE (statement LFs 452–467; proof LFs 469–562)
- Public reconstruction: COMPLETE

**Original-step coverage.**
1. Temporal bound. Each entry of `K` is two continuous wave factors times `(⟨ξ⟩⟨η⟩)^{−1/2}`; `L:masked-continuous-wave` gives
   `‖1_I K_{ij}‖²_{H_a^ℂ} ≤ A_T h^{2−a}Φ_h(ξ,η)`, `A_T = C₁(a)(1+T)^4`.
2. Scalar row. Since `ν_R` is positive, even, Radon and satisfies `ν_R(B(y,r)) ≤ C_νr^α` uniformly in `R` (`E:variance-actual-growth-constant`), `P:frequency-row` applies, giving `E:variance-actual-row-bound`. The note that no nonnegative physical inverse covariance of `ν_R` is needed is retained.
3. Bessel hypotheses. `|c_r| ≤ 1` and `|b_r| ≤ √2·max(1,T)` (low-frequency FTC form `b_r = t⟨r⟩∫₀¹cos(vrt)dv`, high-frequency `|sin|·⟨r⟩/r ≤ √2`) make each `1_I K_{ij}` a bounded, frequency-continuous element of `H_a^ℂ` (Schur) with strong measurability by separability; multiplication by shifted Schwartz `U,V` components gives the required `L²` integrability.
4. Input direction. Set `V = Jz`, `U_k = Je_k`, `g_j^λ(η) = Σ_i 1_IK_{ij}(·;η+λ,η)\‾{V_i(η+λ)}`. Cauchy–Schwarz on the two output components (`|a+b|² ≤ 2(|a|²+|b|²)`) gives `Σ_j‖g_j^λ‖² ≤ 4A_Th^{2−a}Φ_h(η+λ,η)Σ_i|V_i(η+λ)|²`. Change `ξ = η+λ`, Tonelli, the row bound, and `‖z‖_{E_{s−γ}} = ‖⟨ξ⟩^{−γ}Jz‖₂` give `E:wave-input-variance` with `C_T = 4A_TKC_ν`.
5. Output direction. With `η = ξ−λ`, define `f_i^λ(ξ) = Σ_j1_IK_{ij}(·;ξ,ξ−λ)U_j(ξ−λ)`; the conjugated Bessel control gives `4A_Th^{2−a}∫Φ_h(ξ,ξ−λ)Σ_j|U_j(ξ−λ)|²dξ`. Changing variables gives the row `∫Φ_h(η+λ,η)ν_R(dλ)`; reflecting `λ` (evenness of `ν_R`) and using symmetry `Φ_h(ξ,η) = Φ_h(η,ξ)` turns it into `∫Φ_h(η,η−λ)ν_R(dλ)`, bounded by the row estimate at `ξ = η`. This proves `E:wave-output-variance` with the same `C_T`.
6. Time-power refinement. Applying `C:frequency-time` at both applications gives the `h^{2β}` replacements, including absorption of the `α = 1` logarithm; uniformity in `R,I` and family size is explicit; the `R`-dependent admission estimate is not used as the uniform bound.

**Argument preservation.** PRESERVED. Both directions and equal constant `C_T` are kept.

**New explanations.** JUSTIFIED. The added sentence “Under `ξ = η+λ`, the factor `Σ_i|V_i(ξ)|²` is independent of λ, leaving the row integral as its coefficient” is exactly the Tonelli structure used.

**Evidence.** Verify `A_Th^{2−a}Φ_h(η+λ,η)Σ_i|V_i(η+λ)|²` is integrable: `V = Jz` is Schwartz (polynomial Fourier weights preserve Schwartz), `Φ ≤ 2/(⟨η+λ⟩⟨η⟩)` since both brackets are ≤1, so the η-integral is finite. The constant `C_T = 4A_TKC_ν` is the product of the four-entry bound (4), the time constant, the row constant, and `C_ν`; the two directions use the same bound by the symmetry/evenness reduction.

**Lost steps/qualifiers.** None identified. The finite-vs-infinite distinction is preserved: `L:phase-bessel` handles finite orthonormal families here; the passage to infinite columns is deferred to `P:wave-square-columns` via `L²` limits. No independence of coefficients is asserted here.

## P:wave-square-columns

- Old reading: COMPLETE (statement LFs 479–493; proof LFs 495–539)
- New reading: COMPLETE (statement LFs 568–582; proof LFs 584–651)
- Public reconstruction: COMPLETE

**Original-step coverage.**
1. Basis and density. A countable real Schwartz orthonormal basis `{e_k}` of `E_s` is obtained by Gram–Schmidt from a countable dense Schwartz family; density in `E_s` and `E_{s−γ}` follows from smooth Fourier cutoffs plus real symmetrization `g(ξ) ↦ (g(ξ)+‾g(−ξ))/2` and the inverse maps. Gram–Schmidt preserves the Schwartz class.
2. Column construction. For real Schwartz `z`, `m_N(z) = Σ_{k≤N}ℓ_R(I;z,e_k)e_k` and `n_N(z) = Σ_{k≤N}ℓ_R(I;e_k,z)e_k` are finite centered Gaussian sums on the original `W`. Orthogonality gives the squared tail norms as the corresponding sums of expected squares, which are finite by `P:wave-two-variances`; hence both sequences converge in `L²(Ω;E_s)` with squared bounds `C_Th^{2−a}B_α(h)`, without requiring independence. Separability of `E_s` and finite-sum measurability give strong measurability of the limits, which extend uniquely as bounded real linear maps to `E_{s−γ}^{real}`.
3. Pairing identities. `w_N` being the `E_s` projection of Schwartz `w`, conjugate-linearity in the second slot gives `⟨m_N(z),w⟩_E = ℓ_R(I;z,w_N)`. The residual `w − w_N` is Schwartz (finite linear combination of Schwartz basis vectors); normalizing it in `E_s` (if nonzero) into a singleton orthonormal family and applying `E:wave-output-variance` gives
   `E|ℓ_R(I;z,w−w_N)|² ≤ C_Th^{2−a}B_α(h)‖z‖²_{E_{s−γ}}‖w−w_N‖²_{E_s} → 0`.
   This proves the first identity in `E:variance-square-columns`; projecting `z` instead and using `E:wave-input-variance` proves the second. A fixed basis plus Parseval give basis independence.
4. Gaussian laws. Continuous linear functionals of the limits (and finite linear combinations) are `L²` limits of centered Gaussian variables with convergent variances; characteristic functions converge to centered Gaussian characteristic functions. The same holds after the bounded extension to `E_{s−γ}`, giving joint Gaussianity of arbitrary fixed inputs and finite families of the two maps.

**Argument preservation.** PRESERVED.

**New explanations.** JUSTIFIED. The added explanation that `w − w_N` is Schwartz and how the singleton normalization is applied is correct: `w_N` is a finite Schwartz combination, and `P:wave-two-variances` is legitimately instantiated with the one-element orthonormal family `{(w−w_N)/‖w−w_N‖}`.

**Evidence.** `⟨m_N(z),φ⟩_E = Σ_k⟨e_k,φ⟩ℓ_R(I;z,e_k) = ℓ_R(I;z,Σ_k‾⟨e_k,φ⟩e_k)` by conjugate-linearity, which is a single Gaussian variable; convergence of characteristic functions therefore identifies the limit laws without invoking a Wiener–Itô chaos decomposition. Gaussianity is used only for law identification; no first-chaos (`p=1` homogeneous chaos) identity is claimed.

**Lost steps/qualifiers.** None identified. The zero-covariance branch (`Γ = 0` ⇒ all forms and columns vanish, bounds direct) is retained before `P:actual-wave-form`.

## AUDIT dispositions
No `AUDIT` comments remain in the module, and I find no AUDIT-worthy issue requiring a marker. The two observations below (the imprecise old bracket phrasing and the phase-level gloss in `P:actual-wave-form`) are readable-argument notes, not audit findings.

## Findings and limits
Scope: this is an internal proof-readability/argument-preservation comparison of the six assigned proofs only. I did not certify primary-source theorem fidelity, re-prove the upstream results in `notes_stratonovich_ham_second_moment.tex` or `notes/integrated_covariance_foundation.tex`, inspect rendered pages/images, or verify Lean quotation correspondence. Upstream inputs (`H:homog`, `L:masked-time-completion`, `P:masked-noise-completion`, `P:masked-auxiliary-norm`, `L:masked-continuous-wave`, etc.) were used under their stated hypotheses and their consumer uses were checked.

Summary of checks: translated frequency-row estimate is preserved with all three `α` regimes, `ε = 1−2γ`, `α+2γ−2 < 0`, `α+a−2 < 0`, dyadic tail/finite sums, and `d`-independent constants; the time-power corollary retains `1/2 < β < min(1−a/2,(3−a−α)/2)` with no endpoint use. The displacement/velocity form keeps the full real–complex phase, the continuous zero-frequency sine quotient (`b_0 = t`; kernel `[[−t,−t²],[1,t]]` at `ξ=η=0`), the free matrix, both adjoints (`E:variance-physical-adjoint`, `E:variance-cutoff-adjoint`), and the normalized kernel with `(2π)^dc_d² = 1`. Both variance directions keep `C_T = 4A_TKC_ν`, equal constants, and the `h^{2β}` refinement. Column maps keep the same `W`, strong measurability, basis independence, and Gaussian law identification only.

Notes (pre-existing, not introduced by the rewrite): (i) in `P:frequency-row` the phrase “Each oscillatory bracket is at least ⟨hr⟩/2” is imprecise — the bracket’s argument is; the NEW added “raising the lower bound … coefficient 2^{1−a}” sentence makes the intended inequality explicit and correct. (ii) In `P:actual-wave-form`, the added “observed form” gloss should be read at phase-adjoint level; `G_{D_χ^{*,E}w}` is not pointwise `χG_w` because the sine and `Λ` multipliers do not commute with `χ`; the module correctly states that `D_χ` is not self-adjoint and asserts no scalar commutation. No required step, case, qualifier, constant, or limiting order was lost in the rewrite.
