# Pós-graduação | Desenvolvimento Web Full Stack
### CRUD de Produtos, Clientes e Pedidos
Projeto desenvolvido para obtenção de nota na disciplina de Modelagem de Banco de dados.

#### Alunos:
>   - Miquéias R. M. Soares
>   - Eduardo Henrique Fidelis Porto

## Descrição

Desenvolvido em Python com uso do Flask.

O projeto lida com uma persistência poliglota, com dados em um banco relacional e um não relacional.

1. Relacional MySQL com as tabelas:
   - Produtos (que mantém): ID_produto, Nome, Descricao, Categoria e Preço
   - Clientes: ID_cliente, Nome, Email, CPF e Data de Nascimento
  
2. Não reacional MongoDB com a coleção:
   - Pedidos: ID_produto, ID_Cliente, Data_pedido, Valor_pedido
  


## Get started

> As dependências e pacotes utilizados estão no arquivo `requirements.txt`
#### Install
```
$ pip install -r requirements.txt 
```
#### Run
```
$ flask --app main run
```

## Rotas 

Produtos: MySQL

| Request | URL |  Observações |
|-|-|-|
| **GET** | /produtos | Busca todos os produtos
| **POST** | /produto | Salva um produto na base de dados
| **PUT** | /produto/id | Atualiza os dados do produto (int: id)
| **DELETE** | /produto/id | Remove um produto (int: id)

Clientes: MySQL

| Request | URL |  Observações |
|-|-|-|
| **GET** | /clientes | Busca todos os clientes
| **POST** | /cliente | Salva um cliente na base de dados
| **PUT** | /cliente/id | Atualiza os dados do cliente (int: id)
| **DELETE** | /cliente/id | Remove um cliente (int: id)

Pedidos: MongoDB

| Request | URL |  Observações |
|-|-|-|
| **GET** | /pedidos | Busca todos os pedidos
| **POST** | /pedido | Salva um pedido na base de dados
| **PUT** | /pedido/id | Atualiza os dados do pedido (int: id)
| **DELETE** | /pedido/id | Remove um pedido (int: id)
