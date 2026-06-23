from backend.database.db import db
from backend.domains.episodios.processor import ProcessamentoDadosEpisodiosAPIRickMorty
from backend.domains.episodios.consumer import ConsumerEpisodiosAPIRickMorty


class SyncDatabase:
    def __init__(self):
        self.api_consumer = ConsumerEpisodiosAPIRickMorty
        self.processamento_dados_episodios = ProcessamentoDadosEpisodiosAPIRickMorty


    def salvar_episodios_datababase(self):

        try:
            dados_episodios = self.api_consumer.get_epsiodios()
            episodios_processados = self.processamento_dados_episodios.processamento_dados_episodioss(dados_episodios)

            for episodio in episodios_processados:
                episodio_existente = db.session.get(
                    episodio.__class__,
                    episodio.external_id
                )

                if not episodio_existente:
                    db.session.add(episodio)

            db.session.commit()

            return len(episodios_processados)
        
        except Exception as e:
            db.session.rollback()
            raise e
