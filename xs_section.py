# -*- coding: utf-8 -*-

def _temp():
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
                           HM194='H-194x150x6x9', HM244='H-244x175x7x11', HM294='H-294x200x8x12',
                           HM340='H-340x250x9x14',
                           HM390='H-390x300x10x16', HM440='H-440x300x11x18', HM488='H-488x300x11x18',
                           HM582='H-582x300x12x17', HM588='H-588x300x12x20',
                           HM692='H-692x300x13x20', HM700='H-700x300x13x24', HM792='H-792x300x14x22',
                           HM800='H-800x300x14x26',
                           HM890='H-890x299x15x23', HM900='H-900x300x16x28', HM912='H-912x302x18x34',
                           HM918='H918x303x19x37',

                           MZ75='[-75x40x5x7', MZ100='[-100x50x5x7.5', MZ125='[-125x65x6x8',
                           MZ150_1='[-150x75x6.5x10', MZ150_2='[-150x75x9x12.5',
                           MZ180='[-180x75x7x10.5', MZ200_1='[-200x80x7.5x11', MZ200_2='[-200x90x8x13.5',

                           P272_19='P-27.2x1.9', P272_23='P-27.2x2.3', P427_23='P-42.7x2.3',
                           P486_23='P-48.6x2.3', P486_32='P-48.6x3.2', P605_23='P-60.5x2.3', P605_28='P-60.5x2.8',
                           P605_32='P-60.5x3.2', P763_28='P-76.3x2.8', P763_32='P-76.3x3.2',
                           P891_28='P-89.1x2.8', P891_32='P-89.1x3.2', P891_42='P-89.1x4.2',
                           P1016_32='P-101.6x3.2', P1016_35='P-101.6x3.5', P1016_42='P-101.6x4.2',
                           P1143_28='P-114.3x2.8', P1143_35='P-114.3x3.5', P1143_45='P-114.3x4.5', P1143_6='P-114.3x6',
                           P1398_35='P-139.8x3.5', P1398_4='P-139.8x4', P1398_45='P-139.8x4.5', P1398_5='P-139.8x5',
                           P1652_38='P-165.2x3.8', P1652_4='P-165.2x4', P1652_45='P-165.2x4.5', P1652_5='P-165.2x5',
                           P1907_53='P-190.7x5.3',

                           C60_16='C-60x30x10x1.6', C60_23='C-60x30x10x2.3', C75_16='C-75x45x15x1.6',
                           C75_23='C-75x45x15x2.3', C100_16='C-100x50x20x1.6', C100_23='C-100x50x20x2.3',
                           C100_32='C-100x50x20x3.2', C120_23='C-120x60x20x2.3', C120_32='C-120x60x20x3.2',
                           C125_32='C-125x50x20x3.2',

                           KP50_16='□P-50x50x1.6', KP50_23='□P-50x50x2.3', KP50_32='□P-50x50x3.2',
                           KP60_16='□P-60x60x1.6', KP60_23='□P-60x60x2.3', KP60_32='□P-60x60x3.2',
                           KP75_16='□P-75x75x1.6', KP75_23='□P-75x75x2.3', KP75_32='□P-75x75x3.2',
                           KP75_45='□P-75x75x4.5',
                           KP100_23='□P-100x100x2.3', KP100_32='□P-100x100x3.2', KP100_45='□P-100x100x4.5',
                           KP100_6='□P-100x100x6.0', KP125_32='□P-125x125x3.2', KP125_45='□P-125x125x4.5',
                           KP125_6='□P-125x125x6.0', KP125_9='□P-125x125x9.0', KP150_45='□P-150x150x4.5',
                           KP150_6='□P-150x150x6.0', KP150_9='□P-150x150x9.0', KP175_45='□P-175x175x4.5',
                           KP175_6='□P-175x175x6.0', KP175_9='□P-175x175x9.0',
                           KP200_45='□P-200x200x4.5', KP200_6='□P-200x200x6.0', KP200_8='□P-200x200x8.0',
                           KP200_9='□P-200x200x9.0',

                           KP60_30_16='□P-60x30x1.6', KP60_30_23='□P-60x30x2.3', KP60_30_32='□P-60x30x3.2',
                           KP75_45_16='□P-75x45x1.6', KP75_45_23='□P-75x45x2.3', KP75_45_32='□P-75x45x3.2',
                           KP100_50_16='□P-100x50x1.6', KP100_50_23='□P-100x50x2.3', KP100_50_32='□P-100x50x3.2',
                           KP100_50_45='□P-100x50x4.5',
                           KP125_75_23='□P-125x75x2.3', KP125_75_32='□P-125x75x3.2', KP125_75_45='□P-125x75x4.5',
                           KP125_75_6='□P-125x75x6.0', KP150_75_32='□P-150x75x3.2', KP150_75_45='□P-150x75x4.5',
                           KP150_100_32='□P-150x100x3.2', KP150_100_45='□P-150x100x4.5', KP150_100_6='□P-150x100x6.0',
                           KP200_100_45='□P-200x100x4.5', KP200_100_6='□P-200x100x6.0',
                           KP200_150_45='□P-200x150x4.5', KP200_150_6='□P-200x150x6.0', KP200_150_9='□P-200x150x9.0',
                           KP250_150_45='□P-250x150x4.5', KP250_150_6='□P-250x150x6.0', KP250_150_9='□P-250x150x9.0'
                           )
    # dict生成でキーワード引数に*が使えないため、ここで追加。
    items = list(short_full_name.items())
    for item in items:
        k, v = item[0], item[1]
        if '_' in k:
            new_k = k.replace('_', '*')
            short_full_name[new_k] = v


