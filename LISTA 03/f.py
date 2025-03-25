# Escreva um algoritmo que leia 10 números,
# armazenando-os em um array e mostre o
# maior número e em que índice se encontra.
import ler

exibir =ler.ler_dados(5)
local =0
maior = exibir[0]
for i in range(0,5):
        if exibir[i] > maior:
            maior = exibir[i]
            local =i

print(f"Indice de maior valor  [{local}]")