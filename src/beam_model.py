# -*- coding: utf-8 -*-
__author__ = 'mskz'

# import dataclasses
from dataclasses import dataclass, field
from load import *   # インポートするパッケージの書き方で、Enumの等値性が変わる！！
from beam_formula import SimplySupportedBeamWithUniformDistributedLoad, SimplySupportedBeamWithMultiplePointLoad
from xs_section import make_section_db, short_full_name, HS_SEC_DATA, HM_SEC_DATA, HW_SEC_DATA
from xs_section import xs_section_property
from section_check import allowable_bending_moment

DIR_AROUND_XX = "xx"
DIR_AROUND_YY = "yy"


class BeamModel:
    """
    はりモデルのクラス


    """

    def __init__(self, span, n_support_xx=0, n_support_yy=0):
        self._span = span
        self._n_support_xx = n_support_xx  # 強軸方向の中間支点の数
        self._n_support_yy = n_support_yy  # 弱軸方向の中間支点の数
        self.load_case_xx = []  # 強軸方向の荷重ケースを登録するリスト
        self.load_case_yy = []

    @property
    def span(self):
        return self._span

    @span.setter
    def span(self, span):
        self._span = span

    def add_load_case(self, l_case, _dir=DIR_AROUND_XX):
        """
        荷重ケースを追加
        :param l_case:
        :param _dir:
        :return:
        """
        if _dir == DIR_AROUND_XX:
            self.load_case_xx.append(l_case)
        else:
            self.load_case_yy.append(l_case)

    def calc_stress(self):
        """
        応力解析を実行
        :return:
        """
        pass

    def output_result(self):
        """
        計算結果を出力
        :return:
        """
        pass


@dataclass
class SimpleBeamSteel:
    """
    鉄骨単純はりのモデル
    """
    span: float = 6000.  # (mm)
    section_name: str = ''  # 断面形状略号
    ld_reg: LoadRegistry = None
    Lb: float = 0.0  # 横座屈長さ（mm）
    F: float = 235.0  # 材料の基準強度（N/mm2）

    s_f_long = 0.96  # 検定比（長期）制限値
    s_f_short = 0.96  # 検定比（短期）制限値
    l_d_long = 300.0  # たわみ（長期）制限値　たわみ/スパン比の逆数
    l_d_short = 250.0  # たわみ（短期）制限値　たわみ/スパン比の逆数
    # beam_formulas: list = field(default_factory=list)
    lcombo_beamFormulas: dict[str, list] = field(default_factory=dict)

    sec_db = make_section_db(HS_SEC_DATA)

    def set_load_registry(self, reg):
        """荷重登録"""
        self.ld_reg = reg
        for lcombo in self.ld_reg.load_combo.keys():
            self.lcombo_beamFormulas[lcombo] = []

    def add_udl(self, lcombo: str, a: float):
        """UDL荷重登録"""
        w = self.ld_reg.get_as_distributed_load(lcombo, a / 1000.)
        self.lcombo_beamFormulas[lcombo].append(
            SimplySupportedBeamWithUniformDistributedLoad(self.span / 1000., w / 1000.))

    def add_n_pt_l(self, lcombo: str, p: float, n: int):
        # WIP:2024-0916
        """n-点集中荷重登録 ＊WIP＊"""
        self.lcombo_beamFormulas[lcombo].append(SimplySupportedBeamWithMultiplePointLoad(self.span / 1000., p, n))

    def get_max_internal_force(self, term=LoadTerm.LONG):
        """
        長期/短期を指定し、該当する荷重組合せによる部材応力（曲げモーメント）の最大値を返す
        :param term:
        :return:
        """
        lcombo_names = self.ld_reg.get_load_combo_names(term)
        m_max = []
        for label in lcombo_names:
            m = 0.
            for bf in self.lcombo_beamFormulas[label]:
                m += bf.getMmax()
            m_max.append(abs(m))  # 絶対値
        return max(m_max)

    def get_max_deflection(self, term=LoadTerm.LONG):
        """
        長期/短期を指定し、該当する荷重組合せによる部材たわみの最大値を返す
        :param term:
        :return:
        """
        lcombo_names = self.ld_reg.get_load_combo_names(term)
        d_max = []
        Ix = xs_section_property(short_full_name[self.section_name], 'Ix', self.sec_db)
        for label in lcombo_names:
            d = 0.
            for bf in self.lcombo_beamFormulas[label]:
                d += bf.getDmax(I=Ix)
            d_max.append(abs(d))  # 絶対値
        return max(d_max)

    def check_section(self):
        # FIXME:
        # print(LoadTerm.LONG == LoadTerm.LONG)
        # print(self.ld_reg.get_load_combo_names(LoadTerm.LONG))
        M_l = self.get_max_internal_force(LoadTerm.LONG)
        Mal = allowable_bending_moment(short_full_name[self.section_name], lb=self.Lb, term='LONG')
        s_f_long = M_l / allowable_bending_moment(short_full_name[self.section_name], lb=self.Lb, term='LONG')
        print(f'Ml= {M_l:.5f}, Mal= {Mal:.5f}')
        # WIP-2024-0916

        pass
