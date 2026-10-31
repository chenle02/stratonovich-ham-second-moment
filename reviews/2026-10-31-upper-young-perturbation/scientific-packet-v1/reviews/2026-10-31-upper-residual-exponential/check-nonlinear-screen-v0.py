"""Exact scalar diagnostics for the NEXT screen, not an operator theorem."""
from fractions import Fraction as F
import json
rows=[]
# theta=2/3, nu=3/2, B=1; D(t)=x*t, ||D||Ctheta=2*x,
# exact log U(1)=x. Refute logU <= C*||D||**nu by squaring.
for c in (1,2,10,100):
    x=F(1,16*c*c)
    lhs_squared=x*x
    claimed_rhs_squared=c*c*(2*x)**3
    assert lhs_squared>claimed_rhs_squared
    rows.append({'C':c,'x':str(x),'logU_squared':str(lhs_squared),
                 'claimed_rhs_squared':str(claimed_rhs_squared),
                 'pure_nu_bound_refuted':True})
rare=[]
# r=4, nu=3/2, amplitude=L^2, exactly L^8 blocks, one nonzero.
for L in (2,4,8,16):
    amplitude=L*L; delta=F(1,L**8)
    budget=delta*amplitude**4
    cost=delta*L**3
    assert budget==1 and cost==F(1,L**5)
    rare.append({'L':L,'number_of_blocks':L**8,'delta':str(delta),
                 'max_amplitude':amplitude,'averaged_r4_budget':str(budget),
                 'averaged_nu_3_over_2_cost':str(cost)})
print(json.dumps({'scope':'exact deterministic scalar controls only; no Gaussian/operator/CM-realizability/SPDE assertion',
                  'pure_nu_rows':rows,'rare_block_rows':rare},indent=2))
