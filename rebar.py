# -*- coding: utf-8 -*-


D_BAR_SIZE = ['D6', 'D8', 'D10', 'D13', 'D16', 'D19', 'D22', 'D25', 'D29', 'D32', 'D35', 'D38', 'D41', 'D51']

D6, D8, D10, D13, D16, D19, D22, D25, D29, D32, D35, D38, D41, D51 = D_BAR_SIZE

PROPERTY_NAMES = ['d', 'DO', 'A', 'L']
PROPERTY_UNITS = ['mm', 'mm', 'mm**2', 'mm']
# 公称直径(mm), 最外径(mm), 断面積(mm2), 周長(mm) JIS G3112
d, DO, A, L = PROPERTY_NAMES

PROPERTY_INFO = []
for name, unit in zip(PROPERTY_NAMES, PROPERTY_UNITS):
    PROPERTY_INFO.append("{}({})".format(name, unit))

DEFORMED_BAR_SPEC = {}
DEFORMED_BAR_SPEC[D6] = {d: 6.35, DO: 7, A: 31.67, L: 20}
DEFORMED_BAR_SPEC[D8] = {d: 7.94, DO: 9, A: 49.51, L: 25}
DEFORMED_BAR_SPEC[D10] = {d: 9.53, DO: 11, A: 71.33, L: 30}
DEFORMED_BAR_SPEC[D13] = {d: 12.7, DO: 14, A: 126.7, L: 40}
DEFORMED_BAR_SPEC[D16] = {d: 15.9, DO: 18, A: 198.6, L: 50}
DEFORMED_BAR_SPEC[D19] = {d: 19.1, DO: 21, A: 286.5, L: 60}
DEFORMED_BAR_SPEC[D22] = {d: 22.2, DO: 25, A: 387.1, L: 70}
DEFORMED_BAR_SPEC[D25] = {d: 25.4, DO: 28, A: 506.7, L: 80}
DEFORMED_BAR_SPEC[D29] = {d: 28.6, DO: 33, A: 642.4, L: 90}
DEFORMED_BAR_SPEC[D32] = {d: 31.8, DO: 36, A: 794.2, L: 100}
DEFORMED_BAR_SPEC[D35] = {d: 34.9, DO: 40, A: 956.6, L: 110}
DEFORMED_BAR_SPEC[D38] = {d: 38.1, DO: 43, A: 1140, L: 120}
DEFORMED_BAR_SPEC[D41] = {d: 41.3, DO: 46, A: 1340, L: 130}
DEFORMED_BAR_SPEC[D51] = {d: 50.8, DO: 58, A: 2027, L: 160}


def rebar_spec(name="", prop_name='ALL'):
    if name != "" and name[0] == 'D':
        if prop_name in PROPERTY_NAMES:
            return DEFORMED_BAR_SPEC[name][prop_name]

    if prop_name == 'ALL':
        return PROPERTY_INFO


def rebar_size_list():
    # return D_BAR_SIZE
    res = '[ '
    for d in D_BAR_SIZE:
        res += d + ', '
    return res[:-2] + ' ]'
