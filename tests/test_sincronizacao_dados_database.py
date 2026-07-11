import sys
from pathlib import Path
ROOT_DIR = Path(__file__).resolve().parent.parent
if str(ROOT_DIR) not in sys.path:
    sys.path.insert(0, str(ROOT_DIR))
import pytest
from backend.app import create_app
from backend.database.db import db
from backend.aplicacao_sincronizacao_dados import (
    sincronizacao_dados_personagens_db,
    sincronizacao_dados_localizacoes_db,
    sincronizacao_dados_episodios_db,

)
from backend.models import Personagem, Planeta, Filme


def test_personagens_salvos_db():
    app = create_app()

    with app.app_context():
        sincronizacao_dados_personagens_db()
        qtd_personagens_salvos = Personagem.query.count()
        assert qtd_personagens_salvos == 20



def test_localizacoes_salvos_db():
    app = create_app()

    with app.app_context():
        sincronizacao_dados_localizacoes_db()
        qtd_localizacoes_salvos = Planeta.query.count()
        assert qtd_localizacoes_salvos == 20


def test_episodios_salvos_db():
    app = create_app()

    with app.app_context():
        sincronizacao_dados_episodios_db()
        qtd_localizacoes_salvos = Filme.query.count()
        assert qtd_localizacoes_salvos == 20


