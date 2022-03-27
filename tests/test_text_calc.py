# -*- coding: utf-8 -*-
import pytest

from src.text_calc import strip_square_brackets, get_square_brackets_index

""" VBA の textCalc udf のpython版

サンプル

excelのセルへの入力から数式計算に不要なものを除く

A1セルへの入力（文字）
0.6[kN/m2] * 3.2[m] * 3.4[m]

A2 セルへの入力
=calcText(A1)

A2セルの計算結果は、
0.6*3.2*3.4 の結果が入る

"""


# @pytest.mark.skip('まだ未実装')
def test_strip_square_brackets():
    assert strip_square_brackets('0.6[kN/m2]') == '0.6'

    assert strip_square_brackets('3.2[m]') == '3.2'

    assert strip_square_brackets('0.6[DL:kN/m2]*3[幅:m]*4.5[高さ:m]') == '0.6*3*4.5'

    assert strip_square_brackets('0123 [567] 9') == '0123  9'

    assert strip_square_brackets('0123 [567] 9xxx [zz] x [zzz] xx [ zzzzz ] xx') == '0123  9xxx  x  xx  xx'

    assert strip_square_brackets('0123［567] 9xxxx[zz] x [zzz] xx [ zzzzz ] xx') == '0123 9xxxx x  xx  xx'


def test_square_brackets_index():
    # 補助関数のテスト
    # 有効な例
    assert get_square_brackets_index('0123 [567] 9') == [(5, 9)]

    # 有効な例
    #                    1         2         3         4         5
    #          012345678901234567890123456789012345678901234567890
    src_txt = '0123 [567] 9xxx [zz] x [zzz] xx [ zzzzz ] xx'
    assert get_square_brackets_index(src_txt) == [(5, 9), (16, 19), (23, 27), (32, 40)]

    # 有効な例　全角混じり
    #                     1         2         3         4         5
    #          01234 5678901234567890123456789012345678901234567890
    src_txt = '0123［567] 9xxxx[zz] x [zzz] xx [ zzzzz ] xx'
    assert get_square_brackets_index(src_txt) == [(4, 8), (15, 18), (22, 26), (31, 39)]

    # エラーの例　バランスしていない。括弧の数が違う
    src_txt = 'x [ zz [ zz ] xxx [z] x [zz] xx [zz] xx'
    with pytest.raises(ValueError, match='Square brackets are not balanced'):
        idx = get_square_brackets_index(src_txt)

    # エラーの例　括弧が入れ子
    src_txt = 'xx [ zz [ z ] z ] xxx [zz] xx [zzz] xx [zz] xx'
    # print('=== source:{}'.format(src_txt))
    with pytest.raises(ValueError, match='Nested brackets'):
        idx = get_square_brackets_index(src_txt)
