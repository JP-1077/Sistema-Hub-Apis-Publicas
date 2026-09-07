from flask import Blueprint, jsonify
from backend.services.service_db_espaco_naves_st import EspacoNavesService

espaco_naves_bp = Blueprint("espaco_naves", __name__, url_prefix="/api/starwars/espaco_naves")

@espaco_naves_bp.route("/", methods=["GET"])
def get_espaco_naves():
    service = EspacoNavesService()
    espaco_naves_st = service.coleta_dados_naves()
    return jsonify(espaco_naves_st)
