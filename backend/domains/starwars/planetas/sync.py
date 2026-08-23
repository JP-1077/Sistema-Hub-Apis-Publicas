from backend.database.db import db
from backend.domains.starwars.planetas.consumer import ConsumerPlanetasApiStarwars
from backend.domains.starwars.planetas.processor import ProcessorPlanetasApiStarWars
from backend.models.planetas_api_starwars import PlanetasApiStarWars

class SyncDataBasePlanetasStarWars:

    def __init__(self):
        self.api_consumer = ConsumerPlanetasApiStarwars()
        self.processor = ProcessorPlanetasApiStarWars()

    def armazenamento_planetas_starwars_db(self):
        try:
            dados_planetas = self.api_consumer.get_planetas()
            planetas_processados = self.processor.processamento_dados_planetas(dados_planetas)

            for planeta in planetas_processados:
                if planeta.external_id is None:
                    continue

                planeta_existente = db.session.query(PlanetasApiStarWars).filter_by(external_id=planeta.external_id).first()

                if planeta_existente is None:
                    db.session.add(planeta)
                else:
                    planeta_existente.nome_planeta = planeta.nome_planeta
                    planeta_existente.periodo_rotacao = planeta.periodo_rotacao
                    planeta_existente.periodo_orbital = planeta.periodo_orbital
                    planeta_existente.diametro = planeta.diametro
                    planeta_existente.clima = planeta.clima
                    planeta_existente.gravidade = planeta.gravidade
                    planeta_existente.terreno = planeta.terreno
                    planeta_existente.agua_superficie = planeta.agua_superficie
                    planeta_existente.populacao = planeta.populacao
                    planeta_existente.data_atualizacao = planeta.data_atualizacao

            db.session.commit()
            return len(planetas_processados)

        except Exception as e:
            db.session.rollback()
            raise e
