from flask import Blueprint, jsonify
from backend.services.service_db_veiculos_st import VeiculosService

veiculos_bp = Blueprint("veiculos", __name__, url_prefix="/api/starwars/veiculos")

@veiculos_bp.route("/", methods=["GET"])
def get_veiculos():
    service = VeiculosService()
    veiculos_st = service.coleta_dados_veiculos()
    return jsonify(veiculos_st)
