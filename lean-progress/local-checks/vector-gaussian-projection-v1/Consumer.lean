import VectorProjection

set_option autoImplicit false
open StratonovichHAMAudit.VectorProjection

universe u v w

-- Exact first frozen closed proposition, including all universe-polymorphic binders.
example : (∀ {Mode : Type u} {E : Type v}
    [NormedAddCommGroup E] [InnerProductSpace ℝ E] [CompleteSpace E]
    (p : (Mode →₀ ℕ) → Prop) (f : (Mode →₀ ℕ) →₀ E),
    (cutoffSpace (E := E) p).toSubmodule.starProjection (realize f) = realize (cut p f)) :=
  @projection_realize

-- Exact second frozen closed proposition: dependent original coordinate set, no extra modes.
example : (∀ {Color : Type w} {E : Type v}
    [DecidableEq Color] [NormedAddCommGroup E] [InnerProductSpace ℝ E] [CompleteSpace E]
    (m N : Color → ℕ) (f : ((Σ c, Fin (m c)) →₀ ℕ) →₀ E),
    (cutoffSpace (E := E) (colorLow Sigma.fst N)).toSubmodule.starProjection (realize f) =
      realize (cut (colorLow Sigma.fst N) f)) := by
  intro Color E _ _ _ _ m N f
  exact projection_realize (colorLow Sigma.fst N) f
