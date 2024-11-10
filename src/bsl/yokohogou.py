import math
from enum import Enum
from dataclasses import dataclass, field

from xs_section import xs_section_property, short_full_name, make_all_section_db
from section_check import allowable_bending_moment
from allowable_stress import steel_fb_aij2005, steel_fb_bsl, calc_C


class Material(Enum):
    S400N = '400N'
    S490N = '490N'


class Condition(Enum):
    Mp_Mp = 'Mp_Mp'
    Mp_M1 = 'Mp_M1'


@dataclass
class Yokohogou:
    """鉄骨梁　保有耐力横補剛の検討"""
    sec: str = "H40"
    L: float = 5000.0  # (mm)
    material: Material = Material.S400N
    end_force_condition: Condition = Condition.Mp_Mp
    M_Left: float = 0.0  # 検討用梁端M 左端(N*mm)
    M_Right: float = 0.0  # 検討用梁端M 右端(N*mm)
    # restraint_location: list = field(default_factory=list)  # 補剛材位置を格納
    restraint_spans: list = field(default_factory=list)  # 横補剛の配置間隔

    db = make_all_section_db()

    def get_number_of_equivalent_placement_lateral_restraint(self) -> int:
        """ 均等配置による必要横補剛個所数 n を返す"""
        iy = xs_section_property(self.sec, 'iy', self.db) * 10  # (mm)
        lambda_y = self.L / iy
        if self.material == Material.S400N:
            n = (lambda_y - 170) / 20
        elif self.material == Material.S490N:
            n = (lambda_y - 130) / 20
        else:
            raise ValueError
        return math.ceil(n)

    def get_lb(self, step=0) -> float:
        """
        梁端部に近い部分に横補剛を設ける場合 Myを超える領域での最長補剛間隔 lb (mm)を返す
        step (mm)を指定すると、stepの倍数で、lb以下となる数値を返す。
        """
        B = xs_section_property(self.sec, 'B', self.db)
        tf = xs_section_property(self.sec, 't2', self.db)
        Af = B * tf
        H = xs_section_property(self.sec, 'H', self.db)
        iy = xs_section_property(self.sec, 'iy', self.db) * 10  # (mm)
        if self.material == Material.S400N:
            lb = min(250 * Af / H, 65 * iy)
        elif self.material == Material.S490N:
            lb = min(200 * Af / H, 50 * iy)
        else:
            raise ValueError
        if step:
            # return self.x_ceiling(lb, step)
            return self.x_flooring(lb, step)
        else:
            return lb

    @property
    def alpha(self) -> float:
        """材質の強度クラスに応じた安全率 α を返す。"""
        if self.material == Material.S400N:
            return 1.2
        elif self.material == Material.S490N:
            return 1.1
        else:
            raise ValueError

    @property
    def Mp(self) -> float:
        """全塑性モーメント Mp (N*mm)を返す"""
        Zpx = xs_section_property(self.sec, 'Zpx', self.db) * 1e3  # (mm3)
        if self.material == Material.S400N:
            return Zpx * 235.0  # (N*mm)
        elif self.material == Material.S490N:
            return Zpx * 325.0  # (N*mm)
        else:
            raise ValueError

    @property
    def My(self) -> float:
        """降伏モーメント My (N*mm)を返す"""
        Zx = xs_section_property(self.sec, 'Zx', self.db) * 1e3  # (mm3)
        if self.material == Material.S400N:
            return Zx * 235.0  # (N*mm)
        elif self.material == Material.S490N:
            return Zx * 325.0  # (N*mm)
        else:
            raise ValueError

    def Mas(self, Lb=0.0, M1=0., M2=0.) -> float:
        """短期許容曲げモーメント Mas (N*mm) を返す"""
        Zx = xs_section_property(self.sec, 'Zx', self.db) * 1e3  # (mm3)
        F = 235 if self.material == Material.S400N else 325
        fb = steel_fb_aij2005(shape_name=short_full_name[self.sec], db=self.db, lb=Lb, M1=M1, M2=M2, F=235)

        # todo : 建築基準法のfbでの検討も入れる？
        # B = xs_section_property(self.sec, 'B', self.db)
        # tf = xs_section_property(self.sec, 't2', self.db)
        # Af = B * tf
        # H = xs_section_property(self.sec, 'H', self.db)
        # iy = xs_section_property(self.sec, 'iy', self.db) * 10  # (mm)
        # ib = xs_section_property(self.sec, 'ib', self.db) * 10  # (mm)
        # c = calc_C(M1, M2)
        # fb = steel_fb_bsl(F=F, lb=Lb, i=ib, C=c, h=H, Af=Af)
        return 1.5 * fb * Zx

    def set_Me(self):
        """検討用　端部モーメントの設定を行う"""
        if self.end_force_condition == Condition.Mp_Mp:
            self.M_Left = self.alpha * self.Mp
            self.M_Right = self.alpha * self.Mp
        else:
            raise NotImplementedError

    @property
    def lb_spans(self) -> list:
        """横補剛間隔の一覧を返す"""
        return self.restraint_spans

    @property
    def lb_positions(self) -> list:
        """横補剛位置（部材左端からの距離）を返す。０、スパンを含む"""
        result = [0]
        for sp in self.restraint_spans:
            x_prev = result[-1]
            result.append(x_prev + sp)
        return result

    @property
    def Q(self):
        """想定モーメント分布に対応する せん断力 Q を返す Q = (M1+M2) / L"""
        return (self.M_Left + self.M_Right) / self.L

    def M_at(self, x):
        """指定位置の想定モーメントを返す。部材左端からの距離 x (mm)を指定"""
        return abs(self.M_Left - x * self.Q)

    def get_My_position(self) -> float:
        """端部からMyとなる位置の距離を返す（両端ヒンジの場合）"""
        self.set_Me()
        x = (self.alpha * self.Mp - self.My) / self.Q
        return x

    def set_member_end_restraints(self, step=0):
        self.restraint_spans.clear()
        self.set_Me()
        req_lb = self.get_lb(step)

        x_My = self.get_My_position()
        num_of_tanbu = int(x_My / req_lb) + 1
        tanbu_restraint_spans = []
        for i in range(num_of_tanbu):
            tanbu_restraint_spans.append(req_lb)
        for l in tanbu_restraint_spans:
            self.restraint_spans.append(l)
        for l in tanbu_restraint_spans:
            self.restraint_spans.append(l)
        # ---
        # max_n = int(self.L / (2 * req_lb))
        # for i in range(max_n):
        #     if self.M_at(i * req_lb) > self.My:
        #         self.restraint_spans.insert(i, req_lb)
        #         self.restraint_spans.insert(-i, req_lb)
        # ---

        center_span = self.L - sum(self.restraint_spans)
        tanbu_only_spans = self.restraint_spans[:]

        center_index = int(len(self.restraint_spans) / 2)
        self.restraint_spans.insert(center_index, center_span)

        # todo : 左右非対称配置となる場合の処理　2024-1104

        div_num = 2
        while self.check_hogou_rule_tanbu() == 'NG':
            center_span_div = center_span / div_num
            self.restraint_spans = tanbu_only_spans[:]
            for n in range(div_num):
                self.restraint_spans.insert(center_index, center_span_div)
            div_num += 1

    def get_input_data(self) -> str:
        """計算条件の出力用文字列を返す"""
        result = []
        result.append("=" * 20)
        result.append("保有耐力横補剛検討")
        result.append(f'スパン：{self.L} [mm]')
        result.append(f'はり断面：{short_full_name[self.sec]}')
        result.append(f'鋼材強度：{"400N" if self.material.S400N else "490N"}')
        result.append(f'Mp={self.Mp / 1e6:.2f}, My={self.My / 1e6:.2f},'
                      f' α*Mp={self.alpha * self.Mp / 1e6:.2f} [kN*m] (α={self.alpha})')
        return '\n'.join(result)

    def get_output_data(self, step=0) -> str:
        """計算結果の出力用文字列を返す"""
        result = []
        result.append('-' * 20)
        result.append('検討結果')
        result.append('方法①：均等配置')
        eq_n = self.get_number_of_equivalent_placement_lateral_restraint()
        result.append(f'  補剛数 = {eq_n}, 補剛間隔 = {self.L / (eq_n + 1):.3f} [mm]')
        iy = xs_section_property(self.sec, 'iy', self.db) * 10  # (mm)
        if self.material == Material.S400N:
            eq_str = f'170 + 20*n = {170 + 20 * eq_n}'
        else:
            eq_str = f'130 + 20*n = {130 + 20 * eq_n}'
        result.append(f'  iy = {iy} [mm], λy = {self.L / iy:.1f} < {eq_str}')

        result.append('-' * 10)
        result.append('方法②：主として端部に配置')
        self.set_member_end_restraints(step=step)
        tanbu_n = len(self.restraint_spans) - 1
        result.append(f'  補剛数 = {tanbu_n}, 補剛間隔 = {self.restraint_spans} [mm]')
        result.append(self.check_hogou_rule_tanbu(get_txt=True))
        return '\n'.join(result)

    def check_hogou_rule_tanbu(self, print_on=False, get_txt=False):
        """現状の　補剛スパンで、端部に配置の条件を満たすかチェックを行う。"""
        status = 'OK'
        result = []
        self.set_Me()
        req_max_lb = self.get_lb()
        if not self.restraint_spans:
            raise ValueError
        if not get_txt:
            result.append(str(self.restraint_spans))

        x1 = 0.0
        for span in self.restraint_spans:
            x2 = x1 + span
            m1 = self.M_at(x1)
            m2 = self.M_at(x2)
            m_max = max(m1, m2)
            m_min = min(m1, m2)
            if m_max >= self.My:
                if span <= req_max_lb:
                    result.append(
                        f'{x1:10} - {x2:8} Lb={span}: [M={m_max / 1e6:6.2f} > My] max_Lb={req_max_lb:6.2f} -> Lb_ok')
                else:
                    result.append(
                        f'{x1:10} - {x2:8} Lb={span}: [M={m_max / 1e6:6.2f} > My] max_Lb={req_max_lb:6.2f} -> Lb_NG')
                    status = 'NG'
            else:
                Mas = self.Mas(Lb=span, M1=m_max, M2=m_min)
                if m_max <= Mas:
                    result.append(
                        f'{x1:10} - {x2:8} Lb={span}: [M={m_max / 1e6:6.2f} < My]    Mas={Mas / 1e6:6.2f} -> Mas_ok')
                else:
                    result.append(
                        f'{x1:10} - {x2:8} Lb={span}: [M={m_max / 1e6:6.2f} < My]    Mas={Mas / 1e6:6.2f} -> Mas_NG')
                    status = 'NG'
            x1 = x2

        if print_on:
            print()
            print('\n'.join(result))

        if get_txt:
            return '\n'.join(result)
        return status

    @staticmethod
    def x_ceiling(x, step):
        """数値 x を x以上の　指定の数 step の倍数となるようにまるめる"""
        return -(-x // step) * step

    @staticmethod
    def x_flooring(x, step):
        """数値 x を x以下の　指定の数 step の倍数となるようにまるめる"""
        return (x // step) * step
