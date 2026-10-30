# Actual nonseparable positive-profile spectral bridge: target v1

PROPOSED, unproved/unreviewed. This removes an actual class restriction
on the route to the original sharp lower bound. It is not a sharp/source
constant, optimizer sufficiency or higher-dimensional result.

## Actual objects and allowed inputs

Fix d1,0<a<1,0<alpha<=1,alpha+a<2, original nonzero positive Riesz/white
Gamma including its amplitude. Fix ONE nonzero nonnegative real
psi in C_c^infinity((0,1) x R), not assumed separable. For slow parameter
sigma in[0,1] define the ACTUAL Gaussian covariance profile

 q_sigma(x)=int_0^1 |sigma-u|^-a psi(u,x)du,
 h_sigma(x)=Gamma*q_sigma(x)=Cov(W(sigma,x),W(psi)),
 q_avg(x)=int_0^1 psi(u,x)du, U_avg=Gamma*q_avg.

The covariance notation is distributional shorthand; the convolution
formula defines h_sigma, with no pointwise noise evaluation.
The symbol q_avg is the UNWEIGHTED time average, not q_(sigma=0).
sigma is an INDEX, never a multiplicative
coupling: H_sigma is NOT -d2-sigma U. Time sigma=0 is allowed, with a
nonzero attractive potential. Derive that each q_sigma is smooth compact
with one common spatial support and q_sigma>=q_avg>=0 nonzero; hence
h_sigma>=U_avg. Accepted general-psi tilt(5)-(6) supplies bounded spatial
derivatives, Lipschitz dependence into C_b^1 and uniform spatial C1 tails.
Use that exact accepted profile result, not a separable substitute.

Let H_sigma=-d2-h_sigma on real L2 (complexified for spectral statements),
P_sigma(tau) the PHYSICAL autonomous wave flow for frozen h_sigma,
evolving (v,w) by (w,v_xx+h_sigma v). tau>=0 is fast propagation time.
Use actual F of local-causal-young-flow Section4: closure of compact
smooth phases PLUS both constants in uniformly local H1/2 x H-1/2.
Initial phase e0=(1,0). No global L2 requirement on constants.

Pointwise accepted scalar inputs may be instantiated at EACH fixed
q_sigma with multiplicative coupling1 in a positive interval containing1.
All q_sigma must first be shown to satisfy their exact hypotheses.
Those results give no automatic sigma-UNIFORM constants. The new uniform
statements below are obligations, not premises or a relabelled bU theorem.
The accepted ground/weighted/complement proofs are available as blueprints
and for explicitly generic subarguments whose hypotheses are matched.

## Target deductions

S1. Derive simple negative lowest eigenvalue E1(sigma)=-lambda_sigma^2
and positive real normalized p_sigma, with 0<l<=lambda_sigma<=L finite
UNIFORMLY in sigma. Define second max-min level E2(sigma)<=0, taking
threshold0 if no second negative eigenvalue. Prove uniform positive
energy gap Delta=inf_sigma(E2-E1)>0 and rate separation from
mu_sigma=sqrt(-E2(sigma)), allowing infinitely many Riesz bound states.
The common positive profile U_avg or direct variational trial may establish
uniform negativity; use common min-max test classes and actual potential
perturbation norm to establish continuity. Uniform gap is NOT assumed.

S2. Prove some beta>0,C finite independent of sigma with

 |p_sigma(x)|+|p_sigma'(x)|+|p_sigma''(x)|<=C exp(-beta|x|).

Define continuous real local dualities on actual F (both entries) and

 e_sigma=(p_sigma,lambda_sigma p_sigma),
 ell_sigma(v,w)=(<p_sigma,v>+<p_sigma,w>/lambda_sigma)/2,
 Pi_sigma=e_sigma ell_sigma.

Prove uniformly bounded projection/dual/eigenphase norms, Pi_sigma^2=Pi_sigma,
positive constant entrance inf_sigma ell_sigma(e0)>0, and continuity of
e_sigma in F and ell_sigma/Pi_sigma in operator norm over[0,1]. Prove
forward invariance and COMMUTATION
P_sigma(tau)Pi_sigma=Pi_sigma P_sigma(tau)=exp(lambda_sigma tau)Pi_sigma.
For each fixed nonnegative smooth compact unit-mass phi, also prove
J_phi bounded on F and inf_sigma J_phi(e_sigma)>0.
Do not delete velocity, the reciprocal lambda, or the decaying partner.

S3. Derive actual uniform complementary bound for ALL sigma in[0,1],tau>=0:

 ||P_sigma(tau)(I-Pi_sigma)||B(F)
           <=C exp((lambda_sigma-eta)tau),

with0<eta<inf_sigma lambda_sigma. Must justify global fractional Sobolev
phase calculus and the genuine local F transfer with constants including
the nonlocal projection tails after growth. Per-member L2 spectral gaps
or per-member F estimates alone do NOT yield this uniform statement.
No desired complementary/product/event estimate may be a hypothesis.

## Scope, witness and later consumer

The actual white two-bump witness in falsification-v1.md rules out a
universal exact representation h_sigma=b(sigma)U. It does not prove
separable tests fail at the optimizer, nor refute any moment conjecture.
The pointwise order h_sigma>=U_avg is a deterministic positive-profile
calculation, not covariance monotonicity on arbitrary wave phases.

After S1-S3 are proved/reviewed, the moving-cone/event application must
be extended with its hypotheses checked for this actual indexed family.
Do not silently substitute sigma for the old positive coupling b. Only
then extend the actual raw lower/variational class. Source normalization
and optimizer correspondence, sharp upper constant and original higher
dimensions remain open. No novelty, Skorohod, whole-paper/circulation,
private companion, HPC or correspondence action is authorized here.
