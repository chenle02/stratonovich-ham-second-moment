# Actual SAME-W operator driver from smooth test-noise projections

UNREVIEWED statements before long proof. Original all-dimensional sharp/
source objective retained. Canonical originalGamma/H:homog,d1/2/3,
a=alpha_0 in(0,1),alpha+a<2,0<alpha<d oralpha=d=1. Gamma nonzero; SAME
realW, no newprobabilityspace/other-law substitute. E=E_s,s=1/2,
J0(u,v)=(Lambda^1/2u,Lambda^-1/2v), physicalL2^2 coordinates. S(t) full
MASSLESS wave, B(h)(u,v)=(0,hu), continuouszero sinc. Physicalnoise mask
zeta_R(x)=zeta(x/R),real even nonnegative C_c^infinity base1onB1,0offB2.
R>0,T>0 fixed. AllI=[s0,s0+h] subset[0,T],0<h<=1. For intervals longer
than1, define rawell by additive partition and actualtestcompletion, not
an unproved uniform-long-h estimate. Prior ell_R is NO observationcutoff.

M1. ActualrawnoiseHilbert H_W is the nullquotient completion of REAL
C_c^infinity((0,infinity)xRd) under the modelcovariance. Prove separability
and a countable infinite ONbasis with representatives f_j in that SAMEtest
space; no injectivity of tests (invariantdirections allow nulltests). Let
g_j=W(f_j), real independentstandardGaussians. Need actualnonzero/infinite
regime: spatialtest q with int q(Gamma*q)>0 plus strict timeRiesz form on
nonzero compacttau gives infinite dimension. GramSchmidt of countabletest
dense set preserves compact smooth representatives; zero residuals discarded.

M2. Define ACTUAL deterministic CM coefficient
 H_j,R(t,x)=zeta_R(x)int_(u>0) |t-u|^-a int Gamma(dy) f_j(u,x-y)du.
Prove real C_infinity on every finite time/spacecompact and supported inB2R;
all derivativebounds finite for fixedj,R,T, no uniformj bound assumed.
Move time derivatives onto zero-extended smoothtest, NOT onto the singular
kernel. This zeroextension is deterministic, no negative-time W introduced.
Mask is AFTER covarianceconvolution, notGamma*(zeta_R f_j). Nullrepresentative
changes must not change the resulting operator covariance coefficients.
Define A_j(I)=int_I S(-t)B(H_j,R(t))S(t)dt strongly onstates. For EVERYrealr,
A_j:E_r->E_(r+1) bounded, with primitive A_j(0,t) Lipschitz in the appropriate
operatornorm on finiteT. The adjoint relativeE_s also gains one order on
the corresponding Sobolevscale by actualduality. No operatornorm continuity
of S(t) assumed. For real compact chi=1 onB_(2R+T+1), prove BOTH physical
localizations Dchi A_j=A_j=A_j Dchi, including displacementANDvelocity.
Prove SAME-W identity E[g_j ell_R(I;z,w)]=<A_j(I)z,w>_E for eachfixed
Schwartzpair (complex extension ifused), by actual covariance/Fubini/
Sobolevadjoint. No noise-operator realization premise.

M3. For finite N define X_N(I)=sum_(j<=N)g_j A_j(I), bona-fide finite bounded
operators, primitives X_N(t) from0t Lipschitz paths. Matrixforms are EXACT
orthogonal Gaussian projection of rawell onto g_1,...,g_N. They are TEST-BASIS
truncations, NOT claimed canonical epsilon/delta source mollifiers.
Using acceptedactualtwo-variance finitefamily bounds, prove in J0coordinates
 Vout_N=sum_(j<=N)a_j a_j* <=C_T h^(2-a)B_alpha(h)D_gamma^2,
 Vin_N =sum_(j<=N)a_j* a_j <=C_T h^(2-a)B_alpha(h)D_gamma^2,
wherea_j=J0A_jJ0^-1,D_gamma=diagLambda^-gamma,
0<gamma<min(1/2,(2-alpha)/2), B_alpha=1/log/power as in acceptedscalar note.
C_T uniformN,R,I (source/maskshape/modelfixed), not a sum of individualj norms.
Both variance directions separately, real-to-complex norm conventions checked.

M4. The accepted SAME-W mean-squarecolumn maps satisfy for EVERYfixed
z,w inE_(s-gamma) the actualGaussian expansions
 m_R,I(z)=sum_j g_j A_j(I)z,
 n_R,I(w)=sum_j g_j A_j(I)^*E w inL2(Omega;E).
Prove first-chaos membership from their actualmatrixforms, not merely from
being Gaussian. Extend A_j and its E-adjoint to these rough inputs by gain1
and density, gamma<1. Hence actualpositive variance strongsums Vout_infty,
Vin_infty exist boundedly; their positive tails T_out,>N,T_in,>N tend strongly
to0 and keep the SAMEweightedbound and BOTH localization identities. No
operatorpath/sampleboundedness inferred from columns alone.

