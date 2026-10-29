"""Exact finite Gaussian-tool checks;no HAM lower theorem or novelty claim."""
from fractions import Fraction as F
from math import factorial
from pathlib import Path
import json


def moment(n, variance=F(1)):
    if n % 2:
        return F(0)
    k = n // 2
    return F(factorial(2 * k), 2 ** k * factorial(k)) * variance ** k


def oscillator_coefficients(order, horizon):
    # Truncation of cosh(T*sqrt(Z));ordinary degree,not pure Wick chaos.
    return [horizon ** (2 * n) / factorial(2 * n) for n in range(order + 1)]


cases = []
for order in range(9):
    for horizon in [F(1, 2), F(1), F(2), F(4), F(8)]:
        coeff = oscillator_coefficients(order, horizon)
        second = sum(c * d * moment(i + j)
                     for i, c in enumerate(coeff) for j, d in enumerate(coeff))
        for variance in [F(5, 4), F(3, 2), F(7, 4), F(19, 10), F(199, 100)]:
            mean = sum(c * moment(n, variance) for n, c in enumerate(coeff))
            assert second >= 0 and mean > 0
            # Square both nonnegative sides to check the irrational prefactor
            # entirely in rationals,retaining every unequal-chain split.
            assert second ** 2 >= variance * (2 - variance) * mean ** 4
            # The normal Gaussian-square integral has positive precision
            # only for variance<2;the endpoint must not be substituted.
            precision = 2 / variance - 1
            assert precision > 0
            density_norm_squared_squared = 1 / (variance ** 2 * precision)
            assert density_norm_squared_squared == 1 / (variance * (2 - variance))
            cases.append({"order": order, "T": str(horizon), "variance": str(variance)})

assert 2 / F(2) - 1 == 0
assert 2 / F(5, 2) - 1 < 0
out = {
    "status": "PASS",
    "finite_cases": len(cases),
    "orders": "0 through8",
    "horizons": ["1/2", "1", "2", "4", "8"],
    "variances": ["5/4", "3/2", "7/4", "19/10", "199/100"],
    "candidate_factor_checked": "sqrt(a*(2-a))",
    "variance_not_amplitude": True,
    "all_unequal_chain_splits_kept": True,
    "density_precision_endpoint_2_is_zero": True,
    "scope": "Exact finite Gaussian polynomial controls and algebraic Gaussian-integral normalization only;not proof of the density integration,source representation extension,large-time asymptotics or any H:homog HAM lower bound",
    "model_specific_first_moment_bridge": "UNPROVED",
    "no_sharp_goal_claim": True,
}
Path(__file__).with_suffix(".json").write_text(json.dumps(out, indent=2) + "\n")
print(json.dumps(out, indent=2))
