from flask import Blueprint, jsonify
from backend.services.service_db_localizacoes import LocalizoesServices


localizacao_bp = Blueprint(
    "localizacao",

    __name__,

    url_prefix="/api/rickmorty/localizacao"
)


@localizacao_bp.route("/", methods = ["GET"])

def listagem_localizacoes():

    service = LocalizoesServices()

    resultado = service.coleta_dados_localizoes()
    
    return jsonify(resultado)