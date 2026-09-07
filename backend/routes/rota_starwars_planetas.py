from flask import Blueprint, jsonify
from backend.services.service_db_planetas_st import PlanetasService

planetas_bp = Blueprint("planetas", __name__, url_prefix="/api/starwars/planetas")

@planetas_bp.route("/", methods=["GET"])
def get_planetas():
    service = PlanetasService()
    planetas_st = service.coleta_dados_planetas()
    return jsonify(planetas_st)
