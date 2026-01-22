import json
import os

DIRETORIO_ATUAL = os.path.dirname(os.path.abspath(__file__))
ARQUIVO_DB = os.path.join(DIRETORIO_ATUAL, 'banco_dados.json')

class banco:
    
    # --- MÉTODOS PRIVADOS (Auxiliares) ---
    def _ler_arquivo_completo():
        if not os.path.exists(ARQUIVO_DB):
            return {"livros": [], "autores": []}
        
        try:
            with open(ARQUIVO_DB, 'r', encoding='utf-8') as arquivo:
                dados = json.load(arquivo)
                # Garante integridade das chaves
                if "livros" not in dados: dados["livros"] = []
                if "autores" not in dados: dados["autores"] = []
                return dados
        except json.JSONDecodeError:
            return {"livros": [], "autores": []}

    def _salvar_arquivo_completo(dados_completos):
        with open(ARQUIVO_DB, 'w', encoding='utf-8') as arquivo:
            json.dump(dados_completos, arquivo, indent=2, ensure_ascii=False)

    # --- LIVROS ---
    def ler_livros():
        dados = banco._ler_arquivo_completo()
        return dados["livros"]

    def salvar_livro(novo_livro):
        dados_completos = banco._ler_arquivo_completo()
        dados_completos["livros"].append(novo_livro)
        banco._salvar_arquivo_completo(dados_completos)

    def buscar_livro_por_titulo(titulo: str):
        lista_livros = banco.ler_livros()
        if not titulo: return [], 200
        
        return [l for l in lista_livros if titulo.lower() in l.get('titulo', '').lower()]

    def apagar_livro(id_livro) -> bool:
        dados_completos = banco._ler_arquivo_completo()
        lista_livros = dados_completos["livros"]
        
        # Filtra removendo o item desejado
        nova_lista = [l for l in lista_livros if int(l.get('id')) != int(id_livro)]
        
        if len(nova_lista) == len(lista_livros):
            return False # Nada foi apagado

        dados_completos["livros"] = nova_lista
        banco._salvar_arquivo_completo(dados_completos)
        return True

    # --- AUTORES (NOVO) ---
    
    def ler_autores():
        """Retorna apenas a lista de autores."""
        dados = banco._ler_arquivo_completo()
        return dados["autores"]

    def salvar_autor(novo_autor):
        """Salva um autor e gera ID automático se não tiver."""
        dados_completos = banco._ler_arquivo_completo()
        
        # Lógica de Auto-Incremento de ID para Autor
        lista_autores = dados_completos["autores"]
        
        if not novo_autor.get('id'):
            if len(lista_autores) > 0:
                # Pega o ID do último da lista e soma 1
                novo_id = lista_autores[-1].get('id', 0) + 1
            else:
                novo_id = 1
            novo_autor['id'] = novo_id

        dados_completos["autores"].append(novo_autor)
        banco._salvar_arquivo_completo(dados_completos)
        return novo_autor # Retorna com o ID gerado