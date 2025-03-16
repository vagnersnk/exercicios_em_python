#Sabe-se que para iluminar 1 metro quadro de um ambiente
# ão necessários 18W de potência. Desenvolva um algoritmo que
# leia a largura e a profundidade de uma sala e informa a potência da lâmpada que deve ser usada.
largura = int(input("Digite a largura: "))
fundura = int(input("Digite a profundidade: "))
area = (largura*fundura)*18
print(f"A potencia da lampada é de : {area} W")