HS_SEC_DATA = """SERIES,HS-,H形鋼細幅,H-HxBxt1xt2
FORMAT,H-,H,B,t1,t2
PROPERTY, H,  B, t1, t2,  r,    An,     W,    Ix,    Iy, ix, iy,    Zx,    Zy, ib,   eta,   Zpx, Zpy 
UNIT,    mm, mm, mm, mm, mm, cm**2, kgf/m, cm**4, cm**4, cm, cm, cm**3, cm**3, cm,   -, cm**3, cm**3
HS-,150,75,5,7,8,17.85,14,666,49.5,6.11,1.66,88.8,13.2,1.96,5.6,102,20.7
HS-,175,90,5,8,8,22.9,18,1210,97.5,7.26,2.06,138,21.7,2.39,5.81,156,33.6
HS-,198,99,4.5,7,8,22.69,17.8,1540,113,8.25,2.24,156,22.9,2.6,7.43,175,35.5
HS-,200,100,5.5,8,8,26.67,20.9,1810,134,8.23,2.24,181,26.7,2.63,6.57,205,41.6
HS-,248,124,5,8,8,31.99,25.1,3450,255,10.4,2.82,278,41.1,3.27,8.19,312,63.2
HS-,250,125,6,9,8,36.97,29,3960,294,10.4,2.82,317,47,3.3,7.33,358,72.7
HS-,298,149,5.5,8,13,40.8,32,6320,442,12.4,3.29,424,59.3,3.85,9.61,475,91.7
HS-,300,150,6.5,9,13,46.78,36.7,7210,508,12.4,3.29,481,67.7,3.87,8.61,542,105
HS-,346,174,6,9,13,52.45,41.2,11000,791,14.5,3.88,638,91,4.53,10,712,140
HS-,350,175,7,11,13,62.91,49.4,13500,984,14.6,3.96,771,112,4.6,8.35,864,173
HS-,396,199,7,11,13,71.41,56.1,19800,1450,16.6,4.5,999,145,5.23,9.45,1110,223
HS-,400,200,8,13,13,83.37,65.4,23500,1740,16.8,4.56,1170,174,5.29,8.13,1310,267
HS-,446,199,8,12,13,82.97,65.1,28100,1580,18.4,4.36,1260,159,5.16,9.64,1420,245
HS-,450,200,9,14,13,95.43,74.9,32900,1870,18.6,4.43,1460,187,5.23,8.4,1650,290
HS-,496,199,9,14,13,99.29,77.9,40800,1840,20.3,4.31,1650,185,5.14,9.16,1870,288
HS-,500,200,10,16,13,112.2,88.2,46800,2140,20.4,4.36,1870,214,5.2,8.13,2130,333
HS-,596,199,10,15,13,117.8,92.5,66600,1980,23.8,4.1,2240,199,5.03,10,2580,312
HS-,600,200,11,17,13,131.7,103,75600,2270,24,4.16,2520,227,5.09,8.98,2900,358"""

