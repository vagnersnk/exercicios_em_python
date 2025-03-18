#Crie um algoritmo que receba vários números,
# enquanto forem positivos,
# e ao final imprima a média dos números digitados.
media =0
count = 0
while(True):
    num = int(input("digite um numero: "))
    if num >0:
        media += num
        count +=1
    else:
        print(f"Terminou e a media foi : {media/count}")
        break