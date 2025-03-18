# Crie um algoritmo que mostre a soma dos cem primeiros números primos.
# Resolução do chatgpt
def eh_primo(n):

    if n < 2:
        return False
    for i in range(2, n):  # Testamos de 2 até n-1
        if n % i == 0:
            return False
    return True


soma_primos = 0
contador = 0
num = 2

while contador < 100:
    if eh_primo(num):
        soma_primos += num
        contador += 1
    num += 1

