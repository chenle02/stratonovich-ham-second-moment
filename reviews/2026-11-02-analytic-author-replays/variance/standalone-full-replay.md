# Actual two variances and the same-noise interval operator limit

Author-only analytic replay of PROOF088 (`L:driver-actual-variances`) and PROOF091 (`L:driver-interval-limit`), with their actual use of PROOF069/071/073/074 expanded below. The last part connects these results to PROOF092/093 through the existing support/dyadic supplement; it does not redo that entire supplement. No prior verdict is a mathematical premise. No native reviewer, new source, Article edit, ref mutation, Lean or cluster job is used. This is worked author evidence for root inspection, not independent acceptance or a grade change.

The two subaims are established below under the original hypotheses and the explicitly instantiated earlier local results. I found no additional mathematical gap in this bounded chain. The imported lemmas and remaining scope are listed precisely, so this conclusion does not silently certify other modules or the full paper.

## 1. Hypotheses, objects and falsification controls

Keep d∈{1,2,3}, 0<a<1, the original homogeneous nonnegative even positive-definite tempered spatial covariance Γ of exponent α, with 0<α<d or α=d=1 (spatial white noise), and α+a<2. Its spectral measure μ is allowed to be singular; no angular or Riesz density hypothesis is used. Covariance amplitude is unchanged. Treat Γ=0 directly at the end. Fix R,T>0 and a fixed real even nonnegative compact smooth profile ζ, equal to one on B1 and zero outside B2. The physical multiplier is ζ_R(x)=ζ(x/R), applied to the completed raw test, not inserted into the covariance convolution defining a coefficient.

Use Λ=(1−Δ)^(1/2), s=1/2, E_r=H^r×H^(r−1), E=E_s, and the original real isonormal W on its prescribed covariance-null completion H_W. Write E_- = E_(s−γ), where

    0<γ<min(1/2,(2−α)/2).

The physical and Fourier unitaries are respectively

    J0(u,v)=(Λ^(1/2)u, Λ^(−1/2)v),       J=(Fourier⊕Fourier)J0.

Thus, if U=Jz,

    ||z||_(E_-)² = ∫ <ξ>^(−2γ) (|U1(ξ)|²+|U2(ξ)|²) dξ.       (1.1)

All fixed intervals below initially have I⊂[0,T], h=|I|∈(0,1]. The empty interval is defined separately as zero. Set

    Bα(h)=1                         (α<1),
          1+log(1/h)                (α=1),
          h^(1−α)                   (α>1).

Before proving the construction, the following controls rule out the relevant shortcuts.

1. Both variance directions are indispensable. For n=16, A_j=e_j^T (one-by-n rows), the Gaussian sum has fourth Schatten moment E(Σg_j²)²=n(n+2)=288. Keeping only the input variance in the dimension-free Gaussian maximum bound would give 3² Tr(I_n²)=144, false. Transposition rules out an output-only argument. This finite control is not a substitute for the actual wave estimates below.
2. Strong convergence alone does not imply vanishing trace or norm: on ℓ², T_N=e_N⊗e_N converges strongly to zero, but ||T_N||=Tr(T_N^m)=1. A common compact summable envelope is essential. Likewise a uniform moment bound for the compact random operators g(e_N⊗e_N) does not make them operator-norm Cauchy.
3. The balanced cutoff is not assumed self-adjoint or a projection. Its two phase blocks are Λ^(1/2)χΛ^(−1/2) and Λ^(−1/2)χΛ^(1/2); their adjoints interchange. Replacing Pχ* by Pχ would discard precisely the distinction needed for the two variance envelopes.
4. One admissible critical-log tuple is d=1, α=1, a=1/2, γ=1/4, θ=9/16, η=5/8, β=11/16, q0=32: q0γ=8>d and β−η−1/q0=1/32>0. The same α,a,γ,θ,η,β,q0 are admissible for the singular d=2 covariance Γ(dx1,dx2)=dx1 δ0(dx2). For a higher-exponent tuple take d=3, α=3/2, a=1/4, γ=1/8, θ=9/16, η=37/64, β=19/32, q0=128: q0γ=16>3 and β−η−1/q0=1/128>0. Neither control restricts the proof to these covariances or endpoints.

## 2. Earlier local inputs, with their actual hypotheses

These are mathematical lemmas already proved in the supplied current source, not new assumptions added to the model.

- PROOF069, `P:frequency-row`: for a positive Radon ν satisfying ν(B(y,r))≤C r^α for all y,r, with the strict γ range above and α+a<2, the frequency row (2.3) is bounded by K(α,a,γ) C Bα(h). Evenness and a density are not hypotheses of this scalar lemma. The strict γ conditions control its near-frequency power q^(α+2γ−2) and its factor q^(−1+2γ); α+a<2 controls the far-frequency geometric series. The constants are independent of dimension, ν, C, h and the row frequency.
- The actual-mask auxiliary construction gives a positive even Radon ν_R with ν_R(B(y,r))≤Cν r^α uniformly in R, where

      Lζ=||ζhat||_1,  Cν=c_d² Lζ² CΓ,  c_d=(2π)^(−d/2).

  Here CΓ is the translated spectral-growth constant of the actual covariance. Although the mask construction produces an auxiliary density, the argument below uses only its measure, evenness and growth; μ itself need not have a density. ν_R is a norm-comparison measure, not a declaration that the masked physical field is stationary or has a positive physical inverse covariance.
