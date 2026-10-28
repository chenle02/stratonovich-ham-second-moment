"""Exact interval check for the stated scalar toy; no SPDE or Lean certificate."""
from fractions import Fraction as F
from math import factorial


def bounds(a, n=20):
    def term(k):
        return F(2 ** (3 * k - 1) * factorial(2 * k),
                 factorial(k) * factorial(4 * k)) * a ** k
    lo = 1 + sum(term(k) for k in range(1, n + 1))
    q = F(16 * a, (4 * n + 1) ** 3)
    assert 0 < q < 1
    return lo, lo + term(n + 1) / (1 - q)


lo99, hi99 = bounds(99)
lo100, hi100 = bounds(100)
lo101, hi101 = bounds(101)
gap = lo100 * lo100 - hi99 * hi101
assert gap > 0
print("Exact positive lower gap:", gap)
print("Approximate gap:", float(gap))
