module
public import StratonovichHAMAudit.MiddleCross
set_option autoImplicit false
example : StratonovichHAMAudit.MiddleCross.upper (4/3) 1 (Real.sqrt (((4:ℝ)/3)^2+1^2-1)) (Real.sqrt (((4:ℝ)/3)^2+1)) < StratonovichHAMAudit.MiddleCross.actual (4/3) 1 := by
  have hd : ((4:ℝ)/3)^2+1^2-1 = ((4:ℝ)/3)^2 := by norm_num
  have he : ((4:ℝ)/3)^2+1 = ((5:ℝ)/3)^2 := by norm_num
  rw [hd,he]
  norm_num [Real.sqrt_sq_eq_abs,StratonovichHAMAudit.MiddleCross.upper,StratonovichHAMAudit.MiddleCross.resolvent,StratonovichHAMAudit.MiddleCross.massK,StratonovichHAMAudit.MiddleCross.part1,StratonovichHAMAudit.MiddleCross.part2,StratonovichHAMAudit.MiddleCross.actual]
