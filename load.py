# -*- coding: utf-8 -*-
__author__ = 'mskz'

try:
    from . import ureg, Q_
except SystemError:
    from __init__ import ureg, Q_

#load_type
DISTRIBUTED_LOAD = 1
POINT_LOAD = 2

LIVE_LOAD = "LIVE_LOAD"
DEAD_LOAD = "DEAD_LOAD"

#Basic Load Case 基本荷重ケース
BLC_G = 'BASIC_LOAD_CASE_G'
BLC_S = 'BLC_S'
BLC_P = 'BLC_P'
BLC_W = 'BLC_W'
BLC_K = 'BLC_K'

#Load Category 荷重カテゴリー
DL = 'DEAD_LOAD'
LL = 'LIVE_LOAD'
SL = 'SNOW_LOAD'
WL = 'WIND_LOAD'
EL = 'EARTH_QUAKE_LOAD'


class UnitLoad():
    """
    単位荷重の定義データ
    """

    def __init__(self, name="", value=Q_(300, 'N/m^2'), category=DL):
        self._name = name
        self._value = value
        self._category = category

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        self._value = value

    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, category):
        self._category = category


class LoadCaseDB():
    pass


class MemberLoad():
    pass
