# -*- coding: utf-8 -*-
from unittest import TestCase

__author__ = 'mskz'

#from load import UnitLoad
import load


class TestUnitLoad(TestCase):
    def test_1(self):
        ld1 = load.UnitLoad(name="屋根", value=load.Q_(300., 'N/m^2'))
        self.assertEquals(ld1.name, '屋根')
        self.assertEqual(ld1.value.magnitude, 300.)
