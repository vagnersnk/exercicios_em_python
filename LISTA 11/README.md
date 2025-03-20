# LISTA 11 - PROGRAMAÇÃO FUNCIONAL

### A. Funções Lambda Simples
Crie uma função lambda que receba um número e retorne seu quadrado. Depois, aplique essa função a uma lista de números de 1 a 10 utilizando map().

### B. Função filter() para Filtrar Elementos
Crie uma lista de números de 1 a 20 e use filter() para filtrar apenas os números múltiplos de 3.

### C. Uso de reduce() para Acumulação de Resultados
Utilize a função reduce() para somar todos os números de uma lista de 1 a 5. Lembre-se de importar reduce de functools.

### D. Função map() com Strings
Crie uma lista de palavras e utilize map() para converter todas as palavras para maiúsculas.

### E. Compreensão de Listas com Funções
Crie uma lista de números e use list comprehension para criar uma nova lista contendo apenas os números pares.


### F. Funções de Alta Ordem
Crie uma função operacao() que recebe uma função como argumento. Essa função deve aplicar a operação recebida a dois números e retornar o resultado.

### G. Currying em Funções
Implemente uma função multiplicacao() que recebe um número x e retorna uma função que multiplica seu argumento por x. Utilize essa função para criar multiplicadores de 2 e 3.

### H. Uso de zip() para Manipulação Funcional
Dadas duas listas, uma com nomes e outra com idades, utilize map() e zip() para criar uma lista de tuplas contendo o nome e a idade de cada pessoa.

### I. Função Recursiva
Crie uma função recursiva que calcule o fatorial de um número.

### J. Aplicação de Funções em Sequência
Crie uma sequência de funções (por exemplo, uma função que dobra um número, seguida por uma que adiciona 10) e utilize reduce() para aplicar essas funções a uma lista de números.


### K. Uso de functools.partial para Currying Avançado
Crie uma função somar() que recebe dois números. Use functools.partial para criar uma versão dessa função que sempre adiciona 10 ao primeiro número.

### L. Funções Imutáveis com namedtuple
Crie uma classe imutável Pessoa usando namedtuple e defina uma função que compare duas instâncias dessa classe para verificar se elas são iguais.

### M. Aplicação de Funções em Dicionários com map()
Crie um dicionário de preços de produtos e use map() para aplicar um desconto de 10% a todos os preços, retornando um novo dicionário.

### N. Funções como Argumentos de Outras Funções
Crie uma função operar() que recebe uma função e dois números como argumentos. Essa função deve aplicar a operação à lista de números fornecida.

### O. Imutabilidade e Funções em Python
Implemente uma função que utilize um set para garantir que elementos duplicados sejam removidos de uma lista, sem alterar a lista original.