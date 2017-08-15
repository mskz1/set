# -*- coding: utf-8 -*-
__author__ = 'mskz'

FORCE_UNIT_COEF = dict(kN=1000.0, N=1.0)

LENGTH_UNIT_COEF = dict(m=1000.0, cm=10.0, mm=1.0)

AREA_UNIT_COEF = dict(m2=1000000.0, cm2=100.0, mm2=1.0)  #長さから算出する？


#単位定義
kN = "kN"
N = "N"

m = "m"
mm = "mm"
cm = "cm"

m2 = "m2"
cm2 = "cm2"
mm2 = "mm2"

m3 = "m3"
cm3 = "cm3"
mm3 = "mm3"

kN_m = "kN/m"
N_m = "N/m"

kN_m2 = "kN/m2"
kN_cm2 = "kN/cm2"
N_mm2 = "N/mm2"

kNm = "kN*m"

# UNIT_KN = "kN"
# UNIT_N = "N"
# UNIT_M = "m"
# uMM = "mm"
# UNIT_CM = "cm"
# UNIT_M2 = "m2"
# UNIT_CM2 = "cm2"
# UNIT_MM2 = "mm2"
# UNIT_KN_M2 = "kN/m2"
# UNIT_KN_CM2 = "kN/cm2"
# UNIT_N_MM2 = "N/mm2"
# UNIT_KNxM = "kN*m"


class UaNum(object):
    """単位付き数値クラス
    """

    def __init__(self, val=0.0, unit=N):
        self._val = val
        self._unit = unit

    def __repr__(self):
        return "".join(map(str, [self._val, "[", self._unit, "]"]))

    def __add__(self, other):
        return UaNum(self.val + other.val)

    def _get_value(self, unit=N):
        return self._val

    val = property(_get_value)

def test1():
    print(LENGTH_UNIT_COEF)
    print(FORCE_UNIT_COEF)
    print(AREA_UNIT_COEF)

    f1 = UaNum(10., kN)
    f2 = UaNum(2000.)
    print(f1)
    print(f2)
    f3 = f1+f2
    print(f3)

    l1 = UaNum(5., m)
    l2 = UaNum(4000., mm)
    print(l1, l2)


#----------------------------------
if __name__ == '__main__':
    test1()