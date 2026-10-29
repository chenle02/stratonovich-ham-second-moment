module
public import StratonovichHAMAudit.MiddleCross
set_option autoImplicit false
example : StratonovichHAMAudit.MiddleCross.numerator (4/3) (9/4) (29/12) (5/3) ≤ 0 := by norm_num [StratonovichHAMAudit.MiddleCross.numerator]