M5. MATCH these ACTUALfinitefamilies to accepted compact-cutoff Props2-3/
Cor4, with Pchi=J0DchiJ0^-1, Kchi=PchiD_gamma. For evenp>=2,pgamma>d,
 (E||X_N(I)||_Sp(E)^p)^(1/p)
 <=sqrt(p-1) sqrt(C_T) h^(1-a/2)B_alpha(h)^1/2 ||Kchi||_Sp.
Equivalent strictbeta bound for1/2<beta<min(1-a/2,(3-a-alpha)/2).
R-dependence of compactnorm allowed; no uniformR pathmoment claim.
For fixed evenp0 withp0gamma>d, monotonicity of unnormalized singular-value
norms should allow||Kchi||_Sp<=||Kchi||_Sp0 forp>=p0, preserving sqrt(p).
Allhypotheses (gain/localization/two variances/Gaussianlaw) derived, notassumed.

M6. Prove actual compact-tail convergence, not just uniformmoments.
T_out,>N<=C h^(2-a)B_alpha B_out, T_in,>N<=same*B_in with compact positive
S_(p/2) envelopes from acceptedcutoff. A NEW compact-domination lemma toprove:
0<=T_N<=B compactpositive inS_m,m>=1,T_N->0 weakly implies
||T_N||op->0 andTr T_N^m->0. Candidateproof: finite-spectralprojection ofB,
positivequadratic CS to bound high/offblocks, then eigenvalueminmax and
scalar dominatedsummation. Do NOT infer A^m<=B^m. Counterexample without
compactB: rankone translatedstate projections weakto0,norm1,dominatedbyI.
Retain actualtailtracepowers in the finite-MATRIX compression/Fatou argument
to obtain LpSpnorm Cauchy of finiteGaussian tails, hence Lp(B(E)) Cauchy.
Construct SAME-W limit X_R(I) in a separable closed subspace ofB(E), allfinite
p>=1 by larger evenmoments, compact samples, fixed-I Spnormmoments and
rawmatrix compatibility. Avoid assuming an infiniteGaussianseries theorem
or Banach martingale convergence. No Sp-Bochner path claim required.

M7. Actual operator path: for every1/2<theta<beta<min(1-a/2,(3-a-alpha)/2),
X_N(t) converges in Lp(Omega;C^theta([0,T];B(E))) for EVERYfinitep>=1 to a
centeredGaussian SAME-W path M_R, M_R(0)=0, compactoperator values. Eachfixed
matrixpair/time is a version of rawell_R((0,t);z,w); basisindependent through
countabledensepairs/rationaltimes and continuity. Show actualtime convergence,
not onlypointwise. Candidateproof: high evenq withqgamma>d and
q(beta-theta')>1 forsome theta<theta'<beta gives uniformdyadic Ctheta' bounds;
pointwiseLpCauchy+finitegrid =>supnormCauchy, deterministicinterpolation =>
CthetaCauchy. Paths take values in closure of countablymany deterministic
A_j(0,.) paths, resolving Bochnermeasurability even though ambientHolder/
operator space can be nonseparable. FiniteT>1 handled by finiteunitpartition.
No independent timeincrements or adapted finitebasis projections assumed.

M8. For fixedR,T,theta and modelparameters prove pathnormGaussian growth
 (E||M_R||_Ctheta(B(E))^p)^(1/p)<=C sqrt(p), allp>=1,
and Eexp(c||M_R||_Ctheta^2)<infinity forsomec>0. Track dyadicsum constant
uniformhighq by fixedq0 margin and||Kchi||_Sq<=||Kchi||_Sq0; prove exponential
bound from evenmoment series (no unverified Fernique input). This is a
LOCALmasked firstdriver norm, NOT a stochastic solution moment/asymptotic.

Boundary controls: nullrawtests allowed; nonzero basisdirections may have
zero maskedCMmean. Missing maskafterconvolution is falsified in actuald2
Gamma=delta_x1 tensorLeb_x2,alpha1,a<1. Uniform mean-squarecolumns alone
don't give sampleboundedoperator: independentGaussian diagonal along
translatedcompactstates hasvariance<=I but sup|g_j|=infinitya.s.; it lacks
compact localization/envelope. No suchno-go for the actualmaskedmodel.

No canonical epsilon/delta SOURCE convergence, timeboundary-filter claim,
allorder/Youngflow/canonicalinitialdata/growingcone/newmoment/source-energy/
sharpupper/exactlimit theorem. Initialconstant(1,0) is in no globalE; no
point-evaluation or replacementmodel inferred. Original full all-dimensional
sharp/source goal ACTIVE. No newLeanupgrade/companion/contact/Skorohod/HPC/
TeX/PDF/wiki/publicrelease/wholepaper clearance. Full independent analytic/
source/application gate required after this statement audit before adoption.
