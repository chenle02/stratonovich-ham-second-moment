#!/usr/bin/env python3
"""Unreviewed subsequent scalar target: xi=0 radial calibration only."""
import mpmath as m,json
from pathlib import Path
m.mp.dps=40
rows=[]
for alpha0 in ['0.5','1','1.25']:
 alpha=m.mpf(alpha0);a=m.mpf('0.5')
 for n in [0,2,4,8,12]:
  h=m.mpf(2)**(-n)
  f=lambda r:2*r**(alpha-1)/m.sqrt(1+r*r)*(1+h*h*r*r)**((a-1)/2)
  val=m.quad(f,[0,1,1/h,m.inf])
  b=1 if alpha<1 else (1+m.log(1/h) if alpha==1 else h**(1-alpha))
  assert val>0
  rows.append({'alpha':alpha0,'a':'0.5','h_power_of_2':-n,'xi':'0','radial_integral':m.nstr(val,25),'predicted_scale':m.nstr(b,25),'ratio':m.nstr(val/b,25)})
out={'status':'UNREVIEWED numeric calibration only','scope':'xi=0 normalized radial mass alpha; not all xi, not operator variance, not path or moment theorem','precision':40,'rows':rows}
Path(__file__).with_name('next-scalar-row-diagnostics.json').write_text(json.dumps(out,indent=2)+'\n')
print('15 subsequent scalar xi=0 cases computed; no uniform estimate proved.')
