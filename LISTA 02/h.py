#Criar um algoritmo que leia vários números e imprima o fatorial de cada número digitado.
# O algoritmo se encerra quando -1 for digitado.
fat =1
while(True):
    num = int(input("Digite um numero: "))
    for i in range(1,num+1):
        fat *=i
    print(f"Fatorial de [{num}] é : [{fat}]")
    if num == -1:
        break
