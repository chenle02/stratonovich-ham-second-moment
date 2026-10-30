# Actual physically masked first-driver variance forms: frozen target

UNREVIEWED statements/objects/feasibility before a long proof. Full original
all-dimensional sharp/source objective retained. d in{1,2,3}, a=alpha_0 in
(0,1), alpha+a<2, 0<alpha<d or alpha=d=1, Gamma NONZERO in canonical
H:homog, SAME original real raw Gaussian W. Complex extension W_C(F)=
W(Re F)+iW(Im F), E|W_C(F)|^2 is the complex covariance form.
Spatial Fourier is unitary c_d=(2pi)^(-d/2). Fix a real even C_c^infinity
zeta>=0,1 onB1,0 offB2; zeta_R(x)=zeta(x/R), ALLR>0. Let
E=E_(1/2)=H^(1/2)xH^(-1/2), inner product linear in first variable,
Jz(xi)=(<xi>^(1/2)hat z1,<xi>^(-1/2)hat z2), a unitary onto L2(C^2).
S(t) full massless wave, B(b)(u,v)=(0,bu). The sine quotient is continuous
at zero. All I=[s,s+h] subset[0,T], T>0,0<h<=1. Phase tests Schwartz.

D1 ACTUAL form without an observation cutoff:
 v_z(t)=[S(t)z]_1,
 G_w(t)=-sin(t|D|)/|D| [Lambda w1]+cos(t|D|)[Lambda^-1 w2],
 F_z,w(t,x)=1_I(t) v_z(t,x) overline(G_w(t,x)),
 ell_R(I;z,w)=W_C(zeta_R F_z,w).
Prove admission in SAME-W test completion, sesquilinearity and exact
potential pairing
 <S(-t)B(b(t))S(t)z,w>_E=int b(t,x)v_z(t,x)overline(G_w(t,x))dx.
For smooth sources this is the first linear response paired with z,w;
NO sourcecutoff convergence claimed. No observation chi in ell_R itself.
For an optional real compact smooth chi, the OLD accepted localized form
is ell_chi(z,w)=ell_R(z,Dchi^*E w); do not set chi=1 in a theorem requiring
compact chi. Dchi is generally NOT E-selfadjoint. Derive this relation
from actual Sobolev duality, not an operator realization premise.

Let r=|xi|,rho=|eta|, c_r(t)=cos(rt), b_r(t)=<r>sin(rt)/r, b_0=t.
The exact normalized instantaneous phase kernel, after removing spatial
potential coefficient and its convolution c_d, should be
 K(t;xi,eta)=(<xi><eta>)^-1/2
             [[-b_r c_rho,-b_r b_rho],[c_r c_rho,c_r b_rho]].
Check ALLentries/weights/signs/time argument, full public DimensionalMatrix
identity at r,rho>0, and continuous zero cases; no scalar-only surrogate.
With U=Jz,V=Jw, exact product Fourier reflection should give
 hat F_z,w(t,-lambda)=c_d int sum_(i,j=1,2)
 K_ij(t;eta+lambda,eta) U_j(eta)conj(V_i(eta+lambda))deta *1_I(t).
This sign/reflection matters; use evenness of the auxiliary nu_R when
reflecting its variance integral. Original masked noise is NOTstationary.

D2 TWO uniform finite-family inequalities:
Fix 0<gamma<min(1/2,(2-alpha)/2). B_alpha(h)=1 (alpha<1),
1+log(1/h) (alpha1), h^(1-alpha) (alpha>1). Seek finite C_T depending on
Gamma,zeta,a,alpha,gamma,T but NOTR,I,z,finitefamily or family size, such that
for every finite complex E-orthonormal Schwartz phase family {e_k},
 sum_k E|ell_R(I;e_k,z)|^2 <= C_T h^(2-a)B_alpha(h)||z||_(E_(1/2-gamma))^2,
 sum_k E|ell_R(I;z,e_k)|^2 <= C_T h^(2-a)B_alpha(h)||z||_(E_(1/2-gamma))^2.
Here ||z||_(E_(1/2-gamma))=||<xi>^-gamma Jz||L2. For every
1/2<beta<min(1-a/2,(3-a-alpha)/2), both RHS also <=C_T,beta h^(2beta)
||z||_(E_(1/2-gamma))^2. No HS trace or pathwise operator assertion.

Candidate route: apply accepted physical-mask auxiliary covariance bound
FIRST to each LINEAR matrix form, including complex and indicator completion.
Its positive even nu_R satisfies uniform translated-ball bound with
C=c_d^2 ||hat zeta||1^2 C_Gamma. Actual variance factor(2pi)^d times
product-Fourier c_d^2 must cancel exactly. Use Hilbert-valued finite Bessel
in input family for the first inequality and output family for the second;
handle two phase components by CS, never independence. Reverse row needs
actual evenness of nu_R and the symmetric temporal bound. Then accepted
continuous b/c temporal bound and uniform scalar row. Every analytic
interchange, pointwise test domain and finite Bessel step needs proof.
An auxiliary stochastic field is not necessary: only its positive norm
enters. The nonlinear PDE/noise is not replaced.

D3 limited actual reconstruction: by a fixed countable real Schwartz ON
basis of E, D2 should yield deterministic bounded real linear maps
 m_R,I,n_R,I:E_(1/2-gamma)->L2(Omega;E) on SAME-W with
 <m_R,I z,w>_E=ell_R(I;z,w)=<z,n_R,I w>_E inL2 for each fixed real
Schwartz pair, and bounds matching D2. Construct Gaussian limits; no common
uncountable almostsure version or random bounded operator is inferred.
These are mean-square column/adjoint-column maps, NOT L2(Omega;B(E)) or HS.

No operatornorm/Schatten/timepath/Young/sourcecutoff/allorder/canonicaldata/
newmoment/sourceconstant theorem. Original d2/3 lower/sharpupper/source
normalization/domain/label/exactlimit work remains OPEN. No newLeanmodule
or oldfiniteproof upgrade, officialcompanion/contact/Skorohod/HPC/TeX/PDF/
wiki/publicrelease/wholepaper clearance. Full independent proof gate needed
before adopting D1-D3 even if this statement gate passes.
