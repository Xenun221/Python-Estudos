#Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e quantos dolar ela pd comprar
dinCarteira = float(input("Quanto dinheiro vc tem na sua carteira: "))
dolar = 5.53
compraDolar =  dinCarteira / dolar
print("Voce tem {} reais e convertenado em dolar vc tem {:.2f}".format(dinCarteira, compraDolar))

