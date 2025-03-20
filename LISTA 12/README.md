# LISTA 12 - BANCO DE DADOS COM PYTHON

### A. Conexão com Banco de Dados MySQL
Crie um programa em Python que se conecte ao banco de dados MySQL utilizando a biblioteca mysql-connector-python e exiba a versão do MySQL.

### B. Criação de Tabela Simples
Crie um script em Python que se conecte ao MySQL e crie uma tabela chamada clientes com as colunas id, nome, email e telefone.

### C. Inserção de Dados em uma Tabela
Crie um programa que insira dados de clientes em uma tabela clientes, com os seguintes valores: nome, email e telefone. Use um loop para inserir múltiplos registros.

### D. Leitura de Dados da Tabela
Crie um programa que se conecte ao MySQL e leia todos os registros da tabela clientes, exibindo o nome e email de cada cliente.

### E. Atualização de Dados em uma Tabela
Crie um programa que atualize o telefone de um cliente específico na tabela clientes, baseando-se no id do cliente.


### F. Deleção de Dados
Crie um programa que remova um cliente da tabela clientes, dado o id do cliente. Certifique-se de que o cliente foi removido corretamente.

### G. Consulta com Condição
Crie um programa que faça uma consulta na tabela clientes e retorne apenas os clientes que possuem o nome começando com a letra "A".

### H. Consultas com Junção (JOIN)
Crie um banco de dados de duas tabelas: clientes e pedidos. A tabela pedidos deve ter as colunas id_cliente, produto, e quantidade. Crie uma consulta para retornar todos os pedidos de um cliente, juntando as tabelas clientes e pedidos pelo id_cliente.

### I. Uso de Transações
Crie um programa que faça uma transação para adicionar um novo cliente e, em seguida, adicionar um pedido para esse cliente. Caso a inserção do pedido falhe, a transação deve ser revertida.

### J. Uso de LIMIT e OFFSET
Crie um programa que faça uma consulta na tabela clientes e retorne apenas os primeiros 5 registros usando LIMIT e, em seguida, os próximos 5 registros usando OFFSET.


### K. Consultas Complexas com Subconsultas
Crie uma consulta que retorne todos os clientes que realizaram pedidos com uma quantidade superior a 10 unidades. Utilize uma subconsulta para filtrar os pedidos.

### L. Índices para Performance
Crie um índice na tabela clientes para a coluna email e explique como ele pode melhorar a performance das consultas que filtram por email.

### M. Relacionamento entre Tabelas com Chaves Estrangeiras
Crie duas tabelas, clientes e enderecos, sendo que a tabela enderecos possui uma chave estrangeira que se relaciona com a tabela clientes. Implemente o relacionamento e insira dados para testar.

### N. Backup e Restauração de Banco de Dados
Crie um script Python que faça o backup da base de dados loja e, em seguida, restaure esse banco de dados em um novo banco com o nome loja_backup.

### O. Normalização de Banco de Dados
Crie um banco de dados para uma loja online, com as tabelas clientes, produtos, pedidos e itens_pedido. Implemente o modelo de dados normalizado, garantindo que as tabelas estejam de acordo com as formas normais de normalização (1NF, 2NF, 3NF).