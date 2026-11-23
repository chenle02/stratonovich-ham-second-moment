# Verification ledger

One row per numbered theorem, proposition, lemma, corollary and no-go result of the manuscript, in document order.

## How to use this ledger

- **Label** is the LaTeX label of the result. It is the stable key of the row; numbers may change between revisions, labels do not.
- **Kind** and **Title** are copied from the LaTeX source (TeX commands stripped for readability; math kept in `$...$`).
- **File** is the source file, relative to the manuscript repository, that contains the statement.
- **AI review** points to the record of automated model reviews. An AI review grade is a triage signal, not a proof and not a sign-off.
- **Lean** says what the Lean companion checks for this result (legend below). A Lean entry never certifies the analytic inputs.
- **Human** records sign-offs by mathematicians: `unchecked`, `checked by @name (PR #n)`, or `disputed (issue #n)`.
- **To sign off**, open a pull request that changes exactly one row and states in its description what you checked (statement, proof, cited inputs and their hypotheses) and what you did not check.
- **To dispute** a result, open an issue naming the label and the step in question; the row then becomes `disputed (issue #n)` until the issue is resolved.
- A row moves from `disputed` back to `checked` only through a new pull request that links the closed issue.

## Proof groups

For credit (see `CONTRIBUTING.md`), the results fall into five groups:
four proof groups and the obstructions of Chapter 12.
- **Groups are defined by chapter.** The first and last labels below are
  the current anchors in document order. A result added later belongs to
  the group of the chapter that contains it.
- **What a check covers.** A complete check of a group means every row of
  the group, read line by line. Results from other groups may be used as
  given, cited by label.
- **Cited results.** The rows that restate a cited source (`T:first`,
  `T:crude`) are checked against the source's statement, not reproved.

| Group | Chapters (chapter labels) | Scope | Rows | First label | Last label | Source size |
|---|---|---|---:|---|---|---:|
| I. Setting, construction and the independent upper bound | 1–3 (`S:book-setting`, `S:G0`, `S:book-independent-upper`) | the expansion, two-chain estimates and cross terms; the upper bound at scale $t^\kappa$ (`T:full-upper`, stated as `T:intro-upper`) | 31 | `T:first` | `T:full-upper` | ≈5,400 lines |
| II. Gaussian approximation and the lower bound | 4–7 (`S:book-gaussian-foundations`, `S:book-operator-paths`, `S:book-wave-evolution`, `S:book-lower`) | covariance estimates and Gaussian approximation; the original noise and operator paths; fixed masks and wave evolution; scaling and the point lower bound | 72 | `P:masked-spectral-growth` | `P:variational-positive-scores` | ≈6,900 lines |
| III. Matching upper bound and the constant | 8–11 (`S:book-means`, `S:book-growing-radius`, `S:book-point-upper`, `S:book-constant`) | spatial controls and Gaussian means; bounds as the radius grows; the point upper bound; identification of the constant (`T:intrinsic-second-moment`, stated as `T:intro-second-moment`) and its consequences | 82 | `L:equilibrium-gamma-beta` | `C:white-relative-width` | ≈6,700 lines |
| IV. Appendices | A–D (`S:appendix-finite-order`, `S:appendix-direct`, `S:appendix-covariance`, `S:appendix-static-clock`) | finite-order calculations; direct upper bounds and static interpolation; covariance comparisons in higher dimensions; static comparisons and the clock obstruction | 35 | `P:white-four` | `P:clock-copy-obstruction` | ≈4,400 lines |
| V. Obstructions | 12 (`S:book-no-go`) | the numbered no-go results: routes that fail, counterexamples and obstructions, each with its proof and its scope | 33 | `P:nogo-01` | `P:nogo-33` | ≈2,500 lines |

The five groups have 253 rows in total (31 + 72 + 82 + 35 + 33). The Group column of the results table gives each row's group. Row counts are those of this ledger; source sizes count the TeX lines of each chapter and its included files at development revision `7e81252` of the private development repository (figure drawings are not counted). The introduction theorems `T:intro-upper` and `T:intro-second-moment` restate `T:full-upper` (group I) and `T:intrinsic-second-moment` (group III); they are rows of group I, where they are stated, and checking them means checking that they agree with the theorems they restate.

## Lean column legend

- `formalized in full`: the result's conclusions are proved in Lean under the manuscript's own hypotheses (sometimes through an exact-hypothesis wrapper of a more general Lean theorem). The setting `H:homog` is modelled in Lean.
- `formalized, narrower conclusion`: as above, but Lean proves only part of the conclusion; the companion's `coverage.yaml` row says which part.
- `every conclusion, inputs supplied`: every conclusion is proved in Lean, with the named analytic inputs entering as explicit hypotheses.
- `steps checked`: Lean checks steps, parts or a narrower form of the result; analytic and probabilistic facts either enter as explicit hypotheses or stay outside Lean. The result itself is not checked.
- `outside Lean`: recorded in the companion's coverage file but not formalized (two of the four main theorems; the SPDE, stochastic integrals and analytic asymptotics are outside Lean).
- `no Lean claim`: no Lean declaration is mapped to this label.
- The count in brackets is the number of companion claims mapped to the row. A Lean entry never certifies the analytic inputs, and it is AI-checked correspondence, not human verification.

## Results

