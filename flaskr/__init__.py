import os

from flask import Flask

def create_app(test_config=None):
    #cria e configura o app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite')
    )

    if test_config is None:
        #Carrega a instância da configuração, se ela existir, quando não está testando
        app.config.from_pyfile('config.py', silent=True)
    else:
        #Carrega o teste se ele for passado
        app.config.from_mapping(test_config)

    #Garante que a pasta da instância existe
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # Uma simples pagina que diz oi
    @app.route('/')
    def hello():
        return "Hello, Friend"

    from . import db
    db.init_app(app)

    return app
  

