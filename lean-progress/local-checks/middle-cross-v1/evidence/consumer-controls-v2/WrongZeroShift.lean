module
public import StratonovichHAMAudit.MiddleCross
set_option autoImplicit false
example : StratonovichHAMAudit.MiddleCross.resolvent 1 (11/10) 1 ≤ StratonovichHAMAudit.MiddleCross.actual 1 (11/10) := by norm_num [StratonovichHAMAudit.MiddleCross.resolvent, StratonovichHAMAudit.MiddleCross.actual]
