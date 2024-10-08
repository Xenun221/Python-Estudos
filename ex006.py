#Crie um algoritmo que leia um numero e mostre seu dobri triplo e raiz quadrada
num = float(input("Digite um numero: "))
dobro = num * 2
triplo = num * 3
raiz = num **(1/2) #pow(num,(1/2))
print("Seu numero é: {}".format(num))
print("O dobro do seu numero é {}".format(dobro))
print("O triplo do seu numero é {}".format(triplo))
print("A raiz quadrada do seu numero é {:.2f}".format(raiz))

