# -*- coding: utf-8 -*-
from unittest import TestCase
from material import Steel

try:
    from . import ureg, Q_
except SystemError:
    from __init__ import ureg, Q_

from collections import namedtuple

__author__ = 'mskz'


class TestSteel(TestCase):
    def setUp(self):
        self.ss400 = Steel()
        TestData = namedtuple("TestData","Lb Lk")


    def test_ss400(self):
        N_MM2 = 'N/mm**2'
        # self.assertEqual(self.ss400.F, Q_(23.5, "kN / centimeter**2"))  # TODO:うまくいかない？
        self.assertEqual(self.ss400.F, Q_(235, "N/mm**2"))
        a = Q_(23.5, "kN / centimeter**2")
        self.assertAlmostEqual(self.ss400.ft.magnitude, Q_(156.6667, 'N/mm**2').magnitude, delta=0.01)

        self.assertAlmostEqual(self.ss400.fc(lmd=100.).magnitude, Q_(86.2, N_MM2).magnitude, delta=0.1)
        self.assertAlmostEqual(self.ss400.fc(lmd=0.).magnitude, Q_(156.6, N_MM2).magnitude, delta=0.1)
        self.assertAlmostEqual(self.ss400.fc(lmd=50.).magnitude, Q_(135.0, N_MM2).magnitude, delta=0.1)
        self.assertAlmostEqual(self.ss400.fc(lmd=150.).magnitude, Q_(41.5, N_MM2).magnitude, delta=0.1)

        # 許容曲げ応力度のテスト






    def test_ft(self):
        pass