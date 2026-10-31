# Actual masked operator driver on the balanced wave phase

ACCEPTED internal actual operator-path result: native Opus5.5/high full
review, PASS_WITH_NOTES/HIGH, scientific93d71e4; see the
2026-10-30-actual-operator-driver packet and adjudication.
This constructs a LOCAL physically masked first Gaussian operator path on
the SAME original W, in every admissible dimension and covariance class.
It proves no source-cutoff convergence, Young flow, canonical solution
identity or new solution-moment asymptotic.

## 1. Objects and precise result

Use canonical H:homog: d in {1,2,3}, a=alpha_0 in (0,1), alpha+a<2,
0<alpha<d or alpha=d=1, and the nonzero nonnegative even positive-definite
tempered Radon spatial covariance Gamma. W is the original real Gaussian
noise with raw covariance |t-u|^-a Gamma on positive time. Write H_W for
the null-quotient completion of real C_c^infinity((0,infinity)xR^d).
Zero covariance gives the zero driver and is trivial; below Gamma is nonzero.

Let Lambda=(1-Delta)^(1/2), E_r=H^r(R^d)xH^(r-1)(R^d), s=1/2, E=E_s.
Initially phases are real; complexification will be explicit. Set

 J0(u,v)=(Lambda^(1/2)u,Lambda^(-1/2)v),
 H0=L2(R^d;R^2), D_gamma=diag(Lambda^-gamma,Lambda^-gamma).

J0:E->H0 is unitary; the frequency coordinates of the accepted variance
note differ only by unitary Fourier transform. S(t) is the FULL massless
wave group, with sine quotient t at frequency zero, and B(h)(u,v)=(0,hu).
Fix a real even compact smooth nonnegative zeta equal1 on B1, zero off B2,
and zeta_R(x)=zeta(x/R), R>0. Fix T>0.

OWN accepted inputs are precisely:
- actual-two-variance-forms.md Propositions1-2 and Sections2-3: actual
  physically masked forms ell_R, their Sobolev adjoint and BOTH uniform
  finite-family variance bounds, real mean-square columns m,n and the
  Schwartz phase basis/density construction of its Section6;
- compact-sobolev-cutoff.md Propositions1-3, Corollary4 and their proofs:
  actual whole-space compact cutoffs, correctly adjointed two envelopes,
  positive-order minmax, and finite Gaussian OPERATOR moments;
- finite-gaussian-schatten.md Theorem1: finite MATRIX Gaussian moments;
- spectral-mask-covariance-foundation.md Section4: temporal positivity,
  Schur continuity and the positive Laplace representation.
All new basis, coefficient, tail, series, path and application steps are
proved below. No old HS result is promoted to a new operator norm.

Choose parameters

 0<gamma<min(1/2,(2-alpha)/2),
 1/2<theta<beta<min(1-a/2,(3-a-alpha)/2).                            (1)

**Theorem.** There is a real smooth compact-test ONbasis {f_j} of H_W,
g_j=W(f_j) independent standard real Gaussians, and deterministic operators
A_j(0,t) on E such that X_N(t)=sum_(j<=N)g_j A_j(0,t) converges, for every
finite p>=1, in

    Lp(Omega;C^theta([0,T];B(E)))                                  (2)

to a centered Gaussian SAME-W path M_R. It starts at0, has compact operator
values for ALL times on a single probability-one path set, and for every
fixed real Schwartz pair z,w and time t,

    <M_R(t)z,w>_E=ell_R((0,t);z,w) in L2(Omega).                     (3)

Intervals longer than1 in (3) mean additive partitions into short intervals,
or equivalently their actual raw-test completion; no long-h bound is assumed.
The construction is basis independent up to a version. Its complexification
has the corresponding sesquilinear identity with W_C.

