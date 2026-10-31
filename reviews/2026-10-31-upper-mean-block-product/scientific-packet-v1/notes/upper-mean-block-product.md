# Actual mean-block products with polynomially growing control balls

FULL PROOF CANDIDATE, NOT ADOPTED. Statement gated6ef042 passed
16checks/HIGH234.987seconds,no requiredrepairs. A NEW FULL analytic/source/
type/actual-application gate is required. FixedR mean-product upper only,
not an original point/sharp-source theorem. Full original goalACTIVE.

## 1. Exact statement, objects and accepted inputs

Use original all-Gamma/d1/2/3, amplitude and actual fixed physical mask
m_R=eta_R² ONCE. Real phase F=E directsum R², E=H1/2xH-1/2, same S_F and
BOTH constant columns. The supported raw Hilbert space is H_I, I=(0,1),
with compact mean T:H_I->Lr(I;K(F)). Choose once
 1/2<theta<min(1-a/2,(3-a-alpha)/2),
 1/(1-theta)<r<2/a, nu=1/theta<=p<2<r.
The stricter r upper bound is essential and is retained throughout.

Direct OWN accepted inputs, checked for fit rather than recertified:
- upper-cameron-compactness.md C3 Sections7-8, especially(13): actual free
  Fourier matrix, true clock, compact-valued mean primitive, exact norm.
- upper-young-perturbation.md E1 and Sections2,4-6: multiplicative Young
  error preserving the PHYSICAL endpoint, refined piece counts/inverse,
  actual deterministic means and scalar finite Holder budgets.
- upper-signed-static.md S1-S4,scientific404354a/adoption7c91352: actual
  signed static P_L, exact lambda(L)>=0 and
  ||P_L(t)||<=16(1+K)^4(1+t)^3 exp(lambda(L)t), ||L||<=K,K>=1;
  actual compact T images, closed LINEAR multiplier class mathcalV_R and
  uniform Bochner averaging/rate convergence. No ground/gap assumption.
- fixed-mask-young-constant-phase.md Sections2-4 supplies the same real F
  phase and Young calculus. No new primary book theorem is imported here.

Fix integer B>=1,0<delta<min(1,1/B),
 N=floor(1/(delta B)),n=N+1,s_m=m delta B,
 ell_m=B for m<N, ell_N=1/delta-NB in[0,B).
Cells I_m=[s_m,s_m+delta ell_m] partition[0,1] up to endpoints. Empty
last cells have no average. For M>0 and ||Phi||H_I<=M put
 W_Phi=T Phi, Z=||T||M,
 H_m(Phi)(u)=int_0^min(u,ell_m)
           S_F(-v)W_Phi(s_m+delta v)S_F(v)dv,
 P_m^0(Phi)=S_F(ell_m)U_(H_m(Phi))(ell_m),
 a_m=C_B delta^(-1/r)||W_Phi||Lr(I_m),
 C_B=G_B²[B^(1-1/r)+B^(1-1/r-theta)],
 G_B=sup_(|v|<=B)||S_F(v)||.
Primitives start at0 and are extended CONSTANTLY after ell_m on[0,B].
The full path norm ||D||theta=sup||D||+[D]_theta is always used.
Rate(Phi)=int_I lambda(T Phi(s))ds is the S4 scalar functional.

**B1.** We can take
 G_B<=4B, C_B<=32B^(3-1/r), C_B B^(1/r)>=B,
 log||S_F(ell)U_D(ell)||<=C_theta B(1+(||D||theta)^nu),        (1)
for0<=ell<=B,D(0)=0, with C_theta independent of B,D,R,Gamma,d.

**B2.** With C=C_theta32^r,

 limsup_(delta->0) sup_(||Phi||<=M)
 [delta sum_m log||P_m^0(Phi)||-Rate(Phi)]
 <=[log16+4log(1+K)+3log(1+B)]/B
    +C Z^r B^(3r)(K^-r+K^(nu-r)), K>=1.                    (2)

**B3.** For EVERY M0>0 and fixed real m>=0 let M_B=M0 B^m. For any
s>r(3+m)/(r-nu), with K_B=B^s,

 limsup_(integer B->infinity) limsup_(delta->0)
 sup_(||Phi||<=M_B)
 [delta log product_j||P_j^0(Phi)||-Rate(Phi)]<=0.           (3)

