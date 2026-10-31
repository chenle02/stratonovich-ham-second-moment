module
public import StratonovichHAMAudit.PositiveGram
open scoped BigOperators
example : 2 * (1 : ℝ) * Real.sqrt (-2) - (0 : ℝ)^2 / 2 ≤
    (1 : ℝ)^2 / 1 - 2 * 1 + (1 : ℝ)^2 / 2 := by
  norm_num
