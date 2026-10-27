# Screen v2 repair record

The immutable v1 reviewer returned **FAIL / medium**, with C4 FAIL and C1–C3,C5–C9 PASS. Its sole major finding was the unqualified transfer of static-endpoint necessary constants to arbitrary fixed positive alpha0. This repair accepts that finding. The v1 report, packet, raw numerical results and producer code were not changed. This is a substantive quantifier correction, not a request to upgrade the v1 verdict.

## Required repair

1. Route-screen3a now distinguishes:
   - A1/a1=4 at every fixed positive alpha0, so C(alpha0)>=4 for the displayed no-front-prefactor(MC);
   - A2/a2→32 as alpha0↓0, so C>=sqrt(32) only at the static endpoint or for a constant uniform near that endpoint;
   - C=4 fails at order four for sufficiently small positive alpha0 by fixed-order continuity, not for an arbitrary fixed positive alpha0 on this evidence.
2. Route-screen3b now makes the parallel distinctions for D1/a1=2 and D2/a2→17. The claimed necessary sqrt(17) is confined to the static/uniform-near-static setting; C=2 fails for sufficiently small positive alpha0 by continuity.
3. The probe memo's interpretation states the same distinctions. Its numerical data remain statistical evidence only and are not used to justify the logical repair.
4. `work/mean-comparison-attempt.md` was inspected. Its references to ratios32,17 explicitly concern alpha0=0 and merely illustrate that the fully integrated ratios can be finite despite the conditional-density obstruction. It contains no necessary-constant claim for an arbitrary fixed positive alpha0. No edit to that file was needed.

## Other reviewer points addressed

- Replaced “must exceed” by “must be at least” for the Riesz order-one necessary bound, allowing equality.
- Added the general-k spatial delta approximate-identity justification in Screen1: positive increments, negligible indicator boundaries, uniform spatial bound t^k/2^k, and integrable disjoint temporal-pair domination.
- Screen4 now explicitly gives the majorant exp(C t^(3-alpha0)) and calls3-alpha0 its exponential TIME power; the factorial denominator is k!.
- Made the first-moment coefficient upper bound explicit, using the author-version Theorem1.2,(1.10),p3 and positivity: a_n t^(beta n)<=E u(t)<=exp(L t^kappa), optimize t=(q n/L)^(1/kappa), q=3-alpha, then absorb the finite prefix into B. No unstated Section8 coefficient estimate is imported.
- Clarified that the working-repository probe filenames can be copied to packet aliases `probe.py`/`probe.json`; aliases do not indicate another experiment. The real producer filename and its invocation remain unchanged.
- The G1 floating Riesz value is still explicitly diagnostic and is not used in the exact counterexample proof.

## Frozen files and preservation checks

| Artifact | SHA-256 |
|---|---|
| `recon/math-route-screen.md` (v2) | `31dcdf281bc9b007cd59c2ce3199727385ae0095f1ffa8fa59ae0581a0107806` |
| `recon/white-coefficient-probe.md` (v2 interpretation) | `f623d729022f417d365cbafacb641b4c42c99591a95a9cb8b091a70e5d178f21` |
| `recon/white-coefficient-probe.json` (unchanged) | `1d234edf7858244d3d918d25e6b5f273cbfbd2910b100beb5d8ec1b66c4c3fd0` |
| `recon/white-coefficient-probe.py` (unchanged) | `2a8ded32f3a09817bdff27018d6957560860014f1b48732926b013f52974c943` |
| `work/mean-comparison-attempt.md` (inspected, unchanged) | `d065dd2cfaa3820bf2391cda7cd1fcffa84dc572c124b62facb4c9d84bb8716b` |

[held back: collaborators' unpublished work]

STATUS: DONE_WITH_CONCERNS — v2 frozen for fresh independent review; neither surviving comparison nor G:upper is proved.
