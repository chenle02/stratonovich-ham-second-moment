module
public import StratonovichHAMAudit.MiddleCross
open StratonovichHAMAudit.MiddleCross
example : paramC 3 (((29:ℝ)/12+9/4)/(4/3-1)) = 9/4 := by norm_num [paramC,paramB]
