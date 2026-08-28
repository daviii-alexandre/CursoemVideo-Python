# Calcular a hipotenusa

from math import hypot
CatOp = float(input('Comprimento do Cateto Oposto: '))
CatAd = float(input('Comprimento do Cateto Adjascente: '))
hip = hypot(CatOp, CatAd)
print('A hipotenusa vai medir {:.2f}'.format(hip))