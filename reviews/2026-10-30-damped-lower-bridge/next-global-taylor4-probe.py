import mpmath as mp,json
mp.mp.dps=50
rows=[]
for text in ['0.001','0.01','0.1','0.25','0.5','0.75','0.9','0.99']:
 a=mp.mpf(text);d=4-2*a;qgap=mp.mpf(3)
 terms=[(-1)**j*mp.gamma((a+j)/2)/mp.gamma(a)*2**a*d**((a+j)/2)/(mp.factorial(j)*(j+2-a)) for j in range(5)]
 B4=sum(terms);assert B4>0
 Ceff=mp.gamma(1+a)*mp.gamma((1-a)/2)/mp.gamma((1+a)/2)
 Delta=(qgap*mp.log(qgap)+(qgap-2*a)*mp.log(qgap-2*a))/2-(qgap-a)*mp.log(qgap-a)
 margin=mp.log(Ceff/B4)-Delta
 rows.append({'a':text,'d_envelope':mp.nstr(d,25),'B4':mp.nstr(B4,35),'capacity':mp.nstr(Ceff,35),'Delta_q3':mp.nstr(Delta,35),'log_margin':mp.nstr(margin,35),'positive':bool(margin>0),'terms':[mp.nstr(t,35) for t in terms]})
 assert margin>0
print(json.dumps({'scope':'UNREVIEWED eight-point reconnaissance of a sufficient one-variable Gamma inequality; not a global proof. q=4 is an envelope, not an alpha=0 SPDE model.','precision_decimal_digits':50,'all_sampled_margins_positive':True,'rows':rows},indent=2))
