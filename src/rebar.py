# -*- coding: utf-8 -*-
from enum import Enum


class Size(Enum):
    """
    鉄筋サイズ　呼び名
    """
    D6 = 'D6'
    D8 = 'D8'
    D10 = 'D10'
    D13 = 'D13'
    D16 = 'D16'
    D19 = 'D19'
    D22 = 'D22'
    D25 = 'D25'
    D29 = 'D29'
    D32 = 'D32'
    D35 = 'D35'
    D38 = 'D38'
    D41 = 'D41'
    D51 = 'D51'


class Property(Enum):
    """
    鉄筋の特性名
    """
    Diameter = 'd'  # diameter　[mm]鉄筋直径
    MaxOuterDiameter = 'DO'  # max_diameter [mm]最外径
    Area = 'A'  # area　[mm2]断面積
    Perimeter = 'L'  # perimeter　[mm]周長


D_BAR_SIZE = ['D6', 'D8', 'D10', 'D13', 'D16', 'D19', 'D22', 'D25', 'D29', 'D32', 'D35', 'D38', 'D41', 'D51']
D6, D8, D10, D13, D16, D19, D22, D25, D29, D32, D35, D38, D41, D51 = D_BAR_SIZE

PROPERTY_NAMES = ['d', 'DO', 'A', 'L']
PROPERTY_UNITS = ['mm', 'mm', 'mm**2', 'mm']
# 公称直径(mm), 最外径(mm), 断面積(mm2), 周長(mm) JIS G3112
d, DO, A, L = PROPERTY_NAMES

PROPERTY_INFO = []
for name, unit in zip(PROPERTY_NAMES, PROPERTY_UNITS):
    PROPERTY_INFO.append("{}({})".format(name, unit))

DEFORMED_BAR_SPEC = {}
DEFORMED_BAR_SPEC[D6] = {d: 6.35, DO: 7, A: 31.67, L: 20}
DEFORMED_BAR_SPEC[D8] = {d: 7.94, DO: 9, A: 49.51, L: 25}
DEFORMED_BAR_SPEC[D10] = {d: 9.53, DO: 11, A: 71.33, L: 30}
DEFORMED_BAR_SPEC[D13] = {d: 12.7, DO: 14, A: 126.7, L: 40}
DEFORMED_BAR_SPEC[D16] = {d: 15.9, DO: 18, A: 198.6, L: 50}
DEFORMED_BAR_SPEC[D19] = {d: 19.1, DO: 21, A: 286.5, L: 60}
DEFORMED_BAR_SPEC[D22] = {d: 22.2, DO: 25, A: 387.1, L: 70}
DEFORMED_BAR_SPEC[D25] = {d: 25.4, DO: 28, A: 506.7, L: 80}
DEFORMED_BAR_SPEC[D29] = {d: 28.6, DO: 33, A: 642.4, L: 90}
DEFORMED_BAR_SPEC[D32] = {d: 31.8, DO: 36, A: 794.2, L: 100}
DEFORMED_BAR_SPEC[D35] = {d: 34.9, DO: 40, A: 956.6, L: 110}
DEFORMED_BAR_SPEC[D38] = {d: 38.1, DO: 43, A: 1140, L: 120}
DEFORMED_BAR_SPEC[D41] = {d: 41.3, DO: 46, A: 1340, L: 130}
DEFORMED_BAR_SPEC[D51] = {d: 50.8, DO: 58, A: 2027, L: 160}


def make_deformed_bar_data():
    # Enum版のデータ生成
    sizes = [Size.D6, Size.D8, Size.D10, Size.D13, Size.D16, Size.D19, Size.D22, Size.D25, Size.D29, Size.D32, Size.D35,
             Size.D38, Size.D41, Size.D51]
    properties = [Property.Diameter, Property.MaxOuterDiameter, Property.Area, Property.Perimeter]
    #           d,DO, 　 　A, L
    data = [[6.35, 7, 31.67, 20],  # D6
            [7.94, 9, 49.51, 25],  # D8
            [9.53, 11, 71.33, 30],  # D10
            [12.7, 14, 126.7, 40],  # D13
            [15.9, 18, 198.6, 50],  # D16
            [19.1, 21, 286.5, 60],
            [22.2, 25, 387.1, 70],
            [25.4, 28, 506.7, 80],
            [28.6, 33, 642.4, 90],
            [31.8, 36, 794.2, 100],
            [34.9, 40, 956.6, 110],
            [38.1, 43, 1140, 120],
            [41.3, 46, 1340, 130],
            [50.8, 58, 2027, 160]]
    propertyName_data = []
    for d in data:
        propertyName_data.append({k: v for k, v in zip(properties, d)})

    result = {k: v for k, v in zip(sizes, propertyName_data)}
    return result


DEFORMED_BAR_SPEC2 = make_deformed_bar_data()


def rebar_spec2(size: Size, prop_name: Property):
    # 改良版 Enum利用
    return DEFORMED_BAR_SPEC2[size][prop_name]


def rebar_spec(name="", prop_name='ALL'):
    # if prop_name == 'ALL':
    #     return PROPERTY_INFO
    if prop_name == 'ALL':
        return str(PROPERTY_INFO)  # excel addin では、リストを直接返すとvalueエラーとなるため
    if name != "" and name[0] == 'D':
        if prop_name in PROPERTY_NAMES:
            try:
                return DEFORMED_BAR_SPEC[name][prop_name]
            except KeyError:
                return 'NO_DATA'


def rebar_size_list_as_string():
    # この関数必要か？
    # return D_BAR_SIZE
    res = '[ '
    for d in D_BAR_SIZE:
        res += d + ', '
    return res[:-2] + ' ]'


def rebar_size_list():
    # この関数必要か？
    return D_BAR_SIZE
