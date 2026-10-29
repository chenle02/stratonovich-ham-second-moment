module
public import StratonovichHAMAudit.MiddleCross
set_option autoImplicit false
example : 2*StratonovichHAMAudit.MiddleCross.upper (4/3) (9/4) (29/12) (5/3) < StratonovichHAMAudit.MiddleCross.actual (4/3) (9/4) := by
  norm_num [StratonovichHAMAudit.MiddleCross.upper,StratonovichHAMAudit.MiddleCross.resolvent,StratonovichHAMAudit.MiddleCross.massK,StratonovichHAMAudit.MiddleCross.part1,StratonovichHAMAudit.MiddleCross.part2,StratonovichHAMAudit.MiddleCross.actual]
