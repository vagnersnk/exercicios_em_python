# Faça um algoritmo para calcular o MMC de dois números.
# (MMC é o menor múltiplo comum entre os dois números.
# Note que um dos dois números já pode ser o MMC)

def calcular_mmc(n1, n2):
    def mdc(a, b):
        while b:
            a, b = b, a % b
        return a

    return (n1 * n2) // mdc(n1, n2)


num1 = int(input("Insira o primeiro número: "))
num2 = int(input("Insira o segundo número: "))


resultado = calcular_mmc(num1, num2)
print(f"O MMC de {num1} e {num2} é {resultado}")
#corrigido pelo chatgpt