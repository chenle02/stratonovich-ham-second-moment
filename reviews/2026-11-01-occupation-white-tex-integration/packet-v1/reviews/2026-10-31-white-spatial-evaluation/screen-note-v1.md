# Frozen white CDF profile checks and proposed bound evaluations

Target frozen before new diagnostics. Four deterministic normalized profiles
were integrated at40/70working digits: two sech and two Gaussian profiles,
with distinct widths/shifts. For each, the script independently integrates
mass, fourth power, derivative square, CDF mixed term and CDF square term,
then the full squared expression at z0,+width,-width. It also checks the
pointwise CDF derivative at three points and the minimized z=3A square.
Twelve square rows per precision are deterministic checks, not samples.

All per-profile quantities, square rows, precision-specific maxima and tied
cases are retained before formatting. Square-expansion maximum residuals
are1.83671e-40 (Gaussian width2,z-2) and2.03753e-71 (same profile,z2).
Several residuals are recorded0.0 at working precision, not exactness or
certified integration accuracy. Cross-precision A,b differences use85digits.
Both signed roundoff slacks and nonnegative direct square integrals are
retained; no negative slack is clipped to make a numerical inequality pass.

The wrong cross-sign expansion and wrong1/4 coefficient are detected for
nonzero z. At z0 they are blind, which is why those rows are calibration
only. Exact wrong-sharpness controls are the soliton's A=b=1/3 refuting
4A²<=b and its c1,width1 energy1/6 refuting a ceiling1/12. These need
analytic justification and independent review; no all-H1 proof follows
from profile checks. The full endpoint/chain-rule argument remains open.

The script also evaluates the PROPOSED white moment bounds for a1/4,1/2,
3/4 and covariance mass c1,4. These are formula evaluations conditional on
the WS1 spatial evaluation and application gate; the all-model OC bracket
itself has now passed its full gate. They are not exact values of C2,
PDE simulations, probability confidence intervals or global optimizations.

At unit spatial-white covariance and raw temporal kernel |s-t|^-1/2,
the proposed endpoints are approximately1.0795179077 and1.1211952203.
Their exact proposed formulas are(2/3)sqrt(1/M_(1/2)) and
(2/3)sqrt(K0(1/2)); the ratio is about1.038607338. Decimal values are
approximations, not certified decimal enclosures. c4 endpoints are twice
c1 endpoints, exercising covariance-mass versus noise-amplitude conventions.
No Chen constant is inserted, fitted or used to choose these values.

mpmath version/source SHA retained, script exit0. No new Lean theorem or
H1/CDF/model statement is certified by this screen. No old test was rerun.
