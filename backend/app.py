from flask import Flask
from flask_migrate import Migrate
from backend.config import Config
from backend.database.db import db
from backend.routes.rota_rickmorty import rickmorty_bp
from backend.models import *

def create_app():

    app = Flask(__name__)

    app.config.from_object(Config)
    db.init_app(app)
    Migrate(app, db)

    with app.app_context():
        db.create_all()
    
    app.register_blueprint(
        rickmorty_bp
    )

    return app