- PROOF071, `P:actual-wave-form`: the masked wave products are admitted in the original positive-time noise completion, and the actual covariance obeys (2.2) below. This admission uses common compact spatial support and temporal Schur approximation, and may have R-dependent admission constants. It does not supply the uniform-in-R quantitative variance constant by that route. The exact physical adjoint identity and the original W are retained.
- `L:masked-continuous-wave`: each of the four continuous wave-factor products has temporal H_a norm squared bounded by A_T h^(2−a) Q_h, with A_T=C1(a)(1+T)^4. Its hypotheses are t∈[0,T], h≤1, r,ρ≥0 and 0<a<1, including zero frequencies.
- PROOF085/086: a complete real compact-smooth-representative ONB {f_j} of the given H_W exists, g_j=W(f_j) are independent standard real Gaussians, and the literal covariance coefficients H_(j,R) give E[g_j ℓ_R(I;z,w)]=<A_j(I)z,w>_E. The coefficient operators are the actual statewise integrals, not a source-mollified replacement.
- PROOF087: A_j(I) has gain E_r→E_(r+1) at every real r, and its E-adjoint has the dual gain. For χ∈C_c∞ real equal to one on B_(2R+T+1), Dχ A_j=A_j=A_j Dχ. This follows from the full two-entry finite-propagation/support argument expanded in the existing supplement, not from scalar displacement positivity. Its individual j-dependent gain constants will never be summed below. In dimension three the actual free wave is used through its Fourier phase and distributional support theorem; no sphere measure is replaced by an ordinary spatial density.
- `P:cutoff-singular-values`: Λ^σ χ Λ^(−σ−γ) is compact, with singular values at most C_(χ,σ,γ,d) j^(−γ/d). It applies here only with σ=±1/2, γ>0, χ real compact smooth, hence belongs to S_q when qγ>d. The auxiliary torus is a cutoff factorization only; the states remain on R^d.
- `P:finite-gaussian-matrix`: independent real standard Gaussian coefficients and finite complex matrices obey the retained average in (6.1). Constants are independent of every matrix dimension and the number of coefficients. Its finite Gaussian integration-by-parts proof is not reproved here. The compact-operator extension needed here is derived by actual compressions in section6.

Only these stated hypotheses are consumed. PROOF073/074 are reconstructed in sections2–3 rather than treated as unexplained variance premises.

## 3. Actual normalized Fourier row and both Hilbert-Bessel bounds

The free wave has both entries

    S(t,ξ) = [[cos(t|ξ|),       sin(t|ξ|)/|ξ|],
              [−|ξ|sin(t|ξ|),  cos(t|ξ|)]],

with the sine quotient equal to t at zero. For fixed Schwartz z,w put

    v_z=[S(t)z]_1,
    G_w=−sin(t|D|)/|D| Λw1 + cos(t|D|) Λ^(−1)w2,
    ℓ_R(I;z,w)=W_C(ζ_R 1_I v_z overline(G_w)).

This is the actual raw form, linear in z and conjugate linear in w. For real phases it is real. The deterministic identity

    <S(−t)B(b(t))S(t)z,w>_E = ∫ b(t,x)v_z(t,x) overline(G_w(t,x)) dx

fixes its two-entry adjoint convention. In particular no observation cutoff is silently inserted in ℓ_R.

Let c_r(t)=cos(rt), b_r(t)=<r>sin(rt)/r for r>0 and b_0(t)=t. If U=Jz, V=Jw, ξ=η+λ, the two Fourier factors are

    vhat_z(t,η)=<η>^(−1/2)[c_|η| U1(η)+b_|η| U2(η)],
    Ghat_w(t,ξ)=<ξ>^(−1/2)[−b_|ξ| V1(ξ)+c_|ξ| V2(ξ)].

Consequently the 2-by-2 time kernel, with output index i and input index j, is

    K(t;ξ,η)= [−b_|ξ| c_|η|   −b_|ξ| b_|η|
                 c_|ξ| c_|η|    c_|ξ| b_|η| ] /sqrt(<ξ><η>).       (2.1)

At ξ=η=0 its matrix is [−t,−t²;1,t]. Dropping the velocity entry or replacing the zero-frequency sine factor by zero would change the actual form.