| Label | Group | Kind | Title | File | AI review | Lean | Human |
|---|---|---|---|---|---|---|---|
| `T:first` | I | Theorem | [chen:author2026:time-dependency, Theorem 1.2, (1.10)–(1.13)] | `notes/notes_stratonovich_ham_second_moment.tex` | see review record | no Lean claim | unchecked |
| `T:crude` | I | Theorem | [chen:author2026:time-dependency, Remark 5.1, (5.8)] | `notes/notes_stratonovich_ham_second_moment.tex` | see review record | no Lean claim | unchecked |
| `P:Jensen` | I | Proposition | Jensen lower bound | `notes/notes_stratonovich_ham_second_moment.tex` | see review record | no Lean claim | unchecked |
| `T:intro-upper` | I | Theorem | Upper bound at the correct scale | `notes/notes_stratonovich_ham_second_moment.tex` | see review record | no Lean claim | unchecked |
| `T:intro-second-moment` | I | Theorem | Second-moment limit | `notes/notes_stratonovich_ham_second_moment.tex` | see review record | no Lean claim | unchecked |
| `P:mixed` | I | Proposition | Mixed terms | `notes/notes_stratonovich_ham_second_moment.tex` | see review record | formalized in full (51 Lean claims) | unchecked |
| `L:white-test` | I | Lemma | White-space test | `notes/notes_stratonovich_ham_second_moment.tex` | see review record | formalized in full (18 Lean claims) | unchecked |
| `L:damped-homogeneous-norms` | I | Lemma | Homogeneous damped norms and temporal tails | `notes/notes_stratonovich_ham_second_moment.tex` | see review record | formalized in full (68 Lean claims) | unchecked |
| `L:translated-covariance-CS` | I | Lemma | Translated covariance Cauchy–Schwarz | `notes/notes_stratonovich_ham_second_moment.tex` | see review record | formalized in full (26 Lean claims) | unchecked |
| `L:pairing-product-envelope` | I | Lemma | Pairing product envelope | `notes/notes_stratonovich_ham_second_moment.tex` | see review record | formalized in full (84 Lean claims) | unchecked |
| `L:spatial-wick-measures` | I | Lemma | Positive spatial Wick-measure limit | `notes/notes_stratonovich_ham_second_moment.tex` | see review record | formalized in full (80 Lean claims) | unchecked |
| `L:joint-fixed-order` | I | Lemma | Joint diagram limits and fixed-order construction | `notes/notes_stratonovich_ham_second_moment.tex` | see review record | formalized in full (86 Lean claims) | unchecked |
| `L:crude-corrected` | I | Lemma | Corrected crude estimate | `notes/notes_stratonovich_ham_second_moment.tex` | see review record | formalized in full (65 Lean claims) | unchecked |
| `L:vertex-crude` | I | Lemma | Uniform vertexwise regularization bound | `notes/notes_stratonovich_ham_second_moment.tex` | see review record | formalized in full (18 Lean claims) | unchecked |
| `P:mild-construction` | I | Proposition | Mild construction from the fixed-order limits | `notes/notes_stratonovich_ham_second_moment.tex` | see review record | formalized in full (87 Lean claims) | unchecked |
| `P:envelope` | I | Proposition | The uniform pairing estimate | `notes/notes_stratonovich_ham_second_moment.tex` | see review record | formalized in full (69 Lean claims) | unchecked |
| `L:phase-contractions` | I | Lemma | Two static contraction bounds | `notes/notes_stratonovich_ham_second_moment.tex` | see review record | formalized in full (37 Lean claims) | unchecked |
| `P:static-phase-variance` | I | Proposition | First variance estimate for arbitrary phase | `notes/notes_stratonovich_ham_second_moment.tex` | see review record | no Lean claim | unchecked |
| `L:complex-phase` | I | Lemma | A complex phase bound | `notes/notes_stratonovich_ham_second_moment.tex` | see review record | steps checked (52 Lean claims) | unchecked |
| `L:fock-form` | I | Lemma | Gaussian cutoff form bound | `notes/notes_stratonovich_ham_second_moment.tex` | see review record | formalized, narrower conclusion (64 Lean claims) | unchecked |
| `L:finite-word-cutoff` | I | Lemma | Exact cutoffs for finite Gaussian words | `notes/notes_stratonovich_ham_second_moment.tex` | see review record | formalized in full (30 Lean claims) | unchecked |
| `P:static-phase-all-orders` | I | Proposition | All regularized static phase orders | `notes/notes_stratonovich_ham_second_moment.tex` | see review record | steps checked (29 Lean claims) | unchecked |
| `C:static-interaction` | I | Corollary | Summable static interaction bounds | `notes/notes_stratonovich_ham_second_moment.tex` | see review record | steps checked (26 Lean claims) | unchecked |
| `L:interval-contractions` | I | Lemma | Dimension-independent Gaussian contractions | `notes/notes_stratonovich_ham_second_moment.tex` | see review record | formalized, narrower conclusion (27 Lean claims) | unchecked |
| `L:interval-complex` | I | Lemma | Complex sums and changing phase weights | `notes/notes_stratonovich_ham_second_moment.tex` | see review record | steps checked (15 Lean claims) | unchecked |
| `L:inventory-product` | I | Lemma | A coefficient bound for a product with nonnegative coefficients | `notes/notes_stratonovich_ham_second_moment.tex` | see review record | formalized in full (11 Lean claims) | unchecked |
| `L:fixed-split` | I | Lemma | A fixed degree-split estimate | `notes/notes_stratonovich_ham_second_moment.tex` | see review record | steps checked (72 Lean claims) | unchecked |
| `P:interval-coefficients` | I | Proposition | Uniform interval coefficients | `notes/notes_stratonovich_ham_second_moment.tex` | see review record | steps checked (26 Lean claims) | unchecked |
| `L:terminal-wick` | I | Lemma | The finite terminal-chain Wick formula | `notes/notes_stratonovich_ham_second_moment.tex` | see review record | formalized in full (65 Lean claims) | unchecked |
| `L:uniform-series-tail` | I | Lemma | Uniform series tails from scaled moments | `notes/notes_stratonovich_ham_second_moment.tex` | see review record | formalized in full (13 Lean claims) | unchecked |
| `T:full-upper` | I | Theorem | Full upper scale | `notes/notes_stratonovich_ham_second_moment.tex` | see review record | outside Lean | unchecked |
| `P:masked-spectral-growth` | II | Proposition | Translated spectral mass | `notes/integrated_covariance_foundation.tex` | see review record | formalized in full (9 Lean claims) | unchecked |
| `P:masked-auxiliary-norm` | II | Proposition | Auxiliary mask norm | `notes/integrated_covariance_foundation.tex` | see review record | formalized in full (31 Lean claims) | unchecked |
| `L:masked-time-completion` | II | Lemma | Temporal covariance completion | `notes/integrated_covariance_foundation.tex` | see review record | formalized in full (23 Lean claims) | unchecked |
| `P:masked-noise-completion` | II | Proposition | Completion on the same noise | `notes/integrated_covariance_foundation.tex` | see review record | steps checked (2 Lean claims) | unchecked |
| `P:masked-quotient-obstruction` | II | Proposition | A physical mask need not preserve noise-null tests | `notes/integrated_covariance_foundation.tex` | see review record | formalized, narrower conclusion (27 Lean claims) | unchecked |
| `L:masked-temporal-modulation` | II | Lemma | Modulated amplitudes | `notes/integrated_covariance_foundation.tex` | see review record | formalized in full (7 Lean claims) | unchecked |
| `L:masked-trig-products` | II | Lemma | Correlated trigonometric products | `notes/integrated_covariance_foundation.tex` | see review record | formalized in full (21 Lean claims) | unchecked |
| `L:masked-continuous-wave` | II | Lemma | Continuous sine factors | `notes/integrated_covariance_foundation.tex` | see review record | formalized in full (6 Lean claims) | unchecked |
| `P:frequency-row` | II | Proposition | Uniform scalar row | `notes/integrated_wave_variance.tex` | see review record | formalized in full (8 Lean claims) | unchecked |
| `C:frequency-time` | II | Corollary | A time exponent above one half | `notes/integrated_wave_variance.tex` | see review record | formalized in full (3 Lean claims) | unchecked |
| `P:actual-wave-form` | II | Proposition | Form and phase kernel | `notes/integrated_wave_variance.tex` | see review record | steps checked (4 Lean claims) | unchecked |
| `L:phase-bessel` | II | Lemma | Hilbert-valued finite Bessel inequality | `notes/integrated_wave_variance.tex` | see review record | formalized in full (3 Lean claims) | unchecked |
| `P:wave-two-variances` | II | Proposition | Both variance directions | `notes/integrated_wave_variance.tex` | see review record | steps checked (14 Lean claims) | unchecked |
| `P:wave-square-columns` | II | Proposition | Column and adjoint-column maps | `notes/integrated_wave_variance.tex` | see review record | no Lean claim | unchecked |
| `L:gaussian-scalar-powers` | II | Lemma | Scalar power estimates | `notes/integrated_compact_gaussian.tex` | see review record | formalized in full (5 Lean claims) | unchecked |
| `L:gaussian-trace-bounds` | II | Lemma | Two Hermitian trace bounds | `notes/integrated_compact_gaussian.tex` | see review record | formalized in full (7 Lean claims) | unchecked |
| `P:finite-gaussian-matrix` | II | Proposition | Finite Gaussian matrix moment | `notes/integrated_compact_gaussian.tex` | see review record | formalized in full (44 Lean claims) | unchecked |
| `L:cutoff-factorization` | II | Lemma | Cutoff factorization | `notes/integrated_compact_gaussian.tex` | see review record | no Lean claim | unchecked |
| `P:cutoff-singular-values` | II | Proposition | Whole-space cutoff singular values | `notes/integrated_compact_gaussian.tex` | see review record | no Lean claim | unchecked |
| `P:compact-two-envelopes` | II | Proposition | Both compact envelopes | `notes/integrated_compact_gaussian.tex` | see review record | no Lean claim | unchecked |
| `L:compact-positive-order` | II | Lemma | Compact positive order and trace | `notes/integrated_compact_gaussian.tex` | see review record | no Lean claim | unchecked |
| `P:localized-finite-variance` | II | Proposition | Localized finite variance bounds | `notes/integrated_compact_gaussian.tex` | see review record | no Lean claim | unchecked |
| `C:finite-gaussian-operators` | II | Corollary | Finite Gaussian operators | `notes/integrated_compact_gaussian.tex` | see review record | no Lean claim | unchecked |
| `P:cutoff-boundary-tests` | II | Proposition | Whole-space cutoff tests | `notes/integrated_compact_gaussian.tex` | see review record | no Lean claim | unchecked |
| `P:actual-operator-driver` | II | Proposition | Compact operator path on the original noise space | `notes/integrated_actual_operator_driver.tex` | see review record | no Lean claim | unchecked |
| `L:driver-noise-basis` | II | Lemma | Basis in the prescribed quotient | `notes/integrated_actual_operator_driver.tex` | see review record | no Lean claim | unchecked |
| `L:driver-covariance-coefficients` | II | Lemma | Covariance coefficients | `notes/integrated_actual_operator_driver.tex` | see review record | no Lean claim | unchecked |
| `L:driver-gain-localization` | II | Lemma | Deterministic coefficient operators | `notes/integrated_actual_operator_driver.tex` | see review record | no Lean claim | unchecked |
| `L:driver-actual-variances` | II | Lemma | Both variances and their tails | `notes/integrated_actual_operator_driver.tex` | see review record | no Lean claim | unchecked |
| `L:driver-dominated-tails` | II | Lemma | Compact domination of positive tails | `notes/integrated_actual_operator_driver.tex` | see review record | no Lean claim | unchecked |
| `L:driver-gaussian-tail-average` | II | Lemma | Retained finite Gaussian variance powers | `notes/integrated_actual_operator_driver.tex` | see review record | no Lean claim | unchecked |
| `L:driver-interval-limit` | II | Lemma | Fixed-interval operator construction | `notes/integrated_actual_operator_driver.tex` | see review record | steps checked (1 Lean claim) | unchecked |
| `L:driver-holder-limit` | II | Lemma | Hölder path limit | `notes/integrated_actual_operator_driver.tex` | see review record | steps checked (2 Lean claims) | unchecked |
| `L:source-finite-comparison` | II | Lemma | Finite Gaussian linear images | `notes/integrated_source_convergence.tex` | see review record | formalized in full (10 Lean claims) | unchecked |
| `P:source-gaussian-transfer` | II | Proposition | Gaussian transfer and stability | `notes/integrated_source_convergence.tex` | see review record | no Lean claim | unchecked |
| `L:source-spatial-heat` | II | Lemma | Original spatial space and heat | `notes/integrated_source_convergence.tex` | see review record | formalized in full (35 Lean claims) | unchecked |
| `L:source-retaining-isometry` | II | Lemma | Feature isometry preserving the given noise | `notes/integrated_source_convergence.tex` | see review record | no Lean claim | unchecked |
| `P:source-canonical-convergence` | II | Proposition | Canonical sources on the extended space containing the given noise | `notes/integrated_source_convergence.tex` | see review record | no Lean claim | unchecked |
| `L:source-pointfield-regularity` | II | Lemma | Regularity for each fixed cutoff | `notes/integrated_source_convergence.tex` | see review record | no Lean claim | unchecked |
| `P:source-ordinary-response` | II | Proposition | Ordinary source response | `notes/integrated_source_convergence.tex` | see review record | no Lean claim | unchecked |
| `L:masked-chain-comparison` | II | Lemma | Chains and mixed-order comparison | `notes/integrated_masked_moments.tex` | see review record | no Lean claim | unchecked |
| `P:masked-source-moments` | II | Proposition | Ordinary solutions and tested moments | `notes/integrated_masked_moments.tex` | see review record | no Lean claim | unchecked |
| `P:masked-canonical-transfer` | II | Proposition | Canonical point-moment limit and conditional transfer | `notes/integrated_masked_moments.tex` | see review record | no Lean claim | unchecked |
| `L:constant-phase-free` | II | Lemma | Constants and finite propagation | `notes/integrated_constant_phase_young.tex` | see review record | no Lean claim | unchecked |
| `P:constant-phase-driver` | II | Proposition | Extended operator path | `notes/integrated_constant_phase_young.tex` | see review record | no Lean claim | unchecked |
| `L:constant-source-response` | II | Lemma | Ordinary response on all of $F$ | `notes/integrated_constant_phase_young.tex` | see review record | no Lean claim | unchecked |
| `P:constant-young-linear` | II | Proposition | Linear Young evolution | `notes/integrated_constant_phase_young.tex` | see review record | no Lean claim | unchecked |
| `P:constant-gaussian-flow` | II | Proposition | Gaussian Young and physical flows | `notes/integrated_constant_phase_young.tex` | see review record | no Lean claim | unchecked |
| `L:constant-source-solution` | II | Lemma | Identification with the ordinary source equation | `notes/integrated_constant_phase_young.tex` | see review record | no Lean claim | unchecked |
| `P:constant-raw-average` | II | Proposition | Original average and original point moment | `notes/integrated_constant_phase_young.tex` | see review record | no Lean claim | unchecked |
| `P:constant-compact-base` | II | Proposition | Compact deterministic base | `notes/integrated_constant_phase_young.tex` | see review record | no Lean claim | unchecked |
| `P:compact-ground-family` | II | Proposition | Ground states and a uniform rate gap | `notes/integrated_compact_mean_family.tex` | see review record | no Lean claim | unchecked |
| `L:compact-fractional-phase` | II | Lemma | Uniform fractional phase norms | `notes/integrated_compact_mean_family.tex` | see review record | no Lean claim | unchecked |
| `P:compact-E-wave` | II | Proposition | The complementary wave on $E$ | `notes/integrated_compact_mean_family.tex` | see review record | no Lean claim | unchecked |
| `P:compact-F-projection` | II | Proposition | The growing projection on the wave phase space | `notes/integrated_compact_mean_family.tex` | see review record | no Lean claim | unchecked |
| `P:compact-F-complement` | II | Proposition | Complementary wave evolution and parameter dependence | `notes/integrated_compact_mean_family.tex` | see review record | no Lean claim | unchecked |
| `L:compact-raw-profile` | II | Lemma | The original mean and variance | `notes/integrated_compact_mean_family.tex` | see review record | no Lean claim | unchecked |
| `P:compact-original-common-trial` | II | Proposition | Binding with the original control and cost fixed | `notes/integrated_compact_mean_family.tex` | see review record | no Lean claim | unchecked |
| `L:exact-canonical-scaling` | II | Lemma | Canonical law scaling | `notes/integrated_exact_scaling.tex` | see review record | steps checked (3 Lean claims) | unchecked |
| `L:raw-block-inputs` | II | Lemma | Coupled Gaussian block inputs | `notes/integrated_raw_block_lower.tex` | see review record | steps checked (1 Lean claim) | unchecked |
| `P:raw-block-gaussian-law` | II | Proposition | Change of law on the whole norm-Borel space | `notes/integrated_raw_block_lower.tex` | see review record | no Lean claim | unchecked |
| `L:raw-block-uniform-error` | II | Lemma | Uniform block error | `notes/integrated_raw_block_lower.tex` | see review record | no Lean claim | unchecked |
| `L:raw-block-indexed-cone` | II | Lemma | Indexed cone and terminal displacement | `notes/integrated_raw_block_lower.tex` | see review record | steps checked (22 Lean claims) | unchecked |
| `L:raw-block-restart` | II | Lemma | Composition over time blocks and regularized products | `notes/integrated_raw_block_lower.tex` | see review record | steps checked (1 Lean claim) | unchecked |
| `P:raw-block-point-comparison` | II | Proposition | The square observable and canonical comparison | `notes/integrated_raw_block_lower.tex` | see review record | no Lean claim | unchecked |
| `P:raw-block-original-lower` | II | Proposition | Original point lower rate at the Gaussian quadratic cost | `notes/integrated_raw_block_lower.tex` | see review record | steps checked (1 Lean claim) | unchecked |
| `L:variational-heat-envelope` | II | Lemma | Gaussian envelope for the original covariance | `notes/integrated_unmasked_variational.tex` | see review record | formalized in full (6 Lean claims) | unchecked |
| `L:variational-global-mean` | II | Lemma | Global regularity of the original mean | `notes/integrated_unmasked_variational.tex` | see review record | formalized in full (13 Lean claims) | unchecked |
| `P:variational-unmasked-rate` | II | Proposition | The unmasked Rayleigh rate | `notes/integrated_unmasked_variational.tex` | see review record | formalized, narrower conclusion (6 Lean claims) | unchecked |
| `P:variational-remove-mask` | II | Proposition | Monotone rates and the original point moment | `notes/integrated_unmasked_variational.tex` | see review record | steps checked (23 Lean claims) | unchecked |
| `L:variational-control-dilation` | II | Lemma | Radon and Rayleigh dilation | `notes/integrated_unmasked_variational.tex` | see review record | formalized, narrower conclusion (22 Lean claims) | unchecked |
| `P:variational-positive-scores` | II | Proposition | Intrinsic variational lower bounds | `notes/integrated_unmasked_variational.tex` | see review record | formalized, narrower conclusion (18 Lean claims) | unchecked |
| `L:equilibrium-gamma-beta` | III | Lemma | Gamma and Beta identities | `notes/integrated_temporal_equilibrium.tex` | see review record | formalized in full (7 Lean claims) | unchecked |
| `L:temporal-equilibrium` | III | Lemma | Exact potential and mass | `notes/integrated_temporal_equilibrium.tex` | see review record | formalized in full (13 Lean claims) | unchecked |
| `L:spatial-physical-pair` | III | Lemma | The physical two-point integral | `notes/integrated_spatial_occupation.tex` | see review record | formalized in full (3 Lean claims) | unchecked |
| `L:spatial-static-controls` | III | Lemma | Smooth temporal controls | `notes/integrated_spatial_occupation.tex` | see review record | formalized, narrower conclusion (36 Lean claims) | unchecked |
| `L:spatial-fourier-bound` | III | Lemma | Deterministic Fourier bound for the spatial energy | `notes/integrated_spatial_occupation.tex` | see review record | formalized in full (18 Lean claims) | unchecked |
| `P:spatial-smooth-ratio` | III | Proposition | The finite smooth spatial ratio | `notes/integrated_spatial_occupation.tex` | see review record | formalized, narrower conclusion (22 Lean claims) | unchecked |
| `P:spatial-four-linear` | III | Proposition | The physical four-linear extension | `notes/integrated_spatial_occupation.tex` | see review record | formalized in full (47 Lean claims) | unchecked |
| `P:spatial-energy-map` | III | Proposition | The spatial energy and static lower variational expression | `notes/integrated_spatial_occupation.tex` | see review record | formalized, narrower conclusion (10 Lean claims) | unchecked |
| `L:occupation-kernel-row` | III | Lemma | Exact row maximum | `notes/integrated_spatial_occupation.tex` | see review record | formalized in full (9 Lean claims) | unchecked |
| `P:occupation-physical-class` | III | Proposition | The full physical occupation class | `notes/integrated_spatial_occupation.tex` | see review record | formalized in full (24 Lean claims) | unchecked |
| `L:cameron-fractional-products` | III | Lemma | Fractional covariance products | `notes/integrated_cameron_mean.tex` | see review record | formalized in full (21 Lean claims) | unchecked |
| `P:cameron-spatial-map` | III | Proposition | Compact spatial mean map | `notes/integrated_cameron_mean.tex` | see review record | steps checked (25 Lean claims) | unchecked |
| `L:cameron-supported-tensor` | III | Lemma | Supported original tensor space | `notes/integrated_cameron_mean.tex` | see review record | no Lean claim | unchecked |
| `P:cameron-temporal-map` | III | Proposition | The compact temporal mean, without trace class | `notes/integrated_cameron_mean.tex` | see review record | formalized, narrower conclusion (60 Lean claims) | unchecked |
| `P:cameron-full-mean` | III | Proposition | The compact time-space mean | `notes/integrated_cameron_mean.tex` | see review record | formalized, narrower conclusion (9 Lean claims) | unchecked |
| `L:cameron-actual-residual` | III | Lemma | Supported residual paths | `notes/integrated_cameron_mean.tex` | see review record | no Lean claim | unchecked |
| `P:cameron-actual-embedding` | III | Proposition | Cameron covariance and averaged bound | `notes/integrated_cameron_mean.tex` | see review record | no Lean claim | unchecked |
| `L:young-upper-growth` | III | Lemma | Refined growth and uniform inverse control | `notes/integrated_young_upper_foundation.tex` | see review record | no Lean claim | unchecked |
| `P:young-upper-multiplicative` | III | Proposition | Multiplicative upper perturbation | `notes/integrated_young_upper_foundation.tex` | see review record | no Lean claim | unchecked |
| `L:uniform-mean-cutoff` | III | Lemma | Uniform cutoff and physical mean | `notes/integrated_uniform_mean.tex` | see review record | formalized, narrower conclusion (17 Lean claims) | unchecked |
| `L:uniform-mean-spatial-tails` | III | Lemma | Uniform heat and frequency tails | `notes/integrated_uniform_mean.tex` | see review record | no Lean claim | unchecked |
| `L:uniform-mean-tensor` | III | Lemma | Dimension-free Hilbert tensor extension | `notes/integrated_uniform_mean.tex` | see review record | formalized, narrower conclusion (8 Lean claims) | unchecked |
| `P:uniform-mean-regulator` | III | Proposition | Uniform approximation of the completed mean | `notes/integrated_uniform_mean.tex` | see review record | steps checked (21 Lean claims) | unchecked |
| `P:uniform-actual-cameron` | III | Proposition | Uniform-radius Cameron bound | `notes/integrated_uniform_mean.tex` | see review record | no Lean claim | unchecked |
| `L:radius-outer-maps` | III | Lemma | Uniform rescaled outer maps | `notes/integrated_radius_anchor.tex` | see review record | no Lean claim | unchecked |
| `P:radius-compact-envelopes` | III | Proposition | Radius-explicit compact envelopes | `notes/integrated_radius_anchor.tex` | see review record | no Lean claim | unchecked |
| `P:radius-actual-moments` | III | Proposition | Radius-explicit path moments | `notes/integrated_radius_anchor.tex` | see review record | no Lean claim | unchecked |
| `C:radius-covariance-residuals` | III | Corollary | Deterministic covariance residuals | `notes/integrated_radius_anchor.tex` | see review record | no Lean claim | unchecked |
| `P:radius-mean-anchor` | III | Proposition | Averaged block mean tends to zero | `notes/integrated_radius_anchor.tex` | see review record | steps checked (24 Lean claims) | unchecked |
| `L:signed-limiting-multiplier` | III | Lemma | The limiting multiplier | `notes/integrated_signed_static.tex` | see review record | no Lean claim | unchecked |
| `P:signed-closed-form` | III | Proposition | Closed form and quarter-power phase | `notes/integrated_signed_static.tex` | see review record | steps checked (16 Lean claims) | unchecked |
| `L:signed-spectral-wave` | III | Lemma | The bottom and spectral wave | `notes/integrated_signed_static.tex` | see review record | no Lean claim | unchecked |
| `P:signed-physical-wave` | III | Proposition | Identification with the physical wave | `notes/integrated_signed_static.tex` | see review record | no Lean claim | unchecked |
| `L:symplectic-free` | III | Lemma | Free wave form and compact Young baseline | `notes/integrated_symplectic_phase.tex` | see review record | steps checked (32 Lean claims) | unchecked |
| `L:symplectic-source-mean` | III | Lemma | Covariance means and source primitives | `notes/integrated_symplectic_phase.tex` | see review record | no Lean claim | unchecked |
| `P:symplectic-source` | III | Proposition | Source conservation | `notes/integrated_symplectic_phase.tex` | see review record | no Lean claim | unchecked |
| `P:symplectic-raw` | III | Proposition | Conservation, inverse and a lower norm bound | `notes/integrated_symplectic_phase.tex` | see review record | no Lean claim | unchecked |
| `P:symplectic-block-mean` | III | Proposition | The exact completed block mean | `notes/integrated_symplectic_phase.tex` | see review record | no Lean claim | unchecked |
| `P:tube-wiener-realization` | III | Proposition | First Wiener chaos realization on the support | `notes/integrated_gaussian_tubes.tex` | see review record | no Lean claim | unchecked |
| `L:tube-closed-geometry` | III | Lemma | Compact images and attained tube radii | `notes/integrated_gaussian_tubes.tex` | see review record | formalized, narrower conclusion (9 Lean claims) | unchecked |
| `P:tube-rayleigh-transfer` | III | Proposition | Comparison with the Rayleigh integral, including jumps and zero law | `notes/integrated_gaussian_tubes.tex` | see review record | every conclusion, inputs supplied (20 Lean claims) | unchecked |
| `P:tube-actual-law` | III | Proposition | Eligibility of the E law | `notes/integrated_gaussian_tubes.tex` | see review record | no Lean claim | unchecked |
| `L:tube-actual-endpoint` | III | Lemma | The endpoint functional | `notes/integrated_gaussian_tubes.tex` | see review record | no Lean claim | unchecked |
| `P:tube-coarse-envelope` | III | Proposition | Coarse tube envelope and operator moment | `notes/integrated_gaussian_tubes.tex` | see review record | no Lean claim | unchecked |
| `L:tube-rayleigh-tail` | III | Lemma | Exact Rayleigh tail bound | `notes/integrated_gaussian_tubes.tex` | see review record | formalized, narrower conclusion (6 Lean claims) | unchecked |
| `L:tube-half-action` | III | Lemma | Supremum with the Gaussian quadratic cost | `notes/integrated_gaussian_tubes.tex` | see review record | formalized in full (3 Lean claims) | unchecked |
| `L:uniform-E-lift` | III | Lemma | Unique potential and fixed-radius lift | `notes/integrated_uniform_products.tex` | see review record | formalized, narrower conclusion (28 Lean claims) | unchecked |
| `P:uniform-E-spectral` | III | Proposition | Spectral rate in E | `notes/integrated_uniform_products.tex` | see review record | no Lean claim | unchecked |
| `P:uniform-rate-averaging` | III | Proposition | Uniform completed-field averaging | `notes/integrated_uniform_products.tex` | see review record | no Lean claim | unchecked |
| `L:uniform-product-budgets` | III | Lemma | Explicit physical primitive and growth bounds | `notes/integrated_uniform_products.tex` | see review record | no Lean claim | unchecked |
| `P:uniform-mean-product` | III | Proposition | Finite-mesh physical mean-product bound | `notes/integrated_uniform_products.tex` | see review record | no Lean claim | unchecked |
| `C:uniform-polynomial-balls` | III | Corollary | Every polynomial control radius | `notes/integrated_uniform_products.tex` | see review record | no Lean claim | unchecked |
| `P:uniform-arbitrary-residual` | III | Proposition | Residual comparison and the integrated rate | `notes/integrated_uniform_products.tex` | see review record | no Lean claim | unchecked |
| `L:point-actual-finiteness` | III | Lemma | Restriction and fixed-parameter finiteness | `notes/integrated_point_transfer.tex` | see review record | no Lean claim | unchecked |
| `L:point-fast-sources` | III | Lemma | The same regularized fast noises preserving the given noise | `notes/integrated_point_transfer.tex` | see review record | no Lean claim | unchecked |
| `L:point-compact-source` | III | Lemma | Compact-data source identification | `notes/integrated_point_transfer.tex` | see review record | no Lean claim | unchecked |
| `P:point-source-cone` | III | Proposition | Cone identity and an average of squares | `notes/integrated_point_transfer.tex` | see review record | no Lean claim | unchecked |
| `P:original-point-transfer` | III | Proposition | Exact original point transfer and polynomial cost | `notes/integrated_point_transfer.tex` | see review record | no Lean claim | unchecked |
| `L:signed-score-envelope` | III | Lemma | Signed variational expression and quantitative radial envelope | `notes/integrated_signed_moment_upper.tex` | see review record | no Lean claim | unchecked |
| `P:signed-moment-bulk-tail` | III | Proposition | Finite-delta bulk and exact tail | `notes/integrated_signed_moment_upper.tex` | see review record | no Lean claim | unchecked |
| `P:signed-operator-upper` | III | Proposition | Two limits on the same moment | `notes/integrated_signed_moment_upper.tex` | see review record | no Lean claim | unchecked |
| `P:original-signed-point-upper` | III | Proposition | Pointwise upper bound from the signed variational expression | `notes/integrated_signed_moment_upper.tex` | see review record | no Lean claim | unchecked |
| `L:gram-scalar-algebra` | III | Lemma | Scalar and Hilbert identities | `notes/integrated_positive_gram.tex` | see review record | formalized in full (8 Lean claims) | unchecked |
| `L:gram-dual-minimum` | III | Lemma | Interior dual minimum | `notes/integrated_positive_gram.tex` | see review record | no Lean claim | unchecked |
| `P:gram-positive-optimizer` | III | Proposition | Positive conic maximizer | `notes/integrated_positive_gram.tex` | see review record | steps checked (1 Lean claim) | unchecked |
| `L:gram-realization` | III | Lemma | Real Gram realization | `notes/integrated_positive_gram.tex` | see review record | no Lean claim | unchecked |
| `P:gram-entrywise-comparison` | III | Proposition | Entrywise Gram comparison | `notes/integrated_positive_gram.tex` | see review record | steps checked (1 Lean claim) | unchecked |
| `L:positive-raw-embedding` | III | Lemma | Inclusion into the covariance space and the smooth mean | `notes/integrated_intrinsic_constant.tex` | see review record | formalized in full (42 Lean claims) | unchecked |
| `L:positive-physical-gram` | III | Lemma | Finite covariance vectors and entrywise order | `notes/integrated_intrinsic_constant.tex` | see review record | formalized, narrower conclusion (18 Lean claims) | unchecked |
| `L:positive-uniform-optimizer` | III | Lemma | Uniform optimizer norm and positive smoothing | `notes/integrated_intrinsic_constant.tex` | see review record | no Lean claim | unchecked |
| `P:positive-signed-comparison` | III | Proposition | Signed variational values bounded by the variational value over nonnegative controls | `notes/integrated_intrinsic_constant.tex` | see review record | no Lean claim | unchecked |
| `P:positive-score-cutoff` | III | Proposition | Cutoff removal for the optimized variational expression | `notes/integrated_intrinsic_constant.tex` | see review record | no Lean claim | unchecked |
| `T:intrinsic-second-moment` | III | Theorem | Intrinsic original second-moment constant | `notes/integrated_intrinsic_constant.tex` | see review record | outside Lean | unchecked |
| `L:occupation-raw-square` | III | Lemma | Full-profile squares in the original space | `notes/integrated_occupation_ceiling.tex` | see review record | formalized, narrower conclusion (27 Lean claims) | unchecked |
| `P:raw-occupation-energy` | III | Proposition | Original occupation energy and dilation | `notes/integrated_occupation_ceiling.tex` | see review record | formalized in full (33 Lean claims) | unchecked |
| `L:occupation-rayleigh-selection` | III | Lemma | Countable Rayleigh near-occupations | `notes/integrated_occupation_ceiling.tex` | see review record | formalized, narrower conclusion (7 Lean claims) | unchecked |
| `T:intrinsic-occupation-ceiling` | III | Theorem | The computed occupation ceiling | `notes/integrated_occupation_ceiling.tex` | see review record | formalized, narrower conclusion (26 Lean claims) | unchecked |
| `C:intrinsic-spatial-bracket` | III | Corollary | A common spatial-energy bracket | `notes/integrated_occupation_ceiling.tex` | see review record | formalized, narrower conclusion (19 Lean claims) | unchecked |
| `L:white-cdf-square` | III | Lemma | A square identity for the distribution function | `notes/integrated_white_evaluation.tex` | see review record | no Lean claim | unchecked |
| `P:white-spatial-energy` | III | Proposition | Exact white spatial energy | `notes/integrated_white_evaluation.tex` | see review record | steps checked (6 Lean claims) | unchecked |
| `T:white-moment-bounds` | III | Theorem | Explicit white moment bounds | `notes/integrated_white_evaluation.tex` | see review record | steps checked (25 Lean claims) | unchecked |
| `C:white-relative-width` | III | Corollary | Uniform relative width of the bound formulas | `notes/integrated_white_evaluation.tex` | see review record | formalized in full (12 Lean claims) | unchecked |
| `P:nogo-01` | V | No-go | The common-parameter majorant has the wrong scale | `notes/no-go/pairings.tex` | see review record | no Lean claim | unchecked |
| `P:nogo-02` | V | No-go | No uniform cubic factorial denominator per diagram | `notes/no-go/pairings.tex` | see review record | no Lean claim | unchecked |
| `P:nogo-03` | V | No-go | Failure of the all-time comparison with unit prefactor | `notes/no-go/pairings.tex` | see review record | no Lean claim | unchecked |
| `P:nogo-04` | V | No-go | Divergence of the first coefficient ratio | `notes/no-go/pairings.tex` | see review record | no Lean claim | unchecked |
| `P:nogo-05` | V | No-go | Support obstruction to pointwise concatenation | `notes/no-go/pairings.tex` | see review record | no Lean claim | unchecked |
| `P:nogo-06` | V | No-go | The geometry-free majorant | `notes/no-go/pairings.tex` | see review record | no Lean claim | unchecked |
| `P:nogo-07` | V | No-go | Large label span does not imply a cubic denominator | `notes/no-go/pairings.tex` | see review record | no Lean claim | unchecked |
| `P:nogo-10` | V | No-go | No finite spatial-supremum pullout in the merge lens | `notes/no-go/pairings.tex` | see review record | no Lean claim | unchecked |
| `P:nogo-17` | V | No-go | Constant-correlation clock copying misses a positive factor | `notes/no-go/pairings.tex` | see review record | no Lean claim | unchecked |
| `P:nogo-18` | V | No-go | The shift-erased envelope is not below the wave transform | `notes/no-go/pairings.tex` | see review record | no Lean claim | unchecked |
| `P:nogo-08` | V | No-go | A spatial maximum need not be finite | `notes/no-go/covariance.tex` | see review record | no Lean claim | unchecked |
| `P:nogo-09` | V | No-go | Radial lowering can destroy positive definiteness | `notes/no-go/covariance.tex` | see review record | no Lean claim | unchecked |
| `P:nogo-11` | V | No-go | A scalar wave moment is not log-convex in variance | `notes/no-go/covariance.tex` | see review record | no Lean claim | unchecked |
| `P:nogo-12` | V | No-go | Failure of a heat–Mellin endpoint recipe | `notes/no-go/covariance.tex` | see review record | no Lean claim | unchecked |
| `P:nogo-13` | V | No-go | No uniform isotropic envelope for a plane covariance | `notes/no-go/covariance.tex` | see review record | no Lean claim | unchecked |
| `P:nogo-19` | V | No-go | A positive semidefinite residual can lower the wave mean | `notes/no-go/covariance.tex` | see review record | no Lean claim | unchecked |
| `P:nogo-14` | V | No-go | Two independent wave blocks do not multiply scalar moments | `notes/no-go/phase.tex` | see review record | no Lean claim | unchecked |
| `P:nogo-15` | V | No-go | The first variance coefficient need not be nonnegative | `notes/no-go/phase.tex` | see review record | no Lean claim | unchecked |
| `P:nogo-16` | V | No-go | A deterministic surrogate can lose the annealed factor | `notes/no-go/phase.tex` | see review record | no Lean claim | unchecked |
| `P:nogo-20` | V | No-go | A positive control need not have proportional covariance profiles | `notes/no-go/phase.tex` | see review record | no Lean claim | unchecked |
| `P:nogo-31` | V | No-go | Growth does not give every-phase lower bounds or local cutoff consistency | `notes/no-go/phase.tex` | see review record | no Lean claim | unchecked |
| `P:nogo-21` | V | No-go | A same-noise Hilbert–Schmidt obstruction | `notes/no-go/topology.tex` | see review record | no Lean claim | unchecked |
| `P:nogo-22` | V | No-go | A mask that separates noise-null representatives | `notes/no-go/topology.tex` | see review record | no Lean claim | unchecked |
| `P:nogo-24` | V | No-go | Translations defeat whole-space compactness | `notes/no-go/topology.tex` | see review record | no Lean claim | unchecked |
| `P:nogo-25` | V | No-go | Escape from every fixed smooth projection | `notes/no-go/topology.tex` | see review record | no Lean claim | unchecked |
| `P:nogo-26` | V | No-go | A pure Young power and a maximum from an average | `notes/no-go/topology.tex` | see review record | no Lean claim | unchecked |
| `P:nogo-27` | V | No-go | The temporal concentration threshold | `notes/no-go/topology.tex` | see review record | no Lean claim | unchecked |
| `P:nogo-30` | V | No-go | Escaping variational scores | `notes/no-go/topology.tex` | see review record | no Lean claim | unchecked |
| `P:nogo-32` | V | No-go | The point feature is outside the closed noise image | `notes/no-go/topology.tex` | see review record | no Lean claim | unchecked |
| `P:nogo-23` | V | No-go | A one-sided variance bound fails | `notes/no-go/optimization.tex` | see review record | no Lean claim | unchecked |
| `P:nogo-28` | V | No-go | An occupation ceiling need not improve a comparison value | `notes/no-go/optimization.tex` | see review record | no Lean claim | unchecked |
| `P:nogo-29` | V | No-go | Empty sets, concavity and matrix order | `notes/no-go/optimization.tex` | see review record | no Lean claim | unchecked |
| `P:nogo-33` | V | No-go | Three invalid proof steps | `notes/no-go/optimization.tex` | see review record | no Lean claim | unchecked |
| `P:white-four` | IV | Proposition | White-space order four | `notes/notes_stratonovich_ham_second_moment.tex` | see review record | formalized in full (43 Lean claims) | unchecked |
| `L:static-four` | IV | Lemma | Static finite-order calibration | `notes/notes_stratonovich_ham_second_moment.tex` | see review record | no Lean claim | unchecked |
| `P:riesz-small` | IV | Proposition | Riesz finite coefficients | `notes/notes_stratonovich_ham_second_moment.tex` | see review record | formalized, narrower conclusion (52 Lean claims) | unchecked |
| `L:d1-spatial` | IV | Lemma | Spatial estimate | `notes/notes_stratonovich_ham_second_moment.tex` | see review record | formalized in full (31 Lean claims) | unchecked |
| `P:d1-upper` | IV | Proposition | One-dimensional upper bound | `notes/notes_stratonovich_ham_second_moment.tex` | see review record | formalized in full (63 Lean claims) | unchecked |
| `L:low-alpha-convolution` | IV | Lemma | Low-$\alpha$ convolution bound | `notes/notes_stratonovich_ham_second_moment.tex` | see review record | formalized in full (23 Lean claims) | unchecked |
| `L:alpha-one-convolution` | IV | Lemma | Degree-one convolution bound | `notes/notes_stratonovich_ham_second_moment.tex` | see review record | formalized in full (28 Lean claims) | unchecked |
| `P:low-alpha-upper` | IV | Proposition | Upper bound for $\alpha \le 1$ | `notes/notes_stratonovich_ham_second_moment.tex` | see review record | formalized in full (24 Lean claims) | unchecked |
| `C:d1-first-calibration` | IV | Corollary | First-moment calibration | `notes/notes_stratonovich_ham_second_moment.tex` | see review record | formalized in full (41 Lean claims) | unchecked |
| `P:higher-transfer` | IV | Proposition | Conditional upper bound | `notes/notes_stratonovich_ham_second_moment.tex` | see review record | no Lean claim | unchecked |
| `L:higher-riesz` | IV | Lemma | Riesz spatial maxima | `notes/notes_stratonovich_ham_second_moment.tex` | see review record | formalized in full (42 Lean claims) | unchecked |
| `C:higher-riesz` | IV | Corollary | Riesz moment bounds | `notes/notes_stratonovich_ham_second_moment.tex` | see review record | no Lean claim | unchecked |
| `P:higher-obstructions` | IV | Proposition | Obstructions to the spatial hypothesis | `notes/notes_stratonovich_ham_second_moment.tex` | see review record | no Lean claim | unchecked |
| `L:static-holder-input` | IV | Lemma | Static coefficient input | `notes/notes_stratonovich_ham_second_moment.tex` | see review record | no Lean claim | unchecked |
| `P:static-holder-upper` | IV | Proposition | Interpolation bound for Riesz covariance | `notes/notes_stratonovich_ham_second_moment.tex` | see review record | no Lean claim | unchecked |
| `L:planar-endpoints` | IV | Lemma | Planar endpoint covariances | `notes/notes_stratonovich_ham_second_moment.tex` | see review record | no Lean claim | unchecked |
| `L:planar-static-input` | IV | Lemma | General planar static coefficient input | `notes/notes_stratonovich_ham_second_moment.tex` | see review record | no Lean claim | unchecked |
| `P:planar-upper` | IV | Proposition | Planar homogeneous-covariance upper bound | `notes/notes_stratonovich_ham_second_moment.tex` | see review record | no Lean claim | unchecked |
| `C:planar-range` | IV | Corollary | Full planar parameter range | `notes/notes_stratonovich_ham_second_moment.tex` | see review record | no Lean claim | unchecked |
| `L:product-endpoints` | IV | Lemma | Strict product endpoints | `notes/notes_stratonovich_ham_second_moment.tex` | see review record | formalized in full (33 Lean claims) | unchecked |
| `L:plane-endpoints` | IV | Lemma | Plane-supported endpoints | `notes/notes_stratonovich_ham_second_moment.tex` | see review record | formalized in full (21 Lean claims) | unchecked |
| `L:endpoint-closure` | IV | Lemma | Linear images and finite positive sums | `notes/notes_stratonovich_ham_second_moment.tex` | see review record | formalized in full (18 Lean claims) | unchecked |
| `P:three-transfer` | IV | Proposition | Conditional three-dimensional transfer | `notes/notes_stratonovich_ham_second_moment.tex` | see review record | no Lean claim | unchecked |
| `C:three-product-riesz` | IV | Corollary | Ordinary product and Riesz covariances in dimension three | `notes/notes_stratonovich_ham_second_moment.tex` | see review record | steps checked (21 Lean claims) | unchecked |
| `C:three-finite-images` | IV | Corollary | Finite sums of linear images | `notes/notes_stratonovich_ham_second_moment.tex` | see review record | steps checked (12 Lean claims) | unchecked |
| `L:physical-spectral-energy` | IV | Lemma | Sobolev energy identification | `notes/notes_stratonovich_ham_second_moment.tex` | see review record | no Lean claim | unchecked |
| `L:mean-coefficient-holder` | IV | Lemma | Mean coefficients for the power covariance | `notes/notes_stratonovich_ham_second_moment.tex` | see review record | no Lean claim | unchecked |
| `L:positive-series-type` | IV | Lemma | Type of a positive coefficient series | `notes/notes_stratonovich_ham_second_moment.tex` | see review record | formalized in full (9 Lean claims) | unchecked |
| `P:static-minorant-lower` | IV | Proposition | Static temporal-minimum comparison | `notes/notes_stratonovich_ham_second_moment.tex` | see review record | no Lean claim | unchecked |
| `P:near-static-mean-gap` | IV | Proposition | Near-static strict gap from the mean rate | `notes/notes_stratonovich_ham_second_moment.tex` | see review record | no Lean claim | unchecked |
| `L:full-moment-coefficient-holder` | IV | Lemma | Interpolation of the full moment coefficients | `notes/notes_stratonovich_ham_second_moment.tex` | see review record | no Lean claim | unchecked |
| `P:moment-growth-logconvex` | IV | Proposition | Log-convexity of the upper growth type | `notes/notes_stratonovich_ham_second_moment.tex` | see review record | steps checked (10 Lean claims) | unchecked |
| `C:static-moment-constant-continuity` | IV | Corollary | Recovery of the static moment constant | `notes/notes_stratonovich_ham_second_moment.tex` | see review record | steps checked (5 Lean claims) | unchecked |
| `L:white-clock-laplace` | IV | Lemma | White-space low-order Laplace transforms | `notes/notes_stratonovich_ham_second_moment.tex` | see review record | formalized in full (8 Lean claims) | unchecked |
| `P:clock-copy-obstruction` | IV | Proposition | Obstruction to unweighted constant-correlation clock copying | `notes/notes_stratonovich_ham_second_moment.tex` | see review record | formalized in full (23 Lean claims) | unchecked |