HM_SEC_DATA = """SERIES,HM-,H形鋼中幅,H-HxBxt1xt2
FORMAT,H-,H,B,t1,t2
PROPERTY, H,  B, t1, t2, r , An ,   W ,  Ix, Iy , ix, iy,  Zx,  Zy, ib, eta, Zpx, Zpy 
UNIT,    mm, mm, mm, mm, mm, cm**2, kgf/m, cm**4, cm**4, cm, cm, cm**3, cm**3, cm,   -, cm**3, cm**3
HM-,148,100,6,9,8,26.35,20.7,1000,150,6.17,2.39,135,30.1,2.71,4.46,154,46.4
HM-,194,150,6,9,8,38.11,29.9,2630,507,8.3,3.65,271,67.6,4.09,5.87,301,103
HM-,244,175,7,11,13,55.49,43.6,6040,984,10.4,4.21,495,112,4.72,5.99,550,172
HM-,294,200,8,12,13,71.05,55.8,11100,1600,12.5,4.75,756,160,5.38,6.59,842,245
HM-,340,250,9,14,13,99.53,78.1,21200,3650,14.6,6.05,1250,292,6.79,6.6,1380,445
HM-,390,300,10,16,13,133.2,105,37900,7200,16.9,7.35,1940,480,8.19,6.66,2140,730
HM-,440,300,11,18,13,153.9,121,54700,8110,18.9,7.26,2490,540,8.16,6.65,2760,823
HM-,482,300,11,15,13,141.2 ,111,58300,6760,20.3 ,6.92 ,2420,450 ,7.99,8.56,2700,690
HM-,488,300,11,18,13,159.2,125,68900,8110,20.8,7.14,2820,540,8.1,7.32,3130,825
HM-,582,300,12,17,13,169.2,133,98900,7660,24.2,6.73,3400,511,7.9,9.01,3820,786
HM-,588,300,12,20,13,187.2,147,114000,9010,24.7,6.94,3890,601,8.01,7.85,4350,921
HM-,692,300,13,20,18,207.5 ,163,168000,9020,28.5 ,6.59 ,4870,601,7.81,9.01,5500,930
HM-,700,300,13,24,18,231.5 ,182,197000,10800,29.2 ,6.83 ,5640,721,7.95,7.73,6340,1110
HM-,792,300,14,22,18,239.5 ,188,248000,9920,32.2 ,6.44 ,6270,661,7.74,9.28,7140,1030
HM-,800,300,14,26,18,263.5 ,207,286000,11700,33.0 ,6.67 ,7160,781,7.87,8.08,8100,1210
HM-,890,299,15,23,18,266.9 ,210,339000,10300,35.6 ,6.20 ,7610,687,7.59,9.83,8750,1080
HM-,900,300,16,28,18,305.8 ,240,404000,12600,36.4 ,6.43 ,8990,842,7.75,8.31,10300,1320
HM-,912,302,18,34,18,360.1 ,283,491000,15700,36.9 ,6.59 ,10800,1040,7.90,7.01,12300,1620
HM-,918,303,19,37,18,387.4 ,304,535000,17200,37.2 ,6.67 ,11700,1140,7.96,6.52,13400,1780
"""

HW_SEC_DATA = """SERIES,HW-,H形鋼広幅,H-HxBxt1xt2
FORMAT,H-,H,B,t1,t2
PROPERTY, H,  B, t1, t2, r , An ,   W ,  Ix, Iy , ix, iy,  Zx,  Zy, ib, eta, Zpx, Zpy 
UNIT,    mm, mm, mm, mm, mm, cm**2, kgf/m, cm**4, cm**4, cm, cm, cm**3, cm**3, cm,   m/m, cm**3, cm**3
HW-,100,100,6,8,8,21.59,16.9,378,134,4.2,2.49,75.6,26.7,2.75,3.44,86.4,41
HW-,125,125,6.5,9,8,30,23.6,839,293,5.29,3.13,134,46.9,3.45,3.84,152,71.7
HW-,150,150,7,10,8,39.65,31.1,1620,563,6.4,3.77,216,75.1,4.15,4.15,243,114
HW-,175,175,7.5,11,13,51.42,40.4,2900,984,7.5,4.37,331,112,4.8,4.36,370,172
HW-,200,200,8,12,13,63.53,49.9,4720,1600,8.62,5.02,472,160,5.5,4.59,525,244
HW-,250,250,9,14,13,91.43,71.8,10700,3650,10.8,6.32,860,292,6.91,4.93,953,443
HW-,300,300,10,15,13,118.4,93,20200,6750,13.1,7.55,1350,450,8.28,5.52,1480,683
HW-,350,350,12,19,13,171.9,135,39800,13600,15.2,8.89,2280,776,9.71,5.11,2520,1180
HW-,400,400,13,21,22,218.7,172,66600,22400,17.5,10.1,3330,1120,11,5.25,3670,1700"""

