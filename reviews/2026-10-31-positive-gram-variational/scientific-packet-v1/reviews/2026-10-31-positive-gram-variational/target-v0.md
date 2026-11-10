# PG1-PG2 finite occupation-score target, BEFORE screen

UNREVIEWED independent finite-dimensional proposal. No proof or actual
SPDE/signed-positive/sourceconstant application. Screen while UR native
statementattempt58076 remains live; this supplies NO premise to UR.
Original fullallmodel goal unchanged.

Let H be a real Hilbert space,finite labels k_i,positive weights ell_i>0,
kinetic costs b_i>=0 and Gram C_ij=<k_i,k_j>. Assume C entrywise>=0
(and necessarily PSD). Discard zero labels: their positive-part terms0.
For each nonempty subset A of remaining nonzero labels define
 D_A(w)=sum_(i inA)ell_i^2/w_i-sum_(i inA)b_i w_i
                   +(1/2)sum_(i,j inA)w_i C_ij w_j, w_i>0.
The empty subset's value is0. Proposed PG1 is
 sup_(Phi inH)[2sum_i ell_i sqrt((<Phi,k_i>-b_i)_+)-||Phi||^2/2]
                    =max_(A includingempty) inf_(w>0)D_A(w).
No covariance inverse; singular Grams permitted. For nonzero diagonals and
entrywisepositive C,the proposed finitedualminimum is attained at positive
w; a fullscoremaximizer may be chosen as Phi=sum_(i inA)w_i k_i,or0.
Negative individualactive-branch values are permitted; fullscore>=0.

Proposed PG2: for ANYtwo nonnegativePSD Gram matrices C,D with C<=D
ENTRYWISE,same b/ell,optimizedfullscore forC <= thatforD,even if D-C is
not PSD. This concerns optimized deterministic scores,not arbitraryphase
covariance monotonicity. Zero labels handled via discard beforeactive dual.

Test small scalar/fullrank/rankdeficient/zero-label cases. Independently
compare direct nonconcave primal optimization in raw Phi coordinates with
active-subset convex-dual optimization; test global-search truncation and
percase gradient/precision errors. Include explicit wrong full-active-only
formula,wrong halfaction and omittedempty-subset negativecontrols. No
numericalagreement is a proof or certifiedglobaloptimum/enclosure.

Future physics is ONLY a possible consumer: labels may be timecell raw
occupation m_R f_i^2 with nonnegative Gamma/timekernel,comparing masked
and unmasked Gram entries. ActualH_I membership,time/Rayleigh approximation,
positivecontrol lower-class fit,kinetic constants,measurability/density/
coercivity and intendedauthor dictionary all need OWN proofs/gates. No
p1auxiliaryidentity/Skorohod/contact/HPC/companion/sourcefix/TeX/PDF/wiki/
bib/publication. No newLean/compiler/count. Freeze beforetests.