For fixed data there are C,c>0 such that

 (E||M_R||_Ctheta(B(E))^p)^(1/p)<=C sqrt(p), all p>=1,
 E exp(c||M_R||_Ctheta(B(E))^2)<infinity.                            (4)

Constants may depend on R,T,theta,beta,gamma, the model and mask shape,
not on the test basis. No uniform-R pathnorm bound is claimed. For each
FIXED short interval I and each EVEN q>=2 with q gamma>d, its increment
also has the fixed-interval S_q moment bound in Section7. Arbitrary finite
p in (2)-(4) refers to B(E), not arbitrary Schatten indices. No claim of
a C^theta S_q-valued path is made.

## 2. The actual test-noise basis, with null directions retained

For tests supported in a fixed time interval [0,L] and spatial compact K,
the raw covariance absolute value is bounded by

 |K|Gamma(K-K)*[2L^(1-a)/(1-a)]
       *||t->||F(t)||infinity||_L2 *||t->||G(t)||infinity||_L2.       (5)

The spatial integral only uses differences in K-K and has absolute bound
|K| times the two suprema; temporal Schur gives (5). This uses local
Radon mass, not a spatial density. For each increasing rational compact
box inside positive time, a countable smooth compact collection is dense
in the uniform norm, with support in a fixed slightly larger box. One may
construct it by rational step approximations followed by smooth compact
mollification with rational scales. Uniform approximation and (5) give
noise-norm approximation. The countable union is dense in H_W, proving
separability without assuming injectivity of the original test space.

We also verify this is an infinite nonzero Hilbert space. Choose L>=1
with 0<Gamma(B_L)<infinity, and real nonnegative compact smooth q>=1 on
B_(2L+1). Then

 Q_sp=int Gamma(dy)int q(x)q(x-y)dx
             >=|B_(L+1)|Gamma(B_L)>0,

and Q_sp is finite by the same compact bound. For any real smooth compact
positive-time tau, ||tau tensor q||_H_W^2=Q_sp||tau||_a^2.
The temporal form is STRICTLY positive for every signed nonzero tau, not
only nonnegative ones. Indeed the accepted positive Laplace identity gives

 ||tau||_a^2=Gamma_E(a)^-1 int_0^infinity lambda^(a-1) E_lambda(tau)dlambda,
 E_lambda(tau)=int_R 2lambda |int_r^infinity
                 exp(-lambda(t-r))tau(t)dt|^2 dr.                  (6)

Here tau is smoothly zero-extended to the real line. Formula (6) follows
from the elementary factorization of exp(-lambda|t-u|); all signed
interchanges are absolutely integrable on the compact support, and the
final squared integral is nonnegative. If the norm were0, some lambda>0
would have E_lambda=0. The inner Volterra integral v(r) is continuous and
satisfies v'=lambda v-tau. It would vanish almost everywhere, hence
everywhere, forcing tau=0. This proves strict positivity. An infinite
linearly independent family of compact time bumps therefore injects into
H_W after multiplication by q.

Gram-Schmidt on a countable dense real test collection, discarding zero
residuals in the NULL quotient, now yields an infinite ONbasis with smooth
compact representatives f_j. Each representative is a finite linear
combination of original tests. The isonormal property of the original W
gives Eg_j g_k=delta_jk; joint Gaussian characteristic functions then
factor, proving independence. No spatial null direction was removed from
the physical model; it was handled by its prescribed covariance quotient.

## 3. Actual deterministic covariance coefficients

For each representative f_j define

 H_j,R(t,x)=zeta_R(x) int_(u>0)|t-u|^-a
                              int Gamma(dy)f_j(u,x-y)du.           (7)