All products here are scalar products of FULL operator norms. They majorize
ordered physical product norms, but no global raw restart/point identity
is asserted in this theorem. The actual fixed-mask raw restart exists as
a separate accepted input for a later stochastic consumer; it is not used
by this deterministic proof. No arbitrary B_delta or growing-R claim.

## 2. Explicit polynomial block budgets

In Bessel-unitary E coordinates the accepted free Fourier matrix at
frequency omega=|xi| is
 [[cos(v omega),sqrt(1+omega²)sin(v omega)/omega],
  [-omega sin(v omega)/sqrt(1+omega²),cos(v omega)]],
with its continuous value at omega0. For |v|<=B and B>=1, the upper entry
is at most sqrt2 B in absolute value: split omega<=1 and omega>=1, using
|sin(v omega)|<=min(|v|omega,1). The other three entries are at most1.
Its Frobenius bound is sqrt(3+2B²)<=sqrt5 B. The constant block tau(v)
has norm<=1+|v|<=2B. Since free S_F is the direct sum, G_B<=4B, uniformly
over d and all model data. Also G_B>=1 by v0. As theta>0 and B>=1,
 B^(1-1/r-theta)<=B^(1-1/r).
Thus C_B<=2G_B² B^(1-1/r)<=32B^(3-1/r), while its first term gives
C_B B^(1/r)>=B.

To expose the Young dependence on B, use the ACTUAL piece counts of E1
Section2. Let c_theta=2max(1,C_Young),d0=||D||theta. If
c_theta d0 B^theta<=1/4, log sup||U_D||<=1/2. Otherwise at most
2B(4c_theta d0)^nu pieces, each of norm<=4/3, give
 log sup||U_D||<=2B(4c_theta)^nu log(4/3)d0^nu.
Since log G_B<=log(4B), the choice
 C_theta=4+log4+2(4c_theta)^nu
covers both cases in(1), using log B<=B for B>=1. No generic C(theta,B)
is left in this crude bound. It is NOT the small-error factorization used
on good blocks. This proves B1.

## 3. Actual frozen means, primitive errors and finite Holder reuse

For each positive-length I_m let
 barM_m=|I_m|^-1 int_(I_m) W_Phi(s)ds,
and let barW_delta be that piecewise-constant field. Put barM_N=0 if the
last cell is empty. All averages lie in the SAME mathcalV_R by S4 and are
Bochner integrals, not point samples. Define Hbar_m by the primitive above
with constant barM_m, stopped at ell_m and constantly extended to[0,B].
Set
 e_m=C_B delta^(-1/r)||W_Phi-barW_delta||Lr(I_m).
The accepted C3 primitive map is bounded linear on Lr, so

 ||H_m-Hbar_m||theta<=e_m, ||Hbar_m||theta<=a_m,
 delta sum_m a_m^r=C_B^r||W_Phi||Lr^r<=C_B^r Z^r,
 delta sum_m e_m^r=C_B^r||W_Phi-barW_delta||Lr^r.             (4)

For the second primitive bound, Bochner Jensen gives
|I_m|^(1/r)||barM_m||<=||W_Phi||Lr(I_m). On FULL cells this also yields

 ||barM_m||<=(delta B)^(-1/r)||W_Phi||Lr(I_m)
            =a_m/(C_B B^(1/r))<=a_m/B.                      (5)

No version of(5) with a FULL length is used on a short last cell.

The exact finite inequalities needed below are
 delta sum e_m<=(delta n)^(1-1/r)(delta sum e_m^r)^(1/r),
 delta sum e_m^nu<=(delta n)^(1-nu/r)(delta sum e_m^r)^(nu/r). (6)
They follow from EXISTING Mathlib
Real.rpow_sum_le_const_mul_sum_rpow_of_nonneg, whose COMPLETE public type
is retained. First apply exponent r>=1 to f=e_m>=0; then exponent r/nu>1
to f=e_m^nu>=0. Raise each result to the positive reciprocal exponent and
multiply by delta. Real-power products give(e_m^nu)^(r/nu)=e_m^r, including
zero e_m because exponents are positive. Cardinality n=N+1>=1 and delta>0
avoid zero-cardinality/negative-base ambiguities. This reuses the general
finite fact; no new kernel or formally verified operator claim is made.

