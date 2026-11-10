# Review Result — deepseek

- category: paper-review-deepseek
- model: deepseek/deepseek-v4-pro
- verdict: PASS
- confidence: HIGH

## Critical findings

None. All ten target proofs (PROOF075–084) and their boundary tests were reconstructed and checked. No false identity, false adjoint, missed boundary term, incorrect sign, incorrect final coefficient, or invalid large-time/asymptotic claim was found within the bounded MAIN unit. The mandatory manual controls (n16 one-variance counterexample with row and transpose, noncommuting Hermitian word expansion, p2 equality, zero/empty/C=0 cases, negative Sobolev exponent, lattice-spacing dependence, and the translation noncompactness witness) all check out against hand calculations.

## Noncritical findings

1. **PROOF078 lattice-sum constant (presentational).** The bound
   `⟨y-ak⟩^{-N} ≤ max(1,2/a)^N ⟨k⟩^{-N}` for `|k|≥√d` is asserted without spelling out the two-regime argument. It is correct:
   - `a≤2`: `⟨y-ak⟩ ≥ (a/2)⟨k⟩` (because `1 ≥ a²/4`), giving constant `(2/a)^N`;
   - `a>2`: `⟨y-ak⟩² ≥ 1+a²|k|²/4 ≥ ⟨k⟩²`, giving constant `1`.
   Only a clarity expansion, not a correction.

2. **PROOF083 wording (“Fatou in probability”).** The actual rigorous step is Fatou’s lemma in expectation applied to the nonnegative real variables `‖X_n‖_{S_p}^p`, combined with the pointwise singular-value Fatou `‖X‖_{S_p}^p ≤ liminf_n ‖X_n‖_{S_p}^p`. No mathematical error, only loose wording.

3. **PROOF077 constant is an upper bound, not a sharpness claim.** `√(p-1)` is explicitly asserted as equality only at `p=2`; for `p>2` it is valid but not claimed optimal. The proof supports exactly this.

4. **PROOF079 small-`j` constant uses `‖K‖ ≤ M` implicitly.** This holds because `‖I_γ‖ = sup_k ⟨κ_k⟩^{-γ} ≤ 1` for `γ>0`; worth stating, but not a gap.

## Checked derivations

**CMP01 — PROOF075 `L:gaussian-scalar-powers` — CHECKED.**
Statement (source LF 14–28), proof (LF 30–48). Weighted AM–GM via `φ(t)=θt+1-θ-t^θ`, derivative `θ(1-t^{θ-1})`, minimum zero at `t=1`; continuity at `t=0`, `v=0` immediate. Integer-power endpoints `q=0,L` are exact identities under `a⁰=1`. Finite Hölder via normalization; zero-norm case handled. Concave expectation `E[Z^r] ≤ (EZ)^r` via Young at `θ=r`; `F=0` ⇒ `Z=0` a.s., `F>0` division handled. **Decision: PASS.**

**CMP02 — PROOF076 `L:gaussian-trace-bounds` — CHECKED.**
Statement (LF 50–63), proof (LF 65–95). Noncommuting word in the `Y`-eigenbasis yields exactly `Σ_{i,j}|b_{ij}|² λ_j^q λ_i^{L-q}` (real; sign of `λ_j^qλ_i^{L-q}` handled by absolute bound), AM–GM per term, index swap by `|b_{ij}|=|b_{ji}|`, weights `q/L + (L-q)/L = 1`, giving `Re Tr(BY^qBY^{L-q}) ≤ Tr(B²|Y|^L)`. Trace Hölder via `d_i = Σ_j|U_{ij}|²θ_j`, doubly stochastic convexity `Σd_i^m ≤ Tr D^m`, exponent `(2m-2)m/(m-1) = 2m`; zero-sum case covered. No operator-power monotonicity assumed. **Decision: PASS.**

**CMP03 — PROOF077 `P:finite-gaussian-matrix` — CHECKED.**
Statement (LF 97–117), proof (LF 119–179). Zero-boundary Gaussian IBP `E[g_kP(g)]=E[∂_kP(g)]`; differentiated `Y^{2m-1}` gives exactly `F = Σ_k Σ_{q=0}^{L} E Tr(B_kY^qB_kY^{L-q})`, `L=2m-2` (L+1=2m−1 ordered positions). Trace bounds give `F ≤ (2m-1)(TrD^m)^{1/m}F^{(m-1)/m}`; division valid when `F>0`; raise to `m` ⇒ `E Tr Y^{2m} ≤ (2m-1)^m Tr D^m`. `m=1` is exact equality. Rectangular dilation `B_k=[[0,A_k],[A_k^*,0]]`, `D=diag(V_out,V_in)`; `(XX^*)^m=X(X^*X)^{m-1}X^*` ⇒ `Tr Y^{2m}=2Tr((X^*X)^m)`; substitution gives the average bound with `√(p-1)`. `p=2` equality verified (`Tr V_in = Tr V_out`). The n16 Remark (LF 183–197): `E‖X‖_{S_4}⁴ = n(n+2) = 288`, input-only `9Tr I_n²=144` false, transposed row refutes output-only; average bound fourth power `9·136=1224`, maximum bound `9·256=2304` — all verified. **Decision: PASS.**

