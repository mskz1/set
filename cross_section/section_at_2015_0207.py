# -*- coding: utf-8 -*-
__author__ = 'mskz'

H_HOSOHABA = "HS-"
H_TYUUHABA = "HM-"
H_HIROHABA = "HW-"
KAKU_PIPE = "KP-"
ALL_SERIES = ["HS-", "HM-", "HW-", "KP-", "P-", "C-", "[-"]

HS = "HS-"
HM = "HM-"
HW = "HW-"
KP = "KP-"
P = "P-"
C = "C-"
MIZO = "[-"

ERROR = "(PROPERTY ERROR)"

# 断面シリーズ用定数
JIS_H_S = "JIS H形鋼 細幅"
JIS_H_M = "JIS H形鋼 中幅"
JIS_H_W = "JIS H形鋼 広幅"
STKR = "JIS 冷間成形角形鋼管"
PIPE = "JIS 鋼管"




# 断面特性用定数
An = "Gross sectional area"   # 全断面積
As = "sectional area for shear"  # せん断用断面積
Ix = "moment of inertia around x-axis"   # 断面２次モーメントX軸まわり
Iy = "moment of inertia around y-axis"   # 断面２次モーメントY軸まわり
Zx = "Section modulus around x-axis"  # 断面係数X軸まわり
Zy = "Section modulus around y-axis"  # 断面係数Y軸まわり

# 単位用定数
uMM = "mm"
uCM = "cm"


class SectionDB():
    """
    鋼材断面のデータベースクラス
    """

    def __init__(self):
        self._sections = {}
        self._sections_name = []
        self._section_series = None

    def load(self, csd_file="section.dat", series="ALL"):
        self._sections, self._sections_name, self._section_series = load_dat(series)

    def get_section(self, section_name):
        return self._sections[section_name]

    def get_list(self):
        return self._sections_name

class Section(object):
    """
    鋼材断面クラス
    H形鋼、角形鋼管、鋼管、リップ付き軽量溝形鋼、溝形鋼など

    """

    def __init__(self, series_symbol, series_name, prop_name, prop_unit, prop_value,
                 name_symbol, name_keys):
        """
        # 引数
        # series_symbol 文字列
        # series_name 文字列
        # prop_name, prop_value, prop_unit リスト
        # name_symbol 文字列
        # name_keys リスト
        #
        """

        # 断面シリーズ記号
        self.seriesSymbol = series_symbol
        # 断面シリーズ名称
        self.series_name = series_name
        # 断面特性値（空ディクショナリ）
        self.propValue = {}
        # 断面特性値の単位（空ディクショナリ）
        self.propUnit = {}
        # 断面名の頭記号（H-,□P-,[-など）
        self.nameSymbol = name_symbol
        # 断面名で用いる特性名称キーワード
        self.nameKeys = name_keys

        # 断面シリーズ内の通し番号
        #self.id = id
        # 断面特性値の設定
        i = 0
        for key in prop_name:
            self.propValue[key] = prop_value[i]
            self.propUnit[key] = prop_unit[i]
            i += 1

    def get_name(self):
        # 断面名称を返す
        name = ""
        for key in self.nameKeys:
            name = name + self.propValue[key] + "x"
        # 最後の'x'を除く
        name = name[:-1]
        name = self.nameSymbol + name
        return name

    def get_prop(self, key):
        return self.propValue[key]

    # def print_name(self):
    #     # それぞれの断面に応じた名称を表示
    #     # 削除予定
    #     if (self.seriesSymbol == "HS-" or self.seriesSymbol == "HM-" or
    #             self.seriesSymbol == "HW-"):
    #         print("H-"+self.propValue['H']+"x"+self.propValue['B']
    #               + "x"+self.propValue['t1']+"x"+self.propValue['t2'])
    #
    #     elif self.seriesSymbol == "KP-":
    #         print("□P-"+self.propValue['H']+"x"+self.propValue['B']
    #               + "x"+self.propValue['t'])
    #
    #     elif self.seriesSymbol == "P-":
    #         print("P-"+self.propValue['D']+"x"+self.propValue['t'])
    #
    #     elif self.seriesSymbol == "C-":
    #         print("C-"+self.propValue['H']+"x"+self.propValue['B']
    #               + "x"+self.propValue['C']+"x"+self.propValue['t'])
    #
    #     elif self.seriesSymbol == "[-":
    #         print("[-"+self.propValue['H']+"x"+self.propValue['B']
    #               + "x"+self.propValue['t1']+"x"+self.propValue['t2'])
    #     else:
    #         print("---SECTION SERIES ERROR---")

    #断面特性--断面積An------------------------
    def get_An(self):
        try:
            return float(self.propValue['An'])
        except KeyError:
            return 0.0

    def get_An_unit(self):
        try:
            return self.propUnit['An']
        except KeyError:
            return ERROR

    def get_An_str(self):
        try:
            txt = "断面積A:"+self.propValue['An']+"("+self.get_An_unit()+")"
            return txt
        except KeyError:
            return ERROR

    #断面特性--断面係数X------------------------
    def get_Zx(self):
        try:
            return float(self.propValue['Zx'])
        except KeyError:
            return 0.0

    def get_Zx_unit(self):
        try:
            return self.propUnit['Zx']
        except KeyError:
            return ERROR

    #断面特性--断面係数Y------------------------
    def getZy(self):
        try:
            return float(self.propValue['Zy'])
        except KeyError:
            return 0.0

    def getZyUnit(self):
        try:
            return self.propUnit['Zy']
        except KeyError:
            return ERROR

    #断面特性--断面二次モーメントX------------------------
    def getIx(self):
        try:
            return float(self.propValue['Ix'])
        except KeyError:
            return 0.0

    def getIxUnit(self):
        try:
            return self.propUnit['Ix']
        except KeyError:
            return ERROR

    #断面特性--断面二次モーメントY------------------------
    def getIy(self):
        try:
            return float(self.propValue['Iy'])
        except KeyError:
            return 0.0

    def getIyUnit(self):
        try:
            return self.propUnit['Iy']
        except KeyError:
            return ERROR

    #断面特性--単位重量------------------------
    def get_weight(self):
        try:
            return float(self.propValue['W'])
        except KeyError:
            return 0.0

    def get_weight_unit(self):
        try:
            return self.propUnit['W']
        except KeyError:
            return ERROR

    #断面特性--断面二次半径------------------------
    def get_ix(self):
        try:
            return float(self.propValue['ix'])
        except KeyError:
            return 0.0

    def get_ix_unit(self):
        try:
            return self.propUnit['ix']
        except KeyError:
            return ERROR

    #断面特性--断面二次半径------------------------
    def get_iy(self):
        try:
            return float(self.propValue['iy'])
        except KeyError:
            return 0.0

    def get_iy_unit(self):
        try:
            return self.propUnit['iy']
        except KeyError:
            return ERROR

    #断面特性--各寸法------------------------
    def get_H(self):
        try:
            return float(self.propValue['H'])
        except KeyError:
            return 0.0

    def get_B(self):
        try:
            return float(self.propValue['B'])
        except KeyError:
            return 0.0

    def get_t2(self):
        try:
            return float(self.propValue['t2'])
        except KeyError:
            return 0.0

    def get_t1(self):
        try:
            return float(self.propValue['t1'])
        except KeyError:
            return 0.0

    #断面特性--断面二次半径-曲げ用------------------------
    def get_ib(self):
        try:
            return float(self.propValue['ib'])
        except KeyError:
            return 0.0

    def get_ib_unit(self):
        try:
            return self.propUnit['ib']
        except KeyError:
            return ERROR

    #断面特性--η-曲げ用------------------------
    def get_eta(self):
        try:
            return float(self.propValue['η'])
        except KeyError:
            return 0.0

    def get_eta_unit(self):
        try:
            return self.propUnit['η']
        except KeyError:
            return ERROR

    #断面特性などの表示--曲げ材用------------------------
    def show_prop(self):
        print("Section Property")
        print(" Name : ", self.get_name())
        print(" An : ", self.get_An(), self.get_An_unit())
        print(" Ix : ", self.getIx(), self.getIxUnit())
        print(" Zx : ", self.get_Zx(), self.get_Zx_unit())
        print(" ib : ", self.get_ib(), self.get_ib_unit())

    #断面特性などの表示--すべて表示------------------------
    def show_all_prop(self):
        print("-"*40)
        print("--Section Property")
        print(" Name : ", self.get_name())
        print(self.propValue.keys())
        for key in self.propValue.keys():
            print(" %s : %s (%s)" % (key, self.propValue[key],
                                     self.propUnit[key]))


