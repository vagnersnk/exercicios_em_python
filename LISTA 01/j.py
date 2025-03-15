#Desenvolva um algoritmo que leia duas notas e calcule a nota final do aluno.
# Considere a média ponderada, onde a primeira nota tem peso 2 e a segunda nota tem peso 3.
nota1= int(input("Digite a nota1: "))
nota2= int(input("Digite a nota2: "))
media =(nota1*2+nota2*3)/5
print(f"Sua media foi {media}")