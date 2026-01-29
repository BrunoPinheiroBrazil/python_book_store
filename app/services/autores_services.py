from ..repositories.persistence import banco
from ..models.livro import Livro

class AutoresService:
  def listar_autores(self):
    return banco.ler_autores(), 200
  

  def pesquisar_autor(self, idlivro):
    """
      Pesquisa um autor específico pelo ID 
    """
    try:
      id_livro_autor_int = int(idlivro)
    except (ValueError, TypeError):
      return {'erro': 'ID deve ser um número'}, 400
    if id_livro_autor_int <= 0:
      return {'erro': 'ID deve ser maior que 0'}, 400
    autores = banco.ler_autores()

    for autor in autores:
      if autor.get('id') == id_livro_autor_int:
        return autor, 200
    return {'erro': 'autor não encontrado'}, 404