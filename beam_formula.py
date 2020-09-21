# -*- coding: utf-8 -*-
__author__ = 'mskz'
from collections import namedtuple


# Cantilever with End Load - T301
# Cantilever with Intermediate Load - T302
# Cantilever with Uniform Load - T303
# Cantilever with Moment Load - T304
# Simple Supports with Center Load - T305
# Simple Supports with Intermediate Load - T306
# Simple Supports with Uniform Load - T307
# Simple Supports with Moment Load - T308
# Simple Supports with Twin Loads - T309
# Simple Supports with Overhanging Load - T310
# Propped Cantilever with Center Load - T311
# Propped Cantilever with Intermediate Load - T312
# Propped Cantilever with Uniform Load - T313
# Fixed Beam with Center Load - T314
# Fixed Beam with Intermediate Load - T315
# Fixed Beam with Uniform Load - T316

# -----------------------------------------------
# Simply Supported Beam with a Centered Load
# 単純梁＿中央集中荷重
#
# def M_SSB_CL(L=0.0,P=0.0):
#    return P * L / 4.0
#
# def D_SSB_CL(L=0.0, P=0.0, E=20500.0, I=0.0):
#    return  P * L**3 / (48.0 * E * I) *10.0
#

# ----------------------------------------------

# load_type = dict(UDL='uniform distributed load',)
class LoadType:
    UDL = 'Uniform Distributed Load'
    UIL = 'Uniformly Increasing Load to One End'
    PDL = 'Partial Distributed Load'

    PLC = 'Point Load at Center'
    PLA = 'Point Load at Any'


# DistributedLoad = namedtuple('DistributedLoad','value')
# PointLoad = namedtuple('PointLoad','value position')

def uniform_distributed_load(load=0.0):
    ld = Load(load_type=Load.DL)
    ld.value = load
    return ld


def point_load_at_center(load=0.0):
    ld = Load(load_type=LoadType.PLC)
    ld.value = load
    return ld


class Load:
    DL = 'DistributedLoad'
    PL = 'PointLoad'

    def __init__(self, load_type=DL):
        self._type = load_type
        # 分布荷重
        self._distributed_load1 = 0.  # 分布荷重　始端側
        self._distributed_load2 = 0.  # 分布荷重　終端側
        self._distributed_load_position1 = 0.  # 分布荷重　始端位置
        self._distributed_load_position2 = 0.  # 分布荷重　終端位置

        self._point_load = 0.
        self._point_load_position = 0.

    @staticmethod
    def uniform_distributed_load(value):
        ld = Load(load_type=Load.DL)
        ld._distributed_load1 = value
        ld._distributed_load2 = value
        return ld

    @property
    def type(self):
        return self._type

    @property
    def value(self):
        if self.type == Load.DL:
            return self._distributed_load1

    @value.setter
    def value(self, val):
        if self.type == Load.DL:
            self._distributed_load1 = val


class AbstractBeamFormula(object):
    # 抽象クラス
    def __init__(self):
        pass

    def calcM(self):
        pass

    def printResult(self):
        propKeys = self.__dict__.keys()

        for key in propKeys:
            print(key, ":", self.__dict__[key])

    def getR1(self):
        # 始点側反力を返す
        pass

    def getR2(self):
        # 終点側反力を返す
        pass

    def getM_at_n(self, n):
        # モーメント値を返す（部材をn分割する？）
        pass

    def getM_at(self, a):
        # モーメント値を返す（指定位置）
        pass

    def getD_at_n(self, n, E, I):
        # たわみ値を返す（部材をn分割する？）
        pass

    def getD_at(self, n, E, I):
        # たわみ値を返す（部材をn分割する？）
        pass

    def getMmax(self):
        # 最大モーメント値を返す
        pass

    def getDmax(self, E, I):
        # 最大たわみ値を返す
        pass

    def getMcenter(self):
        # スパン中央位置のモーメント値を返す
        pass

    def getDcenter(self, E, I):
        # スパン中央位置のたわみ値を返す
        pass


# ----------------------------

def simply_supported_beam_udl():
    pass


class SimplySupportedBeam:
    def __init__(self, span, load_type=LoadType.UDL, **param):
        self._span = span
        self._param = param
        self._load_type = load_type

    def param(self):
        return self._param


class SimplySupportedBeamWithUniformDistributedLoad(AbstractBeamFormula):
    """
    単純ばり公式　等分布荷重作用
    """

    def __init__(self, span, load):
        self._span = span
        self._load = load

    def getMmax(self):
        return self._load * self._span ** 2 / 8.

    def getR1(self):
        return self._load * self._span / 2.

    def getR2(self):
        return self._load * self._span / 2.

    def getMcenter(self):
        return self.getMmax()

    def getDmax(self, I=1.0, E=20500.):
        """
        最大変形量を算出
        :param I: 断面２次モーメント[cm4]
        :param E: ヤング係数[kN/cm2]
        :return:変形量[cm]
        """
        return 5 * self._load * 0.01 * (self._span * 100) ** 4 / (384 * E * I)

    def getM_at(self, a):
        return (self._load * a / 2) * (self._span - a)

    def getD_at(self, a, I=1.0, E=20500.):
        return self._load * 0.01*a*100 *((self._span * 100) ** 3-2* (self._span * 100)*(a*100)**2+(a*100)**3)/ (24*E*I)