KP_SEC_DATA = """SERIES,KP-,角形鋼管,□P-HxBxt
FORMAT,□P-,H,B,t
PROPERTY,H,B,t,An,W,Ix,Iy,ix,iy,Zx,Zy,Zpx,Zpy
UNIT,mm,mm,mm,cm**2,kgf/m,cm**4,cm**4,cm,cm,cm**3,cm**3,cm**3,cm**3
KP-,50,50,1.6,3.032,2.38,11.7,11.7,1.96,1.96,4.68,4.68,5.46,5.46
KP-,50,50,2.3,4.252,3.34,15.9,15.9,1.93,1.93,6.34,6.34,7.52,7.52
KP-,50,50,3.2,5.727,4.50,20.4,20.4,1.89,1.89,8.16,8.16,9.89,9.89
KP-,60,60,1.6,3.672,2.88,20.7,20.7,2.37,2.37,6.89,6.89,7.99,7.99
KP-,60,60,2.3,5.172,4.06,28.3,28.3,2.34,2.34,9.44,9.44,11.1,11.1
KP-,60,60,3.2,7.007,5.50,36.9,36.9,2.30,2.3,12.3,12.3,14.7,14.7
KP-,75,75,1.6,4.632,3.64,41.3,41.3,2.99,2.99,11.0,11.0,12.7,12.7
KP-,75,75,2.3,6.552,5.14,57.1,57.1,2.95,2.95,15.2,15.2,17.7,17.7
KP-,75,75,3.2,8.927,7.01,75.5,75.5,2.91,2.91,20.1,20.1,23.8,23.8
KP-,75,75,4.5,12.17,9.55,98.6,98.6,2.85,2.85,26.3,26.3,31.7,31.7
KP-,100,100,2.3,8.852,6.95,140,140.0,3.97,3.97,27.9,27.9,32.3,32.3
KP-,100,100,3.2,12.13,9.52,187,187.0,3.93,3.93,37.5,37.5,43.7,43.7
KP-,100,100,4.5,16.67,13.1,249,249.0,3.87,3.87,49.9,49.9,59.0,59.0
KP-,100,100,6,21.63,17.0,311,311.0,3.79,3.79,62.3,62.3,75.1,75.1
KP-,125,125,3.2,15.33,12.0,376,376.0,4.95,4.95,60.1,60.1,69.6,69.6
KP-,125,125,4.5,21.17,16.6,506,506.0,4.89,4.89,80.9,80.9,94.8,94.8
KP-,125,125,6,27.63,21.7,641,641.0,4.82,4.82,103 ,103.0,122,122.0
KP-,125,125,9,39.67,31.1,865,865.0,4.67,4.67,138 ,138.0,169,169.0
KP-,150,150,4.5,25.67,20.1,896,896.0,5.91,5.91,120 ,120.0,139,139.0
KP-,150,150,6,33.63,26.4,1150,1150.0,5.84,5.84,153 ,153.0,180,180.0
KP-,150,150,9,48.67,38.2,1580,1580.0,5.69,5.69,210 ,210.0,253,253.0
KP-,175,175,4.5,30.17,23.7,1450,1450.0,6.93,6.93,166 ,166.0,192,192.0
KP-,175,175,6,39.63,31.1,1860,1860.0,6.86,6.86,213 ,213.0,249,249.0
KP-,175,175,9,57.67,45.3,2600,2600.0,6.71,6.71,297 ,297.0,354,354.0
KP-,200,200,4.5,34.67,27.2,2190,2190.0,7.95,7.95,219 ,219.0,253,253.0
KP-,200,200,6,45.63,35.8,2830,2830.0,7.88,7.88,283 ,283.0,330,330.0
KP-,200,200,8,59.79,46.9,3620,3620.0,7.78,7.78,362 ,362.0,426,426.0
KP-,200,200,9,66.67,52.3,3990,3990.0,7.73,7.73,399 ,399.0,472,472.0
#
KP-,60,30,1.6,2.712,2.13,12.5,4.25,2.15,1.25,4.16,2.83,5.19,3.20
KP-,60,30,2.3,3.792,2.98,16.8,5.65,2.11,1.22,5.61,3.76,7.11,4.37
KP-,60,30,3.2,5.087,3.99,21.4,7.08,2.05,1.18,7.15,4.72,9.27,5.66
KP-,75,45,1.6,3.672,2.88,28.4,12.9,2.78,1.88,7.56,5.75,9.16,6.46
KP-,75,45,2.3,5.172,4.06,38.9,17.6,2.74,1.84,10.4,7.82,12.7,8.94
KP-,75,45,3.2,7.007,5.50,50.8,22.8,2.69,1.80,13.5,10.1,16.9,11.8
KP-,100,50,1.6,4.632,3.64,61.3,21.1,3.64,2.13,12.3,8.43,15.0,9.33
KP-,100,50,2.3,6.552,5.14,84.8,29.0,3.60,2.10,17.0,11.6,21.0,13.0
KP-,100,50,3.2,8.927,7.01,112,38.0,3.55,2.06,22.5,15.2,28.2,17.4
KP-,100,50,4.5,12.17,9.55,147,48.9,3.47,2.00,29.3,19.5,37.6,23.0
KP-,125,75,2.3,8.852,6.95,192,87.5,4.65,3.14,30.6,23.3,37.0,26.1
KP-,125,75,3.2,12.13,9.52,257,117,4.60,3.10,41.1,31.1,50.1,35.3
KP-,125,75,4.5,16.67,13.1,342,155,4.53,3.04,54.8,41.2,67.7,47.5
KP-,125,75,6,21.63,17.0,428,192,4.45,2.98,68.5,51.1,86.2,60.3
KP-,150,75,3.2,13.73,10.8,402,137,5.41,3.16,53.6,36.6,66.3,41.0
KP-,150,75,4.5,18.92,14.9,539,183,5.34,3.11,71.9,48.7,90.0,55.5
KP-,150,100,3.2,15.33,12.0,488,262,5.64,4.14,65.1,52.5,78.0,59.2
KP-,150,100,4.5,21.17,16.6,658,352,5.58,4.08,87.7,70.4,106,80.5
KP-,150,100,6,27.63,21.7,835,444,5.50,4.01,111,88.8,137,103
KP-,200,100,4.5,25.67,20.1,1330,455,7.20,4.21,133,90.9,165,102
KP-,200,100,6,33.63,26.4,1700,577,7.12,4.14,170,115,213,132
KP-,200,150,4.5,30.17,23.7,1760,1130,7.64,6.13,176,151,209,172
KP-,200,150,6,39.63,31.1,2270,1460,7.56,6.06,227,194,271,223
KP-,200,150,9,57.67,45.3,3170,2020,7.41,5.93,317,270,386,317
KP-,250,150,4.5,34.67,27.2,3000,1370,9.31,6.29,240,183,290,205
KP-,250,150,6,45.63,35.8,3890,1770,9.23,6.22,311,236,378,266
KP-,250,150,9,66.67,52.3,5480,2470,9.06,6.09,438,330,542,380
#"""

