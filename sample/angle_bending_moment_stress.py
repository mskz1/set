import math
import sys

from src.xs_section import *


def sample_L_100x75x7():
    # sample1  L-100x75x7　円周上の点を追加
    alpha = math.radians(28.7088147)
    rpts1 = get_points_on_arc(r=5, dx=2, dy=95, start=0, end=math.radians(90), n=32)
    rpts2 = get_points_on_arc(r=5, dx=70, dy=2, start=0, end=math.radians(90), n=32)

    pts = [(0, 0), (0, 100)]
    pts.extend(rpts1)
    pts.extend(rpts2)
    pts.extend([(75, 0)])

    # dx, dy = -18.31, -30.59
    dx, dy = -18.313859367, -30.586318718  # (mm)
    rotated_pts = get_rotated_points(pts, dx, dy, alpha)
    # Iu, Iv = 144.136, 30.76  # (cm4)
    Iu, Iv = 144.13587130, 30.759679370  # (cm4)
    # Mx, My = 40, 0  # (kN*cm)
    Mx, My = 100, 0  # (kN*cm)
    ss = get_stress_at_points_mx_my(rotated_pts, alpha, Iu, Iv, Mx, My)
    print(' Start '.center(40, '='))
    print('L-100x75x7 修正　Mx=100[kN*cm]')
    print("max_ss={:10.4f}, min_ss={:10.4f}".format(max(ss), min(ss)))

    ss2 = get_stress_at_points_m11_m22(rotated_pts, Iu, Iv, Mu=Mx * math.cos(alpha), Mv=Mx * math.sin(alpha))
    print('L-100x75x7 修正　Mu=100*cos(α)[kN*cm],Mv=100*sin(α)[kN*cm]')
    print("max_ss={:10.4f}, min_ss={:10.4f}".format(max(ss2), min(ss2)))
    print(' End '.center(40, '='))


def sample_BL_75x45():
    # sample2  BL-75x45x4.5 円周上の点を追加
    alpha = math.radians(21.107967)
    rpts1 = get_points_on_arc(r=9, dx=9, dy=9, start=math.radians(180), end=math.radians(270), n=32)
    pts = []
    pts.extend(rpts1)
    pts.extend([(0, 9), (0, 75), (4.5, 75), (45, 4.5), (45, 0), (9, 0)])
    dx, dy = -10.38, -25.77
    dx, dy = -10.380125, -25.7687

    rotated_pts = get_rotated_points(pts, dx, dy, alpha)
    # Iu, Iv = 33.501, 4.689  # (cm4)
    Iu, Iv = 33.50109163, 4.68886877  # (cm4)

    # Mx, My = 40, 0  # (kN*cm)
    Mx, My = 100, 0  # (kN*cm)
    ss = get_stress_at_points_mx_my(rotated_pts, alpha, Iu, Iv, Mx, My)
    print('BL-75x45x4.5 修正　Mx=100[kN*cm]')
    # print(ss)
    print("max_ss={:10.4f}, min_ss={:10.4f}".format(max(ss), min(ss)))

    ss2 = get_stress_at_points_m11_m22(rotated_pts, Iu, Iv, Mu=Mx * math.cos(alpha), Mv=Mx * math.sin(alpha))
    print('BL-75x45x4.5 修正　Mu=100*cos(α)[kN*cm],Mv=100*sin(α)[kN*cm]')
    print("max_ss={:10.4f}, min_ss={:10.4f}".format(max(ss2), min(ss2)))


def sample_L_65x65x6():
    # sample4  L-65x65x6 円周上の点を分割計算
    alpha = math.radians(45)
    rpts1 = get_points_on_arc(r=4, dx=2, dy=61, start=math.radians(0), end=math.radians(90), n=32)
    rpts2 = get_points_on_arc(r=4, dx=61, dy=2, start=math.radians(0), end=math.radians(90), n=32)
    pts = [(0, 0), (0, 65)]
    pts.extend(rpts1)
    pts.extend(rpts2)
    pts.extend([(65, 0)])

    # dx, dy = -18.10, -18.10
    dx, dy = -18.096555532, -18.096555532
    rotated_pts = get_rotated_points(pts, dx, dy, alpha)
    # Iu, Iv = 46.580, 12.164  # (cm4)
    Iu, Iv = 46.579727445, 12.164198330  # (cm4)
    # Mx, My = 40, 0  # (kN*cm)
    Mx, My = 100, 0  # (kN*cm)
    ss = get_stress_at_points_mx_my(rotated_pts, alpha, Iu, Iv, Mx, My)
    print(' Start '.center(40, '='))
    print('L-65x65x6 修正　Mx=100[kN*cm]')
    print("max_ss={:10.4f}, min_ss={:10.4f}".format(max(ss), min(ss)))
    print(' End '.center(40, '='))


