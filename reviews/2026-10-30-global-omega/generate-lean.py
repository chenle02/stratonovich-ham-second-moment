from pathlib import Path
import json
root=Path.cwd();d=root/'lean-progress/local-checks/global-omega-v1';c=json.loads((root/'reviews/2026-10-30-global-omega/certificates-v1.json').read_text())
Q=c['Q_expression'].replace('**','^')
s='''module
public import Mathlib.Tactic
@[expose] public section
noncomputable section
set_option autoImplicit false
namespace StratonovichHAMAudit.GlobalOmega

'''
s+='def envelopePolynomial (x : ℝ) : ℝ :=\n  '+Q+'\n\n'
s+='''def envelopeDenom (x : ℝ) : ℝ :=
  750*(3-x)*(2-x)*(1-x)*(5-2*x)*(3-2*x)*(5-3*x)*(3-4*x-2*x^2)

def envelopeRational (x : ℝ) : ℝ :=
  2*(1-x^2+x^4/2)*(1-4*x^2)/(1-3*x/5)*
    (1/(2*(1-x))+x*(1-x)/(2-x)+x*(x+1)*(1-x)^2/(3*(3-x))-
      2*(1-3*x/5)*(1/(3-2*x)+(2*x+1)*(1-x)/(3*(5-2*x)))*
        x*(177/100)*(1-7*x/5))*(3-4*x)/(3-4*x-2*x^2)

'''
for cert in c['certificates']:
 label=cert['label'];arg='t/4' if label=='left' else '(1+t)/4'
 rhs=' +\n    '.join(f'({v}:ℝ)*t^{i}*(1-t)^{15-i}' for i,v in enumerate(cert['shifted_positive_coefficients']))
 s+=f'''theorem {label}_certificate (t : ℝ) (ht0 : 0 ≤ t) (ht1 : t ≤ 1) :
    1 ≤ (4:ℝ)^15*envelopePolynomial ({arg}) := by
  have h1 : 0 ≤ 1-t := by linarith
  have hid : (4:ℝ)^15*envelopePolynomial ({arg})-1 =
    {rhs} := by
    unfold envelopePolynomial
    ring
  have hn : 0 ≤
    {rhs} := by positivity
  linarith

'''
s+='''theorem polynomial_pos (x : ℝ) (hx0 : 0 ≤ x) (hx1 : x ≤ 1/2) :
    0 < envelopePolynomial x := by
  by_cases h : x ≤ 1/4
  · have hb := left_certificate (4*x) (by linarith) (by linarith)
    have he : (4*x)/4=x := by ring
    rw [he] at hb
    nlinarith
  · have hb := right_certificate (4*x-1) (by linarith) (by linarith)
    have he : (1+(4*x-1))/4=x := by ring
    rw [he] at hb
    nlinarith

theorem rational_lt_one (x : ℝ) (hx : 0 < x) (hh : x ≤ 1/2) :
    envelopeRational x < 1 := by
  have h1 : 0 < 1-x := by linarith
  have h2 : 0 < 2-x := by linarith
  have h3 : 0 < 3-x := by linarith
  have h4 : 0 < 3-2*x := by linarith
  have h5 : 0 < 5-2*x := by linarith
  have h6 : 0 < 5-3*x := by linarith
  have hg : 0 < 1-3*x/5 := by linarith
  have h8 : 0 < 3-4*x-2*x^2 := by
    have hm := mul_nonneg hx.le (sub_nonneg.mpr hh)
    nlinarith
  have hd : 0 < envelopeDenom x := by
    unfold envelopeDenom
    positivity
  have n4 : 3-x*2 ≠ 0 := by simpa only [mul_comm] using ne_of_gt h4
  have n5 : 5-x*2 ≠ 0 := by simpa only [mul_comm] using ne_of_gt h5
  have n8 : 3-x*4-x^2*2 ≠ 0 := by simpa only [mul_comm] using ne_of_gt h8
  have hid : envelopeDenom x*(1-envelopeRational x)=x*envelopePolynomial x := by
    unfold envelopeDenom envelopeRational envelopePolynomial
    field_simp [ne_of_gt h1, ne_of_gt h2, ne_of_gt h3, ne_of_gt h4,
      ne_of_gt h5, ne_of_gt h6, ne_of_gt hg, ne_of_gt h8, n4, n5, n8]
    ring
  have hp := mul_pos hx (polynomial_pos x hx.le hh)
  by_contra hnot
  have hv : 1 ≤ envelopeRational x := le_of_not_gt hnot
  have hn := mul_nonpos_of_nonneg_of_nonpos hd.le (sub_nonpos.mpr hv)
  rw [hid] at hn
  linarith

end StratonovichHAMAudit.GlobalOmega
'''
(d/'StratonovichHAMAudit/GlobalOmega.lean').write_text(s)
audit='import StratonovichHAMAudit.GlobalOmega\nset_option pp.universes true\nset_option pp.all true\n'
for name in ['envelopePolynomial','envelopeDenom','envelopeRational']:audit+='#print StratonovichHAMAudit.GlobalOmega.'+name+'\n'
for name in ['left_certificate','right_certificate','polynomial_pos','rational_lt_one']:audit+='#check StratonovichHAMAudit.GlobalOmega.'+name+'\n#print axioms StratonovichHAMAudit.GlobalOmega.'+name+'\n'
(d/'Audit.lean').write_text(audit)
print('Generated exactdefs, two32term certificate uses and4publictheorem types.')
