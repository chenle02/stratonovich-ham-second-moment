# Proposed exact finite seam headers, not compiled

Standalone checks are authorized; no official private companion/package.
These two scalar deductions are proposed AFTER the independent statement
gate; no body, compiler run, kernel/count or axiom claim yet.

```lean
namespace StratonovichHAMAudit.AllAlphaMoment

theorem moment_lower (a D x y : ℝ) (ha : 0 < a) (hD : 0 < D)
    (hmean : x + y = a) (hcs : x^2 ≤ D*y/2) :
    2*a^2/(D+4*a) ≤ y

theorem rational_gap (a D : ℝ) (ha : 0 < a) (hD : 0 < D) :
    a^2/(D*(D+4*a))-a^2/(2*D*(D+2*a))
      =a^2/(2*(D+4*a)*(D+2*a)) ∧
    0 < a^2/(2*(D+4*a)*(D+2*a))

end StratonovichHAMAudit.AllAlphaMoment
```

Actual later inputs: a=temporal alpha0 in(0,1), D=q-2a>0;
x=E[u lambda], y=E[u lambda²]/D under the normalized ACTUAL positive
joint density. ANALYTIC normalization/finiteness/IBP/CS must supply hmean
and hcs before the moment lemma is applied. Derivative lower algebra
rational_gap is not a formal derivative or Gaussian integral theorem.
Reuse Mathlib squares/positive division/ring normalization/tactics;
no new probability or integration foundation. Complete separate pp.all
types/standard axioms, owned source replay and semantic negative controls
are required BEFORE any accepted new finite count/application claim.
