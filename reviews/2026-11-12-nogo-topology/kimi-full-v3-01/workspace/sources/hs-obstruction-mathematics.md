## 1. Actual phase, operator and statements

Let d in{2,3},s be ANYfixedreal number,T in(0,1]. Work first on real
E_s=H^s(R^d)xH^(s-1)(R^d),with inhomogeneousBessel norms. Write
<xi>=(1+|xi|^2)^(1/2) and Lambda=(1-Delta)^(1/2).
Use the massless freewave phase group with multiplier

 S(t,xi)=[[cos(t|xi|),sin(t|xi|)/|xi|],
          [-|xi|sin(t|xi|),cos(t|xi|)]],                  (1)

where the sinequotient atxi0 is its continuousvalue t. Both displacement
and velocity are retained. For a scalar h define B(h)(v,w)=(0,hv).
Fix a nonzero EVEN nonnegative H in C_c^infinity(R^d),suppH subsetB_A,
and a real k inW1infinity([0,T]) with its AC representative k>=k0>0.
Put h(u,x)=k(u)H(x),and define a strong-integral operator

 A_h(T)z=int_0^T S(-u)B(h(u))S(u)z du.                   (2)

We prove that A_h(T) is bounded onE_s but NOTHilbert–Schmidt,for every s.
For any real chi inC_c^infinity equal1 onB_(A+T+1),let Dchi multiply both
entries. We also prove A_h=Dchi A_h Dchi. Thus the obstruction remains
with a FIXEDcompact observation and compact physical coefficient; it is
not merely infinite spatial volume of an unmasked stationary operator.

Sections6-8 realize this h as the covariance mean of the ACTUALoriginal
Gaussian noise with a fixed test Z. They rule out a compatible
L2(Omega;HS(E_s)) realization of the localized Gaussian first-driver law.
They do not assume that law is an operator in any larger topology, and
supply no new Youngflow or stochastic moment nonexistence claim.

## 2. Boundedness, actual finite propagation and localization

The freegroup is bounded onE_s on each compact time interval. Indeed,
normalizing Fourier coordinates by diag(<xi>^s,<xi>^(s-1)), its nontrivial
offdiagonal sizes are <xi>|sin(t|xi|)|/|xi|<=C_T and
|xi||sin(t|xi|)|/<xi><=1; the diagonal is bounded by1.
Pointwise continuity,includingxi0,and domination prove strong continuity.
No operator-norm time continuity is claimed.

Multiplication by H is bounded onH^s for every real s. To see the exact
hypothesis, use the unitary Fourier transform
Ff(xi)=(2pi)^(-d/2)int exp(-ix.xi)f(x)dx. From
<xi><=sqrt(2)<eta><xi-eta> and its reversed version,
<xi>^s/<eta>^s<=2^(|s|/2)<xi-eta>^|s|. The Fourier kernel of multiplication
is (2pi)^(-d/2)Hhat(xi-eta). Its weightedabsolute kernel is dominated by an
L1convolution kernel, sinceHhat isSchwartz; Minkowski and translation
invariance ofL2 prove the bound. H^s embeds inH^(s-1),so B(H) is bounded
onE_s. For each z, the integrand of(2) is strongly continuous, with norm
<=C_T^2||B(H)|| ||k||infinity||z||. Its E_s Bochner integral defines a
bounded linear A_h. This is a strong integral,not an assumed HS integral.

For clarity the classical finitepropagation fact used here has a direct
energy proof. For Schwartz initialdata, the Fourier solution is smooth.
On a shrinking ball B(x0,r-t), differentiate
(1/2)int(v_t^2+|grad v|^2). The wave equation leaves the boundary flux
v_t partial_n v-(v_t^2+|grad v|^2)/2<=0. If initialdata vanish onB(x0,r),
this energy stays0. Time derivatives and gradients vanish in the cone;
integrating v_t along vertical lines and using initialv0 givesv0 there.
The same holds backward by time reversal. Consequently data supported in
B_A remain supported inB_(A+|u|),and data vanishing on a larger ball stay
zero in its interior backward cone. Standard cutoff approximation and
Schwartz density extend these distributional support statements toE_s:
S and smooth multiplication are bounded, and testing against a compact
smooth function is continuous in each Sobolev entry.

For Schwartz z, B(h(u))S(u)z is supported inB_A. Applying S(-u) puts its
output inB_(A+T),as does its time integral. Also(1-Dchi)z vanishes on
B_(A+T+1),so S(u)(1-Dchi)z is zero onB_A for0<=u<=T. Thus

 Dchi A_h=A_h=A_h Dchi.                                  (3)

