# Conditional Borell-tube upper route to screen after the current gates

UNREVIEWED RESEARCH PLAN ONLY. No new lemma, Gaussian Laplace bound,
operator upper, variational comparison or sharp constant is proved here.
SA expectednorm FULL gate is now accepted; SP statement gate is accepted
but its FULL baseline proof gate remains pending. Do not build a proof on their candidates before those gates.
This does not replace or shrink the original all-model sharp-point goal.

## Source already held and read

Friz-Hairer2020,friz.hairer:20:course,DOI10.1007/978-3-030-41556-3,
PRIMARY Theorem11.6 printed190,physicalPDF200; both printed190-191
page renders were visually read in this turn. Exact held excerpt and
hash custody are in the accepted upper-gaussian-projection-screen and
upper-residual-exponential directories. Theorem11.6 is SET enlargement,
not merely the norm-specialized generalized Fernique11.7. Its footnote
requires attention to measurable enlargements/outer measure.

Local wiki CLI search/cite retained in borell-tube-recon-v0.json; read
synthesized li_shao-01-gaussian.md lines1-150 plus earlier Gaussian-noise
boundary page. The survey is background only; no Li-Shao theorem or
novelty claim imported. Existing Friz-Hairer citekey verified in read-only
canonical All.bib. No missing helpful source/intake or external theorem
acquisition needed. No wiki/bib/sourcePDF edit.

## Candidate abstract mechanism, every application still an obligation

1. Use the ACTUAL fullnoise E block tuple X_delta with norm
   (delta sum||x_m||Ctheta^p)^(1/p),and its genuine Gaussian/Radon/AWS
   realization on its support E0. The actual covariance map is
   L_delta Phi=sqrt(delta)H_delta(Phi),not H_delta alone. Allblocks share W.
   A prospective SA mean estimate gives b_delta=2E||X_delta||->0 on
   R_delta=1/delta+2. Handle the zero Gaussian case separately.

2. Put A_delta={||x||<=b_delta},probability>=1/2. The genuine mean image
   of each fixed raw control ball is compact for EACH fixeddelta,R (old
   fixedR compact mean map and bounded time primitive suffice); no UNIFORM
   compactness is asserted. Closedball A plus compact mean image is closed,
   so proposed tube sets A_delta+H_delta(Ball_H(r)) are Borel. This exact
   identification with (r/sqrt(delta)) times the TRUE CM unit ball,including
   the seen-space minimum norm,needs its own proof.

3. PRIMARY Borell11.6 would give tube-complement probability
       <=exp(-r^2/(2delta)),r>=0.
   Define the control-distance D_delta(x) as the least r entering that
   tube. Prove measurability/attainment/finiteness almost surely; do not
   ignore the source outer-measure footnote. D_delta would be stochastically
   DOMINATED BY a Rayleigh radius with density
       r/delta *exp(-r^2/(2delta)),r>0.
   No finite Gaussian head,raw H-valued standard Gaussian or dimension-
   dependent density is needed. This is NOT yet an applied theorem.

4. A deterministic wave estimate must bound the ORIGINAL actual endpoint
   on EVERY such tube. Proposed control envelope: x=a+H_delta(Phi),
   ||a||_tuple<=b_delta,||Phi||H<=r; first match the ACTUAL E noise-only
   block restart to GC's global endpoint,not an abstract product surrogate.
   Then use generic Young physical comparison,
   a true E mean endpoint norm baseline (SP),uniform E mean Lr budget and
   mean time averaging,then deterministic signed spectral/product bounds.
   ALL constants and the good/bad/partial-block terms must be uniformR.
   U3's scalar-time-tail tensor bound suggests uniform time averaging even
   without spatial compactness; this is a NEW application to prove. Old
   fixedR E1-B3 are not automatically uniformR theorems.

5. If a Borel nondecreasing envelope G_delta(r) controls
   2delta log max(1,||P_delta||) on these tubes,Rayleigh integration would
   bound its exponential moment by
       int_0^infty (r/delta)exp((G_delta(r)-r^2/2)/delta)dr.
   Preserve the half Gaussian action. Prove the expectation/monotonicity/
   tail comparison and fixedB large-r coercivity G<=C_B(1+r^nu),nu<2,
   not an unexplained Laplace principle. The target control supremum
       sup_r[sup_(||Phi||<=r)2Rate_R(Phi)-r^2/2]
   formally equals sup_Phi[2Rate_R(Phi)-||Phi||^2/2]; an actual uniform-
   error/tail/limit argument is still missing. No projection-rank prefactor
   may be silently dropped; this route avoids introducing that density.

