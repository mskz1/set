# import re
SPACE_CHAR = '#'


# SPACE_CHAR_ZENKAKU = '＃'


def replace_space_moji(txt):
    """
    意図的に入力されているスペースを別の文字に一旦置き換える。
    :param txt:
    :return:
    """
    return txt.replace(' ', ' ' + SPACE_CHAR + ' ')


def add_space_around_operator(txt):
    """
    演算子の前後にスペースを追加する。
    :param txt:
    :return:
    """
    operators = ['+', '-', '*', '/', '%', '^', '(', ')', 'MOD', '\\'] \
                + ['＋', 'ー', '＊', '／', '％', '＾', '（', '）']
    for op in operators:
        txt = txt.replace(op, ' ' + op + ' ')
    return txt


def var2val(txt, var_val):
    """
    変数名の含まれる計算式の文字列の、変数名を実際の値に置き換えた文字列にして返す。
    :param txt:
    :param var_val:
    :return:
    """
    txt_m = add_space_around_operator(replace_space_moji(txt))
    txt_lst = txt_m.split(' ')
    result = []
    for wd in txt_lst:
        if wd in var_val.keys():
            result.append(str(var_val[wd]))
        elif wd == SPACE_CHAR:
            result.append(' ')
        else:
            result.append(wd)
    return "".join(result)


def array2dict(array):
    """
    エクセルのセルレンジの最左列に変数名、最右列に値が入っているとして変数名：値の辞書オブジェクトを返す
    xloil版：セル範囲がndarrayに変換される

    2023-0304 仮実装
    :param array:
    :return:
    """
    r, c = array.shape
    result = {}
    for row_i in range(0, r):
        if array[row_i][0]:
            result[str(array[row_i][0])] = array[row_i][c - 1]
    return result
