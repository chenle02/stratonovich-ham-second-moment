# Author-side reconciliation of symplectic PROOF165–169

I recommend **scoped root adoption of these five exact proof bodies after recording the source-based adjudications below**, while retaining all unmet upstream and whole-paper gates. This is an author-side recommendation, not a new independent review, a grade upgrade, an adoption action, or permission to describe the correction report as entirely accurate. No manuscript repair is indicated by this audit. Two additional statements in the same-session correction are false as written and must be excluded from the adopted reasoning.

The native original and correction both report PASS_WITH_NOTES/HIGH. Their session is `ses_e63f17bafffeoRyE7VYCoz4YwU`; the correction adds one user message and one assistant message to the exact preserved original two-message prefix. It is one reviewer and one same-session correction, not two independent votes. Both actual assistant routes are `deepseek/deepseek-v4-pro`, both finish with `stop`, and neither uses tools. The original 64-member archive and correction 34-member archive were independently read back against their inventories. Their raw reports and grades remain unchanged.

The snapshot is bound in `provenance-checks.json` to ACTIVE HEAD `b1ca9e2abcd4f1c979f87cc0631ad24d8867cd65`. All five targets and eight prerequisite/source files in `source/` match both that current Git/live snapshot and the earlier reviewed scientific887 bytes. Target identity is index-v3 inner-body hash plus declaration/closing label, not ordinal alone. The main manuscript has changed elsewhere since887; this audit does not transfer unrelated887 coverage to new text.

## What the reports establish and what must be rejected

Report line numbers below refer to the retained native `report.txt` copies under `native-evidence/`. Source line numbers refer to the retained current files under `source/notes/`.

| Issue | Original report | Same-session correction | Source adjudication |
|---|---|---|---|
| Input delivery versus reading | Original24,48,54 falsely classifies delivered Cameron/Friz bodies as absent. | Correction14–21 retracts that classification;31,76–86 separates consumed, unused and upstream inputs. | Delivery is not reading. The original packet contains complete Cameron/Young/source bodies and Friz text. The corrected consumed clauses can be used within their actual scope; unreviewed upstream claims remain upstream obligations. |
| Statewise interaction C¹ versus physical evolution | Original39 incorrectly says physical P inherits C¹ on all E. | Correction37–41 retracts this and proves physical conservation by free invariance. | Symplectic167–184 proves C¹ only for each interaction trajectory U(t,s)e. The physical group is strongly continuous on rough E; no C¹ free evolution or generator derivative is needed. |
| Force cancellation variables | Original51 mistypes a velocity variable in the cancellation. Original33 already has the correct formula. | Correction43–51 gives the correct displacement pairing. | Symplectic77–82: −∫fbu + ∫ubf = 0. The variables u,f are displacements in L²; g is a general distributional velocity and is not an L² multiplier. |
| Zero stochastic amplitude versus zero mean direction | Original51 conflates zero c or Φ with a free driver. | Correction53–58 distinguishes the deterministic mean c=0 from centered raw Φ=0, but55 adds the false necessity “not free unless Φ=0 as well.” | Symplectic193–198,259–267,384–388 only asserts the correct sufficient cases. c=0 gives a deterministic mean, generally nonfree. A nonzero Φ may be in the observed covariance kernel, so Φ=0 is sufficient, not necessary, for a zero mean driver. |
| Constant columns in the completed mean | Original15 correctly says they are retained until compression. | Correction62 incorrectly says the instantaneous spatial map “annihilates constant columns.” | Cameron89–100,133–134 retains the finite-rank c₁ displacement column; only instantaneous c₂ is zero. Cameron447–449 and Young149–185 retain both response columns after free conjugation. Range in iE is true and does not imply annihilation of constant inputs. |

No recommendation to weaken the stated smoothness hypothesis on b is adopted. The proof works under the stated stronger hypothesis. The original report’s suggested broadening is unnecessary.

## The constant-column point, explicitly

On F=E⊕R², write a state as (e,c₁,c₂). The actual instantaneous force is

    B_F(b)(e,c₁,c₂) = (0, b(e₁+c₁)) in E.

Consequently, for the pure constant-displacement and constant-velocity inputs q₁=(0,1,0), q₂=(0,0,1),

    B_F(b)q₁ = (0,b),          B_F(b)q₂ = 0.

For any nonzero compact smooth real b, the first expression is nonzero. This directly falsifies the correction’s “annihilates constant columns” assertion. The smooth spatial mean T_sp q=iB_F(m_R(Γ*q)) has exactly this c₁ column; its operator-norm closure still has range in closed iE, without killing c₁. Its row identity contains c₁ explicitly: k(z,w)=(η_R z₁+c₁η_R)(η_R Λ⁻¹w₂).

The free F group acts by (e,c₁,c₂)↦(S_E(v)e,c₁+vc₂,c₂). Thus

    B_F(b(v))S_F(v)q₂ = (0,v b(v)).

