# -*- coding: utf-8 -*-

from collections import namedtuple
from typing import Tuple


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
    # 不要？
    UDL = 'Uniform Distributed Load'
    UIL = 'Uniformly Increasing Load to One End'
    PDL = 'Partial Distributed Load'

    PLC = 'Point Load at Center'
    PLA = 'Point Load at Any'


# DistributedLoad = namedtuple('DistributedLoad','value')
# PointLoad = namedtuple('PointLoad','value position')

def uniform_distributed_load(load=0.0):
    # 不要？
    ld = Load(load_type=Load.DL)
    ld.value = load
    return ld


def point_load_at_center(load=0.0):
    # 不要？
    ld = Load(load_type=LoadType.PLC)
    ld.value = load
    return ld


class Load:
    # 不要？
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
    def __init__(self, span, load):
        self._span = span
        self._load = load

    @property
    def span(self):
        """はり公式のスパン"""
        return self._span

    @span.setter
    def span(self, span):
        self._span = span

    @property
    def load(self):
        return self._load

    @load.setter
    def load(self, load):
        self._load = load

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
        """最大モーメント値を返す"""
        # 最大モーメント値を返す
        pass

    def getDmax(self, E, I):
        """最大たわみ値を返す"""
        # 最大たわみ値を返す
        pass

    def getMcenter(self):
        """スパン中央位置のモーメント値を返す"""
        # スパン中央位置のモーメント値を返す
        pass

    def getDcenter(self, E, I):
        """スパン中央位置のたわみ値を返す"""
        # スパン中央位置のたわみ値を返す
        pass


class SimplySupportedBeam:
    # 不要？
    def __init__(self, span, load_type=LoadType.UDL, **param):
        self._span = span
        self._param = param
        self._load_type = load_type

    def param(self):
        return self._param


class SimplySupportedBeamWithUniformDistributedLoad(AbstractBeamFormula):
    """
    単純ばり公式　等分布荷重が作用する場合。　
    :param span: スパン（m）
    :param load: 荷重値（kN/m）
    """

    def __init__(self, span: float, load: float):
        try:  # python2
            super(AbstractBeamFormula, self).__init__(span, load)
        except TypeError:  # python3
            super().__init__(span, load)

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
        return self._load * 0.01 * a * 100 * (
                (self._span * 100) ** 3 - 2 * (self._span * 100) * (a * 100) ** 2 + (a * 100) ** 3) / (24 * E * I)


class SimpliSupportedBeamWithUniformlyIncreasingDistributedLoad(AbstractBeamFormula):
    """
    単純ばり公式　単純増加分布荷重が作用する場合。
    :param span: スパン（m）
    :param load: 荷重値（kN/m2）
    :param a: 荷重負担幅（m）端部位置での
    """

    def __init__(self, span, load, a):
        try:  # python2
            super(AbstractBeamFormula, self).__init__(span, load)
        except TypeError:  # python3
            super().__init__(span, load)
        self._a = a

    @property
    def a(self):
        return self._a

    @a.setter
    def a(self, a):
        self._a = a

    def getMmax(self):
        return 2 * self._span * self._span * self._a * self._load / (9 * 3 ** 0.5 * 2)

    def getR1(self):
        return (self._span * self._a / 2) / 3

    def getR2(self):
        return 2 * self.getR1()

    def getM_at(self, a):
        return a / (3 * self._span ** 2) * (1 / 2) * self._span * self._a * self._load * (self._span ** 2 - a ** 2)

    def getMcenter(self):
        return self.getM_at(self._span / 2)

    def getDmax(self, E=20500., I=1.0):
        """
        最大変形量を算出
        :param I: 断面２次モーメント[cm4]
        :param E: ヤング係数[kN/cm2]
        :return:変形量[cm]
        """

        return 0.01304 * ((self._span * 100.0) ** 3 / (E * I)) * (1 / 2) * (self._span * self._a * self._load)


class SimplySupportedBeamWithPointLoadAtCenter(AbstractBeamFormula):
    """
    単純ばり公式　中央集中荷重が作用する場合。
    :param span: スパン（m）
    :param load: 荷重値（kN）
    """

    def __init__(self, span, load):
        try:
            super(AbstractBeamFormula, self).__init__(span, load)
        except TypeError:
            super().__init__(span, load)

    def getMmax(self):
        return self._load * self._span / 4.

    def getMcenter(self):
        return self.getMmax()

    def getR1(self):
        return self._load / 2.

    def getR2(self):
        return self.getR1()

    def getDmax(self, I=1.0, E=20500.):
        """
        最大変形量を算出
        :param I: 断面２次モーメント[cm4]
        :param E: ヤング係数[kN/cm2]
        :return:変形量[cm]
        """
        return self._load * (self._span * 100) ** 3 / (48. * E * I)

    def getM_at(self, a):
        if a <= self._span / 2.:
            return self._load * a / 2
        elif a <= self._span:
            return self._load * (self._span - a) / 2.

    def getD_at(self, a, I=1.0, E=20500.):
        if a <= self._span / 2.:
            return self._load * (a * 100) * (3 * (self._span * 100) ** 2 - 4 * (a * 100) ** 2) / (48. * E * I)
        elif a <= self._span:
            b = self._span - a
            return self._load * (b * 100) * (3 * (self._span * 100) ** 2 - 4 * (b * 100) ** 2) / (48. * E * I)


