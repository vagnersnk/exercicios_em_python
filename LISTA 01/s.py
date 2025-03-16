#Elabore um algoritmo que leia três valores inteiros e calcule a soma do menor valor com o maior.
lista =[]
for i in range(0,3):
    num = int(input(f"digite o valor [{i+1}]: "))
    lista.append(num)
lista.sort()
soma = lista[0]+lista[2]
print("A seguir temos os valores digitados e posteriomente a soma do maior com menor")
print(lista)
print(soma)