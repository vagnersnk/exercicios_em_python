#  Elabore um algoritmo que, informada a idade de um nadador, classifique-o em uma das seguintes categorias
#  Idade Categoria
#  5 até 7 anos Infantil A
#  8 até 10 anos Infantil B
#  11 até 13 anos Juvenil A
#  14 até 17 anos Juvenil B
#  Maiores de 18 anos Adulto

idade = int(input("Insira a idade do nadador: "))
if idade >= 5 and idade <=7:
    print("Infantil A")
elif idade >8 and idade<=10:
    print("Infantil B")
elif idade >=11 and idade <=13:
    print("Juvenil A")
elif idade >=14 and idade <=17:
    print("Juvenil B")
elif idade >=18:
    print("Aldulto")
else:
    print("Idade invalida")