from datetime import datetime
from backend.database.db import db

class PlanetasApiStarWars (db.Model):
    __tablename__ = "tb_planetas_api_starwars"

    id = db.Column(
        db.Integer, 
        primary_key=True
    )

    external_id = db.Column(
        db.Integer, 
        nullable=False
    )

    nome_planeta = db.Column(
        db.String(500),
        nullable=False
    )

    periodo_rotacao = db.Column(
        db.String(500),
        nullable=False
    )

    periodo_orbital = db.Column(
        db.String(500),
        nullable=False
    )

    diametro = db.Column(
        db.String(500),
        nullable=False
    )

    clima = db.Column(
        db.String(500),
        nullable=False
    )

    gravidade = db.Column(
        db.String(500),
        nullable=False
    )

    terreno = db.Column(
        db.String(500),
        nullable=False
    )

    agua_superficie = db.Column(
        db.String(500),
        nullable=False
    )

    populacao = db.Column(
        db.String(500),
        nullable=False
    )

    data_criacao_planeta = db.Column(
        db.DateTime,
        nullable=False
    )

    data_atualizacao_planeta = db.Column(
        db.DateTime,
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