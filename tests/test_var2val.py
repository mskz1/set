import numpy as np
import pytest
from src.var2val import *


def make_dict():
    return dict(a=2, b=3, c=4, x=1.1, y=2.2, α=111, β=222, γ=333)


var_value_csv = """
a,=,,2
b,=,,10
x,=,,9.8
y,=,,11.5"""


def test_replace_space_moji():
    assert replace_space_moji('a + b') == 'a # + # b'
    assert replace_space_moji('(a + b)') == '(a # + # b)'


def test_replace_space_moji_zenkaku():
    assert replace_space_moji('a ＋ b') == 'a # ＋ # b'
    assert replace_space_moji('(a ＋ b)') == '(a # ＋ # b)'


def test_add_space_around_operator():
    assert add_space_around_operator('a+b') == 'a + b'
    assert add_space_around_operator('a + b') == 'a  +  b'
    assert add_space_around_operator('a+b-c/d+(2*x/y)^2') == 'a + b - c / d +  ( 2 * x / y )  ^ 2'
    assert add_space_around_operator('(a+b)') == ' ( a + b ) '
    assert add_space_around_operator('(a)+(b)') == ' ( a )  +  ( b ) '


def test_add_space_around_operator_zenkaku():
    assert add_space_around_operator('a＋b') == 'a ＋ b'
    assert add_space_around_operator('a ＋ b') == 'a  ＋  b'
    assert add_space_around_operator('a＋bーc／d＋（2＊x／y）＾2') == 'a ＋ b ー c ／ d ＋  （ 2 ＊ x ／ y ）  ＾ 2'
    assert add_space_around_operator('（a＋b）') == ' （ a ＋ b ） '
    assert add_space_around_operator('（a）＋（b）') == ' （ a ）  ＋  （ b ） '


def test_var2val():
    var_dict = make_dict()
    assert var2val("(a*b)+((c))", var_dict) == '(2*3)+((4))'
    assert var2val("(a*b) + ((c))", var_dict) == '(2*3) + ((4))'

    assert var2val("a*b", var_dict) == '2*3'
    assert var2val("-a*b", var_dict) == '-2*3'
    assert var2val("a+b+c-a-b-c*a/b^c", var_dict) == '2+3+4-2-3-4*2/3^4'
    assert var2val("a + b + c - a - b - c*a/b^c", var_dict) == '2 + 3 + 4 - 2 - 3 - 4*2/3^4'
    assert var2val("cos(radians(a))*b + tan(a/b) - sqrt(x)-((a/b)*c)", var_dict) \
           == 'cos(radians(2))*3 + tan(2/3) - sqrt(1.1)-((2/3)*4)'

    assert var2val("a * b + x1 * y3", var_dict) == '2 * 3 + x1 * y3'
    assert var2val("a * b + α1 * y_3 + b4", var_dict) == '2 * 3 + α1 * y_3 + b4'


def test_var2val_zenkaku():
    var_dict = make_dict()
    assert var2val("（a＊b）＋（（c））", var_dict) == '（2＊3）＋（（4））'
    assert var2val("（a＊b） ＋ （（c））", var_dict) == '（2＊3） ＋ （（4））'

    assert var2val("a＊b", var_dict) == '2＊3'
    assert var2val("ーa＊b", var_dict) == 'ー2＊3'
    assert var2val("a＋b＋cーaーbーc＊a／b＾c", var_dict) == '2＋3＋4ー2ー3ー4＊2／3＾4'
    assert var2val("a ＋ b ＋ c ー a ー b ー c＊a／b＾c", var_dict) == '2 ＋ 3 ＋ 4 ー 2 ー 3 ー 4＊2／3＾4'
    assert var2val("cos（radians（a））＊b ＋ tan（a／b） ー sqrt（x）ー（（a／b）＊c）", var_dict) \
           == 'cos（radians（2））＊3 ＋ tan（2／3） ー sqrt（1.1）ー（（2／3）＊4）'


def test_array2dict():
    # 以下だと、全て文字列となる。xloilでは数値は自動で変換してる？
    arr = np.array([['x', 1],
                    ['y', 2],
                    ['z', 3]])
    assert array2dict(arr) == {'x': '1', 'y': '2', 'z': '3'}
    print(arr[0][1].dtype)
    arr = np.array([['x', -1, 1],
                    ['y', -1, 2],
                    ['z', -1, 3]])
    assert array2dict(arr) == {'x': '1', 'y': '2', 'z': '3'}