This is a covariance coefficient, not point evaluation of raw noise.
Extend f_j by zero in time. Since its support is compact inside positive
time, that extension is smooth. With v=t-u, the unmasked expression is
int_R |v|^-a int Gamma(dy)f_j(t-v,x-y)dv. On every compact (t,x) set,
only a common compact set of y and bounded range of v contribute.
Gamma has finite mass there and |v|^-a is locally integrable. Thus any
mixed derivative in t,x can be moved onto f_j under dominated integration.
The expression is real smooth; multiplying by zeta_R makes its spatial
support a subset of B_(2R), with all derivatives bounded on finite time
compacts. Bounds can depend on j,R,T. No negative-time W was introduced:
zero extension was only of the deterministic test in this calculation.

For any smooth compact real test F, covariance and absolute Fubini give

    E[W(zeta_R F)g_j]=int H_j,R(t,x)F(t,x)dt dx.                    (8)

Only a compact difference set in Gamma and a bounded time rectangle occur.
The temporal singularity is integrable. For the actual wave test
F=1_I v_z conj(G_w) of the variance note, approximate in its raw completion
by smooth tests with common masked spatial support and L2-time supnorm
convergence. The left side converges by Cauchy-Schwarz in the noise Hilbert
space, and the right side by the boundedness of H_j,R on this support.
Thus (8) extends to that indicator test, with the complex extension if used.

If two representatives give the same H_W class, their Gaussian difference
is zero. Apply (8) to arbitrary smooth tests: their masked coefficients
agree as distributions for t>0. Smoothness gives equality there, and
continuity extends it to t=0. Independence of representatives is asserted
on t>=0 only; no negative-time noise conclusion is needed.

## 4. Deterministic wave operators, gain, adjoint and localization

The free S(t) is strongly continuous and bounded on every E_r on compact
time intervals. In normalized Fourier coordinates its off-diagonal sizes
are <xi>|sin(t|xi|)|/|xi|<=C_T and |xi||sin(t|xi|)|/<xi><=1.
Pointwise continuity and domination prove the strong assertion. No operator-
norm continuity of S(t) is invoked. Multiplication by H_j,R(t) is bounded
on every H^r, continuously in t, by weighted Fourier convolution/Peetre
and its compact smooth spatial derivatives. Consequently B(H_j,R(t))
maps E_r to E_(r+1): its first entry is0 and its second is H_j,R times
the input displacement in H^r.

Define, on states,

    A_j(I)z=int_I S(-t)B(H_j,R(t))S(t)z dt.                         (9)

The integrand is strongly continuous in E_(r+1) for each z in E_r and
uniformly bounded there on [0,T]. Its statewise Bochner integral gives

 ||A_j(I)||_(B(E_r,E_(r+1)))<=C_(j,r,R,T)|I|.                       (10)

In particular A_j(0,t) is LIPSCHITZ in precisely this operator norm. This
does not require a Bochner integral in the operator-norm topology for the
instantaneous conjugated wave multiplier.

The E_s pairing identifies the dual of E_r with E_(2s-r), isometrically
by their Bessel coordinates. Dualizing the gain E_r->E_(r+1) therefore
gives the E_s adjoint gain

 A_j(I)^*E_s:E_(2s-r-1)->E_(2s-r).                                  (11)

As r ranges over the reals this is gain one at every Sobolev index. It
agrees on Schwartz phases with the actual E_s adjoint of the bounded E_s
operator. In particular A_j and its adjoint act from E_(s-gamma) into E
because gamma<1. No physical multiplication cutoff has been declared
selfadjoint in E_s.

We justify support statements for both phase entries. The classical wave
finite-speed proof uses kinetic plus gradient energy on a shrinking ball.
The boundary flux is at most0. Initially vanishing data give zero velocity
and gradient in the cone; integrating the velocity from the initially
zero displacement gives zero displacement there too. Time reversal gives
the backward version. For every dimension here this proves that S(+-t)
enlarges supports by at most |t|. Smooth cutoff approximation, Schwartz
density and continuity against compact test functions extend this to all
Sobolev phases. Multiplication by H_j,R is supported in B_(2R), so (9)
has output support in B_(2R+T). If real compact smooth chi equals1 on
B_(2R+T+1), input (1-Dchi)z has zero free displacement on B_(2R) throughout
[0,T]; it contributes nothing. Hence, on every E_r,

    Dchi A_j(I)=A_j(I)=A_j(I)Dchi.                                 (12)

