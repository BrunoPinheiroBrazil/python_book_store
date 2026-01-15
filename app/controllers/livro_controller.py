from flask import Blueprint, request, jsonify
from ..services.livro_services import LivroService

# Cria o Blueprint
livro_bp = Blueprint('livros', __name__)

# Instancia o serviço
service = LivroService()

@livro_bp.route('/livros', methods=['GET'])
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

@livro_bp.route('/livros/<id_livro>', methods=['GET'])
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

@livro_bp.route('/livros', methods=['POST'])
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