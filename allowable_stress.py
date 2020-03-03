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


def steel_fc_aij(F=235, lambda_=100):
    """
    長期許容圧縮応力度(N/mm2)を返す。日本建築学会版
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


def steel_fc_bsl(F=235, lambda_=100):
    """
    長期許容圧縮応力度(N/mm2)を返す。建築基準法(Building Standard Law)版
    :param F:F値(N/mm2)
    :param lambda_:細長比
    :return:
    """
    # critical slenderness ratio 限界細長比
    c_s_ratio = 1500. / (F / 1.5) ** 0.5
    if lambda_ <= c_s_ratio:
        mu = 3.0 / 2.0 + 2.0 / 3.0 * ((lambda_ / c_s_ratio) ** 2)
        fc = F * (1.0 - 2. / 5. * (lambda_ / c_s_ratio) ** 2) / mu
    else:
        fc = (18. / 65.) * F / ((lambda_ / c_s_ratio) ** 2)
    return fc


def steel_fb_aij(F=235, lb=0, i=0, C=1, h=100, Af=30):
    """
    許容曲げ応力度を返す　式(5.7,5.8)
    N/mm2
    lb :圧縮フランジの支点間距離(mm)
    i :断面二次半径(mm)
    C : 補正係数
    h :はりのせい(mm)
    Af :圧縮フランジの断面積(mm2)
    """
    fb1 = steel_fb1_aij(F, lb, i, C)
    fb2 = steel_fb2_aij(F, lb, h, Af)

    return min(max(fb1, fb2), steel_ft(F))


def steel_fb_bsl(F=235, lb=0, i=0, C=1, h=100, Af=30):
    fb1 = steel_fb1_bsl(F, lb, i, C)
    fb2 = steel_fb2_aij(F, lb, h, Af)

    return min(max(fb1, fb2), steel_ft(F))


def steel_fb1_aij(F=235, lb=0, i=0, C=1):
    c_s_ratio = (((math.pi ** 2 * E) / (0.6 * F)) ** 0.5)

    return (1.0 - 0.4 * (lb / i) ** 2 / C / c_s_ratio ** 2) * steel_ft(F)


def steel_fb1_bsl(F=235, lb=0, i=0, C=1):
    c_s_ratio = 1500. / (F / 1.5) ** 0.5
    return F * ((2. / 3.) - (4. / 15.) * (lb / i) ** 2 / (C * c_s_ratio ** 2))


def steel_fb2_aij(F=235, lb=0, h=100, Af=30):
    """
    許容曲げ応力度を返す　AIJ_ASD_SS 式(5.8)
    みぞ形断面など
    """
    try:
        fb2 = 89000.0 / (lb * h / Af)
    except ZeroDivisionError:
        fb2 = steel_ft(F)

    fb = min(fb2, steel_ft(F))

    return fb
