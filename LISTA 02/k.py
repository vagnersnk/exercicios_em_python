# Faça um algoritmo que represente a expressão matemática abaixo: i=5n(2i2+5i+1)

n = float(input("Digite o valor de n: "))
i = float(input("Digite o valor inicial de i: "))

i = 5 * n * (2 * (i ** 2) + 5 * i + 1)


print(f"O valor de i é: {i}")