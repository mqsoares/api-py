from config import SQLALCHEMY_DATABASE_URI, mongodb
from flask import Flask, jsonify, request
from sqlalchemy import Integer, String, Float, Date
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI

mysql = SQLAlchemy(app)


class Produtos(mysql.Model):
    id_produto = mysql.Column(Integer, primary_key=True)
    nome = mysql.Column(String)
    descricao = mysql.Column(String)
    preco = mysql.Column(Float)
    categoria = mysql.Column(String)

    def serialize(self):
        return {
            "id": self.id_produto,
            "nome": self.nome,
            "descricao": self.descricao,
            "preco": self.preco,
            "categoria": self.categoria
        }


class Clientes(mysql.Model):
    id_cliente = mysql.Column(Integer, primary_key=True)
    nome = mysql.Column(String)
    email = mysql.Column(String)
    cpf = mysql.Column(Float)
    data_nasc = mysql.Column(Date)

    def serialize(self):
        return {
            "id": self.id_cliente,
            "nome": self.nome,
            "email": self.email,
            "cpf": self.cpf,
            "data_nasc": self.data_nasc
        }


@app.route("/produtos", methods=["GET"])
def get_produtos():
    produtos = Produtos.query.all()
    return jsonify([produto.serialize() for produto in produtos])


@app.route("/produto", methods=["POST"])
def set_produtos():
    try:
        dados = request.get_json()
        produto = Produtos(
            nome=dados["nome"],
            descricao=dados["descricao"],
            preco=dados["preco"],
            categoria=dados["categoria"]
        )
        mysql.session.add(produto)
        mysql.session.commit()
        return jsonify(produto.serialize()), 201
    except Exception as e:
        print(f"Erro: {e}")
        return "Erro ao cadastrar Produto.", 400


@app.route("/produto/<int:id>", methods=["PUT"])
def update_produto(id):
    try:
        dados = request.get_json()
        produto = mysql.session.query(Produtos).get(id)
        produto.nome = dados["nome"]
        produto.descricao = dados["descricao"]
        produto.preco = dados["preco"]
        produto.categoria = dados["categoria"]

        mysql.session.commit()
        return jsonify(produto.serialize()), 201
    except Exception as e:
        print(f"Error: {e}")
        return "Erro ao alterar os dados", 400


@app.route("/produto/<int:id>", methods=["DELETE"])
def delete_produto(id):
    try:
        produto = mysql.session.query(Produtos).get(id)
        mysql.session.delete(produto)
        mysql.session.commit()
        return jsonify("Excluido com sucesso."), 200
    except Exception as e:
        print(f"Erro: {e}")
        return "Erro ao excluir produto", 400


@app.route("/clientes", methods=["GET"])
def get_clientes():
    clientes = Clientes.query.all()
    return jsonify([cliente.serialize() for cliente in clientes])


@app.route("/cliente", methods=["POST"])
def set_clientes():
    dados = request.get_json()
    cliente = Clientes(
        nome=dados["nome"],
        email=dados["email"],
        cpf=dados["cpf"],
        data_nasc=dados["data_nasc"],
    )
    mysql.session.add(cliente)
    mysql.session.commit()
    return jsonify(cliente.serialize()), 201


@app.route("/cliente/<int:id>", methods=["PUT"])
def update_cliente(id):
    try:
        dados = request.get_json()
        cliente = mysql.session.query(Clientes).get(id)
        cliente.nome = dados["nome"]
        cliente.email = dados["email"]
        cliente.cpf = dados["cpf"]
        cliente.data_nasc = dados["data_nasc"]

        mysql.session.commit()
        return jsonify(cliente.serialize()), 201
    except Exception as e:
        print(f"Error: {e}")
        return "Erro ao alterar os dados", 400


@app.route("/cliente/<int:id>", methods=["DELETE"])
def delete_cliente(id):
    try:
        cliente = mysql.session.query(Clientes).get(id)
        mysql.session.delete(cliente)
        mysql.session.commit()
        return jsonify("Excluído com sucesso"), 200
    except Exception as e:
        print(f"Erro: {e}")
        return "Erro ao excluir cliente", 400


if __name__ == '__main__':
    app.run(debug=True)
