#Faça um algoritmo que mostre seu preço e faça o novo preço com 5% de desconto
preco = float(input("Digite o valor do produto: "))
desconto = (preco * 5)/100
precoDesconto = preco - desconto
print("O produto é {} com 5% de desconto fica {:.2f} e o preço total fica {:.2f}".format(preco, desconto, precoDesconto))