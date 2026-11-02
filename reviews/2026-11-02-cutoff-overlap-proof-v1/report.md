# Review Result — deepseek

- category: paper-review-deepseek
- model: deepseek/deepseek-v4-pro
- verdict: PASS_WITH_NOTES
- confidence: HIGH

## Critical findings

None. I found no proof-breaking gap, no false identity, and no silently assumed raw-overlap theorem in the audited excerpt (proof.md lines 1–221). The three added deductions — Lemma A (E-restriction and all-state/all-initial-time ordinary source identification), Lemma B (ordinary-source overlap and horizon restriction), and Proposition C (raw overlap/horizon transfer to a common original-W event) — are internally consistent and make correct use of the inlined construction modules. The only assumptions that could block the argument are exactly the named, tailormade inputs (C1–C5 in statement.json), whose interfaces match the inlined source material. The residual findings below are completeness/explicitness issues, not correctness errors.

One scoping note: the PaperDev-Tailored-Workflow.md excerpt is marked missing in this snapshot; I record that limitation but it does not change the verdict, since the statement.json, scope.txt, and the four construction modules give a sufficient audit interface.

## Noncritical findings

1. **Event bookkeeping in Lemma B is implicit.** Lemma B says “fix a regular source sample” and then compares two masks/horizons. For this sample to work simultaneously for R1,R2 (and T1,T2 in the horizon case), it must lie in the intersection of the Lemma A all-state events for the two coefficients. Lemma A line 120–121 does allow intersecting over countably many (n,R,T), so this is repairable, but Lemma B should say explicitly that the sample is drawn from `∩(Ω_A(n,R1,T), Ω_A(n,R2,T))` (and the corresponding T1,T2 in horizon argument).

2. **Distributional finite-propagation invocation is compressed.** Lemma B’s induction uses speed-one finite propagation for the free group applied to phase *distributions*, including the velocity component and local cancellation, and multiplier preservation of the vanishing-on-K_r property for both the `(m_R1−m_R2)Y_n Q` term and the state-difference term. This is exactly covered by L:constant-phase-free/L:driver-gain-localization, but the draft should name those interfaces at the two places where it says “free propagation” (lines 135, 142) instead of leaving it to the reader.

3. **Young-to-ordinary exchange glosses the Young estimate.** Lines 89–95 replace the Young integral by an ordinary strong integral using only “modulus of continuity of V.” The prerequisite that C(r)=S(−r)B_R,n(r)S(r) and V(r)=U(r,s)S(−s)e are both C^θ with θ>1/2 (from the fixed driver parameters and P:constant-young-linear) is not restated in Lemma A. It is supplied by the imports, but the lemma should state the θ>1/2 hypothesis once.

4. **Triangle−supremum measurability of D depends on joint strong continuity.** Proposition C needs sup over the uncountable triangle of an operator norm to be W-measurable. The draft correctly offers the fallback: strong state continuity plus a countable dense unit sphere and rational time pairs. This requires *joint* strong continuity of P(t,s) in (s,t); P:constant-gaussian-flow supplies “strong continuity on states,” and the composition S_F(t)U_A(t,s)S_F(−s) with U_A norm-continuous makes it joint, but the draft should state “joint” explicitly to forestall the objection that only separate continuity was imported.

5. **Multiplier-norm constant at line 84.** “||B_R,n(r)||_B(E) ≤ ||b_R,n(r)||_∞, up to the fixed Sobolev norm convention” is asserted without the finite multiplier constant. It is true because b_R,n has bounded spatial derivatives on the horizon (input 3/C2), and only an ever-finite K is used later, so this is a presentation gap, not an error.

6. **Local–global cutoff fact in O3.** The step `e = D_ψ_M z ∈ E` for z∈E_local uses the standard fact that a smooth compact multiplier sends H^±1/2_loc into H^±1/2. The surrounding L:constant-phase-free proof establishes boundedness of multiplication on E, but the draft should add one sentence citing local membership to close O3.

7. **Named source-paper results are inputs, not re-proved.** The draft correctly disclaims independent verification of the source papers; I audited their declared interfaces and found no mismatch with the uses made here. This is a limitation to record, not a defect of the draft.

## Checked derivations

