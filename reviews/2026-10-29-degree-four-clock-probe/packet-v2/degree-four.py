"""Full Stratonovich degree-four gap-transform probe, NOT a proof.

48 labelled global-order cones map to 15 ordered-chain pairing diagrams.
Spatial wave positions and the physical radial time are integrated exactly.
The shared-clock Gaussian average is sampled by its positive Laplace mixture.
No clipping; independently scrambled Sobol replicates give diagnostics only,
not certified enclosures or an IID confidence interval.
"""
from __future__ import annotations

import argparse
from collections import Counter
from fractions import Fraction
import hashlib
import itertools
import json
import math
from pathlib import Path
import platform
import time

import numpy as np
import scipy
from scipy.integrate import quad
from scipy.special import gammaincinv, gammaln
from scipy.stats import qmc


PAIRINGS = (((0, 1), (2, 3)), ((0, 2), (1, 3)), ((0, 3), (1, 2)))


def key(m, pairing):
    return str(m) + ':' + '|'.join(''.join(map(str, p)) for p in pairing)


def graphs():
    out = []
    for colors in itertools.product(range(2), repeat=4):
        chains = [[j for j, c in enumerate(colors) if c == i] for i in range(2)]
        m = len(chains[0])
        local = {j: k for k, j in enumerate(chains[0] + chains[1])}
        for pairing in PAIRINGS:
            labels = [next(k for k, p in enumerate(pairing) if j in p) for j in range(4)]
            canon = tuple(sorted(tuple(sorted(local[j] for j in p)) for p in pairing))
            # Two pair differences, expressed in eight independent Brownian increments.
            charges = np.zeros((2, 8), dtype=int)
            for row, (i, j) in enumerate(pairing):
                for k in range(i + 1):
                    charges[row, 4 * colors[i] + k] -= 1
                for k in range(j + 1):
                    charges[row, 4 * colors[j] + k] += 1
            # Cauchy--Binet positive polynomial; no subtractive determinant cancellation.
            terms = Counter()
            for i, j in itertools.combinations(range(8), 2):
                minor = int(charges[0, i] * charges[1, j] - charges[0, j] * charges[1, i])
                if minor:
                    terms[tuple(sorted((i % 4, j % 4)))] += minor * minor
            roots = [chain[0] for chain in chains if chain]
            edges = [(i, j) for chain in chains for i, j in zip(chain, chain[1:])]
            abc = [sum(labels[i] == p for i in roots) for p in range(2)]
            abc.append(sum(labels[i] != labels[j] for i, j in edges))
            A, B, C = abc
            static = Fraction(A + B + C, 4 * (A + B) * (A + C) * (B + C))
            out.append(dict(colors=colors, chains=chains, pairing=pairing,
                            labels=labels, key=key(m, canon), m=m,
                            det_terms=[(i, j, c) for (i, j), c in sorted(terms.items())],
                            static=static, abc=abc))
    counts = Counter(g['key'] for g in out)
    assert len(out) == 48 and len(counts) == 15
    assert all(counts[k] == math.comb(4, int(k[0])) for k in counts)
    for k in counts:
        subset = [g for g in out if g['key'] == k]
        assert len({g['static'] for g in subset}) == 1
    return out


def physical_volume(x, t, g):
    """Area in the two paired spatial positions, divided by 2**4."""
    bounds = [np.full(len(x), np.inf), np.full(len(x), np.inf)]
    cross = np.full(len(x), np.inf)
    for chain in g['chains']:
        if not chain:
            continue
        first = chain[0]
        p = g['labels'][first]
        bounds[p] = np.minimum(bounds[p], t[:, first])
        for i, j in zip(chain, chain[1:]):
            if g['labels'][i] != g['labels'][j]:
                cross = np.minimum(cross, x[:, i + 1:j + 1].sum(axis=1))
    A, B = bounds
    if np.isinf(A).all():
        area = 4 * B * cross
    elif np.isinf(B).all():
        area = 4 * A * cross
    elif np.isinf(cross).all():
        area = 4 * A * B
    else:
        low, high = np.minimum(A, B), np.maximum(A, B)
        c = np.minimum(cross, high + low)
        # Stable equivalent of rectangle minus the two clipped triangles.
        area = 4 * low * c - np.maximum(0, c - (high - low)) ** 2
    assert np.isfinite(area).all() and (area > 0).all()
    return area / 16


