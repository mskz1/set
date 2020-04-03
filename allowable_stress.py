# -*- coding: utf-8 -*-

import math

E = 205000.0  # ヤング係数 N/mm2  (20500 kN/cm2)
G = 79000.0  # せん弾弾性係数 N/mm2 (7900 kN/cm2)


def steel_ft(F=235):
    """
    長期許容引張応力度(N/mm2)を返す。
    :param F: F値(N/mm2)
    :return: ft(N/mm2)
    """
    return F / 1.5


def steel_fs(F=235):
    """
    長期許容せん断応力度（N/mm2）を返す。
    :param F:
    :return:
    """
    return F / (1.5 * 3 ** 0.5)


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


def steel_fb_aij2002(shape_name, db, lb=0, M1=0, M2=0, M3=0, F=235):
    ib = db[shape_name][0]['ib']  # cm
    C = calc_C(M1, M2, M3)  # TODO :内容check　2002と2005でM2/M1の符号の取り方変更有。結果の意味は同じ
    h = db[shape_name][0]['H']  # mm
    Af = db[shape_name][0]['B'] * db[shape_name][0]['t2']  # mm2

    fb1 = steel_fb1_aij(F, lb, ib*10, C)
    fb2 = steel_fb2_aij(F, lb, h, Af)

    return min(max(fb1, fb2), steel_ft(F))


def steel_fb_bsl(F=235, lb=0, i=0, C=1, h=100, Af=30):
    """
    許容曲げ応力度を返す　建築基準法
    N/mm2
    lb :圧縮フランジの支点間距離(mm)
    i :断面二次半径(mm)
    C : 補正係数
    h :はりのせい(mm)
    Af :圧縮フランジの断面積(mm2)
    """
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


def steel_fb_aij2005(shape_name, db, lb=0, M1=0, M2=0, M3=0, F=235):
    """

    :param shape_name:
    :param db:
    :param lb: (mm)
    :param F: (N/mm2)
    :return:
    """
    Zx = db[shape_name][0]['Zx']

    My = F / 10 * Zx  # [kN*cm]
    Iy = db[shape_name][0]['Iy']
    if shape_name[0] == 'H':
        Iw = calc_Iw(shape_name, Iy)
    if shape_name[0] == '[':
        Cy = db[shape_name][0]['Cy']
        An = db[shape_name][0]['An']
        Ix = db[shape_name][0]['Ix']
        Iw = calc_Iw(shape_name, Iy, Cy, An, Ix)

    if lb == 0:
        return steel_ft(F)
    Me_fm1 = math.pi ** 4 * E / 10 * Iy * E / 10 * Iw / (lb / 10) ** 4
    Me_fm2 = math.pi ** 2 * E / 10 * Iy * G / 10 * calc_J(shape_name) / (lb / 10) ** 2
    Me = calc_C(M1, M2, M3) * (Me_fm1 + Me_fm2) ** 0.5
    lam_b = (My / Me) ** 0.5  # Myに対する曲げ材の基準化細長比
    e_lam_b = 1 / 0.6 ** 0.5  # 弾性限界細長比
    p_lam_b = calc_p_lam_b(M1, M2, M3)
    nu = 3. / 2 + 2. / 3 * (lam_b / e_lam_b) ** 2

    if lam_b <= p_lam_b:
        return F / nu
    elif p_lam_b < lam_b <= e_lam_b:
        return (1. - 0.4 * ((lam_b - p_lam_b) / (e_lam_b - p_lam_b))) * F / nu
    else:
        return (1 / lam_b ** 2) * F / 2.17


def calc_Iw(shape_name, Iy, Cy=0, An=0, Ix=0):
    """
    曲げねじり定数を返す(cm6) H鋼、溝形鋼

    :param shape_name:
    :param Iy: (cm4)
    :param Cy: (cm)
    :param An: (cm2)
    :param Ix: (cm4)
    :return:
    """
    Iw = 0
    if shape_name[0] == 'H':
        H, B, t1, t2 = [float(x) for x in shape_name[2:].split('x')]
        h = H - t2
        Iw = Iy * (0.1 * h) ** 2 / 4.
    if shape_name[0] == '[':
        H, B, t1, t2 = [float(x) for x in shape_name[2:].split('x')]
        h = H - t2
        Iw = (0.1 * h) ** 2 / 4. * (Iy + (Cy - 0.1 * t1 / 2.) ** 2 * An * (1. - (0.1 * h) ** 2 * An / (4. * Ix)))
    return Iw


def calc_J(shape_name):
    # サンブナンのねじり定数を返す(cm4) H鋼、溝形鋼
    j = 0
    if shape_name[0] == 'H':
        H, B, t1, t2 = [float(x) for x in shape_name[2:].split('x')]
        # print(H, B, t1, t2)
        h = H - t2
        j = (1. / 3) * (2 * B * t2 ** 3 + h * t1 ** 3)
    if shape_name[0] == '[':
        H, B, t1, t2 = [float(x) for x in shape_name[2:].split('x')]
        # print(H, B, t1, t2)
        h = H - t2
        b = B - t1 / 2
        j = (1. / 3) * (2 * b * t2 ** 3 + h * t1 ** 3)

    return j / 10000.


def calc_C(M1=0, M2=0, M3=0):
    """
    許容曲げ応力度の補正係数を返す
    :param M1: 座屈補剛区間端部の大きい方のM
    :param M2: 座屈補剛区間端部の小さい方のM
    :param M3: 座屈補剛区間内の最大のM
    :return:
    """
    if abs(M3) > abs(M1):
        return 1.
    if M1 == 0:
        return 1.
    else:
        return min(1.75 + 1.05 * (M2 / M1) + 0.3 * (M2 / M1) ** 2, 2.3)


def calc_p_lam_b(M1, M2, M3):
    """
    塑性限界細長比を返す。
    :param M1:
    :param M2:
    :param M3:
    :return:
    """
    if abs(M3) > abs(M1):
        return 0.3
    return 0.6 + 0.3 * (M2 / M1)
