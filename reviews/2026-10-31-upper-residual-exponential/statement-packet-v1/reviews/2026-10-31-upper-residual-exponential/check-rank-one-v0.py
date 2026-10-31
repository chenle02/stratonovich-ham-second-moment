from pathlib import Path
import json,mpmath as m

def compute(digits):
 m.mp.dps=digits;rows=[]
 for ns in ['1','1.5','1.8']:
  n=m.mpf(ns)
  for es in ['0.5','1']:
   e=m.mpf(es);A=e**n;star=(n*A)**(1/(2-n));S=(2-n)/2*n**(n/(2-n))*A**(2/(2-n))
   for ds in ['0.1','0.03','0.01']:
    d=m.mpf(ds);width=4*m.sqrt(d/(2-n));pts=sorted(set([m.mpf(0),max(m.mpf(0),star-width),star,star+width]));pts.append(m.inf)
    I=m.quad(lambda x:m.exp((A*x**n-x*x/2-S)/d),pts)
    logM=m.log(2/m.sqrt(2*m.pi*d))+S/d+m.log(I)
    if n==1:
     exact=m.log(2)+A*A/(2*d)+m.log(m.erfc(-A/m.sqrt(2*d))/2)
     assert abs(logM-exact)<m.mpf('1e-25')
    rows.append({'nu':ns,'epsilon':es,'delta':ds,'delta_log_moment':m.nstr(d*logM,32),'saddle_rate':m.nstr(S,32)})
 return rows
r40=compute(40);r60=compute(60)
for a,b in zip(r40,r60):assert abs(m.mpf(a['delta_log_moment'])-m.mpf(b['delta_log_moment']))<m.mpf('1e-25')
Path(__file__).with_name('rank-one-v0.json').write_text(json.dumps({'status':'FLOATING SCALAR CONSISTENCY ONLY','rows':r60,'working_digits':[40,60],'model':'Y=sqrt(delta)*epsilon*|G|,eta1; no operator, Ctheta, projection, solution or original noise moment evaluated','scope':'Stable saddle-subtracted integration over0..infinity; nu1 closed-form Gaussian calibration. No certified quadrature/tail/roundoff enclosure or general theorem. nu2 and beyond divergence guards are analytic, not integrated numerically.'},indent=2)+'\n')
print('18 rank-one Gaussian norm controls at40/60digits and nu1 exact calibrations pass; no upper theorem.')
