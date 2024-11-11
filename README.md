Exercício Integrado de Orientação a Objetos, Programação Funcional, RPA com BotCity, Arquivos Binários e Tratamento de Exceções
Objetivo do Exercício
Criar uma aplicação Python orientada a objetos para gerenciar pedidos de uma loja virtual fictícia. Aplicar conceitos de programação funcional e RPA com BotCity, além de manipulação de arquivos em diferentes formatos (JSON e binário com pickle) e tratamento de exceções. A aplicação terá funcionalidades de cadastro, manipulação de pedidos e automatização de tarefas.

Especificações do Exercício
1. Estrutura de Classes
A equipe deve criar uma estrutura de classes para representar Produto, Pedido e GestorDePedidos.

Classe Produto:

Atributos:
nome (str)
preco (float)
categoria (str)
Método:
detalhes(): Retorna uma descrição do produto.
Classe Pedido:

Atributos:
produtos (lista de instâncias Produto)
quantidade (dicionário que mapeia cada produto à sua quantidade)
cliente (str)
status (str - valores possíveis: "Novo", "Processando", "Enviado")
Métodos:
total_pedido(): Calcula o total do pedido aplicando map e reduce nos produtos e suas quantidades.
detalhes_pedido(): Retorna os detalhes do pedido (produtos, quantidade, cliente, status).
Classe GestorDePedidos:

Atributos:
pedidos (lista de pedidos)
Métodos:
adicionar_pedido(pedido): Adiciona um novo pedido à lista.
listar_pedidos_por_status(status): Retorna pedidos com um status específico usando filter.
pedidos_por_categoria(categoria): Usa map para gerar um relatório de quantos produtos de uma categoria específica foram vendidos.
total_vendas(): Retorna o valor total de vendas utilizando reduce.
Manipulação de Arquivos:

salvar_dados_json(): Salva os pedidos em um arquivo JSON.
carregar_dados_json(): Carrega os dados de pedidos do JSON.
salvar_dados_binario(): Salva os dados em um arquivo binário usando pickle.
carregar_dados_binario(): Carrega os dados de um arquivo binário usando pickle.
2. Tratamento de Exceções
Para tornar a aplicação mais robusta, implemente tratamento de exceções nos seguintes casos:

Manipulação de Arquivos:

Utilize try-except para lidar com erros de abertura e leitura de arquivos (ex.: FileNotFoundError).
Adicione mensagens de erro ao usuário para que ele saiba quando ocorre um problema durante a leitura ou gravação dos dados.
Validação de Pedidos e Produtos:

Verifique se os preços dos produtos são válidos (positivos) ao adicioná-los, lançando uma exceção personalizada ValorInvalidoError caso contrário.
Ao tentar adicionar um pedido, verifique se a quantidade é um número positivo e levante uma exceção QuantidadeInvalidaError caso contrário.