Write
 Omega_delta(M)=sup_ball||W_Phi-barW_delta||Lr,
 Lambda_delta(M)=sup_ball int|lambda(barW_delta)-lambda(W_Phi)|.
S4 gives BOTH quantities->0 at fixed B,M; they are finite. Since
 delta n<=2/B,
(4)-(6) imply the uniform bound

 delta sum(e_m+e_m^nu)
 <=(2/B)^(1-1/r) C_B Omega_delta(M)
   +(2/B)^(1-nu/r) C_B^nu Omega_delta(M)^nu ->0.             (7)

This is used only at fixed B,K,M before the error constant matters.

## 4. Full good blocks: preserve the physical endpoint

Split only the FULL indices m<N into good a_m<=K and bad a_m>K. On a
good block Hbar_m has norm<=K and starts at0. Apply E1 with base Hbar_m,
perturbation H_m-Hbar_m and LEFT endpoint multiplier S_F(B):

 log||P_m^0(Phi)||
 <=log||S_F(B)U_(Hbar_m)(B)||+C_E1(theta,B,K)(e_m+e_m^nu).   (8)

The operator before the error is precisely the ACTUAL static physical
flow P_(barM_m)(B), by S2 Section5; not an interaction-only norm. By(5)
||barM_m||<=K/B<=K and K>=1, so S2 applies with the sufficient K budget:

 log||P_m^0||<=L_BK+B lambda(barM_m)
                       +C_E1(theta,B,K)(e_m+e_m^nu),
 L_BK=log16+4log(1+K)+3log(1+B).                             (9)

No equality of noncommuting frozen and unfrozen evolutions, no covariance
ordering or positive mean potential has been used. This is a signed static
upper with exact lambda, including zero rate and no ground-state gap.
Since L_BK>=0 and delta N<=1/B, the good prefactors sum to at mostL_BK/B.
The nonnegative rates obey

 delta sum_good B lambda(barM_m)
   <=int_I lambda(barW_delta)
   <=Rate(Phi)+Lambda_delta(M).                             (10)

Dropping bad/last/empty cells in this scalar rate sum has the correct
upper-bound direction because lambda>=0. The Young errors vanish uniformly
by(7), with C_E1(theta,B,K) FIXED during that delta limit.

## 5. Bad blocks, the true last remainder, and the quantitative bound

For full bad blocks B1 and ||H_m||theta<=a_m give
 log||P_m^0||<=C_theta B(1+a_m^nu).
On a_m>K>=1 and nu<r,
 1+a_m^nu<=(K^-r+K^(nu-r))a_m^r.
Indeed a_m^r>=K^r and a_m^(nu-r)<=K^(nu-r). Therefore(4) and B1 imply

 delta sum_bad log||P_m^0||
 <=C_theta B C_B^r Z^r(K^-r+K^(nu-r))
 <=C_theta32^r Z^r B^(3r)(K^-r+K^(nu-r)).                   (11)

The constant is independent of B,K,M,delta and all model data except Z;
no uniform maximum over the blocks is inferred from an averaged budget.

If ell_N=0, P_N^0=I so its log norm is0. If0<ell_N<B, apply B1 directly
to its ACTUAL stopped path, without a frozen spectral bound or any division
by the small cell length. The global Lr bound gives
 a_N<=C_B delta^(-1/r)Z,
 delta log||P_N^0||
 <=C_theta B[delta+C_B^nu Z^nu delta^(1-nu/r)] ->0           (12)
for fixed B,M, since nu<r. This holds uniformly on the ball even if the
last cell becomes arbitrarily short. No last velocity or clock is discarded.

Combining(7),(9)-(12) gives a fully finite-delta upper bound for
 delta sum_m log||P_m^0||-Rate(Phi):
it is at most the RHS of(2), plus
 Lambda_delta(M)+C_E1(theta,B,K)delta sum(e_m+e_m^nu)
 +C_theta B[delta+C_B^nu Z^nu delta^(1-nu/r)].
Each extra term vanishes uniformly at fixed B,K,M. Taking the supremum and
then limsup_delta proves(2) with C=C_theta32^r. This proves B2.

