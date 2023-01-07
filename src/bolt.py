# -*- coding: utf-8 -*-

"""ボルト／HTBに関するデータを返す関数"""

HTB_SIZES = ['M16', 'M20', 'M22', 'M24', 'M27', 'M30']
M16, M20, M22, M24, M27, M30 = HTB_SIZES  # アンパック代入
M12 = 'M12'

HTB_STRENGTHS = ['F8T', 'F10T']
F8T, F10T = HTB_STRENGTHS

BOLT_STRENGTHS = ['4T', '6T']
B4T, B6T = BOLT_STRENGTHS

TERMS = ['LONG', 'SHORT']
LONG, SHORT = TERMS

PROPERTY_NAMES = ['QA', 'TA', 'Dia', 'Hole_dia']
# 許容せん断力, 許容引張力, ボルト軸径(mm), ボルト孔径(mm)
QA, TA, DIA, HOLE_DIA = PROPERTY_NAMES

LONG_TERM = 'LONG_TERM'  # 長期
SHORT_TERM = 'SHORT_TERM'  # 短期

# property:特性
Qal = 'Qal'  # 長期許容せん断力(kN) １面せん断
Qas = 'Qas'  # 短期許容せん断力(kN) １面せん断

Tal = 'Tal'  # 長期許容引張力(kN)
Tas = 'Tas'  # 短期期許容引張力(kN)

Qu = 'Qu'  # 最大せん断耐力（kN）
Tu = 'Tu'  # 最大引張耐力（kN）

# 寸法はmm, 力はkN
# HTB_M16 = dict(name='M16', dia=16, hole_dia=18, Qal=30.2, Qas=45.3)
# HTB_M20 = dict(name='M20', dia=20, hole_dia=22, Qal=47.1, Qas=70.6)

# HTB F10T データの設定
HTB_SPC_F10T = {}
HTB_SPC_F10T[M16] = {DIA: 16, HOLE_DIA: 18, Qal: 30.2, Qas: 45.2, Tal: 62.3, Tas: 93.5, Qu: 121, Tu: 157}
HTB_SPC_F10T[M20] = {DIA: 20, HOLE_DIA: 22, Qal: 47.1, Qas: 70.7, Tal: 97.4, Tas: 146.0, Qu: 188, Tu: 245}
HTB_SPC_F10T[M22] = {DIA: 22, HOLE_DIA: 24, Qal: 57.0, Qas: 85.5, Tal: 118.0, Tas: 177.0, Qu: 228, Tu: 303}
HTB_SPC_F10T[M24] = {DIA: 24, HOLE_DIA: 26, Qal: 67.9, Qas: 102.0, Tal: 140.0, Tas: 210.0, Qu: 271, Tu: 353}
HTB_SPC_F10T[M27] = {DIA: 27, HOLE_DIA: 30, Qal: 85.9, Qas: 129.0, Tal: 177.0, Tas: 266.0, Qu: 343, Tu: 459}
HTB_SPC_F10T[M30] = {DIA: 30, HOLE_DIA: 33, Qal: 106.0, Qas: 159.0, Tal: 219.0, Tas: 329.0, Qu: 424, Tu: 561}

# HTB F8T データの設定
HTB_SPC_F8T = {}
HTB_SPC_F8T[M16] = {DIA: 16, HOLE_DIA: 18, Qal: 21.4, Qas: 32.1, Tal: 50.3, Tas: 75.4, Qu: 96.5, Tu: 125}
HTB_SPC_F8T[M20] = {DIA: 20, HOLE_DIA: 22, Qal: 33.5, Qas: 50.2, Tal: 78.5, Tas: 117.0, Qu: 151, Tu: 196}
HTB_SPC_F8T[M22] = {DIA: 22, HOLE_DIA: 24, Qal: 40.5, Qas: 60.8, Tal: 95.0, Tas: 142.0, Qu: 182, Tu: 242}
HTB_SPC_F8T[M24] = {DIA: 24, HOLE_DIA: 26, Qal: 48.2, Qas: 72.3, Tal: 113.0, Tas: 169.0, Qu: 217, Tu: 282}
HTB_SPC_F8T[M27] = {DIA: 27, HOLE_DIA: 30, Qal: 61.0, Qas: 91.5, Tal: 143.0, Tas: 214.0, Qu: 274, Tu: 367}
HTB_SPC_F8T[M30] = {DIA: 30, HOLE_DIA: 33, Qal: 75.4, Qas: 113.0, Tal: 177.0, Tas: 265.0, Qu: 339, Tu: 448}

