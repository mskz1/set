# -*- coding: utf-8 -*-

"""溶接に関する計算をするモジュール"""

import allowable_stress

def fillet_weld_size(t, weld_type='T'):
    """
    隅肉溶接のサイズ（脚長）を返す。
    ＤＨ標準　2019.1.28
    :param t:母材の薄い方の板厚（㎜）
    :param weld_type: 'T':T継手 Tee、'L':重ね継手 Lap
    :return:
    """
    if t < 0:
        raise ValueError('Negative thickness value Error')
    if not weld_type in ['T', 'L']:
        raise ValueError('Invalid weld_type parameter')

    if weld_type == 'T':
        if t <= 1.6:
            return 2.0
        elif t <= 2.3:
            return 3.5
        elif t <= 3.2:
            return 4.5
        elif t <= 6.0:
            return 6.0
        elif t <= 9.0:
            return 7.0
        elif t <= 12.0:
            return 9.0
        elif t <= 16.0:
            return 12.0
        elif t <= 19.0:
            return 14.0
        else:
            return 14.0

    elif weld_type == 'L':
        if t <= 2.3:
            return 2.0
        elif t <= 3.2:
            return 2.5
        elif t <= 4.0:
            return 3.5
        elif t <= 4.5:
            return 4.0
        elif t <= 6.0:
            return 5.0
        elif t <= 9.0:
            return 7.0
        elif t <= 12.0:
            return 9.0
        elif t <= 16.0:
            return 12.0
        else:
            return 12.0


def fillet_weld_strength(L, S, n=1, F=235):
    """
    隅肉溶接の長期許容耐力（Ｎ）を返す
    :param L: 溶接長さ（mm）
    :param S: 脚長（サイズ）(mm)
    :param n: 溶接個所数 1, 2
    :param F: 母材のＦ値（N/mm2)
    :return:
    """
    len_e = L - 2 * S   # 有効溶接長さ
    a = 0.7 * S         # のど厚

    return n * len_e * a * allowable_stress.steel_fs(F)

