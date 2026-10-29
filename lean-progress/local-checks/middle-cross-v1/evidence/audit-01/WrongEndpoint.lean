module
public import StratonovichHAMAudit.MiddleCross
open StratonovichHAMAudit.MiddleCross
example : upper (4/3) 1 (Real.sqrt (((4:ℝ)/3)^2+1^2-1)) (Real.sqrt (((4:ℝ)/3)^2+1)) < actual (4/3) 1 := by
  have hd : ((4:ℝ)/3)^2+1^2-1 = ((4:ℝ)/3)^2 := by norm_num
  have he : ((4:ℝ)/3)^2+1 = ((5:ℝ)/3)^2 := by norm_num
  rw [hd,he]
  norm_num [Real.sqrt_sq_eq_abs,upper,resolvent,massK,part1,part2,actual]
