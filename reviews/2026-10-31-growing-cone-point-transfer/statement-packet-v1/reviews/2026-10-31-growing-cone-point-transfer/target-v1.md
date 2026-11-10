# GC1-GC3 growing-cone original-point upper transfer

FROZEN UNREVIEWED STATEMENTS, not proof. Previous goal turn PROGRESS:
GL1-GL3 fixedR operator upper/finite tail fact accepted180bf1a/2320fd8,
74acceptedfinitefacts20seams. Current16adb9a clean. This target addresses
an ORIGINAL-point reduction but does not supply the needed uniform growingR
operator upper or the source sharp constant. Full original goalACTIVE.

## Exact models, geometry and actual E flow

Keep ALL original nonzero H:homog Gamma/amplitudes,d=1,2,3,
0<a=alpha_0<1,0<alpha<d or alpha=d=1,alpha+a<2; zero covariance freecase
may be handled separately. Let original canonical u be data(1,0). Put
 kappa=(4-alpha-a)/(3-alpha)>1,
 0<delta<1,L_delta=1/delta,T_delta=delta^(-1/kappa),
 g_delta=delta^((1-a)/2),Gamma_delta=g_delta²Gamma.
Fix real even eta in C_c^infinity(R^d),0<=eta<=1,eta1 onB1,support inB2.
Set
 R_delta=L_delta+2,
 eta_R(x)=eta(x/R_delta), physical mask m_delta=eta_R² ONCE,
 psi_delta=eta_R, z_delta=(psi_delta,0) inE=H1/2xH-1/2,
 D=B1(0), v_d=Lebesgue volume(D)>0.
The SAME cutoff profile is initial data and mask ROOT, not a second noise
mask square. R_delta is not the shrinking physical scaleT_delta*delta.

Let W_fast(f)=W(T_(delta,0)f) be the actual fast raw noise from the existing
calibration. At fast horizonL_delta define P_delta,E^R_delta as the ACTUAL
physical E Young flow driven by g_delta times the masked FIRST E driver
A_E,R_delta(W_fast). Use accepted actual-operator/source/Young construction,
not a separately defined spectral flow. On every fixed delta the radius,
horizon and amplitude are fixed finite parameters.

The cone is
 K_delta={(t,x):0<=t<=L_delta, |x|<=1+L_delta-t}.
It lies strictly insideB_R_delta in space. Both psi_delta and m_delta equal1
on its required initial/coefficient region. BOTH displacement and physical
fast velocity are carried. No raw point Sobolev trace is used.

## GC1. Exact ordinary-source cone identity

Use one retaining slow sourceY_(epsilon,eta_cut), shared fast pullback
Y_fast(t,x)=delta^(a/2)Y_slow(delta*t,x) and amplitudeg_delta, as in accepted
raw-block Section7/8. Its fast law is canonical for Gamma_delta at heatwidth
epsilon and temporal Laplace cutoffeta_cut/delta. Noise is FIRST smoothed,
then PHYSICALLY multiplied by m_delta; never smooth a masked raw covariance.
Let u_(delta,rho)^full be the ordinary full-source solution with data(1,0),
and v_(delta,rho) the displacement of the actual E source flow with data
z_delta and coefficient m_delta*g_delta*Y_fast. Propose at FIXEDdelta,rho,

 v_(delta,rho)(L_delta,x)=u_(delta,rho)^full(L_delta,x), x inD,          (GC1a)

on the locally continuous source event, indeed throughout K_delta with
its causal cones. Source phase must be identified with the scalar mild
solution for this COMPACT smooth data, not only e0 inF. Ordinary finite
propagation/local Picard uniqueness must be proved on the cone, including
d3 Green measures/derivative initial propagator and the velocity data.
There is no common null event for all uncountable cutoff parameters.

Spatial stationarity of the unmasked source solution then proposes

 E|u_(delta,rho)^full(L_delta,0)|²
   =v_d^-1 E||v_(delta,rho)(L_delta)||L2(D)².                (GC1b)

