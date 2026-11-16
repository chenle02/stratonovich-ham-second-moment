# Review Result
Category: proof-readability-equivalence
Model: deepseek/deepseek-v4-pro
Verdict: PASS_WITH_NOTES
Confidence: high

All five assigned OLD/NEW pairs were read in full from the embedded sources. Every target proof is readable and its deductions reconstruct cleanly. The rewrite adds one roadmap and (mostly) step headings per proof, a handful of explanatory sentences, and uniformly retains the substantive deductions. I found exactly one OLD sentence deleted in `P:symplectic-block-mean`; it is a methodological remark whose mathematical role is met by the remaining construction (shown below), not a missing deduction. The new explanatory sentences are all correct under the unchanged hypotheses. Pre-existing concerns (a cross-module mask-notational exactness in the combined source coefficient, and the terse "rank zero" instantiation of a Cameron identity) are identical in OLD and NEW and are flagged, not imputed to the rewrite. No AUDIT markers remain in the module.

---

## L:symplectic-free

- Old reading: COMPLETE (proof LF 63–134)
- New reading: COMPLETE (proof LF 63–160)
- Public reconstruction: COMPLETE
- Original-step coverage: all four OLD deductions present; NEW adds a preamble and four step headings plus one clarifying sentence.

Steps and checkable working.

**(1) J_E construction (OLD ~63–72 / NEW Step 1).** With `C_bal(u,v)=(Λ^{1/2}u,Λ^{-1/2}v)` an onto real isometry to `L^2×L^2` and `J_symp(q,p)=(p,-q)`, set `J_E=C_bal^{-1}J_symp C_bal`. Then `J_E^2=C_bal^{-1}J_symp^2C_bal=-I`, `J_E^*=C_bal^{-1}(-J_symp)C_bal=-J_E` (C_bal unitary), and `J_E` is isometric, so it is a bounded isometric skew-adjoint with square `-I`. The form expands as
`<z,J_Ew>_E = <Λ^{1/2}u,Λ^{-1/2}g>_2 + <Λ^{-1/2}v,−Λ^{1/2}f>_2 = <u,g>_{H^{1/2},H^{-1/2}} − <f,v>_{H^{1/2},H^{-1/2}}`, matching the displayed duality; no `L^2` pairing of a general `H^{-1/2}` velocity is taken.

**(2) Free-wave invariance (OLD ~73–86 / NEW Step 1).** In balanced Fourier coordinates the free matrix is `W_t(ξ)=[[cos, ⟨ξ⟩sin/k],[−k sin/⟨ξ⟩, cos]]`, `k=|ξ|`. Direct computation: for `a=cos`, `b=⟨ξ⟩sin/k`, `c=−k sin/⟨ξ⟩`, `W_t^T J_symp W_t = [[−c,a],[−a,b]][[a,b],[c,a]] = [[a^2−cb,0],[0,a^2−bc]]`, and `cb=−sin^2` gives `a^2−cb=1`, so the product equals `J_symp`; this is consistent with `det W_t=cos^2+sin^2=1` (the determinant remark is a check, not the whole argument). At `ξ=0`, the continuous sine quotient gives `[[1,t],[0,1]]`. Integrating against symmetric Fourier phases is legitimate by `L^2` Cauchy–Schwarz and yields `ω(S_E(t)z,S_E(t)w)=ω(z,w)`; Schwartz density extends to all `E`. No generator derivative or `ξ=0` trace is used. Correct.

**(3) Force skewness and Young endpoint compactness (OLD ~88–104 / NEW Step 2).** `B(b)(u,v)=(0,bu)` has `‖bu‖_{H^{-1/2}} ≤ ‖bu‖_2 ≤ ‖b‖_∞‖u‖_2 ≤ ‖b‖_∞‖u‖_{H^{1/2}}`, so `B(b)` maps `E` to `E`; the cancellation `−∫fbu+∫ubf=0` for real `b` gives `ω(Bz,w)+ω(z,Bw)=0` (skewness in `ω`, not in `⟨·,·⟩_E`). The Young construction of `P:constant-young-linear` on `L(E)` applies (Banach algebra, product norm one). Each left Young sum `Σ_j(X(t_{j+1})−X(t_j))U_X(t_j,s)` is a finite sum of compact operators; these sums converge in operator norm to `U_X(t,s)−I`, and `K(E)` is norm-closed, so `U_X(t,s)−I∈K(E)` is the first assertion of `E:symplectic-compact-young-baseline`. Bounded composition gives `S_E(t)U_X(t,s)S_E(−s)=S_E(t−s)+S_E(t)KS_E(−s)` with the second term compact.