Even the initially zero instantaneous c₂ column contributes after free conjugation and time integration. The actual response columns are the integrals of S_E(−v)(0,b(v)) and S_E(−v)(0,vb(v)), respectively. This is why the full F driver and completed block mean retain both columns.

The E compression is nevertheless valid. S_F(v)i=iS_E(v), every TΦ(s) has range in iE, and i*i=I_E. Hence

    H_F(Φ)(u)i = i H_E(Φ)(u),
    i* E[A_F,m(u) W(i_IΦ)] i = E[M_m(u) W(i_IΦ)].

These are restriction/compression identities on zero-constant inputs, not identities obtained by deleting the full F constant columns. They justify exactly symplectic341–345. No full-F symplectic theorem follows from the E theorem.

## Reconstruction of the five claims

**PROOF165, L:symplectic-free.** Symplectic34–85 defines the actual bounded form on E=H¹ᐟ²×H⁻¹ᐟ². The balanced isometry C_bal(u,v)=(Λ¹ᐟ²u,Λ⁻¹ᐟ²v) pulls back J(q,p)=(p,−q), giving J_E(f,g)=(Λ⁻¹g,−Λf), J_E²=−I, J_E*=−J_E and norm one. Its duality formula never pairs a general velocity as an L² function. The balanced Fourier matrix has determinant cos²(tk)+sin²(tk)=1 and the continuous k=0 shear [[1,t],[0,1]]. Its entries are bounded on finite horizons. The finite 2×2 identity W_tᵀJW_t=J passes through the L² Fourier pairing to all real E states. This is not a determinant of an infinite-dimensional operator. For bounded smooth real b, bu,bf lie in L², and the force bracket is exactly −∫fbu+∫ubf=0. This is skewness for the symplectic form, not Hilbert skew-adjointness of B(b).

**PROOF166, L:symplectic-source-mean.** Symplectic87–146 takes Z=W(Φ) for an arbitrary fixed full raw direction. Bochner Cauchy–Schwarz gives

    ‖E[Z(Mρ−M)]‖_Cθ ≤ ‖Φ‖_H_W ‖Mρ−M‖_L²Cθ.

The source contraction also gives the uniform deterministic mean bound. In the retaining source realization, h_Φρ(t,x)=⟨j_srcΦ,v_ρ;t,x⟩ is deterministic, time-continuous and spatially smooth at positive widths. On the fixed mask support its needed derivatives are bounded. Fubini is controlled by E|ZYρ(t,x)|≤‖Φ‖√E|Yρ(t,x)|²; completed test rows then identify the actual statewise primitive ∫S_E(−r)B(m_R h_Φρ(r))S_E(r)dr. The mask occurs once. This primitive is operator-norm Lipschitz; neither a pointwise raw potential for general Φ nor an operator-norm derivative of the free group is asserted. The combined source coefficient m_R(cYρ+h_Φρ) can be signed and noncentered.

**PROOF167, P:symplectic-source.** Symplectic148–186 works on one fixed-parameter source regularity/identification event. C_b(r)=S_E(−r)B(bρ(r))S_E(r) is uniformly bounded and strongly continuous on every state, and is skew for ω by free invariance plus force cancellation. A Young sum applied to e differs from ∫C_b(r)U(r,s)e dr by at most the uniform coefficient bound times the integral of ‖U(t_i,s)e−U(r,s)e‖ on partition cells, which tends to zero. Thus U(t,s)e is C¹ with derivative C_b(t)U(t,s)e. Differentiating ω(Ue,Uf) is legitimate and gives zero. For P(t,s)=S_E(t)U(t,s)S_E(−s), apply free invariance before and after the interaction identity. P is not claimed C¹ on rough E. The event concerns fixed c,Φ,R,T,ρ; all states/time pairs follow from the bounded ordinary evolution and common source event, not an uncountable intersection of state-dependent null events.

**PROOF168, P:symplectic-raw.** Symplectic188–274 passes conservation to the actual given-noise flow. Uniform √p path moments, including the fixed deterministic mean shifts, give square-exponential tails. Young local Lipschitz dependence gives convergence on driver balls; the growth exponent 1/θ<2 and those tails give uniform integrability and all finite Lᵖ uniform-triangle convergence. The map from interaction differences to physical differences is bounded in the triangle supremum norm; no operator-norm continuity of S_E itself is assumed. E/F intertwining follows by applying the closed isometric inclusion i to the Young sums, including covariance means, and using state uniqueness.

Choose a source subsequence with expected squared uniform physical error ≤2⁻⁴ⁿ. Markov at threshold2⁻ⁿ gives probability ≤2⁻²ⁿ, summable. Intersect the countably many source conservation events and pass P_n*J_EP_n=J_E in operator norm. The actual raw flow is W-measurable, so the event descends from the retaining extension to the base space. Only fixed parameter tuples are covered.

