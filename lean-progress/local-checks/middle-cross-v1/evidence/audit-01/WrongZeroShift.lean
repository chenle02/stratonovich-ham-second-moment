module
public import StratonovichHAMAudit.MiddleCross
open StratonovichHAMAudit.MiddleCross
example : resolvent 1 (11/10) 1 ≤ actual 1 (11/10) := by norm_num [resolvent, actual]
