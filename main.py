from app import create_app

app = create_app()

if __name__ == '__main__':
    # O 0.0.0.0 é a chave mágica que abre o Flask para o mundo
    app.run(host='0.0.0.0', debug=True, port=5002)