P_SEC_DATA = """SERIES,P-,鋼管,P-Dxt
FORMAT,P-,D,t
PROPERTY,D,t,An,W,Ix,ix,Zx,Zxp
UNIT,mm,mm,cm**2,kgf/m,cm**4,cm,cm**3,cm**3
P-,27.2,1.9,1.51,1.24,1.26,0.897,0.93,1.22
P-,27.2,2.3,1.799,1.41,1.41,0.88,1.03,1.43
P-,42.7,2.3,2.92,2.29,5.97,1.43,2.8,3.75
P-,48.6,2.3,3.345,2.63,8.99,1.64,3.7,4.93
P-,48.6,3.2,4.564,3.58,11.8,1.61,4.86,6.6
P-,60.5,2.3,4.205,3.3,17.8,2.06,5.9,7.79
P-,60.5,2.8,5.073,3.98,21.2,2.04,7,9.33
P-,60.5,3.2,5.76,4.52,23.7,2.03,7.84,10.5
P-,76.3,2.8,6.465,5.08,43.7,2.6,11.5,15.1
P-,76.3,3.2,7.35,5.77,49.2,2.59,12.9,17.1
P-,89.1,2.8,7.59,5.96,70.7,3.05,15.9,20.9
P-,89.1,3.2,8.64,6.78,79.8,3.04,17.9,23.6
P-,89.1,4.2,11.2,8.79,101,3.01,22.7,30.3
P-,101.6,3.2,9.89,7.76,120,3.48,23.6,31
P-,101.6,3.5,10.79,8.47,130,3.47,25.6,33.67
P-,101.6,4.2,12.85,10.1,153,3.45,30.1,39.87
P-,114.3,2.8,9.808,7.7,153,3.94,26.7,34.82
P-,114.3,3.5,12.18,9.56,187,3.92,32.7,42.98
P-,114.3,4.5,15.5,12.2,234,3.89,41,54.3
P-,114.3,6,20.41,16,300,3.83,52.5,70.45
P-,139.8,3.5,14.99,11.8,348,4.82,49.8,65.04
P-,139.8,4,17.1,13.4,394,4.8,56.3,73.8
P-,139.8,4.5,19.1,15,438,4.79,62.7,82.4
P-,139.8,5,21.17,16.6,482,4.77,68.9,90.9
P-,165.2,3.8,19.27,15.1,628,5.71,76,99
P-,165.2,4,20.26,15.9,658,5.7,79.7,104
P-,165.2,4.5,22.7,17.8,734,5.68,88.9,116
P-,165.2,5,25.2,19.8,808,5.67,97.8,128
P-,190.7,5.3,30.87,24.2,1330,6.56,139,182
"""

C_SEC_DATA = """SERIES,C-,リップ付き軽量溝形鋼,C-HxBxCxt
FORMAT,C-,H,B,C,t
PROPERTY,H,B,C,t,An,W,Cx,Cy,Ix,Iy,ix,iy,Zx,Zy,Sx,Sy
UNIT,mm,mm,mm,mm,cm**2,kgf/m,cm,cm,cm**4,cm**4,cm,cm,cm**3,cm**3,cm,cm
C-,60,30,10,1.6,2.072,1.63,0,1.06,11.6,2.56,2.37,1.11,3.88,1.32,2.5,0
C-,60,30,10,2.3,2.872,2.25,0,1.06,15.6,3.32,2.33,1.07,5.2,1.71,2.5,0
C-,75,45,15,1.6,2.952,2.32,0,1.72,27.1,8.71,3.03,1.72,7.24,3.13,4.1,0
C-,75,45,15,2.3,4.137,3.25,0,1.72,37.1,11.8,3,1.69,9.9,4.24,4,0
C-,100,50,20,1.6,3.403,2.88,0,1.87,58.4,14,3.99,1.95,11.7,4.36,4.5,0
C-,100,50,20,2.3,5.172,4.06,0,1.86,80.7,19,3.95,1.92,16.1,6.06,4.4,0
C-,100,50,20,3.2,7.007,5.5,0,1.86,107,24.5,3.9,1.87,21.3,7.81,4.4,0
C-,120,60,20,2.3,6.083,4.78,0,2.13,140,31.3,4.79,2.27,23.3,8.09,5.1,0
C-,120,60,20,3.2,8.287,6.51,0,2.12,186,40.9,4.74,2.22,31,10.5,4.9,0
C-,125,50,20,3.2,7.807,6.13,0,1.68,181,26.6,4.82,1.85,29,8.02,4,0
"""

