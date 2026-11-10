# Derived occupation bounds for the intrinsic second-moment constant

AUTHOR PROOF, UNREVIEWED. OC1-OC4 FIT passed17HIGHchecks atb2942ef,
368.062seconds; that did NOT accept this new proof. The full proof/application
gate is required. Le's2026-10-31 instruction is to derive the constant from
the model; matching Chen's predictions is not a completion requirement.

## 1. Exact model, prior inputs and the derived constant

Fix every original H:homog covariance Gamma and its actual amplitude in
d=1,2,3,0<a<1,0<alpha<d or alpha=d=1,alpha+a<2. Gamma is an even nonnegative
positive-definite homogeneous tempered Radon measure. Put I=(0,1),
K(s,t)=|s-t|^-a (assign any finite value on the null diagonal),
q=4-alpha>2,k=3-alpha=q-1>1,m=q/k. In particular q-2a>2-a>1.
No restriction alpha<=1 or q>=3 is imposed in d2/3. All fields are REAL.

OWN accepted inputs, exact roles:

- B=all-dimensional-static-occupation-bridge.md,scientific249e2c4,
  Sections3-5,(11),(15)-(18): the actual physical form
  B_Gamma(f,h)=int dx int Gamma(dy)f(x)h(x-y),
  positive finite R_sp, and continuous physical four-linear form
  C4(f1,f2,f3,f4)=B_Gamma(f1 f2,f3 f4) on full H1. With
  N(f)=||f||2^(1-alpha/4)||grad f||2^(alpha/4),
  |C4(f1,f2,f3,f4)|<=R_sp product_j N(fj),
  A_sp(f)=B_Gamma(f²,f²)<=R_sp||f||2^(4-alpha)||grad f||2^alpha.
  It gives actual covariance PSD/CS on H1 squares, representative independence,
  compact smooth H1 density, and the full strongly-H1-measurable class O
  defined below. No angular density of Gamma or global H1 supremum embedding.
- U=uniform-e-cameron-regulator.md,f54e92b: H_sp is the ORIGINAL spatial
  covariance test-null completion. Smooth test inner products equal the
  physical B_Gamma, with Gamma applied once.
- PB=physical-signed-positive-score-comparison.md,scientific40ec9a9,
  adopted d52d1d8, PB0 andPB5: J:L2(I;H_sp)->H_I, H_I=H_t tensor H_sp,
  has ||JF||²=int int K(s,t)<F(s),F(t)>dsdt. Positive smooth spacetime
  Psi belongs to the SAME raw space and ||Psi||²=v_Psi=int Psi h_Psi.
  For the SAME original canonical point solution and each fixed x,
  C2:=lim_(T->infinity)T^-kappa log E|u(T,x)|²=S_2^pos=2^m S_1^pos,
  kappa=(4-alpha-a)/(3-alpha).
- UL=unmasked-variational-lower.md,61ac2a3,Sections1-4,6-7: C_pos is ALL
  nonnegative nonzero smooth compact spacetime tests, including nonseparable
  tests. For each such Psi, h_Psi,s=int K(s,t)(Gamma*Psi_t)dt is jointly
  measurable and globally bounded, and
  lambda_Psi(s)²=sup_(real||f||2=1,f inH1)
                   [int h_Psi,s f²-||grad f||2²]>=0.
  I_Psi=int lambda_Psi(s)ds, v_Psi=E W(Psi)²,
  S_c^pos=sup_(Psi inC_pos)(cI_Psi-v_Psi/2)=c^m S_1^pos.
  No unmasked ground eigenstate is required.
- RawValueCeiling.strict_log_gap: unchanged complete public type and
  standard-three axiom evidence in local-checks/raw-value-ceiling-v1;
  its guards are a>0,q-2a>0. Only this scalar deduction is reused in Section6.
  It does not certify this note's analytic occupation or moment arguments.

