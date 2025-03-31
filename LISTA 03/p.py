# P. Escreva um algoritmo que leia dois arrays A1 e A2 de 30 elementos
# cada e crie um terceiro array A3 que contenha todos os elementos dos dois arrays (união).
# Considere que os elementos contidos em um array são diferentes, mas pode haver o mesmo elemento nos dois arrays. Por fim, imprima A3.
###
dados1 =[int(input(f"digite o valor [{x}]: ")) for x in range(5)]
print("Array 2")
dados2 =[int(input(f"digite o valor [{x}]: ")) for x in range(5)]
dados3 = zip(dados2,dados1)
print(list(dados3))