# Rendered-source audit:unreviewed local findings

Pinned author PDF SHA2565f7385ca451e643a1f3ff31835e4ee52b2708b5d2e3652eec3fb5d3958b97b6c.
All eight direct-PDF windows of printed25--28were opened;these are printed
formulas,not merely extraction errors. Algebra-screen.py retains exact controls.
These are intermediate proof-line issues,NOT a refutation of Theorem4.1.
Every proposed repair/reconstruction still needs independent review.

- p25,second-chain tail coefficient:printed lower index n+l is beyond2n
  for every n+1<=l<=2n. The telescoping coefficient is sum_(j=l)^(2n)lambda_j.
  Expanding sum_l c_l*(t_l-t_predecessor) proves the identity;the second chain
  has its own zero root. Five exact small-ncontrols fail the printed identity
  and satisfy the corrected one.
- p26,consecutive Gaussian-characteristic equalities:the spatial heat
  multiplier loses its factor1/2. Fourier convolution gamma_(eps_j+eps_k)
  supplies exp[-(eps_j+eps_k)|xi|^2/2],and the Brownian characteristic
  expectation supplies exp[-Var/2];the former stays unchanged. Both choices
  retain monotonicity and the same zero-width limit,but not finite-width
  equality. No source PDF is changed.
- p27,horizon identity:the displayed integral times theta1theta2 equals
  4/(theta1theta2),not1. The prefactor making it1is theta1^2 theta2^2/4.
  This is a finite positive correction at each fixed pair of parameters.
- p28,occupation powers:mutual Cauchy--Schwarz gives A12<=sqrt(S1S2).
  If counts a,b,c satisfy a+b+c=n,the product is bounded by
  S1^(a+c/2) S2^(b+c/2),not automatically S1^n S2^n. Scalar S1=S2=A12=1/4
  satisfies the Cauchy premise and violates the latter implication.
  The safe bound (1+S1)^n(1+S2)^n holds for all nonnegative inputs;165exact
  count/value controls pass. This is an algebraic proof-line countercheck,
  not a newly reviewed stochastic theorem or a moment no-go.

The intended finite-nfiniteness argument appears repairable. Rather than
relying on these literal Chapter4equalities,the bounded plan uses positive
Laplace transforms of time INCREMENTS,elementary Brownian heat bounds,and
homogeneity to prove the construction in the original class. It does not
adopt any intended correction of the source's variational constants.
