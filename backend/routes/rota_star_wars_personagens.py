from flask import Blueprint, jsonify
from backend.services.service_db_personagens_st import PersonagemServiceStarWars

personagens_bp = Blueprint("personagens", __name__, url_prefix="/api/starwars/personagens")

@personagens_bp.route("/", methods=["GET"])

def get_personagens():
    service = PersonagemServiceStarWars()
    personagens_st = service.coleta_dados_personagens_st()
    return jsonify(personagens_st)