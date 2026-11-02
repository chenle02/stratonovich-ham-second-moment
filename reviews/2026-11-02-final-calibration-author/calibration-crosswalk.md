# Final calibration crosswalk — author audit only

The stated intrinsic formula, common spatial-energy bracket and white example retain the four required calibrations. This is a bounded source crosswalk and a check of consequences of already-stated results; it supplies no independent reviewer vote, production theorem, source correction, endpoint-limit interchange, or completion verdict. The fresh full214 MAIN review remains separate.

Scientific source: `b4b6efccacbbccd8f747225330e9ccb27bc097a6`. The files bound in `source-bindings.json` were checked byte-for-byte against that revision and current ACTIVE source. Pinpoints below are source lines and stable labels, not rendered-page assertions.

[held back: collaborators' unpublished work]

## White bound formulas at the static endpoint

The exact source formulas are

    M_a = Γ_E((1+a)/2) / [Γ_E(1+a) Γ_E((1−a)/2)],
    K₀(a) = 2^a/(1−a),                    0<a<1.

All three Gamma arguments remain positive. Euler’s integral gives continuity near a=0 by dominated convergence: for 0≤a≤1/2 the arguments lie in[1/4,3/2], with an integrable common bound near zero and infinity. Consequently

    lim M_a = Γ_E(1/2) / [Γ_E(1)Γ_E(1/2)] = 1,
    lim K₀(a) = 1.

The Gamma identities used here are already proved in L:equilibrium-gamma-beta; Γ_E(1)=1. This limit is a check of the scalar formula, not a substitution a=0 into the positive-a Laplace-prefix construction. In particular, the limiting equilibrium density is 1/[π√(t(1−t))], which has unit mass but is not L²; no uniform L² endpoint estimate is asserted.

At α=d=1, the existing exact spatial energy E_sp=c²/6 gives

    F₀(E_sp)=√c/(3√2),
    2^(3/2)F₀(E_sp)=(2/3)√c.

The stated white bracket (E:white-moment-bounds) is

    (2/3)√(c/M_a) ≤ C₂(c,a) ≤ (2/3)√(cK₀(a)).

Both bound formulas therefore tend to (2/3)√c as a↓0, while κ(a)=(3−a)/2→3/2. Conditional only on the already-stated bracket and intrinsic-limit theorem, squeezing C₂(c,a) gives that same iterated-in-a value. This is an implication/calibration of those bounds, not a new production theorem, a fresh numerical evaluation at arbitrary a, or an interchange with the large-time limit. At c=0 the identities are zero and u=1.

## What remains open or qualified

[held back: collaborators' unpublished work]