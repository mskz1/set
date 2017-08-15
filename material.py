# -*- coding: utf-8 -*-
__author__ = 'mskz'

""" 材料定義など
"""
try:
    from . import ureg, Q_
except SystemError:
    from __init__ import ureg, Q_

import math


class Steel(object):
    def __init__(self, name="SS400", F=Q_(235, "N/mm**2"), E=Q_(205000.0, 'N/mm**2'),
                 G=Q_(79000.0, 'N/mm**2'), mu=0.3, cte=0.00012):
        self._name = name  # 名称
        self._F = F     # 設計基準強度（N/mm2）
        self._E = E     # ヤング係数（N/mm2）
        self._G = G     # せん断弾性係数(N/mm2)
        self._mu = mu   # ポアソン比
        self._cte = cte     # 線膨張係数（1/℃）

        self._lamuda = (((math.pi ** 2 * E) / (0.6*F))**0.5).magnitude


    def fc(self, lmd, rev=2003):
        """
        許容圧縮応力度を返す
        :param lmd:
                rev:鋼構造設計規準の版
        :return:
        """
        mu = 3.0/2.0 + 2.0/3.0 * ((lmd / self._lamuda)**2)
        if lmd <= self._lamuda:
            fc = (1.0-0.4*(lmd/self._lamuda)**2) * self._F / mu
        else:
            fc = 0.277 * self._F / ((lmd/self._lamuda)**2)
        return fc

    def fb(self, lb, i, C, h, Af):
        """
        許容曲げ応力度を返す　式(5.7,5.8)
        N/mm2
        lb :圧縮フランジの支点間距離(mm)
        i :断面二次半径(mm)
        C : 補正係数
        h :はりのせい(mm)
        Af :圧縮フランジの断面積(mm2)
        """

        fb1 = (1.0 - 0.4 * (lb/i)**2 /C / self._lamuda**2) * self.ft

        fb2 = self.fb2(lb, h, Af)

        fb = min(max(fb1, fb2), self.ft)

        return fb

    def fb2(self, lb, h, Af):
        """
        許容曲げ応力度を返す　式(5.8)
        みぞ形断面など
        """
        fb2 = 89000.0 / (lb * h / Af)

        fb = min(fb2, self.ft)

        return fb


    @property
    def F(self):
        return self._F

    @F.setter
    def F(self, value):
        self._F = value

    @property
    def ft(self):
        return self._F/1.5

    @property
    def fs(self):
        return self._F/(3**0.5*1.5)


    @property
    def name(self):
        return self._name


#-------------------------test code
if __name__ == '__main__':
    print("---テスト---")
    ss400 = Steel()
    print('Name:', ss400.name)
    print("F:", ss400.F)
    print("ft:", ss400.ft)
    a = Q_(23.5, "kN/cm**2")
    print ("Λ:",ss400._lamuda)
    print(a)
    pass
