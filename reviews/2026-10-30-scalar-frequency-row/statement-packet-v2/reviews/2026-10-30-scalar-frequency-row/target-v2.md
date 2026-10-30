# Weighted scalar frequency row: proposed bounded target

UNREVIEWED statement, before long proof. This is a scalar measure estimate,
not an identification of a Gaussian phase-operator covariance.

Let d in {1,2,3}, a=alpha_0 with 0<a<1, 0<alpha<d or alpha=d=1, alpha+a<2. Let nu be
ANY positive Radon measure on R^d with nu(B(y,r))<=C r^alpha for ALL y,r>0.
Evenness and homogeneity of nu are unnecessary; actual auxiliary nu_R
qualify by the separately accepted covariance foundation (d967ea5). Here
ball growth is an explicit hypothesis, not an imported proof step. Let
0<gamma<min(1/2,(2-alpha)/2) and <z>=sqrt(1+|z|^2).
For 0<h<=1 put

 J_h(xi)=<xi>^(2gamma) int_Rd
    [<h(|xi|-|eta|)>^(a-1)+<h(|xi|+|eta|)>^(a-1)]
              /(<xi><eta>) nu(d(xi-eta)).

The measure notation means the pushforward eta=xi-lambda, lambda~nu;
no density, orientation or change-of-variables Jacobian is assumed.
Target: finite K=K(alpha,a,gamma) independent of d,nu,C,h,xi such that

 sup_xi J_h(xi)<=K C B_alpha(h),
 B_alpha(h)=1 if alpha<1;
 B_alpha(h)=1+log(1/h) if alpha=1;
 B_alpha(h)=h^(1-alpha) if alpha>1.

If dimensional independence turns out false it must be identified, not
silently deleted; a shell proof using only the ball bound should suffice.
Zero measure/C=0 is trivial. No lower bound on C or spectral density.
Proof candidate: q=max(1,|xi|), split |lambda|<=4q and its complement.
Near: drop oscillatory brackets (each<=1), use translated-ball growth
in eta on |eta|<=5q and inverse-Bessel shell sums, multiplied by
q^(2gamma-1). This is bounded because gamma<1/2 and 2gamma+alpha<2;
critical alpha1 has a log q absorbed by the strict negative power.
Far: both ||xi|-|eta|| and |xi|+|eta| >=|lambda|/2, denominator |eta|
comparable to |lambda|, <xi>^(2gamma-1)<=1. Centered shell sums
sum_{j>=0} 2^(j(alpha-1))<h2^j>^(a-1) give B_alpha(h), with tail summable
EXACTLY by alpha+a<2. All constants/small modes/shell endpoints need proof.

Scalar consequence only: h^(2-a) sup J_h <= K C h^(2-a)B_alpha(h).
For every beta with 1/2<beta<min(1-a/2,(3-a-alpha)/2), this is <=K_beta C
h^(2beta) for 0<h<=1. At alpha1 absorb the logarithm via the STRICT beta
inequality; do not assert the endpoint. Original threshold gives a nonempty
beta interval. This is not a Gaussian Holder/path/Young theorem.

All four phase components, E[XX*] and E[X*X], temporal modulation bounds,
masked SAME-W compatibility, source tails and localization still need
actual derivation. Scalar row alone cannot yield Gaussian operatornorm or
Schatten/path moments. Original all-dimensional lower/sharp upper/source
completion goal remains active. No PDE/noise replacement, source-energy
identification, new Lean certificate, Skorohod result/contact/HPC/companion/
public release or whole-paper clearance.
