module
public import StratonovichHAMAudit.PositiveGram
open scoped BigOperators
example : 2 * (1 : ℝ) * Real.sqrt 1 ≤ (1 : ℝ)^2 / 0 + 0 * 1 := by
  norm_num
