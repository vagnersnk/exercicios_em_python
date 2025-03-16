#Escreva um algoritmo que leia dois valores monetários em reais e centavos e calcule
# a soma entre eles. Note que o valor somado do centavos não pode ser maior ou igual a 100
valor1= float(input("Digite a valor 1 : "))
valor2= float(input("Digite a valor 2 : "))
real1,centavo1 = divmod(valor1,1)
real2,centavo2 = divmod(valor2,1)
real1 = int(real1)
centavo1= int(centavo1*100)
real2 = int(real2)
centavo2= int(centavo2*100)
soma_real= real1+real2
soma_centavo=centavo1+centavo2
if soma_centavo >=100:
    soma_real += soma_centavo //100
    soma_centavo = soma_centavo %100
print(f"A soma foi {soma_real},{soma_centavo}")

