# Wave L9 correspondence reviews: adjudication of every finding

Companion branch `wave-l9/repair`, from the reviewed commit eb253a5. First the
merge of main aff7409 (wave L8 with both rounds of L8 review repairs), then
the repair commit "Wave L9 review repairs (docs)". The file:line references
point to the files at the repair commit. "Ledger" means docs/statement-ledger.md.
No Lean file was changed.

## Merge of main aff7409 (L8 repairs) into the L9 docs

Five files conflicted. Each resolution keeps the L8 repair and the L9 addition,
and restates the result so that it is true after L9.

- coverage.yaml, `L:damped-homogeneous-norms`: same-assumptions/weaker kept (L8). The
  scope sentence was rewritten for L9 (387 characters). Covariance smoothing appears
  only as membership of the Gaussian factor in the multiplier class, and its spectral
  identification is not formalized. The Green-smoothing identification is proved in
  d = 1, 2, 3. The note adds "(its spectral identification is not formalized)". The
  summary count follows the L9 numbers, adjusted.
- docs/coverage-scope-tex.yaml: rebuilt from both sides. A row is kept when its ascii
  equals the merged coverage.yaml scope. The new damped TeX sentence was written by
  hand. 42 scopes and 42 mirrors.
- README.md: the L8 narrower form is kept, with the Green identification in d = 1, 2,
  3 credited to `damped_homogeneous_norms_fourier_one` and
  `WaveGreenFourier.damped_homogeneous_norms_fourier_wave`.
- COMPLETION.md: the L8 and L10/L11 state rows from main are kept and the L9 row is
  merged in. The damped status is back to "narrower" (26/18/5/24/3).
- Ledger: four hunks. (1) In Scope, only the covariance-smoothing gap remains. (2) The
  `full_wave` row heading uses the narrower reading and names both Fourier wrappers.
  (3) The StaticPhaseCauchy Cauchy rows take L8's version (rho > 0, c > 0, d >= 0).
  The fockD row takes L9's FockForm cross-reference. (4) The WaveGreen closing
  paragraph combines the two versions: the Fourier identities hold in d = 1, 2, 3,
  `full_wave` is the narrower bundle, and the Green identification comes from the two
  Fourier wrappers, not from `full_wave`.

## Findings

