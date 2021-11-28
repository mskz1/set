# -*- coding: utf-8 -*-
import pytest
import pprint

from text_calc import strip_square_brackets, get_square_brackets_index

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
    src_txt = '0.6[kN/m2]'
    res_txt = strip_square_brackets(src_txt)
    assert res_txt == '0.6'

    src_txt = '3.2[m]'
    res_txt = strip_square_brackets(src_txt)
    assert res_txt == '3.2'

    src_txt = '0.6[DL:kN/m2]*3[幅:m]*4.5[高さ:m]'
    res_txt = strip_square_brackets(src_txt)
    assert res_txt == '0.6*3*4.5'

    src_txt = '0123 [567] 9'
    res_txt = strip_square_brackets(src_txt)
    assert res_txt == '0123  9'

    src_txt = '0123 [567] 9xxx [zz] x [zzz] xx [ zzzzz ] xx'
    res_txt = strip_square_brackets(src_txt)
    assert res_txt == '0123  9xxx  x  xx  xx'

    src_txt = '0123［567] 9xxxx[zz] x [zzz] xx [ zzzzz ] xx'
    res_txt = strip_square_brackets(src_txt)
    assert res_txt == '0123 9xxxx x  xx  xx'


def test_square_brackets_index():
    # 補助関数のテスト
    # 有効な例
    src_txt = '0123 [567] 9'
    # print('=== source:{}'.format(src_txt))
    # get_square_brackets_index(src_txt)
    # assert get_square_brackets_index(src_txt) == (4,8)
    assert get_square_brackets_index(src_txt) == [(5, 9)]

    # 有効な例
    src_txt = '0123 [567] 9xxx [zz] x [zzz] xx [ zzzzz ] xx'
    # print('=== source:{}'.format(src_txt))

    # get_square_brackets_index(src_txt)
    assert get_square_brackets_index(src_txt) == [(5, 9), (16, 19), (23, 27), (32, 40)]

    # 有効な例　全角混じり
    src_txt = '0123［567] 9xxxx[zz] x [zzz] xx [ zzzzz ] xx'
    # print('=== source:{}'.format(src_txt))

    # get_square_brackets_index(src_txt)
    assert get_square_brackets_index(src_txt) == [(4, 8), (15, 18), (22, 26), (31, 39)]

    # エラーの例　バランスしていない。括弧の数が違う
    src_txt = 'x [ zz [ zz ] xxx [z] x [zz] xx [zz] xx'
    # print('=== source:{}'.format(src_txt))

    with pytest.raises(ValueError, match='Square brackets are not balanced'):
        idx = get_square_brackets_index(src_txt)

    # エラーの例　括弧が入れ子
    src_txt = 'xx [ zz [ z ] z ] xxx [zz] xx [zzz] xx [zz] xx'
    # print('=== source:{}'.format(src_txt))

    with pytest.raises(ValueError, match='Nested brackets'):
        idx = get_square_brackets_index(src_txt)
