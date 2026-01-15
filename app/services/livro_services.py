from ..repositories.persistence import ler_livros, salvar_livro
from ..models.livro import Livro

class LivroService:
    def listar_todos(self): 
        # Apenas repassa a lista do banco
        return ler_livros(), 200

    def criar_novo(self, dados):
        # Extrai os dados
        id_livro = dados.get('id_livro')
        titulo = dados.get('titulo')
        descricao = dados.get('descricao')

        # --- SUAS VALIDAÇÕES (Vieram do main.py) ---
        if not id_livro or not titulo or not descricao: 
            return {'erro': 'Todos os campos são obrigatórios'}, 400
        
        try:
            id_livro_int = int(id_livro)
        except ValueError:
            return {'erro': 'ID deve ser um número'}, 400

        if id_livro_int <= 0:
            return {'erro':'id incorreto, deve ser maior que 0'}, 400
        
        if len(titulo) > 40:
            return {'erro':'titulo deve conter no maximo 40 caracteres'}, 400
        
        if len(descricao) >= 300:
            return {'erro':'descrição deve conter menos de 300 caracteres'}, 400

        # --- REGRA DE NEGÓCIO: DUPLICIDADE ---
        livros_existentes = ler_livros()
        for livro in livros_existentes:
            if livro.get('id') == id_livro_int:
                return {'erro': 'Já existe um livro com este ID'}, 409 # Conflict

        # --- SUCESSO ---
        # Instancia o Model
        novo_livro = Livro(id_livro_int, titulo, descricao)
        
        # Chama a persistência passando o dicionário
        salvar_livro(novo_livro.to_dict())

        return '', 201