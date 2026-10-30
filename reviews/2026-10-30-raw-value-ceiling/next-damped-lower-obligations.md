# Next actual target: compare the raw lower value with the DAMPED lower input

UNREVIEWED reconnaissance/planning only, outside the running scientific
packet. No theorem/identity/lower bound below is adopted. The ceiling on
V does NOTcompare the source damped lower input against V. Original goal
still requires an actual lower comparison, sharp upper and dimensions.

A concrete possible route to freeze/falsify before proof:
1. Temporal equilibrium candidate
 f_a(t)=[t(1-t)]^((a-1)/2)/[Gamma((1-a)/2)Gamma((1+a)/2)]
 has proposed potential int|s-t|^-a f_a(t)dt=1 on[0,1] and mass
 M_a=Gamma((1+a)/2)/[Gamma(1+a)Gamma((1-a)/2)].
 Verify this actual Riesz-potential identity (source or self-contained
 Beta proof), positivity and L2(time) at0<a<1. Do not assume the formula
 from reconnaissance. Then psi(t,x)=f_a(t)phi(x) is a legal Xpositive
 control with TIME-CONSTANT meanGamma*phi and cost M_a intphiGamma*phi.
 All raw-rate/variance matching must be proved, not a roughflow theorem.

2. Define a NEW purely spatial raw energy
 E_sp= sup_{||g||2=1,g in realH1} [int g²(Gamma*g²)-||g'||2²/2].
 Derive, without staticM numericalvalues or optimizerattainment, a static
 Rayleigh/control lower bound which would give
 V_1^pos >= M_a^(-1/k) F_0(E_sp).
 SourceE_sp uses NOtemporal kernel; F0 keeps its explicitalgebraic meaning.
 The natural proof must optimize actual Gaussian-control amplitude and
 occupation spatial scale, retaining ALLsquare-root/cost factors.

3. Let K_star(u) be the ACTUAL sourcep4(1.13) damped kernel with
 d=q-2a>0. Its time row maximum is expected at1/2 by monotone Laplace
 kernel, giving R_star=2int_0^(1/2)K_star(u)du. Prove a meaningful O-domain
 dampedoccupation energy bound E_star^O<=R_star^(2/(2-alpha)) E_sp by
 spatialCS/ratio and timeSchur. No equality to all printedAd readings.

4. The sufficient scalar comparison would be
 1/M_a >= R_star exp(Delta_map(q,a)).
 If all earlier steps and this hold on the ORIGINALparameter range, they
 would imply V1>=F_a(E_star^O), hence viaacceptedrawhomogeneity/pointconsumer
 Q2>=2^m F_a(E_star^O). This would target the damped lower endpoint rather
 than the larger raw upper input ruled out for some normalizations by
 the current ceiling. It would STILLnot fix source normalization, prove
 literalbothendpoints or the sharp upper/higherdimensional goal.

Numerical gate, no proof: next-damped-lower-probe.py/json evaluates
R_star by TWO independent quadratures (sourceLaplace formula afterexact
lambda substitution and parabolic-cylinder expression), agreeing to1e-15
at35digits, on9explicitalpha/a pairs in{.1,.5,1}x{.1,.5,.9}. All9candidate
log margins log(1/Ma)-logRstar-Delta arepositive (~.01358 to1.7366).
The capacity identity itself, staticcontrol comparison, rowmaximum,
energy comparison and GLOBALscalar inequality are UNPROVED. The pcfd
representation is checked numerically against actualLaplacequadrature,
not imported as a source theorem. No grid establishes forallparameters.
Retain exactformula/domain/source checks and frozen independentstatement
review BEFOREany long proof. No newreference acquisition, source/wiki/
sibling edit, Skorohod, correspondence, companion or HPC authorized.
