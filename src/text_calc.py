# -*- coding: utf-8 -*-

"""Excel セルの入力文字列　計算向けのモジュール"""


def strip_square_brackets(src: str) -> str:
    """
    src文字列から、角括弧で囲まれた部分を削除した文字列を返す
    """
    idx_list = get_square_brackets_index(src)

    res = ''
    s_idx = 0
    for idx in idx_list:
        e_idx = idx[0]
        res += src[s_idx:e_idx]
        s_idx = idx[1] + 1
    res += src[s_idx:]

    return res


def get_square_brackets_index(src: str) -> list:
    """
    補助関数　角括弧の位置をタプルのリストで返す
    """

    def zenkaku_to_hankaku():
        return src.replace('［', '[').replace('］', ']')

    def check_brackets_counts(src):
        num_of_open_brackets = src.count('[')
        num_of_close_brackets = src.count(']')
        if num_of_open_brackets != num_of_close_brackets:
            raise ValueError('Square brackets are not balanced')

    src2 = zenkaku_to_hankaku()
    check_brackets_counts(src2)

    index_of_open_brackets = []
    index_of_close_brackets = []
    for i, c in enumerate(src2):
        if c == '[':
            index_of_open_brackets.append(i)
        elif c == ']':
            index_of_close_brackets.append(i)
    res = list(zip(index_of_open_brackets, index_of_close_brackets))

    prev_close_pos = 0
    for pos in res:
        if pos[0] > pos[1] or prev_close_pos > pos[0]:
            raise ValueError('Nested brackets')
        prev_close_pos = pos[1]

    return res
