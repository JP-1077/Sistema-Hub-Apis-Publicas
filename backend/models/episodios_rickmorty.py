from datetime import datetime
from backend.database.db import db


class Filme (db.Model):
    __tablename__ = "tb_episodios_rickmorty"

    id = db.Column(db.Integer, primary_key=True)

    external_id = db.Column(
        db.Integer, 
        nullable=False
    )

    nome_episodio = db.Column(
        db.String(500),
        nullable=False

    )

    data_lancamento = db.Column(
        db.DateTime,
        default=datetime.utcnow
    )

    nomenclatura_episodio = db.Column(
        db.String(255),
        nullable=False
    )

    url_personagens_episodio = db.Column(
        db.String(500)
    )

    
    nome_api = db.Column(
        db.String(50),
        nullable=False
    )

    data_criacao_episodio = db.Column(
        db.DateTime,
        default=datetime.utcnow
    )

    data_atualizacao = db.Column(
        db.DateTime,
        default=datetime.utcnow,
        onupdate=datetime.utcnow
    )