- **P01 — original model, same retaining source, raw W.** Pass. proof.md lines 25–54 route through P:actual-operator-driver/P:constant-phase-driver/P:constant-gaussian-flow on the original W probability space, and the single source field Y_n=ℐ(v_{ρ_n;t,x}) has no (R,T) index (C1), so the same realization is used for every mask/horizon. Raw flows are W-measurable; source fields are on the retaining extension but never claimed W-measurable.
- **P02 — closed E restriction, invariance, compression, strong triangle measurability.** Pass. Lemma A (lines 65–79) uses A i = i M_E, π_C A = 0, S_F(t) i = i S(t), and π_C U = π_C to preserve iE; the restriction inequality ||Q|E−Q′|E|| ≤ ||Q−Q′|| is correct because iE carries the induced norm; restriction is a bounded linear map on the invariant subspace and transfers strong triangle measurability/moments from the F flow.
- **P03 — all-state/all-initial-time ordinary Duhamel.** Pass. Lemma A derives (A1) for every e∈E and every 0≤s≤t≤T from the source primitive (input 3/P:source-ordinary-response) via the Young-to-strong-integral exchange, then re-verifies by the bounded-coefficient Picard series. It is not inferred only from data (1,0).
- **P04 — strong Picard series/uniqueness without norm continuity of S.** Pass. Lines 103–119 use only strong continuity, the local bound C_T, and the factorial bound ||Q_k(t,s)|| ≤ C_T(C_T K T)^k/k!, giving uniform triangle operator-norm convergence; uniqueness follows by iterating the homogeneous difference to (C_T K T)^k/k! → 0. No operator-norm derivative of the free group is assumed.
- **P05 — inflated backward-cone support induction, both components, exact cutoffs.** Pass. The inflated balls K_r = B_(2j+1+t−r) with guard R,N ≥ 2j+T+3 ≥ (2j+1+T)+2 are correct: masks/cutoffs are 1 on every K_r, the base-case difference vanishes on K_r by free propagation, and the forcing difference vanishes on K_r; K_v enlarged by v−r is exactly K_r. The argument treats the full phase distribution, hence “includes velocity, not only displacement.” Exact margin (2 units) is respected.
- **P06 — raw zero-expectation transfer on extension, original W-measurable event.** Pass. Proposition C’s triangle inequality is term-by-term correct; the middle ordinary-source difference is zero by Lemma B; E_original D = E_extension D holds because D is a W-measurable pullback; both flanking errors vanish by input 4. D is genuinely W-measurable (with the measurability caveat in Noncritical finding 4).
- **P07 — source horizon uniqueness, raw source-limit uniqueness, countable universal quantifiers.** Pass. Lemma B’s horizon restriction uses ordinary uniqueness of Lemma A with the same time field on both horizons. Proposition C then bounds the shorter-triangle raw difference by the two source-to-raw errors and gets E D′=0. Only countably many integer tuples (j,T,R1,R2,N1,N2,T1≤T2) are intersected; a zero operator-triangle sup covers all states/real times, so no uncountable intersection is introduced.
- **P08 — local initial-data consequence, scaffold-only scope.** Pass. Choosing integer M > 2 max(N1,N2) makes ψ_M = 1 on neighbourhoods of both data-cutoff supports, so e = D_ψ_M z ∈ E and D_ψ_Ni e = D_ψ_Ni z; applying Proposition C to e proves the tested O3 identity without feeding z into a global operator. The draft explicitly refrains from claiming the local Fréchet flow/composition law (lines 204–212).
- **P09 — input fidelity, nonvacuity, zero-covariance/finite-norm guards.** Pass. One mask m_R (not its square), the Γ=0 free reduction (line 200), finite per-tuple cutoff norms (lines 172–173), and the three falsification guards (same realization not same law; full-cone not terminal-only; operator-norm not merely strong) are all respected.
- **P10 — defects/repairs/limitations.** Pass (with the repair list below). No critical defect; the named external paper interfaces match their declared roles, and no point trace, C2 asymptotics, novelty, or Lean claim is required or made.

## Required fixes before production gate

1. **Lemma B:** state explicitly that the “regular source sample” is taken from the countable intersection of Lemma A’s all-state events over the two masks (and both horizons for the horizon argument), and that the ordinary series/uniqueness from Lemma A hold there.
2. **Lemma B:** name L:constant-phase-free/L:driver-gain-localization at each “free propagation” step, and note that smooth-multiplier multiplication preserves the vanishing-on-K_r property for both the coefficient-difference term and the state-difference term, in both phase components (distributional).
3. **Lemma A:** restate the fixed parameter condition θ>1/2 from the driver parameters and the C^θ character of C and V before replacing the Young integral by the ordinary strong integral (lines 89–95).
4. **Proposition C:** make the measurability of D explicit as joint strong continuity of P(t,s) in (s,t) plus a countable dense unit sphere and rational time pairs (or cite the construction’s uniform-triangle strong measurability), so the uncountable sup is a countable supremum of measurable variables.
5. **Lemma A line 84:** replace the “up to the fixed Sobolev norm convention” phrase with the explicit finite K = C_k sup_r ||b_R,n(r)||_{C^k} (from input 3 derivative bounds), so the Picard constant K is visibly finite.
6. **O3 consequence:** add the one-sentence standard fact that a C_c^∞ multiplier sends H^±1/2_loc to H^±1/2, so D_ψ_M z ∈ E is justified, citing the multiplier-boundedness argument already present in L:constant-phase-free.
7. **Scope note:** retain the explicit statement that the named Gaussian/source/free-group results are imported inputs and that the PaperDev-Tailored-Workflow.md excerpt was unavailable in the review snapshot.

## One-line summary

The added Lemmas A/B and Proposition C are mathematically sound given the declared construction inputs: signs, boundary supports, guards, constants, expectation transfer, measurable-event bookkeeping, and the local cutoff consequence all check out, with only a handful of interface-explicitness/continuity repairs needed before production.