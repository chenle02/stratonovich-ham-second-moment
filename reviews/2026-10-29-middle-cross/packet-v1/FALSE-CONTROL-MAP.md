# Semantic negative controls

Only the fully qualified controls-v2 count as semantic controls. Three of
the initial open-namespace controls failed during simp-name resolution;
those logs are preserved as SETUP failures,not mathematical failures.
All current controls set autoImplicit=false and use fully qualified symbols.

- WrongZeroShift uses b=1,c=11/10. The root-shift-erased M(0) is
  1025/21483,above actual545/11616. It tests a false SHORTCUT,not J<=I.
- WrongPrefactor uses b=4/3,c=9/4,d=29/12,e=5/3,which satisfy the exact
  square-root identities. U=51329/9827636,I=5277/706552;2U>I. The missing
  heat-Jacobian factor makes the proposed comparison false.
- WrongEndpoint uses the ACTUALtwo square roots at b=4/3,c=1. Both roots
  reduce to4/3and5/3,andU=I=189/7744. The strict theorem requires c>1.
- WrongInverse uses the same valid roots,Z=3. Correct T=(d+c)/(b+1)=2;
  replacing the denominator by b-1 gives14and the false paramC(3,14)=9/4.
- WrongNumeratorSign negates the positive cleared numerator at that valid
  b=4/3,c=9/4root point.

Each current control resolves imports/names and then fails on an unsolved
False. A process exit1or an invalid simp theorem alone is not a valid control.
