#Escreva um algoritmo para ler um número e determinar se ele é maior, igual ou menor que zero.
num = int(input("Digite o numero: "))
if num > 0:
    print("Maior que zero")
elif num == 0:
    print("Igual a zero")
else:
    print("Menor que zero")