# todo:　公開関数
# todo: 表形式の出力

def get_T(h: float, alpha: float = 1.0) -> float:
    """
    設計用一次固有周期を算出 （建築基準法　施行令88条　告示昭和55建告第1793号）
    :param h: 建築物の高さ（m）
    :param alpha: 木造・鉄骨造である階の高さの合計のhに対する比
    :return:
    """
    return h * (0.02 + 0.01 * alpha)


def get_Rt(T: float, Tc: float = 0.8) -> float:
    """
    振動特性係数を算出（建築基準法　施行令88条　告示昭和55建告第1793号）
    :param T: 設計用一次固有周期（秒）
    :param Tc:基礎底部直下の地盤種別に応じた値　第１種地盤 0.4、第２種地盤 0.6、第３種地盤 0.8
    :return:
    """
    if T < Tc:
        return 1.0
    elif Tc <= T < 2 * Tc:
        return 1 - 0.2 * ((T / Tc) - 1) ** 2
    else:  # 2*Tc < T
        return 1.6 * Tc / T


def xxx_get_alpha_i(w: list) -> list:
    """ ＊＊＊ 消す？ ＊＊＊
    Aiを算出する高さの部分が支える荷重 / 建物全体の荷重の和 の数値を算出
    :param w: 建物の層ごとの荷重（リスト）
    :return:
    """
    result = []
    total_w = sum(w)
    for wi in w:
        result.append(wi / total_w)
    return result


def get_alpha_i(goukei_w: list) -> list:
    """
    Aiを算出する高さの部分が支える荷重 / 建物全体の荷重の和 の数値を算出
    :param w: 建物の層位置で支える荷重（上層からの加算）（リスト）
    :return:
    """
    result = []
    total_w = goukei_w[0]
    for wi in goukei_w:
        result.append(wi / total_w)
    return result


def get_sum_of_W(w: list) -> list:
    """
    層ごとの重量のリストから、上層の重量を加算したリストを返す
    :param w: 建物の層ごとの荷重（リスト）下層から上層の順
    :return:
    """
    result = []
    w.reverse()
    w_prev = 0
    for wi in w:
        result.append(wi + w_prev)
        w_prev += wi
    result.reverse()
    return result


def get_Ai(alpha_i: list, T: float) -> list:
    """
    Aiを算出する
    :param alpha_i: 層が支える重量の全体に対する比率（リスト）
    :param T: 設計用一次固有周期（秒）
    :return:
    """
    result = []
    for alpha in alpha_i:
        result.append(1 + (1 / alpha ** 0.5 - alpha) * 2 * T / (1 + 3 * T))
    return result


def get_Qi(goukei_w: list, Ai: list, C0=0.2, Z=1.0, Rt=1.0):
    """
    Qiを算出する
    :param goukei_w: 各層が支える重量（リスト）下層から上層の順
    :param Ai: Ai分布（リスト）
    :param C0: ベースシェア係数
    :param Z: 地域係数
    :param Rt: 振動特性係数
    :return:
    """
    if len(goukei_w) != len(Ai):
        return
    result = []
    for w, ai in zip(goukei_w, Ai):
        result.append(w * Z * Rt * ai * C0)
    return result


def get_Pi(Qi: list) -> list:
    """
    層せん断力から、各層に作用させる荷重を算出
    :param Qi: 層せん断力（リスト）
    :return:
    """
    result = []
    Qi.reverse()
    q_prev = 0
    for q in Qi:
        result.append(q - q_prev)
        q_prev = q
    result.reverse()
    return result


def pub_get_Qi(w: list, T, Tc=0.6, C0=0.2, Z=1.0) -> list:
    """
    層せん断力を算出する
    :param w: 建物の層ごとの荷重（リスト）下層から上層の順
    :param T: 設計用一次固有周期（秒）
    :param Tc: 基礎底部直下の地盤種別に応じた値　第１種地盤 0.4、第２種地盤 0.6、第３種地盤 0.8
    :param C0: ベースシェア係数
    :param Z: 地域係数
    :return:
    """
    Rt = get_Rt(T, Tc)
    goukei_w = get_sum_of_W(w)
    alpha_i = get_alpha_i(goukei_w)
    return get_Qi(goukei_w, get_Ai(alpha_i, T), C0, Z, Rt)
