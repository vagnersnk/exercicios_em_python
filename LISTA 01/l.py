#Desenvolva um algoritmo que leia um valor de hora
# (uma variável para a hora e outra para minuto) e
# informe quantos minutos se passaram desde o início do dia.

horas = int(input("Digite as horas: "))
minutos = int(input("Digites os minutos: "))
final = (horas*60)+minutos
print(f"{final:.1f}")