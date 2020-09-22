# -*- coding: utf-8 -*-
import pytest
from pytest import approx
from beam_formula import LoadType, SimplySupportedBeam

from beam_formula import Load
from beam_formula import uniform_distributed_load, point_load_at_center
from beam_formula import SimplySupportedBeamWithUniformDistributedLoad
from beam_formula import SimplySupportedBeamWithPointLoadAtCenter
from beam_formula import SimplySupportedBeamWithPointLoadAtAny


# from beam_formula import DistributedLoad,PointLoad

@pytest.mark.skip()
def test_simply_supported_beam():
    bf = SimplySupportedBeam(span=6, dl=1)
    print(bf.param())

    bf = SimplySupportedBeam(span=6, load_type=LoadType.PLC, P=10)
    print(bf.param())


@pytest.mark.skip()
def test_load_object():
    ld = Load()
    assert ld.type == LoadType.UDL


@pytest.mark.skip()
def test_uniform_distributed_load_factory():
    udl = uniform_distributed_load(1.0)
    assert udl.value == 1.


@pytest.mark.skip()
def test_point_load_at_center_factory():
    pcl = point_load_at_center(5.)
    assert pcl.value == 5.


@pytest.mark.skip()
def test_1():
    dl = DistributedLoad(1)
    print(dl)
    print(dl.value)


@pytest.mark.skip()
def test_Load_class():
    udl = Load.uniform_distributed_load(2)
    print(udl.value)


def test_SimplySupportedBeamWithUniformDistributedLoad():
    bf = SimplySupportedBeamWithUniformDistributedLoad(5., 1.)
    assert bf.span == 5.
    assert bf.load == 1.
    assert bf.getMmax() == 3.125
    assert bf.getMcenter() == 3.125
    assert bf.getR1() == 2.5
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


def test_SimplySupportedBeamWithPointLoadAtCenter():
    bf = SimplySupportedBeamWithPointLoadAtCenter(5., 10.)
    assert bf.span == 5.
    assert bf.load == 10.
    assert bf.getMmax() == 12.5
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
    assert bf.span == 7.
    assert bf.load == 10.
    assert bf.a == 2.
    assert bf.getMmax() == approx(14.2857, abs=0.001)
    assert bf.getMcenter() == 10.0
    assert bf.getR1() == approx(7.1429, abs=0.001)
    assert bf.getR2() == approx(2.8571, abs=0.001)
    assert bf.getDmax() == approx(2698.9431)
    assert bf.getD_at(1.5) == approx(1894.5993)
    assert bf.getD_at(3.5) == approx(2662.6016)

