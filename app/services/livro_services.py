from ..repositories.persistence import banco
from ..models.livro import Livro

class LivroService:
    def listar_todos(self): 
        # Apenas repassa a lista do banco
        return banco.ler_livros(), 200

    def pesquisar_por_id(self, id_livro):
        """
        Pesquisa um livro específico pelo ID
        """
        try:
            id_livro_int = int(id_livro)
        except (ValueError, TypeError):
            return {'erro': 'ID deve ser um número'}, 400
        
        if id_livro_int <= 0:
            return {'erro': 'ID deve ser maior que 0'}, 400
        
        livros = banco.ler_livros()
        
        for livro in livros:
            if livro.get('id') == id_livro_int:
                return livro, 200
        
        return {'erro': 'Livro não encontrado'}, 404

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
        livros_existentes = banco.ler_livros()
        for livro in livros_existentes:
            if livro.get('id') == id_livro_int:
                return {'erro': 'Já existe um livro com este ID'}, 409 # Conflict

        # --- SUCESSO ---
        # Instancia o Model
        novo_livro = Livro(id_livro_int, titulo, descricao)
        
        # Chama a persistência passando o dicionário
        banco.salvar_livro(novo_livro.to_dict())

        return '', 201
    
    def apagar_livro_por_id(self, id_livro):
        """
        Apaga um livro específico pelo ID
        """
        removeu = banco.apagar_livro(id_livro)
        
        if removeu:
            return '', 204
        
        return {'erro': 'Livro não encontrado'}, 404
    
    def pesquisar_por_titulo(self, titulo):
        """
        Pesquisa livros pelo título
        """
        return {'erro': 'Livro não encontrado'}, 404