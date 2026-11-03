#!/usr/bin/env python3
"""Exact finite algebra checks; no discretized analytic premise."""
import json
from fractions import Fraction as F
from pathlib import Path

checks = {}
# k=ell=b=1, threshold phi=1, epsilon=1/16.
eps = F(1, 16)
gain = 2 * F(1, 4) - eps - eps * eps / 2
assert gain == F(223, 512) and gain > 0
checks['nonzero_active_boundary_gain'] = str(gain)
# Two identical unit labels, each ell=1/2 and b=0. Positive optimizer phi=1.
w = [F(1, 2), F(1, 2)]
assert all(sum(w) == F(1, 4) / x**2 for x in w)
score = F(2) - F(1, 2)
dual = sum(F(1, 4)/x for x in w) + sum(w)**2/2
assert score == dual == F(3, 2)
checks['singular_duplicate_labels'] = {'rank': 1, 'value': str(score), 'positive_coefficients': list(map(str,w))}
# A zero label's row is zero; for b>=0 its positive-part contribution is zero.
assert all(max(-b,F(0)) == 0 for b in [F(0),F(1),F(17,3)])
checks['zero_label_threshold_and_inactive_cases'] = True
# C=I, D has off-diagonal 1/2. D is positive definite, D-C indefinite.
assert F(1) - F(1,2)**2 == F(3,4) > 0
q_plus = 2*F(1,2)
q_minus = -2*F(1,2)
assert q_plus > 0 > q_minus
checks['entrywise_comparison_without_psd_difference'] = {'det_D': '3/4', 'difference_quadratics': [str(q_plus),str(q_minus)]}
# One label: ell=1/10, b=4, C=1. A nonempty dual branch can be negative.
value = F(1,100)/4 - 4*4 + F(4*4,2)
assert value == F(-3199,400) < 0
checks['empty_branch_required'] = str(value)
# The two-cell root average is 1 whereas root of average is sqrt(2).
assert F(2) > F(1)**2
checks['reverse_jensen_fails'] = {'mean_roots': '1', 'root_mean_squared': '2'}
# Exact temporal total mass at a=1/2.
a=F(1,2)
za=2/((1-a)*(2-a))
assert za == F(8,3)
checks['temporal_total_mass_a_half'] = str(za)
out={'method':'Python standard-library Fraction; exact rational arithmetic', 'checks':checks,'all_passed':True}
Path(__file__).with_name('finite_checks.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
print(json.dumps(out,indent=2))
