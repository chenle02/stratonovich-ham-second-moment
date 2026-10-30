"""Recompute stored finite controls; does not certify analytic operators."""
import json
from fractions import Fraction as Q
from pathlib import Path

stored = json.loads(Path(__file__).with_name('diagnostics.json').read_text())
rows = stored['geometry_rows']
assert len(rows) == stored['geometry_cases'] == 155
for row in rows:
  t, j = Q(row['t']), row['j']
  distance = abs(j) + max(t - abs(j), 0)
  assert Q(row['tail_exponent_distance']) == distance >= t
ell = lambda z: sum(z) / 2
remainder = lambda z: (z[0] - ell(z), z[1] - ell(z))
z, cut = (Q(3), Q(5)), (Q(3), Q(0))
correction = ell((cut[0] - z[0], cut[1] - z[1]))
control = stored['cutoff_identity']
assert Q(control['left']) == remainder(z)[0]
assert Q(control['localized']) == remainder(cut)[0]
assert Q(control['correction']) == correction
assert remainder(z)[0] == remainder(cut)[0] + correction
assert remainder(z)[0] != remainder(cut)[0] - correction
assert remainder(z)[0] != remainder(cut)[0]
zero = stored['threshold_zero']
assert Q(zero['displacement']) == Q(zero['t']) * Q(zero['velocity']) != 0
print('PASS: 155 geometry cases, cutoff correction/sign controls, zero threshold')
