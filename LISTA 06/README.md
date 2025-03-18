LISTA 06 - FUNCÕES E CLASSES
### A. Implemente uma função que recebe por parâmetro o raio de uma esfera e retorna o seu volume. A fórmula para o volume de uma esfera é:  
\[ \text{Volume} = \frac{4}{3} \times \pi \times \text{raio}^3 \]

### B. Implemente uma função que recebe por parâmetro o tempo de duração de uma maratona, expressa em horas, minutos e segundos, e retorna esse tempo apenas em segundos.  
Exemplo: 1 hora, 2 minutos e 32 segundos equivalem a 3752 segundos.

### C. Faça um programa para receber um número inteiro do usuário. Em seguida, verifique se ele é:
- Par
- Divisível por 3
- Divisível por 5  
Crie uma função separada para cada item acima. Cada função deve receber o número a ser verificado como argumento e devolver ‘1’ para verdadeiro e ‘0’ para falso.

### D. Implemente uma função que recebe a média final de um aluno como parâmetro e retorna o caractere equivalente ao seu conceito, conforme abaixo:
- 0,0 a 4,9 = Conceito 'D'
- 5,0 a 6,9 = Conceito 'C'
- 7,0 a 8,9 = Conceito 'B'
- 9,0 a 10,0 = Conceito 'A'

### E. Implemente uma função que recebe como parâmetro 50 valores inteiros armazenados em uma lista e retorna o maior valor dentre eles.

### F. Implemente uma função `eqvalue(vetor, n)` que recebe um número inteiro `n` e retorna o número de vezes que `n` aparece no vetor `vetor`, que possui 10 elementos.

### G. Implemente uma função para retornar as seguintes informações. Todas elas devem receber como entrada uma lista de 20 elementos do tipo `Produto`, com as informações já preenchidas (não devem ser lidas):
- Imprimir o título do produto mais caro.
- Imprimir o título dos 10 produtos mais vendidos.
- Retornar a quantidade de vendas do produto mais barato.

```python
class Produto:
    def __init__(self, titulo, quantidade_vendida, preco):
        self.titulo = titulo
        self.quantidade_vendida = quantidade_vendida
        self.preco = preco
H. Implemente funções para cada uma das pesquisas abaixo:
Dado um título, imprima suas informações (o título também é um parâmetro da função).
Dado um preço P, imprima o título dos produtos cujo preço é maior que P (o preço também é um parâmetro da função).
Retorne a média das quantidades vendidas por todos os produtos.
I. Construa um programa que leia o resultado da loteria esportiva com 13 jogos. O resultado em cada jogo pode ser "time 1", "empate", ou "time 2". Em seguida, leia o nome e o palpite de 30 apostadores na loteria. Ao final, informe:
O nome e número de acertos de cada apostador.
O(s) nome(s) do(s) apostador(es) com maior quantidade de acertos.
A quantidade média de acertos. O programa deverá ter no mínimo 4 funções: ler dados, e outras 3 equivalentes a cada requisito descrito acima.
J. Implemente uma função que determine se um número é ímpar (retorno 1) ou par (retorno 2). Para isso, não use o operador de resto, mas sim subtrações sucessivas.

