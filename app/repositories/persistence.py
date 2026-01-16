import json
import os

# --- A MÁGICA ACONTECE AQUI ---
# 1. __file__ é o caminho deste arquivo (persistence.py)
# 2. abspath garante que o caminho seja absoluto (c:\users\...\persistence.py)
# 3. dirname pega apenas a pasta onde o arquivo está (...\app\repositories)
DIRETORIO_ATUAL = os.path.dirname(os.path.abspath(__file__))

# Agora montamos o caminho do JSON baseado na pasta deste arquivo
ARQUIVO_DB = os.path.join(DIRETORIO_ATUAL, 'banco_dados.json')

class banco:
    def ler_livros():
        """Lê o arquivo JSON e retorna a lista de livros."""
        # Se o arquivo não existir, retorna lista vazia
        if not os.path.exists(ARQUIVO_DB):
            return [] 
        
        try:
            with open(ARQUIVO_DB, 'r', encoding='utf-8') as arquivo:
                return json.load(arquivo)
        except json.JSONDecodeError:
            return []

    def salvar_livro(novo_livro):
        """Lê os livros atuais, adiciona o novo e salva tudo de volta."""
        lista_livros = banco.ler_livros()
        lista_livros.append(novo_livro)
        
        # Não precisamos mais criar a pasta com os.makedirs, 
        # pois se este script está rodando, a pasta app/repositories já existe.

        with open(ARQUIVO_DB, 'w', encoding='utf-8') as arquivo:
            json.dump(lista_livros, arquivo, indent=2, ensure_ascii=False)

    def apagar_livro(id_livro) -> bool:
        """Apaga um livro específico pelo ID."""
        lista_livros = banco.ler_livros()

        #lista_atualizada = [livro for livro in lista_livros if livro.get('id') != id_livro]
        lista_atualizada = []
        for livro in lista_livros:
            print("if livro.get('id') != id_livro: " + str(livro.get('id')) + " != " + str(id_livro) + " = " + str(livro.get('id') != int(id_livro)))
            if (int(livro.get('id')) != int(id_livro)):
                lista_atualizada.append(livro)
        
        if(len(lista_livros) == len(lista_atualizada)):
            return False;

        with open(ARQUIVO_DB, 'w', encoding='utf-8') as arquivo:
            json.dump(lista_atualizada, arquivo, indent=2, ensure_ascii=False)
        
        return True;
        
