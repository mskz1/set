# -*- coding: utf-8 -*-
__author__ = 'mskz'

# import dataclasses
from dataclasses import dataclass, field
from load import *  # インポートするパッケージの書き方で、Enumの等値性が変わる！！
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
    応力は梁公式により、等分布荷重とｎ点集中荷重に対応
    """
    # todo: 後から荷重値の変更への対応　2024-0922
    # todo: 軸力対応
    # todo: 2軸曲げ対応
    # ---------------------------------
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
        """
        荷重登録をセット
        :param reg:
        :return:
        """
        self.ld_reg = reg
        for lcombo in self.ld_reg.load_combo.keys():
            self.lcombo_beamFormulas[lcombo] = []

    def add_udl(self, lcombo: str, a: float):
        """
        UDL　等分布荷重の追加
        :param lcombo: 荷重組合せ名
        :param a: 負担幅（mm）
        :return:
        """
        w = self.ld_reg.get_as_distributed_load(lcombo, a / 1000.)
        self.lcombo_beamFormulas[lcombo].append(
            SimplySupportedBeamWithUniformDistributedLoad(self.span / 1000., w / 1000.))

    def add_n_pt_l(self, lcombo: str, a: float, n: int):
        """
        n点集中荷重の追加
        :param lcombo: 荷重組合せ名
        :param a: 負担幅（mm）
        :param n: 荷重の数
        :return:
        """
        # self.lcombo_beamFormulas[lcombo].append(SimplySupportedBeamWithMultiplePointLoad(self.span / 1000., p, n))
        p = self.ld_reg.get_as_point_load(lcombo, a / 1000., (self.span / 1000.) / (n + 1))
        self.lcombo_beamFormulas[lcombo].append(
            SimplySupportedBeamWithMultiplePointLoad(self.span / 1000., p / 1000., n))

    def get_max_internal_force(self, term=LoadTerm.LONG):
        """
        長期/短期を指定し、該当する荷重組合せによる部材応力（曲げモーメント）の最大値を返す
        :param term:
        :return:
        """
        lcombo_names = self.ld_reg.get_load_combo_names(term)
        if lcombo_names:
            m_max = []
            for label in lcombo_names:
                m = 0.
                for bf in self.lcombo_beamFormulas[label]:
                    m += bf.getMmax()
                m_max.append(abs(m))  # 絶対値
            return max(m_max)
        else:
            return 0.0  # 該当の荷重種別の荷重状態が無い

    def get_max_deflection(self, term=LoadTerm.LONG):
        """
        長期/短期を指定し、該当する荷重組合せによる部材たわみ(cm)の最大値を返す
        :param term:
        :return:
        """
        lcombo_names = self.ld_reg.get_load_combo_names(term)
        if lcombo_names:
            d_max = []
            Ix = xs_section_property(short_full_name[self.section_name], 'Ix', self.sec_db)
            for label in lcombo_names:
                d = 0.
                for bf in self.lcombo_beamFormulas[label]:
                    d += bf.getDmax(I=Ix)  # cm
                d_max.append(abs(d))  # 絶対値
            return max(d_max)
        else:
            return 0.0  # 該当の荷重種別の荷重状態が無い

    def check_section(self, do_print=False):
        """
        鉄骨断面の断面算定結果を返す（長期検定比、短期検定比）のタプル
        :param do_print:
        :return:
        """
        M_l = self.get_max_internal_force(LoadTerm.LONG)
        Mal = allowable_bending_moment(short_full_name[self.section_name], lb=self.Lb, term='LONG')
        s_f_long = M_l / Mal

        d_long = self.get_max_deflection(LoadTerm.LONG) * 10  # cm -> mm

        M_s = self.get_max_internal_force(LoadTerm.SHORT)
        Mas = allowable_bending_moment(short_full_name[self.section_name], lb=self.Lb, term='SHORT')
        s_f_short = M_s / Mas

        d_short = self.get_max_deflection(LoadTerm.SHORT) * 10  # cm -> mm

        if do_print:
            print(f'Ml= {M_l:.5f}, Mal= {Mal:.5f}, Ml/Mal={s_f_long:.3f}')
            if d_long > 1e-6:
                print(f'd_l= {d_long:.5f} (mm), d/L= 1/{int(self.span / d_long)}')
            print(f'Ms= {M_s:.5f}, Mas= {Mas:.5f}, Ms/Mas={s_f_short:.3f}')
            if d_short > 1e-6:
                print(f'd_s= {d_short:.5f} (mm), d/L= 1/{int(self.span / d_short)}')

        return s_f_long, s_f_short