MZ_SEC_DATA = """SERIES,[-,溝形鋼,[-HxBxt1xt2
FORMAT,[-,H,B,t1,t2
PROPERTY,H,B,t1,t2,r1,r2,An,W,Ix,Iy,ix,iy,Zx,Zy,Cy
UNIT,mm,mm,mm,mm,mm,mm,cm**2,kgf/m,cm**4,cm**4,cm,cm,cm**3,cm**3,cm
[-,75,40,5,7,8,4,8.82,6.92,75.3,12.2,2.92,1.17,20.1,4.47,1.28
[-,100,50,5,7.5,8,4,11.92,9.36,188,26,3.97,1.48,37.6,7.52,1.54
[-,125,65,6,8,8,4,17.11,13.4,424,61.8,4.98,1.9,67.8,13.4,1.9
[-,150,75,6.5,10,10,5,23.71,18.6,861,117,6.03,2.22,115,22.4,2.28
[-,150,75,9,12.5,15,7.5,30.59,24,1050,147,5.86,2.19,140,28.3,2.31
[-,180,75,7,10.5,11,5.5,27.2,21.4,1380,131,7.12,2.19,153,24.3,2.13
[-,200,80,7.5,11,12,6,31.33,24.6,1950,168,7.88,2.32,195,29.1,2.21
[-,200,90,8,13.5,14,7,38.65,30.3,2490,277,8.02,2.68,249,44.2,2.74
"""

L_SEC_DATA = """SERIES,L-,等辺山形鋼,L-AxBxt
FORMAT,L-,A,B,t
PROPERTY,A,B,t,r1,r2,An,W,Ix,Iy,Iu,Iv,ix,iy,iu,iv,Zx,Zy
UNIT,mm,mm,mm,mm,mm,cm**2,kg/m,cm**4,cm**4,cm**4,cm**4,cm,cm,cm,cm,cm**3,cm**3
L-,30,30,3,4,2,1.727,1.36,1.42,1.42,2.26,0.59,0.908,0.908,1.14,0.585,0.661,0.661
L-,30,30,5,4,3,2.746,2.16,2.14,2.14,3.37,0.902,0.882,0.882,1.11,0.573,1.03,1.03
L-,40,40,3,4.5,2,2.336,1.83,3.53,3.53,5.6,1.46,1.23,1.23,1.55,0.79,1.21,1.21
L-,40,40,5,4.5,3,3.755,2.95,5.42,5.42,8.59,2.25,1.2,1.2,1.51,0.774,1.91,1.91
L-,45,45,4,6.5,3,3.492,2.74,6.5,6.5,10.3,2.7,1.36,1.36,1.72,0.88,2,2
L-,45,45,5,6.5,3,4.302,3.38,7.91,7.91,12.5,3.29,1.36,1.36,1.71,0.874,2.46,2.46
L-,50,50,4,6.5,3,3.892,3.06,9.06,9.06,14.4,3.76,1.53,1.53,1.92,0.983,2.49,2.49
L-,50,50,5,6.5,3,4.802,3.77,11.1,11.1,17.5,4.58,1.52,1.52,1.91,0.976,3.08,3.08
L-,50,50,6,6.5,4.5,5.644,4.43,12.6,12.6,20,5.23,1.5,1.5,1.88,0.963,3.55,3.55
L-,60,60,4,6.5,3,4.692,3.68,16,16,25.4,6.62,1.85,1.85,2.33,1.19,3.66,3.66
L-,60,60,5,6.5,3,5.802,4.55,19.6,19.6,31.2,8.09,1.84,1.84,2.32,1.18,4.52,4.52
L-,65,65,5,8.5,3,6.367,5,25.3,25.3,40.1,10.5,1.99,1.99,2.51,1.28,5.35,5.35
L-,65,65,6,8.5,4,7.527,5.91,29.4,29.4,46.6,12.2,1.98,1.98,2.49,1.27,6.26,6.26
L-,65,65,8,8.5,6,9.761,7.66,36.8,36.8,58.3,15.3,1.94,1.94,2.44,1.25,7.96,7.96
L-,70,70,6,8.5,4,8.127,6.38,37.1,37.1,58.9,15.3,2.14,2.14,2.69,1.37,7.33,7.33
L-,75,75,6,8.5,4,8.727,6.85,46.1,46.1,73.2,19,2.3,2.3,2.9,1.48,8.47,8.47
L-,75,75,9,8.5,6,12.69,9.96,64.4,64.4,102,26.7,2.25,2.25,2.84,1.45,12.1,12.1
L-,75,75,12,8.5,6,16.56,13,81.9,81.9,129,34.5,2.22,2.22,2.79,1.44,15.7,15.7
L-,80,80,6,8.5,4,9.327,7.32,56.4,56.4,89.6,23.2,2.46,2.46,3.1,1.58,9.7,9.7
L-,90,90,6,10,5,10.55,8.28,80.7,80.7,128,33.4,2.77,2.77,3.48,1.78,12.3,12.3
L-,90,90,7,10,5,12.22,9.59,93,93,148,38.3,2.76,2.76,3.48,1.77,14.2,14.2
L-,90,90,10,10,7,17,13.3,125,125,199,51.7,2.71,2.71,3.42,1.74,19.5,19.5
L-,90,90,13,10,7,21.71,17,156,156,248,65.3,2.68,2.68,3.38,1.73,24.8,24.8
L-,100,100,7,10,5,13.62,10.7,129,129,205,53.2,3.08,3.08,3.88,1.98,17.7,17.7
L-,100,100,10,10,7,19,14.9,175,175,278,72,3.04,3.04,3.83,1.95,24.4,24.4
L-,100,100,13,10,7,24.31,19.1,220,220,348,91.1,3,3,3.78,1.94,31.1,31.1
L-,120,120,8,12,5,18.76,14.7,258,258,410,106,3.71,3.71,4.67,2.38,29.5,29.5
L-,130,130,9,12,6,22.74,17.9,366,366,583,150,4.01,4.01,5.06,2.57,38.7,38.7
L-,130,130,12,12,8.5,29.76,23.4,467,467,743,192,3.96,3.96,5,2.54,49.9,49.9
L-,130,130,15,12,8.5,36.75,28.8,568,568,902,234,3.93,3.93,4.95,2.53,61.5,61.5
L-,150,150,12,14,7,34.77,27.3,740,740,1180,304,4.61,4.61,5.82,2.96,68.1,68.1
L-,150,150,15,14,10,42.74,33.6,888,888,1410,365,4.56,4.56,5.75,2.92,82.6,82.6
L-,150,150,19,14,10,53.38,41.9,1090,1090,1730,451,4.52,4.52,5.69,2.91,103,103
"""


