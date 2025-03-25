# Escreva um algoritmo que leia 20 números, armazenando-os em um array e troque de lugar
# o primeiro com o último, o segundo com o penúltimo,
# etc... Ao final, mostre o array resultante.
import ler

exibir =ler.ler_dados(5)
print("Antes da troca",exibir)
for i in range(5//2):
    print(f"debug i[{i}]")
    exibir[i], exibir[5-i-1] = exibir[5-i-1], exibir[i]

print("Depois de troca",exibir)