class Simpul(object):
   def __init__(self, data):
      self.data = data
      self.kiri = None
      self.kanan = None
      
A = Simpul('Ambarawa')
B = Simpul('Bantul')
C = Simpul('Cilacap')
D = Simpul('Denpasar')
E = Simpul('Enrekang')
F = Simpul('Flores')
G = Simpul('Garut')
H = Simpul('Halmahera Timur')
I = Simpul('Indramayu')
J = Simpul('Jakarta')

A.kiri = B
A.kanan = C
B.kiri = D
B.kanan = E
C.kiri = F
C.kanan = G
E.kiri = H
G.kanan = I