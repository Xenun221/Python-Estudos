"""
from math import hypot
cto = float(input("Comprimento do cateto oposto: "))
cta = float(input("Comprimento do cateto adjacente: "))
hipo = hypot(cto, cta)
print("A hipotenusa vai medir {:.2f}".format(hipo))
"""

cto = float(input("Comprimento do cateto oposto: "))
cta = float(input("Comprimento do cateto adjacente: "))
hi = (cto ** 2 + cta **2) ++ (1/2)
print("A hipotenusa vai medir{:.2f}".format(hi))