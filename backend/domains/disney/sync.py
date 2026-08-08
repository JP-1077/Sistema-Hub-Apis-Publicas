from backend.database.db import db
from backend.domains.disney.consumer import ConsumerPersonagensApiDisney
from backend.domains.disney.processor import ProcessorPersonagensApiDisney

class SyncDataBasePersonagensDisney:

    def __init__(self):
        self.api_consumer = ConsumerPersonagensApiDisney()
        self.processor = ProcessorPersonagensApiDisney()

    def armazenamento_personagens_disney_db(self):
        try:
            dados_personagens = self.api_consumer.get_personagens()
            personagens_processados = self.processor.processamento_dados_personagens(dados_personagens)

            for personagem in personagens_processados:
                personagem_existente = db.session.get(
                    personagem.__class__,
                    personagem.external_id
                )

            db.session.commit()
            return len(personagens_processados)
        
        except Exception as e:
            db.session.rollback()
            raise e