Our bounds are for the ACTUAL C2 just identified, not a fitted conjectural
constant. For positive labels c other than2, S_c is auxiliary, not an
assertion about actual p=c moments or the first mean.

O consists of strongly H1-measurable g:I->H1(R^d), ||g_s||2=1 a.e., with
T(g)=int_I b_s ds<infinity, b_s=||grad g_s||2². Set
 A(g)=int int K(s,t)B_Gamma(g_s²,g_t²)dsdt,
 C_occ=sup_(g inO) A(g)/T(g)^(alpha/2),
 E_eta^O=sup_(g inO)[A(g)-eta T(g)], eta>0.              (1)
These are OWN raw-kernel occupation objects. We prove their legitimacy
before using their values. Define F_b(0)=0 and, for z>0,0<=b<q/2, put
 F_b(z)=k[(q-2b)^((q-2b)/2)/(8(q-b)^(q-b))
                   *(2z/(2-alpha))^((2-alpha)/2)]^(1/k). (2)
Here b is a DISPLAY parameter; F_0 does not change the actual temporal a.

Gamma=0 is separate: raw norms, h, I, S_c and C2 vanish. In(1), A=0,
C_occ=0. Every unit H1 profile has positive gradient energy, but dilating
a fixed unit compact profile by ell^(d/2)g(ell x), ell->0, makes T->0.
Thus sup(-eta T)=0, so E_eta^O=0. With F_b(0)=0 all non-strict bounds
below are zero identities. Strict ratios are asserted only for Gamma!=0.
Assume Gamma!=0 henceforth.

## 2. Full-H1 squares in the ACTUAL spatial and raw completions

Let f_n be compact smooth real profiles converging to f in H1. Such
approximants exist by input B. For smooth f_n,f_l, the physical norm is
 ||f_n²-f_l²||H_sp²
 =C4(f_n-f_l,f_n+f_l,f_n-f_l,f_n+f_l)
 <=R_sp N(f_n-f_l)²N(f_n+f_l)² ->0.                     (3)
Indeed N is continuous on H1 and N(h)<=||h||H1. Completeness defines Q(f)
in H_sp. Interlacing two approximating sequences proves independence.
Passing physical C4 continuity and the Hilbert inner product to limits gives

 <Q(f),Q(h)>H_sp=B_Gamma(f²,h²), ||Q(f)||²=A_sp(f).       (4)

The same difference estimate proves continuity f->Q(f) on H1: approximate
f,h by smooth functions in(3), pass to the limit, then use N(f-h)->0
and boundedness of N(f+h) when h->f. This is a covariance-space square
map, not a claim of pointwise H1 multiplication into Linfinity.

For every g inO, F_g(s)=Q(g_s) is strongly H_sp-measurable by continuous
composition. On the unit-mass class, (4) and input B give
 int ||F_g(s)||²ds<=R_sp int b_s^(alpha/2)ds
                  <=R_sp T(g)^(alpha/2)<infinity,        (5)
by concavity, since0<alpha/2<1 and |I|=1. Hence rho_g:=JF_g is a genuine
element of ORIGINAL H_I. PB0's norm identity and(4) show

                         ||rho_g||HI²=A(g).             (6)

The joint physical integrand and its representative independence are those
constructed in input B Section5; equivalently (4) is a continuous function
of the two H1 arguments and is jointly measurable after composition. Thus
(6) identifies the actual physical integral, not a surrogate abstract form.
All time bilinear integrals are absolutely finite by PB0's Schur bound.

We also require the mixed identity with an actual Psi inC_pos. At each
time t choose one fixed compact smooth chi=1 on ALL spatial supports of
Psi_t. For any f inH1, take f_n as above. Then
 <Psi_t,Q(f)>H_sp=lim_n B_Gamma(Psi_t,f_n²)
 =lim_n C4(chi,Psi_t,f_n,f_n)
 =C4(chi,Psi_t,f,f)=B_Gamma(Psi_t,f²).                   (7)