6. Even a successful tube bound only gives an OWN ALL-signed variational
   operator upper. Original point transfer is separately accepted GC.
   Signed-positive optimization,mask removal and intended author energy/
   normalization remain separate. A potential finite-profile diagnostic
   is to fix positive occupation labels k_i and kinetic costs b_i,then
   examine sup_phi[2sum ell_i sqrt((<phi,k_i>-b_i)_+)-||phi||^2/2].
   A putative active-set/positive-weight dual involving the Gram matrix
   could compare masked/unmasked positive covariance entries. This is
   an IDEA ONLY: inactive thresholds,duality/interchange,measurable Rayleigh
   selection and approximation to the full time/H1 class are unproved.
   No firstmean/sourceL identity or exactlimit claim is made.

## Required falsification before any long proof

- Scalar Gaussian with a linear objective must recover its exact MGF and
  half-action constant; wrong sqrt(delta) CM scaling must fail.
- Polynomially many independent Gaussian cells vs exponentially many cells:
  the latter has nonvanishing expected maximum at small-noise scale,so the
  proposed b_delta->0 premise fails. Do not claim entropy disappeared free.
- Degenerate Gaussian/unused raw directions,zero law,nonclosed ambient
  enlargements and infinite spatial rank need exact tests/proofs.
- Arbitrary small residual path may be non-Hamiltonian: generic Young
  comparisons must be valid there; mean denominator baseline must be
  established for the ACTUAL deterministic Cameron mean,not assumed.
- If the method only reproduces a crude squared-Lr norm constant rather
  than the integrated spectral rate,it has not reached the sharp objective.

Get a scoped independent source/statement/falsification gate before proof.
This plan is outside the current SA and SP packets and supplies no premise.
No Skorohod development/contact/HPC/companion/sourcefix/TeX/PDF/wiki/bib/
publication action. Original source normalization/sharp/exactlimit OPEN.

## Later finite-profile variational idea, also UNREVIEWED

This is a second proposal to screen only after the operator-upper mechanism.
It is NOT an adopted comparison and supplies no premise above.
For finite nonnegative occupation labels k_i in the RAW Hilbert space,
nonnegative Gram entries C_ij=<k_i,k_j>,kinetic costs b_i>=0 and weights
ell_i>0,consider
 sup_phi [2sum_i ell_i sqrt((<phi,k_i>-b_i)_+)-||phi||^2/2].
The proposed reduction is a maximum over active subsets A,including the
empty subset with value0,of the candidate dual value
 inf_(w_i>0,i inA)
       [sum_i ell_i^2/w_i-sum_i w_i b_i+(1/2)sum_(i,j)w_i C_ij w_j].
No covariance inverse is used; Gram matrices may be singular.

A possible proof mechanism,NOT a completed proof: project phi onto the
finite label span; on a chosen active subset impose <phi,k_i>>=b_i.
If each retained C_ii>0 and C_ij>=0,the positive sum of labels gives strict
feasibility. An active boundary might be excluded by a small positive
label perturbation (square-root gain versus linear quadratic-cost change).
An interior maximizer would satisfy phi=sum w_i k_i with positive
w_i=ell_i/sqrt(<phi,k_i>-b_i),and scalar AMGM would give the dual equality.
Every existence,boundary,active-subset and interchange step needs a proof
and exact small-matrix falsification before use. Zero labels must be
handled separately,not divided by their zero Gram diagonal.

If that equality is correct,entrywise increase of a NONNEGATIVE Gram matrix
would increase the dual expression for every positive w and hence its
infimum/max-over-subsets. This concerns an OPTIMIZED DETERMINISTIC occupation
score,NOT monotonicity of arbitrary-phase wave covariance. Physical labels
would be k_i=(1_Ii/|I_i|)m_R f_i^2 with real smooth compact unit-L2 f_i,
b_i=||grad f_i||2^2 (FULL kinetic cost),ell_i=|I_i|. Nonnegative temporal
K and physical Gamma suggest masked entries <=unmasked entries. All actual
H-membership,covariance normalizations and strict/nonzero cases need gates.

The infinite-time/Rayleigh consumer is the dangerous part: Jensen or a
finite grid is not the original integrated rate. Optimizers change with
the grid. A proposed way forward is uniform scalar-time approximation via
U3 tensor bounds,coercivity giving a control-norm bound independent of the
grid,and density of smooth positive occupation controls for the existing
LOWER class. The corresponding unmasked deterministic E mean operator
would need its own bounded construction (global H^s product),not an
unmasked Gaussian operator or instantaneous random field. Do not infer
uniformity from pointwise time averaging or fixed-profile convergence.

An auxiliary label-one variational score is NOT the actual first moment.
Do not use p1 lower/upper constants to identify it without a separate proof;
p1 samples need not be nonnegative,and the p2 rare-event square argument
does not automatically apply to a signed first mean. The intended author
energy/domain/normalization dictionary remains unresolved; no half-kinetic
repair or sourceL identity is chosen here. No Skorohod advance is developed.
