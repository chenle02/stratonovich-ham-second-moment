# Exact input and application crosswalk

This is a statement gate, not a completed proof or fresh recertification of
accepted inputs. GC1-GC3 target the ORIGINAL all-Gamma point observable.

- notes/fixed-mask-moment-transfer.md Section4: the ordinary unmasked
  source scalar solution is locally continuous and jointly measurable;
  Picard terms have compact-cone M^n T^(2n)/(2n)! control and absolute
  L2 summability uniform in space. Spatial stationarity is proved there.
  Section5(11) supplies the FULL unmasked source point second-moment
  limit. Section5(12) is a lower-direction tested comparison and MUST NOT
  be reversed. GC1 instead proposes exact local source equality.
- notes/fixed-mask-young-constant-phase.md Section2: actual full free
  matrix finite propagation on TOTAL E plus constant distributions,
  including derivative Green entries and d3 sphere measures. Sections3-5:
  driver restriction A_F i=i M_E and free restriction, ordinary Duhamel
  identity on states, all finite Lp operator source convergence. Its
  detailed scalar identification is written for constant datum e0 only;
  GC1 must explicitly extend identification to smooth compact psi_delta.
- notes/source-operator-convergence.md Theorems1-2 and Sections6-7:
  actual retaining sources, contraction/test convergence, spatial smooth
  and time continuous source versions, actual ordinary driver identity.
  All constants allowed to depend on the fixed finite radius/horizon.
- notes/raw-block-event-lower.md Sections7-8: actual slow-source fast
  pullback, Y_fast(t)=delta^(a/2)Y_slow(delta t), Laplace cutoff eta/delta,
  amplitude g_delta and covariance Gamma_delta. The unmasked law identity
  preceding(26) applies independently of its lower comparison(25).
- notes/direct-event-calibration.md Section1(S)-(M): original canonical
  point moment equals the weak-noise rescaled point moment at fixed delta,
  including all mixed/self/empty-chain terms and d3 Green-before-noise.
  Physical radius T*delta is different from the growing mask radius.
- notes/upper-gaussian-operator.md: actual fixed-R full-F operator moment
  FINITENESS can be used for EACH fixed delta and chosen R_delta. Its
  iterated fixed-R RATE cannot be substituted along growing R_delta.
- Existing DirectEvent Lean declarations and complete compile-audit type
  fixture are supplied. Reuse kappa_gt_one, physical_scale, noise_scale,
  vertex_scale at T=delta^(-1/kappa)>0, original alpha<2<3,a<1.
  Existing bytes match the frozen accepted source, see reuse JSON.
  This is an old finite scalar application, no new kernel or count.
  Gaussian/Green/cone/Fubini/source law/SPDE/norm estimates remain analytic.

## Planned proof obligations, not premises

At fixed positive cutoffs b=m_delta*g_delta*Y_fast is smooth in space,
continuous in time, compactly supported, with bounded derivatives on each
fixed horizon. Construct its ordinary compact-datum phase in H^k x H^(k-1)
with integer k>d/2+1, using the free Fourier matrix and Leibniz multiplier
bound. Embed into E and use ordinary E uniqueness to identify it with the
actual source Young flow; H^k Fourier embedding yields continuous scalar
mild displacement. No such higher regularity is claimed after raw limits.

Compare with the accepted full ordinary scalar source solution inside
K_delta. Initial difference is psi_delta-1 with zero velocity and vanishes
on the enlarged initial region; TOTAL free finite propagation applies.
The coefficient difference also vanishes inside this cone. Bound the
local difference by iteration using the positive Green MEASURE mass t-s
and the finite SAMPLE source supremum, yielding factorial zero. This
requires no sign of the sample potential, global Gaussian supremum bound,
point trace, or multiplication of scalar moments across blocks.

Integrate squared values over D using source stationarity and Tonelli;
pass to raw E displacement in L2(Omega;L2(D)) at fixed delta using actual
operator L2 convergence and fixed deterministic datum. Match the separate
unmasked source point second-moment limit via the exact fast law. Source
cutoffs tend to zero BEFORE delta. H1 scaling gives polynomial initial
norm cost, with vanishing delta-log. Growing-R stochastic norm asymptotics
and the source normalization remain unproved.

## Wiki-first reconnaissance

wiki-recon-v1.json retains two successful CLI search calls and the exact
failed local cite lookup for chen:author2026:time-dependency. The latter
is not evidence of missing primary custody: the author edition and its
accepted applications are already local. Read synthesized wiki
content/concepts/stochastic-wave-equation.md lines54-125: finite light-cone
support, positive d1/d3 measure kernels, and a warning separating L2-valued
solutions from point random fields. The Walsh/time-white results mentioned
there are NOT imported into this Stratonovich time-fractional problem.
No external search or new reference used; no reference queue request.
REFRAME standard finite propagation applied to the actual accepted
source/raw construction; no novelty or literature-completeness claim.
