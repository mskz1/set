# -*- coding: utf-8 -*-
__author__ = 'mskz'

import material

from material import ureg, Q_
from material import steel_spec
from pytest import approx


# from .. import ureg, Q_
# try:
#     from .. import ureg, Q_
# except SystemError:
#     from ..__init__ import ureg, Q_

def test_pint():
    l = Q_(1, 'm')
    assert l == Q_(100., 'cm')


def test_material_steel():
    ss400 = material.Steel(F=Q_(235, 'N/mm**2'))
    # print (ss400.F)
    assert ss400.F == Q_(235, "N/mm**2")
    assert ss400.F == Q_(23500, "N / centimeter ** 2")
    assert ss400.ft == Q_(156.66666666666666, 'N/mm**2')
    # assert ss400.ft == Q_(15.666666666666666, 'kN/cm**2')
    assert '{:8.4f}'.format(ss400.ft.to('kN/cm**2').magnitude).strip() == '15.6667'
    assert ss400.ft.magnitude == approx(156.66667)
    assert ss400.ft.to('kN/cm**2').magnitude == approx(15.666667)
    # print(ss400.ft.to('kN/cm**2'))
    # print( type(ss400.ft.to('kN/cm**2').magnitude))
    # print( '{:10.4f}'.format(ss400.ft.to('kN/cm**2').magnitude))

    sm = material.Steel(F=Q_(32.5, 'kN/cm**2'))
    assert sm.F == Q_(325, 'N/mm**2')


def test_material_1():
    assert steel_spec(name='SS400', data_name='F') == 235
    assert steel_spec(name='SS400', data_name='SIGMA_U') == 400
