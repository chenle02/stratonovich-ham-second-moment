module
public import StratonovichHAMAudit.PositiveGram
open scoped BigOperators
example : 2 * (1 : ℝ) * Real.sqrt 1 - (1 : ℝ)^2 / 2 ≤
    (1 : ℝ)^2 / 1 - 0 + (1 : ℝ)^2 / 4 := by
  norm_num
