# -*- coding: utf-8 -*-
__author__ = 'mskz'


def test_material_steel():
    import material
    ss400 = material.Steel(F=400.)
    pass


if __name__ == '__main__':
    from x_material import steel
    print("F2 =", steel.F)
    print("ftサンプル =", steel.ft(steel.F[steel.SN400]))
    print("ヤング係数", steel.E)
    # steel.ft()