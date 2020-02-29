# -*- coding: utf-8 -*-

import math

E = 205000.0  # ヤング係数 N/mm2


def steel_ft(F=235):
    """
    長期許容引張応力度(N/mm2)を返す。
    :param F: F値(N/mm2)
    :return:
    """
    return F / 1.5


def steel_fc(F=235, lambda_=100):
    """
    長期許容圧縮応力度(N/mm2)を返す。
    :param F:F値(N/mm2)
    :param lambda_:細長比
    :return:
    """
    # critical slenderness ratio 限界細長比
    c_s_ratio = (((math.pi ** 2 * E) / (0.6 * F)) ** 0.5)
    if lambda_ <= c_s_ratio:
        mu = 3.0 / 2.0 + 2.0 / 3.0 * ((lambda_ / c_s_ratio) ** 2)
        fc = (1.0 - 0.4 * (lambda_ / c_s_ratio) ** 2) * F / mu
    else:
        fc = 0.277 * F / ((lambda_ / c_s_ratio) ** 2)
    return fc

