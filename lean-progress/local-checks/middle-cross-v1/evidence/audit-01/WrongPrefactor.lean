module
public import StratonovichHAMAudit.MiddleCross
open StratonovichHAMAudit.MiddleCross
example : 2*upper (4/3) (9/4) (29/12) (5/3) < actual (4/3) (9/4) := by
  norm_num [upper,resolvent,massK,part1,part2,actual]
