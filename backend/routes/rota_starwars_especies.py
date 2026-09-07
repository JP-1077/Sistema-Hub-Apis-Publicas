from flask import Blueprint, jsonify
from backend.services.service_db_especies_st import EspeciesService

especies_bp = Blueprint("especies", __name__, url_prefix="/api/starwars/especies")

@especies_bp.route("/", methods=["GET"])
def get_especies():
    service = EspeciesService()
    especies_st = service.coleta_dados_especies()
    return jsonify(especies_st)
