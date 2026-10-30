#!/usr/bin/env python3
"""Unreviewed scalar-row diagnostics, actual d1 measures; no operator claim."""
import mpmath as m,json
from pathlib import Path
m.mp.dps=30
rows=[]
a=m.mpf('0.5');g=m.mpf('0.2')
br=lambda x:m.sqrt(1+x*x)
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
   nodes=sorted(set([m.mpf(0),m.mpf(1),max(m.mpf(0),q-1),q,q+1,1/h,4*max(1,q)]))+[m.inf]
   v=m.quad(f,nodes)
   b=1 if alpha<1 else 1+m.log(1/h)
   assert v>0 and m.isfinite(v)
   rows.append({'d':1,'alpha':aa,'a':'0.5','gamma':'0.2','xi':qq,'h':hh,'measure':'|lambda|^(alpha-1) dlambda (d1 Riesz / white up to positive covariance amplitude)','weighted_row':m.nstr(v,22),'B_alpha':m.nstr(b,22),'ratio':m.nstr(v/b,22)})
Path(__file__).with_name('diagnostics-v1.json').write_text(json.dumps({'status':'UNREVIEWED finite diagnostic only','precision':30,'rows':rows,'scope':'12 actual d1 Riesz/white nonzero- and zero-frequency calibrations; no all-xi proof or operator variance identification'},indent=2)+'\n')
print('12 scalar frequency controls computed; no uniform bound proved.')