Unitary Fourier multiplication yields Fhat(t,−λ)=c_d ∫Σ_ij 1_I K_ij(t;η+λ,η) U_j(η) overline(V_i(η+λ))dη. The actual masked-noise covariance has factor (2π)^d; thus (2π)^d c_d²=1 cancels it. Evenness permits λ reflection. The precise consequence of PROOF071 is

    E|ℓ_R(I;z,w)|²
      ≤ ∫ν_R(dλ) || ∫Σ_ij 1_I K_ij(·;η+λ,η)
                        U_j(η) overline(V_i(η+λ))dη ||_(H_a,C)².   (2.2)

No infinite oscillatory measure interchange or stationary masked-noise law is required in this formula.

Define

    Q_h(r,ρ)=<h(r−ρ)>^(a−1)+<h(r+ρ)>^(a−1),
    Φ_h(ξ,η)=Q_h(|ξ|,|η|)/(<ξ><η>).

The continuous-factor lemma gives, for each i,j,

    ||1_I K_ij(·;ξ,η)||_(H_a,C)² ≤ A_T h^(2−a) Φ_h(ξ,η).         (2.3)

All four products are covered; neither trigonometric orthogonality nor independent time modes is asserted. Since Q_h≤2, for fixed λ the kernels below multiplied by a shifted Schwartz component are L² in the spatial variable with values in H_a,C. Their strong measurability follows from the continuous time factors into L²[0,T], the bounded temporal-completion inclusion, and separability. Thus the Hilbert-valued Bessel applications are well-defined before integrating λ. Tonelli will apply to their nonnegative squares.

The actual row bound, with every hypothesis checked above, is

    ∫ Φ_h(ξ,ξ−λ)ν_R(dλ)
       ≤ K(α,a,γ) Cν Bα(h) <ξ>^(−2γ).                          (2.4)

The strict conditions 1−2γ>0, α+2γ−2<0 when α>1, and α+a−2<0 are exactly those needed by PROOF069. Near α=1 the factor q^(−1+2γ)(1+log q) is bounded; the time-critical logarithm is retained in Bα(h).

**Vary the input family; fix the output.** Let {e_k} be any finite E-orthonormal complex Schwartz family, U_k=Je_k and V=Jz fixed. For each λ define an H_a,C-valued two-component kernel

    g_j^λ(η)=Σ_i 1_I K_ij(·;η+λ,η) overline(V_i(η+λ)).

Hilbert-valued Bessel gives Σ_k ||∫Σ_j U_(k,j) g_j^λ||²≤∫Σ_j||g_j^λ||². To see the conjugation convention, expand g in an ONB of H_a,C; scalar Bessel applies to the orthonormal family {overline(U_k)}. Cauchy–Schwarz over the two i-components, followed by summing the two j-components, gives exactly

    Σ_j ||g_j^λ(η)||²
      ≤2 Σ_ij |V_i(η+λ)|² ||1_I K_ij||²
      ≤4 A_T h^(2−a) Φ_h(η+λ,η) |V(η+λ)|².                   (2.5)

Use (2.2), change only the Lebesgue variable ξ=η+λ for each fixed λ, then Tonelli and (2.4). The result is

    Σ_k E|ℓ_R(I;e_k,z)|² ≤ b_I ||z||_(E_-)²,
    b_I=4 A_T K(α,a,γ) Cν h^(2−a) Bα(h).                       (2.6)

The factor4 comes from two finite component sums, not from a dimension or the family size.

**Vary the output family; fix the input.** Now U=Jz is fixed and V_k=Je_k. After ξ=η+λ in the Lebesgue integral define

    f_i^λ(ξ)=Σ_j 1_I K_ij(·;ξ,ξ−λ) U_j(ξ−λ).

Apply the conjugated Hilbert-valued Bessel inequality to the family V_k. The same two-component Cauchy–Schwarz calculation bounds the sum by

    4 A_T h^(2−a) ∫Φ_h(ξ,ξ−λ)|U(ξ−λ)|²dξ.

After η=ξ−λ, the row left to estimate is ∫Φ_h(η+λ,η)ν_R(dλ). It is not (2.4) until using both actual evenness and kernel symmetry:

    ∫Φ_h(η+λ,η)ν_R(dλ)
      =∫Φ_h(η−λ,η)ν_R(dλ)
      =∫Φ_h(η,η−λ)ν_R(dλ).                                   (2.7)

It therefore has the bound (2.4) at η. Thus

    Σ_k E|ℓ_R(I;z,e_k)|² ≤ b_I ||z||_(E_-)².                    (2.8)

This proves the two actual random Fourier-row variance bounds, including the step that would fail without evenness for the second direction.

C_T=4A_T K Cν is independent of R, the interval location/length (apart from h), either orthonormal family and its size, the future noise truncation N, and Gaussian moment index q. It depends on the fixed original covariance/amplitude, dimension through Cν, fixed mask profile, a,α,γ,T. The R-dependent raw admission constants of PROOF071 did not enter (2.6) or (2.8).

For strict 1/2<β<min(1−a/2,(3−a−α)/2), these estimates also hold with b_I replaced by C_(T,β)h^(2β). For α<1 this uses 2−a−2β>0; for α>1 it uses 3−a−α−2β>0. At α=1, δ=2−a−2β>0 gives

    h^δ(1+log(1/h)) ≤1+1/(eδ),       0<h≤1.                    (2.9)

