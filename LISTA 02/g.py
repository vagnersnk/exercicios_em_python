#Crie um algoritmo que leia o sexo de cada pessoa e ao final,
# imprima quantas pessoas são do sexo masculino e feminino.
# Imprima também o percentual de pessoas do sexo masculino e feminino.
# A condição de parada será o número “0” – zero)
m=0
f=0
t=0
while(True):
 sexo = input("Digite o sexo [M] para masculino[F] para feminino: ")
 t+=1
 if sexo=="M":
     m +=1
 elif sexo =="F":
     f +=1
 elif int(sexo) == 0:
     t-=1
     print(f"Terminou  MASCULINO {(m/t)*100}%")
     print(f"Terminou  FEMININO  {(f/t) * 100}%")
     break