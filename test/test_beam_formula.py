# -*- coding: utf-8 -*-
import pytest

from beam_formula import LoadType, SimplySupportedBeam

from beam_formula import Load
from beam_formula import uniform_distributed_load, point_load_at_center

from beam_formula import DistributedLoad,PointLoad

@pytest.mark.skip()
def test_simply_supported_beam():
    bf = SimplySupportedBeam(span=6, dl=1)
    print(bf.param())

    bf = SimplySupportedBeam(span=6, load_type=LoadType.PLC, P=10)
    print(bf.param())


def test_load_object():
    ld = Load()
    assert ld.type == LoadType.UDL


def test_uniform_distributed_load_factory():
    udl = uniform_distributed_load(1.0)
    assert udl.value == 1.

@pytest.mark.skip()
def test_point_load_at_center_factory():
    pcl = point_load_at_center(5.)
    assert pcl.value == 5.

def test_1():
    dl = DistributedLoad(1)
    print(dl)
    print(dl.value)
