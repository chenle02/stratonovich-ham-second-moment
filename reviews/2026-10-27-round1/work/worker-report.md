# Round 1 mathematical worker report

## Todo
- [x] Read project scope, handoff, goal, workflow authority, source manifest and notes.
- [x] Read source formulas from rendered author PDF pages 10–12, 14–15, 22–23, 34–35, 37, 60–61.
- [x] Falsification first: derive white-space degree-two integrals and enumerate low-order pairing counts.
- [x] Write complete mixed expansion, corrected crude estimate, and scoped homogeneous-envelope verdict.
- [x] Build notes: zero errors, undefined references/citations, overfull boxes.
- [ ] Independent Opus review and root adjudication (root owns).

## Candidate conclusion

The uniform-per-pair application of Theorem 3.1 is not viable for the target scale. With beta=4-alpha-alpha0, its best common-Laplace-parameter majorant has growth exponent beta/(beta-1), larger than kappa=beta/(3-alpha). Its coefficients lack a factor (k!)^alpha0. This is a proved obstruction for the specified numerical majorant, not for every possible use of Theorem 3.1, and not a lower bound on the actual moment.

The complete mixed expansion includes all splits m+n=2k; no multinomial coefficient appears. Absolute convergence of the nonnegative expectation series follows from L2 convergence of the partial sums, without assuming almost-sure positivity of individual random terms.

## Source fidelity and imported inputs

Authority: `sources/chen-2026-author/aap-chen-2025.pdf`, SHA-256 `5f7385ca451e643a1f3ff31835e4ee52b2708b5d2e3652eec3fb5d3958b97b6c`. Rendered images were inspected, not solely PDF text. No arXiv theorem was used.

| Input | Pinpoint | Actual role and fidelity |
|---|---|---|
| Deterministic kernels and expansion | (2.13)–(2.16), p10 | Definition; no orthogonal-chaos assumption |
| Product integrability | Lemma 2.5 and (2.18), p11 | L4 convergence gives L2 convergence of products |
| Wick expectation | (2.20)–(2.21), p12 | Includes domestic pairings; odd total orders vanish |
| Generalized kernels | Remark 2.3 and pp13–14 | Measure-valued d3 Green kernel convention, retained explicitly |
| Two-chain bound | (3.3)–(3.6), pp14–15 | Finite spectral measures first; regularization needed for full covariance |
| Integrability | Theorem 4.1, (4.2)–(4.3), p22 | Fixed-order L2 limits and diagonal identity |
| Smoothing argument | (4.14), p33 | Removal of spatial spectral multiplier in the second norm |
| Solution series | Theorem 1.1, Section5 p34 | L2 convergence to solution; corrected crude estimate independently gives sum of L2 norms |
| Claimed uniform bound | (5.3)–(5.4), p35 | SOURCE-INTERNAL-DISCREPANCY in uniformity over time |
| Final crude bound | Remark5.1 (5.8), p37 | Recovered with theta=theta0+n/t; no reliance on invalid all-time uniformity |
| Laplace norms | LemmaA.1 (A.1)–(A.3), pp60–61 | Finiteness at positive theta; last estimate only for large theta |

The regime is nonempty: d=alpha=1 and alpha0=1/2. In this case I11(t)=(8/15)t^(5/2), contradicting any bound C t² for all t. The source's reference in Remark5.1 to (4.4) points to a smoothing limit, whereas (5.4) is the bound relevant to its argument. There is also a harmless displayed typo N0=(t/n)^(2n) on p34; the integral there is (t/n)^2 and the following count uses the correct power. The notes focus on the substantive time-uniformity issue rather than cataloguing typographical defects.

## Falsification controls

The analytic white-space calculation preceded the new general argument. `check_counts.py` enumerates actual pairings at total orders 2,4,6,8, for every split, and records cross/domestic counts. Totals are 3,15,105,945 across all splits. The script checks pair counts 1,3,15,105 and the white-space rational coefficient 8/15 at alpha0=1/2. Enumeration is only finite evidence; the all-order count proof is in the notes.

## Honesty / review focus

1. Check the precise source convention for generalized kernels in d3 and white space; the proof deliberately passes uniform inequalities through regularized mixed moments, rather than asserting pointwise convergence of delta covariances.
2. The negative verdict is narrowly quantified over the common-theta uniform pairing envelope B_K. It must not be restated as an impossibility theorem for every use of Theorem3.1.
3. Homogeneous norm gains improve the crude exponent but do not reach G:upper. Neither G:upper nor G:sharp is claimed.
4. G0 calibrations are diagnostic. No full Round2 low-order wave or Skorohod proof was undertaken. The Skorohod comparison is structural (absent self-pairings), not a new assertion about its asymptotics.
5. Source Theorem1.1 existence is imported. The corrected estimate avoids relying on the identified source uniformity issue and gives convergence of the norm series itself.
6. No Lean claim, package, external message or git operation was made by this worker.

STATUS: DONE_WITH_CONCERNS (candidate complete; independent review pending).
