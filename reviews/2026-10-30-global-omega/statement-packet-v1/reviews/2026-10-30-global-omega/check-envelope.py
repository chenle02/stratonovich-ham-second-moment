import mpmath as m,json
from pathlib import Path
m.mp.dps=60
rows=[]
for aa in ['0.001','0.01','0.1','0.25','0.5','0.75','0.9','0.99']:
 a=m.mpf(aa);x=a/2;d=4-2*a
 B=sum((-1)**j*m.gamma((a+j)/2)/m.gamma(a)*2**a*d**((a+j)/2)/(m.factorial(j)*(j+2-a)) for j in range(5))
 cap=m.gamma(1+a)*m.gamma((1-a)/2)/m.gamma((1+a)/2)
 E=1/(2*(1-x))+x*(1-x)/(2-x)+x*(x+1)*(1-x)**2/(3*(3-x))
 C=1/(3-2*x)+(2*x+1)*(1-x)/(3*(5-2*x));g=1-m.mpf(3)/5*x;L=m.mpf(177)/100*(1-m.mpf(7)/5*x)
 V=2*(1-x*x+x**4/2)*(1-4*x*x)/g*(E-2*g*C*x*L)*(3-4*x)/(3-4*x-2*x*x)
 Delta=(3*m.log(3)+(3-2*a)*m.log(3-2*a))/2-(3-a)*m.log(3-a)
 ratio=B*m.exp(Delta)/cap
 G=2*m.pi*(1-x)**x/(m.gamma(m.mpf('.5')+x)*m.gamma(m.mpf('.5')-x)*m.gamma(1+x))*(E-2*m.sqrt(1-x)*C*x*m.gamma(m.mpf('.5')+x)/m.gamma(1+x))
 assert m.almosteq(G,B/cap,rel_eps=m.mpf('1e-50'))
 assert m.gamma(1+x)>=g
 assert m.gamma(m.mpf('.5')+x)/m.gamma(1+x)>=L
 assert m.gamma(m.mpf('.5')+x)*m.gamma(m.mpf('.5')-x)>=m.pi/(1-4*x*x)
 assert (1-x)**x<=1-x*x+x**4/2
 assert Delta<=2*x*x/(3-4*x)
 assert 0<ratio<=V<1
 rows.append({'a':aa,'actual_G4_ratio':m.nstr(ratio,40),'rational_envelope':m.nstr(V,40),'one_minus_envelope':m.nstr(1-V,40)})
out={'scope':'Eight60digit scalar controls only, no global analytic inequality or SPDE proof','all_assertions_passed':True,'rows':rows}
Path(__file__).with_name('envelope-diagnostics-v1.json').write_text(json.dumps(out,indent=2)+'\n')
print('Eight scalar controls PASS; each ratio<=candidate rational envelope<1.')
