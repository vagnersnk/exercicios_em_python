# Pedro está a aprender a fazer mágica.
# Ele diz que é capaz de adivinhar qualquer número que alguém pensar.
# Para verificar se é verdade, crie um algoritmo que represente este truque.
# Ou seja, um número deverá ser lido e guardado em segredo.
# Em seguida, Pedro tentará acertar o número secreto,
# tendo tentativas ilimitadas enquanto os números não forem iguais (palpite e segredo).
import os
entrada= int(input("Digite um numero para se o segredo: "))
os.system("cls")

while(True):
    tent = int(input("Digite um numero: "))
    if tent == entrada:
        print("Acertou mizeravi!")
        break
    else:
        print("Errouuuu!")