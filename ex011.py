#Faça um programa que leia a largura e a altura de uma parede em metros calcula a sua area e a quantidade necessaria para pinta-la sabendo que cada litro de tinta pinta uma área de 2m2
##Não entendi muito bem fazer junto
largura = float(input("Digite a largura da parede: "))
altura = float(input("DIgite o valor da altura da parede: "))
mla = altura * largura
print("Sua parede tem a dimensão de {}x{} e sua área é de {}".format(largura, altura, mla))
litros = mla /2
print("Para pintar essa parede, voce precisará de {}l de tinta".format(litros))