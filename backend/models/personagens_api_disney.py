from datetime import datetime
from backend.database.db import db

class Personagemdisney (db.Model):
    __tablename__ = "tb_personagens_api_disney"

    id = db.Column(
        db.Integer, 
        primary_key=True
    )

    external_id = db.Column(
        db.Integer, 
        nullable=False
    )

    filmes = db.Column(
        db.String(500),
        nullable=False
    )

    filmes_shorts = db.Column(
        db.String(500),
        nullable=False
    )

    tv_shows = db.Column(
        db.String(500),
        nullable=False
    )

    video_games = db.Column(
        db.String(500),
        nullable=False
    )

    park_attractions = db.Column(
        db.String(500),
        nullable=False
    )

    allies = db.Column(
        db.String(500),
        nullable=False
    )

    enemies = db.Column(
        db.String(500),
        nullable=False
    )

    nome_personagem = db.Column(
        db.String(500),
        nullable=False
    )

    url_imagem_personagem = db.Column(
        db.String(500),
        nullable=True
    )

    url_api_personagem = db.Column(
        db.String(500), 
        nullable=True
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
    