**CMP04 — PROOF078 `L:cutoff-factorization` — CHECKED.**
Statement (LF 208–230), proof (LF 232–307). Peetre `(⟨x⟩/⟨y⟩)^r ≤ 2^{|r|/2}⟨x-y⟩^{|r|}` verified for both signs (interchange `x,y` for `r<0`). Lattice sum tail constant `max(1,2/a)^N` verified (see noncritical 1). Mixed discrete/continuous Schur: test with `M₁M₂` via weighted Cauchy–Schwarz then Tonelli. Kernel normalizations verified exactly: `(P_ψu)_k = L^{-d/2}∫ψ̂(κ_k-ξ)û(ξ)dξ`, `(E_χv)^∧(ξ) = L^{-d/2}Σ_k v_k χ̂(ξ-κ_k)`; the unitary-`c_d` Fourier convention leaves `L^{-d/2}` with **no extra `c_d`** (inversion `c_d` cancels the `c_d^{-1}` inside `ψ̂`). Recovery `E_χI_γP_ψu=χu` on Schwartz, extended by density in `H^{σ+γ}`; no point sampling of rough Fourier L², no alias term. **Decision: PASS.**

**CMP05 — PROOF079 `P:cutoff-singular-values` — CHECKED.**
Statement (LF 309–319), proof (LF 321–366). Factorization `K=Λ^σE_χI_γP_ψΛ^{-σ-γ}` with the outer Bessel maps unitary; `I_γ` diagonal entries `⟨κ_k⟩^{-γ}`; `rank Q_n=(2n+1)^d`; tail `[1+(2π/L)²(n+1)²]^{-γ/2}→0`. For `j≥3^d`, `n=⌊j^{1/d}/4⌋` gives `rank K_n < j` and `‖K-K_n‖ ≤ M(2L/π)^γ j^{-γ/d}` (using `n+1>j^{1/d}/4` and `(1+(2π/L)²(n+1)²)^{-γ/2} ≤ ((2π/L)(n+1))^{-γ}`). Rank-`<j` approximation ⇒ `s_j(K) ≤ ‖K-F‖` via first-`j` singular-vector subspace; `j<3^d` covered by `s_j≤‖K‖≤M≤Cj^{-γ/d}` with `C = M max(3^γ,(2L/π)^γ)`. `Σ j^{-pγ/d}` converges iff `pγ>d`. Constant depends on `L,ψ,χ,σ,γ,d`; no support-uniform or endpoint claim. **Decision: PASS.**

**CMP06 — PROOF080 `P:compact-two-envelopes` — CHECKED.**
Statement (LF 392–408), proof (LF 410–437). `A_σ=Λ^σχΛ^{-σ}`; `A_σ^*=A_{-σ}` (self-adjoint real `Λ^σ`, real multiplication) extended from Schwartz by density. `P_χ=diag(A_{1/2},A_{-1/2})`, exactly `P_χ^*=diag(A_{-1/2},A_{1/2})=UP_χU` with the swap `U(v,w)=(w,v)`; swap commutes with `D_γ`, so `K_in=UK_outU`. Blocks are `K_{χ,1/2,γ}`, `K_{χ,-1/2,γ}`; direct-sum S_p power is the multiset union; unitary conjugation preserves it. `KK^*`/`K^*K` positive eigenvalue multiplicities agree via the `K/√λ` inverse isometry; zero eigenvalues contribute nothing to the trace. `P_χ` is **not** self-adjoint/projection (correctly stated). **Decision: PASS.**

**CMP07 — PROOF081 `L:compact-positive-order` — CHECKED.**
Statement (LF 443–451), proof (LF 453–471). `‖(1-Q_n)A^{1/2}‖²=‖(1-Q_n)A(1-Q_n)‖ ≤ ‖(1-Q_n)B(1-Q_n)‖→0` ⇒ `A^{1/2}` compact ⇒ `A` compact. Max-min formula in an eigenbasis with the upper-bound subspace-intersection argument; Rayleigh quotient comparison gives `λ_j(A)≤λ_j(B)`; sum of scalar powers of order `t≥1` gives the trace comparison. No false `A^t ≤ B^t` operator assertion is made. **Decision: PASS.**

**CMP08 — PROOF082 `P:localized-finite-variance` — CHECKED.**
Statement (LF 473–490), proof (LF 492–513). From `P_χZ_ℓ=Z_ℓ=Z_ℓP_χ` (hence `Z_ℓ^*=P_χ^*Z_ℓ^*=Z_ℓ^*P_χ^*`): the left localization gives the **distinct** congruence `V_out=P_χV_outP_χ^*`, the right gives `V_in=P_χ^*V_inP_χ`; positive congruence on both `CD_γ²` hypotheses gives `V_out≤CB_out`, `V_in≤CB_in`. PROOF080+PROOF081 give compactness and trace powers `≤ C^{p/2}‖K_out‖_{S_p}^p`. `C=0` forces all `Z_ℓ=0`. For each `ℓ`, `Z_ℓZ_ℓ^*≤V_out`, finite spectral projections pass to `‖(1-Q_n)Z_ℓ‖²=‖(1-Q_n)Z_ℓZ_ℓ^*(1-Q_n)‖→0` ⇒ `Z_ℓ` compact; singular-value comparison gives `‖Z_ℓ‖_{S_p}^p≤Tr V_out^{p/2}`. Localization is an explicit hypothesis, not derived. **Decision: PASS.**

