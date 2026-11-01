# Physical signed-to-positive comparison and the intrinsic second-moment value

ACCEPTED at the scoped FULL analytic/actual-application gate: scientific
40ec9a9,actualOpus5.5/HIGH,19checksPASS,387.047seconds,no requiredrepairs.
All27five-way input bindings and42rawnativearchive members verified BEFORE
optional clarity/adoption. All8minor findings adjudicated in
reviews/2026-10-31-physical-score-comparison/scientific-adjudication-v1.md.
Frozen proof/report unchanged. This identifies the original point limit by
an INTRINSIC positive-control value for all original models, not author
L_*/L^* or actual p1. Le's later2026-10-31 instruction makes the derived
constant the goal; agreement with Chen is now a comparison only. Final
integration/verification requirements remain OPEN.

## 1. Exact model, inputs and conclusions

Keep EVERY original even nonnegative positive-definite homogeneous tempered
Radon covariance Gamma, with its actual amplitude, d=1,2,3, 0<a<1,
0<alpha<d or alpha=d=1, alpha+a<2. I=(0,1), K(s,t)=|s-t|^-a.
Use the real raw H_I=H_t tensor H_sp for this ORIGINAL covariance and
E=Hhalf x Hminus-half, Lambda=(1-Delta)^(1/2), unitary Fourier. Fix once
the admissible auxiliary choices of U/US/UR. The smooth even root eta
satisfies0<=eta<=1,eta=1 onB1,suppeta subsetB2. Put m_R(x)=eta(x/R)^2,
R>=1. It is used ONCE after noise smoothing. No monotonicity in R is assumed.

Direct OWN accepted inputs, not proved or re-reviewed here:

- U=uniform-e-cameron-regulator.md, scientificf54e92b, Sections1-2,5-6:
  actual spatial J_R:H_sp->K(E) (called T_R in U), its literal row equation(2), scalar
  C_t:H_t->Lr(I), r>2,r<2/a, tensor bound(15), and completed mean
  mathcalT_R=J_R(C_t tensor Id), ||mathcalT_R||<=C_mean, equation(17),
  with C_mean independent of R. H_t and H_sp are the test-null completions.
- US=uniform-e-spectral-products.md, scientifica14c6bb, Sections2-4:
  actual signed E rate, real H1 Rayleigh formula and compact trial density;
  lambda(L)<=max(1,||L||); integrated continuity(15); and uniform scalar
  time averaging(16) on bounded H_I balls, all R>=1.
- PG=positive-gram-variational-comparison.md, scientific4e2219d, PG1-PG2:
  for finite labels in ANY real Hilbert space, ell_i>0,b_i>=0 and entrywise
  nonnegative Gram, the score has a maximizer0 or a positive conic sum of
  labels; increasing a Gram ENTRYWISE cannot decrease the optimized score.
  Singular/zero labels and empty active subsets are included. Here score
  monotonicity is nondecreasing, as PG2 states. This imports
  the reviewed analytic theorem, not a kernel proof of whole PG or of PB.
- UR=rayleigh-signed-moment-upper.md, scientific939d697, Sections1-2,6-8,
  especially(16)-(18): for the SAME original canonical point solution,
  limsup_(T->infinity) T^-kappa log E|u(T,x)|²
       <=limsup_(delta->0) S_(delta^-1+2),
  kappa=(4-alpha-a)/(3-alpha), and S_R is defined below. Its source-first,
  all-chain, displacement/velocity and stationarity identifications stay
  within that accepted original-point theorem; they are not rederived here.
- UL=unmasked-variational-lower.md, scientific61ac2a3, Sections1-4,6-7:
  C_pos is ALL nonnegative nonzero real C_c^infinity(I x R^d), including
  nonseparable tests. For each Psi, h_Psi,s=int K(s,t)(Gamma*Psi_t)dt is
  globally bounded, and its full-gradient unmasked real H1 rate is
  lambda_Psi(s)=sqrt(sup_(real||f||2=1,f inH1)
                       [int h_Psi,s f²-||grad f||2²]).
  Its square is positive for nonzero Gamma. I_Psi=int_I lambda_Psi(s)ds,
  v_Psi=E W(Psi)²=int Psi h_Psi, and the SAME original point liminf is
  >=2I_Psi-v_Psi/2. The positive finite intrinsic scores satisfy
  S_c^pos=sup_(Psi inC_pos)[cI_Psi-v_Psi/2]=c^m S_1^pos,
  m=(4-alpha)/(3-alpha). Their finiteness used the OLD canonical full upper,
  not this note. S_1^pos is not an actual first moment or an author constant.

