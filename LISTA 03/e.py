# Escreva um programa que leia notas de 30 alunos,
# depois mostre a média da turma,
# quantos alunos estão acima da média e
# liste todas as notas dos alunos acima da média.
import ler
qtd = 5
exibir =ler.ler_dados(qtd)

media = sum(exibir)/qtd
for i in range(0,qtd):
    if exibir[i] > media:
        print(f"Nota: [{exibir[i]}] maior que a media [{media}]")
