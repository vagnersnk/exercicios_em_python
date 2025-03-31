# S. Escreva um algoritmo que leia 50 números, armazene-os na ordem em que foram lidos,
# ordene-os, e mostre-os ordenados.
###
import bisect
lista = []
for i in range(5):
    dados = int(input(f"Digite o número [{i}]: "))
    bisect.insort(lista, dados)
print(lista)