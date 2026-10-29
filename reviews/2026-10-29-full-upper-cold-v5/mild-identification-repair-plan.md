# Concrete next repair: close the Section5(ii) dependency

Status:unreviewed proof plan,not a result. Same full covariance class and
original nonsharp upper theorem. No new lower-bound or paper-polishing wave.
Actual source pp35--36,eqs(5.5)--(5.6),use a width-uniform bound on the
one-external-regularized integrals. This is the exact missing consumer.

1. Extend the already proved corrected crude calculation to n ordered
   factors with arbitrary positive vertexwise noise widths. The two-chain
   Wick formula has per-edge temporal maximum/spatial sum widths. Every
   norm bound in L:crude-corrected is uniform in those widths. With
   theta=theta0+n/t obtain q_n(t)=exp(theta0*t)*C^(n/2)*t^n/sqrt(n!).
   Show this explicitly before any partial width is sent to zero. Do not
   restore the false t-uniform source constant.
2. Finite Gaussian degree,not pure Wick order:each regularized n-term and
   its fixed-order L2 limit lie in the closed Gaussian degree<=n space.
   For a Gaussian linear coordinate W(h),multiplication on degree<=n
   has L2 norm at most (sqrt(n+1)+sqrt(n))*||h||,by normalized Hermite
   raising/lowering after choosing h/||h|| as the first coordinate.
   Closedness extends the bound to the degree-closed space. This gives
   product convergence with fixed external smoothed noise without needing
   a new hypercontractivity citation or any p=1 transfer.
3. At fixed external widths,integrate W_ext(s,y)*X_(n-1)(s,y) against the
   terminal Green measure. The multiplication bound and q_(n-1)(T)
   give Bochner/time domination. Inner regularizations converge in L2
   pointwise(s,y),with a width-uniform bound. This identifies the partial
   inner limit with the actual integral,not just an unnamed mixed limit.
4. Spatial continuity:smoothed fixed-order terms are L2-continuous by
   their continuous bounded covariance products. Joint stationarity makes
   their L2 approximation error independent of the spatial point,so the
   fixed-order limit is uniformly-in-space L2-continuous at fixed time.
   Multiplication by fixed external Gaussian noise preserves continuity
   using the finite-degree bound. For d3 this justifies weak Green-width
   convergence in L2 before outer noise removal;time domination uses mass
   t-s. Retain the source's eta-before-noise order and measurability.
5. The uniform mixed-vertex bound q_n(t) survives that inner limit,
   independently of external widths. Joint fixed-order Theorem4.1 then
   gives external-width limit X_n:use its joint Cauchy convergence and
   passage through the existing inner limit,not an unjustified exchange.
6. The sums of q_n(T) and sqrt(n+1)*q_n(T) converge. The latter proves the
   onefold regularized product integral against u equals the series of
   termwise integrals at each fixed external width;closedness of Gaussian
   multiplication and dominated Green integration identify the product.
   The former gives uniform order tails,so outer noise limit of the whole
   integral is sum_(n>=1)X_n=u-1. This proves Definition2.1's mild equation
   independently of source(5.3)/(5.4) and its Section5(ii) proof. No uniqueness.

Before promotion:source image/text proof fidelity for Definition2.1,Theorem3.1,
LemmaA.1,Theorem4.1 and Section5(ii);small finite-degree/product checks;
write self-contained proof;clean build;fresh source-bound primary/HIGH and
then fresh cold read. New source-image cohort needs native carrier calibration
before science. Never infer calibration from dimensions or reuse old24-image
coverage for newly added images. Existing calibrated images may be retained
byte-for-byte;calibrate the complete final cohort.
