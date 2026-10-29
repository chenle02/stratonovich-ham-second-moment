module
public import StratonovichHAMAudit.TerminalCross
example : StratonovichHAMAudit.TerminalCross.polynomial 1 2 ≤ 0 := by
  norm_num [StratonovichHAMAudit.TerminalCross.polynomial, StratonovichHAMAudit.TerminalCross.numP, StratonovichHAMAudit.TerminalCross.numN]