def sample_L_90x90x10():
    # sample5  L-90x90x10 例題 円周上の点を分割計算
    alpha = math.radians(45)
    rpts1 = get_points_on_arc(r=7, dx=3, dy=83, start=math.radians(0), end=math.radians(90), n=32)
    rpts2 = get_points_on_arc(r=7, dx=83, dy=3, start=math.radians(0), end=math.radians(90), n=32)

    pts = [(0, 0), (0, 90)]
    pts.extend(rpts1)
    pts.extend(rpts2)
    pts.extend([(90, 0)])

    dx, dy = -25.722377552, -25.722377552
    rotated_pts = get_rotated_points(pts, dx, dy, alpha)
    Iu, Iv = 198.64812558, 51.619538241  # (cm4)
    # Mx, My = 40, 0  # (kN*cm)
    Mx, My = 225, 0  # (kN*cm)
    ss = get_stress_at_points_mx_my(rotated_pts, math.radians(23.2), Iu, Iv, Mx, My)
    print('L-90x90x10 修正　M=225[kN*cm] 角度あり')
    print("max_ss={:10.4f}, min_ss={:10.4f}".format(max(ss), min(ss)))

    ss = get_stress_at_points_mx_my(rotated_pts, math.radians(45.), Iu, Iv, Mx, My)
    print('L-90x90x10 修正　M=225[kN*cm]　角度なし')
    print("max_ss={:10.4f}, min_ss={:10.4f}".format(max(ss), min(ss)))

    ssuv2 = get_stress_at_points_m11_m22(rotated_pts, Iu, Iv, 207, 88.7)
    print("max_ss={:10.4f}, min_ss={:10.4f}".format(max(ssuv2), min(ssuv2)))

    Mu = Mx * math.cos(math.radians(23.2))
    Mv = Mx * math.sin(math.radians(23.2))

    ssuv3 = get_stress_at_points_m11_m22(rotated_pts, Iu, Iv, Mu, Mv)
    print("max_ss={:10.4f}, min_ss={:10.4f}".format(max(ssuv3), min(ssuv3)))


def sample_allowable_moment():
    sec_name = xs_section_name('L65*6')
    sec_name = xs_section_name('L90*10')
    sec_name = xs_section_name('L100*75*7')
    db = make_all_section_db()
    # print(sec_name)
    tan_alpha = xs_section_property(sec_name, 'tan_alpha', db)
    alpha = math.atan(tan_alpha)
    # print(alpha)
    A = xs_section_property(sec_name, 'A', db)
    B = xs_section_property(sec_name, 'B', db)
    t = xs_section_property(sec_name, 't', db)
    r1 = xs_section_property(sec_name, 'r1', db)
    r2 = xs_section_property(sec_name, 'r2', db)
    cx = xs_section_property(sec_name, 'Cx', db)
    cy = xs_section_property(sec_name, 'Cy', db)
    Iu = xs_section_property(sec_name, 'Iu', db)
    Iv = xs_section_property(sec_name, 'Iv', db)
    print('A={}, B={}, t={}, r1={}, r2={}, cx={}, cy={}, Iu={}, Iv={}'.format(A, B, t, r1, r2, cx, cy, Iu, Iv))
    rpts1 = get_points_on_arc(r=r2, dx=t - r2, dy=A - r2, start=math.radians(0), end=math.radians(90), n=32)
    rpts2 = get_points_on_arc(r=r2, dx=B - r2, dy=t - r2, start=math.radians(0), end=math.radians(90), n=32)
    pts = [(0, 0), (0, A)]
    pts.extend(rpts1)
    pts.extend(rpts2)
    pts.extend([(B, 0)])
    dx, dy = -cy * 10, -cx * 10
    rotated_pts = get_rotated_points(pts, dx, dy, alpha)
    Mx, My = 100, 0  # (kN*cm)
    # Mx, My = 225, 0  # (kN*cm)
    ss = get_stress_at_points_mx_my(rotated_pts, alpha, Iu, Iv, Mx, My)
    print(' Start '.center(40, '='))
    print('{}　Mx={}[kN*cm], My={}[kN*cm]'.format(sec_name, Mx, My))
    print("max_ss={:10.4f}, min_ss={:10.4f}".format(max(ss), min(ss)))

    fb = 23.5 / 1.5
    factor = fb / max(abs(max(ss)), abs(min(ss)))
    print('factor={:10.4f}'.format(factor))
    print('xMal={:10.4f}, yMal={:10.4f}'.format(Mx * factor, My * factor))
    print(' End '.center(40, '='))


if __name__ == '__main__':
    # sample_L_100x75x7()
    # sample_BL_75x45()
    # sample_L_65x65x6()
    # sample_L_90x90x10()
    sample_allowable_moment()
