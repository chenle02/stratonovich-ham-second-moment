# Rendered author-source follow-up

Date: 2026-10-28 UTC. Scope: cold-reader source questions #3/#4/#9 only.
Status: **DONE_WITH_CONCERNS**. No new substantive manuscript defect found in
these three checks. One localized source reversal-index typo is explicitly
retained below; the notes do not reproduce it.

This is a GPT-family source/application check, **not an independent cross-family
review**, a re-proof of the imported theorems, or an upgrade of DeepSeek's actual
source coverage. It does not change any historical reviewer verdict/confidence.

## Source identity and actual visual coverage

- Authority: `sources/chen-2026-author/aap-chen-2025.pdf`, the pinned64-page
  author manuscript, citekey `chen:author2026:time-dependency`.
- SHA256: `5f7385ca451e643a1f3ff31835e4ee52b2708b5d2e3652eec3fb5d3958b97b6c`.
- Actually rendered and viewed in this follow-up: PDF pages **10,11,13,14,
  22,23,34,35,37,60,61**. Images are retained in `source-followup/chen-XX.png`.
- The existing Round1 `root-source-check.md` and current notes were used to
  locate the questions. Extracted text was navigation, not the final evidence.
  No arXiv-v1 statement or later publication status substitutes for this PDF.

## A. Lemma2.5 and product (2.18): VERIFIED at cited scope

On rendered p11, Lemma2.5 explicitly says that for a deterministic integrand,
the L2 convergence in Definition2.2 can be replaced by Lp convergence for
p>=2. Thus L4 is included. Immediately below, the source states that the
Stratonovich integrability of deterministic f1,...,fm implies that of their
tensor product and prints the product identity (2.18).

Rendered p10 supplies the L2 regularization definition (2.17); pp13–14 explain
the measure-valued d3 Green-kernel convention: remove Green smoothing at fixed
noise smoothing, then remove noise smoothing. These are the source's own
objects, not a new pointwise evaluation of a delta or sphere measure.

**Application:** the notes' fixed deterministic chain kernels obtain their
integrability from Theorem4.1. Using p=4 and Hölder/Cauchy–Schwarz for the
product is consistent with Lemma2.5 and the explicit (2.18). This check does
not attribute convergence of the infinite order sum to Lemma2.5; the notes
supply a separate summability argument. The source lemma's proof refers back
to time-independent Gaussian-integral results and treats time as an extra
coordinate; those referenced proofs were not re-proved here.

## B. Two roots and chain reversal: root convention VERIFIED;
## displayed source reversal index has a SOURCE-INTERNAL-DISCREPANCY

Rendered p22, Theorem4.1, explicitly defines two blocks I1={1,...,n},
I2={n+1,...,2n}. In the Green factor for the first vertex of the second block,
the preceding coordinates s_n,x_n are set to zero. This is a local convention
for that factor, **not** a constraint setting the first block's random endpoint
to zero. Page14 states the same convention for unequal block lengths n1,n2,
and explicitly allows either block to be empty. Both chains have separate
root slots with common root value(0,0); they are not concatenated.

Page23 first shows the two original terminal-anchored products and then
reverses them. However, the displayed second-block index is printed as
`2n-l+1` for n+1<=l<=2n, including in the definition of sigma. Literally this
maps into the first block, contradicting the immediately following sentence
that sigma preserves both blocks. The correct within-second-block reversal
index is `3n-l+1`; already n=1 exposes the printed collision. This is a localized
index discrepancy in the source display, not evidence that the two-root formula
or Theorem4.1 is false.

**Application:** the current P:mixed proof says to reverse each chain's own
variables, replace time by t minus time and position by x minus position.
It does not copy the erroneous second-block index. For unequal lengths the
unambiguous maps are l -> m+1-l on the first block and
l -> 2m+n+1-l on the second. Covariance differences change sign and evenness
preserves them; the resulting bijection relabels pair partitions. This is the
local change of variables described in the notes, not a stronger claim that
Theorem4.1 itself prints the unequal-chain mixed formula. That formula uses
(2.18) plus the local argument. No manuscript repair is forced by this check;
future source summaries should not repeat the literal erroneous p23 index.

## C. (5.4), Remark5.1 and parameter scale: known discrepancy confirmed

**SOURCE-INTERNAL-DISCREPANCY for the asserted uniform intermediate bound.**
Rendered pp34–35 set theta=n/t. Page35 states that C in(5.3) is independent
of the smoothing parameters,n,t, then passes to(5.4):

  E[X_n(t,x)^2] <= C^n t^(2n)/n!.

Rendered p61 states(A.3) only for **large theta**. Page60(A.1) gives finiteness
for every positive theta, not a uniform theta-down-to-zero bound. Therefore
the substitutions on pp34–35 do not justify the asserted all-t uniformity.
The independent white-space calculation already in L:white-test gives
E[X1(t,x)^2]=t^(3-alpha0)/[(1-alpha0)(2-alpha0)(3-alpha0)], incompatible
with Ct^2 as t tends to infinity for0<alpha0<1. This parameter regime is
nonempty: d=alpha=1 and alpha0=1/2 satisfies alpha+alpha0<2; p13 expressly
includes delta covariance in d1 in the source's generalized setting.

Rendered p37, Remark5.1, prints the references(2.13) and(4.4), and the
conclusion E u(t,x)^2<=exp(Ct^2) **for large t**. Rendered p22 shows that(4.4)
is a smoothing-covariance limit, not the advertised bound. The apparent intended
reference to(5.4) is an inference, not a silent correction to the source.

**Application:** the notes already distinguish these two defects from the final
large-time conclusion. L:crude-corrected retains theta>=theta0 and chooses
theta=theta0+n/t, obtaining the extra exp(2theta0 t) factor in the diagonal
bound before summing. The current source remark reports the printed edition
faithfully and labels the repair as local. This follow-up confirms the cited
source boundary; it does not newly certify every step of the repaired proof
or refute Remark5.1's final exponential conclusion.

## Disposition

- #9: source support for finite-order L4/product use is present; no new gap.
- #4: source has two separate roots; the project describes the correct separate
  reversal. Retain the p23 index typo as a source discrepancy rather than
  silently quoting it as correct. No new mixed-root manuscript defect found.
- #3: the previously recorded uniformity issue and Remark5.1 misreference are
  confirmed on actual rendered pages. They are already scoped in the notes.

The check is limited to these statement/application questions. It does not
supply a whole-source proof audit, novelty determination, formal verification,
or permission to promote Round4's acceptance status.