These equalities extend toallE_s by boundedness and density. No density
of globalE_s in a localphaseF or positivity order of wavephases was used.
Initialconstant(1,0) need not belong toglobalE_s; this is a test of the
operator space used by the old construction,not a claim about all possible
state spaces for that initialdatum.

## 3. Full phase product and exact normalized Fourier kernel

Complexify only for Fourier analysis. A real orthonormal basis ofE_s
is a complex orthonormal basis of its complexification,so a realHS
operator has the same HS norm after complexification. Define the unitary
J_s:E_s^C->L2(R^d;C)^2 by its two Bessel-weighted Fourier coordinates.
The lower-left block of J_s A_h J_s^-1 is a bounded L2 operator K_s.
For r=|xi|>0,rho=|eta|>0, write c_r=cos(ru),s_r=sin(ru),and similarlyrho.
The complete elementary product is

 [[c_r,-s_r/r],[r s_r,c_r]] [[0,0],[Hhat(xi-eta),0]]
                 [[c_rho,s_rho/rho],[-rho s_rho,c_rho]]
 = [[-(s_r/r)Hhat c_rho,-(s_r/r)Hhat(s_rho/rho)],
    [c_r Hhat c_rho,c_r Hhat(s_rho/rho)]].

This is the new finite local lemma DimensionalMatrix.full_interaction.
Its symbolic divided-frequency matrices are used only atr,rho>0; the
physicalzero modes use (1)'s continuous sinc. The lower-left expression
itself extends continuously tozero.

Schwartz inputs/outputs justify all Fourier and time interchanges: the
weights have polynomial growth,Hhat has rapid decay in the difference,
andk is bounded on a compact time interval. The ACTUALcontinuous kernel is

 K_s(xi,eta)=(2pi)^(-d/2)<xi>^(s-1)<eta>^-s Hhat(xi-eta)
                  *I(r,rho),
 I(r,rho)=int_0^T k(u)cos(ru)cos(rho u)du.                 (4)

The factor(2pi)^(-d/2) is the unitary-Fourier convolution constant. This
kernel is obtained from the full phase matrices; there is no scalar
solution-value multiplier or covariance-monotonicity substitution.

## 4. A positive near-frequency-diagonal lower bound

Hhat is real,even,continuous and Hhat(0)=(2pi)^(-d/2)intH>0.
Choose epsilon>0 with Hhat>=Hhat(0)/2 onB_epsilon,
epsilon T<=1 andepsilon<=1. Set
J0=int_0^T k(u)du>0 and B0=||k||infinity+T||k'||infinity>0.
For |xi-eta|<=epsilon,reverse triangle gives |r-rho|T<=1.
Since cos z>=1-z^2/2 forrealz, the difference integral
Ddiff=int k(u)cos((r-rho)u)du is >=J0/2.
Forr>0, integration by parts in the AC functionk gives

 |Dsum|:=|int k(u)cos((r+rho)u)du|<=B0/(r+rho)<=B0/r.

The lower endpoint contributes k(0)sin0=0; the upper and derivative
terms give exactly the stated bound. Product-to-sum yields
I=(Ddiff+Dsum)/2. Pick
R0>=max(1,2epsilon,4B0/J0). Then onr>=R0,

 I>=J0/4-B0/(2r)>=J0/8>0.                               (5)

Both reused scalar lemmas have exact applications here.
PhaseResponse.two_frequency_average takes x=ru,y=rho u. For the purely
scalar PhaseResponse.frequency_window, set its parameters
J=I,A=Ddiff/2,B=B0/2,t_win=1,r_win=r,a_win=1.
A>=J0/4>0,B>=0,andits threshold2B/(At_win)=B0/A<=4B0/J0<=r holds.
Its error bound is |I-A|<=B0/(2r)=B r^(-1),so r>0 gives all its rpow
hypotheses. Its lower conclusion is I>=A/2>=J0/8. The indexa_win=1
is NOTthe actual temporal-noise exponenta,which stays in(0,1).
t_win=1 is also an auxiliaryscalar parameter; physicalT was not changed.
The unchanged proof internals do not supply the analytic time/error bounds.

The Besselweights give the same highfrequency order for ANYfixedreal s.
The reverse triangle inR^(d+1) gives |<xi>-<eta>|<=|xi-eta|.
Forr>=2epsilon,<eta>/<xi> lies in[1/2,3/2],so <xi>/<eta> lies in[1/2,2].
Taking logs and then the real power s gives

 <xi>^(s-1)<eta>^-s=<xi>^-1(<xi>/<eta>)^s
          >=2^(-|s|)/<xi>>=2^(-|s|)/(sqrt(2)r),r>=1.

