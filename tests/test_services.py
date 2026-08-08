import pytest
from backend.services.service_db_personagem import PersonagemService
from backend.models.personagem_rickmorty import Personagem
from backend.database.db import db

@pytest.fixture
def personagem_teste(app):
    p = Personagem(
        external_id=1,
        nome_personagem="Rick Sanchez",
        status="Alive",
        tipo_especie="Human",
        genero="Male",
        url_imagem_personagem="http://img",
        nome_api="rickmorty"
    )
    db.session.add(p)
    db.session.commit()
    return p

def test_coleta_dados_personagem_retorna_lista(personagem_teste):
    resultado = PersonagemService().coleta_dados_personagem()
    assert resultado == [{
        "id": personagem_teste.id,
        "name": "Rick Sanchez",
        "status": "Alive",
        "especie": "Human",
        "genero": "Male",
        "imagem": "http://img",
        "api": "rickmorty"
    }]