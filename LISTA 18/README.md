# LISTA 18 - PARADIGMAS DE PROGRAMAÇÃO AVANÇADOS 

### A. Criando um Decorador Simples
Implemente um decorador simples em Python que registre a execução de uma função. O decorador deve exibir uma mensagem antes e depois da execução da função.

### B. Usando Geradores para Sequências
Implemente um gerador que retorna uma sequência de números Fibonacci. O gerador deve ser capaz de retornar a sequência sem armazenar todos os valores na memória de uma vez.

### C. Decorador para Medir Tempo de Execução
Crie um decorador que mede o tempo de execução de uma função. O decorador deve retornar o tempo que a função levou para ser executada e imprimir essa informação.

### D. Metaprogramação com type()
Crie uma classe dinamicamente utilizando o type() em Python. A classe deve ser criada em tempo de execução com base em parâmetros fornecidos pelo usuário.

### E. Geradores com Parâmetros
Implemente um gerador que aceita um parâmetro e retorna múltiplos números inteiros em uma sequência crescente. O gerador deve continuar de onde parou quando chamado novamente.


### F. Decorador para Cache de Resultados
Implemente um decorador de cache que armazena os resultados de uma função. Se a função for chamada com os mesmos parâmetros novamente, o resultado deve ser retornado diretamente do cache, sem precisar recalcular.

### G. Metaprogramação com exec() e eval()
Crie uma função que utiliza exec() e eval() para executar e avaliar código Python dinamicamente em tempo de execução. A função deve receber uma string com código Python e executá-lo.

### H. Geradores com yield e Estado
Implemente um gerador que mantenha o estado de sua execução entre as chamadas usando yield. O gerador deve retornar os valores de uma lista de maneira eficiente, sem carregar toda a lista na memória.

### I. Decorador para Verificação de Tipos
Crie um decorador que verifica os tipos de parâmetros passados para uma função. Se os tipos não forem os esperados, o decorador deve lançar uma exceção.

### J. Metaprogramação com __new__
Implemente um exemplo de metaprogramação usando __new__. O método __new__ deve ser utilizado para controlar a criação de novas instâncias de uma classe.


### K. Decoradores de Classe
Implemente um decorador de classe que modifica o comportamento de uma classe. O decorador deve adicionar um método extra à classe durante sua definição.

### L. Geradores e Concorrência com asyncio
Implemente um gerador assíncrono utilizando async def e await para simular uma tarefa que faz chamadas assíncronas, como buscar dados de uma API de maneira eficiente.

### M. Metaprogramação com __getattr__ e __setattr__
Implemente uma classe que utilize __getattr__ e __setattr__ para interceptar o acesso e a atribuição de atributos. A classe deve verificar se o atributo existe antes de permitir a atribuição ou o acesso.

### N. Decoradores com Argumentos
Crie um decorador com argumentos que recebe um parâmetro e aplica uma lógica personalizada à função decorada. Por exemplo, o decorador pode alterar o comportamento da função dependendo do argumento fornecido.

### O. Geradores para Busca em Arquivo Grande
Implemente um gerador que lê um arquivo grande linha por linha, de maneira eficiente. O gerador deve ser capaz de retornar as linhas de texto do arquivo sem carregar o arquivo inteiro na memória.

