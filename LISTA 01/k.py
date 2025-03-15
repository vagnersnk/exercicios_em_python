#Escreva um algoritmo que receba os lados de
# quadrilátero e diga se ele é um quadrado ou não.
lado1 = int(input("Digite o lado 1: "))
lado2 = int(input("Digite o lado 2: "))
lado3 = int(input("Digite o lado 3: "))
lado4 = int(input("Digite o lado 4: "))
if lado1 == lado2 == lado3 ==lado4:
    print("é um quadrado")
else:
    print("não é um quadrado")