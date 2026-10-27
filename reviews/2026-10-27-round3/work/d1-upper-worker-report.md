# Candidate d=1 upper bound: writer and honesty report

Status: **CANDIDATE — mandatory Opus review pending.** The root supplied the spatial-removal/temporal-symmetrization mechanism. This worker independently audited it, then wrote the proposed proof. Same-family audit is not the required cross-family acceptance. No higher-dimensional upper theorem, sharp constant, final goal completion, Lean certificate, or circulation clearance is claimed.

## Owned changes

[held back: collaborators' unpublished work]

The new section is `S:d1-upper` (Section5), with:

- `L:d1-spatial` (Lemma5.1): uniform smoothed spatial bound, proved by processing **every vertex in descending block-label order**. At a closing label exactly its covariance remains dependent on the increment; at an opening label its partner has already been removed and only the Green mass remains.
- `P:d1-upper` (Proposition5.2): for k>=1, A_k(t)<=(2ZK_sp)^k t^(beta k)/[k! k^((2-alpha)k)]<=(2ZK_sp)^k t^(beta k)/(k!)^(3-alpha), followed by E u²<=exp{q(2ZK_sp)^(1/q)t^kappa}. The k=0 term is defined separately as1.
- `C:d1-first-calibration` (Corollary5.3): the same argument on one chain gives E u<=exp(C1 t^kappa), C1=C2/2^((4-alpha)/(3-alpha)); the imported first-moment lower bound implies2L_*<=2C1<C2.
- `R:d1-upper-checks` and `R:d1-comparisons` (Remarks5.4–5.5): low-order controls, relation to the scoped G0 no-go, static exponent calibration, normalized Riesz-to-white constant check, and read-only Skorohod exponent comparison.

Every new result/remark has “Candidate” in its heading, and the section opens with a visible CANDIDATE notice. The abstract says the d=1 target-scale proof is a candidate awaiting independent review. Higher dimensions and the sharp constant remain open.

## Exact hypotheses and constants

Dimension1; 0<alpha0<1; either gamma(y)=c_alpha |y|^(-alpha),0<alpha<1,c_alpha>0, or gamma=c_delta delta_0,alpha=1,c_delta>0. Let beta=4-alpha-alpha0,b=2-alpha,q=3-alpha,kappa=beta/q and

    Z=2/[(1-alpha0)(2-alpha0)],
    K_sp=c_alpha*2^(2-alpha)*(1-alpha)^(-alpha)/(2-alpha)^(2-alpha)
          for Riesz,
    K_sp=c_delta for white.

The main upper constant is C2=q(2ZK_sp)^(1/q). It is explicit but not asserted sharp. The normalized choice c_alpha=(1-alpha)/2 gives K_sp→1 as alpha↑1, matching unit white covariance.

## Proof and import boundaries

The spatial lemma starts with Gaussian-smoothed covariance, including white noise, and proves the convolution supremum uniformly by averaging (Riesz) or by G<=1/2 and mass-one smoothing (white). No pointwise delta evaluation is used. Pair-dependent Gaussian widths are allowed in the lemma, so the noise covariance's epsilon_i+epsilon_j form is covered.

The proposition begins with the source's spatial smoothing and temporal truncation. Temporal factors are bounded by the full nonnegative |s-r|^(-alpha0) factors. Only after extracting the common spatial maximum are **all temporal pairings summed** into the fully symmetric F_k. The ordered-domain factorial, pair count and split count are then derived explicitly. This is the decisive summed argument; no symmetry is asserted for a fixed pairing.

Fixed-order L2 convergence from the source's Theorem4.1, already used in reviewed G0, gives L1 convergence of mixed products. The finite split sum at fixed k therefore inherits the uniform bound. The full series is the reviewed `P:mixed` series. This proof does not import the false uniformity in source(5.4), the earlier common-Laplace norm majorant, Balan's static trace estimate, or any unproved mean-comparison assumption.

The p=1 calibration uses the tighter sum of increments<=t. Its temporal simplex factor is P_k/(2k)! and its spatial bound is2^(-(2-alpha)k) times the two-chain bound. This gives the coefficient ratio2^(-(4-alpha)k) and hence C1=C2/2^((4-alpha)/(3-alpha)). The Jensen consistency statement uses the author-version first-moment lower bound only; it does not identify C1 with L^*.

## Falsification and validation

The preceding independent audit is `work/root-upper-candidate-audit.md`. It contains the general pivot dependency argument and exact finite support enumeration through k=4 over all1068 split/pairing cases. These checks found no dependency defect.

Established G1 checks:
- Unit white order two: ratio of coefficient bound to exact value is2(3-alpha0)>4.
- Static white order four: exact coefficient11/540; the stronger proposed coefficient bound gives1/2 and the relaxed factorial bound gives1.

The proposal avoids the earlier per-diagram and conditional-time-density obstructions. Its spatial maximum retains k^(-(2-alpha)k), and it exploits temporal symmetry only after summing matchings. Those earlier scoped no-gos remain valid.

The new section was formatted with format-tex before insertion. Complete latexmk build:0 errors,0 undefined references/citations,0 overfull boxes. Notes now have21 pages. Rendered proposition/proof pages18–19 were inspected. No numerical simulation was required to justify the proof.

## Additional source comparison, not a proof input

Balan–Conus(2016), Theorem2.1(b),(8),(10),journal p1492, was checked from the rendered fifth page of `../../../All_PDFs/b/balan_conus-16-intermittency.pdf`. SHA-256 `4fc3f73cc6164c1c9cc6a384ffdfb3389d21d34be1e86bcfbc681375a59d2756`. Rendered journal pp1489,1490,1494 were also inspected for covariance normalization, Riesz/white cases and the Skorohod solution concept. Their exponent(2H+2-a)/(3-a) matches kappa under H=1-alpha0/2,a=alpha, but their temporal normalization has H(2H-1). The notes compare exponents only; no constants or solutions are identified and no Skorohod argument is developed.

The existing author-version source remains the authority for the Stratonovich model and fixed-order construction. No arXiv-v1 first-moment theorem is substituted.

## Honesty / required reviewer attention

1. Check the descending-all-vertices invariant across block chains, including opening vertices whose partners have already been processed.
2. Check convolution bounds and their uniformity in the Gaussian regularizations.
3. Check that F_k is symmetrized only after the spatial factor is replaced by a time-independent common bound.
4. Check all factors2, k!, (2k)! and empty-chain handling.
5. Check the regularized mixed-moment passage and the imported G0 series identification.
6. Check the one-chain calibration and the restricted d=1 scope.

No gap is known to the writer after the independent same-family audit. That is an honest author assessment, not an accepted proof verdict. The new argument must pass the requested independent Opus review before being marked proved.

## Freeze hashes

- Candidate TeX SHA-256: `94e284361c0e907b8244217df806908e3492bce87654aff336f4ce9347542b70`.
- Candidate PDF SHA-256: `1edd8bd019b0a7369bdf2714781d8ebbfaf63f9b30414324d600e4f211d97fa7`.

STATUS: DONE_WITH_CONCERNS — candidate written, build clean, edits frozen for cross-family review.