This proof applies to time-dependent, signed H_j,R and to d1 as well as
d2/3. It is a new application of the full phase finite-speed argument,
not an invocation of a static positive-mean theorem outside its scope.

The actual Sobolev pairing formula of the variance note, applied to (9),
and (8) now give for each fixed Schwartz pair

    E[g_j ell_R(I;z,w)]=<A_j(I)z,w>_E.                             (13)

Thus these deterministic operators are derived from the SAME-W covariance.
The mask in (7) is AFTER convolution. Inserting it inside Gamma*f_j would
give a different coefficient and invalidate (13).

## 5. Finite noise projections and BOTH variance operators

Let X_N(I)=sum_(j<=N)g_j A_j(I). These are actual finite bounded random
operators. Their primitives are Lipschitz B(E) paths by (10). Equation(13)
shows that their matrix forms are exactly the orthogonal Gaussian projection
of ell_R onto the span of g_1,...,g_N, so

 E|<X_N(I)z,w>|^2<=E|ell_R(I;z,w)|^2.                              (14)

They are smooth TEST-BASIS projections, not epsilon/delta source mollifiers.
No time independence or adaptedness of these finite projections is assumed.

Write a_j=J0 A_j J0^-1. Choose a real Schwartz ONbasis {e_k} of E. For fixed
Schwartz w, finite Gaussian covariance and then Parseval give

 sum_(j<=N)||A_j^*E w||_E^2
   =E||X_N^*E w||_E^2=sum_k E|<X_N e_k,w>_E|^2
   <=C_T h^(2-a)B_alpha(h)||w||_(E_(s-gamma))^2.                    (15)

Use (14), the accepted actual-variance Proposition1 for each finite k sum,
and nonnegative monotone convergence. The other direction uses its OTHER
finite-family inequality, with input z fixed and output e_k varying, giving
sum_(j<=N)||A_j z||_E^2 with the same bound. Here

 B_alpha(h)=1 if alpha<1; 1+log(1/h) if alpha=1; h^(1-alpha) if alpha>1.

Extend the quadratic bounds from dense Schwartz phases to E. In J0
coordinates they are exactly

 Vout_N=sum_(j<=N)a_j a_j* <=b_I D_gamma^2,
 Vin_N =sum_(j<=N)a_j* a_j <=b_I D_gamma^2,
 b_I=C_T h^(2-a)B_alpha(h).                                        (16)

C_T is uniform in N,R,I, as in the accepted actual variance result; no sum
of individual j-dependent bounds in (10) was used. The coordinate change
from its frequency J to J0 is unitary and commutes with the Bessel weight.

For complex phases define m_C(z1+i z2)=m(z1)+i m(z2), and similarly n_C,
using the real mean-square columns of that result. The Hilbert norms split
as sums of squared real/imaginary norms, so the same bounds hold. Both maps
are complex linear; their matrix form is linear in z and CONJUGATE linear
in w. The real a_j complexify isometrically: their operator norms and
singular values are unchanged, since a real Hilbert ONbasis complexifies
to a complex ONbasis. Thus all applications to the complex finite-matrix
Gaussian theorem preserve constants and multiplicities.

## 6. First-chaos columns and actual strong covariance tails

For fixed real Schwartz z, the accepted mean-square column m(z) has
coordinates ell_R(I;z,e_k), each in the CLOSED real first chaos W(H_W).
This assertion uses the actual linear test representation, not only the
word Gaussian. Their coefficients in g_j are <A_j z,e_k> by (13).
Scalar Parseval in that chaos and then in E, with positive Tonelli, gives

 sum_j||A_j z||_E^2=E||m(z)||_E^2,
 m(z)=sum_j g_j A_j z in L2(Omega;E).                              (17)

