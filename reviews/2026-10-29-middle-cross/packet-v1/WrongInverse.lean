module
public import StratonovichHAMAudit.MiddleCross
set_option autoImplicit false
example : StratonovichHAMAudit.MiddleCross.paramC 3 (((29:ℝ)/12+9/4)/(4/3-1)) = 9/4 := by norm_num [StratonovichHAMAudit.MiddleCross.paramC,StratonovichHAMAudit.MiddleCross.paramB]