**(4) Compact-perturbation norm bound (OLD ~105–125 / NEW Step 3).** Translations `τ_y` act isometrically on both entries and commute with the (translation-invariant) free group. For fixed `z,w∈E`, `<τ_yz,w>_E` is the Fourier transform of an `L^1` function (the two weighted products `Λ^{±1/2}` of two `L^2` factors are `L^1`), hence tends to zero as `|y|→∞` by Riemann–Lebesgue; equivalently each entry `τ_y z ⇀ 0` weakly. Therefore a compact `K` satisfies `Kτ_yz→0` in norm (a nonzero norm limit along a weak-null net is excluded by compactness + bounded linear testing). For unit `z`, `‖(S_E(h)+K)τ_yz‖ ≥ ‖S_E(h)τ_yz‖−‖Kτ_yz‖ = ‖S_E(h)z‖−o(1)`, so `liminf ≥ ‖S_E(h)z‖`; supremum over unit `z` gives `‖S_E(h)+K‖ ≥ ‖S_E(h)‖`. The velocity reversal `R(u,v)=(u,−v)` is an isometry with `S_E(−h)=RS_E(h)R` (checked: conjugation of `[[cos,b],[c,cos]]` by `diag(1,−1)` gives `[[cos,−b],[−c,cos]]=W_{−h}`), so `‖S_E(−h)‖=‖S_E(h)‖` and the group law gives `1≤‖S_E(h)‖‖S_E(−h)‖=‖S_E(h)‖^2`, i.e. `‖S_E(h)‖≥1`. This proves `E:symplectic-compact-young-baseline`.

**(5) Finite ordered products (OLD ~126–133 / NEW Step 4).** `P_j−S_E(ℓ_j)=S_E(ℓ_j)(U_{X_j}(ℓ_j,0)−I)` is compact. Telescoping `P_N…P_0−S_E(Σℓ_j)` against the free product produces a finite sum of bounded–compact–bounded products (only free factors are regrouped by the group law; no noisy factors are commuted), hence compact. The same translation argument gives the norm lower bound `E:symplectic-compact-product-baseline`. Zero length gives `P_j=I`. Correct.

- Argument preservation: PRESERVED. All OLD sentences appear; nothing substantive removed.
- New explanations: JUSTIFIED. The new Step 3 sentence is exactly the reverse-triangle-inequality computation given in (4): `‖S_E(h)τ_yz‖=‖τ_yS_E(h)z‖=‖S_E(h)z‖`, `Kτ_yz→0`, hence the `liminf ≥ ‖S_E(h)z‖` before the supremum. The "Finally" in Step 2 is only a vestigial transition word carried verbatim from OLD; not a mathematical issue.
- Evidence: equation labels `E:symplectic-compact-young-baseline`, `E:symplectic-compact-product-baseline`; computations above; OLD LF 63–134 vs NEW LF 63–160 reduced to four headings + one sentence.
- Lost steps/qualifiers: none identified. Pre-existing concerns: none; the compact-baseline bound correctly needs no Gaussian or Hamiltonian hypothesis, as the statement emphasizes.

---

## L:symplectic-source-mean

- Old reading: COMPLETE (proof LF 154–186)
- New reading: COMPLETE (proof LF 180–235)
- Public reconstruction: COMPLETE
- Original-step coverage: all three OLD paragraphs present; NEW adds a preamble, three step headings, one citation sentence, and one identification sentence.

Steps and checkable working.