The same calculation for n(w), with the actual adjoint, gives
n(w)=sum_j g_j A_j^*E w. Cross coefficients have exactly these values by
(13). The tail equalities follow from orthogonal Gaussian projection;
no independence of the output coordinates is required.

Both expansions extend to every fixed E_(s-gamma) input. The individual
operators extend by (10)-(11). The finite column inequalities extend from
Schwartz inputs to that space by density and the gain one estimate; their
constant is uniform in N. Approximate a rough input by a Schwartz one,
apply the uniform L2 partial-sum bound to the difference, then take N to
infinity for the fixed Schwartz input in(17). The continuous real column
maps m,n give the other side of this approximation. This proves(17) on
the full claimed domain. Complexification works as in Section5.

For w in E, the convergent sum sum_j||A_j^*E w||^2 is a bounded positive
quadratic form. Polarization and Riesz give bounded positive operators
on E. Transport them by J0 and denote their H0-coordinate operators by
Vout_infty,Vin_infty. The finite partial sums in (16) increase to these
forms and keep the bound b_I D_gamma^2 on H0. Their positive tails T_out,N=Vout_infty-Vout_N and T_in,N
have quadratic forms tending to0. Since they are uniformly bounded,

 ||T_N v||^2<=||T_N||<T_N v,v> ->0,

so the tails tend STRONGLY to0. Weak limits in (12) also give

 Vout_infty=Pchi Vout_infty Pchi*,
 Vin_infty =Pchi* Vin_infty Pchi,
 Pchi=J0DchiJ0^-1,

and the analogous identities for their tails. Positive congruence applied
to T_N<=b_I D_gamma^2 yields

 T_out,N<=b_I B_out,       T_in,N<=b_I B_in,                        (18)

with the actual two compact envelopes of the accepted cutoff result.
In particular none of these steps assumes Pchi selfadjoint.

## 7. Finite Schatten estimates and compact domination of the tails

The ACTUAL family a_j,j<=N satisfies all hypotheses of the accepted
compact-cutoff Propositions2-3/Corollary4: bounded coefficients, BOTH
physical localizations (12), BOTH weighted variances (16), and independent
real g_j. Hence each coefficient is compact in the required ideals, and
for EVEN q>=2 with q gamma>d,

 (E||X_N(I)||_Sq(E)^q)^(1/q)
    <=sqrt(q-1) sqrt(C_T) h^(1-a/2)B_alpha(h)^(1/2)||Kchi||_Sq,
 Kchi=Pchi D_gamma.                                                (19)

The compact factor can depend on R,T through chi. For a fixed admissible
q0, ||Kchi||_Sq<=||Kchi||_Sq0 when q>=q0: normalize the singular-value
sequence by its l^q0 norm, after which every term is at most1. Its q-power
sum is then at most its q0-power sum. This proves the monotonicity, with
the zero case trivial. For beta in(1), the scalar power/log bound IMPLIES

    ||X_N(t)-X_N(u)||_(Lq B(E))<=C sqrt(q)|t-u|^beta                 (20)

for |t-u|<=1, uniformly N and even q>=q0; constants include the fixed
||Kchi||_Sq0. The strict beta bound is not equivalent to the natural profile.

Here is the new compact-tail fact in the needed generality. If
0<=T_N<=B, with B compact positive in S_m,m>=1, and T_N->0 weakly, then

    ||T_N||op->0,       Tr T_N^m->0.                               (21)

Choose a finite spectral projection Q of B with
||(1-Q)B(1-Q)||<epsilon. Positive quadratic Cauchy-Schwarz gives, for
unit x,

 <T_N x,x><=2<T_N Qx,Qx>+2<T_N(1-Q)x,(1-Q)x>
            <=2||Q T_N Q||+2epsilon.

