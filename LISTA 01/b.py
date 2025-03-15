#Construa um algoritmo que, tendo como dados de entrada dois pontos quaisquer
# do plano, 1
# imprima a distância entre eles.
import math
pontos=[] # lista que vai refere aos quatros pontos
for i in range(0,4):
    x = int(input(f"Digite o ponto: {i} \n"))
    pontos.append(x)
pwd = math.pow(pontos[0]-pontos[1],2)+math.pow(pontos[2]-pontos[3],2)
distancia= math.sqrt(pwd)
print(f"A distancia entre os pontos foi : {distancia}")
