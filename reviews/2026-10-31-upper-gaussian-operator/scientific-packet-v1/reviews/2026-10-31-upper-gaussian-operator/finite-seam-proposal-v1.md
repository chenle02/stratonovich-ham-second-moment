# Proposed finite tail seam, before proof

FROZEN PLANNED STATEMENT, not a Lean theorem yet. Worthwhile scalar boundary
for the actual finite-head Gaussian tail, not a new analytic foundation.
Search/reuse existing JointTilt/FiniteYoung/Mathlib first. No official package
or companion/registry/lease/HPC action; local standalone checks authorized.

For REAL M,x,C,nu with
 0<M, M<=x, 0<=C, 1<nu<2, 4C<=M^(2-nu),
propose the single public finite conclusion
 C x^nu-x²/2 <= -M²/8-x²/8.
The proof must derive absorption C x^nu<=x²/4 from those hypotheses, not
assume it. Model application: C=C1 B^(3nu), M=M_B, x=||Phi_delta,J|| on
the tail. Cutoff condition and Gaussian/measure/limit applications remain
ANALYTIC inputs. No Gaussian probability, H-valued field or SPDE statement
would be certified by this finite inequality.

Existing Mathlib source names inspected read-only at the previous pinned
4.35.0 cache: Real.rpow_le_rpow, Real.rpow_add, Real.rpow_natCast. Exact
public types and guard use must be checked during the local build; no
proof/compile/adoption/count increase before the statement gate.
Old JointTilt four facts remain unchanged and do not prove this general-real
cutoff. Their half-cost/sign diagnostics may be reused at their exact scope.
