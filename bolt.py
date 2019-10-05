# -*- coding: utf-8 -*-

"""ボルト／HTBに関するデータを返す関数"""

HTB_SIZES = ['M16', 'M20', 'M22', 'M24', 'M27', 'M30']
M16, M20, M22, M24, M27, M30 = HTB_SIZES  # アンパック代入

HTB_STRENGTHS = ['F8T', 'F10T']
F8T, F10T = HTB_STRENGTHS

TERMS = ['LONG', 'SHORT']
LONG, SHORT = TERMS

PROPERTY_NAMES = ['QA', 'TA', 'DIA', 'HOLE_DIA']
# 許容せん断力, 許容引張力, ボルト軸径(mm), ボルト孔径(mm)
QA, TA, DIA, HOLE_DIA = PROPERTY_NAMES

LONG_TERM = 'LONG_TERM'  # 長期
SHORT_TERM = 'SHORT_TERM'  # 短期

# property:特性
Qal = 'Qal'  # 長期許容せん断力(kN) １面せん断
Qas = 'Qas'  # 短期許容せん断力(kN) １面せん断

Tal = 'Tal'  # 長期許容引張力(kN)
Tas = 'Tas'  # 短期期許容引張力(kN)

# 寸法はmm, 力はkN
# HTB_M16 = dict(name='M16', dia=16, hole_dia=18, Qal=30.2, Qas=45.3)
# HTB_M20 = dict(name='M20', dia=20, hole_dia=22, Qal=47.1, Qas=70.6)

# HTB F10T データの設定
HTB_SPC_F10T = {}
HTB_SPC_F10T[M16] = {DIA: 16, HOLE_DIA: 18, Qal: 30.2, Qas: 45.2, Tal: 62.3, Tas: 93.5}
HTB_SPC_F10T[M20] = {DIA: 20, HOLE_DIA: 22, Qal: 47.1, Qas: 70.7, Tal: 97.4, Tas: 146.}
HTB_SPC_F10T[M22] = {DIA: 22, HOLE_DIA: 24, Qal: 57.0, Qas: 85.5, Tal: 118., Tas: 177.}
HTB_SPC_F10T[M24] = {DIA: 24, HOLE_DIA: 26, Qal: 67.9, Qas: 102., Tal: 140., Tas: 210.}
HTB_SPC_F10T[M27] = {DIA: 27, HOLE_DIA: 30, Qal: 85.9, Qas: 129., Tal: 177., Tas: 266.}
HTB_SPC_F10T[M30] = {DIA: 30, HOLE_DIA: 33, Qal: 106., Qas: 159., Tal: 219., Tas: 329.}

# HTB F8T データの設定
HTB_SPC_F8T = {}
HTB_SPC_F8T[M16] = {DIA: 16, HOLE_DIA: 18, Qal: 21.4, Qas: 32.1, Tal: 50.3, Tas: 75.4}
HTB_SPC_F8T[M20] = {DIA: 20, HOLE_DIA: 22, Qal: 33.5, Qas: 50.2, Tal: 78.5, Tas: 117.}
HTB_SPC_F8T[M22] = {DIA: 22, HOLE_DIA: 24, Qal: 40.5, Qas: 60.8, Tal: 95.0, Tas: 142.}
HTB_SPC_F8T[M24] = {DIA: 24, HOLE_DIA: 26, Qal: 48.2, Qas: 72.3, Tal: 113., Tas: 169.}
HTB_SPC_F8T[M27] = {DIA: 27, HOLE_DIA: 30, Qal: 61.0, Qas: 91.5, Tal: 143., Tas: 214.}
HTB_SPC_F8T[M30] = {DIA: 30, HOLE_DIA: 33, Qal: 75.4, Qas: 113., Tal: 177., Tas: 265.}


class ParameterError(Exception):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return repr(self.value)


def htb_spec(size=M16, prop=QA, term=LONG, strength=F10T):
    """指定されたHTBの性能値を返す。

    サイズ(M16～M30)、性能名(QA/TA/DIA/HOLE_DIA)、長期・短期(LONG/SHORT)、HTB強度(F10T/F8T)を指定
    return : 許容せん断力(kN)、許容引張力(kN)、軸径(mm)、孔径(mm)"""

    size, prop, term, strength = list(map(lambda w: w.upper(), [size, prop, term, strength]))

    if size in HTB_SIZES and prop in PROPERTY_NAMES and term in TERMS and strength in HTB_STRENGTHS:
        SPC = None
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
            if term == LONG:
                actual_prop = 'Tal'
            elif term == SHORT:
                actual_prop = 'Tas'
        elif prop == DIA:
            actual_prop = DIA
        elif prop == HOLE_DIA:
            actual_prop = HOLE_DIA

        return SPC[size][actual_prop]
    else:
        raise ParameterError('invalid parameter given')
