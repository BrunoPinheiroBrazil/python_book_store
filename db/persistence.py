import json
import os

# Define o nome da pasta e o caminho completo do arquivo
PASTA_DB = 'db'
ARQUIVO_DB = os.path.join(PASTA_DB, 'banco_dados.json') # Isso cria algo como "db/banco_dados.json"

def ler_livros():
    """Lê o arquivo JSON e retorna a lista de livros."""
    # Verifica se o ARQUIVO existe (se a pasta não existir, isso também retorna False)
    if not os.path.exists(ARQUIVO_DB):
        return [] 
    
    try:
        with open(ARQUIVO_DB, 'r', encoding='utf-8') as f:
            return json.load(f)
    except json.JSONDecodeError:
        return []

def salvar_livro(novo_livro):
    """Lê os livros atuais, adiciona o novo e salva tudo de volta."""
    lista_livros = ler_livros()
    lista_livros.append(novo_livro)
    
    if not os.path.exists(PASTA_DB):
        os.makedirs(PASTA_DB)
    # --------------------------------------

    with open(ARQUIVO_DB, 'w', encoding='utf-8') as f:
        json.dump(lista_livros, f, indent=4, ensure_ascii=False)