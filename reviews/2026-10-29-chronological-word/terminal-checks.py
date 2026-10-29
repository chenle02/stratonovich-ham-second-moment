"""Exact bounded-Gaussian terminal-kernel calibration,not a proof certificate."""
from fractions import Fraction
from math import factorial
import json
def pairings(k):
 return factorial(2*k)//(2**k*factorial(k))
rows=[]
for k,expected in [(1,Fraction(1,3)),(2,Fraction(1,105))]:
 splits=[Fraction(pairings(k),factorial(2*m)*factorial(2*(2*k-m))) for m in range(2*k+1)]
 value=sum(splits,Fraction(0));assert value==expected
 rows.append({"variance_order":k,"split_moments":[str(x) for x in splits],"sum":str(value),"cosh_squared_coefficient":str(expected)})
assert Fraction(1,factorial(2))**2==Fraction(1,4)
assert Fraction(1,factorial(4))==Fraction(1,24)
print(json.dumps({"status":"PASS","scope":"One centered Gaussian constant potential,not an H:homog covariance;tests terminal mass,all unequal-chain splits and absence of extra symmetrization factors","checks":rows},indent=2))