All products here are pointwise products; Gamma convolution is separate.
The C4 bound proves absolute convergence and justifies these limits.

Polarize PB0's norm identity (or pass from its finite tensors) to obtain
 <Psi,rho_g>HI=int int K(s,t)<Psi_t,Q(g_s)>H_sp dtds.
Its absolute value integrand is dominated by the product of the two
H_sp norms against K, integrable by Schur and L2 Cauchy-Schwarz. Equation
(7), evenness of Gamma and Tonelli for the nonnegative physical integrands
therefore identify

 <Psi,rho_g>HI=int_I int_Rd h_Psi,s(x)g_s(x)² dxds,
             <=sqrt(v_Psi A(g)).                       (8)

The latter is the ACTUAL raw Hilbert Cauchy-Schwarz inequality, using
PB0's ||Psi||²=v_Psi and(6). No unmasked potential or stochastic flow
for the rough occupation rho_g is constructed. This proves Lemma OC0.

## 3. Finite occupation energy, dilation and exact ratio identity

Unit L2 H1 profiles have positive gradient energy: a zero weak gradient
would make the function constant, and an L2 constant on R^d is0. Thus
b_s>0 a.e., so0<T(g)<infinity. Input B's physical covariance CS gives
 B_Gamma(g_s²,g_t²)<=R_sp b_s^(alpha/4)b_t^(alpha/4).
The raw temporal row maximum is K0=2^a/(1-a), by direct integration.
Apply Schur to F(s)=b_s^(alpha/4) and then concavity as in(5):

             0<=A(g)<=K0 R_sp T(g)^(alpha/2).            (9)

O is nonempty by a fixed compact smooth unit spatial profile constant
in time. Its A(g)>0 by input B's A_sp>0 and the positive time integral.
Consequently0<C_occ<=K0 R_sp<infinity. No strict positivity of every
off-diagonal spatial pairing is asserted or needed.

For ell>0, (U_ell g)_s(x)=ell^(d/2)g_s(ell x) is an L2-unitary H1
isomorphism with inverse U_(1/ell), so it is a bijection on O and preserves
strong measurability. The actual Radon change of variables gives
 B_Gamma((U_ell f)²,(U_ell h)²)=ell^alpha B_Gamma(f²,h²):
the two densities contribute ell^(2d), dx contributes ell^-d and the
pushforward of Gamma contributes ell^(alpha-d). Hence
 A(U_ell g)=ell^alpha A(g), T(U_ell g)=ell²T(g).           (10)

Taking the union over g and ell does not enlarge O (ell1 includes it).
For A>0,T>0, derivative of A ell^alpha-eta T ell² has sign
alpha A-2eta T ell^(2-alpha), so its global maximum is at
ell=(alpha A/(2eta T))^(1/(2-alpha)). It equals
 D_eta[A/T^(alpha/2)]^(2/(2-alpha)),
 D_eta=(2-alpha)/2*(alpha/(2eta))^(alpha/(2-alpha)).
For A=0 the supremum is0 as ell->0, the same formula with zero ratio.
Bound every ratio by C_occ and approximate that positive supremum from
below. Continuity of the positive power proves BOTH inequalities in

 E_eta^O=D_eta C_occ^(2/(2-alpha)) in(0,infinity),
 E_eta^O=eta^(-alpha/(2-alpha))E_1^O,
 C_occ=(2E_eta^O/(2-alpha))^((2-alpha)/2)
                                *(2eta/alpha)^(alpha/2). (11)

No occupation optimizer, compactness or minimax interchange is assumed.
This proves Proposition OC1.

## 4. Countable Rayleigh near-occupations in every original dimension

