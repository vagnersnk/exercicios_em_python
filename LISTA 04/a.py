# Leia 3 notas de 3 alunos e imprima em ordem crescente as médias obtidas.
# matriz 3 por 3
matriz=[]
for i in range(0,3):
    linha = list(map(int, input(f"Digite 3 números para a linha {i + 1}, separados por espaço: ").split()))
    matriz.append(linha)
medias =[]
for linha in matriz:
    medias.append(sum(linha)/3)
print(f"Medias: ",sorted(medias))