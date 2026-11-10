import ColoredWord

set_option autoImplicit false
open StratonovichHAMAudit
open MeasureTheory GaussianChaos.GaussianProduct
open StratonovichHAMAudit.ColoredWord StratonovichHAMAudit.VectorProjection

example : (∀ {C E : Type} [DecidableEq C] [NormedAddCommGroup E]
    [InnerProductSpace ℝ E] [CompleteSpace E] (m : C → ℕ)
    (K : ∀ c, Fin (m c) → E →L[ℝ] E) (c : C) (f : Poly m E),
    MemLp (signal K c (realize f)) 2 (noise (Index m)) ∧
      coordinate K c (realize f) = realize (insertCoeff K c f)) :=
  @StratonovichHAMAudit.ColoredWord.coordinate_realize

example : (∀ {C B E : Type} [DecidableEq C] [NormedAddCommGroup E]
    [InnerProductSpace ℝ E] [CompleteSpace E] (m : C → ℕ)
    (K : ∀ c, Fin (m c) → E →L[ℝ] E) (F : B → E →L[ℝ] E)
    (F₀ : E →L[ℝ] E) (v : E) (N : C → ℕ) (w : List (C × B)) (c : C),
    MemLp (signal K c (rawVector K F F₀ v w)) 2 (noise (Index m)) ∧
      MemLp (signal K c (project N (cutVector K F F₀ v N w))) 2 (noise (Index m))) :=
  @StratonovichHAMAudit.ColoredWord.word_admissible

example : (∀ {C B E : Type} [DecidableEq C] [NormedAddCommGroup E]
    [InnerProductSpace ℝ E] [CompleteSpace E] (m : C → ℕ)
    (K : ∀ c, Fin (m c) → E →L[ℝ] E) (F : B → E →L[ℝ] E)
    (F₀ : E →L[ℝ] E) (v : E) (N : C → ℕ) (w : List (C × B)),
    (∀ c, HermiteWord.counts w c ≤ N c) →
      cutVector K F F₀ v N w = rawVector K F F₀ v w) :=
  @StratonovichHAMAudit.ColoredWord.word_cutoff
