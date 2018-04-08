# -*- coding: utf-8 -*-
__author__ = 'mskz'

try:
    from . import ureg, Q_
except ImportError:
    from __init__ import ureg, Q_

H_HOSOHABA_SERIES = "HS-"
H_TYUUHABA_SERIES = "HM-"
H_HIROHABA_SERIES = "HW-"
KAKU_PIPE_SERIES = "KP-"
PIPE_SERIES = "P-"
LIGHT_CHANNEL_SERIES = "C-"
CHANNEL_SERIES = "[-"

ALL_SERIES = ["HS-", "HM-", "HW-", "KP-", "P-", "C-", "[-"]

# HS = "HS-"
# HM = "HM-"
# HW = "HW-"
# KP = "KP-"
# P = "P-"
# C = "C-"
# MIZO = "[-"

ERROR = "(PROPERTY ERROR)"

# 断面シリーズ用定数
# JIS_H_S = "JIS H形鋼 細幅"
# JIS_H_M = "JIS H形鋼 中幅"
# JIS_H_W = "JIS H形鋼 広幅"
# STKR = "JIS 冷間成形角形鋼管"
# PIPE = "JIS 鋼管"

# 断面特性用定数
# An = "Gross sectional area"   # 全断面積
# As = "sectional area for shear"  # せん断用断面積
# Ix = "moment of inertia around x-axis"   # 断面２次モーメントX軸まわり
# Iy = "moment of inertia around y-axis"   # 断面２次モーメントY軸まわり
# Zx = "Section modulus around x-axis"  # 断面係数X軸まわり
# Zy = "Section modulus around y-axis"  # 断面係数Y軸まわり

# 単位用定数
uMM = "mm"
uCM = "cm"
uM = "m"


# def conversion_factor(src = uMM, dist = uMM):
#     # 単位変換の係数を返す
#     unit_conv_factor = {(uCM,uMM):10.0, (uM,uMM):1000.0, (uM,uCM):100.0}
#     if src == dist:
#         return 1.0
#     unit_con = (src, dist)
#     if unit_con in unit_conv_factor:
#         return unit_conv_factor[unit_con]
#     else:
#         unit_con = (dist, src)
#         return 1./unit_conv_factor[unit_con]


class SecParameter():
    '''
    断面諸量データクラス　Pintを使わない試行
    '''
    def __init__(self, name, value, unit):
        self._name = name
        self._value = value
        self._unit = unit

    def _unit_convert_factor(self, unit):
        unit_base_from = self._unit_base(self._unit)
        unit_base_to = self._unit_base(unit)
        if self._unit[-1] not in '123456789':
            unit_dim = 1
        else:
            unit_dim = int(self._unit[-1])
        if unit_base_from == uMM and unit_base_to == uCM:
            return 0.1 ** unit_dim
        if unit_base_from == uMM and unit_base_to == uM:
            return 0.001 ** unit_dim
        if unit_base_from == uCM and unit_base_to == uMM:
            return 10. ** unit_dim
        if unit_base_from == uCM and unit_base_to == uM:
            return 0.01 ** unit_dim
        if unit_base_from == uM and unit_base_to == uMM:
            return 1000. ** unit_dim
        if unit_base_from == uM and unit_base_to == uCM:
            return 100. ** unit_dim

    def _unit_base(self, unit):
        res = ''
        for c in unit:
            if c in '123456789':
                pass
            else:
                res+=c
        return res

    def get(self, unit=''):
        if unit == '':
            unit = self._unit
        if unit == self._unit:
            return self._value
        else:
            return self._value * self._unit_convert_factor(unit)

    def set(self, value, unit):
        self._value = value
        self._unit = unit