Weak convergence makes the finite-dimensional matrix Q T_N Q converge
in norm to0. Thus ||T_N||op->0. The accepted compact positive-order minmax
fact gives lambda_j(T_N)<=lambda_j(B); each lambda_j(T_N) tends to0 by
operator-norm convergence. Dominated summation of lambda_j(B)^m proves
(21). There is no assertion T_N^m<=B^m. Apply (21) to (18), whose fixed-I
envelopes are in S_(q/2), to get vanishing q/2 trace powers of BOTH tails.

We need the finite Gaussian operator inequality with its two variance
trace powers RETAINED, not already replaced by a common envelope. If a
finite family of compact operators Z_l has output/input variances Vout,Vin
in S_m, m=q/2, the same finite-compression proof as the accepted cutoff
Corollary4 gives

 E||sum_l g_l Z_l||_Sq^q
    <=(q-1)^(q/2) [Tr Vout^(q/2)+Tr Vin^(q/2)]/2.                  (22)

Here are the relevant steps so this is a proved new application. Compress
by finite-rank orthogonal Q_k strongly tending to I. The compressed output
variance is at most Q_k Vout Q_k, since the difference is a sum of
Q_k Z_l(1-Q_k)Z_l*Q_k>=0; likewise for the input variance. Positive minmax
and compression minmax bound its trace power by the uncompressed one.
Apply the accepted finite MATRIX Gaussian Theorem1 on range Q_k, preserving
the average of the two trace powers. For each finite Gaussian coordinate
vector, compactness gives Q_k(sum g_l Z_l)Q_k operator-norm convergence;
singular values are norm-Lipschitz. Nonnegative Fatou over singular values
and then probability gives(22). Its extended norm is measurable by
continuity of the finite coordinate map into operator norm. No infinite
Gaussian or S_q-Bochner convergence theorem was assumed.

For X_M-X_N apply (22) to j=N+1,...,M. Its two variance operators are
bounded by T_out,N,T_in,N. Eigenvalue minmax and(21) show the right side
tends to0 uniformly M>N. Thus X_N(I) is Lq(B(E)) Cauchy, since operator
norm is at most S_q norm. It is also Cauchy in the EXPECTED q-th power
of its S_q difference at this admissible EVEN index. Lower or arbitrary
finite B(E) moment orders follow by choosing a larger even q; no such
argument is asserted for a smaller Schatten index.

## 8. Construction on the SAME space and fixed-interval compatibility

Each finite X_N(I) is strongly measurable in the separable closed real
span of {A_j(I)} inside the Banach space B(E). The preceding Cauchy property
has a limit there in Lq. One elementary construction avoids any Banach
martingale theorem: choose a subsequence whose Lq successive differences
sum to a finite number. Their L1 norms also sum finitely, so their pointwise
operator-norm differences are absolutely summable almost surely. Banach
completeness gives a limit; Fatou bounds the Lq distance of the full
sequence to it by the preceding Cauchy distances. This also proves strong
measurability in that closed separable span. The limit is an actual function
of the SAME g_j=W(f_j), on the original probability space.

Call it X_R(I). Limits constructed at different even q agree by uniqueness
of convergence in probability. Thus convergence holds in every finite
Lp(B(E)), p>=1. A pointwise operator-norm convergent subsequence shows its
values are compact. Singular-value Fatou and(19) give the same fixed-I
moment bound for S_q at every admissible EVEN q, and membership almost
surely for each such fixed interval. This is not a claim of an S_q path.
Every continuous linear functional of the limit is an L2 limit of centered
Gaussians, so it is centered Gaussian; the same holds jointly for finite
families of such evaluations.

