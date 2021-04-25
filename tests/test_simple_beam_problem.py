# -*- coding: utf-8 -*-
import pytest
from pytest import approx

from beam_model import SimpleBeam


def test_simple_beam():
    sb = SimpleBeam(span=5.0)
    sb.add_load_case(l_case="G")



