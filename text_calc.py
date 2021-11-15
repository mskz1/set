# -*- coding: utf-8 -*-

"""Excel セルの入力文字列　計算向けのモジュール"""


def strip_square_brackets(src):
    SQUARE_BRACKETS = ('[', ']')
    res = ''
    for c in src:
        if c not in SQUARE_BRACKETS:
            res += c
    return res


def get_square_brackets_index(src):

    def zenkaku_to_hankaku():
        return src.replace('［', '[').replace('］', ']')


    def check_brackets_counts(src):
        num_of_open_brackets = src.count('[')
        num_of_close_brackets = src.count(']')
        if num_of_open_brackets != num_of_close_brackets:
            print('** INVALID DATA ** --Square brackets are not balanced')
            # raise ValueError('Square brackets are not balanced')
            return

    src2 = zenkaku_to_hankaku()
    # print('==== modified src:{}'.format(src2))
    check_brackets_counts(src2)

    index_of_open_brackets = []
    index_of_close_brackets = []
    for i, c in enumerate(src2):
        if c == '[':
            index_of_open_brackets.append(i)
        elif c == ']':
            index_of_close_brackets.append(i)
    # print(index_of_open_brackets)
    # print(index_of_close_brackets)
    res = list(zip(index_of_open_brackets, index_of_close_brackets))

    prev_close_pos = 0
    for pos in res:
        if pos[0] > pos[1] or prev_close_pos > pos[0]:
            print('** INVALID DATA ** --Nested brackets')
            # raise ValueError('Nested brackets')
        prev_close_pos = pos[1]

    # print(res)
    return res