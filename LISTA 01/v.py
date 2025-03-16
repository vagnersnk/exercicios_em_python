#Tendo como dados de entrada a altura e o sexo de uma pessoa,
# construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas:
#Para homens: (72.7 * h) – 58
#Para mulheres (62.1 * h) – 44.7
h = float(input("Digite sua altura:"))
imc1 = (72.7*h)-58
imc2 = (62.1*h)-44.7
print(f"Imc ideal para M {imc1:.2f} | para F {imc2:.2f}")