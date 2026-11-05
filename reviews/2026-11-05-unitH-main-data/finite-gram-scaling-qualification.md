# Finite Gram covariance scaling: required qualification

This is an AUTHOR finite-algebra/source-normalization diagnostic. It identifies an overbroad prospective TASK statement, not a defect in the manuscript or a new SPDE theorem. Root independently checked and upheld the finding. Originals remain unchanged.

## The actual finite problem

For real Hilbert labels k_i, ell_i>0, b_i>=0 and nonnegative PSD Gram C_ij=<k_i,k_j>, write

V(C,b)=sup_Phi { 2 sum_i ell_i sqrt((<Phi,k_i>−b_i)_+) − ||Phi||²/2 }.

Realization independence is source197; zero/empty/singular cases are retained. No covariance inverse is needed for the following calculation.

For c>0 choose labels k_i'=sqrt(c)k_i and the bijection Phi'=c^(1/6)Phi. Then

<Phi',k_i'>=c^(2/3)<Phi,k_i>,
||Phi'||²=c^(1/3)||Phi||².

If thresholds are ALSO b_i'=c^(2/3)b_i, every positive-part root is multiplied by c^(1/3). Thus the ENTIRE objective is multiplied by c^(1/3), and taking suprema over the bijection gives

V(cC,c^(2/3)b)=c^(1/3)V(C,b),
V(cC,b)=c^(1/3)V(C,c^(−2/3)b).

Therefore V(cC,0)=c^(1/3)V(C,0). The unqualified V(cC,b)=c^(1/3)V(C,b) is false for general fixed b>=0. At c=0 all labels vanish and V(0,b)=0 directly for b>=0; no inverse scale or negative-power formula at zero is used.

## Exact existing-source countercontrol

Take one label with C=1 (k=1), ell=1/10 and b=4. If phi<=4, the objective is −phi²/2<=0. If phi>4, set y=phi−4>0. Since sqrt(y)<= (y+1)/2,

(1/5)sqrt(y) − (y+4)²/2
<= −y²/2 −39y/10 −79/10 <0.

The empty/origin branch gives V(1,4)=0.

Now scale only the covariance to C'=256, so k'=16, keeping the SAME threshold4 and ell1/10. At phi=1 the score is

(1/5)sqrt(16−4) −1/2 = 2sqrt(3)/5 −1/2 >0,

because sqrt(3)>5/4 (3>25/16). Hence V(256,4)>0, whereas 256^(1/3)V(1,4)=0. This is a finite Gaussian-label countercontrol under the source's broad abstract hypotheses, not an original SPDE covariance counterexample.

The reference ell=1/10,b=4,C=1 already appears in source R:gram-controls/S225, whose dual D(4)=−3199/400 is a TEST VALUE, not the dual infimum. The countercontrol here does not assert an incorrect optimizer or use that test value as an infimum.

## Compatibility with physical covariance/kinetic scaling

For the physical L2-unit spatial profiles f_i,r(x)=r^(d/2)f_i(rx), the threshold is b_i,r=r²b_i and the raw physical Gram at covariance amplitude s>0 is C'=s r^alpha C. Taking r=s^(1/(3−alpha)) gives s r^alpha=r³. The JOINT finite law therefore yields

V(r³C,r²b)=r V(C,b).

This is consistent with the original C2 covariance-amplitude power s^(1/(3−alpha)); it does not prove that SPDE theorem by itself. The actual full positive-test source dilation and same-object moment arguments remain their authority. Threshold/kinetic scaling cannot be ignored, and changing a single fixed test's amplitude does not remove its gradient penalty.

## Exact original H DATA locations needing the qualifier

- scoped-assignment.txt LF17: “finite-Gram covariancec^(1/3)” in the constants paragraph.
- scoped-assignment.txt LF69 / mandatory Root precision12: “finite-Gram covariance has c^(1/3).”
- Root-selection.json /task_precision_clauses/11 contains the latter phrase.

The agent has no such claim. Original source194–198 does not assert the false general fixed-threshold law. A superseding task should explicitly retain the c>0 joint-threshold identities, the zero-threshold special case and c=0 direct branch, with the complete derivation and countercontrol. No paper source repair, silent raw-document change or confidence/grade conversion is indicated.
