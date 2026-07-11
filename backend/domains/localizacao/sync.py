from backend.database.db import db
from backend.domains.localizacao.processor import ProcessamentoDadosLocalizacaoAPIRickMorty
from backend.domains.localizacao.consumer import ConsumerLocalizacaoAPIRickMorty


class SyncDatabaseLocalizacao:
    def __init__(self):
        self.api_consumer = ConsumerLocalizacaoAPIRickMorty()
        self.processamento_dados_localizacao = ProcessamentoDadosLocalizacaoAPIRickMorty()


    def salvar_localizacoes_database(self):

        try:
            dados_localizoes = self.api_consumer.get_localizacoes()
            localizacoes_processadas = self.processamento_dados_localizacao.processamento_dados_localizacao(dados_localizoes)

            for localizacao in localizacoes_processadas:
                localizacao_existente = db.session.get(
                    localizacao.__class__,
                    localizacao.external_id
                )

                if not localizacao_existente:
                    db.session.add(localizacao)

            db.session.commit()

            return len(localizacoes_processadas)
        
        except Exception as e:
            db.session.rollback()
            raise e
