from backend.database.db import db
from backend.domains.starwars.filmes.consumer import ConsumerFilmesApiStarwars
from backend.domains.starwars.filmes.processor import ProcessorFilmesApiStarWars
from backend.models.filmes_api_starwars import Filmesstarwars

class SyncDataBaseFilmesStarWars:
    
    def __init__(self):
        self.api_consumer = ConsumerFilmesApiStarwars()
        self.processor = ProcessorFilmesApiStarWars()

    def armazenamento_filmes_starwars_db(self):
        try:
            dados_filmes = self.api_consumer.get_filmes()
            filmes_processados = self.processor.processamento_dados_personagem(dados_filmes)

            for filme in filmes_processados:
                if filme.external_id is None:
                    continue

                filme_existente = db.session.query(Filmesstarwars).filter_by(external_id=filme.external_id).first()

                if filme_existente is None:
                    db.session.add(filme)
                else:
                    filme_existente.titulo_filme = filme.titulo_filme
                    filme_existente.episodio = filme.episodio
                    filme_existente.texto_abertura = filme.texto_abertura
                    filme_existente.diretor = filme.diretor
                    filme_existente.produtor = filme.produtor
                    filme_existente.data_lancamento = filme.data_lancamento
                    filme_existente.url_personagens_filme = filme.url_personagens_filme
                    filme_existente.data_atualizacao = filme.data_atualizacao

            db.session.commit()
            return len(filmes_processados)
        
        except Exception as e:
            db.session.rollback()
            raise e
