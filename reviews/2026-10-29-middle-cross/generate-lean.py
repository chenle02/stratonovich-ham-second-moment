"""Build an auditable local scalar consumer from the frozen300term certificate."""
from pathlib import Path
import json,hashlib
ROOT=Path(__file__).resolve().parents[2]
DATA=ROOT/'reviews/2026-10-29-terminal-cross/successor-middle/algebra-screen.json'
d=json.loads(DATA.read_text());coeff=d['shifted_coefficients'];assert len(coeff)==300
assert all(v['coefficient']>0 and v['y']>=1 for v in coeff)
groups={}
for v in coeff:groups.setdefault(v['x'],{})[v['y']-1]=v['coefficient']
def horner(values,var):
 k=max(values);s=str(values[k])
 for i in range(k-1,-1,-1):s=f'({s}*{var} + {values.get(i,0)})'
 return s
ys={k:horner(v,'y')for k,v in groups.items()}
expr=ys[max(ys)]
for i in range(max(ys)-1,-1,-1):expr=f'({expr}*x +\n    {ys.get(i,"0")})'
header='''module
public import Mathlib.Tactic
public import Mathlib.Analysis.Real.Sqrt
@[expose] public section
noncomputable section
set_option autoImplicit false
set_option maxRecDepth 4000
namespace StratonovichHAMAudit.MiddleCross

def actual (b c : ℝ) : ℝ :=
  (2*b^2+4*b*c+2*c^2-c+1) /
    (8*b*c*(b+1)*(2*b+1)*(b+c-1)*(2*b+2*c-1))
def massK (b c : ℝ) : ℝ := 1/(4*b*c*(c+1))
def resolvent (b c r : ℝ) : ℝ :=
  (b+c+r+1)/(4*b*c*(c+1)*r*(b+c+r)*(b+r+1))
def part1 (b d e : ℝ) : ℝ :=
  (d+e+b+1)/(d*e*(b+d+1)*(b+e+1))
def part2 (b c d e : ℝ) : ℝ :=
  (d^2+d*e+e^2+(2*b+c+1)*(d+e)+(b+c)*(b+1)) /
    (d*e*(b+c+d)*(b+c+e)*(b+d+1)*(b+e+1))
def upper (b c d e : ℝ) : ℝ :=
  resolvent b c e + massK b c*(part1 b d e+part2 b c d e)/(d+e)
def denominator (b c d e : ℝ) : ℝ :=
  8*b*c*d*e*(b+1)*(2*b+1)*(c+1)*(d+e)*(b+c-1)*
    (b+c+d)*(b+c+e)*(b+d+1)*(b+e+1)*(2*b+2*c-1)
def numerator (b c d e : ℝ) : ℝ :=
  (2*b^2+4*b*c+2*c^2-c+1)*d*e*(c+1)*(d+e)*
    (b+c+d)*(b+c+e)*(b+d+1)*(b+e+1) -
  2*(b+1)*(2*b+1)*(b+c-1)*(2*b+2*c-1)*
    (d*(d+e)*(b+c+d)*(b+d+1)*(b+c+e+1) +
      (b+c+d)*(b+c+e)*(b+d+e+1) +
      (d^2+d*e+e^2+(2*b+c+1)*(d+e)+(b+c)*(b+1)))
def paramB (z : ℝ) : ℝ := (z^2-1)/(2*z)
def paramE (z : ℝ) : ℝ := (z^2+1)/(2*z)
def paramC (z t : ℝ) : ℝ := ((paramB z+1)*t-(paramB z-1)/t)/2
ndef_placeholder
'''.replace('ndef_placeholder','')
header+='def paramD (z t : ℝ) : ℝ := ((paramB z+1)*t+(paramB z-1)/t)/2\n'
header+='def certificate (x y : ℝ) : ℝ := y * (\n    '+expr+')\n\n'
body='''theorem certificate_pos (x y : ℝ) (hx : 0 ≤ x) (hy : 0 < y) :
    0 < certificate x y := by
  unfold certificate
  positivity

set_option maxHeartbeats 2000000 in
 theorem parameter_identity (z t : ℝ) (hz : 0 < z) (ht : 0 < t) :
    numerator (paramB z) (paramC z t) (paramD z t) (paramE z) *
      (32768*t^7*z^9) = certificate (z-2) (t-1) := by
  unfold numerator paramC paramD paramE paramB certificate
  field_simp [hz.ne', ht.ne']
  ring

 theorem parameter_numerator_pos (z t : ℝ) (hz : 2 ≤ z) (ht : 1 < t) :
    0 < numerator (paramB z) (paramC z t) (paramD z t) (paramE z) := by
  have hzpos : 0 < z := by linarith
  have htpos : 0 < t := by linarith
  have hs : 0 < (32768:ℝ)*t^7*z^9 := by positivity
  have hp : 0 < numerator (paramB z) (paramC z t) (paramD z t) (paramE z) *
      (32768*t^7*z^9) := by
    rw [parameter_identity z t hzpos htpos]
    exact certificate_pos (z-2) (t-1) (by linarith) (by linarith)
  exact (mul_pos_iff_of_pos_right hs).1 hp

set_option maxHeartbeats 2000000 in
 theorem difference_identity (b c d e : ℝ) (hb : 1 ≤ b) (hc : 1 ≤ c)
    (hd : 0 < d) (he : 0 < e) :
    actual b c - upper b c d e = numerator b c d e / denominator b c d e := by
  have hb0 : 0 < b := by linarith
  have hc0 : 0 < c := by linarith
  have hbc : 0 < b+c-1 := by linarith
  have h2bc : 0 < 2*b+2*c-1 := by linarith
  have hbe : 0 < b+c+e := by positivity
  have hbd : 0 < b+c+d := by positivity
  have hb1d : 0 < b+d+1 := by positivity
  have hb1e : 0 < b+e+1 := by positivity
  have hb1 : 0 < b+1 := by positivity
  have h2b1 : 0 < 2*b+1 := by positivity
  have hc1 : 0 < c+1 := by positivity
  have hde : 0 < d+e := by positivity
  unfold actual upper resolvent massK part1 part2 numerator denominator
  field_simp (disch := first | positivity | linarith)
  ring

set_option maxHeartbeats 2000000 in
 theorem resolvent_difference (b c d e : ℝ) (hb : 1 ≤ b) (hc : 1 ≤ c)
    (hd : 0 < d) (he : 0 < e) :
    resolvent b c d - resolvent b c e =
      (e-d)*massK b c*(part1 b d e+part2 b c d e) := by
  have hb0 : 0 < b := by linarith
  have hc0 : 0 < c := by linarith
  have hbe : 0 < b+c+e := by positivity
  have hbd : 0 < b+c+d := by positivity
  have hb1d : 0 < b+d+1 := by positivity
  have hb1e : 0 < b+e+1 := by positivity
  have hc1 : 0 < c+1 := by positivity
  unfold resolvent massK part1 part2
  field_simp (disch := first | positivity | linarith)
  ring

 theorem root_numerator_pos (b c : ℝ) (hb : 1 ≤ b) (hc : 1 < c) :
    0 < numerator b c (Real.sqrt (b^2+c^2-1)) (Real.sqrt (b^2+1)) := by
  let d := Real.sqrt (b^2+c^2-1)
  let e := Real.sqrt (b^2+1)
  have hb0 : 0 < b := by linarith
  have hc0 : 0 < c := by linarith
  have hcsq : 1 < c^2 := by nlinarith [sq_nonneg (c-1)]
  have hrad : 0 < b^2+c^2-1 := by nlinarith [sq_nonneg b]
  have hd0 : 0 < d := Real.sqrt_pos.2 hrad
  have he0 : 0 < e := Real.sqrt_pos.2 (by positivity)
  have hdsq : d^2 = b^2+c^2-1 := Real.sq_sqrt hrad.le
  have hesq : e^2 = b^2+1 := Real.sq_sqrt (by positivity)
  have hegt : b < e := (sq_lt_sq₀ hb0.le he0.le).1 (by nlinarith)
  have hdge : b ≤ d := (sq_le_sq₀ hb0.le hd0.le).1 (by nlinarith)
  let z := b+e
  let t := (d+c)/(b+1)
  have hz : 2 ≤ z := by dsimp [z]; linarith
  have hz0 : 0 < z := by linarith
  have hb1 : 0 < b+1 := by positivity
  have ht : 1 < t := by
    dsimp [t]
    exact (one_lt_div hb1).2 (by linarith)
  have ht0 : 0 < t := by linarith
  have hB : paramB z = b := by
    unfold paramB
    field_simp [hz0.ne']
    dsimp [z]
    nlinarith [hesq]
  have hE : paramE z = e := by
    unfold paramE
    field_simp [hz0.ne']
    dsimp [z]
    nlinarith [hesq]
  have hmul : (b+1)*t = d+c := by
    dsimp [t]
    field_simp [hb1.ne']
  have hsubmul : (d-c)*t = b-1 := by
    dsimp [t]
    field_simp [hb1.ne']
    nlinarith [hdsq]
  have hdiv : (b-1)/t = d-c := (div_eq_iff ht0.ne').2 hsubmul.symm
  have hC : paramC z t = c := by
    unfold paramC
    rw [hB,hmul,hdiv]
    ring
  have hD : paramD z t = d := by
    unfold paramD
    rw [hB,hmul,hdiv]
    ring
  have hp := parameter_numerator_pos z t hz ht
  rw [hB,hC,hD,hE] at hp
  exact hp

 theorem middle_bound (b c : ℝ) (hb : 1 ≤ b) (hc : 1 < c) :
    upper b c (Real.sqrt (b^2+c^2-1)) (Real.sqrt (b^2+1)) < actual b c := by
  have hb0 : 0 < b := by linarith
  have hc0 : 0 < c := by linarith
  have hcsq : 1 < c^2 := by nlinarith [sq_nonneg (c-1)]
  have hd : 0 < Real.sqrt (b^2+c^2-1) := Real.sqrt_pos.2 (by nlinarith [sq_nonneg b])
  have he : 0 < Real.sqrt (b^2+1) := Real.sqrt_pos.2 (by positivity)
  have hbc : 0 < b+c-1 := by linarith
  have h2bc : 0 < 2*b+2*c-1 := by linarith
  have hden : 0 < denominator b c (Real.sqrt (b^2+c^2-1)) (Real.sqrt (b^2+1)) := by
    unfold denominator
    positivity
  have hp := root_numerator_pos b c hb hc
  have hdiff : 0 < actual b c - upper b c (Real.sqrt (b^2+c^2-1)) (Real.sqrt (b^2+1)) := by
    rw [difference_identity b c _ _ hb hc.le hd he]
    exact div_pos hp hden
  linarith

end StratonovichHAMAudit.MiddleCross
end
'''
# Keep the generated certificate lines below the native reader's long-line limit.
text=header+body
assert max(map(len,text.splitlines()))<2000
out=ROOT/'lean-progress/local-checks/middle-cross-v1/StratonovichHAMAudit/MiddleCross.lean'
out.write_text(text)
print(json.dumps({'source':str(out.relative_to(ROOT)),'bytes':len(text.encode()),'max_line':max(map(len,text.splitlines())),'certificate_data_sha256':hashlib.sha256(DATA.read_bytes()).hexdigest()},indent=2))