Since ‖J_E‖=1, conservation gives 1≤‖P‖². Surjectivity is not inferred from that identity. Young local pieces separately satisfy ‖U−I‖≤1/3, giving a Neumann inverse; finite composition gives the global inverse. The physical inverse is S_E(s)U(t,s)⁻¹S_E(−t).

For c=0, D=D_Φ is deterministic and the same results hold deterministically for each fixed Φ. For Φ=0, D=cM is centered Gaussian, possibly zero. If both are zero, or Γ=0, D=0 and P(t,s)=S_E(t−s). Further directions may also have D_Φ=0. For example, with admissible d=1 spatial white noise, a nonzero smooth raw control supported spatially outside the fixed masked wave-test region has zero covariance with every driver row. This shows why the correction’s “unless Φ=0” necessity must be rejected. The growing-cone substitution at fixed δ provides only a pointwise norm baseline, not a uniform δ/R/T budget.

**PROOF169, P:symplectic-block-mean.** Symplectic276–382 uses the actual partition with final length ℓ_N∈[0,B), not a fictitious full final cell. The raw pullback T_m f(s,x)=δ^(a/2−1)f((s−s_m)/δ,x) has covariance factor δ^(a−2)δ²δ^(−a)=1, respects nulls, and extends isometrically with closed range. Thus its adjoint is contractive and φ_m=δ^(−a/2)T_m*i_IΦ is a legitimate raw fast direction, with finite bound δ^(−a/2)‖Φ‖ at fixed δ.

The actual completed mean TΦ is a compact-operator Lʳ field; the parameter package has θ>1/2 and 1−1/r>θ. Compact-valued free conjugation makes the block primitive Bochner measurable; affine time pullback and the Lʳ primitive estimate put the stopped H_m,E in Cθ. This consumes the completed operator field, not a general pointwise potential.

At projection rank zero the exact full-F covariance is

    E[gδ A_F,m(u) W(i_IΦ)] = √δ H_m,F(Φ)(u),     u≤ℓ_m.

Here gδ=δ^((1−a)/2), so √δ/gδ=δ^(a/2). The valid compression described above yields

    E[M_m(u) W(i_IΦ)] = δ^(a/2) H_m,E(Φ)(u).

T_mT_m* is the raw-range projection. The orthogonal complement of i_IΦ is orthogonal to every fast first-chaos coordinate; each continuous linear statistic of M_m is an L² limit of such coordinates. Therefore its Bochner covariance can replace W(i_IΦ) by W_m(T_m*i_IΦ). Multiplying by δ^(−a/2) gives D_φ_m(u)=H_m,E(Φ)(u) on[0,ℓ_m], and then both sides are stopped. No unstopped identity beyond ℓ_m is used.

Apply the deterministic c=0 case of PROOF168 with reference W_m and direction φ_m. At the true endpoint, Young uniqueness identifies the same E flow, giving ‖S_E(ℓ_m)U_H(ℓ_m,0)‖≥1. If ℓ_m=0, the endpoint is I and its norm is one. No uniform control-radius assertion follows from the finite bound on φ_m, and no product ratio, stochastic moment upper bound, or global intrinsic constant is established here.

## Remaining obligations and recommendation boundary

1. Root must record that the original delivery/C¹/force/zero-case attestations were wrong, and that the correction additionally overstates constant-column annihilation and the necessity of Φ=0 for freeness. The recommendation uses the source arguments above, not those false sentences. Neither raw report is rewritten or upgraded.
2. Existing ledger-v27 records PROOF093 (actual operator driver) and PROOF105/107/108 (extended driver, standalone Young evolution and Gaussian flow) as MEDIUM/not accepted. This audit reads their actual consumed clauses but supplies no new independent review or grade for those IDs. Their separate depth gates remain. Likewise, the correction’s named un-reaudited cutoff/physical-pair prerequisites cannot acquire review coverage from its HIGH header; their existing exact scope receipts must be consumed separately. The current ledger records079/135 and Cameron143/146/148 as scoped HIGH, which is workflow context, not a substitute for their proof bodies.
3. The Friz–Hairer input is the bounded-bilinear Young estimate (4.3), printed p.62, with general Banach-space applicability in §1.5, p.13. The source text was delivered and the particular import is appropriate for bounded operator composition. Its full upstream proof is imported, not reproduced or visually certified here. Teschl/Crouzeix/Chen-author carriers are not premises for these five symplectic proofs.
4. No image/render/cold-read credit, full-paper acceptance, independent-family count increase, all214 completion, or actual-all-model constant completion follows. This source-aware author audit is neither blind nor cold.
5. No additional native call, Article edit, staging, commit, reset, ref mutation, message to coauthors, or publication was performed. All output is confined to this external audit directory. Root alone can adopt the five exact targets and update the authoritative ledger.

The recommended scope is precisely PROOF165–169 as reconstructed here, conditional on their named upstream interfaces and retaining the outstanding upstream review obligations. The existing source does not need the two false correction-report claims.