No β endpoint or uniformity as the strict gaps close is claimed.

## 4. Actual mean-square columns, projections and both operator inequalities

Choose a real Schwartz ONB {e_k} of E. On fixed real Schwartz inputs define

    m_L(z)=Σ_(k≤L) ℓ_R(I;z,e_k)e_k,
    n_L(w)=Σ_(k≤L) ℓ_R(I;e_k,w)e_k.

Equations (2.8) and (2.6) show that the respective sums of expected coefficient squares converge. Orthogonality in the phase E, not independence of the raw coefficients, gives

    E||m_L(z)−m_K(z)||²=Σ_(K<k≤L) E|ℓ_R(I;z,e_k)|² →0,

and the analogous identity for n. Hence m(z),n(w) exist in L²(Ω;E), both with norm at most sqrt(b_I) times the E_- input norm. They are strongly measurable as limits of finite sums in separable E, and bounded linear extension defines deterministic maps E_-→L²(Ω;E). Their scalar coordinates belong to the closed original first chaos W(H_W), since each raw form is an actual completed linear noise test and closed-chaos L² limits stay in that subspace.

The singleton versions of (2.8)/(2.6) give two different scalar Cauchy bounds:

    E|ℓ_R(I;z,w)|² ≤ b_I ||z||_(E_-)² ||w||_E²,
    E|ℓ_R(I;z,w)|² ≤ b_I ||z||_E² ||w||_(E_-)².                 (3.1)

For the first bound, if w≠0 take the singleton orthonormal family {w/||w||_E} in (2.8); for the second normalize z in (2.6). A zero vector gives the zero identity. Let Π_L be the E projection onto e_1,…,e_L. For Schwartz w, <m_L(z),w>=ℓ_R(I;z,Π_Lw); its difference from ℓ_R(I;z,w) has L² norm at most sqrt(b_I)||z||_(E_-)||w−Π_Lw||_E→0. Since the finite projections remain Schwartz, this application is within the admitted raw-test class. Similarly <z,n_L(w)>=ℓ_R(I;Π_Lz,w), and the second bound in (3.1) makes its error tend to zero. These identify the row of m and the adjoint row of n. They do not assert the stronger, unjustified product of two E_- norms. This reconstructs the relevant content of PROOF074 and explains exactly which side is weakened in each direction.

Let g_j=W(f_j) be the complete real noise basis and let A_j=A_j(I) be the deterministic actual covariance coefficients. For fixed real Schwartz z,w their literal coefficient relation is

    E[g_j ℓ_R(I;z,w)]=<A_j z,w>_E.                               (3.2)

Put X_N(I)=Σ_(j≤N)g_j A_j. Then <X_N z,w> is precisely the orthogonal L² projection of the raw row onto span{g_1,…,g_N}. In particular

    E|<X_N z,w>|² =Σ_(j≤N)|<A_j z,w>|² ≤E|ℓ_R(I;z,w)|².         (3.3)

This is an orthogonal noise-test-basis projection, not a source regularization. It uses the same W and the exact coefficient mask after convolution.

There are now two operator quadratic inequalities, not merely scalar row bounds. For fixed Schwartz w, phase Parseval and independence of the finite real g_j give

    Σ_(j≤N)||A_j* w||_E²
      =E||X_N* w||_E²
      =Σ_k E|<X_N e_k,w>|²
      ≤Σ_k E|ℓ_R(I;e_k,w)|²
      ≤b_I ||w||_(E_-)².                                       (3.4)

Apply the finite-family bound (2.6) up to k=L, then let L→∞ by nonnegative monotone convergence; this legitimizes the infinite phase sum. Interchanging the roles gives

    Σ_(j≤N)||A_j z||_E²
      =E||X_N z||_E²
      =Σ_k E|<X_N z,e_k>|²
      ≤b_I ||z||_(E_-)².                                       (3.5)

For (3.5) it is (2.8), not (2.6), that supplies the final estimate.

Each A_j and its E-adjoint extends E_-→E by the gain-one input. Explicitly A_j:E_(s−γ)→E_(s+1−γ)↪E; for A_j* use the dual gain at r=γ−s, giving E_(s−γ)→E_(s+1−γ)↪E. Here γ<1, and all j-dependent constants are finite at fixed j,R,T. For each fixed finite N, approximate an E_- input by Schwartz inputs. Both sides of (3.4)/(3.5) converge, so the inequalities extend with the same b_I **uniformly in N**. No sum of those individual j-dependent gain bounds is taken.

Transport to H0=L²(R^d;R²): a_j=J0 A_j J0^(-1), Dγ=diag(Λ^(−γ),Λ^(−γ)). Restrict the extended inequalities to E and use (1.1). For every x∈H0,

    <(Σ_(j≤N)a_j a_j*)x,x>=Σ_(j≤N)||a_j*x||² ≤b_I||Dγx||²,
    <(Σ_(j≤N)a_j* a_j)x,x>=Σ_(j≤N)||a_j x||² ≤b_I||Dγx||².       (3.6)

