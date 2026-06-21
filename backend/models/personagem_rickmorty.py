from datetime import datetime
from backend.database.db import db

class Personagem(db.Model):
    __tablename__ = "tb_personagens_rickmorty"

    __table_args__ = (
        db.UniqueConstraint(
            'external_id',
            'nome_api',
            name='uk_personagem_api'
        ),
    )

    id = db.Column(db.Integer, primary_key=True)

    external_id = db.Column(
        db.Integer, 
        nullable=False
    )

    nome_personagem = db.Column(
        db.String(255), 
        nullable=False
    )

    status = db.Column(
        db.String(255)
    )

    tipo_especie = db.Column(
        db.String(100)
    )

    genero = db.Column(
        db.String(50)
    )

    url_imagem_personagem = db.Column(
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
