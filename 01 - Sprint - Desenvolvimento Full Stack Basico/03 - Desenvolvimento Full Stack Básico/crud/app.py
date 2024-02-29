'''
IMPORTS
'''
# acessar arquivo .env
import os
# conexao com o banco
import psycopg2
# carregar arquivo .env
from dotenv import load_dotenv
# servidor http
from flask import Flask, request

'''
VARIAVEIS LOCAIS
'''
# carregando o arquivo .env
load_dotenv()
# recuperando url do arquivo .env
url = os.getenv("DATABASE_URL")
# criando conexao com o banco
connection = psycopg2.connect(url)

'''
SCRIPTS BANCO DE DADOS
'''
CREATE_TABLE_PRODUTO = ("CREATE TABLE IF NOT EXISTS produto (id SERIAL PRIMARY KEY, nome TEXT, quantidade INT, valor FLOAT, data_registro DATE DEFAULT CURRENT_DATE);")
INSERT_PRODUTO_RETURNING_ID = "INSERT INTO produto (nome, quantidade, valor) VALUES (%s, %s, %s) RETURNING id;"
SELECT_PRODUTO_BY_ID = "SELECT * FROM produto WHERE id = (%s);"



app = Flask(__name__)

'''
URL PARA CADASTRO DE PRODUTO
'''
@app.post("/produto")
def create_produto():
    print("\nIniciando cadastro de produto\n")
    data = request.get_json()
    print("Requisição recebida com sucesso: " + str(data) + "\n")
    nome = data["nome"]
    quantidade = data["quantidade"]
    valor = data["valor"]
    print("\nnome: " + str(nome))
    print("quantidade: " + str(quantidade))
    print("valor: " + str(valor) + "\n")
    print("\nIniciando transação com o banco\n")
    with connection:
        with connection.cursor() as cursor:
            cursor.execute(CREATE_TABLE_PRODUTO)
            cursor.execute(INSERT_PRODUTO_RETURNING_ID, (nome, quantidade, valor))
            produto_id = cursor.fetchone()[0]
            print("\nProduto cadastrado com sucesso\n")
        return {"id": produto_id, "message": "Produto cadastrado com sucesso"}, 201
    
'''
URL PARA CONSULTA DE PRODUTO
'''
@app.route("/produto/<id>")
def get_produto(id):
    print("\nIniciando consulta de produto\n")
    print("Requisição recebida com sucesso: " + str(id) + "\n")
    print("Iniciando transação com o banco\n")
    with connection:
        with connection.cursor() as cursor:
            cursor.execute(CREATE_TABLE_PRODUTO)
            cursor.execute(SELECT_PRODUTO_BY_ID, (id))
            produto = cursor.fetchall()[0]
            print("\nProduto encontrado com sucesso: " + str(produto))
        return {"produto": str(produto), "message": "Produto encontrado com sucesso"}, 200