# ## T. Escreva um algoritmo que leia 30 matrículas e notas dos alunos,
# armazene-as em arrays matrículas e notas, onde a nota da matrícula correspondente
# fique no mesmo índice. Ordene os arrays pela matrícula e mostre a
# matrícula e nota de todos os alunos. obs.: considere a matrícula como um número inteiro.
matriculas = []
notas = []

# Leitura das matrículas e notas
for i in range(30):
    matricula = int(input(f"Digite a matrícula do aluno {i + 1}: "))
    nota = int(input(f"Digite a nota do aluno {i + 1}: "))

    # Adicionando diretamente na lista de matrículas e notas
    matriculas.append(matricula)
    notas.append(nota)

# Ordenando as listas pela matrícula
dados = list(zip(matriculas, notas))
dados.sort(key=lambda x: x[0])  # Ordena pela matrícula

# Exibindo as matrículas e notas ordenadas
print("\nMatrículas e Notas dos Alunos:")
for matricula, nota in dados:
    print(f"Matrícula: {matricula}, Nota: {nota}")