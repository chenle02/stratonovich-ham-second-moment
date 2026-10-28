"""Exact finite screening of the proposed endpoint exponent construction."""
from fractions import Fraction as F
from itertools import product
from pathlib import Path
import json
values=[F(0),F(1,10),F(1,3),F(1,2),F(2,3),F(9,10),F(99,100)]
count=0
examples=[]
for aa in product(values,repeat=3):
    alpha=sum(aa)
    if not 1<alpha<2:
        continue
    for fraction in [F(1,10),F(1,2),F(9,10)]:
        theta=(2-alpha)*fraction
        lo=[max(F(0),(a-1+theta)/theta) for a in aa]
        hi=[min(F(1),a/theta) for a in aa]
        assert sum(lo)<1<sum(hi)
        lam=(1-sum(lo))/(sum(hi)-sum(lo))
        bb=[l+lam*(u-l) for l,u in zip(lo,hi)]
        cc=[(a-theta*b)/(1-theta) for a,b in zip(aa,bb)]
        beta=(alpha-theta)/(1-theta)
        assert sum(bb)==1 and sum(cc)==beta and 1<beta<2
        for a,b,c in zip(aa,bb,cc):
            assert a==theta*b+(1-theta)*c
            assert (b==c==0) if a==0 else (0<b<1 and 0<c<1)
        count+=1
        if aa in [(F(9,10),F(2,3),F(0)),(F(99,100),F(99,100),F(0))] and fraction==F(1,2):
            examples.append({'a':list(map(str,aa)),'theta':str(theta),'b':list(map(str,bb)),'c':list(map(str,cc)),'beta':str(beta)})
out={'status':'finite exact rational screening; not proof, review or Lean','ordered_parameter_cases':count,'grid':list(map(str,values)),'theta_fractions':['1/10','1/2','9/10'],'all_assertions_pass':True,'examples':examples}
Path(__file__).with_name('root-feasibility.json').write_text(json.dumps(out,indent=2)+'\n')
print(count,'rational endpoint cases PASS')
