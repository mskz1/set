# -*- coding: utf-8 -*-
from unittest import TestCase

from cross_section.section import SectionDB, H_HOSOHABA_SERIES, H_TYUUHABA_SERIES

try:
    from cross_section import ureg, Q_
except SystemError:
    from __init__ import ureg, Q_

__author__ = 'mskz'


class TestSectionDB(TestCase):
    def setUp(self):
        self.sec_db = SectionDB()
        self.sec_db.load()

    def test_load(self):
        # sec_db = SectionDB()
        # sec_db.x_load()
        pass
        #self.fail()

    def test_get_section(self):

        h20 = self.sec_db.get_section("H-200x100x5.5x8")
        self.assertEqual(h20.name, "H-200x100x5.5x8")
        self.assertEqual(h20.series_symbol, H_HOSOHABA_SERIES)
        self.assertEqual(h20.get_prop("An"), Q_(26.67, "cm**2"))
        self.assertNotEqual(h20.get_prop("An"), Q_(1.0, "cm**2"))
        self.assertRaises(KeyError, h20.get_prop,'As')

        h588 = self.sec_db.get_section("H-588x300x12x20")
        self.assertEqual(h588.series_symbol, H_TYUUHABA_SERIES)
        self.assertEqual(h588.get_prop("Zx"), Q_(3890, "cm**3"))

        kp150 = self.sec_db.get_section("□P-150x150x6.0")
        self.assertEqual(kp150.get_prop("Ix"), Q_(1150, "cm**4"))

        p165 = self.sec_db.get_section("P-165.2x5")
        self.assertEqual(p165.get_prop("An"), Q_(25.2, "cm**2"))
        self.assertEqual(p165.get_prop("Zxp"), Q_(128, "cm**3"))

        c100 = self.sec_db.get_section("C-100x50x20x2.3")
        self.assertEqual(c100.get_prop("An"), Q_(5.172, "cm**2"))
        self.assertEqual(c100.get_prop("Zx"), Q_(16.1, "cm**3"))

        m150 = self.sec_db.get_section("[-150x75x6.5x10")
        self.assertEqual(m150.get_prop("An"), Q_(23.71, "cm**2"))

    def test_get_list(self):
        all_list = self.sec_db.get_list()
        hs_list = self.sec_db.get_list(H_HOSOHABA_SERIES)

        pass
        # self.fail()