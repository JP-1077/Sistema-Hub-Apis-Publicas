from datetime import datetime
from backend.database.db import db

class EspacoNavesApiStarWars(db.Model):
    __tablename__ = "tb_espaco_naves_api_starwars"

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    nome = db.Column(
        db.String(500),
        nullable=False
    )

    modelo = db.Column(
        db.String(500),
        nullable=False
    )

    fabricante = db.Column(
        db.String(500),
        nullable=False
    )

    custo_creditos = db.Column(
        db.String(500),
        nullable=False
    )

    comprimento = db.Column(
        db.String(500),
        nullable=False
    )

    velocidade_maxima_atmosfera = db.Column(
        db.String(500),
        nullable=False
    )

    tripulacao = db.Column(
        db.String(500),
        nullable=False
    )

    passageiros = db.Column(
        db.String(500),
        nullable=False
    )

    capacidade_carga = db.Column(
        db.String(500),
        nullable=False
    )

    consumiveis = db.Column(
        db.String(500),
        nullable=False
    )

    classificacao_hiperpropulsor = db.Column(
        db.String(500),
        nullable=False
    )

    mglt = db.Column(
        db.String(500),
        nullable=False
    )

    classe_nave = db.Column(
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