Thus the actual V_out,N and V_in,N are both at most b_I Dγ² in positive operator order. In particular they are bounded by b_I I, but this weaker unlocalized bound alone does not imply compactness or Gaussian operator convergence.

For completeness, the full noise-basis expansions are actual given-noise expansions. Each scalar coordinate <m(z),e_k> is in W(H_W) and has coefficients <A_jz,e_k>. Parseval in that closed first chaos, phase Parseval and positive Tonelli give

    Σ_j||A_jz||² =Σ_kΣ_j |E[g_j<m(z),e_k>]|²
                 =Σ_k E|<m(z),e_k>|² =E||m(z)||².

Consequently

    m(z)=Σ_j g_j A_jz,     n(z)=Σ_j g_j A_j*z  in L²(Ω;E).       (3.7)

For a fixed E_- input z, approximate by Schwartz z_l. The uniform-N inequalities applied to z−z_l bound every finite partial sum difference by sqrt(b_I)||z−z_l||_(E_-); the m/n limits have the same continuity. First approximate the input, then use (3.7) for z_l. This extends (3.7) to every fixed E_- input. It supplies no uncountable almost-sure operator version by itself.

## 5. Localized variance envelopes and vanishing tails

The two bounded maps

    C_in x=(a_jx)_j,       C_out x=(a_j*x)_j

from H0 to ℓ²(H0) exist by (3.6) and monotone sums, and have norm at most sqrt(b_I). Therefore V_in,∞=C_in* C_in and V_out,∞=C_out* C_out are bounded positive operators. If Q_N retains the first N sequence coordinates, V_in,N=C_in*Q_N C_in and similarly for out. Since Q_N→I strongly, both finite variances converge strongly to their displayed limits. Their positive tails

    T_in,N=V_in,∞−V_in,N,        T_out,N=V_out,∞−V_out,N

converge strongly to zero and remain at most b_I Dγ². Equivalently the quadratic tails tend to zero and positivity gives ||T_Nx||²≤||T_N||<T_Nx,x>→0. These are fixed-interval statements; no rate uniform in interval or choice of noise basis is inferred.

By the actual coefficient support/localization, with P=Pχ=J0DχJ0^(-1),

    P a_j=a_j=a_j P.

It follows exactly, without P being self-adjoint or idempotent, that

    V_out,N=P V_out,N P*,        V_in,N=P* V_in,N P.             (4.1)

Bounded multiplication by P/P* passes these identities through strong limits, hence they hold for V_∞ and T_N. Congruence of the weighted bounds in (3.6) now gives

    V_out,N,V_out,∞,T_out,N ≤ b_I B_out,
    V_in,N, V_in,∞, T_in,N  ≤ b_I B_in,

    B_out=P Dγ² P*=(P Dγ)(P Dγ)*,
    B_in =P*Dγ² P =(P*Dγ)(P*Dγ)*.                               (4.2)

This is the real use of the support cutoff. The uncut Dγ on whole space is not compact, so it cannot replace these envelopes.

The balanced cutoff blocks and their adjoints are

    P=diag(Λ^(1/2)χΛ^(−1/2), Λ^(−1/2)χΛ^(1/2)),
    P*=U P U,                  U(x1,x2)=(x2,x1).

U commutes with Dγ. Hence, with Kχ=P Dγ and K_in=P*Dγ,

    K_in=U Kχ U,
    ||K_in||_(S_q)=||Kχ||_(S_q),
    Tr(B_out^(q/2))=Tr(B_in^(q/2))=||Kχ||_(S_q)^q.               (4.3)

Here the two blocks of Kχ are exactly Λ^σχΛ^(−σ−γ) with σ=±1/2. The imported cutoff singular-value lemma has all its hypotheses satisfied; it gives Kχ,K_in compact and in S_q for qγ>d. In particular B_out,B_in∈S_(q/2) for any admissible even q≥2. The equal traces are a unitary-swap/singular-value fact, not an assumed equality of V_out and V_in. Their constants depend on χ and therefore on fixed R,T. No uniform-R cutoff norm is available or claimed.

Each a_j is compact: a_j a_j*≤V_out,N≤b_I B_out for N≥j. Positive compact order gives compactness of a_j a_j*. If Q_l is a finite spectral projection of that compact positive operator, then

    ||(1−Q_l)a_j||²=||(1−Q_l)a_j a_j*(1−Q_l)||→0.

The finite-rank Q_l a_j approximate a_j. Its singular values squared are the positive eigenvalues of a_j a_j*, so the same max-min comparison yields a_j∈S_q whenever qγ>d. Thus every finite X_N is an actual compact-operator sum before any infinite limit is taken.

