"""Finite exact Gaussian/Jacobian falsification controls; not a general proof."""
from fractions import Fraction as F
from itertools import permutations
from pathlib import Path
import json


def det(a):
    n = len(a)
    total = F(0)
    for p in permutations(range(n)):
        sign = (-1) ** sum(p[i] > p[j] for i in range(n) for j in range(i + 1, n))
        value = F(sign)
        for i in range(n):
            value *= a[i][p[i]]
        total += value
    return total


def mul(a, b):
    return [[sum(a[i][k] * b[k][j] for k in range(len(b)))
             for j in range(len(b[0]))] for i in range(len(a))]


def transpose(a):
    return [list(row) for row in zip(*a)]


def inverse(a):
    n = len(a)
    b = [[F(x) for x in row] + [F(i == j) for j in range(n)] for i, row in enumerate(a)]
    for col in range(n):
        pivot = next(i for i in range(col, n) if b[i][col])
        b[col], b[pivot] = b[pivot], b[col]
        scale = b[col][col]
        b[col] = [x / scale for x in b[col]]
        for i in range(n):
            if i != col:
                factor = b[i][col]
                b[i] = [x - factor * y for x, y in zip(b[i], b[col])]
    return [row[n:] for row in b]


matrices = [
    [[2, 0, 0], [0, 1, 0], [0, 0, F(1, 2)]],
    [[2, 0, 0], [0, 1, 0], [0, 0, 1]],
    [[1, 1, 0], [0, 1, 1], [0, 0, 1]],
    [[-2, 0, 0], [0, 1, 0], [0, 0, F(1, 2)]],
    [[3, 0, 0], [0, 3, 0], [0, 0, 3]],
    [[2, 1, 0], [0, 1, 1], [1, 0, 1]],
]
cases = 0
for raw in matrices:
    t = [[F(x) for x in row] for row in raw]
    ti = inverse(t)
    ident = [[F(i == j) for j in range(3)] for i in range(3)]
    assert mul(t, ti) == ident
    d = abs(det(t))
    for eps in [F(1, 10), F(1), F(7, 3)]:
        sigma = [[eps * x for x in row] for row in mul(ti, transpose(ti))]
        assert det(sigma) == eps ** 3 / d ** 2
        assert inverse(sigma) == [[x / eps for x in row] for row in mul(transpose(t), t)]
        # A conservative scalar variance; no floating eigenvalue calculation.
        a = eps / (2 * sum(x * x for row in t for x in row))
        rest = [[sigma[i][j] - (a if i == j else 0) for j in range(3)] for i in range(3)]
        assert a > 0
        assert all(det([row[:n] for row in rest[:n]]) > 0 for n in [1, 2, 3])
        for theta in [F(1, 5), F(1, 2), F(4, 5)]:
            assert -theta - (1 - theta) == -1
            cases += 1

c = F(3, 7)
plane_checks = []
for diagonal in [(F(2), F(1), F(1, 2)), (F(2), F(1), F(1))]:
    d = abs(diagonal[0] * diagonal[1] * diagonal[2])
    actual = c / abs(diagonal[0] * diagonal[1])
    transformed = c * abs(diagonal[2]) / d
    assert actual == transformed
    plane_checks.append({"diagonal": list(map(str, diagonal)), "plane_amplitude": str(actual)})

out = {"status": "PASS", "matrices": len(matrices), "exact_parameter_cases": cases,
       "plane_amplitude_controls": plane_checks,
       "scope": "finite exact matrix/Jacobian and Gaussian exponent controls only; no analytic, independent-review or Lean certificate"}
Path(__file__).with_suffix(".json").write_text(json.dumps(out, indent=2) + "\n")
print(json.dumps(out, indent=2))
