#Elabore um algoritmo que leia quatro valores inteiros exiba a média aritmética entre eles.
# O algoritmo também deve exibir os números menores e maiores do que a média.
qtd = 4
def ler_valor(tam):
    lista = []
    for i in range(0, tam):
        num = int(input(f"digite o valor [{i + 1}]: "))
        lista.append(num)
    return lista

ordem =ler_valor(qtd)
media= (sum(ordem)/qtd)

print(f"a media foi {media}")
for i in ordem:
    if i > media:
        print(f"Valor acima da media: {i}")
    elif i == media:
        print("valor igual a media")
    else:
        print(f"Valor abaixo da media: {i}")