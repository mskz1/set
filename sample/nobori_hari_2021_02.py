# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
from beam_formula import SimpliSupportedBeamWithUniformlyIncreasingDistributedLoad, \
    SimplySupportedBeamWithPointLoadAtAny


def divided_loads(w, a, n, on_edge=True):
    """
    三角形平面の斜め（45度）部分の梁にかかる荷重を算出する。

    :param w:分布荷重 kN/m2
    :param a:  負担三角形面積の一辺の長さ m
    :param n: 一辺の分割数
    :param on_edge: P1が支点に乗る配置
    :return:　[(P1, x1), (P2, x2)...]
    """
    result = []
    if on_edge:
        for i in range(n + 1):
            futan_nagasa = a - (a / n) * i
            if i == 0 or i == n:
                futan_haba = 0.5 * a / n  # 負担幅
            else:
                futan_haba = a / n  # 負担幅
            kajuu = w * futan_haba * futan_nagasa
            saika_ten = (a / n) * i
            result.append((kajuu, saika_ten))
            # print("P = {:4.2f} * {:6.2f} * {:6.2f} = {:6.2f} at pos={:6.2f}".format(w, futan_nagasa, futan_haba, kajuu, saika_ten))
    else:
        for i in range(n):
            futan_nagasa = a - 0.5 * a / n * (2 * (i + 1) - 1)
            futan_haba = a / n
            kajuu = w * futan_haba * futan_nagasa
            saika_ten = (a / n) * (i) + 0.5 * (a / n)
            result.append((kajuu, saika_ten))
            # print("P = {:4.2f} * {:6.2f} * {:6.2f} = {:6.2f} at pos={:6.2f}".format(w, futan_nagasa, futan_haba, kajuu, saika_ten))

    return result


def hikaku_sample():
    a = 3.
    span = a * 2 ** 0.5

    bf_base = SimpliSupportedBeamWithUniformlyIncreasingDistributedLoad(span=span, load=1, a=a / 2 ** 0.5)
    Mmax = bf_base.getMmax()
    Dmax = bf_base.getDmax()
    print("三角形分布荷重：Mmax={:8.2f}, Dmax={:8.2f}".format(Mmax, Dmax))

    from beam_formula import sum_lists
    import matplotlib.pyplot as plt
    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)

    n_segment = 50

    loads = divided_loads(w=1, a=a, n=4, on_edge=True)
    # loads = divided_loads(w=1, a=a, n=4, on_edge=False)

    r1_m = [0.0] * (n_segment + 1)
    r1_d = [0.0] * (n_segment + 1)

    for load in loads:
        bf = SimplySupportedBeamWithPointLoadAtAny(span, load[0], load[1] * 2 ** 0.5)
        x = bf.get_points(n_segment)

        moment = bf.getM_npoints(n_segment)

        result_m = sum_lists(moment, r1_m)
        r1_m = result_m[:]

        disp = bf.getD_npoints(n_segment)
        result_d = sum_lists(disp, r1_d)
        r1_d = result_d[:]

    Mmax_1 = max(result_m)
    Dmax_1 = max(result_d)

    print("集中荷重１：Mmax={:8.2f}, Dmax={:8.2f}".format(Mmax_1, Dmax_1))

    # ax.plot(x, result, marker=".")
    # plt.show()


def test_divide_load():
    import pprint
    pprint.pprint(divided_loads(w=1, a=3, n=3))
    assert divided_loads(w=1, a=3, n=3) == [(1.5, 0.0), (2.0, 1.0), (1.0, 2.0), (0.0, 3.0)]
    # pprint.pprint(divided_loads(w=1, a=3, n=30))

    pprint.pprint(divided_loads(w=1, a=3, n=3, on_edge=False))
    assert divided_loads(w=1, a=3, n=3, on_edge=False) == [(2.5, 0.5), (1.5, 1.5), (0.5, 2.5)]


if __name__ == '__main__':
    # test_divide_load()
    hikaku_sample()
    pass
