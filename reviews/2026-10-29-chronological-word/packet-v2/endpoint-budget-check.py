"""Finite falsification of the proposed one-ending metric budget, not proof."""
from fractions import Fraction as F
from itertools import combinations_with_replacement, product
from pathlib import Path
import json
import math

T = F(4)
points = list(map(F, [-1, 0, 1, 2, 3, 4, 5]))
intervals = [(a, b) for a in points for b in points if a < b and a < T and b > 0]
insertions = [F(1, 2), F(3, 2), F(5, 2), F(7, 2)]
tested = 0
worst = F(0)
simultaneous = clipped = 0


def budget(family, weights, base, split):
    grid = {F(0), T}
    for a, b in family:
        grid.update((max(F(0), a), min(T, b)))
    grid.update(split)
    grid = sorted(grid)
    heights = []
    for left, right in zip(grid, grid[1:]):
        mid = (left + right) / 2
        heights.append(base + sum(w for (a, b), w in zip(family, weights) if a < mid < b))
    # Initial change base -> first height contracts; final return is charged.
    actual = F(1)
    old = base
    for new in heights + [base]:
        actual *= max(F(1), old / new)
        old = new
    return actual, len(heights)


for size in range(1, 4):
    for family in combinations_with_replacement(intervals, size):
        for weights in product([F(1), F(2)], repeat=size):
            for base in [F(1, 2), F(1), F(2)]:
                actual, pieces = budget(family, weights, base, [])
                refined, refined_pieces = budget(family, weights, base, insertions)
                charged = math.prod(1 + w / base for w in weights)
                assert actual == refined, (family, weights, base)
                assert actual <= charged, (family, weights, base, actual, charged)
                assert pieces <= 2 * size + 1
                assert refined_pieces <= 2 * size + len(insertions) + 1
                worst = max(worst, actual / charged)
                endpoints = [max(F(0), a) for a, _ in family] + [min(T, b) for _, b in family]
                simultaneous += len(set(endpoints)) < len(endpoints)
                clipped += any(a < 0 or b > T for a, b in family)
                tested += 1

out = {
    "status": "PASS",
    "scope": "Finite exact-rational endpoint/identity norm budget only; not a propagator, coefficient, factorial or theorem certificate",
    "schedules_tested": tested,
    "background_colors": "1 through 3",
    "interval_endpoints": "-1,0,1,2,3,4,5; active window [0,4]",
    "weights": [1, 2],
    "base_weights": ["1/2", "1", "2"],
    "cross_partition_cuts": [str(t) for t in insertions],
    "simultaneous_endpoint_cases": simultaneous,
    "clipped_interval_cases": clipped,
    "largest_actual_over_charged": str(worst),
    "insertion_cuts_add_no_metric_cost": True,
    "no_mathematical_claim_adopted": True,
}
Path(__file__).with_suffix(".json").write_text(json.dumps(out, indent=2) + "\n")
print(json.dumps(out, indent=2))
