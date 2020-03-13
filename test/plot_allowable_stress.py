# -*- coding: utf-8 -*-
import pytest

from allowable_stress import steel_ft, steel_fc_aij, steel_fc_bsl, steel_fb2_aij, steel_fb_aij, steel_fb1_aij, \
    steel_fb_bsl, steel_fs

import matplotlib.pyplot as plt
import numpy as np


def data_plot():
    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)
    F = 235
    i = 1
    Af = 1

    x = []
    y = []
    for lb in range(1, 251, 1):
        x.append(lb)
        y.append(steel_fb_bsl(F=F, lb=lb, i=i, C=1, h=10, Af=Af))
    ax.plot(x, y)
    x.clear()
    y.clear()
    for lb in range(1, 251, 1):
        x.append(lb)
        y.append(steel_fb_bsl(F=F, lb=lb, i=i, C=2.3, h=10, Af=Af))
    ax.plot(x, y)

    x.clear()
    y.clear()
    for lb in range(1, 251, 1):
        x.append(lb)
        y.append(steel_fb_bsl(F=F, lb=lb, i=i, C=2.3, h=4, Af=Af))
    ax.plot(x, y)

    ax.grid()
    ax.set_ylim(0, 160)
    # ax.set_ylim(0, 220)
    ax.set_xlim(0, 250)
    plt.show()


if __name__ == '__main__':
    data_plot()
