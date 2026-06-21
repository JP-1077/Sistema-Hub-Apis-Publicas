from datetime import datetime
from backend.database.db import db


class Filme (db.Model):
    __tablename__ = "tb_filmes"

    id = db.Column(db.Integer, primary_key=True)

    external_id = db.Column(
        db.Integer, 
        nullable=False
    )

    titulo = db.Column(
        db.String(255),
        nullable=False

    )

    data_lancamento = db.Column(
        db.DateTime,
        default=datetime.utcnow
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