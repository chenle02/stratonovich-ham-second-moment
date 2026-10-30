# Actual retained-residual flow: event and raw-cost lower-rate target

PROPOSED, not proved or accepted. Two linked statements for the original
Stratonovich sharp-lower consumer; not a claim of the full sharp constant.
No novel deterministic or Gaussian method is proposed.

## Exact objects and accepted inputs

Work in original d1 positive Riesz/white covariance Gamma including its
amplitude,0<a<1,0<alpha<=1,alpha+a<2. All spaces/noises are REAL.
Fix nonzero nonnegative f in C_c^infinity((0,1)), q in C_c^infinity(R),
psi(t,x)=f(t)q(x), Z=W(psi), v=E Z^2 (RAW common Gaussian variance).
Let U=Gamma*q and k(t)=integral_0^1 |t-s|^-a f(s)ds,t in[0,1].
Fix one positive compact interval K containing k([0,1]); prove its
existence from k positivity/regularity, do not assume a vanishing lower end.
Use the ACTUAL positive normalized p_b,lambda_b,e_b,ell_b,Pi_b on
F=closure of compact smooth phases PLUS constants in uniformly local
H1/2 x H-1/2, and physical P_b from the accepted spectral/moving-cone notes.
Set I_psi=integral_0^1 lambda_(k(t))dt.

Fix nonnegative smooth compact phi of integral1, M its support radius,
c>=1+M. As in accepted notes/joint-gaussian-tilt.md, for0<delta<=1 set
L=1/delta,r=c/delta,g=delta^((1-a)/2), use the SAME W^delta and Z.
Let mathcalP_delta^h(u,t) be the accepted physical Young evolution on F
for the retained potential

 g zeta_r W^delta(u,x)+zeta_r k(delta u)U(x),0<=u<=L.

Define the SIGNED real measurable average
Y_delta=integral phi(x)[mathcalP_delta^h(L,0)e0]_1(x)dx, e0=(1,0).
The square is exactly J_delta^h in accepted joint-gaussian-tilt(13).
No residual discard, independent Gaussian copy or global stationary
operator bound is allowed. All parameters/test/family fixed before delta.

Accepted inputs, scoped rather than newly proved:
- notes/local-causal-young-flow.md Sections4-7: actual F, deterministic
  base admissibility/stability and uniformly controlled ALLunit-block
  physical flows with the raw common field and r=c/delta.
- notes/joint-gaussian-tilt.md Sections3-5: raw profile C1 time/spatial
  tails, actual shifted-flow identity with exp(-Z/sqrt(delta)-v/(2delta)),
  and exact original point-moment consumer(14).
- notes/moving-block-cone.md: independently accepted actual-family
  deterministic integer-T cone/entrance/terminal theorem, UNDER its
  explicit uniform operator-error premise; discharge that premise here.

## Event target A

For EVERY epsilon>0, with the actual residual retained,

 P{Y_delta>=exp((I_psi-epsilon)/delta)} ->1 as delta down0.

Derive actual fixed-T block errors tending to0 in probability UNIFORMLY
over all O(1/delta)blocks and partial block times. Do not assume this
error control or whole-product growth as a premise of A. Required steps:
positive smooth k with uniform slow variation; C1 mask defect ->0 for
Riesz (not equality); fixed-INTEGER-T telescope of accepted unit-block
physical difference estimates; bounded deterministic freezing stability;
adjacent b_m=k(delta mT) closeness; actual composition and cone use;
Riemann sum plus per-block loss and prefactor budgets. No independence.

For L=NT+s, N=floor(L/T)>=1 for small delta, s in[0,T), the last actual
block D_N(t) is used for t<=s; extend it for s<t<=T by
D_N(t)=P_(b_N)(t-s)D_N(s). Prove this extension has small sup[0,T]error
while its value at s is the actual physical operator. Thus no estimate
for the noise beyond L is silently used. Unit-block profiles at the
last fractional unit may be defined using k(min(delta u,1)); this equals
the actual profile up to L and keeps the SAME K.

## Raw-cost moment target B

For the ORIGINAL stationary Stratonovich model and kappa=(4-alpha-a)/(3-alpha),

 liminf_(t->infinity) t^(-kappa) log E|u(t,0)|^2
       >=2 I_psi-v/2.

Use target A plus the accepted Gaussian identity and original-point
consumer, with delta=t^(-kappa) and physical spatial rescaling as already
fixed there. Intersect A's event with |Z|<=delta^(-1/4); its probability
must tend to1 without independence. Bound the MINUS Gaussian density
from below on that intersection, retain exactly v/(2delta), and show
the moderate Z penalty is o(1/delta). B is for EACH fixed positive
separable psi, not for an assumed optimizing profile. No source constant
or first-moment upper constant is an input.

## Fences and formal triage

This is an actual-field event/lower-rate application, not merely a
conditional scalar cone. Original all-dimensional/sharp/normalization
objectives remain open even after A/B for this subclass. No identification
with source E_*,E or intended L_* is asserted. General/nonseparable
optimizer approximation and sharp upper constant remain separate.
Existing accepted cone scalar budgets, Gaussian sign/cost and physical
scaling seams are reusable at unchanged scope; analytic probability,
Young/source/operator and variational inputs are NOT formalized by them.
No new foundational library, companion/package, HPC or correspondence.
