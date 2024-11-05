import math
angulo = float(input("Digite o ãngulo que você deseja: "))
rad = math.radians(angulo)
seno = math.sin(rad)
cos = math.cos(rad)
tan = math.tan(rad)
print("O Ângulo DE {} tem o SENO de {:.2f}".format(angulo, seno))
print("O Ângulo de {} tem o COSSENO de {:.2f}".format(angulo, cos))
print("O Ângulo de {} tem a TANGENTE DE {:.2f}".format(angulo, tan))