Write Rate_R(Phi)=int_I lambda(mathcalT_R Phi(s))ds and
S_R=sup_(Phi inH_I)[2Rate_R(Phi)-||Phi||HI²/2].
We prove, for nonzero Gamma,

 S_R<=S_2^pos for EVERY R>=1,                         (PB3)
 lim_(R->infinity) S_R=S_2^pos,                       (PB4)
 lim_(T->infinity) T^-kappa log E|u(T,x)|²
          =S_2^pos=2^m S_1^pos for each fixed x.       (PB5)

These are intrinsic conclusions, not identification of the
source's L_* or L^*. Section8 records the necessary earlier ceiling.
For Gamma=0, H_I={0},Rate=S_R=0,h_Psi=0,v_Psi=0,define S_c^pos=0;
the canonical solution is1, so all three statements are direct identities.
We now assume Gamma!=0.

## 2. Actual raw membership and mean of nonseparable smooth controls

Direct integration gives
int_I K(s,t)dt=[s^(1-a)+(1-s)^(1-a)]/(1-a)<=K0=2^a/(1-a).
The maximum is at1/2 by concavity. For scalar F>=0, Cauchy-Schwarz
against K(s,t)dt, then integration in s, gives ||KF||2<=K0||F||2.
Consequently, for finite simple G-valued fields F and any real Hilbert G,

 ||J_G F||_(H_t tensor G)²
  =int int K(s,t)<F(s),F(t)>G dsdt
  <=int int K(s,t)||F(s)||G||F(t)||G dsdt
  <=K0||F||L2(I;G)².                                  (20)

Here scalar L2 functions first enter H_t by approximating them with real
C_c^infinity(I): the same bound on differences makes this a well-defined
bounded inclusion into the completion. Finite tensors give the first
identity in(20). Bochner simple fields are dense in L2(I;G), so(20)
defines a bounded map J_G on all that space. The bilinear integral is
continuous there by the same Schur estimate, hence the identity extends.
No raw multiplication operator or H_I-valued Gaussian is constructed.

For G=H_sp the accepted C_t tensor Id composed with J_G agrees with
the Bochner integral int K(s,t)F(t)dt in Lr(I;G). Indeed its pointwise
norm is bounded by int K(s,t)||F(t)||G dt, so the scalar Schur estimate
above proves existence a.e. and a bounded map L2(I;G)->L2(I;G), with
norm at most K0. Simple-field approximation and this Schur bound give a
strongly measurable L2-limit version of the integral. On smooth finite
tensors the identity is the actual
covariance definition of C_t. Approximate a general F by such tensors
in L2(I;G), using simple-field density and scalar smooth density. The
Bochner integral converges in L2 by Schur. The composed map converges
in Lr by U equation(15) and(20), hence also in L2 because r>2 and |I|=1.
Uniqueness of the L2 limit proves equality a.e., and the integral thus
belongs to Lr. No additional temporal convolution theorem is needed.

Let Psi be any nonnegative real C_c^infinity(I x R^d), not necessarily separable.
Choose one closed ball B containing all spatial supports. For any real compact
smooth q supported in B, positivity and local finiteness of Gamma give

 ||q||H_sp²<=|B| Gamma(B-B)||q||infinity².                (21)

Indeed use the absolute physical integral int dx int Gamma(dy)
q(x)q(x-y); only x inB,y inB-B contribute. This also covers white and
singular Radon covariances. Thus t->Psi_t is continuous in H_sp, bounded
and compactly supported in I, by uniform continuity of Psi and(21).
It lies in L2(I;H_sp), so J_Hsp Psi is a genuine element of H_I. For
brevity call this element Psi as well. Fubini and(20) identify

 ||Psi||HI²=int int K(s,t)<Psi_s,Psi_t>H_sp dsdt
           =int Psi(s,x)h_Psi,s(x)dxds=v_Psi.             (22)

