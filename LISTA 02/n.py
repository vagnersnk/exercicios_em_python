# Faça um algoritmo que liste todos os divisores de um número.
num= int(input("Digite um numero: "))
for i in range(2,num+1):
    if num%i ==0:
        print(i)