The tail trace convergence needs a separate argument. Let 0≤T_N≤B where B=b_I B_out or b_I B_in is compact positive in S_m, m=q/2≥1. Choose a finite spectral projection Q of B with ||Q⊥B Q⊥||<ε. For every unit x,

    <T_Nx,x> =||T_N^(1/2)(Qx+Q⊥x)||²
      ≤2<T_NQx,Qx>+2<T_NQ⊥x,Q⊥x>
      ≤2||Q T_N Q||+2ε.

Strong (even weak) convergence T_N→0 makes the finite matrix Q T_N Q converge in norm to zero. Hence limsup_N||T_N||≤2ε; let ε↓0. Positive compact order, instantiated with T_N≤B, gives λ_l(T_N)≤λ_l(B), while norm convergence makes each λ_l(T_N)→0. Since Σ_l λ_l(B)^m<∞, dominated summation proves

    Tr(T_out,N^m)→0,       Tr(T_in,N^m)→0.                       (4.4)

No claim T_N^m≤B^m for noncommuting positive operators is made. The exponent m is fixed in this convergence argument. A common compact summable envelope, not mere strong convergence or a uniform moment bound, supplies (4.4).

## 6. Retained Gaussian average and genuine interval operator convergence

Fix one even q=2m≥2 with qγ>d. For finitely many compact operators Z_j with both variances in S_m, the finite matrix result says, after compression to a finite-dimensional range,

    E||Σ_j g_j Z_j||_(S_q)^q
      ≤(q−1)^(q/2) [Tr(V_out^m)+Tr(V_in^m)]/2.                  (6.1)

Here is the exact compact-operator passage, so no infinite series is hidden in this application. Let Π_l be finite-rank orthogonal projections tending strongly to I and set Z_(j,l)=Π_l Z_j Π_l. Their output variance is at most Π_l V_out Π_l because the difference is

    Σ_j Π_l Z_j(1−Π_l)Z_j* Π_l ≥0.

The input statement is the same with adjoints interchanged. Positive eigenvalue max-min bounds both compressed variance trace powers by their uncompressed ones. Apply the finite matrix theorem to the same independent real g_j and these finite matrices. For each fixed Gaussian coefficient vector, compactness of the finite operator sum Z=Σg_jZ_j gives Π_l Z Π_l→Z in operator norm: first approximate Z by finite rank and then use strong convergence uniformly on the finite-dimensional ranges of it and its adjoint. Compact singular values are norm-Lipschitz; Fatou first in their nonnegative q-power sum and then in probability gives (6.1) for the compact operators themselves. Measurability follows from continuity of the finite coefficient map, continuity of each singular value, and a countable nonnegative sum. This proves exactly the retained average needed here, with no factor2 loss and no S_q-Bochner or infinite-series assumption.

Apply (6.1) first to Z_j=a_j, j≤N. By (4.2), compact positive max-min and (4.3),

    E||X_N(I)||_(S_q)^q
      ≤(q−1)^(q/2) b_I^(q/2) ||Kχ||_(S_q)^q,                  (6.2)

uniformly in N and in the chosen compact-smooth noise basis. J0 is unitary and does not alter singular values. The average of the two trace bounds is exactly one copy of the right side, not two.

For M>N the finite tail Y_(N,M)=Σ_(N<j≤M)g_j a_j has variances

    V_out,(N,M)=V_out,M−V_out,N ≤T_out,N,
    V_in,(N,M) =V_in,M −V_in,N  ≤T_in,N.

Consequently the same finite, compact theorem gives the new load-bearing Cauchy estimate

    sup_(M>N) E||Y_(N,M)||_(S_q)^q
      ≤(q−1)^(q/2) [Tr(T_out,N^(q/2))+Tr(T_in,N^(q/2))]/2
      →0.                                                       (6.3)

Every comparison of trace powers here is through eigenvalue order/max-min; it is not operator monotonicity of a power. Equation (6.3), not the uniform bound (6.2), proves that X_N(I) is L^q(Ω;B(E))-Cauchy, because operator norm is at most the Schatten q norm.

Let F_I be the operator-norm closed real span of the countably many deterministic A_j(I). It is a separable closed Banach subspace of B(E). Choose N_l increasing so that ||X_(N_(l+1))−X_(N_l)||_(L^q B(E))≤2^(−l). The sum of their L1 norms is finite, so Tonelli makes the sum of pointwise operator-norm differences finite almost surely. Their partial sums therefore converge in F_I on the original Ω. Give the limit value zero on the null exceptional set. It is strongly measurable, since it is a pointwise limit of measurable separably valued finite Gaussian sums. Fatou and the Cauchy property show convergence of the whole sequence in L^q. No new probability space, noise or distributional coupling has been introduced.

Different admissible even q give this same operator limit, by uniqueness of convergence in probability. For any requested finite p≥1 choose an admissible even q≥p (strict qγ>d); Lyapunov then gives L^p operator-norm convergence to that same X_R(I). One fixed q does not imply every p. No uniform-in-q tail rate is asserted or required.