All absolute integrals are finite by(21), K's bounded rows and the common
compact supports. The preceding Bochner identity and the actual U row
equation(2) now give

              mathcalT_R Psi(s)=B_E(m_R h_Psi,s) a.e.    (23)

Explicitly, test first with compact smooth displacement f and dual state
w2=Lambda g. The U row equals
<int K(s,t)Psi_t dt,m_R f g>H_sp=int m_R h_Psi,s f g.
Fubini is justified by local finiteness on the two fixed supports and
time integrability. Both sides are bounded E operators: the left by U,
the right for each s by UL's bounded smooth h and the compact smooth
mask. Equality on dense smooth states extends to E. For this FIXED smooth
Psi the H_sp-valued temporal integral exists at EVERY s: its norm is bounded
by K0 sup_t||Psi_t||H_sp. Applying J_R gives an actual E mean-class operator
for every R,s, and the same row Fubini argument identifies it with
B_E(m_R h_Psi,s). We may use this explicit canonical version for all R for
this fixed test. Its integral agrees with the completed Lr mean class for
each R. No simultaneous pointwise representative over all rough controls
is required. This proves Lemma PB0.

## 3. Finite normalized raw labels and actual Gram comparison

Let a finite partition of I have nonempty cells I_i of length ell_i>0,
sum ell_i=1. Let f_i be real C_c^infinity(R^d) with ||f_i||2=1, and put
hi=1_Ii/ell_i, bi=||grad f_i||2²,
kiR=hi tensor(m_R f_i²), kiInf=hi tensor f_i².
The scalar inclusion in(20) puts hi in H_t. Compact smooth spatial
f_i² and m_R f_i² lie in H_sp by U's product bound or(21) and its test
definition. Hence these are genuine raw labels.

For every Phi in H_I,

 <Phi,kiR>HI=(1/ell_i)int_Ii v_(mathcalT_R Phi(s))(f_i,f_i)ds. (24)

For a smooth finite tensor h tensor q, U equation(2) with z=(f_i,0)
and w=(0,Lambda f_i) has row product
(eta_R f_i)(eta_R Lambda^-1 Lambda f_i)=m_R f_i².
Integrating the temporal covariance gives <h,hi>Ht. The physical
H_sp pairing already contains Gamma; neither another Gamma application
nor a Fourier c_d factor occurs. This proves(24) on dense tensors.
The left side is a bounded raw functional; the right is bounded by
ell_i^(-1/r) C_mean||Phi||HI ||f_i||Hhalf² using U and Holder.
Thus (24) extends to the completed H_I. The bilinear form v here is
exactly US's displacement multiplier form, by its actual E reconstruction.

CR_ij=<kiR,kjR> and D_ij=<kiInf,kjInf> are symmetric PSD Grams.
Their entries factor into the time pairing of nonnegative hi,hj and
the physical spatial covariance pairing. Since K,Gamma,fi²,fj² are
nonnegative and0<=m_R<=1, Tonelli gives

                         0<=CR_ij<=D_ij.                 (25)

This is entrywise order only. Vanishing masked labels are permitted;
PG already handles changing zero-row eligibility. Its finite real-Hilbert,
positive ell, nonnegative b and common ell/b hypotheses are now all checked.
This proves Lemma PB1.

## 4. Noncircular uniform norm bound and positive smoothing

Put C=C_mean and M=4C+4. US gives Rate_R(Phi)<=1+C||Phi||, uniformly R.
For q=||Phi||>M,
2Rate_R(Phi)-q²/2<=2+2Cq-q²/2<2-2q<0.
Since Phi=0 gives0, S_R is the supremum over ||Phi||<=M.

