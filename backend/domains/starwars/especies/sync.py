from backend.database.db import db
from backend.domains.starwars.especies.consumer import ConsumerEspeciesApiStarwars
from backend.domains.starwars.especies.processor import ProcessorEspeciesApiStarWars
from backend.models.especies_api_starwars import EspeciesApiStarWars

class SyncDataBaseEspeciesStarWars:

    def __init__(self):
        self.api_consumer = ConsumerEspeciesApiStarwars()
        self.processor = ProcessorEspeciesApiStarWars()

    def armazenamento_especies_starwars_db(self):
        try:
            dados_especies = self.api_consumer.get_especies()
            especies_processadas = self.processor.processamento_dados_especies(dados_especies)

            for especie in especies_processadas:
                if especie.id is None:
                    continue

                especie_existente = db.session.query(EspeciesApiStarWars).filter_by(id=especie.id).first()

                if especie_existente is None:
                    db.session.add(especie)
                else:
                    especie_existente.nome = especie.nome
                    especie_existente.classificacao = especie.classificacao
                    especie_existente.designacao = especie.designacao
                    especie_existente.altura_media = especie.altura_media
                    especie_existente.cor_pele = especie.cor_pele
                    especie_existente.cor_cabelo = especie.cor_cabelo
                    especie_existente.cor_olhos = especie.cor_olhos
                    especie_existente.expectativa_vida_media = especie.expectativa_vida_media
                    especie_existente.idioma = especie.idioma
                    especie_existente.id_planeta_origem = especie.id_planeta_origem
                    especie_existente.data_atualizacao = especie.data_atualizacao

            db.session.commit()
            return len(especies_processadas)

        except Exception as e:
            db.session.rollback()
            raise e