Joint measurability/Fubini and finiteness must hold. This is average-of-
SQUARES, not square-of-average or covariance order. No positivity of the
sample source potential is required for the exact local identity.

## GC2. Actual canonical/raw limit and original point moment upper

At FIXEDdelta, accepted fixed-mask-moment-transfer Section5(11) for the
NONZERO admissible Gamma_delta gives the full-source POINT second-moment
limit. Actual E source/Young flow convergence gives the L2(Omega;L2(D))
limit of v_(delta,rho). These are different limits to be matched on the
SAME actual source law; no pointwise raw phase evaluation is inferred.
The fast heat/Laplace cutoff law and source-before-delta order must be
checked, not merely assumed from amplitudeg1 statements. Propose

 E|u_(Gamma_delta)(L_delta,0)|²
   =v_d^-1 E||pr1 P_delta,E^R_delta z_delta||L2(D)²,         (GC2a)

and, using the EXACT accepted canonical law scaling9d77f90/raw-block(26),

 E|u(T_delta,0)|²=E|u_(Gamma_delta)(L_delta,0)|²
 <=v_d^-1 ||psi_delta||H1/2² E||P_delta,E^R_delta||B(E)².    (GC2b)

The E/F restriction identity must be checked for this actual flow if used
for finite-moment existence. FixedR GL gives FINITENESS pointwise for each
delta,R_delta, not an asymptotic bound alongR_delta. No F3 reversal or
claim that the fixedR score controls the original point moment.

## GC3. Polynomial data budget and conditional upper reduction

Let C_eta=||eta||2²+||grad eta||2². Propose

 ||psi_delta||H1/2²<=||psi_delta||H1²
   =R_delta^d||eta||2²+R_delta^(d-2)||grad eta||2²
   <=C_eta R_delta^d,
 delta log(v_d^-1 C_eta R_delta^d)->0.                     (GC3a)

All E operator second moments positive/finite at fixed delta. Since
T_delta->infinity bijects delta->0 and delta=T_delta^-kappa, propose

 limsup_(T->infinity)T^-kappa log E|u(T,0)|²
 <=limsup_(delta->0)delta log E||P_delta,E^R_delta||B(E)².   (GC3b)

This is a reduction to the UNPROVED growing-mask E-operator upper, not a
proof of its sharp constant. No uniform source-cutoff estimate in delta
is asserted: source limits are always first at fixed finite delta/R.
OwnS_R_all, sourceL^*, firstmean and positive-control scores are not equated.

## Falsification, reuse and remaining full goal

Before proof test d1free d'Alembert with GOOD growing data vs bad fixeddata,
noise-mask necessity via a smooth potential pulse outside a fixedmask but
inside the cone, heat-mask noncommutation, spatial square-of-average trap,
and actual C_eta/H1 scaling in d1/2/3. Calibrations are deterministic/source
and toy guards, not stochastic moment or uniform-operator estimates.
Reuse exact existing DirectEvent scalar scaling types; no new kernel just
for routine finite propagation or norm embedding.74facts20seams/L0 unchanged.
Local wiki/corpus/source crosswalk then independent statement and FULL gates
required. Accepted F(11)/Young/scaling inputs checked for exact use, not
recertified. No new external primary theorem or novelty claim needed here.

Original uniform growingR Gaussian/CM/operator control, signed-positive
variational optimization, intended source normalization/sharpconstant/
conditional exactlimit remainOPEN. E symplectic/uniform-regulator/IMS route
is UNREVIEWED, not input. White fixedfinite smoothprojection uniformR guard
stands. No pointtrace/rawHGaussian/independent timeblocks or heaterrors/
F3reverse/Skorohod/contact/HPC/sourcefix/companion/TeX/PDF/wiki/bib/publication
or wholegoal completion. Full original all-model objective ACTIVE.
