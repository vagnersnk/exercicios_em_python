# O. Escreva um algoritmo que leia dois arrays A1 e A2 de 30 elementos
# cada e crie um terceiro array A3
# que contenha os elementos que existam nos dois arrays (intersection). Por fim, imprima o array A3.
dados1 =[int(input(f"digite o valor [{x}]: ")) for x in range(5)]
print("Array 2")
dados2 =[int(input(f"digite o valor [{x}]: ")) for x in range(5)]
dados3= []
for i in dados1:
    for j in  dados2:
        if i == j:
            dados3.append(i)
print(f"dados3: ",dados3)