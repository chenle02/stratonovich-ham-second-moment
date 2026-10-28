"""Exact parameter/discrete-Holder controls only, not a proof or Lean check."""
from fractions import Fraction as F
from itertools import product
from pathlib import Path
import json

cases = 0
zero_coordinates = 0
for a in product([F(0), F(1, 10), F(1, 4), F(2, 5), F(3, 4), F(99, 100)], repeat=2):
    s = sum(a)
    if not 0 < s < 1:
        continue
    for ratio0 in [F(1, 100), F(1, 2), F(99, 100)]:
        a0 = (1 - s) * ratio0
        for ratio_theta in [F(1, 100), F(1, 2), F(99, 100)]:
            theta = a0 + (1 - s - a0) * ratio_theta
            alpha = 1 + s
            beta = (alpha - theta) / (1 - theta)
            v = [x / (1 - theta) for x in a]
            assert a0 < theta < 2 - alpha
            assert 1 < alpha < beta < 2
            assert all(0 <= x < 1 for x in v)
            assert sum(v) + 1 == beta
            assert alpha == theta + (1 - theta) * beta
            assert 2 - s == 3 - alpha
            assert 2 - sum(v) == 3 - beta
            cases += 1
            zero_coordinates += any(x == 0 for x in a)

# The separately displayed example must actually be computed and asserted.
fixed_a, fixed_a0, fixed_theta = [F(1, 2), F(0)], F(1, 4), F(3, 8)
fixed_alpha = 1 + sum(fixed_a)
fixed_v = [x / (1 - fixed_theta) for x in fixed_a]
fixed_beta = (fixed_alpha - fixed_theta) / (1 - fixed_theta)
assert fixed_a0 < fixed_theta < 2 - fixed_alpha
assert fixed_v == [F(4, 5), F(0)] and fixed_beta == F(9, 5)

# At theta=1/2, squaring gives a purely rational Cauchy control.
mixture_cases = 0
for l1, l2, s1, s2 in product([F(0), F(1, 4), F(1), F(4)], repeat=4):
    # (sqrt(l1*s1)+sqrt(l2*s2))^2 <= (l1+l2)(s1+s2)
    # reduces to 2sqrt(l1*l2*s1*s2) <= l1*s2+l2*s1.
    rhs = l1 * s2 + l2 * s1
    assert rhs >= 0 and rhs * rhs >= 4 * l1 * l2 * s1 * s2
    mixture_cases += 1

out = {"scope": "finite exact algebra diagnostics only; no analytic, stochastic, independent-review or Lean certificate",
       "plane_parameter_cases": cases, "cases_with_zero_tangential_coordinate": zero_coordinates,
       "two_term_half_theta_mixture_controls": mixture_cases,
       "fixed_white_plane_example": {"a": list(map(str, fixed_a)), "alpha0": str(fixed_a0),
                                     "theta": str(fixed_theta), "v": list(map(str, fixed_v)),
                                     "beta": str(fixed_beta), "executed_assertion": True},
       "status": "PASS"}
Path(__file__).with_suffix(".json").write_text(json.dumps(out, indent=2) + "\n")
print(json.dumps(out, indent=2))
