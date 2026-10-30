# Temporal finite controls and limits

Initial72 constant/linear-amplitude local controls were expanded to120
before freezing: a .1/.5/.9, h1 or1/8, omega0/1/16/64, amplitudes1,t,t^2,
with starts0 and2 for the two polynomial amplitudes. Exact polynomial lag
autocorrelations reduce the raw two-time covariance to one integral.
The change v=h z^(1/(1-a)) removes v^-a at the origin. Forty-digit
working precision is not certified accuracy; positivity and finiteness
asserted. For constant amplitude/omega0 exact variance
2h^(2-a)/((1-a)(2-a)) is compared at rel_eps1e-35.

No numerical test of arbitrary complex C1 amplitude, negative omega,
product phase norm, small-frequency sinc or operator variance is claimed.
The product/sinc steps need analytic checks. The polynomial amplitude
controls are relevant for the proposed low-mode argument but do not verify
that argument. No all-frequency proof from120 finite examples.
No new Lean module: analytic oscillatory estimate has no worthwhile finite
seam beyond existing elementary identities; no formal coverage inferred.