def evaluate(a, power, reps, eta, seed, all_graphs):
    assert 0 <= a < 1 and 0 < eta < 1 - a
    keys = sorted({g['key'] for g in all_graphs})
    rows = []
    q = 6 - 2 * a
    # Positive mixture: Y_i = sqrt(2*Gamma(a/2,1)).
    ca = math.exp((a / 2 - 1) * math.log(2) + gammaln(a / 2) - gammaln(a)) if a else 1
    pref = ca ** 2 * math.gamma(3 - a) * 2 ** (3 - a) / (32 * math.pi)
    for rep in range(reps):
        u = qmc.Sobol(7, scramble=True, seed=seed + 7919 * rep).random_base2(power)
        z = gammaincinv(eta, u[:, :4])
        x = z / z.sum(axis=1)[:, None]
        t = np.cumsum(x, axis=1)
        invpdf = np.exp(4 * gammaln(eta) - gammaln(4 * eta)
                        + (1 - eta) * np.log(x).sum(axis=1))
        y = np.sqrt(2 * gammaincinv(a / 2, u[:, 4:6])) if a else np.zeros((len(x), 2))
        radial = gammaincinv(3 - a, u[:, 6]) if a else np.zeros(len(x))
        actual = {k: np.zeros(len(x)) for k in keys}
        candidate = {k: np.zeros(len(x)) for k in keys}
        for g in all_graphs:
            intervals = [x[:, i + 1:j + 1].sum(axis=1) for i, j in g['pairing']]
            d1, d2 = intervals
            ell = sum(t[:, chain[-1]] for chain in g['chains'] if chain)
            volume = physical_volume(x, t, g)
            physical = math.gamma(q) * volume * (d1 * d2) ** (-a) / ell ** q
            det = sum(c * x[:, i] * x[:, j] for i, j, c in g['det_terms'])
            assert (det > 0).all()
            if a:
                (i, j), (k, l) = g['pairing']
                left, right = max(i, k), min(j, l)
                overlap = x[:, left + 1:right + 1].sum(axis=1) if left < right else np.zeros(len(x))
                corr = overlap / np.sqrt(d1 * d2)
                S = np.sqrt(d1) * y[:, 0] + np.sqrt(d2) * y[:, 1]
                mixture = np.exp(-np.sqrt(2 * radial / ell) * S - corr * y[:, 0] * y[:, 1])
            else:
                mixture = np.ones(len(x))
            copied = pref * ell ** (a - 3) * (d1 * d2) ** (-a / 2) / np.sqrt(det) * mixture
            assert np.isfinite(physical).all() and np.isfinite(copied).all()
            actual[g['key']] += physical * invpdf
            candidate[g['key']] += copied * invpdf
        for k in keys:
            rows.append(dict(rep=rep, key=k, actual=float(actual[k].mean()),
                             shared=float(candidate[k].mean()),
                             difference=float((actual[k] - candidate[k]).mean()),
                             actual_largest_draw_fraction=float(actual[k].max() / actual[k].sum()),
                             shared_largest_draw_fraction=float(candidate[k].max() / candidate[k].sum())))
    result = []
    for k in keys:
        subset = [r for r in rows if r['key'] == k]
        r = {'key': k, 'static_exact': str(next(g['static'] for g in all_graphs if g['key'] == k))}
        for name in ['actual', 'shared', 'difference']:
            v = np.array([s[name] for s in subset])
            r[name] = float(v.mean())
            r[name + '_replicate_se'] = float(v.std(ddof=1) / math.sqrt(reps))
        r['ratio'] = r['shared'] / r['actual']
        for n in ['actual_largest_draw_fraction', 'shared_largest_draw_fraction']:
            r[n] = max(s[n] for s in subset)
        result.append(r)
    totals = []
    for rep in range(reps):
        subset = [r for r in rows if r['rep'] == rep]
        totals.append({n: sum(r[n] for r in subset) for n in ['actual', 'shared', 'difference']})
    total = {}
    for n in ['actual', 'shared', 'difference']:
        v = np.array([s[n] for s in totals])
        total[n] = float(v.mean())
        total[n + '_replicate_se'] = float(v.std(ddof=1) / math.sqrt(reps))
    total['ratio'] = total['shared'] / total['actual']
    return dict(a=a, eta=eta, sobol_power=power, replicates=reps, seed=seed,
                points_per_replicate=2 ** power, diagrams=result, total=total,
                raw_replicates=rows)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--a', type=float, nargs='+', default=[0, .5])
    parser.add_argument('--power', type=int, default=14)
    parser.add_argument('--replicates', type=int, default=4)
    parser.add_argument('--eta', type=float, default=.25)
    parser.add_argument('--seed', type=int, default=314159)
    parser.add_argument('--out', type=Path, required=True)
    args = parser.parse_args()
    started = time.monotonic()
    gs = graphs()
    data = [evaluate(a, args.power, args.replicates, args.eta, args.seed, gs) for a in args.a]
    manifest = [{k: v for k, v in g.items() if k not in ['static']} | {'static': str(g['static'])} for g in gs]
    exact_total = sum({g['key']: g['static'] for g in gs}.values())
    result = dict(status='UNREVIEWED finite floating probe;not an analytic comparison',
                  theta=1, source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
                  versions=dict(python=platform.python_version(), numpy=np.__version__, scipy=scipy.__version__),
                  static_total_exact=str(exact_total), graphs=manifest, runs=data,
                  elapsed_seconds=time.monotonic() - started,
                  errors='Scramble-replicate SE is diagnostic,not a certified bound. No clipping/discretization of covariance;floating-point and finite-sample errors remain.',
                  excludes='No all-order comparison,diagonal-horizon transfer,sharp constant,Skorohod result or novelty verdict.')
    args.out.write_text(json.dumps(result, indent=2) + '\n')
    print(json.dumps({'output': str(args.out), 'elapsed_seconds': result['elapsed_seconds'],
                      'static_exact': str(exact_total),
                      'totals': [{'a': r['a'], **r['total']} for r in data]}, indent=2))


if __name__ == '__main__':
    main()
