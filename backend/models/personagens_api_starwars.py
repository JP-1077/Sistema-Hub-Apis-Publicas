from datetime import datetime
from backend.database.db import db

class PersonagemApiStarWars (db.Model):
    __tablename__ = "tb_personagens_api_starwars"

    id = db.Column(
        db.Integer, 
        primary_key=True
    )

    external_id = db.Column(
        db.Integer, 
        nullable=False
    )

    nome_personagem = db.Column(
        db.String(500),
        nullable=False
    )

    altura = db.Column(
        db.String(500),
        nullable=False
    )

    peso = db.Column(
        db.String(500),
        nullable=False
    )

    cor_cabelo = db.Column(
        db.String(500),
        nullable=False
    )

    cor_pele = db.Column(
        db.String(500),
        nullable=False
    )

    cor_olhos = db.Column(
        db.String(500),
        nullable=False
    )

    ano_nascimento = db.Column(
        db.String(500),
        nullable=False
    )

    genero = db.Column(
        db.String(500),
        nullable=False
    )

    id_planeta_origem = db.Column(
        db.String(500),
        nullable=False
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