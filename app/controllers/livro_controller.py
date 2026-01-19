from flask import Blueprint, request, jsonify
from ..services.livro_services import LivroService

# Cria o Blueprint
controllers = Blueprint('livros', __name__)

# Instancia o serviço
service = LivroService()

@controllers.route('/livros', methods=['GET'])
def obter_livros():
    """
    Lista todos os livros
    ---
    tags:
      - Livros
    responses:
      200:
        description: Lista retornada com sucesso
    """
    resposta, status = service.listar_todos()
    return jsonify(resposta), status

@controllers.route('/livros/<id_livro>', methods=['GET'])
def obter_livro(id_livro):
    """
    Obtém um livro específico por ID
    ---
    tags:
      - Livros
    parameters:
      - in: path
        name: id_livro
        type: integer
        required: true
        description: ID do livro
    responses:
      200:
        description: Livro encontrado
      400:
        description: ID inválido
      404:
        description: Livro não encontrado
    """
    resposta, status = service.pesquisar_por_id(id_livro)
    return jsonify(resposta), status

@controllers.route('/livros', methods=['POST'])
def livros():
    """
    Cria um novo livro
    ---
    tags:
      - Livros
    parameters:
      - in: body
        name: body
        required: true
        schema:
          type: object
          properties:
            id_livro:
              type: integer
            titulo:
              type: string
            descricao:
              type: string
    responses:
      201:
        description: Livro criado
      400:
        description: Erro de validação
      409:
        description: ID duplicado
    """
    dados = request.get_json()
    resposta, status = service.criar_novo(dados)
    
    # Se a resposta for vazia (caso do 201), jsonify lida bem
    return jsonify(resposta) if resposta else ('', status)

@controllers.route('/livros/<id_livro>', methods=['DELETE']) #o nome do parâmetro na rota deve ser identico ao parametro no método.
def deletar_livro(id_livro : int):
    """
    Apaga um livro específico pelo ID
    ---
    tags:
      - Livros
    parameters:
      - in: path
        name: id_livro
        type: integer
        required: true
        description: ID do livro
    responses:
      200:
        description: Livro deletado com sucesso
      400:
        description: ID inválido
      404:
        description: Livro não encontrado então não deletou nada
    """
    print("Recebido o request: Id_Livro -> " + id_livro)
    resposta, status = service.apagar_livro_por_id(id_livro)
    return jsonify(resposta), status

@controllers.route('/livros/buscar', methods=['POST'])
def buscar_livros_por_titulo():
    """
    Busca livros por título
    ---
    tags:
      - Livros
    parameters:
      - in: body
        name: body
        required: true
        schema:
          type: object
          properties:
            titulo:
              type: string
              description: Título ou parte do título do livro a ser buscado.
    responses:
      200:
        description: Lista de livros encontrados.
      400:
        description: Requisição inválida (título não fornecido).
    """
    dados = request.get_json()
    titulo = dados.get('titulo')
    if not titulo:
      return jsonify({'erro': 'O campo "titulo" é obrigatório'}), 400

    resposta, status = service.pesquisar_por_titulo(titulo)
    return jsonify(resposta), status