**(1) Bochner means and convergence bound (OLD ~156–160 / NEW Step 1, LF ~182–195).** `Z=W(Φ)` is scalar Gaussian with `‖Z‖_2=‖Φ‖_{H_W}`; Cauchy–Schwarz gives `E‖ZM‖_{C^θ} ≤ ‖Φ‖‖M‖_{L^2C^θ}`, and the Bochner bound gives `‖D_Φ^ρ−D_Φ‖_{C^θ}=‖E[Z(M^ρ−M)]‖_{C^θ}≤‖Φ‖‖M^ρ−M‖_{L^2C^θ}→0`, proving `E:symplectic-mean-convergence`. The added citation is correct: `E:source-driver-limit` supplies `M^ρ→M` in `L^2C^θ`; `E:source-two-dominations` gives the variance bound with `C=1`, and `E:source-transfer-norm` then gives `‖M^ρ‖_{L^2C^θ}≤‖M‖_{L^2C^θ}`, which with covariance contraction yields the uniform source bound `‖D_Φ^ρ‖_{C^θ}≤‖Φ‖‖M‖_{L^2C^θ}`.

**(2) Regularized deterministic coefficient (OLD ~161–173 / NEW Step 2).** `j_src:H_W→G` isometry, `I` isonormal with `I(j_src h)=W(h)`; the field `Y^ρ(t,x)=I(v_{ρ;t,x})` has continuous `G`-valued spatial derivatives at positive widths. Hence `h_Φ^ρ(t,x)=E[W(Φ)Y^ρ(t,x)]=<j_srcΦ,v_{ρ;t,x}>_G` inherits that spatial smoothness and time continuity and is real; bounded linear testing commutes with the derivatives. Multiplying by `m_R` gives one compact support with bounded derivatives on `[0,T]`.

**(3) Primitive identification (OLD ~174–186 / NEW Step 3).** On Schwartz states the row of `E:symplectic-source-primitive` is the integral of `h_Φ^ρ` against the masked source wave product. Fubini is justified by `E|ZY^ρ(t,x)|≤‖Φ‖√(E|Y^ρ(t,x)|^2)` with bounded point variance `‖v_{ρ;t,x}‖_G^2` on the compact set at positive widths; indicator approximation extends to completed rows by Gaussian Cauchy–Schwarz and covariance contraction. This identifies the row with the row of `E[ZM^ρ(t)]`; countable dense states + rational times + continuity of both sides identify the operator path; the bounded integrand gives the Lipschitz bound. Hence `D^ρ=∫S_E(−r)B(b^ρ(r))S_E(r)dr` with combined source coefficient `b^ρ=m_R(cY^ρ+h_Φ^ρ)`, noncentered, mask occurring once. The added sentence ("`P:source-ordinary-response` identifies `M^ρ` with the ordinary source primitive; the approximation here extends smooth time tests to the indicator wave tests in `E:source-transferred-row`") summarises exactly this deduction. Correct.

- Argument preservation: PRESERVED. No OLD content removed.
- New explanations: JUSTIFIED (citations verified in step (1); summary sentence verified in step (3)).
- Evidence: `E:symplectic-mean-convergence`, `E:symplectic-source-primitive`, plus upstream `E:source-driver-limit`, `E:source-transfer-norm`, `E:source-two-dominations`; OLD LF 154–186 ↔ NEW LF 180–235.
- Lost steps/qualifiers: none identified.
- Pre-existing concern: the exactness of `b^ρ=m_R(cY^ρ+h_Φ^ρ)` depends on the module's mask convention (`m_R`) matching the source-primitive mask `ζ_R` of `P:source-ordinary-response`. `raw_block_lower` explicitly equates `m_R=ζ_R`, so this is self-consistent in the symplectic module; but the Cameron module uses `m_R=η_R^2`, so a careful cross-module reading is needed. This is identical in OLD and NEW, and does not affect the conservation results (Lemma `L:symplectic-free` needs only bounded real smooth `b`).

---

## P:symplectic-source

- Old reading: COMPLETE (proof LF 197–219)
- New reading: COMPLETE (proof LF 246–272)
- Public reconstruction: COMPLETE
- Original-step coverage: both OLD paragraphs plus the closing "No uncountable intersection…" sentence present; NEW adds one explanatory paragraph after the skewness assertion.

Steps and checkable working.

**(1) Coefficient regularity event (OLD ~199–209 / NEW ~248–256).** Intersect the coefficient-regularity event with the event identifying the first primitive with the ordinary primitive for all times and states (both supplied at fixed `ρ`). On the intersection `b^ρ` has common compact support, is sup-norm continuous and uniformly bounded on `[0,T]`; hence `C_b(r)=S_E(−r)B(b^ρ(r))S_E(r)` is uniformly bounded and strongly continuous on states (multiplier sup-bound factors the `B` norm; both free groups are strongly continuous and bounded on the horizon).

