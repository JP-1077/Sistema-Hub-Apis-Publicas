from datetime import datetime
from backend.models.planetas_api_starwars import PlanetasApiStarWars
from backend.domains.starwars.utils import extracao_id_url



class ProcessorPlanetasApiStarWars:

    def processamento_dados_planetas(self, dados):

        planetas_processados = []

        if not dados:
            return []

        if isinstance(dados, dict):
            resultados = dados.get("results", dados.get("data", []))
        else:
            resultados = dados

        for item in resultados:
            data_criacao_str = item.get("created")
            data_criacao = (
                datetime.fromisoformat(data_criacao_str.replace("Z", "+00:00"))
                if data_criacao_str
                else None
            )

            planeta = PlanetasApiStarWars(
                external_id = extracao_id_url(item.get("url")),
                nome_planeta=item.get("name"),
                periodo_rotacao=item.get("rotation_period"),
                periodo_orbital=item.get("orbital_period"),
                diametro=item.get("diameter"),
                clima=item.get("climate"),
                gravidade=item.get("gravity"),
                terreno=item.get("terrain"),
                agua_superficie=item.get("surface_water"),
                populacao=item.get("population"),
                data_criacao_planeta=data_criacao,
                data_atualizacao_planeta=data_criacao,
                nome_api="StarWars",
                data_criacao=data_criacao,
                data_atualizacao=datetime.utcnow(),
            )

            planetas_processados.append(planeta)

        return planetas_processados
