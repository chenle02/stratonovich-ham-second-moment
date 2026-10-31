module
public import StratonovichHAMAudit.PositiveGram
open scoped BigOperators
example : (1 / 2 : ℝ) *
    (∑ i : Fin 2, ∑ j : Fin 2,
      (if i = 0 then 1 else -1) * (if i = j then 1 else 0) *
        (if j = 0 then 1 else -1)) ≤
    (1 / 2 : ℝ) * (∑ i : Fin 2, ∑ j : Fin 2,
      (if i = 0 then 1 else -1) * (if i = j then 1 else 1 / 2) *
        (if j = 0 then 1 else -1)) := by
  norm_num [Fin.sum_univ_two]
