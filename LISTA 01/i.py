#Desenvolva um algoritmo que leia três valores (a, b e c) de uma equação do segundo grau
# do tipo ax2+bx+c = 0 e mostre as raízes dessa equação.
# delta= b²-4.a.c
# Raiz (-b +- sqrt(delta)/2a
import math

a= int(input("Digite o valor de a: "))
b= int(input("Digite o valor de b: "))
c= int(input("Digite o valor de c: "))
delta= b**2-4*a*c
if delta<0:
    print("Sem raizes reais")
else:
    raiz1= (-b+math.sqrt(delta))/(2*a)
    raiz2= (-b-math.sqrt(delta))/(2*a)
    print(f"A raizes da equação são {raiz1} e {raiz2}")