# HTB_PROPNAME_UNIT = dict(DIA='mm', HOLE_DIA='mm', Qal='kN', Qas='kN', Tal='kN', Tas='kN', Qu='kN', Tu='kN')
HTB_PROPNAME_UNIT = {DIA: 'mm', HOLE_DIA: 'mm', Qal: 'kN', Qas: 'kN', Tal: 'kN', Tas: 'kN', Qu: 'kN', Tu: 'kN'}

# 6.8 BOLT  データの設定 AIJ S規準
BOLT_SPC_6T = {}
BOLT_SPC_6T[M12] = {DIA: 12, HOLE_DIA: 13, Qal: 13.6, Qas: 20.4, Tal: 23.6, Tas: 35.4}
BOLT_SPC_6T[M16] = {DIA: 16, HOLE_DIA: 17, Qal: 25.4, Qas: 38.1, Tal: 44.0, Tas: 65.9}
BOLT_SPC_6T[M20] = {DIA: 20, HOLE_DIA: 21.5, Qal: 39.6, Qas: 59.4, Tal: 68.6, Tas: 103.0}
BOLT_SPC_6T[M22] = {DIA: 22, HOLE_DIA: 23.5, Qal: 49.0, Qas: 73.5, Tal: 84.8, Tas: 127.0}
BOLT_SPC_6T[M24] = {DIA: 24, HOLE_DIA: 25.5, Qal: 57.1, Qas: 85.6, Tal: 98.8, Tas: 148.0}
BOLT_SPC_6T[M27] = {DIA: 27, HOLE_DIA: 28.5, Qal: 74.2, Qas: 111.0, Tal: 129.0, Tas: 193.0}
BOLT_SPC_6T[M30] = {DIA: 30, HOLE_DIA: 31.5, Qal: 90.7, Qas: 136.0, Tal: 157.0, Tas: 236.0}

# 4.8 BOLT データの設定
BOLT_SPC_4T = {}
BOLT_SPC_4T[M12] = {DIA: 12, HOLE_DIA: 13, Qal: 7.79, Qas: 11.7, Tal: 13.5, Tas: 20.2}
BOLT_SPC_4T[M16] = {DIA: 16, HOLE_DIA: 17, Qal: 14.5, Qas: 21.8, Tal: 25.1, Tas: 37.7}
BOLT_SPC_4T[M20] = {DIA: 20, HOLE_DIA: 21.5, Qal: 22.6, Qas: 33.9, Tal: 39.2, Tas: 58.8}
BOLT_SPC_4T[M22] = {DIA: 22, HOLE_DIA: 23.5, Qal: 28.0, Qas: 42.0, Tal: 48.5, Tas: 72.7}
BOLT_SPC_4T[M24] = {DIA: 24, HOLE_DIA: 25.5, Qal: 32.6, Qas: 48.9, Tal: 56.5, Tas: 84.7}
BOLT_SPC_4T[M27] = {DIA: 27, HOLE_DIA: 28.5, Qal: 42.4, Qas: 63.6, Tal: 73.4, Tas: 110.0}
BOLT_SPC_4T[M30] = {DIA: 30, HOLE_DIA: 31.5, Qal: 51.8, Qas: 77.7, Tal: 89.8, Tas: 135.0}

# BOLT_PROPNAME_UNIT = dict(DIA='mm', HOLE_DIA='mm', Qal='kN', Qas='kN', Tal='kN', Tas='kN')
BOLT_PROPNAME_UNIT = {DIA: 'mm', HOLE_DIA: 'mm', Qal: 'kN', Qas: 'kN', Tal: 'kN', Tas: 'kN'}


class ParameterError(Exception):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return repr(self.value)