For each fixed Schwartz pair, the finite matrix coefficients are the
orthogonal projections of ell_R onto g_1,...,g_N. Completeness of the
basis gives L2 convergence to that ACTUAL raw Gaussian form. Operator-
norm L2 convergence gives convergence to <X_R(I)z,w> as well. The two
limits coincide. This is SAME-W compatibility, not an equal-law substitute.
Intervals of length>1 are handled by finite unit partitions and additivity.
Their indicators sum to the long-interval indicator except at finitely many
endpoints, which have zero raw norm. The common fixed-support completion
and linearity of W_C therefore identify the summed raw forms with the
long-interval raw test itself. Strong-integral additivity gives the same
identity for each X_N, hence also its operator limit.

## 9. Actual time-path convergence, including measurability

The finite processes X_N(t)=X_N((0,t)) start at0 and have Lipschitz B(E)
paths by (10). Fix theta<eta<beta and a sufficiently large EVEN q0 with
q0 gamma>d and beta-eta-1/q0>0. Bound(20) holds with a common C sqrt(q)
for all even q>=q0. Coarse increments longer than1 are sums of finitely
many unit increments, with constants depending on T only.

Let D_n(F) be the maximum of adjacent increments on the dyadic grid
kT2^-n of [0,T]. For levels with T2^-n<=1,

 ||D_n(X_N)||_Lq <=2^(n/q) C sqrt(q)(T2^-n)^beta.

This uses the elementary maximum bound, NOT independence. The finitely
many coarse levels are bounded by the unit partition. Therefore

 sup_N ||sum_(n>=0)2^(n eta)D_n(X_N)||_Lq<=C_eta sqrt(q),           (23)

uniformly even q>=q0: the fine-level geometric ratio is at most
2^(-(beta-eta-1/q0))<1.

For a continuous Banach-valued F starting at0, finiteness of this dyadic
sum gives ||F||_Ceta<=C_(T,eta)sum 2^(n eta)D_n. To see it directly,
approximate any two times by dyadic times at the scale comparable to their
separation. Those grid points differ by at most two adjacent increments;
each endpoint's finer binary corrections sum to at most the tail of D_n.
The weighted sum bounds that total by a constant times the separation^eta.
Continuity identifies the endpoint limits. Apply this to the Lipschitz
finite paths. It proves uniform C^eta Lq bounds and the same bounds for
differences X_N-X_M by the triangle inequality.

For any fixed finite time grid, Section8 gives Lq convergence of every
point value. For a continuous F with bounded C^eta norm,

 ||F||infinity <=max_grid ||F(t_k)||+C mesh^eta||F||_Ceta.

Use this on differences, first send M,N to infinity at fixed grid, then
mesh to0, using the uniform bound(23). This proves Lq supnorm Cauchy.
The deterministic interpolation inequality

 ||F||_Ctheta<=C ||F||infinity^(1-theta/eta)||F||_Ceta^(theta/eta)     (24)

follows by bounding each difference both by 2||F||infinity and by its
C^eta bound, then splitting at the balancing scale. Its supremum term
is controlled as well. Scalar Holder in probability and q>=p show that
X_N is Cauchy in Lp C^theta for every finite p, choosing such a large even
q for each requested p.

The ambient Holder/operator space can be nonseparable. Nevertheless all
finite paths lie in the linear span of the COUNTABLE deterministic paths
{A_j(0,.)}, each Lipschitz and hence C^theta. Its C^theta-closed span is a
separable Banach space. The same elementary Lp Cauchy construction used
in Section8 applies in this span and gives a strongly measurable C^theta
limit M_R on the SAME probability space. An almost surely C^theta-convergent
subsequence converges uniformly in operator norm. All finite paths have
compact values on short intervals by Section7; for t>1, finite unit-interval
sums give compact X_N(0,t) as well. Therefore M_R has compact values at every time on that single
path set. This proves(2). The limits obtained for different p agree by uniqueness
of convergence in probability in the path norm, as in Section8.
Evaluation at any fixed time agrees
with Section8; (3) follows. The complexified version is obtained from the
four real pair identities and is sesquilinear as stated.

