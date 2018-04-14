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

short_full_name = dict(HS15='H-150x75x5x7', HS17='H-175x90x5x8', HS19='H-198x99x4.5x7', HS20='H-200x100x5.5x8',
                       HS24='H-248x124x5x8', HS25='H-250x125x6x9', HS29='H-298x149x5.5x8', HS30='H-300x150x6.5x9',
                       HS34='H-346x174x6x9', HS35='H-350x175x7x11', HS39='H-396x199x7x11',
                       HS40='H-400x200x8x13', HS44='H-446x199x8x12', HS45='H-450x200x9x14', HS49='H-496x199x9x14',
                       HS50='H-500x200x10x16', HS59='H-596x199x10x15', HS60='H-600x200x11x17',

                       HW100='H-100x100x6x8', HW125='H-125x125x6.5x9',
                       HW150='H-150x150x7x10', HW175='H-175x175x7.5x11', HW200='H-200x200x8x12',
                       HW250='H-250x250x9x14', HW300='H-300x300x10x15', HW350='H-350x350x12x19',
                       HW400='H-400x400x13x21',

                       HM148='H-148x100x6x9',
                       HM194='H-194x150x6x9', HM244='H-244x175x7x11', HM294='H-294x200x8x12', HM340='H-340x250x9x14',
                       HM390='H-390x300x10x16', HM440='H-440x300x11x18', HM488='H-488x300x11x18',
                       HM582='H-582x300x12x17', HM588='H-588x300x12x20',

                       MZ75='[-75x40x5x7', MZ100='[-100x50x5x7.5', MZ125='[-125x65x6x8',
                       MZ150_1='[-150x75x6.5x10', MZ150_2='[-150x75x9x12.5',
                       MZ180='[-180x75x7x10.5', MZ200_1='[-200x80x7.5x11', MZ200_2='[-200x90x8x13.5',

                       P272_19='P-27.2x1.9', P272_23='P-27.2x2.3', P427_23='P-42.7x2.3',
                       P486_23='P-48.6x2.3', P486_32='P-48.6x3.2', P605_23='P-60.5x2.3', P605_28='P-60.5x2.8',
                       P605_32='P-60.5x3.2', P763_28='P-76.3x2.8', P763_32='P-76.3x3.2',
                       P891_28='P-89.1x2.8', P891_32='P-89.1x3.2', P891_42='P-89.1x4.2',
                       P1016_32='P-101.6x3.2', P1016_35='P-101.6x3.5', P1016_42='P-101.6x4.2',
                       P1143_28='P-114.3x2.8', P1143_35='P-114.3x3.5', P1143_45='P-114.3x4.5', P1143_6='P-114.3x6',
                       P1398_35='P-139.8x3.5', P1398_4='P-139.8x4', P1398_45='P-139.8x4.5', P1398_5='P-139.8x5',
                       P1652_38='P-165.2x3.8', P1652_4='P-165.2x4', P1652_45='P-165.2x4.5', P1652_5='P-165.2x5',
                       P1907_53='P-190.7x5.3',

                       C60_16='C-60x30x10x1.6', C60_23='C-60x30x10x2.3', C75_16='C-75x45x15x1.6',
                       C75_23='C-75x45x15x2.3', C100_16='C-100x50x20x1.6', C100_23='C-100x50x20x2.3',
                       C100_32='C-100x50x20x3.2', C120_23='C-120x60x20x2.3', C120_32='C-120x60x20x3.2',
                       C125_32='C-125x50x20x3.2',

                        KP50_16='□P-50x50x1.6', KP50_23='□P-50x50x2.3', KP50_32='□P-50x50x3.2',
                       KP60_16='□P-60x60x1.6', KP60_23='□P-60x60x2.3', KP60_32='□P-60x60x3.2',
                       KP75_16='□P-75x75x1.6', KP75_23='□P-75x75x2.3', KP75_32='□P-75x75x3.2', KP75_45='□P-75x75x4.5',
                       KP100_23='□P-100x100x2.3', KP100_32='□P-100x100x3.2', KP100_45='□P-100x100x4.5',
                       KP100_6='□P-100x100x6.0', KP125_32='□P-125x125x3.2', KP125_45='□P-125x125x4.5',
                       KP125_6='□P-125x125x6.0',KP125_9='□P-125x125x9.0', KP150_45='□P-150x150x4.5',
                       KP150_6='□P-150x150x6.0', KP150_9='□P-150x150x9.0', KP175_45='□P-175x175x4.5',
                       KP175_6='□P-175x175x6.0', KP175_9='□P-175x175x9.0',
                       KP200_45='□P-200x200x4.5', KP200_6='□P-200x200x6.0', KP200_8='□P-200x200x8.0',
                       KP200_9='□P-200x200x9.0',
                       KP60_30_16='□P-60x30x1.6', KP60_30_23='□P-60x30x2.3', KP60_30_32='□P-60x30x3.2',
                       KP75_45_16='□P-75x45x1.6', KP75_45_23='□P-75x45x2.3',KP75_45_32='□P-75x45x3.2',
                       KP100_50_16='□P-100x50x1.6', KP100_50_23='□P-100x50x2.3', KP100_50_32='□P-100x50x3.2',
                       KP100_50_45='□P-100x50x4.5',
                       KP125_75_23='□P-125x75x2.3',KP_125_75_32='□P-125x75x3.2', KP_125_75_45='□P-125x75x4.5',
                       KP_125_75_6= '□P-125x75x6.0', KP_150_75_32='□P-150x75x3.2', KP_150_75_45='□P-150x75x4.5',
                       KP_150_100_32='□P-150x100x3.2',KP_150_100_45='□P-150x100x4.5', KP_150_100_6='□P-150x100x6.0',
                       KP200_100_45='□P-200x100x4.5', KP200_100_6='□P-200x100x6.0',
                       KP200_150_45='□P-200x150x4.5', KP200_150_6='□P-200x150x6.0', KP200_150_9='□P-200x150x9.0',
                       KP250_150_45='□P-250x150x4.5', KP250_150_6='□P-250x150x6.0', KP250_150_9='□P-250x150x9.0'
                       )

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


class SecParameter:
    """
    断面諸量データクラス　Pintを使わない試行
    """

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
                res += c
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


class SectionDB:
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
                    # self._sections[short_name] = sec
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


class Section:
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


class SectionProperty:
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
