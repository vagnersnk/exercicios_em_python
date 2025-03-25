# Escreva um programa que leia 10 números e mostre-os na ordem inversa a que foram lidos.
import ler

exibir =ler.ler_dados(5)
# MÉTODO COM REVERSE
#exibir.reverse()
#print(exibir)
# MÉTODO COM FOR
for i in range(4,-1,-1):
    print(exibir[i])