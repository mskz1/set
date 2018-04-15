# -*- coding: utf-8 -*-
__author__ = 'mskz'

import material

from material import ureg, Q_

from pytest import approx

# from .. import ureg, Q_

# try:
#     from .. import ureg, Q_
# except SystemError:
#     from ..__init__ import ureg, Q_


def test_material_steel():
    ss400 = material.Steel(F=Q_(235,'N/mm**2'))
    # print (ss400.F)
    assert ss400.F == Q_(235, "N/mm**2")
    assert ss400.F == Q_(23500, "N / centimeter ** 2")
    sm = material.Steel(F=Q_(32.5, 'kN/cm**2'))
    assert sm.F == Q_(325, 'N/mm**2')



    # if __name__ == '__main__':
    #     from x_material import steel
    #     print("F2 =", steel.F)
    #     print("ftサンプル =", steel.ft(steel.F[steel.SN400]))
    #     print("ヤング係数", steel.E)
    #     # steel.ft()
