# -*- coding: utf-8 -*-


class Bolt:
    def __init__(self):
        self._name = ""
        self._hole_dia = 0
        self._Qa_long = 0.
        self._Qa_short = 0.
        self._Na_long = 0.
        self._Na_short = 0.


# 寸法はmm, 力はkN
HTB_M16 = dict(name='M16', dia=16, hole_dia=18, Qal=30.2, Qas=45.3)
HTB_M20 = dict(name='M20', dia=20, hole_dia=22, Qal=47.1, Qas=70.6)

HTB_SPC = {}
HTB_SPC['M16'] = HTB_M16
HTB_SPC['M20'] = HTB_M20

HTB_SIZE = ['M16', 'M20', 'M22', 'M24', 'M27', 'M30']
HTB_STRENGTH = ['F8T', 'F10T']


def htb_spec(size, type, term):
    return