An almost-sure operator-norm convergent subsequence makes X_R(I) compact valued, because the compact operators are norm closed. On that subsequence the singular values converge individually, and the double Fatou argument in (6.2) yields

    (E||X_R(I)||_(S_q)^q)^(1/q)
      ≤sqrt(q−1) sqrt(C_T) h^(1−a/2) Bα(h)^(1/2) ||Kχ||_(S_q).    (6.4)

This is a fixed-interval Schatten moment at admissible even q. It is not a C^θ S_q-valued path assertion, nor a statement at arbitrary Schatten indices or at qγ=d.

The limit is not merely Gaussian in distribution. For every continuous real linear functional ρ on F_I, ρ(X_N)=Σ_(j≤N)g_j ρ(A_j) lies in the original closed first chaos W(H_W). L² convergence of X_N gives L² convergence of these scalars; hence ρ(X_R(I)) is in that same first chaos. Its characteristic function is the limit of exp(−t²σ_N²/2), with σ_N² convergent, so it is centered Gaussian. Finite combinations of functionals have the same property. They are jointly Gaussian with any fixed finite collection of the given W(f)'s. Thus X_R(I) is a strongly measurable, compact-valued centered Gaussian operator on the given original noise space, with actual first-chaos scalar coordinates.

## 7. Literal covariance row, additivity and versions

For fixed Schwartz z,w, the finite scalar rows in (3.3) are complete noise-basis projections of the actual raw form. Thus they converge in L² to ℓ_R(I;z,w). On the other hand, L² operator-norm convergence in section6 gives

    <X_N(I)z,w>_E → <X_R(I)z,w>_E  in L².

Uniqueness proves the literal identity

    <X_R(I)z,w>_E =ℓ_R(I;z,w)  in L²(Ω).                         (7.1)

In particular the covariance with any fixed raw noise test is retained, not just the marginal variance or Gaussian law. For f∈H_W the covariance of (7.1) with W(f) is the covariance pairing of the actual completed masked wave test with f; at f=f_j this is exactly (3.2). The complexification is obtained from the four real pair identities and has the required sesquilinear convention. Real orthonormal bases complexify without doubling singular-value multiplicities, so every constant in (3.6)–(6.4) is unchanged.

For a fixed long interval I⊂[0,T], choose any finite partition into short intervals I_l of length≤1. The masked deterministic wave product depends on time continuously on a common spatial compact before its indicator is inserted. The common-support temporal Schur estimate admits its long test, and changing finitely many indicator endpoints has zero raw norm. Hence its actual completed raw test is the finite sum of those short tests, and ℓ_R(I;z,w)=Σ_lℓ_R(I_l;z,w) in L². The deterministic statewise coefficient integrals also add: A_j(I)=Σ_l A_j(I_l). Therefore finite X_N add exactly, and their finite-sum L^p operator limits give

    X_R(I)=Σ_l X_R(I_l)   almost surely for each fixed finite partition. (7.2)

This is independent of the chosen finite partition by common refinement. It uses no independent time blocks, and no short-h formula is extrapolated to h>1. Constants for long-interval bounds may depend on T through a finite unit partition.

At the fixed-interval stage, (7.1)/(7.2) are equalities for fixed rows, intervals and finite collections; uncountably many independently selected null sets are not intersected. To obtain a coherent countable version, choose all rational endpoint intervals (and the countable dyadic grids on [0,T]) and a fixed countable dense real Schwartz phase collection. Countable unions yield a common event for their finite additivity and row comparisons. PROOF092 then constructs a continuous C^θ path on the same space as recalled below, and its increments supply the simultaneous continuous operator version. The raw distributional identity remains an L² identity for each fixed Schwartz row/time; no uncountable pathwise evaluation of W on arbitrary tests is claimed.

Similarly, use a second compact-smooth noise basis. Its construction obeys the same covariance row (7.1) against the same actual W. A countable dense Schwartz pair collection makes the two bounded operators agree almost surely at each fixed interval; on rational times and continuous paths they become indistinguishable. This is basis independence on the given probability space, not equality in law on a new space.

## 8. Interface to PROOF092/093, without redoing the support/dyadic proof

The existing analytic supplement sectionA establishes the two-entry distributional support extension needed by PROOF087; sectionB displays the binary-grid estimate, coarse levels, finite-grid convergence, interpolation and p-dependent moment choice. Those are concrete mathematical calculations available as context, not reviewer verdicts. The new sections3–7 above supply their formerly unexpanded operator variance and fixed-grid convergence input.

Here are the exact quantities passed to that calculation. Fix θ<η<β in the strict allowed range and an even q0 such that q0γ>d and β−η−1/q0>0. For every even q≥q0,

    ||Kχ||_(S_q)≤||Kχ||_(S_q0),

by normalizing the singular-value sequence by its S_q0 norm and using x^q≤x^q0 for x∈[0,1]. Use (2.9)'s strict β variance improvement in (6.2). It gives, uniformly in N, the noise basis and such even q,

    ||X_N(t)−X_N(u)||_(L^q B(E)) ≤C sqrt(q)|t−u|^β,  |t−u|≤1.   (8.1)

