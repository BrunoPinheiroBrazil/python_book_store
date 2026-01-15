class Livro:
  def __init__(self, id_livro, titulo, descricao):
      self.id_livro = id_livro
      self.titulo = titulo
      self.descricao = descricao

  def to_dict(self):
      return {
          "id": self.id_livro,
          "titulo": self.titulo,
          "descricao": self.descricao
      }
  