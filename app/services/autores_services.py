from ..repositories.persistence import banco
from ..models.livro import Livro

class AutoresService:
  def listar_autores(self):
    return banco.ler_autores(), 200