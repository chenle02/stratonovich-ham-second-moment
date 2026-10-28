"""Exact matrix/rational controls plus Gaussian quadrature, not the H1 proof."""
from fractions import Fraction as F
from itertools import permutations
from pathlib import Path
import json
import mpmath as mp


def det(a):
    n = len(a)
    total = F(0)
    for p in permutations(range(n)):
        value = F((-1) ** sum(p[i] > p[j] for i in range(n) for j in range(i + 1, n)))
        for i in range(n):
            value *= a[i][p[i]]
        total += value
    return total


def mul(a, b):
    return [[sum(a[i][k] * b[k][j] for k in range(len(b)))
             for j in range(len(b[0]))] for i in range(len(a))]


def tr(a):
    return [list(row) for row in zip(*a)]


def inv(a):
    n = len(a)
    b = [[F(x) for x in row] + [F(i == j) for j in range(n)] for i, row in enumerate(a)]
    for j in range(n):
        pivot = next(i for i in range(j, n) if b[i][j])
        b[j], b[pivot] = b[pivot], b[j]
        scale = b[j][j]
        b[j] = [x / scale for x in b[j]]
        for i in range(n):
            if i != j:
                scale = b[i][j]
                b[i] = [x - scale * y for x, y in zip(b[i], b[j])]
    return [row[n:] for row in b]


profiles = [[[1, 0, 0], [0, 1, 0], [0, 0, 1]],
            [[2, 1, 0], [1, 2, 0], [0, 0, 3]],
            [[2, 1, 1], [1, 3, 0], [1, 0, 2]]]
maps = [[[1, 0, 0], [0, 1, 0], [0, 0, 1]],
        [[2, 0, 0], [0, 1, 0], [0, 0, F(1, 2)]],
        [[-2, 0, 0], [0, 1, 0], [0, 0, F(1, 2)]],
        [[1, 0, 0], [0, 1, 0], [1, 1, 1]]]
count = 0
for raw_b in profiles:
    b = [[F(x) for x in row] for row in raw_b]
    assert all(det([row[:n] for row in b[:n]]) > 0 for n in [1, 2, 3])
    for raw_t in maps:
        t = [[F(x) for x in row] for row in raw_t]
        ti = inv(t)
        normal = [[x] for x in ti[2]]  # T^(-transpose)e3 = row3 of T^(-1).
        q = mul(tr(normal), mul(inv(b), normal))[0][0]
        tp = [row[:2] for row in t]
        gram = mul(tr(tp), mul(b, tp))
        assert det(gram) == det(t) ** 2 * det(b) * q
        count += 1

# H1 but not Schwartz: normalized tensor tent profile and a normal-plane delta.
tent_energy = F(3, 2) ** 6 * F(2, 3) ** 4 * F(2, 5)
assert tent_energy == F(9, 10)

mp.mp.dps = 60
gaussian = mp.quad(lambda x: mp.exp(-x * x / 2), [-mp.inf, 0, mp.inf])
half_gaussian = mp.quad(lambda x: mp.exp(-x * x / 2), [0, mp.inf])
radial = mp.quad(lambda x: x * mp.exp(-x * x / 2), [0, mp.inf])
plane_physical = gaussian ** 2 / (2 * mp.pi) ** mp.mpf('1.5')
plane_spectral = gaussian / (2 * mp.pi)
riesz_physical = 4 * mp.pi * radial / (2 * mp.pi) ** mp.mpf('1.5')
riesz_spectral = 4 * mp.pi * half_gaussian / (2 * mp.pi ** 2)
constant_physical = gaussian ** 3 / (2 * mp.pi) ** mp.mpf('1.5')
assert abs(plane_physical - plane_spectral) < mp.mpf('1e-45')
assert abs(riesz_physical - riesz_spectral) < mp.mpf('1e-45')
assert abs(constant_physical - 1) < mp.mpf('1e-45')
out = {"scope": "finite exact matrix/rational and numerical normalization checks only; not the analytic H1 lemma, independent review or Lean",
       "initial_control_failure": "used a column instead of the inverse row for T^(-transpose)e3; nonsymmetric tilt refused; corrected before any manuscript or review freeze",
       "matrix_profile_map_cases": count, "tent_plane_energy_exact": str(tent_energy),
       "gaussian_plane_physical": str(plane_physical), "gaussian_plane_spectral": str(plane_spectral),
       "gaussian_riesz_physical": str(riesz_physical), "gaussian_riesz_spectral": str(riesz_spectral),
       "constant_covariance_physical": str(constant_physical), "status": "PASS"}
Path(__file__).with_suffix('.json').write_text(json.dumps(out, indent=2) + '\n')
print(json.dumps(out, indent=2))
