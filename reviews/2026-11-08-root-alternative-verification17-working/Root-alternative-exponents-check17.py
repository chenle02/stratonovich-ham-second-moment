import json
from sympy import symbols, simplify
alpha, a0, r, v = symbols("alpha a0 r vartheta")
delta=alpha-1
rp=r/(r-1)
theta=a0*rp
chi=(alpha-v)/(1-v)
b0=a0/v
checks={
 "higher_time_power_minus_beta": simplify(1+(2-delta*r)/r+(2-theta)/rp-(4-alpha-a0)),
 "higher_factorial_power_minus_q": simplify(1+(2-delta*r)/r+2/rp-1-(3-alpha)),
 "three_time_power_minus_beta": simplify(v*(3-b0)+(1-v)*(4-chi)-(4-alpha-a0)),
 "three_factorial_power_minus_q": simplify(2*v+(1-v)*(3-chi)-(3-alpha)),
 "control_omit_opening_time_factor": simplify((2-delta*r)/r+(2-theta)/rp-(4-alpha-a0)),
 "control_omit_pairing_factorial_numerator": simplify(1+(2-delta*r)/r+2/rp-(3-alpha)),
}
assert all(checks[k]==0 for k in list(checks)[:4])
assert checks["control_omit_opening_time_factor"]==-1
assert checks["control_omit_pairing_factorial_numerator"]==1
print(json.dumps({"status":"EXACT_SYMBOLIC_CHECK_PASS_NOT_LEAN_OR_REVIEW_GRADE","source_main_sha256":"516d6a650bdac7d3da68672f37836afd084b651c39553b43d5135d0512e39d14","source_labels":["P:higher-transfer","P:three-transfer"],"definitions":{"delta":"alpha-1","rprime":"r/(r-1)","theta":"alpha0*rprime","chi":"(alpha-vartheta)/(1-vartheta)","b0":"alpha0/vartheta"},"results":{k:str(w) for k,w in checks.items()},"analytic_proofs_and_admissibility_outside_CAS":True},indent=2))
