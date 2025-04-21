# Leia 10 nomes e apresente-os em ordem alfabética crescente
nomes=[]
for i in range(0,3):
   nome = input(f"digite o nome {i+1}: ").strip()
   nomes.append(nome)
print(sorted(nomes))