**(2) Skewness of the conjugate (OLD ~210 / NEW ~257–263 + added).** Lemma `L:symplectic-free` gives `ω(C_b(r)z,w)+ω(z,C_b(r)w)=0`. The added paragraph is correct: with `S=S_E(−r)` and free invariance `ω(Sx,Sy)=ω(x,y)`, one has `ω(S_E(−r)x,w)=ω(x,S_E(r)w)`, so `ω(S_E(−r)BS_E(r)z,w)+ω(z,S_E(−r)BS_E(r)w)=ω(BS_E(r)z,S_E(r)w)+ω(S_E(r)z,BS_E(r)w)=0` by the `B(b^ρ)` force skewness. The closing sentence is also accurate: `B(b)` is skew for `ω`, not for the `E` Hilbert inner product.

**(3) Young equation = ordinary equation (OLD ~212–218 / NEW ~264–269).** Replace each Young path increment by its statewise integral `∫C_b(r)dr`; the replacement error is bounded by the uniform coefficient bound times the uniform continuity error of `U` on the partition. Each state trajectory is `C^1` with derivative `C_b(t)U(t,s)e` (strong-integral difference quotient, using sup-norm continuity of `C_b(r)`), so `U(t,s)e=e+∫_s^tC_b(r)U(r,s)e dr`.

**(4) Differentiate the form.** `d/dt ω(U(t,s)e,U(t,s)f)=ω(C_bU e,Uf)+ω(Ue,C_bU f)=0` by (2), so `U(t,s)^*J_EU(t,s)=J_E` for all `s,t` on the same path set.

**(5) Free conjugation.** `P_{D^ρ}(t,s)=S_E(t)U(t,s)S_E(−s)` gives `P^*J_EP=S_E(−s)^*U^*S_E(t)^*J_ES_E(t)US_E(−s)=S_E(−s)^*U^*J_EUS_E(−s)=S_E(−s)^*J_ES_E(−s)=J_E`, using free conservation at `t` and at `−s`. Correct; the "No uncountable intersection of state-dependent null sets or derivative of the free generator on a rough state" claim is accurate (only the strongly differentiable `U` is differentiated).

- Argument preservation: PRESERVED.
- New explanations: JUSTIFIED (verified computation in (2)).
- Evidence: equation `P_{D^ρ}(t,s)^*J_EP_{D^ρ}(t,s)=J_E`; OLD LF 197–219 ↔ NEW LF 246–272; the added paragraph is the isolated insertion between the skewness sentence and "The source and mean primitive identities…".
- Lost steps/qualifiers: none identified. Pre-existing concerns: none beyond the mask-convention remark inherited from `L:symplectic-source-mean`.

---

## P:symplectic-raw

- Old reading: COMPLETE (proof LF 237–285)
- New reading: COMPLETE (proof LF 290–358)
- Public reconstruction: COMPLETE
- Original-step coverage: all four OLD paragraphs present as Steps 1–4; NEW adds a preamble only.

Steps and checkable working.

**(1) The closed constraint `g_J` (OLD ~239–250 / NEW Step 1).** `g_J={A:A^*J_E+J_EA=0}` is a closed real linear subspace (kernel of the bounded map `A↦A^*J_E+J_EA`). `H_{j,R}` in `E:driver-covariance-coefficient` is real smooth; free conservation gives `S_E(−r)^*J_E=J_ES_E(r)` and `J_ES_E(−r)=S_E(r)^*J_E`. Verified: `S_E(t)` is a unitary group preserving `ω`, so `S_E(t)^*J_ES_E(t)=J_E`; left-multiplying by `S_E(t)` gives `J_ES_E(t)=S_E(t)J_E`, and with `S_E(t)^*=S_E(−t)` both displayed identities follow. Since `B(H_{j,R}(r))` is `ω`-skew (Lemma `L:symplectic-free`), `B^*J+JB=0`, and conjugation `S_E(−r)(·)S_E(r)=S_E(r)^*(B^*J+JB)S_E(r)=0` puts the conjugate in `g_J`. Testing the statewise integral in `E:driver-coefficient-operator` against two states passes the closed constraint to `A_j(0,t)∈g_J` for every `j,t`. Real finite sums in `E:driver-path-convergence` inherit it; as `A↦A^*J+JA` is bounded on path space, the `L^2C^θ` limit `M` obeys it at all times on one probability-one path set.

