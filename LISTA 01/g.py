#Escreva um algoritmo que leia duas variáveis inteiras e troque o conteúdo entre elas.
a = int(input("Digite o valor 1: "))
b = int(input("Digite o valor 2: "))
a= a-b
b= a+b
a= b-a
print(F"Valor1: {a}, Valor2: {b}")