# -*- coding: utf-8 -*-
__author__ = 'mskz'

import math

"""
日本建築学会　鋼構造設計規準
　計算式モジュール


"""

from pint import UnitRegistry
ur = UnitRegistry()

#----------Constants----------------
# 鋼材種
SS400 = "SS400"
SM490 = "SM490"
STK400 = "STK400"
STKR400 = "STKR400"

SN400 = "SN400"
SN490 = "SN490"

BCR295 = "BCR295"



# ヤング係数(N/mm2)
E = 205000.0
# E = 205000.0 * ur("N/mm^2")

# せん断弾性係数(N/mm2)
G = 79000.0

# ポアソン比
MU = 0.3

# F値(N/mm2)
# F = { "400":235.0, "490":325.0}
F = dict(SS400=235.0, SM490=325.0, STK400=235.0, STKR400=235.0,
         SN400=235.0, SN490=325.0, BCR295=295.0)

# 線膨張係数（1/℃）
CTE = 0.000012


#----------------Functions---------
#----------------------------------
def ft(F_value):
    """
    許容引張応力度を返す　式(5.1)
    入力単位：N/mm2、出力単位：N/mm2
    :rtype : double
    :param F_value: double
    """
    return F_value/1.5


#----------------------------------
def fs(F_value):
    """
    許容せん断応力度を返す　式(5.2)
    N/mm2
    """
    return F_value/3.0**0.5/1.5


#----------------------------------
def lamuda(F_value):
    """
    限界細長比Λを返す　式(5.5)
    """
    return (math.pi**2 * E / (0.6*F_value))**0.5


#----------------------------------
def calcC(m2, m1):
    """
    許容曲げ応力度算定用係数Ｃを返す　式(-)
    m1,m2 :座屈区間端部のモーメント
    """
    if m2 <= m1:
        a = m2/m1
    else:
        a = m1/m2

    C = 1.75 - 1.05*a + 0.3*(a**2)
    if C <= 2.3:
        return C
    else:
        return 2.3


#----------------------------------
def fb(F_value, lb, i, C, h, Af):
    """
    許容曲げ応力度を返す　式(5.7,5.8)
    N/mm2
    lb :圧縮フランジの支点間距離(mm)
    i :断面二次半径(mm)
    C : 補正係数
    h :はりのせい(mm)
    Af :圧縮フランジの断面積(mm2)
    """

    _fb1 = (1.0 - 0.4 *(lb/i)**2 / C / lamuda(F_value)**2) * ft(F_value)
    _fb2 = 89000.0 / (lb*h / Af)

    return min(max(_fb1, _fb2), ft(F_value))


#----------------------------------
def fb2(F_value, lb, h, Af):
    """
    許容曲げ応力度を返す　式(5.8)
    みぞ形断面など
    """
    _fb2 = 89000.0 / (lb*h / Af)

    return min(_fb2, ft(F_value))


#----------------------------------
def fc(F_value, lk, i):
    """
    許容圧縮応力度を返す　式(5.3)(5.4)

    lamuda :限界細長比
    lk :座屈長さ(mm)
    i :座屈軸についての断面二次半径(mm)

    """
    lam = lk/i
    mu = 3.0/2.0 + 2.0/3.0*((lam/lamuda(F_value))**2)
    if lam <= lamuda(F_value):
        res_fc = (1.0-0.4*(lam/lamuda(F_value))**2) * F_value / mu
    else:
        res_fc = 0.277 * F_value / ((lam/lamuda(F_value))**2)

    return res_fc

#-------------------------test code
if __name__ == '__main__':
    print("---テスト---")
    # print("{:~}".format(E))
    pass
