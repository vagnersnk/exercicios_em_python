# Escreva um programa que leia 20 números e diga quantos são pares e quantos são ímpares.
import ler

exibir =ler.ler_dados(5)
par =0
impar = 0
for i in range(0,5):

    if exibir[i] % 2 ==0:
        par +=1
    else:
        impar +=1
print(f"Pares [{par}] . Impares [{impar}]")