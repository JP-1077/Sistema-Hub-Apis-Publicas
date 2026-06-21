from datetime import datetime
from backend.database.db import db

class Planeta (db.Model):
    __tablename__ = 'tb_planetas'

    id = db.Column(
        db.Integer, 
        primary_key=True
    )

    external_id = db.Column(
        db.Integer, 
        nullable=False
    )

    nome = db.Column(
        db.String(255),
        nullable = False
    )

    clima = db.Column(
        db.String(100),
        nullable = False
    )

    populacao = db.Column(
        db.String(100),
        nullable = False
    )

    nome_api = db.Column(
        db.String(50),
        nullable=False
    )

    data_criacao = db.Column(
        db.DateTime,
        default=datetime.utcnow
    )

    data_atualizacao = db.Column(
        db.DateTime,
        default=datetime.utcnow,
        onupdate=datetime.utcnow
    )



