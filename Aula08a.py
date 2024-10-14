"""
import  math
num = int(input("Digite um numero: "))
#Importando um modulo
raiz = math.sqrt(num)
print("Raiz de {} é {}".format(num, math.ceil(raiz)))

#math.ceil(raiz), math.ciel
"""
"""
#Usando from import
import math
from math import  sqrt, floor
#Ja tras o metodo diretamento para a past
num = int(input("Digite um numero: "))
raiz = sqrt(num)
print("A riz de {} e {:.2f}".format(num, floor(raiz)))
"""

"""
#Importando o random
import random
num = random.randint(1,10)
print(num)
"""

import  emoji
print(emoji.emojize("Olá mundo :sunglasses:", use_aliases=True))