For ANY finite trial family from Section3 define
JD(Phi)=2sum_i ell_i sqrt((<Phi,kiInf>-bi)_+)-||Phi||²/2.
PG gives an attained maximum >=0, at0 or a positive conic sum PhiD of
unmasked labels. Choose a finite R' large enough that m_R'=1 on ALL
f_i supports. This R' may depend on the finite family. Equation(24)
and the frozen real Rayleigh formula give for EVERY Phi

 JD(Phi)<=2sum_i ell_i lambda(avg_Ii mathcalT_R' Phi)-q²/2
          <=2+2Cq-q²/2.                                 (26)

The second inequality uses lambda(L)<=max(1,||L||)<=1+||L||,
||avg_Ii W||<=avg_Ii||W||, sum ell_i=1, and ||W||L1<=||W||Lr<=Cq.
It uses NO time-averaging error or concavity of sqrt positive-part.
As in the first paragraph, any maximizing PhiD with nonnegative score
has ||PhiD||<=M, uniformly in partition, profiles and R'. This norm bound
has been proved BEFORE applying US averaging to PhiD.

On a nonempty maximizing branch PhiD=sum_i wi hi tensor fi² with wi>0.
At this FIXED finite grid/control choose nonnegative hi,j in C_c^infinity(I)
converging to hi in L2. For existence, extend hi by0, convolve with a
nonnegative compact smooth approximate identity, and multiply by compact
smooth cutoffs chi_j in I with0<=chi_j<=1 and chi_j->1 pointwise. The
L2 error is bounded by the convolution error plus||(chi_j-1)hi||2,
which tends to0 by dominated convergence. Put Psi_j=sum_i wi hi,j fi².
It is a nonnegative smooth compact spacetime test, nonzero for large j,
so belongs to the ACTUAL all-model C_pos class. The finite tensor triangle
inequality and(20) give Psi_j->PhiD in H_I. No norm or derivative bound
uniform over grids is asserted. The costs converge. US equation(15) and
U equation(17) give, for bounded raw Phi,Psi,

 |Rate_R'(Psi)-Rate_R'(Phi)|
 <=sqrt(3+C||Psi||+C||Phi||)*sqrt(C||Psi-Phi||),            (27)

so rates converge as well, uniformly R'. The zero maximizing branch
will instead use0<=S_2^pos and requires no zero test in C_pos.
This proves Lemma PB2.

## 5. Signed scores bounded by the accepted positive score

Take uniform partitions with n>=2, mesh1/n. They are US's B=1,
delta=1/n partitions with empty last cell omitted. Denote the uniform
error in US(16) on ||Phi||<=M by e_n; then e_n->0 independently of R.
Fix R>=1 and Phi with ||Phi||<=M. Write Wi=avg_Ii mathcalT_R Phi.
For each cell the real compact smooth Rayleigh trials are dense in H1.
Continuity of the form in H1 and L2 normalization therefore imply

 lambda(Wi)=sup_(real compact smooth||f||2=1)
               sqrt((v_Wi(f,f)-||grad f||2²)_+).          (28)

There are finitely many cells. For any eps>0 choose one fi per cell so
the right side is within eps of lambda(Wi). This is a finite choice,
not a measurable continuum optimizer. By US averaging and(24),

 2Rate_R(Phi)-||Phi||²/2
 <=JC(Phi)+2e_n+2eps,
 JC(Phi)=2sum_i ell_i sqrt((<Phi,kiR>-bi)_+)-||Phi||²/2.   (29)

Apply PG and(25) to the OPTIMIZED finite objectives:
JC(Phi)<=sup JC=S(CR)<=S(D)=JD(PhiD).
This does not compare individual controls. By Section4, ||PhiD||<=M
before another use of US; choose its finite support radius R'. Equation
(24), the frozen Rayleigh bound and uniform US averaging now give

 JD(PhiD)<=2Rate_R'(PhiD)-||PhiD||²/2+2e_n.               (30)

For the positive smooth approximants of Section4, (23), bounded h_Psi>=0
and0<=m_R'<=1 give the deterministic REAL H1 form inequality

                        Rate_R'(Psi_j)<=I_(Psi_j).      (31)

No arbitrary-phase wave or Gaussian covariance monotonicity is used.
Equations(22),(27),(31) and the definition of S_2^pos imply
2Rate_R'(PhiD)-||PhiD||²/2<=S_2^pos after j->infinity.
If PhiD=0, JD(PhiD)=0<=S_2^pos directly, which suffices for the same
bound JD(PhiD)<=S_2^pos+2e_n. Combining(29)-(30) yields

 2Rate_R(Phi)-||Phi||²/2<=S_2^pos+4e_n+2eps.              (32)

Every n, R and Phi was fixed before finite profiles, R', PhiD and smooth
approximants were chosen. The right side depends only on n,eps and the
fixed model choices, not those finite choices. Thus take eps->0, then
the supremum over the bounded raw ball, then n->infinity. Section4's
restriction to that ball proves S_R<=S_2^pos for EVERY R>=1. The proof
used no new finiteness argument based on its own conclusion. This proves
Proposition PB3.

## 6. Cutoff removal for a fixed control and for optimized scores

Fix Psi in C_pos before R or moment limits. Use PB0's explicit canonical
mean B_E(m_R h_Psi,s) for this fixed test for EVERY R,s; its rate integral
equals Rate_R(Psi) for each R. Write lambda_R(s) for this rate and
lambda_inf(s) for the UL rate.
The form order gives0<=lambda_R(s)<=lambda_inf(s). For any real compact
smooth L2-unit f, all sufficiently large R have m_R=1 on supp f. Hence

 liminf_R lambda_R(s)²>=int h_Psi,s f²-||grad f||2².

Compact trial density and UL's real H1 formula show the supremum of the
right sides is lambda_inf(s)². Thus lambda_R(s)->lambda_inf(s) pointwise
for these explicit versions, without monotonicity in R or an unmasked
eigenfunction. UL's global bound H=sup_(s,x)h_Psi,s(x)<infinity gives
lambda_R(s)<=sqrt(H). Dominated convergence therefore gives

                         Rate_R(Psi)->I_Psi.            (33)

The original H_I representative and its cost are independent of R by(22).
For every fixed Psi, S_R>=2Rate_R(Psi)-v_Psi/2. Taking liminf_R and using
(33) bounds it below by each positive-test score. To justify the supremum
step explicitly, choose for any eps>0 one fixed Psi with score>S_2^pos-eps;
then liminf_R S_R>=S_2^pos-eps, and let eps->0. PB3 supplies limsup_R
S_R<=S_2^pos. This proves Proposition PB4.

## 7. Same original point limit and exact scope of the conclusion

UR(18), with R_delta=delta^-1+2 tending to infinity, and PB4 give
limsup_(T->infinity) T^-kappa log E|u(T,x)|²<=S_2^pos.
UL(3)-(4) gives the reverse liminf for the SAME canonical solution and
the SAME raw variance-half cost and exponent. Consequently the limit
exists and equals S_2^pos=2^m S_1^pos, the latter equality being UL's
already accepted auxiliary-label homogeneity. Both inequalities use
fixed controls before their own moment limits. Source limits, mixed and
self-pairings, initial displacement1/velocity0 and fixed-x stationarity
are carried by the cited accepted original-point inputs. In particular,
UR Section7 cites GC Section8's identity E|u(T,x)|²=E|u(T,0)|², which
transfers the lower liminf as well as the upper limsup to every fixed x.
These identifications are not replaced by
independent blocks or a surrogate solution. This proves Theorem PB5.

[held back: collaborators' unpublished work]

## 8. Necessary d1 ceiling consequence and retained source qualification

Within the d1 Riesz/white scope, import occupation-control-approximation.md
(scientific80e47d6), Sections3,5: on the SAME full smooth nonnegative
spacetime class the raw variance and real full-gradient rates match
exactly; its notation V_c^pos is the supremum of those smooth scores.
The UL definitions therefore give S_c^pos=V_c^pos by identity of the
admissible class, cost and H1 form, not by identifying actual p1 moments.

Import raw-positive-value-ceiling.md (scientificad6c188), (15),(17),(19).
It defines OWN raw finite-energy occupation E_eta and proves
V_2^pos<=U_2(eta). By the accepted PB5, the original moment LIMIT is now
equal to this V_2^pos and hence is <=U_2(eta). In particular its strict
comparisons yield a moment value strictly below2^m F_a(E_(1/2)) and,
at alpha=1/10,a=9/10, strictly below2^m F_a(E_1), in those OWN domains.
This is a NEW consequence of this note's PB5,
not an earlier moment ceiling attributed to the old lower-mechanism note.

No source lower-constant comparison F_a(E_star) follows: its damped
temporal kernel matters. The reviewed literal source-normalization
discrepancy remains; the intended correction and exact domain dictionary
are UNKNOWN. No energy, coefficient, source PDF, goal definition or
conjecture is repaired on the author's behalf. The derived-constant goal
stays ACTIVE; matching this prediction is no longer required by Le.
No novelty, human, whole-paper, publication, correspondence,
HPC, official companion, or manuscript-integration clearance is asserted.
