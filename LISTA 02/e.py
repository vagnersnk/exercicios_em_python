#  Crie um algoritmo que lê números enquanto
#  forem positivos e ao final imprima quantos
#  números foram digitados e a soma dos mesmos.
soma = 0
while(True):
    num = int(input("digite um numero: "))
    if num >0:
        soma +=num
    else:
        print(f"Terminou e a soma foi : {soma}")
        break