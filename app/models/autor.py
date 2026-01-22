class Autor:
  def __init__(self, id_autor, nome, nacionalidade, genero):
      self.id_autor = id_autor
      self.nome = nome
      self.nacionalidade = nacionalidade

  def to_dict(self):
      return {
          "id": self.id_autor,
          "nome": self.nome,
          "nacionalidade": self.nacionalidade
      }
  