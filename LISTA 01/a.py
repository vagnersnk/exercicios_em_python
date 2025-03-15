# Faça um algoritmo para calcular o volume de uma esfera de raio R,
# em que R é um dados fornecido pelo usuário. O volume da esfera é calculado por .
#V = (4/3) * π * r^3
import math
r = int(input("Digite o raio da esfera: "))
volume =(4/3)* math.pi*(r**3)
print(f"volme da esfera é : {round(volume,2)}")
