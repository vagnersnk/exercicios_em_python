# Crie um algoritmo que leia nomes de pessoas enquanto for diferente do seu próprio nome.
nome = (input("digite seu nome: "))
while(True):
    comp= input("Digite o nome: ")
    if nome == comp:
        print("Nome equivalente")
        break