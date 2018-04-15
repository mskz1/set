# -*- coding: utf-8 -*-
from unittest import TestCase

from cross_section.section import SectionDB, H_HOSOHABA_SERIES, H_TYUUHABA_SERIES
from cross_section.section import short_full_name

try:
    from cross_section import ureg, Q_
# except SystemError:
except ImportError:
    from __init__ import ureg, Q_

__author__ = 'mskz'


class TestSectionDB(TestCase):
    def setUp(self):
        # print('*setup')
        self.sec_db = SectionDB()
        self.sec_db.load('/Users/mskz/PycharmProjects/set/cross_section/section.dat')

    def test_get_section(self):
        print('*test1')
        h20 = self.sec_db.get_section("H-200x100x5.5x8")
        self.assertEqual(h20.name, "H-200x100x5.5x8")
        self.assertEqual(h20.series_symbol, H_HOSOHABA_SERIES)
        self.assertEqual(h20.get_prop("An"), Q_(26.67, "cm**2"))
        self.assertNotEqual(h20.get_prop("An"), Q_(1.0, "cm**2"))
        self.assertRaises(KeyError, h20.get_prop, 'As')

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
        print('*test2')
        all_list = self.sec_db.get_list()
        hss = ['H-150x75x5x7', 'H-175x90x5x8', 'H-198x99x4.5x7', 'H-200x100x5.5x8', 'H-248x124x5x8', 'H-250x125x6x9',
               'H-298x149x5.5x8', 'H-300x150x6.5x9', 'H-346x174x6x9', 'H-350x175x7x11', 'H-396x199x7x11',
               'H-400x200x8x13', 'H-446x199x8x12', 'H-450x200x9x14', 'H-496x199x9x14', 'H-500x200x10x16',
               'H-596x199x10x15', 'H-600x200x11x17']
        hsw = ['H-100x100x6x8', 'H-125x125x6.5x9', 'H-150x150x7x10', 'H-175x175x7.5x11', 'H-200x200x8x12',
               'H-250x250x9x14', 'H-300x300x10x15', 'H-350x350x12x19', 'H-400x400x13x21']
        hsm = ['H-148x100x6x9', 'H-194x150x6x9', 'H-244x175x7x11', 'H-294x200x8x12', 'H-340x250x9x14',
               'H-390x300x10x16', 'H-440x300x11x18', 'H-488x300x11x18', 'H-582x300x12x17', 'H-588x300x12x20']
        kps = ['□P-50x50x1.6', '□P-50x50x2.3', '□P-50x50x3.2', '□P-60x60x1.6', '□P-60x60x2.3', '□P-60x60x3.2',
               '□P-75x75x1.6', '□P-75x75x2.3', '□P-75x75x3.2', '□P-75x75x4.5', '□P-100x100x2.3', '□P-100x100x3.2',
               '□P-100x100x4.5', '□P-100x100x6.0', '□P-125x125x3.2', '□P-125x125x4.5', '□P-125x125x6.0',
               '□P-125x125x9.0', '□P-150x150x4.5', '□P-150x150x6.0', '□P-150x150x9.0', '□P-175x175x4.5',
               '□P-175x175x6.0', '□P-175x175x9.0', '□P-200x200x4.5', '□P-200x200x6.0', '□P-200x200x8.0',
               '□P-200x200x9.0', '□P-60x30x1.6', '□P-60x30x2.3', '□P-60x30x3.2', '□P-75x45x1.6', '□P-75x45x2.3',
               '□P-75x45x3.2', '□P-100x50x1.6', '□P-100x50x2.3', '□P-100x50x3.2', '□P-100x50x4.5', '□P-125x75x2.3',
               '□P-125x75x3.2', '□P-125x75x4.5', '□P-125x75x6.0', '□P-150x75x3.2', '□P-150x75x4.5', '□P-150x100x3.2',
               '□P-150x100x4.5', '□P-150x100x6.0', '□P-200x100x4.5', '□P-200x100x6.0', '□P-200x150x4.5',
               '□P-200x150x6.0', '□P-200x150x9.0', '□P-250x150x4.5', '□P-250x150x6.0', '□P-250x150x9.0']
        ps = ['P-27.2x1.9', 'P-27.2x2.3', 'P-42.7x2.3', 'P-48.6x2.3', 'P-48.6x3.2', 'P-60.5x2.3', 'P-60.5x2.8',
              'P-60.5x3.2', 'P-76.3x2.8', 'P-76.3x3.2', 'P-89.1x2.8', 'P-89.1x3.2', 'P-89.1x4.2', 'P-101.6x3.2',
              'P-101.6x3.5', 'P-101.6x4.2', 'P-114.3x2.8', 'P-114.3x3.5', 'P-114.3x4.5', 'P-114.3x6', 'P-139.8x3.5',
              'P-139.8x4', 'P-139.8x4.5', 'P-139.8x5', 'P-165.2x3.8', 'P-165.2x4', 'P-165.2x4.5', 'P-165.2x5',
              'P-190.7x5.3']
        cs = ['C-60x30x10x1.6', 'C-60x30x10x2.3', 'C-75x45x15x1.6', 'C-75x45x15x2.3', 'C-100x50x20x1.6',
              'C-100x50x20x2.3', 'C-100x50x20x3.2', 'C-120x60x20x2.3', 'C-120x60x20x3.2', 'C-125x50x20x3.2']
        mizoss = ['[-75x40x5x7', '[-100x50x5x7.5', '[-125x65x6x8', '[-150x75x6.5x10', '[-150x75x9x12.5',
                  '[-180x75x7x10.5', '[-200x80x7.5x11', '[-200x90x8x13.5']

        assert self.sec_db.get_list(H_HOSOHABA_SERIES) == hss
        assert self.sec_db.get_list(H_TYUUHABA_SERIES) == hsm

    def test_get_section_shortname(self):
        print('*test3')
        h20 = self.sec_db.get_section(short_full_name['HS20'])
        assert h20.name == 'H-200x100x5.5x8'
        assert h20.get_prop('Zx') == Q_(181, 'cm**3')
        assert h20.get_prop('Ix').magnitude == 1810
        assert h20.get_prop('Iy') == Q_(134, 'cm**4')
        h244 = self.sec_db.get_section(short_full_name['HM244'])
        assert h244.get_prop('An') == Q_(55.49, 'cm**2')

