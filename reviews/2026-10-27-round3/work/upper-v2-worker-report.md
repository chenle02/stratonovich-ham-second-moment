# Upper-bound candidate v2: substantive extension and writer honesty

**Status: CANDIDATE, awaiting fresh cross-family review.** The immutable d=1 v1 report is PASS_WITH_NOTES/medium, all10 checks PASS, no fatal/major findings or required repairs; it did not meet the configured high-confidence acceptance gate. This v2 adds a genuinely new mathematical scope and detailed limiting argument. It is not a confidence-only retry, and the v1 report has not been relabeled as covering it.

## New scope and statements

The proposed target-scale upper bound now covers:

- the existing d=1 Riesz cases0<alpha<1 with their real-space constants;
- the existing d=1 spatial-white endpoint alpha=1 with its separate mass bound;
- **new:** every nonnegative, nonnegative-definite homogeneous tempered covariance of degree-alpha with0<alpha<1 in d=1,2,3, without isotropy or a spectral-density hypothesis.

The original full G:upper remains unchanged. The range1<=alpha<2-alpha0 in d=2,3 remains open. The sharp constant remains open. All new result headings, the section notice, abstract and scope notes say CANDIDATE.

New statements:

- `L:low-alpha-convolution` (Lemma5.3): spectral dilation and exact layer-cake bound, followed by a uniform Gaussian-smoothed wave/covariance convolution bound.
- `P:low-alpha-upper` (Proposition5.4): the target-scale coefficient and second-moment bounds in all three dimensions for0<alpha<1.
- `R:low-alpha-scope` (Remark5.5): zero covariance, anisotropy, no density requirement, and the alpha>=1 boundary limitation.
- `C:d1-first-calibration` (now Corollary5.6, stable label retained): explicitly extended to either spatial constant, with the corresponding one-chain upper constant and Jensen consistency.

The existing `L:d1-spatial` and `P:d1-upper` retain their sharper one-dimensional constants and white endpoint. They are not replaced by the potentially larger Fourier-envelope constant.

## Exact new proof mechanism

Let mu be the positive Radon spectral measure in the source convention gamma(x)=integral exp(i xi.x)mu(dxi), and V=mu(B1). Fourier uniqueness transfers covariance homogeneity to mu(cA)=c^alpha mu(A), so mu(B_R)=V R^alpha. No radial-density assertion is used. The layer-cake calculation gives

    integral min(h,1/|xi|) mu(dxi)
      = integral_0^h mu(B_(1/u))du
      = V h^(1-alpha)/(1-alpha).

For0<alpha<1 this is finite. The source's Fourier wave formula and mass are

    Ghat_h(xi)=sin(h|xi|)/|xi|,     mass(G_h)=h.

Gaussian covariance smoothing makes the spectral measure finite, permitting Fourier Fubini. Gaussian wave smoothing contributes another multiplier of magnitude at most one. The real-space convolution is nonnegative by covariance positivity; its absolute Fourier value is bounded by the layer-cake integral. No positivity of the oscillatory sine integrand is assumed.

Thus each closing vertex has uniform bound[V/(1-alpha)] h^(1-alpha), while every opening gives mass h, in all d=1,2,3. The descending-all-vertices invariant works for vector increments because only earlier labels enter a position. Weighted AM–GM gives

    K_sp^gen=V*2^(2-alpha)*(1-alpha)^(-alpha)/(2-alpha)^(2-alpha).

All temporal symmetrization and counting are dimension-free and reused with explicit hypotheses checked. For k>=1,

    A_k(t) <= (2ZK_sp^gen)^k t^(beta*k)/(k! k^((2-alpha)k))
            <= (2ZK_sp^gen)^k t^(beta*k)/(k!)^(3-alpha),
    E u² <= exp{(3-alpha)(2ZK_sp^gen)^(1/(3-alpha))*t^kappa}.

A0=1 is handled separately. If V=0, dilation gives mu=0 and u=1; the proposition states V>0 and the following remark records this trivial case.

## Dimension-three limiting argument is explicit

The source's limit order is preserved: first eta→0 at fixed noise smoothing, then the noise parameters→0. For the inner limit, the text supplies a direct L2 Cauchy argument:

