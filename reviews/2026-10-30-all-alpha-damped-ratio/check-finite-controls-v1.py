from fractions import Fraction as F
from pathlib import Path
import json

a,D=F(1,2),F(4);lo=2*a*a/(D+4*a)
x,y=F(2,5),F(1,10);assert x+y==a and x*x<=D*y/2 and lo<=y
xn,yn=F(43,100),F(7,100);assert xn+yn==a and xn*xn<=D*yn and yn<lo
x0,y0=F(0),F(0);assert x0+y0<=a and x0*x0<=D*y0/2 and y0<lo
gap=a*a/(D*(D+4*a))-a*a/(2*D*(D+2*a));assert gap==a*a/(2*(D+4*a)*(D+2*a))==F(1,240)
data={'scope':'Exact Python rational falsification, not a Lean run or analytic moment identity','positive_case':{'a':str(a),'D':str(D),'x':str(x),'y':str(y),'target_lower':str(lo)},'lost_half_counterexample':{'a':str(a),'D':str(D),'x':str(xn),'y':str(yn),'weaker_cs_true':True,'target_bound_false':True},'missing_mean_counterexample':{'a':str(a),'D':str(D),'x':'0','y':'0','weaker_mean_inequality_true':True,'target_bound_false':True},'rational_gap':str(gap),'wrong_double_gap':str(2*gap),'zero_a_strict_gap':False}
encoded=(json.dumps(data,indent=2)+'\n').encode()
assert encoded==Path(__file__).with_name('finite-controls-v1.json').read_bytes()
print('Exact fixture generator matches frozen JSON bytes; no source artifact mutated.')
