# -*- coding: utf-8 -*-
__author__ = 'mskz'
try:
    from pint import UnitRegistry

    ureg = UnitRegistry()
    Q_ = ureg.Quantity

except ModuleNotFoundError:
    pass
