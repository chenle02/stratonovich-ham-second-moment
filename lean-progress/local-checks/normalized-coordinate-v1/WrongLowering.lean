import NormalizedCoordinate

set_option autoImplicit false
open GaussianChaos.WienerChaos

-- Deliberately wrong: suppressing the lowering vacuum term at degree one.
example :
    Real.sqrt 2 *
      (Hm (Finsupp.single (0 : Fin 2) 2) (fun _ => 0) /
        Real.sqrt (mfact (Finsupp.single (0 : Fin 2) 2))) = 0 := by
  norm_num [Hm, mfact, He, Polynomial.hermite]
