# -*- coding: utf-8 -*-

"""ボルト／HTBに関するデータを返す関数"""


HTB_SIZES = ['M16', 'M20', 'M22', 'M24', 'M27', 'M30']
M16, M20, M22, M24, M27, M30 = HTB_SIZES  # アンパック代入

HTB_STRENGTHS = ['F8T', 'F10T']
F8T, F10T = HTB_STRENGTHS

TERMS = ['LONG', 'SHORT']
LONG, SHORT = TERMS

PROPERTY_NAMES = ['QA', 'TA', 'DIA', 'HOLE_DIA']


QA = 'QA'  # 許容せん断力
TA = 'TA'  # 許容引張力

LONG_TERM = 'LONG_TERM'  # 長期
SHORT_TERM = 'SHORT_TERM'  # 短期

# property:特性
Qal = 'Qal'  # 長期許容せん断力(kN) １面せん断
Qas = 'Qas'  # 短期許容せん断力(kN) １面せん断

Tal = 'Tal'  # 長期許容引張力(kN)
Tas = 'Tas'  # 短期期許容引張力(kN)

Dia = 'Dia'  # ボルト軸径(mm)
Hole_dia = 'Hole_dia'  # ボルト孔径(mm)

# 寸法はmm, 力はkN
# HTB_M16 = dict(name='M16', dia=16, hole_dia=18, Qal=30.2, Qas=45.3)
# HTB_M20 = dict(name='M20', dia=20, hole_dia=22, Qal=47.1, Qas=70.6)

HTB_M16_F10T = {Dia: 16, Hole_dia: 18, Qal: 30.2, Qas: 45.3, Tal: 0, Tas: 0}
HTB_M20_F10T = {Dia: 20, Hole_dia: 22, Qal: 30.2, Qas: 45.3, Tal: 0, Tas: 0}
HTB_M22_F10T = {Dia: 22, Hole_dia: 24, Qal: 30.2, Qas: 45.3, Tal: 0, Tas: 0}
HTB_M24_F10T = {Dia: 24, Hole_dia: 26, Qal: 30.2, Qas: 45.3, Tal: 0, Tas: 0}
HTB_M27_F10T = {Dia: 27, Hole_dia: 29, Qal: 30.2, Qas: 45.3, Tal: 0, Tas: 0}
HTB_M30_F10T = {Dia: 30, Hole_dia: 32, Qal: 30.2, Qas: 45.3, Tal: 0, Tas: 0}

HTB_SPC_F10T = {}
HTB_SPC_F10T[M16] = HTB_M16_F10T
HTB_SPC_F10T[M20] = HTB_M20_F10T


class ParameterError(Exception):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return repr(self.value)


def htb_spec(size=M16, prop=QA, term=LONG, strength=F10T):
    """指定されたHTBの性能値を返す。

    サイズ(M16~M30)、性能名(QA,TA,DIA,HOLE_DIA)、長期・短期(LONG/SHORT)、HTB強度(F10T/F8T)を指定
    return : 許容せん断力(kN)、許容引張力(kN)、軸径(mm)、孔径(mm)"""

    if size in HTB_SIZES and prop in PROPERTY_NAMES and term in TERMS and strength in HTB_STRENGTHS:
        if strength == F10T:
            SPC = HTB_SPC_F10T
        elif strength == F8T:
            SPC = HTB_SPC_F8T
        actual_prop = ''
        if prop == QA:
            if term == LONG:
                actual_prop = 'Qal'
            elif term == SHORT:
                actual_prop = 'Qas'
        elif prop == TA:
            pass

        return SPC[size][actual_prop]

    else:
        raise ParameterError('invalid parameter given')


