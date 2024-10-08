#Escreva um programa que leia um valor em metros e exiba convertido em centimetros e milimetros
metro = float(input("Digite o valor em metro: "))
centimetro = metro * 100
milimetro = metro * 1000
decametro = metro  *10
km = metro / 1000
hm = metro /100
dam = metro /10
print("O valor de {} Metros em Km fica {}".format(metro, km))
print("O valor de {} Metro em hm fica {}".format(metro, hm))
print("O valor de {} Metros em dm fica {}".format(metro, dam))
print("O valor de {} Metro em dm fica {}".format(metro, decametro))
print("O valor de {} Metro convertido em Centimetros fica {}cm".format(metro, centimetro))
print("O valor de {} Metro convertido em Milimetros fica {}mm".format(metro, milimetro))