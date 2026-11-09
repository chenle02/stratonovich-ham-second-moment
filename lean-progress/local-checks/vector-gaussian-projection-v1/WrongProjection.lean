import VectorProjection

set_option autoImplicit false
open StratonovichHAMAudit.VectorProjection GaussianChaos.ChaosDensity

-- Deliberately wrong: a projection that selects no modes cannot retain a nonzero first mode.
example :
    (cutoffSpace (E := ℝ) (fun _ : Fin 2 →₀ ℕ => False)).toSubmodule.starProjection
      (hermiteNormalized (Finsupp.single (0 : Fin 2) 1)) =
        hermiteNormalized (Finsupp.single (0 : Fin 2) 1) := by
  classical
  have hb := (orthonormal_hermite (ι := Fin 2)).ne_zero (Finsupp.single (0 : Fin 2) 1)
  have hbot : (cutoffSpace (E := ℝ) (fun _ : Fin 2 →₀ ℕ => False)).toSubmodule = ⊥ := by
    change (Submodule.span ℝ {z : MeasureTheory.Lp ℝ 2 (GaussianChaos.GaussianProduct.noise (Fin 2)) |
      ∃ (ν : Fin 2 →₀ ℕ) (x : ℝ), False ∧ z = atom ν x}).topologicalClosure = ⊥
    simp only [false_and, exists_false, Set.setOf_false, Submodule.span_empty]
    exact IsClosed.submodule_topologicalClosure_eq isClosed_singleton
  simp [hbot, hb, eq_comm]
