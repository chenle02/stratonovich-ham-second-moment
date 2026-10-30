#!/usr/bin/env python3
"""v2: explicit phase resonance and numerical precision comparison."""
import mpmath as m,json
from pathlib import Path

def compute(dps):
 m.mp.dps=dps;out=[]
 a=m.mpf('0.5');g=m.mpf('0.2');br=lambda x:m.sqrt(1+x*x)
 for aa in ['0.5','1']:
  alpha=m.mpf(aa)
  for qq in ['0','8','64']:
   q=m.mpf(qq)
   for hh in ['1','0.015625']:
    h=m.mpf(hh)
    def f(r):
     def k(eta):
      return (br(h*(q-abs(eta)))**(a-1)+br(h*(q+abs(eta)))**(a-1))/(br(q)*br(eta))
     return r**(alpha-1)*(k(q-r)+k(q+r))*br(q)**(2*g)
    nodes=sorted(set([m.mpf(0),m.mpf(1),max(m.mpf(0),q-1),q,q+1,1/h,4*max(1,q),max(m.mpf(0),2*q-1/h),2*q,2*q+1/h]))
    v=m.quad(f,nodes+[m.inf]);b=1 if alpha<1 else 1+m.log(1/h);C=2/alpha
    assert v>0 and m.isfinite(v)
    out.append({'d':1,'alpha':aa,'a':'0.5','gamma':'0.2','xi':qq,'h':hh,'measure':'|lambda|^(alpha-1) dlambda','ball_constant_C':m.nstr(C,8),'finite_nodes':[m.nstr(x,12) for x in nodes],'weighted_row':m.nstr(v,dps-5),'B_alpha':m.nstr(b,dps-5),'ratio_J_over_B':m.nstr(v/b,dps-5),'normalized_ratio_J_over_CB':m.nstr(v/(C*b),dps-5)})
 return out
lo=compute(30);hi=compute(50)
diffs=[]
for l,h in zip(lo,hi):
 diff=abs(m.mpf(l['weighted_row'])-m.mpf(h['weighted_row']))/m.mpf(h['weighted_row'])
 assert diff<m.mpf('1e-10')
 diffs.append(m.nstr(diff,18))
out={'status':'finite diagnostic; no uniform estimate or certified quadrature accuracy','working_precisions':[30,50],'comparison_relative_tolerance':'1e-10','relative_differences':diffs,'rows_30_digits':lo,'rows_50_digits':hi,'scope':'12 actual d1 Riesz/white full scalar rows; explicit phase-resonance lambda=2|xi| plus neighbors width1/h. No alpha>1 nonzero-xi or singular-measure controls.'}
Path(__file__).with_name('diagnostics-v2.json').write_text(json.dumps(out,indent=2)+'\n')
print('12 corrected resonance controls at30/50digits agree to1e-10; no certified quadrature accuracy or theorem claimed.')
