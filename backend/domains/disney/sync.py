from backend.database.db import db
from backend.domains.disney.consumer import ConsumerPersonagensApiDisney
from backend.domains.disney.processor import ProcessorPersonagensApiDisney
from backend.models.personagens_api_disney import Personagemdisney

import json
class SyncDataBasePersonagensDisney:

    def __init__(self):
        self.api_consumer = ConsumerPersonagensApiDisney()
        self.processor = ProcessorPersonagensApiDisney()

    def armazenamento_personagens_disney_db(self):
        try:
            dados_personagens = self.api_consumer.get_personagens()

            personagens_processados = self.processor.processamento_dados_personagens(dados_personagens)

            for personagem in personagens_processados:
                if personagem.external_id is None:
                    continue

                personagem.filmes = json.dumps(personagem.filmes or [], ensure_ascii=False)

                personagem.filmes_shorts = json.dumps(personagem.filmes_shorts or [], ensure_ascii=False)

                personagem.tv_shows = json.dumps(personagem.tv_shows or [], ensure_ascii=False)

                personagem.video_games = json.dumps(personagem.video_games or [], ensure_ascii=False)

                personagem.park_attractions = json.dumps(personagem.park_attractions or [], ensure_ascii=False)

                personagem.allies = json.dumps(personagem.allies or [], ensure_ascii=False)

                personagem.enemies = json.dumps(personagem.enemies or [], ensure_ascii=False)

                personagem_existente = (db.session.query(Personagemdisney).filter_by(external_id=personagem.external_id).first())

                if personagem_existente is None:
                    db.session.add(personagem)
                else:
                    personagem_existente.filmes = personagem.filmes

                    personagem_existente.filmes_shorts = (personagem.filmes_shorts)

                    personagem_existente.tv_shows = personagem.tv_shows

                    personagem_existente.video_games = personagem.video_games

                    personagem_existente.park_attractions = (personagem.park_attractions)

                    personagem_existente.allies = personagem.allies

                    personagem_existente.enemies = personagem.enemies

                    personagem_existente.nome_personagem = (personagem.nome_personagem)

                    personagem_existente.url_imagem_personagem = (personagem.url_imagem_personagem)

                    personagem_existente.url_api_personagem = (personagem.url_api_personagem)

                    personagem_existente.nome_api = personagem.nome_api

                    personagem_existente.data_criacao_episodio = (personagem.data_criacao_episodio)

                    personagem_existente.data_atualizacao = (personagem.data_atualizacao)

            db.session.commit()
            return len(personagens_processados)
        
        except Exception as e:
            db.session.rollback()
            raise e

