# LISTA 8 - EXCEÇÕES E TRATAMENTO DE ERROS

### A. Tratamento de Divisão por Zero
Crie um programa que solicite dois números ao usuário e realize a divisão entre eles. O programa deve tratar a exceção no caso de uma divisão por zero e exibir uma mensagem apropriada.

### B. Validação de Entrada de Dados
Peça ao usuário um número inteiro. Caso o usuário digite algo inválido, exiba uma mensagem de erro e peça o número novamente.

### C. Manipulação de Arquivos com Tratamento de Erros
Faça um programa que tente abrir um arquivo chamado dados.txt. Se o arquivo não existir, exiba uma mensagem de erro e crie um novo arquivo com esse nome.

### D. Lidando com Múltiplas Exceções
Crie um programa que peça ao usuário dois números e realize a divisão. O programa deve tratar os seguintes erros:

- Divisão por zero.
- Entrada de um valor não numérico.
- Outros erros inesperados.
### E. Capturando e Registrando Exceções em um Log
Crie um programa que tente ler um arquivo especificado pelo usuário. Se ocorrer um erro, registre a exceção em um arquivo erros.log com a data e a descrição do erro.


### F. Repetir uma Função até Entrada Válida
Crie uma função que solicita ao usuário um número e só retorna quando um valor válido for inserido. A função deve lidar com erros de tipo e continuar pedindo até que a entrada seja correta.

### G. Criando e Lançando Exceções Personalizadas
Crie uma classe de exceção personalizada chamada ErroIdadeInvalida. Em seguida, crie uma função que recebe uma idade e lança essa exceção se a idade for negativa ou maior que 120.

### H. Manipulação de JSON com Tratamento de Erros
Escreva um programa que tente abrir um arquivo dados.json e carregá-lo. O programa deve tratar:

- Arquivo inexistente.
- Erros de formatação JSON.
- Outros erros inesperados.
### I. Gerenciador de Contexto Personalizado
Crie uma classe que funcione como um gerenciador de contexto para manipular arquivos de maneira segura. A classe deve garantir que o arquivo seja fechado corretamente, mesmo se ocorrer um erro durante a leitura ou escrita.

### J. Tratamento de Exceções em Threads
Crie um programa que execute múltiplas threads, onde cada thread realiza operações matemáticas diferentes. Use try-except para capturar e tratar erros individualmente em cada thread.

