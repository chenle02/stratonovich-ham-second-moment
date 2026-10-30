# Raw test-profile variational dilation: exact proposed statement

PROPOSED, unproved/unreviewed. Standard spatial dilation applied to the
accepted actual Stratonovich lower functional; no standalone novelty or
sharp source-constant theorem is claimed. Original full goal stays active.

## Actual class and imported inputs

Fix original d1 positive Riesz/white Gamma with amplitude,0<a<1,
0<alpha<=1,alpha+a<2. Let C_sep contain psi(t,x)=f(t)q(x), where
EACH of f and q is nonzero, nonnegative and smooth compact, supp f
contained in(0,1), q on R. For each fixed psi use exact raw covariance
objects of accepted notes/actual-shifted-event.md:

 k_f(t)=int_0^1 |t-u|^-a f(u)du, U_q=Gamma*q,
 H_(b,q)=-d2-bU_q, lambda_(b,q)>0 the actual ground rate,
 I_psi=int_0^1 lambda_(k_f(t),q)dt, v_psi=E W(psi)^2.

All chosen compact families K_par and their constants are selected for
each fixed f,q BEFORE the time limit, as in the accepted theorem.
No uniformity over moving test/scales is assumed. If psi has multiple
positive separable factorizations, prove I_psi is well-defined via the
operator potential h_psi(t,x)=k_f(t)U_q(x), which depends only on psi.
The dilation is intrinsically psi_s(t,x)=s^(3-alpha)psi(t,sx).
Accepted input:

 Q2:=liminf_(t->infinity)t^-kappa log E|u(t,0)|^2
    >=2I_psi-v_psi/2 for EACH fixed psi,
 kappa=(4-alpha-a)/(3-alpha),

with the ORIGINAL point solution and covariance unchanged. Also import
the already accepted finite limsup upper rate from canonical T:full-upper
in the exact statement excerpt in this packet, not a source first-mean
constant. This supplies a common finite upper bound for all raw scores
at coefficient2, not a uniform event estimate across psi.

## Proposed deductions

1. Fixed s>0 dilation is q_s(x)=s^(3-alpha)q(s x),
   psi_s=f tensor q_s. Prove the class map is bijective with inverse
   scale1/s and composition of scales by multiplication. Prove exact
   distributional/measure covariance and L2-unitary spectral identities:

   U_(q_s)(x)=s^2 U_q(sx),
   lambda_(b,q_s)=s lambda_(b,q),
   I_(psi_s)=s I_psi, v_(psi_s)=s^(4-alpha)v_psi.

   Keep white Radon endpoint and actual amplitude. The unitary dilation
   on L2 is g(x)->sqrt(s)g(sx); its kinetic factor is s^2.
   No Fourier-density convention or compact Riesz potential is assumed.
2. For EACH scalar c>0 define AUXILIARY variational score supremum

   V_c=sup_(psi in C_sep)[c I_psi-v_psi/2].

   Establish well-defined finite REAL values and V_1>0, using the actual
   lower and full upper inputs at c2 plus positive fixed tests/dilation,
   without assuming an optimizer or a desired sharp constant. Prove

   V_c=c^((4-alpha)/(3-alpha))*V_1.

   In particular V_2=2^((4-alpha)/(3-alpha))*V_1>2V_1 and Q2>=V_2.
   c is a VARIATIONAL LABEL, not a theorem about arbitrary moments.
   V_1 is NOT identified with the first-mean growth rate, L_*, E or E_star.
   The strict comparison V2>2V1 is NOT improvement over actual Jensen.
3. State all source/class boundaries: no nonseparable optimizer transfer,
   no source normalization correction, no full sharp upper bound, no
   original higher-dimensional closure. Each s,c is fixed before the
   original time limit; no s=s(delta) substitution or uniform event claims.

## Source and novelty crosswalk

Local wiki search/cite and synthesis reads are recorded in local-recon.md.
They are recon, not imported theorem or novelty clearance. Primary original
variance homogeneity comes from the project's standing H:homog; spectral
scaling must be proved directly by unitary conjugation of the accepted
self-adjoint operators on H2. Class/supremum transformations and positivity
must be written completely, not just a guessed p-power calculation.

Pinned author PDF p4(1.11)-(1.13) has source E with raw kernel/gradient
penalty1 and E_star with damped kernel/penalty1/2. Accepted retained source
audit establishes a literal normalization discrepancy at an admissible
point; intended correction UNKNOWN. V_c stays DISTINCT from both. The
static Chen-Hu wiki page also flags a published white-constant mismatch;
no numerical static/source value is imported. No novelty/publication claim.