1. Fixed-noise Gaussian Wick factors are bounded and continuous in the spatial coordinates.
2. Product Green measures G_(h,eta) converge weakly with unchanged masses h.
3. A constant times the product of all time increments dominates the covariance integrals on finite time simplexes.
4. Dominated convergence gives a common joint covariance limit for two possibly different eta approximations, hence L2 Cauchy convergence.
5. Products converge in L1; after this inner limit, source Theorem4.1 supplies the outer fixed-order L2 noise limit, again yielding L1 product convergence.

The sphere kernel is treated as a measure throughout. In d=1,2 only the outer limit is needed. This is not a statement that the old d=1 review already checked d=3.

## V1 optional points addressed

- Clarified that x_l are positions and y_l increments locally in the new section, unlike the position notation in the earlier mixed-diagram formula; the evaluation point remains x.
- Added explicit Tonelli averaging for the Riesz convolution under Gaussian smoothing.
- Smoothing pinpoints now include(2.9),(2.11),(2.23)–(2.24), rather than relying on(2.11) alone. Root supplies the full primary source pages in the successor packet.
- Updated abstract, candidate notice, title, goal-coverage note and upper-route item to the enlarged candidate and its remaining regime. The original G:upper statement is not weakened.
- Softened the Balan–Conus comparison to “Skorohod mild solution”; it remains an exponent-only comparison, not a proof input or constant identification.
- Kept the pre-existing G0/G1 white-space proof unchanged. The new proof itself never uses pointwise delta covariance evaluation.
- The prior finite enumeration is support only, not a proof input; its separate audit remains available without upgrading its review status.

## Sources and checks

Author source: `sources/chen-2026-author/aap-chen-2025.pdf`, SHA-256 `5f7385ca451e643a1f3ff31835e4ee52b2708b5d2e3652eec3fb5d3958b97b6c`.

Rendered pp3,7,8,9 were checked for homogeneity/spectral convention, wave positivity/Fourier formula/mass, and common-field covariance smoothing. The pp13–14 construction and Theorem4.1 were already read for G0 and remain imported analytic inputs. The new source correspondence follows `work/low-alpha-dimension-extension-audit.md`; the full source proof has not been re-proved.

The general ball-mass argument was checked against an anisotropic example gamma(x)=c|x1|^(-alpha), whose spectral measure is supported on an axis. This guards against silently inserting rotational invariance. The normalized Riesz-to-white constant limit in the notes is explicitly about the separate d=1 real-space K_sp; no such limit is claimed for K_sp^gen.

The p=1 argument now applies to either K_*=K_sp or K_sp^gen. It gives C_(1,*)=C_(2,*)/2^((4-alpha)/(3-alpha)); the imported first-moment lower bound implies2L_*<=2C_(1,*)<C_(2,*). This is a logical consistency check, not a numerical evaluation of the source's variational constants.

## Preservation and build

The complete old model/G0/G1 mathematical block was compared with checkpoint8358d58: byte-identical after removing only terminal whitespace for the boundary comparison. Block SHA-256: `aa888a76060f292a4ba5cadf5a9fec5a4d5e1b0084e08a9f184582768c2ec17a`. Only the candidate section, abstract/title, target-coverage note and upper-route prose were changed, with the rebuilt PDF. No Progress, HANDOFF, source, bibliography, sibling, Git or Lean changes were made.

The owned candidate section was passed through format-tex. Full latexmk build:0 errors,0 undefined references/citations,0 overfull boxes;24 pages. Rendered extension/proof pages20–21 were inspected.

Final candidate TeX SHA-256: `19a392540804177c0c6a300cd2d5605a9f9007d5e9934b5ba1e2b23462be2735`.
Final candidate PDF SHA-256: `73b2de20bb11c4d7d0dfdd4f89073798c7de3d58cafa552a01f53fb6427d34f2`.

## Honesty and fresh-review focus

No gap is known to the writer, but the new scope is unaccepted until fresh review. Check spectral dilation without density assumptions, the exact V/(1-alpha) layer-cake constant, nonnegative covariance versus oscillatory Fourier integrand, Gaussian weighting/Fubini, and the two-stage d=3 limit. Verify that the earlier temporal symmetry/count argument transfers only after a common spatial maximum. Confirm the remaining alpha>=1 d=2,3 regime is not claimed. No Skorohod result, sharp constant, higher-alpha obstruction, full-source certification or Lean verification is asserted.

STATUS: DONE_WITH_CONCERNS — substantive v2 written and frozen for fresh Opus review; v1 medium report preserved.