class SectionDB():
    """
    鋼材断面のデータベースクラス
    """

    def __init__(self):
        self._sections = {}  # 断面データ
        self._section_names = []  # 断面名称のリスト　ファイルの並び順となる
        self._section_series = None

    def load(self, csd_file="./cross_section/section.dat", series="ALL"):
        # ファイルから断面データを読み込む
        # 断面シリーズの集合
        series_set = {""}

        i_file = open(csd_file, "r", encoding="shift-jis")
        lines = i_file.readlines()
        series_symbol = ""

        if series == "ALL":
            target_series = ALL_SERIES
        else:
            target_series = series

        # ファイルから読み込み
        for line in lines:
            if line[0] != "#":
                words = line.strip().split(",")

                if words[0] == "SERIES":
                    series_symbol = words[1]
                    series_set.add(series_symbol)
                    series_name = words[2]

                if words[0] == "FORMAT":
                    # name_symbol = words[1]
                    name_format = words[1:]

                if words[0] == "PROPERTY":
                    prop_name = [s.strip() for s in words[1:]]

                if words[0] == "UNIT":
                    prop_unit = [s.strip() for s in words[1:]]

                if (words[0] == series_symbol) and (words[0] in target_series):
                    prop_value = [s.strip() for s in words[1:]]

                    # 断面特性値のセット
                    _prop = {}
                    for i, _name in enumerate(prop_name):
                        _prop[_name] = prop_value[i]
                    sec_name = name_format[0]
                    for kw in name_format[1:]:
                        sec_name += _prop[kw] + "x"
                    sec_name = sec_name[:-1]

                    for i, _name in enumerate(prop_name):
                        _prop[_name] = Q_(float(prop_value[i]), str(prop_unit[i]))

                    sec = Section(series_symbol, series_name, _prop, name_format)
                    sec.set_name(sec_name)
                    self._sections[sec_name] = sec
                    self._section_names.append(sec_name)
        i_file.close()

    def get_section(self, section_name):
        return self._sections[section_name]

    def get_list(self, series=""):
        """
        断面シリーズを指定して、部材名の一覧（リスト）を返す。
        デフォルトでは、全断面
        """
        if series == "":
            return self._section_names
        res = []
        for sec_name in self._section_names:
            if self._sections[sec_name].series_symbol == series:
                res.append(sec_name)
        return res


class Section():
    """
    鋼材断面クラス
    各種断面形状寸法、特性値を保持
    H形鋼、角形鋼管、鋼管、リップ付き軽量溝形鋼、溝形鋼など
    """

    def __init__(self, series_symbol, series_name, prop, name_form):
        """
        # 引数
        # series_symbol 文字列
        # series_name 文字列
        # prop ディクショナリ
        # name_form リスト
        #
        """
        # 断面名称
        self._name = ""
        # 断面シリーズ記号 ex) HS-,HM-,,,
        self._series_symbol = series_symbol
        # 断面シリーズ名称 ex) H形鋼細幅,角形鋼管,
        self._series_name = series_name
        # 断面特性値（空ディクショナリ）
        self._prop = prop

        # 断面名で用いる特性名称キーワード H,B,tw,tf
        # set_name で　popすると、書き換えられる？ため、コピーする
        self._name_form = name_form[:]

    # def set_name(self):
    #     """
    #     断面名称を設定
    #     """
    #     _name = self._name_form.pop(0)
    #     for k in self._name_form:
    #         _name += str(self._prop[k].magnitude) + "x"
    #     # 最後の'x'を除く
    #     self._name = _name[:-1]

    def set_name(self, name):
        """
        断面名称を設定
        """
        self._name = name

    @property
    def name(self):
        return self._name

    @property
    def series_symbol(self):
        return self._series_symbol

    def get_prop(self, prop_name):
        return self._prop[prop_name]


class SectionProperty():
    """
    断面特性データを保持するクラス
    """

    def __init__(self, name="", value=Q_(0, "mm")):
        self._name = name
        self._value = value

    @property
    def name(self):
        return self._name

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, val):
        self._value = val


# ------------------------------------------------------------------
# def _test1():
#     sp_H = SectionProperty("H",100.0)
#     #print(sp.value)
#     #print(sp.value(unit=uCM))
#     print(sp_H)
#     print(sp_H.name,":",sp_H.get_value(uCM),"cm",sp_H.dimension)
#     print(sp_H.name,":",sp_H.get_value(uM),"m",sp_H.dimension)
#
#     sp_A = SectionProperty("An",20.0,unit=uCM,dim=2)
#     print(sp_A)
#     print(sp_A.name,":",sp_A.get_value(uMM),"mm",sp_A.dimension)
#
#     sp_Z = SectionProperty("Zx",400.0,unit=uCM,dim=3)
#     print(sp_Z)
#     print(sp_Z.name,":",sp_Z.get_value(uMM),"mm",sp_Z.dimension)
#
#     sp_I = SectionProperty("Ix",1800.0,unit=uCM,dim=4)
#     print(sp_I)
#     print(sp_I.name,":",sp_I.get_value(uMM),"mm",sp_I.dimension)

def test2():
    sec_db = SectionDB()
    sec_db.load()
    # print(sec_db.get_list())
    print(sec_db.get_list(H_HOSOHABA_SERIES))
    print(sec_db.get_list(H_HIROHABA_SERIES))
    print(sec_db.get_list(H_TYUUHABA_SERIES))
    print(sec_db.get_list(KAKU_PIPE_SERIES))
    print(sec_db.get_list(PIPE_SERIES))
    print(sec_db.get_list(LIGHT_CHANNEL_SERIES))
    print(sec_db.get_list(CHANNEL_SERIES))


# ====================================================================
if __name__ == "__main__":
    import sys, os

    print(sys.path)
    print(os.getcwd())
    print("-----main run-----")
    # _test1()
    test2()
