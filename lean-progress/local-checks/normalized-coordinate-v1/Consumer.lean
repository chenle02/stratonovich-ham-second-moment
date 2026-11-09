import NormalizedCoordinate

set_option autoImplicit false
open GaussianChaos.WienerChaos
open StratonovichHAMAudit.NormalizedCoordinate

universe u

-- Exact frozen proposition assigned to the compiled theorem: no strengthened premises.
example : (∀ {Mode : Type u} [DecidableEq Mode]
    (ν : Mode →₀ ℕ) (j : Mode) (ω : Mode → ℝ),
    ω j * (GaussianChaos.WienerChaos.Hm ν ω /
      Real.sqrt (GaussianChaos.WienerChaos.mfact ν)) =
      Real.sqrt ((ν j : ℝ) + 1) *
        (GaussianChaos.WienerChaos.Hm (ν + Finsupp.single j 1) ω /
          Real.sqrt (GaussianChaos.WienerChaos.mfact (ν + Finsupp.single j 1))) +
      Real.sqrt (ν j : ℝ) *
        (GaussianChaos.WienerChaos.Hm (ν - Finsupp.single j 1) ω /
          Real.sqrt (GaussianChaos.WienerChaos.mfact (ν - Finsupp.single j 1)))) :=
  @normalized_coordinate

-- Canonical polynomials, independent of the recurrence proof: first two actual modes.
example : Hm (Finsupp.single (0 : Fin 2) 1) (fun _ => 0) = 0 := by
  norm_num [Hm, He, Polynomial.hermite]

example : Hm (Finsupp.single (0 : Fin 2) 2) (fun _ => 0) = -1 := by
  norm_num [Hm, He, Polynomial.hermite]

example : mfact (Finsupp.single (0 : Fin 2) 2) = 2 := by
  norm_num [mfact]

-- The nonzero first mode forces the vacuum lowering term, even at omega = 0.
example :
    Real.sqrt 2 *
      (Hm (Finsupp.single (0 : Fin 2) 2) (fun _ => 0) /
        Real.sqrt (mfact (Finsupp.single (0 : Fin 2) 2))) +
      Hm (0 : Fin 2 →₀ ℕ) (fun _ => 0) / Real.sqrt (mfact (0 : Fin 2 →₀ ℕ)) = 0 := by
  have hs : Real.sqrt (2 : ℝ) ≠ 0 := by positivity
  norm_num [Hm, mfact, He, Polynomial.hermite]
  field_simp [hs]
  norm_num

-- Two active independent Gaussian coordinates: normalized product L2 norm is one.
open scoped InnerProductSpace
example :
    let ν : Fin 2 →₀ ℕ := Finsupp.single 0 2 + Finsupp.single 1 1
    ⟪GaussianChaos.ChaosDensity.hermiteNormalized ν,
      GaussianChaos.ChaosDensity.hermiteNormalized ν⟫_ℝ = 1 := by
  classical
  let ν : Fin 2 →₀ ℕ := Finsupp.single 0 2 + Finsupp.single 1 1
  exact (orthonormal_iff_ite.mp
    (GaussianChaos.ChaosDensity.orthonormal_hermite (ι := Fin 2)) ν ν).trans (by simp)
