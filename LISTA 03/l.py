# Escreva um algoritmo que leia dois arrays de 10 elementos cada
# e calcule um terceiro array onde cada índice contém a
# multiplicação dos elementos dos dois primeiros arrays nos índices correspondentes.
a1= [int(input(f"insira o intem [{i}] do array[1]: ")) for i in range(5)]
a2= [int(input(f"insira o intem [{i}] do array[2]: ")) for i in range(5)]
a3 = [x*y for x,y in zip(a1,a2)]
print("Terceiro Array",a3)