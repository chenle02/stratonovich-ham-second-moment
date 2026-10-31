#!/usr/bin/env python3
"""Finite positive wave-chain controls; no continuum or quadrature certification."""
from collections import defaultdict
from functools import lru_cache
from itertools import combinations, product
from pathlib import Path
import json
import mpmath as mp

mp.mp.dps = 50
a, epsilon, delta = map(mp.mpf, ['.5', '.1', '.2'])
times = [mp.mpf(x) for x in ['.2', '.4', '.6', '.8']]
# Actual d2 homogeneous Gamma=delta_(x1=0) tensor Lebesgue_(x2), alpha=1.
# All nodes have x1=0, so the smoothed source is constant across these x2.
nodes = [mp.mpf('0'), mp.mpf('.1')]
weights = [mp.mpf(1), mp.mpf('.5')]
# A smooth radial cutoff equal 1 on r<=1, zero on r>=2 can have value .5
# at r=1.5; choose L=1/15. These are its exact two sampled values.
terminals = [mp.mpf('0'), mp.mpf('.05')]
def kappa(t):
    if t == 0:
        return delta**(-a)/(a*mp.gamma(a))
    return abs(t)**(-a)*mp.gammainc(a, 0, abs(t)/delta)/mp.gamma(a)
heat_zero = 1/mp.sqrt(4*mp.pi*epsilon)
cov = [[heat_zero*kappa(t-s) for s in times] for t in times]
assert min(mp.eigsy(mp.matrix(cov), eigvals_only=True)) > 0

def green(dt, dx):
    assert dt > abs(dx)  # all quadrature points strictly inside light cones
    return 1/(2*mp.pi*mp.sqrt(dt*dt-dx*dx))

def polynomial(n, endpoint, masked):
    out = defaultdict(mp.mpf)
    if n == 0:
        out[(0, 0, 0, 0)] = mp.mpf(1)
        return out
    for inds in combinations(range(4), n):
        powers = tuple(int(i in inds) for i in range(4))
        for choices in product(range(2), repeat=n):
            coefficient = mp.mpf('.02')**n  # positive dt*spatial quadrature weight
            for j in range(n):
                later_t = times[inds[j+1]] if j+1 < n else mp.mpf(1)
                later_x = nodes[choices[j+1]] if j+1 < n else endpoint
                coefficient *= green(later_t-times[inds[j]], later_x-nodes[choices[j]])
                if masked:
                    coefficient *= weights[choices[j]]
            out[powers] += coefficient
    return out

@lru_cache(None)
def wick(powers):
    degree = sum(powers)
    if degree == 0:
        return mp.mpf(1)
    if degree % 2:
        return mp.mpf(0)
    i = next(j for j, p in enumerate(powers) if p)
    remaining = list(powers)
    remaining[i] -= 1
    result = mp.mpf(0)
    for j, count in enumerate(remaining):
        if count:
            tail = remaining.copy()
            tail[j] -= 1
            result += count*cov[i][j]*wick(tuple(tail))
    return result

def mixed(p, q):
    return sum((u*v*wick(tuple(x+y for x,y in zip(k,l)))
                for k,u in p.items() for l,v in q.items()), mp.mpf(0))

polys = {(e,n,m):polynomial(n,e,m) for e in terminals for n in range(5) for m in [False,True]}
rows = []
for x, y in product(terminals, repeat=2):
    for n, k in product(range(5), repeat=2):
        full = mixed(polys[x,n,False], polys[y,k,False])
        masked = mixed(polys[x,n,True], polys[y,k,True])
        assert 0 <= masked <= full
        if (n+k) % 2:
            assert masked == full == 0
        rows.append({'x':str(x),'y':str(y),'n':n,'k':k,
                     'full':mp.nstr(full,30),'masked':mp.nstr(masked,30),
                     'ratio':None if full == 0 else mp.nstr(masked/full,25)})
assert any(r['n'] != r['k'] and r['ratio'] is not None and mp.mpf(r['ratio']) < 1 for r in rows)
# Actual same-time source point covariance at the two spatial nodes is c*ones.
# Entrywise decrease does NOT imply PSD decrease: eigenvalues are -c/4,c.
c = cov[0][0]
difference = mp.matrix([[0,c/2],[c/2,3*c/4]])
assert mp.det(difference) == -c*c/4
assert min(mp.eigsy(difference,eigvals_only=True)) < 0
# Signed field observable Z(x0)-Z(x1): full variance zero, masked positive.
full_signed, masked_signed = mp.mpf(0), c/4
assert masked_signed > full_signed

out = {'working_decimal_precision':50,'printed_digits':30,
       'scope':'Finite positive quadrature with actual d2 singular homogeneous source covariance. Not an error-controlled PDE approximation, continuum proof, or certified accuracy.',
       'model':'d=2; Gamma=delta_x1 tensor Leb_x2; alpha=1; a=.5; epsilon=.1; delta=.2; T=1',
       'time_grid':[str(t) for t in times], 'spatial_x2_nodes':[str(x) for x in nodes],
       'mask_values':[str(w) for w in weights], 'mixed_order_rows':rows,
       'row_count':len(rows),'odd_total_zero_rows':sum((r['n']+r['k'])%2 for r in rows),
       'self_pairing_control':'n=0,k=2 and n=0,k=4 included; n=k=2 includes all three pairings',
       'psd_order_negative_control':{'difference_eigenvalues_over_c':['-1/4','1'],
                                     'difference_determinant_over_c_squared':'-1/4'},
       'signed_observable_negative_control':{'full_variance':'0','masked_variance_over_c':'1/4'}}
Path(__file__).with_name('low-orders-v1.json').write_text(json.dumps(out,indent=2)+'\n')
print(f'PASS {len(rows)} mixed-order controls (orders 0..4, total <=8), PSD/signed negative controls.')