Together with(4)-(5),this proves for some c_s>0

 |K_s(xi,eta)|>=c_s/|xi| on |xi|>=R0,|xi-eta|<=epsilon.   (6)

The constant can depend on s andthefixeddata,not the frequency cutoff.
No assertion of uniformity over all Sobolevindices is needed.

## 5. Actual finite-frequency HS norms diverge

Let P_N be Fourier-space multiplication by1_(B_N),not a projection onto a
periodic or spatialbox model. The kernel of P_N K_s P_N is its continuous
kernel(4) restricted toB_N xB_N,so it is inL2 there and gives the actual
truncated operator by density of compact smooth testfunctions in the ball.
For such an L2 kernel, Parseval in its second variable with an orthonormal
basis and then positive Tonelli prove
||P_N K_s P_N||HS^2=int_(B_N x B_N)|K_s(xi,eta)|^2d xi d eta.
This also supplies the needed kernel/HS criterion self-containedly.

Use the ACTUALband R0<=|xi|<=N-epsilon,|xi-eta|<=epsilon. Both frequencies
are inB_N; the change eta=xi-z has Jacobian1. From(6),

 ||P_N K_s P_N||HS^2
 >=c_s^2 |B_epsilon| |S^(d-1)| int_R0^(N-epsilon)r^(d-3)dr. (7)

For d2 the right side grows as log((N-epsilon)/R0),and for d3 as
N-epsilon-R0. It diverges in either case. If A_h wereHS, its normalized
block and all its frequency truncations would have HS norm at most
||A_h||HS,by the elementary HS ideal bound (or by Bessel's inequality
on an orthonormal basis). Equation(7) contradicts this. Thus

 A_h(T) is NOTHS(E_s) for every s,d in{2,3}.              (8)

Equation(3) shows compact physical localization does not remove this
obstruction. It is ultraviolet near the frequency diagonal,not infinite
physical volume. In d1 the same lower radial integral is int r^-2dr,
which converges; this is consistent with the accepted d1 driver and
asserts no new d1HS theorem from a single block.

## 6. An actual original Gaussian mean produces this compact coefficient

Now take ANYnonzeroGamma in the canonical H:homog class in d2or3:
nonnegative,even,positive-definite tempered Radon covariance,with
0<alpha<d,0<a<1 andalpha+a<2. Its raw Gaussian test covariance is

 B_W(F,G)=int int|u-v|^-a intGamma(dz)intF(u,x)G(v,x-z)dx du dv. (9)

W on its realtestHilbertcompletion is the SAMEnoise in the original
model. No d2/3white noise, density assumption or Riesz-only replacement
is made. Choose L>=1 with0<Gamma(B_L)<infinity, and a realeven
nonnegative q inC_c^infinity withq>=1 onB_(2L+1). Put U=Gamma*q.
On each compact x-set its defining integral and every q-derivative
involve only a compact Gamma-set; localfiniteness justifies differentiation
and continuity. Hence U is locallysmooth,even,nonnegative and U(0)>0.
Moreover Q_sp:=intqU is finite and

 Q_sp>=|B_(L+1)| Gamma(B_L)>0,                            (10)

since q(x)q(x-z)>=1 forx inB_(L+1),z inB_L.

Choose a smooth realeven physical mask zeta_R>=0,equal1 onB_R and
supported inB_(2R),R>=1. Then H=zeta_R U is even,nonnegative,compact
smooth,nonzeroat0. It meets Sections1-5 with A=2R. The physical mask
is AFTERthe covariance convolution,not Gamma*(zeta_R q).

Choose a nonnegative real C1 function f onR supported in[0,1],with its
value andderivative0 atboth endpoints andm_f=intf>0. A positive compact
smooth function in(0,1) is one choice. Define
k(u)=int_0^1|u-v|^-a f(v)dv for0<=u<=1.
Zeroextension and moving the derivative ontof givek inC1,with
||k||infinity<=2||f||infinity/(1-a),||k'||infinity<=2||f'||infinity/(1-a).
These bounds follow from localintegrability of |u-v|^-a; differentiation
is also valid distributionally followed by ordinary continuity.
Since|u-v|^-a>=1 ontheunit square,k>=m_f>0.

