from flask import Blueprint, jsonify
from backend.services.service_db_episodios import EpisodiosServices


episodios_bp = Blueprint (
    "episodios",

    __name__,

    url_prefix="/api/rickmorty/episodios"
)

@episodios_bp.route("/", methods = ["GET"])

def listagem_episodios():
    service = EpisodiosServices()
    resultado = service.coleta_dados_episodios()
    return jsonify(resultado)