## Notes

- Results: 253 (8 theorems, 93 propositions, 106 lemmas, 13 corollaries, 33 no-go results).
- Lean: 59 formalized in full, 22 formalized with a narrower conclusion, 1 with every conclusion and inputs supplied, 30 with steps checked, 2 outside Lean, 139 with no Lean claim.
- `T:first` and `T:crude` restate results of the cited source; their titles give the citation key and pinpoint.
- The companion's coverage file also maps 4 labels that are not numbered theorems, propositions, lemmas or corollaries (displayed equations and a remark), class same-assumptions. They have no rows here.
- The proofs were rewritten for readability after the AI reviews this ledger points to; the final text is at development commit `cdef8c83` of the private development repository. Those earlier reviews do not cover the added sentences. A separate re-read of every rewritten proof by DeepSeek V4 Pro is reported in Appendix E ("The re-reads after the readability pass").
- Manuscript read at development revision `a1c318a` of the private development repository; the book's TeX there is as at development revision `7e81252`. The Lean column is taken from the `coverage.yaml` (class, conclusion and claims of each row) of the public Lean companion, release `v0.11.0` (DOI 10.5281/zenodo.24479072), at its commit `3bd5c06`, the file pinned in `scripts/lean-coverage/`. The release is cut from the wave-L21 gate (development commit `38a3e00` of the private development repository); its lean-pkg receipts are those of the release commit `4d0e11c` (5,326 theorem claims compared, 6,632 claims, 0 `sorry`, standard axioms only). `3bd5c06` changes only documentation after `4d0e11c`, and the companion's `provenance/DEVELOPMENT.md` lists every change from the gate. Le closed the wave-L21 gate on 2026-11-23 and accepted release v0.11.0 on 2026-11-23. The coverage file's manuscript anchor is revision `edf7085f`; the 33 no-go results of Chapter 12 have no Lean claim. Every theorem, proposition, lemma or corollary label in that coverage file exists at `7e81252`.
