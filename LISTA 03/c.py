# Escreva um programa que leia 10 números e
# mostre-os na ordem em que foram lidos,
# dizendo para cada número se é par ou ímpar.

import ler

exibir =ler.ler_dados(5)
print("Exibindo a lista:",exibir)
for i in range(0,5):

    if exibir[i] % 2 ==0:
        print(f"O numero: {exibir[i]} é par ")
    else:
        print(f"O numero: {exibir[i]} é ímpar ")