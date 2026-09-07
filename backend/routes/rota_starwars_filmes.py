from flask import Blueprint, jsonify
from backend.services.service_db_filmes_st import FilmesService

filmes_bp = Blueprint("filmes", __name__, url_prefix="/api/starwars/filmes")

@filmes_bp.route("/", methods=["GET"])
def get_filmes():
    service = FilmesService()
    filmes_st = service.coleta_dados_filmes()
    return jsonify(filmes_st)