The finite paths are Gaussian linear combinations of deterministic paths.
Every continuous linear functional on their closed path span therefore
converges in L2 to a centered Gaussian. This proves the asserted Gaussian
path property. The construction used only compact smooth representatives, orthonormality
and completeness, so it applies to any such test basis. If a different
one is used on the SAME W,
compare matrix coefficients on a fixed countable dense Schwartz phase
collection and rational times. Both versions equal the same raw forms.
A countable null-set union, phase density and path continuity imply equality
of the two operator paths on one probability-one set for all times
(indistinguishability). There is no uncountable
compatibility assumption or independent time-increment argument.

## 10. Gaussian growth of the local path norm

Bound(23), followed by C^theta<=C C^eta and the Lq C^theta convergence,
gives ||M_R||_(Lq Ctheta)<=C sqrt(q) for all even q>=q0, with C independent
of q and the basis. For arbitrary p>=1 choose even q>=max(p,q0), with
q<=p+q0+2<=(q0+3)p. Lyapunov then gives the first bound(4), with an enlarged
constant independent of p.

Let Y=||M_R||_Ctheta and write the resulting constant as C1. If C1=0,
Y=0 and the exponential assertion is immediate. Otherwise
E Y^(2m)<=(C1 sqrt(2m))^(2m). Since
m!>=(m/e)^m, obtained by integrating log x from1 to m, the exponential
series has m-th term at most (2e c C1^2)^m. For c<1/(2e C1^2), positive
Tonelli and a geometric series prove the second assertion(4). This is an
elementary moment argument, not an unverified Fernique invocation.

The constants allow R,T dependence through the compact cutoff norm. These
are masked FIRST-driver estimates, not growth constants for a stochastic
solution. This completes the theorem.

## 11. Controls, boundary failures and remaining original scope

The 21 CM time controls use one UNNORMALIZED genuine compact smooth
positive-time test, rather than a numerical construction of the ONbasis,
supported[1,2], not a boundary-singular basis element. They compare moving
the derivative onto the test with finite differences. The actual d2
Gamma=delta_x1 tensorLeb_x2 mask-order controls distinguish
zeta_R(Gamma*q) from Gamma*(zeta_R q). Null raw tests and zero masked means
for some nonzero noise directions are allowed; no all-nonzero CM claim.
Four finite diagonal tail controls are only calibrations. Working precision
is not certified accuracy; none of these proves an operator or path bound.

The compact envelope in(21) is essential. On H0=L2(R^d;R^2), the actual whole-space NORMALIZED coordinates, choose
disjoint translated compact smooth normalized states e_j. They are
orthonormal there; their unitary E representatives need not have disjoint
physical supports.
Rank-one projections onto e_j tend weakly to0 but keep operator/Schatten
norm1 and are dominated only by noncompact I. Gaussian diagonal sums
sum g_j e_j tensor e_j have variance at most I and mean-square column
limits, yet no bounded sample operator: for finite M,
P(sup_j |g_j|<=M)=lim_N P(|g_1|<=M)^N=0. This boundary counterexample
lacks the compact physical localization/envelope. It is not a no-go for
the actual masked model, nor a contradiction of the accepted same-index
HS obstruction in d2/3. The present path is bounded in B(E); no HS claim.

Still open: canonical epsilon/delta SOURCE-driver convergence on its
correct common Laplace-slice construction, Young evolution and actual
source/canonicaldata identification, growing cones and lower asymptotics
in d2/3, sharp upper constants and source normalization/domain/label/
conditional exact-limit questions. The constant initial phase(1,0) is not
in global E and no point evaluation is inferred from H^(1/2) in d2/3.
Original full goal ACTIVE. No new Lean proof or71facts/18seams upgrade,
companion/contact/Skorohod/HPC/sourcefix/TeX/PDF/wiki/publication or
whole-paper/cold-reader clearance follows here.
