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