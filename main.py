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


@app.route("/produtos", methods=["POST"])
def set_produtos():
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

@app.route("/clientes", methods=["GET"])
def get_clientes():
    clientes = Clientes.query.all()
    return jsonify([cliente.serialize() for cliente in clientes])

@app.route("/clientes", methods=["POST"])
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


if __name__ == '__main__':
    app.run(debug=True)
