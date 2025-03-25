# Escreva um algoritmo que leia 10 números, armazenando-os
# em um array e troque de lugar o maior elemento com o último elemento,
# mostrando em que índice estava o maior elemento e qual é esse elemento
# e mostrando o valor que estava no último índice.
import ler

exibir =ler.ler_dados(5)
local =0
local2 = 0
maior = exibir[0]
menor = exibir[0]

for i in range(0,5):
        if exibir[i] > maior:
            maior = exibir[i]
            local =i
        if exibir[i]< menor:
            menor = exibir[i]
            local2 = i

#print(f"maior valor foi: [{maior}] estando no indice :  [{local}]")
#print(f"menor valor foi: [{menor}] estando no indice :  [{local2}]")
exibir[local2] = maior
exibir[local] = menor
print(exibir)