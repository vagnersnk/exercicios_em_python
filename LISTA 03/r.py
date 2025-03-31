# R. Escreva um algoritmo que leia 5 números e no momento da leitura do número,
# o mesmo deverá ficar armazenado de forma crescente no array.
# Ao final, você terá os elementos ordenados e deverá mostrá-los.
#
import bisect
lista = []
for i in range(5):
    dados = int(input(f"Digite o número [{i}]: "))
    bisect.insort(lista, dados)
print(lista)