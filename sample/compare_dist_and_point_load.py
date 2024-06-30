from src.beam_formula import SimplySupportedBeamWithUniformDistributedLoad, SimplySupportedBeamWithMultiplePointLoad
import pprint


def compare1():
    # ｎ点集中荷重と等分布荷重のモーメント、たわみの比較
    span = 8.  # m
    w = 1.0  # kN/m
    I = 1870.
    E = 20500.
    # 等分布荷重
    bf_udl = SimplySupportedBeamWithUniformDistributedLoad(span, w)
    uMmax = bf_udl.getMmax()
    uDmax = bf_udl.getDmax(I, E)
    result = [f"{'n':>5}, {'pM/uM':>10}, {'pD/uD':>10}"]
    for n in range(1, 11):
        # point_load = w * span / (n + 1)  # 荷重
        point_load = w * span / n
        bf_npl = SimplySupportedBeamWithMultiplePointLoad(span, point_load, n)
        pMmax = bf_npl.getMmax()
        pDmax = bf_npl.getDmax(I, E)
        result.append(f"{n:5}, {pMmax / uMmax:10.6f}, {pDmax / uDmax:10.6f}")

    # pprint.pprint(result)
    output_txt = '\n'.join(result)
    print(output_txt)


if __name__ == '__main__':
    compare1()
