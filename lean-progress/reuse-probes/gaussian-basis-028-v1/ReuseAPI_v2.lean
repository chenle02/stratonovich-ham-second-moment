import GaussianChaos.ChaosDensity

set_option autoImplicit false
set_option pp.universes true
set_option pp.maxSteps 1000000

#check @GaussianChaos.GaussianProduct.noise
#print GaussianChaos.WienerChaos.He
#print GaussianChaos.WienerChaos.Hm
#print GaussianChaos.WienerChaos.mfact
#print GaussianChaos.ChaosDensity.hermiteNormalized
#check @GaussianChaos.ChaosDensity.coord_mul_Hm
#check @GaussianChaos.ChaosDensity.orthonormal_hermite
#check @GaussianChaos.ChaosDensity.hermiteBasis
#check GaussianChaos.ChaosDensity.hermiteBasis (ι := Fin 2)
#print axioms GaussianChaos.ChaosDensity.coord_mul_Hm
#print axioms GaussianChaos.ChaosDensity.orthonormal_hermite
#print axioms GaussianChaos.ChaosDensity.hermiteBasis
#check @orthonormal_iff_ite

open scoped InnerProductSpace

-- Private reuse control: the first Gaussian mode has normalized L2 norm squared one.
example : ⟪GaussianChaos.ChaosDensity.hermiteNormalized (Finsupp.single (0 : Fin 2) 1),
    GaussianChaos.ChaosDensity.hermiteNormalized (Finsupp.single (0 : Fin 2) 1)⟫_ℝ = 1 := by
  classical
  have h := orthonormal_iff_ite.mp
    (GaussianChaos.ChaosDensity.orthonormal_hermite (ι := Fin 2))
  simpa using h (Finsupp.single (0 : Fin 2) 1) (Finsupp.single (0 : Fin 2) 1)
