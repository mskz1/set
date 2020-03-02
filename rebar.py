# -*- coding: utf-8 -*-


D_BAR_SIZE = ['D6', 'D8', 'D10', 'D13', 'D16', 'D19', 'D22', 'D25', 'D29', 'D32', 'D35', 'D38', 'D41']

D6, D8, D10, D13, D16, D19, D22, D25, D29, D32, D35, D38, D41 = D_BAR_SIZE

PROPERTY_NAMES = ['D', 'A', 'L']
PROPERTY_UNITS = ['mm', 'mm**2', 'mm']
# 最外径(mm), 断面積(mm2), 周長(mm)
D, A, L = PROPERTY_NAMES


PROPERTY_INFO = []
for name, unit in zip(PROPERTY_NAMES, PROPERTY_UNITS):
    PROPERTY_INFO.append("{}({})".format(name, unit))

DEFORMED_BAR_SPEC = {}
DEFORMED_BAR_SPEC[D6] = {D: 0, A: 32, L: 20}
DEFORMED_BAR_SPEC[D8] = {D: 0, A: 50, L: 25}
DEFORMED_BAR_SPEC[D10] = {D: 11, A: 71, L: 30}
DEFORMED_BAR_SPEC[D13] = {D: 15, A: 127, L: 40}


def rebar_spec(name="", prop_name='ALL'):
    if name != "" and name[0] == 'D':
        if prop_name in PROPERTY_NAMES:
            return DEFORMED_BAR_SPEC[name][prop_name]

    if prop_name == 'ALL':
        return PROPERTY_INFO