Fix Psi inC_pos and H=H_Psi=sup_(s,x)h_Psi,s(x)<infinity. Choose a
countable compact smooth real family dense in H1; discard0 and normalize
each element in L2. The resulting f_j are dense IN THE L2-UNIT H1 SPHERE:
an H1 approximation to a unit vector has L2 norms tending to1, so its
normalized approximation converges in H1 as well. All b_j=||grad f_j||2²
are finite. The bounded-potential form is H1-continuous, hence UL gives
lambda_Psi(s)²=sup_j R_j(s), R_j(s)=int h_Psi,s f_j²-b_j.
These functions and lambda² are measurable by the accepted mean/rate
properties and bounded-potential integration. For eps>0 put
 U_j={s:R_j(s)>lambda_Psi(s)²-eps},
 A_1=U_1, A_j=U_j minus union_(i<j)U_i.
The U_j cover I up to any canonical null set. The FIRST-INDEX cells A_j
are Borel, not necessarily open, and form a disjoint partition. On any
remaining null set choose one fixed unit compact profile.

Set g_eps(s)=f_j on A_j. Finite-valued truncations using f_1 on the
remaining cells converge pointwise in H1, so g_eps is strongly measurable.
It has L2 norm1 a.e. Since lambda²>=0 and h<=H, its choice gives
 b(g_eps(s))<int h_Psi,s f_j²-lambda_Psi(s)²+eps<=H+eps.
Therefore g_eps belongs to the ACTUAL O, with finite integrated kinetic
cost. No unmasked ground vector, spatial supremum embedding, continuum
selector or convergence as eps->0 is required.

Integrate its defining inequality and use(8):
 int lambda_Psi(s)²ds+T(g_eps)
       <=<Psi,rho_(g_eps)>HI+eps<=sqrt(v_Psi A(g_eps))+eps.
Time Cauchy-Schwarz on unit I gives I_Psi²<=int lambda_Psi². Thus

 I_Psi²+T(g_eps)<=sqrt(v_Psi A(g_eps))+eps.               (12)

This is the direction needed for an UPPER bound. The occupation is only
a deterministic raw Hilbert test in this argument; no rough occupation
is passed as a stochastic lower-bound control. This proves Lemma OC2.

## 5. The computed scalar coefficient and original moment ceiling

Fix Psi and write v=v_Psi>=0,C=C_occ>0,beta=alpha/4 in(0,1/2).
Definition of C and(12) give, for every eps>0,
 I_Psi²<=sqrt(vC)T^beta-T+eps for some T=T(g_eps)>0.
The right side is at most its supremum over ALL T>=0, independently of
eps or g_eps. If v=0 that supremum is0, so I=0 by eps->0. If v>0,
the derivative beta sqrt(vC)T^(beta-1)-1 decreases from positive infinity
to-1; the unique global maximum occurs at
T_*=(beta sqrt(vC))^(1/(1-beta)). Its value is
(q/4)(alpha/4)^(alpha/q)(vC)^(2/q).
Thus after eps->0 in either case,
 I_Psi<=D v^(1/q),
 D=sqrt(q/4)(alpha/4)^(alpha/(2q))C^(1/q).                (13)

For every c>0, cI-v/2<=cD v^(1/q)-v/2. The latter is0 at v0, tends
to minus infinity as v->infinity, and has strictly decreasing derivative
(cD/q)v^(1/q-1)-1/2. Its unique positive global maximizer is
v_*=(2cD/q)^(q/k), with maximum k v_*/2. This is the RAW HALF cost.
Squaring D and multiplying positive powers yields
 (2D/q)^q=q^(-q/2)(alpha/4)^(alpha/2)C.
Use k+alpha=3 and(11). The same maximum has the two EXACT forms

 U_c=c^m k[alpha^(alpha/2)C_occ/(8q^(q/2))]^(1/k)
    =c^m(2eta)^(alpha/(2k))F_0(E_eta^O), eta>0.           (14)

For clarity, substituting(11) leaves
2^-k*(eta/2)^(alpha/2)=(2eta)^(alpha/2)/8 inside the1/k power.
No factor2eta is omitted. Taking the real supremum over the actual C_pos
class gives S_c^pos<=U_c. PB5 then gives the SAME original point limit

 C2<=U_2=2^m(2eta)^(alpha/(2k))F_0(E_eta^O), ALL models. (15)