def htb_spec_old(size=M16, prop_name=QA, term=LONG, strength=F10T, property_names=False, doc=False):
    """指定されたHTBの性能値を返す。

    サイズ(M16～M30)、性能名(QA/TA/DIA/HOLE_DIA)、長期・短期(LONG/SHORT)、HTB強度(F10T/F8T)を指定
    property_names=True でプロパティ名の一覧を返す
    doc=True でdocstringを返す
    return : 許容せん断力(kN)、許容引張力(kN)、軸径(mm)、孔径(mm)"""

    if doc:
        return htb_spec_old.__doc__

    if property_names:
        return PROPERTY_NAMES

    size, prop_name, term, strength = list(map(lambda w: w.upper(), [size, prop_name, term, strength]))

    if size in HTB_SIZES and prop_name in PROPERTY_NAMES and term in TERMS and strength in HTB_STRENGTHS:
        SPC = None
        if strength == F10T:
            SPC = HTB_SPC_F10T
        elif strength == F8T:
            SPC = HTB_SPC_F8T

        actual_prop = ''
        if prop_name == QA:
            if term == LONG:
                actual_prop = 'Qal'
            elif term == SHORT:
                actual_prop = 'Qas'
        elif prop_name == TA:
            if term == LONG:
                actual_prop = 'Tal'
            elif term == SHORT:
                actual_prop = 'Tas'
        elif prop_name == DIA:
            actual_prop = DIA
        elif prop_name == HOLE_DIA:
            actual_prop = HOLE_DIA

        return SPC[size][actual_prop]
    else:
        raise ParameterError('invalid parameter given')


def bolt_spec(size: str, prop_name: str, strength: str = B4T):
    """
    ボルトの性能値を返す。

    :param size: 'M12', 'M16', 'M20', 'M22', 'M24', 'M27', 'M30'
    :param prop_name: 'Dia', 'Hole_dia', 'Qal', 'Qas', 'Tal', 'Tas'
    :param strength: '4T', '6T'
    :return:
    """
    b_spc = {}

    if strength.upper() == B6T:
        b_spc = BOLT_SPC_6T
    elif strength.upper() == B4T:
        b_spc = BOLT_SPC_4T
    else:
        return 'NO_DATA'
    try:
        return b_spc[size.upper()][prop_name.capitalize()]
    except KeyError:
        return 'NO_DATA'


def htb_spec(size, prop_name, strength=F10T):
    """
    HTBの性能値を返す。

    :param size: 'M16', 'M20', 'M22', 'M24', 'M27', 'M30'
    :param prop_name: 'Dia', 'Hole_dia','Qal','Qas','Tal','Tas'
    :param strength: 'F8T', 'F10T'
    :return:
    """
    b_spc = {}

    if strength.upper() == F10T:
        b_spc = HTB_SPC_F10T
    elif strength.upper() == F8T:
        b_spc = HTB_SPC_F8T
    else:
        return 'NO_DATA'
    try:
        return b_spc[size.upper()][prop_name.capitalize()]
    except KeyError:
        return 'NO_DATA'


def xs_bolt_spec(strength, size, prop_name):
    """
    ボルト関連のデータを返す関数
    中ボルトとHTBを統一化する？

    :param strength:  F10T, F8T, 6T, 4T
    :param size:
    :param prop_name:
    :return:
    """
    if strength.upper() == F10T:
        b_spc = HTB_SPC_F10T
    elif strength.upper() == F8T:
        b_spc = HTB_SPC_F8T
    elif strength.upper() == B4T:
        b_spc = BOLT_SPC_4T
    elif strength.upper() == B6T:
        b_spc = BOLT_SPC_6T
    else:
        return 'NO_DATA'
    if prop_name.upper() == 'ALL' and (strength == F10T or strength == F8T):
        return xs_htb_all_property_names()
    elif prop_name.upper() == 'ALL' and (strength == B6T or strength == B4T):
        return xs_bolt_all_property_names()

    try:
        return b_spc[size.upper()][prop_name.capitalize()]
    except KeyError:
        return 'NO_DATA'

    # return htb_spec_old(size=size, prop_name=prop_name, strength=strength)


def xs_bolt_all_property_names():
    # return BOLT_SPC_4T[list(BOLT_SPC_4T.keys())[0]].keys()
    res = ''
    for name in BOLT_SPC_4T[list(BOLT_SPC_4T.keys())[0]].keys():
        res += '{}({}), '.format(name, BOLT_PROPNAME_UNIT[name])

    return res[:-2]


def xs_htb_all_property_names():
    res = ''
    for name in HTB_SPC_F10T[list(HTB_SPC_F10T.keys())[0]].keys():
        res += '{}({}), '.format(name, HTB_PROPNAME_UNIT[name])
    return res[:-2]
