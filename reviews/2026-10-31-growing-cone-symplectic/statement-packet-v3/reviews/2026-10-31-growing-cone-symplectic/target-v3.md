# SP1-SP4: exact actual E source/raw/mean and block application

FROZEN UNREVIEWED refinement of v2; exact block-mean application added. No proof acceptance, stochastic upper
or source sharp constant is asserted. V1 diagnostics and evaluator repair
are retained. This wave addresses the original growing-cone upper route's
E-phase norm denominator, not a different goal or model subset.

## Objects and pairing

Use ALL original H:homog Gamma/amplitudes,d=1,2,3,0<a<1,alpha+a<2,
0<alpha<d or alpha=d=1. Fix any finite R,T>0, real amplitude c and real
even eta_R in C_c^infinity,0<=eta_R<=1,eta_R=1 onB_R,supp inB_2R.
Physical NOISE mask m_R=eta_R^2 ONCE after source smoothing.
E=H^(1/2)(R^d;R) x H^(-1/2)(R^d;R), with Hilbert direct-sum norm.
Let Lambda=(1-Delta)^(1/2) and C(u,v)=(Lambda^(1/2)u,Lambda^(-1/2)v),
an isometry onto real L2 x L2. Set J(q,p)=(p,-q),J_E=C^-1 J C.
Then J_E is an isometric skew-adjoint bounded operator with norm1 and
omega(z,w)=<z,J_E w>_E=dual(u,g)-dual(f,v),z=(u,v),w=(f,g).
Dual denotes the real H1/2,H-1/2 pairing, not a velocity L2 integral.

Let M=M_R(W) be the actual E interaction FIRST driver on[0,T], and
M_rho=M_R(Y_rho) the SAME-W-retaining ordinary-source approximations,
from accepted source-operator-convergence.md. These live in a separable
closed Ctheta operator-path span,1/2<theta<min(1-a/2,(3-a-alpha)/2).
All source limits below are at fixed R,T and actual noise parameters.

For any FIXED Phi in raw H_W put Z=W(Phi), ||Z||L2=||Phi||H_W, and define
D_Phi=E[Z M], D_Phi,rho=E[Z M_rho] as Bochner path integrals.
No H-valued raw Gaussian variable is assumed. Zero Phi is legal.
Their source coefficient is the deterministic real function
h_Phi,rho(t,x)=E[Z Y_rho(t,x)]. This is a cross covariance with the GIVEN W,
not a newly chosen equal-law RKHS realization. It is time continuous and
smooth in x at every fixed rho; its derivatives are obtained from the
accepted G-vector source representation, not sample supremum expectations.
The proposal includes the exact identities
 D_Phi,rho(t)=int_0^t S_E(-r)B(m_R h_Phi,rho(r))S_E(r)dr,
 ||D_Phi,rho-D_Phi||Ctheta <=||Phi||H_W ||M_rho-M||L2(Ctheta) ->0.
The deterministic driver D_Phi is defined by the Bochner covariance above;
no instantaneous raw mean function is presumed for arbitrary Phi.

Let H_rho=c M_rho+D_Phi,rho,H=c M+D_Phi.
Source ordinary coefficient b_rho=m_R(c Y_rho+h_Phi,rho).
The same eta_R^2 appears exactly ONCE in both terms. H drives the actual
Young interaction evolution U_H, with physical phase
P_H(t,s)=S_E(t)U_H(t,s)S_E(-s),0<=s<=t<=T.
Cases Phi=0 give original noise amplitude c; c=0 gives pure real
Cameron covariance means; c=Phi=0 gives the free wave.
At every fixed Phi,c the proposed source evolution converges in uniform
physical operator-difference norm in all finite Lp to P_H, as a consequence
to be checked of accepted Gaussian-source convergence, deterministic mean
convergence and Young stability/uniform moments. No uniform-in-Phi claim.

## SP1 ordinary source conservation

Propose P_Hrho(t,s)^* J_E P_Hrho(t,s)=J_E on a per-rho probability-one set,
for all0<=s<=t<=T. Signed source sample potentials allowed. Free wave
conservation must be verified in the correct Bessel coordinates, including
zero spatial frequency. For smooth compact real b, B(b)(u,v)=(0,bu) is
omega-skew by actual Sobolev duality. This does not say B(b) is skew for
the E Hilbert inner product. Ordinary source interaction coefficients
S_E(-r)B(b_rho(r))S_E(r) are uniformly bounded and strongly continuous on
states at fixed rho,R,T, so statewise differentiability of the bounded
interaction equation is a proposed route avoiding differentiation of the
unbounded free generator on arbitrary E states. Actual source response
and Young/Duhamel identity must be checked, not merely a formal ODE.

