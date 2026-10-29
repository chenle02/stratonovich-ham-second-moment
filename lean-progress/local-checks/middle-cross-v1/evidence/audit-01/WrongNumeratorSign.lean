module
public import StratonovichHAMAudit.MiddleCross
open StratonovichHAMAudit.MiddleCross
example : numerator (4/3) (9/4) (29/12) (5/3) ≤ 0 := by norm_num [numerator]
