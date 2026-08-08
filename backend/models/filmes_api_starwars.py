from datetime import datetime
from backend.database.db import db

class Filmesstarwars (db.Model):
    __tablename__ = "tb_filmes_api_starwars"

    id = db.Column(
        db.Integer, 
        primary_key=True
    )

    external_id = db.Column(
        db.Integer, 
        nullable=False
    )

    titulo_filme = db.Column(
        db.String(500),
        nullable=False
    )

    episodio = db.Column(
        db.String(500),
        nullable=False
    )

    texto_abertura = db.Column(
        db.String(500),
        nullable=False
    )

    diretor = db.Column(
        db.String(500), 
        nullable=False
    )

    produtor = db.Column(
        db.String(500), 
        nullable=False
    )

    data_lancamento = db.Column(
        db.DateTime,
        default=datetime.utcnow
    )

    url_personagens_filme = db.Column(
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

