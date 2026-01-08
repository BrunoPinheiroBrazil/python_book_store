from flask import Flask
from flasgger import Swagger
from .controllers.livro_controller import livro_bp

def create_app():
    app = Flask(__name__)
    
    # Configura Swagger
    app.config['SWAGGER'] = {'title': 'Book Store API', 'uiversion': 3}
    swagger_config = {
        "headers": [],
        "specs": [
            {
                "endpoint": 'apispec',
                "route": '/apispec.json',
                "rule_filter": lambda rule: True,  # inclua todas as regras
                "model_filter": lambda tag: True,  # inclua todos os models
            }
        ],
        "static_url_path": "/flasgger_static",
        "swagger_ui": True,
        "specs_route": "/swagger/"  # <--- AQUI ESTÁ A MÁGICA
    }
    Swagger(app, swagger_config)
    
    # Registra as rotas com prefixo /api
    app.register_blueprint(livro_bp, url_prefix='/api')
    
    return app