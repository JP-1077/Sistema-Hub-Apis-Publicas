from backend.database.db import db
from backend.domains.personagem.processor import ProcessamentoDadosPersonsagemAPIRickMorty
from backend.services.api_consumer_rickmorty import consumer_api_rick_and_morty



class SyncDatabase:
    def __init__(self):
        self.api_consumer = consumer_api_rick_and_morty()
        self.processamento_dados = ProcessamentoDadosPersonsagemAPIRickMorty()

    def salvar_personagens_database(self):

        try:
            dados_personagens = self.api_consumer.get_personagens()
            personagens_processados = self.processamento_dados.processar_dados_personagens(dados_personagens)

            for personagem in personagens_processados:
                personagem_existente = db.session.get(
                    personagem.__class__,
                    personagem.external_id
                )

                if not personagem_existente:
                    db.session.add(personagem)

            db.session.commit()

            return len(personagens_processados)
    
        except Exception as e:
            db.session.rollback()
            raise e