C depends on fixed Γ,a,α,γ,β,ζ,R,T,q0 through ||Kχ||_(S_q0), but not on q,N,t,u apart from the increment factor. Longer increments are finite sums of short ones.

For D_n the largest adjacent increment on the grid kT2^(−n), the finite-maximum inequality gives ||D_n||_(Lq)≤2^(n/q) C sqrt(q)(T2^(−n))^β at fine levels. Therefore the weighted dyadic sum at exponent η is bounded in Lq by C_η sqrt(q), using the common geometric gap β−η−1/q0>0; finitely many coarse levels use unit partitions. No independence of increments is used. The supplement's deterministic binary approximation bounds the C^η norm by this weighted sum for zero-start continuous paths. The finite paths are operator-norm Lipschitz by PROOF087, so this input is noncircular.

Section6 now gives L^q convergence of every value on each finite time grid. Combining it with the uniform C^η estimate gives L^q C^0 Cauchy convergence, first fixing the grid and then refining it. The deterministic interpolation estimate

    ||F||_(C^θ) ≤C ||F||_∞^(1−θ/η) ||F||_(C^η)^(θ/η)

and scalar probability Holder give L^q C^θ Cauchy convergence. The path limit lies in the separable C^θ-closed span of the countably many deterministic Lipschitz paths A_j(0,·); it is strongly measurable on the original Ω. An a.s. C^θ convergent subsequence is uniformly operator-norm convergent, so the compact values hold at **all times on one path event**. Evaluation at any fixed time agrees with the section6 interval limit by uniqueness in probability. This is the precise operator-convergence seam needed by the PROOF093 assembly.

For each finite p, choose an even q≥max(p,q0) with q≤p+q0+2≤(q0+3)p. It follows that || ||M_R||_(C^θ) ||_(Lp)≤C sqrt(p), with a p-independent fixed-data constant. The existing supplement's positive exponential series then gives E exp(c||M_R||_(C^θ)²)<∞ for sufficiently small c>0. Neither this interface nor section6 asserts a Schatten-valued Holder path. No source-cutoff convergence, nonlinear Young evolution, canonical solution/moment theorem, growing-R estimate or new covariance comparison is deduced here.

## 9. Constant and quantifier ledger; disposition

| Quantity | Dependence / uniformity actually proved |
|---|---|
| Scalar row K | α,a,γ only; independent of d,ν_R,Cν,h,frequency. Strict gaps are fixed; no endpoint uniformity. |
| Cν | Original covariance/amplitude and dimension, fixed profile ζ; independent of R by ||ζhat_R||_1=||ζhat||_1. |
| A_T and C_T | A_T=C1(a)(1+T)^4, C_T=4A_T K Cν. Uniform in R, short I/location/h beyond its factor, phase family size, noise truncation N and Gaussian q. |
| Raw admission / coefficient gain | May depend on fixed R,T,j and Sobolev index. Only identify each coefficient/domain/localization; their j-dependent bounds are not summed. |
| χ, Kχ, B_out/in | χ is chosen after fixed R,T. Compact/Schatten constants may depend on χ,d,γ. qγ>d is strict; no uniform-R cutoff norm or endpoint Schatten result. |
| Positive tails | Strong convergence and Tr(T_N^(q/2))→0 at each fixed I and admissible fixed q. No uniform rate over I,R,q or bases. |
| Finite Gaussian moment | Only explicit sqrt(q−1), with the retained average; independent of coefficient count and matrix compression dimensions. |
| Uniform finite increment bound | For even q≥fixed q0, same fixed cutoff S_q0 norm, same C_(T,β); hence C sqrt(q) independent of q and N. |
| Arbitrary p | Select a new admissible even q for each requested p; all limits agree by convergence in probability. No claim that one fixed q supplies all p. |
| Probability/version | Original given W throughout; first-chaos scalar coordinates, fixed-row L² identity, finite/countable interval coherence, then continuous path version. No initial random bounded operator is presumed from mean-square columns. |

If Γ=0, H_W is the zero quotient, all coefficients, forms, variances, columns and drivers are zero. No infinite nonzero noise basis is then required; every statement is the direct zero identity. If h=0, define the interval objects as zero rather than evaluate Bα at zero. The phase E itself is retained.

**Author disposition:** the two requested subaims are fully worked above: actual random Fourier-row/Bessel bounds give both finite coefficient operator inequalities and their original first-chaos expansions; actual localization yields compact summable two-sided envelopes; vanishing tail traces give genuine same-space compact Gaussian interval convergence and the retained row/additivity; the existing dyadic argument then has its missing interval/operator input. No real gap was found in this chain. This does not upgrade any independent review, reprove the imported cutoff/finite-matrix theorem, grant source-image or cold credit, or certify the entire PROOF085–093 module/application graph. Root inspection remains the next step, with any later review dispatch separate and not authorized by this artifact itself.