def xs_section_all_data(db, sr=None):
    """dbに登録されている断面(key)の名称を返す。略称も追加"""

    #  TODO シリーズ名のパラメーター　文字列の場合、リストに変換せずともOKか？
    def get_keys_from_value(d, val):
        return [k for k, v in d.items() if v == val]

    all_sr = ['H', '□', 'P', 'C', '[', 'L']
    if not sr:
        sr = all_sr
    res = []
    names = db.keys()
    for name in names:
        if name[0] in sr:
            sh_names = get_keys_from_value(short_full_name, name)
            sh_names_str = ''
            for sh_name in sh_names:
                sh_names_str += sh_name + ', '
            if sh_names_str.endswith(', '):
                sh_names_str = sh_names_str[:-2]
            res.append('[ ' + sh_names_str + ' ]' + ' : ' + name)
    # return ", ".join(res)
    return "\r\n".join(res)








def xs_show_all_data(db):
    #  部材種類順に、すべての略称：フル名称を返す。上記xs_section_all_dataで事足りる？　作成中だが＜保留＞
    srs = ['H', 'MZ', 'KP', 'C', 'P', 'L']
    res = []
    return sorted(short_full_name.items())


def xs_section_help():
    return """登録されている鉄骨断面の断面性能などを返します。
xsSectionName()

xsSectionProperty()"""


def xs_section_name(short_name):
    """
    短縮名（略名）から、フル名称を返す。
    'x'が含まれている場合は、フル名称としてそのまま返す。
    :param short_name:
    :return:
    """
    # 文字列
    if 'x' in short_name:
        return short_name
    try:
        return short_full_name[short_name.upper()]
    except KeyError:
        return 'Section_Not_Defined'


def xs_section_property(name, property_name=None, db=None):
    """
    断面名称と断面特性名から、断面特性値を返す。
    断面名称が略名の時は内部でフル名称に変換する。
    断面特性のディクショナリデータが渡されたらそれを用い、渡されなければ生成する。
    property_name = 'ALL'の時は、登録されている断面特性名全てを文字列で返す。
    :param name:
    :param property_name:
    :param db:
    :return:数値あるいは文字列
    UDF用公開関数
    """
    try:
        full_name = short_full_name[name.upper()]
    except KeyError:
        full_name = name
    if db is None:
        db = make_all_section_db()
    try:
        if property_name is not None and property_name.upper() == 'ALL':
            return str(db[full_name][1])

        if property_name is not None:
            return db[full_name][0][property_name]
        else:
            return db[full_name][1]
    except KeyError:
        return 'NO_DATA'


