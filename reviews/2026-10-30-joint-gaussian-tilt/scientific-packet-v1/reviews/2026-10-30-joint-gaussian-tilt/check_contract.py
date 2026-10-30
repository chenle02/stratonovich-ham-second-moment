"""Exact finite falsification probes; not a Gaussian/flow theorem or Lean gate."""
from fractions import Fraction as Q
import json
from pathlib import Path

rows = []
# A=X, Z=sigma*X+tau*Y, X,Y independent standard normals.
# s=1/sqrt(delta), Cov(A,Z)=sigma, v=sigma^2+tau^2.
for r, sigma, tau, s in [
    (Q(1), Q(1), Q(0), Q(2)),
    (Q(-2, 3), Q(3, 2), Q(4, 5), Q(3)),
    (Q(2), Q(0), Q(3), Q(1, 2)),
    (Q(0), Q(2), Q(1), Q(4)),
]:
    v = sigma*sigma + tau*tau
    lhs = r*r/2
    # Log expectation of exp(-s Z -s^2 v/2 +r(A+s sigma)).
    rhs = -s*s*v/2 + r*s*sigma + ((r-s*sigma)**2+(s*tau)**2)/2
    wrong_sign = -s*s*v/2 + r*s*sigma + ((r+s*sigma)**2+(s*tau)**2)/2
    wrong_cost = -s*s*v + r*s*sigma + ((r-s*sigma)**2+(s*tau)**2)/2
    assert rhs == lhs
    assert wrong_cost != lhs
    if r*sigma:
        assert wrong_sign != lhs
    rows.append(dict(r=str(r), sigma=str(sigma), tau=str(tau), s=str(s),
                     log_lhs=str(lhs), log_rhs=str(rhs),
                     wrong_sign_error=str(wrong_sign-lhs),
                     wrong_cost_error=str(wrong_cost-lhs)))

powers = []
for a in [Q(1, 100), Q(1, 2), Q(99, 100)]:
    amplitude = (1-a)/2+a/2-Q(1, 2)
    assert amplitude == 0
    powers.append(dict(a=str(a), shifted_amplitude_power=str(amplitude)))
result = dict(status='PASS', scope='Exact rational MGF-exponent and amplitude probes only',
              gaussian_cases=rows, amplitude_cases=powers,
              exclusions=['No Gaussian measure proof', 'No path/flow measurability proof',
                          'No spectral product or moment-rate proof', 'No Lean certificate'])
Path(__file__).with_name('finite-checks.json').write_text(json.dumps(result, indent=2)+'\n')
print(json.dumps(result, indent=2))
