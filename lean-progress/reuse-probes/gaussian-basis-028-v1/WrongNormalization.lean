import GaussianChaos.ChaosDensity
set_option autoImplicit false
open scoped InnerProductSpace

example : ⟪GaussianChaos.ChaosDensity.hermiteNormalized (Finsupp.single (0 : Fin 2) 1),
    GaussianChaos.ChaosDensity.hermiteNormalized (Finsupp.single (0 : Fin 2) 1)⟫_ℝ = 2 := by
  classical
  have h := orthonormal_iff_ite.mp
    (GaussianChaos.ChaosDensity.orthonormal_hermite (ι := Fin 2))
  have hn : ⟪GaussianChaos.ChaosDensity.hermiteNormalized (Finsupp.single (0 : Fin 2) 1),
      GaussianChaos.ChaosDensity.hermiteNormalized (Finsupp.single (0 : Fin 2) 1)⟫_ℝ = 1 := by
    simpa using h (Finsupp.single (0 : Fin 2) 1) (Finsupp.single (0 : Fin 2) 1)
  rw [hn]
  norm_num
