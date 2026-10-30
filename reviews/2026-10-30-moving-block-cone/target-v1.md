# Actual-family moving-block cone and terminal average: target v1

PROPOSED, not proved or accepted. This is a deterministic perturbative
consumer for the original Stratonovich sharp-lower goal, not a novel cone
theorem, a stochastic event estimate or a claim of sharp constants.

## Fixed actual inputs

Use EXACT real F and physical frozen family P_b(t) from
notes/local-causal-young-flow.md Sections4-5 and the accepted notes
spectral-ground-family.md, spectral-weighted-projection.md and
spectral-complement-transfer.md. Same nonzero actual d1 Riesz/white
Gamma including amplitude, nonzero q>=0 smooth compact, U=Gamma*q,
fixed K=[b0,b1] subset(0,infinity). Constants are for this ONE family.
No global L2 requirement on constant data or Riesz U is imposed.

e_b=(p_b,lambda_b p_b), ell_b(v,w)=(<p_b,v>+<p_b,w>/lambda_b)/2,
Pi_b=e_b ell_b, ell_b(e_b)=1, normalized positive p_b. The accepted
bounds give lambda_b>=l>0, uniformly bounded e_b,ell_b,Pi_b and uniform
continuity in b, and P_b(t)Pi_b=Pi_b P_b(t)=exp(lambda_b t)Pi_b.
For some C_R>=1,eta>0 independent of b and every t>=0,

 ||exp(-lambda_b t) P_b(t)(I-Pi_b)||B(F)<=C_R exp(-eta t).

Also e0=(1,0) belongs to F and a_*=inf_b ell_b(e0)>0.
These are scoped accepted INPUTS, not assumed product growth.

Fix any real nonnegative smooth compact phi of unit integral. Define
J(z)=integral phi(x)z_1(x)dx through distributional duality. First
establish J bounded on F and j_*=inf_b J(e_b)>0 from the accepted
positive eigenfunctions and their parameter continuity.

## Target conclusion, with exact quantifiers

For EACH fixed loss 0<rho<1/2, there exist theta>0,T>=1,omega>0,
epsilon>0,c_*>0, independent of N, s and b_m, such that the following
holds for every integer N>=1. Let b_0,...,b_N in K with
|b_m-b_(m-1)|<=omega for1<=m<=N. Let D_m(t) be real bounded linear
operators on F for0<=t<=T,0<=m<=N, with

 sup_(m,t) ||D_m(t)-P_(b_m)(t)||B(F)<=epsilon.

No independence, positivity or semigroup property of D is a premise.
This is an operator perturbation lemma; physical random-block errors
will have to discharge this premise separately before stochastic use.
Set z_0=e0 and z_(m+1)=D_m(T) z_m for m=0,...,N-1. Then:

1. Entrance: z_1 lies in the cone C_(b_0)(theta), with
   ell_(b_0)(z_1)>= (a_*/2) exp(lambda_(b_0)T).
2. Every subsequent full block preserves the moving cone:
   z_(m+1) in C_(b_m)(theta) and
   ell_(b_m)(z_(m+1))
     >=exp(lambda_(b_m)T)(1-rho)ell_(b_(m-1))(z_m),
   for1<=m<=N-1.
3. For EVERY s in[0,T], the final averaged displacement obeys

 J(D_N(s) z_N) >= c_* (1-rho)^(N-1)
    exp(T sum_(m=0,...,N-1) lambda_(b_m)+s lambda_(b_N)).

Here C_b(theta)={z=a e_b+r : a=ell_b(z)>0, ell_b(r)=0,
||r||F<=theta a}. This definition tracks both phase entries.

## Noncircular parameter order and application fence

Choose the aperture using j_*, ||J||, C_R and uniform e,ell bounds.
For a residual in ker ell_b, the normalized bound

 |J(exp(-lambda_b s)P_b(s)r)| <= ||J|| C_R ||r||F

holds for ALL s>=0, with no constant growing with T. This is the
mechanism to investigate before fixing T. Choose large T for cone
contraction and entrance; only THEN choose small omega,epsilon for
parameter changes and actual operator errors. An argument that first
chooses theta from a crude exp(C T) terminal bound and then chooses T
from theta has not established existence of simultaneous choices.

After this deterministic lemma, separate obligations remain: uniform
slow variation of k(delta t), fixed-T actual random block estimates,
Riesz mask error in W1infinity, all-block high-probability event and
composition with the accepted Gaussian tilt, retained residual/cost,
original point-moment consumer and variational optimizer class.
A separable positive profile remains a lower subclass. No higher-dimensional,
source-normalization, sharp moment, novelty or whole-paper clearance.
