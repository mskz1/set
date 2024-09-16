from src.xs_section import make_all_section_db, xs_section_property, xs_section_name

from beam_formula import SimplySupportedBeamWithUniformDistributedLoad
from beam_model import SimpleBeamSteel
from section_check import section_check
from load import *

def sample1():
    db = make_all_section_db()

    sec_name = 'H24'
    a = xs_section_property(sec_name, 'An', db)
    # print(a)
    span = 6000.  # mm
    load = 1200.  # N/m2
    term = 'LONG'
    lb = 0.  # (mm)
    F = 235
    bf = SimplySupportedBeamWithUniformDistributedLoad(span / 1000., load / 1000.)
    Md = bf.getMmax()
    Dmax = bf.getDmax(I=xs_section_property(sec_name, 'Ix'), E=20500.)
    s_f = section_check(sec_name, F, term, N=0., Mx=Md, lb=lb)

    print('＝＝＝　単純梁　鉄骨断面検討　＝＝＝')
    print('メモ：単一荷重、荷重ケースの例')
    print(f'span = {span} [mm], load = {load} [N/m], 荷重種別 = {"長期" if term == "LONG" else "短期"}')
    print(f'Lb = {lb} [mm], F = {F} [N/mm2]')
    print(f'Md = {Md:.2f} [kN*m]')

    # 荷重ケースや荷重組合せをどう扱うか。モデル１つに、複数の荷重組合せ？　G　と　G+S　G+0.7S　とか。
    # ２軸曲げ
    print('================')
    print(f'断面：{xs_section_name(sec_name)}, σ/f={s_f:.2f}, たわみ={Dmax:.2f}[cm]')


def simple_beam_sample():
    beam = SimpleBeamSteel()
    beam.span = 6000.
    print(beam)


if __name__ == '__main__':
    # sample1()
    simple_beam_sample()