def make_section_db(csv_data):
    """
    CSV文字列を受け取り、断面名称をキー、断面特性データ（辞書）と断面特性名（リスト）のリストを値とする辞書を返す。
    :param csv_data:
    :return:
    """
    db = {}
    series_data, format_data, property_name_data, unit_data = [], [], [], []
    series_sym = ""
    lines = csv_data.split('\n')

    for line in lines:
        data = [x.strip() for x in line.split(',')]
        if data[0] == 'SERIES':
            series_data = data[1:]
            series_sym = series_data[0]
        if data[0] == 'FORMAT':
            format_data = data[1:]
        if data[0] == 'PROPERTY':
            property_name_data = data[1:]
        if data[0] == 'UNIT':
            unit_data = data[1:]
        if series_sym and data[0] == series_sym:
            prop_data = data[1:]
            sec_d = {}
            section_name = format_data[0]
            section_name_prop = format_data[1:]
            section_name_val = []
            property_name_unit = []
            for n, u, v in zip(property_name_data, unit_data, prop_data):
                property_name_unit.append("{}({})".format(n, u))
                if n in section_name_prop:
                    section_name_val.append(v)
            for n, v in zip(section_name_prop, section_name_val):
                section_name += v + 'x'
            section_name = section_name[:-1]
            for n, u, v in zip(property_name_data, unit_data, prop_data):
                sec_d[n] = float(v)
            db[section_name] = [sec_d, property_name_unit]
    return db


def make_all_section_db():
    """
    複数の鋼材種別のデータをまとめたデータを生成し、返す。
    :return:
    """
    db = make_section_db(HS_SEC_DATA)
    db.update(make_section_db(HM_SEC_DATA))
    db.update(make_section_db(HW_SEC_DATA))
    db.update(make_section_db(KP_SEC_DATA))
    db.update(make_section_db(P_SEC_DATA))
    db.update(make_section_db(C_SEC_DATA))
    db.update(make_section_db(MZ_SEC_DATA))
    db.update(make_section_db(L_SEC_DATA))
    return db


def make_short_name(db):
    """
    dbから省略名を生成する
    :param db:鋼材データ
    :return: 省略名 => フル名称の辞書
    """
    names = db.keys()
    res = {}
    for name in names:
        if name[0] == 'H':
            h, w, t1, t2 = name[2:].split('x')
            sh_name = 'H' + h + '*' + w

            res[sh_name] = name
            if int(h) in [150, 175, 198, 200, 248, 250, 298, 300, 346, 350, 396, 400, 446, 450, 496, 500, 596,
                          600] and h != w:
                res['H{}'.format(h[:2])] = name
            if int(h) in [148, 194, 244, 294, 340, 390, 440, 482, 488, 582, 588, 692, 700, 792, 800, 890, 900, 912,
                          918]:
                res['H{}'.format(h)] = name
            if int(h) in [100, 125, 150, 175, 200, 250, 300, 350, 400] and h == w:
                res['H{}'.format(h)] = name

        # 鋼管の場合　P89.1*2.8, p139.8*4.5 など
        if name[0] == 'P':
            sh_name = name.replace('-', '').replace('x', '*')
            res[sh_name] = name
        # 角パイプの場合　KP100*100*3.2, kp150*100*4.5 など
        if name[0] == '□':
            h, w, t = name[3:].split('x')

            sh_name = name.replace('□', 'K').replace('-', '').replace('x', '*')
            if sh_name.endswith('.0'):
                sh_name = sh_name[:-2]
            res[sh_name] = name
            if h == w:
                res['KP{}*{}'.format(h, t)] = name

        # C形鋼の場合 C100*50*2.3, C125*50*3.2 など
        if name[0] == 'C':
            h, w, l, t = name[2:].split('x')
            sh_name = 'C' + h + '*' + w + '*' + t
            res[sh_name] = name

        # 溝形鋼の場合 MZ100*50, mz150*75 など
        if name[0] == '[':
            h, w, t1, t2 = name[2:].split('x')
            sh_name = 'MZ' + h + '*' + w
            # 150x75 2種類対応 既に登録されているときは、t1を追加
            if sh_name in res:
                sh_name += '*' + t1
            res[sh_name] = name
            if sh_name in ['MZ75*40', 'MZ100*50', 'MZ125*65', 'MZ150*75', 'MZ180*75', 'MZ200*80']:
                sh_name2 = 'MZ' + h
                res[sh_name2] = name

        # 等辺山形鋼の場合 L65*65*6, L65*6 どちらも可
        if name[0] == 'L':
            a, b, t = name[2:].split('x')
            sh_name = 'L' + a + '*' + b + '*' + t
            res[sh_name] = name
            sh_name = 'L' + a + '*' + t
            res[sh_name] = name
    return res


# import された時点で、省略名の辞書データを生成する
short_full_name = make_short_name(make_all_section_db())
# print(short_full_name)
