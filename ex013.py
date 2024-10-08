#Faça um salario de um funcionario so que agora com 15% de aumento
salario = float(input("Digite seu salario: "))
salarioAumento = (salario *15)/100
valorSalario = salario + salarioAumento
print("O valor do seu salario é {} com o aumento de 15% fica {:.2f}".format(salario, valorSalario))