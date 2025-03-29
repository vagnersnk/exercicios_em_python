# Escreva um algoritmo que leia dois array A1 e A2 de 8 números
# e efetue a troca dos elementos desses arrays.
# Os elementos que estavam em A1 vão para A2 e vice-versa.

def ler_dados(n):
    return [int(input(f"Digite o valor [{i}]: ")) for i in range(n)]

print("Insira o primeiro array (8 números): ")
a1 = ler_dados(8)

print("Insira o segundo array (8 números): ")
a2 = ler_dados(8)


temp = a1[:]
a1[:] = a2
a2[:] = temp

print("\nApós a troca:")
print("a1:", a1)
print("a2:", a2)