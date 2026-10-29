"""Exact exponent budgets before analytic proof; no full-flow result."""
from fractions import Fraction as F
from pathlib import Path
import json,hashlib
rows=[]
for alpha in [F(1,4),F(1,2),F(1),F(3,2)]:
 for a in [F(1,10),F(1,2),F(9,10)]:
  b=alpha+a
  if b>=2:continue
  s=1-b/4
  assert F(1,2)<s<1 and 2*s+b<3
  assert 2*s+b-3==(b-2)/2<0
  assert (2+b<3)==(b<1)
  # Two high-q sector powers in the localized first-response HS audit.
  assert 2*s+b-4<-1 and b-3<-1
  rows.append(dict(alpha=str(alpha),a=str(a),phase_s=str(s),trace_exponent=str(2*s+b-3),energy_passes=b<1,d1_operator_eligible=alpha<=1,HS_sector_A_power=str(2*s+b-4),HS_other_sector_power=str(b-3)))
# Homogeneous-annulus geometric budgets,including the critical endpoint.
annuli=[]
for e in [F(-1,2),F(0),F(1,2)]:
 for N in [4,8,16]:
  # Use exact squared ratios so every sum is rational.
  assert (2*e).denominator==1
  ratio=F(2)**int(2*e)
  v=sum(ratio**n for n in range(N))
  assert (v==N) if e==0 else v>0
  annuli.append(dict(exponent=str(e),annuli=N,squared_ratio=str(ratio),geometric_sum=str(v)))
out=dict(status='PASS exact finite budgets only',cases=len(rows),rows=rows,annulus_controls=annuli,source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),not_analytic_phase_or_operator_proof=True,not_allorder_sharp=True)
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
