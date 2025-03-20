# LISTA 9 - ORIENTAÇÃO A OBJETOS AVANÇADA

### A. Classe Base e Instâncias
Crie uma classe Veiculo com os atributos marca, modelo e ano. Instancie um objeto dessa classe e exiba seus atributos.

### B. Métodos e Encapsulamento
Modifique a classe Veiculo para incluir um método exibir_dados() que imprime as informações do veículo. Torne os atributos marca, modelo e ano privados e crie métodos getters e setters.

### C. Classe com Método Estático
Crie uma classe Conversor que tenha um método estático km_para_milhas(km), que converte quilômetros para milhas e retorna o valor convertido.

### D. Classe com Método de Classe
Crie uma classe Contador com um atributo de classe total_instancias. Toda vez que um novo objeto for criado, incremente esse valor.

### E. Classe com __str__ e __repr__
Crie uma classe Livro com os atributos titulo e autor. Sobrescreva os métodos __str__ e __repr__ para que a impressão do objeto seja mais informativa.


### F. Herança e Sobrescrita de Métodos
Crie uma classe Funcionario com os atributos nome e salario, e um método calcular_bonus(). Em seguida, crie uma subclasse Gerente que sobrescreve o método calcular_bonus().

### G. Uso de @property para Atributos Calculados
Crie uma classe Retangulo com largura e altura. Use @property para criar um atributo area que retorna a área do retângulo sem precisar ser chamado como método.

### H. Polimorfismo
Crie duas classes Cachorro e Gato, ambas com um método emitir_som(), que retorna "Latido" para cachorro e "Miado" para gato. Teste o polimorfismo chamando emitir_som() em objetos das duas classes.

### I. Interface com Classes Abstratas
Crie uma classe abstrata FormaGeometrica com um método abstrato calcular_area(). Implemente as classes Quadrado e Circulo, que herdam de FormaGeometrica e implementam o método de cálculo de área.

### J. Singleton em Python
Implemente um padrão Singleton em uma classe Configuracao, garantindo que só exista uma única instância dessa classe no programa.


### K. Uso de dataclass para Criar Objetos de Forma Simples
Utilize @dataclass para definir uma classe Produto que tenha os atributos nome, preco e estoque, simplificando a inicialização e exibição dos dados.

### L. Métodos Mágicos para Comparação de Objetos
Crie uma classe Pessoa com nome e idade e implemente os métodos __eq__, __lt__ e __gt__ para comparar instâncias dessa classe com base na idade.

### M. Gerenciador de Contexto com __enter__ e __exit__
Crie uma classe Arquivo que implemente um gerenciador de contexto para abrir e fechar arquivos automaticamente usando os métodos __enter__ e __exit__.

### N. Múltipla Herança e Conflito de Métodos
Crie duas classes A e B, ambas com um método mostrar(). Depois, crie uma classe C que herda de A e B e chame mostrar() para analisar qual método será executado.

### O. Metaprogramação com type
Use a função type() para criar dinamicamente uma classe Dinamica com um atributo x e um método mostrar(), que imprime o valor de x.

