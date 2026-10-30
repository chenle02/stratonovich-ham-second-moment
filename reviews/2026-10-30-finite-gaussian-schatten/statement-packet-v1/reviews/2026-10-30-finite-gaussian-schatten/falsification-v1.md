# Finite Gaussian falsification controls

Twelve rows: complex scalar coefficients(1,2i); three noncommuting Hermitian
2x2 matrices; three complex rectangular3x2 matrices; p2/4/6/8. Code evaluates
the polynomial Tr((X*X)^m) with tensor Hermite quadrature orderm+1 at50-digit
working precision, standard Gaussian scaling sqrt2 and1/sqrtpi. Positive
variance powers computed directly, no MonteCarlo. p2 equality asserted,
proposed MAX-variance bound checked. The stronger AVERAGE bound in N1 is
NOT separately checked by this version of the diagnostic; requires proof.
Quadrature choice is motivated by polynomial degree; no certified accuracy
or formal quadrature exactness claim is used as proof of N1.

Two negative controls are exact analytic prescriptions from row/column
16-dimensional independent Gaussian examples; script checks integer288>144
and the correct-max upper2304. It does not integrate16 Gaussian dimensions.
Gaussian moment formulas are to be explicitly derived/used in the proof.
No actual model covariance, timepath/operator/Schattenseries or continuum
limit tested; finite matrices are not a substitute for actual driver work.
No new Lean check before the statement gate. N2 is a proposed local finite
seam; no Mathlib name/import or official package assumed.
