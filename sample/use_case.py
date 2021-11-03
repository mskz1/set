# 利用例のコードイメージ

# 部材算定

# 小梁の例
rb1 = set.SimpleBeam()
rb1.fugou = 'RB1'
rb1.span = 6000
rb1.memo = '屋根小梁１'

load_case_g = set.load.LoadCase()
load_case_s = set.load.LoadCase()

p1 = set.load.PointLoad('GY', -10)
w1 = set.load.DistributedLoad('GY', -0.6)

load_case_g.add(p1)
load_case_g.add(w1)

p2 = set.load.PointLoad('GY', -20)
w2 = set.load.DistributedLoad('GY', -0.8)

load_case_s.add(p2)
load_case_s.add(w2)



rb1.add_load_case_combi('G', (load_case_g, 1))
rb1.add_load_case_combi('G+S', (load_case_g, 1), (load_case_s, 1))
