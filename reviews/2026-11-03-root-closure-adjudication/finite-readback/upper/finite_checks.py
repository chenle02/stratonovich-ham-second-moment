from fractions import Fraction as F
from math import factorial,pi,sin
import json
from pathlib import Path
O=Path(__file__).parent
# Independent Dirichlet and layer-cake integration of the three pairings in
# E[Y_4] for d1 static white covariance c delta0 at T=1.
# Five time gaps sum to1 (four free variables); product c*e/4 gives 1/(4*6!).
a=F(1,4*factorial(6))
# Three (resp. two) gaps constrained >=u. Integral e over residual simplex is
# (1-m*u)^5/5!; integrating u gives 1/(m*6*5!).
b=F(1,4*3*6*factorial(5));c=F(1,4*2*6*factorial(5))
assert (a,b,c)==(F(1,2880),F(1,8640),F(1,5760))
assert a+b+c==F(11,17280)
# Constant-in-space/time one-dimensional Gaussian noise: u=sum Z^n T^(2n)/(2n)!.
# Diagnostic finite model only (alpha=0 excluded from original model).
def moment_coeff(total):
 gaussian=1
 for j in range(1,total,2):gaussian*=j
 return gaussian*sum((F(1,factorial(m*2)*factorial((total-m)*2)) for m in range(total+1)),F(0))
assert moment_coeff(2)==F(1,3);assert moment_coeff(4)==F(1,105)
# d1white finite interval I=[0,h], alpha=1, a=1/2, T=1, covariance amplitude1.
# Exact first response variance = h²/2-h³/3; fresh-color bound=R*T*h²=h²/2.
intervals=[]
for h in [F(1,128),F(1,4),F(1),F(8)]:
 effective=min(h,F(1));amp2=float(h)**(-.5)
 exact=amp2*float(effective**2/F(2)-effective**3/F(3))
 bound=amp2*float(h*h/F(2))
 assert exact<=bound*(1+1e-14)
 intervals.append({'h':str(h),'exact_variance':exact,'fresh_color_upper':bound,'ratio':exact/bound})
# K0 with H0=8 and all three shifted grids contains s=1/8,r=3/8
# in all three intervals. It already exceeds the original kernel at a=1/2.
k0=3*(6/8)**.5;original=(F(3,8)-F(1,8))**F(-1,2)
assert k0>float(original)
# PSD kernels A=I and B=all-ones satisfy entrywise A<=B but B-A has eigenvalue-1.
psd_counterexample={'A':[[1,0],[0,1]],'B':[[1,1],[1,1]],'B_minus_A_eigenvalues':[-1,1],'test_vector':[1,-1],'quadratic_difference':-2}
# Dyadic inventory cardinality check through depth12, including touching endpoints.
counts=[]
H0=F(8)
for J in range(13):
 count=0
 for j in range(J+1):
  h=H0/F(2**j)
  for t in [F(0),F(1,3),F(2,3)]:
   shift=(-1)**j*t
   # Conservative endpoint-inclusive enumeration.
   for n in range(-2,2**j+3):
    lo=h*(n+shift);hi=lo+h
    if lo<=1 and hi>=0:count+=1
 upper=F(78)/h
 assert count<=upper,(J,count,upper)
 counts.append({'depth':J,'intervals_meeting_[0,1]':count,'last_length':str(h),'inventory_upper':str(upper)})
# Parametric fine-scale exponents, alpha=7/5,a=2/5: one mean-metric power works;
# replacing it by two would make the dyadic sum divergent.
alpha=F(7,5);time=F(2,5);beta=4-alpha-time
assert beta-2==F(1,5)>0 and beta-3==F(-4,5)<0
# The three Wick pairings in E[Y2²] for d1staticwhite, T=1.
# In the swapped-cross pairing, integrate the two rectangle radii first.
# The resulting five polynomial integrals on 0<=e<=b<=1 are elementary.
I0=F(1,12)-F(1,30)+F(1,180)
I1=F(1,10)*(F(2**6-1,6)-F(2**6,18))
I2A=F(1,5)*(F(1,6)-F(1,12))
I2B=F(1,10)-F(1,120)
I3=F(1,60)
swapped=(I0-I1/12+(I2A+I2B)/6-I3/12)/8
EY2sq=F(1,144)+F(1,480)+swapped
assert swapped==F(31,17280) and EY2sq==F(187,17280)
out={'scope':'Finite algebra/normalization falsification controls; not an all-order proof or independent review','white_static_EY4_pairings':{'12|34':str(a),'13|24':str(b),'14|23':str(c),'sum':str(a+b+c),'meaning':'E[Y4]=c² T6 * sum'},'white_static_EY2_squared':{'self_self':'1/144','parallel_cross':'1/480','swapped_cross':str(swapped),'sum':str(EY2sq),'polynomial_integrals':list(map(str,[I0,I1,I2A,I2B,I3]))},'white_static_total2':{'EY1_squared':'c*T³/6','EY2':'c*T³/12','B1':'c*T³/3'},'constant_Gaussian_total2':str(moment_coeff(2)),'constant_Gaussian_total4':str(moment_coeff(4)),'interval_checks':intervals,'K0_vs_original':{'a':.5,'H0':8,'s':.125,'r':.375,'K0':k0,'original':float(original)},'PSD_order_counterexample':psd_counterexample,'inventory_counts':counts,'metric_power_control':{'alpha':str(alpha),'a':str(time),'beta':str(beta),'correct_dyadic_exponent':str(beta-2),'incorrect_squared_mean_metric_exponent':str(beta-3)}}
(O/'finite-check-results.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({'all_checks_passed':True,'white_EY4':str(a+b+c),'white_total2':'c*T³/3','K0':k0,'original':float(original),'inventory_depths':13},indent=2))
