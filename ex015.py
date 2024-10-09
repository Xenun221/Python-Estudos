diasAlugado = int(input("Quantos dias alugados? "))
kmRodado = float(input("Quantos Km rodados? "))
totalPagar = (kmRodado * 0.15) + (diasAlugado * 60)
print("Valor total a pagar e de {}".format(totalPagar))