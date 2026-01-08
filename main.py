from flask import Flask, jsonify, request
from db.persistence import *

# Inicializa a aplicação Flask
app = Flask(__name__)

# Define a rota (endpoint), o método HTTP (GET)
@app.route('/api/mensagem', methods=['GET'])
def obter_mensagem():
    # O objeto que será retornado (Dicionário em Python vira JSON automaticamente)
    resposta = {
        'mensagem': 'Olá! Requisição recebida com sucesso.'
    }
    
    # jsonify converte o dicionário para JSON
    # 200 é o status code HTTP (OK)
    return jsonify(resposta), 200

@app.route('/api/media', methods=['POST'])
def calcular_media():
    dados = request.get_json();
    notas = dados.get('notas');
    
    if not notas or len(notas) == 0:
        return jsonify({'erro': 'Lista de notas vazia ou inválida'}), 400
        
    media = calcular_a_media(notas[0], notas[1], notas[2])
    return jsonify({'media': media}), 200

def calcular_a_media(n1: int, n2: int, n3: int) -> float:
    media = (n1 + n2 + n3) / 3;
    return media;

@app.route('/api/verificar_nome', methods=['POST'])
def verificar_nome():
    dados = request.get_json();
    nome = dados.get('nome');
    
   # if not nome:
    #    return jsonify({'erro': 'nome ausente'}), 400

    if len(nome) % 2 == 0:
        return jsonify({'é':'PAR'}), 200;
    
    return jsonify({'VACILO':'vacilão'}), 200;

# ------------------------------------------------------ API LIVROS  ----------------------------------------------------

@app.route('/api/livros', methods=['GET'])
def obter_livros():
    # 1. Busca a lista no arquivo
    lista = ler_livros()
    
    # 2. Retorna a lista como JSON e status 200 (OK)
    return jsonify(lista), 200

@app.route('/api/livros', methods=['POST'])
def livros():
    dados = request.get_json()
    
    # .get() evita erro se a chave não existir
    id_livro = dados.get('id_livro')
    titulo = dados.get('titulo')
    descricao = dados.get('descricao')
    
    # --- VALIDAÇÕES (Lógica corrigida para garantir que funcione) ---
    
    if not id_livro or not titulo or not descricao: 
        return jsonify({'erro': 'Todos os campos são obrigatórios'}), 400
    
    # Converte para int para fazer as comparações matemáticas
    try:
        id_livro_int = int(id_livro)
    except ValueError:
        return jsonify({'erro': 'ID deve ser um número'}), 400

    if id_livro_int <= 0:
        return jsonify({'erro':'id incorreto, deve ser maior que 0'}), 400
    
    if len(titulo) > 40:
        return jsonify({'erro':'titulo deve conter no maximo 40 caracteres'}), 400
    
    if len(descricao) >= 300:
        return jsonify({'erro':'descrição deve conter menos de 300 caracteres'}), 400

    # --- NOVIDADE: Verifica se o ID já existe no banco ---
    livros_existentes = ler_livros()
    for livro in livros_existentes:
        if livro['id'] == id_livro_int:
            return jsonify({'erro': 'Já existe um livro com este ID'}), 409 # 409 = Conflict

    # --- PERSISTÊNCIA: Cria o objeto e salva ---
    novo_livro_obj = {
        "id": id_livro_int,
        "titulo": titulo,
        "descricao": descricao
    }
    
    salvar_livro(novo_livro_obj)

    # Retorna 201 (Created)
    return '', 201
    
# Roda o servidor se este arquivo for executado diretamente
if __name__ == '__main__':
    # debug=True faz o servidor reiniciar sozinho se você mudar o código
    app.run(debug=True, port=5002)
