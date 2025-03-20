# LISTA 13 - TESTES E QUALIDADE DE CÓDIGO

### A. Teste Unitário Simples com unittest
Crie uma função que retorna o quadrado de um número. Em seguida, escreva um teste unitário utilizando o módulo unittest para verificar se o valor retornado é o esperado.

### B. Teste de Exceção com unittest
Crie uma função que recebe um número e retorna o seu inverso. Se o número for zero, deve levantar uma exceção ZeroDivisionError. Escreva um teste unitário para verificar se a exceção é levantada corretamente.

### C. Teste de Funções com assert
Crie uma função que recebe uma lista de números e retorna o maior número da lista. Teste essa função com a palavra-chave assert para garantir que o valor retornado esteja correto.

### D. Teste de Valor de Retorno com unittest
Escreva uma função que recebe dois números e retorna o resultado de sua soma. Em seguida, crie um teste unitário para verificar se a soma está correta.

### E. Teste de Função de String com unittest
Implemente uma função que recebe uma string e retorna ela invertida. Escreva um teste unitário para garantir que a função está funcionando corretamente.


### F. Teste de Função com Dependências Externas
Crie uma função que utiliza uma API externa (exemplo: obtendo dados do clima de uma API). Escreva um teste unitário utilizando o unittest.mock para simular a resposta da API sem realmente chamar a API.

### G. Teste de Funcionalidade com pytest
Crie uma função que verifica se um número é primo. Escreva uma suíte de testes utilizando o pytest para testar vários números e verificar se a função retorna os resultados corretos.

### H. Teste de Função Assíncrona com pytest
Implemente uma função assíncrona que faz uma requisição HTTP para obter informações de um site. Em seguida, escreva um teste assíncrono utilizando o pytest para verificar o comportamento da função.

### I. Teste de Condições de Fronteira
Crie uma função que retorna a média de uma lista de números. Escreva testes para verificar o comportamento da função em condições de fronteira, como listas vazias, listas de um único número e listas de números negativos.

### J. Teste de Cobertura de Código com pytest-cov
Crie um programa que contém funções simples, como soma, subtração e multiplicação. Escreva testes unitários para essas funções e depois utilize o plugin pytest-cov para verificar a cobertura de código dos testes.


### K. Teste de Integração com Banco de Dados
Crie um programa que interage com um banco de dados (por exemplo, MySQL). Escreva um teste de integração para garantir que os dados podem ser corretamente inseridos e lidos do banco de dados.

### L. Teste de Sistema Completo com pytest
Implemente um sistema simples, como um gerenciador de tarefas. Escreva testes de sistema com o pytest para garantir que os fluxos principais do sistema (criação, atualização e exclusão de tarefas) funcionem corretamente.

### M. Teste de Performance com pytest-benchmark
Implemente uma função que realiza uma operação de ordenação (como o quicksort). Utilize o plugin pytest-benchmark para medir o desempenho da função em diferentes tamanhos de entrada e verificar se o desempenho é aceitável.

### N. Teste de Conformidade com Padrões de Codificação (PEP 8)
Escreva um script Python que tenha várias funções. Utilize uma ferramenta como o flake8 ou pylint para verificar se o código segue os padrões de codificação PEP 8 e corrija os problemas encontrados.

### O. Teste de Resiliência com tox
Implemente um projeto simples e configure o tox para testar o código em múltiplas versões do Python. Escreva e execute testes para garantir que o código funciona em todas as versões suportadas.