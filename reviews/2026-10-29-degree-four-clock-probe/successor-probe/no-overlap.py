"""Stronger fixed-Laplace-parameter screen; integrated signs remain separate."""
import argparse
import hashlib
import importlib.util
import itertools
import json
import math
from pathlib import Path
import time

import numpy as np
from scipy.special import gammaincinv, gammaln
from scipy.stats import qmc


BASE = Path(__file__).resolve().parents[1] / 'degree-four.py'
spec = importlib.util.spec_from_file_location('degree_four', BASE)
base = importlib.util.module_from_spec(spec)
spec.loader.exec_module(base)


def evaluate(parameters, power, reps, eta, seed):
    remaining={'1:02|13','1:03|12','2:02|13','2:03|12','3:01|23','3:02|13'}
    gs = [g for g in base.graphs() if g['key'] in remaining]
    keys = sorted({g['key'] for g in gs})
    values = {p: [] for p in parameters}
    for rep in range(reps):
        u = qmc.Sobol(4, scramble=True, seed=seed + rep * 7919).random_base2(power)
        z = gammaincinv(eta, u)
        x = z / z.sum(axis=1)[:, None]
        t = np.cumsum(x, axis=1)
        invpdf = np.exp(4 * gammaln(eta) - gammaln(4 * eta)
                        + (1 - eta) * np.log(x).sum(axis=1))
        for parameters_pair in parameters:
            totals = {k: [0., 0.] for k in keys}
            for g in gs:
                local = {j: k for k, j in enumerate(g['chains'][0] + g['chains'][1])}
                pairs = [tuple(sorted(local[j] for j in p)) for p in g['pairing']]
                canon = sorted(pairs)
                lam, nu = [parameters_pair[canon.index(p)] for p in pairs]
                (i, j), (k, l) = g['pairing']
                d1 = x[:, i + 1:j + 1].sum(axis=1)
                d2 = x[:, k + 1:l + 1].sum(axis=1)
                left, right = max(i, k), min(j, l)
                overlap = x[:, left + 1:right + 1].sum(axis=1) if left < right else np.zeros(len(x))
                ell = sum(t[:, chain[-1]] for chain in g['chains'] if chain)
                det = sum(c * x[:, i] * x[:, j] for i, j, c in g['det_terms'])
                volume = base.physical_volume(x, t, g)
                actual = math.gamma(6) * volume / (ell + lam * d1 + nu * d2) ** 6
                H = ell / 2 + lam * d1 + nu * d2 + (lam ** 2 * d1 + nu ** 2 * d2) / 2
                copied = 1 / (16 * math.pi * np.sqrt(det) * H ** 3)
                totals[g['key']][0] += float((invpdf * actual).mean())
                totals[g['key']][1] += float((invpdf * copied).mean())
            values[parameters_pair].append(totals)
    output = []
    for p in parameters:
        rows = []
        for k in keys:
            a = np.array([v[k][0] for v in values[p]])
            b = np.array([v[k][1] for v in values[p]])
            rows.append(dict(key=k, actual=float(a.mean()), shared=float(b.mean()),
                             ratio=float(b.mean() / a.mean()),
                             difference=float((a-b).mean()),
                             difference_replicate_se=float((a-b).std(ddof=1) / math.sqrt(reps))))
        output.append(dict(lambdas=p, diagrams=rows,
                           total_actual=sum(r['actual'] for r in rows),
                           total_shared=sum(r['shared'] for r in rows)))
    return output


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--power', type=int, default=15)
    p.add_argument('--replicates', type=int, default=4)
    p.add_argument('--eta', type=float, default=.125)
    p.add_argument('--out', type=Path, required=True)
    args = p.parse_args()
    start = time.monotonic()
    params = list(itertools.product([0, .1, 1, 10], repeat=2))
    data = evaluate(params, args.power, args.replicates, args.eta, 271828)
    result = dict(status='UNREVIEWED stronger upper-candidate after dropping positive clock overlap;not original J',
                  source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
                  helper_sha256=hashlib.sha256(BASE.read_bytes()).hexdigest(),
                  power=args.power, replicates=args.replicates, eta=args.eta,
                  seed=271828, runs=data, elapsed_seconds=time.monotonic()-start,
                  scope='Tests J_no_overlap<=I for six remaining diagrams. Failure kills only this shortcut,not original J<=I or the SPDE conjecture.')
    args.out.write_text(json.dumps(result, indent=2)+'\n')
    mixed = [r for run in data for r in run['diagrams'] if r['key'][0] not in '04']
    print(json.dumps(dict(output=str(args.out), elapsed_seconds=result['elapsed_seconds'],
                          max_mixed_ratio=max(r['ratio'] for r in mixed),
                          negative_mixed=[r for r in mixed if r['difference'] < -8*r['difference_replicate_se']]), indent=2))


if __name__ == '__main__':
    main()
