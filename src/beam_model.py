# -*- coding: utf-8 -*-
__author__ = 'mskz'

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


class SimpleBeam(BeamModel):
    """
    単純はりのモデル
    """
    pass
