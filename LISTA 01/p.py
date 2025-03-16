#Escreva um algoritmo que leia dois números e exiba-os em ordem crescente.
num1 = int(input("Digite no numero1: "))
num2 = int(input("Digite no numero2: "))
if num1>num2:
    print(f"{num1} | {num2}")
else:
    print(f"{num2} | {num1}")