from flask import Blueprint, request, jsonify
from ..services.autores_services import AutoresService

  

# Cria o Blueprint
autorControllers = Blueprint('autores', __name__)

# Instancia o serviço
service = AutoresService()

@autorControllers.route('/autores', methods=['GET'])
def obter_autores():
    """
    Lista todos os autores
    ---
    tags:
      - Autores
    responses:
      200:
        description: Lista retornada com sucesso
    """
    resposta, status = service.listar_autores()
    return jsonify(resposta), status

@autorControllers.route('/autores/<idlivro>', methods=['GET'])
def obter_autor(idlivro):
    """
    Pesquisa autor por ID
    ---
    tags:
      - Autores
    responses:
      200:
        description: pesquisa retornada com sucesso
    """
    resposta, status = service.pesquisar_autor(idlivro)
    return jsonify(resposta), status