**CMP09 — PROOF083 `C:finite-gaussian-operators` — CHECKED.**
Statement (LF 519–528), proof (LF 530–579). Compressed output/input variances and the positive residual differences `Π_nZ_ℓ(1-Π_n)Z_ℓ^*Π_n ≥ 0` and `Π_nZ_ℓ^*(1-Π_n)Z_ℓΠ_n ≥ 0`; compression max-min gives `λ_j(Π_nVΠ_n)≤λ_j(V)`, hence both compressed trace powers ≤ `C^{p/2}‖K_out‖_{S_p}^p`. PROOF077 on the finite range with the average of the two trace powers gives `E‖X_n‖_{S_p}^p ≤ (p-1)^{p/2}C^{p/2}‖K_out‖_{S_p}^p` — **exact average factor, no extra 2**. Compact-norm convergence `Π_nXΠ_n→X`; singular-value Lipschitz via `s_j(A)=inf_{dim L<j} sup_{v∈L^⊥,‖v‖=1}‖Av‖`; pointwise singular-value Fatou plus Fatou in expectation gives the bound and a.s. finiteness; measurability by continuity of singular values. Finite even `p` throughout; no `S_p`-Bochner convergence or infinite Gaussian series. **Decision: PASS.**

**CMP10 — PROOF084 `P:cutoff-boundary-tests` — CHECKED.**
Statement (LF 583–588), proof (LF 590–632). Actual placements verified: `P_χ(Λ^{1/2}v,0)=(Λ^{1/2}v,0)` and `P_χ^*(Λ^{-1/2}f,0)=(Λ^{-1/2}f,0)` for plateau-supported `v,f`; rank-one `Zx=⟨x,w̃⟩ṽ` satisfies both localizations; variances are `‖w̃‖²ṽ⊗ṽ^*` and `‖ṽ‖²w̃⊗w̃^*`. `|⟨x,a⟩|=|⟨D_γx,D_γ^{-1}a⟩|≤‖D_γx‖‖D_γ^{-1}a‖` with `D_γ^{-1}` applied only to Schwartz `a`; finite `C=max(‖w̃‖²‖D_γ^{-1}ṽ‖², ‖ṽ‖²‖D_γ^{-1}w̃‖²)`. Noncompactness of `Λ^{-γ}`: translates `T_hf ↦ T_hg`, Plancherel `⟨T_hg,g⟩=c_d^{-1}F(|ĝ|²)(h)→0`, large spacing gives `≥‖g‖` image separation, no Cauchy subsequence. **Decision: PASS.**

**CMP11 — Manual controls and downstream fit — PASS.**
Hand-verified: p2 equality; p4 recurrence (ordered product rule count `L+1=2m-1`); n16 row+transpose counterexample; noncommuting Hermitian word; negative Sobolev exponent for `r<0`/`σ=-1/2`; lattice-spacing-dependent constants; cutoff/noncompact translation witness; zero/empty/C=0 cases. The downstream driver (LF 2217–2294, 2374–2420) consumes these finite/localized bounds under fixed `R,T`, both variance hypotheses, and compact envelopes exactly as supplied; the driver’s own Cauchy/tail/path arguments are separate and were **not** fully certified by this MAIN unit (consistent with CMP11’s “inspect what it separately proves, without certifying all consumer proofs”).

**CMP12 — Completeness/noncircularity/scope — PASS.**
All ten proofs reconstructed with explicit hypotheses. Implicit inputs are Bessel self-adjointness, compact-operator spectral theory (max-min, singular-value variational formula), the Schur test, Peetre inequality, and standard AM–GM/Hölder/Jensen — all invoked identifiably. No covert infinite Gaussian series, Young path, time path, source construction, or moment assertion appears in PROOF075–084; PROOF083 is explicitly finite even `p`; the section text (LF 636–643) explicitly defers actual coefficient localization, compact variance tails, the infinite Gaussian series and time regularity to later sections. No radius-uniform estimate is imported.

## Required fixes before production gate

None blocking. Optional clarity additions only:
- Spell out the two-regime proof of the lattice-sum constant `max(1,2/a)^N` in PROOF078.
- Replace “Fatou in probability” with “Fatou in expectation” in PROOF083.
- State explicitly in PROOF079 that `‖I_γ‖ ≤ 1` justifies `‖K‖ ≤ M` for the small-`j` constant.

## One-line summary

All ten finite-Gaussian and compact-Schatten foundation proofs (PROOF075–084) and their boundary tests are logically sound, with correct signs, constants, adjoints, both variance directions, and fixed-parameter asymptotic behavior; PASS at HIGH confidence.