#Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações sobre ela
tipo = input("Digite algo: ")
print("Seu tipo primitivo desse valor é: ", type(tipo))
print("Esta em maiuculas? ", tipo.isupper())
print("E alfabetico? ", tipo.isalpha())
print("Esta capitalizada? ", tipo.capitalize())
print("Esta em minusculas? ", tipo.islower())
print("E um nuemro? ", tipo.isnumeric())
print("So tem espaços? ", tipo.isspace())
print("É Alfanumerico ", tipo.isalnum())