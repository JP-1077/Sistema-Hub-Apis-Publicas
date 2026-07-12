from flask import Blueprint, jsonify
from backend.services.service_db_personagem import PersonagemService


personagens_bp = Blueprint (
    "personagens",

    __name__,

    url_prefix="/api/rickmorty/personagens"
)

@personagens_bp.route("/", methods = ["GET"])


def listagem_personagens():
    service = PersonagemService()
    resultado = service.coleta_dados_personagem()
    return jsonify(resultado)