import mpmath as mp,json
mp.mp.dps=35
rows=[]
for alpha in [mp.mpf('0.1'),mp.mpf('0.5'),mp.mpf('1')]:
 for a in [mp.mpf('0.1'),mp.mpf('0.5'),mp.mpf('0.9')]:
  q=4-alpha;d=q-2*a;k=3-alpha
  def star(u):return (d/u)**(a/2)*mp.exp(d*u/4)*mp.pcfd(-a,mp.sqrt(d*u))
  row_pcfd=2*mp.quad(star,[0,mp.mpf('0.5')])
  def integrand(z):
   if z==0:return mp.mpf('0.5')
   lam=z**(1/a);w=lam+lam**2/(2*d)
   return -mp.expm1(-w/2)/w
  row_direct=2/mp.gamma(1+a)*mp.quad(integrand,[0,1,mp.inf])
  assert mp.almosteq(row_pcfd,row_direct,rel_eps=mp.mpf('1e-15'))
  capacity_candidate=mp.gamma(1+a)*mp.gamma((1-a)/2)/mp.gamma((1+a)/2)
  gap=(q*mp.log(q)+(q-2*a)*mp.log(q-2*a))/2-(q-a)*mp.log(q-a)
  margin=mp.log(capacity_candidate)-mp.log(row_direct)-gap
  rows.append({'alpha':str(alpha),'a':str(a),'star_row_pcfd':mp.nstr(row_pcfd,25),'star_row_direct_laplace':mp.nstr(row_direct,25),'candidate_temporal_capacity':mp.nstr(capacity_candidate,25),'map_log_gap':mp.nstr(gap,25),'candidate_log_margin':mp.nstr(margin,25),'positive':bool(margin>0)})
print(json.dumps({'scope':'UNREVIEWED numerical reconnaissance only. Candidate temporal capacity identity and all functional/spectral comparisons unproved. Two independent source-kernel quadratures agree; no source lower/no-go theorem.','precision_decimal_digits':35,'rows':rows},indent=2))
