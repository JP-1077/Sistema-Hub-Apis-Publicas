from datetime import datetime
from backend.database.db import db

class EspeciesApiStarWars(db.Model):
    __tablename__ = "tb_especies_api_starwars"

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    nome = db.Column(
        db.String(500),
        nullable=False
    )

    classificacao = db.Column(
        db.String(500),
        nullable=False
    )

    designacao = db.Column(
        db.String(500),
        nullable=False
    )

    altura_media = db.Column(
        db.String(500),
        nullable=False
    )

    cor_pele = db.Column(
        db.String(500),
        nullable=False
    )

    cor_cabelo = db.Column(
        db.String(500),
        nullable=False
    )

    cor_olhos = db.Column(
        db.String(500),
        nullable=False
    )

    expectativa_vida_media = db.Column(
        db.String(500),
        nullable=False
    )

    idioma = db.Column(
        db.String(500),
        nullable=False
    )

    id_planeta_origem = db.Column(
        db.String(500),
        nullable=False
    )

    nome_api = db.Column(
        db.String(500),
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
