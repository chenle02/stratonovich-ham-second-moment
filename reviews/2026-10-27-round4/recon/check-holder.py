"""Exact exponent checks and floating (not certified) Gamma diagnostics."""
import math,json
from fractions import Fraction as F
from pathlib import Path
rows=[]
for al,a0 in [(F(5,4),F(1,4)),(F(3,2),F(1,4)),(F(7,4),F(1,8)),(F(19,10),F(1,20))]:
 b=al-1;p=(1/(1-a0)+1/b)/2;pc=p/(p-1);a=1-b*p/2
 assert b*p<1 and a0*pc<1
 assert 1+(2/p-b)+(2/pc-a0)==4-al-a0
 assert (2-b*p)/p+2/pc==3-al
 D=math.exp(2)*(math.e/float(a))**(2*float(a))
 ratios=[2*math.lgamma(1+float(a)*k)+k*math.log(D)-(2-float(b*p))*math.lgamma(k+1) for k in [1,2,4,16,64]]
 assert min(ratios)>=0
 rows.append(dict(alpha=str(al),alpha0=str(a0),p=str(p),p_conjugate=str(pc),gamma_lower_bound_log_slack=ratios))
Path(__file__).with_name('holder-checks.json').write_text(json.dumps({'status':'exact rational exponent identities; floating Gamma diagnostic only','rows':rows,'prior_attempt':'Inline harness asserted 3-alpha+1 instead of 3-alpha for the combined Holder denominator. That diagnostic typo failed; corrected here. Mathematical memo already had the correct denominator.'},indent=2)+'\n')
print('Four exact parameter/exponent checks and twenty floating Gamma checks passed.')

def pairings(items):
 if not items:
  yield ()
  return
 i,*rest=items
 for j in rest:
  for tail in pairings([x for x in rest if x!=j]):
   yield ((i,j),)+tail

counts=[]
for k in range(1,5):
 ps=list(pairings(list(range(1,2*k+1))))
 assert len(ps)==math.factorial(2*k)//(2**k*math.factorial(k))
 checked=0
 for m in range(2*k+1):
  n=2*k-m
  assert math.factorial(m)*math.factorial(n)>=math.factorial(k)**2
  for D in ps:
   closings=[j for i,j in D]
   k1=sum(j<=m for j in closings); k2=k-k1
   assert k1<=m and k2<=n
   # Positivity of every Dirichlet parameter, and exact denominator sum.
   assert m-b*p*k1>=0 and n-b*p*k2>=0
   assert (m-b*p*k1)+(n-b*p*k2)==(2-b*p)*k
   checked+=1
 counts.append({'k':k,'pairings':len(ps),'split_pairings':checked})
Path(__file__).with_name('finite-count-checks.json').write_text(json.dumps({'scope':'Finite diagnostics only, not an all-order proof','counts':counts},indent=2)+'\n')
print('Finite closing-count and split-factorial checks passed through k=4.')
