# Scalar-shape obstruction: not an SPDE counterexample

This screens the attempted deduction of the FULL sharp p2/mean ratio from
positive coefficients,Holder/log-convexity,static continuity and Jensen ALONE.
It does not refute the model conjecture or the new static-limit result.

Set nu=2,kappa_st=3/2,a in[0,log2],x=exp(a),and
F1(z,a)=sum (x^2*z)^k/(k!)^2,
F2(z,a)=sum (8*x*z)^k/(k!)^2.
These series are finite for allz>=0 by the ell2series bound. Each coefficient
is log-affine ina,so all coefficient Holder and growth-type interpolation
inequalities hold with equality. Their normalized types are
Lambda1(a)=2*x and Lambda2(a)=2*sqrt(8*x).
The actual liminf equals the limsup:the upper bound is exp(2sqrt(Az));
taking the k=floor(sqrt(Az))term and using the proved elementary factorial
log bounds gives logF>=2sqrt(Az)-O(logz),for any fixedA>0.
With z=T^(3-a),these are the same kappa(a)=(3-a)/2normalizations.

Static lower comparison holds coefficientwise since x>=1.
Jensen holds for EVERY z,not just asymptotically. Its degree-kcomparison is
x^(2k)*sum_j binomial(k,j)^2 <= (8*x)^k.
Indeed sum binomial(k,j)^2 <= (sum binomial(k,j))^2=4^k,
and4*x^2<=8*x for1<=x<=2.

At a=0,Lambda1=2 and Lambda2=4sqrt2=2^kappa_st*Lambda1.
Both rates are positive,finite,log-convex and converge to these static
constants. Yet for everya>0,
Lambda2/Lambda1 = sqrt(8/x) < sqrt8 =2^kappa_st,
while it remains >=2throughout1<=x<=2.
Thus the global sharp proportionality does not follow from these scalar
properties. Additional model geometry/comparison is essential. This only
rules out that inference;the functions are not claimed to arise from the
SPDE,its Gaussian covariances or its wave kernels. No Skorohod adaptation
is proposed. No numeric white-noise rate is asserted.