def load_dat(series="ALL"):
    # ファイルから読み込んだ断面データのディクショナリを返す
    #
    # 断面データ
    sec_dat = {}
    # 断面名称のリスト　ファイルの並び順となる
    name_list = []
    # 断面シリーズの集合
    series_set = {""}

    ifile = open("section.dat", "r", encoding="shift-jis")
    lines = ifile.readlines()
    series_symbol = ""

    if series == "ALL":
        target_series = ALL_SERIES
    else:
        target_series = series

    #ファイルから読み込み
    for line in lines:
        if line[0] != "#":
            words = line.strip().split(",")
            # words = string.split(string.strip(line), ",")
            if words[0] == "SERIES":
                series_symbol = words[1]
                series_set.add(series_symbol)
                series_name = words[2]

            if words[0] == "FORMAT":
                nameSymbol = words[1]
                nameKeys = words[2:]

            if words[0] == "PROPERTY":
                propName = [s.strip() for s in words[1:]]
                # propName = map(string.strip(), words[1:])

            if words[0] == "UNIT":
                propUnit = [s.strip() for s in words[1:]]
                # propUnit = map(string.strip, words[1:])

            if (words[0] == series_symbol) and (words[0] in target_series):
                propValue = [s.strip() for s in words[1:]]
                # propValue = map(string.strip, words[1:])
                sec = Section(series_symbol, series_name, propName, propUnit,
                              propValue, nameSymbol, nameKeys)
                sec_dat[sec.get_name()] = sec
                name_list.append(sec.get_name())
    ifile.close()
    return sec_dat, name_list, series_set


#------------------------------------------------------------------
def _test2():
    secHSD, secHSL = load_dat(series=HS)
    secHMD, secHML = load_dat(series=HM)
    secHSD["H-500x200x10x16"].show_all_prop()
    secHMD["H-390x300x10x16"].show_all_prop()

##    for name in secHML:
##        print secHMD[name].showAllProp()


def _test3():
    secHSD, secHSL = load_dat(series=HS)
    secHMD, secHML = load_dat(series=HM)
    secHWD, secHWL = load_dat(series=HW)
    L = secHSL+secHML+secHWL
    for b in L:
        print('"'+b+'"'+' :"B",')

def _test4():
    db = SectionDB()
    db.load()
    print(db._section_series)
    print("-"*40)
    for s in db.get_list():
        print(s)
    print("-"*40)
    s = db.get_section(db.get_list()[4])
    s.show_prop()

#====================================================================
if __name__ == "__main__":
    # _test3()
    # import os
    # print(os.getcwd())
    # _test2()
    _test4()
