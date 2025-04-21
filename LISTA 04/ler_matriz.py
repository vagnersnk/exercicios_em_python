matriz=[]
def ler_matriz(a,b):
    """
    :param a: recebe o numero de linha
    :param b: recebe o numero de colunas: serve mais para visualização não é feito calcuclo com ele.
    :return: uma matriz com o tamanho de a.
    """
    for i in range(0,a):
        linha = list(map(int, input(f"Digite {b} números para a linha {i + 1}, separados por espaço: ").split()))
        matriz.append(linha)
    return matriz

