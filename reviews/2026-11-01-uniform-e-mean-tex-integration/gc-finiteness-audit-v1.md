# Candidate fixed-parameter finiteness substitution for GC

UNREVIEWED integration-application candidate, not an adopted removal of
the conservative GLF/MB/EA/D1 branches. Goal/result/model scope unchanged.
Relevant exact source: growing-cone-point-upper-transfer.md Section2,
lines96/132-149. It invokes GL ONLY for finite moments at a FIXED
delta,R=L+2,L=1/delta, never its fixedR RATE on a growing diagonal.

Potential direct replacement:
1. At these FIXED parameters the actual F first driver is g_delta times
   the Gaussian masked driver; constant-phase-driver and SC transfer give
   sqrt(p)/square-exponential norms uniformly in source cutoffs.
2. P:constant-gaussian-flow and its proof give every finite moment of
   the actual physical F flow on the finite horizon, because1/theta<2.
3. GC already proves exact A_F i=iD_E and S_F i=iS_E, then state Young
   uniqueness yields P_F i=iP_E and the isometric norm/difference bounds.
   Thus E operator moments are finite, and source Lp convergence follows,
   from these SAME actual F flows. Invertibility gives strict positivity.
4. No uniformR/delta bound is supplied or needed by this substitution.
   Growing-radius RATE must still be proved via U/SA/BT/US/UR.

Guards to verify at the future GC integration gate: same given W_fast,
same mask m_R, actual source pullback at FIXED delta before any limit,
same Holder class and both phase entries, operator measurability,
uniform source-cutoff moments/differences. Free-noise g0 control checks
the E/F restriction but is not a substitute for these analytic guards.

BT's references to D1 are separately selected: Sections2-3 generic
Radon/first-chaos/support/measurable-norm construction, which BT Section5
explicitly rechecks on its actual E tuple. D1's norm concentration11.7 and
EA's finite-head product bound are not assumed needed by BT. Before pruning,
recheck every actual later consumer and write the generic realization
steps self-contained. The final tube uses PRIMARY set-enlargement11.6,
not a replacement by an easier norm-only statement.

This audit explains a possible dependency compression; no proof result
or required hard growing-radius objective is dropped. Preserve historical
notes/reviews and all failed/negative routes. No kernel/compiler run.
