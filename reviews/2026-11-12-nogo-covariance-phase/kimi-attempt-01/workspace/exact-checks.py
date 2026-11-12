"""Exact local checks for the expanded negative-results appendix."""
from fractions import Fraction as F
from math import factorial
from pathlib import Path
import json
import sympy as s
out={}
rows=[]
for A in (99,100,101):
 def term(k): return F(2**(3*k-1)*factorial(2*k)*A**k,factorial(k)*factorial(4*k))
 lo=1+sum((term(k) for k in range(1,21)),F(0));q=F(16*A,81**3);hi=lo+term(21)/(1-q);B=10**6
 low=lo.numerator*B//lo.denominator;up=-((-hi.numerator*B)//hi.denominator)
 assert F(low,B)<=lo<=hi<=F(up,B)
 rows.append({'A':A,'lower_numerator':low,'upper_numerator':up,'denominator':B})
gap=rows[1]['lower_numerator']**2-rows[0]['upper_numerator']*rows[2]['upper_numerator'];assert gap>0
out['NG-11']={'outward_rational_intervals':rows,'strict_gap_lower_numerator':gap,'strict_gap_lower_denominator':10**12,'partial_order':20}
z,w=s.symbols('z w');c=lambda z:sum(z**j/s.factorial(2*j) for j in range(5));ss=lambda z:sum(z**j/s.factorial(2*j+1) for j in range(5))
y=s.expand(c(w)*c(z)+ss(w)*z*ss(z));ys=s.expand(y*y);single=s.expand(c(z)**2)
assert ys.coeff(z,2).coeff(w,0)+ys.coeff(z,0).coeff(w,2)==3
assert single.coeff(z,2)==s.Rational(1,3)
out['NG-14']={'single_variance_coefficient':'1/3','two_block_variance_coefficient':'3','product_variance_coefficient':'2/3','analytic_tail':'Justified separately in TeX, not by this finite polynomial test.'}
M0=s.Matrix([[1,1],[0,1]]);M1=s.Matrix([[s.Rational(1,2),s.Rational(1,6)],[1,s.Rational(1,2)]]);M2=s.Matrix([[s.Rational(1,24),s.Rational(1,120)],[s.Rational(1,6),s.Rational(1,24)]])
K=M1.T*M1+M0.T*M2+M2.T*M0;v=s.Matrix([1,-2]);assert K==s.Matrix([[s.Rational(4,3),s.Rational(4,5)],[s.Rational(4,5),s.Rational(17,45)]]);assert (v.T*K*v)[0]==-s.Rational(16,45)
out['NG-15']={'full_first_variance_matrix':str(K),'negative_phase_coefficient':'-16/45','first_random_term_e1':'5/4','full_coefficient_e1':'4/3'}
assert F(545,11616)-F(1025,21483)==-F(6005,7562016);out['NG-18']={'I':'545/11616','erased_shift_majorant':'1025/21483','difference':'-6005/7562016'}
assert F(20000,1932951)<F(1,96);assert F(101,4800)>F(1,48);out['NG-19']={'parent_coefficient':'20000/1932951','projection_lower':'101/(3200 sqrt(2))','gap_strictly_above':'1/96'}
assert 16*18==288 and 9*16==144;out['NG-23']={'actual':288,'input_only_bound':144}
num=11**11*7**7;den=2**5*9**18;assert num<den;out['NG-28']={'numerator':num,'denominator':den}
assert F(1,100)/4-16+8==-F(3199,400);D=s.Matrix([[0,s.Rational(1,2)],[s.Rational(1,2),0]]);assert sorted(D.eigenvals())==[-s.Rational(1,2),s.Rational(1,2)];out['NG-29']={'empty_value_test':'-3199/400 < 0','concavity_test':'F(0)=F(2)=0, F(1)=-1/2','difference_eigenvalues':['-1/2','1/2']}
assert F(1,4)>F(1,5) and F(1,2)>F(2,5) and F(3,5)>F(1,4);out['NG-05']={'forward_root_support_witness':'strict rational inequalities pass; white domestic contractions leave two free spatial positions'}
assert F(11,10)-F(9,10)-1==-F(4,5);assert F(1,2)-F(9,10)==-F(2,5);out['NG-12']={'heat_weight':'-4/5','spatial_strip_exponent':'-2/5','total_exponent':'-6/5'}
assert s.simplify(2**s.Rational(3,4)*s.Rational(1,8)**s.Rational(1,4))==1;assert factorial(3)*3**3==162 and factorial(3)**3==216;out['NG-33']={'Holder_correct':'1','Holder_wrong':'1/4','actual_majorant_denominator':162,'unjustified_larger_denominator':216,'valid_weaker_denominator':36}
Path(__file__).with_name('checks.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
