# Escreva um algoritmo que leia um array de 20 elementos
# e mostre a maior diferença entre dois elementos consecutivos desse array e em que índice eles estão.

a1= [int(input(f"insira o intem [{i+1}] do array[1]: ")) for i in range(5)]

maior = 0
indice = 0

for i in range(4):
    diff = abs(a1[i] - a1[i + 1])
    if diff > maior:
        maior = diff
        indice = i

print(f"A maior diferença é {maior} e ocorre entre os elementos nos índices {indice} e {indice + 1}.")