The test Z=W(f tensorq) belongs to the ACTUALrawtestcompletion. Indeed
smoothinterior cutoffs followed by positive mollification approximatef
inC1: f=f'=0 at endpoints makes the derivative cutoff errors vanish.
Time Schur then bounds the noise-norm error by a fixed multiple of the
L2time error. Its variance is exactly

 EZ^2=Q_sp int_0^1 f(u)k(u)du in(0,infinity).              (11)

All Gaussian variables stay onW. No point evaluation of noise was used.
In particular k(u)H(x) is the actual covariance mean of the physically
masked rawnoise withZ,including for singular or invariant-direction Gamma.
Only local smoothness and mass were needed,not decay ofU or a spatial
L2ground state.

## 7. Exact Gaussian first-driver forms with the Sobolev adjoint

Let chi inC_c^infinity be real and1 onB_(2R+T+1). On realSchwartz phases
z,w,write v_u=[S(u)z]_1 and define

 G_w,chi(u)=-sin(u|D|)/|D| [chi Lambda^(2s)w_1]
                 +cos(u|D|)[chi Lambda^(2s-2)w_2].        (12)

These are Schwartz functions uniformly onthefixedtime interval. The
sinequotient has its continuouszero limit. Applying the L2transpose
ofDchi S(-u),with the two Es Besselweights, gives EXACTLY

 G_w,chi(u)=Lambda^(2s-2)(((Dchi S(-u))^*_(E_s)w)_2).

Thus Dchi is NOTsilently selfadjoint inEs,and it has not been commuted
through a freewave or a Besselweight. For any smoothcoefficient b,
ordinary duality gives

 <Dchi S(-u)B(b(u))S(u)z,w>_(E_s)
        =int b(u,x)v_u(x)G_w,chi(u,x)dx.                 (13)

Define the actual deterministic noise test
F_z,w(u,x)=1_(0,T)(u) zeta_R(x)v_u(x)G_w,chi(u,x).
It is smoothcompact in x and bounded on the time interval,with only the
indicator endpoint jumps. Its rawnoise norm is finite. More generally,
for tests F supported in a fixed compact K in space,

 |B_W(F,F)|<=|K|Gamma(K-K)*[2^a T^(1-a)/(1-a)]
                   *||u->||F(u)||infinity||L2(0,T)^2,    (14)

by the absolute spatial bound and time Schur. Approximation by smooth
interior timecutoffs/mollification with common spatial support proves
F_z,w lies in the testHilbertcompletion. This uses fixed masked tests
only. NOhigher-dimensional version of the d1 boundedmask multiplier on
the ENTIREnoiseHilbertquotient is assumed or needed.

Define the Gaussian bilinear first-driver form ell_chi(z,w)=W(F_z,w).
At any smooth sourcewidth, pairing the ordinary localized first response
withz,w is exactly the corresponding linear noise functional W^rho(F_z,w),
by(13) andordinary timeintegration. The raw fixed-pair Gaussian law is
therefore precisely the formal Dchi intS(-u)B(W_R(du))S(u) with
W_R(F)=W(zeta_R F),whenever compatible testwise limits are taken.
We construct the rawform directly bycompletion; no HSoperator or
higher-dimensional source-operator convergence was assumed.

Absolute Fubini in(9) is legitimate for F_z,w andf tensorq: both have
fixed compact spatial support andbounded time envelopes, Gamma has
finite mass ontheir compact differences,and the time kernel is locally
integrable. Equations(9),(12)-(13) yield the SAME-W covariance identity

 E[ell_chi(z,w)Z]
 =int_0^T k(u)int zeta_R(x)U(x)v_u(x)G_w,chi(u,x)dx du
 =<Dchi A_h(T)z,w>_(E_s)=<A_h(T)z,w>_(E_s).              (15)

This is derived fromtheactualtestlaw,notpostulated as an operator premise.

## 8. The compatible L2HS reconstruction is impossible

Suppose a stronglymeasurable X_chi inL2(Omega;HS(E_s)) ontheSAMEspace
satisfied <X_chi z,w>=ell_chi(z,w) almostsurely for every fixed real
Schwartzpair. Z is inL2 by(11). Cauchy-Schwarz gives
E||Z X_chi||HS<=||Z||2||X_chi||L2HS<infinity,so its Bochner expectation
Y=E[Z X_chi] belongs toHS. Matrix evaluation is a continuous functional
onHS,so(15) gives <Yz,w>=<A_hz,w> for everyfixedSchwartzpair.
Both Y andA_h are bounded,so density impliesY=A_h,contradicting(8).
No simultaneous uncountable almostsure version or extra independence
was used,and no measurability withrespect toW beyondthefixed-pair law
is needed. This proves there is NOsuch L2HS realization.

