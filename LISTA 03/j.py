# Escreva um algoritmo que leia 5 números,
# armazenando-os em um array A1
# e calcule um segundo array A2,
# onde cada índice de A2 é o quadrado do valor do índice correspondente em A1.
# Ao final imprima cada valor com o seu quadrado.
import ler

a1= ler.ler_dados(5)
a2 =[i**2 for i in a1]
print("A2:",a2)