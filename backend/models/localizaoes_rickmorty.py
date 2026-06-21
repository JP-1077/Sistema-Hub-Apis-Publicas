from datetime import datetime
from backend.database.db import db

class Planeta (db.Model):
    __tablename__ = 'tb_localizaoes_rickmorty'

    id = db.Column(
        db.Integer, 
        primary_key=True
    )

    external_id = db.Column(
        db.Integer, 
        nullable=False
    )

    nome_localizacao = db.Column(
        db.String(255),
        nullable = False
    )

    tipo_localizacao = db.Column(
        db.String(255)
    )

    dimensao = db.Column(
        db.String(255)
    )
    
    residentes_localizacao = db.Column(
        db.String(500)
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