class SimplySupportedBeamWithPointLoadAtAny(AbstractBeamFormula):
    """
    単純ばり公式　任意位置　集中荷重が作用する場合。
    :param span: スパン（m）
    :param load: 荷重値（kN）
    :param a: 荷重作用位置(m)　左端から
    """

    def __init__(self, span, load, a):
        try:
            super(AbstractBeamFormula, self).__init__(span, load)
        except TypeError:
            super().__init__(span, load)
        self._a = a
        self._b = self._span - self._a

    @property
    def a(self):
        return self._a

    @a.setter
    def a(self, a):
        self._a = a
        self._b = self._span - self._a

    def getMmax(self):
        return self._load * self._a * self._b / self._span

    def getMcenter(self):
        return self.getM_at(self._span / 2.)

    def getM_at(self, x):
        if x <= self._a:
            return self._load * self._b * x / self._span
        elif x <= self._span:
            return self._load * self._a * (self._span - x) / self._span

    def getR1(self):
        return self._load * self._b / self._span

    def getR2(self):
        return self._load * self._a / self._span

    def getDmax(self, I=1.0, E=20500.):
        """
        最大変形量を算出
        :param I: 断面２次モーメント[cm4]
        :param E: ヤング係数[kN/cm2]
        :return:変形量[cm]
        """
        P = self._load
        if self._a > self._b:
            a = self._a * 100.
            b = self._b * 100.
        else:
            a = self._b * 100.
            b = self._a * 100.
        L = self._span * 100.

        return P * a * b * (a + 2 * b) * ((3 * a * (a + 2 * b)) ** 0.5) / (27. * E * I * L)

    def getD_at(self, x, I=1.0, E=20500.):

        P = self._load
        a = self._a * 100.
        b = self._b * 100.
        L = self._span * 100.
        x1 = x * 100.

        if x <= self._a:
            return P * b * x1 * (L ** 2 - b ** 2 - x1 ** 2) / (6. * E * I * L)
        elif x <= self._span:
            return P * a * (L - x1) * (2 * L * x1 - x1 ** 2 - a ** 2) / (6. * E * I * L)

    def getD_npoints(self, n, E=20500., I=1.0):
        # スパンをn分割した点ごとのたわみをリストで返す
        result = []
        for pos in self.get_points(n):
            result.append(self.getD_at(pos, I, E))
        return result

    def getM_npoints(self, n):
        # スパンをn分割した点ごとのモーメントをリストで返す
        result = []
        for pos in self.get_points(n):
            result.append(self.getM_at(pos))
        return result

    def get_points(self, n):
        # スパンをn分割した座標値をリストで返す。最初の要素は0,最後はスパン
        segment = self._span / n
        points = [segment * i for i in range(n)]
        points.append(self._span)
        return points


class SimplySupportedBeamWithMultiplePointLoad(AbstractBeamFormula):
    """
    単純ばり公式　n点集中荷重（均等配置）が作用する場合。
    :param span: スパン（m）
    :param load: 荷重値（kN）
    """

    def __init__(self, span, load, n: int = 2):
        try:
            super(AbstractBeamFormula, self).__init__(span, load)
        except TypeError:
            super().__init__(span, load)
        self._n = n

    def getMmax(self):
        n = self._n
        if n % 2 == 0:
            return self._load * self._span * (1 / 8) * n * (n + 2) / (n + 1)
        else:
            return self._load * self._span * (1 / 8) * (n + 1)

    def getMcenter(self):
        return self.getMmax()

    def getR1(self):
        return self._load * self._n / 2.

    def getR2(self):
        return self.getR1()

    def getDmax(self, I=1.0, E=20500.):
        """
        最大変形量を算出
        :param I: 断面２次モーメント[cm4]
        :param E: ヤング係数[kN/cm2]
        :return: 変形量[cm]
        """
        n = self._n
        if n % 2 == 0:
            return (self._load * (self._span * 100) ** 3 * n * (n + 2) * (5 * n ** 2 + 10 * n + 6) / (n + 1) ** 3) / (
                    384. * E * I)
        else:
            return (self._load * (self._span * 100) ** 3 * (5 * n ** 2 + 10 * n + 1) / (n + 1)) / (384. * E * I)

    # def getM_at(self, a):
    #     pass

    # def getD_at(self, a, I=1.0, E=20500.):
    #     pass


def get_max_moment_and_disp_with_multiple_point_load(span: float, load: float, n: int, I: float = 1.0,
                                                     E: float = 20500.) -> Tuple[float, float, float]:
    # 任意点集中荷重の公式の足し合わせにより、中央モーメント、中央たわみ、反力を求める。
    Mmax = 0.
    Dmax = 0.
    R1 = 0.
    load_points = [a * span / (n + 1) for a in range(n + 2)][1:-1]
    # print(load_points)
    for a in load_points:
        bf = SimplySupportedBeamWithPointLoadAtAny(span, load, a)
        Mmax += bf.getMcenter()
        Dmax += bf.getD_at(span / 2, I=I, E=E)
        R1 += bf.getR1()
    return Mmax, Dmax, R1


def add_list_contents(a, b):
    # 下記sum_listsで対応可能か。
    result = [x + y for (x, y) in zip(a, b)]
    return result


def sum_lists(*args):
    return list(map(sum, zip(*args)))