**(2) Constraint to the combined driver (OLD ~252–258 / NEW Step 2).** `D_Φ=E[ZM]` is a Bochner expectation (`E‖ZM‖_{C^θ}≤‖Φ‖‖M‖_{L^2C^θ}<∞` by `E:driver-gaussian-norm` and Cauchy–Schwarz); bounded real-linear maps commute with it, so `D_Φ(t)∈g_J`. Thus `D=cM+D_Φ` starts at zero (`M(0)=0`, `D_Φ(0)=0`) and is a `C^θ` path in `g_J` on that path set; no complex Gaussian coefficients, all on the given `W`.

**(3) Young conservation (OLD ~260–275 / NEW Step 3).** Fix `s`, `V(r)=U_D(r,s)`. The Young remainder gives `V(v)−V(u)=D_{u,v}V(u)+R_{u,v}`, `‖R_{u,v}‖≤C|v−u|^{2θ}`. Expanding `V(v)^*J_EV(v)−V(u)^*J_EV(u)` (telescoping) gives the first-order term `V(u)^*(D_{u,v}^*J_E+J_ED_{u,v})V(u)`, which vanishes because increments `D_{u,v}=D(v)−D(u)∈g_J` (linear subspace). The residual is `Δ^*J_EΔ`-type plus cross terms with `R_{u,v}`, of norm `≤C′|v−u|^{2θ}` (uses `[D]_θ`, bounded `‖V‖`, `‖R‖`). Summing over a partition gives `C′(t−s)mesh^{2θ−1}→0` since `θ>1/2`; hence `U_D(t,s)^*J_EU_D(t,s)=J_E`. Deterministic on the fixed path; no state-dependent null sets.

**(4) Free conjugation and norm (OLD ~276–279 / NEW Step 3 end).** As in `P:symplectic-source`, `P_D(t,s)=S_E(t)U_D(t,s)S_E(−s)` satisfies `P_D^*J_EP_D=J_E`, and `1=‖J_E‖≤‖P_D(t,s)‖^2` (here `‖J_E‖=1` because `J_E` is an isometry). This is `E:symplectic-raw-conservation`.

**(5) Invertibility, `c=0`, fixed-`δ` reference (OLD ~281–285 / NEW Step 4).** Invertibility via local Young Neumann pieces and finite products followed by the free inverse (`U_D` invertible by `P:constant-young-linear`; `P_D` is a product of invertibles), not inferred from infinite-dimensional conservation. For `c=0`, `D=D_Φ` is deterministic for fixed `Φ`; zero covariance gives the free flow directly. The fixed-`δ` instance (`W∘T_{δ,0}`, `R=δ^{-1}+2`, `T=δ^{-1}`, `c=g_δ`, `Φ=0`) is retained, with no uniform-radius/bound assertion.

- Argument preservation: PRESERVED.
- New explanations: JUSTIFIED (the preamble "…prove conservation by summing Young remainder estimates; invertibility comes separately from the Young construction" matches Steps 3–4 exactly).
- Evidence: `E:symplectic-raw-conservation`; computations in (1), (3); OLD LF 237–285 ↔ NEW LF 290–358 differing only by the preamble and headings.
- Lost steps/qualifiers: none identified. Pre-existing concerns: none in this proof.

---

## P:symplectic-block-mean

- Old reading: COMPLETE (proof LF 314–382)
- New reading: COMPLETE (proof LF 387–476)
- Public reconstruction: COMPLETE
- Original-step coverage: all five OLD deductions present; NEW adds a preamble, four step headings, and one citation sentence; one OLD sentence is deleted (analyzed below).

Steps and checkable working.

**(1) Fast control (OLD ~316–324 / NEW Step 1, LF ~390–399).** `T_m=T_{δ,m}` is an isometry of the completion (covariance factor `δ^{a−2}δ^2δ^{−a}=1` in `E:raw-block-pullback`), so its Hilbert adjoint is a contraction and `‖φ_m‖≤δ^{−a/2}‖Φ‖` is finite at fixed `δ`; no uniform control-radius assertion. The fast noise `W_m(f)=W(T_mf)` remains on the given `W`.

