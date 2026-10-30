"""Replay the exact frozen two-entry rational proxy; not a HAM theorem."""
from fractions import Fraction as Q
from pathlib import Path
import json
d = json.loads(Path(__file__).with_name('diagnostics-v2.json').read_text())
z = (Q(1), Q(0))
previous = None
for m, row in enumerate(d['rows']):
  lam = 1 + Q(m % 2, 100)
  ell = lambda z: (z[0] + z[1] / lam) / 2
  a = ell(z)
  z = (a + (z[0] - a) / 16, lam*a + (z[1] - lam*a) / 16)
  amplitude = ell(z)
  residual = max(abs(z[0] - amplitude), abs(z[1] - lam*amplitude))
  assert row == {'m': m, 'lambda': str(lam),
    'positive_amplitude': amplitude > 0,
    'cone': residual <= Q(1, 8)*amplitude,
    'positive_displacement': z[0] > 0}
  assert amplitude > 0 and residual <= Q(1, 8)*amplitude and z[0] > 0
  if previous is not None:
    assert amplitude >= Q(99, 100)*previous
  previous = amplitude
assert len(d['rows']) == d['moving_proxy_cases'] == 100 and d['all_pass']
A = ((Q(2), Q(0)), (Q(0), Q(1, 2)))
B = ((Q(1, 2), Q(0)), (Q(0), Q(2)))
assert [[sum(B[i][k]*A[k][j] for k in range(2)) for j in range(2)]
        for i in range(2)] == [[1, 0], [0, 1]]
assert (Q(0), Q(100))[0] == 0
print('PASS: all100 exact proxy rows/amplitude controls and both kill witnesses')
