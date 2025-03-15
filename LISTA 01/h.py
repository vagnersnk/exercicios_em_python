#Prepare um algoritmo capaz de inverter um número de 3 dígitos
# fornecido pelo usuário. A inversão consiste em apresentar primeiro a
# unidade, seguida da dezena e por último a centena.
valor= int(input("Insira o valor: "))
u = (valor //1) % 10
d = (valor //10) % 10
c= (valor //100) % 10
print(f"unidade: {u}, dezena: {d} e centena {c}")