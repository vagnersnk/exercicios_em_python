# Escreva um algoritmo que leia 50 números
# e diga quantos elementos não repetidos (diferentes) existem.
# Exemplo: array {4, 6, 4, 3, 8, 6, 2, 9, 8, 0, 1, 2} existem 8 elementos diferentes: {4, 6, 3, 8, 2, 9, 0, 1}
dados =[int(input(f"digite o valor [{x}]: ")) for x in range(5)]
diff =[]
for i in dados:
    if dados.count(i)==1:
        diff.append(i)
print(f"Diferentes: ",diff)
