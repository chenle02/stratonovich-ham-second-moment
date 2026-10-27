# White-space finite-coefficient importance probe

Status: **unreviewed numerical reconnaissance**, not certified integration, a theorem, or an asymptotic estimate. This probe evaluates only full Stratonovich order-four coefficients and their diagonal/mean ratios. No pure-cross estimate or Skorohod result is developed.

## Sampler normalization

Fix a=alpha0 in [0,1). For one labelled covariance pair, sample independently:

1. h~Beta(1-a,2);
2. l uniform on [0,1-h], conditional on h;
3. fair orientation, giving the ordered labelled pair (s,r)=(l,l+h) or (l+h,l).

Since B(1-a,2)=1/[(1-a)(2-a)], the density on either triangle s<r or r<s is

    (1/2) * h^(-a)(1-h)/B(1-a,2) * 1/(1-h)
      = |s-r|^(-a)/Z,
    Z = 2/[(1-a)(2-a)].

Two pairs are sampled independently. Their two free spatial colors are independent uniform[-1,1]. For a specified pairing and split, test the ORIGINAL chain ordering and all four Green-cone inequalities, without sorting the paired times. The time proposal has density the product of the two temporal covariance factors divided by Z²; the spatial proposal has density1/4; the four Green indicators have factor1/16. Therefore

    J_(m,n,D)(1) = (Z²/4) * P(the ordering and all four cones hold).

The estimator is a bounded event indicator times a deterministic constant. No singular weight is sampled or clipped.

## Arithmetic treatment of tiny gaps

At a=.9, many positive h values are smaller than machine precision relative to l. Naively computing (l+h)-l would turn them into zero and incorrectly reject domestic-pair ordering. Each vertex is therefore represented by its pair base l and an endpoint flag times h. For two vertices of the same color, the code calculates their time difference directly as (flag1-flag2)*h. The synthetic h=1e-50 control passes despite l+h rounding to l.

Observed would-be collapsed pairs, out of8388608 sampled pairs per parameter: 0 at a=0,.25,.5; 815 at a=.75; 204526 at a=.9. No beta gap was zero; the smallest sampled gap at a=.9 was approximately6.48e-68. These diagnostics address a concrete cancellation bias, not every possible floating-point error. Cross-color differences and root times still use ordinary double precision; no verified-arithmetic claim is made.

## Budget, dependence, and error statements

Each parameter used N=4194304=2^22 independent draws, in chunks of2^16. Parameters were 0,.25,.5,.75,.9, in that order, with seeds2026102700 through2026102704. No sample-budget escalation was made.

Within a draw, the nine distinct diagrams reuse the same pair times and spatial colors. Thus their estimates are correlated. Chain-exchange symmetry supplies the other six terms: A2=2*sum04+2*sum13+sum22; a2=sum04; D2=sum22. Aggregate and ratio errors use the observed covariance of those per-draw quantities. Treating the nine estimates as independent would be wrong.

Each individual diagram has an ideal-IID binomial error and a Wilson95% interval. Ratios use the delta method and normal95% intervals. These are pointwise statistical intervals, not simultaneous guarantees, certified integration bounds, or PRNG/floating-error enclosures. The small JSON preserves every event count, coefficient estimate and uncertainty calculation.

## Static calibration, run first

All nine estimates were compared with G1's exact static coefficients. The largest absolute standardized deviation was2.58, in the (2,2),A row. One row falls outside its pointwise95% interval; this is not unexpected across nine correlated comparisons, and no confidence level is retrospectively changed. The exact static ratios A2/a2=32 and D2/a2=17 lie within the reported ratio intervals. Minimum static event count was1925.

Additional checks, evaluated using the same saved counts rather than additional samples, compare (0,4),A with [Gamma(1-a)/2]^2/Gamma(1+2(3-a)), and (2,2),A with 1/[4((1-a)(2-a)(3-a))^2]. Across the fractional-time runs the largest absolute deviation for these controls was2.36 standard errors at a=.75. The analytic formulas come from the adjacent-pair beta integral and the product of the two domestic order-two integrals. The controls are not independent extra Monte Carlo samples.

## Results

Here ± denotes one estimated standard error, not a deterministic error bound.

| a | A2/a2 | D2/a2 | Smallest diagram event count |
|---|---|---|---:|
| 0 | 32.2613 ±0.2647 | 17.1378 ±0.1525 | 1925 |
| .25 | 29.3531 ±0.2069 | 15.4602 ±0.1190 | 1474 |
| .5 | 26.1523 ±0.1533 | 13.5535 ±0.0876 | 931 |
| .75 | 22.6600 ±0.1049 | 11.5044 ±0.0595 | 314 |
| .9 | 21.0732 ±0.0843 | 10.6156 ±0.0478 | 52 |

The 52-event row at a=.9 is (0,4),B. Its relative statistical error is roughly14%; it cannot support a precise individual-diagram conclusion. It contributes little to the sampled sums, whose errors are computed separately. No extra sampling was used to sharpen that rare row.

## Interpretation and limitations

The probe does not falsify the white-space comparisons A2<=64a2 or D2<=64a2 at total order four, the k=2/n=2 tests corresponding to the proposed white-space constant C=8. It does not establish either comparison, much less an all-order statement. The apparent decrease in the ratios across this finite parameter grid is not a monotonicity theorem.

The exact static results force C>=sqrt(32) for A_k<=C^k a_k and C>=sqrt(17) for D_n<=C^n a_n only at the static endpoint a0=0, or for constants that work uniformly as a0 decreases to zero. They do not impose these values on a parameter-dependent C at an arbitrary fixed positive a0. By the fixed-order continuity proved in G1, C=4 in the first comparison and C=2 in the second fail for all sufficiently small positive a0; this endpoint argument does not show failure at every other positive a0. At each fixed a0 the exact order-one necessary bounds remain C(a0)>=4 and C(a0)>=2, respectively. This numerical grid supplies additional finite-parameter diagnostics but no improved rigorous necessary constant. The separate Riesz a0↑1 obstruction to a universal sharp coefficient bound is unaffected by this white-only experiment.

Files in the working repository: `white-coefficient-probe.py`, `white-coefficient-probe.json`. Review packets may carry byte-bound copies named `probe.py` and `probe.json`; those shorter names do not denote a different experiment. Invocation: `uv run --with numpy python reviews/2026-10-27-round3/recon/white-coefficient-probe.py --output <output.json>`. The saved JSON records the actual NumPy/Python versions and labels the analytic-control postprocessing. The source is ready to reproduce the same statistical formulas; no full mathematical or independent scientific review has yet been performed.

V2 repair note: only the interpretation/provenance prose above was corrected after the v1 screen review. The raw numerical JSON and producer code are unchanged. STATUS: DONE_WITH_CONCERNS — bounded numerical falsification probe complete; repaired interpretation awaiting review; no route selected or claim promoted.
