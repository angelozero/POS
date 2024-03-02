'''
IMPORTS
'''
# acessar arquivo .env
import os
# conexao com o banco
import psycopg2
# json
import json
# carregar arquivo .env
from dotenv import load_dotenv
# servidor http
from flask import Flask, request
from flask_cors import CORS

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
app.config['CORS_HEADERS'] = 'Content-Type'
CORS(app, resources={r"/produto": {"origins": "*"}})

'''
URL PARA CADASTRO DE PRODUTO
'''
@app.post("/produto")
def create_produto():
    print("Iniciando cadastro de produto: " + str(request.get_json()) + "\n")
    data = request.get_json()
    nome = data["nome"]
    quantidade = data["quantidade"]
    valor = data["valor"]
    with connection:
        with connection.cursor() as cursor:
            # Criando a tabela se caso não exisitr 
            cursor.execute(CREATE_TABLE_PRODUTO)
            
            # Inserindo um produto na tabela
            cursor.execute(INSERT_PRODUTO_RETURNING_ID, (nome, quantidade, valor))
            produto_id = cursor.fetchone()[0]
            print("\nProduto cadastrado com sucesso " + str(produto_id) + "\n")
            cursor.connection.commit()
            
            # Consultando e retornando o objeto salvo
            cursor.execute(SELECT_PRODUTO_BY_ID, (produto_id,))
            produto_salvo = cursor.fetchall()[0]
            produto_response = dict(zip([x[0] for x in cursor.description], produto_salvo))
            produto_json = json.dumps(produto_response, indent=4, sort_keys=True, default=str)
            
            print("\nPRODUTO SALVO: " + str(produto_json) + "\n")

        return produto_json, 201
    
'''
URL PARA CONSULTA DE PRODUTO
'''
@app.route("/produto/<id>")
def get_produto(id):
    print("Iniciando consulta de produto: " + str(id) + "\n")
    with connection:
        with connection.cursor() as cursor:
            # Criando a tabela se caso não existir
            cursor.execute(CREATE_TABLE_PRODUTO)
            
            # Consultando o objeto pelo seu ID
            cursor.execute(SELECT_PRODUTO_BY_ID, (id,))
            produto_encontrado = cursor.fetchall()[0]
            produto_response = dict(zip([x[0] for x in cursor.description], produto_encontrado))
            produto_json = json.dumps(produto_response, indent=4, sort_keys=True, default=str)
            
            print("\nProduto encontrado com sucesso: " + str(produto_json))
        return produto_json, 200