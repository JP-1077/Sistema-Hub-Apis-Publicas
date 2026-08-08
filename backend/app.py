from flask import Flask
from flask_migrate import Migrate

from backend.config import Config
from backend.database.db import db

from backend.routes.rota_rickmorty import rickmorty_bp
from backend.models import *

from backend.routes.rota_rickmorty_localizacao import localizacao_bp
from backend.routes.rota_rickmorty_personagem import personagens_bp
from backend.routes.rota_rickmorty_episodios import episodios_bp

try:
    from backend.routes.rota_rickmorty import rickmorty_bp
except ModuleNotFoundError:
    rickmorty_bp = None

migrate = Migrate()

def create_app():

    app = Flask(__name__)

    app.config.from_object(Config)

    db.init_app(app)
    migrate.init_app(app, db)

    app.register_blueprint(localizacao_bp)
    app.register_blueprint(personagens_bp)
    app.register_blueprint(episodios_bp)

    return app