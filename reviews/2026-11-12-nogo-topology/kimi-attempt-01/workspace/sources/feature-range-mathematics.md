## Exact counterexample in the actual feature space

Fix any t0>0, finiteLambda=eta^(-1)>0,epsilon>0,x, and nonzero original admissibleGamma. Letnu_a(dlambda)=lambda^(a−1)dlambda/Gamma_E(a). Letg=p_epsilon(x−·) inH_Gamma. It is nonzero, since||g||²=Gamma_(2epsilon)(0)=∫p_(2epsilon)(y)Gamma(dy)>0; finiteness follows from temperedness and Gaussian decay. This includes legal d1white and legal singular Radon examples.

Choose disjoint compact intervalsA inside(0,Lambda) andB inside(Lambda,infinity), both away from0. Choose nonnegative nonzero real smooth bumpsu_A,u_B supported inside them, and set

    p(lambda)=u_A(lambda)/(∫u_A dnu_a)
                −u_B(lambda)/(∫u_B dnu_a).

Then∫p dnu_a=0, but∫_(lambda≤Lambda)p dnu_a=1. Both normalizers are finite and strictly positive. Choose realphi inCc∞((0,infinity)) withphi(t0)=1. In the actual G=L2((0,infinity)_lambda×R_r,nu_a dr;H_Gamma), define

    q(lambda,r)=p(lambda)[phi′(r)+lambda phi(r)]/sqrt(2lambda) tensor g.

This is a legitimate G vector: its lambda andr supports are compact, lambda is bounded above and away from0, andg has finite norm. More explicitly, integration ofphi′phi gives0 and

    ||q||²=||g||²/2 · [||phi′||2² ∫p²/lambda dnu_a
                              +||phi||2² ∫lambda p² dnu_a] < infinity.

No generalized raw point noise or negative-time original noise is used. The auxiliaryr coordinate still ranges over the FULL real line exactly as in097.

For any smooth compact raw tensorF, the actual map is

    PhiF(lambda,r)=sqrt(2lambda)∫_(t>0,t≥r)
                                      exp(−lambda(t−r))F_t dt.

All exchanges below are absolutely integrable: q has compact support away fromlambda0 and compactr support; F is compact in positive time with bounded spatial H_Gamma norm; forr≤t the exponential is at most1. The PLUS sign inq is essential, because

    d/dr [exp(−lambda(t−r))phi(r)]
       = exp(−lambda(t−r))[phi′(r)+lambda phi(r)].

The inner integral from−infinity tot is thereforephi(t). Thus

    <PhiF,q>_G
       = [∫_(t>0)<F_t,g>_H_Gamma phi(t)dt] · ∫p dnu_a =0.

Finite smooth tensors are dense inH_W, Phi is an isometry with CLOSED range, and pairing withq is continuous. Consequentlyq is orthogonal to the entire closedPhi(H_W), not merely to a finite test class.

The actual positive-cutoff point feature is

    v(lambda,r)=1_(lambda≤Lambda) sqrt(2lambda)
                 exp(−lambda(t0−r))1_(r≤t0) tensor g.

The SAME inner integral now gives

    <v,q>_G = phi(t0)||g||² ∫_(lambda≤Lambda)p dnu_a
              = ||g||² >0.

Hencev does NOT belong to closedPhi(H_W). This disproves the range inclusion. A concrete legal specialization is d1,alpha1,a1/2,Gamma=delta0,t0=1,Lambda1, withA inside(1/4,1/2) andB inside(2,3). The argument actually works for every nonzero admissibleGamma at each positive finite cutoff andt0>0. ZeroGamma is the separate trivial zero feature and is not a counterexample.

## What this proves about the actual fixed extension

LetP be the orthogonal projection ontoPhi(H_W). The draft defines ONE isonormal extension

    I(v)=W(Phi^(-1)Pv)+J((I−P)v),

withJ independent of the originalW. Sinceq is in the orthogonal complement and<v,q>≠0, (I−P)v≠0. Therefore

    Var(Y_rho(t0,x) | sigma(W))=||(I−P)v||²
                       ≥ |<v,q>|²/||q||² >0.

So the actual positive-cutoff point source is NOT sigma(W)-measurable: it has a nontrivial independentJ component. It is not merely that W-only measurability has not been proved. The claimed range inclusion and the claimed positive-cutoff W-only consequence are false. The source explicitly says cutoff fields may useJ and makes no W-only assertion.

This finite-cutoff counterexample does NOT settle the SEPARATE question whether a particular nonlinear/canonical LIMIT is sigma(W)-measurable by another argument. For example, source/residual raw-test convergence can remove auxiliary components in a limit. The report’s stated reasoning about that limit is invalid, but this counterexample alone is not a proof that every nonlinear limit has a nontrivialJ component. No stronger negative theorem is asserted.

