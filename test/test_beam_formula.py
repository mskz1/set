# -*- coding: utf-8 -*-
import pytest
from pytest import approx
# from beam_formula import LoadType, SimplySupportedBeam

# from beam_formula import Load
# from beam_formula import uniform_distributed_load, point_load_at_center

from beam_formula import SimplySupportedBeamWithUniformDistributedLoad
from beam_formula import SimplySupportedBeamWithPointLoadAtCenter
from beam_formula import SimplySupportedBeamWithPointLoadAtAny
from beam_formula import SimpliSupportedBeamWithUniformlyIncreasingDistributedLoad


# from beam_formula import DistributedLoad,PointLoad

@pytest.mark.skip("不要？")
def test_simply_supported_beam():
    bf = SimplySupportedBeam(span=6, dl=1)
    print(bf.param())

    bf = SimplySupportedBeam(span=6, load_type=LoadType.PLC, P=10)
    print(bf.param())


@pytest.mark.skip("不要？")
def test_load_object():
    ld = Load()
    assert ld.type == LoadType.UDL


@pytest.mark.skip("不要？")
def test_uniform_distributed_load_factory():
    udl = uniform_distributed_load(1.0)
    assert udl.value == 1.


@pytest.mark.skip("不要？")
def test_point_load_at_center_factory():
    pcl = point_load_at_center(5.)
    assert pcl.value == 5.


@pytest.mark.skip("不要？")
def test_1():
    dl = uniform_distributed_load(1)
    print(dl)
    print(dl.value)


@pytest.mark.skip("不要？")
def test_Load_class():
    udl = Load.uniform_distributed_load(2)
    print(udl.value)


def test_SimplySupportedBeamWithUniformDistributedLoad():
    bf = SimplySupportedBeamWithUniformDistributedLoad(5., 1.)
    assert bf.span == 5.  # (m)
    assert bf.load == 1.  # (kN/m)
    assert bf.getMmax() == 3.125  # (kN*m)
    assert bf.getMcenter() == 3.125
    assert bf.getR1() == 2.5  # (kN)
    assert bf.getDmax() == approx(396.9766)
    assert bf.getM_at(1.5) == 2.625
    assert bf.getD_at(1.5) == approx(322.7896)

    bf = SimplySupportedBeamWithUniformDistributedLoad(7., 3.5)
    assert bf.getMmax() == 21.4375
    assert bf.getMcenter() == 21.4375
    assert bf.getR1() == 12.25
    assert bf.getDmax() == approx(5337.5889)
    assert bf.getM_at(1.5) == 14.4375
    assert bf.getD_at(1.5) == approx(3359.9466)


def test_SimplySupportedBeamWithUniformlyIncreasingDistributedLoad():
    # a = 3./(2**0.5)
    a = 2.1212

    bf = SimpliSupportedBeamWithUniformlyIncreasingDistributedLoad(5., 1., a)
    assert bf.getMmax() == approx(3.4019, abs=0.001)

    # span:5[m], w=1[kN/m2], a=2[m]
    bf = SimpliSupportedBeamWithUniformlyIncreasingDistributedLoad(5., 1., 2)
    assert bf.getMmax() == approx(3.2075)
    assert bf.getR1() == approx(1.6666666666666667)
    assert bf.getR2() == approx(3.333333333333333)
    assert bf.getMcenter() == approx(3.125)
    assert bf.getM_at(0.5) == approx(0.825)
    # https://structx.com/Beam_Formulas_002.html のたわみ間違い？
    assert bf.getDmax() == approx(397.56, abs=0.02)


def test_SimplySupportedBeamWithPointLoadAtCenter():
    bf = SimplySupportedBeamWithPointLoadAtCenter(5., 10.)
    assert bf.span == 5.  # (m)
    assert bf.load == 10.  # (kN)
    assert bf.getMmax() == 12.5  # (kN*m)
    assert bf.getMcenter() == 12.5
    assert bf.getR1() == 5.
    assert bf.getDmax() == approx(1270.3252)
    assert bf.getM_at(1.5) == 7.5
    assert bf.getM_at(3.5) == 7.5
    assert bf.getM_at(2.5) == 12.5
    assert bf.getD_at(1.5) == approx(1006.0976)
    assert bf.getD_at(3.5) == approx(1006.0976)
    assert bf.getD_at(2.5) == approx(1270.3252)


def test_SimplySupportedBeamWithPointLoadAtAny():
    bf = SimplySupportedBeamWithPointLoadAtAny(7., 10., 2.)
    assert bf.span == 7.  # (m)
    assert bf.load == 10.  # (kN)
    assert bf.a == 2.  # (m)
    assert bf.getMmax() == approx(14.2857, abs=0.001)
    assert bf.getMcenter() == 10.0
    assert bf.getR1() == approx(7.1429, abs=0.001)
    assert bf.getR2() == approx(2.8571, abs=0.001)
    assert bf.getDmax() == approx(2698.9431)
    assert bf.getD_at(1.5) == approx(1894.5993)
    assert bf.getD_at(3.5) == approx(2662.6016)


def test_SSBwPL_calc_delta_n_points():
    bf = SimplySupportedBeamWithPointLoadAtAny(4., 10., 2.)
    assert bf.get_points(2) == [0.0, 2.0, 4.0]
    assert bf.get_points(4) == [0.0, 1.0, 2.0, 3.0, 4.0]
    # たわみはcm
    assert bf.getD_npoints(2) == approx([0.0, 650.4065, 0.0], abs=0.01)
    assert bf.getD_npoints(4) == approx([0.0, 447.1545, 650.4065, 447.1545, 0.0], abs=0.01)
    assert bf.getD_npoints(4) == approx([0.0, 447.1545, 650.4065, 447.1545, 0.0], abs=0.01)

    bf = SimplySupportedBeamWithPointLoadAtAny(6., 10., 1.)
    assert bf.getD_npoints(6) == approx([0.0, 677.5068, 1029.8103, 1056.9106, 840.1084, 460.7046, 0.0], abs=0.01)


# @pytest.mark.skip()
def test_SSBwPL_plot():
    import matplotlib.pyplot as plt
    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)

    bf = SimplySupportedBeamWithPointLoadAtAny(6., 10., 2)
    x = bf.get_points(50)
    y = bf.getD_npoints(50)
    ax.plot(x, y, marker=".")
    plt.show()
