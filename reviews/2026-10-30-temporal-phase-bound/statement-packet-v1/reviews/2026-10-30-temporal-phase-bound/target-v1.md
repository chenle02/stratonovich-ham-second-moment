# Temporal modulation and the actual balanced-wave factors

UNREVIEWED proposed bounded statements, before long proof. a=alpha_0 in
(0,1). Use the complexified raw temporal covariance Hilbert H_a on [0,T]
from accepted spectral-mask-covariance-foundation.md Section4, whose
positivity and L2 continuity are supplied in an exact excerpt. For any
interval I=[s,s+h] contained in[0,T], 0<h<=1, indicator times a C1 function
is admitted through L2 approximation. No time derivative of its zero
extension is assumed. Let <z>=sqrt(1+|z|^2).

T1. For any complex A in C1(I), M=sup_I|A|, D=sup_I|A'|, omega real,

 ||1_I(t) A(t) exp(i omega t)||_a^2
       <=C_a h^(2-a) (M+hD)^2 <h omega>^(a-1),

with finite C_a independent of T,s,h,A,omega. Zero amplitude trivial.
Candidate: exact lag autocorrelation c(v)=int_s^(s+h-v)
A(u+v)conj A(u)du, |c|<=hM^2, |c'|<=M^2+hMD, c(h)=0;
quadratic form=2Re int_0^h v^-a exp(i omega v)c(v)dv.
Scale v=h y, split |omega|h<=1 or at y=1/(|omega|h), integrate by parts
on the nonsingular part. Every endpoint/complex sign/constant to be proved.

T2. If P_r(t) is either cos(rt) or sin(rt), and Q_rho similarly, r,rho>=0,
then for the same A,

 ||1_I A P_r Q_rho||_a^2 <= C_a h^(2-a)(M+hD)^2
       [<h(r-rho)>^(a-1)+<h(r+rho)>^(a-1)].

Finite signed-exponential expansion plus Hilbert Cauchy-Schwarz; no false
cross-frequency independence claim, coefficient and phase correlations
must be handled. C_a can be increased once to cover all three statements.

T3. Actual balanced interaction factors c_r=cos(rt),
b_r=<r>sin(rt)/r with continuous value b_0=t. For each F_r chosen from
{c_r,b_r} and G_rho from{c_rho,b_rho},

 ||1_I F_r G_rho||_a^2 <= C_a (1+T)^4 h^(2-a)
       [<h(r-rho)>^(a-1)+<h(r+rho)>^(a-1)].

For r>=1, <r>/r<=sqrt2. For 0<=r<=1,
b_r=t<r>int_0^1 cos(vrt)dv, including r=0. The low/high cases thus use
T2 with A=1,t,t^2, normalized integrals and frequencies shifted by at most2.
For h<=1, bracket comparability under shifts of size<=2 should suffice;
no division by a tiny r or deletion of a low mode. T3 is only a temporal
factor estimate: the actual normalized 2x2 interaction kernel/signs,
spatial Fourier constants and BOTH operator variances are not proved here.

The scalar frequency row is under a separate repaired STATEMENT review;
none of its conclusions is needed for T1-T3. No Gaussian operator/path/
Schatten/Young/sourcecutoff/actual moment theorem follows yet. Original
all-dimensional sharp/source goal active, no source normalization repair,
Skorohod/contact/HPC/new Lean/companion/public release/wholepaper clearance.
