module

public import Mathlib.MeasureTheory.Integral.Bochner.Basic
public import Mathlib.Tactic

@[expose] public section

set_option autoImplicit false

open MeasureTheory Filter

namespace StratonovichHAMAudit.ClockFilter

theorem resolvent_partial_fraction (θ λ r : ℝ) (hθ : 0 < θ) (hλ : 0 < λ) :
    (2 * θ + λ) / (2 * θ * (θ ^ 2 + r ^ 2) * ((θ + λ) ^ 2 + r ^ 2)) =
      (1 / (θ ^ 2 + r ^ 2) - 1 / ((θ + λ) ^ 2 + r ^ 2)) / (2 * θ * λ) := by
  have hA : θ ^ 2 + r ^ 2 ≠ 0 := ne_of_gt (by positivity)
  have hB : (θ + λ) ^ 2 + r ^ 2 ≠ 0 := ne_of_gt (by positivity)
  field_simp [hθ.ne', hλ.ne', hA, hB]
  <;> ring

theorem clock_filter_bounds (θ λ : ℝ) (hθ : 0 < θ) (hλ : 0 < λ) :
    0 < 2 * θ / (2 * θ + λ) ∧ 2 * θ / (2 * θ + λ) < 1 := by
  have hden : 0 < 2 * θ + λ := by linarith
  constructor
  · exact div_pos (by linarith) hden
  · exact (div_lt_one hden).2 (by linarith)

theorem strict_filter_integral (θ : ℝ) (hθ : 0 < θ)
    (σ : Measure ℝ) (hσ : σ ≠ 0)
    (hλ : ∀ᵐ λ ∂σ, 0 < λ)
    (w : ℝ → ℝ) (hw : Integrable w σ)
    (hwpos : ∀ᵐ λ ∂σ, 0 < w λ) :
    Integrable (fun λ => 2 * θ / (2 * θ + λ) * w λ) σ ∧
      (∫ λ, 2 * θ / (2 * θ + λ) * w λ ∂σ) < ∫ λ, w λ ∂σ := by
  let f : ℝ → ℝ := fun λ => 2 * θ / (2 * θ + λ) * w λ
  have hmeas : Measurable (fun λ : ℝ => 2 * θ / (2 * θ + λ)) :=
    measurable_const.div (measurable_const.add measurable_id)
  have hfm : AEStronglyMeasurable f σ :=
    hmeas.aestronglyMeasurable.mul hw.aestronglyMeasurable
  have hnonneg : ∀ᵐ λ ∂σ, 0 ≤ f λ := by
    filter_upwards [hλ, hwpos] with λ hλ0 hw0
    exact (mul_pos (clock_filter_bounds θ λ hθ hλ0).1 hw0).le
  have hstrict : ∀ᵐ λ ∂σ, f λ < w λ := by
    filter_upwards [hλ, hwpos] with λ hλ0 hw0
    calc
      f λ = 2 * θ / (2 * θ + λ) * w λ := rfl
      _ < 1 * w λ := mul_lt_mul_of_pos_right
        (clock_filter_bounds θ λ hθ hλ0).2 hw0
      _ = w λ := one_mul _
  have hle : f ≤ᵐ[σ] w := hstrict.mono fun _ h => h.le
  have hfi : Integrable f σ := hw.mono_nonneg hfm hnonneg hle
  have hIntLe : (∫ λ, f λ ∂σ) ≤ ∫ λ, w λ ∂σ :=
    integral_mono_ae hfi hw hle
  have hne : (∫ λ, f λ ∂σ) ≠ ∫ λ, w λ ∂σ := by
    intro heq
    have hae : f =ᵐ[σ] w := (integral_eq_iff_of_ae_le hfi hw hle).1 heq
    letI : (ae σ).NeBot := ae_neBot.2 hσ
    obtain ⟨λ, hlt, heqλ⟩ := (hstrict.and hae).exists
    exact (ne_of_lt hlt) heqλ
  refine ⟨hfi, ?_⟩
  exact lt_of_le_of_ne hIntLe (Ne.symm hne)

end StratonovichHAMAudit.ClockFilter
