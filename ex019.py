import random
p1 = str(input("Primeiro Aluno: "))
p2 = str(input("Segundo Aluno: "))
p3 = str(input("Terceiro Aluno: "))
p4 = str(input("Quarto Aluno: "))
lista = [p1,p2,p3,p4]
escolhido = random.choice(lista)
print("O aluno escolhido é {}".format(escolhido))