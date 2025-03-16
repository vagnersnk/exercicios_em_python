#Escreva um algoritmo que leia três valores inteiros e e mostre-os em ordem decrescente.
lista =[]
for i in range(0,3):
    num = int(input(f"digite o valor [{i+1}]: "))
    lista.append(num)
lista.sort(reverse=True)
print(lista)