## SP2 raw and completed deterministic mean conservation

Propose P_H(t,s)^* J_E P_H(t,s)=J_E for all time pairs on one event for
these FIXED c,Phi,R,T. Use source uniform operator-difference convergence
and an a.s. subsequence; handle all times with the accepted uniform
triangle norm or countable times plus strong state continuity. Never
claim operator-norm continuity of S_E. Actual E/F restriction and uniqueness
must establish the evolution used, including its deterministic source
approximation. No static spectral replacement, positive potential,
Girsanov assumption, independent blocks or uncountable parameter event.

## SP3 norm baseline and exact growing-cone use

Propose ||P_H(t,s)||B(E)>=1 for every time pair, since ||J_E||=1 and the
SP2 identity. For the evolution the accepted Young inverse/free inverse
supplies invertibility; P*JP=J alone is NOT claimed to imply surjectivity
on infinite-dimensional E. No determinant or eigenstate argument for E.

At each fixed0<delta<1 take R=1/delta+2,T=1/delta,c=delta^((1-a)/2),
M constructed from actual W_fast; Phi may be any fixed direction in that
fast raw covariance Hilbert space (or zero). The same norm baseline holds
pointwise for EACHdelta, allowing no claim of uniform source cutoffs,
noise suprema or moment upper bounds along the growingR diagonal.

## SP4 exact deterministic block-mean application

Use accepted upper-cameron-compactness.md Section7 with J=0, supported
slow control Phi in H_I (closed subspace of H_slow), true block length
ell_m in[0,B], slow origin s_m, fast pullback isometry
 T_m f(s,x)=delta^(a/2-1) f((s-s_m)/delta,x).
Let T_m^*:H_slow->H_fast be its Hilbert adjoint; it is a contraction.
W_m(f)=W(T_m f) is the actual fast isonormal process. Define the FAST
Cameron direction
 phi_m=delta^(-a/2) T_m^* Phi in H_fast.
This direction can have norm as large as delta^(-a/2)||Phi||, which is
finite at FIXEDdelta but is NOT a uniform control-radius bound.

Let A_m=M_R(W_m) on the real E phase and D_(phi_m) be its SP2 covariance
driver using W_m(phi_m). Propose that for0<=u<=ell_m,
 D_(phi_m)(u)=H_(m,E)(Phi)(u),
 H_(m,E)(Phi)(u)=int_0^u S_E(-v) T_E Phi(s_m+delta v) S_E(v)dv,
where T_E Phi is the actual restriction to E of the accepted completed
mean field T Phi in Lr(I;K(F)). This is an EXACT source/mean application,
not merely a proposed direction with a compatible norm.

Required covariance check: for every completed fast row label k,
 E[W_m(k)W(Phi)]=<k,T_m^*Phi>_Hfast. The difference between W(Phi) and
W_m(T_m^*Phi) is orthogonal to the whole fast first chaos; actual A_m is
measurable in that chaos with mean0, so its Bochner covariance with this
difference vanishes. Use accepted C3(12) at J=0 and g_delta>0 to identify
 E[A_m W(Phi)]=delta^(a/2) H_(m,E)(Phi),
not sqrt(delta) H for the UNSCALED A_m. Indeed g_delta*delta^(a/2)
=sqrt(delta). This yields the proposed exact equality above.
Both constant columns in the accepted F formula must be restricted by i,
not discarded in the source construction or treated as dense E data.

Consequently the pure mean block's ACTUAL physical E endpoint
 S_E(ell_m)U_(H_(m,E)(Phi))(ell_m,0)
would have norm>=1 by SP2-SP3 with c=0 and direction phi_m. Empty blocks
ell_m=0 give identity. Stopped constant extension is only a path convention;
use the true endpoint ell_m. This supplies the E denominator needed in the
future E version of the physical product ratio. It supplies NO uniform
mean budget, residual estimate or growingR stochastic upper.

## Boundary and falsification

Corrected v2 rational surrogates check exact physical Bessel similarity,
four signed/offdiagonal Hamiltonian Cayley products and three false guards.
They are not a projection/discretization/convergence of this Gaussian PDE.
No new Lean declaration/count needed just for this functional-analytic
baseline; all74facts20seams/L0 remain unchanged. Kernel facts do not certify
source regularity, Bochner covariance, phase pairing or raw convergence.

Independent statement/source/actual-application and FULL proof gates remain
required. Current reviewer quota is not a report. GC1-GC3 transfer, uniformR
Gaussian/CM/regulator/localization estimates, signed-positive optimization,
intended source normalization/sharpconstants/conditional exactlimit stay
OPEN. No source repair/Skorohod/HPC/contact/companion/TeX/PDF/wiki/bib/
publication or whole-goal completion action.