**(2) Completed mean and compact primitive (OLD ~326–339 / NEW Step 1, LF ~400–414).** `TΦ` (full `F` mean, `P:cameron-full-mean`) has range in the closed `iE`; the bounded compression `A↦i^*Ai` passes strong measurability, the `L^r` bound and compact values to `T_EΦ∈L^r(I;K(E))`. The parameter intervals in `E:cameron-block-parameters` are nonempty because `θ<1−a/2` and `θ>1/2`. Compact-conjugation (norm continuity of conjugation on compact-valued strongly measurable fields) makes `E:symplectic-block-primitive` a Bochner integral; the `L^r` primitive estimate gives `C^θ` since `1−1/r>θ`; affine pullback preserves nulls; closedness of `K(E)` under Bochner integration makes `H_{m,E}(Φ)` compact-valued, starting at zero, and constant stopping preserves this. The added sentence — "The compact-conjugation and primitive estimates are those in `P:cameron-actual-embedding`, including `E:cameron-local-primitive-bound`, restricted from `F` to `E`: compactness gives norm-continuous conjugation and Hölder integration gives exponent `1−1/r`" — is a correct structural citation: the `F`-arguments in that proposition carry over to the invariant closed subspace `iE≅E` (via `S_Fi=iS_E`), and the Hölder exponent is space-independent.

**(3) Unscaled covariance by compression (OLD ~341–355 / NEW Step 2).** With `A_{F,m}` the full `F` path (`P:constant-phase-driver`) and `H_{m,F}` the stopped completed mean primitive of `E:cameron-actual-covariance` at projection rank zero, `E[g_δA_{F,m}(u)W(i_IΦ)]=√δ H_{m,F}(Φ)(u)` for `u≤ℓ_m`. Compress through `i` using `A_{F,m}i=iM_m`, `S_Fi=iS_E`, mean range in `iE` preserved by `S_F`, and commutation of Bochner expectation with the bounded compression; the constant columns are retained until compression (inactive on `iE` inputs). Since `g_δδ^{a/2}=δ^{(1−a)/2}δ^{a/2}=√δ` and `g_δ>0`, division gives `E:M_m(u)W(i_IΦ)=δ^{a/2}H_{m,E}(Φ)(u)` for `u≤ℓ_m` (`E:symplectic-unscaled-covariance`); the factor is correctly `δ^{a/2}`, not `√δ`. Completion permits every `Φ∈H_I` without positivity or smoothness.

**(4) Fast-noise direction (OLD ~357–368 / NEW Step 3).** `T_mT_m^*` is the orthogonal projection onto the isometry's closed range, so `W((I−T_mT_m^*)i_IΦ)` is orthogonal to the fast first chaos. Every continuous linear coordinate of `M_m` is an `L^2` limit of finite `W_m`-basis sums, so its covariance with that orthogonal direction vanishes; Bochner covariance exists by `L^2` path moments and bounded linear functionals separate values. Hence `E[M_m(u)W(i_IΦ)]=E[M_m(u)W_m(T_m^*i_IΦ)]`. Multiplying by `δ^{−a/2}` and using `E:symplectic-unscaled-covariance` gives `E:symplectic-block-direction` on `[0,ℓ_m]`, then both sides are stopped; no unstopped equality beyond `ℓ_m` is asserted.

**(5) Endpoint lower bound (OLD ~370–382 / NEW Step 4).** Apply Lemma `L:symplectic-free` to the compact-valued `C^θ` path `H_{m,E}(Φ)` starting at zero on `[0,B]`: `‖S_E(ℓ_m)U_{H_{m,E}(Φ)}(ℓ_m,0)‖≥‖S_E(ℓ_m)‖≥1`; zero length gives the identity with norm one. The radius `δ^{-1}+2` is chosen only after fixing `δ`; all identities are fixed-parameter instances.

