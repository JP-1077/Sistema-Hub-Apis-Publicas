from backend.database.db import db
from backend.domains.starwars.espaco_naves.consumer import ConsumerEspacoNavesApiStarwars
from backend.domains.starwars.espaco_naves.processor import ProcessorEspacoNavesApiStarWars
from backend.models.espaco_naves_api_starwars import EspacoNavesApiStarWars


class SyncDataBaseEspacoNavesStarWars:

    def __init__(self):
        self.api_consumer = ConsumerEspacoNavesApiStarwars()
        self.processor = ProcessorEspacoNavesApiStarWars()

    def armazenamento_espaco_espaco_naves_starwars_db(self):
        try:
            dados_espaco_espaco_naves = self.api_consumer.get_espaco_naves()
            espaco_espaco_naves_processadas = self.processor.processamento_dados_espaco_naves(dados_espaco_espaco_naves)

            for espaco_nave in espaco_espaco_naves_processadas:
                if espaco_nave.id is None:
                    continue

                espaco_nave_existente = db.session.query(EspacoNavesApiStarWars).filter_by(id=espaco_nave.id).first()

                if espaco_nave_existente is None:
                    db.session.add(espaco_nave)
                else:
                    espaco_nave_existente.nome = espaco_nave.nome
                    espaco_nave_existente.modelo = espaco_nave.modelo
                    espaco_nave_existente.fabricante = espaco_nave.fabricante
                    espaco_nave_existente.custo_creditos = espaco_nave.custo_creditos
                    espaco_nave_existente.comprimento = espaco_nave.comprimento
                    espaco_nave_existente.velocidade_maxima_atmosfera = espaco_nave.velocidade_maxima_atmosfera
                    espaco_nave_existente.tripulacao = espaco_nave.tripulacao
                    espaco_nave_existente.passageiros = espaco_nave.passageiros
                    espaco_nave_existente.capacidade_carga = espaco_nave.capacidade_carga
                    espaco_nave_existente.consumiveis = espaco_nave.consumiveis
                    espaco_nave_existente.classificacao_hiperpropulsor = espaco_nave.classificacao_hiperpropulsor
                    espaco_nave_existente.mglt = espaco_nave.mglt
                    espaco_nave_existente.classe_nave = espaco_nave.classe_nave
                    espaco_nave_existente.data_atualizacao = espaco_nave.data_atualizacao

            db.session.commit()
            return len(espaco_espaco_naves_processadas)

        except Exception as e:
            db.session.rollback()
            raise e
