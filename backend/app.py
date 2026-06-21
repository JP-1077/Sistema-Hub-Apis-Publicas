from flask import Flask
from backend.config import Config
from backend.database.db import db

from backend.models import *

def criacao_banco_dados():

    banco = Flask(__name__)
    banco.config.from_object(Config)
    db.init_app(banco)

    with banco.app_context():
        db.create_all()
        
    return banco