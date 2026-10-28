# Static endpoint interpolation worker report

Status: **DONE_WITH_CONCERNS — complete written candidate, independent review
pending**. Date:2026-10-28 UTC. No git action, sibling edit, source-PDF edit,
message to a person, registry action, or cluster work.

## Delivered candidate

Inserted one295-line section, `S:static-holder`, immediately before Targets.
The canonical PDF is rebuilt and now has35pages. Current compiled labels:

- Lemma7.1 (`L:static-holder-input`), p30: source-grounded static coefficient
  bound, with the finite low-order enlargement of its constant proved locally.
- Proposition7.2 (`P:static-holder-upper`), p31: isotropic Riesz d2/d3,
  1<alpha<2-alpha0, all-time target-scale coefficient and second-moment bound.
- Remark7.3 (`R:static-holder-scope`), p33: static exponent, first-moment/Jensen,
  comparison-only Skorohod calibration, and precise remaining scope.

The section is visibly marked candidate. Accepted abstract/global scope and
old Round4's medium/unaccepted status remain unchanged. The deterministic
weighted-wave lemma was not inserted or used.

## Proof mechanism and important boundaries

The static input uses Chen–Hu's published(5.1),(5.15), pp2173/2180, only for
homogeneity and a finite upper coefficient rate. A finite constant covers all
orders after absorbing the initial finite set. It is not a uniform static
large-time estimate at positive smoothing and its numerical value is not computed.

The parameter choice alpha0<vartheta<2-alpha gives b0=alpha0/vartheta<1 and
beta=(alpha-vartheta)/(1-vartheta)<2. The covariance identity retains the SAME
amplitude c at both endpoints. Gaussian Hölder uses one common edgewidth2epsilon.
The temporal cutoff is only dominated by the raw alpha0 power; no cutoff
logconvexity is asserted.

Hölder is on the entire finite disjoint measure of splits, pairings, ordered
time domains, and positive product-Green increment measures. The degree-one
endpoint is a DETERMINISTIC raw-time integral. Its bound is derived using the
accepted Section5 degree-one convolution, opening AM–GM, and full temporal
pairing/split count. No mixed-regularization stochastic identity is assumed
for that endpoint.

The second endpoint is the actual regularized static coefficient. In d3 Green
smoothing is removed first at fixed noise widths. Fixed-order L2 convergence
of the two static factors comes from Chen–Hu Theorem3.8(i); the target uses the
current author source Theorem4.1. Products pass in L1, and split sums are finite.
Only AFTER these limits is the static coefficient majorant applied. The proof
uses neither epsilon monotonicity nor a uniform-in-epsilon static asymptotic.
The coefficient powers are affine and yield exactly3-alpha and4-alpha-alpha0.
The k0 term and empty chains are explicit. P:mixed supplies the full positive
series; its scalar factorial summation is used with q=3-alpha>1.

## Falsification/calibration diagnostics

`author-checks.py` and `author-checks.json` contain exact rational parameter
checks and finite enumeration for total orders2 and4, including all splits
and empty chains:3 and15 disjoint components respectively. These counts do
not replace the all-order Hölder proof.

At alpha=7/4,alpha0=3/16,vartheta=7/32, the endpoint degrees are b0=6/7 and
beta=49/25. The old single-input wedge alpha+2alpha0<2 fails at this witness,
while the new interval and both affine exponent identities hold exactly.
For the one-pair same-chain split(0,2), direct integration gives

  J02 = K_d(alpha) t^(4-alpha-alpha0)
          /[(2-alpha-alpha0)(3-alpha-alpha0)(4-alpha-alpha0)],
  K3(alpha)=c, K2(alpha)=(c/2)B(1-alpha/2,1/2).

Indeed, its spatial factor is s1*K_d(alpha)*(s2-s1)^(1-alpha);
set h=s2-s1 and integrate s1 over(0,t-h), then integrate h. At amplitude3/7
and time2/3,60-decimal mpmath values give target/Holder-RHS ratios
0.2820437214961650(d2) and0.8446710866011001(d3). This exercises the actual
same-chain normalization and amplitude powers. These are floating diagnostic
values, not certified enclosures or the proof of the inequality. No numerical
static coefficient constant or infinite-order test is claimed.

## Preservation and build

Baseline commit62f4bb4b8c6f23af907e54396a5eefe5dd7e473a. Deleting the new
section recovers the complete baseline source BYTE-FOR-BYTE, hence every
existing proof, formal statement, remark, abstract and global-scope passage.
Explicit environment checks also preserve all18old proofs and23old statement
environments(the latter count excludes remarks and goals).

Final source SHA256:
`c21b9e691a8a81b5414b65a53b0411b3894bd002d6a058686f7bb9e1e15dff3a`.
Final PDF SHA256:
`d6e937e540175383dc8153a52b905643221c8f0d4706a58318289b21674cea72`.
Bindings/check counts are in worker-baseline.json and worker-checks.json.

Build used ONLY the prescribed root command:

  latexmk -pdf -interaction=nonstopmode -halt-on-error -outdir=notes notes/notes_stratonovich_ham_second_moment.tex

Final log:0errors,0undefined references/citations,0overfull boxes. Source has
0tabs. Existing hyperref PDF-string and counter-print warnings remain; they
are outside the required zero-error/reference/overfull gate. The new theorem
page31 was rendered and visually inspected: statement, displays and common
measure fit without clipping. The scoped new-section le-style checker passes.
The unchanged source was not globally reformatted, honoring the exact
preservation instruction; no whole-manuscript Le-Typing PASS is claimed.
Both bibliography keys were located before citation; All.bib was read only.

## Honest concerns and exclusions

No missing premise was found in this bounded development, but independent
cross-family review remains mandatory. The imported static coefficient theorem
and fixed-order convergence are source inputs, not re-proved here. The source
application audit controls their printed scope; this worker did not repeat a
full static-source proof audit. The static finite constant is existential and
nonsharp. This covers isotropic Riesz, not arbitrary anisotropic homogeneous
covariance; it does not close full G:upper or G:sharp. Novelty and Lean remain
unverified. Source/proof preservation and a clean build do not certify the
mathematics or authorize status promotion.

Pre-freeze root check caught three literal commas in new C_low superscripts.
They were replaced by the intended TeX thin-space commands; the canonical
build and full baseline-preservation check were rerun. Prior draft hashes
and this correction are retained in worker-checks.json.
