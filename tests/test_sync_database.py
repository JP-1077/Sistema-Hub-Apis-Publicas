from backend.services.api_consumer_rickmorty import consumer_api_rick_and_morty
from backend.services.sync_database_rickmorty import SyncDatabase
from backend.app import criacao_banco_dados


def teste_salvar_personagens_database():
    app = criacao_banco_dados()

    with app.app_context():
        sync_database = SyncDatabase()

        qtd_personagens_salvos = sync_database.salvar_personagens_database()

        print(f"A quantidade de personagens salvos na tabela tb_personagem foi: {qtd_personagens_salvos}")

teste_salvar_personagens_database()