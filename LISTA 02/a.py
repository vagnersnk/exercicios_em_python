#Faça um algoritmo que some os n primeiros números, a partir de 1.
n= int(input("Digite o  numero final: "))
soma =0
for i in range(1,n+1):
    soma+=i

print(f"Soma : {soma}")