**The deleted OLD sentence.** OLD LF ~322–325 contains: "For applying the preceding propositions, construct regularized noises with `W_m` as the given reference, extending by an independent auxiliary source while retaining all base variables. No slow-source pullback is presumed; the original covariance direction is independent of the auxiliary realization." This is absent from NEW. Its mathematical role in *this* proof is nil: the direction identity (steps (3)–(4)) and the endpoint bound (step (5)) are established purely from the Cameron mean, the fast-noise projection, and Lemma `L:symplectic-free`; the preceding conservation propositions (`P:symplectic-source`, `P:symplectic-raw`) are never invoked in NEW or OLD at the final step. The sentence was a remark about how one *would* re-run those propositions for `W_m`; the proof instead gets the norm bound from the deterministic compact baseline, which is stronger (no Gaussian or Hamiltonian hypothesis). The qualifier on `φ_m` (no slow-source pullback is presumed) is still enforced by the definition `φ_m=δ^{−a/2}T_m^*i_IΦ` in the unchanged statement. Consequently the deletion removes explanatory prose but no step, and its mathematical role is met by the remaining construction under the same hypotheses.

- Argument preservation: PRESERVED (with the one non-load-bearing deletion noted above).
- New explanations: JUSTIFIED (preamble matches the four steps; the `P:cameron-actual-embedding` citation is verified structurally; the "Step 3" heading "remove the orthogonal complement of the fast first chaos" matches the deduction).
- Evidence: `E:symplectic-block-primitive`, `E:symplectic-block-direction`, `E:symplectic-unscaled-covariance`, `E:cameron-actual-covariance`, `E:raw-block-pullback`; OLD LF 314–382 ↔ NEW LF 387–476.
- Lost steps/qualifiers: the single deleted sentence (role shown met above); no other OLD content dropped. Pre-existing concern: `E:cameron-actual-covariance` is stated with the residual projection `Q_J=I−P_J`; it is instantiated here "at original projection rank zero" (`P_J=0`, `Q_J=I`), which is a valid fixed instance but is only paraphrased, not restated as an equation, so a reader must supply that identification. Identical in OLD/NEW. Additionally the cross-module mask convention (`m_R` vs `ζ_R`/`η_R^2`) noted under `L:symplectic-source-mean` propagates here through the Cameron mean, but the compression/covariance algebra is convention-independent.

---

## AUDIT dispositions

No AUDIT comments remain in this module (neither OLD nor NEW text contains an AUDIT flag). AUDIT-worthy items worth recording, all pre-existing and byte-identical across OLD and NEW:

1. **Combined source-coefficient exactness (`L:symplectic-source-mean`, statement + proof end).** The claim `b^ρ=m_R(cY^ρ+h_Φ^ρ)` is exact only relative to the book's convention that the module mask `m_R` equals the source-primitive mask `ζ_R` of `P:source-ordinary-response`; `raw_block_lower` asserts `m_R=ζ_R`, but the Cameron module defines its `m_R=η_R^2`. Not a rewrite defect, and harmless for the conservation proofs (which use only bounded real smooth coefficients), but the cross-module notation should be pinned down.
2. **"Projection rank zero" instantiation (`P:symplectic-block-mean`).** The phrase "the completed identity `E:cameron-actual-covariance` at original projection rank zero" is a paraphrase for `P_J=0` (`Q_J=I`); an explicit equation would remove ambiguity. Valid, but terse.

---

## Findings and limits

Scope: exactly the five assigned proof pairs and their unchanged statements; baseline context modules were used only as stated-input sources under their checked hypotheses and were not counted as reviewed proofs. I did not certify upstream theorem fidelity or whole-book truth; the match between OLD and NEW statements is verified at the level of the indexed statement line ranges (all five statements are textually identical modulo line offsets). All five reconstructions above are public and computational at the substantive steps (symplectic matrix identity `W_t^TJ_sympW_t=J_symp`, the reverse-triangle compact-perturbation bound, the `g_J` propagation through the Gaussian path and covariance mean, the `δ^{a/2}`-vs-`√δ` scaling, and the fast-first-chaos orthogonality), and no target step was left as "unchanged" without a reconstruction. The equivalence verdict is high-confidence: the rewriting introduced no mathematical change, no lost deduction, and no unjustified new assertion; the only deletion is a provably non-load-bearing methodological sentence; the only concerns found are pre-existing and identical in both revisions. These results provide the operator-norm lower bound and its completed-mean application but, as the module states, no uniform control radius, stochastic upper bound, or nonlinear product ratio.
