import GaussianChaos.ChaosDensity

set_option autoImplicit false

namespace StratonovichHAMAudit.NormalizedCoordinate

open GaussianChaos.WienerChaos GaussianChaos.ChaosDensity

universe u
variable {Mode : Type u} [DecidableEq Mode]

private lemma mfact_raise (ν : Mode →₀ ℕ) (j : Mode) :
    mfact (ν + Finsupp.single j 1) = ((ν j : ℝ) + 1) * mfact ν := by
  classical
  let s := insert j ν.support
  have hj : j ∈ s := Finset.mem_insert_self _ _
  have h0 : ν.support ⊆ s := Finset.subset_insert _ _
  have h1 : (ν + Finsupp.single j 1).support ⊆ s := by
    intro i hi
    rw [Finsupp.mem_support_iff] at hi
    by_cases hij : i = j
    · rw [hij]; exact hj
    · apply h0
      rw [Finsupp.mem_support_iff]
      simpa [Finsupp.single_apply, Ne.symm hij] using hi
  rw [mfact_eq_prod_of_subset h1, mfact_eq_prod_of_subset h0,
    ← Finset.mul_prod_erase _ _ hj, ← Finset.mul_prod_erase _ _ hj]
  have hr : ∏ i ∈ s.erase j, (((ν + Finsupp.single j 1 : Mode →₀ ℕ) i).factorial : ℝ)
      = ∏ i ∈ s.erase j, ((ν i).factorial : ℝ) :=
    Finset.prod_congr rfl fun i hi => by
      simp [Ne.symm (Finset.ne_of_mem_erase hi)]
  rw [hr]
  simp only [Finsupp.coe_add, Pi.add_apply, Finsupp.single_eq_same,
    Nat.factorial_succ, Nat.cast_mul, Nat.cast_add, Nat.cast_one]
  ring

private lemma mfact_lower (ν : Mode →₀ ℕ) (j : Mode) (hj : 0 < ν j) :
    mfact ν = (ν j : ℝ) * mfact (ν - Finsupp.single j 1) := by
  have hrestore : ν - Finsupp.single j 1 + Finsupp.single j 1 = ν := by
    ext i
    by_cases h : i = j
    · subst i
      simp only [Finsupp.coe_add, Finsupp.coe_tsub, Pi.add_apply, Pi.sub_apply,
        Finsupp.single_eq_same]
      omega
    · simp [Ne.symm h]
  have hindex : (((ν - Finsupp.single j 1 : Mode →₀ ℕ) j) : ℝ) + 1 = (ν j : ℝ) := by
    have hn : (ν - Finsupp.single j 1 : Mode →₀ ℕ) j + 1 = ν j := by
      simp only [Finsupp.coe_tsub, Pi.sub_apply, Finsupp.single_eq_same]
      omega
    exact_mod_cast hn
  calc
    mfact ν = mfact (ν - Finsupp.single j 1 + Finsupp.single j 1) :=
      congrArg mfact hrestore.symm
    _ = ((((ν - Finsupp.single j 1 : Mode →₀ ℕ) j) : ℝ) + 1) *
        mfact (ν - Finsupp.single j 1) := mfact_raise _ j
    _ = _ := congrArg (fun r : ℝ => r * mfact (ν - Finsupp.single j 1)) hindex

/-- The canonical normalized polynomial representative, including the zero lowering case.
This is the exact proposition frozen and independently reviewed before proof work. -/
theorem normalized_coordinate (ν : Mode →₀ ℕ) (j : Mode) (ω : Mode → ℝ) :
    ω j * (GaussianChaos.WienerChaos.Hm ν ω /
      Real.sqrt (GaussianChaos.WienerChaos.mfact ν)) =
      Real.sqrt ((ν j : ℝ) + 1) *
        (GaussianChaos.WienerChaos.Hm (ν + Finsupp.single j 1) ω /
          Real.sqrt (GaussianChaos.WienerChaos.mfact (ν + Finsupp.single j 1))) +
      Real.sqrt (ν j : ℝ) *
        (GaussianChaos.WienerChaos.Hm (ν - Finsupp.single j 1) ω /
          Real.sqrt (GaussianChaos.WienerChaos.mfact (ν - Finsupp.single j 1))) := by
  have hν : Real.sqrt (mfact ν) ≠ 0 := (Real.sqrt_pos.mpr (mfact_pos ν)).ne'
  have hr : Real.sqrt ((ν j : ℝ) + 1) ≠ 0 := by positivity
  have hp : Real.sqrt (mfact (ν + Finsupp.single j 1)) =
      Real.sqrt ((ν j : ℝ) + 1) * Real.sqrt (mfact ν) := by
    rw [mfact_raise, Real.sqrt_mul (by positivity)]
  rw [← mul_div_assoc, coord_mul_Hm, add_div]
  congr 1
  · rw [hp]
    field_simp [hr, hν]
  · by_cases hj : ν j = 0
    · simp [hj]
    · have hpos : 0 < ν j := Nat.pos_of_ne_zero hj
      have hs : Real.sqrt (ν j : ℝ) ≠ 0 := by positivity
      have hm : Real.sqrt (mfact (ν - Finsupp.single j 1)) ≠ 0 :=
        (Real.sqrt_pos.mpr (mfact_pos _)).ne'
      have hd : Real.sqrt (mfact ν) =
          Real.sqrt (ν j : ℝ) * Real.sqrt (mfact (ν - Finsupp.single j 1)) := by
        rw [mfact_lower ν j hpos, Real.sqrt_mul (by positivity)]
      rw [hd]
      calc
        (ν j : ℝ) * Hm (ν - Finsupp.single j 1) ω /
            (Real.sqrt (ν j : ℝ) * Real.sqrt (mfact (ν - Finsupp.single j 1))) =
          (Real.sqrt (ν j : ℝ) * Real.sqrt (ν j : ℝ)) *
            Hm (ν - Finsupp.single j 1) ω /
            (Real.sqrt (ν j : ℝ) * Real.sqrt (mfact (ν - Finsupp.single j 1))) := by
              rw [Real.mul_self_sqrt (Nat.cast_nonneg (ν j))]
        _ = _ := by field_simp [hs, hm]

end StratonovichHAMAudit.NormalizedCoordinate

set_option pp.universes true
#check @StratonovichHAMAudit.NormalizedCoordinate.normalized_coordinate
#print axioms StratonovichHAMAudit.NormalizedCoordinate.normalized_coordinate
