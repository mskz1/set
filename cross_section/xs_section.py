# -*- coding: utf-8 -*-

short_full_name = dict(HS15='H-150x75x5x7', HS17='H-175x90x5x8', HS19='H-198x99x4.5x7', HS20='H-200x100x5.5x8',
                       HS24='H-248x124x5x8', HS25='H-250x125x6x9', HS29='H-298x149x5.5x8', HS30='H-300x150x6.5x9',
                       HS34='H-346x174x6x9', HS35='H-350x175x7x11', HS39='H-396x199x7x11',
                       HS40='H-400x200x8x13', HS44='H-446x199x8x12', HS45='H-450x200x9x14', HS49='H-496x199x9x14',
                       HS50='H-500x200x10x16', HS59='H-596x199x10x15', HS60='H-600x200x11x17',

                       HW100='H-100x100x6x8', HW125='H-125x125x6.5x9',
                       HW150='H-150x150x7x10', HW175='H-175x175x7.5x11', HW200='H-200x200x8x12',
                       HW250='H-250x250x9x14', HW300='H-300x300x10x15', HW350='H-350x350x12x19',
                       HW400='H-400x400x13x21',

                       HM148='H-148x100x6x9',
                       HM194='H-194x150x6x9', HM244='H-244x175x7x11', HM294='H-294x200x8x12', HM340='H-340x250x9x14',
                       HM390='H-390x300x10x16', HM440='H-440x300x11x18', HM488='H-488x300x11x18',
                       HM582='H-582x300x12x17', HM588='H-588x300x12x20')

section_property = {}

section_property[short_full_name['HS20']] = dict(H=200, An=26.67, Ix=1810, Iy=134, ix=8.23, iy=2.24, Zx=181, Zy=26.7)


# PROPERTY,   H,  B,  t1, t2, r,   An ,   W ,    Ix,  Iy , ix,   iy,  Zx,  Zy,  ib,  η,   Zpx, Zpy
# HS-,      200,100, 5.5,  8, 8, 26.67,  20.9, 1810,  134, 8.23, 2.24, 181,26.7, 2.63, 6.57, 205,41.6

def xs_section_name(short_name):
    try:
        return short_full_name[short_name.upper()]
    except KeyError:
        return 'Section_Not_Defined'


def xs_section_property(name, property_name=None):
    try:
        full_name = short_full_name[name]
    except KeyError:
        full_name = name

    if property_name is not None:
        return section_property[full_name][property_name]
    else:
        return section_property[full_name].keys()
