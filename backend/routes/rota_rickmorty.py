from flask import Blueprint, jsonify
import requests
from backend.models.personagem_rickmorty import Personagem


rickmorty_bp = Blueprint(
    "rickmorty", __name__,
    url_prefix="/api/rickmorty"
)

@rickmorty_bp.route("/Personagem", methods=["GET"])
def get_Personagem():
    personagens = Personagem.query.all()

    response = []

    for personagem in personagens:
        response.append({
            "id": personagem.id,
            "name": personagem.nome_personagem,
            "status": personagem.status,
            "especie": personagem.tipo_especie,
            "genero": personagem.genero,
            "imagem": personagem.url_imagem_personagem,
            "api": personagem.nome_api
        })

    return jsonify({"personagens": response})