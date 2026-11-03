# Author factual checks on the same-lineage completion

Read-only input: `stratonovich-main-four-closures-math-packet-v2/completion/native/report.json`. These are author factual/normalization findings, not a new review or request for a confidence change. The original203 rows and completion are retained immutable. No further provider action is proposed.

## 1. PROOF169 erratum retains a false parenthesis

JSON pointer `/factual_errata/14/correct_deduction` correctly distinguishes the compensated identity D_φm=H_m,E from the uncompensated identity E[M_mW(i_IΦ)]=δ^(a/2)H_m,E. But it then says:

    “the driver amplitude g_delta times the a/2 temporal Jacobian
     gives delta^{a/2}; the sqrt(delta) appears only in the raw125/148 covariance”

This parenthesis is false. Since g_δ=δ^((1−a)/2), the product g_δδ^(a/2)=δ^(1/2). The unscaled M_m covariance has factor δ^(a/2) precisely because M_m does NOT include g_δ. The scaled X_m=g_δM_m covariance has √δ, including source155 and173 as well as148/125. Source `integrated_symplectic_phase.tex:285,298` sets φ_m=δ^(−a/2)T_m*i_IΦ and D_φm=H_m,E; its unscaled-covariance equation follows by dividing the scaled identity by g_δ. For a=1/2 and δ=1/16, g_δ=1/2 and δ^(a/2)=1/2; their product is1/4=√δ, not1/2. The main compensated/uncompensated formulas in the erratum are correct; replace only the erroneous explanatory parenthesis.

## 2. The I_η calibration substitutes α at the wrong scale

Pointer `/calibration_and_finite_checks/worked_scope/6` says I_η=Beta(1/2,1−α/2). Actual new `independent-upper-full-closure.txt:58–61` sets η=α/2 and

    I_η=∫₀∞ s^(−1/2)(1+s)^((η−3)/2)ds
       =Beta(1/2,1−η/2)=Beta(1/2,1−α/4).

With u=s/(1+s), the integrand becomes u^(−1/2)(1−u)^(−η/2)du, proving the displayed beta parameter directly. The abstract source complex-phase lemma at `notes_stratonovich_ham_second_moment.tex:5052` uses the same integral with an abstract exponent a; in this application that abstract exponent is η=α/2, not temporal α₀ and not spatial α. The completion's beta expression is therefore a factual calibration error. It does not alter the actual source/supplement integral, and both expressions happen to be finite on the admissible range; finiteness alone does not make them equal.

## 3. C23 application at036 is quartic (1.5), not square-root (1.4)

Pointer `/source_fidelity/2/hypotheses_checked` says C23 is used “only for the square-root variational finiteness at036.” The supplied primary text `carrier/primary/chen-2023-actual-import-contexts.txt`, EJP28(2023), paper119, printed page2, contains BOTH distinct functionals in Theorem1.1:

    (1.4): sup_unit-H¹ { Q(g)^(1/2) − ||∇g||²/2 },
    (1.5): sup_unit-H¹ { Q(g)       − ||∇g||²/2 },

and states both finite. Actual036, `notes_stratonovich_ham_second_moment.tex:4676–4685`, explicitly imports the closing-sentence finiteness for the variation in (1.5), restricted initially to real unit-L² Schwartz g. That gives Q(g)≤||∇g||²/2+C₀ and hence the homogeneous quartic bound for general Schwartz f. Only after this import does it prove the two different Cauchy inequalities and strong approximation identifying the full H¹ physical and spectral energies. Replacing that input by the square-root finiteness would not yield the stated quartic bound by the same immediate deduction. The source036 pinpoint is correct; the completion's source-use description needs correction. This is not a demand to identify other energy domains or to reprove all of C23.

## 4. PROOF174 original hash typo was not acknowledged

Pointer `/metadata_errata/6` labels the reported value as the correct map hash and says “no reproducible mismatch reproduced here.” The immutable original row in `native/exact-complete-proof-row-prefix.json` actually contains

    returned: 667115a04ac09d63cf1e2c4e1c1d70c01d388a402837584e4caaa9cc0ab2adf4
    map/body: 667115a04ac09d63cf1e2e4c1e1d70c01d388a402837584e4caaa9cc0ab2adf4

The mismatch c versus e in the prefix is reproducible from those original bytes. The completion keeps the correct map value, which is appropriate, but its assertion about the original reported value is false. An external composite/errata record should preserve the original row and acknowledge this one-character transcription error. Neither the typo nor its correction is evidence of proof-body reading or a mathematical defect.

These four findings leave the full original-goal scope and every declared reconstruction limit intact. They do not justify a new vote, an automatic current-lineage call, a forced grade or any whole/image/cold clearance.

## Custody

- `stratonovich-main-four-closures-math-packet-v2/completion/native/report.json`: SHA256 `c89193bed6d7f4cd996f5a0787b6e4d842f3f62dce853f551c7ed46f80e39509`.
- `stratonovich-main-four-closures-math-packet-v2/native/exact-complete-proof-row-prefix.json`: SHA256 `9179019e494e8c127b1421abbf97cdd0fc7fa72c30f085719c43a0bf5d91024d`.
- `stratonovich-main-four-closures-math-packet-v2/carrier/primary/chen-2023-actual-import-contexts.txt`: SHA256 `1f41ba86fb992470f71d8034155a2a1a3fdfa214bfe10e70035d130a00527f94`.
