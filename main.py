from flask import Flask, jsonify

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

# Roda o servidor se este arquivo for executado diretamente
if __name__ == '__main__':
    # debug=True faz o servidor reiniciar sozinho se você mudar o código
    app.run(debug=True, port=5002)