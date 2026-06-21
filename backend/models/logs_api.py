from datetime import datetime
from backend.database.db import db

class logs (db.Model):
    __tablename__ = "tb_logs_apis"

    id = db.Column(
        db.Integer, 
        primary_key=True
    )

    tipo_api = db.Column(
        db.String(50),
        nullable=False
    )

    tipo_entidade = db.Column(
        db.String(50),
        nullable=False
    )

    registros_importados = db.Column(
        db.Integer,
        nullable=False
    )

    status = db.Column(
        db.String(50),
        nullable=False
    )

    data_ultima_sincronizacao = db.Column(
        db.DateTime,
        default=datetime.utcnow,
        onupdate=datetime.utcnow
    )