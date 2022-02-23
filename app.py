import json
from flask import Flask, request, jsonify

app = Flask(__name__)

lista_de_nomes = [
    {'nome': 'Elton Marcelino'},
    {'nome': 'Yasmin Marcelino'},
    {'nome':'Hellena Victória'}
]

# @app.get('/nomes')
# def todos_nomes():
#     return jsonify(lista_de_nomes), 200

# @app.post('/nomes')
# def registrar_nome():
#     data = request.get_json()
#     novo_nome = data.get('nome')
#     lista_de_nomes.append(data)

#     return {'msg': f'Usuario {novo_nome} cadastrado!'},201

#  Segundo jeito de fazer

@app.route('/nomes', methods=['GET','POST'])
def registrar_listar_nomes():
    if request.method == 'POST':
        data = request.get_json()
        novo_nome = data.get('nome')
        lista_de_nomes.append(data)

        return  {'msg': f'Usuario {novo_nome} cadastrado!'},201

    elif request.method == 'GET':

        return jsonify(lista_de_nomes)