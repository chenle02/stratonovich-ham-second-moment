module
public import StratonovichHAMAudit.ClockFilter
open MeasureTheory
example : (∫ x : ℝ, (2 / (2 + x) : ℝ) ∂(0 : Measure ℝ)) < ∫ x : ℝ, (1 : ℝ) ∂(0 : Measure ℝ) := by simp