Here all quantities under the supremum are well-defined Borel functions
of Phi at each fixed delta,B. The primitive maps are bounded linear into
the separable path space, the accepted Young map is locally Lipschitz,
endpoint multiplication/norm are continuous, and mean physical norms are
at least1 by E2's constant-displacement coordinate. Thus log norms are
continuous. Rate is continuous by S4. The supremum is deterministic and
finite, by B1/(4)/(6), not a random supremum. Since H_I is separable,
it can also be represented over a countable dense set in the closed ball.
No common pointwise representative of T Phi for uncountably many Phi is
needed: primitives and averages are maps on Bochner Lr equivalence classes.

## 6. Polynomially growing control balls and the large-block limit

Fix ANY M0>0 and real m>=0; let M_B=M0 B^m. At EACH B this is a fixed
finite radius, so B2 applies without asserting compactness on unbounded
balls. Choose s>r(3+m)/(r-nu) and K_B=B^s. The second term of(2) becomes

 C_theta32^r ||T||^r M0^r
 [B^(r(3+m)-sr)+B^(r(3+m)+s(nu-r))].                        (13)

The second exponent is negative by the strict s condition. Moreover
r/(r-nu)>1, hence s>3+m, so the first exponent is negative too. Thus(13)
tends to0. Since s>0 and B>=1,
 log(1+B^s)<=log2+s logB, log(1+B)<=log2+logB.
The first term of(2) is consequently at most
 [log16+7log2+(4s+3)logB]/B ->0.                             (14)

All fixed-B freezing errors and last remainders were removed in the INNER
delta limit, even if their constants grow rapidly with B,K_B,M_B. This
justifies their order rather than exchanging limits. The scalar product
of positive norms has log equal to their sum; this is not log norm of
an ordered operator product. Equations(13)-(14) prove(3). This proves B3.
No prescribed diagonal B_delta or M_delta follows from this iterated result.

## 7. Evidence and scope of the actual consumer

At Phi0, P_m^0=S_F(ell_m), Rate0=0. Along delta=1/(NB),N>=2, the empty
last cell contributes1, and the delta-normalized full product rate is
log||S_F(B)||/B, at least log||tau(B)||/B>0. Tau is the ACTUAL invariant
constant sector with norm2=(sqrt(B²+4)+B)/2. This lower calibration is
consistent with(2), since ||tau(B)||<=1+B; it shows why removing all
prefactor cost at fixedB would be wrong. It does not compute the fullF
norm or prove equality of local norm products and the global flow norm.

Falsification preceded proof:7free-sector40/70 rows/Jordan norm calibration,
12exact clocks,16threshold rows from4specific exponent cases,4nonempty
last-budget exponents,11finite scalar-wave toy cases. Nine toy switches
reject exact averaging/reversed order; two endpoints calibrate. The exact
negative diagonal primitive gap is entry(1,1), opposite sign at(2,2).
Generic toy phases are not compact spatial potentials or actual CM fields.
No certified numerical enclosure or uniform operator/SPDE theorem from
them, and no unchanged diagnostic rerun during proof. All actual analytic
uniformity and finite-type applications are written above.

Existing finite powermean complete type is reused only for(6). No new
Lean source/compiler/module/kernel/count73facts19seams/L0. Mean-field,
Young, spectral, Bochner, limit and SPDE content remain INFORMAL analysis.
The original accepted self/unequal/empty Stratonovich diagrams and moment
scale are untouched, and no Skorohod theorem is developed.

The target is an actual deterministic MEAN operator product. To use it in
a moment upper still requires Gaussian head bulk/tails/action optimization
and the correct upper transfer to the original point model. The existing
raw-block-event-lower Section7 supplies a fixed-mask raw restart input for
a later exact consumer fit; it does not reverse F3 or handle growing masks.
Growing original cone/localization/entropy, original POINT upper, intended
source constants/normalization and conditional exact limit remain OPEN.
The white fixed-finite-smooth-projection uniformR guard stands. No point
Sobolev trace, rawL2Gaussian, independent blocks/heaterrors, contact/HPC/
sourcefix/companion/TeX/PDF/wiki/bib/publication/full-goal certificate.
