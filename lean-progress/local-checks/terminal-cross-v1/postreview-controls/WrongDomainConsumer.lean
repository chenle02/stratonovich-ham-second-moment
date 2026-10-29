module
public import StratonovichHAMAudit.TerminalCross
open StratonovichHAMAudit.TerminalCross
example : numP 1 / (16*(1:ℝ)^3*(1+1)*Real.sqrt ((1:ℝ)^2+((1:ℝ)^2-1)/(1^2+1))) <
    numN 1 1 / (32*(1:ℝ)^3*(1+1-1)*(1+1)) := by
  norm_num [numP, numN]
