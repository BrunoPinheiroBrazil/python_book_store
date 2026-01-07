from flask import Flask, jsonify, request

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

@app.route('/api/livros', methods=['POST'])
def livros():
    dados = request.get_json()
    id_livro = dados.get('id_livro')
    titulo = dados.get('titulo')
    descricao = dados.get('descricao')
    
    if not id_livro and not titulo and not descricao: 
        return jsonify({'erro': 'nenhum campo foi preenchido'}), 400
    elif int(id_livro) <= 0:
        return jsonify({'erro':'id incorreto'}), 400
    elif len(titulo) >= 40:
        return jsonify({'erro':'titulo deve conter no maximo 40 caracteres'}), 400
    elif len(descricao) > 300:
        return jsonify({'erro':'descrição deve conter no maximo 299 caracteres'}), 400

    return '', 204
    
# Roda o servidor se este arquivo for executado diretamente
if __name__ == '__main__':
    # debug=True faz o servidor reiniciar sozinho se você mudar o código
    app.run(debug=True, port=5002)
