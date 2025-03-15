#Escreva um algoritmo para calcular e exibir o
# comprimento de uma circunferência, sendo dada o valor de seu raio.
# raio= 2πr
import math
r= int(input("Digite o raio: "))
comprimento = 2*math.pi*r
print(f"O comprimento foi: {comprimento:.2f}")