The bound is independent of eta because(11) cancels that factor. It retains
the actual temporal a through C_occ and E_eta^O even when b=0 in F_b.
This is a derived UPPER ceiling, not equality or attained sharpness of
the ceiling. The exact constant remains the PB variational formula.
This proves Theorem OC3.

## 6. Comparisons are consequences, not prescribed answers

At q=4-alpha the OLD certified strict_log_gap gives Delta(q,a)>0 from
a>0,q-2a>1>0, with no q>=3 hypothesis. Here
Delta=[qlogq+(q-2a)log(q-2a)]/2-(q-a)log(q-a).
From the positive bases in(2), subtraction of logarithms gives exactly
 log(F_a(z)/F_0(z))=Delta/k for any z>0.
Consequently

 c^m F_a(E_eta^O)/U_c
        =exp([Delta-(alpha/2)log(2eta)]/k).               (16)

For eta1/2, (15)-(16) yield
 C2<=2^mF_0(E_half^O)<2^mF_a(E_half^O).                  (17)
For eta1 the comparison has the stated scalar sign gate; it is not
universally favorable. At alpha5/4,a1/2,d2, the factors of4 cancel and
 8[Delta-(alpha/2)log2]
       =log[(11^11*7^7)/(2^5*9^18)]<0,
because150094635296999121<234966429149994773<4803028329503971872.
Thus the UPPER BOUND U_c(1) exceeds c^mF_a(E_1^O) there. This refutes
only that automatic comparison of bounds; it proves no failure of the
actual moment inequality. No stronger uniform-sign assertion is used.

For an independent spatial normalization, input B gives
 E_sp=sup_(unitrealH1)[A_sp-b/2]
     =(2-alpha)/2*alpha^(alpha/(2-alpha))*R_sp^(2/(2-alpha)).
Equation(9) and the first form of(14) give the explicit ceiling
 C2<=2^m K0^(1/k)F_0(E_sp).
The accepted B equation(18) gives S_1^pos>=M_a^(-1/k)F_0(E_sp), with
 M_a=Gamma_E((1+a)/2)/[Gamma_E(1+a)Gamma_E((1-a)/2)].
Gamma_E denotes Euler's Gamma function, not the spatial covariance.
Using PB5 on this SAME model therefore records the computed bracket

 2^m M_a^(-1/k)F_0(E_sp)<=C2<=2^m K0^(1/k)F_0(E_sp).    (18)

This uses a common SPATIAL energy, not an assumed source first moment.
Alternatively the already accepted all-alpha-damped-lower.md,ed2e5f5,
(3)-(4), supplies C2>=2^m V(a/2)^(-1/k)F_a(E_star^O), with0<V<1 and
the DIFFERENT damped time kernel/half-gradient occupation energy. Combining
that lower bound with(15) is legitimate, without identifying its energy
with E_eta^O. All imported lower bounds retain their earlier proof scopes.
This proves Corollary OC4 and the comparison formulas.

Le's revised goal is the actual derived constant; (16)-(17) do not choose
the author's intended normalization or impose his conjectured value.
Printed raw E uses kinetic1, while printed damped E_star uses kinetic1/2;
their documented source/domain issues stay comparison qualifications.
No source PDF, mathematical definition or unadopted1.24proposal is repaired.

## 7. Calibration and evidence boundaries

[held back: collaborators' unpublished work]

New alpha>1 scalar tests check the coefficient algebra at synthetic C_occ,
not a physical occupation energy or PDE. The first-index construction,
actual singular-Radon covariance membership, all limits and global scalar
optimizations are justified analytically above, not by those rows. All old
finite kernel proof internals are reused unchanged; no new formal theorem,
compiler, package or companion. Every NEW analytic assertion in this note
still awaits its OWN full independent proof/application gate. No novelty,
human/whole-paper/cold-read/public/correspondence/companion/HPC clearance.
