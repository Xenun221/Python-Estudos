#Formas de replicar informações
nome = input("Qual e seu nome? ")
#Escreveu o nome em 20 espaços >Direita <Esquerda ^Centralizado =20Espaços colocando igual em volta
print("Prazer te conhecer {:20} !".format(nome))


n1 = int(input("Digite um numero: "))
n2 = int(input("Digite o segundo numero: "))
s = n1 + n2
m = n1 * n2
d = n1 /n2
r = n1  % n2
sub = n1 - n2
di = n1 // n2
e = n1 ** n2
print("A soma é {}, \n a Subtração é {}, a Divisão é {:.2f}, a Multiplicação é {}".format(s,sub, d, m), end='>>>')
print("Divisao inteiro {}, e potencia é {}".format(di, e))