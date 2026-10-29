module
public import StratonovichHAMAudit.TerminalCross
open StratonovichHAMAudit.TerminalCross
example : numP 7 / (4*(7:ℝ)^3*(7+1)*Real.sqrt ((1:ℝ)^2+((7:ℝ)^2-1)/(7^2+1))) <
    numN 1 7 / (32*(7:ℝ)^3*(1+7-1)*(1+1)) := by
  have hs : (1:ℝ)^2+((7:ℝ)^2-1)/(7^2+1) = ((7:ℝ)/5)^2 := by norm_num
  rw [hs, Real.sqrt_sq (by norm_num)]
  norm_num [numP, numN]