| Group | Id | Sev | Verdict | Change |
|---|---|---|---|---|
| g1 | W1 | fatal | ACCEPTED (the author's decision: same-assumptions, conclusion weaker) | coverage.yaml:237-238 (conclusion weaker, scope restored) and note :282-284. docs/coverage-scope-tex.yaml:17-19 (ASCII and TeX). Each whole-lemma or `full_wave` sentence the reviewer listed is now qualified. Ledger Scope 202-215 and 254-258. Index 600, 723 and 800. DampedMultiplier intro 1686-1697. `full_wave` row 1852. DampedNormsHomog 1885-1888 and 1915-1921. WaveGreen intro 8318-8323 and closing paragraph 8397-8411. README.md:87-97. FORMALIZATION.md:80, where the damped lemma joins the narrower list. Each place where the Green identification is claimed cites `damped_homogeneous_norms_fourier_one` (d = 1) and/or `WaveGreenFourier.damped_homogeneous_norms_fourier_wave` (d = 1, 2, 3). The ledger does not present `LowAlphaConvolution.gammaEps_spectral` as the spectral-measure statement: its row (3765) calls it a pointwise representation. COMPLETION status is narrower. |
| g1 | W2 | major | ACCEPTED | Ledger LowAlphaConvolution 3676-3681 (gammaEps_spectral is an identity of Lean integrals with no integrability conclusion, and smoothed_pairing_spectral concludes integrability). 3709-3718 replace the blanket sentence with the declarations that prove integrability: integrable_heatDens, smoothed_pairing_spectral and the four wrappers. gammaEps_spectral and gammaEps_nonneg are marked as having no integrability conclusion. The gammaEps row (3746) and the gammaEps_spectral row (3765) say the same. |
| g1 | W3 | minor | ACCEPTED | Ledger 8391-8392 and 8515-8516: `radial2 s r = 0` for `s^2 <= r^2`, in particular `0 <= s <= r`. |
| g1 | W4 | minor | ACCEPTED, deferred (Lean comment) | refutations/wave-green-fourier/ArchimedesUnit.lean:7-9 says the proof uses the package law at a unit vector, but the proof uses `Measure.toSphere_ne_zero`. Lean was not changed, as decided. This is listed below as a proposed comment-only fix. |
| g2 | W1 | major | ACCEPTED | Ledger PhaseContractions 5046-5057. The integrability guarantee is limited to the principal statements under the tempered, locally finite class: phase_resolvent, phase_trace, traceT_fourier, phase_contractions_paper and the L9Completed wrappers. gauss_shift_le and gammaEps_fourier (under the bare `IsSpectralMeasure` predicate, a totalized equality) and gammaEps_nonneg are named as statements of Lean integrals with no integrability conclusion. |
| g2 | W2 | major | ACCEPTED (documentation). The in-domain control is not supplied. | Ledger 5088-5100 is a new controls paragraph. MiddleRegionExponent and NormalCoordinateConstant are (a) in the manuscript domain. ShiftInvariance is (c): a control of the broader Lean statement of gauss_shift_le. Its witness, Lebesgue measure with alpha = 0 in d = 1, lies outside S:static-phase (d = 3, 0 < alpha < 2), so it is not a counterexample under the manuscript's standing class. The paragraph says that no shift-equality control inside that class is supplied. The reviewer's alternative, a new in-domain Lean refutation, needs a Lean change. It is left for a later Lean wave (see below). |
| g2 | W3 | minor | ACCEPTED | Ledger 3620-3622 and row 3644, and claims.yaml:17377. `alpha0` does not occur in the conclusion, but `alpha0 > 0` and `alpha + alpha0 < 2` are used to get `alpha < 2`. |
| g2 | CROSS-REFERENCES, SCOPE-AND-NOT-IN-LEAN (INCONCLUSIVE) | — | no action | These are reviewer coverage limits, not findings. |
| g3 | W1 | major | ACCEPTED | Ledger 4551-4560 (OccupationCeilingExact) and 5473-5481 (RawOccupationEnergy) account for the six controls. ComparisonNeedsA, EnergyExponent and ScalarConstantHalved are (a). CellWidth and TrapezoidLimit are (b) Lean-route-only controls (idx and trap are not TeX constructions) and are expressly not manuscript negative controls. PenaltyPositive is (c), a totalized-arithmetic control (D_0 = 0 from 1/0 = 0). The route-only files are not certified as manuscript controls. |
| g3 | W2 | minor | ACCEPTED | Ledger 4569 and claims.yaml:15845: `min(natfloor((N+1)s), N)`, with natural floor 0 for negative arguments. |
| g3 | W3 | minor | ACCEPTED | Ledger 5440-5444. The finiteness of A(g) is a conclusion. T(g) < infinity is part of membership in O (`energy_lt_top`, as in the TeX's definition of O), and its real integral representation is a conclusion. |
| g3 | W4 | minor | ACCEPTED (the author's decision for T:intrinsic-occupation-ceiling) | Ledger 5459-5469 (RawOccupationEnergy) and 4542-4545 (OccupationCeilingExact). The joint representatives are the same a.e. data as the TeX's strongly H^1-measurable occupations, not a smaller class, and the bridge is not formalized. The representation disclaimer stays. The coverage class of T:intrinsic-occupation-ceiling is unchanged: same-assumptions, weaker because of the C_2 sentence. |
| g4 | W1 | major | ACCEPTED | claims.yaml:16448, 272 characters. The summary of phase_block_of_inputs now has 0<a<1, 0<lam, 0<=h, the coupling `c lam^(a-2) <= deltaA a`, measurability of J and the explicit domination. |
| g4 | W2 | major | ACCEPTED (documentation) | Ledger 1582-1595 is a new controls paragraph. BlockExponent, NeumannInverse, PhaseWeight and ParabolaQuarter are (a). ImaginaryRoot is (c): a control of the reduced-premise implication of im_root_le. Its witness `w = -1`, `lambda = 1` violates `x >= -lambda^2/4` (main TeX 2393). Whether `lambda/2` fails under the full hypotheses is not decided. The refutation file is unchanged. |
| g4 | W3 | minor | ACCEPTED | Ledger 1540-1543: phaseG is the `if` branch that supplies the removable sine-quotient value, and phaseH, a product involving phaseG, then has value 0 at w = 0. |
| g4 | W4 | minor | ACCEPTED | Ledger 1666: "a point of W(A_0 - T) when norm(u) = 1". The general identity is unchanged. |
| g5a | W1 | minor | ACCEPTED | Ledger 2700-2704. A truncated lowering index carries a coefficient that vanishes exactly when the subtraction truncates: `sqrt(k_i)` or `sqrt(n)` in normalized formulas, and `k_i` or `n` (as in `n * hermR (n - 1)`) in unnormalized ones. |
| g5b | W1 | minor | ACCEPTED | Ledger creOp_bound row 3034. The column bound is the only hypothesis. Symmetry is needed only by the annihilation and combined bounds. |
| g5b | W2 | minor | ACCEPTED | Ledger 2976-2985 and annOp_bound row 3035. The N+1-to-N indexing is explained. Applied to an input already supported through N, it leaves one unused degree of slack. The TeX's `sqrt(n)` concerns input degrees <= n. The direct "(N+1)c versus Nc" comparison was removed. |
| g5b | W3 | minor | ACCEPTED | Ledger 2953-2957 adds the convention. Mathlib's inner product is conjugate-linear in the first slot, the TeX's is linear (line 2824), and every adjoint identity survives. |
| g6a | W1 | fatal | ACCEPTED (the author's decision) | coverage.yaml:338-339 change L:finite-word-cutoff to inputs-supplied, conclusion weaker. Input :357-358: "one Gaussian mode per color ... the multi-mode case is not formalized". Note :359-362: "Nothing supplied in the one-mode special case", and wave L11 K10 has the multi-mode case. The scope sentence (unchanged) and its mirror were already accurate. Ledger Scope 56-60, 61-63, 72-74 (fifty-two, forty-seven), 274-280 and 343-360 (now among the parts of six further results). The HermiteWordFock intro (1028-1034) says that the restriction is to admissible operator data. README.md:21-25 and 249-253. FORMALIZATION.md:80, 82, 135 and 144. COMPLETION.md: steps/narrower. Counts are below. |
| g6a | W2 | major | ACCEPTED | Headings were renamed: "## HermiteWordFock (one-mode special case of `L:finite-word-cutoff`)" (ledger 1019) and "## FockForm (parts of results, spatial column bounds supplied)" (2367). The references at ledger 60, 782 (Index fockD row) and 2423 were updated. Scope 61-63 notes the FockForm exception to the "whole result" marking. |
| g6a | W3 | minor | ACCEPTED | Ledger 2458-2460: "symmetry is proved ... (the finite coefficient pairing identity; no operator-space packaging as a self-adjoint operator is stated)". |
| g6b | W1 | minor | ACCEPTED | Ledger 6929-6930, 6968-6971 and the rows at 6978 and 6988. The shorthand was replaced by "the scalar and weighted-block-map deductions" (L:complex-phase) and "the coefficient-model sandwich estimate" (L:fock-form). |
| all | Limitations (no build, partial provenance reading) | — | no action | These are reviewer coverage limits, not findings. |

Control classes, as used in the new ledger paragraphs:
- (a) A manuscript-claim perturbation: a changed constant, exponent or form, or a dropped manuscript hypothesis, refuted at a witness that satisfies the manuscript's other hypotheses.
- (b) A Lean-route-only control.
- (c) A control of Lean's totalized arithmetic, or of a broader Lean generalization outside the manuscript's domain.

## Class and count changes

- L:damped-homogeneous-norms: L9 docs had same/full. It is now same/weaker, and in COMPLETION "formalized, manuscript hypotheses, narrower conclusion".
- L:finite-word-cutoff: L9 docs had same/weaker. It is now inputs-supplied/weaker, and in COMPLETION "inputs supplied, steps/narrower".
- Totals: coverage rows were 48 same, 29 inputs and 3 outside. They are now 47 same, 30 inputs and 3 outside, for 80 rows. COMPLETION labelled results were 27/17/5/24/3/144. They are now 26/17/5/25/3/144, for 220. coverage.yaml summary: "Forty-seven ... (seventeen with a narrower conclusion) ... five more ... parts of 25 further". Ledger Scope and README: fifty-two whole results, forty-seven with no input. FORMALIZATION: 47 results and H:homog, 1562 theorems. "Part of" is 10 modules and the audit file HermiteWordFock, 300 theorems.

## Proposed comment-only Lean fixes (for a later Lean wave; not made now)

1. refutations/wave-green-fourier/ArchimedesUnit.lean:7-9 (g1 W4): the comment should say that nonzero sphere mass comes from `Measure.toSphere_ne_zero`, not from the package law at a unit vector.
2. refutations/phase-contractions/ShiftInvariance.lean:9-12: add that the witness (d = 1, Lebesgue, alpha = 0) lies outside S:static-phase and controls the general Lean statement only. Optionally, add an in-domain shift-equality refutation (d = 3, 0 < alpha < 2, for example Gamma = |x|^(-alpha) dx with q != 0). That would need new Lean.
3. refutations/complex-phase-scalar/ImaginaryRoot.lean:7-10: add that the witness w = -1, lambda = 1 violates x >= -lambda^2/4 (main TeX 2393), so it controls only the reduced-premise implication.
4. refutations/occupation-ceiling-exact/CellWidth.lean and TrapezoidLimit.lean: say "Lean-route control" in the headers. They now say "Refutation for ... (Lean route of ...)", which is already accurate, so this is optional.

## Confirmation round, 338cdba

The reviews were c1 (damped and Green merge), c2 (phase, occupation and complex scalar), c3 (Hermite, Fock and word) and c4 (scope and totals rerun). The repairs sit on branch `wave-l9/repair`, on top of 3938893 (the L9 comparator merge). Only documentation changed, no Lean.

| Review | Finding | Sev | Decision | Change |
|---|---|---|---|---|
| c1 | C1 README "full conclusions of fifty-two" | major | ACCEPTED | README.md:24-26 now reads "formalize fifty-two labelled results to the scopes specified below, some with narrower conclusions, and parts of further results". A grep for other count claims of whole or full conclusions found these, all repaired: FORMALIZATION.md:144 ("fifty-two labelled results formalized to their stated scopes (seventeen with a narrower conclusion)"); README.md:325 and ledger 42 and 422 ("whole-result modules" becomes "library modules"); README.md:346. The ledger Scope (74-76) already said "to the scopes specified below (some with a narrower conclusion)". FORMALIZATION.md:80 states its seventeen narrower results explicitly, so it was left. |
| c1 | C2 ArchimedesUnit proof-route comment | minor | REJECTED as a documentation repair, deferred | This is a Lean comment. It stays on the comment-only list for a later Lean wave (item 1 above). No documentation claim depends on it. |
| c2 | C1 BlockExponent and PhaseWeight targets | minor | ACCEPTED | Ledger ComplexPhaseScalar controls paragraph. BlockExponent refutes the scalar block-sum majorant `(39+12x)e^x <= 100 e^x`, not an identified propagator bound. PhaseWeight refutes the unsquared factor in the multiplier (squared-norm) inequality, whereas the TeX's unsquared factor is for norms. |
| c2 | C2 generic "wrong variants of the whole results" | minor | ACCEPTED | README.md:267-270 and :327, and FORMALIZATION.md:87. Refutations are now described as proofs refuting specified variants of declarations: manuscript scalar steps, Lean-route-only constructions, and controls of totalized arithmetic or of broader generalizations, with the ledger giving each one's domain. |
| c3 | C1 "(whole result)" headings of partial modules | major | ACCEPTED | Headings were renamed (listed below). The Index references "section IntervalScalar (whole result)" (seven rows) and "section StaticPhaseCauchy (whole result)" (five rows), and the SymplecticFree rows, now carry the new heading text. The Scope bullet (61-67) now names the ten modules that formalize only proof steps or parts of results, so "whole result" is not their classification. `E:static-block-series` stays marked as complete: its Index row says "in full, nothing supplied", and the IntervalScalar heading says so. |
| c4 | C1 COMPLETION L9 dimensions | major | ACCEPTED | COMPLETION.md:29 now reads "low-alpha convolution in d = 1, 2, 3 and phase contractions in d = 3, with nothing supplied". |

The scan of every "(whole result)" heading was checked against the module classification in FORMALIZATION.md, which lists the modules that count as parts of labelled results. Headings changed (FockForm was already changed in the previous round):
- `ComplexPhaseScalar (parts of results, analytic inputs supplied)`
- `GaussianComparison (part of a result: the finite Gaussian comparison)`
- `IntervalScalar (proof steps and parts of results, analytic inputs supplied; E:static-block-series in full)`
- `IntervalScalarCompleted (parts of results, analytic inputs supplied)`
- `RemoveMask (part of a result, one display over a supplied input)`
- `StaticPhaseCauchy (proof steps of P:static-phase-all-orders, analytic inputs supplied)`
- `SymplecticFree (part of a result, analytic inputs supplied)`
- `TerminalWick (part of a result, analytic inputs supplied)`
- `WaveTwoVariances (part of a result, named inputs supplied; spectral core in full)`

Some modules keep "(whole result)" although they take named inputs: `RadiusMeanAnchor`, `TypeContinuity`, `UniformSeriesTail` and `L8Completed` (for its `uniform_series_tail_terminal_wick_paper`). They prove every conclusion of their results with named inputs (coverage inputs-supplied/full, and COMPLETION "inputs supplied, every conclusion proved"), so they are whole results with inputs, not partial consumers. The other "(whole result)" headings belong to modules counted as nothing supplied: their abstract inputs are discharged by a completion module, as FORMALIZATION.md records. The WaveTwoVariances Index rows that still say "(whole result)" (`E:variance-normalized-kernel`, `E:variance-kernel-time-bound`, `E:variance-actual-growth-constant`) are definitions and bounds formalized in full with no input, so they are correct.

Checks: claims PASS (2468 claims). Coverage OK (80 rows: 47 same, 30 inputs, 3 outside). index_check: 0 errors (1310 labelled, 1158 unlabelled). Mirror check OK (42 scopes). COMPLETION table matches coverage.yaml. No tabs or absolute paths.

## Re-confirmation round, ba6c565

Reviews: r1 (the earlier findings and the renames) and r2 (every whole-result heading). Both failed. The orchestrator's decision was to adopt the strict meaning of "whole result". The changes are documentation only: no Lean change and no coverage class change. The coverage.yaml summary sentence was reworded; its counts did not change.

Category definitions. They are written into the ledger Scope (lines 62-75) and into FORMALIZATION.md ("Heading categories").
- (A) "(whole result)": every conclusion of the labelled result is a Lean conclusion under the manuscript's hypotheses, possibly with named supplied inputs that are disclosed (coverage same-assumptions/full or inputs-supplied/full). No other section carries it.
- (B) "(narrower result: <what is missing>)": a labelled result some of whose conclusions are not Lean conclusions, or are proved for a modelled object whose identification with the manuscript's object is not formalized. Examples of such objects are the class O by joint representatives, the rate in Rayleigh form and the cost in integral form. Discharging a named input in a completion module does not make a narrower result whole.
- (C) "(foundation: ...)" or "(proof steps ...)": facts used by labelled results, not a labelled result themselves. Every StratonovichHAMAudit section except HermiteWordFock is of this kind.

| Review | Finding | Sev | Decision | Change |
|---|---|---|---|---|
| r1 | R1 RemoveMask Index row (ledger 772) | major | ACCEPTED | The row now reads "(part of a result: the rates with nothing supplied, in Rayleigh form; the point display over the named input `RawBlockOriginalLower`, with a real function standing in for the point moment)". |
| r1 | R2 ArchimedesUnit comment | minor | DEFERRED (Lean comment) | It stays on the comment-only list. |
| r2 | R1-R7 whole-result headings | major | ACCEPTED | All headings were reclassified (table below). The eight INCONCLUSIVE modules were decided conservatively as B, because the class-O bridge or the rate, cost and variance identification is not formalized. All the other headings were checked against the strict definition through their coverage rows. The A headings are exactly the modules whose main labelled result is same/full or inputs/full. |
| r2 | R8 classification conflates assumptions and conclusions | major | ACCEPTED | FORMALIZATION.md has a new kind table: whole results with nothing supplied, whole results with inputs supplied, narrower results, foundations or proof steps, and step facts, with module and theorem counts recomputed from claims.yaml. Its counting paragraph was rewritten, as were the ledger Scope bullets (categories and counts), the README overview (31 whole, 17 narrower, steps or parts of 25; by module 32 / 26 / 18) and the coverage.yaml summary sentence (thirty with every conclusion, counting the four E:/R: rows; seventeen narrower; five with inputs; 25 parts). COMPLETION.md did not change: it is driven by coverage.yaml, and no class changed. |

Counts. Labelled results: 26 whole (manuscript hypotheses), 5 whole (inputs supplied), 17 narrower (manuscript hypotheses), 25 steps or parts, 3 outside and 144 not formalized, total 220 (unchanged). Modules (76): 28 whole with nothing supplied (624 theorems, 152 definitions), 4 whole with inputs (106 theorems, 28 definitions), 26 narrower plus the audit file HermiteWordFock (772 theorems, 154 definitions), 18 foundation or proof steps (466 theorems, 78 definitions). There are 23 step modules (82 theorems, 6 definitions). Theorems sum to 2050. Ledger headings: 29 "whole result", 27 "narrower result", 34 "foundation" or "proof steps".

Coverage rows that may be inconsistent with A/B. None was found that needs a class change: every A heading's main row is full and every B heading's main rows are weaker. One subtlety: ClockCopy (A, main result P:clock-copy-obstruction) and some other A modules also contain rows for narrower labels, such as the finiteness part of L:damped-homogeneous-norms. Those rows are marked in the Index, not by the heading.

### Section headings changed (old -> new)

| Module | Old | New |
|---|---|---|
| DampedMultiplier | (whole result) | (narrower result: `L:damped-homogeneous-norms`, covariance-smoothing identification not formalized) |
| DampedNormsHomog | (whole result) | (narrower result: `L:damped-homogeneous-norms`, covariance-smoothing identification not formalized) |
| L8Completed | (whole result) | (narrower results: completions of the wave-L8 wrappers, see the rows; `L:uniform-series-tail` is a whole result with inputs supplied) |
| MaskedAuxiliaryNorm | (whole result) | (narrower result: `P:masked-auxiliary-norm` for complex `H` only) |
| OccupationCeilingExact | (whole result) | (narrower result: `T:intrinsic-occupation-ceiling` without the `C_2` sentence; class `O` bridge not formalized) |
| OccupationCeilingFinite | (whole result) | (narrower result: the occupation ceiling with the larger constant `K_0 R_sp`; `C_2` sentence not formalized) |
| OccupationPhysicalClass | (whole result) | (narrower result: `P:occupation-physical-class` over the modelled class `O`, bridge not formalized) |
| RawOccupationEnergy | (whole result) | (narrower result: `P:raw-occupation-energy` over the modelled class `O`, bridge not formalized) |
| RayleighTail | (whole result) | (narrower result: `L:tube-rayleigh-tail`, application to the operator moment not formalized) |
| SpatialBracket | (whole result) | (narrower result: `C:intrinsic-spatial-bracket` for `S_2^pos`, not `C_2`) |
| SpatialFourLinear | (whole result) | (narrower result: `P:spatial-four-linear` with sequential continuity; rate and cost identification not formalized) |
| SpatialOccupationCompleted | (whole result) | (narrower results: Rayleigh-form rate and integral-form cost, their identification not formalized) |
| SpatialOccupationL7Completed | (whole result) | (narrower results: class `O` bridge and rate and cost identification not formalized) |
| SpatialSmoothRatio | (whole result) | (narrower result: `P:spatial-smooth-ratio`, rate and cost identification not formalized) |
| SpatialStaticControls | (whole result) | (narrower result: `L:spatial-static-controls`, rate and cost identification not formalized) |
| VariationalDilation | (whole result) | (narrower result: `L:variational-control-dilation`, rate and variance identification not formalized) |
| VariationalMean | (whole result) | (narrower result: `L:variational-global-mean` without the mixed derivatives; `L:variational-heat-envelope` whole) |
| VariationalRate | (whole result) | (narrower result: operator half of `P:variational-unmasked-rate` and `Q_2 >= S_2^pos` not formalized) |
| ComplexPhaseScalar | (parts of results, analytic inputs supplied) | (narrower result: scalar steps of `L:complex-phase` and `L:interval-complex`, analytic inputs supplied) |
| FockForm | (parts of results, spatial column bounds supplied) | (narrower result: `L:fock-form` and `L:interval-contractions`, spatial column bounds supplied) |
| GaussianComparison | (part of a result: the finite Gaussian comparison) | (narrower result: only the finite Gaussian comparison of `P:masked-noise-completion`) |
| IntervalScalarCompleted | (parts of results, analytic inputs supplied) | (narrower result: steps of `P:interval-coefficients`, analytic inputs supplied) |
| RemoveMask | (part of a result, one display over a supplied input) | (narrower result: `P:variational-remove-mask` for Rayleigh-form rates; point display over a supplied input) |
| SymplecticFree | (part of a result, analytic inputs supplied) | (narrower result: `L:symplectic-free` with the free group and Young convergence supplied) |
| TerminalWick | (part of a result, analytic inputs supplied) | (narrower result: `L:terminal-wick` with inputs supplied and an added measurability restriction) |
| WaveTwoVariances | (part of a result, named inputs supplied; spectral core in full) | (narrower result: `P:wave-two-variances` with named inputs; spectral core in full) |
| HermiteWordFock | (one-mode special case of `L:finite-word-cutoff`) | (narrower result: `L:finite-word-cutoff` for one Gaussian mode per color) |
| IntervalScalar | (proof steps and parts of results, analytic inputs supplied; `E:static-block-series` in full) | (proof steps of `C:static-interaction` and `P:interval-coefficients`, inputs supplied; `E:static-block-series` in full) |
| StaticPhaseCauchy | (proof steps of `P:static-phase-all-orders`, analytic inputs supplied) | (proof steps of `P:static-phase-all-orders`, analytic inputs supplied) |
| FiniteWick | (whole result) | (foundation: the finite Wick formula, used by `L:terminal-wick`) |
| GaussianHermite | (whole result) | (foundation: normalized Hermite polynomials) |
| HermiteFock | (whole result) | (foundation: the finite Gaussian Fock layer) |
| H1Density | (whole result) | (foundation: density of test functions in `H^1`) |
| SeriesType | (whole result) | (foundation: elementary series bounds) |
| VariationalFloor | (whole result) | (foundation: the variational floor) |
| WaveGreen | (whole result) | (foundation: the wave Green measures) |
| WaveGreenFourier | (whole result) | (foundation: Fourier identities of the wave Green measures) |
| SpaceTimePositivity | (whole result) | (foundation: integral-form identities of the space-time occupation form) |
| ActualEvent | (none) | (proof steps) |
| AllAlphaMoment | (none) | (proof steps) |
| ClockFilter | (none) | (proof steps) |
| DampedLower | (none) | (proof steps) |
| DimensionalMatrix | (none) | (proof steps) |
| DirectEvent | (none) | (proof steps) |
| FiniteYoung | (none) | (proof steps) |
| GaussianTail | (none) | (proof steps) |
| GlobalOmega | (none) | (proof steps) |
| HermiteWord | (none) | (proof steps) |
| InteractionDriver | (none) | (proof steps) |
| JointTilt | (none) | (proof steps) |
| LocalFlow | (none) | (proof steps) |
| MiddleCross | (none) | (proof steps) |
| MovingCone | (none) | (proof steps) |
| OccupationForm | (none) | (proof steps) |
| PhaseResponse | (none) | (proof steps) |
| PositiveGram | (none) | (proof steps) |
| ProjectionResidual | (none) | (proof steps) |
| RawValueCeiling | (none) | (proof steps) |
| RawVariational | (none) | (proof steps) |
| TerminalCross | (none) | (proof steps) |
| WhiteCDF | (none) | (proof steps) |

Unchanged "(whole result)" (category A): ClockCopy, DriverParameters, FiniteGaussianMatrix, FrequencyRow, GaussianScalarPowers, GramScalarAlgebra, HomogHypothesis, IndexedCone, InventoryProduct, KappaRange, L9Completed, LowAlphaConvolution, MaskedContinuousWave, MaskedModulation, MaskedSpectralGrowth, MaskedTrigProducts, OccupationKernelRow, PhaseBessel, PhaseContractions, QuotientObstruction, RadiusMeanAnchor, SpatialFourierBound, SpectralMassIdentity, TemporalEquilibrium, TimeCompletion, TypeContinuity, UniformSeriesTail, WhiteClockLaplace, WhiteRelativeWidth.

### Index first cells changed (ledger line numbers before the Scope rewrite; add 11 for the committed file. Label; "whole result" -> new wording)

Rule: an Index first cell keeps "whole result" only if the label's coverage row is full or, for an equation label with no row, the display is formalized as stated. Cells for weaker labels, and for equation labels proved with a substitution (R_0 for R_sp, a real constant for C_occ, the modelled class O, integral form, complex H), now say "narrower result" (or "part of a result" for RemoveMask). Index cells that cite a renamed section were updated to its new heading.

| Line | Label | New first-cell qualifier |
|---|---|---|
| 495 | `L:tube-rayleigh-tail` | (narrower result: application to the operator moment not formalized) |
| 509 | `L:variational-control-dilation` | (narrower result: integral-form variance and Rayleigh-form rate, their identification not formalized) |
| 577 | `P:masked-auxiliary-norm` | (narrower result; the real-`H` clause after complexification is not formalized) |
| 580 | `E:masked-hilbert-fourier` | (narrower result: complex `H`, indeed any complex Banach space; the real-`H` clause not formalized) |
| 593 | `L:variational-global-mean` | (narrower result: the display `E:variational-global-mean` in full; the mixed-derivative sentence is not formalized; `variational_global_mean_lipschitz_paper` is a first-order complement to the display, not a TeX statement) |
| 623 | `P:variational-positive-scores` | (narrower result: everything except `Q_2 >= S_2^pos`; supremum forms on the named input `S1Bdd`, proved in `L8Completed`) |
| 645 | `L:spatial-static-controls` | (narrower result: Rayleigh-form rate and integral-form cost, their identification not formalized) |
| 684 | `P:spatial-four-linear` | (narrower result: joint continuity of `C_4` in sequential form) |
| 689 | `P:spatial-energy-map` | (narrower result: the energy set and `E_sp`) |
| 693 | `P:occupation-physical-class` | (narrower result; class `O` modelled by joint representatives; `SquarePairingBounds` discharged in `SpatialOccupationL7Completed`) |
| 695 | `E:occupation-physical-bound` | (narrower result, with `R_0` for `R_sp`) |
| 696 | `E:occupation-own-energy` | (narrower result over the modelled class, bound with `spEnergyVal alpha R_0` for `E_sp`) |
| 733 | `E:positive-bochner-inclusion` | (narrower result: the space-time form with the physical pairing, product and iterated forms; SpaceTimePositivity) |
| 734 | `E:occupation-raw-identities` | (narrower result: second identity in integral form for continuous compactly supported fields, nothing supplied; SpaceTimePositivity) |
| 735 | `E:positive-raw-mean` | (narrower result: first identity in integral form, nothing supplied; SpaceTimePositivity) |
| 737 | `L:positive-raw-embedding` | (narrower result: the variance identity in integral form, nothing supplied; SpaceTimePositivity) |
| 738 | `E:positive-bochner-inclusion` | (narrower result: the constant `K_0` and the iterated space-time form; OccupationCeilingFinite) |
| 740 | `L:positive-raw-embedding` | (proof) (narrower result: the row bound and the scalar Schur bound with `K_0`, nothing supplied; OccupationCeilingFinite) |
| 741 | `T:intrinsic-occupation-ceiling` | (proof) (narrower result: the two scalar maxima, the power algebra, and `I_Psi <= D v_Psi^(1/q)` with `K_0 R_0` on the named input `SpaceTimeCS`, discharged in `L8Completed`; OccupationCeilingFinite) |
| 742 | `E:occupation-score-ceiling` | (narrower result: `U_c` with a real constant in place of `C_occ`; OccupationCeilingFinite) |
| 743 | `P:raw-occupation-energy` | (proof) (narrower result: the square bound for smooth unit tests, nothing supplied; OccupationCeilingFinite) |
| 744 | `T:intrinsic-occupation-ceiling` | (narrower result: `K_0 R_sp` (or `K_0 R_0`) in place of `C_occ`, on the named input `SpaceTimeCS`, discharged in `L8Completed`; the exact `C_occ`: OccupationCeilingExact; OccupationCeilingFinite) |
| 745 | `P:variational-positive-scores` | (narrower result: the boundedness claim and the supremum statements on the named input `SpaceTimeCS`, discharged in `L8Completed`; `Q_2 >= S_2^pos` not formalized; OccupationCeilingFinite) |
| 746 | `E:spatial-static-score` | (narrower result: `sSup` form on the named input `SpaceTimeCS`, discharged in `L8Completed`; OccupationCeilingFinite) |
| 747 | `E:spatial-smooth-score` | (narrower result: `sSup` form on the named input `SpaceTimeCS`, discharged in `L8Completed`; OccupationCeilingFinite) |
| 748 | `P:spatial-smooth-ratio` | (narrower result: `R_0` bounded by `S_1^pos` (the route before `a284420`) on the named input `SpaceTimeCS`, discharged in `L8Completed`; OccupationCeilingFinite) |
| 749 | `E:spatial-static-energy-score` | (narrower result: `sSup` form on the named input `SpaceTimeCS`, discharged in `L8Completed`; OccupationCeilingFinite) |
| 752 | `C:intrinsic-spatial-bracket` | (proof): `Delta`, the ratio identity, the strict comparison and the `zeta = 1` counterexample (narrower result, with a real constant in place of `C_occ`) |
| 758 | `C:intrinsic-spatial-bracket` | (narrower result for `S_2^pos`, not `C_2`; named input `OccupationCeilingK0`, discharged in `L8Completed`) |
| 761 | `P:variational-remove-mask` | (part of a result: the rates with nothing supplied, in Rayleigh form; the point display over the named input `RawBlockOriginalLower`, with a real function standing in for the point moment) |
| 821 | `E:raw-occupation-definitions` | (narrower result: `A(g)`, `C_occ`, `E_zeta^O` and their value sets, over the class `O` modelled by `IsOccField`; RawOccupationEnergy) |
| 822 | `E:raw-occupation-bound` | (narrower result: general form on the hypothesis `SquarePairingBounds`, proved under `H:homog`; RawOccupationEnergy) |
| 823 | `P:raw-occupation-energy` | (proof) (narrower result: positivity, the dilation `U_l` and the scalar maximum, nothing supplied; RawOccupationEnergy) |
| 824 | `P:raw-occupation-energy` | (narrower result: general form and exact-hypothesis wrapper, nothing supplied; `O` modelled by `IsOccField`; RawOccupationEnergy) |
| 827 | `L:occupation-rayleigh-selection` | (narrower result: exact-hypothesis wrapper, nothing supplied; finite equal time cells in place of the countable selection; `O` modelled by `IsOccField`; OccupationCeilingExact) |
| 828 | `T:intrinsic-occupation-ceiling` | (proof) (narrower result: the first scalar maximum with the exact `C_occ`, nothing supplied; OccupationCeilingExact) |
| 829 | `T:intrinsic-occupation-ceiling` | (narrower result: both forms of `E:occupation-score-ceiling` with the exact `C_occ` for `S_c^pos`, nothing supplied; `C_2(Gamma,a) <= U_2` not formalized; `O` modelled by `IsOccField`; OccupationCeilingExact) |
| 830 | `C:intrinsic-spatial-bracket` | (narrower result: the comparison with the exact `E_(1/2)^O` for `S_2^pos`, not `C_2`, nothing supplied; OccupationCeilingExact) |

## Re-confirmation round 3, d5667f5, and Le's split modelled-object rule

Reviews h1-h5 were run on the strict headings; h5 (the consistency of the r1 diff) passed. Only documentation changed, no Lean. Le then chose the SPLIT modelled-object rule (relayed by the orchestrator). This round records that decision and applies it.

**Decision (Le, split rule).** A documented definitional model choice that is the standard construction is a registered model choice. A result whose only modelled object is such a choice stays "(whole result)", and its section names the model. The ledger Scope has a new model-choice register; M1 is the d = 3 wave Green measure via volume.toSphere, wave L6 decision 4, whose surface-measure identification is not proved. FORMALIZATION.md references the register. A missing construction makes a result narrower.

| Review | Finding | Sev | Decision | Change |
|---|---|---|---|---|
| h1 | H1 coverage conclusion field for A rows | major | ACCEPTED | `conclusion: full` was added to E:driver-parameters, E:kappa, L:gaussian-scalar-powers, L:gaussian-trace-bounds, L:gram-scalar-algebra, P:finite-gaussian-matrix and R:gaussian-one-variance-test, and also to L:equilibrium-gamma-beta, L:temporal-equilibrium (h3 H3) and P:radius-mean-anchor (h2 H5). L:raw-block-indexed-cone got `conclusion: weaker` under the split rule (below). No class or conclusion field is now missing. |
| h1 | H2 ComplexPhaseScalar | major | ACCEPTED | The heading names the block-map/propagator identification and the interval-norm telescoping. Index cells 849-850 refer to the section. |
| h1 | H3 FockForm | major | ACCEPTED | The heading and the L:fock-form / L:interval-contractions Index cells name the coefficient model of the m coordinates, symmetry without self-adjoint packaging, and spatial operators not constructed. |
| h1 | H4 IndexedCone | major | ACCEPTED under the split rule | Now "narrower result: abstract ground family; identification with the physical wave family not formalized". Coverage row is inputs-supplied/weaker with a scope sentence and TeX mirror. The Index cell is narrower. |
| h1 | H5 IntervalScalarCompleted | major | ACCEPTED | The heading and Index cell say positive-noise scalar assembly only; the evolution identification and the zero/sign reduction are not formalized. |
| h1 | H6 L8Completed missing items | major | ACCEPTED | The heading names K_0 R_sp for C_occ, S_2^pos for C_2, energyValue(K_0 R_sp) for E_(1/2)^O, and the rate/cost identification. The completion Index cells carry the same qualifiers. |
| h1 | H7 L:uniform-series-tail exception | major | ACCEPTED under the split rule | The exception is removed from the L8Completed heading (chain measures fixed only by their masses). UniformSeriesTail is now B. Coverage row is inputs-supplied/weaker with a scope sentence and mirror. Index cells are narrower. |
| h2 | H1 L9Completed, LowAlphaConvolution, PhaseContractions | major | REJECTED by Le's split rule | toSphere is registered model choice M1. The three sections stay "(whole result)" and now name M1. |
| h2 | H2 OccupationCeilingExact | major | ACCEPTED | The heading and Index cells add the rate/cost identification. |
| h2 | H3 OccupationCeilingFinite | major | ACCEPTED | The heading names the missing occupation-energy form and the rate/cost identification. The T:intrinsic Index cells say the same. |
| h2 | H4 QuotientObstruction | major | ACCEPTED under the split rule | Now "narrower result: covariance-functional obstruction; noise W not constructed, identification with noise variances not formalized". Coverage row is same-assumptions/weaker with scope and mirror. The Index cell, Scope sentence and README item are updated. |
| h2 | H5 RadiusMeanAnchor coverage | major | ACCEPTED | `conclusion: full` added. |
| h2 | H6 RemoveMask | major | ACCEPTED | The heading names the rate/cost identification and the real function in place of the canonical moment. Index cell (former 772) changed from "part of a result" to "narrower result". |
| h2 | H7 SpatialBracket | major | ACCEPTED | The heading and Index cells name energyValue(K_0 R_sp) for E_(1/2)^O and the rate/cost identification. |
| h3 | H1 SpatialOccupationL7Completed | major | ACCEPTED | The heading adds joint continuity only in sequential form. The P:spatial-four-linear and P:occupation-physical-class completion cells are narrower. |
| h3 | H2 SymplecticFree | major | ACCEPTED | The heading reads as the reviewer worded it. The five Index cells cite the section heading. |
| h3 | H3 TemporalEquilibrium coverage | major | ACCEPTED | `conclusion: full` on both rows. |
| h3 | H4 TerminalWick | major | ACCEPTED | The heading and the principal Index cell say: real r only, per mixed moment, chain measures by masses, hmeas supplied, hK added. |
| h3 | H5 VariationalRate | major | ACCEPTED | The heading and the P:variational-positive-scores / P:variational-unmasked-rate cells name the spectral and stochastic identification. |
| h3 | H6 WaveTwoVariances | major | ACCEPTED | The heading and the P:wave-two-variances cell name the abstract variance and phase spaces and the unformalized identification. |
| h3 | H7 HermiteWordFock | major | ACCEPTED | The heading and Index cell add single finite words, and that finite sums and Bochner integrals are not formalized. |
| h3 | H8 SpatialFourLinear, SpatialOccupationCompleted, SpatialSmoothRatio cells | major | ACCEPTED | The main-result cells say "narrower result: rate and cost identification not formalized". |
| h4 | H1 audit cells | major | ACCEPTED | Every audit-label Index cell is now "(proof steps: ...; <Module>)". C:intrinsic-spatial-bracket reads "(proof steps: scalar logarithmic gap only; RawValueCeiling)". |
| h4 | H2 completion cells | major | ACCEPTED | See H6, H1 and H8. |
| h4 | H3 helpers with inputs | major | ACCEPTED | The cells are split. squareBound_of_smooth_completed is its own row, keeping hsm. C4_square_CS_completed and square_pairing_CS_completed are their own row, keeping SquareBound. The paper wrappers are separate rows. |
| h4 | H4 SpaceTimePositivity definitions cell | major | ACCEPTED | The cell is now "(foundation: definitions of the physical space-time integral forms only; J_G and its covariance-space norm identity not formalized)". |
| h4 | H5 TerminalWick cell | major | ACCEPTED | As h3 H4. |

**Counts after the split rule.**

| | Count |
|---|---|
| Coverage rows | 47 same / 30 inputs / 3 outside (class unchanged) |
| Conclusion changes | P:masked-quotient-obstruction full → weaker; L:raw-block-indexed-cone none → weaker; L:uniform-series-tail full → weaker |
| COMPLETION labelled results | 25 / 18 / 3 / 27 / 3 / 144, total 220 |
| Modules: whole, nothing supplied | 27 (559 theorems, 135 definitions) |
| Modules: whole, inputs | 2 (57, 18) |
| Modules: narrower, plus HermiteWordFock | 29 (886, 181) |
| Modules: foundation / proof steps | 18 (466, 78) |
| Audit step modules | 23 (82, 6) |
| Ledger headings | 26 whole, 30 narrower, 34 foundation or proof steps |

The coverage summary, FORMALIZATION table, README overview and ledger Scope use these numbers. Every remaining "(whole result)" heading's main coverage rows are full; this was checked by script.

### Headings changed this round (old -> new)

| Module | Old | New |
|---|---|---|
| ComplexPhaseScalar | (narrower result: scalar steps of `L:complex-phase` and `L:interval-complex`, analytic inputs supplied) | (narrower result: scalar steps of `L:complex-phase` and `L:interval-complex`; the weighted block map not identified with the propagator, the interval-norm telescoping not formalized; functional-calculus inputs supplied) |
| FockForm | (narrower result: `L:fock-form` and `L:interval-contractions`, spatial column bounds supplied) | (narrower result: `L:fock-form` and `L:interval-contractions` on the coefficient model of the `m` multiplied coordinates (coordinates `i > m` not modelled), symmetry without self-adjoint operator packaging, spatial operators not constructed; spatial column bounds supplied) |
| IntervalScalarCompleted | (narrower result: steps of `P:interval-coefficients`, analytic inputs supplied) | (narrower result: positive-noise scalar coefficient assembly of `P:interval-coefficients`; identification with the interval evolution and the zero and sign reduction not formalized; analytic inputs supplied) |
| L8Completed | (narrower results: completions of the wave-L8 wrappers, see the rows; `L:uniform-series-tail` is a whole result with inputs supplied) | (narrower results: `K_0 R_sp` in place of `C_occ`, `S_2^pos` in place of `C_2`, `energyValue(K_0 R_sp)` in place of `E_(1/2)^O`, Rayleigh-form rate and integral-form cost not identified; `L:uniform-series-tail` with chain measures fixed only by their masses) |
| OccupationCeilingExact | (narrower result: `T:intrinsic-occupation-ceiling` without the `C_2` sentence; class `O` bridge not formalized) | (narrower result: `T:intrinsic-occupation-ceiling` without the `C_2` sentence; class `O` bridge and rate and cost identification not formalized) |
| OccupationCeilingFinite | (narrower result: the occupation ceiling with the larger constant `K_0 R_sp`; `C_2` sentence not formalized) | (narrower result: the occupation ceiling with the larger constant `K_0 R_sp`; the occupation-energy form, the `C_2` sentence and the rate and cost identification not formalized) |
| RemoveMask | (narrower result: `P:variational-remove-mask` for Rayleigh-form rates; point display over a supplied input) | (narrower result: `P:variational-remove-mask` for Rayleigh-form rates and integral-form costs, their identification not formalized; the point display for a real function in place of the canonical solution's moment, over a supplied input) |
| SpatialBracket | (narrower result: `C:intrinsic-spatial-bracket` for `S_2^pos`, not `C_2`) | (narrower result: `C:intrinsic-spatial-bracket` for `S_2^pos` in place of `C_2`, with `energyValue(K_0 R_sp)` in place of `E_(1/2)^O`; rate and cost identification not formalized) |
| SpatialOccupationL7Completed | (narrower results: class `O` bridge and rate and cost identification not formalized) | (narrower results: class `O` bridge and rate and cost identification not formalized; joint continuity only in sequential form) |
| SymplecticFree | (narrower result: `L:symplectic-free` with the free group and Young convergence supplied) | (narrower result: `J_E`, the duality-form identification and symplectic preservation on `E` not formalized; force skewness only at the `L^2` level; free-group data and Young convergence supplied) |
| TerminalWick | (narrower result: `L:terminal-wick` with inputs supplied and an added measurability restriction) | (narrower result: `L:terminal-wick` for real `r` only, comparison per mixed moment only, chain measures specified by their masses, not constructed; inputs supplied and an added measurability restriction) |
| VariationalRate | (narrower result: operator half of `P:variational-unmasked-rate` and `Q_2 >= S_2^pos` not formalized) | (narrower result: Rayleigh-form rates and integral-form costs, their spectral and stochastic identification, the operator half of `P:variational-unmasked-rate` and `Q_2 >= S_2^pos` not formalized) |
| WaveTwoVariances | (narrower result: `P:wave-two-variances` with named inputs; spectral core in full) | (narrower result: `P:wave-two-variances` for abstract variance and phase spaces, their identification with `ell_R` and the manuscript's spaces not formalized; named inputs; spectral core in full) |
| HermiteWordFock | (narrower result: `L:finite-word-cutoff` for one Gaussian mode per color) | (narrower result: `L:finite-word-cutoff` for one Gaussian mode per color and single finite words; finite sums and Bochner integrals not formalized) |
| QuotientObstruction | (whole result) | (narrower result: covariance-functional obstruction; noise `W` not constructed, identification with noise variances not formalized) |
| IndexedCone | (whole result) | (narrower result: abstract ground family; identification with the physical wave family not formalized) |
| UniformSeriesTail | (whole result) | (narrower result: `L:uniform-series-tail` for an abstract `L^2` family with the two facts of `L:terminal-wick` supplied; identification with the terminal-chain terms not formalized) |

### Index first cells changed this round (line numbers are from before the Scope additions of this round)

| Line or kind | Old first cell | New first cell |
|---|---|---|
| 624 | `P:wave-two-variances` (spectral core in full; the proposition itself with the named inputs hlink, hJL2/hJ, hnormSG) | `P:wave-two-variances` (narrower result: abstract variance and phase spaces, their identification with `ell_R` and the manuscript's spaces not formalized; spectral core in full; the proposition with the named inputs hlink, hJL2/hJ, hnormSG) |
| 633 | `P:variational-unmasked-rate` (Rayleigh-form part; the operator half is not formalized) | `P:variational-unmasked-rate` (narrower result: Rayleigh-form part; the operator half and the rate identification are not formalized) |
| 634 | `P:variational-positive-scores` (narrower result: everything except `Q_2 >= S_2^pos`; supremum forms on the named input `S1Bdd`, proved in `L8Completed`) | `P:variational-positive-scores` (narrower result: Rayleigh-form rates and integral-form costs, their spectral and stochastic identification and `Q_2 >= S_2^pos` not formalized; supremum forms on the named input `S1Bdd`, proved in `L8Completed`) |
| 655 | `P:spatial-smooth-ratio` (both claims; score in existential form) | `P:spatial-smooth-ratio` (narrower result: rate and cost identification not formalized; both claims, score in existential form) |
| 661 | `L:spatial-static-controls` (completed wrappers, nothing supplied) | `L:spatial-static-controls` (narrower result: Rayleigh-form rate and integral-form cost, their identification not formalized; completed wrappers, nothing supplied) |
| 662 | `P:spatial-smooth-ratio` (completed wrappers; supremum forms on the named input `S1Bdd`, proved in `L8Completed`) | `P:spatial-smooth-ratio` (narrower result: rate and cost identification not formalized; completed wrappers; supremum forms on the named input `S1Bdd`, proved in `L8Completed`) |
| 700 | `P:spatial-energy-map` (narrower result: the energy set and `E_sp`) | `P:spatial-energy-map` (narrower result: the energy set and `E_sp`; rate and cost identification not formalized) |
| 727 | `E:interval-coefficient-bound` (completion step rows; `L:inventory-product` discharged) | `E:interval-coefficient-bound` (narrower result: positive noise only, identification with the interval evolution and the zero and sign reduction not formalized; completion step rows; `L:inventory-product` discharged) |
| 734 | `P:occupation-physical-class` (completion wrappers, nothing supplied) | `P:occupation-physical-class` (narrower result: class `O` modelled by joint representatives, bridge not formalized; completion wrappers, `SquarePairingBounds` discharged, nothing supplied) |
| 744 | `E:positive-bochner-inclusion` (narrower result: the space-time form with the physical pairing, product and iterated forms; SpaceTimePositivity) | `E:positive-bochner-inclusion` (foundation: definitions of the physical space-time integral forms only; `J_G` and its covariance-space norm identity not formalized; SpaceTimePositivity) |
| 755 | `T:intrinsic-occupation-ceiling` (narrower result: `K_0 R_sp` (or `K_0 R_0`) in place of `C_occ`, on the named input `SpaceTimeCS`, discharged in `L8Completed`; the exact `C_occ`: OccupationCeilingExact; OccupationCeilingFinite) | `T:intrinsic-occupation-ceiling` (narrower result: `K_0 R_sp` (or `K_0 R_0`) in place of `C_occ`; the occupation-energy form, `C_2 <= U_2` and the rate and cost identification not formalized; on the named input `SpaceTimeCS`, discharged in `L8Completed`; the exact `C_occ`: OccupationCeilingExact; OccupationCeilingFinite) |
| 769 | `C:intrinsic-spatial-bracket` (narrower result for `S_2^pos`, not `C_2`; named input `OccupationCeilingK0`, discharged in `L8Completed`) | `C:intrinsic-spatial-bracket` (narrower result: `S_2^pos` in place of `C_2`, `energyValue(K_0 R_sp)` in place of `E_(1/2)^O`, rate and cost identification not formalized; named input `OccupationCeilingK0`, discharged in `L8Completed`) |
| 772 | `P:variational-remove-mask` (part of a result: the rates with nothing supplied, in Rayleigh form; the point display over the named input `RawBlockOriginalLower`, with a real function standing in for the point moment) | `P:variational-remove-mask` (narrower result: the rates with nothing supplied, in Rayleigh form, with integral-form costs, their identification not formalized; the point display over the named input `RawBlockOriginalLower`, with a real function standing in for the canonical solution's point moment) |
| 785 | `L:terminal-wick` (TerminalWick) | `L:terminal-wick` (narrower result: real `r` only; comparison per mixed moment; chain measures specified by their masses, `hmeas` supplied; the Wick formula additionally assumes `hK`; TerminalWick) |
| 801 | `T:intrinsic-occupation-ceiling` (completion wrappers: `K_0 R_sp` in place of `C_occ`, nothing supplied; L8Completed) | `T:intrinsic-occupation-ceiling` (narrower result: `K_0 R_sp` in place of `C_occ`; the occupation-energy form, `C_2 <= U_2` and the rate and cost identification not formalized; completion wrappers, nothing supplied; L8Completed) |
| 802 | `P:variational-positive-scores` (completion wrappers: the boundedness claim `S1Bdd` and the supremum statements, nothing supplied; `Q_2 >= S_2^pos` not formalized; L8Completed) | `P:variational-positive-scores` (narrower result: completion wrappers for the boundedness claim `S1Bdd` and the supremum statements, nothing supplied; `Q_2 >= S_2^pos` and the rate and cost identification not formalized; L8Completed) |
| 807 | `E:intrinsic-spatial-bracket` (completion wrappers for `S_2^pos`, nothing supplied; L8Completed) | `E:intrinsic-spatial-bracket` (narrower result: `S_2^pos` in place of `C_2`, rate and cost identification not formalized; completion wrappers, nothing supplied; L8Completed) |
| 808 | `C:intrinsic-spatial-bracket` (completion wrapper for `S_2^pos`, not `C_2`, nothing supplied; L8Completed) | `C:intrinsic-spatial-bracket` (narrower result: `S_2^pos` in place of `C_2`, `energyValue(K_0 R_sp)` in place of `E_(1/2)^O`, rate and cost identification not formalized; completion wrapper, nothing supplied; L8Completed) |
| 840 | `T:intrinsic-occupation-ceiling` (narrower result: both forms of `E:occupation-score-ceiling` with the exact `C_occ` for `S_c^pos`, nothing supplied; `C_2(Gamma,a) <= U_2` not formalized; `O` modelled by `IsOccField`; OccupationCeilingExact) | `T:intrinsic-occupation-ceiling` (narrower result: both forms of `E:occupation-score-ceiling` with the exact `C_occ` for `S_c^pos`, nothing supplied; `C_2(Gamma,a) <= U_2` and the rate and cost identification not formalized; `O` modelled by `IsOccField`; OccupationCeilingExact) |
| 841 | `C:intrinsic-spatial-bracket` (narrower result: the comparison with the exact `E_(1/2)^O` for `S_2^pos`, not `C_2`, nothing supplied; OccupationCeilingExact) | `C:intrinsic-spatial-bracket` (narrower result: the comparison with the exact `E_(1/2)^O` for `S_2^pos`, not `C_2`, rate and cost identification not formalized, nothing supplied; OccupationCeilingExact) |
| 860 | `L:fock-form` (general form and exact-hypothesis wrapper, inputs supplied: the spatial column bound `FockColumn`; FockForm) | `L:fock-form` (narrower result: coefficient model of the `m` multiplied coordinates, symmetry without self-adjoint packaging, spatial operators not constructed; general form and exact-hypothesis wrapper, inputs supplied: the spatial column bound `FockColumn`; FockForm) |
| 861 | `L:interval-contractions` (general form and exact-hypothesis wrapper, inputs supplied: `E:interval-column` as `FockColumn`; FockForm) | `L:interval-contractions` (narrower result: coefficient model of finitely many modes, spatial operators not constructed; general form and exact-hypothesis wrapper, inputs supplied: `E:interval-column` as `FockColumn`; FockForm) |
| 865 | `L:finite-word-cutoff` (the Fock model, one Gaussian mode per color, single finite words; nothing supplied; HermiteWordFock) | `L:finite-word-cutoff` (narrower result: one Gaussian mode per color and single finite words; finite sums and Bochner integrals not formalized; nothing supplied; HermiteWordFock) |
| 477 | `C:intrinsic-spatial-bracket` | `C:intrinsic-spatial-bracket` (proof steps: scalar logarithmic gap only; RawValueCeiling) |
| 478 | `E:driver-parameters` | `E:driver-parameters` (proof steps; InteractionDriver) |
| 479 | `L:driver-holder-limit` | `L:driver-holder-limit` (proof steps; InteractionDriver) |
| 480 | `L:driver-interval-limit` | `L:driver-interval-limit` (proof steps; InteractionDriver) |
| 481 | `E:kappa` (lower inequality) | `E:kappa` (proof steps: lower inequality; DirectEvent) |
| 482 | `L:exact-canonical-scaling` | `L:exact-canonical-scaling` (proof steps; DirectEvent) |
| 483 | `L:finite-word-cutoff` | `L:finite-word-cutoff` (proof steps; HermiteWord) |
| 484 | `L:gaussian-scalar-powers` | `L:gaussian-scalar-powers` (proof steps; FiniteYoung) |
| 485 | `L:gram-scalar-algebra` | `L:gram-scalar-algebra` (proof steps; PositiveGram) |
| 486 | `L:masked-trig-products` (cosine-cosine case) | `L:masked-trig-products` (proof steps: cosine-cosine case; PhaseResponse) |
| 487 | `L:raw-block-indexed-cone` (scalar steps) | `L:raw-block-indexed-cone` (proof steps: scalar steps; MovingCone) |
| 488 | `L:raw-block-inputs` | `L:raw-block-inputs` (proof steps; JointTilt) |
| 489 | `L:raw-block-restart` | `L:raw-block-restart` (proof steps; ActualEvent) |
| 490 | `L:temporal-equilibrium` (with `alpha` = `a`) | `L:temporal-equilibrium` (proof steps: with `alpha` = `a`; LocalFlow) |
| 491 | `L:tube-rayleigh-tail` | `L:tube-rayleigh-tail` (proof steps; GaussianTail) |
| 492 | `L:variational-control-dilation` (exponent step) | `L:variational-control-dilation` (proof steps: exponent step; RawVariational) |
| 493 | `P:clock-copy-obstruction` (scalar steps) | `P:clock-copy-obstruction` (proof steps: scalar steps; ClockFilter) |
| 494 | `P:actual-wave-form` | `P:actual-wave-form` (proof steps; DimensionalMatrix) |
| 495 | `P:gram-entrywise-comparison` | `P:gram-entrywise-comparison` (proof steps; PositiveGram) |
| 496 | `P:gram-positive-optimizer` | `P:gram-positive-optimizer` (proof steps; PositiveGram) |
| 497 | `P:radius-mean-anchor` (case `d = 2`) | `P:radius-mean-anchor` (proof steps: case `d = 2`; InteractionDriver) |
| 498 | `P:raw-block-original-lower` | `P:raw-block-original-lower` (proof steps; ActualEvent) |
| 499 | `P:variational-positive-scores` | `P:variational-positive-scores` (proof steps; RawVariational) |
| 500 | `P:white-spatial-energy` | `P:white-spatial-energy` (proof steps; WhiteCDF) |
| split | P:spatial-four-linear (completion wrappers, nothing supplied) | helper row (hsm kept) + narrower wrapper row |
| split | E:spatial-square-CS (completion wrappers, nothing supplied) | helper row (SquareBound kept) + wrapper row |
| addendum | `L:raw-block-indexed-cone` (whole result; rows labelled with the lemma or its proof) | `L:raw-block-indexed-cone` (narrower result: abstract ground family, its identification with the physical wave family not formalized; rows labelled with the lemma or its proof) |
| addendum | `P:masked-quotient-obstruction` (whole result) | `P:masked-quotient-obstruction` (narrower result: covariance-functional obstruction; noise `W` not constructed, identification with noise variances not formalized) |
| addendum | `L:uniform-series-tail` (whole result; the two facts | `L:uniform-series-tail` (narrower result: an abstract `L^2` family, identification with the terminal-chain terms not formalized; the two facts |
| addendum | `L:uniform-series-tail` (combined with `L:terminal-wick` for nonnegative covariance; L8Completed) | `L:uniform-series-tail` (narrower result: combined with `L:terminal-wick` for nonnegative covariance, chain measures fixed only by their masses; L8Completed) |

## Re-review round 4, e2c50b5

Reviews h1, h2, h3, h4a-d and h5 were run on e2c50b5. Le's decision (2026-11-12): every Index-by-label first cell starts with one of "whole result", "narrower result: …", "foundation: …" or "proof steps: …". The category is derived from the section heading, with per-row overrides where a row's declarations differ, and mixed rows are split. Le also applied the split rule to RadiusMeanAnchor and to the two TypeContinuity moment results. Only documentation changed, no Lean.

| Review | Finding | Sev | Decision | Change |
|---|---|---|---|---|
| h1 | K1 L8Completed heading | major | ACCEPTED | The heading appends "the occupation-energy form of the ceiling and `Q_2 >= S_2^pos` not formalized". |
| h3 | K1 register text | major | ACCEPTED | README states M1 with the surface-measure disclaimer, both in the WaveGreen description and in a register note before the two M1 results. FORMALIZATION states M1 and the rule that a registered standard choice preserves whole status only with the model named, while a missing construction makes a result narrower. |
| h3 | K2 RadiusMeanAnchor | major | ACCEPTED (Le's split rule) | The heading and Index cell are narrower: abstract random paths, `M_R(Y_m)` and residual noises not constructed. The coverage row is inputs-supplied/weaker with a scope sentence and TeX mirror, and the note no longer says "exactly". |
| h3 | K3 TypeContinuity | major | ACCEPTED (Le's split rule) | The heading is narrower for P:moment-growth-logconvex and C:static-moment-constant-continuity (abstract moment function, solution moments not constructed), with L:positive-series-type kept whole. Both coverage rows are weaker with scopes and mirrors, and the Index cells (including E:moment-growth-types) are narrower. |
| h4a | K1 37 cells without category | major | ACCEPTED | All cells are categorized (see below). Cell 549 now reads "narrower result: integral-form cost only; identification with `E W(Psi)^2` not formalized"; cell 550 reads "narrower result: Rayleigh-form rate only; spectral-bottom identification `-E_s` not formalized". |
| h4a | K2 integrability transfers labelled L:variational-control-dilation | major | ACCEPTED | The Index cell is now "no direct label (foundation: Lean-route integrability-transfer auxiliaries supporting `L:variational-control-dilation`; conditional transfers only, not stated in the TeX)". The 7 table rows are relabelled "no direct label (…)". Totals are now 1303 labelled and 1165 unlabelled, updated in the ledger Totals and README. |
| h4b | K1 row 610 | fatal | ACCEPTED | The row is split. The completed theorem is a whole result with nothing supplied. The abstract wrapper with `hmem`, `hnorm` and the abstract E/V/emb, together with its helpers, is now "proof steps". |
| h4b | K2 66 cells without category | major | ACCEPTED | All cells are categorized. |
| h4b | K3 whole-result cells in narrower sections (613-614, 622, 646-647, 652) | major | ACCEPTED | Each is now "proof steps: <display> in full; section … is a narrower result". |
| h4b | K4 damped-norm rows 620/639 | major | ACCEPTED | Row 620 is narrower: the DampedNormsHomog wrapper omits the general multiplier lower bounds and the smoothing identifications. Row 639 (foundation) says that `damped_homogeneous_norms_wave` omits the lower bounds and the smoothing remark. |
| h4c | K1 57 cells without category | major | ACCEPTED | All cells are categorized. |
| h4c | K2 row 788, rows 771/772/774 | major | ACCEPTED | Row 788 is now "proof steps: the scalar map `F_b` in full; section SpatialBracket is a narrower result". Rows 771, 772, 773 and 774 are now foundation cells that keep their integral-form restrictions. |
| h4c | K3 rows 764 and 780 | major | ACCEPTED | Row 764 is split. The input-free wrappers with nothing supplied are separated from the general forms that keep `GreenMass G` or `GreenFourier G` (proof steps). Row 780 is now "conditional on the smooth homogeneous bound `hR` as a hypothesis". |
| h4c | K4 rows 730-731 constant | major | ACCEPTED | These rows describe the general form for any `R` with `SquarePairingBounds Gamma alpha R`, and that the paper wrapper specializes R = R_0 (identified with R_sp). |
| h4d | K1 row 894 | fatal | ACCEPTED | The row is split. `traceT_fourier_completed` is now "proof steps: the Fourier identity of `T_eps` only". The two phase_contractions completed theorems stay "whole result with nothing supplied; registered model choice M1". |
| h4d | K2 64 cells without category | major | ACCEPTED | All cells are categorized. Lines 801 (FiniteWick) and 875 are covered. |
| h4d | K3 rows 859-860, 865 | major | ACCEPTED | These cells name the class-O bridge, and the rate and cost identifications, or refer to the qualified section. The general forms taking `SquarePairingBounds` are split from the wrappers with nothing supplied (rows 860 and 861). |
| h4d | K4 rows 886 and 816 | major | ACCEPTED | Row 886 is split: `FockColumn`, its compression and the input-free `fock_const_eq` are proof steps, and the consumers are narrower with inputs supplied. Row 816 is split: the input-free `orderedProd` definition is separate. Row 819 is also split: the input-free force-skew wrapper is separate from the baseline wrapper with inputs. |
| h5 | K1 rows 875-876, 752, 754-755 | major | ACCEPTED | Rows 875-876 are narrower, with the propagator gap, the telescoping gap (876) and the named inputs. Rows 752 and 754 are proof steps (helpers keep `hsm` or `SquareBound`). Row 755 is narrower, with nothing supplied. |
| h5 | K2 row 775 | major | ACCEPTED | Now "foundation: definition of `K_0` and the iterated physical space-time form only; `J_G` and its covariance-space norm identity not formalized". |
| h5 | K3 MovingCone wording | minor | ACCEPTED | "whole lemma" becomes "abstract cone statement" in both places. The RadiusMeanAnchor reference in InteractionDriver now says "a narrower result". |

**Category check.** The checker is `<HOME>/.local/state/tmp/claude-1247658/-<HOME>-Dropbox-workspace-svn-Article-Stratonovich-HAM-Second-Moment/4c4c8276-f434-4c95-9605-690953ef166f/scratchpad/l9/index_category_check.py`. It is kept in scratch and is not added to the repository. Rules:
- R1: every first cell has a category word.
- R2: "whole result" requires a full coverage row, or no row and whole-result sections only.
- R3: "narrower result" requires a row that is not full and a narrower-result section, unless the cell says override.
- R4: no labelled-result category in foundation or proof-step sections.
- R5: "nothing supplied" may not cover a theorem whose Lean binders take a named input (named Prop inputs such as GreenMass, FockColumn, SquareBound and S1Bdd, and named binders such as hmem, hnorm, hsm, hborn, hcoef and hCPC). "inputs supplied" may not cover a theorem that takes none. References inside "section X (…)" are ignored. This check is best effort.

Output: "cells checked: 402; problems: 0".

**Auto-categorized cells.** 255 first cells had no category. A script assigned them from the section heading and the label's coverage row: 57 "proof steps", 4 "whole result", 108 "foundation", 86 "narrower result". The full old → new list is in <HOME>/.local/state/tmp/claude-1247658/-<HOME>-Dropbox-workspace-svn-Article-Stratonovich-HAM-Second-Moment/4c4c8276-f434-4c95-9605-690953ef166f/scratchpad/l9/autocat.json. 38 cells were then rewritten or split by hand (table below), and 4 more cells for RadiusMeanAnchor and TypeContinuity.

**Counts.**

| | Count |
|---|---|
| Coverage rows (class unchanged) | 47 same / 30 inputs / 3 outside |
| Conclusion changes | P:radius-mean-anchor, P:moment-growth-logconvex, C:static-moment-constant-continuity full → weaker |
| COMPLETION labelled results | 25 / 18 / 0 / 30 / 3 / 144, total 220 |
| Modules: whole result | 27 (559 theorems, 135 definitions), none with inputs |
| Modules: narrower, plus HermiteWordFock | 31 (943, 199) |
| Modules: foundation or proof steps | 18 (466, 78) |
| Audit step modules | 23 (82, 6) |
| Ledger headings | 24 whole, 32 narrower, 34 foundation or proof steps |

The coverage summary now reads twenty-nine with every conclusion (25 plus the four E:/R: rows), eighteen narrower, and steps or parts of 30.

### Headings changed

| Module | Old | New |
|---|---|---|
| L8Completed | (narrower results: `K_0 R_sp` in place of `C_occ`, `S_2^pos` in place of `C_2`, `energyValue(K_0 R_sp)` in place of `E_(1/2)^O`, Rayleigh-form rate and integral-form cost not identified; `L:uniform-series-tail` with chain measures fixed only by their masses) | (narrower results: `K_0 R_sp` in place of `C_occ`, `S_2^pos` in place of `C_2`, `energyValue(K_0 R_sp)` in place of `E_(1/2)^O`, Rayleigh-form rate and integral-form cost not identified; the occupation-energy form of the ceiling and `Q_2 >= S_2^pos` not formalized; `L:uniform-series-tail` with chain measures fixed only by their masses) |
| RadiusMeanAnchor | (whole result) | (narrower result: `P:radius-mean-anchor` for abstract random paths; the operator paths `M_R(Y_m)` and the residual noises not constructed, their identification not formalized; moment inputs supplied) |
| TypeContinuity | (whole result) | (narrower result: `P:moment-growth-logconvex` and `C:static-moment-constant-continuity` for an abstract moment function, the solution moments not constructed and their identification not formalized; `L:positive-series-type` whole) |

### Cells rewritten or split by hand (old first cell → new first cell(s))

| Old | New |
|---|---|
| `L:variational-control-dilation` (narrower result, see section `VariationalDilation`; Lean-route integrability auxiliaries, not stated in the TeX; conditional transfers only) | no direct label (foundation: Lean-route integrability-transfer auxiliaries supporting `L:variational-control-dilation`; conditional transfers only, not stated in the TeX) |
| `E:compact-raw-cost` (narrower result, see section `VariationalDilation`; integral form only; `v = E W(Psi)^2` is not formalized) | `E:compact-raw-cost` (narrower result: integral-form cost only; identification with `E W(Psi)^2` not formalized) |
| `E:variational-real-rayleigh` (narrower result, see section `VariationalDilation`; right side defined in Lean; its equality with `-E_s` is not formalized) | `E:variational-real-rayleigh` (narrower result: Rayleigh-form rate only; spectral-bottom identification `-E_s` not formalized) |
| `L:masked-continuous-wave` (whole result; no supplied input) | `L:masked-continuous-wave` (whole result with nothing supplied: the completed theorem) // `L:masked-continuous-wave` (proof steps: the abstract wrapper `masked_continuous_wave_paper` keeps `hmem` and `hnorm` and works on an abstract space `E`, `V`, `emb`, discharged by the completed theorem; and its scalar helpers and definitions) |
| `E:masked-auxiliary-measure` (whole result) | `E:masked-auxiliary-measure` (proof steps: the display defining `rho_R` and `nu_R` in full; section MaskedAuxiliaryNorm is a narrower result) |
| `E:masked-auxiliary-growth` (whole result) | `E:masked-auxiliary-growth` (proof steps: the ball bound in full; section MaskedAuxiliaryNorm is a narrower result) |
| `L:damped-homogeneous-norms` (proof steps: `DampedNormsHomog`: for an arbitrary family `G` with `GreenMass G` as hypothesis, discharged by `WaveGreen` (rows below); the proof steps of `E:damped-multiplier-comparison`) | `L:damped-homogeneous-norms` (narrower result: `DampedNormsHomog` wrapper for an arbitrary family `G` with `GreenMass G` as hypothesis, discharged by `WaveGreen`; it proves the upper bounds of `E:damped-multiplier-comparison` but omits the general multiplier lower bounds and the smoothing identifications; with its proof steps) |
| `E:damped-tail-norms` (whole result) | `E:damped-tail-norms` (proof steps: the tail norms and their limits in full; section DampedNormsHomog is a narrower result) |
| `L:damped-homogeneous-norms` (foundation: with nothing supplied except the smoothing remark, see `DampedMultiplier`; the mass identity of line 881 and `N_0`, built on `WaveGreen.waveGreen`) | `L:damped-homogeneous-norms` (foundation: the mass identity of line 881 and `N_0` for `WaveGreen.waveGreen`, and the wrapper `damped_homogeneous_norms_wave`, which omits the general multiplier lower bounds and the smoothing remark (see `DampedMultiplier`)) |
| `E:variance-normalized-kernel` (whole result) | `E:variance-normalized-kernel` (proof steps: the kernel display in full; section WaveTwoVariances is a narrower result) |
| `E:variance-kernel-time-bound` (whole result) | `E:variance-kernel-time-bound` (proof steps: the time bound in full; section WaveTwoVariances is a narrower result) |
| `E:variance-actual-growth-constant` (whole result) | `E:variance-actual-growth-constant` (proof steps: the growth constant in full; section WaveTwoVariances is a narrower result) |
| `E:occupation-physical-bound` (narrower result, with `R_0` for `R_sp`) | `E:occupation-physical-bound` (narrower result: general form for any constant `R` with `SquarePairingBounds Gamma alpha R` as hypothesis, conclusion with `Rstar a D * R`; the paper wrapper specializes `R = R_0`, identified with `R_sp` by `spatial_ratio_H1_paper_completed`; class `O` modelled by joint representatives) |
| `E:occupation-own-energy` (narrower result over the modelled class, bound with `spEnergyVal alpha R_0` for `E_sp`) | `E:occupation-own-energy` (narrower result: general form for any constant `R` with `SquarePairingBounds Gamma alpha R`, bound `spEnergyVal alpha R`; the paper wrapper specializes `R = R_0`, giving `E_sp`; class `O` modelled by joint representatives) |
| `C:static-interaction` (proof steps and the definitions of the statement; inputs supplied; section IntervalScalar (proof steps of `C:static-interaction` and `P:interval-coefficients`, inputs supplied; `E:static-block-series` in full)) | `C:static-interaction` (proof steps: the definitions of the statement and scalar helpers, which take no input; the step rows below take the supplied inputs; section IntervalScalar (proof steps of `C:static-interaction` and `P:interval-coefficients`, inputs supplied; `E:static-block-series` in full)) |
| `P:spatial-four-linear` (narrower result, see section `SpatialOccupationL7Completed`; completion helper; only the density input discharged, the smooth-test pairing bound `hsm` kept as a hypothesis) | `P:spatial-four-linear` (proof steps: completion helper; only the density input discharged, the smooth-test pairing bound `hsm` kept as a hypothesis) |
| `E:spatial-square-CS` (narrower result, see section `SpatialOccupationL7Completed`; general completion helpers; only the density input discharged, `SquareBound` kept as a hypothesis) | `E:spatial-square-CS` (proof steps: general completion helpers; only the density input discharged, `SquareBound` kept as a hypothesis) |
| `E:spatial-square-CS` (narrower result, see section `SpatialOccupationL7Completed`; completion wrapper with the proposition's hypotheses, nothing supplied) | `E:spatial-square-CS` (narrower result, see section `SpatialOccupationL7Completed`: the display with the proposition's hypotheses, nothing supplied; rate and cost and class `O` identifications not formalized) |
| `L:damped-homogeneous-norms` (narrower result, see section `DampedMultiplier`; `DampedMultiplier`: with nothing supplied, the full multiplier comparison and the smoothing assertions of lines 845-847 and 915-917 in a narrower reading: covariance smoothing as multiplier membership only, the smoothed Green norm identified with `N_{2,m,S}` in `d = 1` by `fourier_one`, and in `d = 1, 2, 3` by `WaveGreenFourier.damped_homogeneous_norms_fourier_wave`) | `L:damped-homogeneous-norms` (narrower result, see section `DampedMultiplier`: wrappers with nothing supplied; covariance smoothing as multiplier membership only, the smoothed Green norm identified with `N_{2,m,S}` in `d = 1` by `fourier_one` and in `d = 1, 2, 3` by `WaveGreenFourier.damped_homogeneous_norms_fourier_wave`; the general multiplier lower bounds are in `damped_multiplier_comparison`) // `L:damped-homogeneous-norms` (proof steps: general forms for a family `G`, keeping `GreenMass G` or `GreenFourier G` as hypotheses, discharged for the wave Green measures by the wrappers of the row above) |
| `E:occupation-raw-identities` (narrower result: second identity in integral form for continuous compactly supported fields, nothing supplied; SpaceTimePositivity) | `E:occupation-raw-identities` (foundation: second identity in integral form for continuous compactly supported fields, nothing supplied; the Hilbert-space objects of the TeX not constructed; SpaceTimePositivity) |
| `E:positive-raw-mean` (narrower result: first identity in integral form, nothing supplied; SpaceTimePositivity) | `E:positive-raw-mean` (foundation: first identity in integral form, nothing supplied; the Hilbert-space objects of the TeX not constructed; SpaceTimePositivity) |
| `L:occupation-raw-square` (foundation: narrower form for continuous compactly supported fields in place of the class `O`, nothing supplied; no coverage row, the profile class differs; SpaceTimePositivity) | `L:occupation-raw-square` (foundation: the final display for continuous compactly supported fields in place of the class `O`, nothing supplied; no coverage row, the profile class differs; SpaceTimePositivity) |
| `L:positive-raw-embedding` (narrower result: the variance identity in integral form, nothing supplied; SpaceTimePositivity) | `L:positive-raw-embedding` (foundation: the variance identity in integral form, nothing supplied; `J_G` not constructed; SpaceTimePositivity) |
| `E:positive-bochner-inclusion` (narrower result: the constant `K_0` and the iterated space-time form; OccupationCeilingFinite) | `E:positive-bochner-inclusion` (foundation: definition of `K_0` and the iterated physical space-time form only; `J_G` and its covariance-space norm identity not formalized; OccupationCeilingFinite) |
| `P:raw-occupation-energy` (proof steps of a narrower result: the square bound for smooth unit tests, nothing supplied; OccupationCeilingFinite) | `P:raw-occupation-energy` (proof steps of a narrower result: the square bound for smooth unit tests, conditional on the smooth homogeneous bound `hR` as a hypothesis; OccupationCeilingFinite) |
| `E:occupation-scalar-map` (whole result) | `E:occupation-scalar-map` (proof steps: the scalar map `F_b` in full; section SpatialBracket is a narrower result) |
| `E:symplectic-compact-product-baseline` (narrower result, see section `SymplecticFree`; the ordered product, general form and exact-hypothesis wrapper, inputs supplied; section SymplecticFree (narrower result: `J_E`, the duality-form identification and symplectic preservation on `E` not formalized; force skewness only at the `L^2` level; free-group data and Young convergence supplied)) | `E:symplectic-compact-product-baseline` (proof steps: the ordered product, an input-free definition) // `E:symplectic-compact-product-baseline` (narrower result, see section `SymplecticFree`: general form and exact-hypothesis wrapper, inputs supplied) |
| `L:symplectic-free` (narrower result, see section `SymplecticFree`; exact-hypothesis wrappers, inputs supplied; section SymplecticFree (narrower result: `J_E`, the duality-form identification and symplectic preservation on `E` not formalized; force skewness only at the `L^2` level; free-group data and Young convergence supplied)) | `L:symplectic-free` (narrower result, see section `SymplecticFree`: the force-skewness wrapper at the `L^2` level, input-free) // `L:symplectic-free` (narrower result, see section `SymplecticFree`: exact-hypothesis wrapper of the baseline, inputs supplied) |
| `E:raw-occupation-bound` (narrower result: general form on the hypothesis `SquarePairingBounds`, proved under `H:homog`; RawOccupationEnergy) | `E:raw-occupation-bound` (narrower result: general form with `SquarePairingBounds` as hypothesis, proved under `H:homog`; class `O` modelled by joint representatives, bridge not formalized; RawOccupationEnergy) |
| `P:raw-occupation-energy` (proof steps of a narrower result: positivity, the dilation `U_l` and the scalar maximum, nothing supplied; RawOccupationEnergy) | `P:raw-occupation-energy` (proof steps of a narrower result: positivity witness `exists_pos_member`, conditional on `SquarePairingBounds` as hypothesis; class `O` bridge not formalized; RawOccupationEnergy) // `P:raw-occupation-energy` (proof steps of a narrower result: positivity, the dilation `U_l` and the scalar maximum, nothing supplied; class `O` bridge not formalized; RawOccupationEnergy) |
| `P:raw-occupation-energy` (narrower result: general form and exact-hypothesis wrapper, nothing supplied; `O` modelled by `IsOccField`; RawOccupationEnergy) | `P:raw-occupation-energy` (narrower result: general form with `SquarePairingBounds` as hypothesis; class `O` modelled by `IsOccField`, bridge not formalized; RawOccupationEnergy) // `P:raw-occupation-energy` (narrower result: exact-hypothesis wrapper, nothing supplied; class `O` modelled by `IsOccField`, bridge not formalized; RawOccupationEnergy) |
| `T:intrinsic-occupation-ceiling` (proof steps of a narrower result: the first scalar maximum with the exact `C_occ`, nothing supplied; OccupationCeilingExact) | `T:intrinsic-occupation-ceiling` (proof steps of a narrower result: the first scalar maximum with the exact `C_occ`, nothing supplied; class `O` bridge and rate and cost identification not formalized, see section OccupationCeilingExact) |
| `L:complex-phase` (proof steps) (scalar, numerical-range and Banach-algebra steps: constants, scalar resolvent integral, Neumann bounds, resolvent identity, parabola, scalar bounds, assembly constants; nothing supplied; ComplexPhaseScalar) | `L:complex-phase` (proof steps: scalar, numerical-range and Banach-algebra lemmas, each with its premises as hypotheses (the inverse-root representation where used): constants, scalar resolvent integral, Neumann bounds, resolvent identity, parabola, scalar bounds, assembly constants; ComplexPhaseScalar) |
| `L:interval-complex` (proof steps) (Neumann bounds `7/6`, `6/5`, form bounds, adjoint sandwich, phase-weight change and jump ratio; nothing supplied; ComplexPhaseScalar) | `L:interval-complex` (proof steps: Neumann bounds `7/6`, `6/5`, form bounds, adjoint sandwich, phase-weight change and jump ratio, each with its premises as hypotheses; ComplexPhaseScalar) |
| `L:complex-phase` (narrower result, see section `ComplexPhaseScalar`; exact-hypothesis wrappers: the numerical-range layer with nothing supplied; the propagator layer with `E:cp-input` and the inverse-root representation supplied, concluded for the weighted block map, not `M_z(h)`; ComplexPhaseScalar) | `L:complex-phase` (narrower result: block map not identified with the propagator `M_z(h)`; exact-hypothesis wrappers: the numerical-range layer with nothing supplied, the propagator layer with the named inputs `E:cp-input` and the inverse-root representation; ComplexPhaseScalar) |
| `L:interval-complex` (narrower result, see section `ComplexPhaseScalar`; exact-hypothesis wrappers: the numerical-range layer with nothing supplied; the propagator layer with `E:cp-input` and the inverse-root representation supplied, concluded for the weighted block map, not the propagator in `X_Lambda`; ComplexPhaseScalar) | `L:interval-complex` (narrower result: block map not identified with the propagator in `X_Lambda`, interval-norm telescoping not formalized; exact-hypothesis wrappers: the numerical-range layer with nothing supplied, the propagator layer with the named inputs `E:cp-input` and the inverse-root representation; ComplexPhaseScalar) |
| `L:fock-form` (narrower result: coefficient model of the `m` multiplied coordinates, symmetry without self-adjoint packaging, spatial operators not constructed; general form and exact-hypothesis wrapper, inputs supplied: the spatial column bound `FockColumn`; FockForm) | `L:fock-form` (proof steps: the column-bound predicate `FockColumn`, its band compression and the input-free normalization `fock_const_eq` of `d_N`; FockForm) // `L:fock-form` (narrower result: coefficient model of the `m` multiplied coordinates, symmetry without self-adjoint packaging, spatial operators not constructed; general form and exact-hypothesis wrapper, inputs supplied: the spatial column bound `FockColumn`; FockForm) |
| `L:phase-contractions` (whole result with nothing supplied; the Fourier form of `T_eps`; L9Completed) | `L:phase-contractions` (proof steps: the Fourier identity of `T_eps` only, nothing supplied; L9Completed) // `L:phase-contractions` (whole result with nothing supplied; registered model choice M1; L9Completed) |
| `P:radius-mean-anchor` (whole result) | `P:radius-mean-anchor` (narrower result: abstract random paths, `M_R(Y_m)` and the residual noises not constructed; moment inputs supplied) |
| `E:moment-growth-types` (whole result) | `E:moment-growth-types` (narrower result: the growth types of an abstract moment function; the solution moments not constructed) |
| `P:moment-growth-logconvex` (whole result) | `P:moment-growth-logconvex` (narrower result: an abstract moment function, the solution moments not constructed and their identification not formalized; inputs supplied) |
| `C:static-moment-constant-continuity` (whole result) | `C:static-moment-constant-continuity` (narrower result: an abstract moment function, the solution moments not constructed and their identification not formalized; inputs supplied) |

## Re-review round 5, 350d191

Round 5 found 0 fatal and 18 major findings, most of them mixed Index rows. The fix was systematic, and documentation only (no Lean).

**Method.**
1. `<HOME>/.local/state/tmp/claude-1247658/-<HOME>-Dropbox-workspace-svn-Article-Stratonovich-HAM-Second-Moment/4c4c8276-f434-4c95-9605-690953ef166f/scratchpad/l9/decltable.py` builds a per-declaration table for all 2431 Index-listed declarations (the other 37 are in the aggregate audit row). For each declaration it records: name; kind; label (from the Index row; it agrees with the section table, checked by index_check); category; whether it is a statement wrapper (`*_paper`, `*_completed`); and its supplied-input set.
   - The supplied-input set is read from the Lean binders before the final colon. It counts named Prop inputs (GreenMass, GreenFourier, FockColumn, SquareBound, SquarePairingBounds, SpaceTimeCS, S1Bdd, StaticControls, RayleighFloor, OccupationCeilingK0, InventoryProduct, H1TestDense, TerminalWickInput, RawBlockOriginalLower, TypeContinuityInputs, LeftYoungSumsConverge, FreeWaveData, GroundFamily, WaveFourierThree, ArchimedesLaw).
   - It also counts, per module, the h-binders that carry supplied analytic inputs, for example hmem/hmod/hnorm, hborn/hmean/hY/hodd/hfirst/hstep, hsplits/hfixed, hCPC/hCPF/hCPH/hJ, hlink/hJL2, hmass/hmeas/hK, hTW/hsum/hpos, hsm, and hR in OccupationCeilingFinite.
2. `<HOME>/.local/state/tmp/claude-1247658/-<HOME>-Dropbox-workspace-svn-Article-Stratonovich-HAM-Second-Moment/4c4c8276-f434-4c95-9605-690953ef166f/scratchpad/l9/regen_index.py` regenerates the rows. Declarations are grouped only when category, kind class (definition or theorem), role and input set are all identical:
   - Definitions are always "proof steps: definitions…" or "foundation".
   - In a whole or narrower row, only the statement wrappers keep that category. General forms and supporting lemmas become "proof steps: general forms and supporting lemmas…".
   - Each generated qualifier names its group's inputs ("with `x` as hypotheses"), or says "no named analytic input, premises as stated".
   - The original human qualifier is kept on each row's main group. Inputs it did not name are appended as "hypotheses kept: …".
   - Result: 179 rows split into 252 new rows. Index rows went from 403 to 657 (including the later hand splits).
3. 31 cells were then rewritten or split by hand for the specific findings (table below).

**Checker (extended).** `<HOME>/.local/state/tmp/claude-1247658/-<HOME>-Dropbox-workspace-svn-Article-Stratonovich-HAM-Second-Moment/4c4c8276-f434-4c95-9605-690953ef166f/scratchpad/l9/index_category_check.py` has no exemption; the aggregate audit row must carry a category. It now builds the per-declaration table itself and adds these rules:
- R6: a row may not mix definitions and theorems.
- R7: a row may not mix input sets.
- R8: no definitions in a whole or narrower row.
- R9: no wrapper together with supporting or general theorems in a whole or narrower row.
- R10: the qualifier names every input of its row.
- R11: "nothing supplied" may not appear over declarations that take inputs, unless they are disclosed.
- R12: "inputs supplied" may not appear when no declaration takes an input.

R1-R4 are kept. The old R5 heuristic, whose generic binder list gave false positives, is replaced by R6-R12. Output: **"cells checked: 657; problems: 0"**.

| Review | Finding | Sev | Decision | Change |
|---|---|---|---|---|
| h1 | K1 TypeContinuity prose | minor | ACCEPTED | Now "Every conclusion formula is proved for the abstract moment function; its identification with the solution moments is not formalized." |
| h2 | K1 DampedNormsHomog heading | major | ACCEPTED | The heading adds "without the general multiplier lower bounds, which are in `DampedMultiplier`". The WaveGreen paragraph (former 1940-1942) says that `damped_homogeneous_norms_wave` omits the lower bounds and the smoothing remark. |
| h2 | K2 coverage header count | major | ACCEPTED | Now 1168. The count moved from 1165 to 1168 this round because 3 further declarations are now unlabelled (below). |
| h2 | K3 aggregate row | major | ACCEPTED | Now "no direct label (foundation: unlabelled audit facts of the modules listed…)". The checker exemption is removed. |
| h2 | K4 M1 in cells | major | ACCEPTED | The whole-result cells of `L:low-alpha-convolution` (LowAlphaConvolution, L9Completed) and `L:phase-contractions` (PhaseContractions, L9Completed) name "registered model choice M1". So do the inputs cells of their five section-table rows. |
| i1 | K1 masked-trig-products row | major | ACCEPTED | The row is split. The completed theorem is whole with nothing supplied. The two abstract wrappers are proof steps, with `hmem`/`hmod` and `hmem`/`hnorm` as hypotheses. |
| i2 | K1 masked-time-completion definitions | major | ACCEPTED | Now "proof steps: definitions of the temporal form and kernel only". |
| i2 | K2 mixed whole rows (596, 637, 631, 593, 595, 597, 603, 605, 610, 611) | major | ACCEPTED | Split by the regeneration. Wrappers stay whole; general forms and lemmas, such as frequencyPair_le_two, phase_bessel and phase_bessel_conj, and heat_envelope without positivity, are proof steps; definitions are separate. |
| i2 | K3 rows 621, 632, 635 | major | ACCEPTED | These are proof steps with their own scope: the closed-ball mass bound only; the Fourier identity only; the trial-set membership criterion only. |
| i2 | K4 joint-Lipschitz complement | major | ACCEPTED | `variational_global_mean_lipschitz_paper` is moved to "no direct label (foundation: first-order joint-Lipschitz complement…)", in both the Index and its table row. |
| i3 | K1 static-interaction helpers | major | ACCEPTED | The row is split by premises: input-free scalar estimates; pair_norm_le (hY); the assembly (hY, hY0, hodd, hfirst); first_coefficient_le (hborn, hmean); independent_blocks_scalar (hstep); and definitions. |
| i3 | K2 uniform-series-tail | major | ACCEPTED | The paper wrappers keep `hTW` (TerminalWickInput). The general forms (arbitrary index, filter and inner product space, with hsum and hpos) and term_bound are proof steps. |
| i3 | K3 occupation physical bound / energy | major | ACCEPTED | These cells now state `R >= 0` (hR) and the full bound `EstarO <= Rstar^(2/(2-alpha)) spEnergyVal alpha R`. The energy definitions are split off. |
| i4 | K1 interval coefficient row | major | ACCEPTED | The row is split. The general completed assembly (R >= 0, sigma_i^2 bound, hsplits, hfixed, no sign condition) is proof steps. The paper wrapper (positive noise) is narrower. |
| i4 | K2 rows 760-763 | major | ACCEPTED | Now "proof steps: the display in full, nothing supplied; the enclosing result and module remain narrower". |
| i4 | K3 TerminalWick row 817 | major | ACCEPTED | Split by the regeneration: definitions; theorems with hmeas; hmass; neither; and hK where it applies. |
| i4 | K4 hRdef_iff_resolvent | major | ACCEPTED | Moved to "no direct label (foundation: Lean-interface equivalences…)", in both the Index and its two table rows. `ralpha` stays under `E:intro-spectral-mass`. |
| i5 | K1 score_le_ceiling_Cocc | major | ACCEPTED | Now "proof steps: the individual-control ceiling only". "Both forms" stays on intrinsic_occupation_ceiling_paper. |
| i5 | K2 finite-word hypotheses row | major | ACCEPTED | Now "proof steps: the hypotheses of the finite-word induction… one mode per color; nothing supplied". The definitions are a separate proof-steps row. |

The 3 declarations now unlabelled are the joint-Lipschitz complement and the two hRdef_iff_resolvent declarations. Totals are now 1300 labelled and 1168 unlabelled, in the ledger, README and coverage header.

### Cells rewritten or split by hand (old → new)

| Old | New |
|---|---|
| `L:masked-trig-products` (whole result: no supplied input via `masked_trig_products_completed_paper`; with `hmem`, `hnorm` as hypotheses) | `L:masked-trig-products` (proof steps: the abstract bridged wrapper on a space `V` with `hmem`, `hnorm` as hypotheses; discharged by `masked_trig_products_completed_paper`) |
| `L:masked-trig-products` (whole result: no supplied input via `masked_trig_products_completed_paper`; with `hmem`, `hmod` as hypotheses) | `L:masked-trig-products` (proof steps: the abstract wrapper on a space `V` with `hmem`, `hmod` as hypotheses; discharged by `masked_trig_products_completed_paper`) |
| `L:masked-trig-products` (whole result; no supplied input via `masked_trig_products_completed_paper`) | `L:masked-trig-products` (whole result with nothing supplied, in the complexified temporal completion `H_a`) |
| `L:masked-time-completion` (proof steps: definitions (the form and its kernel); whole result at the level of the result) | `L:masked-time-completion` (proof steps: definitions of the temporal form and kernel only; the completion itself is the whole-result row of `TimeCompletion`) |
| `E:masked-translated-ball` (narrower result, see section `MaskedAuxiliaryNorm`; at every center, closed ball) | `E:masked-translated-ball` (proof steps: the closed-ball mass bound `mu(closed ball(y, r)) <= C_Gamma r^alpha` at every center only) |
| `E:variational-heat-envelope` (narrower result, see section `VariationalMean`; the spectral integrand and the identity) | `E:variational-heat-envelope` (proof steps: the Fourier identity only; the nonnegative upper bound and finiteness are in the whole-result row of `L:variational-heat-envelope`) |
| `E:variational-real-rayleigh` (narrower result, see section `VariationalMean`; side condition `integrable_pot` automatic for `h_s`) | `E:variational-real-rayleigh` (proof steps: the membership criterion of the Rayleigh trial set for `h_s` only (side condition `integrable_pot` automatic), not the rate identity) |
| `L:variational-heat-envelope` (proof steps: general forms and supporting lemmas of the result, split from the wrapper row; no named analytic input, premises as stated) | `L:variational-heat-envelope` (proof steps: general forms and supporting lemmas; `heat_envelope` without the positivity clause, which is `heat_conv_pos`; no named analytic input, premises as stated) |
| `L:phase-bessel` (proof steps: general forms and supporting lemmas of the result, split from the wrapper row; no named analytic input, premises as stated) | `L:phase-bessel` (proof steps: the general unconjugated inequality and its conjugated version, each one direction, for any measure space; no named analytic input, premises as stated) |
| `P:frequency-row` (proof steps: general forms and supporting lemmas of the result, split from the wrapper row; no named analytic input, premises as stated) | `P:frequency-row` (proof steps: the general form and supporting lemmas such as `frequencyPair_le_two`; no named analytic input, premises as stated) |
| `C:static-interaction` (proof steps: the definitions of the statement and scalar helpers, which take no input; the step rows below take the supplied inputs; section IntervalScalar (proof steps of `C:static-interaction` and `P:interval-coefficients`, inputs supplied; `E:static-block-series` in full)) | `C:static-interaction` (proof steps: input-free scalar estimates; section IntervalScalar (proof steps of `C:static-interaction` and `P:interval-coefficients`, inputs supplied; `E:static-block-series` in full)) |
| `C:static-interaction` (proof steps: the definitions of the statement and scalar helpers, which take no input; the step rows below take the supplied inputs; section IntervalScalar (proof steps of `C:static-interaction` and `P:interval-coefficients`, inputs supplied; `E:static-block-series` in full); with `hY` as hypotheses) | `C:static-interaction` (proof steps: the pair-norm estimate, with the order-bound premise `hY` as hypothesis) |
| `C:static-interaction` (proof steps: the definitions of the statement and scalar helpers, which take no input; the step rows below take the supplied inputs; section IntervalScalar (proof steps of `C:static-interaction` and `P:interval-coefficients`, inputs supplied; `E:static-block-series` in full); with `hY`, `hY0`, `hfirst`, `hodd` as hypotheses) | `C:static-interaction` (proof steps: the assembly, with the order bounds `hY`, `hY0`, the parity `hodd` and the first-variance bound `hfirst` as hypotheses) |
| `C:static-interaction` (proof steps: the definitions of the statement and scalar helpers, which take no input; the step rows below take the supplied inputs; section IntervalScalar (proof steps of `C:static-interaction` and `P:interval-coefficients`, inputs supplied; `E:static-block-series` in full); with `hborn`, `hmean` as hypotheses) | `C:static-interaction` (proof steps: the first coefficient, with the Born and mean premises `hborn`, `hmean` as hypotheses) |
| `C:static-interaction` (proof steps: the definitions of the statement and scalar helpers, which take no input; the step rows below take the supplied inputs; section IntervalScalar (proof steps of `C:static-interaction` and `P:interval-coefficients`, inputs supplied; `E:static-block-series` in full); with `hstep` as hypotheses) | `C:static-interaction` (proof steps: the block iteration, with the per-block bound `hstep` as hypothesis) |
| `L:uniform-series-tail` (proof steps: general forms and supporting lemmas of the result, split from the wrapper row; with `hpos`, `hsum` as hypotheses) | `L:uniform-series-tail` (proof steps: general forms over an arbitrary index, filter and real inner product space, with the eventual summability `hsum` and nonnegative inner products `hpos` as hypotheses) |
| `E:uniform-series-tail` (narrower result, see section `UniformSeriesTail`; hypotheses kept: `hpos`, `hsum`) | `E:uniform-series-tail` (proof steps: the term bound for a general family, with `hsum`, `hpos` as hypotheses) |
| `E:occupation-physical-bound` (narrower result: general form for any constant `R` with `SquarePairingBounds Gamma alpha R` as hypothesis, conclusion with `Rstar a D * R`; the paper wrapper specializes `R = R_0`, identified with `R_sp` by `spatial_ratio_H1_paper_completed`; class `O` modelled by joint representatives) | `E:occupation-physical-bound` (narrower result: general form for any constant `R >= 0` (hypothesis `hR`) with `SquarePairingBounds Gamma alpha R`, conclusion with `Rstar a D * R`; the paper wrapper specializes `R = R_0`, identified with `R_sp` by `spatial_ratio_H1_paper_completed`; class `O` modelled by joint representatives) |
| `E:occupation-own-energy` (narrower result: general form for any constant `R` with `SquarePairingBounds Gamma alpha R`, bound `spEnergyVal alpha R`; the paper wrapper specializes `R = R_0`, giving `E_sp`; class `O` modelled by joint representatives) | `E:occupation-own-energy` (narrower result: general form for any constant `R >= 0` (hypothesis `hR`) with `SquarePairingBounds Gamma alpha R`, bound `EstarO <= Rstar a D^(2/(2-alpha)) * spEnergyVal alpha R`; the paper wrapper specializes `R = R_0`, giving `E_sp`; class `O` modelled by joint representatives) |
| `E:interval-coefficient-bound` (narrower result: positive noise only, identification with the interval evolution and the zero and sign reduction not formalized; completion step rows; `L:inventory-product` discharged; hypotheses kept: `hfixed`, `hsplits`) | `E:interval-coefficient-bound` (proof steps: the general completed assembly, with `R >= 0`, `sigma_i^2 <= c h_i^(-alpha0)` and the named inputs `hsplits`, `hfixed` as hypotheses; no sign condition on `sigma_i`) // `E:interval-coefficient-bound` (narrower result: the paper wrapper, positive noise only (`R > 0`, `sigma_i > 0`), identification with the interval evolution and the zero and sign reduction not formalized; named inputs `hsplits`, `hfixed`; `L:inventory-product` discharged) |
| `E:spatial-square-CS` (narrower result, see section `SpatialOccupationL7Completed`: the display with the proposition's hypotheses, nothing supplied; rate and cost and class `O` identifications not formalized) | `E:spatial-square-CS` (proof steps: the display in full, nothing supplied; the enclosing result and module remain narrower) |
| `E:spatial-homogeneous-bound` (narrower result, see section `SpatialOccupationL7Completed`; completion wrapper, nothing supplied) | `E:spatial-homogeneous-bound` (proof steps: the display in full, nothing supplied; the enclosing result and module remain narrower) |
| `E:spatial-four-linear` (narrower result, see section `SpatialOccupationL7Completed`; completion wrapper, nothing supplied) | `E:spatial-four-linear` (proof steps: the display in full, nothing supplied; the enclosing result and module remain narrower) |
| `E:spatial-energy-map` (narrower result, see section `SpatialOccupationL7Completed`; completion wrapper, nothing supplied) | `E:spatial-energy-map` (proof steps: the display in full, nothing supplied; the enclosing result and module remain narrower) |
| `T:intrinsic-occupation-ceiling` (proof steps: general forms and supporting lemmas of the result, split from the wrapper row; no named analytic input, premises as stated) | `T:intrinsic-occupation-ceiling` (proof steps: the individual-control ceiling `c I_Psi - v_Psi/2 <= U_c` only, nothing supplied; class `O` bridge and rate and cost identification not formalized) |
| `L:finite-word-cutoff` (narrower result, see section `FockForm`; the hypotheses of `HermiteWord.cut_eq_raw` for the Fock model, one mode per color; nothing supplied; FockForm) | `L:finite-word-cutoff` (proof steps: the hypotheses of the finite-word induction for the Fock model, one mode per color; nothing supplied) |
| `L:finite-word-cutoff` (proof steps: definitions of the objects in the statement; no named analytic input, premises as stated) | `L:finite-word-cutoff` (proof steps: degree-support definitions of the finite-word induction, one mode per color) |
| `L:low-alpha-convolution` (whole result with nothing supplied, `d = 1, 2, 3`; L9Completed) | `L:low-alpha-convolution` (whole result with nothing supplied, `d = 1, 2, 3`; registered model choice M1 in `d = 3`; L9Completed) |
| `L:low-alpha-convolution` (whole result: the general form and the wrappers; LowAlphaConvolution; hypotheses kept: `GreenFourier`) | `L:low-alpha-convolution` (whole result with the named input `GreenFourier`, discharged in `L9Completed`; registered model choice M1 in `d = 3`; LowAlphaConvolution) |
| `L:low-alpha-convolution` (proof steps: general forms and supporting lemmas of the result, split from the wrapper row; no named analytic input, premises as stated) | `L:low-alpha-convolution` (proof steps: the `d = 1` wrapper with nothing supplied; LowAlphaConvolution) |
| `L:phase-contractions` (whole result with the two named inputs `WaveFourierThree`, `ArchimedesLaw`; PhaseContractions) | `L:phase-contractions` (whole result with the two named inputs `WaveFourierThree`, `ArchimedesLaw`, discharged in `L9Completed`; registered model choice M1; PhaseContractions) |
| `L:variational-global-mean` (narrower result: …; `variational_global_mean_lipschitz_paper` is a first-order complement …) | wrapper row kept narrower // no direct label (foundation: first-order joint-Lipschitz complement…) |
| `E:intro-spectral-mass` (proof steps: the constant `R_alpha`; equivalently `R = R_Gamma(1)`) | no direct label (foundation: Lean-interface equivalences…) |
| `E:variational-real-rayleigh` (narrower result: Rayleigh-form rate only…) [trial-set lemmas] | proof steps: lemmas on the Rayleigh trial set… |

## Re-review round 6, a723987, and Le's pointer-Index decision

Round 6 found no fatal findings and many major ones. Almost all of them concerned per-declaration qualifiers in Index cells. Le decided on 2026-11-12 to make the Index by label a pointer table. Documentation only, no Lean.

**Pointer Index.**
- **Script:** `<HOME>/.local/state/tmp/claude-1247658/-<HOME>-Dropbox-workspace-svn-Article-Stratonovich-HAM-Second-Moment/4c4c8276-f434-4c95-9605-690953ef166f/scratchpad/l9/pointer_index.py` regenerates the Index from the section tables and headings. It is scratch only, not in the repo.
- **Row format:** one row per manuscript label, plus a single "no direct label" row. Each row points to the sections whose tables use the label, each followed by the category phrase that starts that section's heading (whole result, narrower result(s), foundation, proof steps). There are no declaration lists, captions, qualifiers or input sets.
- **Size:** 403 → 657 → **177 rows** (176 labels plus the no-direct-label row).
- **Scope text:** the old every-cell rule is replaced. The Index is a pointer table; what each declaration states, and its analytic inputs, are stated once in the section tables. FORMALIZATION.md now says the same.

**New checker.** `<HOME>/.local/state/tmp/claude-1247658/-<HOME>-Dropbox-workspace-svn-Article-Stratonovich-HAM-Second-Moment/4c4c8276-f434-4c95-9605-690953ef166f/scratchpad/l9/index_category_check.py` (rewritten; scratch only) checks:
- P1: every first cell is exactly a label or "no direct label".
- P2: every second cell is well-formed `Section` (category) entries.
- P3: every referenced section exists.
- P4: every category equals that section's heading category.
- P5: every (label, section) pair used in the tables is in the Index, and every Index pointer has a table row.
- P6: every Index label exists as `\label{...}` in the manuscript at a284420, read with `git grep` from the article repository; no copy is written to disk.
- P7: every claims.yaml declaration has a table row.

Output: **"Index rows: 177; labels: 176; manuscript labels at a284420: 879; problems: 0"**.

**index_check.py.** The old index_check.py assumes the Index lists every declaration, so on the pointer Index it reports "missing from index 2468". This is expected and is not a defect. I adapted it, without changing its table checks, as `<HOME>/.local/state/tmp/claude-1247658/-<HOME>-Dropbox-workspace-svn-Article-Stratonovich-HAM-Second-Moment/4c4c8276-f434-4c95-9605-690953ef166f/scratchpad/l9/index_check_pointer.py`. That version checks (label, section) pointers instead and reports 0 problems, with totals of 1300 labelled and 1168 unlabelled (unchanged).

**Round-6 findings.**
- **Index-cell findings (moot):** h2a K1-K3, h2b K1-K2, h3 K1-K4, i1 K1-K3, i2 K1-K6, i3 K1-K4, i4 K1-K3, i5 K1-K2, i6 K1-K8, i7 K1-K4 and i8 K1-K2 are about qualifiers in Index cells. Those cells no longer exist. Where the same claim appears in a section table, I checked the table row; the rows I fixed are listed below. These rows were checked and found correct, so they were not changed:
  - `resolvent_eq_ralpha_paper`: its table label is already "(proof, display at lines 152-155)".
  - SpectralHomogeneous `hI`: already disclosed in the ClockCopy, DampedNorms and SpectralHomog rows.
  - `static_phase_order_cutoff`: names only hentire, hcircle, hz and hv.
  - `spatial_static_energy_score_paper_completed`: existential form, nothing supplied.
  - `variational_remove_mask_rates_paper`: rates only, nothing supplied.
  - The three bracket halves: each states its own half and input.
  - `measure_closedBall_eq` and `integral_lowKernel`: already separate rows with their own scopes.
  - `hQ'`: already named in the inputs of `complex_phase_paper` and `interval_complex_paper`.
  - The GaussianIBP helper: its table label is already "(integration-by-parts step)".
- **Section-table rows changed:**
  - `FrequencyRow.one_le_scaleProfile` (i2 K4): label `E:variance-scale-profile` → `P:frequency-row` (proof step `B_alpha(h) >= 1`, used at TeX line 136). The labelled count is unchanged.
  - The inputs cells in the table below.

| Declaration | Old inputs cell (start) | New inputs cell (start) |
|---|---|---|
| `IndexedCone.GroundFamily.Pi_apply` | None. | The abstract ground family `G` it is stated for (a `GroundFamily`, whose fields are supplied C16 outputs). |
| `IndexedCone.GroundFamily.Q_apply` | None. | The abstract ground family `G` it is stated for (a `GroundFamily`, whose fields are supplied C16 outputs). |
| `IndexedCone.GroundFamily.decomp` | None. | The abstract ground family `G` it is stated for (a `GroundFamily`, whose fields are supplied C16 outputs). |
| `IndexedCone.GroundFamily.norm_Q_le` | None. | The abstract ground family `G` it is stated for (a `GroundFamily`, whose fields are supplied C16 outputs). |
| `IndexedCone.GroundFamily.norm_Pi` | None. | The abstract ground family `G` it is stated for (a `GroundFamily`, whose fields are supplied C16 outputs). |
| `IndexedCone.GroundFamily.norm_Pi_sub_le` | None. | The abstract ground family `G` it is stated for (a `GroundFamily`, whose fields are supplied C16 outputs). |
| `IndexedCone.ConeConstants.norm_Q_le` | None. | The abstract ground family `G` it is stated for (a `GroundFamily`, whose fields are supplied C16 outputs); the cone constants `K` (`ConeConstants G`: the supplied gap and smallness bounds). |
| `IndexedCone.ConeConstants.norm_PQ_le` | The `gap` field of `ConeConstants` (from `E:compact-normalized-complement`). | The `gap` field of `ConeConstants` (from `E:compact-normalized-complement`); the abstract ground family `G` (a supplied `GroundFamily`). |
| `IndexedCone.ConeConstants.step_ell` | Supplied `GroundFamily` (C16 outputs: `E:compact-F-eigen`, `E:compact-normalized-complement`, `E:compact-positive-margins`, continuity from `P:compact-F-project | Supplied `GroundFamily` (C16 outputs: `E:compact-F-eigen`, `E:compact-normalized-complement`, `E:compact-positive-margins`, continuity from `P:compact-F-projection`, `E:compact-rate-gap`); the cone constants `K` (`ConeCo |
| `IndexedCone.ConeConstants.step_Q` | Supplied `GroundFamily` (C16 outputs: `E:compact-F-eigen`, `E:compact-normalized-complement`, `E:compact-positive-margins`, continuity from `P:compact-F-project | Supplied `GroundFamily` (C16 outputs: `E:compact-F-eigen`, `E:compact-normalized-complement`, `E:compact-positive-margins`, continuity from `P:compact-F-projection`, `E:compact-rate-gap`); the cone constants `K` (`ConeCo |
| `IndexedCone.ConeConstants.step_obs` | Supplied `GroundFamily` (C16 outputs: `E:compact-F-eigen`, `E:compact-normalized-complement`, `E:compact-positive-margins`, continuity from `P:compact-F-project | Supplied `GroundFamily` (C16 outputs: `E:compact-F-eigen`, `E:compact-normalized-complement`, `E:compact-positive-margins`, continuity from `P:compact-F-projection`, `E:compact-rate-gap`); the cone constants `K` (`ConeCo |
| `IndexedCone.ConeConstants.rebase` | Supplied `GroundFamily` (C16 outputs: `E:compact-F-eigen`, `E:compact-normalized-complement`, `E:compact-positive-margins`, continuity from `P:compact-F-project | Supplied `GroundFamily` (C16 outputs: `E:compact-F-eigen`, `E:compact-normalized-complement`, `E:compact-positive-margins`, continuity from `P:compact-F-projection`, `E:compact-rate-gap`); the cone constants `K` (`ConeCo |
| `IndexedCone.ConeConstants.qB_nonneg` | None. | The abstract ground family `G` it is stated for (a `GroundFamily`, whose fields are supplied C16 outputs); the cone constants `K` (`ConeConstants G`: the supplied gap and smallness bounds). |
| `IndexedCone.ConeConstants.entrance` | Supplied `GroundFamily` (C16 outputs: `E:compact-F-eigen`, `E:compact-normalized-complement`, `E:compact-positive-margins`, continuity from `P:compact-F-project | Supplied `GroundFamily` (C16 outputs: `E:compact-F-eigen`, `E:compact-normalized-complement`, `E:compact-positive-margins`, continuity from `P:compact-F-projection`, `E:compact-rate-gap`); the cone constants `K` (`ConeCo |
| `IndexedCone.ConeConstants.block` | Supplied `GroundFamily` (C16 outputs: `E:compact-F-eigen`, `E:compact-normalized-complement`, `E:compact-positive-margins`, continuity from `P:compact-F-project | Supplied `GroundFamily` (C16 outputs: `E:compact-F-eigen`, `E:compact-normalized-complement`, `E:compact-positive-margins`, continuity from `P:compact-F-projection`, `E:compact-rate-gap`); the cone constants `K` (`ConeCo |
| `IndexedCone.ConeConstants.terminal` | Supplied `GroundFamily` (C16 outputs: `E:compact-F-eigen`, `E:compact-normalized-complement`, `E:compact-positive-margins`, continuity from `P:compact-F-project | Supplied `GroundFamily` (C16 outputs: `E:compact-F-eigen`, `E:compact-normalized-complement`, `E:compact-positive-margins`, continuity from `P:compact-F-projection`, `E:compact-rate-gap`); the cone constants `K` (`ConeCo |
| `IndexedCone.ConeConstants.chain_cone` | Supplied `GroundFamily` (C16 outputs: `E:compact-F-eigen`, `E:compact-normalized-complement`, `E:compact-positive-margins`, continuity from `P:compact-F-project | Supplied `GroundFamily` (C16 outputs: `E:compact-F-eigen`, `E:compact-normalized-complement`, `E:compact-positive-margins`, continuity from `P:compact-F-projection`, `E:compact-rate-gap`); the cone constants `K` (`ConeCo |
| `IndexedCone.ConeConstants.positive_product_of_constants` | Supplied `GroundFamily` (C16 outputs: `E:compact-F-eigen`, `E:compact-normalized-complement`, `E:compact-positive-margins`, continuity from `P:compact-F-project | Supplied `GroundFamily` (C16 outputs: `E:compact-F-eigen`, `E:compact-normalized-complement`, `E:compact-positive-margins`, continuity from `P:compact-F-projection`, `E:compact-rate-gap`); the cone constants `K` (`ConeCo |
| `RadiusMeanAnchor.mean_anchor_bound_blocks` | The moment bound of `C:radius-covariance-residuals` (`M_m` a.s. `C^theta`, `p`th power integrable, `(E \/\/M_m\/\/^p)^(1/p) <= C sqrt(p) R^e`); measurability of | The moment bound of `C:radius-covariance-residuals` (`hMC`: `M_m` a.s. `C^theta`; `hMint`: `p`th power integrable; `hMmom`: `(E \/\/M_m\/\/^p)^(1/p) <= C sqrt(p) R^e`); measurability of `\/\/X_m\/\/` (`hXmeas`). |
| `RadiusMeanAnchor.radius_mean_anchor_paper` | The moment bound of `C:radius-covariance-residuals` (from `P:radius-actual-moments`) for `M_m = M_R(Y_m)`, `m <= N`; measurability of `\/\/X_m\/\/_{C^theta}` (` | The moment bound of `C:radius-covariance-residuals` (from `P:radius-actual-moments`) for abstract paths `M_m` standing for `M_R(Y_m)`, `m <= N` (`hMC`, `hMint`, `hMmom`; the paths are not constructed); measurability of ` |
| `TerminalWick.mixed_moment_mono` | Supplied `hmeas` for both fields (from the proof of `L:terminal-wick`, TeX lines 3657-3659). | Supplied `hmeas₁`, `hmeas₂` (the a.e. strong measurability of the products for each field) (from the proof of `L:terminal-wick`, TeX lines 3657-3659). |
| `TerminalWick.terminal_wick_mono_paper` | Supplied `hmeas` for both fields (from the proof of `L:terminal-wick`, TeX lines 3657-3659). The chain measures are not constructed: `nu n` is any finite measur | Supplied `hmeas₁`, `hmeas₂` for the two fields (from the proof of `L:terminal-wick`, TeX lines 3657-3659); the masses `_hmass` are carried, unused. The chain measures are not constructed: `nu n` is any finite measure wit |
| `ComplexPhaseScalar.phase_block_of_inputs` | None of its own (the Crouzeix-Palencia and inverse-root hypotheses are the supplied inputs of `complex_phase_paper` and `interval_complex_paper`). | Its hypotheses `hCPC`, `hCPF`, `hCPH` (Crouzeix-Palencia) and `hJm`, `hJ`, `hQ'` (the inverse-root representation `Q' - 1 = pi^(-1) int J`) are the supplied inputs of `complex_phase_paper` and `interval_complex_paper`. |
| `IndexedCone.exists_coneConstants` | Supplied GroundFamily (…) | … It constructs the cone constants K; it does not assume them. |
| `FrequencyRow.one_le_scaleProfile` | (label) `E:variance-scale-profile` | (label) `P:frequency-row` (proof step: `B_alpha(h) >= 1` …) |

## Re-review round 7, 434a7e2

Round 7 passed the section tables and the counts. It failed the pointer Index, because the generator and the checker read only the first label in a table row's label cell.

**Decision (orchestrator, implementing Le's pointer-Index decision).** Every label written in a section-table label cell is an assignment and creates an Index pointer. A label that only gives context is moved out of the label column into the "What it states" cell, as "(Context: …)".

**Classification of the extra labels found in label cells.**
- **Kept as assignments:**
  - `E:finite-word-cutoff` (HermiteWordFock).
  - `L:low-alpha-convolution` ("also", in the ClockCopy and MaskedSpectralGrowth homogeneity rows).
  - `E:gaussian-trace-word` and `E:gaussian-trace-holder` (now in backticks).
  - `E:interval-column` and `E:fock-sandwich` (FockForm).
  - `P:compact-F-complement` and `P:compact-ground-family` (IndexedCone `GroundFamily`, genuine co-labels).
  - `E:spatial-static-score` (SpatialSmoothRatio named input).
  - The `E:temporal-equilibrium-*` displays.
  - `E:masked-time-schur` (TimeCompletion).
  - `L:white-test` (WaveGreen, the `d = 1` measure used in its proof).
- **Moved as context:** the 17 labelled rows listed below.
- **No-direct-label cells:** in the 31 rows whose label cell mentioned a label, the whole description moved into "What it states" as "(Context: …)". Their label cells now read just "no direct label", keeping a `[D4 foundation: …]` tag where one was present.

**Tools updated.** `pointer_index.py`, `index_category_check.py` and `index_check_pointer.py` now read every backticked label in a label cell. `index_category_check.py` adds rule P8: every label in a label cell counts, and no-direct-label cells carry no label.

**Index.** 177 → 186 rows (185 labels plus the no-direct-label row). Pointers added:
- ('E:finite-word-cutoff', 'HermiteWordFock', 'narrower result')
- ('E:fock-sandwich', 'FockForm', 'narrower result')
- ('E:gaussian-trace-holder', 'FiniteGaussianMatrix', 'whole result')
- ('E:gaussian-trace-word', 'FiniteGaussianMatrix', 'whole result')
- ('E:interval-column', 'FockForm', 'narrower result')
- ('E:spatial-static-score', 'SpatialSmoothRatio', 'narrower result')
- ('E:temporal-equilibrium-density', 'TemporalEquilibrium', 'whole result')
- ('E:temporal-equilibrium-mass', 'TemporalEquilibrium', 'whole result')
- ('E:temporal-equilibrium-potential', 'TemporalEquilibrium', 'whole result')
- ('L:low-alpha-convolution', 'ClockCopy', 'whole result')
- ('L:low-alpha-convolution', 'MaskedSpectralGrowth', 'whole result')
- ('L:white-test', 'WaveGreen', 'foundation')
- ('P:compact-F-complement', 'IndexedCone', 'narrower result')
- ('P:compact-ground-family', 'IndexedCone', 'narrower result')

No pointer was removed.

**Totals.** Unchanged at 1300 labelled and 1168 unlabelled. Every moved label sat beside a primary label that stays, or in a no-direct-label row.

**Minor findings.** All accepted:
- p1 P4: FORMALIZATION.md now says the audit step modules are category C "except `HermiteWordFock`, a narrower result".
- p2 P1: the `ConeConstants.step_Q` row defines `q(t) = C_gap exp(-eta_gap t)` (Lean `K.Cg * exp(-(K.ηg t))`; the TeX's `q_B` is its full-block value).
- p2 P2: the `ClockCopy.degree_one` inputs cell now reads `SpectralHomogeneous mu 1`.

**Checker outputs.**
- `index_category_check.py`: "Index rows: 186; labels: 185; manuscript labels at a284420: 879; problems: 0".
- `index_check_pointer.py`: 0 missing pointers, 0 extra pointers, 0 bad rows.
- Claims, coverage, mirror and COMPLETION checks: all OK.

### Context labels moved (labelled rows)

| Declaration | Old label cell | New label cell | Added to "What it states" |
|---|---|---|---|
| `FrequencyRow.one_le_scaleProfile` | `P:frequency-row` (proof step: `B_alpha(h) >= 1`, used at TeX line 136; `E:variance-scale-profile` defines `B_alpha` but does not state this) | `P:frequency-row` (proof step: `B_alpha(h) >= 1`, used at TeX line 136) | (Context: `B_alpha` is defined by `E:variance-scale-profile`, which does not state this inequality.) |
| `IntervalScalarCompleted.interval_coefficient_assembly_completed` | `E:interval-coefficient-bound` (step row, `L >= 1`, general form; `L:inventory-product` discharged) | `E:interval-coefficient-bound` (step row, `L >= 1`, general form) | (Context: the inventory input of `L:inventory-product` is discharged.) |
| `IntervalScalarCompleted.interval_coefficient_assembly_paper_completed` | `E:interval-coefficient-bound` (step row; `L:inventory-product` discharged) | `E:interval-coefficient-bound` (step row) | (Context: the inventory input of `L:inventory-product` is discharged.) |
| `L9Completed.phase_contractions_homog_completed` | `L:phase-contractions` (under `H:homog` in `d = 3`, nothing supplied) | `L:phase-contractions` (in `d = 3`, nothing supplied) | (already stated there) |
| `MaskedSpectralGrowth.spectral_gaussTest` | `P:masked-spectral-growth` (proof: `E:masked-spectral-convention` applied to the test, lines 65-66) | `P:masked-spectral-growth` (proof: the spectral convention applied to the test, lines 65-66) | (Context: the convention is `E:masked-spectral-convention`.) |
| `PhaseContractions.PhaseCovariance.of_homog` | `S:static-phase` (the class contains every covariance of `H:homog` in `d = 3`, lines 2048-2049) | `S:static-phase` (the class contains every covariance of the original three-dimensional class, lines 2048-2049) | (already stated there) |
| `QuotientObstruction.homogCovariance_Gamma0` | `P:masked-quotient-obstruction` (proof, `H:homog` with `alpha = 1`, lines 266-270) | `P:masked-quotient-obstruction` (proof: the example covariance satisfies the standing hypothesis with `alpha = 1`, lines 266-270) | (Context: the standing hypothesis is `H:homog`.) |
| `SpatialSmoothRatio.R0_pos_finite` | `P:spatial-smooth-ratio` (R_0 positive and finite, proof lines 182-188, through `L:spatial-fourier-bound` as in the TeX) | `P:spatial-smooth-ratio` (R_0 positive and finite, proof lines 182-188) | (Context: through `L:spatial-fourier-bound`, as in the TeX.) |
| `SpatialSmoothRatio.spatial_smooth_ratio_R0_paper` | `P:spatial-smooth-ratio` (R_0 positive and finite, proof lines 182-188, through `L:spatial-fourier-bound` as in the TeX) | `P:spatial-smooth-ratio` (R_0 positive and finite, proof lines 182-188) | (Context: through `L:spatial-fourier-bound`, as in the TeX.) |
| `SpatialSmoothRatio.ratio_le_of_S1Bdd` | `P:spatial-smooth-ratio` (every ratio bounded on the named input S1Bdd, from `E:spatial-smooth-score`; the manuscript's route before `a284420`) | `P:spatial-smooth-ratio` (every ratio bounded on the named input S1Bdd; the manuscript's route before `a284420`) | (Context: derived from `E:spatial-smooth-score`.) |
| `SpatialSmoothRatio.R0_finite_of_S1Bdd` | `P:spatial-smooth-ratio` (R_0 finite on the named input S1Bdd, from `E:spatial-smooth-score`; the manuscript's route before `a284420`) | `P:spatial-smooth-ratio` (R_0 finite on the named input S1Bdd; the manuscript's route before `a284420`) | (Context: derived from `E:spatial-smooth-score`.) |
| `SpatialSmoothRatio.R0_finite_of_S1Bdd_paper` | `P:spatial-smooth-ratio` (R_0 finite on the named input S1Bdd, from `E:spatial-smooth-score`; the manuscript's route before `a284420`) | `P:spatial-smooth-ratio` (R_0 finite on the named input S1Bdd; the manuscript's route before `a284420`) | (Context: derived from `E:spatial-smooth-score`.) |
| `SpectralMassIdentity.resolvent_eq_ralpha_paper` | `L:spatial-fourier-bound` (proof, display at lines 152-155, under `H:homog`) | `L:spatial-fourier-bound` (proof, display at lines 152-155) | (already stated there) |
| `SpectralMassIdentity.hRdef_iff_resolvent_paper` | no direct label (Lean-interface equivalence with `R = R_Gamma(1)`, under `H:homog`, bridging `E:intro-spectral-mass`) | no direct label (Lean-interface equivalence with `R = R_Gamma(1)`) | (Context: it bridges the definition `E:intro-spectral-mass`.) |
| `VariationalMean.gauss_conv` | `L:variational-heat-envelope` (applied at `eps = 1`, as in the proof of `L:variational-global-mean`) | `L:variational-heat-envelope` (applied at `eps = 1`) | (Context: as in the proof of `L:variational-global-mean`.) |
| `VariationalMean.isRayleighTrial_mean_iff_paper` | `E:variational-real-rayleigh` (side condition, via `L:variational-global-mean`) | `E:variational-real-rayleigh` (side condition) | (Context: obtained via `L:variational-global-mean`.) |
| `WhiteRelativeWidth.boundMass_eq_mass` | no direct label (identifies the `M_a` of `E:white-moment-bounds` with the mass of `L:temporal-equilibrium`, `E:temporal-equilibrium-mass`) | no direct label (identification of two Lean constants) | (Context: identifies the `M_a` of `E:white-moment-bounds` with the mass of `L:temporal-equilibrium`, `E:temporal-equilibrium-mass`.) |

### No-direct-label cells cleared (old label cell; its text is now "(Context: …)" in What it states)

| Declaration | Old label cell |
|---|---|
| `StratonovichHAMAudit.JointTilt.tilt_exponent` | no direct label (auxiliary to `P:raw-block-gaussian-law`) |
| `StratonovichHAMSecondMoment.SpectralHomog.resolvent` | no direct label (`R_Gamma` in the setup of `P:clock-copy-obstruction`, line 7720) [D4 foundation: SpectralHomog] |
| `StratonovichHAMSecondMoment.SpectralHomog.heat` | no direct label (`h_Gamma` in the setup of `P:clock-copy-obstruction`, line 7718) [D4 foundation: SpectralHomog] |
| `StratonovichHAMSecondMoment.ClockCopy.vRho` | no direct label (`v_rho`, line 7737, setup of `P:clock-copy-obstruction`) |
| `StratonovichHAMSecondMoment.InventoryProduct.pOf` | no direct label (InventoryProduct: the exponent `p` of `S:interval-upper`, line 2812) |
| `StratonovichHAMSecondMoment.MaskedAuxiliaryNorm.cd` | no direct label (the unitary transform of `S:masked-covariance`, lines 8-12) (`c_d`, line 11) |
| `StratonovichHAMSecondMoment.MaskedAuxiliaryNorm.paperHat` | no direct label (the unitary transform of `S:masked-covariance`, lines 8-12) |
| `StratonovichHAMSecondMoment.MaskedAuxiliaryNorm.integrable_paperHat_integrand` | no direct label (the unitary transform of `S:masked-covariance`, lines 8-12) (the defining integral converges for Schwartz maps) |
| `StratonovichHAMSecondMoment.MaskedAuxiliaryNorm.zetaR` | no direct label (setup of `P:masked-auxiliary-norm`, lines 79-82) (`zeta_R`, line 80) |
| `StratonovichHAMSecondMoment.MaskedAuxiliaryNorm.kR` | no direct label (setup of `P:masked-auxiliary-norm`, lines 79-82) (`k_R`, line 80) |
| `StratonovichHAMSecondMoment.MaskedAuxiliaryNorm.Lz` | no direct label (setup of `P:masked-auxiliary-norm`, lines 79-82) (`L`, lines 80-81) |
| `StratonovichHAMSecondMoment.MaskedAuxiliaryNorm.integrable_kR` | no direct label (setup of `P:masked-auxiliary-norm`, lines 79-82) (`k_R` in `L^1`, line 81) |
| `StratonovichHAMSecondMoment.MaskedAuxiliaryNorm.kR_scale` | no direct label (setup of `P:masked-auxiliary-norm`, lines 79-82) (`k_R(u) = R^d zeta-hat(Ru)`, line 81) |
| `StratonovichHAMSecondMoment.MaskedAuxiliaryNorm.integral_norm_kR` | no direct label (setup of `P:masked-auxiliary-norm`, lines 79-82) (`norm(k_R)_1 = L`, lines 81-82) |
| `StratonovichHAMSecondMoment.MaskedAuxiliaryNorm.Lz_pos` | no direct label (setup of `P:masked-auxiliary-norm`, lines 79-82) (`L > 0`, line 82) |
| `StratonovichHAMSecondMoment.SpectralMassIdentity.hRdef_iff_resolvent` | no direct label (Lean-interface equivalence with `R = R_Gamma(1)`, bridging `E:intro-spectral-mass` and the hypothesis `hRdef` of `IntervalScalar`) |
| `StratonovichHAMSecondMoment.TypeContinuity.nuOf` | no direct label (TypeContinuity: the parameters of `S:near-static-lower`, lines 7062-7069) |
| `StratonovichHAMSecondMoment.TypeContinuity.amaxOf` | no direct label (TypeContinuity: the parameters of `S:near-static-lower`, lines 7062-7069) |
| `StratonovichHAMSecondMoment.TypeContinuity.betaOf` | no direct label (TypeContinuity: the parameters of `S:near-static-lower`, lines 7062-7069) |
| `StratonovichHAMSecondMoment.TypeContinuity.kappaOf` | no direct label (TypeContinuity: the parameters of `S:near-static-lower`, lines 7062-7069) |
| `StratonovichHAMSecondMoment.TypeContinuity.kappaSt` | no direct label (TypeContinuity: the parameters of `S:near-static-lower`, lines 7062-7069) |
| `StratonovichHAMSecondMoment.VariationalDilation.integrable_dilation_iff` | no direct label (Lean-route integrability transfer supporting `L:variational-control-dilation`; not stated in the TeX) |
| `StratonovichHAMSecondMoment.VariationalDilation.conv_dil_integrable_iff` | no direct label (Lean-route integrability transfer supporting `L:variational-control-dilation`; not stated in the TeX) |
| `StratonovichHAMSecondMoment.VariationalDilation.mean_dil_integrable_iff` | no direct label (Lean-route integrability transfer supporting `L:variational-control-dilation`; not stated in the TeX) |
| `StratonovichHAMSecondMoment.VariationalDilation.cost_inner_integrable_iff` | no direct label (Lean-route integrability transfer supporting `L:variational-control-dilation`; not stated in the TeX) |
| `StratonovichHAMSecondMoment.VariationalDilation.rawCost_integrable_iff` | no direct label (Lean-route integrability transfer supporting `L:variational-control-dilation`; not stated in the TeX) |
| `StratonovichHAMSecondMoment.VariationalDilation.rate_integrable_iff` | no direct label (Lean-route integrability transfer supporting `L:variational-control-dilation`; not stated in the TeX) |
| `StratonovichHAMSecondMoment.VariationalDilation.variational_control_dilation_integrable_paper` | no direct label (Lean-route integrability transfer supporting `L:variational-control-dilation`; not stated in the TeX) |
| `StratonovichHAMSecondMoment.VariationalMean.variational_global_mean_lipschitz_paper` | no direct label (first-order joint-Lipschitz complement to `L:variational-global-mean`, not a TeX statement) |
| `StratonovichHAMSecondMoment.WaveGreen.scaling_one` | no direct label (the `d = 1` case of the scaling stated for `d = 2, 3` in the proof of `L:higher-riesz`, lines 5186-5187) |
| `StratonovichHAMSecondMoment.WhiteClockLaplace.green` | no direct label (the Green function `G_s` of `S:two-clock-screen`, TeX line 7642) |

## Re-review round 8, 06ee849

In round 8 everything substantive passed. Three items remained, and I made a mechanical lost-disclosure check. Documentation only, no Lean.

| Review | Finding | Sev | Decision | Change |
|---|---|---|---|---|
| q2 | P1 labelling convention | major | ACCEPTED | Written into the ledger Scope (in the Index paragraph) and FORMALIZATION.md. Every backticked manuscript label in a section-table label cell is an assignment and creates an Index pointer. A label mentioned only as context goes in the "What it states" cell as "(Context: …)". A "no direct label" cell contains no manuscript label. |
| q1a | step_Q Lean expression | minor | ACCEPTED | Now written exactly as in the source: `K.Cg * Real.exp (-(K.ηg * t))`. |

**Lost-disclosure check.** This mechanical check replaces the inconclusive semantic re-read of the deleted per-declaration Index rows. The script is `<HOME>/.local/state/tmp/claude-1247658/-<HOME>-Dropbox-workspace-svn-Article-Stratonovich-HAM-Second-Moment/4c4c8276-f434-4c95-9605-690953ef166f/scratchpad/l9/lost_disclosure_check.py` (scratch only). What it does:
- It takes every Index row removed in `git diff a723987 434a7e2 -- docs/statement-ledger.md`: 657 rows.
- For every declaration a removed row named, it collects the disclosure tokens of that row's first cell. These are named Prop inputs (GreenMass, FockColumn, SquareBound and the others, including GroundFamily, ConeConstants and SpectralHomogeneous), backticked h-binders, "added restriction", model-choice mentions (M1/toSphere), and "not formalized"/"not constructed" clauses.
- It checks each token against the declaration's section-table row in the working tree. A binder or input token counts only when the declaration's Lean binders actually take it. A clause counts as found when the row, or else the row's section heading and prose, states a negation ("not formalized", "not constructed", "not identified" or "not proved") and covers at least 60% of the clause's content words.

First run: 376 (declaration, token) checks; 78 LOST.
- 58 were binder or input tokens that the row stated only in words, or did not name (for example `hY`, `hborn`, `hmean`, `hstep`, `hTW`, `hsum`/`hpos`, `hmass`, `hK`, `hR`, `hsm`, `hJ`/`hJm`/`hQ`, `FockColumn`, `InventoryProduct`, `SquareBound`, `GroundFamily`).
- 20 were clause tokens.

After I tightened the clause matching (allowing for hyphenation, and treating clauses with no content words as satisfied by a negation), 55 section-table rows still lacked a disclosure. I fixed each by appending to its "Inputs left outside Lean" cell:
- "Hypothesis names in Lean: `…`." for missing binder or input names;
- the exact omitted limitation for the 20 clause cases. These are: the real-`H` clause of `P:masked-auxiliary-norm`; the mixed-derivative sentence; `J_G` and its norm identity; the Hilbert-space objects not constructed; the rest of `L:compact-raw-profile`; the `E W(Psi)^2` identification; the `splitEll` supplied lemma; the Fock coefficient-model limits on `fockD`.

Final run: **376 checks: 291 found in the row, 85 found in the section heading or prose, 0 LOST.** The summary table is in `<HOME>/.local/state/tmp/claude-1247658/-<HOME>-Dropbox-workspace-svn-Article-Stratonovich-HAM-Second-Moment/4c4c8276-f434-4c95-9605-690953ef166f/scratchpad/l9/lost-disclosure-check.out`.

**Checks.**
- Pointer checks: 0 problems (186 Index rows).
- `index_check_pointer.py`: 0 problems.
- Claims: PASS. Coverage: OK. Mirror: OK. COMPLETION: matches.
- Totals unchanged: 1300 labelled, 1168 unlabelled.

### Section-table rows given a disclosure (declaration: lost tokens → appended text)

| Declaration | Lost tokens | Appended to Inputs cell |
|---|---|---|
| `RadiusMeanAnchor.mean_anchor_bound_general` | hmom | Hypothesis names in Lean: `hmom`. |
| `MaskedTrigProducts.trig_product_bound_half` | hmem, hmod | Hypothesis names in Lean: `hmem`, `hmod`. |
| `VariationalDilation.conv` | clause: the rest of `L:compact-raw-profile` is not formalized | The rest of `L:compact-raw-profile` is not formalized. |
| `VariationalDilation.mean` | clause: the rest of `L:compact-raw-profile` is not formalized | The rest of `L:compact-raw-profile` is not formalized. |
| `VariationalDilation.rawCost` | clause: ^2` not formalized | Its identification with `E W(Psi)^2` is not formalized. |
| `IndexedCone.ConeConstants` | GroundFamily | Hypothesis names in Lean: `GroundFamily`. |
| `MaskedAuxiliaryNorm.masked_auxiliary_norm_paper` | clause: the real-`H` clause after complexification is not formalized | The clause for a real `H` after complexification is not formalized. |
| `MaskedAuxiliaryNorm.masked_hilbert_fourier` | clause: the real-`H` clause not formalized | The clause for a real `H` after complexification is not formalized. |
| `MaskedAuxiliaryNorm.masked_hilbert_fourier_lintegral` | clause: the real-`H` clause not formalized | The clause for a real `H` after complexification is not formalized. |
| `MaskedAuxiliaryNorm.lintegral_paperHat_nu_lt_top` | clause: the real-`H` clause not formalized | The clause for a real `H` after complexification is not formalized. |
| `VariationalMean.variational_global_mean_paper` | clause: the mixed-derivative sentence is not formalized | The mixed-derivative sentence is not formalized. |
| `WaveTwoVariances.orthonormal_J` | hJ, hJL2 | Hypothesis names in Lean: `hJ`, `hJL2`. |
| `UniformSeriesTail.uniform_series_tail_paper` | hTW | Hypothesis names in Lean: `hTW`. |
| `UniformSeriesTail.uniform_series_tail_second_moment_paper` | hTW | Hypothesis names in Lean: `hTW`. |
| `UniformSeriesTail.uniform_series_tail` | hpos, hsum | Hypothesis names in Lean: `hpos`, `hsum`. |
| `UniformSeriesTail.uniform_series_tail_second_moment` | hpos, hsum | Hypothesis names in Lean: `hpos`, `hsum`. |
| `UniformSeriesTail.norm_sq_le_of_inner_nonneg` | hpos | Hypothesis names in Lean: `hpos`. |
| `UniformSeriesTail.term_bound` | hpos, hsum | Hypothesis names in Lean: `hpos`, `hsum`. |
| `SpatialFourLinear.C4_sub_le` | SquareBound | Hypothesis names in Lean: `SquareBound`. |
| `OccupationPhysicalClass.occupation_physical_bound` | hR | Hypothesis names in Lean: `hR`. |
| `OccupationPhysicalClass.Jlin_le` | hR | Hypothesis names in Lean: `hR`. |
| `OccupationPhysicalClass.occupation_own_energy` | hR | Hypothesis names in Lean: `hR`. |
| `IntervalScalar.pair_norm_le` | hY | Hypothesis names in Lean: `hY`. |
| `IntervalScalar.static_interaction_assembly` | hY, hY0, hfirst, hodd | Hypothesis names in Lean: `hY`, `hY0`, `hfirst`, `hodd`. |
| `IntervalScalar.first_coefficient_le` | hborn, hmean | Hypothesis names in Lean: `hborn`, `hmean`. |
| `IntervalScalar.independent_blocks_scalar` | hstep | Hypothesis names in Lean: `hstep`. |
| `IntervalScalar.splitEll` | clause: the lemma is not formalized and enters as a supplied hypothesis | The lemma it belongs to is not formalized and enters as a supplied hypothesis. |
| `IntervalScalar.interval_coefficient_assembly_paper` | InventoryProduct | Hypothesis names in Lean: `InventoryProduct`. |
| `IntervalScalar.square_sum_eq` | hodd | Hypothesis names in Lean: `hodd`. |
| `IntervalScalar.ralpha_nonneg` | h0 | Hypothesis names in Lean: `h0`. |
| `SpatialOccupationL7Completed.squareBound_of_smooth_completed` | hsm | Hypothesis names in Lean: `hsm`. |
| `SpaceTimePositivity.stPair` | clause: `J_G` and its covariance-space norm identity not formalized | `J_G` and its covariance-space norm identity are not formalized. |
| `SpaceTimePositivity.stForm` | clause: `J_G` and its covariance-space norm identity not formalized | `J_G` and its covariance-space norm identity are not formalized. |
| `SpaceTimePositivity.stFormIter` | clause: `J_G` and its covariance-space norm identity not formalized | `J_G` and its covariance-space norm identity are not formalized. |
| `SpaceTimePositivity.integral_mean_mul_eq_stForm_swap` | clause: the Hilbert-space objects of the TeX not constructed | The Hilbert-space objects of the TeX are not constructed. |
| `SpaceTimePositivity.integral_mean_mul_eq_stForm` | clause: the Hilbert-space objects of the TeX not constructed | The Hilbert-space objects of the TeX are not constructed. |
| `SpaceTimePositivity.integral_mean_mul_sq_eq_stForm` | clause: the Hilbert-space objects of the TeX not constructed | The Hilbert-space objects of the TeX are not constructed. |
| `SpaceTimePositivity.stForm_self_eq_rawCost` | clause: the Hilbert-space objects of the TeX not constructed | The Hilbert-space objects of the TeX are not constructed. |
| `SpaceTimePositivity.positive_raw_variance_form_paper` | clause: `J_G` not constructed | `J_G` is not constructed. |
| `OccupationCeilingFinite.K0` | clause: `J_G` and its covariance-space norm identity not formalized | `J_G` and its covariance-space norm identity are not formalized. |
| `OccupationCeilingFinite.stForm` | clause: `J_G` and its covariance-space norm identity not formalized | `J_G` and its covariance-space norm identity are not formalized. |
| `OccupationCeilingFinite.field_energy_le` | hR | Hypothesis names in Lean: `hR`. |
| `OccupationCeilingFinite.pair_unit_le` | hR | Hypothesis names in Lean: `hR`. |
| `TerminalWick.integrable_pairWeight` | hK | Hypothesis names in Lean: `hK`. |
| `TerminalWick.summable_norm_smul_chainIntegral` | hmass | Hypothesis names in Lean: `hmass`. |
| `TerminalWick.terminalWickInput_of_nonneg` | hmass | Hypothesis names in Lean: `hmass`. |
| `TerminalWick.terminal_wick_paper` | hmass | Hypothesis names in Lean: `hmass`. |
| `TerminalWick.mixed_moment_eq_sum_pairings` | hK | Hypothesis names in Lean: `hK`. |
| `StaticPhaseCauchy.fockD` | clause: , symmetry without self-adjoint operator packaging, spatial operators not constr | The coefficient-model limits of `L:fock-form` apply: symmetry without self-adjoint operator packaging, spatial operators not constructed. |
| `ComplexPhaseScalar.resolvent_integral_le` | hJ, hJm | Hypothesis names in Lean: `hJ`, `hJm`. |
| `ComplexPhaseScalar.q_sub_one_le` | hJ, hJm, hQ | Hypothesis names in Lean: `hJ`, `hJm`, `hQ`. |
| `ComplexPhaseScalar.neumann_root_comparison` | hQ | Hypothesis names in Lean: `hQ`. |
| `FockForm.fockColumn_compress` | FockColumn | Hypothesis names in Lean: `FockColumn`. |
| `FockForm.fock_form_paper` | FockColumn | Hypothesis names in Lean: `FockColumn`. |
| `FockForm.interval_contractions_paper` | FockColumn | Hypothesis names in Lean: `FockColumn`. |
