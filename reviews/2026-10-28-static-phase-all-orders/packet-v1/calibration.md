# Scope, falsification and dependency map

Status: the complete Section12 is a new candidate,independent review pending.
It is an all-order REGULARIZED STATIC phase theorem and a small-block
interaction estimate for the FULL spatial covariance class of Section11.
It is not the colored-time HAM upper bound. In particular,a product of
independent successive blocks is different from overlapping/repeated fields.

Before drafting,the finite checks used noncommuting selfadjoint spatial
matrices and Gaussian creation/annihilation matrices through degree5,plus
complex two-mode wave propagators. They passed. After drafting,the exact
vacuum-cutoff assertion was additionally checked at orders1 and2:cutoffN=n
agrees numerically withN=n+2,whileN=n-1refuses by visible gaps. These are
finite diagnostics,not the proofs or Lean certification.

For the abstract complex test take A0=diag(1,R²),B_R=R^a[[0,1],[1,0]],R>=1,
0<a<1. Its sandwich norm equals
R^a/sqrt((rho²+1)(rho²+R²)). It is <=rho^{a-2} for ALLrho:
- rho<=1:the ratio after multiplication by rho^{2-a} is <=R^{a-1}<=1;
- 1<=rho<=R:it is <=R^{a-1}rho^{1-a}<=1;
- rho>=R:it is <=(R/rho)^a<=1.
Thus d=1 is a genuine hypothesis match,not just a grid of rho values.
The complex tests check the branch/weight/root comparisons at growingR,
where a real selfadjoint estimate alone would not justify Cauchy's formula.

The old Section11 scalar first-variance test remains a guard:arbitrary-phase
energy need not be monotone in covariance,and its mean second-order term
cannot be dropped. The new proof uses no such monotonicity. The small-block
corollary deliberately retains that sharper first coefficient;higher even
orders are controlled by the all-order coefficient estimate. Norm-change
losses1/(lambda h)can be tolerated there because the remainder begins at
variance order2,not1.

New imported input ONLY: Crouzeix-Palencia arXiv1702.00668v1,(3)p1 and
Theorem6pp5-6,bounded operators on a COMPLEX Hilbert space. The version is
eight pages,SHA2560e33b65b3fab07632364111290e380b0696d7ace8168c9b834028de57d943c53.
No journal theorem numbering is inferred. No unbounded-operator extension,
generic Kato square-root domain theorem,unproved real-to-complex continuation,
Nelson hypercontractivity or static asymptotic theorem is imported.
All weak-phase comparisons and cutoff limits are written in the new proof.

Dependency map:
1. Prior Lemma11.1 shifted spectral resolvent -> sandwich variance.
2. Hermite creation AND annihilation -> chaos-cutoff form bound.
3. Abstract complex lemma + explicit root integral + imported bounded
   spectral-set inequality -> uniform complex phase norm.
4. Cauchy atN=n andlambda=n/h -> factorial all-order bounds.
5. Fixed-positive-smoothing cutoff removal -> actual ordinary Gaussian
   Duhamel words,including self-pairings,not pure Wick chaoses.
6. Prior Proposition11.2's two first-variance terms + higher-order bound ->
   interaction map close to identity and summable INDIVIDUAL fine-block costs.
7. Continuous L2 extension + independence -> finite successive-block bound.
There is no identification with overlapping colored-time noise in any step.

No new source-author contact,Skorohod exact-constant development,private
Lean creation,public release or source-normalization correction occurred.
The existing normal six-repo Crouzeix-Palencia reference request is reused;
the source-specific local bibliography entry pins the preprint numbering.
