"""Exact rational pre-investment controls; not a full mean or asymptotic proof."""
from fractions import Fraction as F
from pathlib import Path
import json,hashlib

def parent(a):
    return (1-a)/(F(1,2)*(F(3,2)-a)*(F(5,2)-a)*(F(7,2)-a))

rows=[]
for a in [F(1,2),F(3,4),F(9,10),F(19,20),F(49,50),F(99,100),F(999,1000)]:
    # Projection lower bound (2-a)/(32*sqrt(2)) > (2-a)/48.
    # A negative lower-minus-parent value does NOT decide the actual sign.
    lower=(2-a)/48;A=parent(a)
    rows.append(dict(a=str(a),parent=str(A),rational_projection_lower=str(lower),certified_projection_exceeds_parent=lower>A))
a=F(99,100);A=parent(a)
assert A==F(20000,1932951)<F(1,96)
assert (2-a)/48>F(1,48)
for q in [F(5,4),F(3,2),F(7,4),F(199,100)]:
    p=(2-a)/48
    assert q*p-(A+(q-1)*p)==p-A>F(1,96)
# Independent two-pulse quadratic sanity check. PSD residual contributes
# (x-y)^2/2, but its off-diagonal entry is negative.
for x in range(-4,5):
 for y in range(-4,5):
    assert F(x*x+y*y)-F((x+y)**2,2)==F((x-y)**2,2)>=0
out=dict(status='PASS exact finite controls only',alpha='1/2',a=str(a),parent_coefficient=str(A),projection_actual_lower='101/(3200*sqrt(2))',certified_gap='>1/96',rows=rows,tilt_parameters_checked=['5/4','3/2','7/4','199/100'],pulse_quadratic_controls=81,source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),full_model_analytic_projection_and_mean_comparison='CANDIDATE; independent analytic/type review required',not_a_sharp_or_all_tilts_no_go=True)
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
