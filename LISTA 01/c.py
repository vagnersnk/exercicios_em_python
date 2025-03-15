#Escreva um algoritmo para calcular e exibir a média ponderada
# de 2 notas dadas (nota1 = peso 6 e nota2 = peso 4).
# media = ((x*6)+(x*4))/6+4
nota1= int(input("digite a primeira nota: "))
nota2= int(input("digite a segunda nota: "))
media = ((nota1*6)+(nota2*4))/10
print(f"A média foi: {media}")