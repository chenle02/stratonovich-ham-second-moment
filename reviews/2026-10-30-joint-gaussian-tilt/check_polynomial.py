"""Exact polynomial falsification of finite tilt normalization; no measure theorem."""
from fractions import Fraction as Q
from pathlib import Path
import json

# Sparse polynomials over Q in (r,s,c,v,w); no floating point or CAS oracle.
def add(p, q):
    out = dict(p)
    for k, a in q.items():
        out[k] = out.get(k, Q(0)) + a
    return {k: a for k, a in out.items() if a}
def scale(p, c):
    return {k: c*a for k, a in p.items() if c*a}
def mul(p, q):
    out = {}
    for k, a in p.items():
        for l, b in q.items():
            m = tuple(x+y for x, y in zip(k, l))
            out[m] = out.get(m, Q(0)) + a*b
    return {k: a for k, a in out.items() if a}
def var(i):
    powers = [0]*5
    powers[i] = 1
    return {tuple(powers): Q(1)}
def square(p):
    return mul(p, p)
def encoded(p):
    return [{'powers_r_s_c_v_w': list(k), 'coefficient': str(a)} for k, a in sorted(p.items())]
r, s, c, v, w = [var(i) for i in range(5)]
rsc = mul(mul(r, s), c)
s2v = mul(square(s), v)
r2w = mul(square(r), w)
# Joint Gaussian MGF formal exponent: Var(r A - s Z)/2.
minus_variance = add(add(r2w, scale(rsc, -2)), s2v)
correct_error = add(add(scale(s2v, Q(-1, 2)), rsc),
                    add(scale(minus_variance, Q(1, 2)), scale(r2w, Q(-1, 2))))
assert correct_error == {}
# Wrong plus density changes the covariance cross term, hence adds 2 r s c.
plus_variance = add(add(r2w, scale(rsc, 2)), s2v)
wrong_sign = add(add(scale(s2v, Q(-1, 2)), rsc),
                 add(scale(plus_variance, Q(1, 2)), scale(r2w, Q(-1, 2))))
assert wrong_sign == scale(rsc, 2)
# Wrong full-variance cost instead of half-cost.
wrong_cost = add(add(scale(s2v, -1), rsc),
                 add(scale(minus_variance, Q(1, 2)), scale(r2w, Q(-1, 2))))
assert wrong_cost == scale(s2v, Q(-1, 2))
result = dict(status='PASS', coefficient_field='exact rational',
              variables=['r', 's', 'c', 'v', 'w'],
              correct_error=encoded(correct_error),
              wrong_sign_error=encoded(wrong_sign),
              wrong_cost_error=encoded(wrong_cost),
              exclusions=['No Gaussian MGF or measure theorem proved',
                          'No path/flow theorem', 'No Lean certificate',
                          'No event/constant bound'])
Path(__file__).with_name('polynomial-checks.json').write_text(json.dumps(result, indent=2)+'\n')
print(json.dumps(result, indent=2))
