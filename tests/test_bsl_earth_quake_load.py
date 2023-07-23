import pytest
from src.bsl.earth_quake_load import *


def test_get_T():
    # 固有周期を求める関数のテスト
    assert get_T(h=10, alpha=1) == 0.3
    assert get_T(h=10, alpha=0) == 0.2


def test_get_Rt():
    # 振動特性係数を求める関数のテスト
    assert get_Rt(T=0.3, Tc=0.4) == 1.0
    assert get_Rt(T=0.4, Tc=0.4) == 1.0
    assert get_Rt(T=0.8, Tc=0.4) == pytest.approx(0.8, abs=0.001)
    assert get_Rt(T=0.6, Tc=0.6) == pytest.approx(1.0, abs=0.001)
    assert get_Rt(T=1.2, Tc=0.6) == pytest.approx(0.8, abs=0.001)
    assert get_Rt(T=0.8, Tc=0.8) == pytest.approx(1.0, abs=0.001)
    assert get_Rt(T=1.6, Tc=0.8) == pytest.approx(0.8, abs=0.001)


def test_get_alpha_i():
    assert xxx_get_alpha_i([100.]) == [1.0]
    assert xxx_get_alpha_i([100.0, 100.0]) == [0.5, 0.5]
    with pytest.raises(TypeError):
        a = xxx_get_alpha_i(["a", 100.0]) == [0.5, 0.5]
    assert xxx_get_alpha_i([10.0, 70.0, 20.0]) == [0.1, 0.7, 0.2]

    assert get_alpha_i([100.]) == [1.0]
    assert get_alpha_i([200.0, 100.0]) == [1.0, 0.5]
    assert get_alpha_i([400, 200.0, 50.0]) == [1.0, 0.5, 0.125]


def test_get_Ai():
    assert get_Ai(alpha_i=[1.0], T=0.4) == [1.0]
    assert get_Ai(alpha_i=get_alpha_i(get_sum_of_W([100])), T=0.4) == [1.0]
    # AIJ RC規準2018 付録設計例より
    goukei_w = get_sum_of_W([7107, 7058, 7058, 7036, 7025, 7024, 6204])
    assert get_Ai(alpha_i=get_alpha_i(goukei_w), T=0.544) == pytest.approx([1.000000, 1.094632, 1.198600, 1.318624,
                                                                            1.467191, 1.678910,
                                                                            2.103066], abs=0.000001)


def test_get_sum_of_W():
    assert get_sum_of_W(w=[10, 10, 10]) == [30, 20, 10]
    assert get_sum_of_W(w=[30, 20, 10]) == [60, 30, 10]


def test_get_Qi():
    # goukei_w = get_sum_of_W([7107, 7058, 7058, 7036, 7025, 7024, 6204])
    goukei_w = [48512, 41405, 34347, 27289, 20253, 13228, 6204]
    # Ai = get_Ai(alpha_i=get_alpha_i(goukei_w), T=0.544)
    Ai = [1.0, 1.0946319353352536, 1.1986003504844938, 1.3186237307318351, 1.4671914862634334, 1.6789101983309898,
          2.1030657722561608]
    assert get_Qi(goukei_w, Ai, C0=0.2) == pytest.approx(
        [9702.400, 9064.647, 8233.665, 7196.785, 5943.006, 4441.725, 2609.484], abs=0.001)


def test_get_Pi():
    Qi = [9702.400, 9064.647, 8233.665, 7196.785, 5943.006, 4441.725, 2609.484]
    assert get_Pi(Qi) == pytest.approx([637.753, 830.982, 1036.880, 1253.779, 1501.281, 1832.241, 2609.484], abs=0.001)


def test_pub_get_Qi():
    assert pub_get_Qi([7107, 7058, 7058, 7036, 7025, 7024, 6204], T=0.544, Tc=0.6, C0=0.2, Z=1.0) == pytest.approx(
        [9702.400, 9064.647, 8233.665, 7196.785, 5943.006, 4441.725, 2609.484], abs=0.001)
