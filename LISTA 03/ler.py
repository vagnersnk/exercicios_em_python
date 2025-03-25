lista=[]
def ler_dados(quant):
    for i in range(0,quant):
        numero = int(input(f"Digite o valor [{i}]: "))
        lista.append(numero)
    return lista

